"""Download a dated snapshot of the Treasury Department land appraisal prices.

Dataset: ราคาประเมินที่ดิน (official land appraisal prices), round 2023-2026,
publisher กรมธนารักษ์ (Treasury Department), DGA Open Government Licence.
Metadata from data.go.th (CKAN package `land-valuation`); files are served by
catalog.treasury.go.th resource download paths (allowed by its robots.txt).
Both sites ask for a 10-second crawl delay, which this script respects.

Raw files are immutable: an existing file with the expected size is skipped, and one with
another size stops the run rather than be overwritten. A package other than the default goes to its
own folder (snapshot_<date>_<package>), so two packages fetched on one day cannot overwrite each other. Usage: .venv/bin/python 04_analysis/src/download_treasury_appraisal.py [--package ID]
For R1 (PAP section 9): if the new round is published as a new CKAN package, pass its id with
--package; if one package lists two files with the same name (old and new rounds side by side), the
run stops rather than let one overwrite the other. rq1_round_change.py --post then refuses any
province file identical to the 2023-26 snapshot.
"""

import argparse
import csv
import datetime as dt
import hashlib
import json
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
PACKAGE_URL = "https://data.go.th/api/3/action/package_show?id={}"
CRAWL_DELAY_S = 10


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", default="land-valuation", help="CKAN package id on data.go.th")
    args = ap.parse_args()
    today = dt.date.today().isoformat()
    tag = "" if args.package == "land-valuation" else "_" + "".join(c if c.isalnum() or c in "-_" else "-" for c in args.package)
    out = ROOT / "03_data" / "raw" / "treasury_land_appraisal" / f"snapshot_{today}{tag}"
    out.mkdir(parents=True, exist_ok=True)

    pkg = requests.get(PACKAGE_URL.format(args.package), timeout=60).json()
    (out / "package_show.json").write_text(json.dumps(pkg, ensure_ascii=False, indent=1))
    resources = pkg["result"]["resources"]
    names = [r["url"].rsplit("/", 1)[-1] for r in resources]
    twice = sorted({n for n in names if names.count(n) > 1})
    if twice:
        raise SystemExit(f"package lists files with the same name more than once: {twice}; download them by hand "
                         "into separate folders and log it")
    time.sleep(CRAWL_DELAY_S)

    rows = []
    for i, r in enumerate(resources, 1):
        url, expected = r["url"], int(r.get("size") or 0)
        dest = out / url.rsplit("/", 1)[-1]
        if dest.exists() and dest.stat().st_size == expected:
            print(f"[{i}/{len(resources)}] skip {dest.name}")
        elif dest.exists():
            raise SystemExit(f"{dest} exists with {dest.stat().st_size} bytes, not the {expected} listed; raw files are "
                             "never overwritten: check it and move it aside by hand")
        else:
            print(f"[{i}/{len(resources)}] get  {dest.name} ({expected / 1e6:.1f} MB)")
            tmp = dest.with_suffix(".part")
            with requests.get(url, stream=True, timeout=300) as resp:
                resp.raise_for_status()
                with tmp.open("wb") as f:
                    for chunk in resp.iter_content(1 << 20):
                        f.write(chunk)
            tmp.rename(dest)
            time.sleep(CRAWL_DELAY_S)
        actual = dest.stat().st_size
        rows.append({
            "province_th": r.get("name"),
            "file": dest.name,
            "url": url,
            "expected_bytes": expected,
            "actual_bytes": actual,
            "size_match": actual == expected,
            "sha256": sha256(dest),
            "resource_last_modified": r.get("last_modified"),
            "snapshot_date": today,
        })

    with (out / "manifest.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    bad = [x["file"] for x in rows if not x["size_match"]]
    print(f"done: {len(rows)} files, {sum(x['actual_bytes'] for x in rows) / 1e9:.2f} GB, size mismatches: {bad or 'none'}")


if __name__ == "__main__":
    main()

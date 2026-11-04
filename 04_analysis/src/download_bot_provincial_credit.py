"""Download a dated snapshot of BOT commercial-bank deposits and loans by province.

Dataset: เงินรับฝากและเงินให้สินเชื่อของธนาคารพาณิชย์จำแนกตามจังหวัด
(commercial-bank deposits and loans by province), Bank of Thailand, monthly,
million baht. Listed on data.go.th as `ds-459` (licence: Creative Commons
Attributions). The data.go.th package has a single resource, a link to the BOT
web table, so the files come from the public BOT statistics server
(app.bot.or.th/BTWS_STAT), which needs no login and no API key.

How the BOT table works: each ReportPage shows ONE month (a cross-section of
provinces). The page is an ASP.NET form; the public "CSV" download button
(imbExportText) exports the month currently selected. So, per month, the script
(1) posts the form with the month selected (btnSubmit) and (2) posts the CSV
button with the returned form state. Responses are saved byte-for-byte.

Series and report IDs (checked 2026-11-02):
  FI_CB_011     reportID=172  1996-2005 (not fetched by default; see --series)
  FI_CB_011_S2  reportID=173  Jul 2005 - Dec 2011
  FI_CB_011_S3  not located on the BOT server or by web search (2012 gap)
  FI_CB_011_S4  reportID=781  Jan 2013 - Jun 2025
  FI_CB_011_S5  reportID=1008 Jul 2024 - Jul 2026 (successor of S4; Bangkok split into head
                office and other branches; S4 frozen at its 8 Aug 2025 update)

Politeness: app.bot.or.th/robots.txt returns 404 (no rules); data.go.th asks
for Crawl-Delay 10. The script waits >= 6 s between BOT requests and 10 s after
data.go.th. No email address or credentials are sent.

Raw files are immutable: an existing month file is skipped, never overwritten.
Usage:
  .venv/bin/python -I 04_analysis/src/download_bot_provincial_credit.py
  .venv/bin/python -I 04_analysis/src/download_bot_provincial_credit.py \
      --series FI_CB_011_S4 --start 2016-01 --end 2025-06
"""

import argparse
import csv
import datetime as dt
import hashlib
import html
import io
import json
import re
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT = "2026-11-02"  # folder name of the snapshot this script maintains
OUT = ROOT / "03_data" / "raw" / "bot_provincial_credit" / f"snapshot_{SNAPSHOT}"
UA = "Mozilla/5.0 (academic research; no-contact)"
DELAY_S = 6
CKAN_URL = "https://data.go.th/api/3/action/package_show?id=ds-459"
PAGE = "https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?reportID={rid}&language=th"

# series_id -> (reportID, default first month, default last month)
SERIES = {
    "FI_CB_011": (172, "1996-01", "2005-06"),
    "FI_CB_011_S2": (173, "2005-07", "2011-12"),
    "FI_CB_011_S4": (781, "2013-01", "2025-06"),
    "FI_CB_011_S5": (1008, "2024-07", "2026-07"),
}
DEFAULT = ["FI_CB_011_S2", "FI_CB_011_S4", "FI_CB_011_S5"]  # Jul 2005 - Jul 2026 (2012 missing)

TH_MONTH = ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.",
            "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def form_state(page_html: str) -> dict:
    """Hidden ASP.NET fields (__VIEWSTATE etc.) of the current page."""
    pairs = re.findall(r'<input type="hidden" name="([^"]+)" id="[^"]*" value="([^"]*)"', page_html)
    return {k: html.unescape(v) for k, v in pairs}


def months(start: str, end: str):
    y, m = map(int, start.split("-"))
    ye, me = map(int, end.split("-"))
    while (y, m) <= (ye, me):
        yield y, m
        m += 1
        if m == 13:
            y, m = y + 1, 1


def csv_period(content: bytes) -> str:
    """Return the period label (e.g. 'ธ.ค. 2554') found in the exported CSV.

    The header cell may carry a flag after the year, e.g. 'ม.ค. 2556 r'
    (r = revised); the flag is dropped here, the raw file keeps it.
    """
    text = content.decode("utf-8-sig", errors="replace")
    for row in list(csv.reader(io.StringIO(text)))[:10]:
        for cell in row:
            mt = re.fullmatch(r"\s*(\S+\.\S*\.?)\s*(25\d\d)\b.*", cell or "")
            if mt and not cell.lstrip().startswith(("FI_", "ปรับปรุง", "วันที่")):
                return f"{mt.group(1)} {mt.group(2)}"
    return ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--series", nargs="*", default=DEFAULT, choices=list(SERIES))
    ap.add_argument("--start", help="YYYY-MM (overrides series default)")
    ap.add_argument("--end", help="YYYY-MM (overrides series default)")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    s = requests.Session()
    s.headers["User-Agent"] = UA
    manifest = OUT / "manifest.csv"
    rows = list(csv.DictReader(manifest.open(encoding="utf-8"))) if manifest.exists() else []
    known = {r["file"] for r in rows}

    def log(url, dest, method):
        if dest.name in known:
            return
        rows.append({"url": url, "method": method, "file": dest.name,
                     "bytes": dest.stat().st_size, "sha256": sha256(dest),
                     "accessed": dt.date.today().isoformat()})
        known.add(dest.name)

    meta = OUT / "ds-459_package_show.json"
    if not meta.exists():
        meta.write_bytes(s.get(CKAN_URL, timeout=60).content)
        time.sleep(10)
    log(CKAN_URL, meta, "GET")

    for sid in args.series:
        rid, d0, d1 = SERIES[sid]
        url = PAGE.format(rid=rid)
        todo = [(y, m) for y, m in months(args.start or d0, args.end or d1)
                if not (OUT / f"{sid}_{y}-{m:02d}.csv").exists()]
        print(f"{sid}: {len(todo)} months to fetch")
        if not todo:
            continue
        r = s.get(url, timeout=120)
        r.raise_for_status()
        state = form_state(r.text)
        time.sleep(DELAY_S)
        for y, m in todo:
            dest = OUT / f"{sid}_{y}-{m:02d}.csv"
            sel = {"drpPeriod": "MTH", "drpFromYear": f"{y}xxxx", "drpFromMonth": f"xxxx{m:02d}xx"}
            if sid == "FI_CB_011_S5":  # S5 has a from-to range and shows its last month
                sel |= {"drpToYear": f"{y}xxxx", "drpToMonth": f"xxxx{m:02d}xx"}
            r = s.post(url, data={**state, **sel, "btnSubmit": "Submit"}, timeout=180)
            r.raise_for_status()
            state = form_state(r.text)
            time.sleep(DELAY_S)
            r = s.post(url, data={**state, **sel, "imbExportText.x": "10", "imbExportText.y": "10"},
                       timeout=180)
            r.raise_for_status()
            time.sleep(DELAY_S)
            if "csv" not in r.headers.get("content-type", "").lower():
                print(f"  {dest.name}: not a CSV ({r.headers.get('content-type')}); skipped")
                continue
            want = f"{TH_MONTH[m - 1]} {y + 543}"
            got = csv_period(r.content)
            if got != want:
                print(f"  {dest.name}: period mismatch (got {got!r}, want {want!r}); skipped")
                continue
            dest.write_bytes(r.content)
            log(url, dest, f"POST form: month {y}-{m:02d}, then CSV export button")
            print(f"  {dest.name} {len(r.content):,} B")
            # keep the manifest current in case the run is interrupted
            with manifest.open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=list(rows[0]))
                w.writeheader()
                w.writerows(rows)

    with manifest.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["url", "method", "file", "bytes", "sha256", "accessed"])
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: r["file"]))
    print(f"done: {len(rows)} files in manifest")


if __name__ == "__main__":
    main()

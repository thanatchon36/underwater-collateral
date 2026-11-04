"""Download ESA WorldCover 10 m (2021, v200) tiles covering the core Chao Phraya basin pilot.

Source: ESA WorldCover 2021 v200, public AWS bucket (Registry of Open Data), CC BY 4.0.
Citation: Zanaga et al. (2022), ESA WorldCover 10 m 2021 v200, doi 10.5281/zenodo.7254221.
Tiles are 3 x 3 degrees; the pilot sheets span 12.8-17.4 N, 99.2-101.8 E -> N12E099, N15E099.
Writes 03_data/raw/landcover/worldcover_2021/<tile>.tif and manifest.csv (bytes, SHA-256).

Run: .venv/bin/python -I 04_analysis/src/download_worldcover.py
"""

import csv
import hashlib
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "03_data/raw/landcover/worldcover_2021"
BASE = "https://esa-worldcover.s3.eu-central-1.amazonaws.com/v200/2021/map/"
TILES = ["N12E099", "N15E099"]
UA = {"User-Agent": "underwater-collateral-datafetch/0.1"}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for t in TILES:
        name = f"ESA_WorldCover_10m_2021_v200_{t}_Map.tif"
        dst = OUT / name
        if not dst.exists():
            with requests.get(BASE + name, headers=UA, stream=True, timeout=120) as r:
                r.raise_for_status()
                with open(dst, "wb") as f:
                    for chunk in r.iter_content(1 << 20):
                        f.write(chunk)
            time.sleep(2)
        h = hashlib.sha256(dst.read_bytes()).hexdigest()
        rows.append({"file": name, "url": BASE + name, "bytes": dst.stat().st_size, "sha256": h,
                     "accessed": "2026-11-02"})
    with open(OUT / "manifest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(r["file"], r["bytes"])


if __name__ == "__main__":
    main()

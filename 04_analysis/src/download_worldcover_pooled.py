"""Download ESA WorldCover 10 m (2021, v200) tiles for the pooled 2024 RQ1 sample outside the north.

Source: ESA WorldCover 2021 v200, public AWS bucket (Registry of Open Data), CC BY 4.0.
Citation: Zanaga et al. (2022), ESA WorldCover 10 m 2021 v200, doi 10.5281/zenodo.7254221.
Nong Khai sheets span 17.6-18.4 N, 102.1-103.5 E and Nakhon Phanom 16.8-18.1 N, 103.9-105.0 E,
so tiles N15E102 and N18E102 (3 x 3 degrees) cover both. Chiang Rai and Phayao use N18E099
(download_north_covariates.py).
The 2025-flood sample (second event, PAP section 10) adds N06E099 and N09E099 for Songkhla, Pattani,
Phatthalung and Nakhon Si Thammarat; its central provinces use N15E099 (download_worldcover.py).
Writes 03_data/raw/landcover/worldcover_2021_pooled/<tile>.tif and manifest.csv (bytes, SHA-256).

Run: .venv/bin/python -I 04_analysis/src/download_worldcover_pooled.py
"""

import csv
import hashlib
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "03_data/raw/landcover/worldcover_2021_pooled"
BASE = "https://esa-worldcover.s3.eu-central-1.amazonaws.com/v200/2021/map/"
TILES = ["N15E102", "N18E102", "N06E099", "N09E099"]
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

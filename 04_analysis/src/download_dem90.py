"""Download Copernicus DEM GLO-90 tiles covering every located cadastral sheet (pooled RQ1 sample).

Copernicus DEM GLO-90 Public (2021 release), 1 x 1 degree COG tiles, public AWS bucket
copernicus-dem-90m (free licence, Copernicus DEM terms; ESA 2022, doi:10.5270/ESA-c5d3d65).
Only tiles listed in the bucket's tileList.txt that contain a sheet are fetched.
Writes 03_data/raw/elevation/copernicus_glo90/*.tif and manifest.csv (bytes, SHA-256, access date).

Run: .venv/bin/python -I 04_analysis/src/download_dem90.py
"""

import csv
import hashlib
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[2]
PANEL = ROOT / "03_data/processed/sheet_panel.csv.gz"
OUT = ROOT / "03_data/raw/elevation/copernicus_glo90"
BASE = "https://copernicus-dem-90m.s3.amazonaws.com/"
UA = {"User-Agent": "underwater-collateral-datafetch/0.1"}
ACCESSED = "2026-11-02"


def tile(lat, lon):
    return f"Copernicus_DSM_COG_30_N{lat:02d}_00_E{lon:03d}_00_DEM"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    d = pd.read_csv(PANEL, usecols=["lon0", "lat0", "lon1", "lat1"]).dropna()
    need = set()
    for c in [("lat0", "lon0"), ("lat0", "lon1"), ("lat1", "lon0"), ("lat1", "lon1")]:
        need |= set(zip(np.floor(d[c[0]]).astype(int), np.floor(d[c[1]]).astype(int)))
    listed = set(requests.get(BASE + "tileList.txt", headers=UA, timeout=60).text.split())
    rows = []
    for la, lo in sorted(need):
        t = tile(la, lo)
        if t not in listed:
            continue
        dst = OUT / f"{t}.tif"
        url = f"{BASE}{t}/{t}.tif"
        if not dst.exists():
            r = requests.get(url, headers=UA, timeout=180)
            r.raise_for_status()
            dst.write_bytes(r.content)
            time.sleep(1)
        rows.append({"file": dst.name, "url": url, "bytes": dst.stat().st_size,
                     "sha256": hashlib.sha256(dst.read_bytes()).hexdigest(), "accessed": ACCESSED})
    with open(OUT / "manifest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "tiles", sum(r["bytes"] for r in rows), "bytes")


if __name__ == "__main__":
    main()

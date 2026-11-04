"""Download JRC Global Surface Water v1.4 occurrence tiles for 0-10 N (southern 2025-flood provinces).

Source: European Commission JRC / Google, Global Surface Water v1.4 (1984-2021), public bucket
(no login); Pekel et al. (2016), Nature, doi:10.1038/nature20584. Tiles 90E_10N and 100E_10N cover
90-110 E, 0-10 N (Songkhla, Pattani, Phatthalung and southern Nakhon Si Thammarat); 10-30 N tiles are
already on disk (build_sheet_panel.py, download_north_covariates.py).
Writes 03_data/raw/flood/jrc_gsw_v1_4_occurrence_10N/<tile>.tif and manifest.csv (bytes, SHA-256).

Run: .venv/bin/python -I 04_analysis/src/download_gsw_south.py
"""

import csv
import hashlib
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "03_data/raw/flood/jrc_gsw_v1_4_occurrence_10N"
BASE = "https://storage.googleapis.com/global-surface-water/downloads2021/occurrence/"
TILES = ["occurrence_90E_10Nv1_4_2021.tif", "occurrence_100E_10Nv1_4_2021.tif"]
UA = {"User-Agent": "underwater-collateral-datafetch/0.1"}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for name in TILES:
        dst = OUT / name
        if not dst.exists():
            with requests.get(BASE + name, headers=UA, stream=True, timeout=120) as r:
                r.raise_for_status()
                with open(dst, "wb") as f:
                    for chunk in r.iter_content(1 << 20):
                        f.write(chunk)
            time.sleep(2)
        rows.append({"file": name, "url": BASE + name, "bytes": dst.stat().st_size,
                     "sha256": hashlib.sha256(dst.read_bytes()).hexdigest(), "accessed": "2026-11-02"})
    with open(OUT / "manifest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(r["file"], r["bytes"])


if __name__ == "__main__":
    main()

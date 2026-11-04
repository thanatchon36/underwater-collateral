"""Download public covariate tiles for the RQ1 2024 design (Chiang Rai and Phayao).

Sheets in the 2024 sample span about 18.8-20.5 N, 99.3-100.7 E. Tiles:
- ESA WorldCover 10 m 2021 v200, tile N18E099 (3 x 3 degrees; CC BY 4.0; Zanaga et al. 2022),
  public AWS bucket esa-worldcover.
- JRC Global Surface Water v1.4 occurrence, tiles 90E_30N and 100E_30N (10 x 10 degrees, 20-30 N;
  the 20 N tiles already in raw/flood/jrc_gsw_v1_4_occurrence cover 10-20 N). Pekel et al. (2016).
- Copernicus DEM GLO-30 Public (2021 release), 1 x 1 degree tiles N18-N20 x E099-E100, public AWS
  bucket copernicus-dem-30m (free licence, Copernicus DEM terms). A surface model: includes
  buildings and vegetation, used for sheet-level elevation only.
Writes into 03_data/raw/{landcover/worldcover_2021_north, flood/jrc_gsw_v1_4_occurrence_30N,
elevation/copernicus_glo30} with manifest.csv (bytes, SHA-256, access date) in each.

Run: .venv/bin/python -I 04_analysis/src/download_north_covariates.py
"""

import csv
import hashlib
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
UA = {"User-Agent": "underwater-collateral-datafetch/0.1"}
ACCESSED = "2026-11-02"
WC = "https://esa-worldcover.s3.eu-central-1.amazonaws.com/v200/2021/map/"
GSW = "https://storage.googleapis.com/global-surface-water/downloads2021/occurrence/"
DEM = "https://copernicus-dem-30m.s3.amazonaws.com/"
DEM_TILES = [f"Copernicus_DSM_COG_10_N{la:02d}_00_E{lo:03d}_00_DEM" for la in (18, 19, 20) for lo in (99, 100)]
JOBS = {
    "03_data/raw/landcover/worldcover_2021_north": [WC + "ESA_WorldCover_10m_2021_v200_N18E099_Map.tif"],
    "03_data/raw/flood/jrc_gsw_v1_4_occurrence_30N": [GSW + f"occurrence_{t}v1_4_2021.tif" for t in ("90E_30N", "100E_30N")],
    "03_data/raw/elevation/copernicus_glo30": [DEM + f"{t}/{t}.tif" for t in DEM_TILES],
}


def main() -> None:
    for sub, urls in JOBS.items():
        out = ROOT / sub
        out.mkdir(parents=True, exist_ok=True)
        rows = []
        for url in urls:
            dst = out / url.rsplit("/", 1)[1]
            if not dst.exists():
                with requests.get(url, headers=UA, stream=True, timeout=180) as r:
                    r.raise_for_status()
                    with open(dst, "wb") as f:
                        for chunk in r.iter_content(1 << 20):
                            f.write(chunk)
                time.sleep(2)
            rows.append({"file": dst.name, "url": url, "bytes": dst.stat().st_size,
                         "sha256": hashlib.sha256(dst.read_bytes()).hexdigest(), "accessed": ACCESSED})
            print(dst.name, rows[-1]["bytes"], flush=True)
        with open(out / "manifest.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)


if __name__ == "__main__":
    main()

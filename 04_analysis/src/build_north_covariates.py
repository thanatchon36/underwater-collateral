"""Ex-ante covariates for the RQ1 2024 design (Chiang Rai and Phayao sheets).

Input:  03_data/processed/sheet_flood2024_north.csv.gz (exposure_2024_north.py)
        03_data/raw/landcover/worldcover_2021_north/*.tif   (download_north_covariates.py)
        03_data/raw/flood/jrc_gsw_v1_4_occurrence{,_30N}/*.tif
        03_data/raw/elevation/copernicus_glo30/*.tif
Output: 03_data/processed/sheet_north_covariates.csv.gz, per sheet in the UNOSAT analysis extent:
  - lc_builtup, lc_cropland, lc_tree, lc_water: WorldCover 2021 shares of the sheet's pixels;
  - elev_m: mean Copernicus GLO-30 surface elevation over the sheet (a surface model: includes
    buildings and canopy);
  - river_km: distance from the sheet centre to the nearest "river" cell, defined as a 90 m cell
    (3 x 3 block of 30 m GSW pixels) in which any pixel held water in at least 50% of valid
    observations, 1984-2021 (JRC GSW occurrence >= 50);
  - rel_elev_m: elev_m minus the 5th percentile of elev_m over the sheets of the same 1:50,000
    sheet (height above the local valley floor; an ex-ante hazard proxy).
  "river" cells include ponds and reservoirs, so river_km is distance to permanent surface water.
All are measured before or independently of the 2024 floods except land cover (2021) and the
GSW record (to 2021), which predate them.

Run: .venv/bin/python -I 04_analysis/src/build_north_covariates.py
"""

from pathlib import Path

import numpy as np
import pandas as pd
import rasterio
from rasterio.merge import merge
from rasterio.windows import from_bounds
from scipy.spatial import cKDTree

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "03_data/processed/sheet_flood2024_north.csv.gz"
OUT = ROOT / "03_data/processed/sheet_north_covariates.csv.gz"
WC = sorted((ROOT / "03_data/raw/landcover/worldcover_2021_north").glob("*.tif"))
GSW = sorted((ROOT / "03_data/raw/flood/jrc_gsw_v1_4_occurrence").glob("*.tif")) + sorted(
    (ROOT / "03_data/raw/flood/jrc_gsw_v1_4_occurrence_30N").glob("*.tif"))
DEM = sorted((ROOT / "03_data/raw/elevation/copernicus_glo30").glob("*.tif"))
LC = {"builtup": [50], "cropland": [40], "tree": [10], "water": [80]}
MARGIN, BLOCK, RIVER_OCC = 0.15, 3, 50
KX, KY = 111.32 * np.cos(np.radians(19.6)), 110.57  # km per degree at the sample's latitude


def mosaic(paths, bounds):
    srcs = [rasterio.open(p) for p in paths]
    arr, tr = merge(srcs, bounds=bounds)
    for s in srcs:
        s.close()
    return arr[0], tr


def main() -> None:
    d = pd.read_csv(SRC)
    d = d[d["in_analysis_extent"]].reset_index(drop=True)
    bb = (d["lon0"].min() - MARGIN, d["lat0"].min() - MARGIN, d["lon1"].max() + MARGIN, d["lat1"].max() + MARGIN)

    # land cover
    with rasterio.open(WC[0]) as s:
        cnt = np.zeros((len(d), 256), dtype=np.int64)
        for i, (x0, y0, x1, y1) in enumerate(d[["lon0", "lat0", "lon1", "lat1"]].itertuples(index=False)):
            w = from_bounds(x0, y0, x1, y1, s.transform).round_offsets().round_lengths()
            cnt[i] = np.bincount(s.read(1, window=w).ravel(), minlength=256)[:256]
    n = cnt[:, 1:].sum(axis=1)
    for k, codes in LC.items():
        d[f"lc_{k}"] = cnt[:, codes].sum(axis=1) / np.where(n > 0, n, np.nan)

    # elevation: sheet means
    dem, dtr = mosaic(DEM, bb)
    dem = dem.astype("float64")
    inv = ~dtr
    el = []
    for x0, y0, x1, y1 in d[["lon0", "lat0", "lon1", "lat1"]].itertuples(index=False):
        c0, r0 = inv * (x0, y1)
        c1, r1 = inv * (x1, y0)
        el.append(dem[int(r0):max(int(r1), int(r0) + 1), int(c0):max(int(c1), int(c0) + 1)].mean())
    d["elev_m"] = el

    # rivers from GSW occurrence (>= 50% of observations), 90 m cells
    occ, gtr = mosaic(GSW, bb)
    occ = np.where(occ == 255, 0, occ)
    h, w = (occ.shape[0] // BLOCK) * BLOCK, (occ.shape[1] // BLOCK) * BLOCK
    river = (occ[:h, :w] >= RIVER_OCC).reshape(h // BLOCK, BLOCK, w // BLOCK, BLOCK).any(axis=(1, 3))
    rr, cc = np.nonzero(river)
    lon = gtr.c + (cc + 0.5) * BLOCK * gtr.a
    lat = gtr.f + (rr + 0.5) * BLOCK * gtr.e
    tree = cKDTree(np.c_[lon * KX, lat * KY])
    cx, cy = (d["lon0"] + d["lon1"]) / 2, (d["lat0"] + d["lat1"]) / 2
    d["river_km"] = tree.query(np.c_[cx * KX, cy * KY])[0]
    d["rel_elev_m"] = d["elev_m"] - d.groupby("series_sheet")["elev_m"].transform(lambda s: s.quantile(0.05))

    keep = ["province", "UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "scale", "series_sheet",
            "lc_builtup", "lc_cropland", "lc_tree", "lc_water", "elev_m", "rel_elev_m", "river_km"]
    d[keep].to_csv(OUT, index=False, compression="gzip")
    print(len(d), "sheets;", int(river.sum()), "river cells")
    print(d[keep[7:]].describe().round(3).to_string())


if __name__ == "__main__":
    main()

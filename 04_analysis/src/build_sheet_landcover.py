"""Land-cover shares per cadastral sheet for the RQ1 pilot (core Chao Phraya basin).

Input:  03_data/processed/sheet_panel.csv.gz (sheet WGS84 bounding boxes)
        03_data/raw/landcover/worldcover_2021/*.tif (download_worldcover.py)
Output: 03_data/processed/sheet_landcover_basin.csv.gz with, per sheet, the share of
        10 m WorldCover 2021 pixels in each class: tree (10), cropland (40), built-up (50),
        water (80), wetland (90), other (all remaining classes); and the pixel count.
Note: WorldCover is 2021, ten years after the 2011 flood, so land cover may itself respond
to flooding; it is used descriptively and as a control in robustness checks only.

Run: .venv/bin/python -I 04_analysis/src/build_sheet_landcover.py
"""

from pathlib import Path

import numpy as np
import pandas as pd
import rasterio
from rasterio.windows import from_bounds

ROOT = Path(__file__).resolve().parents[2]
PANEL = ROOT / "03_data/processed/sheet_panel.csv.gz"
WC = sorted((ROOT / "03_data/raw/landcover/worldcover_2021").glob("*.tif"))
OUT = ROOT / "03_data/processed/sheet_landcover_basin.csv.gz"
BASIN = ["bangkok", "nonthaburi", "pathum-thani", "phra-nakhon-si-ayutthaya", "ang-thong",
         "sing-buri", "chai-nat", "lop-buri", "nakhon-sawan", "suphan-buri", "uthai-thani",
         "phichit", "saraburi", "nakhon-pathom", "samut-prakan", "phitsanulok", "kamphaeng-phet"]
CLASSES = {"tree": [10], "cropland": [40], "builtup": [50], "water": [80], "wetland": [90]}


def main() -> None:
    d = pd.read_csv(PANEL, dtype={"UTMMAP1": str, "UTMMAP3": str, "UTMMAP4": str, "prov_code": str},
                    keep_default_na=False, na_values=[""])
    d = d[d["province"].isin(BASIN) & d["gfd_flood_share"].notna() & d["scale"].isin([1000, 4000])]
    srcs = [rasterio.open(p) for p in WC]
    counts = np.zeros((len(d), 256), dtype=np.int64)
    for i, (x0, y0, x1, y1) in enumerate(d[["lon0", "lat0", "lon1", "lat1"]].itertuples(index=False)):
        for s in srcs:
            b = s.bounds
            if x1 <= b.left or x0 >= b.right or y1 <= b.bottom or y0 >= b.top:
                continue
            w = from_bounds(max(x0, b.left), max(y0, b.bottom), min(x1, b.right), min(y1, b.top), s.transform)
            a = s.read(1, window=w.round_offsets().round_lengths(), boundless=False)
            counts[i] += np.bincount(a.ravel(), minlength=256)[:256]
    n = counts[:, 1:].sum(axis=1)  # class 0 = no data
    out = d[["province", "UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "UTMSCALE", "scale", "series_sheet"]].copy()
    out["wc_px"] = n
    for k, codes in CLASSES.items():
        out[f"lc_{k}"] = counts[:, codes].sum(axis=1) / np.where(n > 0, n, np.nan)
    out["lc_other"] = 1 - out[[f"lc_{k}" for k in CLASSES]].sum(axis=1)
    out.to_csv(OUT, index=False)
    print(len(out), "sheets;", int((n == 0).sum()), "without WorldCover pixels")
    print(out.groupby("scale")[[c for c in out if c.startswith("lc_")]].mean().round(3))


if __name__ == "__main__":
    main()

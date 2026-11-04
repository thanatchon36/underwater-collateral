"""Build the sheet-level RQ1 dataset: Treasury appraisal values x flood exposure.

One row per cadastral sheet reference (UTMMAP1-4, UTMSCALE) and province file.
- Appraisals (2023-26 round, snapshot 2026-11-02): parcel count, mean/median/p90/max
  log EVAPRICE (baht per square wah), number of distinct prices. Values are set per land
  unit x depth x shape factors (04_analysis/treasury_method_notes.md), so the sheet p90/max
  approximates the best road-front unit price and is the main RQ1 outcome.
- Location: mapsheet.sheet_bounds (Indian 1975 UTM) -> WGS84 bounding box.
- 2011 exposure: Global Flood Database DFO 3850 (~250 m), land pixels only
  (jrc_perm_water == 0): flooded share, mean duration (days), mean clear_perc.
- Long-run hazard: JRC GSW v1.4 occurrence (30 m, block-averaged to 120 m),
  mean occurrence (0-100) over valid pixels; tiles cover 90-110E, 10-20N only.

Sheet means use pixel-centre membership of the WGS84 bounding box, with at least one
pixel per sheet; small sheets (500 m, 250 m) are therefore noisy on the 250 m GFD grid.

Output: 03_data/processed/sheet_panel.csv.gz
Run:    .venv/bin/python -I 04_analysis/src/build_sheet_panel.py
"""

import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import rasterio
from rasterio.windows import from_bounds

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mapsheet as m  # noqa: E402

ROOT = HERE.parents[1]
SNAP = ROOT / "03_data/raw/treasury_land_appraisal/snapshot_2026-11-02"
GFD = ("zip://" + str(ROOT / "03_data/raw/flood/gfd_dfo3850/DFO_3850_From_20110805_to_20120109.zip")
       + "!DFO_3850_From_20110805_to_20120109.tif")
GSW_DIR = ROOT / "03_data/raw/flood/jrc_gsw_v1_4_occurrence"
OUT = ROOT / "03_data/processed/sheet_panel.csv.gz"
REF = ["UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "UTMSCALE"]
GSW_BLOCK = 4  # 30 m -> 120 m


def appraisals() -> pd.DataFrame:
    parts = []
    for f in sorted(SNAP.glob("land_*.csv")):
        code, prov = re.match(r"land_(\d+)_(.+)\.csv", f.name).groups()
        df = pd.read_csv(f, dtype=str, usecols=REF + ["EVAPRICE"])
        df["p"] = pd.to_numeric(df["EVAPRICE"], errors="coerce")
        df = df[df["p"] > 0]
        df["lp"] = np.log(df["p"])
        g = df.groupby(REF).agg(n_parcels=("p", "size"), mean_logp=("lp", "mean"),
                                median_p=("p", "median"), sd_logp=("lp", "std"),
                                p90_logp=("lp", lambda s: s.quantile(0.9)), max_logp=("lp", "max"),
                                n_distinct_p=("p", "nunique")).reset_index()
        g.insert(0, "province", prov)
        g.insert(0, "prov_code", code)
        parts.append(g)
        print(f"appraisals {f.name}: {len(df):,} parcels, {len(g):,} sheets", flush=True)
    return pd.concat(parts, ignore_index=True)


def locate(df: pd.DataFrame) -> pd.DataFrame:
    """Add zone, scale and the WGS84 bounding box of each decodable sheet."""
    out = []
    for ref in df[REF].itertuples(index=False):
        try:
            zone, x0, y0, x1, y1 = m.sheet_bounds(*ref)
        except ValueError:
            out.append((np.nan,) * 5)
            continue
        corners = [m.to_wgs84_lonlat(x, y, zone) for x in (x0, x1) for y in (y0, y1)]
        lons, lats = zip(*corners)
        out.append((zone, min(lons), min(lats), max(lons), max(lats)))
    loc = pd.DataFrame(out, columns=["zone", "lon0", "lat0", "lon1", "lat1"], index=df.index)
    return df.join(loc)


def integral(a: np.ndarray) -> np.ndarray:
    s = np.zeros((a.shape[0] + 1, a.shape[1] + 1), dtype=np.float64)
    np.cumsum(np.cumsum(a, axis=0, dtype=np.float64), axis=1, out=s[1:, 1:])
    return s


def box_sums(sats, left, top, res, shape, lon0, lat0, lon1, lat1):
    """Sum each integral image over pixel-centre boxes; returns list of arrays and pixel counts."""
    c0 = np.clip(np.round((lon0 - left) / res), 0, shape[1]).astype(int)
    c1 = np.clip(np.round((lon1 - left) / res), 0, shape[1]).astype(int)
    r0 = np.clip(np.round((top - lat1) / res), 0, shape[0]).astype(int)
    r1 = np.clip(np.round((top - lat0) / res), 0, shape[0]).astype(int)
    c1 = np.maximum(c1, np.minimum(c0 + 1, shape[1]))
    r1 = np.maximum(r1, np.minimum(r0 + 1, shape[0]))
    return [s[r1, c1] - s[r0, c1] - s[r1, c0] + s[r0, c0] for s in sats]


def gfd_exposure(df: pd.DataFrame) -> pd.DataFrame:
    with rasterio.open(GFD) as r:
        flooded, duration, _, clear_perc, perm = (r.read(i + 1) for i in range(5))
        left, top, res, shape = r.bounds.left, r.bounds.top, r.res[0], r.shape
    land = (perm == 0) & np.isfinite(flooded)
    sats = [integral(land), integral(np.where(land, flooded, 0)),
            integral(np.where(land, duration, 0)), integral(np.where(land, clear_perc, 0))]
    ok = df["lon0"].notna()
    n_land, s_fl, s_du, s_cl = box_sums(sats, left, top, res, shape,
                                        *(df.loc[ok, k].to_numpy() for k in ["lon0", "lat0", "lon1", "lat1"]))
    with np.errstate(invalid="ignore", divide="ignore"):
        df.loc[ok, "gfd_land_px"] = n_land
        df.loc[ok, "gfd_flood_share"] = s_fl / n_land
        df.loc[ok, "gfd_duration_mean"] = s_du / n_land
        df.loc[ok, "gfd_clear_perc_mean"] = s_cl / n_land
    return df


def gsw_exposure(df: pd.DataFrame) -> pd.DataFrame:
    df["gsw_valid_px"] = np.nan
    df["gsw_occurrence_mean"] = np.nan
    for tif in sorted(GSW_DIR.glob("occurrence_*.tif")):
        with rasterio.open(tif) as r:
            lo = max(r.bounds.left, 97.0)
            win = from_bounds(lo, r.bounds.bottom, min(r.bounds.right, 106.0), r.bounds.top, r.transform)
            win = win.round_offsets().round_lengths()
            a = r.read(1, window=win)
            wt = r.window_transform(win)
            left, top, res = wt.c, wt.f, r.res[0] * GSW_BLOCK
        h, w = (a.shape[0] // GSW_BLOCK) * GSW_BLOCK, (a.shape[1] // GSW_BLOCK) * GSW_BLOCK
        a = a[:h, :w]
        valid = a <= 100
        cnt = valid.reshape(h // GSW_BLOCK, GSW_BLOCK, w // GSW_BLOCK, GSW_BLOCK).sum(axis=(1, 3))
        tot = np.where(valid, a, 0).astype(np.uint16).reshape(
            h // GSW_BLOCK, GSW_BLOCK, w // GSW_BLOCK, GSW_BLOCK).sum(axis=(1, 3), dtype=np.uint32)
        del a, valid
        sats = [integral(cnt), integral(tot)]
        right, bottom = left + cnt.shape[1] * res, top - cnt.shape[0] * res
        cx, cy = (df["lon0"] + df["lon1"]) / 2, (df["lat0"] + df["lat1"]) / 2
        inside = df["lon0"].notna() & cx.between(left, right) & cy.between(bottom, top)
        n, s = box_sums(sats, left, top, res, cnt.shape,
                        *(df.loc[inside, k].to_numpy() for k in ["lon0", "lat0", "lon1", "lat1"]))
        with np.errstate(invalid="ignore", divide="ignore"):
            df.loc[inside, "gsw_valid_px"] = n * GSW_BLOCK ** 2
            df.loc[inside, "gsw_occurrence_mean"] = s / n
        print(f"gsw {tif.name}: {int(inside.sum()):,} sheets", flush=True)
        del sats, cnt, tot
    return df


def main() -> None:
    df = appraisals()
    df = locate(df)
    print(f"located {df['lon0'].notna().sum():,} of {len(df):,} sheet refs", flush=True)
    df = gfd_exposure(df)
    df = gsw_exposure(df)
    df["scale"] = pd.to_numeric(df["UTMSCALE"], errors="coerce").astype("Int64")
    df["series_sheet"] = df["UTMMAP1"].astype(str) + "-" + df["UTMMAP2"].astype(str)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False, compression="gzip")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(df):,} rows", flush=True)


if __name__ == "__main__":
    main()

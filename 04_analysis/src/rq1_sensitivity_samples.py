"""Sample files for the RQ1 sensitivities that change which sheets enter (PAP sections 3-4).

Each variant applies the rules of rq1_2024_pooled.py with one setting changed, and writes a sample
file in the same layout, which rq1_round_change.py --sensitivities analyses with the registered
code. The "primary" variant must reproduce rq1_2024_sample_sheets.csv.gz exactly (checked here).

Variants (primary settings: threshold 25%, at least 25 treated sheets per province, 5 km buffer,
height cap at the treated 90th percentile, controls dry in every source):
- thr10, thr50: treated if the 2024 radar share > 10% (50%) and the 2025 share <= 10% (50%);
                provinces held at the primary four, so only the flood rule changes
- prov20, prov30: provinces with at least 20 (30) treated sheets
- buf2, buf10:  controls at least 2 (10) km from every treated sheet centre
- nocap:        no height cap on controls ("all dry controls")
- ref2123:      2021-23 radar reference: pixels with water in any 2021 or 2022 scene of the window
                (flood_s1_reference_2122.py) removed from the flooded and valid counts, 2024 and 2025
- nocrop:       radar cells (0.001 degree) at least half WorldCover 2021 cropland removed likewise
For ref2123 and nocrop, provinces and the set of usable sheets are held at the primary ones; only
the flood shares used by the treatment rule change, and controls must still be dry (< 1%) on the
unmasked maps (otherwise a sheet flooded only on cropland would become a control) (recomputed from s1_flood_north.tif; with no pixels removed the
recomputation reproduces the primary shares exactly, checked here).

Land cover is computed once (per-sheet windows); elevation and height above the valley floor are
recomputed over each variant's provinces, as in the primary script (the merged DEM grid depends on
the bounding box, so sheet means differ slightly with it).

Input:  as rq1_2024_pooled.py
Output: 03_data/processed/rq1_2024_sens_<variant>_sample_sheets.csv.gz;
        04_analysis/outputs/tables/rq1_sensitivity_samples.{csv,md} (sizes by variant)
Run: .venv/bin/python -I 04_analysis/src/rq1_sensitivity_samples.py
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import rasterio
from rasterio.windows import Window

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rq1_2024_pooled import (DRY, KEY, LC_COLS, MIN_TREATED, MIN_VALID, RES, S1, SAMPLE_OUT, THRESH, UNO,  # noqa: E402
                             WC, elevation, landcover)
from flood_s1_grd import OUTD, REGIONS  # noqa: E402
from geo import dist_to_treated  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TAB = ROOT / "04_analysis/outputs/tables"
OUT = ROOT / "03_data/processed/rq1_2024_sens_{}_sample_sheets.csv.gz"
COLS = KEY + ["lon0", "lat0", "lon1", "lat1", "series_sheet", "group", "n_parcels", "mean_logp", "elev_m",
              "rel_elev_m"] + LC_COLS + ["s1_share_2024", "s1_share_2025", "flood2024_share", "dist_km"]
BASE = dict(thresh=THRESH, min_treated=MIN_TREATED, buffer=5, cap=True)
VARIANTS = {"primary": {}, "thr10": dict(thresh=0.10), "thr50": dict(thresh=0.50),
            "prov20": dict(min_treated=20), "prov30": dict(min_treated=30),
            "buf2": dict(buffer=2), "buf10": dict(buffer=10), "nocap": dict(cap=False),
            "ref2123": {}, "nocrop": {}}
FIXED_PROVS = ("thr10", "thr50", "ref2123", "nocrop")
FLAGS = OUTD / "s1_flood_north.tif"              # bits: 1 flood 2024, 2 flood 2025, 4 valid 2024, 8 valid 2025
REF2122 = OUTD / "s1_water_2021_22_north.tif"    # bit 1: water in any 2021-22 scene
CROP = OUTD / "worldcover_cropland_share_rq1_{}.tif"  # cache per grid window: cropland share of each cell (x 200)


def window_of(d):
    """Row/column window of the north grid covering the sheets in d."""
    (w_, _, _, n_), _ = REGIONS["north"]
    c0, c1 = int(np.floor((d["lon0"].min() - w_) / RES)), int(np.ceil((d["lon1"].max() - w_) / RES))
    r0, r1 = int(np.floor((n_ - d["lat1"].max()) / RES)), int(np.ceil((n_ - d["lat0"].min()) / RES))
    return max(r0, 0), max(c0, 0), r1, c1


def masked_shares(d, drop):
    """2024 and 2025 flood shares of the sheets in d with pixels where `drop` is True removed from both
    the flooded and the valid counts (box rule of flood_s1_grd.py)."""
    (w_, _, _, n_), _ = REGIONS["north"]
    R0, C0, R1, C1 = window_of(d)
    with rasterio.open(FLAGS) as s:
        f = s.read(1, window=Window(C0, R0, C1 - C0, R1 - R0))
    c0 = np.floor((d["lon0"] - w_) / RES).astype(int) - C0
    c1 = np.ceil((d["lon1"] - w_) / RES).astype(int) - C0
    r0 = np.floor((n_ - d["lat1"]) / RES).astype(int) - R0
    r1 = np.ceil((n_ - d["lat0"]) / RES).astype(int) - R0
    out = pd.DataFrame(index=d.index)
    for k, y in [(1, 2024), (2, 2025)]:
        boxes = []
        for layer in ((f & k) > 0, (f & 4 * k) > 0):
            S = np.pad(layer & ~drop, ((1, 0), (1, 0))).cumsum(0).cumsum(1, dtype=np.int64)
            boxes.append(S[r1, c1] - S[r0, c1] - S[r1, c0] + S[r0, c0])
        fl, va = boxes
        out[f"s1_share_{y}"] = np.where(va > 0, fl / np.maximum(va, 1), np.nan)
        out[f"valid_frac_{y}"] = va / ((d["lon1"] - d["lon0"]) * (d["lat1"] - d["lat0"]) / RES ** 2)  # as rq1_2024_pooled
    return out


def ref2122_mask(d):
    R0, C0, R1, C1 = window_of(d)
    with rasterio.open(REF2122) as s:
        return (s.read(1, window=Window(C0, R0, C1 - C0, R1 - R0)) & 1) > 0


def cropland_mask(d):
    """Cells of the window at least half cropland (WorldCover class 40) among classified 10 m pixels.
    WorldCover pixels are 1/12,000 degree and tiles start at whole degrees, so each 0.001-degree cell
    is exactly a 12 x 12 block."""
    R0, C0, R1, C1 = window_of(d)
    (w_, _, _, n_), _ = REGIONS["north"]
    cache = Path(str(CROP).format(f"{R0}_{C0}_{R1}_{C1}"))   # one file per window: other windows never overwrite it
    if cache.exists():
        with rasterio.open(cache) as s:
            if (np.isclose(s.bounds.left, w_ + C0 * RES) and np.isclose(s.bounds.top, n_ - R0 * RES)
                    and s.height == R1 - R0 and s.width == C1 - C0):
                return s.read(1) >= 100
    crop = np.zeros((R1 - R0, C1 - C0), np.int64)
    tot = np.zeros_like(crop)
    lon0, lat1 = w_ + C0 * RES, n_ - R0 * RES
    for path in WC:
        with rasterio.open(path) as s:
            b = s.bounds
            x0, x1 = max(b.left, lon0), min(b.right, lon0 + (C1 - C0) * RES)
            y1, y0 = min(b.top, lat1), max(b.bottom, lat1 - (R1 - R0) * RES)
            if x1 <= x0 or y1 <= y0:
                continue
            gc0, gc1 = int(round((x0 - lon0) / RES)), int(round((x1 - lon0) / RES))
            gr0, gr1 = int(round((lat1 - y1) / RES)), int(round((lat1 - y0) / RES))
            sc0, sr0 = int(round((x0 - b.left) * 12000)), int(round((b.top - y1) * 12000))
            for gr in range(gr0, gr1, 100):  # strips of 100 cells (1,200 source rows)
                nr = min(100, gr1 - gr)
                a = s.read(1, window=Window(sc0, sr0 + (gr - gr0) * 12, (gc1 - gc0) * 12, nr * 12))
                a = a.reshape(nr, 12, gc1 - gc0, 12)
                crop[gr:gr + nr, gc0:gc1] += (a == 40).sum((1, 3))
                tot[gr:gr + nr, gc0:gc1] += (a > 0).sum((1, 3))
    share = np.where(tot > 0, crop / np.maximum(tot, 1), 0)
    with rasterio.open(cache, "w", driver="GTiff", height=R1 - R0, width=C1 - C0, count=1, dtype="uint8",
                       crs="EPSG:4326", transform=rasterio.transform.from_origin(lon0, lat1, RES, RES),
                       compress="deflate") as o:
        o.write(np.round(share * 200).astype(np.uint8), 1)
    return share >= 0.5


def usable():
    """Usable sheets with UNOSAT shares attached, exactly as in rq1_2024_pooled.main."""
    dt = {"UTMMAP1": str, "UTMMAP3": str, "UTMMAP4": str, "prov_code": str}
    d = pd.read_csv(S1, dtype=dt, keep_default_na=False, na_values=[""])
    u = pd.read_csv(UNO, dtype=dt, keep_default_na=False, na_values=[""])
    u = u[u["in_analysis_extent"] & u["flood2024_share"].notna()]
    for k in KEY:
        u[k], d[k] = u[k].astype(str), d[k].astype(str)
    d = d.merge(u[KEY + ["flood2024_share"]], on=KEY, how="left")
    box_px = (d["lon1"] - d["lon0"]) * (d["lat1"] - d["lat0"]) / RES ** 2
    return d[(d["s1_valid_px_2024"] >= MIN_VALID * box_px) & (d["s1_valid_px_2025"] >= MIN_VALID * box_px)
             & d["mean_logp"].notna()].copy()


def provinces(d, thresh, min_treated):
    T = (d["s1_share_2024"] > thresh) & (d["s1_share_2025"] <= thresh)
    nt = T.groupby(d["province"]).sum()
    return list(nt[nt >= min_treated].index)


def build(d, thresh, min_treated, buffer, cap, provs=None):
    provs = provs if provs is not None else provinces(d, thresh, min_treated)
    p = d[d["province"].isin(provs)].copy()
    p["T"] = ((p["s1_share_2024"] > thresh) & (p["s1_share_2025"] <= thresh)).astype(int)
    if "masked_valid_ok" in p:   # masked variants: the share must rest on at least half the box, as in the primary rule
        p["T"] = p["T"] * p["masked_valid_ok"].astype(int)
    # masked variants change the treatment rule only: the buffer is measured from sheets treated under
    # either rule, the height cap comes from the unmasked rule, and controls must be dry on the unmasked maps
    dry24, dry25 = p.get("dry_share_2024", p["s1_share_2024"]), p.get("dry_share_2025", p["s1_share_2025"])
    t_unmasked = (dry24 > thresh) & (dry25 <= thresh)
    t = p[p["T"] == 1]
    near = p[(p["T"] == 1) | t_unmasked]
    p["dist_km"] = dist_to_treated(p, (p["T"] == 1) | t_unmasked)   # great-circle km (geo.py)
    p["elev_m"] = elevation(p)  # over the variant's bounding box, as in the primary script
    p["rel_elev_m"] = p["elev_m"] - p.groupby("series_sheet")["elev_m"].transform(lambda s: s.quantile(0.05))
    t = p[p["T"] == 1]
    cut = p.loc[t_unmasked if "masked_valid_ok" in p else p["T"] == 1, "rel_elev_m"].quantile(0.90) if cap else np.inf
    c = p[(p["T"] == 0) & (dry24 < DRY) & (dry25 < DRY) & (p["dist_km"] >= buffer) & (p["rel_elev_m"] <= cut)]
    c = c[~(c["flood2024_share"] >= DRY)]
    return pd.concat([t.assign(group="treated"), c.assign(group="control")])[COLS]


def main() -> None:
    d = usable()
    union = sorted(set().union(*(provinces(d, v.get("thresh", THRESH), v.get("min_treated", MIN_TREATED))
                                 for v in VARIANTS.values())))
    d = d[d["province"].isin(union)].copy()
    d[LC_COLS] = landcover(d)                   # per-sheet windows: independent of the variant
    primary_provs = provinces(d, THRESH, MIN_TREATED)
    p4 = d[d["province"].isin(primary_provs)]
    check = masked_shares(p4, np.zeros(np.subtract(window_of(p4)[2:], window_of(p4)[:2]), bool))
    for y in (2024, 2025):
        if not np.allclose(check[f"s1_share_{y}"], p4[f"s1_share_{y}"], equal_nan=True):
            raise SystemExit(f"recomputed {y} shares do not reproduce sheet_flood_s1.csv.gz")
        if not (check[f"valid_frac_{y}"] >= MIN_VALID).all():
            raise SystemExit(f"recomputed {y} valid counts do not reproduce the usable-sheet rule")
    masks = {"ref2123": ref2122_mask, "nocrop": cropland_mask}
    ref_t = pd.read_csv(SAMPLE_OUT, dtype=str, keep_default_na=False)
    ref_t = set(map(tuple, ref_t.loc[ref_t["group"] == "treated", KEY].to_numpy()))
    rows = []
    for name, v in VARIANTS.items():
        s = {**BASE, **v}
        fixed = primary_provs if name in FIXED_PROVS else None
        dv = d
        if name in masks:
            dv = p4.copy()
            dv["dry_share_2024"], dv["dry_share_2025"] = dv["s1_share_2024"], dv["s1_share_2025"]
            ms = masked_shares(p4, masks[name](p4))
            dv[["s1_share_2024", "s1_share_2025"]] = ms[["s1_share_2024", "s1_share_2025"]]
            dv["masked_valid_ok"] = (ms["valid_frac_2024"] >= MIN_VALID) & (ms["valid_frac_2025"] >= MIN_VALID)
        out = build(dv, s["thresh"], s["min_treated"], s["buffer"], s["cap"], provs=fixed)
        if name == "primary":
            ref = pd.read_csv(SAMPLE_OUT, dtype=str, keep_default_na=False)
            mine = pd.read_csv(pd.io.common.StringIO(out.to_csv(index=False)), dtype=str, keep_default_na=False)
            if not mine.equals(ref):
                raise SystemExit("primary variant does not reproduce rq1_2024_sample_sheets.csv.gz")
        else:
            out.to_csv(Path(str(OUT).format(name)), index=False)
        tr = out[out["group"] == "treated"]
        rows.append({"variant": name, **s, "provinces": "+".join(sorted(out["province"].unique())),
                     "treated": len(tr), "treated_also_primary": sum(tuple(map(str, k)) in ref_t
                                                                      for k in tr[KEY].to_numpy()),
                     "controls": int((out["group"] == "control").sum()),
                     "treated_clusters": tr["series_sheet"].nunique()})
    r = pd.DataFrame(rows)
    TAB.mkdir(parents=True, exist_ok=True)
    r.to_csv(TAB / "rq1_sensitivity_samples.csv", index=False)
    (TAB / "rq1_sensitivity_samples.md").write_text(
        "<!-- RQ1 sensitivity samples (one setting changed from the primary each); the primary variant reproduces "
        "rq1_2024_sample_sheets.csv.gz. Sources: Sentinel-1 radar maps; UNOSAT; Treasury Department; author's "
        "calculations. -->\n\n" + r.to_markdown(index=False) + "\n", encoding="utf-8")
    print(r.to_string(index=False))


if __name__ == "__main__":
    main()

"""Pooled 2024 sample (pre-registered primary for RQ1): size, balance and power; S1 vs UNOSAT check.

Input:  03_data/processed/sheet_flood_s1.csv.gz           (flood_s1_grd.py)
        03_data/raw/elevation/copernicus_glo90/*.tif       (download_dem90.py)
        03_data/processed/sheet_flood2024_north.csv.gz    (exposure_2024_north.py; UNOSAT shares)
        03_data/raw/landcover/worldcover_2021{,_north,_pooled}/*.tif
                                                           (download_north_covariates.py,
                                                            download_worldcover_pooled.py)
Rules (as in the pre-analysis plan):
- usable sheet: Sentinel-1 valid pixels cover at least half of the sheet's bounding box in both
  2024 and 2025;
- treated: 2024 share > 25% and 2025 share <= 25%;
- sample provinces: at least MIN_TREATED treated sheets (sensitivity: at least one);
- controls: same provinces, 2024 and 2025 shares < 1%, centre at least 5 km (2 and 10 km as
  sensitivities) from every treated sheet centre;
- hazard-comparable controls: height above the valley floor (sheet mean GLO-90 elevation minus
  the 5th percentile over sheets in the same 1:50,000 sheet) no more than the treated 90th
  percentile;
- clusters: 1:50,000 sheets; MDE with shared clusters as in rq1_2024_design_power.py;
- balance: standardised differences in pre-flood log value and height above the valley floor,
  before and after entropy balancing of controls on both means within each province, with the
  controls' effective sample size, for each buffer; WorldCover 2021 shares (built-up, cropland,
  tree, water) reported before and after the weights; a variant also balances on built-up and
  cropland, the pre-registered weighting (balancing on water as well fails in two provinces: no
  overlap); a sensitivity drops treated sheets wetter than their controls' 99th percentile;
  weights solve the convex entropy-balancing dual by Newton (trust-exact) steps;
- contamination check: comparable 5 km controls that UNOSAT maps as more than 25% flooded
  (Chiang Rai and Phayao only), and the MDE with them dropped;
- primary controls (round 12): dry in every source, i.e. radar 2024 and 2025 < 1% and UNOSAT
  2024 < 1% where UNOSAT maps the sheet, with balance, effective sample size and MDE;
  treated_clusters = 1:50,000 sheets containing at least one treated sheet; the treated sheets and
  these controls are written to 03_data/processed/rq1_2024_sample_sheets.csv.gz with their pre-flood
  covariates (for validate_s1_s2.py and rq1_round_change.py).
Outputs (04_analysis/outputs/tables): rq1_2024_pooled_provinces.{csv,md},
  rq1_2024_pooled_mde.{csv,md}, rq1_2024_pooled_balance.{csv,md}, s1_unosat_validation.{csv,md}

Run: .venv/bin/python -I 04_analysis/src/rq1_2024_pooled.py
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import rasterio
from rasterio.merge import merge
from rasterio.windows import from_bounds
from scipy import stats
from scipy.optimize import minimize

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rq1_2024_design_power import mde_table, smd  # noqa: E402
from geo import dist_to_treated  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
S1 = ROOT / "03_data/processed/sheet_flood_s1.csv.gz"
UNO = ROOT / "03_data/processed/sheet_flood2024_north.csv.gz"
DEM = sorted((ROOT / "03_data/raw/elevation/copernicus_glo90").glob("*.tif"))
WC = sorted((ROOT / "03_data/raw/landcover/worldcover_2021_north").glob("*.tif")) + sorted(
    (ROOT / "03_data/raw/landcover/worldcover_2021_pooled").glob("*.tif")) + sorted(
    (ROOT / "03_data/raw/landcover/worldcover_2021").glob("*.tif"))  # last two dirs also serve the 2025 sample
LC = {"builtup": [50], "cropland": [40], "tree": [10], "water": [80]}
LC_COLS = [f"lc_{k}" for k in LC]
BAL_PRIMARY = ["mean_logp", "rel_elev_m", "lc_builtup", "lc_cropland"]  # pre-registered weighting
TAB = ROOT / "04_analysis/outputs/tables"
SAMPLE_OUT = ROOT / "03_data/processed/rq1_2024_sample_sheets.csv.gz"  # for validate_s1_s2.py
RES, MIN_VALID, THRESH, DRY, MIN_TREATED, ICC = 0.001, 0.5, 0.25, 0.01, 25, 0.2
BUFFERS = [2, 5, 10]
KEY = ["province", "UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "UTMSCALE"]
SOURCE = ("Sources: Treasury Department official land values 2023-26 (snapshot 2026-11-02); Copernicus "
          "Sentinel-1 GRD via Microsoft Planetary Computer; Copernicus DEM GLO-90; author's calculations.")


def write(df, name, note):
    df.to_csv(TAB / f"{name}.csv", index=False)
    (TAB / f"{name}.md").write_text(f"<!-- {note} {SOURCE} -->\n\n" + df.round(3).to_markdown(index=False) + "\n",
                                    encoding="utf-8")


def elevation(d):
    bb = (d["lon0"].min() - 0.01, d["lat0"].min() - 0.01, d["lon1"].max() + 0.01, d["lat1"].max() + 0.01)
    srcs = [rasterio.open(p) for p in DEM]
    arr, tr = merge(srcs, bounds=bb, nodata=np.nan)
    for s in srcs:
        s.close()
    a = arr[0].astype("float64")
    ok = ~np.isnan(a)
    S = np.pad(np.where(ok, a, 0), ((1, 0), (1, 0))).cumsum(0).cumsum(1)
    N = np.pad(ok, ((1, 0), (1, 0))).cumsum(0).cumsum(1, dtype=np.int64)
    inv = ~tr
    c0, r0 = inv * (d["lon0"].values, d["lat1"].values)
    c1, r1 = inv * (d["lon1"].values, d["lat0"].values)
    c0, r0 = np.floor(c0).astype(int), np.floor(r0).astype(int)
    c1, r1 = np.maximum(np.ceil(c1).astype(int), c0 + 1), np.maximum(np.ceil(r1).astype(int), r0 + 1)
    box = lambda M: M[r1, c1] - M[r0, c1] - M[r1, c0] + M[r0, c0]  # noqa: E731
    return box(S) / np.maximum(box(N), 1)


def landcover(d):
    """WorldCover 2021 shares of each sheet's classified pixels; sheets may straddle tiles."""
    cnt = np.zeros((len(d), 256), dtype=np.int64)
    bounds = d[["lon0", "lat0", "lon1", "lat1"]].values
    for path in WC:
        with rasterio.open(path) as s:
            x0, y0, x1, y1 = s.bounds
            hit = np.nonzero((bounds[:, 0] < x1) & (bounds[:, 2] > x0) & (bounds[:, 1] < y1) & (bounds[:, 3] > y0))[0]
            for i in hit:
                w = from_bounds(*bounds[i], s.transform).round_offsets().round_lengths()
                cnt[i] += np.bincount(s.read(1, window=w, boundless=True, fill_value=0).ravel(), minlength=256)[:256]
    n = cnt[:, 1:].sum(axis=1)
    return pd.DataFrame({f"lc_{k}": cnt[:, c].sum(axis=1) / np.where(n > 0, n, np.nan) for k, c in LC.items()},
                        index=d.index)


def ebal(xc, target):
    """Entropy-balancing weights for controls xc (n x k) matching the treated means target (k)."""
    mu, sd = xc.mean(0), xc.std(0)
    z, zt = (xc - mu) / sd, (target - mu) / sd

    def f(lam):
        e = z @ lam
        m = e.max()
        w = np.exp(e - m)
        return m + np.log(w.sum()) - zt @ lam, (w / w.sum()) @ z - zt

    def hess(lam):  # convex dual: Hessian is the weighted covariance of z
        e = z @ lam
        p = np.exp(e - e.max())
        p /= p.sum()
        zc = z - p @ z
        return (zc * p[:, None]).T @ zc

    lam = minimize(f, np.zeros(z.shape[1]), jac=True, hess=hess, method="trust-exact",
                   options={"gtol": 1e-8, "maxiter": 1000}).x
    w = np.exp(z @ lam - (z @ lam).max())
    w /= w.sum()
    gap = np.abs(w @ z - zt).max()
    if gap > 1e-4:
        print(f"ebal: {len(xc)} controls, largest standardised mean gap {gap:.4f} after convergence")
    return w


def balance(t, c, label, cols=("mean_logp", "rel_elev_m")):
    cols = list(cols)
    w = pd.Series(0.0, index=c.index)
    for pr, tp in t.groupby("province"):
        cp = c[c["province"] == pr]
        w[cp.index] = ebal(cp[cols].values, tp[cols].values.mean(0)) * len(tp)
    ess = w.sum() ** 2 / (w ** 2).sum()
    a_g = t.groupby("series_sheet").size() / len(t)
    b_g = w.groupby(c["series_sheet"]).sum() / w.sum()
    a_g, b_g = a_g.align(b_g, fill_value=0)
    G = int(((a_g > 0) | (b_g > 0)).sum())
    se1 = np.sqrt(ICC * ((a_g - b_g) ** 2).sum() + (1 - ICC) * (1 / len(t) + 1 / ess))
    r = {"controls": label, "treated": len(t), "control_sheets": len(c), "ess_controls_weighted": ess,
         "mde_sd0.10_weighted": (stats.t.ppf(0.975, G - 1) + stats.t.ppf(0.80, G - 1)) * 0.10 * se1}
    for col in ["mean_logp", "rel_elev_m"] + LC_COLS:
        pooled_sd = np.sqrt((t[col].var() + c[col].var()) / 2)
        r[f"smd_{col}"] = (t[col].mean() - c[col].mean()) / pooled_sd
        r[f"smd_{col}_weighted"] = (t[col].mean() - np.average(c[col], weights=w)) / pooled_sd
    return r


def main() -> None:
    TAB.mkdir(parents=True, exist_ok=True)
    d = pd.read_csv(S1, dtype={"UTMMAP1": str, "UTMMAP3": str, "UTMMAP4": str, "prov_code": str},
                    keep_default_na=False, na_values=[""])
    u = pd.read_csv(UNO, dtype={"UTMMAP1": str, "UTMMAP3": str, "UTMMAP4": str, "prov_code": str},
                    keep_default_na=False, na_values=[""])
    u = u[u["in_analysis_extent"] & u["flood2024_share"].notna()]
    for k in KEY:
        u[k], d[k] = u[k].astype(str), d[k].astype(str)
    d = d.merge(u[KEY + ["flood2024_share"]], on=KEY, how="left")
    box_px = (d["lon1"] - d["lon0"]) * (d["lat1"] - d["lat0"]) / RES ** 2
    d = d[(d["s1_valid_px_2024"] >= MIN_VALID * box_px) & (d["s1_valid_px_2025"] >= MIN_VALID * box_px)
          & d["mean_logp"].notna()].copy()
    d["T"] = ((d["s1_share_2024"] > THRESH) & (d["s1_share_2025"] <= THRESH)).astype(int)
    nt = d.groupby("province")["T"].sum()
    provs = nt[nt >= MIN_TREATED].index
    p = d[d["province"].isin(provs)].copy()
    t = p[p["T"] == 1]
    p["dist_km"] = dist_to_treated(p, p["T"] == 1)   # great-circle km (geo.py)
    p["elev_m"] = elevation(p)
    p["rel_elev_m"] = p["elev_m"] - p.groupby("series_sheet")["elev_m"].transform(lambda s: s.quantile(0.05))
    p[LC_COLS] = landcover(p)
    t = p[p["T"] == 1]
    cut = t["rel_elev_m"].quantile(0.90)
    dry = (p["T"] == 0) & (p["s1_share_2024"] < DRY) & (p["s1_share_2025"] < DRY)

    pr = p.groupby("province").agg(treated=("T", "sum"), sheets=("T", "size")).reset_index()
    pr["controls_5km_comparable"] = pr["province"].map(
        p[dry & (p["dist_km"] >= 5) & (p["rel_elev_m"] <= cut)].groupby("province").size()).fillna(0).astype(int)
    pr = pr.sort_values("treated", ascending=False)
    write(pr, "rq1_2024_pooled_provinces",
          f"Pooled 2024 sample by province (provinces with >= {MIN_TREATED} treated sheets; "
          f"{int((nt >= 1).sum())} provinces have at least one). Treated: S1 2024 share > 25%, 2025 share <= 25%.")

    mts, bal = [], []
    for b in BUFFERS:
        c = p[dry & (p["dist_km"] >= b)]
        bal.append(balance(t, c[c["rel_elev_m"] <= cut], f"hazard-comparable, {b} km"))
        bal.append(balance(t, c[c["rel_elev_m"] <= cut], f"hazard-comparable, {b} km, also on built-up and cropland",
                           BAL_PRIMARY))
        if b == 5:  # sensitivity: drop treated sheets wetter than their province's controls' 99th percentile
            cc5 = c[c["rel_elev_m"] <= cut]
            q99 = t["province"].map(cc5.groupby("province")["lc_water"].quantile(0.99))
            bal.append(balance(t[t["lc_water"] <= q99], cc5,
                               f"hazard-comparable, {b} km, also on built-up and cropland, high-water treated dropped",
                               BAL_PRIMARY))
        mts.append(mde_table(pd.concat([c, t]), f"all dry, {b} km"))
        cc = c[c["rel_elev_m"] <= cut]
        a = pd.concat([cc, t])
        m = mde_table(a, f"hazard-comparable, {b} km")
        sh = pd.crosstab(a["series_sheet"], a["T"])
        mixed = sh.index[(sh[1] > 0) & (sh[0] > 0)]
        m["treated_in_mixed_clusters"] = int(t["series_sheet"].isin(mixed).sum())
        if b == 5:
            m["smd_logp"] = smd(t["mean_logp"], cc["mean_logp"])
            m["median_rel_elev_treated"] = t["rel_elev_m"].median()
            m["median_rel_elev_controls"] = cc["rel_elev_m"].median()
            wet = cc["flood2024_share"] > THRESH
            m["controls_unosat_flooded"] = int(wet.sum())
            mts.append(m)
            mts.append(mde_table(pd.concat([cc[~wet], t]),
                                 f"hazard-comparable, {b} km, UNOSAT-flooded controls dropped"))
            # primary control set from round 12: dry in every source (radar 2024 and 2025 < 1%, and
            # UNOSAT 2024 < 1% where UNOSAT maps the sheet; outside Chiang Rai-Phayao radar only)
            strict = cc[~(cc["flood2024_share"] >= DRY)]
            samp = pd.concat([t.assign(group="treated"), strict.assign(group="control")])
            samp[KEY + ["lon0", "lat0", "lon1", "lat1", "series_sheet", "group", "n_parcels", "mean_logp", "elev_m",
                  "rel_elev_m"] + LC_COLS + ["s1_share_2024", "s1_share_2025", "flood2024_share", "dist_km"]].to_csv(
                SAMPLE_OUT, index=False)
            bal.append(balance(t, strict, f"hazard-comparable, {b} km, dry in every source, also on built-up and cropland",
                               BAL_PRIMARY))
            m = mde_table(pd.concat([strict, t]), f"hazard-comparable, {b} km, dry in every source")
        mts.append(m)
    write(pd.DataFrame(bal), "rq1_2024_pooled_balance",
          "Balance of the pooled sample by buffer: standardised differences (treated minus controls, pooled SD) "
          "before and after entropy balancing of controls on pre-flood mean log value and height above the valley "
          "floor within each province (WorldCover 2021 land-cover shares reported; the 'also on' rows add built-up and cropland "
          "shares and are the pre-registered weighting; 'high-water treated dropped' removes treated sheets whose water share "
          "exceeds the 99th percentile of their province's controls); ess = Kish effective number of controls; weighted MDE at SD 0.10, ICC 0.2, "
          "with shared clusters.")
    print(pd.DataFrame(bal).round(3).to_string(index=False))
    mt = pd.concat(mts, ignore_index=True)
    write(mt, "rq1_2024_pooled_mde",
          f"MDEs for the pooled sample (80% power, 5% two-sided; t with G-1 df; clusters = 1:50,000 sheets "
          f"shared by treated and controls). Hazard-comparable: rel_elev_m <= {cut:.1f} m (treated 90th "
          f"percentile, GLO-90). Provinces: {', '.join(sorted(provs))}.")
    print(pr.to_string(index=False))
    print(mt[mt["icc_changes"] == 0.2].round(3).to_string(index=False))

    v = d[d["flood2024_share"].notna()]
    a, b = v["flood2024_share"] > THRESH, v["s1_share_2024"] > THRESH
    po = (a == b).mean()
    pe = a.mean() * b.mean() + (1 - a.mean()) * (1 - b.mean())
    val = pd.DataFrame([{"sheets": len(v), "unosat_treated": int(a.sum()), "s1_treated": int(b.sum()),
                         "both": int((a & b).sum()), "unosat_only": int((a & ~b).sum()), "s1_only": int((~a & b).sum()),
                         "recall": (a & b).sum() / a.sum(), "precision": (a & b).sum() / b.sum(),
                         "agreement": po, "kappa": (po - pe) / (1 - pe),
                         "corr_shares": v["flood2024_share"].corr(v["s1_share_2024"])}])
    write(val, "s1_unosat_validation",
          "Chiang Rai and Phayao analysis extent: sheets usable in both maps; treated = share > 25%. "
          "UNOSAT FL20240912THA (multi-sensor) vs the Sentinel-1 rule.")
    print(val.round(3).to_string(index=False))


if __name__ == "__main__":
    main()

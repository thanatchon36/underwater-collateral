"""RQ1 primary design (2024 floods): control set after buffers, and an indicative power bound.

Input:  03_data/processed/sheet_flood2024_north.csv.gz (exposure_2024_north.py)
        03_data/processed/sheet_flood_s1.csv.gz (flood_s1_grd.py; radar shares for the
        "dry in every source" control set)
        03_data/processed/sheet_north_covariates.csv.gz (build_north_covariates.py)
Output: 04_analysis/outputs/tables/rq1_2024_controls_power.{csv,md}
- treated: sheets with UNOSAT 2024 flood share > 25% inside the analysis extent;
- controls: sheets with flood share 0, at least `buffer_km` from any treated sheet centre
  (approximate km from WGS84 centres at 19.5 N);
- MDE (80% power, 5% two-sided, factor 2.8) for the treated-control difference, using the
  2023-26 *level* of mean parcel log value, demeaned by province x scale, as the outcome:
  (a) with 1:50,000-sheet cluster means (conservative: levels vary far more than changes);
  (b) treating sheets as independent (optimistic). The true change-based MDE is unknown until
  the 2027-30 round is released.
- Hazard-comparable controls (the pre-registered primary comparison): unflooded sheets, 5 km
  buffer, whose height above the local valley floor (rel_elev_m) is no more than the 90th
  percentile among treated sheets. Balance table rq1_2024_balance.{csv,md}: medians and
  standardised mean differences of ex-ante covariates for all and comparable controls.
- MDE table (rq1_2024_mde_changes.{csv,md}) for the equally weighted sheet-mean change, for both
  control sets, as a function of the (unknown) SD of sheet-level changes (sigma) and the
  intra-cluster correlation of changes (rho) across 1:50,000 sheets. Treated and control sheets
  share clusters, so with a common cluster effect
      Var(diff) = sigma^2 [rho * sum_g (a_g - b_g)^2 + (1 - rho) (1/n1 + 1/n0)],
  a_g, b_g = cluster g's shares of treated and control sheets; G = distinct clusters;
      MDE = (t_{0.975,G-1} + t_{0.80,G-1}) * sqrt(Var(diff)),
  and the smallest equivalence margin with 80% power for two one-sided 5% tests at a true
  effect of zero is (t_{0.95,G-1} + t_{0.90,G-1}) * sqrt(Var(diff)). The carry-over share is
  binary, so its sheet-level SD is at most 0.5 (MDE in percentage points).

Run: .venv/bin/python -I 04_analysis/src/rq1_2024_design_power.py
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from geo import dist_to_treated  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "03_data/processed/sheet_flood2024_north.csv.gz"
S1 = ROOT / "03_data/processed/sheet_flood_s1.csv.gz"
KEY = ["province", "UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "UTMSCALE"]
COV = ROOT / "03_data/processed/sheet_north_covariates.csv.gz"
COVS = ["rel_elev_m", "elev_m", "river_km", "lc_builtup", "lc_cropland", "lc_tree"]
TAB = ROOT / "04_analysis/outputs/tables"
SAMPLE_OUT = ROOT / "03_data/processed/rq1_2024_unosat_sample_sheets.csv.gz"  # read by rq1_round_change.py
THRESH, BUFFERS = 0.25, [2, 5, 10]
SDS, ICCS = [0.05, 0.10, 0.20], [0.05, 0.20, 0.50]


def mde_table(a: pd.DataFrame, label: str) -> pd.DataFrame:
    """MDEs for the equally weighted sheet-mean change, with shared treated/control clusters."""
    n1, n0 = int((a["T"] == 1).sum()), int((a["T"] == 0).sum())
    sh = pd.crosstab(a["series_sheet"], a["T"])
    G = len(sh)
    ssq = ((sh[1] / n1 - sh[0] / n0) ** 2).sum()
    fac = stats.t.ppf(0.975, G - 1) + stats.t.ppf(0.80, G - 1)
    feq = stats.t.ppf(0.95, G - 1) + stats.t.ppf(0.90, G - 1)
    rows = []
    for icc in ICCS:
        se1 = np.sqrt(icc * ssq + (1 - icc) * (1 / n1 + 1 / n0))
        r = {"controls": label, "treated": n1, "control_sheets": n0, "clusters": G,
             "treated_clusters": int((sh[1] > 0).sum()),
             "mixed_clusters": int(((sh[1] > 0) & (sh[0] > 0)).sum()), "icc_changes": icc}
        for sd in SDS:
            r[f"mde_sd{sd:.2f}"] = fac * sd * se1
        r["equiv_margin_sd0.10"] = feq * 0.10 * se1
        r["mde_carryover_pp"] = 100 * fac * 0.5 * se1
        rows.append(r)
    return pd.DataFrame(rows)


def smd(t: pd.Series, c: pd.Series) -> float:
    return (t.mean() - c.mean()) / np.sqrt((t.var() + c.var()) / 2)


def main() -> None:
    d = pd.read_csv(SRC, dtype={k: str for k in KEY[1:]}, keep_default_na=False, na_values=[""])
    d = d[d["in_analysis_extent"]].reset_index(drop=True)
    cov = pd.read_csv(COV)
    assert (cov["series_sheet"].values == d["series_sheet"].values).all()
    for c in COVS + ["lc_water"]:
        d[c] = cov[c].values
    d = d[d["flood2024_share"].notna()].copy()
    t = d[d["flood2024_share"] > THRESH].assign(T=1)
    d["dist_km"] = dist_to_treated(d, d["flood2024_share"] > THRESH)   # great-circle km (geo.py)
    rows, cuts = [], {}
    for b in BUFFERS:
        c = d[(d["flood2024_share"] == 0) & (d["dist_km"] >= b)].assign(T=0)
        a = pd.concat([c, t])
        a["yd"] = a["mean_logp"] - a.groupby(["province", "scale"])["mean_logp"].transform("mean")
        cl = a.groupby(["T", "series_sheet"])["yd"].mean().reset_index().groupby("T")["yd"].agg(["var", "count"])
        sh = a.groupby("T")["yd"].agg(["var", "count"])
        cuts[b] = c
        if b == 5:
            a5, c5 = a, c
        rows.append({"buffer_km": b, "treated_sheets": len(t), "control_sheets": len(c),
                     "control_urban_1000": int((c["scale"] == 1000).sum()),
                     "control_rural_4000": int((c["scale"] == 4000).sum()),
                     "treated_clusters": int(cl.loc[1, "count"]), "control_clusters": int(cl.loc[0, "count"]),
                     "mde_cluster_levels": 2.8 * np.sqrt((cl["var"] / cl["count"]).sum()),
                     "mde_sheet_iid_levels": 2.8 * np.sqrt((sh["var"] / sh["count"]).sum())})
    r = pd.DataFrame(rows)
    TAB.mkdir(parents=True, exist_ok=True)
    r.to_csv(TAB / "rq1_2024_controls_power.csv", index=False)
    (TAB / "rq1_2024_controls_power.md").write_text(
        "<!-- Source: Treasury Department official land values 2023-26 (snapshot 2026-11-02); UNOSAT "
        "FL20240912THA extents; author's calculations. MDEs use levels, not changes: indicative only. -->\n\n"
        + r.round(3).to_markdown(index=False) + "\n", encoding="utf-8")
    print(r.round(3).to_string(index=False))
    # hazard-comparable controls: no higher above the local valley floor than 90% of treated sheets
    cut = t["rel_elev_m"].quantile(0.90)
    cc = c5[c5["rel_elev_m"] <= cut]
    ac = pd.concat([cc, t])
    # dry in every source (round 12): also drop controls whose radar share is >= 1% in 2024 or 2025
    # (sheets without usable radar are kept and counted)
    s1 = pd.read_csv(S1, usecols=KEY + ["s1_share_2024", "s1_share_2025"], dtype={k: str for k in KEY[1:]},
                     keep_default_na=False, na_values=[""])
    cc_k = cc[KEY].merge(s1, on=KEY, how="left", validate="many_to_one")
    radar_wet = ((cc_k["s1_share_2024"] >= 0.01) | (cc_k["s1_share_2025"] >= 0.01)).values
    # UNOSAT sample for the registered code (rq1_round_change.py --event unosat): treated and the
    # dry-in-every-source controls, same columns as the radar sample
    t_k = t[KEY].merge(s1, on=KEY, how="left", validate="many_to_one")
    samp = pd.concat([t.assign(group="treated", s1_share_2024=t_k["s1_share_2024"].values,
                               s1_share_2025=t_k["s1_share_2025"].values),
                      cc[~radar_wet].assign(group="control", s1_share_2024=cc_k["s1_share_2024"].values[~radar_wet],
                                            s1_share_2025=cc_k["s1_share_2025"].values[~radar_wet])])
    samp[KEY + ["lon0", "lat0", "lon1", "lat1", "series_sheet", "group", "n_parcels", "mean_logp", "elev_m",
                "rel_elev_m", "lc_builtup", "lc_cropland", "lc_tree", "lc_water", "s1_share_2024", "s1_share_2025",
                "flood2024_share", "dist_km"]].to_csv(SAMPLE_OUT, index=False)
    print(f"UNOSAT comparable controls: {len(cc)}, radar-wet (2024 or 2025 >= 1%): {radar_wet.sum()}, "
          f"no radar share: {cc_k['s1_share_2024'].isna().sum()}")
    mt = pd.concat([mde_table(a5, "all unflooded")]
                   + [mde_table(pd.concat([cuts[b][cuts[b]["rel_elev_m"] <= cut], t]),
                                "hazard-comparable" + ("" if b == 5 else f", {b} km buffer")) for b in BUFFERS]
                   + [mde_table(pd.concat([cc[~radar_wet], t]), "hazard-comparable, dry in every source")
                      .assign(controls_radar_wet=int(radar_wet.sum()))],
                   ignore_index=True)
    mt.to_csv(TAB / "rq1_2024_mde_changes.csv", index=False)
    (TAB / "rq1_2024_mde_changes.md").write_text(
        "<!-- MDEs for the sheet-mean change (80% power, 5% two-sided; t with G-1 df, G = distinct 1:50,000 "
        "clusters shared by treated and control sheets), 5 km buffer unless the label says otherwise. SDs and ICCs of changes are assumptions. "
        f"Hazard-comparable: rel_elev_m <= {cut:.1f} m (treated 90th percentile). Author's calculations. -->\n\n"
        + mt.round(3).to_markdown(index=False) + "\n", encoding="utf-8")
    print(mt.round(3).to_string(index=False))
    bal = []
    for v in ["mean_logp"] + COVS:
        bal.append({"variable": v, "treated_median": t[v].median(), "all_controls_median": c5[v].median(),
                    "comparable_controls_median": cc[v].median(), "smd_all": smd(t[v], c5[v]),
                    "smd_comparable": smd(t[v], cc[v])})
    bal = pd.DataFrame(bal)
    bal.to_csv(TAB / "rq1_2024_balance.csv", index=False)
    (TAB / "rq1_2024_balance.md").write_text(
        "<!-- Ex-ante balance, 2024 design, 5 km buffer: treated (UNOSAT share > 25%) vs all unflooded and "
        f"hazard-comparable controls (rel_elev_m <= {cut:.1f} m). mean_logp = 2023-26 round (set before the floods). "
        "SMD = difference in means / pooled SD. Sources: Treasury Department; UNOSAT; ESA WorldCover 2021; "
        "Copernicus GLO-30; JRC GSW. Author's calculations. -->\n\n"
        + bal.round(3).to_markdown(index=False) + "\n", encoding="utf-8")
    print(bal.round(3).to_string(index=False))


if __name__ == "__main__":
    main()

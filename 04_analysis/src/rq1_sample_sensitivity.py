"""RQ1 sample sensitivity: province inclusion threshold (2024) and the 2025 floods as a second event.

Same rules as rq1_2024_pooled.py (usable sheets, 25% treated share, controls < 1% flooded in 2024
and 2025, 5 km buffer, hazard-comparable height cut at the treated 90th percentile, clusters =
1:50,000 sheets), varying:
- the minimum number of treated sheets for a province to enter (20, 25, 30), 2024 event;
- the event: 2025 share > 25% on sheets under 1% flooded in 2024 (a second, separate event,
  candidate Plan B chapter), minimum 25 treated sheets.
MDE at SD 0.10 and 0.20, ICC 0.2, 80% power (mde_table in rq1_2024_design_power.py).

Inputs: as rq1_2024_pooled.py. Output: 04_analysis/outputs/tables/rq1_sample_sensitivity.{csv,md};
03_data/processed/rq1_2025_sample_sheets.csv.gz (2025 treated sheets and controls with pre-flood covariates,
including WorldCover 2021 shares, for rq1_round_change.py --sample)
Run: .venv/bin/python -I 04_analysis/src/rq1_sample_sensitivity.py
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rq1_2024_design_power import mde_table  # noqa: E402
from geo import dist_to_treated  # noqa: E402
from rq1_2024_pooled import DRY, KEY, LC_COLS, MIN_VALID, RES, S1, THRESH, elevation, landcover, write  # noqa: E402

BUFFER = 5
SAMPLE_2025 = Path(__file__).resolve().parents[2] / "03_data/processed/rq1_2025_sample_sheets.csv.gz"


def build(d: pd.DataFrame, treat: pd.Series, min_treated: int, label: str, export=None) -> dict:
    d = d.assign(T=treat.astype(int))
    nt = d.groupby("province")["T"].sum()
    provs = nt[nt >= min_treated].index
    p = d[d["province"].isin(provs)].copy()
    t = p[p["T"] == 1]
    p["dist_km"] = dist_to_treated(p, p["T"] == 1)   # great-circle km (geo.py)
    p["elev_m"] = elevation(p)
    p["rel_elev_m"] = p["elev_m"] - p.groupby("series_sheet")["elev_m"].transform(lambda s: s.quantile(0.05))
    t = p[p["T"] == 1]
    cut = t["rel_elev_m"].quantile(0.90)
    dry = (p["T"] == 0) & (p["s1_share_2024"] < DRY) & (p["s1_share_2025"] < DRY)
    c = p[dry & (p["dist_km"] >= BUFFER) & (p["rel_elev_m"] <= cut)]
    if export is not None:  # sample file in the layout of rq1_2024_sample_sheets.csv.gz (for rq1_round_change.py)
        s = pd.concat([t.assign(group="treated"), c.assign(group="control")])
        s[LC_COLS] = landcover(s)
        s["flood2024_share"] = np.nan
        s[KEY + ["lon0", "lat0", "lon1", "lat1", "series_sheet", "group", "n_parcels", "mean_logp", "elev_m",
           "rel_elev_m"] + LC_COLS + ["s1_share_2024", "s1_share_2025", "flood2024_share", "dist_km"]].to_csv(export, index=False)
    m = mde_table(pd.concat([c, t]), label)
    m = m[m["icc_changes"] == 0.2].iloc[0]
    counts = t.groupby("province").size().sort_values(ascending=False)
    return {"sample": label, "provinces": len(provs),
            "province_counts": "; ".join(f"{k} {v}" for k, v in counts.items()),
            "treated": int(m["treated"]), "controls": int(m["control_sheets"]), "clusters": int(m["clusters"]),
            "mixed_clusters": int(m["mixed_clusters"]), "mde_sd0.10": m["mde_sd0.10"],
            "mde_sd0.20": m["mde_sd0.20"], "mde_carryover_pp": m["mde_carryover_pp"]}


def main() -> None:
    d = pd.read_csv(S1, dtype={"UTMMAP1": str, "UTMMAP3": str, "UTMMAP4": str, "prov_code": str},
                    keep_default_na=False, na_values=[""])
    box_px = (d["lon1"] - d["lon0"]) * (d["lat1"] - d["lat0"]) / RES ** 2
    d = d[(d["s1_valid_px_2024"] >= MIN_VALID * box_px) & (d["s1_valid_px_2025"] >= MIN_VALID * box_px)
          & d["mean_logp"].notna()].copy()
    t2024 = (d["s1_share_2024"] > THRESH) & (d["s1_share_2025"] <= THRESH)
    t2025 = (d["s1_share_2025"] > THRESH) & (d["s1_share_2024"] < DRY)
    rows = [build(d, t2024, k, f"2024 event, provinces with >= {k} treated") for k in (20, 25, 30)]
    rows.append(build(d, t2025, 25, "2025 event (dry in 2024), provinces with >= 25 treated", export=SAMPLE_2025))
    out = pd.DataFrame(rows)
    write(out, "rq1_sample_sensitivity",
          "RQ1 sample sensitivity: hazard-comparable controls at 5 km; MDE at ICC 0.2, 80% power, 5% two-sided.")
    print(out.drop(columns="province_counts").round(3).to_string(index=False))
    for r in rows:
        print(r["sample"], "|", r["province_counts"])


if __name__ == "__main__":
    main()

"""Why does the placebo-footprint test over-reject on synthetic null rounds?

The extended Monte Carlo (rq1_montecarlo_extended.py) finds that the registered placebo-footprint test
rejects a true null about 20% of the time at the 5% level, while the wild cluster bootstrap rejects about
5%. This script compares, on a few synthetic null rounds, the distribution of placebo estimates with the
sampling distribution of the actual estimate: the standard deviation of the placebo draws, the Kish
effective number of controls behind each placebo estimate and the number of 1:50,000 clusters the placebo
footprint covers, against the same quantities for the real treated footprint. If placebo footprints land
on better-overlapped, less clustered sheets than the real treated sheets, their estimates are less
dispersed than the actual estimate under the null, and the test over-rejects.

Run   : .venv/bin/python -I 04_analysis/src/rq1_placebo_diagnostic.py [--draws 3] [--footprints 200]
Writes: 04_analysis/outputs/tables/rq1_placebo_diagnostic.csv / .md
Not results: synthetic rounds only.
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I drops the script directory
import rq1_round_change as r  # noqa: E402

CLUSTER = "series_sheet"  # 1:50,000 sheet, the inference cluster


def ess(w):
    w = np.asarray(w, float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def describe(d, w, cluster):
    c = d["T"] == 0
    return {"ess_controls": ess(w[c.to_numpy()]), "treated_sheets": int(d["T"].sum()),
            "treated_clusters": int(d.loc[d["T"] == 1, cluster].nunique()) if cluster else np.nan}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--draws", type=int, default=3, help="synthetic null rounds")
    ap.add_argument("--footprints", type=int, default=200, help="placebo footprints per round")
    a = ap.parse_args()
    sample = r.load_sample(r.SAMPLES["2024"])
    cluster = CLUSTER
    pre = r.load_parcels(r.PRE, set(sample["province"])).merge(sample[r.SHEET], on=r.SHEET)
    rows = []
    for k in range(a.draws):
        rng = np.random.default_rng(r.SEED + 7919 * (k + 1))  # as the extended Monte Carlo, null effect
        units = r.unit_changes(pre, r.synthetic_post(pre, sample, 0.0, rng))
        sh = sample.merge(r.sheet_outcomes(units), on=r.SHEET, how="left")
        d = sh[sh["dlog"].notna()].reset_index(drop=True)
        w = r.balance_weights(d)
        actual = r.estimate(d, w)
        real = describe(d, w, cluster)
        prng = np.random.default_rng(r.SEED + k)
        ests, esss, ncl = [], [], []
        for _ in range(a.footprints):
            p = r.placebo_assignment(d, prng)
            pw = r.balance_weights(p)
            ests.append(r.estimate(p, pw)["estimate"])
            dd = describe(p, pw, cluster)
            esss.append(dd["ess_controls"])
            ncl.append(dd["treated_clusters"])
        ests = np.array(ests)
        rows.append({"draw": k, "actual_estimate": actual["estimate"], "actual_cluster_se": actual["se"],
                     "actual_ess_controls": real["ess_controls"], "actual_treated_clusters": real["treated_clusters"],
                     "placebo_footprints": a.footprints, "placebo_sd": ests.std(ddof=1),
                     "placebo_mean": ests.mean(), "placebo_mean_ess_controls": float(np.mean(esss)),
                     "placebo_mean_treated_clusters": float(np.nanmean(ncl)),
                     "ri_p": float((1 + (np.abs(ests) >= abs(actual["estimate"])).sum()) / (1 + a.footprints))})
        print(rows[-1])
    out = pd.DataFrame(rows)
    out.to_csv(r.TAB / "rq1_placebo_diagnostic.csv", index=False)
    (r.TAB / "rq1_placebo_diagnostic.md").write_text(
        "<!-- Synthetic null rounds; placebo-footprint dispersion against the actual estimate's. "
        "Compare placebo_sd with the sampling SD of the actual estimate in rq1_montecarlo_extended.csv "
        "(sd_estimate, null row). Not results. -->\n\n" + out.round(4).to_markdown(index=False) + "\n",
        encoding="utf-8")
    print(out.round(4).to_string(index=False))


if __name__ == "__main__":
    main()

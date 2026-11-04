"""Extended Monte Carlo for the registered RQ1 estimator, 2024 radar sample (paper referee round 1, M6).

The registered Monte Carlo (rq1_round_change.monte_carlo) uses 100 replications and evaluates the wild
cluster bootstrap only. This script, on the same synthetic next rounds (rq1_round_change.synthetic_post,
same seeds for the first 100 draws), records for each replication and each planted effect:
- the primary estimate, its CR1 cluster standard error and the wild cluster bootstrap p-value
  (999 draws, Rademacher, restricted);
- the placebo-footprint randomisation p-value (the registered primary p-value), on the first
  `--ri-reps` replications with `--ri-draws` placebo footprints each (the registered test uses 1,000);
- the H1a interaction (treated x height above valley floor), its CR1 standard error and t-statistic;
- the Lee bounds on the moved-unit change (point bounds, no bootstrap) and the naive moved-unit
  difference, as in rq1_lee_bounds.

Summary rows per planted effect: mean and SD of the estimate, mean cluster SE, rejection rates at 5%
of the bootstrap and of the placebo-footprint test, the share of replications in which |t| of the
interaction exceeds 1.96 and in which the Lee bounds exclude zero. Synthetic data: not results.

Output: 04_analysis/outputs/tables/rq1_montecarlo_extended.csv (summary) and
        04_analysis/outputs/tables/rq1_montecarlo_extended_draws.csv (one row per replication)
Run   : .venv/bin/python -I 04_analysis/src/rq1_montecarlo_extended.py [--reps 1000] [--ri-reps 200] [--ri-draws 500] [--workers 16]
"""

import argparse
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I drops the script directory
import rq1_round_change as r  # noqa: E402
import rq1_lee_bounds as lb  # noqa: E402

TAB = r.TAB
_G = {}


def _init():
    sample = r.load_sample(r.SAMPLES["2024"])
    pre = r.load_parcels(r.PRE, set(sample["province"])).merge(sample[r.SHEET], on=r.SHEET)
    _G["sample"], _G["pre"] = sample, pre


def one(args):
    k, effect, ri_draws = args
    sample, pre = _G["sample"], _G["pre"]
    rng = np.random.default_rng(r.SEED + 7919 * (k + 1) + int(round(-effect * 1000)))  # as monte_carlo()
    units = r.unit_changes(pre, r.synthetic_post(pre, sample, effect, rng))
    sh = sample.merge(r.sheet_outcomes(units), on=r.SHEET, how="left")
    d = sh[sh["dlog"].notna()].reset_index(drop=True)
    w = r.balance_weights(d)
    e = r.estimate(d, w)
    inter = r.estimate(d, w, interaction=True)
    row = {"replication": k, "planted_effect": effect, "estimate": e["estimate"], "se": e["se"],
           "wcb_p": r.wild_cluster_p(d, w, n_boot=999, seed=r.SEED + k),
           "interaction": inter["interaction"], "interaction_se": inter["interaction_se"],
           "sheets_treated": int(d["T"].sum()), "sheets_control": int((d["T"] == 0).sum())}
    if ri_draws:
        try:
            row["ri_p"] = r.randomisation_p(d, e["estimate"], n=ri_draws, seed=r.SEED + k)[0]
        except ValueError:
            row["ri_p"] = np.nan
    u = lb.units_table(units, d, w)
    keep = [pr for pr, g in u.groupby("province") if lb.usable(g)]
    pw = u[u["T"] == 1].drop_duplicates(r.SHEET).groupby("province").size().reindex(keep)
    b, _ = lb.bounds(u, pw)
    if b is not None:
        row |= {"lee_naive": b["naive"], "lee_lower": b["lower"], "lee_upper": b["upper"], "lee_trim": b["trim_share"]}
    return row


def summarise(draws):
    rows = []
    for effect, g in draws.groupby("planted_effect", sort=False):
        t = g["interaction"] / g["interaction_se"]
        ri = g["ri_p"].dropna() if "ri_p" in g else pd.Series(dtype=float)
        lee_ok = g[["lee_lower", "lee_upper"]].dropna()
        rows.append({"planted_effect": effect, "expected_sheet_effect": effect * 0.7, "replications": len(g),
                     "mean_estimate": g["estimate"].mean(), "sd_estimate": g["estimate"].std(ddof=1),
                     "mean_cluster_se": g["se"].mean(), "rejection_rate_wcb_5pct": (g["wcb_p"] < 0.05).mean(),
                     "ri_replications": len(ri), "rejection_rate_ri_5pct": (ri < 0.05).mean() if len(ri) else np.nan,
                     "mean_interaction": g["interaction"].mean(), "sd_interaction": g["interaction"].std(ddof=1),
                     "mean_interaction_se": g["interaction_se"].mean(), "share_interaction_t_above_196": (t.abs() > 1.96).mean(),
                     "lee_replications": len(lee_ok), "mean_lee_lower": lee_ok["lee_lower"].mean(),
                     "mean_lee_upper": lee_ok["lee_upper"].mean(),
                     "share_lee_excludes_zero": ((lee_ok["lee_lower"] > 0) | (lee_ok["lee_upper"] < 0)).mean(),
                     "mean_lee_naive": g["lee_naive"].mean()})
    return pd.DataFrame(rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=1000)
    ap.add_argument("--ri-reps", type=int, default=200, help="replications that also run the placebo-footprint test")
    ap.add_argument("--ri-draws", type=int, default=500, help="placebo footprints per replication")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--effects", default="0.0,-0.05")
    a = ap.parse_args()
    effects = [float(x) for x in a.effects.split(",")]
    jobs = [(k, e, a.ri_draws if k < a.ri_reps else 0) for e in effects for k in range(a.reps)]
    with Pool(a.workers, initializer=_init) as pool:
        rows = []
        for i, row in enumerate(pool.imap_unordered(one, jobs, chunksize=4), 1):
            rows.append(row)
            if i % 50 == 0:
                print(f"{i}/{len(jobs)}", flush=True)
    draws = pd.DataFrame(rows).sort_values(["planted_effect", "replication"], ascending=[False, True])
    out = summarise(draws)
    TAB.mkdir(parents=True, exist_ok=True)
    draws.to_csv(TAB / "rq1_montecarlo_extended_draws.csv", index=False)
    r.write(out, "rq1_montecarlo_extended",
            f"Extended Monte Carlo of the registered RQ1 estimator, 2024 radar sample: {a.reps} synthetic next rounds per "
            f"planted effect (rq1_round_change.synthetic_post); wild cluster bootstrap 999 draws; placebo-footprint test on "
            f"the first {a.ri_reps} replications with {a.ri_draws} footprints each; H1a interaction t-statistics; Lee point "
            "bounds. Synthetic data: not results. Author's calculations")
    print(out.round(4).to_string(index=False))


if __name__ == "__main__":
    main()

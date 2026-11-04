"""Monte Carlo of candidate repairs to the placebo-footprint test (2024 radar sample).

The extended Monte Carlo (rq1_montecarlo_extended.py) found the registered placebo-footprint test rejecting a
true null about 20% of the time, and rq1_placebo_diagnostic.py showed why: shifted footprints land on controls
in the middle of the covariate support, so they are balanced against about 500 effective controls where the
real footprint has about 100, and the placebo estimates are too precise. This script tests, on the same
synthetic next rounds, two repairs and their combination:

1. Restricted pool. A logit of treatment on the balancing variables (BAL) with province fixed effects is fitted
   on the estimation sample. In each province the eligible placebo sheets are the controls within the treated
   height range whose fitted propensity is at least the q-th percentile of that province's treated sheets'
   propensities, with q the largest of 25, 10, 5 (then no restriction) that leaves at least twice as many
   eligible sheets as treated sheets. Footprints are then shifted and snapped exactly as in the registered rule.
   A strict variant starts the ladder at the median and accepts 1.5 times the treated count.
2. Studentised comparison. The p-value compares |estimate / CR1 cluster SE| rather than |estimate|, so that a
   placebo estimated with more precision is not counted as a large draw.

For each replication and planted effect: the actual estimate, SE and bootstrap p; placebo draws under the
registered and the restricted pool; p-values for the four combinations (pool x studentised); the SD of the placebo
estimates, their mean effective controls and mean cluster count under each pool. Summary: rejection rates at 5%
per variant, placebo dispersion against the actual estimate's sampling SD. Synthetic data: not results.

Output: 04_analysis/outputs/tables/rq1_placebo_restricted_mc.csv (summary),
        04_analysis/outputs/tables/rq1_placebo_restricted_mc_draws.csv (per replication)
Run   : .venv/bin/python -I 04_analysis/src/rq1_placebo_restricted_mc.py [--reps 200] [--footprints 150] [--workers 16]
"""

import argparse
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I drops the script directory
import rq1_round_change as r  # noqa: E402

TAB = r.TAB
QUANTILES = (0.25, 0.10, 0.05, 0.0)
_G = {}


def propensity(d, cols=r.BAL, ridge=1e-6, iters=50):
    """Fitted P(T=1 | standardised BAL, province) from a logit by Newton's method; returns a Series on d.index."""
    X = d[cols].astype(float)
    X = (X - X.mean()) / X.std().replace(0, 1.0)
    P = pd.get_dummies(d["province"]).astype(float)
    Xm = np.column_stack([X.to_numpy(), P.to_numpy()])
    y = d["T"].to_numpy(float)
    b = np.zeros(Xm.shape[1])
    for _ in range(iters):
        p = 1 / (1 + np.exp(-Xm @ b))
        H = (Xm * (p * (1 - p))[:, None]).T @ Xm + ridge * np.eye(len(b))
        step = np.linalg.solve(H, Xm.T @ (y - p))
        b += step
        if np.abs(step).max() < 1e-8:
            break
    return pd.Series(1 / (1 + np.exp(-Xm @ b)), index=d.index)


def restricted_pool(d, quantiles=QUANTILES, factor=2.0, ps=None):
    """Eligible placebo sheets under the restricted rule, with the quantile used per province.

    `factor`: the least ratio of eligible sheets to treated sheets a province must keep (the registered rule
    requires 2; the strict variant accepts 1.5 and starts its ladder at the median).
    """
    ps = propensity(d) if ps is None else ps
    t, c = d[d["T"] == 1], d[d["T"] == 0]
    lo, hi = t["rel_elev_m"].min(), t["rel_elev_m"].max()
    elig = c[(c["rel_elev_m"] >= lo) & (c["rel_elev_m"] <= hi)]
    keep, used = [], {}
    for pr, tp in t.groupby("province"):
        pool = elig[elig["province"] == pr]
        for q in quantiles:
            sub = pool[ps[pool.index] >= ps[tp.index].quantile(q)] if q > 0 else pool
            if len(sub) >= factor * len(tp):
                break
        keep.append(sub)
        used[pr] = q
    return pd.concat(keep), used


def ess(w):
    w = np.asarray(w, float)
    return float(w.sum() ** 2 / (w ** 2).sum())


def draws(d, rng, n, elig, min_ratio=2.0):
    est, se, es, cl = np.empty(n), np.empty(n), np.empty(n), np.empty(n)
    for i in range(n):
        p = r.placebo_assignment(d, rng, elig, min_ratio)
        pw = r.balance_weights(p)
        e = r.estimate(p, pw)
        est[i], se[i] = e["estimate"], e["se"]
        es[i] = ess(pw[p["T"] == 0].to_numpy())
        cl[i] = p.loc[p["T"] == 1, "series_sheet"].nunique()
    return est, se, es, cl


def pval(draw_stat, actual_stat):
    return float((1 + (np.abs(draw_stat) >= abs(actual_stat)).sum()) / (1 + len(draw_stat)))


def _init():
    sample = r.load_sample(r.SAMPLES["2024"])
    pre = r.load_parcels(r.PRE, set(sample["province"])).merge(sample[r.SHEET], on=r.SHEET)
    _G["sample"], _G["pre"] = sample, pre


def one(args):
    k, effect, n = args
    sample, pre = _G["sample"], _G["pre"]
    rng = np.random.default_rng(r.SEED + 7919 * (k + 1) + int(round(-effect * 1000)))  # as rq1_montecarlo_extended
    units = r.unit_changes(pre, r.synthetic_post(pre, sample, effect, rng))
    sh = sample.merge(r.sheet_outcomes(units), on=r.SHEET, how="left")
    d = sh[sh["dlog"].notna()].reset_index(drop=True)
    w = r.balance_weights(d)
    e = r.estimate(d, w)
    t_act = e["estimate"] / e["se"]
    row = {"replication": k, "planted_effect": effect, "estimate": e["estimate"], "se": e["se"],
           "actual_ess": ess(w[d["T"] == 0].to_numpy()),
           "wcb_p": r.wild_cluster_p(d, w, n_boot=999, seed=r.SEED + k)}
    ps = propensity(d)
    pool, used = restricted_pool(d, ps=ps)
    strict, used_s = restricted_pool(d, quantiles=(0.5,) + QUANTILES, factor=1.5, ps=ps)
    row["restricted_pool"], row["strict_pool"] = len(pool), len(strict)
    row |= {f"q_{pr}": q for pr, q in used.items()}
    row |= {f"qs_{pr}": q for pr, q in used_s.items()}
    for name, elig, ratio in (("reg", None, 2.0), ("res", pool, 2.0), ("str", strict, 1.5)):
        est, se, es, cl = draws(d, np.random.default_rng(r.SEED + k), n, elig, ratio)
        row |= {f"{name}_p": pval(est, e["estimate"]), f"{name}_t_p": pval(est / se, t_act),
                f"{name}_sd": est.std(ddof=1), f"{name}_t_sd": (est / se).std(ddof=1), f"{name}_mean": est.mean(),
                f"{name}_ess": es.mean(), f"{name}_clusters": cl.mean(), f"{name}_se": se.mean()}
    return row


def summarise(dr):
    out = []
    for eff, g in dr.groupby("planted_effect", sort=False):
        row = {"planted_effect": eff, "expected_sheet_effect": 0.7 * eff, "replications": len(g),
               "mean_estimate": g.estimate.mean(), "sd_estimate": g.estimate.std(ddof=1), "mean_cluster_se": g.se.mean(),
               "mean_t_sd": (g.estimate / g.se).std(ddof=1), "actual_ess": g.actual_ess.mean(),
               "rejection_rate_wcb_5pct": (g.wcb_p < 0.05).mean()}
        for name in ("reg", "res", "str"):
            row |= {f"rejection_rate_{name}_5pct": (g[f"{name}_p"] < 0.05).mean(),
                    f"rejection_rate_{name}_t_5pct": (g[f"{name}_t_p"] < 0.05).mean(),
                    f"{name}_placebo_sd": g[f"{name}_sd"].mean(), f"{name}_placebo_t_sd": g[f"{name}_t_sd"].mean(),
                    f"{name}_placebo_ess": g[f"{name}_ess"].mean(), f"{name}_placebo_clusters": g[f"{name}_clusters"].mean(),
                    f"{name}_placebo_se": g[f"{name}_se"].mean()}
        row["restricted_pool"], row["strict_pool"] = g.restricted_pool.mean(), g.strict_pool.mean()
        out.append(row)
    return pd.DataFrame(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=200)
    ap.add_argument("--footprints", type=int, default=150, help="placebo footprints per rule and replication")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--effects", default="0.0,-0.05")
    ap.add_argument("--tag", default="", help="suffix for a smoke-test output")
    a = ap.parse_args()
    effects = [float(x) for x in a.effects.split(",")]
    jobs = [(k, e, a.footprints) for e in effects for k in range(a.reps)]
    with Pool(a.workers, initializer=_init) as pool:
        rows = []
        for i, row in enumerate(pool.imap_unordered(one, jobs, chunksize=2), 1):
            rows.append(row)
            if i % 20 == 0 or i == len(jobs):
                print(f"{i}/{len(jobs)}", flush=True)
    dr = pd.DataFrame(rows).sort_values(["planted_effect", "replication"], ascending=[False, True])
    out = summarise(dr)
    TAB.mkdir(parents=True, exist_ok=True)
    dr.to_csv(TAB / f"rq1_placebo_restricted_mc_draws{a.tag}.csv", index=False)
    r.write(out, f"rq1_placebo_restricted_mc{a.tag}",
            f"Monte Carlo of repairs to the placebo-footprint test, 2024 radar sample: {a.reps} synthetic next rounds per "
            f"planted effect (same draws as rq1_montecarlo_extended), {a.footprints} footprints per rule; reg = registered "
            "pool, res = propensity-restricted pool (ladder 25/10/5, 2x), str = strict pool (ladder 50/25/10/5, 1.5x), "
            "_t = studentised comparison. Synthetic data: not results. "
            "Author's calculations")
    print(out.round(4).T.to_string())


if __name__ == "__main__":
    main()

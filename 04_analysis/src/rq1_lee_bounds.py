"""RQ1 secondary outcome: change among land units whose value moved, with Lee (2009) bounds (PAP section 1).

Carry-over (H1b) can itself respond to the flood, so comparing moved units across groups mixes the
effect on values with a change in which units move. Lee (2009) bounds trim the group whose units
move more often, by the excess share, from the top (lower bound) or the bottom (upper bound) of its
outcome distribution. Monotonicity is assumed: the flood moves units in one direction only.

Rules (registered with rq1_round_change.py):
- Units are pseudo land units present in R1 (rq1_round_change.unit_changes); a unit moved if any
  present parcel changed value (carried == 0); the outcome is its dlog.
- Unit weight = the sheet's registered balancing weight (treated 1) / the sheet's present units, so
  each sheet counts once, as in the primary outcome.
- Bounds are computed within each province (Lee 2009, section 4: trimming within cells of a
  discrete covariate tightens the bounds) and averaged with weights equal to the province's treated
  sheets. Trimming of the boundary unit is fractional (weighted quantiles).
- A province enters only if both groups have moved units in it; skipped provinces are reported.
- Interval: cluster bootstrap over whole 1:50,000 sheets (a cluster spanning two provinces moves
  as one, assigned to the province holding most of its sheets), resampled within that province and
  within stratum (clusters holding treated sheets / control-only clusters), sheet and province weights held at the
  point estimate, 999 draws; reported as the 2.5th percentile of the lower bound and the 97.5th of
  the upper bound. Draws in which a province loses its moved units in a group are counted and dropped.
- Also reported: the untrimmed (naive) moved-unit difference and the moving shares by group.

Output: 04_analysis/outputs/tables/rq1_lee_bounds[_synthetic].{csv,md}
Run: .venv/bin/python -I 04_analysis/src/rq1_lee_bounds.py [--post DIR] [--event 2024|unosat|2025]
"""

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rq1_round_change as r  # noqa: E402

N_BOOT_LEE = 999


def trimmed_mean(y, w, share, top):
    """Weighted mean of y after removing a weight share `share` from the top (or bottom) of y."""
    if share <= 0:
        return np.average(y, weights=w)
    o = np.argsort(-y if top else y, kind="mergesort")
    y, w = y[o], w[o]
    cut = share * w.sum()
    before = np.concatenate([[0.0], np.cumsum(w)[:-1]])
    keep = np.clip(w - np.clip(cut - before, 0, None), 0, None)  # fractional trim of the boundary unit
    return np.average(y, weights=keep)


def province_bounds(u):
    """Lee bounds for one province's unit table (columns T, moved, dlog, wu)."""
    q = {g: np.average(u.loc[u["T"] == g, "moved"], weights=u.loc[u["T"] == g, "wu"]) for g in (0, 1)}
    m = u[u["moved"] == 1]
    yt, wt = m.loc[m["T"] == 1, "dlog"].to_numpy(), m.loc[m["T"] == 1, "wu"].to_numpy()
    yc, wc = m.loc[m["T"] == 0, "dlog"].to_numpy(), m.loc[m["T"] == 0, "wu"].to_numpy()
    naive = np.average(yt, weights=wt) - np.average(yc, weights=wc)
    if q[1] >= q[0]:
        p = 1 - q[0] / q[1]
        lo = trimmed_mean(yt, wt, p, top=True) - np.average(yc, weights=wc)
        hi = trimmed_mean(yt, wt, p, top=False) - np.average(yc, weights=wc)
    else:
        p = 1 - q[1] / q[0]
        mt = np.average(yt, weights=wt)
        lo = mt - trimmed_mean(yc, wc, p, top=False)
        hi = mt - trimmed_mean(yc, wc, p, top=True)
    return {"naive": naive, "lower": lo, "upper": hi, "trim_share": p, "moved_treated": q[1], "moved_control": q[0]}


def units_table(units, d, w):
    """Present units of the analysed sheets with treatment, cluster and unit weights."""
    s = d[r.SHEET + ["T", "series_sheet"]].assign(w=w.to_numpy())
    u = units[units["n_present"] > 0].merge(s, on=r.SHEET)
    u["moved"] = 1 - u["carried"]
    u["wu"] = u["w"] / u.groupby(r.SHEET)["p"].transform("size")
    return u


def usable(g):
    """A province enters the bounds only if both groups have moved units in it."""
    return bool(((g["T"] == 1) & (g["moved"] == 1)).any() and ((g["T"] == 0) & (g["moved"] == 1)).any())


def bounds(u, pw):
    """Province bounds averaged with fixed province weights pw (treated sheets at the point estimate)."""
    rows = {pr: province_bounds(g) for pr, g in u.groupby("province") if pr in pw.index and usable(g)}
    if not rows:
        return None, rows
    out = {k: float(np.average([rows[p][k] for p in rows], weights=pw.reindex(list(rows)))) for k in
           next(iter(rows.values()))}
    return out, rows


def lee(units, d, w, n_boot=N_BOOT_LEE, seed=r.SEED):
    """Pooled bounds, bootstrap interval and per-province detail."""
    u = units_table(units, d, w)
    keep = [pr for pr, g in u.groupby("province") if usable(g)]
    skipped = sorted(set(u["province"]) - set(keep))
    pw = u[u["T"] == 1].drop_duplicates(r.SHEET).groupby("province").size().reindex(keep)
    est, rows = bounds(u, pw)
    if est is None:
        raise SystemExit("no province has moved units in both groups")
    rng = np.random.default_rng(seed)
    # resample whole 1:50,000 clusters (all their provinces' rows) within the province holding most of
    # the cluster's sheets and within stratum (holding treated sheets / control-only), so every draw
    # keeps both groups in every usable province; sheet and province weights stay fixed
    sh = u.drop_duplicates(r.SHEET)
    home = sh.groupby("series_sheet")["province"].agg(lambda x: x.value_counts().sort_index().idxmax())
    has_t = sh.groupby("series_sheet")["T"].max()
    rows_of = u.groupby("series_sheet").indices
    strata = {}
    for c in rows_of:
        strata.setdefault((home[c], has_t[c]), []).append(rows_of[c])
    lo, hi, failed = [], [], 0
    for _ in range(n_boot):
        take = [cls[i] for cls in strata.values() for i in rng.integers(0, len(cls), len(cls))]
        b, br = bounds(u.iloc[np.concatenate(take)], pw)
        if b is None or len(br) < len(keep):        # a draw without moved units in a group
            failed += 1
            continue
        lo.append(b["lower"])
        hi.append(b["upper"])
    est["ci_low"], est["ci_high"] = float(np.quantile(lo, 0.025)), float(np.quantile(hi, 0.975))
    est["boot_draws_failed"] = failed
    est["provinces_skipped"] = "+".join(skipped)
    est["units_moved"] = int(u["moved"].sum())
    est["units_present"] = len(u)
    return est, pd.DataFrame(rows).T.rename_axis("province").reset_index()


def run(sample, post, n_boot=N_BOOT_LEE, real=False):
    """real: `post` returns the real R1, so the matching stop (PAP section 5) applies."""
    pre = r.load_parcels(r.PRE, set(sample["province"])).merge(sample[r.SHEET], on=r.SHEET)
    units = r.unit_changes(pre, post(pre, sample))
    sh = sample.merge(r.sheet_outcomes(units), on=r.SHEET, how="left")
    if real:
        r.check_matching(sh, "Lee bounds")
    d = sh[sh["dlog"].notna()].reset_index(drop=True)
    return lee(units, d, r.balance_weights(d), n_boot=n_boot)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--post", help="folder with the first post-flood round")
    ap.add_argument("--event", choices=list(r.SAMPLES), default="2024")
    ap.add_argument("--provinces", help="comma-separated province subset (PAP section 9, timing by province)")
    args = ap.parse_args()
    sample = r.load_sample(r.SAMPLES[args.event])
    sfx = ""
    if args.provinces:
        keep = sorted({x.strip() for x in args.provinces.split(",") if x.strip()})
        if set(keep) - set(sample["province"]):
            raise SystemExit(f"--provinces: {sorted(set(keep) - set(sample['province']))} not in the {args.event} sample")
        sample = sample[sample["province"].isin(keep)].reset_index(drop=True)
        sfx = "_prov-" + "-".join(keep)
    rows, detail = [], []
    if args.post:
        e, dt = run(sample, lambda pre, s: r.load_post(args.post, pre)[0], real=True)
        rows.append({"sample": args.event, **e})
        detail.append(dt.assign(sample=args.event))
        name, note = f"rq1_lee_bounds{r.TAGS[args.event]}{sfx}", "RQ1 secondary (pre-registered)"
    else:
        for effect, carry_t in ((-0.05, 0.3), (-0.05, 0.2), (0.0, 0.3)):
            rng = np.random.default_rng(r.SEED + 60 + int(round(-effect * 1000)) + int(carry_t * 100))

            def post(pre, s, effect=effect, carry_t=carry_t, rng=rng):
                if carry_t == 0.3:
                    return r.synthetic_post(pre, s, effect, rng)
                # treated units carried over less often: 20% carry-over everywhere, then 1/8 of the
                # remaining control units restored to their old value (controls about 30%)
                p = r.synthetic_post(pre, s, effect, rng, carry=carry_t)
                m = p.merge(pre.rename(columns={"p": "p0"}), on=r.SHEET + ["LAND_NO"], how="left")
                m = m.merge(s[r.SHEET + ["T"]], on=r.SHEET)
                unit = m.groupby(r.SHEET + ["p0"], dropna=False).ngroup().to_numpy()
                draw = rng.random(unit.max() + 1)[unit]
                back = (m["T"] == 0).to_numpy() & m["p0"].notna().to_numpy() & (draw < 0.125)
                m.loc[back, "p"] = m.loc[back, "p0"]
                return m[r.SHEET + ["LAND_NO", "p"]]
            e, dt = run(sample, post)
            rows.append({"sample": args.event, "planted_effect": effect, "carry_treated": carry_t, **e})
            detail.append(dt.assign(planted_effect=effect, carry_treated=carry_t))
        name = f"rq1_lee_bounds{r.TAGS[args.event]}{sfx}_synthetic"
        note = ("Synthetic check of the Lee bounds code: one synthetic R1 per row (rq1_round_change.synthetic_post; "
                "planted effect on changed units, 30% of units carried over). Not results")
    out = pd.DataFrame(rows)
    r.write(out, name, note + f", {args.event} sample: change in log value among units whose value moved, "
            "Lee (2009) bounds within province, cluster-bootstrap interval (999 draws). Author's calculations.")
    r.write(pd.concat(detail, ignore_index=True), name + "_provinces", note + ": bounds by province.")
    print(out.round(4).to_string(index=False))


if __name__ == "__main__":
    main()

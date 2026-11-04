"""RQ3: reverse stress test over a scalar flood severity S (identification.md, framework.md section 5).

Scenario: the 2011 footprint scaled by S, so region r's flood intensity is I_r(S) = min(1, S x_r),
with x_r the exposure-weighted 2011 flood share (S = 1 is the 2011 event).
    PD_r(S)  = min(1, pd0 + beta_pd I_r(S))
    LGD_r(S) = max(0, 1 - (1 - c) V_post / EAD),  V_post / EAD = (1 - delta h_r)(1 - phi I_r) / (ltv_r (1 - lam delta h_r))
    L(S)     = EAD sum_r w_r PD_r(S) LGD_r(S)
    CET1(S)  = (K0 - L(S)) / RWA
    S*       = inf{S : CET1(S) < kappa}, by bisection after a monotonicity check.
A portfolio `p` is a dict of region arrays (w, x, h, ltv) and scalars. All functions are pure.
Capital figures in BASE are illustrative, not calibrated to any bank.
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

# kappa: CET1 minimum 4.5% + conservation buffer 2.5% (BOT Notification 12/2555); D-SIBs 8% (16/2560).
BASE = {"pd0": 0.02, "ead": 1.0, "rwa": 0.6, "k0": 0.096, "kappa": 0.07}


def intensity(S, x):
    return np.clip(S * np.asarray(x), 0.0, 1.0)


def pd_r(S, p):
    return np.clip(p["pd0"] + p["beta_pd"] * intensity(S, p["x"]), 0.0, 1.0)


def lgd_r(S, p):
    dh = p["delta"] * np.asarray(p["h"])
    v_over_ead = (1 - dh) * (1 - p["phi"] * intensity(S, p["x"])) / (np.asarray(p["ltv"]) * (1 - p["lam"] * dh))
    return np.clip(1 - (1 - p["haircut"]) * v_over_ead, 0.0, 1.0)


def loss(S, p):
    return p["ead"] * float(np.sum(np.asarray(p["w"]) * pd_r(S, p) * lgd_r(S, p)))


def cet1(S, p):
    return (p["k0"] - loss(S, p)) / p["rwa"]


def check_monotone(p, s_max=10.0, n=401):
    """Raise if CET1(S) increases anywhere on a grid over [0, s_max]."""
    c = np.array([cet1(s, p) for s in np.linspace(0, s_max, n)])
    if np.any(np.diff(c) > 1e-12):
        raise ValueError("CET1(S) is not monotone decreasing; S* is not unique")


def s_star(p, s_max=10.0, tol=1e-10):
    """Breaking point S* = inf{S : CET1(S) < kappa}; 0 if already breached, inf if never in [0, s_max]."""
    check_monotone(p, s_max)
    if cet1(0.0, p) < p["kappa"]:
        return 0.0
    if cet1(s_max, p) >= p["kappa"]:
        return np.inf
    lo, hi = 0.0, s_max
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        lo, hi = (lo, mid) if cet1(mid, p) < p["kappa"] else (mid, hi)
    return hi


def concentrate(p, theta):
    """Move a share theta of exposure into the most flood-exposed region."""
    top = np.eye(len(p["w"]))[int(np.argmax(p["x"]))]
    return {**p, "w": (1 - theta) * np.asarray(p["w"]) + theta * top}


def draw_s_star(p, n, seed, beta_se, lam_range):
    """Distribution of S* from draws of beta_pd ~ N(beta_pd, beta_se) truncated at 0 and lam ~ U(lam_range)."""
    rng = np.random.default_rng(seed)
    betas = np.maximum(rng.normal(p["beta_pd"], beta_se, n), 0.0)
    lams = rng.uniform(*lam_range, n)
    return np.array([s_star({**p, "beta_pd": b, "lam": lam}) for b, lam in zip(betas, lams)])


def regions_from_panel(d: pd.DataFrame, pre: str = "2011-09") -> dict:
    """Province-level exposure shares, 2011 flood exposure, hazard and book LTV from a prepared panel."""
    g = d[d["month"] == pre].assign(ltv=lambda x: x["balance_thb"] / x["collateral_value_thb"])
    bal = g.groupby("province_code")["balance_thb"].sum()
    wavg = lambda c: (g[c] * g["balance_thb"]).groupby(g["province_code"]).sum() / bal  # noqa: E731
    return {"w": (bal / bal.sum()).to_numpy(), "x": wavg("flood").to_numpy(),
            "h": wavg("hazard").to_numpy(), "ltv": wavg("ltv").to_numpy()}


if __name__ == "__main__":
    import pathlib
    import sys

    sys.path.insert(0, str(pathlib.Path(__file__).parent))  # -I drops the script directory
    import rq2_event_study as rq2

    truth = json.loads((rq2.SYNTH / "loan_panel_synth_true_params.json").read_text())
    d = rq2.prepare(rq2.load_synth())
    est, se = rq2.window_effect(rq2.event_study(d, ["distress"])["distress"], ["F"])
    lgd = {k: truth[k] for k in ["delta", "lam", "phi", "haircut"]}
    p_true = {**BASE, **regions_from_panel(d), **lgd, "beta_pd": 12 * truth["beta_s"]}
    p_hat = {**p_true, "beta_pd": 12 * est}
    draws = draw_s_star(p_hat, 500, seed=1, beta_se=12 * se, lam_range=(0.1, 0.5))
    print(f"beta_s true {truth['beta_s']:.4f}  recovered {est:.4f} (se {se:.4f})")
    print(f"S* true {s_star(p_true):.3f}  recovered {s_star(p_hat):.3f}  "
          f"draws median {np.median(draws):.3f} [5%: {np.percentile(draws, 5):.3f}, 95%: {np.percentile(draws, 95):.3f}]")
    tab = rq2.ROOT / "04_analysis" / "outputs" / "tables"
    tab.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([{"beta_s_true": truth["beta_s"], "beta_s_recovered": est, "beta_s_se": se,
                   "s_star_true": s_star(p_true), "s_star_recovered": s_star(p_hat),
                   "s_star_draws": len(draws), "s_star_median": float(np.median(draws)),
                   "s_star_p05": float(np.percentile(draws, 5)), "s_star_p95": float(np.percentile(draws, 95)),
                   "cet1_before": BASE["k0"] / BASE["rwa"], "kappa": BASE["kappa"], "pd0": BASE["pd0"]}]
                 ).to_csv(tab / "rq3_synthetic_sstar.csv", index=False)  # synthetic data: not results

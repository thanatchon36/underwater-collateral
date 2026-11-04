"""RQ2 Plan A: event study / triple difference on the loan-month panel (identification.md).

    y_it = alpha_i + delta_{d x t} [+ delta_{e x t}] + sum_q beta_q Flood_s * 1[q(t) = q]
           [+ sum_q theta_q Flood_s * e_i * 1[q(t) = q]] + eps_it

q(t) is the event quarter relative to 2011-10 (q = -1 omitted; q <= -4 and q >= 6 binned).
e_i = 1 if the loan was normal or special mention in 2011-09 (eligible for the ว. 1564/2554
classification freeze). Fixed effects are removed by alternating projections; standard errors
are clustered by district. Works on unbalanced panels.
"""
from __future__ import annotations

import json
import pathlib

import numpy as np
import pandas as pd
import scipy.sparse as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
SYNTH = ROOT / "03_data" / "synthetic"
BINS = [q for q in range(-4, 7) if q != -1]
WINDOW = [0, 1, 2, 3]  # 2011-10 .. 2012-09
OUTCOMES = ["default", "restructured", "stage2", "distress"]


def prepare(df: pd.DataFrame, event: str = "2011-10", pre: str = "2011-09",
            event_months: tuple = ("2011-10", "2011-11")) -> pd.DataFrame:
    """Derive outcomes, exposure, eligibility and event quarter from schema fields."""
    d = df.copy()
    ym = pd.to_datetime(d["month"], format="%Y-%m")
    d["t"] = ym.dt.year * 12 + ym.dt.month - 1
    ev = pd.Timestamp(event)
    d["q"] = np.clip(np.floor((d["t"] - (ev.year * 12 + ev.month - 1)) / 3), -4, 6).astype(int)
    d["default"] = (d["dpd"] > 90).astype(float)
    d["restructured"] = d["restructured"].astype(float)
    d["stage2"] = (d["stage"] == 2).astype(float)
    d["distress"] = np.maximum(d["default"], d["restructured"])
    keys = ["utmmap1", "utmmap2", "utmmap3", "utmmap4", "utmscale"]
    d["sheet"] = pd.MultiIndex.from_frame(d[keys].astype(str)).factorize()[0]
    flood = d[d["month"].isin(event_months)].groupby("sheet")["flood_share"].max()
    d["flood"] = d["sheet"].map(flood).fillna(0.0)
    pre_cls = d.loc[d["month"] == pre].set_index("loan_id")["asset_class"]
    d["eligible"] = d["loan_id"].map(pre_cls.isin(["normal", "special_mention"]))
    return d[d["eligible"].notna()].assign(eligible=lambda x: x["eligible"].astype(float))


def design(d: pd.DataFrame, het: str | None = None) -> pd.DataFrame:
    """Event-quarter x exposure regressors (and the triple interaction with `het`)."""
    cols = {f"F:q{q}": d["flood"] * (d["q"] == q) for q in BINS}
    if het:
        cols |= {f"F*{het}:q{q}": d["flood"] * d[het] * (d["q"] == q) for q in BINS}
    return pd.DataFrame(cols, index=d.index).astype(float)


def _fe_codes(d: pd.DataFrame, fe: list) -> list[np.ndarray]:
    return [pd.MultiIndex.from_frame(d[list(f)]).factorize()[0] if isinstance(f, tuple)
            else pd.factorize(d[f])[0] for f in fe]


def demean(M: np.ndarray, codes: list[np.ndarray], tol: float = 1e-10, max_iter: int = 500) -> np.ndarray:
    """Within-transform M on several fixed-effect sets by alternating projections."""
    M = M.astype(float).copy()
    ops = []
    for c in codes:
        G = sp.csr_matrix((np.ones(len(c)), (c, np.arange(len(c)))))
        ops.append((G, c, np.asarray(G.sum(axis=1)).ravel()))
    for _ in range(max_iter):
        delta = 0.0
        for G, c, cnt in ops:
            means = (G @ M) / cnt[:, None]
            M -= means[c]
            delta = max(delta, np.abs(means).max())
        if delta < tol:
            return M
    raise RuntimeError("alternating projections did not converge")


def ols_cluster(X: np.ndarray, y: np.ndarray, cluster: np.ndarray, n_absorbed: int = 0):
    """OLS on demeaned data with CR1 cluster-robust covariance."""
    XtX_inv = np.linalg.inv(X.T @ X)
    b = XtX_inv @ X.T @ y
    u = y - X @ b
    C = sp.csr_matrix((np.ones(len(cluster)), (cluster, np.arange(len(cluster)))))
    S = C @ (X * u[:, None])
    n, k, g = len(y), X.shape[1], S.shape[0]
    adj = g / (g - 1) * (n - 1) / max(n - k - n_absorbed, 1)
    return b, adj * XtX_inv @ S.T @ S @ XtX_inv


def event_study(d: pd.DataFrame, outcomes: list[str], het: str | None = None) -> dict:
    """Estimate the event study for each outcome. Returns {outcome: (coef Series, vcov DataFrame)}."""
    X = design(d, het)
    fe = ["loan_id", ("district_code", "t")] + ([(het, "t")] if het else [])
    codes = _fe_codes(d, fe)
    Z = demean(np.column_stack([X.to_numpy(), d[outcomes].to_numpy()]), codes)
    Xd, cl = Z[:, : X.shape[1]], pd.factorize(d["district_code"])[0]
    out = {}
    for j, y in enumerate(outcomes):
        b, V = ols_cluster(Xd, Z[:, X.shape[1] + j], cl, n_absorbed=len(np.unique(codes[0])))
        out[y] = (pd.Series(b, X.columns), pd.DataFrame(V, X.columns, X.columns))
    return out


def window_effect(res: tuple, terms: list[str], quarters: list[int] = WINDOW) -> tuple[float, float]:
    """Average over `quarters` of the summed coefficients in `terms`; returns (estimate, se)."""
    coef, V = res
    a = pd.Series(0.0, coef.index)
    for t in terms:
        for q in quarters:
            a[f"{t}:q{q}"] += 1 / len(quarters)
    return float(a @ coef), float(np.sqrt(a @ V @ a))


def summary(d: pd.DataFrame) -> pd.DataFrame:
    """Window effects (2011-10 to 2012-09) for the pooled and the triple-difference specifications."""
    pooled = event_study(d, ["distress", "default"])
    triple = event_study(d, ["default", "restructured", "stage2"], het="eligible")
    rows = [("distress, all loans", *window_effect(pooled["distress"], ["F"])),
            ("default, all loans", *window_effect(pooled["default"], ["F"])),
            ("default, ineligible", *window_effect(triple["default"], ["F"]))]
    for y in ["default", "restructured", "stage2"]:
        rows.append((f"{y}, eligible", *window_effect(triple[y], ["F", "F*eligible"])))
    rows.append(("default, censoring gap (eligible - ineligible)", *window_effect(triple["default"], ["F*eligible"])))
    return pd.DataFrame(rows, columns=["effect", "estimate", "se"])


def load_synth() -> pd.DataFrame:
    path = next(p for p in [SYNTH / "loan_panel_synth.parquet", SYNTH / "loan_panel_synth.csv.gz"] if p.exists())
    if path.suffix == ".parquet":
        return pd.read_parquet(path)
    return pd.read_csv(path, dtype={"utmmap1": str, "utmmap3": str, "utmmap4": str})


if __name__ == "__main__":
    truth = json.loads((SYNTH / "loan_panel_synth_true_params.json").read_text())
    print("true beta_s =", truth["beta_s"])
    out = summary(prepare(load_synth()))
    out["true_beta_s"] = truth["beta_s"]
    print(out.round(4).to_string(index=False))
    tab = ROOT / "04_analysis" / "outputs" / "tables"
    tab.mkdir(parents=True, exist_ok=True)
    out.to_csv(tab / "rq2_synthetic_recovery.csv", index=False)  # synthetic data: not results

"""Synthetic Tier 2 loan-level panel with known parameters (RQ2/RQ3 pipeline test).

No real data of any kind: every value is drawn from the seeded process below. The panel
follows 03_data/schemas/loan_panel.yaml. Sheet codes are format-conformant but random.

Data-generating process (monthly linear-probability bands, one uniform draw per loan-month):
    [0, a)            base 90-dpd default, a = p_default[class] + beta_h*h_s + eta_{d,t}
    [a, a+f)          flood stress, f = beta_s * Flood_s for 12 months from 2011-10
    [., +p_tdr)       ordinary restructuring (TDR), stage 2
    [., +p_stage2)    stage 2 without restructuring
    rest              stage 1, current
Relief (circular ว. 1564/2554): a debtor that was normal or special mention in 2011-09, on a
flooded sheet, keeps its classification; its flood-stress months show dpd 0, restructured = 1
(flood_relief) and stage 2 with probability sicr_share, instead of 90-dpd default. Only
flood-induced arrears are covered (the circular requires the flood impact to be linked to the
debtor). Eventual loss: a loan with any latent default month (base or flood) from 2011-10 on is
written off in 2013-12 with LGD = max(0, 1 - (1-c) V_post / EAD), where
V_post = Vbar (1 - delta h)(1 - phi Flood) and the bank lends on A = Vbar (1 - lam delta h).
"""
from __future__ import annotations

import json
import pathlib

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "03_data" / "synthetic"

TRUE = {
    "seed": 20261102,
    "n_loans": 20_000,
    "start": "2009-01",
    "n_months": 60,
    "n_provinces": 10,
    "districts_per_province": 5,
    "sheets_per_district": 16,
    "event_months": ["2011-10", "2011-11"],
    "pre_month": "2011-09",
    "beta_s": 0.05,
    "stress_window_months": 12,
    "relief_window": ["2011-10", "2012-12"],
    "beta_h": 0.004,
    "district_flood_shock": 0.01,
    "district_noise_max": 0.002,
    "class_shares": {"normal": 0.8, "special_mention": 0.1, "substandard": 0.1},
    "p_default": {"normal": 0.004, "special_mention": 0.03, "substandard": 0.55},
    "p_stage2": {"normal": 0.03, "special_mention": 0.6, "substandard": 0.3},
    "p_tdr": 0.01,
    "sicr_share": 0.8,
    "delta": 0.3,
    "lam": 0.3,
    "phi": 0.3,
    "haircut": 0.4,
    "ltv_range": [0.7, 1.0],
    "ecl_pd_by_stage": {"1": 0.02, "2": 0.2, "3": 1.0},
}


def _months(start: str, n: int) -> pd.PeriodIndex:
    return pd.period_range(start, periods=n, freq="M")


def _sheets(rng, p):
    """Sheet table: random format-conformant codes, district, province, hazard and 2011 flood share."""
    n_d = p["n_provinces"] * p["districts_per_province"]
    n_s = n_d * p["sheets_per_district"]
    district = np.repeat(np.arange(n_d), p["sheets_per_district"])
    province = district // p["districts_per_province"]
    footprint = rng.uniform(0.0, 0.7, p["n_provinces"])[province]
    hazard = np.clip(rng.beta(1.5, 3.0, n_s), 0, 1)
    p_flood = np.clip(footprint + 0.5 * (hazard - 0.35), 0.02, 0.95)
    flood = (rng.uniform(size=n_s) < p_flood) * rng.uniform(0.1, 1.0, n_s)
    return pd.DataFrame({
        "utmmap1": rng.integers(4836, 5240, n_s).astype(str),
        "utmmap2": rng.integers(1, 5, n_s),
        "utmmap3": [f"{e:02d}{n:02d}" for e, n in zip(2 * rng.integers(0, 50, n_s), 2 * rng.integers(0, 50, n_s))],
        "utmmap4": [f"{k:02d}" for k in rng.integers(1, 17, n_s)],
        "utmscale": 1000,
        "district": district,
        "province": province,
        "hazard": hazard.round(4),
        "flood_2011": flood.round(4),
    })


def simulate(p: dict = TRUE) -> pd.DataFrame:
    """Return the synthetic panel (one row per loan-month) in the loan_panel schema."""
    rng = np.random.default_rng(p["seed"])
    months = _months(p["start"], p["n_months"])
    n, T = p["n_loans"], p["n_months"]
    t0 = months.get_loc(pd.Period(p["event_months"][0], "M"))
    k = np.arange(T) - t0
    event = np.isin(months.astype(str), p["event_months"])
    stress = (k >= 0) & (k < p["stress_window_months"])
    relief = (months >= pd.Period(p["relief_window"][0], "M")) & (months <= pd.Period(p["relief_window"][1], "M"))

    sh = _sheets(rng, p)
    s = rng.integers(0, len(sh), n)
    F, h, d = sh["flood_2011"].to_numpy()[s], sh["hazard"].to_numpy()[s], sh["district"].to_numpy()[s]

    classes = np.array(list(p["class_shares"]))
    cls = rng.choice(classes, n, p=list(p["class_shares"].values()))
    eligible = cls != "substandard"
    p_def = pd.Series(p["p_default"])[cls].to_numpy()
    p_s2 = pd.Series(p["p_stage2"])[cls].to_numpy()

    # district x month shocks: noise plus a region-wide flood shock (absorbed by district x month FE)
    d_flood = pd.Series(sh["flood_2011"]).groupby(sh["district"]).mean().to_numpy()
    eta = rng.uniform(0, p["district_noise_max"], (len(d_flood), T)) + p["district_flood_shock"] * d_flood[:, None] * stress

    a = p_def[:, None] + p["beta_h"] * h[:, None] + eta[d]
    f = p["beta_s"] * F[:, None] * stress[None, :]
    u = rng.uniform(size=(n, T))
    base_def = u < a
    flood_band = (u >= a) & (u < a + f)
    tdr = (u >= a + f) & (u < a + f + p["p_tdr"])
    s2_band = (u >= a + f + p["p_tdr"]) & (u < a + f + p["p_tdr"] + p_s2[:, None])
    censored = flood_band & (eligible & (F > 0))[:, None] & relief[None, :]
    default = base_def | (flood_band & ~censored)
    sicr = rng.uniform(size=(n, T)) < p["sicr_share"]

    stage = np.where(default, 3, np.where(tdr | s2_band | (censored & sicr), 2, 1))
    restructured = (tdr | censored).astype(int)
    rtype = np.where(censored, "flood_relief", np.where(tdr, "tdr", "none"))
    dpd = np.where(default, rng.integers(91, 361, (n, T)), np.where(s2_band, rng.integers(31, 91, (n, T)), 0))

    # collateral, balances and eventual losses
    vbar = rng.lognormal(np.log(3e6), 0.5, n)
    A = vbar * (1 - p["lam"] * p["delta"] * h)
    ltv = rng.uniform(*p["ltv_range"], n)
    orig = rng.integers(0, 108, n)  # 2000-01 .. 2008-12
    orig_month = pd.period_range("2000-01", periods=108, freq="M").astype(str).to_numpy()[orig]
    term = 240
    age = (np.arange(T)[None, :] + 108 - orig[:, None])
    balance = (ltv * A)[:, None] * np.clip(1 - age / term, 0, 1)
    ead = balance[:, -1]
    v_post = vbar * (1 - p["delta"] * h) * (1 - p["phi"] * F)
    lgd = np.clip(1 - (1 - p["haircut"]) * v_post / ead, 0, 1)
    eventual = (base_def | flood_band)[:, t0:].any(axis=1)
    loss = np.where(eventual, ead * lgd, 0.0)

    lgd_book = np.clip(1 - (1 - p["haircut"]) * A[:, None] / balance, 0, 1)
    ecl = balance * pd.Series(p["ecl_pd_by_stage"]).rename(int)[stage.ravel()].to_numpy().reshape(n, T) * lgd_book

    last = np.zeros((n, T), bool)
    last[:, -1] = eventual
    flood_m = F[:, None] * event[None, :]

    rep = lambda x: np.repeat(x, T)  # noqa: E731  loan-level -> loan-month
    shs = sh.iloc[s]
    return pd.DataFrame({
        "loan_id": rep(np.char.add("L", np.char.zfill(np.arange(1, n + 1).astype(str), 6))),
        "month": np.tile(months.astype(str).to_numpy(), n),
        "product": rep(np.where(rng.uniform(size=n) < 0.7, "mortgage", "sme_secured")),
        "origination_month": rep(orig_month),
        "term_months": term,
        "balance_thb": (balance.ravel() / 1e3).round() * 1e3,
        "dpd": dpd.ravel(),
        "asset_class": rep(cls),
        "restructured": restructured.ravel(),
        "restructure_type": rtype.ravel(),
        "stage": stage.ravel(),
        "ecl_thb": (ecl.ravel() / 1e3).round() * 1e3,
        "write_off_thb": np.where(last, (loss[:, None] / 1e3).round() * 1e3, np.nan).ravel(),
        "write_off_month": np.where(last, months[-1].strftime("%Y-%m"), None).ravel(),
        "recovery_thb": np.where(last, ((ead - loss)[:, None] / 1e3).round() * 1e3, np.nan).ravel(),
        "recovery_month": np.where(last, months[-1].strftime("%Y-%m"), None).ravel(),
        "collateral_value_thb": rep((A / 1e4).round() * 1e4),
        "valuation_month": rep(orig_month),
        "valuation_method": rep(rng.choice(["internal", "external", "treasury"], n)),
        "utmmap1": rep(shs["utmmap1"].to_numpy()),
        "utmmap2": rep(shs["utmmap2"].to_numpy()),
        "utmmap3": rep(shs["utmmap3"].to_numpy()),
        "utmmap4": rep(shs["utmmap4"].to_numpy()),
        "utmscale": rep(shs["utmscale"].to_numpy()),
        "district_code": rep(np.char.add("D", np.char.zfill(d.astype(str), 3))),
        "province_code": rep(np.char.add("P", np.char.zfill(shs["province"].to_numpy().astype(str), 2))),
        "segment": rep(np.where(rng.uniform(size=n) < 0.7, "retail", "sme")),
        "income_band": rep(rng.choice(["low", "middle", "high", "unknown"], n)),
        "flood_share": flood_m.ravel(),
        "hazard": rep(h),
    })


def write(df: pd.DataFrame, p: dict = TRUE, out_dir: pathlib.Path = OUT_DIR) -> pathlib.Path:
    """Write the panel (parquet if pyarrow is available, else CSV.gz) and the true parameters."""
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        import pyarrow  # noqa: F401
        path = out_dir / "loan_panel_synth.parquet"
        df.to_parquet(path, index=False)
    except ImportError:
        path = out_dir / "loan_panel_synth.csv.gz"
        df.to_csv(path, index=False, compression={"method": "gzip", "mtime": 0})
    truth = {
        **p,
        "file": path.name,
        "implied_effects_per_unit_flood_share": {
            "distress_all (default or restructured)": p["beta_s"],
            "default_ineligible": p["beta_s"],
            "default_eligible": 0.0,
            "restructured_eligible": p["beta_s"],
            "stage2_eligible": p["sicr_share"] * p["beta_s"],
            "censoring_gap_default (eligible - ineligible)": -p["beta_s"],
        },
        "note": "Synthetic, no real data. Effects are on the monthly probability, averaged over event quarters 0-3 (2011-10 to 2012-09).",
    }
    (out_dir / "loan_panel_synth_true_params.json").write_text(json.dumps(truth, indent=2))
    return path


if __name__ == "__main__":
    print(write(simulate()))

"""Tier 2 pipeline tests on synthetic data only: .venv/bin/python -I -m pytest 04_analysis/src/test_tier2_pipeline.py"""
import pathlib
import sys

import numpy as np
import pytest
import yaml

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import rq2_event_study as rq2  # noqa: E402
import rq3_reverse_stress as rq3  # noqa: E402
import synth_tier2 as synth  # noqa: E402

P = synth.TRUE
BETA = P["beta_s"]


@pytest.fixture(scope="module")
def panel():
    return synth.simulate(P)


@pytest.fixture(scope="module")
def prepared(panel):
    return rq2.prepare(panel)


@pytest.fixture(scope="module")
def triple(prepared):
    return rq2.event_study(prepared, ["default", "restructured", "stage2"], het="eligible")


def test_synthetic_panel_matches_schema(panel):
    schema = yaml.safe_load((synth.ROOT / "03_data" / "schemas" / "loan_panel.yaml").read_text())
    assert list(panel.columns) == [f["name"] for f in schema["fields"]]


def test_a_event_study_recovers_beta_s(prepared):
    res = rq2.event_study(prepared, ["distress"])["distress"]
    est, se = rq2.window_effect(res, ["F"])
    assert abs(est - BETA) < max(3 * se, 0.15 * BETA) and abs(est - BETA) < 0.15 * BETA
    pre = res[0][[f"F:q{q}" for q in (-4, -3, -2)]]
    assert np.all(np.abs(pre) < 0.25 * BETA)  # no pre-trend


def test_b_default_censored_for_eligible_while_stress_moves(triple):
    dflt_elig, _ = rq2.window_effect(triple["default"], ["F", "F*eligible"])
    dflt_inel, _ = rq2.window_effect(triple["default"], ["F"])
    gap, _ = rq2.window_effect(triple["default"], ["F*eligible"])
    restr, _ = rq2.window_effect(triple["restructured"], ["F", "F*eligible"])
    stage2, _ = rq2.window_effect(triple["stage2"], ["F", "F*eligible"])
    assert abs(dflt_elig) < 0.2 * BETA
    assert dflt_inel > dflt_elig and gap < 0
    assert abs(restr - BETA) < 0.2 * BETA
    assert abs(stage2 - P["sicr_share"] * BETA) < 0.25 * BETA


def _portfolio(**kw):
    p = {**rq3.BASE, "w": np.array([0.4, 0.3, 0.2, 0.1]), "x": np.array([0.1, 0.2, 0.3, 0.5]),
         "h": np.array([0.2, 0.3, 0.5, 0.7]), "ltv": np.full(4, 0.9), "beta_pd": 0.6,
         "delta": 0.3, "lam": 0.3, "phi": 0.3, "haircut": 0.4}
    return {**p, **kw}


def test_c_bisection_matches_closed_form():
    p = _portfolio(phi=0.0)  # LGD constant in S -> loss linear in S
    lgd0 = rq3.lgd_r(0.0, p)
    closed = (p["k0"] - p["kappa"] * p["rwa"] - p["ead"] * np.sum(p["w"] * p["pd0"] * lgd0)) / (
        p["ead"] * p["beta_pd"] * np.sum(p["w"] * p["x"] * lgd0))
    assert 0 < closed and closed * p["x"].max() < 1 and p["pd0"] + p["beta_pd"] < 1  # no clipping
    assert rq3.s_star(p) == pytest.approx(closed, abs=1e-8)
    with pytest.raises(ValueError):
        rq3.s_star(_portfolio(beta_pd=-0.6))


def test_d_s_star_falls_with_concentration_and_appraisal_gap():
    p = _portfolio()
    by_conc = [rq3.s_star(rq3.concentrate(p, th)) for th in (0.0, 0.3, 0.6)]
    by_gap = [rq3.s_star({**p, "lam": lam}) for lam in (0.9, 0.5, 0.1)]  # (1 - lam) rising
    assert np.all(np.isfinite(by_conc + by_gap))
    assert np.all(np.diff(by_conc) < 0) and np.all(np.diff(by_gap) < 0)
    draws = rq3.draw_s_star(p, 50, seed=0, beta_se=0.1, lam_range=(0.1, 0.5))
    assert np.all(draws > 0) and np.std(draws) > 0

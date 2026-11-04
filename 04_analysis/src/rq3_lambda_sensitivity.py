"""RQ3 back-of-envelope (referee round 12, weakness 1): can the appraisal-recognition share lambda_B move S*?

Uses the pure functions of rq3_reverse_stress.py. Everything here is an illustrative assumption,
not a calibration to any bank:
- full hazard discount D = delta (h = 1 in the flooded region): 2.3%, 4.6%, 9.2% (Beltran et al.
  2018's 4.6% for inland 100-year floodplains, halved and doubled, as in the proposal);
- book loan-to-value ltv in {0.7, 0.8, 0.9, 1.0}; sale haircut c = 0.3; damage phi = 0.2 of value
  at full intensity;
- stylised two-region book: 60% of exposure in a flood-prone region (2011-type intensity
  x = 0.3, h = 1) and 40% elsewhere (x = 0.05, h = 0); pd0 = 2%, beta_pd = 0.4; capital as in
  rq3_reverse_stress.BASE (CET1 16% before the flood, threshold 7%).
Reported per cell: flooded-region LGD at S = 1 when appraisals ignore the hazard (lambda_B = 0) and
when they recognise it fully (lambda_B = 1), and S* under each, with the relative change.
Deferral, by contrast, can keep an entire flood-induced PD rise out of reported capital while relief
lasts, so it acts on the whole loss rather than on LGD alone.

Origination assumption (paper referee round 1, M9): loans are written at the same book LTV against the
appraisal whatever lambda_B, so a bank whose appraisals ignore the hazard has lent more against the same
parcel (EAD = ltv x A, A = V(1 - lambda delta h)). lambda_B therefore acts on true leverage at
origination. If loan amounts were held fixed instead, V_post / EAD would not depend on lambda_B and S*
on realised losses would be identical under lambda_B = 0 and 1 (lambda_B would then move only the
reported LTV and the timing of staging), so that variant needs no computation and is stated in the paper.

Second output (same referee point): a grid over the sale haircut c and the damage share phi at
delta = 4.6% and LTV 0.7 and 0.8, which shows how far the LTV-0.7 result depends on those two
assumptions; the grid also records every book parameter so the paper's table notes are generated.

Output: 04_analysis/outputs/tables/rq3_lambda_sensitivity.{csv,md}, rq3_lambda_grid.{csv,md}
Run   : .venv/bin/python -I 04_analysis/src/rq3_lambda_sensitivity.py
"""

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I drops the script directory
import rq3_reverse_stress as r  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TAB = ROOT / "04_analysis/outputs/tables"
DISCOUNTS, LTVS = [0.023, 0.046, 0.092], [0.7, 0.8, 0.9, 1.0]
BOOK = {"w": [0.6, 0.4], "x": [0.3, 0.05], "h": [1.0, 0.0], "pd0": 0.02, "beta_pd": 0.4,
        "phi": 0.2, "haircut": 0.3}


def main() -> None:
    rows = []
    for d in DISCOUNTS:
        for ltv in LTVS:
            p = {**r.BASE, **BOOK, "ltv": [ltv, ltv], "delta": d}
            lgd0, lgd1 = (float(r.lgd_r(1.0, {**p, "lam": lam})[0]) for lam in (0.0, 1.0))
            s0, s1 = (r.s_star({**p, "lam": lam}) for lam in (0.0, 1.0))
            rows.append({"full_discount": d, "ltv": ltv, "lgd_flooded_lambda0": lgd0, "lgd_flooded_lambda1": lgd1,
                         "lgd_change_pp": 100 * (lgd0 - lgd1), "s_star_lambda0": s0, "s_star_lambda1": s1,
                         "s_star_rel_change": s1 / s0 - 1})
    out = pd.DataFrame(rows)
    TAB.mkdir(parents=True, exist_ok=True)
    out.to_csv(TAB / "rq3_lambda_sensitivity.csv", index=False)
    (TAB / "rq3_lambda_sensitivity.md").write_text(
        "<!-- Illustrative only (assumed parameters; see the script docstring). lambda0: bank appraisals ignore "
        "the hazard discount; lambda1: they recognise it fully. S = 1 is a 2011-type event. Author's calculations. "
        "-->\n\n" + out.round(3).to_markdown(index=False) + "\n", encoding="utf-8")
    print(out.round(3).to_string(index=False))

    grid = []
    for ltv in (0.7, 0.8):
        for c in (0.2, 0.3, 0.4):
            for phi in (0.1, 0.2, 0.3):
                p = {**r.BASE, **BOOK, "haircut": c, "phi": phi, "ltv": [ltv, ltv], "delta": 0.046}
                s0, s1 = (r.s_star({**p, "lam": lam}) for lam in (0.0, 1.0))
                grid.append({"full_discount": 0.046, "ltv": ltv, "haircut": c, "phi": phi, "s_star_lambda0": s0,
                             "s_star_lambda1": s1, "s_star_rel_change": s1 / s0 - 1,
                             "w_flooded": BOOK["w"][0], "x_flooded": BOOK["x"][0], "x_other": BOOK["x"][1],
                             "pd0": BOOK["pd0"], "beta_pd": BOOK["beta_pd"], "cet1_before": r.BASE["k0"] / r.BASE["rwa"],
                             "kappa": r.BASE["kappa"]})
    g = pd.DataFrame(grid)
    g.to_csv(TAB / "rq3_lambda_grid.csv", index=False)
    (TAB / "rq3_lambda_grid.md").write_text(
        "<!-- Illustrative only: S* under lambda_B = 0 and 1 at delta = 4.6% over the sale haircut c and the damage "
        "share phi, same two-region book as rq3_lambda_sensitivity.csv (loans written at the same book LTV against "
        "the appraisal whatever lambda_B). Author's calculations. -->\n\n" + g.round(3).to_markdown(index=False) + "\n",
        encoding="utf-8")
    print(g.round(3).to_string(index=False))


if __name__ == "__main__":
    main()

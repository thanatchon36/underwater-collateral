"""Power for RQ2. (1) 2024-25 relief design (primary): flooded vs comparable unflooded borrowers.
(2) H2c, 2011 extension (relief defers rather than avoids loss): fuzzy difference-in-discontinuities.

(1) Outcome: 90+ days past due within 12 months after relief ends (binary), base rate p0 of 3% or
    5%; k comparable unflooded borrowers per flooded borrower (k = 4); design effect DE for
    clustering by map sheet (1.5 or 2). Flooded borrowers needed to detect a rise of d points with
    80% power, 5% two-sided: (z_0.975 + z_0.80)^2 * DE * p0 (1 - p0) (1 + 1/k) / d^2, and the
    detectable rise with 1,000 and 2,000 flooded borrowers. Conservative: no pre-period adjustment.
(2):

Estimand: (jump in cumulative discounted loss at 90 days past due in declared areas
           - the same jump in undeclared areas) / pi, with pi the first stage (jump in the
           probability of receiving relief). Four groups g: declared/undeclared x either side of
           the threshold, n_g borrowers within the bandwidth.
Variance: a local linear fit with a uniform kernel and a running variable spread evenly within
          the bandwidth estimates the boundary intercept with variance 4 sigma^2 / n_g (the
          (1,1) element of the inverse moment matrix of (1, u), u ~ U[0,1], is 4). Hence
          Var = DE * (4 sigma^2 / pi^2) * sum_g 1/n_g = 16 DE sigma^2 / (pi^2 n) with n per group,
          where DE is the design effect of clustering borrowers by area.
Equivalence: two one-sided 5% tests at a true effect of zero have 80% power when the margin is
          at least (z_0.95 + z_0.90) * SE.
sigma:    loss as a share of exposure lies in [0, 1]; with mean m its SD is at most
          sqrt(m (1 - m)) (Bhatia-Davis bound), so 0.3 is the largest SD at m = 0.1; 0.2 is shown too.
Benchmark: the earlier plain 2 x 2 calculation, 4 (z_0.95 + z_0.90)^2 sigma^2 / margin^2.
All inputs are assumptions; nothing here uses data.

Output: 04_analysis/outputs/tables/rq2_power.{csv,md} (2011) and rq2_power_2024.{csv,md} (2024-25)
Run: .venv/bin/python -I 04_analysis/src/rq2_power.py
"""

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[2]
TAB = ROOT / "04_analysis/outputs/tables"
Z = stats.norm.ppf(0.95) + stats.norm.ppf(0.90)
MARGIN = 0.05
NS = [1000, 2000, 5000]


def main() -> None:
    rows = []
    for sigma in (0.2, 0.3):
        for pi in (0.5, 0.75, 1.0):
            for de in (1.0, 1.5):
                r = {"sigma": sigma, "first_stage": pi, "design_effect": de,
                     "n_per_group_for_5pp": int(np.ceil(16 * de * sigma ** 2 * Z ** 2 / (pi ** 2 * MARGIN ** 2)))}
                for n in NS:
                    r[f"margin_pp_at_n{n}"] = 100 * Z * np.sqrt(16 * de * sigma ** 2 / (pi ** 2 * n))
                rows.append(r)
    t = pd.DataFrame(rows)
    plain = int(np.ceil(4 * Z ** 2 * 0.3 ** 2 / MARGIN ** 2))
    TAB.mkdir(parents=True, exist_ok=True)
    t.to_csv(TAB / "rq2_power.csv", index=False)
    (TAB / "rq2_power.md").write_text(
        "<!-- H2b equivalence power, fuzzy difference-in-discontinuities (local linear, uniform kernel; "
        f"80% power, two one-sided 5% tests; margin 5 pp of exposure). Plain 2 x 2 benchmark at sigma 0.3: "
        f"{plain} per cell. All inputs are assumptions. Author's calculations. -->\n\n"
        + t.round(2).to_markdown(index=False) + "\n", encoding="utf-8")
    print("plain 2x2 benchmark per cell:", plain)
    zt = stats.norm.ppf(0.975) + stats.norm.ppf(0.80)
    k, rows = 4, []
    for p0 in (0.03, 0.05):
        for de in (1.5, 2.0):
            v = de * p0 * (1 - p0) * (1 + 1 / k)
            r = {"base_rate": p0, "design_effect": de, "controls_per_flooded": k}
            for d in (0.007, 0.01, 0.02):  # 0.7 pp: euro-area corporate default response (albertazzi2026physical)
                r[f"flooded_needed_{100 * d:g}pp"] = int(np.ceil(zt ** 2 * v / d ** 2))
            for n in (1000, 2000):
                r[f"mde_pp_at_{n}_flooded"] = 100 * zt * np.sqrt(v / n)
            rows.append(r)
    u = pd.DataFrame(rows)
    u.to_csv(TAB / "rq2_power_2024.csv", index=False)
    (TAB / "rq2_power_2024.md").write_text(
        "<!-- RQ2 primary (2024-25 relief): flooded vs comparable unflooded borrowers, 90+ days past due within "
        "12 months after relief ends; 80% power, 5% two-sided; no pre-period adjustment. All inputs are "
        "assumptions. Author's calculations. -->\n\n" + u.round(2).to_markdown(index=False) + "\n", encoding="utf-8")
    print(u.round(2).to_string(index=False))
    print(t.round(2).to_string(index=False))


if __name__ == "__main__":
    main()

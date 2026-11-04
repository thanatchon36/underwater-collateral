# Tier 2 pipeline on synthetic data (RQ2 Plan A, RQ3)

**Working draft, 2026-11-02 (Phase 5).** No real data were used. Every number below is a script output on a seeded synthetic panel. Its job is to show that the estimation code is ready for the day Tier 2 access is granted. It is not evidence about Thailand.

## What was built

| File | Content |
|---|---|
| `03_data/schemas/loan_panel.yaml` | Monthly loan-level panel with collateral: 30 fields, each with type, unit, allowed values, description, source (controller / derived / Tier 1 join) and PDPA note. Location is the DOL cadastral sheet (UTMMAP1–4 + UTMSCALE, 1:500 aggregated up to 1:1,000), never an address or parcel number. |
| `04_analysis/src/synth_tier2.py` | Seeded generator (seed 20261102): 20,000 loans × 60 months (2009-01 to 2013-12), 800 sheets in 50 districts and 10 provinces. Writes `03_data/synthetic/loan_panel_synth.csv.gz` (pyarrow is not installed) and `loan_panel_synth_true_params.json`. |
| `04_analysis/src/rq2_event_study.py` | Event study / triple difference: loan and district × month fixed effects (plus eligibility × month in the triple difference), removed by alternating projections; event quarters relative to 2011-10; SEs clustered by district. |
| `04_analysis/src/rq3_reverse_stress.py` | Pure functions for L(S), CET1(S) and S* (bisection after a monotonicity check), plus concentration, elasticity draws and province aggregation from the panel. |
| `04_analysis/src/test_tier2_pipeline.py` | 5 tests (schema match and tests a–d); all pass in about 7 s. |

Run: `.venv/bin/python -I 04_analysis/src/synth_tier2.py`, then `rq2_event_study.py` and `rq3_reverse_stress.py`; tests with `.venv/bin/python -I -m pytest 04_analysis/src/test_tier2_pipeline.py`.

**Synthetic design in brief.** About 40% of loans sit on sheets with a non-zero 2011 flood share (set in 2011-10 and 2011-11). A flood raises the monthly probability of 90-dpd status by β_s × Flood_s for 12 months. Debtors that were normal or special mention in 2011-09 and sit on a flooded sheet keep their classification (circular ว. 1564/2554): their flood-induced arrears appear as restructuring (flood relief) and, with probability 0.8, stage 2, not as default. Eventual losses use LGD = max(0, 1 − (1 − c) V_post / EAD), with the bank lending on the appraisal A = V̄(1 − λδh). A district-level flood shock is built in to check that district × month effects absorb it.

## True versus recovered (window average, 2011-10 to 2012-09, per unit flood share)

| Quantity | True | Recovered | SE |
|---|---|---|---|
| β_s: distress (default or restructured), all loans | 0.050 | 0.046 | 0.003 |
| Default, eligible (censored by relief) | 0 | −0.001 | 0.002 |
| Default, ineligible (substandard in 2011-09) | 0.050 | 0.039 | 0.023 |
| Restructuring, eligible | 0.050 | 0.049 | 0.002 |
| Stage 2, eligible (0.8 β_s) | 0.040 | 0.043 | 0.004 |
| Censoring gap in default (eligible − ineligible) | −0.050 | −0.041 | 0.024 |
| Default, all loans (what a naive study would see) | (diluted) | 0.003 | 0.003 |

Pre-event quarters are all within ±0.005 of zero.

**Reverse stress test** (S = multiple of the 2011 footprint; illustrative capital: CET1 16% before the scenario, κ = 7%, pd0 = 2%; annual PD elasticity taken as 12 × β_s):

| | S* |
|---|---|
| With true β_s | 2.08 |
| With recovered β_s | 2.17 |
| 500 draws (β ~ N(β̂, SE), λ ~ U(0.1, 0.5)): median [5%, 95%] | 2.18 [2.02, 2.34] |

Test (c): bisection matches the closed-form S* of a linear case to 1e-8. Test (d): S* falls when exposure is concentrated in the most exposed region and when (1 − λ) rises.

## Limitations

- **Stylised DGP.** Monthly status is drawn independently given a linear probability; there is no state persistence, cure dynamics or loan entry and exit. `asset_class` is held at its 2011-09 value. Real data will need absorbing default and an unbalanced panel; the estimator handles the latter, but it is untested on it.
- **The triple difference is weak where it matters.** Ineligible debtors are already non-performing, so their default outcome is noisy (SE 0.023 against an effect of 0.05) and the censoring gap is not significant here. With real data, the comparison group needs thought (for example lenders that did not apply the freeze, which ว. 1564/2554 leaves to the institution's discretion).
- **Relief covers only flood-induced arrears in the DGP.** This is a modelling choice based on the circular's condition that the flood impact be linked to each debtor; actual practice may differ.
- **Stage 2 did not exist in 2011.** TFRS 9 stages apply only after adoption (date [to verify]); for 2011 the schema asks for the bank's internal SICR or watch-list equivalent.
- **LGD is not estimated in RQ2.** The synthetic panel carries write-offs and recoveries, but no recovery-rate regression was built; RQ3 uses the structural LGD formula with the true δ, λ, φ, c.
- **RQ3 mapping.** "Annual PD elasticity = 12 × monthly effect" is a first-order approximation. RWA is fixed, prices are exogenous (no fire sales), and the relief scenario (H3b) is not implemented. Capital figures are illustrative, not drawn from any bank.
- **Inference.** 50 district clusters; small-cluster corrections and spatial HAC errors are not implemented.
- **File format.** pyarrow is absent from `.venv`, so the panel is CSV.gz (9.5 MB). Installing pyarrow would allow parquet; it is not required.

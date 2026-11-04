# Conceptual framework

**Working draft, 2026-11-02 (Phase 4).** This is a deliberately small accounting-plus-incentives framework, not a structural model. Its job is to show where flood risk can enter the chain from collateral to capital, and to generate the signed predictions that RQ1–RQ3 test. Citekeys refer to `01_literature/references.bib`. Everything below is the author's modelling; no part of it is an empirical claim.

## 1. Set-up

A location *i* has flood hazard *h_i* ≥ 0: the expected inundation, summarised as a return-period depth or the share of past years flooded. A flood event in period *t* has realised severity *s_it* ≥ 0, observed with error by satellite.

**Collateral.** The market value of land at *i* is

  V_i = V̄_i · (1 − δ h_i),

where δ > 0 is the hazard discount a fully informed market would apply. After an event, the value falls further by φ s_it, partly transitory.

**Two valuations.** Two valuations of the same land matter, and both are formed by market comparison:
- the state's **official valuation** (Treasury Department), which is public;
- the bank's **collateral appraisal**, which is observable only in Tier 2 data.

No public BOT rule links the second to the first (`04_analysis/treasury_method_notes.md` §4). Each is written as

  A_i^k = V̄_i · (1 − λ_k δ h_i),  k ∈ {T (official), B (bank)},  λ_k ∈ [0, 1].

The parameter λ_k is the *capitalisation share*: λ_k = 1 means the valuation prices hazard fully, and λ_k = 0 means it ignores it.

- **After an event**, the official value adjusts by λ_e φ s_it, but only at the next appraisal round (or a mid-round revision), so its response is lagged.
- **RQ1 measures λ_T.** RQ2, Plan A, measures λ_B, where loan data include the collateral appraisals.
- **RQ3 needs λ_B.** Without Tier 2 data, it uses λ_T as a proxy. *Assumption, stated as such:* both valuations rely on the same market evidence (registered sales), so λ_B ≈ λ_T. This is not established.

**Implied mispricing of collateral.** The bank's appraisal overstates value by

  A_i^B − V_i = (1 − λ_B) δ h_i V̄_i,

which is increasing in hazard whenever λ_B < 1. The reported loan-to-value ratio is then too low in high-hazard locations:

  LTV_i^rep = L_i / A_i^B < L_i / V_i = LTV_i^true.

## 2. Borrower default (PD)

A borrower defaults when a cash-flow shock pushes debt service beyond capacity. In reduced form,

  PD_it = F(α + β_s s_it + β_h h_i + γ LTV_i^true + x_it'θ),

where *F* is a link function, β_s > 0 captures the income and repair-cost channel of a realised flood, and γ > 0 the strategic or forced-sale channel through negative equity.

**Relief.** A relief regime *R_t* ∈ {0, 1} lets eligible borrowers postpone payments and keep their pre-disaster classification. Eligibility depends on rules such as declared zones and debt thresholds; see `02_policy_context/policy_timeline.md`. Under relief, the *observed* 90-day default indicator is

  D_it^obs = D_it · (1 − R_t · e_i),

where e_i ∈ {0, 1} marks eligibility. Credit stress therefore moves into restructuring and, under TFRS 9, into stage 2 if banks judge a significant increase in credit risk (SICR) despite the relief. It does not appear in default. Relief censors default; it does not remove the underlying deterioration.

## 3. Loss given default (LGD)

With recovery from collateral after a haircut *c*,

  LGD_i = max{0, 1 − (1 − c) · V_i^post / EAD_i}.

The bank provisions on its *believed* collateral value, which is based on A_i^B, not V_i. The provisioning error on a defaulted exposure is therefore increasing in (1 − λ_B) δ h_i. This is the link from valuation to credit: a valuation that does not capitalise hazard turns directly into under-provisioned LGD in high-hazard locations. RQ1 informs it through λ_T; RQ2 measures it directly.

## 4. Staging and expected credit loss

Under TFRS 9, ECL = PD × LGD × EAD over 12 months (stage 1) or over the lifetime (stage 2). Flood risk can be under-reflected at three points:
- (i) PD models that omit *h_i*;
- (ii) LGD that uses A_i;
- (iii) relief that delays the stage transition.

The first two errors are *level* errors; the third is a *timing* error.

## 5. Capital and the reverse stress test

Let *w_r* be the bank's exposure share in region *r*, and let a scenario be indexed by a single hazard severity *S*, for example a basin-wide return period. The capital ratio after the scenario is

  CET1(S) = [K₀ − Σ_r w_r · EAD · PD_r(S) · LGD_r(S)] / RWA(S).

The **reverse stress test** solves for the breaking point

  S* = inf{ S : CET1(S) < κ },

for a threshold κ equal to the regulatory minimum plus buffers: CET1 of 4.5% plus a 2.5% conservation buffer, so κ = 7% [@bot2012capital], and κ = 8% for domestic systemically important banks, which hold a further 1% [@bot2017dsib]. The countercyclical buffer (0–2.5% at the Bank of Thailand's discretion) was not required when the notification was issued, and no later activation was found as of 2026-11-02, so the baseline sets it to zero and 2.5% is a sensitivity. This inverts the usual stress test, in the spirit of [@grundke2018macroeconomic], and formalises the scenario ladder in [@caloia2021flood].

## 6. Predictions (testable)

| # | Prediction | Sign | Tested in |
|---|---|---|---|
| P1 | Official values fall with hazard, but less than the market discount: ∂A^T/∂h < 0 and λ_T < 1 | λ_T ∈ (0, 1) | RQ1 (cross-section within districts; benchmark from market evidence, e.g. [@garbarino2021high]) |
| P2 | Official values respond to realised floods only at the next round, and partially | λ_e < 1, lagged | RQ1 (difference-in-differences across rounds) |
| P3 | A realised flood raises PD; under relief, the rise appears in restructuring and stage 2 before it appears in 90-day default | β_s > 0; restructuring and stage 2 lead default | RQ2 |
| P4 | Recovery shortfalls rise with hazard where appraisals do not price it | ∂LGD/∂h > 0, larger when λ_B is low | RQ2 (λ_B measured directly in Plan A) |
| P5 | The breaking point falls with geographic concentration and with the capitalisation gap (1 − λ_B) | ∂S*/∂(concentration) < 0; ∂S*/∂(1 − λ_B) < 0 | RQ3 (λ_T as proxy without Tier 2) |
| P6 | Relief raises the *measured* short-run breaking point without changing the lifetime one | short-run S* rises; lifetime S* roughly unchanged | RQ3 (scenarios with and without relief) |

## 7. What the framework leaves out (deliberately)

- **General-equilibrium price feedback** from fire sales to land values. RQ3 treats prices as exogenous, which biases S* upwards (towards apparent safety); this will be stated as a limitation.
- **Insurance.** It is set to zero in line with the Thai setting. Advanced-economy papers need an insurance term, and the contrast is part of the contribution.
- **Bank lending responses** (rationing or repricing of credit in high-hazard areas). They are relevant, but belong to the existing literature (e.g. [@albertazzi2026physical]), not to this project.

## Author notes

- **Weakest point.** P1 needs a market-value benchmark for δ. Public Thai transaction data at fine geography are not available (REIC terms forbid reuse), so RQ1 identifies the *appraisal* gradient and tests λ < 1 against external benchmarks from the literature. Report this honestly as partial identification.
- A reader may ask why there is no structural model. The answer: the contribution is measurement and identification along the chain; the framework only orders the predictions.

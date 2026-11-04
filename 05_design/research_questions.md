# Research questions and hypotheses

**Working draft, 2026-11-02 (Phase 4).** Approved at CP2: RQ1 and RQ3 are the core, and RQ2 is conditional on Tier 2 access. Predictions P1–P6 are derived in `framework.md`. The gap and the closest papers are in `01_literature/gap_statement.md`. The H labels follow the literature review. All hypotheses are the author's; none is established evidence.

## RQ1: Do official land valuations price flood risk? (Chapter 1, public data)

**Question.** Do Thailand's official land appraisal values (ราคาประเมินที่ดิน, Treasury Department), the state's market-comparison valuation and the base for transfer fees, capitalise (i) ex-ante flood hazard and (ii) realised flood events, and how quickly?

**Unit and data.**
- The unit is the cadastral map sheet: a 2 km, 1 km, 500 m or 250 m cell, decoded for 95.8% of 37.8 million parcels; see `04_analysis/groundwork_notes.md`.
- The outcome is the log appraisal value per square wah, averaged per sheet or at parcel level with sheet-level exposure.
- Exposure: the 2011 inundation (Global Flood Database event 3850), long-run water recurrence (JRC Global Surface Water), and post-2014 events from Sentinel-1.

**Hypotheses.**
- **H2a (level).** Within a district, appraisal values decline in flood hazard by less than market evidence implies. In the framework, the official capitalisation share λ_T is below 1.
- **H2b (event).** Appraisals in areas flooded between rounds fall at the next round by less than the market discount, and not before; that is, λ_e < 1, with the response lagged to the round.
- **H2c (salience).** The response is larger after salient, recent events than for long-run hazard of equal expected depth.

**Falsification.** H2a fails if there is no gradient (λ_T ≈ 0) or a gradient as large as benchmark market estimates (λ_T ≈ 1). Either result is informative.

**Scope limit.** No Thai fine-geography market price data are public, so λ_T is benchmarked against external estimates rather than identified within Thailand. The design therefore identifies the *appraisal gradient*, not the market gap.

## RQ2: Where does flood risk surface in credit risk when relief censors default? (Chapter 2, conditional)

**Question.** Does flood exposure of the collateral raise borrower PD and LGD? Under relief, does the effect surface first in restructuring and TFRS 9 stage 2 rather than in 90-day default, and does it later turn into loss?

**Data.** Plan A: loan-level data with collateral location through a formal access agreement (Tier 2). Plan B: listed-bank disclosures of staging and restructuring, together with provincial credit aggregates (Tier 1).

**Hypotheses.**
- **H1.** A realised flood raises PD and LGD, and LGD rises more where appraisals do not price hazard (P3–P4).
- **H-S5a.** Under relief, the effect appears in restructuring and stage 2 before default. Short-horizon evidence exists for Spain [@perezmontes2025impact]; the test here covers an uninsured setting over a multi-year horizon.
- **H-S5b.** Relief eligibility, meaning pre-flood performing status, declared zones and the dates of declaration (`02_policy_context/policy_timeline.md`), shifts *observed* default without changing eventual loss.

## RQ3: What flood severity breaks bank capital? (Chapter 3, core)

**Question.** Given the elasticities from RQ1–RQ2 (or from published benchmarks if RQ2 data are unavailable), and given the observed geographic concentration of credit, what flood severity S* breaches capital thresholds? How much do relief rules and the appraisal gap move S*?

**Hypotheses.**
- **H3.** S* falls with geographic concentration and with the capitalisation gap (1 − λ_B) (P5).
- **H3b.** Relief raises the short-run S* measured from reported ratios, but leaves the lifetime S* broadly unchanged (P6).

**Output.** A reverse stress-testing tool, solved by formal inversion over a single hazard index, run on public provincial credit data and published bank disclosures, and tested end to end on synthetic loan-level data.

## How the chapters fit

RQ1 supplies λ_T, the official valuation's capitalisation share; it stands in for the bank-appraisal share λ_B, which turns into understated LGD, unless RQ2 measures λ_B directly. RQ2 supplies the PD and LGD flood elasticities and the timing effect of relief. RQ3 combines both with exposure data to locate the breaking point. If RQ2 has no data, RQ3 uses RQ1 together with published elasticities [@albertazzi2026physical; @caloia2021flood] and states the resulting uncertainty explicitly.

## Revision note (round 11, 2026-11-02)

The proposal now makes the 2024–25 relief the primary RQ2 design (H2b: flood-induced delinquency recorded mainly after relief ends; power in `04_analysis/outputs/tables/rq2_power_2024.csv`) and the 2011 difference-in-discontinuities an extension (H2c). The no-access Plan B is Chapter 2's design on the 2025 floods (`rq1_sample_sensitivity.csv`), not the smoothing chapter; smoothing becomes a section if earlier rounds arrive. Where this file differs, `06_proposal/proposal.md` is current.

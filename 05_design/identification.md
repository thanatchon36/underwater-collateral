# Identification strategy

**Working draft, 2026-11-02 (Phase 4).** The equations are the author's design. Citekeys refer to `01_literature/references.bib`. Facts about the data come from `04_analysis/groundwork_notes.md` and `03_data/README.md`; facts about policy rules come from `02_policy_context/policy_timeline.md`. Items marked **[to verify]** must be checked before the proposal is finalised.

---

## RQ1: Do official land valuations capitalise flood hazard and floods?

### Unit, outcome and exposure

- **Unit.** A parcel *p* is located on cadastral sheet *s*: a 2 km, 1 km, 500 m or 250 m cell, decoded for 95.8% of parcels. Sheets nest in subdistricts (tambon), districts *d* and provinces.
- **Outcome.** Log appraisal value in baht per square wah (`EVAPRICE`; unit confirmed in the Ministerial Regulation, item 7(2) [@th2020appraisalmr]). The main outcome is the **sheet-level upper quantile** (p90 or maximum), which approximates the unit price of the best road-front land unit on the sheet; the parcel-weighted mean is a robustness check.
- **Exposure, all aggregated to the sheet** (after the datum shift from Indian 1975 to WGS84):
  - *2011 event:* share of the sheet flooded, and mean flood duration (Global Flood Database DFO 3850, about 250 m). Sheet means are reliable only for sheets at 1:4,000 (2 km), which hold about 64 pixels; 500 m sheets hold about 4 pixels.
  - *Long-run hazard:* mean JRC GSW occurrence outside permanent water (30 m).
  - *2024 event:* share of the sheet inside the UNOSAT Chiang Rai water extent.

**Treasury appraisal method (resolved; `04_analysis/treasury_method_notes.md`).**
- **Setting values.** Provincial committees first price *land units* (หน่วยที่ดิน): mostly road, soi, river, canal or sea frontages. They use market comparison of registered sales and other market evidence. Each parcel's value is then the unit price × a depth factor × a shape factor, rounded to a grid [@th2020appraisalmr].
- **No flood rule.** No written rule adjusts for flood or low-lying land, so any hazard capitalisation runs through the committees' market evidence at land-unit level.
- **Consequences:**
  - (i) Variation within a sheet is largely mechanical (depth, shape), so the identifying variation is between land units and sheets, and inference should be clustered no finer than the sheet.
  - (ii) Waterfront land units have their own unit prices, which bundle water access and amenity with hazard (see the main threat below).
  - (iii) Rounding makes small hazard effects partly invisible.
- **Use.** The values are the base for transfer fees [@dol2026fees]. No public BOT rule ties bank collateral values or LTV to them [@bot2019collateral].

### Design 1a: within-district cross-section (2023–26 round)

  log A_s = α_d + β₁ Flood2011_s + β₂ Hazard_s + X_s′θ + ε_s

- The district fixed effects α_d absorb the provincial committee, the regional price level and broad location.
  - The pilot uses province × 1:50,000-sheet cells, about 27 km across, because district boundaries are not yet joined.
  - District polygons are public: the Common Operational Datasets on HDX **[to verify licence]**.
- Controls X_s: sheet scale (a proxy for urban density), elevation and slope, distance to the main river and to the main road.
  - Elevation needs a public DEM; Copernicus GLO-30 is available without login **[to verify]**.
  - River and road distances need public vector data **[to verify]**.
- Standard errors are clustered at district level, with spatial-HAC errors as a robustness check.

**Interpretation.**
- β₁ and β₂ identify the *appraisal gradient* in hazard.
- The official capitalisation share λ_T (`framework.md`) is the ratio of β to an external market benchmark. There is no Thai fine-geography market price series, so λ_T is reported as a range against published benchmarks, not as a point estimate.

**Main threat: hazard is correlated with amenity.** Flood-prone land is near rivers, flat, fertile and often well connected. β therefore mixes the hazard discount with amenity value, and is biased towards zero if amenity is positively valued. The land-unit typology builds this in, because river and canal frontages are priced as separate units. A related threat is that registered sale prices, the main market input, may be anchored to official values to reduce fees. This is a hypothesis, not verified; if true, it would make official values sticky and attenuate β. Responses:
- compare within frontage classes, or restrict to inland road-front units;
- control for elevation and distance to water;
- compare 1:4,000 (rural) and 1:1,000 (urban) sheets separately;
- **Design 1b** below.

### Design 1b: boundary design at the 2011 flood edge

The sample is restricted to sheets within a band *h* of the 2011 inundation perimeter. The running variable is the signed distance from the sheet centroid to the edge, and β is estimated as the discontinuity [@keele2015geographic]. This follows the spatial RD at flood edges in [@albertazzi2026physical].

**Measurement error in the running variable.** Two sources: the MODIS perimeter is about 250 m, and sheets are cells, not points. The edge is therefore fuzzy. Responses:
- use bias-aware or deconvolution approaches [@pei2017devil; @davezies2017regression];
- treat the 2 km sheets as too coarse for the RD, and run the design on 500 m and 250 m sheets only;
- use donut specifications that drop sheets straddling the edge.

**Second threat: urban under-detection by optical satellites.** MODIS misses water among buildings, so true exposure in Bangkok is understated non-classically. Responses: report results excluding Bangkok and the vicinity, and check against the JRC GSW occurrence.

### Design 1c: difference-in-differences across appraisal rounds (from the 2027 round)

  Δlog A_s = α_d + β_e Flood2024_s + ΔX_s′θ + u_s

Treated sheets fell inside the 2024 northern flood extents (UNOSAT Chiang Rai, plus Phayao and Chiang Mai/Lamphun if downloaded). Controls are unflooded sheets in the same districts, optionally matched on elevation, distance to river and pre-period value. The 2026-11-02 snapshot is the pre-period. This is the design template of [@guo2026rising], applied to official land valuations in an emerging market.

**Testable implications and placebos.**
- *Dose–response.* β_e increases in flood share and duration.
- *Timing.* Floods after the appraisal cut-off date of the 2027 round should have no effect; the cut-off date is **[to verify]**.
- *Pre-trends.* These need earlier rounds (2016–19, 2020–22), whose availability is **[to verify]**. Without them, pre-trends cannot be tested. A partial substitute is to check that 2024-flooded sheets show no difference in 2023–26 values beyond the controls.
- *Placebo treatment.* Sheets flooded in 2011 but not in 2024 should show no change between 2023–26 and 2027–30 attributable to 2024.

**Threats specific to Design 1c.**
- *Mid-round revisions.* Committees revise values that diverge from the market by more than 15% (Ministerial Regulation, item 9), and the Treasury updates files in place. The 2026-11-02 snapshot may therefore already contain post-2024 revisions in Chiang Rai. Before treating it as the pre-period, compare it with an earlier dated copy, or with the published amendment notices.
- *Round timing.* The Act allows a one-year extension of a round. The 2027 start is not guaranteed and must be announced at least 30 days ahead.

**Further event (not yet examined).** HDX lists a Sentinel-1 flood proxy map for Bangkok dated 29 September 2026. If the event and product are confirmed, they give a second treated group for the 2027 round **[to verify]**.

### Robustness (RQ1)

- Alternative exposure measures: GFD versus JRC GSW; flood share versus duration; GSW recurrence.
- Datum sensitivity: results with and without the Indian 1975 → WGS84 shift (an offset of about 520 m), since it is open whether sheets are now on WGS84.
- Samples:
  - excluding `UTMSCALE = 5000` parcels (not decodable) and the 0.08% of codes inconsistent with their 1:50,000 sheet;
  - excluding the southern provinces with irregular coastal sheets.
- Outcome and level: sheet p90 or maximum (main); sheet parcel-weighted mean; parcel level with sheet-level exposure (precision overstated, because within-sheet variation is mechanical).
- Heterogeneity:
  - land-use proxies (rural/urban scale);
  - distance to Bangkok;
  - provinces with high and low 2011 relief uptake (if a public uptake series exists).

### Power (RQ1)

The cross-section has about 317,000 distinct sheet references and 37.8 million parcel rows, so it is not power-constrained. Power is limited by the effective number of independent clusters (districts, about 900 **[to verify]**) and by the spatial correlation of hazard.

For Design 1c, Phase 5 counted 1,214 sheets in Chiang Rai and Phayao that are more than 25% inside the 2024 UNOSAT extents (`04_analysis/outputs/tables/flood2024_treated_sheets.csv`). The minimum detectable effect will be computed from the cross-sectional variance of Δlog A once the 2027 round exists.

---

## RQ2: Flood exposure, PD, LGD and staging under relief

### Plan A: loan-level data (Tier 2)

  y_it = α_i + δ_{d×t} + Σ_k β_k · Flood_s(i) · 1[t = t₀ + k] + ε_it

- **Outcomes:**
  - 30- and 90-day arrears;
  - restructuring flag;
  - TFRS 9 stage 2 and stage 3;
  - write-off;
  - realised recovery rate (LGD) on defaulted loans.
- **Exposure.** Flood intensity at the collateral's sheet.
- **Fixed effects.** District × month effects absorb regional shocks and region-wide relief.

**Separating the flood from relief (H-S5b).**
1. **Pre-flood status.** BOT circular ว. 1564/2554 froze the classification only of debtors that were Normal or Special Mention when the flood hit [@bot2011circular1564]. Within flooded sheets, a triple difference compares eligible with ineligible (already non-performing) debtors. Observed default is censored for the eligible group only, so the gap in *restructuring and stage 2* versus *default* between groups identifies the censoring effect.
2. **Declaration timing (2024 template; December 2025 Level-4 moratorium).** Relief runs 12 months from each area's declaration date (`policy_timeline.md`). Staggered declarations allow an event study around declaration dates, holding flood intensity fixed.
3. **THB 500,000 threshold at state banks (2011).** So far this is known only from the World Bank report, and must be verified from a primary source before use. If verified, it supports an RD on total debt among state-bank borrowers, with a density (manipulation) test.

**Main threats.**
- *Selection into lenders:* borrowers sort to state banks.
- *Unobserved repair finance:* informal credit and family transfers.
- *Endogenous restructuring:* banks choose whom to restructure.

Responses: the triple-difference design, lender × time effects, and pre-flood status measured before the event.

### Plan B: public data

- **Bank level.** The stage 2 and stage 3 shares and restructured loans of listed banks, regressed on exposure-weighted flood intensity. The weights are each bank's regional loan shares where disclosed; otherwise the province shares from FI_CB_011.
- **Province level.** Credit growth and loan-to-deposit ratios after floods, in a difference-in-differences design on provincial flood intensity, with event-study leads as pre-trend tests.

These are descriptive-to-quasi-experimental designs. There are no LGD outcomes, and they are reported as such.

---

## RQ3: Reverse stress test

### Set-up

Hazard severity is indexed by a single scalar *S*. Two scenario families:
1. **Footprint scaling.** The 2011 GFD footprint and duration, scaled by S: inundated area and depth proxied by duration.
2. **Hazard quantile.** All sheets above the S-th quantile of JRC GSW occurrence are flooded.

For each scenario, the loss is

  L(S) = Σ_r w_r · EAD_r · PD_r(S) · LGD_r(S).

- PD_r(S) uses the flood elasticities from RQ2 (Plan A), or published benchmarks with uncertainty ranges [@albertazzi2026physical; @perezmontes2025impact].
- LGD_r(S) uses collateral losses together with the valuation gap (1 − λ_B): measured in RQ2 Plan A, or proxied by RQ1's (1 − λ_T).

### Inversion

  S* = inf{ S : CET1(S) < κ }

The solution is found by bisection. CET1(S) is monotone decreasing in S whenever the elasticities are non-negative, which guarantees a unique S*; this is stated as a lemma. This is formal inversion in the sense of [@grundke2018macroeconomic], replacing the escalating scenario ladder of [@caloia2021flood].

**Uncertainty.** Draws from the sampling distributions of the elasticities and of λ_T or λ_B give a distribution of S*, reported as a median and an interval.

### Calibration and validation

- **Exposures.** Provincial loans from FI_CB_011, and bank regional shares from disclosures.
- **Capital.** Published CET1 and RWA.
- **Validation.**
  - Run the full pipeline on synthetic loan-level portfolios (`03_data/synthetic/`), whose S* is known by construction.
  - Back-cast the 2011 scenario against the reported provincial credit outcomes of 2011–12.

### Testable comparative statics

- ∂S*/∂(concentration) < 0 (H3).
- ∂S*/∂(1 − λ_B) < 0 (H3).
- Relief raises the short-run S* measured from reported ratios, but not the lifetime S* (H3b).

### Limits

- Prices are exogenous, with no fire-sale feedback, which biases S* upwards.
- There is no lending response within the scenario.
- A single-hazard index ignores compound events.

Each limit will be stated in the proposal.

---

## Author notes

- **The biggest open risk for RQ1** is now interpretation, not data. Treasury values are the state's valuation and the base for transfer fees; they are not bank collateral values. RQ1 measures λ_T, and its relevance to credit runs through the assumption λ_B ≈ λ_T, which only RQ2 Plan A can test. Say this plainly in the proposal.
- **The 2027 round is the design's anchor.** Confirm its publication date and appraisal cut-off date from an official Treasury source.
- **Expect this question:** "Isn't the appraisal gradient just amenity?" The answer is Design 1b plus Design 1c, in which amenity is differenced out.

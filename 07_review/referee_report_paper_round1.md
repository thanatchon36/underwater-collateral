# Referee report

**Paper:** "Underwater Collateral: Flood Risk in Official Land Values, Credit under Relief and Bank Capital. Evidence from Thailand" (working paper, version of 4 November 2026, 38 pages)

**Date:** 2026-11-04

**Referee report, round 1 (working paper)**

Page numbers refer to the compiled PDF (`paper/paper.pdf`) and section numbers to its printed headings. The report is written as if the paper had been submitted to a top field journal (JFE, JUE or Review of Finance).

---

## 1. Summary

The paper asks where physical flood risk shows up in an emerging market where flood insurance is negligible and rule-based debt relief is the main buffer. It uses Thailand and has three parts.

**The 2011 cross-section.** Treasury Department official land values for 2023–26, aggregated to 41,000 cadastral sheets holding 8.8 million parcels in the Chao Phraya basin, are related to each sheet's 2011 flood share from the MODIS Global Flood Database. Urban sheets that were almost wholly flooded are 48% cheaper than dry neighbours. Holding 2021 land cover fixed, the gap falls to about 8% (SE about 6%). The rural gradient turns positive with controls. The author says clearly that this is not capitalisation.

**The difference-in-differences design, called pre-registered.** The design will compare the change in official values between the 2023–26 round and the next round on two groups of sheets:
- sheets flooded in 2024 or 2025, measured with Sentinel-1 radar and checked against Sentinel-2 imagery and UNOSAT flood extents;
- nearby dry sheets, weighted by entropy balancing within province.

Inference uses placebo footprints and a wild cluster bootstrap. The estimate needs the next round, which may be delayed to 1 January 2028. The paper reports power calculations, Monte Carlo checks and hashed sample lists.

**Credit (RQ2) and capital (RQ3).** The paper sets out a triple-difference event study and a reverse stress test that solves for the flood severity S\* at which CET1 breaches a threshold. It runs both on a synthetic loan panel. An illustrative two-region calibration suggests that whether bank valuations price hazard (λ_B) moves S\* by 7–9% at loan-to-value ratios of 0.8–1.0, and by 100% at 0.7. Descriptive provincial credit and residential-price aggregates around the 2011 and 2024 floods complete the paper.

A short framework, A = V̄(1 − λδh), links official (λ_T) and bank (λ_B) capitalisation to loan-to-value, a kinked loss given default (LGD) and capital, and yields six predictions (P1–P6).

## 2. Overall assessment

**Score: 4/10. Recommendation: major revision before circulation.**

**Strengths.**
- The question matters, and the setting is interesting for three reasons:
  - the official value is the state's fee and tax base;
  - relief is keyed to administrative declarations;
  - insurance is thin.
- The paper is unusually transparent:
  - every number in the text is a script-generated macro;
  - the sample files are hashed;
  - the radar flood maps are checked against two independent sources, and their errors are reported;
  - the cross-section is explicitly disowned as identification;
  - most synthetic tables say "not results".
- The core idea for RQ1, using the fixed revaluation calendar as the source of variation, is good. Guo et al.'s study of New York City assessments after Hurricane Sandy shows that this kind of test can deliver.

**The main problem.** No estimate yet exists for any of the three questions.
- The only empirical content is one descriptive cross-section, which the author disowns, and two sets of aggregates.
- Everything else is design, power calculations and code tests.
- Yet the abstract announces "three results".

Even when the data arrive, the RQ1 design has two limits:
- It has about 60% power against the effect its own framework implies under full recognition.
- Its coefficient does not map into λ_T without a δ that the paper cannot observe.

Survey timing may also make the 2025 event uninformative.

**Accuracy problems.**
- Several statements in the text are not supported by the outputs they cite: the credit gap, the "transitory" price dip, the "honest" standard errors and the declared-district sensitivity.
- One table note misstates its own calibration.
- Three bibliography keys are cited, in four places, for facts their documents do not contain.
- Two statements about Bank of Thailand policy carry no citation, which breaches the rule the paper sets itself on its title page.

**Contribution against the closest papers.** The comparison papers are characterised from the author's literature matrix and source notes, at the read depth recorded there.

| Closest paper | What it establishes | What this paper adds as it stands | Referee view |
|---|---|---|---|
| Albertazzi et al. (2026) | In the euro-area credit register, default on loans to flooded firms rises by about 0.6–0.7 pp on a base of about 1.4%; credit demand surges, then reverses | An estimator and power calculations for Thai loan-level data | The paper's description of this paper needs correcting (see M11) |
| Pérez Montes et al. (2025) | After the 2024 Valencia floods, stage 2 shares rise by about 0.5 pp; the most exposed banks move more loans into stage 2 and fewer into stage 3 under moratoria | The same question proposed for Thailand | The closest analogue for RQ2; the Thai version needs data |
| Garbarino and Guin (2021) | After the English floods, lender valuations did not fall when prices did (an upward bias of about 3%) | λ_B is assumed, not measured | The λ_B mechanism the paper relies on is their finding, so it should be engaged directly |
| Guo et al. (2026) | New York City assessments fell for inundated homes (about −17%), mostly through relief; they did not fall for undamaged high-risk homes; assessment caps blunt the pass-through | A design for the same test on Thai official values | The closest paper to RQ1. The contribution (an emerging market, nationwide coverage, a satellite-measured treatment) should be stated against Guo et al., not as a "first test" |
| Caloia and Jansen (2021); Caloia, van Ginkel and Jansen (2026) | Geocoded Dutch collateral under increasingly severe flood scenarios; capital depletion is non-linear | A formal inversion by bisection, run on synthetic data | A small step beyond this work. Blickle et al. (2025) already publish a breaking-point calculation on a hazard variable |
| Chitchumnong et al. (2025) | In one Thai bank's mortgage book, default after 2011 fell below predicted levels, attributed to relief | A design for loan-level data | The nearest Thai paper. RQ2 would add geolocation, LGD and staging if the data arrive |
| Sawada et al. (2018) | Thai industrial land prices fell 6.5–8.3% after 2011; residential and commercial land show no significant change | A 2011 cross-section on official values | The paper omits the non-significant residential and commercial result |
| Beltrán et al. (2018); Bin and Landry (2013); Ortega and Taşpınar (2018) | Flood-zone hazard discounts of about 4.6–8.8%; damaged homes lose 17–22% | Uses 4.6% as δ, and "2–8% for a realised flood" as the benchmark | The benchmark mixes up hazard discounts and realised-damage discounts (M2, M11) |

The potential contribution is real: the first nationwide test of whether a state valuation system in a low-insurance economy responds to realised flooding, with a path to credit and capital. As it stands, the paper contributes a design.

---

## 3. Major weaknesses

### M1. There is no estimate yet, and the plan is not registered

**What is wrong.**
- The primary RQ1 estimate needs a valuation round that is not yet published. RQ2 has no loan-level data. RQ3 is synthetic and illustrative.
- The abstract nonetheless says "Three results are reported".
- The RQ1 design is called "pre-registered" in the abstract (p. 1), the introduction (p. 3), the title of Section 6 (p. 15), Section 9.2 (p. 25) and the Conclusion (p. 27).
- But it is not registered:
  - Section 6 itself says "the plan is to be registered before the next round is announced" (p. 15);
  - the plan, `05_design/pre_analysis_plan_rq1_draft.md`, is headed as a working draft "to edit and register on OSF Registries";
  - the transparency statement leaves the registration as a bracketed placeholder.
- The hashes of 2 November 2026 (Table 22, p. 37) sit in a GitHub repository whose visibility is private. They therefore timestamp nothing for a third party.

**Why it matters.** "Pre-registered" is a claim a reader can check. One who checks and finds no registration will discount the rest of the paper. A paper whose only real finding is a cross-section that the author disowns will not be read as an empirical contribution.

**What would fix it.**
1. Either register on OSF now, cite the registration DOI and timestamp, and make the registered commit public; or write "pre-specified (registration pending)" throughout.
2. Rewrite the abstract to say what the paper contains: one descriptive result, one pre-specified design whose estimate awaits the next round, and tested code for the credit and capital steps.
3. Either reframe the paper as a design or registered-report paper (Section 7, item 6), or hold circulation until at least one estimate exists.

**Where.** p. 1 (abstract and title-page date line); p. 3; Section 6 title (p. 15); Section 6.5 (p. 19); Section 9.2 (p. 25); Section 10 and the transparency statement (p. 27); Table 22 (p. 37).

### M2. The design is underpowered for the effect its own framework predicts, and its coefficient does not identify λ_T

**What is wrong.**

*Which minimum detectable effect (MDE) is quoted.*
- The abstract and introduction quote an MDE of 0.047. That is the unweighted figure.
- The registered, weighted MDE is 0.053 (Table 6, p. 18; Section 6.3, p. 17). The UNOSAT sample's is 0.061–0.065.
- "3–5 log points" (p. 19 and p. 27) is correct only for the 2025 sample.

*Power against the effect the framework implies.*
- In the Monte Carlo, a planted fall of 0.05 in each land unit becomes an expected sheet-level effect of −0.035, after 30% carry-over. Power is 0.63 for the 2024 radar sample and 0.53 for UNOSAT (Table 7, p. 18).
- With the paper's own δ = 4.6% and full recognition (λ_T = 1), the sheet-level effect is about 0.7 × 0.046 ≈ 0.032.
- So power against full recognition is below two-thirds. Against λ_T = 0.5 (about 0.016) it is small.
- Table 19 makes the point concretely. The registered estimator, run on a synthetic draw with a planted effect of −0.05, gives −0.0211 (0.0123), with placebo p = 0.111 and bootstrap p = 0.131.

*What a null can mean.*
- The plan says the design cannot separate partial recognition from none.
- The paper says a null "would say that the committees do not revise flooded parcels in the first round after the flood (prediction P2 in its strong form)" (p. 19).
- P2 as written (p. 9) predicts that the response "appears in the first round after the flood". A first-round null therefore contradicts P2; it does not confirm a strong form of it.

*The estimand.*
- The difference-in-differences coefficient is the response of official values, in the first round, to a realised flood. It mixes four things:
  - physical damage;
  - updated beliefs about hazard;
  - administrative or relief-driven revision;
  - changes in the comparables the committees use.
- The framework's A = V̄(1 − λδh) has no term for realised damage, or for a change in h after a flood.
- Yet Section 6.5 says "a negative estimate would give λ_Tδ for a realised event".
- δ is not observed, because Thailand has no public transaction prices. So λ_T is not identified, and no design in the paper tests P1.

**Why it matters.** The parameter that the paper carries into the stress test (λ_T, then λ_B) cannot be recovered. The likeliest outcome, an imprecise null, is interpreted in advance in a way the design cannot support.

**What would fix it.**
1. Report the registered weighted MDE everywhere.
2. Show power as a function of λ_T for δ of 2.3%, 4.6% and 9.2%, and for realised-damage discounts of 10–20% (see M11).
3. Translate the registered equivalence margin (0.049) into the values of λ_T that a null would exclude.
4. Define the estimand as a reduced-form response. Move the λ_T interpretation into a clearly conditional paragraph that needs an outside estimate of δ.
5. Correct the reading of P2.
6. Consider a pooled or stacked 2024 + 2025 test as the primary, if timing allows (M3). The stacked row in Table 20 shows the gain in precision.

**Where.** Abstract (p. 1); introduction (p. 4); Sections 3.1 and 3.4 (pp. 8–9); Section 6.3 (pp. 17–18); Section 6.4 (pp. 18–19); Section 6.5 (p. 19); Section 10 (p. 27); Tables 6, 7 and 19.

### M3. The next round may not be able to see the floods

**What is wrong.**

*When the comparables were collected.* Committees value land by market comparison from registered transactions (Section 2.2, p. 6). Whether the next round can reflect a flood depends on when its comparables were collected, relative to the flood. The paper never discusses this.
- The plan has a timing case for comparables surveyed before the floods, in which R1, the first round after the flood, is only a placebo. For the 2025 floods it treats this as the default expectation.
- In the paper, Table 25 (p. 38) redefines case (b) as "some provinces revalue, others extend", and the survey-timing case disappears.
- Yet the 2025 sample is presented as the most powerful (MDE 0.029, power 1.00; p. 4 and p. 18).

*Whether provinces extend.* The decision to extend the current round is taken province by province, and may be endogenous. Phatthalung, one of the four provinces whose committees have considered an extension, is in the 2025 sample. If flooded provinces are more or less likely to extend, the set that revalues on time is selected on treatment.

*Re-flooding.* Under a delayed round, the 2026 floods enter as well. According to the plan, 18 of Nakhon Phanom's 25 treated sheets flooded again in 2026. Table 20 has a row that drops them, but the text does not say what it removes, or why it matters for a delayed round.

**Why it matters.** If the comparables predate the flood, the primary estimate is a placebo, and reporting a power of 1.00 for it is misleading. If extension is endogenous, the identification argument that motivates the design is weakened.

**What would fix it.**
1. Document the evidence window for the next round (the transaction cut-off dates) from public Treasury documents. If it cannot be documented, say so, and pre-specify that the 2025 event is a placebo in R1 and the primary test in R2.
2. Restore the plan's timing case in Section 6.5 and Table 25.
3. Pre-specify extension itself as an outcome (do flooded provinces extend more often?) and a way to bound its effect.
4. Discuss the 2026 re-flood in the text.

**Where.** Section 2.2 (p. 6); introduction (p. 4); Sections 6.3 and 6.5 (pp. 18–19); Table 20 (p. 37); Table 25 (p. 38).

### M4. What "flooded" means: rice paddy, one reference season and weak agreement with UNOSAT

**What is wrong.**

*The reference season.*
- A pixel counts as flooded if it is water in any scene of the season and in no scene of the same window in 2023 (Section 4.2, p. 11).
- A single reference year cannot remove "paddy that floods every year" if that year happened to be dry in a province. 2023 was an El Niño onset year, so this needs checking.
- The paper's own variant that also screens out water seen in 2021–22 removes 36 of the 198 treated sheets (18%; Table 20, row mislabelled "2019–22 round as reference"). That is direct evidence that the single reference season flags recurrent water.

*Land cover of the treated sheets.*
- Most treated sheets are mostly cropland.
- Excluding cropland leaves 32 treated sheets in 10 clusters (Table 20). The paper concedes "no power in the built-up subsample" (p. 19).

*Agreement with independent sources.*
- Against UNOSAT, the radar maps have precision 0.79, recall 0.07 and kappa 0.11.
- Against Sentinel-2, optical precision is 68.2% overall and 56.8% in Chiang Rai.

*The direction of the error.* The introduction says the maps are "conservative in the direction that attenuates rather than inflates an estimate" (p. 4). That holds when misclassification is unrelated to what the committees know. It fails if the false positives are seasonally wet paddy whose hazard the committees already price.

*Relevance to bank collateral.*
- Bank collateral is largely residential and urban, while the treated sheets are northern and north-eastern rice land.
- Section 8.2 argues that RQ1 is "a necessary input" to RQ2 and RQ3 (p. 24), through the chain λ_T to λ_B to S\*. That chain runs through a population the design cannot speak to.

**Why it matters.** Both what the treatment is (internal validity) and whom it concerns (relevance to bank collateral) depend on this.

**What would fix it.**
1. Before registration, adopt a multi-year reference period (Sentinel-1 is available from 2017), or make the 2021–23 variant the primary.
2. Report treated sheets by Global Surface Water seasonality class and by WorldCover class.
3. Report power separately for built-up and cropland sheets.
4. State the limits on external validity in the abstract.

**Where.** Section 4.2 (p. 11); Section 6.2 (p. 16); Section 6.4 (p. 19); introduction (p. 4); Section 8.2 (p. 24); Table 20 (p. 37).

### M5. Balance and common support are worse than the text says

**What is wrong.**

*Table 5 does not use the registered weights.*
- Table 5 (p. 17) shows every balancing gap at 0.00 after weighting, with 85.5 effective controls and an MDE of 0.052. These are weights without the rural indicator (`rq1_2024_pooled_balance.csv`).
- Under the registered weights (Table 16, p. 35; Table 6, p. 18), the pooled gaps after weighting are, in standard deviations, 0.08 for value, 0.32 for height, 0.13 for cropland, −0.38 for tree cover and 0.67 for water, with 98.0 effective controls.
- The text says entropy balancing "removes these gaps by construction" (p. 17), and quotes tree and water gaps of −0.26 and 0.41 from the unregistered weights.

*Phayao.*
- 25 treated sheets against 82 controls leave 13.2 effective controls.
- The fallback keeps only built-up share and the rural indicator. That leaves gaps of 0.98 on value, 0.64 on height, 1.08 on cropland, −1.39 on tree cover and 9.62 on water.

*Nakhon Phanom.* Its 981 controls shrink to 8.5 effective controls.

*UNOSAT sample.* Phayao holds 378 of the 1,214 treated sheets but only 17 controls.

*The 2025 sample.*
- Water-share gaps are 10.2 in Nakhon Si Thammarat, 10.8 in Pattani, 12.3 in Phatthalung and 7.0 in Songkhla (pooled 4.16).
- The Phatthalung height gap is 7.06.
- The text calls this "not perfect" (p. 18).
- Gaps of 7–12 standard deviations mean that the treated riverside and lagoon sheets lie outside the controls' support, so the estimate there is extrapolation.

**Why it matters.** With 21 treated clusters, a few provinces without common support can drive the estimate. A reader of Table 5 would conclude that balance is perfect.

**What would fix it.**
1. Show the registered weights in Table 5.
2. Pre-specify trimming to common support on height and water, as the primary specification or a co-primary one.
3. Report estimates and effective sample sizes province by province.
4. Remove "by construction".
5. Pre-specify an overlap rule that decides whether Phayao (and Phatthalung in 2025) stays in the primary sample.

**Where.** Section 6.3 (pp. 17–18); Tables 5, 6, 16 and 17.

### M6. The inference claims go further than the Monte Carlo

**What is wrong.**
- "The standard errors are honest" (p. 19): the mean cluster-robust (CR1) standard error is 0.013 against a sampling SD of 0.016 for radar, and 0.013 against 0.0175 for UNOSAT. That is an understatement of 20–25%, which the plan itself acknowledges.
- 100 replications give a Monte Carlo standard error of about 2.2 pp on a 5% rejection rate. "Match nominal size" therefore means somewhere between about 1% and 9%.
- The registered primary p-value comes from 1,000 placebo footprints (Table 19 note). The Monte Carlo, however, evaluates the wild cluster bootstrap. The size and power of the primary test have not been simulated.
- Lee bounds under a planted null are [−0.0275, −0.0124], which excludes zero (naive estimate −0.0197). The bootstrap confidence interval [−0.057, 0.030] does cover zero. This is one draw, but the paper does not discuss it.
- On the null draw, the H1a height interaction is −0.0056 (0.0027), a t-statistic of about 2 (Table 19).
- There are 21 treated clusters in four provinces. Wild cluster bootstraps with few treated clusters are known to be unreliable; the author may wish to consult the work of MacKinnon and Webb [to verify before citing].

**Why it matters.** The paper's credibility rests on its inference machinery, and the text claims more for it than the simulations show.

**What would fix it.**
1. Drop "honest".
2. Run at least 1,000 replications for size.
3. Simulate the placebo-footprint test itself.
4. Report how the Lee bounds and the H1a interaction behave across null draws.
5. Discuss inference with few treated clusters.

**Where.** Abstract (p. 1); introduction (p. 4); Section 6.4 (pp. 18–19); Tables 7, 19 and 21.

### M7. The cross-section: a control measured after the flood, and an understated residual gap

**What is wrong.**
- The specification "with land cover" conditions on WorldCover 2021, ten years after the flood. If the 2011 flood changed land use (through abandonment, conversion or rebuilding), land cover is a bad control. The fall from −48% to about −8% cannot then be read as "mostly land use" (Section 5.2; Section 10).
- With controls, the top urban bin is −0.083 (0.061) and the 60–80% bin is −0.087 (0.039), and the latter is significant. "A few per cent and imprecise" (abstract; p. 4) therefore understates the gap. These magnitudes are as large as the 4.6% δ the paper uses, or larger.
- Urban flood shares rest on a median of four 250 m pixels per 1:1,000 sheet, with only 17 distinct values. Measurement error is therefore severe for exactly the sheets that drive the urban result.
- The section and its three appendix tables take about five pages for an estimate the paper disowns.

**Why it matters.** The interpretive conclusion that land use explains the gap is not supported, and the space is out of proportion to the section's role.

**What would fix it.**
1. Control for land cover measured before 2011 (a 2010 global product, or Land Development Department land-use maps if they are public). Report whether the result survives.
2. Describe the controlled urban gap as "about 8% and imprecise".
3. Cut the section to about 1.5 pages, framed as motivation and as an input to the power calculations (σ and the intra-cluster correlation, ICC).

**Where.** Abstract (p. 1); introduction (p. 4); Section 5 (pp. 11–15); Tables 2–3 and Figure 2; Tables 12–14.

### M8. The RQ2 and RQ3 synthetic sections are code tests, not research results

**What is wrong.**
- Sections 7.2–7.4 and 8.1 (about four pages plus Tables 9, 10 and 24) do two things:
  - they show that an estimator recovers effects planted in a panel generated by the same model;
  - they show that bisection finds the root of the function that generated the data (S\* = 2.08 true against 2.17 recovered; median 2.18; 5–95% range 2.02–2.34).
- These are unit tests. The table notes say "not results", but the abstract counts the recovery of S\* as one of three results, and the Conclusion repeats it.

**Why it matters.** Readers judge a paper on its empirical content. A third of the paper spent on synthetic recovery dilutes the contribution and invites the reaction that the paper has no results.

**What would fix it.**
1. Move the code tests to an online appendix or the replication README.
2. Keep in the main text:
   - the RQ2 estimand and identification (one page);
   - Table 10 (power), which is genuinely useful for a data-access request;
   - half a page on the inversion.
3. Take the recovery of S\* out of the abstract.

**Where.** Abstract (p. 1); Sections 7.2–7.4 (pp. 21–23); Section 8.1 (pp. 23–24); Section 10 (p. 27); Tables 9, 10 and 24.

### M9. The illustrative stress test: misreported parameters, an unstated lending assumption and a knife-edge headline

**What is wrong.**

*The table note misstates the calibration.*
- The Table 11 note (p. 24) gives a damage share φ = 0.3 and a recovery haircut c = 0.4.
- The script (`rq3_lambda_sensitivity.py`) uses φ = 0.2 and c = 0.3. It also uses a 60/40 two-region book with flood intensity x = 0.3 and 0.05, PD0 = 2% and β_pd = 0.4. None of these is reported.
- The table's LGD of 6.0% at LTV 0.7 under λ_B = 1 reproduces only with the script's values: 1 − 0.7 × (1 − 0.2 × 0.3)/0.7 = 0.060. With the stated values it would be 0.22.

*How λ_B enters the model.*
- λ_B enters only through exposure at default, which equals book LTV times the appraisal.
- At a fixed book LTV, a bank that ignores hazard has lent more against the same parcel. The λ_B effect on S\* is therefore a true-leverage effect created at origination, not an effect of valuation on realised losses.
- The assumption that loans are written at the same book LTV whatever λ_B is never stated. If loan amounts were held fixed instead, λ_B would change reported LTV and the timing of staging and expected credit loss (ECL), not realised losses.

*The 100% result at LTV 0.7 is a kink effect.* Under λ_B = 1, S\* = 6.23 for every δ (2.3%, 4.6% and 9.2%; `rq3_lambda_sensitivity.csv`). The flooded loans do not cross the kink until a flood six times the size of 2011, so the headline is driven by the assumed c, φ and x.

*Portfolio weights.* The portfolio weights are loans by booking province, with Bangkok at 75.5%. That places corporate loans at head offices, not at their collateral.

*Two over-reaches.*
- Section 8.2 concludes that valuation pricing is "a first-order input to the breaking point, not a refinement" (p. 24). That rests on one illustrative book; at ordinary LTVs the effect is 7–9%.
- The framework says Section 8 "quantifies P5" (p. 9). Only the λ_B half of P5 is illustrated; concentration is not examined.

**Why it matters.** A reader who tries to reproduce Table 11 from its note will fail. The economic channel that drives the headline is not the one the text describes.

**What would fix it.**
1. Correct the note and report every parameter.
2. State the origination assumption, and add the variant with loan amounts held fixed.
3. Show the dependence on c and φ.
4. Replace the "first-order" conclusion with the 7–9% figure and its conditions.

**Where.** Section 3.4 (p. 9); Section 8.2 (p. 24); Table 11 (p. 24); Section 4.3 (p. 11).

### M10. The descriptive credit and price evidence is misdescribed

**What is wrong.**

*The credit series (Figure 3, Section 7.1, p. 20).*
- The flooded provinces' loan index stands at 106.0 against 108.4 for the other provinces in December 2011, 123.0 against 130.9 in January 2013, and 140.0 against 153.5 in December 2013.
- Before the flood, the difference never exceeds about 1.9 index points. After it, the gaps are −2.4, −7.9 and −13.6. By the end of 2013 the flooded provinces are about 9% lower in relative terms.
- The statement that "the gap is within the range of pre-flood differences in growth" is therefore not supported.
- All of 2012 is missing; the 2012 file (FI_CB_011_S3) was not located (`03_data/README.md`). The gap is visible in Figure 3 but not mentioned in the text.

*Reading the credit series.*
- "No fall in bank lending" (abstract) is literally true of the levels, but it hides a relative shortfall.
- The flooded provinces never rise above the others after June 2011, so there is no "credit-demand surge that reverses" to be consistent with.

*The price index (Table 8, p. 21).*
- The appraisal-based index for Bangkok and its vicinity, relative to other regions, falls 2.2% at three months, 3.4% at six and 7.3% at ten, widening steadily.
- "A transitory price dip" (abstract) and "prices dipped briefly and recovered" (Section 9.1, p. 25) contradict both the table and Section 7.1's own "slow to build" (p. 21).
- The index cannot give "a coarse view of λ_B" (p. 21), because it mixes δ, damage and λ_B across a whole region.

**Why it matters.** These are the paper's only real-data statements about credit and collateral, and as written they point the wrong way.

**What would fix it.**
1. Rewrite the descriptions to match the numbers.
2. Show the range of pre-flood differences explicitly.
3. State the 2012 gap.
4. Or move the section to an appendix figure with a neutral caption.

**Where.** Abstract (p. 1); Section 7.1 (pp. 20–21); Figure 3; Table 8; Section 9.1 (p. 25).

### M11. The contribution claims and the positioning against the literature

**What is wrong.**

*"No study traces …" (p. 4).* "No study traces observed inundation of individual collateral through official and bank valuations to default, restructuring, staging and capital" is true, but this paper does not do it either. The sentence describes the project, not the paper.

*"The first formal reverse stress test" (p. 4).* This claim is contradicted from three directions:
- Blickle, Hamerling and Morgan (2025; JMCB 2026) compute the disaster severity needed to fail a single-county bank (6.7 SD beyond the 95th-percentile event). The author's own literature review calls this "in effect a published reverse stress test on a hazard variable".
- Caloia and Jansen describe their exercise as "in essence a reverse stress test".
- The general literature on reverse stress tests is already cited.

What remains novel is solving the inversion for a scaling of the flood footprint.

*"The first test" of official land values (p. 4).* The test has not been run. Guo et al. (2026) is the analogue the claim should be positioned against.

*Citations held but never cited.* The reference list prints 53 items, although `refs.bib` holds 145 entries. The following papers are in the bibliography file but never cited:
- Blickle et al.;
- Van Gerwen et al. (2025), on a Belgian bank revaluing flooded collateral after 2021, the most direct evidence on λ_B (abstract only);
- Bernstein et al. (2019), Baldauf et al. (2020), Keys and Mulder, Sastry (2026), Lepore and Mok (2024), Dhima et al. (2026) and Kocornik-Mina et al.;
- on debt relief: Giné and Kanz (2018), Mukherjee et al. (2018), Dinerstein et al. (2024), Kim et al. (2024) and Chari et al.;
- on Thailand: Luangaram et al. (2024), Noy et al. (2021) and Chongwilaikasaem (2023);
- on assessment: Avenancio-León and Howard.

*Albertazzi et al.* The description on p. 4 has three problems:
- "No collateral values" conflicts with their LTV results for real-estate-backed micro-firm loans (their Table 17).
- "Their setting is insured" is too general for the euro area.
- The 0.7 pp needs its base of about 1.4%, which makes it a near doubling.

*The "2–8% for a realised flood" benchmark (p. 19).*
- Beltrán et al.'s 4.6% is an inland floodplain hazard discount.
- Bin and Landry's 5.7–8.8% is a flood-zone discount after hurricanes.
- Ortega and Taşpınar find 17–22% for damaged homes and 8% for undamaged flood-zone homes.
- Guo et al. report about −10% for inundated homes.

So 2–8% is a range of hazard-zone discounts. Realised-damage discounts are larger. This cuts in the paper's favour on power, but it changes the comparison the paper makes.

**Why it matters.** Over-stated novelty is the quickest way to lose a referee. The closest papers are exactly the ones a JUE or RF referee will know.

**What would fix it.** State the contribution relative to Guo et al., Garbarino and Guin, Blickle et al., Van Gerwen et al. and Chitchumnong et al. Drop "first". Cite the uncited literature. Correct the descriptions.

**Where.** Introduction (pp. 3–5); Section 6.5 (p. 19); Section 8 (p. 23); the reference list.

### M12. Source discipline on BOT and Treasury facts, and access to the replication files

**What is wrong.** The title-page footnote says that "every statement about Bank of Thailand policy or about banks' practices is taken from a cited public document". This does not hold throughout.

*Uncited statements about BOT policy.*
- The pilot climate stress test (Section 2.4, p. 7) has no citation, although a public source exists (the BOT sustainability report 2567 page in the author's policy notes).
- "The countercyclical buffer at its current zero" (Section 8.3, p. 25) has no citation.

*Citations pointing to the wrong document.*
- `bot2026priceindex`, a price-index table, is cited for commercial-bank loans by province.
- `mgr2012appraisal`, a report on Treasury land values, is cited for the moratorium at the state-owned specialised financial institutions (SFIs).
- `treasury2026extbriefing`, a Suphanburi news item, is cited for the open-data schedule and for "press reports".

*A missing source.* Trat is named but has no entry in the bibliography.

*Replication access.* The repository is presented as the replication materials, but it is private.

**Why it matters.** Any uncited statement about BOT policy invites the question of where it came from, which is exactly what the paper's own rule is meant to prevent.

**What would fix it.**
1. Correct the keys and add the missing entries (see the citation log).
2. Make the repository public, or deposit a public archive with a DOI.

**Where.** p. 1 footnote; Section 2.1 (p. 6); Section 2.2 (p. 6); Section 2.4 (p. 7); Table 1 (p. 10); Section 4.3 (p. 11); Section 6.5 (p. 19); Section 8.3 (p. 25); Table 25 (p. 38).

---

## 4. Minor points

1. **Abstract length (p. 1).** The abstract is about 330 words, well above what field journals allow; cut it to 150 or fewer. Page 2 is nearly blank because the keywords and JEL codes spill over before the `\newpage`.
2. **Abstract wording (p. 1).** "by 9% to 7%" reads backwards; write "by 7–9%".
3. **Introduction (p. 4).** "a planted −0.035 effect": the planted effect is −0.05 per land unit, and −0.035 is the expected sheet-level effect.
4. **Cross-reference to the transparency statement (title footnote, p. 1; end of introduction, p. 5).** The reference prints "Section 10", which is the Conclusion. `\section*` does not step the counter, so the label picks up Section 10. Number the section, or use `\phantomsection` with a named reference.
5. **Labels never referenced.** No labelled table or section should go uncited in the text:
   - Table 17 (`tab:unosatbalance`);
   - Table 20 (`tab:sensitivities`, mentioned only through Table 19);
   - Table 25 (`tab:timing`);
   - appendix sections `app:tables`, `app:credit` and `app:timing`;
   - equation `eq:valuer`.
6. **The 2025 event (Section 4.2, p. 11).** The sentence "A pixel is flooded in the 2024 season (15 August to 31 October in the north; 15 November to 31 December 2025 in the south)" is garbled.
   - The 2025 sample is not "southern": five of its nine provinces (Phitsanulok, Phichit, Phetchabun, Nakhon Phanom and Nakhon Sawan; 231 of the 437 treated sheets) use the northern August–October window.
   - Rename the event.
   - Say whether circular ว. 8158/2568, which the paper ties to the southern floods, covers these provinces.
7. **Grid size (Section 4.2, p. 11).** The text says "80 m grid", but the script uses a 0.001° grid (about 105–111 m at these latitudes). Reconcile.
8. **UNOSAT treatment (Sections 6.1–6.2).** The treatment threshold for the UNOSAT sample is not stated in the paper (the plan says more than 25%).
9. **Contaminated controls (Section 6.2, p. 16).** "Almost all of them in Nong Khai": the split is 18 of 24, with 3 in Chiang Rai and 3 in Nakhon Phanom. "Three-quarters" is accurate.
10. **Pilot sample (Section 5.1, p. 12).** "41,507 sheets": the estimation sample is 41,049 sheets (28,868 urban and 12,181 rural). The other 458 have no flood data.
11. **Weights in Table 5.** Table 5 against Tables 6 and 16: 85.5 against 98.0 effective controls, and an MDE of 0.052 against 0.053. Use the registered weights throughout (M5).
12. **Control counts in the sensitivities (Section 6.4, p. 19, against Table 20).** The text gives 8,591 controls without the height cap (the sample file), while Table 20 gives 8,584 (the estimation sample). Likewise, the 10% threshold has 399 treated and 2,458 controls against 398 and 2,455, and the 20-province threshold has 3,910 controls against 3,904. Report the estimation counts and explain the drops.
13. **Table 18 against Table 6.** The "at least 25 treated" row uses 2,373 radar-only controls and an MDD of 23.3, while Table 6 uses 1,891 and 23.5. Say so in the note.
14. **Mislabelled row in Table 20 (p. 37).** "2019–22 round as reference" should read "2021–23 radar reference" (the label comes from `paper_numbers.py`, line 454). As written, it implies an earlier valuation round exists, which contradicts "no earlier round is public" (Section 9.2, p. 26).
15. **Declared-district rows (Table 20; Section 6.4, p. 19).** The declared-district and declared-tambon rows are identical (1,361 controls; −0.0110 (0.0198); p = 0.651). Both use a stand-in list (every district holding a treated sheet; `rq1_declarations.py`), because the DDPM lists have not been obtained. Say so, and drop "declarations cover most of the floodplain", which has no source.
16. **The 2011 cross-section (Section 5, p. 11).** "Twelve years after the 2011 flood": the 2023–26 values rest on evidence from about 2021–22, so write "about ten years".
17. **Price index wording (Section 7.1, p. 21).** "fell by −2.2%" is a double negative; write "fell by 2.2%".
18. **Price index source.** The data section (p. 11) attributes the index to "a bank's appraisal data", while the Table 8 note says "lenders'". Make the two consistent and cite the BOT methodology note.
19. **NPL forecast (Section 2.1, p. 5).** "About half a percentage point": the source says "about 0.5%". Quote its unit.
20. **CCDR shares (Section 2.4, p. 7).** The 41% and 7% refer to the sample banks' corporate lending; say so.
21. **Moratorium source (Section 2.1, p. 6).** Cite the 15 November 2011 press report of the Cabinet resolution for the SFI moratorium.
    - Then use the 15 June 2012 report for what it actually says. According to the claims ledger, the Treasury found no post-2011 fall in flooded areas, left its late-2011 schedule unrevised, and raised values by 21.34% on average.
    - That is direct, public evidence on P2 for the 2011 event, and the paper does not use it.
22. **δ = 4.6% (p. 4, p. 24).** The figure is Beltrán et al.'s inland floodplain discount; cite it each time it is used.
23. **Sawada et al. (p. 4).** Add that residential and commercial land show no significant change.
24. **Chitchumnong et al. (Section 9.1, p. 25).** "Among relief-eligible borrowers" is more specific than the paper's own summary on p. 4; check it against the source.
25. **Caloia and Jansen.** Cite the published Caloia, van Ginkel and Jansen (2026) version, which `refs.bib` already holds. The author's notes describe it as a forward exercise with fixed scenarios, so check that the "reverse stress test" description survives.
26. **Guo et al.** The bibliography key `guo2025rising` does not match the year 2026. Add the point that assessment caps blunt pass-through, which bears directly on λ_T.
27. **Circular 601 (introduction, p. 3; Section 2.1, p. 6).** According to the author's policy notes, the trigger includes yellow, orange and red alert levels as well as zone declarations. Calling a circular that requests cooperation a "standing rule" is too strong.
28. **Figure 1 (p. 12).** The figure repeats its notes inside the image; remove them.
29. **Table layout (p. 38).** The header of Table 24 is misaligned, and Table 25 is cramped.
30. **Length.** The paper has 38 pages, 25 tables and 3 figures, and about half the tables are synthetic or about the design. A main text of about 25 pages with eight tables or fewer would read far better.
31. **Long sentences in Section 6.** The section carries registration detail (the fallback order, file names, hash rules) in very long sentences. Move it to the plan, and keep in the paper what a reader needs in order to judge identification.
32. **Spelling.** British spelling is consistent; I found no American forms in the sections. The tone is generally measured, apart from the sentences listed in Section 6.

---

## 5. Verification log

**Method.**
- Numbers were checked against `04_analysis/outputs/tables/*.csv`, against the macros in `paper/numbers.tex` (generated by `04_analysis/src/paper_numbers.py`), and, where needed, against the generating scripts.
- Citations were checked against `paper/refs.bib`, the author's literature matrix and notes (`01_literature/`), the policy notes (`02_policy_context/`), `03_data/README.md` and `04_analysis/treasury_2027_round_status.md`.
- I did not re-open the publishers' pages. Verdicts on the content of the comparison papers rest on the author's recorded read depth, which is often abstract or introduction only.

### 5.1 Numbers checked

| # | Quantity (location in paper) | Value in paper | Value in CSV | File | Verdict |
|---|---|---|---|---|---|
| 1 | Top urban flood-share bin, no controls (Table 2; abstract) | −0.647 (0.104), "48% lower" | −0.6470; exp(−0.647) − 1 = −0.476 | `appraisal_flood_binned.csv` | OK |
| 2 | Top urban bin, with land cover (Table 2) | −0.083 (0.061), "a few per cent" | −0.083 (0.061) | `appraisal_flood_binned.csv` | Number OK; wording understates it (M7) |
| 3 | Top rural bin, no controls (Table 2) | −0.271 (0.071), 24% | −0.27120 (0.07124) | `appraisal_flood_binned.csv` | OK |
| 4 | Rural bins with land cover (Table 2) | +0.063 to +0.083 | match | `appraisal_flood_binned.csv` | OK |
| 5 | Within-cell slopes (Table 3) | Rural −0.488 (0.106); urban −0.650 (0.098); p90 −0.733 / −0.815; clusters 108 / 95 | −0.48765 (0.10626); −0.65013 (0.09770); −0.73259 / −0.81466; 108 / 95 | `appraisal_flood_within.csv` | OK |
| 6 | Pilot sheets (Section 5.1, p. 12) | 41,507 | 41,049 with flood data (28,868 + 12,181); 41,507 = 29,207 + 12,300 including sheets with no flood data | `flood_share_support.csv`, `pilot_parcel_reconciliation.csv` | **MISMATCH** |
| 7 | Pilot parcels (Section 5.1) | 8,775,877 | 8,775,877 (5,074,885 + 3,700,992) | `pilot_parcel_reconciliation.csv` | OK |
| 8 | Land cover by bin (introduction, p. 4; Table 14) | Built-up 14 against 36; cropland 48 against 23 | 13.70 / 36.09; 47.6 / 22.5 | `landcover_by_flood_bin.csv` | OK |
| 9 | Flood-share support | Zero shares 72.3 / 52.2; interior 13.5 / 36.8; median pixels 4 / 64 | 0.7234 / 0.5220; 0.1353 / 0.3684; 4 / 64 | `flood_share_support.csv` | OK |
| 10 | Discreteness (Table 12) | 38 / 5; 196 / 11 | match | `sheet_price_discreteness.csv` | OK |
| 11 | Coverage (Section 4.1) | 37,806,594 parcels; 317,081 sheets; 95.8 / 74.9 / 81.8%; 51 provinces | match | `sheet_panel_coverage.csv`, `province_flood_share_2011.csv` | OK |
| 12 | 2011 flood share (Table 13) | Ayutthaya 64.6%; Bangkok 2.5% | 0.6459; 0.0247 | `province_flood_share_2011.csv` | OK |
| 13 | Optical validation (Table 4, p. 16) | Contamination 1.3%; precision 68.2%; Chiang Rai 56.8; Nakhon Phanom 88.0; Nong Khai 5.4% (18); median new water 24.6 | match | `s1_s2_validation.csv` | OK |
| 14 | Contaminated controls "almost all in Nong Khai" (p. 16) | "almost all" | 18 of 24 (Chiang Rai 3, Nakhon Phanom 3) | `s1_s2_validation.csv`; plan | **Wording mismatch** |
| 15 | UNOSAT agreement (Section 6.2) | Precision 0.79; recall 0.07; agreement 0.85; kappa 0.11; correlation 0.35; 7,900 / 1,214 / 114 / 90 | match | `s1_unosat_validation.csv` | OK |
| 16 | Unweighted SMDs (Table 5) | Value −0.41; built-up −0.68; cropland 0.52 | match | `rq1_2024_pooled_balance.csv` | OK |
| 17 | Weighted gaps and ESS (Table 5; text, p. 17) | All 0.00; tree −0.26; water 0.41; ESS 85.5; MDE 0.052 | Registered weights: 0.08 / 0.32 / 0.13 / −0.38 / 0.67; ESS 98.0; MDE 0.053 | `rq1_2024_pooled_balance.csv` against `rq1_round_change_balance.csv` | **INCONSISTENT** (two weight sets; M5) |
| 18 | Phayao and Nakhon Phanom ESS (Table 16) | 13.2; 8.5 | match | `rq1_round_change_balance.csv` | OK |
| 19 | Power inputs (Section 6.3) | MDE 0.047; ICC 0.05 gives 0.030; ICC 0.5 gives 0.070; SD 0.20 gives 0.094; equivalence 0.049; carry-over 23.5 | 0.04696, etc. | `rq1_2024_pooled_mde.csv` | OK |
| 20 | MDE quoted in the abstract and introduction | 0.047 | Registered weighted 0.053 (Table 6) | `rq1_round_change_balance.csv` | **INCONSISTENT** (unweighted figure headlined) |
| 21 | "MDE of 3–5 log points" (p. 19, p. 27) | 3–5 | 2024 radar 5.3; UNOSAT 6.1–6.5; 2025 2.9–3.0 | Table 6 sources | **Understated** |
| 22 | Monte Carlo (Table 7) | Size 0.05, power 0.63 (radar); 0.03 / 0.53 (UNOSAT); 0.04 / 1.00 (2025); mean −0.035; SD 0.016; SE 0.013 | −0.0353; 0.0162; 0.0127 | `rq1_round_change*_montecarlo.csv` | Numbers OK; the "honest SE" claim is not supported (M6) |
| 23 | One synthetic draw (Table 19) | −0.0211 (0.0123); placebo p 0.111; bootstrap p 0.131; unweighted −0.0312 (0.0117) | match | `rq1_round_change_synthetic.csv` | OK |
| 24 | 2025 sample (Table 6; p. 18) | 437 / 7,664 / 134 / 49; MDE 0.029 / 0.030; ESS 633.6; Phatthalung height gap 7.1; water gap 4.16 | match (7.06) | `rq1_round_change_2025_balance.csv`, `rq1_sample_sensitivity.csv` | OK |
| 25 | UNOSAT sample (Table 6, Table 17) | ESS 103.9; gaps 0.68 / 0.52 / −0.63 | match | `rq1_2024_balance.csv`, UNOSAT balance file | OK |
| 26 | No height cap, controls (p. 19 against Table 20) | 8,591 (text); 8,584 (Table 20) | 8,591 in the sample file; 8,584 in the estimate | `rq1_sensitivity_samples.csv`; `rq1_round_change_sensitivities_synthetic.csv` | **MISMATCH** (text against table) |
| 27 | 10% threshold; at least 20 treated per province (Table 20) | 398 / 2,455; 3,904 | Sample files 399 / 2,458; 3,910 | same | **INCONSISTENT** (unexplained drops) |
| 28 | At-least-25 row (Table 18 against Table 6) | 2,373 controls, MDD 23.3 | Table 6: 1,891, 23.5 | `rq1_sample_sensitivity.csv` | **INCONSISTENT** (different control definition, not stated) |
| 29 | Table 20 row label | "2019–22 round as reference" | variant `ref2123`, the 2021–23 radar reference | `paper_numbers.py` l. 454 | **MISLABEL** |
| 30 | Declared-district and declared-tambon rows (Table 20; p. 19) | 1,361; −0.0110 (0.0198); p 0.651 (both rows) | identical; stand-in list from `rq1_declarations.py` | `rq1_round_change_sensitivities_synthetic.csv` | Numbers OK; **description misleading** |
| 31 | Cropland excluded; 2021–23 reference (Table 20) | 32 treated, −0.0072 (0.0132); 162 treated | match | same | OK |
| 32 | Lee bounds (Table 21) | Planted −0.05: naive −0.0568, [−0.0773, −0.0356], trim 9.5; null: [−0.0275, −0.0124] | match | `rq1_lee_bounds_synthetic.csv` | Numbers OK; the null result is not discussed (M6) |
| 33 | Table 11 parameters (note, p. 24) | φ = 0.3, c = 0.4 | Script: φ = 0.2, c = 0.3; weights 60/40; x = 0.3 / 0.05; PD0 0.02; β_pd 0.4 | `rq3_lambda_sensitivity.py` | **MISMATCH** |
| 34 | Table 11 values | S\* 2.31 → 2.52 (+9%) at LTV 0.8; 1.52 → 1.62 (+7%) at 1.0; 3.11 → 6.23 (+100%) at 0.7; LGD change 3.8 pp; 4% / 3% when δ is halved; 19% / 14% when doubled | 2.3118 → 2.5229; 1.5200 → 1.6238; 3.1142 → 6.2268; 3.78; 0.045 / 0.034; 0.191 / 0.140 | `rq3_lambda_sensitivity.csv` | OK |
| 35 | Synthetic S\* (Section 8.1; abstract) | 2.08 true, 2.17 recovered; median 2.18; 5–95% 2.02–2.34 | 2.076 / 2.169; match | `rq3_synthetic_sstar.csv` | OK |
| 36 | RQ2 recovery (Table 9) | 0.0460 (0.0032) … gap −0.0406 | match | `rq2_synthetic_recovery.csv` | OK |
| 37 | RQ2 power (Table 10) | 4,283 / 1,071 / 8,740 / 19,022; MDE 2.07 / 1.46 | match | `rq2_power_2024.csv` | OK |
| 38 | RQ2 equivalence (Table 24) | 13,155 / 2,193 | match | `rq2_power.csv` | OK |
| 39 | Credit index (Section 7.1; Figure 3) | 106.0 / 108.4; 123.0 / 130.9; 140.0 / 153.5 | match | `fig_provincial_credit_2011_data.csv` | Numbers OK |
| 40 | "Gap within the range of pre-flood differences" (p. 20) | within range | Pre-flood maximum difference about 1.9 points; post-flood −2.4 / −7.9 / −13.6; 2012 missing | `fig_provincial_credit_2011_data.csv` | **NOT SUPPORTED** |
| 41 | Provincial credit drift (Table 23) | 0.080 / 0.043 / 0.062 / 0.055 | match | `credit_share_drift.csv` | OK |
| 42 | Bangkok share of loans (Section 4.3) | 75.5% | 0.7555 | `credit_shares_allocation.csv` | OK |
| 43 | Price index, Bangkok relative (Table 8) | −2.2 / −3.4 / −7.3 at 3 / 6 / 10 months | match | `rppi_flood_windows.csv` | Numbers OK; "transitory" and "recovered" are **NOT SUPPORTED** |
| 44 | Registered sample hashes (Table 22) | 17 files | 17 | `registration_hashes.csv` | OK |

In total, 44 checks: 28 OK; 16 mismatches, inconsistencies or unsupported readings.

### 5.2 Citations checked

| Key | Claim in paper (location) | Verdict | Note |
|---|---|---|---|
| `mgr2012appraisal` | The SFI moratorium was conditioned on pre-flood debt status, not flooding (Section 2.1, p. 6) | **Mis-cited** | The entry is MGR, 15 June 2012, on the Treasury confirming new land values ("flooded areas not affected"). The moratorium source in the policy notes is MGR, 15 November 2011 (`mgr2011cabinetmoratorium`), which is missing from `refs.bib`. The 2012 article's own content bears on P2 and is not used |
| `treasury2026extbriefing` | "The parcel-level schedule is published as open data" (Section 2.2, p. 6; Table 1, p. 10) | **Mis-cited** | The entry is a Suphanburi provincial news item (28 October 2026) on an extension briefing. Cite data.go.th/dataset/land-valuation (`03_data/README.md`) |
| `treasury2026extbriefing` | "Press reports in 2026 anticipated an announcement on 1 December 2026" (Section 6.5, p. 19) | **Mis-cited** | A Treasury provincial news item is not a press report. Cite the item that carries the date. Suphanburi is in the bibliography but is never named in the text |
| (none) | The Trat committee is considering an extension (Section 6.5, p. 19; Table 25 note, p. 38) | **Uncited** | A source exists in the author's notes (treasury.go.th provincial news, 3 November 2026, item 336). Add an entry |
| `bot2026priceindex` | Commercial-bank loans by province, monthly from 1996 (Table 1, p. 10; Section 4.3, p. 11) | **Mis-cited** | The entry is the land and residential price index table (EC_EI_008_S3). The loans series is FI_CB_011 (reportIDs 173/781/1008; data.go.th ds-459) |
| (none) | BOT pilot climate stress test, "starting with physical risk" (Section 2.4, p. 7) | **Uncited (BOT rule)** | A public source exists: the BOT sustainability report 2567 page in the author's policy notes |
| (none) | Countercyclical buffer "at its current zero" (Section 8.3, p. 25) | **Uncited (BOT rule)** | A time-sensitive policy fact; cite it with an as-of date |
| `bot2024circular601` | "Standing rule"; relief in "areas declared disaster zones" (p. 3; Section 2.1, p. 6) | Partly supported | According to the policy notes, the trigger includes alert levels as well as declarations, and the document is a request for cooperation |
| `albertazzi2026physical` | Default up by about 0.7 pp; "no collateral values … their setting is insured" (p. 4); a credit surge that reverses (p. 20) | Partly supported | 0.57 pp after one quarter and 0.64–0.69 pp over two, on a base of about 1.4%. Their Table 17 uses LTV for real-estate-backed micro-firm loans. The surge (+3.5% to +5%) and its reversal are supported |
| `perezmontes2025impact` | Stage 2 up by about 0.5 pp; the most exposed banks move more loans into stage 2 and fewer into stage 3 under moratoria; four months (p. 4) | Supported | Banks with more than 40% exposure: stage 2 +24%, stage 3 −9% |
| `garbarino2021high` | Prices fell but lenders' valuations did not; bias of about 3% (p. 4) | Supported | Valuation differential +3.2%; prices −2.6% to −4.2% |
| `guo2025rising` | NYC assessments fell for inundated homes, largely through relief; not for undamaged high-risk homes (p. 4) | Supported; key and year mismatch | Assessed value −17%, mostly through relief. The key says 2025, the entry 2026. Assessment caps are not mentioned |
| `caloia2021flood` | "In essence a reverse stress test"; strongly non-linear capital depletion (p. 4; Section 8, p. 23) | Supported; outdated version | The published 2026 JFS version (Caloia, van Ginkel and Jansen; in `refs.bib`) is described in the notes as a forward exercise with fixed scenarios |
| `chitchumnong2025physical` | One bank's mortgage book; default below predicted because of relief; no geolocation, collateral values or staging (p. 4); "among relief-eligible borrowers" (p. 25) | Mostly supported | The wording on p. 25 is more specific than the summary on p. 4 |
| `sawada2018land` | Industrial land prices fell 6–8% after 2011 (p. 4) | Supported; incomplete | 8.27% and 6.49%. The non-significant residential and commercial results are omitted |
| `beltran2018flood`, `bin2013changes`, `ortega2018rising` | "A full-information discount that the advanced-economy literature puts at 2–8% for a realised flood" (p. 19) | **Not supported** | 4.6% is a floodplain hazard discount; 5.7–8.8% is a post-hurricane flood-zone discount; Ortega and Taşpınar find 17–22% for damaged homes. 2–8% is a range of hazard discounts |
| (none) | δ = 4.6% (p. 4; Section 8.2, p. 24) | **Uncited in text** | Beltrán et al.'s figure, cited only in the script's docstring |
| `worldbank2012thai` | THB 1.43 trillion; about 90% private; fewer than 1% of dwellings insured; NPL ratio up by about 0.5 (p. 5) | Supported | The source says "about 0.5%"; the paper says "half a percentage point" |
| `tellman2021satellite` | Global Flood Database about 83% accurate against Landsat (Section 4.2, p. 11) | Supported | |
| `worldbank2026ccdrfin` | 41% and 7% of corporate lending; 2011 a 1-in-50-year event (p. 7) | Supported; wording | The figures refer to the sample banks' corporate lending |
| `swissre2022extreme` | Insurance covers a small fraction of emerging-market flood losses (p. 3) | Supported | About 5% insured |

In total, 21 citation checks: 5 supported as written; 7 supported but needing a correction (wording, version, key or omitted finding); and 9 mis-cited, uncited or not supported. The mis-citations involve three keys in four places.

### 5.3 Predictions against what is tested (internal consistency)

| Prediction | What would test it | Status in the paper |
|---|---|---|
| P1: λ_T between 0 and 1 | Capitalisation of hazard in official values; needs δ | **Not tested by any design.** The cross-section is disowned, the difference-in-differences measures a realised-flood response, and δ is not observed |
| P2: partial and lagged; appears in the first round | The RQ1 difference-in-differences | Design only. Section 6.5 reads a null as "P2 in its strong form", but P2 as written predicts a first-round response |
| P3, P4 | RQ2 with loan-level data | Synthetic only, and they hold by construction (stated) |
| P5: concentration and λ_B | RQ3 | Only the λ_B part is illustrated, on a two-region book; concentration is not examined. The framework's "quantifies P5" over-states this |
| P6: relief and short-run against lifetime S\* | RQ3 with relief | Not exercised; Section 8.3 lists it as future work |

λ_T and λ_B are kept apart carefully in Sections 2.3 and 3. The separation slips in Section 7.1 (the price index as "a coarse view of λ_B") and in Section 8.2 ("a necessary input"). The status of RQ1 is stated consistently: the title page, abstract, introduction and Section 6.5 all say the estimate does not exist. The exception is the word "pre-registered" (M1).

### 5.4 Checks against the project's rules

- **Non-public information.** None found. All substantive BOT policy statements are tied to public circulars, except the two uncited statements and the mis-cited loans series in M12.
- **Author-specific facts.** These are bracketed placeholders (`\pending{…}`) in the title footnote and the transparency statement. No invented author facts were found.
- **Labelling of synthetic output.** Table notes say "not results" or "not data". But the abstract ("Three results are reported"), the introduction ("Fourth, in the stress test …") and the Conclusion present synthetic and illustrative output as findings.
- **Traceability.** Every number is a macro generated from script outputs. The mismatches are listed in Section 5.1.
- **Public data only.** Satisfied. The DDPM declaration list is a synthetic stand-in, and the paper does not say so.
- **Tone and hype.** See Section 6.

---

## 6. Over-claiming and tone

| # | Sentence as written (location) | Problem | Suggested replacement |
|---|---|---|---|
| 1 | "Three results are reported, with their status marked." (abstract, p. 1) | Only one result is a result | "The paper reports one descriptive result, a pre-specified design whose estimate awaits the next valuation round, and tested code for the credit and capital steps." |
| 2 | "a pre-registered difference-in-differences design" (abstract; also p. 3, Section 6 title, p. 25, p. 27) | Not registered | "a pre-specified (registration pending) difference-in-differences design" |
| 3 | "the design detects a 0.047 log-point change at 80% power, and Monte Carlo rejection rates match nominal size" (abstract) | Unweighted MDE; 100 replications | "the registered design has a minimum detectable effect of 0.053 log points at 80% power, about the size of a fully recognised 4.6% discount, and its rejection rate under the null is close to 5% in 100 replications" |
| 4 | "Descriptive public credit data around 2011 show no fall in bank lending in the most flooded provinces and a transitory price dip." (abstract) | Contradicted by Figure 3 and Table 8 | "Lending in the most flooded provinces kept growing after 2011 but by the end of 2013 was about 9% below the other provinces; the appraisal-based price index for Bangkok and its vicinity fell steadily relative to other regions over the ten months after the flood." |
| 5 | "Three features make the country an unusually clean laboratory rather than a local case study." (p. 3) | Hype | "Three features make Thailand a useful laboratory." |
| 6 | "The paper also contributes, as far as I can find, the first formal reverse stress test that solves for the flood severity breaching a capital threshold, and the first test of whether an emerging market's official land values respond to a satellite-measured flood." (p. 4) | Contradicted by Blickle et al.; the test has not been run | "The paper sets out a reverse stress test that solves for the flood severity breaching a capital threshold, building on the breaking-point calculation of Blickle et al., and a design to test whether official land values respond to a satellite-measured flood, the emerging-market counterpart of Guo et al.'s test for New York City assessments." |
| 7 | "No study traces observed inundation of individual collateral through official and bank valuations to default, restructuring, staging and capital, and none does so where relief rather than insurance is the buffer." (p. 4) | Neither does this paper | Keep only if followed by: "This paper sets out how to do so and takes the first, public-data step; it does not yet trace the chain." |
| 8 | "the maps are conservative in the direction that attenuates rather than inflates an estimate" (p. 4) | True only for misclassification unrelated to what the committees know | "if misclassification is unrelated to the committees' information about hazard, it attenuates the estimate" |
| 9 | "the residual gap is a few per cent and imprecise" (p. 4; similar in abstract) | −8.3% (6.1) and −8.7% (3.9) | "the residual urban gap is about 8% and imprecise, with land cover measured ten years after the flood" |
| 10 | "Entropy balancing removes these gaps by construction" (p. 17) | False under the registered weights | "Under the registered weights the pooled gaps on the balancing variables fall to 0.08–0.32 SD, but not in Phayao, where the fallback leaves gaps of up to 1.08 SD." |
| 11 | "so the estimator is unbiased and the standard errors are honest" (p. 19) | The SE understates the SD by about a fifth | "so the estimator is close to unbiased; the cluster-robust standard error understates the sampling SD by about a fifth, which is why inference rests on the wild bootstrap and placebo footprints" |
| 12 | "A null at that precision would say that the committees do not revise flooded parcels in the first round after the flood (prediction P2 in its strong form)" (p. 19) | The design cannot separate partial recognition from none; P2 predicts a first-round response | "A null at that precision cannot distinguish partial recognition from none; the registered equivalence margin of 0.049 would rule out only responses larger than a fully recognised hazard discount." |
| 13 | "a negative estimate would give λ_Tδ for a realised event" (p. 19) | Not identified | "a negative estimate would measure the first-round response to realised flooding, which combines damage, updated hazard and administrative revision" |
| 14 | "declarations cover most of the floodplain" (p. 19) | No source; stand-in list | Cut |
| 15 | "the gap is within the range of pre-flood differences in growth" (p. 20) | Contradicted by the data | "the gap is several times larger than any pre-flood difference, though the series are two aggregates with no counterfactual and 2012 is missing" |
| 16 | "it is consistent both with the European pattern of a brief credit-demand surge that reverses" (p. 20) | No surge visible | Cut |
| 17 | "and so gives a coarse view of λ_B" (p. 21) | The index cannot separate λ_B from δ | "and is the only public series that bears on bank valuations, although it cannot separate λ_B from the discount itself" |
| 18 | "Whether official and bank valuations price hazard is a first-order input to the breaking point, not a refinement, so Question 1 is not a detour from the credit questions but a necessary input to them." (p. 24) | Rests on one illustrative book | "In this illustrative book, valuation pricing moves the breaking point by 7–9% at ordinary loan-to-value ratios and by much more at low ratios, where the result depends on the assumed damage share and haircut." |
| 19 | "prices dipped briefly and recovered" (p. 25) | Contradicted by Table 8 | "the regional appraisal index fell relative to other regions for at least ten months" |
| 20 | "Section 8 quantifies P5 under an illustrative calibration" (p. 9) | Only half of P5 | "Section 8 illustrates the λ_B part of P5" |
| 21 | "since 2024 the same template is a standing rule" (p. 3); "The 2011 template became a standing rule in 2024." (p. 6) | Over-states a circular that requests cooperation | "since 2024 a standing circular has asked institutions to apply the same template" |
| 22 | "an estimator whose size and power are verified by Monte Carlo" (p. 27) | 100 replications; the primary placebo test is not simulated | "an estimator whose size is checked in 100 Monte Carlo replications of the wild bootstrap" |

---

## 7. What the paper should do next, in priority order

1. **Fix the errors listed in Section 5 before anyone else reads the paper.** These cost little:
   - the Table 11 parameters;
   - the four mis-citations, the uncited Trat entry, the uncited δ and the two uncited BOT statements;
   - the credit and price descriptions;
   - Table 5 against the registered weights;
   - the 41,507 sheets;
   - the declared-district rows;
   - the "2019–22" label;
   - the "Section 10" cross-references;
   - the MDE quoted in the abstract.
2. **Register the plan or stop calling it pre-registered.** Register on OSF and make the registered commit (or a DOI archive) public. Otherwise replace "pre-registered" everywhere.
3. **Settle survey timing from public Treasury documents.** Restore the plan's timing case. Say what the 2025 event can and cannot show in R1. Pre-specify extension as an outcome, and discuss the 2026 re-flood.
4. **Rework the treatment and overlap rules before registration:**
   - a multi-year radar reference period;
   - a pre-specified rule for trimming to common support on height and water;
   - results by land-cover class;
   - power re-run and reported as a function of λ_T, and for realised-damage discounts.
5. **Redefine the estimand and the reading of a null.** Treat the coefficient as a reduced-form first-round response. Report the equivalence bound in λ_T terms. Correct P2 and the framework's claim about P5.
6. **Restructure around RQ1.** Aim for a main text of about 25 pages:
   - institutions;
   - a short framework;
   - data and validation;
   - design, power and timing;
   - the cross-section as a short motivating section with a pre-2011 land-cover control.

   Move the RQ2 and RQ3 synthetic material to an appendix or a separate methods note, keeping Table 10 and a short statement of the inversion.
7. **Reposition the contribution** against Guo et al., Garbarino and Guin, Blickle et al., Van Gerwen et al. and Chitchumnong et al. Drop "first", cite the uncited literature, and correct the descriptions of Albertazzi et al. and of the 2–8% benchmark.
8. **Strengthen the inference evidence:**
   - at least 1,000 Monte Carlo replications;
   - a simulated placebo-footprint test;
   - the behaviour of the Lee bounds and the H1a interaction across null draws;
   - discussion of inference with few treated clusters.
9. **Add a real result that can arrive before R1.** Two options:
   - the public-data Plan B for RQ2 (listed-bank stage 2 and relief disclosures against the World Bank exposure mapping);
   - the public 2012 evidence on whether the Treasury revised flooded areas after 2011.

   Either would give the paper an empirical anchor while the valuation round is awaited.

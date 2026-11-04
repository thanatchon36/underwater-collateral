# Author notes: §4 Methods

> **Phase 7 revision (2026-11-02).** The section was revised after referee rounds 1 and 2 and the citation audit. `07_review/revision_log.md` records each change and its reason. The reasoning below is the Phase 6 draft and may describe designs since replaced, such as the triple difference and the old hypothesis labels.


Working draft, 2026-11-02 (Phase 6). The full detail is in `05_design/identification.md` and `framework.md`.

## Reasoning

- **RQ1 outcome.** The sheet p90 is the outcome because parcel values are unit price × depth × shape factors, rounded (`treasury_method_notes.md` §1a).
- **Three RQ1 designs.** They answer the amenity threat in increasing order of credibility: cross-section, then boundary design, then the change across rounds.
- **RQ2 triple difference.** It uses the eligibility rule in circular 1564/2554.
- **RQ3.** It is an inversion with a monotonicity lemma; uncertainty comes from parameter draws.

## Weak points

- **Pre-trends for Design 1c.** They cannot be tested without earlier rounds, which are not public. A partial placebo exists: 2011-flooded sheets that were not flooded in 2024.
- **Comparison group in the triple difference.** The ineligible group is small and noisy; this shows in the synthetic run (`tier2_pipeline_notes.md`).
- **λ_T.** It is only partially identified, as a range against external benchmarks.
- **RQ3 limits.** Exogenous prices bias S* upwards, towards apparent safety.

## Round 2 changes and remaining weak points (2026-11-02)

- **RQ1 design order reversed.** The round-to-round design is now primary because the 2011 edge cannot be run on urban sheets: 86% of 500 m sheets have a GFD share of exactly 0 or 1 (`04_analysis/outputs/tables/flood_share_support.csv`). The edge design survives on rural 2 km sheets only.
- **Weak point: the primary design does not exist yet.** It needs the 2027–30 round, whose release date and market-data cut-off are unconfirmed. If the cut-off precedes the 2024 floods, the first post-flood round is 2031–34, published by December 2030 (Year 3), and Chapter 2 is finished on it.
- **Weak point: managed edge segments.** No public source of 2011 flood-management records has been located. Without one, the exclusion rule cannot be applied as written.
  - *Update 2026-11-02:* a partial public source exists. JICA (2013), Vol. 2, Table 3.2.1 (printed p. 3-3, bib `jica2013cfmp`) lists 18 dike-break, overflow and gate-opening sections with coordinates and dates, 13–22 Sep 2011, in Chai Nat, Sing Buri, In Buri and at the Phra Ngam gate; Figure 3.2.1 maps them. That lets edges next to a breach be flagged. Sandbag lines and temporary barriers near Bangkok are described only in prose and timelines, not as coordinates, so a complete managed-edge layer is still missing.
- **Weak point: 2011 difference-in-discontinuities.** It needs pre-flood classification and a flooded/unflooded split within one bank's book; days past due can be moved by a single payment, so manipulation tests are required.
- **λ_B.** The loan schema already holds `collateral_value_thb`, `valuation_month` and `valuation_method`, so λ_B relative to λ_T is identifiable if a bank provides them. This is the main repair of the chain and is worth stressing to a data partner.
- **RQ3.** The staged-ECL equation and the frontier reporting answer the referee; the contribution is now modest by design and should be defended as such.

## Round 3 revisions (2026-11-02)

- **RQ1 primary design.** Within-province (Chiang Rai, Phayao) comparisons, same map scale, province × round effects. Placebo footprints test spurious spatial association only; pre-trends need earlier, non-public rounds (to request). Controls drop a 5 km buffer and sheets flooded in late 2025. The 5 km and 1-in-1,000-year values are design choices to defend and fix in the pre-analysis plan, not facts.
- **Outcome.** Mean over a sheet's distinct values approximates land units; it assumes parcels in one land unit share a value, which the published data suggest but no document states. Weak point.
- **Edge design.** Identifies the effect of having been flooded in 2011, not hazard capitalisation. Hazard heterogeneity now sits in H1b.
- **RQ2 2011.** The days-past-due threshold between special mention and substandard is *not yet sourced*; the text is conditional ("as I will confirm"). Find the public classification notification in force in 2011.
- **RQ2 2025.** Eligibility (retail and SME debtors not NPL on 2 Dec 2025) and the repair-loan LTV and risk-weight relief come from circular ว.8158/2568. Area (verified 2026-11-02, ว.8158 p. 1): Level-4 areas declared under s. 31 of the 2007 Act, the example given being Prime Minister's Order 10/2568 for areas of Songkhla; no other Level-4 area found. The Cabinet resolution of 2 Dec 2025 sets only the date and a separate SFI moratorium in DDPM-declared areas (12 southern provinces). So the commercial-bank relief boundary is, on present evidence, Songkhla's provincial border: flooded borrowers in neighbouring provinces got ว.601 template relief, not nothing (moratorium vs lighter relief, confounded with province-wide shocks). Cleaner variation lies inside Songkhla (radar-flooded vs unflooded sheets; the THB 3 m per-group limits fixed on 2 Dec 2025, Q&A 4). Measurement warning: item 2.6 (scanned p. 4) lets lenders hold days past due at the pre-disaster count for assisted debtors not yet NPL, so recorded arrears during relief understate distress by rule; the deferral share must be read off post-relief outcomes. Details: `02_policy_context/level4_2025_notes.md`.
- **RQ3.** Three-dimensional scenarios make the Grundke–Pliszka search non-trivial; reported versus economic capital is the headline. The hazard model is deliberately unnamed until one is verified.

## Round 4 revisions (2026-11-02)

- RQ1 primary outcome: change in log value for parcels in both rounds, keyed by sheet and LAND_NO. Weak point: parcel numbers may be reissued after subdivision; check in the matched panel that matched parcels keep their area or neighbours.
- RQ2 2011: treatment follows circular 1564's eligibility (DDPM-declared areas plus indirectly affected debtors elsewhere). H2b outcomes are payment and recovery records, not classification.
- LGD is described in prose (appraisal net of damage, the omitted hazard share 1 − λ_B, haircut, discounting); the formula is in `05_design/framework.md` territory and should be written out there.
- κ is now cited (2026-11-02): Notification สนส. 12/2555 sets CET1 4.5% plus a 2.5% conservation buffer, so 7% from 2019; Notification สนส. 16/2560 adds 1% for D-SIBs, so 8% (six D-SIBs unchanged in the 2025 assessment). The countercyclical buffer (0–2.5%) was not required at issue and no activation was found; baseline zero, 2.5% as a sensitivity. Weak point: "no activation found" is an absence claim from searching the BOT site, not a document saying 0%.

## Round 5 revisions (2026-11-02)

- RQ1: cluster unit and wild cluster bootstrap; pooled all-province radar specification as primary; two-part outcome on equally weighted sheets; edge continuity stated as an assumption with tests. Weak point: the pooled specification depends on Sentinel-1 maps not yet built; the pre-analysis plan must fix the mapping rule before the 2027 round is out.
- RQ2: primary outcome is cumulative discounted loss over five years. Weak point: the discount rate (contract rate vs funding cost) decides whether an interest-free moratorium counts as a loss; fix it in the plan.
- RQ3: public return-period maps with dependence bounds instead of an event set; JRC Asian damage curves; system frontier, not named banks. Weak point: dependence bounds may be wide; provincial shares (December 2025) are by booking office, not collateral location.
- Chongwilaikasaem and Chalermyanont (2022) use official valuations in Hat Yai: be ready to explain how this project differs (nationwide, post-flood change, carry-over, link to credit).

## Round 6 revisions (2026-11-02)

- Pilot: land cover (WorldCover 2021) explains nearly all of the cross-sectional gap. Defend: land cover is post-treatment (2021), so the controlled estimate is not a hazard discount; the point is only that land use dominates.
- RQ1 power: the MDE table rests on assumed SDs and ICCs of changes. Be ready to say why an SD of 0.10 is plausible (committees revalue many units by similar percentages; province × round effects absorb the common shift) and what happens at 0.20.
- RQ2: the 2011 threshold (more than three months overdue = substandard) is documented from the 2016 successor notification and the 2011 circular's Q&A; the 2008 text itself was not found. The design is fuzzy because qualitative triggers can also downgrade.
- Weak point: the fallback chapter also needs earlier rounds and the BOT land index covers only Bangkok and vicinity.

## Round 7 revisions (2026-11-02)

- Know the cluster story: all 18 treated 1:50,000 clusters also contain controls (29 clusters in all; 28 and 11 mixed with the comparable controls). Shared clusters make the comparison partly within-cluster, which helps precision; the formula in §4.1 assumes a cluster effect common to treated and control sheets.
- Defend the control group: flooded sheets sit about 5 m above the local valley floor, all unflooded sheets about 33 m; the comparable controls about 8 m. Elevation is from a surface model (Copernicus GLO-30), so treat absolute heights as indicative.
- Equivalence margin 0.10: be ready to say that it rules out an official response as large as New York's after Sandy, and no more.
- H2b: first stage = relief actually received (payment holidays, restructuring) from the loan file; the 2011 measure itself was bank-side classification forbearance.
- Weak point: H1b (carry-over) is underpowered in Chiang Rai–Phayao (32 pp); it depends on the multi-province Sentinel-1 extension.

## Round 8 revisions (2026-11-02)

- **Primary sample flipped.** The pooled all-province Sentinel-1 sample is primary; Chiang Rai–Phayao (UNOSAT) is the validation subsample. Weak point: the pooled sample's power is unknown until the radar maps exist, and the mapping rule must be fixed in the OSF plan before the 2027 round is out.
- **Inference.** Randomisation over placebo footprints shifted within province is primary, because only 11 of 28 subsample clusters hold both groups. Be ready to explain how shifts respect province borders and terrain (shifted footprints may land on hills; restrict shifts to sheets with comparable height above the valley floor).
- **Buffers.** 2 km: MDE 0.04 with 18 mixed clusters; 10 km: 0.07 with 2. The trade-off is spillover protection against power; 5 km stays primary.
- **Outcome.** Pseudo land units (parcels sharing a sheet and a 2023–26 value) in log baht per square wah. Weak point: two land units with the same value on one sheet are merged.
- **Interpretation.** Duration-graded falls suggest damage; uniform area-wide cuts suggest administrative relief. Neither separates hazard learning cleanly; say so.
- **Timing fallback.** If 2027 surveys predate the floods, 2027 is a placebo and 2031 the primary test; the 2031 round must be published by 2 December 2030 (s. 19), inside Year 3 (corrected in round 9).
- **RQ2.** Deferral signature: lower recorded delinquency in year one, then catch-up; no year-one difference means relief did not bind. 2 Dec 2025 is the Cabinet resolution date that ว.8158/2568 implements. Plan B is a valuation question, not a flood one.
- **RQ3.** LGD = 1 − discounted recovery / exposure; cut-offs 1 in 200, 500, 1,000; both dependence bounds; Bangkok reallocation sensitivity.


## Round 9 revisions (2026-11-02)

- **Pooled sample exists.** Sentinel-1 rule (VV < −18 dB at about 80 m; new water absent from every 2023 same-season scene; share > 25%) gives 198 flooded sheets in four provinces, 2,390 comparable controls, 57 clusters; MDE 0.05 at SD 0.10. Weak point: radar recall against UNOSAT is 7% (precision 79%). Radar sees lasting water; it misses flash floods and urban water. Be ready to say the primary estimate is about prolonged inundation, and that tuning the rule on UNOSAT would leave no independent validation.
- **Imbalance.** Radar-flooded sheets had lower pre-flood values (SMD −0.53), unlike the UNOSAT subsample (0.02, −0.05). Changes are compared; reweighting on pre-flood value is reported.
- **Contamination.** 260 of 2,390 comparable controls are UNOSAT-flooded; dropping them leaves power unchanged. Outside Chiang Rai–Phayao no independent map exists, so some control contamination remains (biases towards zero).
- **RQ2 power.** H2b at 5 pp needs about 30,000 borrowers per group (SD 0.3, first stage 0.5, design effect 1.5); 2,000 per group give 19 pp. One bank cannot test it; say so.
- **2031 timing.** Published by 2 December 2030 (s. 19), so within Year 3.

## Round 10 revisions (2026-11-02)

- **Two co-primary samples.** Radar (198 sheets, four provinces) estimates prolonged inundation; UNOSAT (1,214 sheets, Chiang Rai–Phayao) any flooding. Expect to be asked which is "the" result: neither; they answer different questions, and agreement between them is informative.
- **Reweighting.** Entropy balancing within province on pre-flood value, height and built-up and cropland shares makes those standardised differences zero at every buffer; effective controls fall from 2,390 to 125 at 5 km but the MDE only from 0.046 to 0.050, because clusters, not sheets, bind. Weighting on value and height alone (the round-10 rule) left built-up at −0.47 and water at 0.35, so land cover was added after WorldCover for Nong Khai and Nakhon Phanom arrived (decided with the user, 2026-11-02).
- **Water share: the weak point.** Flooded sheets hold more permanent water (0.42 after weighting). Balancing on it fails in two provinces: riverside sheets have no unflooded counterparts. It goes into the regression, and dropping the 9 wettest flooded sheets leaves it at 0.34, so it is a broad difference, not outliers. Defence: water share is a pre-flood hazard proxy, the regression adjusts for it linearly, and the within-cluster estimate compares sheets in the same 1:50,000 sheet. A referee could still say the comparison is riverside against inland land; the honest answer is that the UNOSAT co-primary sample is balanced and the two primary tests are reported together.
- **Solver.** The entropy-balancing weights were solved by BFGS until 2026-11-02, which failed silently at 10 km (effective 50, value imbalance 0.075). Newton steps on the convex dual give effective 75 and MDE 0.061 at 10 km, with 2 and 5 km unchanged.
- **Pre-analysis plan.** Details cut from the proposal (thresholds 10% and 50%, buffers, paddy checks, imagery check, placebo rule, within-cluster estimate, pre-trend) live in `05_design/pre_analysis_plan_rq1_draft.md`. It is a draft; the author registers it (CP3) before the 2027–30 round is published.
- **Calibration and materiality.** The full discount is Beltrán et al.'s 4.6% (abstract only read; meta-analysis, wide range, mostly US). Halving and doubling bounds it. The materiality rule is arbitrary in its step size; defend it as fixed in advance, not as optimal.
- **Weak points.** Still one post-flood change and no pre-trend until earlier rounds arrive; credit shares by booking office, not collateral location; the λ_B link remains assumed (Figure 1 makes that visible rather than hiding it).

## Round 11 revisions (2026-11-02)

- **RQ2 re-centred on 2024–25.** The primary design compares flooded with comparable unflooded borrowers through and after the relief. It identifies *when* flood losses are recorded, not whether relief avoided them; that needs a no-relief counterfactual, which only the 2011 eligibility rule offers (now H2c, an extension). Be ready to say so. Power (1,100–2,300 flooded borrowers for a 2-point rise) assumes base delinquency of 3–5% and ignores pre-period adjustment, so it is conservative in one way and optimistic if the true base rate is higher.
- **The 2011 threshold is also the NPL boundary.** Differencing declared and undeclared areas only works if the boundary's own effect is the same in both; pre-flood years test that. The estimate is local to borrowers near three months overdue.
- **Plan B on the same chain.** The 2025 floods (437 radar sheets, nine provinces, from two events: 206 sheets in the 15 November–31 December southern window, Songkhla 113, Pattani 40, Phatthalung 27, Nakhon Si Thammarat 26; 231 in the 15 August–31 October northern window, Phitsanulok 62, Phichit 61, Phetchabun 41, Nakhon Phanom 34, Nakhon Sawan 33; `04_analysis/outputs/tables/rq1_sample_sensitivity.md` row 8; event matching in `02_policy_context/level4_2025_notes.md` §B2). They give a second test with data in hand; analyse the two events separately. Timing caveat: the 2025 floods may postdate the 2027 round's survey, in which case the 2031 round is the test, as for 2024.
- **RQ3 anchoring.** Economic S* ≤ reported S* by construction, so the claim is about the gap's size in the plausible region, not its sign. RQ1's estimate enters only as a scenario for appraisals because official values do not set them.
- **Credit drift.** 8% of non-Bangkok credit changed province over 2005–15, 6% over 2015–25 and 3% over 2019–25 (booking location; the 2015 move of hire-purchase bookings to head offices adds noise). RQ3 allocates by December 2025 shares (`credit_shares_allocation.csv`), so staleness is now small next to the booking-location problem.

## 2011 return period (2026-11-02)

- No project source dates the 2011 flood's return period. The World Bank CCDR financial-sector note assumes 1 in 50 years, citing the 2023 Thailand Economic Monitor (World Bank 2026, p. 11). That is an assumption in a scenario note, not an estimate; RQ3 should place the 2011 footprint on the Aqueduct/JRC return-period maps itself and report where it falls, with 1-in-50 only as a cross-check.

## Coarse λ_B check: BOT regional price index (2026-11-02)

- **Source.** The BOT residential price index uses lenders' appraisal prices from the mortgage-loan database (bib `bot2026rppislides`, p. 3, "the BOT adopted appraisal price from the Mortgage Loan Data (MGL)"). It is the only public series of bank collateral appraisals. Table EC_EI_008_S4 (reportID 993) covers January 2011 to September 2026, monthly, 2011 = 100, for Bangkok and vicinity, Central, North, Northeast and South. Regions are built from representative provinces (slides pp. 8–9): North includes Chiang Mai and Chiang Rai; South includes Songkhla.
- **Proposal use.** One clause in §3 Framework: a coarse check on λ_B in the no-access branch. No result is reported in the proposal.
- **Descriptive windows.** Script `rppi_flood_windows.py`, output `rppi_flood_windows.md`. Each value is the region's log change minus the mean of the other non-Bangkok regions, in per cent.

  | Event | Base month | 3 months | 6 months | 10 months | Typical 10-month drift, 2012–23 |
  |---|---|---|---|---|---|
  | 2025 South | Oct 2025 | +3.1 | +2.2 | +3.2 | −1.6 |
  | 2024 North | Jul 2024 | −1.2 | −0.5 | −1.1 | +0.5 |
  | 2011 Bangkok and vicinity | Sep 2011 | −2.2 | −3.5 | −7.3 | +0.1 |

  The 2011 Bangkok-and-vicinity index fell from 102.6 (Jul) to 98.5 (Oct) and was back at 102.4 by January 2012. The base month (Sep 2011) is already part of that dip.
- **Reading.** No regional fall in bank appraisals after the 2025 southern floods. A dip of about 1–2 points relative to trend after the 2024 northern floods. After 2011, Bangkok and its vicinity lagged the other regions. That last gap has no pre-period (the series starts January 2011), and the other regions boomed after 2011.
- **Weak points (state these openly).**
  - Regions are mostly unflooded.
  - The index is a 3-month moving average of **new originations**. It does not revalue existing collateral.
  - After a flood, originations shift away from flooded land, and location enters the hedonic model only as distance to points of interest. A null is therefore expected even if flooded collateral lost value.
  - Treat it as context for the λ_B range, not as an estimate of λ_B.

## Round 12 responses (2026-11-02)

- **Controls dry in every source.** Radar 2024 and 2025 < 1% and UNOSAT < 1% where mapped. Radar sample: 1,897 controls (493 dropped, 260 of them UNOSAT > 25%); UNOSAT sample: 577 (22 radar-wet dropped). Weighted effective controls fall from 125 to 85; weighted MDE 0.050 → 0.053. Outputs: `rq1_2024_pooled_mde.csv`, `rq1_2024_pooled_balance.csv`, `rq1_2024_mde_changes.csv` (rows "dry in every source").
- **Treated clusters reported.** Radar 198 sheets in 21 clusters (19 mixed); UNOSAT 1,214 in 18 (10 mixed). These bind cluster inference; randomisation inference stays primary.
- **MDE vs full discount.** 0.05 ≈ the central 4.6% discount, so H1a detects damage-scale falls or full recognition only. Stated in §4.1; the PAP lists which λ_T each discount assumption can rule out. Stacked 2024+2025 test is secondary.
- **λ_B back-of-envelope.** `rq3_lambda_sensitivity.py` (illustrative parameters). Flooded-region LGD moves by 1.5–8.6 pp between λ_B = 0 and 1; S* moves 3–19% at LTV 0.8–1.0, but roughly doubles at LTV 0.7, where LGD sits near zero and any unrecognised discount creates a loss (losses are small there anyway). Deferral acts on the whole flood-induced PD rise, so the headline is now the reported-vs-economic gap over the deferral share; λ_B is a second axis. Weak point: no public Thai LTV distribution was used; the LTV range is an assumption.
- **RQ2 relief contrast.** Level-4 (Songkhla) vs ว.601-template relief in neighbouring provinces (confounded with province-wide shocks: report as a contrast, not a clean counterfactual), and borrowers either side of the 2 Dec 2025 non-performing cut-off. Days-past-due freeze (ว.8158 item 2.6) still means recorded arrears understate distress during relief.
- **RQ2 power.** The existing table already used design effects 1.5–2; the proposal now says so. A rise of 0.7 pp (Albertazzi et al.) needs 8,700–19,000 flooded borrowers (`rq2_power_2024.csv`), so a single lender detects only large effects.
- **LGD.** Realised LGD for 2024–25 defaults will arrive too late; haircuts, revaluations and provisions are the early proxies.
- **H2c margin.** Kept at 5 pp but labelled loose; the timing part of H2c (delinquency rising when relief ends) is now explicit. A 1 pp margin would need about 25 times the sample (infeasible).
- **Timing.** Decision tree in PAP §9 and the proposal timeline: (a) on time, post-flood survey; (b) pre-flood survey; (c) one-year extension; (b)+(c) puts the primary test in Year 4, with the 2025-flood chapter carrying Chapter 2 meanwhile.
- **Figure 1.** λ_B arrow relabelled "assumed analogy, 0 to 1, not a causal link; loan appraisals can reveal it".
- **Cut for length (2,400 words).** Bin et al. (2013), Quan and Quigley (1991), Avenancio-León and Howard (2022) and the English price benchmark in §4.1 (Garbarino and Guin stays in §3). The pilot gloss of "scale" is now "same-scale sheets"; the 1:1,000/1:4,000 meaning is in §4.1's sheet sizes.
- **Small points 12–13, 24, 29, 30, 34, 36, 38.** (12) Unit and attrition rule already in PAP §2; (13) equal sheet weights justified (valuation decisions are per sheet) with area- and parcel-weighted sensitivities in PAP §2; (24) "on each side in each area" already in §4.2; (29) §4.3 now says results cover the banking system and stylised banks; (30) the 4.6% transfer caveat: Beltrán et al. pool mostly US and other high-income house prices (land plus buildings), so a land-only official value could carry a different discount in either direction; the proposal says "from richer markets" and halves/doubles it, and this weak point should be raised orally if asked; (34) the CRC URL ending ".pdf.pdf" returns HTTP 200, application/pdf, 1,042,064 bytes (checked 2026-11-02), so it is genuine; (36) §5 pilot now adds "land cover may itself respond to hazard" (bad-control point); (38) advisers already reworded in round 12.
- **Optical validation (done 2026-11-02, `validate_s1_s2.py`, `s1_s2_validation.csv`).** Sentinel-2 L2A SCL, 822 scenes, 15 Aug–31 Oct 2023 vs 2024; rule fixed beforehand (PAP §8). Treated-sheet precision: Chiang Rai 0.57, Phayao 0.64, Nong Khai 0.78, Nakhon Phanom 0.88 (pooled 0.68); controls 1.2% (Nong Khai 4.6%). All provinces pass the author's one-half rule; none dropped. Weak points: Chiang Rai sits close to the threshold and falls to 0.35 at a 0.25 new-water cut (shallow or short floods, or radar false positives on wet paddy); SCL misses water under crops and among buildings (so precision is a lower bound) but can mistake cloud shadow for water; the 2023 reference is one year only. If asked about radar's 7% recall against UNOSAT: radar is specific (precision 0.57–0.88 optically, 0.79 against UNOSAT) but insensitive, which is why the treated group means prolonged inundation and UNOSAT carries any flooding.
- **Registered analysis code (2026-11-02).** `rq1_round_change.py` implements the PAP outcome, weights, regression and inference and runs unchanged on R1 (`--post DIR`). Synthetic check (`rq1_round_change_montecarlo.csv`): unbiased to within MC error, size 6%, power 67% for a 0.035 sheet-level fall; the CR1 SE understates the sampling SD (0.013 vs 0.016), so RI and the wild bootstrap carry inference. A single synthetic draw (`rq1_round_change_synthetic.csv`) shows how noisy one realisation is (−0.014 against an expected −0.035): be ready to explain this if a reader opens the table. Weak point: the simulation's variance components are assumptions (same SD 0.10, ICC 0.2 as the power table).
- **2025 design on the same code.** `--event 2025` (437 treated, 7,609–7,616 controls, 134 clusters): size 6%, power 97% for a 0.035 sheet-level fall (4% and 98% after the round-13 balance fallback); the earlier sheet panel had no GSW coverage south of 10°N, so two southern tiles were added. In one synthetic draw the carry-over coefficient came out −0.062 (wild bootstrap p 0.008) although carry-over is independent of treatment in the simulation; over 20 draws it averages 0.006 (SD 0.027), so that draw was chance, but the carry-over SE may be understated: H1b stays descriptive.
- **Not done (needs the author or more time).** District disaster-declaration lists (DDPM) for the administrative-spillover sensitivity (time-boxed web search 2026-11-02 found only news reports of affected districts, not declarations; request from DDPM or provincial offices); earlier rounds for SD/ICC calibration (request to Treasury).

## Round 13 (2026-11-02): registration form and balance fallback

- OSF form drafted (`05_design/osf_registration_form.md`, Secondary Data Preregistration v3). The PAP governs; the form is a paste-in copy.
- Weak point found and fixed before registration: entropy balancing in Phatthalung (2025) could not match treated height, because six flooded sheets in 1:50,000 sheet 5024-3 sit 39–138 m above the valley floor (likely the valley-floor measure failing on a coastal-hill sheet, or radar false positives on slopes; not investigated further, to avoid tuning on the sample). The registered fallback drops the worst-balanced variable per province until every gap ≤ 0.01. Expect a question on why the treated sample was not trimmed instead: trimming changes the estimand and would shift every reported count; the fallback keeps the sample and is reported.
- RQ1 samples use every cadastral scale (the pilot used 1:4,000 and 1:1,000 only); PAP §2 now says so.

## Round 13g (2026-11-03): buffer metric, R1 safeguards, later floods

- **Buffer metric.** The 5 km rule used each sheet's own latitude for the east–west scale, which is not a projection; 48 of 1,897 controls were within 5 km by great-circle distance. Fixed with `geo.py` (great-circle between box centres); radar controls now 1,891, UNOSAT 579, 2025 7,664; treated unchanged. Weak point to own: the old samples were circulated in earlier drafts; every number in the PAP, form and proposal now comes from the rebuilt files.
- **Balance after weighting.** With the registered weights, Phayao's controls cannot match its treated sheets on value, height or cropland (its fallback keeps built-up share and the rural indicator; within Phayao the gaps are 0.98 on value, 0.64 on height and 1.08 on cropland), which leaves pooled gaps of 0.08 (value), 0.32 (height) and 0.13 (cropland), plus tree −0.38 and water 0.67 (`gap_after_*` in `rq1_round_change_balance.csv`). Elevation, tree and water enter the regression; height above the valley floor does not, so Phayao is the province to discuss if asked about residual imbalance.
- **Later floods.** Nakhon Phanom re-flooded in 2026 (18 of 25 treated sheets). Primary unchanged; registered drop as a sensitivity (34 treated, 47 controls).
- **R1 safeguards.** Missing or unchanged R1 files and the matching alert stop the run; R1 SHA-256 recorded with each confirmatory p.

## Round 13h (2026-11-03): fourth review

- The R1 safeguards now hold on every path: the matching stop runs in the sensitivities and Lee bounds as well as the primary run; a second file for a province, or an old round re-saved or lightly re-issued (more than 99% of matched single-row parcels unchanged; round 13i), stops the run. Weak point: a genuine round that carries over more than 99% in a province would also stop; then it is checked against the Treasury's publication and logged as a deviation. Defence: "the code refuses to estimate on anything that is not demonstrably a new round, and on any sample where identifiers fail to match".
- 2026-drop disclosures: fixed on the day the shares were computed, after seeing 18 of 25; more 2026 radar scenes than 2023 (228 on 65 dates against 174 on 42), so the drop more likely over-counts; the reference check is one-way; 2024 radar sample only. Weak point: a reviewer can call the drop post hoc. Answer: it is a sensitivity, the primary sample is unchanged, and the rule copies the registered thresholds.
- Phayao gaps after weighting (population SD): value 0.98, height 0.64, cropland 1.08, water 9.6. Open for the author: add height as a covariate or report Phayao separately.

## Phayao height slope (2026-11-03, author's decision)

- After the registered weights, Phayao's treated sheets still sit 0.64 controls' SD higher above the valley floor than its controls (value 0.98, cropland 1.08), because the balance fallback drops height there. The author chose to add height × 1[Phayao] to the regression (`HEIGHT_COV_PROVINCES` in `rq1_round_change.py`), fixed by name before registration so the model does not depend on R1.
- Defence: regression adjustment where weighting fails is standard (doubly robust logic); the slope is Phayao's own, so it does not borrow the height gradient of the other provinces. Weak point: with 25 treated sheets the Phayao slope is noisy, and the adjustment extrapolates where treated sheets lie beyond the controls' height range (12 of 25 do, `rq1_round_change_balance.csv`, so for them the slope is an extrapolation). Phatthalung in the 2025 sample has the same problem (fallback drops height; gap 7.1 SD; 6 of 27 treated sheets beyond the controls' height range) and, by the author's second decision the same day, gets its own height slope too (`HEIGHT_COV_PROVINCES = [phayao, phatthalung]`).


# OSF registration form, RQ1 — working draft (not submitted)

Draft of 2026-11-02 for the author to edit and submit on OSF Registries (CP3: the author's account; this draft is not a submission). It maps `05_design/pre_analysis_plan_rq1_draft.md` (the PAP) onto the fields of OSF's **Secondary Data Preregistration** template, version 3 (schema id `64775783798e08000a70407e`; field list read from the public OSF API, `https://api.osf.io/v2/schemas/registrations/64775783798e08000a70407e/schema_blocks/`, as of 2026-11-02). This template fits because the pre-period data exist and have been analysed, while the outcome data (the first post-flood round, R1) do not yet exist.

How to use it: paste each section into the field of the same name; attach the PAP and a zip of the registration commit (all of `04_analysis/src`, which the registered scripts import from, plus `run_all.py`, `requirements.txt`, the schemas and the hash table; commands in `registration_checklist.md`) as uploads; replace every `[bracketed]` placeholder. The PAP is the governing document: if the two disagree, the PAP wins, and the form should be corrected before submission. "Prior knowledge" and "Prior publication" must be written in the author's own words.

Deadline: before any 2027–30 schedule is published; by law at least 30 days before it takes effect, so by 2 December 2026 for a 1 January 2027 start (PAP §9).

---

## Study information

### Research questions

1. When the Treasury Department sets the first official land values after the 2024 floods, do values on land flooded in 2024 fall relative to comparable unflooded land in the same province? (RQ1a)
2. Is that fall smaller where ex-ante flood hazard, measured by height above the valley floor, was already high? (RQ1a, moderation)
3. Are official values on flooded land more often carried over unchanged from the 2023–26 round? (RQ1b)
4. Replication: do the same answers hold for land flooded in 2025 but not 2024, in nine further provinces? (PAP §10)

### Hypotheses

- **H1a (directional, confirmatory).** The change in log official value per square wah between the 2023–26 round and R1 is lower on flooded sheets than on control sheets (treatment coefficient β < 0), tested in the 2024 radar and UNOSAT samples. Rationale: flood damage, administrative relief, or newly recognised risk would each lower values; PAP §11 sets out how they are told apart.
- **H1a, moderation (directional, secondary).** The treatment × height-above-valley-floor coefficient is negative: the fall is smaller on low-lying land, where hazard was already high and could already have been priced in, and larger on higher land.
- **H1b (directional, descriptive).** The share of land units carried over unchanged is higher on flooded sheets. Reported with its estimate and wild-bootstrap p-value but not part of the confirmatory family.
- **Replication (directional, secondary).** H1a holds in the 2025-flood sample.

## Data description

### Datasets used

1. **Official land appraisal values (ราคาประเมินทุนทรัพย์ที่ดิน), Treasury Department (กรมธนารักษ์).** Parcel-level cross-sections by round. The 2023–26 round (77 provincial files; columns `UTMMAP1–4`, `UTMSCALE`, `LAND_NO`, `EVAPRICE`; no coordinates) is the pre-period. The outcome round R1 (expected 2027–30, effective 1 January 2027, or 2028–31 if extended) has not been published. Subset: sheets in the sample provinces, mostly at 1:1,000 (urban) and 1:4,000 (rural), with some at 1:2,000 and 1:500.
2. **Copernicus Sentinel-1 GRD (IW, VV)**, 15 Aug–31 Oct (north of 11° N) and 15 Nov–31 Dec (south), 2023–2025: defines flooding (treatment) by a fixed rule. The same windows in 2021–22 (north, the 2021–23 reference sensitivity) and 2026 (north, the later-flood sensitivity) use the same rule.
3. **UNOSAT water extents, FL20240912THA (Chiang Rai, Phayao)**: the second, independent treatment definition, and a screen on controls.
4. **Covariates**: Copernicus DEM GLO-90 and GLO-30 (elevation, height above valley floor), ESA WorldCover 2021 v200 (land-cover shares), JRC Global Surface Water v1.4 occurrence (distance to permanent water).
5. **Validation**: Copernicus Sentinel-2 L2A scene classification, 15 Aug–31 Oct 2023 and 2024 (already run; PAP §8).
6. **Administrative boundaries**: OCHA COD-AB Thailand (Royal Thai Survey Department; districts and subdistricts), for the declaration drop (PAP §4).

### Data availability

The dataset is publicly available.

### Data access

All sources are public and free without login. Treasury files are published on data.go.th under the "Open Data Common" label (research use with attribution assumed; [author to confirm the terms on data.go.th]). The Treasury revises files in place, so the 2023–26 round is kept as a dated snapshot with SHA-256 checksums. Sentinel-1 and Sentinel-2 are read anonymously from Microsoft Planetary Computer. No restricted or personal data are used.

### Data identifiers

- Treasury: https://data.go.th/dataset/land-valuation (files on catalog.treasury.go.th); snapshot `03_data/raw/treasury_land_appraisal/snapshot_2026-11-02/` with `manifest.csv` (SHA-256).
- Sentinel-1: https://planetarycomputer.microsoft.com/api/stac/v1/collections/sentinel-1-grd
- Sentinel-2: https://planetarycomputer.microsoft.com/api/stac/v1/collections/sentinel-2-l2a
- UNOSAT: https://unosat.org/static/unosat_filesystem/4009/FL20240912THA_SHP.7z (HDX: https://data.humdata.org/dataset/water-extents-from-1-aug-2024-to-22-october-2024-over-chiang-rai-province)
- COD-AB: https://data.humdata.org/dataset/cod-ab-tha (`tha_admin_boundaries.gdb.zip`; SHA-256 in `03_data/README.md`).
- Copernicus DEM: doi:10.5270/ESA-c5d3d65. WorldCover: doi:10.5281/zenodo.7254221. JRC GSW: Pekel et al. (2016), doi:10.1038/nature20584.
- Full log with file names, sizes and scripts: `03_data/README.md`.
- Code repository: [public mirror URL or OSF upload], commit `[hash at registration]`.

### Access date

Pre-period, covariate and flood data accessed 2 November 2026; COD-AB and the 2026 Sentinel-1 scenes on 3 November 2026 (per-file dates in `03_data/README.md`). R1 will be downloaded on its publication date [to be recorded], by `04_analysis/src/download_treasury_appraisal.py`, and checksummed before analysis.

### Data collection procedures

Official values are set by provincial valuation committees under the Property Valuation for the Public Interest Act B.E. 2562 (2019) (พระราชบัญญัติการประเมินราคาทรัพย์สินเพื่อประโยชน์แห่งรัฐ พ.ศ. 2562), by land unit (mostly road or waterway frontages, with parcel values derived by depth and shape factors) and published parcel by parcel within map sheets, for four-year terms that a province may extend by up to one year (`04_analysis/treasury_method_notes.md`). Parcel-level schedules cover every parcel with a title deed (โฉนดที่ดิน) or an N.S. 3 Kor certificate, so the population is complete rather than a sample; land under other title types, which receives one value per land-unit type, is absent (Ministerial Regulation, clause 3, p. 3; same notes). Committee survey dates are not published centrally; PAP §9 sets out how survey timing is handled. The flood maps are produced by this project from Sentinel-1 by the rule in PAP §3 (code `04_analysis/src/flood_s1_grd.py`), which was fixed before any outcome data existed.

### Codebook

No official codebook is published. Column meanings are documented in `03_data/README.md` and `05_design/classification_and_indices_notes.md`: `UTMMAP1–4` and `UTMSCALE` identify the cadastral map sheet, `LAND_NO` the parcel number on the sheet, `EVAPRICE` the official value (presumed baht per square wah; to be confirmed). Sheet scales: 1:1,000 and 1:4,000 dominate (2024 treated: 65 and 120 of 198; 12 at 1:2,000, 1 at 1:500). Sample files (one row per sheet; columns listed in the script docstrings), registered with the SHA-256 of their decompressed contents (`04_analysis/outputs/tables/registration_hashes.csv`, written by `hash_registration_inputs.py`; copy the hashes here at registration): the three primary samples `03_data/processed/rq1_2024_sample_sheets.csv.gz`, `rq1_2024_unosat_sample_sheets.csv.gz` and `rq1_2025_sample_sheets.csv.gz`; the nine rebuilt sensitivity samples `rq1_2024_sens_<variant>_sample_sheets.csv.gz` (thr10, thr50, prov20, prov30, buf2, buf10, nocap, ref2123, nocrop); and the Sentinel-2 sheet counts `s2_sheet_water_rq1_2024.csv.gz` with their sheet-key file `s2_sheet_keys_rq1_2024.csv.gz` behind the optical drop; and the sheets' districts and tambons `rq1_2024_sheet_admin.csv.gz` with the unit list `rq1_admin_units.csv.gz` behind the declaration drop; and the 2026-season radar shares `rq1_2024_sheet_flood_2026.csv.gz` behind the later-flood drop (17 files).

## Variables

### Manipulated variables

Not applicable: observational study. Treatment (flooded in 2024) is a measured, map-derived variable defined below.

### Measured variables

- **Outcome (primary).** For each sheet, the mean over pseudo land units present in both rounds of Δ log value per square wah, R1 minus 2023–26. A pseudo land unit is the set of parcels on a sheet sharing one 2023–26 value; its R1 value is the mean over its parcels still present. Identifiers are matched as strings with surrounding whitespace removed; duplicated identifiers within a round are averaged; rows with a missing parcel number or a non-numeric or non-positive value are dropped.
- **Outcome (H1b).** Sheet share of pseudo land units carried over (every present parcel keeps its 2023–26 value).
- **Outcome (secondary).** Change among units whose value moved, with Lee (2009) bounds.
- **Treatment, radar sample.** Water when sigma0_VV < −18 dB; a pixel is flooded in season Y if water in at least one season-Y scene, in no 2023 scene, and observed in at least two 2023 scenes. A sheet is treated if its 2024 flooded share > 25% and its 2025 share ≤ 25%, in provinces with at least 25 treated sheets.
- **Treatment, UNOSAT sample.** UNOSAT FL20240912THA share > 25% (Chiang Rai, Phayao). Controls: UNOSAT share 0 and radar 2024 and 2025 shares < 1%.
- **Treatment, 2025 sample.** Radar 2025 share > 25% and 2024 share < 1%.
- **Moderator.** Height above the valley floor: sheet mean elevation minus the 5th percentile of sheet elevations in the same 1:50,000 sheet, centred at the treated mean.
- **Covariates.** Mean elevation, distance to permanent water (GSW occurrence ≥ 50), WorldCover 2021 built-up, cropland, tree and water shares, rural-sheet indicator (scale 1:4,000); province fixed effects; in Phayao and Phatthalung only, height above the valley floor (height × 1[province]), because there the controls cannot match the treated sheets on height and the balance fallback drops height from the weights (decided 3 November 2026, before registration; fixed by name in the code).
- **Balancing variables.** Pre-flood mean log value, height above the valley floor, built-up and cropland shares, rural-sheet indicator.

### Missing data

R1 does not exist, so missingness is unknown. Attrition is the share of a sheet's 2023–26 parcels missing from R1, reported by treatment group; parcel numbers new in R1 (subdivisions, mergers) are ignored. The synthetic check assumed 2% attrition. Sheets with no 2023–26 parcel in R1 are dropped, counted by group (`sheets_absent_*`), and the balancing weights re-estimated on the sheets present. If more than 10% of a province's treated or control sheets have no matched parcel, the code stops before computing any estimate (in the primary run, every sensitivity sample and the Lee bounds); identifiers are then checked, and any harmonisation (for example leading zeros or recoded sheets) is applied to every sheet alike and reported as a deviation. Lee (2009) bounds are reported for the change among units whose value moved (PAP §2). All 2,089 radar-sample sheets (198 treated, 1,891 controls) have complete covariates and were observed by Sentinel-2 in both years.

### Unit of analysis

The cadastral map sheet. Included: sheets of any scale in the sample provinces with usable radar coverage (valid pixels at least half the bounding box in 2024 and 2025). Controls: under 1% flooded in every source (radar 2024 and 2025; UNOSAT where it maps the sheet), same province, centre at least 5 km from every treated sheet centre (great-circle distance between bounding-box centres, `geo.py`), and height above the valley floor at most the 90th percentile of all treated sheets in the sample. Controls are not selected by scale; the weights match each province's treated share of rural (1:4,000) sheets. Expected sizes:

- Radar 2024: 198 treated (Chiang Rai 88, Nong Khai 60, Nakhon Phanom 25, Phayao 25), 1,891 controls, 21 treated clusters.
- UNOSAT 2024: 1,214 treated, 579 controls, 18 treated clusters.
- 2025: 437 treated in nine provinces, 7,664 controls, 49 treated clusters (134 in all).

Clusters are 1:50,000 map sheets.

### Statistical outliers

No outcome values are removed or winsorised; the primary p-values (randomisation inference in the radar samples, the wild cluster bootstrap for UNOSAT) do not rely on normal errors. Pre-specified covariate trimming (sensitivity): drop treated sheets whose water share exceeds the 99th percentile of their province's controls (8 of 198).

### Sampling weights

No sampling weights come with the data (it is a census of titled parcels). The analysis uses its own weights: entropy balancing of controls within province on the five balancing variables, with control weights scaled to sum to each province's treated count; treated sheets weight one. A province counts as balanced when every standardised mean gap is at most 0.01; otherwise the variable with the largest gap leaves that province's set and the weights are re-estimated (registered code, `balance_weights`). On the pre-period data it fires in two provinces across three samples (`rq1_round_change*_balance.csv`): Phayao in the radar sample (value, height and cropland dropped; balanced on built-up share and the rural indicator only; 12 treated sheets lie higher than every control), Phayao in the UNOSAT sample (17 controls for 378 treated; balanced on built-up share and the rural indicator only), and Phatthalung in the 2025 sample (height dropped; 6 treated sheets lie higher than every control). Effective controls: 98 (radar), 104 (UNOSAT), 634 (2025). Sheets are weighted equally because committees set values sheet by sheet. Sensitivities: weights × sheet area (bounding box), weights × 2023–26 parcel count, and unweighted.

## Knowledge of data

### Prior publication/dissemination

[Author to state in own words.] Draft: None. The 2023–26 round has been used only in this project's unpublished pilot and research proposal (cross-sectional values against the 2011 flood in 17 Chao Phraya basin provinces).

### Prior knowledge

[Author to rewrite in own words; this is the field reviewers read most closely.] Draft:

- I have analysed the 2023–26 round, the pre-period of this study, in full: the cross-sectional pilot on the 2011 flood; balance and power calculations for the 2024 and 2025 samples; and a synthetic R1 built from the 2023–26 values to test the code. No value from R1 or any later round has been seen, because none has been published.
- The treatment rule, control rule and province threshold were set before the Sentinel-2 check and were not changed by it. The Sentinel-2 check (2 November 2026) was run before registration, under a decision rule fixed beforehand (drop a province whose optical precision is below one half). No province was dropped. Its results are reported in PAP §8.
- No earlier round (before 2023–26) has been obtained, so the SD and ICC of value changes are assumptions.
- I have no role in setting Treasury official values and no access to unpublished Treasury data. [Author to confirm.]

## Analyses

### Statistical models

Weighted least squares at sheet level, separately for each sample:

Δy_s = α_p + β·Flood_s + γ′X_s + ε_s

- α_p: province fixed effects.
- X_s: elevation, distance to permanent water, the built-up, cropland, tree and water shares, the rural-sheet indicator, and height above the valley floor × 1[Phayao] and × 1[Phatthalung] (province-specific height slopes; Phayao is in the radar and UNOSAT samples, Phatthalung in the 2025 sample).
- Weights: the entropy-balancing weights.
- β tests H1a (confirmatory).
- Moderation (secondary): add Flood_s × (height_s − mean treated height) and height_s; the interaction coefficient is tested by the wild cluster bootstrap.
- H1b: the same model with the carry-over share as the outcome.
- Within-cluster variant: 1:50,000 sheet fixed effects in place of province fixed effects.
- Code: `04_analysis/src/rq1_round_change.py --post <R1 folder>` (2024 radar and UNOSAT samples, then Holm) and `--event 2025`, registered at commit `[hash]`; it runs unchanged on R1. It imports `ebal` from `rq1_2024_pooled.py` (same commit).

### Effect size

Smallest effect of interest: a fall of 0.05 log points (about 4.9%) at sheet level. It is close to the assumed full hazard discount of 4.6% for inland 100-year floodplains (Beltrán et al. 2018; 2.3–9.2% when halved or doubled). Ruling out a fall of 0.05 rules out λ_T above about 1.1 under the central discount (0.05 / 0.046; PAP §7).

### Statistical power

The figures below assume a sheet-level SD of changes of 0.10 and an ICC of 0.2. These are assumptions, to be recalibrated if an earlier round arrives before registration.

| Sample | MDE, registered weights (80% power, 5%) | Effective controls | Treated clusters |
|---|---|---|---|
| 2024 radar | 0.053 | 98 | 21 |
| UNOSAT | 0.061 | 104 | 18 |
| 2025 | 0.030 | 634 | 49 |

Source: `rq1_round_change*_balance.csv` (row "all"). Unweighted MDEs: 0.047, 0.065 and 0.029.

Monte Carlo on the registered code, 100 synthetic R1 draws with a planted 0.035 sheet-level fall. Power and size are for the wild cluster bootstrap (999 draws per replication). The placebo test's power was not simulated, because 1,000 footprints per draw is too slow for 100 draws.

| Sample | Power | Size (true effect zero; nominal 5%) |
|---|---|---|
| 2024 radar | 63% | 5% |
| UNOSAT | 53% | 3% |
| 2025 | 100% | 4% |

The design detects damage-scale falls or full recognition. It cannot separate partial recognition from none.

### Inference criteria

- **Primary p-value, radar samples:** two-sided randomisation inference over 1,000 placebo footprints (PAP §6), each the treated footprint shifted within its province onto eligible dry sheets, with weights re-estimated; p = (1 + number of placebo estimates at least as large in absolute value) / 1,001. The 5 km buffer and height cap are not re-applied around placebo sheets.
- **Primary p-value, UNOSAT sample:** the wild cluster restricted bootstrap. Placebo footprints cannot be drawn there, because the sample has fewer controls than treated sheets.
- **Bootstrap:** wild cluster restricted bootstrap, with the null imposed, Rademacher weights, 9,999 draws, CR1 t-statistic, two-sided, clustered by 1:50,000 sheet. In the radar samples it is a check on the placebo p-value.
- **Multiplicity and decision rule:** the H1a tests in the radar and UNOSAT samples form a family of two when every province shares one timing case, Holm-adjusted at 5% (`rq1_round_change_holm.csv`); with mixed timing the R1 family is every R1 run recorded by the waiting date, and the case-(b) provinces' R2 runs form a separate R2 family, Holm-adjusted on their own (PAP §9). H1a is supported if β < 0 with an adjusted p below 0.05 in at least one sample of the R1 family; the R2 family is reported as a separate confirmatory test of the case-(b) provinces. A significantly positive β is reported as evidence against H1a. Everything else is secondary and labelled as such; H1b is descriptive.
- **Ruling out a fall of 0.05:** this requires β̂ > −0.05 and a rejection of H0: β = −0.05 by the same bootstrap at 5% (`wcb_p_fall_005`). It replaces a separate equivalence test.
- **Reporting:** point estimates with β̂ ± 1.96 × CR1 SE, labelled as understated with few treated clusters, alongside the p-values above.

### Assumption violation/model non-convergence

- Entropy balancing: the registered fallback under Sampling weights (drop the worst-balanced variable in that province until every gap is at most 0.01; unweighted if none is left). Each fallback is reported in the output (`balance_fallback`).
- Balancing on the water share is not attempted (PAP §5).
- If the wild bootstrap and randomisation inference disagree at 5%, both are reported and the randomisation p-value governs (PAP §6).
- If placebo footprints cannot be drawn in a radar sample on R1 (for example because missing sheets shrink a province's pool below twice its treated count), the wild bootstrap p-value becomes primary for that sample, as for UNOSAT.
- The timing case is set province by province (PAP §9). Provinces in case (b) move to the R1 placebo. The analysis waits until every sample province's R1 is published, or one year after the first, whichever comes sooner.
- If R1 is surveyed before the floods (PAP §9, case b), R1 becomes a placebo and the primary test moves to R2.
- If R1 is delayed a year (case c), the same code runs on the 2028–31 round.

### Reliability and robustness testing

- **Treatment rule:** thresholds of 10% and 50%; a 2021–23 radar reference; cropland pixels excluded.
- **Provinces:** inclusion threshold of 20 or 30 treated sheets.
- **Controls:** buffers of 2 km and 10 km; all dry controls; dropping the 24 optically flooded controls (18 in Nong Khai); dropping controls in districts (and, where listed, tambons) with a 2024 emergency-zone declaration, if the lists are obtained; dropping sheets flooded again in the 2026 season (controls at 1% or more, treated sheets above 25%, by the registered radar rule).
- **Weights and covariates:** weighting on value, height and the rural indicator only (no land-cover shares); dropping the 8 high-water treated sheets.
- **Specification:** within-cluster fixed effects; area and parcel weights; unweighted; 1:1,000 and 1:4,000 sheets only.

Coded at registration: the primary estimate, interaction, H1b, test of a fall of 0.05, Holm adjustment and the five specification sensitivities above (`analyse`). Also coded (`rq1_round_change.py --sensitivities`; estimate, CR1 SE and wild bootstrap p): thresholds of 10% and 50%, province thresholds of 20 and 30, buffers of 2 and 10 km, all dry controls, the 2021–23 radar reference and cropland exclusion (each on a sample rebuilt by `rq1_sensitivity_samples.py` and hashed below; masks apply to the treatment rule, which also needs half the box valid after masking; the controls are the registered ones), weighting on value, height and the rural indicator only, the high-water and optical drops (the rules are registered, not the counts of 8 and 24), the 2026-flood drop (`flood_s1_2026.py`: the registered radar rule on the 2026 season, fixed on 2026-11-03, the day the shares were computed; a share counts where valid pixels cover half the box, which binds on no current sheet; controls at 1% or more and treated sheets above 25% dropped; 2024 radar sample only; 34 treated, 18 of them in Nakhon Phanom, and 47 controls on the registered sample), and the stacked 2024–2025 test; each reports any balance fallback. The moved-unit outcome and its Lee (2009) bounds are coded in `rq1_lee_bounds.py` (trimming within province, provinces without moved units in a group skipped and reported; cluster-bootstrap interval over whole 1:50,000 sheets, 999 draws stratified by province and by whether a cluster holds treated sheets; PAP §5). The disaster-declaration drop is coded too (`rq1_declarations.py`: fixed list schema, Thai-name matching to OCHA COD-AB districts and tambons, unmatched names stop the run); it runs once the DDPM lists are entered, and stops on any unmatched name, malformed date or village row without its tambon. The case-(b) placebo runs the registered code unchanged on those provinces (`--provinces`, with `--placebo` for the R1 placebo); the sensitivities and Lee bounds take the same `--provinces`. On R1 the code stops if a sample province's file is missing, duplicated (two files for one province) or identical to a 2023–26 file, or if more than 99% of the parcels matched in a province keep their 2023–26 value (an old round re-saved or re-issued), or if more than 50% of them move by one common new-to-old ratio to three significant figures (a unit change or rescaling, such as 0.25 for square wah to square metre), and records each run's R1 SHA-256. With mixed timing, each sample's case-(a) provinces on R1 form the R1 Holm family, and the case-(b) provinces on R2 (`--round R2`) a second family, each adjusted on its own (`--holm`; PAP §9).
- **Replication:** the 2025-flood sample (PAP §10), and a stacked 2024–2025 test reported alongside, not substituted.
- **Validation:** after registration, 100 random sheets against high-resolution imagery.

### Exploratory analysis

Secondary but pre-specified (used to interpret, PAP §11, not confirmatory):
- persistence into R2;
- duration contrasts: sheets flooded in both maps against UNOSAT only, and the number of 2024 radar scenes with water on the sheet.

Labelled exploratory in any paper:
- heterogeneity by scale (urban against rural);
- a pre-trend test if an earlier round arrives;
- links from λ_T to bank collateral values (λ_B), which depend on the stated assumption in `05_design/framework.md` §1.

# Gap statement and candidate research questions

**Working draft, 2026-11-02, for CP2.** It is built on `literature_review.md`; citekeys refer to `references.bib`. Throughout, a plain statement is established evidence, *Interpretation* marks my judgement, and RQ or H marks the author's hypotheses.

## The five closest papers and what they do not do

| # | Paper | What it does | What it does not do |
|---|---|---|---|
| 1 | Albertazzi, Djekic & Ponte Marques (2026), ECB WP 3224 [@albertazzi2026physical]; read at intro depth | Satellite flood perimeters (Copernicus) combined with euro-area loan-level data; spatial RD at the flood edge. Lending rises then reverses; default on existing loans rises by about 0.7 pp. | No collateral values, recoveries or LGD; no IFRS 9 staging or provisions; covers advanced economies where insurance and aid exist; recent floods only, with short horizons. |
| 2 | Chitchumnong, Hatairatana & Khangphukhieo (2025), CRC Edinburgh WP [@chitchumnong2025physical]; read in full | One Thai bank's mortgage book around the 2011 floods. Vintage default model and extreme-value stress scenarios. Post-flood default fell below predicted levels because of debt relief. | No geolocation of collateral, no LGD or valuations, no staging; descriptive decomposition rather than quasi-experimental identification; one bank and one product. |
| 3 | Caloia & Jansen (2021), DNB [@caloia2021flood]; read at intro depth | Geocoded collateral of Dutch banks matched to flood maps; LGD driven by collateral damage. CET1 losses are non-linear across increasingly extreme scenarios, an informal reverse stress test. | Hazard is modelled, not observed, and no causal effect of realised floods is estimated; no formal inversion to solve for the breaking point; the setting is a highly protected, insured advanced economy. |
| 4 | Garbarino & Guin (2021), *J. Financial Stability* [@garbarino2021high]; read at intro depth | After the English floods, sale prices fell 2.6–4.2% but lender valuations did not follow, an upward bias of about 3%. | No default, LGD or provisioning outcomes; insured setting; transaction-based, with no official appraisal values. |
| 5 | Pérez Montes et al. (2025), Banco de España *Financial Stability Review* 48 [@perezmontes2025impact]; read in full (annexes not read) | Credit-register difference-in-differences after the October 2024 Valencia floods, at borrower level. Stage 2 rose by about 0.5 pp for firms and 0.45 pp for households, then faded. The most exposed banks moved more loans into stage 2 and fewer into stage 3 while moratoria were in force (pp. 19–21). | Four-month horizon; treatment by postcode lists, not flood intensity; no LGD or collateral values; insured setting (Spain's public insurer); one advanced economy. |

Also close:
- Sawada et al. [@sawada2018land; @sawada2014natural], the only Thai land-price studies after 2011. They use survey and broker price series, not official appraisals, and province-level treatment.
- Guo et al. [@guo2026rising]. After Hurricane Sandy, New York City property-tax assessments fell for inundated homes, largely through tax relief, but did not change for undamaged high-risk homes. This is the closest test of official values, though for tax rather than collateral.
- Blickle et al. [@blickle2025bad], whose "6.7 standard deviations to failure" is a hazard-based breaking-point calculation for US banks.
- The BOT–World Bank district-level mapping of corporate lending exposure [@dolk2025assessing].

## The gap, in one sentence

Recent advanced-economy evidence shows that floods surface briefly in IFRS 9 stage 2 and that official tax assessments ignore updated hazard. Still, no study traces how flood exposure, measured at the level of individual collateral, moves the state's official land valuations and banks' collateral values, borrower PD and LGD, and staging over horizons long enough to see losses materialise. Nor has any study done so in an emerging market where insurance is negligible and regulatory relief censors observed default. Without that evidence, neither banks nor supervisors know whether provisions and capital reflect flood risk, or what flood severity would breach capital thresholds.

*Status of the absence claims (re-tested 2026-11-02, `strands/S6_notes.md`):*
- (a) **Staging.** The claim was narrowed after Pérez Montes et al.
- (b) **Formal reverse stress test on a hazard variable.** The claim holds. DNB WP 796 is still [UNVERIFIED] and must be read before submission.
- (c) **Official values.** The claim was narrowed after Guo et al.; it still holds for official land valuations in an emerging market and for ex-ante satellite-measured hazard.
- (d) **Asian loan-level PD/LGD.** The claim holds for bank loans.

The searches did not use OpenAlex or Semantic Scholar (quota), so a final check before submission is still advisable.

## Why Thailand makes this answerable

**Evidence: what exists and is verified**
- **2011 floods.** Damage and losses of THB 1.43 trillion, mostly private and manufacturing [@worldbank2012thai]; the event is captured in the Global Flood Database [@tellman2021satellite]. Later floods are observable with Sentinel-1 at 10–20 m.
- **Insurance.** Fewer than 1% of dwellings were insured against natural disasters in 2011 [@worldbank2012thai], so the insurance channel that drives US results [@gallagher2017household] is largely absent.
- **Rule-based relief with sharp thresholds:**
  - in 2011, a freeze of the pre-flood classification for debtors who were performing when the flood hit, in declared disaster areas and for indirectly affected debtors [@bot2011circular1564], and, as reported by the World Bank, a three-year moratorium at state banks for borrowers with total debt under THB 500,000 [@worldbank2012thai];
  - a statutory soft-loan facility [@bot2012emergency];
  - a standing 2024 template that preserves borrowers' pre-disaster classification [@bot2024relief].
- **Public data (`03_data/inventory_R3.md`):**
  - parcel-level official land appraisal values from the Treasury Department (round 2023–26, open licence; snapshot saved 2026-11-02; next round due 2027);
  - monthly commercial-bank loans and deposits by province since 1996.

*Interpretation.* Because the insurance channel is switched off and replaced by relief, Thailand isolates the mechanisms the advanced-economy literature cannot separate.

## Candidate research questions

**RQ1 (Chapter 1, public data). Do official land valuations price flood risk?**
Are flood hazard and realised floods capitalised into Thailand's official land appraisal values, and how quickly?

*What these values are.* They are the state's valuation, set by provincial committees by market comparison from registered sales and other market evidence, and they are the base for transfer fees [@th2020appraisalmr; @dol2026fees]. No public BOT rule ties bank collateral values or LTV to them [@bot2019collateral] (details in `04_analysis/treasury_method_notes.md`).

*Why they matter for credit.* They are the only public, nationwide, parcel-level measure of whether market-comparison valuation prices flood hazard. Bank collateral values (λ_B in `05_design/framework.md`) are observable only with Tier 2 data. Using RQ1's λ_T as a proxy for λ_B in RQ3 is an explicit assumption, tested in RQ2 if access is granted.
- Design sketch: a cross-section of the 2023–26 parcel appraisals against 2011 flood intensity and flood recurrence at map-sheet level, within districts.
- Once the 2027 round is published: a difference-in-differences design for parcels flooded between rounds (for example the 2024 northern floods, observable with Sentinel-1), compared with nearby unflooded parcels.
- Hypothesis (H2a): appraisal values respond weakly and slowly to flood hazard, so LTVs, and therefore LGD, are understated in flood-prone areas.
- Feasibility risks:
  - parcels can be located only at map-sheet level until parcel geometry is obtained;
  - whether earlier appraisal rounds are available is unknown;
  - Sentinel-1 processing needs Google Earth Engine or a direct download (CP3).

**RQ2 (Chapter 2, restricted data). Where does flood risk surface in credit risk when relief censors default?**
Does flood exposure of collateral raise PD and LGD, and does it surface first in restructuring and stage 2 rather than in 90-day default?
- Design sketch: spatial RD or intensity DiD on loan-level data with collateral locations, from a partner bank or a credit-bureau agreement held by the host university. The 2011 relief rules would separate the flood effect from the relief effect: pre-flood performing status [@bot2011circular1564], declared flood zones, and the THB 500,000 threshold at state banks, which is so far known only from the World Bank report. See `02_policy_context/policy_timeline.md`.
- Hypotheses: H1, plus H-S5a (staging and restructuring respond more than default). Short-horizon support for H-S5a in an insured setting: [@perezmontes2025impact]. The contribution here is the uninsured, relief-dominated setting, flood intensity and LGD, and whether stage 2 later becomes loss.
- Plan B: listed-bank disclosures of staging and restructuring around flood years, plus provincial credit aggregates. This is weaker, but uses public data only.

**RQ3 (Chapter 3, stress test). What flood severity breaks bank capital?**
Given the elasticities from RQ1–RQ2 and observed geographic concentration, what flood severity breaches capital thresholds, and how much does relief policy move that breaking point?
- Design sketch: a formal reverse stress test over a physical hazard variable (return period or inundation extent), solved by inversion in the spirit of [@grundke2018macroeconomic] and [@caloia2021flood]. Calibration uses public provincial credit data and published bank disclosures. The pipeline is built and tested on synthetic loan-level data.
- Hypothesis: H3.

*Interpretation.* RQ1 is the proposal's anchor, because it is novel, uses public data and can be answered whatever happens to data access. RQ2 is the high-value chapter that depends on data access. RQ3 turns the estimates into the policy tool supervisors and banks need. I recommend presenting RQ1 and RQ3 as the core and RQ2 as conditional on Tier 2 access, with an explicit Plan B.

## Research governance (to state in the proposal)

The proposal should state that the project uses only public data and data obtained through formal access agreements.

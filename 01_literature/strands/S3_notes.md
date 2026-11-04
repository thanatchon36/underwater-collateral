# Strand S3: Climate risk in credit-risk models, IFRS 9 ECL and stress testing

**Working draft, 2026-11-02, for the author to rewrite in their own voice.** Labels: **[E]** established evidence (from a source opened on 2026-11-02, at the stated read depth); **[H]** the author's hypotheses; **[S]** my speculation or judgement. Page numbers are printed page numbers unless marked "PDF p.". Bib keys refer to `S3.bib`.

Scope note: OpenAlex's shared daily budget for this IP was exhausted and Semantic Scholar returned HTTP 429 throughout, so searching relied on Crossref, RePEc/IDEAS/EconPapers, institutional sites and three web searches. Coverage is therefore narrower than planned (see the final section).

---

## 1. Synthesis

**What is established [E].** Supervisory climate exercises now share a common approach to acute physical risk. A hazard footprint is turned into property damage, damage cuts collateral value, and higher loan-to-value ratios raise LGD and, to a lesser degree, PD. The ECB's 2022 flood scenario shocks real-estate prices in flood-risk regions, mapped at NUTS3 level, so that LTVs and then LGDs rise (`ecb2022climate`, pp. 43–44). Participants in the Federal Reserve pilot mostly lowered property values by uninsured damage, using existing PD/LGD models (`fed2024pilot`, pp. 17–19). In the DNB flood test the LGD increase "entirely reflects" collateral damage (`caloia2021flood`, p. 18). The same exercises report that banks' credit models are not yet climate-sensitive. ECB 2022 found PDs and LGDs "fairly insensitive" to the climate shocks, and that projections did not clearly separate medium- from high-flood-risk areas (pp. 6, 34–35, 44). Banks lack data on building characteristics, insurance and asset location (`fed2024pilot`; `boe2022results`). None of these exercises set capital requirements (`ecb2022climate`; `boe2022results`). Two results recur. First, losses are concentrated geographically: in the BoE exercise, 45% of mortgage impairments came from 10% of postcode areas. Second, capital depletion is non-linear in flood severity: about 110–132 bp of CET1 for floods in unprotected Dutch areas against well over 700 bp for an extreme flood in the protected west (`caloia2021flood`, p. 5; see also `lepore2024beyond`). On provisioning, US banks in counties with higher disaster risk recognise larger loan-loss provisions (`dalmaso2024does`). After the 2013 German flood, savings and cooperative banks had higher but short-lived impairment flows, which the authors read as expected-loss provisioning that proved insufficient (`shala2024impact`). In Thailand, a bank's vintage model suggests that the 2011 floods had a modest effect on mortgage default, dampened by debt relief, while auto-loan defaults spiked (`chitchumnong2025physical`).

**What is contested [E/S].** (i) *Materiality through credit.* Acharya et al. argue that short loan maturities limit the short-run credit channel of climate risk (`acharya2023climate`, NBER WP pp. 2–3). Against this stand the concentration and non-linearity results above, which are about tail events rather than average risk. [S] Both can hold, which is a reason to study the tail, as reverse stress testing does. (ii) *Do provisions anticipate hazard?* Dal Maso et al. find an ex-ante association; Shala and Schumacher find under-provisioning ex post. Correa et al. show that loan spreads react to climate disasters through salience, and the reaction is short-lived (`correa2026rising`). The settings differ (US versus German banks, risk measure versus a realised event), so the question is open. (iii) *Scenario foundations.* The NGFS now warns that its Phase V physical-damage variables rest on a retracted paper (`ngfs2024ngfs`). (iv) *Method.* Market-based measures such as CRISK need only public data but focus on transition risk (`jung2025crisk`), whereas bottom-up tests need loan-level data.

**What is missing for this project [S].** No source read here links *satellite-observed* inundation of *individual collateral* to PD, LGD and **IFRS 9 staging (SICR) and ECL**. Supervisory tests use modelled hazard maps at NUTS3, postcode or district level; Dhima et al. map flood damage into Merton PD/LGD and capital but not staging (`dhima2026integration`, abstract). No academic study of climate-driven stage migration turned up in the searches run. Reverse stress testing is formalised for macro factors (`grundke2018macroeconomic`; `glasserman2015stress`), but the only climate example found is an informal scenario ladder (`caloia2021flood`). Inverting the problem to find the flood severity that breaches CET1 remains undone. Emerging-market evidence is thin: Thai work is either portfolio-level without geolocation (`chitchumnong2025physical`), market-based with an index hazard (`luangaram2024climate`), or district-level (`dolk2025assessing`), and IMF FSAP work in the region describes itself as exploratory (`imf2025indonesia`). Insurance assumptions carry great weight in advanced-economy exercises (`fed2024pilot`), whereas in Thailand debt relief, not insurance, is the buffer, and relief directly affects observed default and staging. **[H]** H2 (provisions do not fully reflect ex-ante flood hazard) and H3 (geographic concentration makes capital more flood-sensitive than standard stress tests assume) sit squarely in these gaps.

---

## 2. Entries

### Supervisory and official frameworks

**`ecb2022climate`: ECB Banking Supervision (2022), *2022 climate risk stress test*.** Read: intro depth (executive summary; Sections 4.3 and 4.3.4; discussion of Chart 12).
- Question: How capable are significant institutions of climate stress testing, and how exposed are they to transition and acute physical risk?
- Data/method: constrained bottom-up test; flood and drought-and-heat scenarios assumed to hit on 1 January 2022; a NUTS3 flood-risk map built from JRC work and Four Twenty Seven geospatial data, with four risk buckets.
- Findings [E]: about €70bn combined credit and market losses for 41 banks under the short-term disorderly transition and two physical scenarios, which the ECB says "significantly understates" risk. About 60% of banks lack a well-integrated framework. Credit parameters were fairly insensitive to the shocks. High- and medium-flood-risk exposures carried half of flood losses with 31% of exposures, and banks did not always separate medium- from high-risk LTV changes. No direct capital implications.

**`alogoskoufis2021ecb`: Alogoskoufis et al. (2021), *ECB's economy-wide climate stress test*, ECB Occasional Paper 281.** Read: intro depth (abstract and executive summary).
- Question/method: top-down, 30-year scenarios with a dataset covering millions of firms and about 1,600 euro area banks, plus climate-specific firm and bank models.
- Findings [E]: physical risk dominates in the long run without transition policy and rises non-linearly. Impacts concentrate in vulnerable geographies. Bank losses are highest where collateral protection is low or physical exposure high.

**`boe2022results`: Bank of England (2022), *Results of the 2021 Climate Biennial Exploratory Scenario*.** Read: abstract depth (results web page, via an automated page summary covering about the first tenth of the page; re-check figures before citing).
- Method: three 30-year scenarios (Early Action, Late Action, No Additional Action) for large UK banks and insurers.
- Findings [E]: under No Additional Action, bank impairment rates were just over 50% higher than normal levels. "45% of the mortgage impairments in the scenario are accounted for by just 10% of the 4-digit postcode areas analysed." Banks appeared less well equipped for physical risk, and estimates for the same corporate customers varied widely. The exercise "will not be used to set capital requirements related to climate risk."

**`fed2024pilot`: Board of Governors of the Federal Reserve System (2024), *Pilot Climate Scenario Analysis Exercise: Summary of Participants' Risk-Management Practices and Estimates*.** Read: intro depth (executive summary; insights; physical-risk module pp. 13–19).
- Design: six large banks; a common Northeast hurricane shock at 100-year and 200-year return-period losses in 2050, plus participant-chosen idiosyncratic shocks; static balance sheet; credit impacts estimated assuming no insurance, including no NFIP cover.
- Findings [E]: most participants used existing PD/LGD models and assumed that historical relationships continue to hold. Damage entered mainly through LTV for residential and LTV plus DSCR for commercial real estate. Building-characteristic data were missing, so vendor defaults were used. Insurance assumptions were a key design choice. PD impacts were highly heterogeneous.

**`bcbs2022principles`: BCBS (2022), *Principles for the effective management and supervision of climate-related financial risks*.** Read: abstract depth (BIS landing page only; the PDF was blocked by a JavaScript challenge).
- Content [E]: the landing page states the aim of improving banks' risk management and supervisors' practices. The number and content of the principles were not read.

**`bcbs2021climate`: BCBS (2021), *Climate-related financial risks: measurement methodologies*.** Read: abstract depth (landing page).
- Content [E]: credit risk measurement "has attracted the most effort"; initial scenario analyses covered selected portfolios and hazards; it flags "gaps in data and risk classification".

**`ngfs2024ngfs`: NGFS (2024), *NGFS Climate Scenarios for central banks and supervisors, Phase V*.** Read: abstract depth (publication page, updated 24 September 2026).
- Content [E]: the page carries a notice that Phase V physical-risk estimates rely on Kotz et al. (2024), which has been retracted from *Nature*. The affected outputs include the NiGEM physical and combined outputs and the "Kotz-Wenz" GDP-damage variables. The page says economic effects "might turn out to be more severe than anticipated", and an updated methodology is planned for the end of 2026. [S] Any Thai scenario built on Phase V physical damages needs this caveat.

**`imf2025indonesia`: IMF (2025), *Indonesia: FSAP Technical Note on Climate Risk Assessment*, Country Report 2025/051.** Read: abstract depth (EconPapers).
- Content [E]: assesses transition and acute physical risk; the transition analysis links sector scenarios to corporate vulnerability and then to bank credit exposures. The results are called exploratory, and it recommends better data and more methodological guidance for financial institutions.

### Academic reviews and methods

**`acharya2023climate`: Acharya, Berner, Engle, Jung, Stroebel, Zeng & Zhao (2023), "Climate Stress Testing", *Annual Review of Financial Economics* 15:291–326.** Read: intro depth (NBER WP 31097 version, pp. 1–5).
- Question: how to design climate stress tests and where research is needed.
- Findings/arguments [E]: research is needed on short-run credit channels given typical loan maturities, on bank lending responses, on the adequacy of climate-risk pricing, and on expectation formation. Climate risk realisations may matter less for current loans than for medium-run repayment capacity and franchise value. Market-based tests are proposed as complements.

**`jung2025crisk`: Jung, Engle & Berner (2021, revised 2025), "CRISK: Measuring the Climate Risk Exposure of the Financial System", FRBNY Staff Report 977.** Read: intro depth.
- Method: CRISK is the expected capital shortfall in a climate stress scenario, from a dynamic "climate beta" of bank stock returns to a climate risk factor (stress at the 1st percentile of six-month factor returns). It is validated with FR Y-14Q loan data.
- Findings [E]: climate betas rose from 2019 and peaked in 2020. The paper focuses on transition risk; physical applications are in separate work not read here.

**`dhima2026integration`: Dhima, Iravani, Itam & Boidot (2026), *Journal of Risk Finance* 27(3):368–391.** Read: abstract depth (Crossref).
- Method: an extended Merton model maps river-flood structural damage on real-estate exposures and collateral into PD, LGD and internal capital.
- Finding [E]: the impact is not systematic while the damage ratio stays below the expected return on immovable assets; it becomes material for firms already vulnerable in indebtedness and collateral value.

**`caloia2021flood`: Caloia & Jansen (2021), "Flood risk and financial stability: Evidence from a stress test for the Netherlands", De Nederlandsche Bank.** Read: intro depth (abstract, introduction, framework modules, results discussion).
- Data/method: geocoded real-estate exposures of ten Dutch banks (over 95% of sector assets) matched to official flood maps at the 4-digit postcode level, with supervisory and loan-level data. The PD module combines interest-rate, business and collateral-repricing (strategic default) risk; in the LGD module the increase reflects collateral damage only. The authors describe the design as "in essence, a reverse stress test", with increasingly extreme scenarios.
- Findings [E]: 110–132 bp extra CET1 depletion for floods in unprotected areas, against well over 700 bp for extreme inundation in the protected west. In the extreme case, 402 bp comes from residential real-estate damage, through LGD and RWA.

**`lepore2024beyond`: Lepore & Mok (2024), "Beyond the Dikes: Flood Scenarios for Financial Stability Risk Analysis", IMF WP 2024/197.** Read: abstract depth (EconPapers).
- Finding [E]: the effect on bank capital varies greatly across flood scenarios (region, type, climate, return period, adaptation). Climate change amplifies it and stronger defences mitigate it. Damage and capital depletion are related non-linearly.

**`grundke2018macroeconomic`: Grundke & Pliszka (2018), "A macroeconomic reverse stress test", *Review of Quantitative Finance and Accounting* 50(4):1093–1130.** Read: abstract depth (IDEAS).
- Method [E]: solves the inversion problem (scenarios that push a bank across the survival/default frontier) and computes scenario probabilities within one model, using PCA over macro risk factors. It warns of considerable model and estimation risk.

**`glasserman2015stress`: Glasserman, Kang & Kang (2015), "Stress scenario selection by empirical likelihood", *Quantitative Finance* 15(1):25–41.** Read: abstract depth (IDEAS).
- Method [E]: reverse stress testing defined as finding the most likely scenarios that produce losses above a threshold, estimated non-parametrically through the conditional mean of factors given large losses, with tail-dependent scaling.

### Empirical evidence on provisions and pricing

**`dalmaso2024does`: Dal Maso, Kanagaretnam, Lobo & Mazzi (2024; online 2022), "Does Disaster Risk Relate to Banks' Loan Loss Provisions?", *European Accounting Review* 33(3):825–854.** Read: abstract depth (IDEAS).
- Data/method: a disaster-risk measure from FEMA major-disaster declarations over 15 years; more than 445,000 bank-quarter observations; difference-in-differences and matched samples.
- Finding [E]: banks in US counties with higher disaster risk recognise larger LLP after bank-level controls.

**`shala2024impact`: Shala & Schumacher (2024), "The impact of natural disasters on banks' impairment flow – Evidence from Germany", *Journal of Climate Finance* 6:100031 (Bundesbank DP 36/2022).** Read: abstract depth (abstract and non-technical summary of the DP).
- Method: difference-in-differences around the 2013 summer flood, for savings and cooperative banks, with treatment assigned by region of primary operations.
- Findings [E]: impairment flow was significantly higher but short-lived. It was driven by corporate loans (agriculture, manufacturing) and to some extent mortgages. The authors conclude that expected-loss provisioning was insufficient despite earlier floods in 2002 and 2006.

**`correa2026rising`: Correa, He, Herpfer & Lel (2026), "The Rising Tide Lifts Some Interest Rates", *Journal of Finance* 81(5):2933–2984.** Read: abstract depth (Crossref).
- Finding [E]: loan spreads for borrowers at risk of, but not hit by, climate-related disasters rise in primary and secondary markets. Non-climate disasters produce no such reaction. The increase is short-lived, amplified by media attention, and mostly explained by salience.

### Thailand

**`chitchumnong2025physical`: Chitchumnong, Hatairatana & Khangphukhieo (2025), "Physical Climate Risk Stress Test: An Evidence-based Approach", CRC Edinburgh WP (authors at Bank of Ayudhya).** Read: full (12 pp.).
- Data/method: proprietary mortgage-portfolio data from 2009 to 2013; a vintage (age-period-cohort type) default model whose benchmark (lifecycle, vintage, seasonality) is extended with macro variables to give a lower bound. Flood-affected and unaffected borrowers are compared for an upper bound. Extreme value analysis uses Royal Irrigation Department runoff at Nakhon Sawan from 1979.
- Findings [E]: a small immediate default rise in 2011Q4 among delinquent borrowers ineligible for relief; post-flood default was lower than predicted because of debt relief. Flood-affected borrowers showed higher risk. The mortgage impact was modest because most homes suffered non-structural damage, whereas auto-loan defaults spiked. The 2011 runoff level is roughly a 1-in-50-year event (2% a year) and double that level about 1-in-1,000 (pp. 7–9). Relief ran from November 2011 to January 2012 for 1–9 months, alongside the BOT soft-loan facility of THB 210bn (p. 6).
- Limits [S]: the paper does not say how "flood-affected" borrowers were identified, and reports no geolocation, LGD, collateral values or IFRS 9 staging. Figures are shown without numerical tables.

**`luangaram2024climate`: Luangaram, Sethapramote, Thampanishvong & Uddin (2024), PIER DP 224.** Read: intro depth.
- Method: bank-level CoVaR on SET data; a brown-minus-green factor for transition risk; SPEI for physical risk; panel regressions.
- Findings [E]: BMG significantly raises systemic risk; physical risk, especially flood-related, challenges bank portfolios (abstract wording; magnitudes not read).

**`dolk2025assessing`: Dolk, Dunz, Lesage, Nie & Pollitt (2025), World Bank *All About Finance* blog.** Read: full (opened during scoping on 2026-11-02).
- Findings [E]: a 2011-based, climate-adjusted Bangkok flood scenario; output could fall by up to 10%; 41% of bank corporate lending is in districts with high riverine flood risk and 7% in very high-risk districts.

---

## 3. Hypotheses and speculation kept separate

- **[H]** H1: collateral flood exposure raises PD and LGD. H2: valuations and ECL do not fully reflect ex-ante hazard. H3: concentration makes capital more flood-sensitive than standard tests assume.
- **[S]** IFRS 9 staging is the natural place for a Thai contribution. Debt relief and restructuring flags interact mechanically with SICR and stage 2 classification, so relief may hide flood-driven credit deterioration in observed default but not in staging. This is a conjecture to test, not a finding.
- **[S]** A formal reverse stress test over a physical hazard variable (inundation depth or return period, as in `chitchumnong2025physical`'s EVT curve) combined with Grundke–Pliszka-style inversion appears not to have been done. This judgement rests on a limited search.

---

## 4. Unverified / not read

Nothing below is used as evidence above.

- [UNVERIFIED] IMF *Philippines: FSAP Technical Note on Bank Stress Test for Climate Change Risks* (2022): IMF page returned 403; the EconPapers record I tried (2022/155) is a different note.
- [UNVERIFIED] Bank Negara Malaysia (2024), *Methodology Paper on Climate Risk Stress Testing*: seen only in search snippets and in Chitchumnong et al.'s reference list, which also cites the HKMA (2023) and MAS (2020, 2022) guidance; the BNM site was not opened.
- [UNVERIFIED] Any IMF FSAP climate technical note for Thailand: none found in one search.
- [UNVERIFIED] Journal or series number for Caloia & Jansen (2021); the version read is the DNB-hosted PDF dated 2 November 2021.
- [UNVERIFIED] Full texts of Dal Maso et al. (publisher and repository returned 403), Lepore & Mok (IMF PDF returned 403) and the BCBS PDFs (JavaScript challenge).
- [UNVERIFIED] Kotz et al. (2024) retraction: reported on the NGFS page, not checked at *Nature*.
- Not opened: Breuer et al. (plausible, severe and useful stress scenarios; Crossref search did not find it); Jung et al. (2023) physical-risk CRISK application; Cartellier (2022); Vermeulen et al. (2021); Battiston et al. (2017); Breeden (2020, 2023); the ECB 2022 CST methodology (October 2021); EBA/ECB material on climate in IFRS 9; a 2026 Montenegro flood–NPL paper and Zanders practitioner notes seen only in search results.
- Carried over from scoping (metadata only): Cugliari, Narizzano & Vassalli (2026); Chu (2026). Ouazad & Kahn (*RFS* 2022) is **retracted** and is mentioned only as such.
- Searches not completed: OpenAlex (daily budget exhausted), Semantic Scholar (HTTP 429), SSRN and NBER full text. In particular, "IFRS 9 staging and climate" received only one Semantic Scholar query, which returned nothing relevant; absence of evidence here is weak.

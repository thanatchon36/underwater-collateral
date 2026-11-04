# S6: Top-up search — absence claims, snowball leads and read depth

**Working draft, 2026-11-02.** The task was to re-test the four absence claims in `01_literature/gap_statement.md` (and §7 "What is not known" in `literature_review.md`), follow the priority leads in §8 "Limitations", and raise the read depth of the closest papers. Bibliography: `S6.bib`. Matrix: `S6_matrix.csv`. Citekeys that already exist in `references.bib` are reused where depth was added.

Labels: **[E]** established evidence from a source I read, at the depth stated; **[H]** the author's hypotheses (H1–H3, H2a, H-S5a); **[S]** my speculation or judgement. Page numbers are PDF page numbers unless a printed page is stated. All PDFs were read from open working-paper, central-bank or author versions; no paywall was bypassed.

**Search sources used this session.** Crossref REST API (bibliographic queries, throttled at about one request per second; two batches of 18 and 8 queries); a general web search engine (eight queries); RePEc/IDEAS; publisher and institutional sites (ECB, BIS, Banco de España, DNB, Bank of England, RIETI, World Bank, Bank Negara Malaysia, CESifo/ifo, Copernicus NHESS, a Brookings-hosted working paper). OpenAlex and Semantic Scholar were not used (quota). SSRN, HAL (bot challenge), the IMF PDF server and direct DNB downloads refused scripted access; two DNB and CESifo PDFs were retrieved through a fetch tool instead.

---

## Absence claims re-tested

### (a) Flood or physical exposure → IFRS 9 / CECL staging, SICR, stage migration or ECL

**Queries.** Crossref: "flood IFRS 9 staging significant increase in credit risk"; "physical climate risk expected credit loss IFRS 9 banks floods"; "natural disasters loan loss provisions CECL banks"; "flood stage 2 loans climate exposures banks". Web: "flood exposure IFRS 9 stage 2 loans 'significant increase in credit risk' physical risk empirical bank"; "Banco de España Financial Stability Review 48 Valencia DANA flood exposures stage 2 loans Pérez Montes".

**Result: the claim is contradicted in its strong form.**
- [E] **perezmontes2025impact** (Banco de España *Financial Stability Review* 48) estimates borrower-level difference-in-differences on Spain's Central Credit Register after the October 2024 Valencia floods, with stage 2 and stage 3 as outcomes. Stage 2 shares rose temporarily (firms about +0.5 pp in December 2024–January 2025; households +0.45 pp in December 2024), and the most exposed banks reclassified more to stage 2 and less to stage 3. Details below.
- [E] Already in the review and relevant here: Shala & Schumacher (impairment flow, Germany; `shala2024impact`, abstract) and Dal Maso et al. (US disaster risk and loan loss provisions; `dalmaso2024does`, abstract). Neither studies staging.
- [E] Albertazzi et al. (2026) use AnaCredit, which records provisions, but their credit-risk outcome is the default ratio (Tables 8–9, pp. 27–28); stage indicators appear only as balance covariates (p. 18).
- Not found: any peer-reviewed study of flood effects on staging or SICR; any study of staging or ECL after floods in an emerging market; any study linking *collateral-level* hazard to staging. Crossref returned only generic IFRS 9 or CECL papers for these queries.

**Implication for the gap statement [S].** "No study yet traces how flood exposure … moves … IFRS 9 staging" is no longer defensible. Revise to: the only staging evidence is a short-horizon (four-month) central-bank article on one flood in an insured advanced economy, with postcode-level treatment and no LGD or collateral-value outcomes. No evidence exists for an emerging market, where relief rather than insurance is the buffer, or over horizons long enough to see whether stage 2 migration later becomes default. Pérez Montes et al. should be cited as the closest prior evidence for H-S5a, and probably added to the five-paper table.

### (b) Formal reverse stress test on a physical-hazard variable

**Queries.** Crossref: "reverse stress test physical climate risk flood"; "reverse stress test natural catastrophe bank capital". Web: "'reverse stress test' flood OR hurricane OR 'physical risk' bank capital breaking point climate"; Bank Negara Malaysia methodology paper (lead).

**Result: the claim survives, provided it says "formal inversion".**
- [E] **caloia2021flood** describes its own design as "in essence, a reverse stress test" (p. 6), but it is implemented as escalating scenarios (1, 3 and 5 m inundation; unprotected vs protected areas). It does not solve for the severity that breaches a threshold. The gap statement already calls this "informal".
- [E] **bnm2024climate** (Bank Negara Malaysia) prescribes a forward one-off 1-in-200-year nationwide flood under RCP 8.5 (S 14.1, p. 23), not a reverse test.
- [E] **pozdyshev2025incorporating** (BIS WP 1274) extends the Vasicek model with a climate-event state; it gives an illustrative calibration, not a reverse test.
- [E] Blickle et al.'s "6.7 SD" figure (`blickle2025bad`, already in the review) remains the closest published breaking-point calculation.
- Not found: a study that inverts a credit-loss model over return period, inundation depth or extent to find the capital-breaching severity. Crossref hits were off-topic (IRRBB, hydrology). One web-search summary listed a DNB follow-up, *Floods and financial stability: scenario-based evidence from below* (DNB WP 796). The PDF returned 403 and I did not read it, so it must be checked before submission ([UNVERIFIED]).

### (c) Do official, assessed or appraisal values capitalise flood hazard or flood events?

**Queries.** Crossref: "assessed property values flood tax assessment"; "appraised value flood risk appraisal bias"; "official land price flood hazard Japan posted land price"; "benchmark land price flood China". Web: "property tax assessed values flood risk capitalization assessor flood zone hedonic 'assessed value'". RIETI DP 14-E-029 (lead) was read for its data source.

**Result: the claim is contradicted for *any country*. It still holds for Thailand and for ex-ante hazard in official collateral-anchoring appraisals.**
- [E] **guo2026rising** (Guo, Miao, Kim & Hou 2025) is a direct test on official assessments. After Hurricane Sandy, New York City assessor-estimated market values of inundated homes fell by 17% and assessed values by 10%, against a 10% fall in sale prices. Non-inundated homes in the high-risk zone lost 11% in sale price, with no change in assessed values. Event damage therefore reached official values, largely through tax relief, but the hazard update did not.
- [E] **garbarino2021high** (now read at results depth) shows that *lender* refinancing valuations did not follow a 2.6–4.2% fall in sale prices.
- [E] Already in the review: Wei & Zhao (`wei2022effect`) argue that Chinese government benchmark land prices already incorporate flood hazard. Mori et al. (`mori2016flood`) find that publishing hazard maps had very little effect on Japanese land prices. [S] The review should check whether Mori et al. use official posted land prices (*kōji chika*). If they do, the review already contains a counter-example to claim 2 of §7.
- [E] Thailand: **sawada2014natural** uses JETRO industrial-estate price surveys and Agency for Real Estate Affairs (AREA) district series, not Treasury Department appraisals (pp. 9–11). The Thai-specific absence holds.

**Implication [S].** Rewrite claim 2 of §7 and the RQ1 novelty claim along these lines: "Official assessments in the United States respond partly to realised flood damage through tax relief but not to updated hazard (Guo et al. 2025). No study examines official appraisal values that anchor *bank collateral valuation*, in an emerging market, or ex-ante satellite-measured hazard." RQ1 stays novel on these three margins, but the general claim must go. Guo et al. also supply a ready design template (DiD on assessment rolls) and a mechanism, assessment caps and relief rules, that has Thai analogues.

### (d) Loan-level evidence on floods and PD or LGD in emerging markets, especially Asia

**Queries.** Crossref: "flood mortgage default emerging market loan-level"; "flood loan default microfinance Bangladesh"; "typhoon loan default Philippines bank"; "natural disaster probability of default loss given default loan level"; "flood loss given default collateral". Web: two queries combining loan-level, borrower-level, flood, typhoon and default with China, India, Vietnam, Philippines, Indonesia, Pakistan and Bangladesh.

**Result: the claim survives for bank credit, with two qualifications.**
- [E] **nie2023banking** (World Bank PRWP 10326) is the closest Asian bank evidence, and it is aggregate: in the Philippines, a 1 pp rise in typhoon damage relative to regional GDP is associated with a rise in the NPL ratio of up to 2.3% (regional data, 2011–2018; p. 5).
- [E] **brei2024transmission** (Caribbean and Central America; bank-level, abstract) finds persistent loan defaults and bank losses in continental countries and losses after four years in small islands.
- Microfinance borrower-level studies exist but were not read: Shoji (2010, *J. Development Studies*) on contingent repayment after the 2004 Bangladesh flood, and Becchetti & Castriota (2011, *World Development*) on MFI loan records after the 2004 tsunami in Sri Lanka. Metadata were verified via Crossref; no abstract was read. They concern MFI repayment, not bank PD or LGD.
- Secondary, not read: Albertazzi et al. (p. 9) report that Fatica et al. (2024a) find, for securitised European SME loans, a *fall* in PD within six months of a flood (attributed to subsidies) followed by a rise at 12–24 months. [UNVERIFIED] Highly relevant to relief censoring; read before drafting. **Resolved 2026-11-02:** see S8_fatica_notes.md (it is Barbaglia, Fatica and Rho 2024, `barbaglia2024flooded`, read in full).
- Not found: any loan-level study of PD or LGD after floods for bank borrowers in Asia apart from Chitchumnong et al. (Thai, single bank, already in the review). No LGD study of any emerging market was found.

**Implication [S].** Keep the claim but narrow it to *bank* loans and to PD *and* LGD. Mention the microfinance literature in one line so a reviewer cannot say it was missed.

---

## Per-paper entries

**perezmontes2025impact** — Pérez Montes (coord.), García Villasur, Gutiérrez de Rozas, Jiménez, Lavín, Matyunina & Vegas (2025), Banco de España *Financial Stability Review* 48, pp. 5–40, doi 10.53479/40135. *Read: full (Sections 1–5; Annexes not read).*
- Q: size and quality of bank exposures in the areas hit by the October 2024 Valencia flash floods, and whether credit and credit quality in those areas diverged afterwards.
- Data: Copernicus flood geolocation matched to the Central Credit Register (CIRBE) and the Cadastre; real-estate collateral is geolocated (pp. 4–6).
- ID: borrower-level DiD, September 2024 to February 2025. Treatment: borrowers or collateral in postcodes of municipalities listed in RDL 6/2024. Control: propensity-score-matched Mediterranean-coast postcodes (matched on income, population, share over 65, number of firms, firm NPL ratio and 500-year flood probability). Firm/household and sector × time and main-bank × time fixed effects (pp. 16–17).
- Exposure [E]: affected lending was 2.6% and 1.7% of national credit to households and firms respectively (p. 4). In September 2024, 8.5% of credit to firms in the affected areas was in stage 2 and 5.5% non-performing; for households, 6.4% and 4.3%. All four ratios were above the national averages (6.8% and 5.9% in stage 2; 4.2% and 3.8% non-performing) (p. 4).
- Findings [E]:
  - Firms: stage 2 share up nearly 0.5 pp, significant for December 2024–January 2025 combined, about 4.5% relative to the mean, falling back in February (p. 19). NPLs significant from January 2025, +3.4% relative (p. 20).
  - Households: stage 2 +0.45 pp in December only (+4.1%), then insignificant; stage 3 +0.44 pp from December (about +9.1%) (p. 21).
  - Banks most concentrated in the affected areas (over 40% of credit there): stage 2 loans to affected firms +24% and stage 3 −9%, against about +3% stage 3 at other banks (p. 21).
  - The authors caution that moratoria under RDL 6/2024 may have improved measured credit quality (p. 17).
  - Credit stocks: firms +2% by February 2025; households up to +0.7% (pp. 17, 21).
- Relevance [S]: 5. This is the first direct evidence that floods surface in stage 2, and that exposed banks shift losses from stage 3 into stage 2 while relief is in force, which is exactly H-S5a. The project differs in having an emerging market with thin insurance (Spain has the CCS public insurer), a national-scale event, satellite intensity rather than postcode lists, LGD and collateral values, and multi-year horizons.

**guo2026rising** — Guo, Miao, Kim & Hou (2025), "Rising Waters, Falling Taxes: The Impact of Hurricane Sandy on Property Tax Assessments in New York City", working paper dated 23 June 2025 (PDF hosted at brookings.edu). *Read: intro and Sections 3.4, 5.1–5.2 (pp. 1–6, 18, 22–24).*
- Q: did Sandy change official property assessments and tax burdens, for inundated homes and for undamaged homes in high-risk zones?
- Data: NYC Department of Finance assessment rolls (assessor-estimated market value, assessed value, exemptions) and property sales; Class 1 residential.
- ID: DiD, inundated vs non-inundated homes; second specification adds evacuation Zone A × post for non-inundated homes (pp. 4, 21–24).
- Findings [E]: inundated homes' sale prices −10%; assessor-estimated market values −17%, "mostly due to the tax relief policy"; assessed values −10%; taxable values −6.5% (Table 3, pp. 22–23). Non-inundated homes in Zone A: sale prices −11%, but no change in assessor market, assessed or taxable values (Table 4, p. 24). Statutory caps (6% a year, 20% over five years) blunt the transmission; about 80% of properties were capped before Sandy (p. 10).
- Relevance [S]: 4. This is a direct counter-example to "no study of official values". It shows that official values respond to realised damage through rules, not to hazard updates. The project differs in studying an emerging market, appraisal values that anchor bank collateral (Thai Treasury appraisals) rather than tax assessments, and ex-ante satellite hazard.

**sawada2014natural** — Sawada, Nakata & Sekiguchi (2014), RIETI DP 14-E-029. *Read: full for Section 3 (land prices) and abstract/intro; Section 2 (location choice) skimmed.*
- Q: did 2011 flood awareness affect firms' location choice, and did the floods affect land prices?
- Data: RIETI survey of firms in Thailand (185 Thai responses); JETRO survey of about 40 industrial estates (IEs) with ten rounds from October 2008 to November 2012 and seven flooded IEs; AREA district price series in 43 districts across nine provinces (pp. 4, 9–11).
- ID: DiD with IE or district fixed effects; flooded provinces (Ayutthaya, Pathum Thani, Nonthaburi) treated (p. 11).
- Findings [E]: IE land prices in flooded estates fell about 10% of the mean relative to non-flooded estates (−337.9, significant at 10%; Table 10, PDF p. 29). The authors attribute the gap to rising prices in non-flooded areas rather than falls in flooded ones (p. 10). AREA data: industrial land −1,025 (10%) and townhouses −71,456 (5%) relative; residential and commercial land not significant (Table 12, PDF p. 30).
- Relevance [S]: 4. This is the working-paper precursor of `sawada2018land` and confirms that neither version uses official appraisal values.

**nie2023banking** — Nie, Regelink & Wang (2023), World Bank Policy Research Working Paper 10326. *Read: abstract and introduction (pp. 2–4); Section 4 skimmed.*
- Q: effect of climate-related disasters on system-wide NPLs, across countries and in the Philippines.
- Data/ID: 184 countries over nearly 40 years, local projections; Philippine regional banking data, 2011–2018.
- Findings [E]: severe disaster episodes raise system-wide NPLs persistently. A 1 pp rise in typhoon damage relative to regional GDP is associated with an NPL ratio up to 2.3% higher in the Philippines (p. 5). The authors cite BSP (2020) as regional and bank-level Philippine evidence (p. 7; not read).
- Relevance [S]: 3. The closest Asian bank evidence, but aggregate.

**brei2024transmission** — Brei, Mohan, Pérez-Barahona & Strobl (2024), *Journal of International Money and Finance* 141:103008. *Read: abstract (RePEc/IDEAS).*
- Finding [E]: 92 damaging tropical storms and 111 banks in 20 Caribbean and Central American jurisdictions. Storms bring immediate and lasting adverse funding shocks (deposit withdrawals in small islands; short-term funding in continental countries), and lending to the private sector falls in the first years. Defaults and losses persist in continental countries, while in small islands losses appear only after four years. The authors call the recovery "credit-less".
- Relevance [S]: 3. Emerging-market, bank-level, storms rather than floods. The four-year lag in loss recognition is consistent with H-S5a (losses surface late).

**bnm2024climate** — Bank Negara Malaysia (2024), *2024 Climate Risk Stress Testing Exercise: Methodology Paper*, BNM/RH/PD 028-132, 29 February 2024. *Read: contents and Part C2 (pp. 2–3, 23–24); keyword search of the full text.*
- Content [E]: the acute scenario is a one-off 1-in-200-year nationwide flood consistent with RCP 8.5 in 2050, applied to the 31 December 2023 balance sheet (S 14.1, S 14.9–14.10). Banks must assume no government policy interventions that would reduce losses (S 14.5), must assess flood risk at least at postcode level (S 14.7), and must cover residential, non-residential and construction property loans at minimum (S 15.1). Traditional macro-driven models "may not be sufficiently sensitive" to localised flood losses (G 14.4).
- Relevance [S]: 4. This is a regional supervisory template and the closest ASEAN comparator to BOT's expectations. It is forward-looking, not reverse. The no-relief assumption contrasts with the Thai setting, where relief is the main buffer.

**pozdyshev2025incorporating** — Pozdyshev, Lobanov & Ilinsky (2025), BIS Working Paper 1274. *Read: abstract and Annex 1 illustrative example (keyword search).*
- Content [E]: extends the one-factor Vasicek model with a climate-event state that carries separate LGD values. In the illustrative example, LGD rises from 10% to 24.8% when the climate state occurs, and unexpected loss rises from 0.0069 to 0.0744 (pp. 28–29).
- Relevance [S]: 2. Modelling only; a candidate building block for the RQ3 loss model.

**fontana2025flood** — Fontana, Jarmulska, Scheid, Scheins & Schwarz (2025), "From flood to fire: is physical climate risk taken into account in banks' residential mortgage rates?", ECB WP 3036. *Read: abstract.*
- Finding [E]: on average, euro-area banks charge a physical-risk premium on mortgages, and it has risen; banks judged "adequate" in the ECB thematic review charge more.
- Relevance [S]: 2. Pricing of hazard, not staging. Recorded because a search engine surfaced it for the staging query.

**fitzmaurice2026flood** — Fitzmaurice et al. (2026), *Natural Hazards and Earth System Sciences* 26:675–701. *Read: abstract.*
- Finding [E]: simulation for seven North Carolina floods, 1996–2019. Damage was USD 4.0 bn, 66% of it uninsured; only 48% of flood-affected mortgage borrowers were insured, and 32% lacked the income or collateral to finance repairs through home-equity borrowing.
- Relevance [S]: 2. A US, simulation-based counterpart to the negative-equity (LGD) channel.

### Depth upgrades of existing entries

**albertazzi2026physical** — ECB WP 3224. *Read depth raised from intro to full text, results sections, not cover-to-cover (Sections 3, 5.3 and Table 17 of 5.5; opening of Section 6; Sections 5.1–5.2 and 5.4 not read in detail).*
- Data [E]: four floods (DE/BE/NL 2021; Marche–Umbria 2022; Emilia-Romagna 2023; Valencia 2024); AnaCredit loans of at least €25,000, located by the borrower's *registered address*, not by collateral (p. 12). Ex-ante hazard comes from the ECB's 0–5 indicator under RCP 4.5 (p. 13).
- Default [E]: default ratio +0.568 pp after one quarter (significant at 10%; Table 8, p. 27) and +0.680 / 0.692 / 0.639 pp over two quarters (Table 9, p. 28). That is about 0.7 pp against a 1.4% average annual default rate, a near doubling; across bandwidths, 0.4–0.9 pp (Table 31).
- Collateral [E]: for real-estate-backed loans to micro firms, LTV rises 5.3 pp (5%); the large-firm interaction is −6.2 pp (Table 17, p. 39). The authors read this as consistent with falling collateral values.
- [S] Collateral location and LGD are still not used, so the "what it does not do" column stands. Correct "covers advanced economies where insurance and aid exist" only in emphasis: the authors note (p. 9) that just 25% of EU catastrophe losses are insured.

**caloia2021flood** — now confirmed as DNB Working Paper No. 730 (November 2021). *Read depth raised from intro to full text, results sections, not cover-to-cover (Sections 1 and 5; methodology not read).*
- Findings [E]:
  - Unprotected areas: CET1 −110 bp at 1 m and −132 bp at 5 m inundation (p. 22).
  - Protected western Netherlands: −307 bp at 1 m, close to −400 bp at 3 m and −712 bp at 5 m (p. 23).
  - In the extreme case, residential real-estate damage contributes 402 bp, via LGD and RWA; in the mild case, macro-financial shocks contribute 59 bp (p. 24).
  - The authors call the exercise "in essence, a reverse stress test" (p. 6).
- [S] The `url` and series number in `references.bib` should be replaced with the WP 730 version (done in `S6.bib`).

**garbarino2021high** — BoE SWP 856. *Read depth raised from intro to full text, results sections, not cover-to-cover (Section 3 data, Sections 4.1–4.3.1).*
- Data [E]: 38,747 refinanced mortgages within a ±3-year window around the 2013–14 winter floods; Environment Agency flood outlines and the 2013–14 hazard-map update (p. 14).
- Findings [E]:
  - Prolonged flooding lowers sale prices by 4.2% (full sample), 3.3% (matched) and 2.6% (with controls) (Table 3, p. 22).
  - The refinancing-valuation differential is +3.2% / +2.9%, unchanged with controls. Valuations are on average 3.4% below sale prices.
  - "Risk up" raises prices by 1.0–1.1% with a −1.2% valuation differential.
  - Rates rise 31 bp / 21 bp in the full sample, but the effect is not robust (14 bp / 9 bp, insignificant); loan amounts are not robustly affected (Table 5, pp. 23–24).
  - Lenders update valuations with house-price indices too aggregated to capture local flood effects (Section 4.3.1).

**noy2021floods** — read via CESifo WP 7644 (May 2019), the open version of the EDCC article. *Read depth raised from abstract to full text, results sections, not cover-to-cover (working-paper version: data, Section 5 text, conclusions; tables not read).*
- Data [E]: Thai Household Socio-Economic Survey waves with a 2012 flood module (self-reported exposure), plus GISTDA satellite images taken weekly from May to December 2011 at 50 × 50 m, giving inundated sub-districts and flood duration (under or over two weeks) (p. 16). Satellite readings cover only Central and Northeastern provinces (fn. 25).
- Findings [E]:
  - Losses are concentrated in business income: −THB 6,465 for directly flooded households and −THB 4,018 for spillover households (Section 5.3, p. 26).
  - Total expenditure does not change significantly; housing spending rises and luxury spending falls (p. 22).
  - Floods of more than two weeks roughly double the income coefficients (pp. 30–31).
  - **Debt and savings: flood coefficients are "small and statistically insignificant"**, the regressions are unreported, and the authors attribute this to reporting noise (pp. 22–23, 33).
- [S] This is the only Thai satellite-plus-microdata study. It gives no usable household-debt result, so it does not pre-empt RQ2, and GISTDA's 50 m duration product is a candidate 2011 exposure source.

---

## Unverified / not read

Not used as evidence; tagged [UNVERIFIED] wherever mentioned.

- [UNVERIFIED] Liew, Gupta, Chia & Ang (2016), *Geomorphology* 262:112–122, doi 10.1016/j.geomorph.2016.03.022. Crossref metadata re-confirmed, but Crossref holds no abstract and no open version was found. Not read; time-boxed.
- [UNVERIFIED] DNB Working Paper 796, *Floods and financial stability: scenario-based evidence from below* (title from a search result; DNB PDF returned 403). This is a possible later reverse or scenario test on floods and must be read before the reverse-stress-test claim is finalised. **Resolved 2026-11-02:** see S8_dnb796_notes.md (Caloia, van Ginkel and Jansen, read in full; `caloia2026floods`).
- [UNVERIFIED] IMF FSAP climate technical note for Thailand: none found. Crossref lists FSAP climate notes for Indonesia, Mexico, Canada, Italy, Japan, Iceland, Kazakhstan, the Philippines and the Maldives, but none for Thailand; a web search found only the 2019 Thailand FSAP risk-assessment technical note (IMF CR 19/318; not opened). Absence as of 2026-11-02.
- [UNVERIFIED] IMF WP 2022/163, *Bank Stress Testing of Physical Risks under Climate Change Macro Scenarios* (typhoons, Philippines). Seen in a search result only; the IMF PDF returned 403.
- [UNVERIFIED] Fatica et al. (2024a) on securitised SME loans: PD falls within six months of a flood, then rises at 12–24 months. Known only as reported by Albertazzi et al. (p. 9). High priority, because it is direct evidence of relief-delayed default. **Resolved 2026-11-02:** see S8_fatica_notes.md (it is Barbaglia, Fatica and Rho 2024, `barbaglia2024flooded`, read in full).
- [UNVERIFIED] Bellaver et al. (2025): Italian house prices and repeated flooding, with discounts of up to 4%; and Carroll et al. (2025): Irish AnaCredit flood-risk premia of 7–13 bp. Both known only via Albertazzi et al. (pp. 8–10).
- Shoji (2010), *J. Development Studies* 46(2):191–210, doi 10.1080/00220380902952381; Shoji (2012), *The Developing Economies*, doi 10.1111/j.1746-1049.2012.00161.x; Becchetti & Castriota (2011), *World Development* 39(6):898–912, doi 10.1016/j.worlddev.2009.10.020. Metadata verified via Crossref; abstracts not read. Microfinance repayment after floods or a tsunami in South Asia; relevant to claim (d).
- Van Gerwen, Degryse, Ongena & Scopelliti, *Flooded Collateral*: no open full text found (the GRASFI page shows the abstract behind a login). Depth unchanged (abstract).
- Brei et al. (2024): HAL post-print hal-04538857 blocked by a bot challenge; only the abstract was read.
- Fontana et al. (2025), ECB WP 3036: magnitudes in the body were not recorded; only the abstract is used.
- A search-engine summary attributed to an ECB Macroprudential Bulletin (November 2025) an extra 77 bp of CET1 depletion from acute floods in the 2025 EU-wide stress test. Not opened; not used.

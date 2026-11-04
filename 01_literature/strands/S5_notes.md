# S5 — Emerging markets: the insurance gap, debt relief and forbearance after disasters, and Thailand's 2011 floods

**Working draft, 2026-11-02. For the author to rewrite in their own voice.**

Labels: **[E]** established evidence (read in a verified source, read depth stated); **[H]** the author's hypothesis; **[S]** my speculation or judgement. Citekeys refer to `01_literature/strands/S5.bib`. Read depth: `abstract`, `intro` or `full`. Statements about BOT policy come only from public documents (Royal Gazette, BOT web pages, World Bank report); nothing here draws on the author's work knowledge.

---

## 1. Synthesis

**What is established.** [E] Thailand's 2011 floods were a large, private-sector, manufacturing-centred shock. The World Bank–RTG rapid assessment puts damage and losses at THB 1.43 trillion (USD 46.5 bn), about 70% in manufacturing and about 90% borne by the private sector, and estimates that the floods cut 2011 real GDP growth by 1.1 percentage points (`worldbank2012thai`, Executive Summary, p. 1). The same assessment finds bank balance sheets resilient on impact. The Thai Bankers' Association expected the flood-related rise in the NPL ratio to be about 0.5%, *after* grace periods of up to six months and restructurings that the BOT allowed (p. 60, fn. 47). Insurance was thin outside the industrial estates: insurance premiums were 4.67% of GDP in 2011, and fewer than 1% of private dwellings were estimated to be insured against natural disasters (p. 59). This matches Swiss Re's finding that only 5% of severe flood losses in emerging markets over the preceding decade were insured, against 34% in advanced economies (`swissre2022extreme`). The closest micro-evidence, a Krungsri mortgage-book study, finds a small default spike in 2011Q4 among delinquent borrowers ineligible for relief, then post-flood default *below* model-predicted levels. The authors attribute this to debt relief and the rapid recovery (`chitchumnong2025physical`).

On relief itself, the Indian evidence is the most rigorous. Unconditional debt waivers reduced debt but did not raise investment or productivity. They pushed households towards informal credit (`kanz2016what`), cut and reallocated new bank lending, and worsened later repayment, especially among borrowers previously in good standing, with defaults becoming more sensitive to the electoral cycle (`gine2018economic`). Non-distressed beneficiaries repaid worse afterwards, while genuinely distressed ones repaid better (`mukherjee2018borrowers`). Forbearance is different from forgiveness. In a randomised experiment, a moratorium offered by the lender cut default by 4 percentage points, while the same offer framed as regulator-mandated had no effect (`fiorin2023how`). In the US, COVID forbearance absorbed distress that fundamentals would otherwise have turned into defaults (`cherry2022government`). Regulatory forbearance on classification and provisioning can also hide insolvency and channel credit to zombie firms (`chari2021unholy`; `caballero2008zombie`).

**What is contested.** Whether relief *reduces* or merely *defers and relocates* default. The Indian waiver evidence points to moral hazard and long-run credit-culture costs. The forbearance evidence (`fiorin2023how`; `cherry2022government`) points to liquidity relief without moral hazard, at least in the short run. Who grants the relief, and whether it is anticipated, seem to matter. The World Bank team flagged exactly this risk in Thailand: a three-year grace period at state-owned specialised financial institutions (SFIs) might lead borrowers to move to SFIs "in the hope of getting a suspension on their loan repayments next time there is a disaster" (`worldbank2012thai`, p. 69).

**Why the PD/LGD response may differ from US/EU evidence [S].** US evidence on post-flood default is shaped by the NFIP, mortgage insurance and federal grants. In Thailand the main buffers are instead (i) regulatory classification forbearance: a freeze of the pre-flood classification for debtors who were performing when the flood hit (BOT ว. 1564/2554, `bot2011circular1564`; the World Bank's "one payment instead of three" is not in that circular and is treated as secondary-only), and in 2024 debtors could keep their pre-disaster classification (`bot2024relief`); (ii) mandated moratoria at state-owned banks; and (iii) subsidised liquidity (the THB 300 bn soft-loan decree, `bot2012emergency`). Three implications follow. First, *observed* default after a flood is a policy-censored outcome, so the measured flood elasticity of PD is a lower bound (as `chitchumnong2025physical` argue). Second, losses may surface later and elsewhere: in SFI balance sheets, in informal credit, or in loan performance at the next shock. Third, with little property insurance, collateral damage is not reimbursed, so LGD should respond more than in insured settings. But that response is masked if restructured loans never reach default. Floods may therefore show up first in stage migration and restructuring flags rather than in defaults, which bears directly on IFRS 9 staging.

**Hypotheses for the project [H].** H-S5a: flood-exposed loans show a larger rise in restructuring and stage-2 flags than in 90-day default. H-S5b: post-relief repayment deteriorates among borrowers who were not distressed but were eligible (the Mukherjee et al. pattern), especially at SFIs. H-S5c: without insurance, realised LGD on flood-damaged collateral exceeds that in comparable insured settings. All three need loan-level data (Tier 2). A public-data proxy is listed-bank restructuring disclosures around flood years.

---

## 2. Per-paper entries

### 2a. Thailand 2011 floods: damage, propagation, relief

**`worldbank2012thai`** — World Bank (2012), *Thai Flood 2011: Rapid Assessment for Resilient Recovery and Reconstruction Planning*. Read: **intro** (Executive Summary; Financial and Insurance Sector chapter, pp. 57–70).
- Question: damage, losses and recovery needs by sector after the 2011 floods.
- Data/method: Damage and Loss Assessment (DALA) methodology, with sector teams and RTG agencies. The financial chapter draws on interviews (BOT, Thai Bankers' Association, SFIs, OIC) and is explicitly "indicative and preliminary" (p. 57).
- Findings [E]: THB 1.43 trn (USD 46.5 bn) in damage and losses, 56% of it losses; manufacturing about 70%; private sector about 90%; recovery needs THB 1.5 trn; 2011 real growth reduced by 1.1 pp (p. 1). Bank physical damage minimal: 631 of 6,138 branches closed at some point (p. 60). NPL rise expected around 0.5% after BOT-allowed grace periods and restructuring (p. 60). Commercial banks could offer grace periods "without changing their provisioning status" (p. 66, fn. 60). Government finance-sector measures (Table 21, pp. 67–68) could cost the government THB 234 bn, of which about THB 183 bn would be fronted by SFIs (p. 69). Insurance: premiums 4.67% of GDP; under 1% of dwellings insured against natural disasters; about 95% of claims reinsured abroad; a catastrophe insurance pool recommended (pp. 57–59, 65).

**`haraguchi2013flood`** — Haraguchi & Lall, *Flood Risks and Impacts: Future Research Questions and Implication to Private Investment Decision-Making for Supply Chain Networks*, background paper for GAR 2013 (UNISDR). This is the open precursor of the IJDRR article `haraguchi2015flood`, which I did **not** read (Elsevier blocked; no abstract in Crossref, OpenAlex or Semantic Scholar). Read: **intro** (abstract, table of contents, introduction, Sections 4.1–4.2).
- Question: how floods propagate through supply chains, using Thailand 2011 (automotive and electronics) as the case; what firms should consider in supply-chain design.
- Data/method: a descriptive case study drawing on industry and press data, plus a review of input–output, CGE and network methods.
- Findings [E]: seven industrial parks were inundated, with 804 companies (Table 3, p. 8). As of 1 June 2012, some 17.5% of factories in those parks could not resume operations (pp. 8–9, Table 4). Impacts differed across firms depending on preparedness and response (abstract).
- Relevance: corporate-borrower channel and spillovers to non-flooded firms; a threat to control-group validity.

**`chitchumnong2025physical`** — Chitchumnong, Hatairatana & Khangphukhieo (2025), CRC Edinburgh WP (Krungsri). Read: **full** (short paper).
- Question: the impact of the 2011 flood on a Thai bank's home-mortgage default, and a stress-test framework.
- Data: proprietary mortgage-portfolio data, 2009–2013 (3-month default rate); hydrological runoff at Nakhon Sawan for extreme value analysis.
- Identification: vintage (age–period–cohort) decomposition. Model-predicted default without flood or relief is compared with actual default, and flood-affected with non-affected borrowers. This is descriptive and decomposition-based, not quasi-experimental.
- Findings [E]: a small immediate rise in 2011Q4, attributed to delinquent borrowers ineligible for relief. After the flood, actual default was below predicted, attributed to debt relief, which the authors read as a lower bound. Flood-affected borrowers show higher "could-be" default, read as an upper bound. Most homes had non-structural damage, while submerged cars were total losses. Relief described: bank programmes (skip or partial payments, instalments, rate cuts) from November 2011 to January 2012, typically 1–9 months; the BOT lent THB 210 bn at 0.01% under the decree, banks added THB 90 bn, and loans to borrowers carried 3% for five years (pp. 7–8).

**`noy2021floods`** — Noy, Nguyen & Patel (2021), *EDCC* 69(2). Read: **abstract** (the CESifo open version was blocked).
- Question: direct and spillover effects of the 2011 flood on households.
- Data: repeated waves of the Thai Household Socio-Economic Survey; 2012 self-reported flood exposure plus satellite-based exposure indicators.
- Identification: compares directly flooded households, non-flooded households in flooded communities (spillovers) and others.
- Findings: the abstract states the outcomes studied (income, expenditure, assets, debt, savings) but not the signs or sizes. **No findings claimed.**

### 2b. Debt relief and moral hazard (India)

**`kanz2016what`** — Kanz (2016), *AEJ: Applied* 8(4). Read: **intro** (World Bank PRWP 6258 version, 2012).
- Question: does debt relief relax debt overhang and raise investment?
- Data: household survey of beneficiaries of India's 2008 debt waiver (Rs 715 bn, 1.6% of GDP, about 45 m households).
- Identification: regression discontinuity at the 2-hectare pledged-land eligibility threshold (100% relief below; 25% conditional relief above).
- Findings [E]: debt falls persistently, but investment and productivity do not rise. Full-relief households borrow 6 pp less from formal sources and rely more on informal credit. The author attributes this to expectations about future access to credit.

**`gine2018economic`** — Giné & Kanz (2018), *RFS* 31(5). Read: **intro** (PRWP 7109 version, 2014).
- Question: credit-market and real effects of the same waiver.
- Data: RBI district- and bank-district-level credit data; regional productivity, wage and employment data.
- Identification: cross-district exposure driven by the retrospective land-pledge eligibility rule (historical land distribution), with bank-district fixed effects absorbing local demand.
- Findings [E]: a 1 s.d. rise in exposure reduces the number of loans by 4–6% and credit outstanding by 13–16%. High-exposure districts received 36 cents of new lending per dollar written off, against 4 dollars in low-exposure districts. Loan performance declined in high-exposure districts, concentrated among borrowers previously in good standing. There was a precise zero effect on productivity, wages and consumption. Defaults became more sensitive to the electoral cycle.
- Note: the introduction mentions a "US$ 2.9 billion bailout for farmers in Thailand" (sourced to USDA ERS); I have not verified this at the primary source.

**`mukherjee2018borrowers`** — Mukherjee, Subramanian & Tantri (2018), *J. Law & Economics* 61(4). Read: **abstract** (ISB open copy unreachable).
- Data: borrower-level loan data. Identification: RD around the waiver's cutoff dates; pre-waiver distress identified from exogenous borrower-level shocks.
- Finding [E]: post-waiver loan performance worsens for non-distressed beneficiaries and improves for distressed ones.

### 2c. Forbearance, moratoria and zombie lending

**`fiorin2023how`** — Fiorin, Hall & Kanz (2023), World Bank PRWP 10358. Read: **intro**.
- Question: how do delinquent borrowers respond to a debt moratorium, and does it matter who grants it?
- Data/identification: a nationwide RCT with a large Indian consumer lender (DMI Finance) during India's COVID moratorium. Offers are framed as voluntary by the lender or as required by regulation, against placebo and control arms, with a follow-up product-adoption experiment.
- Findings [E]: a lender-framed moratorium cuts default by 4 pp (7%); a regulator-framed one has no effect. Demand for the lender's non-credit product is 10 pp (27%) higher after a lender-framed offer. The authors read this as relational contracting rather than moral hazard. The intro notes that over 80 countries enacted COVID moratoria.

**`cherry2022government`** — Cherry, Jiang, Matvos, Piskorski & Seru (2022), *BPEA* 2021(2). Read: **abstract**.
- US credit-bureau evidence: over 70 m consumers (USD 2.3 trn of loans) entered forbearance from March 2020 to May 2021. Forbearance helps explain why defaults stayed low relative to fundamentals. An RD on CARES Act mortgage eligibility shows that government subsidies raise forbearance by about a third. Shadow banks were less likely to grant forbearance.

**`chari2021unholy`** — Chari, Jain & Kulkarni (2021), NBER WP 28435. Read: **abstract** (NBER page).
- RBI provisioning forbearance after the global financial crisis, studied with matched bank–firm data. Stressed banks used it to conceal loans to insolvent firms. In industries and portfolios with many failing firms, credit moved from healthy firms to the weakest.

**`caballero2008zombie`** — Caballero, Hoshi & Kashyap (2008), *AER* 98(5). Read: **abstract**.
- Japanese banks' sham restructurings kept credit flowing to insolvent "zombie" firms. Zombie-dominated industries show depressed job creation and destruction and lower productivity, and zombies depressed the investment and employment growth of non-zombies.

**`hosono2016natural`** — Hosono, Miyakawa, Uchino, Hazama, Ono, Uchida et al. (2016), *IER* 57(4):1335–1370. The first six authors are verified via Crossref; any further authors are not yet checked. Read: **abstract**.
- The 1995 Kobe earthquake as a loan-supply shock. Firms outside the quake area whose main bank was inside it invested significantly less. This is the bank-damage channel, not forbearance. I found no verified Japanese post-disaster *forbearance* paper in this pass.

### 2d. Insurance protection gap and Thai institutional response

**`swissre2022extreme`** — Swiss Re Institute (2022), news release on sigma 1/2022. Read: **full** (2 pp.).
- In 2021, flood economic losses were USD 82 bn and insured flood losses slightly over USD 20 bn. Over the past decade, 5% of severe flood losses were insured in emerging markets and 34% in advanced economies. Asia has the largest flood protection gap, with 7% of economic losses insured.

**`bot2012catastrophe`** — BOT article, "กองทุนประกันภัยพิบัติ: มาตรการฟื้นความเชื่อมั่น" (*The disaster insurance fund: a measure to restore confidence*), by นายนิธิสาร พงศ์ปิยะไพบูลย์. Read: **full** (web article, read via a fetch tool). The page shows no explicit date, only the identifier "Article_17Apr2012".
- Facts [E]: the fund was established by an emergency decree of 26 January 2012 and financed by a THB 50 bn loan. Cover is capped at THB 100,000 for homes, with a 30% sub-limit of asset value for SMEs and industry. Premiums are 0.50% (homes), 1.00% (SMEs) and 1.25% (industry). Sales began on 28 March 2012. Claims from the 2011 flood are put at THB 480 bn ("4.8 แสนล้านบาท").

**`bot2012emergency`** and **`bot2024relief`**: see Section 3.

---

**Pan, Billio, Dufour & Varotto (2025), EGU25-20228 (conference abstract; added in the final sweep, 2026-11-02).** *Read: abstract (OpenAlex; Copernicus meeting page for metadata).* Q: how do residential mortgage defaults respond to floods across European countries? Data: more than 13 million mortgages. Findings [E]: higher post-flood default risk in France, Ireland and the UK; lower defaults in Spain and Italy, "suggesting that timely relief measures may dampen borrower distress"; neutral aggregates in Belgium, the Netherlands and Portugal, with high-LTV borrowers more vulnerable; moderate floods riskier than extreme ones; EU Solidarity Fund interventions indirectly support high-LTV borrowers. [S] Closest new work to RQ2: it reads lower defaults under relief as dampening, whereas H2b asks whether relief *defers* loss until it ends; it uses cross-country variation, not relief rules. Not peer reviewed; not cited in the proposal (word budget), but worth knowing.

## 3. Verified relief measures for borrowers: 2011 floods (and the current template)

Primary sources: the Royal Gazette and BOT pages. The World Bank–RTG assessment is an official joint report, but for BOT measures it is secondary. Rows that rest only on it are marked (WB).

| Date | Measure | Detail | Source |
|---|---|---|---|
| Late 2011 (in force by the time of the assessment) | BOT restructuring rule for flood debtors (WB) | All banks may restructure loans to viable flood-hit borrowers; these can leave the NPL list after **one** payment under the new schedule instead of three. | `worldbank2012thai`, Table 21, p. 68 |
| Late 2011 (WB) | Grace periods without reclassification (WB) | Commercial banks may grant flood victims grace periods at their discretion "without changing their provisioning status"; the Thai Bankers' Association recommends no more than 12 months. | `worldbank2012thai`, p. 66, fn. 60 |
| Late 2011 (WB) | LTV tightening postponed (WB) | The BOT postponed a planned cut in the maximum LTV for mortgages. | `worldbank2012thai`, Table 21, p. 68 |
| Late 2011 to June 2012 (WB) | Credit-card minimum payment waived (WB) | The usual 10% minimum payment was temporarily waived until June 2012. | `worldbank2012thai`, Table 21, p. 68 |
| Cabinet-approved, late 2011 (WB) | 3-year moratorium at SFIs and cooperatives (WB) | A 3-year grace period on principal and interest for flood-hit borrowers with total debt under THB 500,000 at BAAC, GSB, GHB, SME Bank, Islamic Bank and SMC; the same for cooperative farm loans. | `worldbank2012thai`, Table 21, p. 67 |
| Cabinet-approved, late 2011 (WB) | Credit guarantees and soft SME loans (WB) | TCG guarantees up to THB 100 bn of new SME loans (3% cap for 3 years); GSB lends THB 20 bn at 0.01% to banks, matched 50:50, with a 3% cap. | `worldbank2012thai`, Table 21, p. 68 |
| 26 Jan 2012 (Royal Gazette vol. 129, part 10 ก, pp. 11–14; in force the next day) | พระราชกำหนดการให้ความช่วยเหลือทางการเงินแก่ผู้ที่ได้รับความเสียหายจากอุทกภัย พ.ศ. 2555 (*Emergency Decree on Financial Assistance to Persons Damaged by Floods, B.E. 2555*) | A facility capped at THB 300 bn. The BOT lends to financial institutions at **0.01%** a year. The BOT share is at most 70% of each loan, with the institution funding the rest. On-lending to flood-zone individuals and SMEs is capped at **3%** a year. Institutions must apply by 31 Dec 2013 and repay within 5 years, by 31 Dec 2018 at the latest. | `bot2012emergency` (PDF read in full) |
| 26 Jan 2012 (decree); sales from 28 Mar 2012 | Disaster insurance fund (กองทุนส่งเสริมการประกันภัยพิบัติ) | THB 50 bn; cover and premium terms as in Section 2d. | `bot2012catastrophe`. The decree text itself was **not** opened. |
| Nov 2011 – Jan 2012 (bank-reported) | Bank relief programmes at one bank (Krungsri) | Skip or partial payments, instalments and rate cuts, typically 1–9 months; BOT soft-loan drawdown of THB 210 bn. | `chitchumnong2025physical`, pp. 7–8 (secondary for the BOT figure) |
| 30 Aug 2024 (BOT news 35/2567) | Standing disaster-relief template | Lower credit-card minimum payments, emergency personal-loan limits, and restructuring or fee waivers for up to 12 months from the date a disaster zone is declared. Debtors may **keep their pre-disaster classification**. | `bot2024relief` |

**Not verified:** the original BOT circular(s) of late 2011 on flood-debtor classification and restructuring. Neither a web search nor the BOT site turned them up, so those rows rest on the World Bank report. The exact dates of the Cabinet resolutions are also unverified.

---

## 4. Gap this strand reveals [S]

No study I found separates the *flood* effect on default and loss from the *relief* effect using loan-level data with exogenous variation in relief eligibility in an emerging market. Chitchumnong et al. decompose descriptively within one bank. The Indian RD designs (Kanz; Mukherjee et al.) study relief that is not tied to disasters. Thailand's 2011 package had sharp eligibility rules: a THB 500,000 total-debt threshold at SFIs, flood-zone declarations and lender type (SFI versus commercial bank). These rules offer candidate discontinuities, if loan-level data can be accessed.

---

## 5. Unverified / not read

- `haraguchi2015flood` (IJDRR 14:256–272): metadata verified via Crossref and OpenAlex; **not read** (publisher 403; no abstract available). Findings above come only from the 2013 GAR precursor.
- `poapongsakorn2014impact` (Poapongsakorn, Meethom & Pantakua, in *Resilience and Recovery in Asian Disasters*, Springer, pp. 75–104): metadata verified via Crossref; **not read**.
- Noy, Nguyen & Patel (2021): read at abstract depth only; no results claimed.
- Mukherjee, Subramanian & Tantri (2018): open ISB copy unreachable (connection refused); abstract only.
- [UNVERIFIED] The 2011 BOT circulars on flood-debtor restructuring and classification.
- [UNVERIFIED] The text of the พระราชกำหนดกองทุนส่งเสริมการประกันภัยพิบัติ พ.ศ. 2555 (Disaster Insurance Fund decree) in the Royal Gazette.
- [UNVERIFIED] Swiss Re 2025–26 figures (an 80–90% uninsured share in emerging economies; Asian 2025 insured share). These appeared only in a search-engine summary, and the Swiss Re pages returned 403.
- [UNVERIFIED] Thai farm-debt bailout of US$2.9 bn, cited in Kanz (2012) and Giné & Kanz (2014) from USDA ERS.
- Not found in this pass: a peer-reviewed study of post-disaster forbearance in Japan (e.g. after 2011 Tohoku), the Philippines or Latin America; Geneva Association and IMF protection-gap reports; PIER work on Thai flood or relief credit outcomes beyond Luangaram et al. (2024, in `S0_scoping.bib`). These are the first targets for a follow-up search.
- Hosono et al. (2016): my lookup script printed only the first six authors (Crossref). Check the full author list at the publisher before merging.

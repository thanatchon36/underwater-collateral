<!-- Working draft. Length: see the body count printed by 06_proposal/render_references.py. -->

# Underwater Collateral: Flood Risk in Official Land Values, Credit under Relief and Bank Capital — Evidence from Thailand

*Research proposal. Working draft.*

---

## Abstract

This thesis traces how flood risk reaches bank capital in Thailand, where few homes were insured in 2011 and debt relief was the main buffer. It asks how official land values adjust after the 2024 floods, whether relief defers flood-induced credit losses, and what flood severity would breach capital requirements. A pilot on 41,049 cadastral map sheets shows that a cross-section cannot separate flood hazard from land use, so the design compares rounds of values on 198 radar-flooded sheets.

---

## 1. Context and importance

Supervisors, including the Bank of Thailand, expect banks to manage climate-related financial risks (Basel Committee on Banking Supervision 2022; Bank of Thailand 2023), tracing hazards through damaged collateral to loss given default (LGD) (Caloia and Jansen 2021; European Central Bank 2022). Evidence comes mostly from insured markets: after Hurricane Katrina, insurance proceeds repaid mortgages (Gallagher and Hartley 2017).

In Thailand, fewer than 1% of dwellings were insured against natural disasters (World Bank 2012, p. 59) when the 2011 floods caused damage and losses of about THB 1.43 trillion (World Bank 2012, Executive Summary, p. 1). The buffer was regulatory: lenders could keep debtors' pre-flood classification (Bank of Thailand 2011), as again after the 2024 and 2025 floods (Bank of Thailand 2024; Bank of Thailand 2025). One Thai bank's mortgage defaults responded modestly to the 2011 flood, which the authors link to relief and rapid recovery (Chitchumnong et al. 2025). Whether low post-flood default reflects resilience or deferral matters wherever insurance is thin; Thailand makes it observable, as relief follows documented rules and official values are reset nationwide every four years (Kingdom of Thailand 2019, s. 19).

## 2. Research aim and questions

**Aim.** To trace how flood risk passes from land valuation to bank capital where relief, not insurance, is the first buffer, stating where a link is assumed rather than measured (Figure 1).

**RQ1. Do official land values capitalise flood risk, and how do they adjust after a flood?** Provincial committees set official values (ราคาประเมินทุนทรัพย์) by market comparison (Ministry of Finance (Thailand) 2020) as the base for transfer fees and taxes (Department of Lands (Thailand) 2026); bank appraisals are not tied to them (Bank of Thailand 2019). RQ1 also asks whether carry-over (values unchanged between rounds) slows the response. The Treasury found no post-2011 fall in flooded areas and left its schedule unrevised (MGR Online 2012).

**RQ2. Does relief defer or prevent the credit losses that floods cause,** and how does flood exposure move the probability of default (PD) and LGD?

**RQ3. What flood severity would breach banks' capital requirements,** and how much capital does relief hide?

![Figure 1](../04_analysis/outputs/figures/fig_chain.png)

**Figure 1. From flood hazard to bank capital.** λ_B is the share of the hazard discount that bank appraisals recognise. *Source:* author.

## 3. Literature, contribution and hypotheses

Flood risk is capitalised into prices, by about 4.6% for inland 100-year floodplains (Beltrán et al. 2018, abstract). Closest to RQ1, Melbourne statutory valuations discount designated flood zones (Fuerst and Warren-Myers 2021); New York assessments fell after Hurricane Sandy for inundated homes but not for undamaged high-risk homes whose prices fell (Guo et al. 2026); English lender valuations did not follow prices down (Garbarino and Guin 2021); in Hat Yai, flood risk lowers rents and official valuations in a cross-section (Chongwilaikasaem and Chalermyanont 2023); and Semarang's official zone values gained fewest rupiah near tidal flooding (Utami et al. 2021).

On credit, euro-area floods raise corporate default by about 0.7 percentage points (Albertazzi et al. 2026, Section 1) and the 2024 Valencia floods raised stage 2 classification by about half a point (Pérez Montes et al. 2025, pp. 19–21), without measuring collateral values or LGD. European small-business default hazards dip for six months after a flood, then rise, tentatively attributed, without relief data, to aid and payment suspensions (Barbaglia et al. 2024, Table 7). Moratoria change borrowers' behaviour (Dinerstein et al. 2024; Kim et al. 2024), uninsured damage raises delinquency (Kousky et al. 2020), and weak banks may hide losses (Caballero et al. 2008; Blattner et al. 2023). Flood stress tests estimate capital depletion under fixed scenarios (Caloia and Jansen 2021; Caloia et al. 2026), the disaster that would fail a small bank (Blickle et al. 2025) or the probability of the 2011 scenario for one Thai bank (Chitchumnong et al. 2025); none treats relief as a dimension of the breaking point.

**Contribution.** (i) To my knowledge, the first controlled estimate of how an emerging market's official valuations respond to a flood, set by committees on a fixed cycle without an insurance signal. (ii) Evidence on when flood losses are recorded under relief. (iii) A breaking point that separates reported from economic capital under relief, adapting Grundke and Pliszka (2018).

**Framework.** Let λ_T and λ_B be the shares of a fully informed hazard discount that official values and bank appraisals recognise. The full discount is the 4.6% above, from richer markets, halved and doubled, as I found no Thai estimate. RQ1 bears on λ_T; RQ3 varies λ_B from 0 to 1 unless loan appraisals reveal it, with the Bank of Thailand's appraisal-based regional index as a coarse check (Samritpiam and Chongprasoplarp 2026, pp. 3, 7–9).

**Hypotheses** (mine, not established results).
- **H1a.** At the first round after the 2024 floods, values on flooded land fall relative to comparable unflooded land, less where ex-ante hazard was high.
- **H1b** (descriptive). Carry-over is more frequent on flooded land.
- **H2a.** Flood exposure raises PD and LGD more where origination appraisals, relative to the official value then in force, do not fall with mapped hazard.
- **H2b.** Under the 2024–25 relief, flood-induced delinquency is recorded mainly after relief ends.
- **H2c** (2011, if records survive). Relief defers rather than avoids loss: eligible borrowers' delinquency rises when relief ends, and five-year discounted loss matches comparable ineligible flooded borrowers' within 5 percentage points of exposure (a loose margin).

## 4. Methods

### 4.1 RQ1: official values and flood risk

**Data.** The Treasury Department publishes only the 2023–26 round; my snapshot locates 95.8% of 37.8 million parcels on cadastral map sheets (2 km square rural, 500 m urban). Flood maps are the Global Flood Database for 2011 (Tellman et al. 2021), my nationwide Sentinel-1 radar maps for 2024–25 and UNOSAT's 2024 extents for Chiang Rai and Phayao; elevation is from Copernicus (European Space Agency and Airbus 2022), permanent water from Pekel et al. (2016), land cover from Zanaga et al. (2022).

**Outcome.** Parcels are grouped by sheet and 2023–26 value, then followed by parcel number. The primary outcome is the change in log value per square wah between rounds, sheets weighted equally; secondary outcomes are carry-over and, bounded for selection (Lee 2009), the change where values moved.

**Design.** As cross-sections confound hazard with land use (Section 5), identification comes from changes across rounds. A sheet is flooded if radar shows new water, absent from every 2023 image of the season, on over 25% of it in 2024. Controls are under 1% flooded in every 2024–25 map, at least 5 km away and no higher above the valley floor than nine in ten flooded sheets. Changes are regressed on flooding, province effects (absorbing each committee's general revaluation), elevation, distance to permanent water and 2021 land cover; flooding tests H1a, and a flood × height interaction (secondary) its hazard gradient. An OSF pre-analysis plan fixes sensitivities before the 2027–30 round appears.

**Samples.** Four provinces have at least 25 flooded sheets: 198 in Chiang Rai, Phayao, Nong Khai and Nakhon Phanom, in 21 clusters of 1:50,000 sheets, with 1,891 controls. Sentinel-2 shows new water on 57–88% of radar-flooded sheets by province, 1% of controls. In Chiang Rai and Phayao, 79% are flooded in UNOSAT's map, but radar finds only 7% of the 1,214 sheets UNOSAT shows over 25% flooded, missing flash floods and water among buildings. Radar measures prolonged inundation and the co-primary UNOSAT sample (18 treated clusters, 579 controls) any flooding; the two tests are Holm-adjusted. Radar-flooded sheets started cheaper and less built-up (standardised differences −0.41 and −0.68), so both samples' controls are reweighted within province on value, height, built-up and cropland shares and map scale (effective 98 and 104).

**Inference and power.** Inference uses 1,000 placebo footprints shifted within province onto equally low-lying dry sheets, with the wild cluster bootstrap (Cameron et al. 2008) as a check, and as the UNOSAT test (too few controls). Assuming sheet-level changes with standard deviation 0.10 log points and within-cluster correlation 0.2, the weighted radar sample detects a fall of 0.053 with 80% power and the UNOSAT sample 0.061. That is about the full hazard discount and half the fall in inundated New York assessments (Guo et al. 2026, Table 3), so a null cannot separate partial from no recognition.

**Interpretation.** Falls graded by flood duration point to damage, uniform cuts to administrative relief, and falls reaching briefly flooded land or persisting into the next round to recognised risk; in Chiang Rai and Phayao, the two maps separate duration from province.

### 4.2 RQ2: credit risk under relief

**Data.** With pseudonymised data on a bank's land-secured loans, flood exposure is computed at the collateral's map sheet inside the bank's secure environment. Outcomes are 90-day delinquency, restructuring and IFRS 9 stages (Bank of Thailand 2018), with haircuts, revaluations and provisions as early LGD proxies.

**Designs.**
- **2024–25 (primary).** Relief followed disaster-zone declarations or alert levels (Bank of Thailand 2024) and, in 2025, covered retail and SME debtors in Level-4 areas, such as Songkhla, not non-performing on 2 December 2025 (Bank of Thailand 2025, pp. 1–2). Borrowers on flooded and comparable unflooded sheets are compared month by month from a year before the floods to a year after relief ends, with the two floods as cohorts (Callaway and Sant'Anna 2021). The share of the flood-induced gap that opens only after relief ends is RQ3's deferral share. Relief's own effect comes from its rules: Level-4 areas against lighter relief in neighbouring provinces, and borrowers either side of the cut-off. At base delinquency of 3–5% (assumption), 1,100–2,300 flooded borrowers detect a rise of 2 percentage points, with clustering; a euro-area-sized 0.7 points needs 8,700–19,000.
- **2011 (extension).** Relief covered debtors at most three months overdue (Bank of Thailand 2011, Q&A 2). A fuzzy discontinuity in discrete months overdue (Kolesár and Rothe 2018), differenced between declared and undeclared flooded areas, netting out the boundary (pre-flood years test this), identifies relief for borrowers in arrears. H2c needs up to 30,000 borrowers on each side in each area: pooled lenders or bureau data.

**Access and Plan B.** Routes are a bank–University agreement, the National Credit Bureau and an external-researcher programme; I judge the chance of loan data well below one half. Otherwise Chapter 3 repeats Chapter 2's design on the 2025 floods: 437 sheets in nine provinces flooded in 2025 but not 2024, with 7,664 controls and a detectable fall of 0.03.

### 4.3 RQ3: reverse stress test

Scenarios use return-period maps up to 1,000 years (Ward et al. 2020; Dottori et al. 2016), fully dependent or independent across basins, with Asian depth–damage functions that include Thai data (Huizinga et al. 2017, p. 13). PD responses come from published Thai estimates (Chitchumnong et al. 2025), observed under relief and so a lower bound, and, with access, RQ2. Recovery is the appraisal less damage, less the unrecognised share 1 − λ_B of the hazard discount, less a sale haircut. Over two years, reported capital follows staging as relief delays it; economic capital recognises deferred losses at once. S* is the most probable scenario that pushes the common equity tier 1 ratio below the minimum plus buffers (Grundke and Pliszka 2018): 7% of risk-weighted assets, 8% for domestic systemically important banks (Bank of Thailand 2012, cl. 5.3.1; Bank of Thailand 2017, cl. 4.3.2). The headline is the gap between S* on reported and economic capital as the deferral share varies. λ_B matters less: in a stylised book, moving it from 0 to 1 shifts S* by 3–19% at loan-to-value ratios of 0.8–1.0. RQ1 gives λ_B one scenario; RQ2, with access, the deferral share. Scenarios rarer than 1 in 1,000 years are implausible, as at Basel's 99.9% confidence level (Basel Committee on Banking Supervision 2005, p. 11). Deferral is material if, for any λ_B, economic capital breaks at a return period one step shorter (1,000, 500, 200 years) than reported capital. Credit follows the Bank of Thailand's December 2025 provincial shares by booking office, which overstate Bangkok's. Results cover the system and stylised banks, never a named bank.

## 5. Data and feasibility

**In hand.** Official values, flood maps, terrain, land cover and provincial credit, in a reproducible pipeline; loan-level code tested on synthetic data.

**Pilot (exploratory).** In 17 Chao Phraya basin provinces, comparing same-scale sheets within each 1:50,000 sheet, values on 80–100% flooded sheets are 0.65 log points lower on urban sheets (standard error 0.10) and 0.27 lower on rural sheets (0.07) than on sheets under 1% flooded (Figure 2). Those urban sheets are less built-up (14% against 36%); with land-cover controls, the urban gap shrinks to 0.08 (0.06) and flooded rural bins lie above the reference. Land cover may itself respond to hazard, so neither is a hazard discount.

![Figure 2](../04_analysis/outputs/figures/fig_appraisal_flood_binned.png)

**Figure 2. Official land values and the 2011 flood, 17 Chao Phraya basin provinces.** Sheet mean log value by share flooded in 2011, relative to under 1%, without (filled) and with (hollow) land-cover controls; bars ±2 clustered standard errors. *Sources:* Treasury Department; Global Flood Database (Tellman et al. 2021); ESA WorldCover (Zanaga et al. 2022); author's calculations.

**Research governance.** Only public data and data under University agreements are used. Approaches to banks come from the University. Personal data fall under Thailand's Personal Data Protection Act, UK GDPR and University ethics review. pre-analysis plans are public; [named adviser], outside the supervisory team, reviews RQ2's interpretation; no bank-identifiable results are published.

**Preparation.** [Author to state prior quantitative training and which parts of the pilot they built.]

## 6. Expected results and policy relevance

If official values adjust slowly, owners of damaged land are taxed on pre-flood values. If relief defers loss, stress tests calibrated on observed post-flood default overstate resilience. A large gap between reported and economic S* would argue for flood scenarios on economic capital. Nulls are reported with equal weight.

## 7. Draft thesis outline and timeline

1. *Introduction and framework.*
2. *Underwater valuations* (RQ1).
3. *Deferred, not avoided?* (RQ2), or without access, *A second flood* (2025).
4. *Breaking point* (RQ3).
5. *Conclusion and policy implications.*

| Period | Work |
|---|---|
| Before Year 1 | Radar rule checked against Sentinel-2 imagery in all four provinces (done 2 November 2026; no province fell below the pre-set one-half precision); pre-analysis plans for the 2024 and 2025 designs then registered on OSF Registries on [date], with the analysis code, already tested on a simulated round. The 2027–30 round must be published at least 30 days before it takes effect (Kingdom of Thailand 2019, s. 19), so by 2 December 2026 for a 1 January 2027 start; Treasury offices were briefed in October 2026 on extending current schedules, and a provincial committee considered an extension on 2 November, which could delay the round by up to a year (Kingdom of Thailand 2019, s. 19; กรมธนารักษ์ (Treasury Department) 2026a; กรมธนารักษ์ (Treasury Department) 2026b). A plan registered later makes that analysis exploratory. Survey periods (Ministry of Finance (Thailand) 2020) confirmed with the provincial offices concerned (four for 2024, nine for 2025); earlier rounds requested to calibrate power. |
| Timing cases (fixed in the pre-analysis plan) | (a) Round on time, surveyed after the floods: it is the primary test, and the next round (by December 2030) tests persistence. (b) Surveyed before the floods: it is a placebo, the next round is the primary test, and persistence is not testable within the programme, so recognised risk rests on briefly flooded land. (c) One-year extension: the first post-flood schedule is published by early December 2027, and (a) or (b) applies with every later date a year on; under (b) and (c) together the primary test falls in Year 4, and the 2025-flood chapter carries Chapter 2 meanwhile. In every case Chapter 2 adds carry-over and the 2025 floods to the first comparison. |
| Year 1 | Training in spatial econometrics. Remaining pre-analysis plans and hazard inputs. Access approaches and ethics review; go/no-go by year end. Under (a) or (c), Chapter 2's first comparison. |
| Year 2 | Chapter 2: round-to-round design, carry-over and the 2025 floods; working paper. Chapter 4 calibrated on public data and published estimates. With access, the 2024–25 design begins; the 2011 design if records survive. |
| Year 3 | With access: the rest of Chapter 3 and the Chapter 4 update. Without: the 2025-flood chapter; Chapter 4 finalised as illustrative. Working papers and conferences. Under (a), the persistence test; under (b), Chapter 2's primary test on the next round. |
| Year 4 (if needed) | Revisions, integration and submission. |

## References

Albertazzi, Ugo; Djekic, Davor; Ponte Marques, Aurea (2026). Physical climate risk, credit risk and lending activity. *European Central Bank*, Working Paper Series 3224. doi:10.2866/4699723.

Bank of Thailand (2011). หนังสือเวียน ที่ ธปท. ฝนส. (23) ว. 1564/2554 เรื่อง การซักซ้อมความเข้าใจมาตรการการให้ความช่วยเหลือลูกหนี้ที่ได้รับผลกระทบจากอุทกภัย [Circular 1564/2554: clarification of measures to assist flood-affected debtors], with Q&A attachments. *BOT circular, 19 October 2011; Q&A item 8 revised 20 January 2012*. <https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2554/ThaiPDF/25540206.pdf>.

Bank of Thailand (2012). ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 12/2555 เรื่อง หลักเกณฑ์การกำกับดูแลเงินกองทุนสำหรับธนาคารพาณิชย์ [Notification No. FPG. 12/2555: Regulations on Supervision of Capital for Commercial Banks]. *BOT notification, announced 8 November 2012, in force 1 January 2013*. <https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2555/ThaiPDF/25550332.pdf>.

Bank of Thailand (2017). ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 16/2560 เรื่อง แนวทางการระบุและการกำกับดูแลธนาคารพาณิชย์ที่มีนัยต่อความเสี่ยงเชิงระบบในประเทศ [Notification No. 16/2560: Guidelines on the identification and supervision of domestic systemically important banks]. *BOT notification, announced 31 August 2017*. <https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2560/ThaiPDF/25600245.pdf>.

Bank of Thailand (2018). หนังสือเวียน ธปท.ฝนส.(01)ว.195/2561 นำส่งประกาศ สนส. 20–23/2561 [Circular transmitting the asset classification and provisioning notifications aligned with TFRS 9]. *Bank of Thailand circular, 13 December 2018*. <https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2561/ThaiPDF/25610275.pdf>.

Bank of Thailand (2019). แนวนโยบาย เรื่อง การประเมินราคาหลักประกันและอสังหาริมทรัพย์รอการขาย [Policy guideline on the appraisal of collateral and foreclosed real estate], circular ฝนส.(23)ว.575/2562. *BOT circular, 8 May 2019*. <https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2562/ThaiPDF/25620100.pdf>.

Bank of Thailand (2023). ธปท. และ สมาคมธนาคารไทยร่วมเผยแพร่คู่มือการดำเนินธุรกิจสถาบันการเงิน คำนึงถึงสิ่งแวดล้อมและการเปลี่ยนแปลงสภาพภูมิอากาศ [BOT and the Thai Bankers' Association publish the Industry Handbook on financial institution business with regard to environment and climate change]. *Bank of Thailand web page, 14 December 2023; links the Standard Practice policy guideline listed as 15 Feb 2023 and the Thailand Taxonomy listed as 30 Jun 2023*. <https://www.bot.or.th/th/financial-innovation/sustainable-finance/green/Standard_Practice-Industry_Handbook.html>.

Bank of Thailand (2024). หนังสือเวียน ธปท.ฝนส.(01)ว.601/2567 ขอความร่วมมือให้ความช่วยเหลือลูกหนี้ที่ได้รับผลกระทบจากสาธารณภัย [Request for cooperation in assisting debtors affected by disasters]. *Bank of Thailand circular, 30 August 2024*. <https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2567/ThaiPDF/25670146.pdf>.

Bank of Thailand (2025). หนังสือเวียน ธปท. ว.8158/2568 ขอความร่วมมือให้ความช่วยเหลือลูกหนี้ที่ได้รับผลกระทบจากสาธารณภัยในเขตพื้นที่เกิดสาธารณภัยร้ายแรงอย่างยิ่ง (ระดับ 4) [Request to assist debtors affected by disasters in Level-4 extremely severe disaster zones]. *Bank of Thailand circular, 15 December 2025*. <https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2568/ThaiPDF/25680253.pdf>.

Barbaglia, Luca; Fatica, Serena; Rho, Caterina (2024). Flooded credit markets: physical climate risk and small business lending. *Money and Finance Research Group (Mo.Fi.R.), Univ. Politecnica Marche*, Mo.Fi.R. Working Papers 186. <https://ideas.repec.org/p/anc/wmofir/186.html>.

Basel Committee on Banking Supervision (2005). An Explanatory Note on the Basel II IRB Risk Weight Functions. *Bank for International Settlements*. <https://www.bis.org/publications/explanatory-note-basel-ii-irb-risk-weight-functions>.

Basel Committee on Banking Supervision (2022). Principles for the effective management and supervision of climate-related financial risks. *Bank for International Settlements*. <https://www.bis.org/bcbs/publ/d532.htm>.

Beltrán, Allan; Maddison, David; Elliott, Robert J. R. (2018). Is Flood Risk Capitalised Into Property Values? *Ecological Economics*, 146, 668–685. doi:10.1016/j.ecolecon.2017.12.015.

Blattner, Laura; Farinha, Luisa; Rebelo, Francisca (2023). When Losses Turn into Loans: The Cost of Weak Banks. *American Economic Review*, 113(6), 1600–1641. doi:10.1257/aer.20190149.

Blickle, Kristian S.; Hamerling, Sarah N.; Morgan, Donald P. (2025). How Bad Are Weather Disasters for Banks? *Federal Reserve Bank of New York*, Staff Report 990. <https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr990.pdf>.

Caballero, Ricardo J.; Hoshi, Takeo; Kashyap, Anil K. (2008). Zombie Lending and Depressed Restructuring in Japan. *American Economic Review*, 98(5), 1943–1977. doi:10.1257/aer.98.5.1943.

Callaway, Brantly; Sant'Anna, Pedro H. C. (2021). Difference-in-Differences with Multiple Time Periods. *Journal of Econometrics*, 225(2), 200–230. doi:10.1016/j.jeconom.2020.12.001.

Caloia, Francesco; Jansen, David-Jan (2021). Flood risk and financial stability: Evidence from a stress test for the Netherlands. *De Nederlandsche Bank*, DNB Working Paper 730. <https://www.dnb.nl/media/st5psfvb/working_paper_no-_730.pdf>.

Caloia, Francesco G.; van Ginkel, Kees C. H.; Jansen, David-Jan (2026). Floods and financial stability: Scenario-based evidence from below sea level. *Journal of Financial Stability*, 84, 101545. doi:10.1016/j.jfs.2026.101545.

Cameron, A. Colin; Gelbach, Jonah B.; Miller, Douglas L. (2008). Bootstrap-Based Improvements for Inference with Clustered Errors. *Review of Economics and Statistics*, 90(3), 414–427. doi:10.1162/rest.90.3.414.

Chitchumnong, Piyayut; Hatairatana, Adisorn; Khangphukhieo, Wichit (2025). Physical Climate Risk Stress Test: An Evidence-based Approach. *Credit Research Centre, University of Edinburgh Business School*. <https://crc.business-school.ed.ac.uk/sites/crc/files/2025-11/Physical-Climate-Risk-Stress-Test_-An-Evidence-based-Approach-paper.pdf.pdf>.

Chongwilaikasaem, Sukampon; Chalermyanont, Tanit (2023). Flood hazards and housing prices: a spatial regression analysis for Hat Yai, Songkhla, Thailand. *International Journal of Housing Markets and Analysis*, 16(6), 1052–1070. doi:10.1108/IJHMA-04-2022-0053.

Department of Lands (Thailand) (2026). ค่าธรรมเนียม ภาษี และอากร [Fees, taxes and duties], public service manual. *Department of Lands website, accessed 2 November 2026*. <https://www.dol.go.th/dol-services/public-service-manual/land-registration/fees-taxes-duties/>.

Dinerstein, Michael; Yannelis, Constantine; Chen, Ching-Tse (2024). Debt Moratoria: Evidence from Student Loan Forbearance. *American Economic Review: Insights*, 6(2), 196–213. doi:10.1257/aeri.20230032.

Dottori, Francesco; Salamon, Peter; Bianchi, Alessandra; Alfieri, Lorenzo; Hirpa, Feyera Aga; Feyen, Luc (2016). Development and evaluation of a framework for global flood hazard mapping. *Advances in Water Resources*, 94, 87–102. doi:10.1016/j.advwatres.2016.05.002.

European Central Bank (2022). 2022 climate risk stress test. *European Central Bank, Banking Supervision*. doi:10.2866/97350.

European Space Agency and Airbus (2022). Copernicus DEM. *European Space Agency, dataset (GLO-30 Public, 2021 release; Cloud Optimized GeoTIFFs in the AWS Open Data bucket copernicus-dem-30m)*. doi:10.5270/ESA-c5d3d65.

Fuerst, Franz; Warren-Myers, Georgia (2021). Pricing Climate Risk: Are Flooding and Sea Level Rise Risk Capitalised in Australian Residential Property? *Climate Risk Management*, 34, 100361. doi:10.1016/j.crm.2021.100361.

Gallagher, Justin; Hartley, Daniel (2017). Household Finance after a Natural Disaster: The Case of Hurricane Katrina. *American Economic Journal: Economic Policy*, 9(3), 199–228. doi:10.1257/pol.20140273.

Garbarino, Nicola; Guin, Benjamin (2021). High water, no marks? Biased lending after extreme weather. *Journal of Financial Stability*, 54, 100874. doi:10.1016/j.jfs.2021.100874.

Grundke, Peter; Pliszka, Kamil (2018). A macroeconomic reverse stress test. *Review of Quantitative Finance and Accounting*, 50(4), 1093–1130. doi:10.1007/s11156-017-0655-8.

Guo, Wei; Miao, Qing; Kim, Yusun; Hou, Yilin (2026). Rising Waters, Falling Taxes: The Impact of Hurricane Sandy on Property Tax Assessments in New York City. *Journal of Environmental Economics and Management*, 138, 103313. doi:10.1016/j.jeem.2026.103313.

Huizinga, Jan; de Moel, Hans; Szewczyk, Wojciech (2017). Global flood depth-damage functions: Methodology and the database with guidelines. *Publications Office of the European Union*, JRC Technical Report EUR 28552 EN. doi:10.2760/16510.

Kim, You Suk; Lee, Donghoon; Scharlemann, Tess; Vickery, James (2024). Intermediation frictions in debt relief: Evidence from CARES Act forbearance. *Journal of Financial Economics*, 158, 103873. doi:10.1016/j.jfineco.2024.103873.

Kingdom of Thailand (2019). พระราชบัญญัติการประเมินราคาทรัพย์สินเพื่อประโยชน์แห่งรัฐ พ.ศ. 2562 [Property Valuation for the Public Interest Act, B.E. 2562 (2019)]. *Royal Gazette Vol. 136, Part 68 Kor, 25 May 2019; Council of State English translation*. <https://www.treasury.go.th/medias/treasury-intranet/1/post/laws_regulations-80/live/77_1768470668_45efd8473fb2b2907e66c0575a1be045.pdf>.

Kolesár, Michal; Rothe, Christoph (2018). Inference in Regression Discontinuity Designs with a Discrete Running Variable. *American Economic Review*, 108(8), 2277–2304. doi:10.1257/aer.20160945.

Kousky, Carolyn; Palim, Mark; Pan, Ying (2020). Flood Damage and Mortgage Credit Risk: A Case Study of Hurricane Harvey. *Journal of Housing Research*, 29(sup1), S86–S120. doi:10.1080/10527001.2020.1840131.

Lee, David S. (2009). Training, Wages, and Sample Selection: Estimating Sharp Bounds on Treatment Effects. *Review of Economic Studies*, 76(3), 1071–1102. doi:10.1111/j.1467-937X.2009.00536.x.

MGR Online (2012). “ธนารักษ์” ลั่นประกาศราคาที่ดินใหม่ 1 ก.ค. ยันพื้นที่น้ำท่วมไม่กระทบ [Treasury confirms new land values from 1 July; says flooded areas not affected]. *MGR Online, 15 June 2012*. <https://mgronline.com/stockmarket/detail/9550000073410>.

Ministry of Finance (Thailand) (2020). กฎกระทรวงการกำหนดราคาประเมินที่ดินหรือสิ่งปลูกสร้าง การจัดทำบัญชีราคาประเมินที่ดินหรือสิ่งปลูกสร้าง และแผนที่ประกอบการประเมินราคาที่ดิน พ.ศ. 2563 [Ministerial Regulation on determining land and building appraisal values, appraisal schedules and appraisal maps, B.E. 2563]. *Royal Gazette Vol. 137, Part 101 Kor, 9 December 2020, pp. 1–8*. <https://www.treasury.go.th/medias/treasury-intranet/1/post/laws_regulations-80/live/77_1768471785_2dbeb6a65c9d48814767427cc89c5715.pdf>.

Pekel, Jean-François; Cottam, Andrew; Gorelick, Noel; Belward, Alan S. (2016). High-resolution mapping of global surface water and its long-term changes. *Nature*, 540(7633), 418–422. doi:10.1038/nature20584.

Pérez Montes, Carlos; García Villasur, Javier; Gutiérrez de Rozas, Luis; Jiménez, Gabriel; Lavín, Nadia; Matyunina, Alexandra; Vegas, Raquel (2025). The impact of the autumn 2024 flash floods in Spain from a financial stability standpoint. *Financial Stability Review (Banco de España)*, no. 48, 5–40. doi:10.53479/40135.

Samritpiam, Kiattikhun; Chongprasoplarp, Poontharik (2026). The Development of the Bank of Thailand's Residential Property Price Index (RPPI). *Presentation, International Conference on Real Estate Statistics 2026, Tokyo; Data Management and Analytics Department, Bank of Thailand*. <https://cures.hias.hit-u.ac.jp/wp-content/uploads/2026/02/BOT_RPPI_Final.pdf>.

Tellman, Beth; Sullivan, Jonathan A.; Kuhn, Catherine; Kettner, Albert J.; Doyle, Colin S.; Brakenridge, G. Robert; Erickson, Tyler A.; Slayback, Daniel A. (2021). Satellite imaging reveals increased proportion of population exposed to floods. *Nature*, 596(7870), 80–86. doi:10.1038/s41586-021-03695-w.

Utami, Westi; Wibowo, Yuli Ardianto; Permadi, Fajar Buyung (2021). The Impact of Tidal Flooding on Decreasing Land Values in the Areas of Tugu District, Semarang City. *Jurnal Ilmu Lingkungan*, 19(1), 10–20. doi:10.14710/jil.19.1.10-20.

Ward, Philip J.; Winsemius, Hessel C.; Kuzma, Samantha; Bierkens, Marc F. P.; Bouwman, Arno; De Moel, Hans; Díaz Loaiza, Andrés; Eilander, Dirk; Englhardt, Johanna; Erkens, Gilles; Gebremedhin, Eskedar Tafete; Iceland, Charles; Kooi, Henk; Ligtvoet, Willem; Muis, Sanne; Scussolini, Paolo; Sutanudjaja, Edwin H.; Van Beek, Rens; Van Bemmel, Bas; Van Huijstee, Jolien; Van Rijn, Frank; Van Wesenbeeck, Bregje; Vatvani, Deepak; Verlaan, Martin; Tiggeloven, Timothy; Luo, Tianyi (2020). Aqueduct Floods Methodology. *World Resources Institute*. <https://www.wri.org/research/aqueduct-floods-methodology>.

World Bank (2012). Thai Flood 2011: Rapid Assessment for Resilient Recovery and Reconstruction Planning. *The World Bank*. doi:10.1596/26862.

Zanaga, Daniele; Van De Kerchove, Ruben; Daems, Dirk; De Keersmaecker, Wanda; et al. (2022). ESA WorldCover 10 m 2021 v200. *Zenodo dataset*. doi:10.5281/zenodo.7254221.

กรมธนารักษ์ (Treasury Department) (2026a). ธนารักษ์พื้นที่สุพรรณบุรี มอบหมายส่วนประเมินราคาทรัพย์สิน ร่วมประชุมการขยายประกาศใช้บัญชีราคาประเมินทรัพย์สิน [Suphanburi Area Treasury Office joins meeting on extending the use of the property appraisal schedules]. *Treasury Department provincial news, 28 October 2026*. <https://www.treasury.go.th/th/news/provinces-news/provinces-news-20261028-565>.

กรมธนารักษ์ (Treasury Department) (2026b). การประชุมคณะกรรมการประเมินราคาทรัพย์สินเพื่อประโยชน์แห่งรัฐ ประจำจังหวัดฉะเชิงเทรา ครั้งที่ 3/2569 [Meeting 3/2569 of the Chachoengsao provincial committee on state property appraisal]. *Treasury Department provincial news, 2 November 2026*. <https://www.treasury.go.th/th/news/provinces-news/provinces-news-20261102-111>.

# Bibliography fixes for the paper, referee round 1

**Working draft, 2026-11-04.** This responds to `07_review/referee_report_paper_round1.md`, sections M11, M12 and 5.2. It covers bibliography work only: no file under `paper/` and no `.tex` file was changed. All changes are in `01_literature/references.bib` (now 152 entries, previously 145; no duplicate keys; braces balanced) plus the `guo` key rename listed in (i.4). A backup of the earlier bib is at `/tmp/claude-1000/-home-thanatchon36/bfd22f34-7614-46fe-b626-02d55cb8768c/scratchpad/references.bib.bak`.

Pages opened on 2026-11-04 (13 requests, throttled, no logins): one MGR Online article; one Treasury provincial news item; the data.go.th records `land-valuation` and `ds-459`; BOT statistics reportIDs 172, 173, 781 and 1008; the BOT sustainability report 2567 page; and Crossref API queries for the two MacKinnon–Webb papers and the Guo et al. DOI. Two web searches were run for the countercyclical buffer. The IMF PDF returned HTTP 403 and was not retried.

---

## (i) Entries added, renamed or annotated

### (i.1) New entries in `01_literature/references.bib`

| Key | What it is | Verified via (2026-11-04) | Notes |
|---|---|---|---|
| `mgr2011cabinetmoratorium` | MGR Online, "ครม.ไฟเขียวพักหนี้ ต่ำกว่า5แสน3ปี คลังจ่ายเงินเดือนเร็วขึ้น" [Cabinet approves a three-year moratorium for debts under 500,000 baht; Finance Ministry to pay salaries earlier], ผู้จัดการรายวัน front page, online 15 Nov 2011, 22:41 | <https://mgronline.com/daily/detail/9540000145958>, text read | Confirms the following. Deputy Finance Minister บุญทรง เตริยาภิรมย์ made the announcement. Six SFIs took part (BAAC, GSB, SME Bank, GHB, Islamic Bank, SMC). Eligible debtors had NPL and/or restructured debt (at BAAC, arrears and/or restructured debt). The ceiling was "ยอดต้นเงินกู้คงเหลือรวมทุกสัญญาในทุกสถาบันการเงินรายละไม่เกิน 500,000 บาท", with debt status "ณ วันที่ 30 มิ.ย.2554". The moratorium ran for three years, backdated, from 1 Oct 2011 to 30 Sep 2014. **The full headline is longer than the one recorded in `02_policy_context/sfi_2011_and_insurance_fund_notes.md`**, so I used the full headline. **Date nuance:** the text says the Cabinet decided "วานนี้ (15 พ.ย.)" ("yesterday, 15 Nov"), so the copy was written for the next day's print edition. The Cabinet date is 15 Nov 2011 and the online date is 15 Nov 2011. This is a press report, not the resolution text. |
| `treasury2026trat` | Treasury Department provincial news, 3 Nov 2026, Trat committee meeting 3/2569 | <https://www.treasury.go.th/th/news/provinces-news/provinces-news-20261103-336>, text read | Follows the `treasury2026phatthalung` pattern. The page has no headline of its own, so the title is its opening sentence: the acting Trat Area Treasurer and appraisal staff held the meeting at 13.30, chaired by the deputy provincial governor. The meeting was "เพื่อพิจารณาขยายเวลาให้ใช้บัญชีราคาประเมินที่ดินและสิ่งปลูกสร้าง รอบบัญชี พ.ศ. 2566 - 2569" (*to consider extending the land and building schedules, 2023–2026 round*), and also set the fiscal-2570 survey period. **No outcome and no extension length are stated.** |
| `treasury2026opendata` | data.go.th dataset record "ราคาประเมินที่ดิน" (`land-valuation`), กรมธนารักษ์ | <https://data.go.th/dataset/land-valuation>, page read | **Licence shown: "Open Data Common"**, with no licence URL. This matches `03_data/README.md`. The record lists 77 CSV resources, one per province. Data last updated 2025-11-07. Metadata created 22 Mar 2566 and last updated 10 Jun 2569. Published on the portal 20 Aug 2567. Update frequency: 4 years. No existing equivalent key was found. |
| `bot2026loansprovince` | BOT statistics, "เงินรับฝากและเงินให้สินเชื่อของธนาคารพาณิชย์จำแนกตามจังหวัด", FI_CB_011 family | BOT pages reportID 1008 (url), 173, 781 and 172, read; data.go.th `ds-459`, read | **reportID 1008** = FI_CB_011_S5, Jul 2024–Jul 2026, updated 10 Sep 2026; it shows figures only where there are more than five borrowers. **173** = FI_CB_011_S2, Jul 2005–Dec 2011, updated 9 Dec 2024. **781** = FI_CB_011_S4, Jan 2013–Jun 2025, updated 8 Aug 2025. **172** = FI_CB_011, titled "(2539-2548)" (1996–2005); its default view showed Jan 2001–Jun 2005, and the page offers both monthly and quarterly views. **ds-459**: licence "Creative Commons Attributions", monthly, metadata updated 5 May 2026; it lists codes FI_CB_011 to FI_CB_011_S5 but no reportIDs. No existing equivalent key: `bot2026priceindex` is the price index EC_EI_008_S3, as the referee says. |
| `bot2025sustainability2567` | BOT page "การเปิดเผยข้อมูลการดำเนินการของ ธปท. เพื่อรับมือกับความเสี่ยงจากการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม ประจำปี 2567", in รายงานความยั่งยืนประจำปี 2567 | <https://www.bot.or.th/th/about-us/sustainability/report2567.html>, page dated 9 Dec 2568 | Section 2.1.1, item (3), verbatim: "จัดทำโครงการนำร่องการทดสอบภาวะวิกฤตในมิติการเปลี่ยนแปลงสภาพภูมิอากาศ (climate stress test) กับธนาคารพาณิชย์กลุ่ม D-SIBs และธนาคารพาณิชย์อื่นที่มีความพร้อม โดยเริ่มจากความเสี่ยงทางกายภาพ (physical risk)". The page gives no scenario, hazard, dates or results. No existing key: `UKPACT_BOT` is a UK PACT case study on stress-test guidelines, and `BOT_StandardPractice_page` is the 2023 handbook page. |
| `mackinnon2017wild` | MacKinnon and Webb, "Wild Bootstrap Inference for Wildly Different Cluster Sizes", *Journal of Applied Econometrics* 32(2), 233–254 | Crossref API, DOI 10.1002/jae.2508 | Online 21 Feb 2016; issue March 2017. Metadata only. |
| `mackinnon2018few` | MacKinnon and Webb, "The wild bootstrap for few (treated) clusters", *The Econometrics Journal* 21(2), 114–135 | Crossref API, DOI 10.1111/ectj.12107 | Online 6 May 2018; print 1 Jun 2018. Metadata only. (Crossref also returns a different 2019 chapter, "Wild Bootstrap Randomization Inference for Few Treated Clusters", DOI 10.1108/s0731-905320190000039003. It was not added.) |
| `chung2013studentised` | Chung and Romano, "Exact and asymptotically robust permutation tests", *The Annals of Statistics* 41(2), 484–507 | Crossref API, DOI 10.1214/13-AOS1090; abstract via OpenAlex | Issue April 2013. Cited for the problem its abstract states (a permutation test need not hold its level when the groups differ in more than the parameter under test); abstract read, text not read. Added 2026-11-04 after the placebo-repair Monte Carlo. |

### (i.2) Countercyclical capital buffer (task f): no new entry

What the public record in the project supports:
- **Framework.** `bot2012capital` is BOT Notification สนส. 12/2555, clause 5.3.1. It sets a countercyclical buffer of 0–2.5% of RWA at the Bank's discretion and did **not** require one at issue (English translation, PDF pp. 4 and 8–9; bib note verified 2026-11-02). `bot2017dsib` (สนส. 16/2560) puts the D-SIB 1% above the minimum, conservation and countercyclical buffers. That is a framework reference, not a rate.
- **Current rate.** The claims ledger row reads "Countercyclical buffer 0-2.5% at the Bank's discretion, not required at issue; no later activation found (baseline zero)" (`06_proposal/claims_ledger.csv` l. 180). Its source is "สนส. 12/2555; search of bot.or.th 2026-11-02", with status "verified 2026-11-02 (absence of activation: search only)". The same wording is in `05_design/framework.md` §5. **No document in the project states the current rate.** "Zero" is an inference from a search that found no activation.
- **Search on 2026-11-04.** Two web searches found no BOT announcement of a CCyB rate. A search-engine summary attributed to IMF Country Report No. 19/318 (Thailand, 2019) the statement that the CCyB "is currently set at 0 percent". The PDF (imf.org) returned HTTP 403 and was not opened. That statement is therefore **[UNVERIFIED]** and was not added. It would also be a 2019 statement, not a current one.
- **Safe wording.** "The capital notification provides for a countercyclical buffer of 0–2.5% at the Bank of Thailand's discretion and did not require one when issued [`bot2012capital`]; I found no public announcement activating it (as of 4 November 2026), so the baseline sets it to zero." Do not write "at its current zero" as a cited fact.

### (i.3) Annotation of an existing entry
- `bot2024circular601`: I extended the `note` with what citation audit round 2 read in the PDF on 2026-11-02 (see (ii), last part). I changed no other field.

### (i.4) The `guo` key (task h): renamed to `guo2026rising`

- **Check.** The Crossref API for 10.1016/j.jeem.2026.103313 gives *JEEM* 138, article 103313, issued and published in print **June 2026**, Elsevier. The bib entry already had `year = {2026}`; only the key (2025, the working-paper year) was wrong. I renamed it to **`guo2026rising`** and updated the bib note.
- **Files changed** (number of occurrences): `01_literature/references.bib` (1), `01_literature/lit_matrix.csv` (1; its `year` field also changed from 2025 to 2026), `01_literature/literature_review.md` (1), `01_literature/gap_statement.md` (1), `01_literature/strands/S6.bib` (1; this is the working-paper record and keeps `year = 2025`), `01_literature/strands/S6_matrix.csv` (1), `01_literature/strands/S6_notes.md` (2), `01_literature/strands/S9_official_valuation_sweep.md` (1), `05_design/identification.md` (1), `06_proposal/claims_ledger.csv` (3) and `06_proposal/proposal.md` (2).
- **Files under `paper/` that you need to change:** `paper/refs.bib` (l. 1083, `@article{guo2025rising,`) and `paper/sections/introduction.tex` (l. 13, `\citet{guo2025rising}`). `paper/paper.aux` and `paper/paper.bbl` also contain the key, but they are build files and regenerate on the next LaTeX/BibTeX run.
- **Left unchanged on purpose:** the review records in `07_review/` (`citation_audit.md`, `citation_audit_round2.md`, `referee_report_paper_round1.md`). They are dated snapshots, and the referee report's "key and year mismatch" refers to the old key. Rename them with `sed -i 's/guo2025rising/guo2026rising/g'` if you want them changed.
- **Caveat.** `01_literature/merge_strands.py` rebuilds `references.bib` from the strand `.bib` files. Many entries were added straight to `references.bib`, this round's included, so re-running the script would drop them.

### (i.5) Related key/year mismatch found, not changed
- `chongwilaikasaem2022flood` has `year = {2023}`: Crossref issued it in 2022 (online 29 July 2022), and the print issue 16(6) is dated November 2023. It is the **two-author** paper (Chongwilaikasaem and Chalermyanont). The bib holds no single-author "Chongwilaikasaem (2023)", so the referee's "Chongwilaikasaem (2023)" means this entry. Cite it as Chongwilaikasaem and Chalermyanont (2023). The key could be renamed in the same way as `guo` if you want consistency.
- `blickle2025bad` is the NY Fed Staff Report (rev. October 2025). The bib note records a JMCB version (doi 10.1111/jmcb.70036, online 27 March 2026, no volume or pages yet) that was not read.

---

## (ii) Citable sentences (only what the project notes support)

The read depth shown is the one recorded in `lit_matrix.csv`, the strand notes or the bib `note`. A sentence attributed to an abstract-only source is no stronger than the abstract.

**Banks, collateral and flood-risk pricing**

1. **`blickle2025bad`** (intro, staff-report version). Blickle, Hamerling and Morgan find that weather disasters have generally small effects on US banks: a single-county bank would fail only after a disaster about 6.7 standard deviations beyond the 95th-percentile event. They attribute this resilience to higher loan demand and to local banks' knowledge of flood risk, not to federal aid. The calculation is in effect a reverse stress test on a hazard variable; that last clause is the project's characterisation, not the authors' term.
2. **`vangerwen2025flooded`** (abstract). Van Gerwen, Degryse, Ongena and Scopelliti report that, after the 2021 floods, one major Belgian bank revalued flood-exposed collateral downward, with internal staff adjusting more than external valuers, and raised rates on floating-rate loans to exposed firms without reducing its exposure.
3. **`bernstein2019disaster`** (abstract). Bernstein, Gustafson and Lewis find that US coastal homes exposed to projected sea-level rise sell at a discount of about 7% relative to observably equivalent unexposed homes. The discount has grown over time and is driven by sophisticated buyers.
4. **`baldauf2020does`** (abstract). Baldauf, Garlappi and Yannelis show that US homes projected to be under water sell at a discount in neighbourhoods that believe in climate change, relative to neighbourhoods that do not.
5. **`keys2020neglected`** (intro; NBER WP 27930). Keys and Mulder find that, from 2013 to 2018, sales volumes in the coastal Florida tracts most exposed to sea-level rise fell by 16–20% relative to matched tracts while prices moved in step. Relative prices fell 5–10% below trend by 2020, with little change in mortgage denial or securitisation.
6. **`sastry2026who`** (abstract). Sastry shows that Florida mortgage lenders require lower loan-to-value ratios at origination for flood risk that is not insurable under the NFIP's coverage limits.
7. **`lepore2024beyond`** (abstract; IMF WP 2024/197). Lepore and Mok find that the capital impact of floods on Dutch banks varies greatly across scenarios and is non-linear in damage, amplified by climate change and mitigated by flood defences.
8. **`dhima2026integration`** (abstract). Dhima et al. embed flood damage to collateral in an extended Merton model. They find that flooding affects PD, LGD and capital, but not systematically when damage is below the expected return on the property, and materially for already vulnerable firms.
9. **`kocornikmina2020flooded`** (intro and data section of CEP DP 1398; journal abstract). Kocornik-Mina, McDermott, Michaels and Rauch find that low-elevation urban areas flood more yet hold more economic activity and recover as quickly, with little relocation of activity after floods.

**Debt relief and forbearance**

10. **`gine2018economic`** (intro; read in the World Bank PRWP 7109 version). Giné and Kanz find that India's 2008 farm-loan waiver reallocated credit away from more exposed districts and worsened later loan performance, without measurable effects on productivity, wages or employment.
11. **`mukherjee2018borrowers`** (abstract). Mukherjee, Subramanian and Tantri find that, after the same Indian waiver, later loan performance worsened among beneficiaries who had not been distressed and improved among those who had.
12. **`dinerstein2024debt`** (abstract). Dinerstein, Yannelis and Chen show that US borrowers used the liquidity from a student-loan payment moratorium to borrow more rather than to avoid delinquency on other debt. (The wording follows the claims ledger, l. 49. The lit matrix has no row for this paper; read depth is from the bib note.)
13. **`kim2024intermediation`** (abstract). Kim, Lee, Scharlemann and Vickery find that access to CARES Act mortgage forbearance depended on the servicer: small and non-bank servicers with thin liquidity buffers granted fewer forbearances. Easier access raised mortgage non-payment but reduced delinquency outside forbearance.
14. **`chari2021unholy`** (abstract; NBER WP 28435). Chari, Jain and Kulkarni find that stressed Indian banks used regulatory provisioning forbearance to conceal loans to insolvent firms, and that credit shifted from healthy firms to the weakest.

**Thailand**

15. **`luangaram2024climate`** (intro; PIER DP 224). Luangaram, Sethapramote, Thampanishvong and Uddin find, using market-based CoVaR, that transition risk significantly raises the systemic risk of Thai banks. They argue that physical risk, especially floods, challenges bank portfolios.
16. **`noy2021floods`** (full text of results sections, CESifo WP 7644 version; tables not read). Noy, Nguyen and Patel find that the 2011 flood reduced Thai households' business income by about THB 6,465 for directly flooded households and THB 4,018 through spillovers, leaving total spending unchanged. They report the effects on debt and savings as small and insignificant, without tabulating them.
17. **`chongwilaikasaem2022flood`** (abstract; cite as Chongwilaikasaem and Chalermyanont, 2023). Using spatial regressions for Hat Yai, Songkhla, Chongwilaikasaem and Chalermyanont find a negative effect of flood risk on property prices, both in survey-based rents and in Ministry of Finance official valuations.
18. **`chitchumnong2025physical`** (full). In one Thai bank's mortgage book, Chitchumnong, Hatairatana and Khangphukhieo find a small rise in default in late 2011, which they attribute to delinquent borrowers who were **ineligible** for relief, followed by default below model-predicted levels, which they attribute to debt relief and treat as a lower bound. Auto-loan defaults, by contrast, spiked. *Wording check:* the notes (`strands/S3_notes.md` l. 96, `S5_notes.md` l. 42, `literature_review.md` l. 145) tie the initial rise to borrowers *ineligible* for relief. They do **not** say that the below-predicted default was measured "among relief-eligible borrowers". The p. 25 wording should therefore be relaxed to "after the flood", unless the paper is re-read.
19. **`sawada2018land`** (full). Sawada, Nakata, Sekiguchi and Okuyama find that industrial land prices in flooded areas fell after the 2011 floods (by 8.27% of the post-flood mean in the JETRO industrial-estate data and 6.49% in the AREA series). Townhouse prices fell by 4.85%, while residential and commercial land, detached houses and condominiums showed no significant change.

**Official assessments**

20. **`avenancioleon2022assessment`** (abstract). Avenancio-León and Howard find that Black and Hispanic US residents bear a 10–13% higher property-tax burden for the same public services, because assessments are less sensitive to neighbourhood attributes than market prices are.
21. **`guo2026rising`** (intro and results sections, Sections 1, 3.4 and 5.1–5.2, of the 23 June 2025 working paper; the published JEEM version was not read). Guo, Miao, Kim and Hou find that, after Hurricane Sandy, sale prices of inundated New York City homes fell by about 10%. Assessor-estimated market values fell by about 17%, mostly through the tax-relief policy, assessed values by about 10% and taxable values by about 6.5% (Table 3). For undamaged homes in the high-risk zone, sale prices fell by about 11% with no change in official values (Table 4). Statutory assessment caps of 6% a year and 20% over five years, binding for about 80% of properties before Sandy, blunt the transmission (p. 10). *For the "−10% for inundated homes" in M11:* that figure is the sale-price fall and also the assessed-value fall; −17% is assessor market value.

**Stress tests**

22. **`caloia2026floods`** (abstract of the published JFS version; the DNB WP 796 / TI DP 2023-083 version read in full, `strands/S8_dnb796_notes.md`). Caloia, van Ginkel and Jansen run a **forward** loan-level stress test of eight Dutch banks under **38 fixed flood scenarios**. CET1 falls by 30–50 bp in most scenarios and by about 110 bp in the most extreme. Collateral falls only by repair cost, and the test includes no revaluation, forbearance or solved-for breaking point. *Answer to the referee:* the published version is described as scenario-based and forward. The working paper never uses the term "reverse stress test" (a text search for "reverse" found no hits). "In essence, a reverse stress test" is the self-description in the **2021** paper, `caloia2021flood` (DNB WP 730, results sections read): CET1 falls by 110–132 bp for floods in unprotected areas, against more than 700 bp for an extreme flood in the protected west.

**Credit**

23. **`albertazzi2026physical`** (full text of results sections: Sections 1–3, 5.3, Table 17 and the opening of 6). Using AnaCredit data and a spatial discontinuity at Copernicus flood boundaries, Albertazzi, Djekic and Ponte Marques find:
    - default on pre-existing loans rises by 0.568 pp after one quarter (Table 8, p. 27) and by 0.64–0.69 pp over two quarters (Table 9, p. 28), roughly doubling a baseline annual rate of about 1.4%;
    - credit to firms just inside the perimeter rises by 3.5–5% in the flood quarter and then reverses, with no significant cumulative change;
    - for real-estate-backed loans to micro firms, LTV rises by 5.3 pp, with a large-firm interaction of −6.2 pp (Table 17, p. 39).

    *Note on "their setting is insured":* the paper's own review states that only about 25% of catastrophe losses in the EU are insured, with coverage below 5% in several member states (PDF p. 9; `07_review/citation_audit.md` item 4). Use "an advanced-economy setting".

**Hazard and damage discounts (the "2–8%" benchmark)**

24. **`ortega2018rising`** (abstract). Ortega and Taşpınar find that New York homes damaged by Hurricane Sandy lost 17–22% of their value immediately and then partly recovered, while undamaged homes in the flood zone developed a gradual penalty that reached 8% by 2017.
25. **`bin2013changes`** (abstract). Bin and Landry find no flood-zone discount in Pitt County, North Carolina, before Hurricane Fran, but discounts of 5.7% after Fran and 8.8% after Floyd, which faded within five to six years.
26. **`beltran2018flood`** (abstract). In a meta-analysis of 364 estimates, Beltrán, Maddison and Elliott propose a discount of 4.6% for the inland 100-year floodplain as a rule of thumb. This is a hazard-zone discount, not a realised-flood discount.

    *Implication (the referee's point, supported by the notes):* 4.6–8.8% are hazard-zone discounts, and realised-damage discounts are larger (17–22% for damaged homes in New York; about 10% for inundated homes' sale prices in Guo et al.).

**Policy documents**

27. **`bot2024circular601`, the trigger.** Yes, alert levels count as a trigger as well as zone declarations, as recorded from the PDF in `07_review/citation_audit_round2.md` (2026-11-02) and `02_policy_context/policy_timeline.md` row 22:
    - Item 1.1 (p. 2) runs the 12-month relief window from the date "ผู้มีอำนาจออกประกาศเขตพื้นที่ประสบสาธารณภัย … หรือกองบัญชาการหรือกองอำนวยการ … ได้แจ้งระดับสถานการณ์สาธารณภัย เป็นระดับเฉพาะสีเหลือง สีส้ม หรือสีแดง". That is, from a disaster-zone declaration **or** a yellow, orange or red disaster-situation level.
    - Q&A 1 (5 Nov 2567, p. 5) lets affected areas be identified from DDPM alert levels or provincial declarations, with direct or indirect impact.
    - Item 2.1 (p. 3) requires lenders to link the impact to each debtor.
    - The preamble covers windstorm, flood and drought.
    - The title is "ขอความร่วมมือ…" (*request for cooperation*).

    Safe sentence: "Since August 2024 a standing Bank of Thailand circular, framed as a request for cooperation, lets lenders keep the pre-disaster classification of assisted debtors not yet impaired, for up to 12 months from a disaster-zone declaration or from a yellow, orange or red disaster-alert level [`bot2024circular601`, items 1.1 and 2.2]."
28. **`mgr2012appraisal`, MGR Online, 15 June 2012** (article text read, 2026-11-02).
    - The bib note records the Treasury Director-General as saying three things. The 2012–15 round was postponed by six months, to 1 July 2012, because of the floods. Prices in flooded areas were surveyed and no fall was found, and Nakhon Sawan rose. The values compiled in late 2011 were used unchanged, covering 29.3 million parcels with an average rise of 21.34%.
    - The claims ledger (l. 188) records: "After 2011 the Treasury found no fall in flooded areas and left its late-2011 schedule unrevised (the schedule itself raised values 21.34% on average)", status "verified (press report of official statement)".
    - It is a press report of an official statement. It bears on P2, and it does **not** support the SFI moratorium; cite `mgr2011cabinetmoratorium` for that.
    - Safe sentence: "After the 2011 floods the Treasury Department postponed the new schedule by six months, reported that its survey found no fall in prices in flooded areas, and brought the schedule compiled in late 2011 into force unchanged, with an average rise of 21.34% [`mgr2012appraisal`]."

**New policy and data keys, for M12**

- Pilot climate stress test: "The Bank of Thailand reports a pilot climate stress test with the D-SIBs and other ready commercial banks, starting with physical risk [`bot2025sustainability2567`]." No dates, scenarios or results are public.
- Trat: "the Trat committee met on 3 November 2026 to consider extending the 2023–2026 schedules [`treasury2026trat`]". It considered the extension; no decision is reported.
- Open data: "The parcel-level schedule is published as open data on data.go.th under the 'Open Data Common' licence [`treasury2026opendata`]." This replaces `treasury2026extbriefing` in that sentence.
- Loans by province: cite `bot2026loansprovince` in place of `bot2026priceindex`.
  - **On "monthly from 1996":** only the title of reportID 172 says 1996–2005 ("2539-2548"). Its default view showed Jan 2001–Jun 2005, and the page offers monthly and quarterly views. The project downloaded only S2, S4 and S5 (Jul 2005 onwards; S3, for 2012, was not located).
  - Safe wording: "monthly from July 2005 (2012 missing)". Alternatively, verify the 1996–2000 months before writing "from 1996".
- Wild bootstrap: `mackinnon2017wild`, `mackinnon2018few` (metadata only; do not attribute findings beyond the titles without reading them).

---

## (iii) Unverified or not found

- **[UNVERIFIED]** IMF Country Report No. 19/318 (2019) as a source for "CCyB currently set at 0 percent". This came from a search-engine summary only; the PDF returned 403. Not added.
- **Not found:** any public BOT document stating the current countercyclical buffer rate, or an activation decision, as of 2026-11-04 (two searches). The project's "no activation" is an absence-of-evidence finding (claims ledger l. 180).
- **Not verified:** whether FI_CB_011 (reportID 172) actually holds monthly data for 1996–2000. The title says 1996–2005; the default view showed 2001–2005.
- **Not read:** the published JFS text of `caloia2026floods`, the published JEEM text of `guo2026rising` and the JMCB version of `blickle2025bad`. The sentences above rest on the working-paper versions.
- **Not read:** the text of either MacKinnon–Webb paper (metadata only).
- **Not read:** the 15 Nov 2011 Cabinet resolution text (resolution.soc.go.th blocked, per the policy notes). `mgr2011cabinetmoratorium` is a press report.
- `dinerstein2024debt` has no `lit_matrix.csv` row. Its sentence rests on the claims ledger (l. 49) and the bib note (abstract via Crossref).

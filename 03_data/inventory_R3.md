# Data inventory for R3 "Underwater Collateral": public-data chapter

*Working draft. All facts are as of 2026-11-02 unless stated otherwise, and each comes from the page or file cited. Speculation is marked [S]. Nothing here was downloaded in bulk. Small metadata checks are kept in `/tmp/claude-1000/-home-thanatchon36-github/6b2fbf36-677b-40f6-afe6-9f21565701c4/scratchpad/data_checks/` (scratch, not project data).*

**Question.** Is a public-data chapter feasible that asks whether flood exposure is capitalised into Thai collateral or appraisal values and into local credit aggregates?

**Short answer.** Yes, as a cross-sectional (and, from 2027, two-round) design. The Treasury Department now publishes **parcel-level official land appraisal prices for every province as open CSV files** under the DGA Open Government Licence. Flood exposure can be measured from the Global Flood Database, which contains the 2011 Thai event (DFO 3850). BOT publishes **monthly commercial-bank loans and deposits by province from 1996** and a district-level table, so it covers the 2011 floods. The main gaps are (i) only the current appraisal round (2023–2026) is on the portal; (ii) the appraisal files carry map-sheet and parcel numbers, not coordinates, and the official parcel-geometry API requires a formal permission letter; and (iii) market price indices (BOT, REIC) are too coarse for a within-region design.

## Summary table

| # | Item | Exists? | Granularity | Period (public) | Access | Licence / terms | Usable for public chapter |
|---|---|---|---|---|---|---|---|
| 1a | Treasury Dept land appraisal prices (ราคาประเมินที่ดิน), data.go.th / catalog.treasury.go.th | Yes | **Parcel** (title-deed land, keyed by UTM map sheet + parcel number); 77 provincial CSV files | Current round only: 2023–2026 (dataset `created_date` 2023-01-01); next round planned for 1 Jan 2027 (press reports only) | Free bulk CSV download, no login (≈1.44 GB in total; Bangkok file 92 MB) | DGA Open Government Licence (listed as "Open Data Common"): copy, publish, adapt, combine for research; attribution required | **Yes** (core dataset); geocoding is the bottleneck |
| 1b | Treasury condominium, building and other-land appraisal tables | Yes | Condo: tambon (sub-district) coverage; building: province; other land: tambon | Current round | Free CSV | Same | Partly |
| 1c | Treasury per-parcel lookup (assessprice.treasury.go.th; TRD Property Valuation app) | Yes | Parcel | Current round | Interactive lookup only | Not stated on page | No (not for bulk use) |
| 1d | DOL parcel geometry API (ข้อมูลรูปแปลงที่ดิน ตามเลขที่โฉนด / LandsMaps) | Yes | Parcel polygon | Current | API needs a formal permission letter and consumer key/secret issued by DOL | "License not specified" | No without CP3 approval |
| 2 | REIC (ศูนย์ข้อมูลอสังหาริมทรัพย์) price indices | Yes | Bangkok & vicinities; EEC (3 provinces) | Quarterly; series start not stated on pages opened | Free press-release PDFs; membership and paid products exist | Copyright REIC; reproduction requires written consent; automated collection prohibited | Partly (context only) |
| 3a | BOT Residential Property Price Index (EC_EI_008_S4) | Yes | National; Bangkok & vicinities; Central; North; Northeast; South | Monthly, Jan 2011–Sep 2026 | Free web table, no login | BOT statistics; data.go.th BOT entries are CC-BY | Partly (regional control only) |
| 3b | BOT deposits and loans by province (FI_CB_011 series) | Yes | **Province** (77) and region | Monthly, 1996–2005 (FI_CB_011), Jul 2005–Dec 2011 (S2), Jan 2013–Jun 2025 (S4), Jul 2024–Jul 2026 (S5); S3 not checked | Free web table, no login; listed on data.go.th (ds-459) | CC-BY (data.go.th listing) | **Yes** (credit-aggregate outcome) |
| 3c | BOT deposits and loans by district (XLS_CB_004) | Yes | **District (amphoe)** | Monthly; start date not verified | BOT site (file link not located); data.go.th entry now not public | CC-BY on earlier data.go.th listing | Yes, if the archive reaches back to 2011 (unverified) |
| 3d | BOT loans by ISIC sector by province (FI_CB_087, S2, S3) | Yes | Province × sector | Monthly; start not verified | Free web table | CC-BY (data.go.th ds-466) | Partly |
| 3e | BOT API (portal.api.bot.or.th) | Yes | Statistics products by category | — | Account required | Terms at /terms (not read) | Not needed (web tables suffice); registration waits for CP3 |
| 4a | Global Flood Database v1 (GEE `GLOBAL_FLOOD_DB/MODIS_EVENTS/V1`) | Yes; **contains the 2011 Thai flood (DFO 3850)** | Raster per event; native resolution about 250 m (MODIS; event file 0.002246°). The GEE catalogue lists a 30 m pixel grid, which is not the native resolution | 913 events, 2000–2018; 31 events involve Thailand | Event zips are on the public GCS bucket `gfd_v1_4`, no login needed (DFO 3850 on disk, see `04_analysis/groundwork_notes.md`); event metadata CSV on GitHub (MIT) | CC BY-NC 4.0 | **Yes** (exposure measure) |
| 4b | GISTDA flood products (data.go.th listings) | Yes | Raster/vector flood extent; recurrence layer | Recurrence layer 2011–2023; daily flood extent (recent) | API key via GISTDA registration | data.go.th: "Open Data Common" for two datasets; "License not specified" for the Disaster Platform STAC | Partly (after CP3 registration) |
| 5 | Listed-bank disclosures (TFRS 9 staging, ECL, climate) | Yes (SCB checked in full; KBank partly; BBL not reached) | Bank-year; staging and ECL by broad sector incl. housing loans; geography only Thailand vs abroad | FY2025 (and FY2024 comparatives) | Free PDFs | Public company disclosures | Partly (descriptive only; no flood-exposure figures published) |
| 6 | BOT Standard Practice on environment and climate (ว.113/2566) | Yes | Policy text | Dated 15 Feb 2023 | Free PDF | — | Context (policy facts) |

---

## 1. Treasury Department land appraisal prices (กรมธนารักษ์ ราคาประเมินที่ดิน)

**What exists (as of 2026-11-02).**

- Open-data dataset **ราคาประเมินที่ดิน** (*official land appraisal prices*), publisher กรมธนารักษ์, maintainer กองมาตรฐานการประเมินราคาทรัพย์สิน (*Property Valuation Standards Division*). Listed on data.go.th and hosted on the Treasury's own CKAN catalogue.
  - data.go.th entry: <https://data.go.th/dataset/land-valuation> (metadata read via the data.go.th CKAN API `package_search`; data.go.th robots.txt allows this with a 10-second crawl delay).
  - Treasury catalogue: <https://catalog.treasury.go.th/dataset/land-valuation>.
  - Description: "ราคาประเมินที่ดินเพื่อประโยชน์แห่งรัฐ ในการจัดเก็บภาษีที่ดิน ตาม พรบ ภาษีที่ดินและสิ่งปลูกสร้าง พ.ศ. 2562" (*land appraisal prices for state purposes, for land tax collection under the Land and Buildings Tax Act B.E. 2562 (2019)*).
  - Metadata: `created_date` 2023-01-01; update frequency every 4 years; `last_updated_date` 2025-11-07; data classification "เปิดเผย" (*public*); access condition "ไม่มีการจำกัดการเข้าถึงข้อมูล" (*no access restriction*); data source "การวิเคราะห์ราคาซื้อขายของตลาดตามหลักวิชาการด้านประเมินราคาทรัพย์สิน" (*analysis of market transaction prices under valuation methodology*).
  - **77 CSV resources, one per province**, totalling about 1.44 GB (Bangkok 91.8 MB; Mae Hong Son 1.8 MB). Individual resources were last modified between April 2025 and May 2026, so files are revised in place.
- **Granularity: parcel.** One province file was opened as a metadata check (Mae Hong Son, `land_58_mae-hong-son.csv`, 1.76 MB). The server ignored a byte-range request and returned the whole file, which was summarised and then deleted, keeping only the first 2 KB. Columns are `UTMMAP1, UTMMAP2, UTMMAP3, UTMMAP4, UTMSCALE, LAND_NO, EVAPRICE`: a UTM cadastral map-sheet reference, the map scale (500 to 5,000), the parcel number on that sheet and the appraised price. The file has 46,447 parcel rows, with `EVAPRICE` between 30 and 52,000 (median 520). The unit is not stated in the file; it is presumably baht per square wah, the usual Treasury unit [S, to confirm from Treasury documentation].
- **Periods.** Only the current round is published. The Treasury catalogue holds no dataset for the 2016–2019 or 2020–2022 rounds (catalogue search for "ราคาประเมิน", 5 results, opened 2026-11-02). Press reports (not primary) say the 2023–2026 round took effect on 1 January 2023 and that the next round is planned for announcement in December 2026 and use from 1 January 2027 (e.g. [InfoQuest](https://www.infoquest.co.th/?p=567390), [Kaohoon](https://www.kaohoon.com/news/local/845642)). Not confirmed on a Treasury page.
- **Companion datasets** (same licence and catalogue): ราคาประเมินอาคารชุด (*condominium unit appraisal*; geographic coverage "ตำบล", one 18.8 MB CSV, `condo_all_20240805`), ราคาประเมินสิ่งปลูกสร้าง (*building appraisal*; province), ราคาประเมินทุนทรัพย์ที่ดินประเภทอื่น (*appraisal for land with other title types*; tambon).
- **Per-parcel lookup:** <https://assessprice.treasury.go.th> (page is rendered by JavaScript; search options, terms and login could not be read). The condominium dataset links to this system.

**Access and terms.** Free direct CSV download, no login or registration. catalog.treasury.go.th robots.txt disallows `/api/`, `/dataset/rate/`, `/revision/`, `/dataset/*/history` and asks for a 10-second crawl delay; the resource download paths are allowed. The dataset licence is shown as "Open Data Common". The data.go.th terms are the *Terms and Conditions for DGA Open Government License* v1.0 (10 June 2021; [EN PDF](https://data.go.th/uploads/page_images/2021-06-11-053225.908526Terms-and-Conditions-for-DGA-Open-Government-LicenseEN04062021.pdf)): users may "copy, publish, distribute or beneficially process the Data", combine it with other data for "education, analysis, research", must not change substantive meaning, and "shall state references … to the sources of Data and organizations … whom such Data owned by". No fee.

**Geocoding constraint.** The appraisal file has no coordinates. Parcel polygons come from the Department of Lands (กรมที่ดิน): the data.go.th listing *ข้อมูลรูปแปลงที่ดิน ตามเลขที่โฉนด* (`mapland-parcel`) says use of the API requires "ทำหนังสือขออนุญาตใช้ข้อมูล" (*a written request for permission*) and a consumer key and secret issued by DOL; the licence is "not specified". This is outside the public-data route until CP3. A public alternative [S]: the UTM map-sheet fields identify a cadastral sheet of known extent in the Thai UTM sheet system, so parcels can be placed at sheet level (roughly 0.5–2 km cells at 1:1,000–1:4,000) without parcel polygons. The sheet-numbering convention must be verified from a DOL or RTSD source before use.

**Assessment.** Usable: yes. This is the single best public dataset for the chapter. Limitations: (a) appraisal prices are administrative values set for tax and registration fees, not transaction prices, which needs a clear interpretation in the chapter; (b) one public round today, so the first design is cross-sectional (2023–2026 values against 2011 flood exposure and recurrence, with map-sheet or tambon fixed effects); (c) the 2027–2030 round should allow a round-to-round change design, but **the 2023–2026 files are revised in place and may be replaced**, so a dated snapshot should be archived (with user approval) before January 2027.

## 2. REIC (ศูนย์ข้อมูลอสังหาริมทรัพย์, Government Housing Bank)

Opened <https://www.reic.or.th/> and its index section <https://www.reic.or.th/Research/REICReport> on 2026-11-02. Indices published (quarterly, with free press-release PDFs):

- ดัชนีราคาที่ดินเปล่าก่อนการพัฒนา กรุงเทพฯ-ปริมณฑล (*undeveloped vacant land price index, Bangkok and vicinities*); Q3 2026 value 459.0, +2.6% y/y ([press release 302](https://www.reic.or.th/Activities/PressRelease/302)). Base period, start year and sub-zones were not stated on that page.
- ดัชนีราคาที่ดินเปล่าก่อนการพัฒนา EEC (*vacant land price index, EEC*).
- ดัชนีราคาบ้านจัดสรรใหม่ / ห้องชุดใหม่ ที่อยู่ระหว่างการขาย กรุงเทพฯ-ปริมณฑล (*new housing and new condominium price indices, under sale, Bangkok and vicinities*).
- ดัชนีราคาที่อยู่อาศัยที่อยู่ระหว่างการขาย ใน 3 จังหวัด EEC (*residential price index, 3 EEC provinces*); construction cost index; two confidence indices.

**Geography.** Bangkok and vicinities and the EEC only; no province- or zone-level series was found on the pages opened.

**Access and terms.** Releases are free PDFs. The site has membership and paid products ([Product/All](https://www.reic.or.th/Product/All), [HowtoPay](https://www.reic.or.th/Product/HowtoPay)); these were not opened. Terms ([Policy](https://www.reic.or.th/Policy)): content is REIC's copyright; "ห้ามมิให้มีการทำซ้ำ และแก้ไขสิ่งหนึ่งสิ่งใดในเว็บไซต์นี้ … โดยไม่ได้รับความยินยอมเป็นลายลักษณ์อักษร" (*no reproduction or modification without written consent*); automated collection of content is prohibited (s. 2.1.8).

**Assessment.** Partly usable: aggregate context and a check on the appraisal data in Bangkok. Not a basis for identification. Any zone-level REIC data would need written permission or payment (CP3).

## 3. BOT house price indices and BOT loans and deposits by province

All tables below were opened on the BOT statistics server (`app.bot.or.th/BTWS_STAT`) on 2026-11-02. They are free web tables with a download button and need no login. (app.bot.or.th returned 404 for robots.txt; www.bot.or.th robots.txt only disallows system paths.)

**House prices.**

- **EC_EI_008_S4 Residential Property Price Index** ([link](https://app.bot.or.th/BTWS_STAT/statistics/BOTWEBSTAT.aspx?reportID=993&language=ENG)): monthly, Jan 2011–Sep 2026 (last updated 31 Oct 2026), base 2011 = 100. Geography: nationwide; Bangkok and vicinities; Central (excluding Bangkok and vicinities); North; Northeast; South. Single-detached houses: all six; town houses: four (no North or Northeast); condominiums: Bangkok and vicinities only. Hedonic (rolling window, time dummy), 3-month moving average, from commercial-bank and GHB mortgage data, plus other SFIs from January 2023 (footnote 1).
- **RG_SR_046 Residential Property Price Index** ([link](https://app.bot.or.th/BTWS_STAT/statistics/BOTWEBSTAT.aspx?reportID=886&language=ENG)): Mar 2008–Mar 2019, base Jan 2009 = 100, includes a land price index (stratification method); discontinued (last update 2 Dec 2022). The page does not name its region.
- Also listed: EC_EI_008_S2 (house price index, commercial-bank mortgage loans) and EC_EI_008_S3 (with land price index); not opened.

**Loans and deposits by province: public, monthly, from 1996.**

- **FI_CB_011** *เงินรับฝากและเงินให้สินเชื่อของธนาคารพาณิชย์จำแนกตามจังหวัด (2539-2548)* (*commercial-bank deposits and loans by province, 1996–2005*), [reportID=172](https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?reportID=172&language=th) (seen in search results; not opened).
- **FI_CB_011_S2** (2549–2554), [reportID=173](https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?reportID=173&language=th): monthly, Jul 2005–Dec 2011, million baht, Bangkok (head office/other), nine regional zones (เขต 1–9) and provinces; Bueng Kan has no data (province created March 2011). Last updated 9 Dec 2024.
- **FI_CB_011_S4**, [reportID=781](https://app.bot.or.th/BTWS_STAT/statistics/BOTWEBSTAT.aspx?reportID=781&language=th): monthly, Jan 2013–Jun 2025; by deposit type and loan type (overdrafts, loans, bills), loan-to-deposit ratio and number of offices, by province and four regions. Footnote 3/: from January 2015 some banks book hire-purchase car loans at head office rather than the branch, which shifts loans towards Bangkok.
- **FI_CB_011_S5**, [reportID=1008](https://app.bot.or.th/BTWS_STAT/statistics/BOTWEBSTAT.aspx?reportID=1008&language=TH): monthly, Jul 2024–Jul 2026 (updated 10 Sep 2026), same variables. New footnote 3/: data are shown only where there are more than five debtors, to prevent identification.
- The S3 table was not opened, so the 2012 coverage is unverified.
- data.go.th lists the whole series as *เงินรับฝากและเงินให้สินเชื่อจำแนกตามจังหวัด* (`ds-459`, BOT, licence **Creative Commons Attributions**), naming FI_CB_011 and S2 to S5.
- The source change from August 2025 is documented at <https://www.bot.or.th/th/statistics/revised-table-list.html>: S4 replaced by S5 from the July 2025 period, back-filled to July 2024; XLS_CB_004 and FI_CB_087 changed source from the same date.

**District level.** **XLS_CB_004** *รายงานเงินฝากและเงินให้สินเชื่อธนาคารพาณิชย์รายอำเภอ* (*commercial-bank deposits and loans by district*) is listed on the BOT revised-table page. Its earlier data.go.th entry (`bot-ds-460`, CC-BY, monthly) now returns an authorisation error through the API. The BOT download link and start date were not found.

**Loans by sector by province.** **FI_CB_087_S3** *ยอดคงค้างเงินให้สินเชื่อในประเทศของธนาคารพาณิชย์แยกตามประเภทธุรกิจรายจังหวัด* (*domestic loans by ISIC business type by province*), data.go.th `ds-466` (CC-BY), [reportID=1020](https://app.bot.or.th/BTWS_STAT/statistics/BOTWEBSTAT.aspx?reportID=1020&language=TH). Start date not checked.

**BOT API.** The developer portal moved to <https://portal.api.bot.or.th/> (gateway `gateway.api.bot.or.th`; the old `apiportal.bot.or.th` no longer resolves). It offers high-frequency data, statistics (financial institutions among them) and other data, requires an account ("existing users must create a new account"), and links its terms at `/terms` (not read). Registration waits for CP3; the web tables make it unnecessary for this chapter.

**Assessment.** Provincial loans and deposits: **yes**, a monthly provincial panel spanning 2011 that supports an event-study of local credit aggregates around the 2011 flood. Two caveats: these are booking-location data (branch, with head-office booking of some loans), and the series breaks in 2005, 2013 and 2024 need splicing. House price indices: partly (regional controls only).

## 4. Flood exposure: Global Flood Database and GISTDA

**Global Flood Database v1.** Catalogue page <https://developers.google.com/earth-engine/datasets/catalog/GLOBAL_FLOOD_DB_MODIS_EVENTS_V1> (opened 2026-11-02): 913 events, 2000-02-17 to 2018-12-10; bands `flooded`, `duration`, `clear_views`, `clear_perc`, `jrc_perm_water`; 30 m pixels in the GEE catalogue, but the downloaded DFO 3850 event raster is about 250 m (0.002246°; MODIS native), which is what limits the resolution; event properties include `id` (DFO-aligned), country fields, DFO deaths, displaced, cause and severity. Licence **CC BY-NC 4.0**. Citation: Tellman et al., *Nature*, doi:10.1038/s41586-021-03695-w.

**Event list check (metadata only, no imagery).** The authors' repository [cloudtostreet/MODIS_GlobalFloodDatabase](https://github.com/cloudtostreet/MODIS_GlobalFloodDatabase) (MIT licence) contains `data/gfd_qcdatabase_2019_08_01.csv`, 913 rows, matching the GEE event count. **31 events** list Thailand as main or other country. The 2011 floods are:

| DFO ID | Began | Ended | Cause | Dead | Severity |
|---|---|---|---|---|---|
| 3795 | 2011-03-23 | 2011-04-10 | Heavy rain | 59 | 2 |
| **3850** | **2011-08-05** | **2012-01-09** | Tropical storms, monsoonal rain | 790 | 2 |
| 3889 | 2012-01-01 | 2012-01-09 | Torrential rain | 0 | 1 |

Other Thai events in the file include 2006 (DFO 2951), 2010 (3737), 2013 (4092) and Dec 2016–Feb 2017 in the South (4432). That the GEE image for DFO 3850 has usable cloud-free coverage of the Chao Phraya basin has **not** been checked: it needs a GEE account, which waits for CP3.

**GISTDA.** www.gistda.or.th and flood.gistda.or.th did not respond on 2026-11-02; disaster.gistda.or.th responded but renders by JavaScript. data.go.th lists GISTDA flood datasets (CKAN API search, 2026-11-02):

- `disasters-01` *ข้อมูลพื้นที่น้ำท่วมซ้ำซาก* (*recurrent flood areas*): "ชั้นข้อมูลพื้นที่น้ำท่วมซ้ำซากในรอบ 13 ปี (2011-2023)" (*recurrent-flood layer over 13 years, 2011–2023*); API by point or geometry; licence "Open Data Common".
- `disasters-03` *ข้อมูลขอบเขตพื้นที่น้ำท่วม* (*flood extent*, last 1 day); API; "Open Data Common".
- `flood-disaster-data` *[Disaster Platform] ข้อมูลภัยพิบัติน้ำท่วม*: STAC API of 1-, 3-, 7- and 30-day flood composites; "License not specified".
- Access condition for all: "สมัครใช้งานเพื่อสร้าง API Key ได้ที่ https://api-gateway.gistda.or.th/v2" (*register to create an API key*). Registration waits for CP3. (Some data.go.th resource URLs embed a key; it was not used.)

No GISTDA bulk download of the 2011 flood extent was found. Whether the annual flood-extent archive (2011 onward) can be obtained as files, and under which terms, could not be verified.

**Assessment.** GFD: **yes**, gives a public 2011 flood-extent measure for the chapter, under a non-commercial licence that fits academic research. GISTDA recurrence 2011–2023: partly; valuable for a hazard-frequency measure but registration-gated.

## 5. Listed Thai banks' public disclosures

Three large banks were targeted, using FY2025 documents. Kasikornbank's website refused most automated requests and Bangkok Bank's timed out; neither was circumvented. Page references are PDF page / printed page.

**SCB X / Siam Commercial Bank (checked in full for Pillar 3 and the climate report).**

- *Pillar 3 Disclosure December 2025* (SCB and SCBX Financial Group, as at 31 Dec 2025): <https://investor.scbx.com/storage/document/basel-iii-pillar-3-market-disclosures/2025/pillar-3-disclosure-dec-25-en.pdf>.
  - **Staging by sector: yes.** Table 13 "Loans by Type of Business and Asset Classification" (p. 56/51), bank-only and consolidated, 31 Dec 2025 and 31 Dec 2024, by Stage 1/2/3. Sectors: agriculture and mining; manufacturing and commercial; real estate and construction; utilities and services; **housing loans**; others. Example (bank-only, 31 Dec 2025, THB m): housing loans S1 561,826, S2 39,237, S3 24,648 (checked in the PDF text).
  - ECL by the same categories: Table 14 (p. 57/52), with general provisions shown as one total.
  - **Staging by geography: Thailand vs foreign countries only.** Table 11 (p. 54/49) and ECL in Table 12 (p. 55/50). No province or region split.
  - Collateral: Table 18 (p. 62/57) covers eligible financial collateral and guarantees by Basel asset class. There is no mortgage LTV distribution, no collateral value and no regional split. LTV appears only as an LGD-model input (Section 6.4, p. 45/40).
  - Climate: Section 5.4.3 (pp. 36–37/31–32) is qualitative.
- *SCBX Climate Report 2025* (TCFD-aligned, calendar 2025): <https://www.scbx.com/wp-content/uploads/2026/07/SCBX-Climate-Report-2025.pdf>.
  - p. 15: a sector heat map with percentages (e.g. hospitality 15%, "Medium-high" physical risk). The denominator is not stated.
  - pp. 15–17: "SCBX is currently conducting physical risk stress testing", using WRI Aqueduct flood maps (RCP 4.5 and 8.5; 2030, 2050, 2080). It covers the mortgage book (collateral-value loss feeding stressed LGD and ECL) and hospitality and power loans, and builds on SCB's participation in a 2024 BOT climate stress test.
  - **No loss, ECL or flood-exposure numbers are published.**
- The FY2025 56-1 One Report and audited notes were not located on investor.scbx.com; the SEC Thailand filing index lists the 2025 Form 56-1 as received on 9 Mar 2026 (not opened).

**Kasikornbank (partly checked).** *Management Discussion and Analysis, for the year ending December 31, 2025*: <https://www.kasikornbank.com/en/IR/FinanInfoReports/financialReports/4Q25_MDxA_En.pdf>.

- Consolidated stage totals and ECL only (p. 51/47; e.g. Stage 3 loans 91,950, ECL 45,023, THB m). No sector, regional or product split; p. 14 points to the Pillar 3 section of the website.
- Physical risk is qualitative (pp. 24–30): the bank "created hazard heat maps identifying locations exposed to various types of disaster risks under multiple climate change scenarios" (p. 30). No figures.
- Not opened: the Pillar 3 report (listing page needs JavaScript), the One Report and audited notes, and the 2025 sustainability report (<https://www.kasikornbank.com/en/sustainable-development/SDAnnualReports/y2025-sd-en.pdf>; download refused).

**Bangkok Bank (not checked).** The site timed out. Candidate documents: Sustainability Report 2025 (<https://www.bangkokbank.com/-/media/files/investor-relations/sustainability-report/2025/sr2025_en.pdf>) and the AGM 2026 One Report summary (<https://www.bangkokbank.com/-/media/files/investor-relations/agm/2026/agm2026_summaryonerport-en.pdf>).

**Assessment.** Partly usable. Pillar 3 reports give bank-year staging and ECL by broad sector, including housing loans, but geography is only "Thailand vs abroad". Climate reports describe flood stress-testing methods but publish no exposures or losses. Bank disclosures can motivate the chapter and support a descriptive bank-level panel. They cannot identify flood effects on collateral or credit by area. Search results also showed a World Bank blog figure on the share of Thai corporate lending in high river-flood-risk districts. It was not opened, so it is not used here.

## 6. BOT climate Standard Practice

**Document.** แนวนโยบายธนาคารแห่งประเทศไทย เรื่อง การดำเนินธุรกิจสถาบันการเงินโดยคำนึงถึงมิติด้านสิ่งแวดล้อมและการเปลี่ยนแปลงสภาพภูมิอากาศ (*BOT policy statement on conducting financial institution business with regard to environmental and climate change dimensions*). Landing page <https://www.bot.or.th/th/financial-innovation/sustainable-finance/green/FIPCS-internalizing_environmental_and_climate_change.html>; PDF (16 pages, Thai) <https://www.bot.or.th/content/dam/bot/financial-innovation/sustainable-finance/green/Policy-20230215-Internalizing_Environmental_and_Climate_Change_Aspects_into_Financial_Institution_Business_TH.pdf>. Opened 2026-11-02.

**Issuance date.** **15 February 2023** (15 กุมภาพันธ์ 2566): cover page (PDF p. 3), document code ฝกสว00-สล00001-25660215 "วันที่ 15 ก.พ. 2566", and the Q&A annex "ลงวันที่ 15 กุมภาพันธ์ 2566". The landing page gives the circular number **ธปท.ฝกส.(01)ว.113/2566**. Issued by ฝ่ายกลยุทธ์สถาบันการเงิน, สายนโยบายสถาบันการเงิน (*Financial Institutions Strategy Department, Financial Institutions Policy Group*). The listing date in the feasibility memo is therefore confirmed.

**Physical risk.** The policy defines environmental risk as physical risk and transition risk, giving floods as an example of acute physical risk: "เช่น ไฟป่า น้ำท่วม หรือพายุ ซึ่งเป็นความเสี่ยงจากผลกระทบทางกายภาพรูปแบบฉับพลัน (Acute physical risk)" (*e.g. wildfire, flood or storm, which are acute physical risks*; footnote 3, PDF p. 5).

**Scenario analysis and stress testing.** Risk-management item (2.3) (PDF p. 10, printed p. 7) says institutions *should* "ประเมินและทบทวนความเสี่ยงด้านสิ่งแวดล้อมและผลกระทบที่อาจมีต่อความเสี่ยงทางการเงิน ในลักษณะ Forward-looking ทั้งเชิงปริมาณและเชิงคุณภาพ … เช่น พิจารณาปัจจัยด้านสิ่งแวดล้อมในการกำหนดสถานการณ์จำลองและการทดสอบภาวะวิกฤติ (Scenario analysis and stress testing) และนำผลที่ได้ไปใช้เป็นส่วนหนึ่งของการวางแผนธุรกิจ การบริหารความเสี่ยง การประเมินความเพียงพอของฐานะเงินกองทุน และการรายงานฐานะการดำเนินงาน" (*assess and review environmental risks and their possible effect on financial risks in a forward-looking manner, quantitatively and qualitatively … for example, consider environmental factors when designing scenario analysis and stress tests, and use the results in business planning, risk management, capital adequacy assessment and reporting*). Footnote 8: where impacts or risks are material, institutions should follow the BOT notification on supervisory review (Pillar 2). It gives scenario analysis as an example ("เช่น"), not as a stand-alone mandatory stress test, and sets no scenario, horizon or frequency.

**Collateral.** Item (3.2) (PDF pp. 10–11) gives, as an example of additional controls for high-risk customers, "การผนวกความเสี่ยงด้านสิ่งแวดล้อมเป็นส่วนหนึ่งในการกำหนดอัตราดอกเบี้ยหรือประเมินมูลค่าหลักประกัน" (*incorporating environmental risk into interest-rate setting or collateral valuation*). This links directly to the chapter's question.

**Disclosure.** The disclosure section refers to TCFD and ISSB standards (PDF p. 12).

**Timelines.** Q&A item 1 (PDF p. 15): "ธปท. จะเริ่มประเมินความคืบหน้าการดำเนินการตามแนวนโยบายฉบับนี้ ตั้งแต่ปี 2567 เป็นต้นไป … ในช่วงแรกจะให้สถาบันการเงินประเมินความคืบหน้าการดำเนินการด้วยตนเอง (Self-Assessment) ก่อน" (*BOT will start assessing progress from 2024, initially through self-assessment by institutions*), and BOT will develop an Industry Handbook with banks "ในครึ่งแรกของปี 2566" (*in the first half of 2023*). The handbook was in fact published on 14 Dec 2023 ([BOT page](https://www.bot.or.th/th/financial-innovation/sustainable-finance/green/Standard_Practice-Industry_Handbook.html)). No date for a supervisory physical-risk stress test appears in the policy text.

**Sourcing note.** Everything above comes from the public PDF and landing page.

---

## Could not verify

1. Whether earlier Treasury appraisal rounds (2016–2019, 2020–2022) are available in any public, bulk form. None is on the open-data catalogue; the Treasury may hold them on request (not asked).
2. The unit of `EVAPRICE` and the exact decoding of the `UTMMAP1–4` map-sheet fields. Both are needed before geocoding at sheet level.
3. The official announcement and publication format of the 2027–2030 appraisal round (press reports only).
4. Search options, terms and access controls of assessprice.treasury.go.th (JavaScript page).
5. REIC: base periods, start years and any zone-level data of its land and housing indices; prices and terms of paid products.
6. BOT FI_CB_011_S3 coverage (2012); start dates of XLS_CB_004 (district) and FI_CB_087 (sector by province); the BOT download link for XLS_CB_004; the BOT API terms text.
7. Whether the GEE image for DFO 3850 has usable coverage of the Chao Phraya floodplain (needs a GEE account, CP3).
8. GISTDA's historical flood-extent archive (2011 onward): file availability, format and licence; www.gistda.or.th and flood.gistda.or.th were unreachable on 2026-11-02.
9. Bank disclosures: Bangkok Bank (all documents; site timed out); Kasikornbank Pillar 3, One Report, audited notes and sustainability report (automated access refused); SCB FY2025 One Report and audited notes (not located), the Pillar 3 publication date, and the denominator of the climate-report heat-map percentages. The audited notes might break down ECL further; this is unchecked.
10. A World Bank blog figure on the share of Thai corporate lending in high river-flood-risk districts (seen only in a search result).

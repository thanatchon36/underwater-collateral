# Loan classification rules (2011) and Thai price indices for a valuation-smoothing check

Date: 2026-11-02. Public sources only, no logins. PDFs were saved under the session scratchpad (`q_class/`) and parsed with `pypdf` run as `python -I`. Anything not read directly is marked [UNVERIFIED].

---

## Q1. BOT loan classification and provisioning rule in force in 2011

### 1.1 Which notification was in force

- **Confirmed:** ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 31/2551 เรื่อง หลักเกณฑ์การจัดชั้นและการกันเงินสำรองของสถาบันการเงิน, dated 3 August 2008 (B.E. 2551). Source: clause 3, "Repealed Notification", of the notification that replaced it, BOT Notification FPG. 5/2559 (12 October 2016). English unofficial translation, PDF p. 2:
  > "3. Repealed Notification — Notification of the Bank of Thailand No. FPG. 31/2551 Re: Regulations on Asset Classification and Provisioning of Financial Institutions dated 3 August 2008"

  URL: https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2559/EngPDF/25590128.pdf
- So สนส. 31/2551 was in force from August 2008 until 5/2559 replaced it in October 2016. That window covers the 2011 floods.
- **What I could not find:** the text of สนส. 31/2551 itself, in Thai or English, on bot.or.th. I tried several searches and a few neighbouring `FPG/2551` file numbers (25510320 to 25510322 returned 404). The rule may have been removed from the site after it was repealed.
- **Amendments between 2008 and 2011:** [UNVERIFIED]. I did not check whether any were issued.
- **Later succession, for context:** 5/2559 (2016) was replaced by สนส. 23/2561, the notification listed in the current BOT index under section (3.1.2)(1). Source: https://www.bot.or.th/content/dam/bot/fipcs/Index-of-BOT-Announcements-in-Fl-group_upload.pdf, PDF p. 9.

### 1.2 Days-past-due thresholds

**Caveat:** I could not read the text of 31/2551. The thresholds below come from its direct successor, **FPG. 5/2559**, clause 5.2.2. The 5/2559 rationale (clause 1, Eng PDF p. 1) describes the 2016 change as adding new types of collateral (business collateral under the Business Security Act 2558, and non-contractual claims). It does not mention changing the overdue periods. It is therefore likely, but [UNVERIFIED], that 31/2551 used the same ladder. The 2011 circular gives one contemporaneous cross-check (section 1.4): in 2011, Pass and Special Mention debtors were those "ค้างชำระดอกเบี้ยไม่เกิน 3 เดือน", which fits a 3-month Substandard threshold.

**Sources**
- Thai official text (scanned; I read it from page images): https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2559/ThaiPDF/25590128.pdf. Printed page "- 5 -" is PDF p. 6; printed page "- 6 -" is PDF p. 7.
- English unofficial translation: the EngPDF link above.

| Class | Overdue threshold (cumulative, principal or interest) | Clause in 5/2559 | Where read |
|---|---|---|---|
| สงสัยจะสูญ (Doubtful of Loss) | > 12 months | 5.2.2 (2)(2.1) | Eng PDF p. 4 (Thai page not read) |
| สงสัย (Doubtful) | > 6 months | 5.2.2 (3)(3.1) | Eng PDF p. 5 (Thai page not read) |
| ต่ำกว่ามาตรฐาน (Substandard) | > 3 months | 5.2.2 (4)(4.1) | Thai PDF p. 6; Eng PDF p. 6 |
| กล่าวถึงเป็นพิเศษ / ควรระวังเป็นพิเศษ (Special Mention) | > 1 month | 5.2.2 (5)(5.1) | Thai PDF p. 7; Eng PDF p. 7 |
| ปกติ (Pass) | not in default; residual class | 5.2.2 (6)(6.1)-(6.4) | Thai PDF p. 7 |

There is also a sixth class, **สูญ (Loss)**, clause 5.2.2 (1). It has no overdue threshold. It covers claims that cannot be collected, such as a dead or disappeared debtor with no assets, or a court ruling with no assets to satisfy it.

**Thai quotes (read from the scanned page images)**

- Substandard, clause 5.2.2 (4.1), Thai PDF p. 6 (printed "- 5 -"):
  > "(4) สินทรัพย์จัดชั้นต่ำกว่ามาตรฐาน หมายถึง สินทรัพย์ที่เข้าลักษณะตามข้อใดข้อหนึ่งดังต่อไปนี้ (4.1) ลูกหนี้ที่ค้างชำระต้นเงินหรือดอกเบี้ยเป็นระยะเวลารวมกันเกินกว่า 3 เดือน นับแต่วันถึงกำหนดชำระ ไม่ว่าจะเป็นไปตามเงื่อนไขหรือเงื่อนเวลาตามสัญญา หรือวันที่สถาบันการเงินทวงถามหรือเรียกให้ชำระคืน แล้วแต่วันใดจะถึงก่อน ยกเว้นลูกหนี้ที่จัดชั้นสูญ สงสัยจะสูญหรือสงสัยแล้ว ..."

  Translation: "(4) Substandard assets are assets with any one of the following attributes: (4.1) a debtor whose principal or interest is overdue for a cumulative period of more than 3 months from the due date, whether the due date comes from the contract's conditions or terms or from the date the institution demands repayment, whichever comes first, except debtors already classified as Loss, Doubtful of Loss or Doubtful ..."

- Special Mention, clause 5.2.2 (5.1), Thai PDF p. 7 (printed "- 6 -"):
  > "(5.1) ลูกหนี้ที่ค้างชำระต้นเงินหรือดอกเบี้ยเป็นระยะเวลารวมกันเกินกว่า 1 เดือนนับแต่วันถึงกำหนดชำระ ... ยกเว้นลูกหนี้ที่จัดชั้นสูญ สงสัยจะสูญ สงสัย หรือต่ำกว่ามาตรฐาน ..."

  Translation: "(5.1) a debtor whose principal or interest is overdue for a cumulative period of more than 1 month from the due date ... except debtors classified as Loss, Doubtful of Loss, Doubtful or Substandard ..."

- Pass, clause 5.2.2 (6), Thai PDF p. 7:
  > "(6) สินทรัพย์จัดชั้นปกติ หมายถึง สินทรัพย์ที่เข้าลักษณะตามข้อใดข้อหนึ่งดังต่อไปนี้ (6.1) ลูกหนี้ที่ไม่ผิดนัดชำระ ... (6.3) ลูกหนี้อื่นที่ไม่เข้าข่ายเป็นลูกหนี้จัดชั้นสูญ สงสัยจะสูญ สงสัย ต่ำกว่ามาตรฐาน หรือกล่าวถึงเป็นพิเศษ (หรือควรระวังเป็นพิเศษ)"

  Translation: "(6) Pass assets are assets with any one of the following attributes: (6.1) a debtor not in default ... (6.3) any other debtor that does not fall under Loss, Doubtful of Loss, Doubtful, Substandard or Special Mention (Requiring Special Caution)."

**English quotes (translation PDF)**

- Doubtful of Loss, clause (2.1), Eng PDF p. 4:
  > "A debtor overdue the principal or interest payments for a cumulative period exceeding 12 months starting from the contractual due date ..."
- Doubtful, clause (3.1), Eng PDF p. 5: same wording with "exceeding 6 months".

Each class also has a parallel overdraft clause, (x.2), with the same 1, 3, 6 or 12-month periods. For overdrafts the clock starts when the credit line is revoked, when the balance exceeds the line, or at contract maturity, whichever is earliest.

### 1.3 Mechanical overdue periods or qualitative judgement too?

**Both.** The classes are defined disjunctively ("ข้อใดข้อหนึ่ง", any one of the listed attributes). Overdue days set a floor: a loan cannot sit in a better class than its overdue period implies. Qualitative triggers can push a loan into a worse class earlier. Under 5/2559:

- **Doubtful:**
  - (3.3) the debtor is under a court receivership order;
  - (3.4) the debtor has ceased or dissolved its business, or is in liquidation;
  - (3.5) the debtor is evading repayment, for example by moving abroad or disposing of assets;
  - (3.6) the institution cannot contact or find the debtor;
  - (3.7) the debtor's business is uncertain, or funds were used for a purpose other than the one agreed;
  - (3.9) full repayment is unlikely;
  - (3.10) the BOT orders it.
- **Substandard:** (4.3), indicators of collection difficulty, as ordered by the BOT (Thai PDF p. 7).
- **Doubtful of Loss:** (2.5) to (2.7).
- **Reclassification power:** clause 5.2.2 says the BOT "may require financial institutions to reclassify assets as considered appropriate" (Eng PDF p. 3).
- **Upgrades are not mechanical either.** Under the 2011 circular's Q&A (section 1.4), a Special Mention debtor can return to Pass only after 3 consecutive months or 3 installments of performance.

All of this describes 5/2559. Whether 31/2551 had identical qualitative clauses is [UNVERIFIED].

### 1.4 Does circular ฝนส. (23) ว. 1564/2554 (`bot2011circular1564`) refer to it?

**Yes, by title only, without the number.** In the Q&A attachment, items 2 and 3 are on PDF p. 9 and item 6 is on PDF p. 10. Source: https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2554/ThaiPDF/25540206.pdf

- Q3, PDF p. 9:
  > "สถาบันการเงินยังคงต้องติดตามผลการปฏิบัติตามสัญญาของลูกหนี้ติดต่อกันไม่น้อยกว่า 3 เดือนหรือ 3 งวดการชำระเงิน ในการปรับชั้นลูกหนี้จากชั้นกล่าวถึงเป็นพิเศษเป็นลูกหนี้จัดชั้นปกติตามประกาศธนาคารแห่งประเทศไทย เรื่อง หลักเกณฑ์การจัดชั้นและการกันเงินสำรองของสถาบันการเงิน"

  Translation: "Financial institutions must still monitor the debtor's contractual performance for no less than 3 consecutive months or 3 payment installments before upgrading a debtor from Special Mention to Pass under the BOT Notification Re: Regulations on Asset Classification and Provisioning of Financial Institutions."
- Q2, PDF p. 9: the question refers to Pass and Special Mention debtors that are "ค้างชำระดอกเบี้ยไม่เกิน 3 เดือน" ("interest overdue no more than 3 months"). The answer allows accrual-basis income recognition for them under the flood measures.
- Q1, PDF p. 9: the measures let institutions "คงสถานะการจัดชั้นลูกหนี้เช่นเดิม" (keep a debtor's pre-flood classification). There is no BOT cut-off date, but institutions may use 25 July 2011 as a guide.
- Q6, PDF p. 10: reviews of the measures are allowed until 31 Dec 2012, but "จะต้องไม่เป็นการหลีกเลี่ยงการจัดชั้นและการกันเงินสำรอง" ("must not be a way to avoid classification and provisioning").

Inference, not stated in the circular: in October 2011 the notification "เรื่อง หลักเกณฑ์การจัดชั้นและการกันเงินสำรองของสถาบันการเงิน" can only be สนส. 31/2551. Suggested citation wording: "BOT Notification สนส. 31/2551 (3 Aug 2008), as identified in clause 3 of FPG. 5/2559".

---

## Q2. Public Thai price indices for comparison with official land values

### 2.1 Bank of Thailand: ดัชนีราคาที่อยู่อาศัยและดัชนีราคาที่ดิน (Residential and land price indices)

- **Table:** EC_EI_008_S3 "ดัชนีราคาที่อยู่อาศัยและดัชนีราคาที่ดิน".
- **URL:** https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?reportID=920&language=th
- **How I read it:** with a WebFetch extraction (a model summary of the page), not a manual read. The page showed data last updated 28 Feb 2025. **Re-check this by eye before citing.**

**Series** (the page gives Thai names only; the English names are my translations):

| Thai series | English | Geography |
|---|---|---|
| ดัชนีราคาบ้านเดี่ยวพร้อมที่ดิน | Single-detached house with land | ทั้งประเทศ (whole kingdom); กรุงเทพฯ และปริมณฑล (Bangkok and vicinity); ภูมิภาคไม่รวมกรุงเทพฯ และปริมณฑล (regions excluding Bangkok and vicinity) |
| ดัชนีราคาทาวน์เฮ้าส์พร้อมที่ดิน | Townhouse with land | the same three areas |
| ดัชนีราคาอาคารชุด | Condominium | Bangkok and vicinity only |
| **ดัชนีราคาที่ดิน** | **Land price index** | **Bangkok and vicinity only** |

**Methodology, base, frequency and coverage**
- **Base:** 2554 (2011) = 100.
- **Coverage shown:** Jan 2011 to Dec 2024.
- **Frequency:** monthly, quarterly, half-yearly and annual. The quarterly value is the last month of the quarter.
- **House and condo indices:** hedonic regression with a rolling window and time dummies, as a 3-month moving average. Data come from residential-collateral loans at commercial banks and GHB.
- **Land index:** "คำนวณด้วยวิธี Stratification โดย Monthly weight (เฉลี่ยเคลื่อนที่ 3 เดือน) ... จากฐานข้อมูลสินเชื่อที่มีที่อยู่อาศัยเป็นหลักประกันของธนาคารพาณิชย์เท่านั้น". It uses commercial-bank residential-collateral data only.
- **Breakdown:** no province-level series was seen.

**Methodology note, read 2026-11-02 (full text, PDF pp. 2–7)**
- Source: การปรับปรุงดัชนีราคาที่อยู่อาศัยของประเทศไทย (The Improvement of Thailand's RPPI), BOT Stat Horizon, https://www.bot.or.th/content/dam/bot/documents/th/research-and-publications-pdf/statistical-articles/stat-horizon/StatHorizon_NRPPI.pdf.
- **Start date and revisions, PDF p. 4.** "ธปท. เริ่มจัดทำดัชนีราคาที่อยู่อาศัยโดยใช้ข้อมูลสินเชื่อที่มีที่อยู่อาศัยเป็นหลักประกันจากธนาคารพาณิชย์มาตั้งแต่ปี 2554 และได้ปรับปรุงมาแล้ว 2 ครั้งในปี 2558 และ 2564". So the series starts in 2011, with revisions in 2015 and 2021. The note mentions no pre-2011 series.
- **Method, PDF pp. 4 and 7.** Hedonic regression, rolling window with time dummies. The dependent variable is ln(P), "ราคาที่อยู่อาศัย", with land area, usable area, distance to the nearest point of interest, storeys and building age as controls.
- **Data source, PDF pp. 4 and 6.** The mortgage-collateral database (MGL) of commercial banks plus one SFI. All SFIs are added from January 2023 data.
- **Coverage, PDF p. 7.** The data cover 55% of residential ownership transfers in 2021–2023 before adding the SFIs, and 61% after.
- **Revised series, PDF p. 2.** Published from January 2025 data (B.E. 2568). It adds regional indices for BKK, Central, North, Northeast and South, and an all-types index.
- **What P measures.** The note does not define P as appraised value in so many words. However, its Figures 1–2 (PDF p. 6) weight the database by "มูลค่าราคาประเมินรวม" (total appraised value), so P is most likely the lender's collateral appraisal. This is an inference, not a quoted definition.
- **Implication.** The BOT index is a coarse, regional-level read of bank collateral values (λ_B), not of market transaction prices. That makes it the only public check on whether bank appraisals in flooded regions moved with Treasury values. It cannot identify flood effects at sheet level.
- **Land index.** This note does not discuss the land index. Its stratification method remains as read from the table page above.

**Successor table, read 2026-11-02 (raw CSV saved)**
- **EC_EI_008_S4** "ดัชนีราคาที่อยู่อาศัย" (reportID 993) runs January 2011 to September 2026 and was updated 31 Oct 2026. Base 2011 = 100.
  - All-types index for the whole kingdom, Bangkok and vicinity, Central, North, Northeast and South.
  - Detached houses for the same six areas.
  - Townhouses for the whole kingdom, Bangkok and vicinity, Central and South.
  - Condominiums for Bangkok and vicinity only.
  - The regional split **is** back-cast to January 2011.
  - There is no land index. The land index stays in S3, which is frozen at December 2024.
- **Appraisal, confirmed.** The BOT conference slides (bib `bot2026rppislides`, p. 3) say: "the BOT adopted appraisal price from the Mortgage Loan Data (MGL) for constructing the RPPI". The regional indices use representative provinces (pp. 8–9).
- **Where it is used.** Descriptive windows are in `06_proposal/notes/04_methods.md` ("Coarse λ_B check").

**Access**
- The page has a "ดาวน์โหลด" (download) button, and the extraction showed no login prompt.
- I did not test the actual file download, and I did not read the BOT terms of use. [UNVERIFIED]

### 2.2 REIC (ศูนย์ข้อมูลอสังหาริมทรัพย์, under GHB): ดัชนีราคาที่ดินเปล่าก่อนการพัฒนา กรุงเทพฯ-ปริมณฑล

- **English name:** usually "Undeveloped Vacant Land Price Index". The English name appears in a REIC PDF filename; the press release itself has no English name.
- **URL:** https://reic.or.th/Activities/PressRelease/246 (press release dated 21 Nov 2024, Q3 2024). Read with a WebFetch extraction.
- **Coverage:** six provinces: กรุงเทพ นนทบุรี ปทุมธานี สมุทรปราการ สมุทรสาคร นครปฐม.
- **Scope:** vacant land "ไม่รวมสิ่งปลูกสร้าง ที่มีขนาดที่ดินตั้งแต่ 200 ตารางวาขึ้นไป" (excluding structures, plots of 200 sq. wah or more).
- **Frequency:** quarterly, judging from the release pattern. Releases also report zone-level changes, for example Phra Khanong–Bang Na.
- **Not stated on the page:** base year, start date, and sampling method (whether it is built from listings or surveys). All [UNVERIFIED].
- **Access:** press-release PDFs are linked for download from public pages. I did not read the site's "เงื่อนไขและข้อตกลง" (terms and conditions), and whether the full index time series is free is [UNVERIFIED].
- **Other REIC housing series:** a series such as ดัชนีราคาบ้านจัดสรรที่อยู่ระหว่างการขาย (price index of new housing for sale, Bangkok and vicinity) exists, per a search-result title: https://www.reic.or.th/Activities/PressRelease/220. I did not open it; coverage and access are [UNVERIFIED].

### 2.3 Implications for the valuation-smoothing chapter

- **Land-only comparison:** only the BOT land price index from 2011 and the REIC vacant-land index are land-only. Both cover only Bangkok and vicinity, so a land-on-land smoothing test is limited to Bangkok and vicinity provinces.
- **Outside Bangkok:** the only regional benchmark is the BOT house and townhouse "with land" indices. These bundle structure and land and have no province breakdown. The revised series, published from January 2025 data, splits the regions into Central, North, Northeast and South [@bot2025rppi, p. 2]. The flooded 2011 provinces (Central) and 2025 provinces (South) therefore each sit in one regional index. That supports a coarse λ_B check of a region and period, not a sheet-level test. Whether the regional split is back-cast to 2011 is [UNVERIFIED] until the table is downloaded.
- **Source differences:**
  - The BOT indices are built from bank collateral data, which is itself appraisal-based. They may be smoothed too, so a test against them compares one appraisal source with another.
  - The REIC index tracks large undeveloped plots, of 200 sq. wah or more.
  - The method difference (appraisal-based versus a land-market index) should be stated explicitly.

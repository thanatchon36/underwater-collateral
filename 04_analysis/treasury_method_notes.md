# Treasury land appraisal method: notes for RQ1

Working draft, Phase 5. All facts as of 2026-11-02 unless stated otherwise. Each answer cites a primary source with a locator. Press reports appear only where no primary source was found, and they are labelled **secondary**. Downloaded PDFs are in the session scratchpad (`pdfs/treasury/`), not in the repository.

## Sources used

| Key | Document (Thai title, English translation) | Publisher / locator | URL |
|---|---|---|---|
| **ACT** | พระราชบัญญัติการประเมินราคาทรัพย์สินเพื่อประโยชน์แห่งรัฐ พ.ศ. ๒๕๖๒ (*Property Valuation for the Public Interest Act, B.E. 2562 (2019)*) | Royal Gazette Vol. 136, Part 68 Kor, 25 May 2019 (Thai text, 13 pp.); Council of State English translation (12 pp.) | Thai: <https://www.treasury.go.th/medias/treasury-intranet/1/post/laws_regulations-80/live/77_1768470668_45efd8473fb2b2907e66c0575a1be045.pdf>; English: <https://www.treasury.go.th/medias/treasury-intranet/1/post/laws_regulations-80/live/77_1768470666_5e20c6f57bb59b7bbf4be4acf5ea18a2.pdf> |
| **MR** | กฎกระทรวงการกำหนดราคาประเมินที่ดินหรือสิ่งปลูกสร้าง การจัดทำบัญชีราคาประเมินที่ดินหรือสิ่งปลูกสร้าง และแผนที่ประกอบการประเมินราคาที่ดิน พ.ศ. 2563 (*Ministerial Regulation on determining land and building appraisal values, preparing appraisal schedules and appraisal maps, B.E. 2563 (2020)*) | Royal Gazette Vol. 137, Part 101 Kor, 9 December 2020, pp. 1–8; signed 30 November 2020 | <https://www.treasury.go.th/medias/treasury-intranet/1/post/laws_regulations-80/live/77_1768471785_2dbeb6a65c9d48814767427cc89c5715.pdf> (listed in force on <https://www.treasury.go.th/th/laws-and-regulations-act/property-appraisal>) |
| **GUIDE** | แนวทางการใช้บัญชีราคาประเมินที่ดิน (*Guidelines for using the land appraisal schedule*) | กรมธนารักษ์ (Treasury Department), cover page; 35 PDF pages, undated; refers to a 2024 (B.E. 2567) DOL–Treasury agreement, so issued in or after 2024 | <https://talad.go.th/fileupload/641047.pdf> (hosted by a local-government site, not by treasury.go.th; see "Could not verify") |
| **FPO** | รู้จักกับ ... "ราคาประเมินทรัพย์สิน" (*Getting to know official property appraisal values*), FPO KM series | Fiscal Policy Office (สำนักงานเศรษฐกิจการคลัง), Tax Policy Division; 1 page, undated | <https://www.fpo.go.th/main/getattachment/General-information-public-service/FPO-KM/17337/6-%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B8%AA%E0%B8%B9%E0%B9%88%E0%B8%84%E0%B8%99%E0%B8%84%E0%B8%A5%E0%B8%B1%E0%B8%87-%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%A1%E0%B8%B4%E0%B8%99%E0%B8%97%E0%B8%B8%E0%B8%99%E0%B8%97%E0%B8%A3%E0%B8%B1%E0%B8%9E%E0%B8%A2%E0%B9%8C.pdf.aspx> |
| **META** | ราคาประเมินที่ดิน (*Land appraisal values*), dataset `land-valuation` | data.go.th CKAN API `package_search`, read 2026-11-02 | <https://data.go.th/dataset/land-valuation> |
| **BOT19** | แนวนโยบาย เรื่อง การประเมินราคาหลักประกันและอสังหาริมทรัพย์รอการขาย … (*Policy on appraisal of collateral and foreclosed real estate*), circular ฝนส.(23)ว.575/2562 | Bank of Thailand, 8 May 2019 | <https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2562/ThaiPDF/25620100.pdf> |
| **LTV18** | คำถาม-คำตอบแนบท้ายประกาศ ธปท. ที่ สนส. 24/2561 เรื่อง หลักเกณฑ์การกำกับดูแลสินเชื่อเพื่อที่อยู่อาศัย… (*Q&A annexed to BOT Notification SorNorSor 24/2561 on the regulation of housing loans*) | Bank of Thailand, 2018 | <https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2561/ThaiPDF/25610271.pdf> |
| **DOL** | ค่าธรรมเนียม ภาษี และอากร (*Fees, taxes and duties*), public service manual | Department of Lands | <https://www.dol.go.th/dol-services/public-service-manual/land-registration/fees-taxes-duties/> |

---

## 1. Method

### 1a. How values are set: per land unit, then per parcel

**Answer.** Values are set in two stages. The provincial committee first prices **land units** (หน่วยที่ดิน), which are mostly road, soi or waterway frontage segments. Each parcel's value is then derived from its unit price with **depth and shape adjustment factors**, and the result is rounded to a fixed grid. Confidence: **high** for the two-stage structure (MR); **medium-high** for the exact factor tables (GUIDE).

- **Who sets values.** A provincial committee (คณะกรรมการประเมินราคาทรัพย์สินเพื่อประโยชน์แห่งรัฐประจำจังหวัด, *Provincial Property Valuation Committee*) determines values and schedules under criteria set by ministerial regulation (ACT s. 18; EN p. 6).
- **Land unit (definition).** "หน่วยที่ดิน" is "ที่ดินในบริเวณเดียวกัน ซึ่งประกอบด้วยปัจจัยต่าง ๆ ที่มีผลทำให้ราคาที่ดินนั้นแตกต่างกันน้อยที่สุด ได้แก่ ทางหลวง ถนน ซอย ทะเล แม่น้ำ คลอง หมู่บ้านจัดสรร หรือลักษณะทางกายภาพอื่น ที่ใช้แสดงให้ทราบถึงตำแหน่งที่ตั้งของแปลงที่ดิน". In English: *land in the same area whose price-relevant factors differ least, namely highways, roads, sois, sea, rivers, canals, housing estates or other physical features that locate the parcel* (MR ข้อ 1, Gazette p. 2).
- **Step 1, unit prices.** The committee's report must show "ราคาประเมินที่ดินเป็นรายหน่วยที่ดิน และอัตราร้อยละของการเปลี่ยนแปลง… พร้อมทั้งราคาประเมินที่ดินเฉพาะรายถนนสำคัญ" (*appraisal values by land unit and the percentage change on the previous round, together with values for major roads*) (MR ข้อ 5(4), p. 3).
- **Step 2, parcel values.** "เมื่อคณะกรรมการประจำจังหวัด… เห็นชอบราคาประเมินที่ดินรายหน่วยที่ดินแล้ว ให้นำราคาประเมินที่ดินรายหน่วยที่ดินดังกล่าวมากำหนดราคาประเมินที่ดินแต่ละแปลง". In English: *once the committee approves the per-unit values, they are used to set the value of each parcel* (MR ข้อ 6, p. 3).
- **Scope.** Per-parcel schedules cover only land with a title deed (โฉนดที่ดิน) or an N.S. 3 Kor certificate (MR ข้อ 3, p. 3). Other title types receive one value per land-unit type, by municipality or tambon, set at the lowest unit value of each type in that area (MR ข้อ 10, p. 4; GUIDE PDF p. 3). The open CSV is the per-parcel schedule, keyed by UTM sheet and parcel number; this is the "แบบเรียงเลขที่ดินตามระวางในระบบพิกัดฉาก UTM" format (*listed by parcel number within UTM map sheet*), used for parcels that could not be linked to the land register (GUIDE PDF p. 5, printed p. 3).
- **Factors used to go from unit to parcel.** The guide states that parcel values take account of "ระยะความลึกแปลงที่ดิน รูปแปลงที่ดิน และข้อจำกัดในการเข้าออก" (*parcel depth, parcel shape and access restrictions*) (GUIDE PDF p. 33, printed p. 31). Per-parcel calculation needs "ตำแหน่งที่ตั้งของแปลงที่ดิน ระยะความลึกของแปลงที่ดิน และรูปร่างของแปลงที่ดิน" (*location, depth and shape*), taken from DOL parcel polygons (GUIDE PDF p. 3, printed p. 1).
- **Depth table, 40 m standard depth** (GUIDE PDF p. 21, printed p. 19). The percentage of the unit price falls by depth band:

  | Depth (m) | ≤ 50 | ≤ 90 | ≤ 130 | ≤ 170 | ≤ 210 | ≤ 250 | > 250 |
  |---|---|---|---|---|---|---|---|
  | % of unit price | 100 | 87.5 | 75 | 62.5 | 53.75 | 46.88 | 41.07 |

- **Shape table** (GUIDE PDF p. 22, printed p. 20):

  | Parcel shape or use | % of unit price |
  |---|---|
  | Normal road-front parcel | 100 |
  | Parcel with no access | 100 (but valued at the "other land" unit) |
  | Rhomboid parcel at ≤ 30° to the road | 95 |
  | Triangle, base on the road | 65 |
  | Triangle, apex on the road | 35 |
  | Flag lot, neck > 2 m | 75 |
  | Flag lot, neck < 2 m | 65 |
  | Parcel used as an access road | 50 |

- **Rounding grid** (GUIDE PDF p. 23, printed p. 21). Values are rounded to steps of 5 for tens, 10 for hundreds, 50 for thousands, 500 for tens of thousands, 5,000 for hundreds of thousands and 50,000 for millions.
- **Caveat.** These tables appear in the guide's worked method for land with *other* title types (unit price × depth % × shape %). The guide shows the same three factors for deed parcels (PDF pp. 3 and 33). It does not reprint the tables for deed parcels, so applying identical percentages to deed parcels is an **inference**.
- **Land-unit typology** for land with other title types (GUIDE PDF p. 16, printed p. 14): (1) national highway frontage; (2) rural highway or local road frontage; (3) sea frontage; (4) river frontage; (5) canal frontage; (6) other road, soi or track frontage; (7) all other land, including land with no access. Waterfront land therefore has **its own unit price**.

### 1b. Market evidence

**Answer.** The required method is market comparison (วิธีเปรียบเทียบราคาตลาด). The income method is used only if market data are missing or insufficient. Confidence: **high** (MR).

- **Required method.** "การกำหนดราคาประเมินที่ดิน ให้ใช้วิธีเปรียบเทียบราคาตลาด ในกรณีที่ไม่มีข้อมูลราคาตลาดหรือมีแต่ไม่เพียงพอ… ให้ใช้วิธีรายได้". In English: *land values use the market-comparison method; where market data are absent or insufficient, the income method* (MR ข้อ 4, p. 3).
- **Market data (definition).** "ข้อมูลราคาตลาด" covers "ข้อมูลราคาซื้อขายจดทะเบียน ข้อมูลราคาตามสัญญาจะซื้อจะขาย ข้อมูลเสนอขาย ข้อมูลสอบทาน ข้อมูลค่าเช่า". In English: *registered sale prices, prices in sale-and-purchase agreements, asking prices, verified (survey) data and rents* (MR ข้อ 1, p. 1).
- **Comparison method (definition).** Market data of nearby land, or representative data, "และอาจนำปัจจัยที่สำคัญต่าง ๆ ที่มีผลกระทบต่อราคาที่ดินมาวิเคราะห์" (*and may analyse important factors affecting land prices*) (MR ข้อ 1, p. 1).
- **Field survey.** The committee announces survey areas and periods. It surveys land condition (สำรวจสภาพที่ดิน) and gathers market prices, recording at least (1) location, (2) parcel shape, (3) land use and (4) environment (สภาพแวดล้อม) (MR ข้อ 2, pp. 2–3).
- **Dataset metadata.** The data source is described as "การวิเคราะห์ราคาซื้อขายของตลาดตามหลักวิชาการด้านประเมินราคาทรัพย์สิน" (*analysis of market transaction prices under valuation methodology*) (META field `data_source`).
- **Legal principles.** Valuation must suit each property type and follow "basic principles of property valuation and the economic principles" (ACT s. 6; EN p. 2).

### 1c. Flood, low-lying land or land condition

**Answer.** No rule adjusts for flood hazard, flooding or low-lying land (ที่ลุ่ม) in the Act, the ministerial regulation or the Treasury guide. Confidence: **medium-high**. This is an absence finding in three documents, and committee-level rules were not found (see "Could not verify").

- **Implicit routes only.** Land condition can enter only implicitly:
  - through the survey of "สภาพที่ดิน" and "สภาพแวดล้อม" (MR ข้อ 2);
  - through the factors that "may" be analysed in the comparison method (MR ข้อ 1);
  - through the FPO summary that valuations "อาจนำปัจจัยอื่นๆ มาคำนวณร่วมด้วย เช่น ทำเลที่ตั้ง สิ่งอำนวยความสะดวก สภาพแวดล้อม" (*may include other factors such as location, amenities, environment*) (FPO, p. 1).
- **Explicit physical-condition rules.** The only explicit rules found cover high-voltage lines and ponds (GUIDE PDF p. 33, printed p. 31):
  - The standard parcel factors "ไม่รวมถึง แนวเขตสายไฟฟ้าแรงสูง หรือแปลงที่ดินที่มีการขุดหน้าดินและมีสภาพเป็นบ่อ ลึกจากระดับพื้นดินเกิน 3 เมตร". In English: *exclude land under high-voltage lines and land excavated into a pond more than 3 m below ground level*.
  - These cases are handled by separate provincial committee announcements, following Treasury letter ที่ กค 0311/ว 135 of 10 November 2022.
  - Officials apply the reduction when "เจ้าของที่ดินแจ้ง… ให้เจ้าของที่ดินแสดงหลักฐาน" (*the owner notifies and shows evidence*).
  - Worked examples use 30% of the value for the high-voltage corridor (PDF p. 34) and 25% for the pond area (PDF p. 35).
  - **Implication.** These reductions are applied on request at registration and probably do not appear in the published schedule [inference].

### 1d. Expected within-block variation

**Answer.** Within a land unit, parcel values differ only through the depth, shape and access factors and rounding, so the variation is mechanical. A map sheet usually spans several land units, so variation within a sheet mixes several unit prices with these mechanical factors. Confidence: **high** for the mechanism; **exploratory** for the numbers below.

- **Exploratory check.** Run on 2026-11-02 on the archived snapshot `03_data/raw/treasury_land_appraisal/snapshot_2026-11-02/`, with sheet = UTMMAP1–4 + UTMSCALE and sheets of ≥ 20 parcels. The script is in the session scratchpad (`scripts/within.py`), not yet in `04_analysis/src/`, so these figures must be reproduced in the pipeline before any use in a deliverable.

  | Province | Parcels | Distinct values in province | Median distinct values per sheet | Median share of parcels at the sheet's modal value | Share of log-value variance within sheets |
  |---|---|---|---|---|---|
  | Samut Songkhram | 99,667 | 244 | 14 | 0.36 | 0.33 |
  | Uthai Thani | 154,166 | 228 | 9 | 0.46 | 0.22 |
  | Lamphun | 356,992 | 302 | 7 | 0.49 | 0.26 |

- **Pattern.** Values are highly discrete: a few hundred distinct values per province, consistent with the rounding grid. Roughly one-fifth to one-third of the variance in log values lies within sheets.

## 2. The `EVAPRICE` unit

**Answer.** **Baht per square wah** (บาท/ตารางวา). Confidence: **high**.

- **Primary statement.** A land appraisal schedule must contain "ราคาประเมินที่ดิน โดยกำหนดให้ราคาประเมินมีหน่วยเป็นบาทต่อตารางวา" (*the land appraisal value, expressed in baht per square wah*) (MR ข้อ 7(2), Gazette p. 3).
- **Treasury guide.** The UTM-sheet schedule format, the one matching the CSV columns, lists "ราคาประเมิน (บาท/ตร.ว.)" (GUIDE PDF p. 5, printed p. 3).
- **Fiscal Policy Office.** "ราคาประเมินฯที่ดิน – ประเมินเป็นราคาต่อตารางวา" (FPO, p. 1).
- **Dataset metadata.** The data.go.th entry has no data dictionary (`data_support`: "ไม่มี", *none*), and the CSV does not state the unit (META).
- **Conversion.** 1 square wah = 4 m², so 1 rai = 400 square wah. This is standard; no source was opened for it.

## 3. Rounds and timing

### 3a. Schedule of rounds

| Round | Legal basis | Status and dates | Source strength |
|---|---|---|---|
| 2016–2019 (B.E. 2559–2562) | Land Code schedule (บัญชีกำหนดราคาประเมินทุนทรัพย์ … ตามประมวลกฎหมายที่ดิน) | The start date of 1 Jan 2016 was not checked in a primary source. | **[UNVERIFIED]** for dates |
| 2020–2022 | ACT s. 34 para. 2 (transitional): the Land Code schedule in force before the Act "มาใช้เป็นบัญชีราคาประเมินที่ดินหรือสิ่งปลูกสร้างตามพระราชบัญญัตินี้ไปพลางก่อน" (*is used in the meantime as the schedule under this Act*) until the first schedule under the Act takes effect (Thai PDF p. 11) | In practice the 2016–19 values remained in force for 2020–2022. This was a statutory carry-over, not a new round. | Legal mechanism **high**; the 2020–22 span is consistent with the 1 Jan 2023 start below |
| 2023–2026 (B.E. 2566–2569) | ACT s. 19 | Start date of 1 Jan 2023: the Treasury guide says the provincial announcements were to "ประกาศใช้ในวันที่ 1 มกราคม พ.ศ. 2566" (GUIDE PDF p. 33). Dataset `created_date` is 2023-01-01 (META). The committee notice of November 2021 that fixed this date was seen only in press reports. | **high** for the start date |
| 2027–2030 (B.E. 2570–2573) | ACT s. 19 | Not published as of 2026-11-02. See 3c. | Press only |

- **Mid-round changes.** Values can change within a round in three ways:
  - **Committee revisions.** A provincial committee can amend a schedule within a round, valid only for the rest of the round (ACT s. 20; EN p. 6).
  - **Divergence trigger.** If average sale prices in an area differ from the schedule by **more than 15%**, the committee must re-price that area and issue a new schedule "โดยไม่ต้องรอให้ครบรอบ" (*without waiting for the round to end*) (MR ข้อ 9, p. 4; ACT s. 27(1)).
  - **In-place revisions.** The open CSV files are revised in place: resource `last_modified` dates run to 2026-05-08 (META).

### 3b. Legal basis for the round length

- **Four-year interval.** "ให้คณะกรรมการประจำจังหวัดประกาศบัญชีราคาประเมินที่ดินหรือสิ่งปลูกสร้าง… ทุกรอบสี่ปี โดยต้องประกาศล่วงหน้าก่อนวันเริ่มใช้บัญชีเป็นเวลาไม่น้อยกว่าสามสิบวัน". In English: *every four years, announced at least 30 days before the start date* (ACT s. 19 para. 1; Gazette p. 24).
- **Start date.** Schedules start "ณ วันที่ ๑ มกราคม ของปีที่คณะกรรมการกำหนด" (*on 1 January of the year the central committee sets*) (s. 19 para. 2).
- **Extension.** With central committee approval, a province may extend the current schedule by **up to one year** after its four-year term. The next schedule then runs only for the remainder of its own four-year term (s. 19 para. 3; Thai PDF p. 7).
- **Posting.** The schedule must be posted at the Provincial Treasury Office, Land Office and District Office for at least 60 days from the start date (s. 19 para. 4).
- **Entry into force of the Act.** The Act took effect 180 days after Gazette publication (ACT s. 2; EN p. 1); publication was on 25 May 2019. The first nationwide start date had to be ordered within two years of entry into force (s. 34 para. 1).

### 3c. The 2027 round: publication, effective date and cut-off

- **Effective date.** By law, 1 January of the year the central committee sets (s. 19). If the 2023 round runs a full four years, the next round starts on **1 January 2027**, unless provinces use the one-year extension in s. 19 para. 3.
- **Publication date.** The statutory latest date for a 1 January 2027 start is **2 December 2026**, i.e. at least 30 days before (s. 19 para. 1).
- **Press reports (secondary):**
  - Treasury officials said the round would be announced in December 2026 and used from 1 January 2027 ([Kaohoon](https://www.kaohoon.com/news/local/845642); [InfoQuest](https://www.infoquest.co.th/?p=567390)).
  - Bangkok Biznews reported a planned announcement on 1 December 2026 ([Bangkok Biznews](https://www.bangkokbiznews.com/economics/1242623)).
  - No Treasury or Royal Gazette notice was found as of 2026-11-02.
- **Appraisal reference date (market-data cut-off).** No official statement was found. The MR requires each provincial committee to *announce the survey area and survey period* (ประกาศกำหนดพื้นที่และกำหนดระยะเวลาที่จะดำเนินการสำรวจที่ดิน) (MR ข้อ 2, p. 2). Those provincial notices are the most likely primary source for the data window.
  - The Treasury site lists such notices: for example, a Saraburi notice of 30 October 2026 on the condominium survey area and period, a 44.72 KB PDF at <https://www.treasury.go.th/th/announcement/property-appraisal-announcement/provinces-announcement-20261030-454> (title read; PDF not opened).

### 3d. Public availability of earlier rounds

- **Catalogue.** Only the current round is in the open-data catalogue: 77 province CSVs totalling **1,444,828,939 bytes (≈1.44 GB)**, with Bangkok the largest at 91,819,103 bytes (META resources list).
- **Metadata dates.** The data.go.th record was created 2024-08-20 and last modified 2026-06-25. It was harvested from catalog.treasury.go.th, where the harvest record was created 2023-03-22 (META `extras`).
- **CKAN history.** catalog.treasury.go.th robots.txt disallows `/revision/` and `/dataset/*/history` (`03_data/inventory_R3.md`, item 1), so past file versions were not retrieved.
- **Internet Archive.** The CDX query for archived copies of the CSVs returned no rows on the first attempt and "Temporarily Offline" on the second (2026-11-02). Not resolved.
- **Treasury e-services (not opened):**
  - a certified-copy service: <https://www.treasury.go.th/th/services/land-assessment/appeal-price>;
  - a National Property Valuation Center data-request service: <https://www.treasury.go.th/th/services/land-assessment/request-data-center>.
  - Either may supply past rounds on request. Both would require a request and possibly registration, which waits for CP3.
- **Local snapshot.** The repository already holds a snapshot of the current files dated 2026-11-02 (79 files in `03_data/raw/treasury_land_appraisal/snapshot_2026-11-02/`).

### 3e. Provincial survey notices for the 2027 round (checked 2026-11-02)

**Result: no survey-area or survey-period notice (ประกาศกำหนดพื้นที่และกำหนดระยะเวลาที่จะดำเนินการสำรวจที่ดิน) was found for Chiang Rai or Phayao.** The market-data window for the 2027–2030 (B.E. 2570–2573) schedule in these provinces is therefore **unknown**. It is also unknown whether that window postdates the September 2024 floods. No 2570–2573 schedule was found for either province or nationally.

- **Pages checked.** All are public pages; robots.txt on www, chiangrai and phayao.treasury.go.th is `Disallow:` (empty). Requests were throttled at 2 s, and raw HTML was saved to the session scratchpad, not to the repository.
  - **Chiang Rai.** The property-appraisal notices list ([chiangrai.treasury.go.th/th/announcement/property-appraisal-announcement](https://chiangrai.treasury.go.th/th/announcement/property-appraisal-announcement)) has one item under "all" and under the 2568 filter: a recruitment-committee notice dated 26 Dec 2568 listing candidates for a temporary land-surveyor (นายช่างสำรวจ) post (`…/news-52dec7eb`). It is a staffing notice, not a survey notice. The 2569 filter returns "ไม่พบข้อมูล" (*no data found*).
  - **Phayao.** The property-appraisal notices list ([phayao.treasury.go.th/th/announcement/property-appraisal-announcement](https://phayao.treasury.go.th/th/announcement/property-appraisal-announcement)) returns "ไม่พบข้อมูล" for "all", 2569 and 2568.
  - **Treasury central list.** The list at /th/announcement/property-appraisal-announcement/ shows "ไม่มีข้อมูล" (*no data*) when fetched without a script engine, and its RSS feed has 0 items. A search there for "เชียงราย" or "สำรวจ" returns "ไม่พบผลลัพธ์" (*no results*), although the Saraburi notice in 3c exists on the same site. The central list and its search therefore **cannot be relied on** to show provincial notices, and a negative result there proves nothing.
  - **Web search.** Two Thai web searches (one per province, using the notice title wording) found no Treasury notice. The only near-match is a different instrument: a Ministry of Interior notice listing the provinces for cadastral surveys to issue title deeds (ออกโฉนด) in FY2570, which press reports say was published in the Royal Gazette in October 2026 ([PPTV](https://www.pptvhd36.com/news/%E0%B8%AA%E0%B8%B1%E0%B8%87%E0%B8%84%E0%B8%A1/285560)). It does not concern appraisal values.
  - **National schedule.** One web search for a Royal Gazette notice from the central committee setting 1 Jan 2570 as the start date found none. Results were press items and notices from earlier rounds. Ratchakitcha was not searched directly.
- **Indirect evidence (Treasury provincial news, not notices):**
  - **Chiang Rai.** The provincial committee (คณะกรรมการประเมินราคาทรัพย์สินเพื่อประโยชน์แห่งรัฐประจำจังหวัดเชียงราย) met as "ครั้งที่ 4/2569" on 18 Sep 2569, chaired by the deputy governor (posted 21 Sep 2569; [provinces-news-20260921-581](https://chiangrai.treasury.go.th/th/news/provinces-news/provinces-news-20260921-581)). The 2/2569 meeting was on 18 Jun 2569 ([provinces-news-20260827-175](https://chiangrai.treasury.go.th/th/news/provinces-news/provinces-news-20260827-175)); that item's body says "ครั้งที่ 2/2568", which contradicts its own title. Neither item states the agenda, so neither shows that a 2570–2573 schedule or a survey window was discussed.
  - **Phayao.** A news item titled "…ประชุมคณะกรรมการประเมินราคาทรัพย์สินเพื่อประโยชน์แห่งรัฐประจำจังหวัดพะเยา ครั้งที่ 1/2569" (*Phayao provincial committee meeting no. 1/2569*), posted 5 Jun 2569 ([provinces-news-20260605-637](https://phayao.treasury.go.th/th/news/provinces-news/provinces-news-20260605-637)), has no body text that could be extracted.
  - **Floods.** The Chiang Rai site carries a news item on a ministerial inspection of flood preparedness (ความพร้อมรับสถานการณ์อุทกภัย) in Mae Sai, dated 19 Aug 2569. Nothing found links floods to the appraisal survey.
- **Implications for RQ1 (my judgement):**
  - Committees are active in 2026, but the survey window for the 2027 land values in Chiang Rai and Phayao cannot be dated from public sources found so far.
  - Until it is, treat it as an unknown. Do not assume that 2027-round land values reflect post-September-2024 market data in Chiang Rai.
  - Survey notices for this round may have been issued in 2023–2025 and since dropped from the current listings, which show only 2568–2569 filters. They may also exist only on paper at the provincial office.
- **Unverified / not done:**
  - the Ratchakitcha full-text search;
  - archived copies (Internet Archive) of the provincial notice lists for 2566–2568;
  - Chiang Rai and Phayao Land Office notice boards;
  - a direct enquiry to the Phayao office (0 5444 9512 ext. 4, appraisal section) or the Chiang Rai office. Any enquiry is a user action.

## 4. The unit of use: banks, BOT rules, fees

- **BOT collateral appraisal policy (BOT19).** A full-text search of the 2019 policy finds no reference to กรมธนารักษ์, ราคาประเมินทางราชการ or any government appraisal value. Confidence: **high**.
  - The only references to government agencies concern guarantees and claims on the Thai government (PDF pp. 18, 23).
  - Annex 3 allows alternative methods for revaluation: "ระบบฐานข้อมูลราคาที่เป็นปัจจุบัน หรือแบบจำลองทางสถิติ" (*current price databases or statistical models*). It names no specific database (PDF p. 16).
- **BOT LTV rules (LTV18 Q&A).** V (collateral value) is the actual sale price, citing as a reliable source "ราคาซื้อขายในสัญญาซื้อขายของกรมที่ดิน (ท.ด. 13 …)" (*the sale price in the Land Department contract*) (item 10).
  - For refinance or top-up loans, the "ราคาประเมิน" (*appraised value*) is used instead (items 11 and 13, PDF pp. 12–13). The text does not refer to Treasury values, so "ราคาประเมิน" there means the lender's collateral appraisal [inference from context].
  - This Q&A belongs to the 2018 notification (สนส. 24/2561). Later notifications (e.g. สนส. 1/2563) were not opened.
- **Mortgage registration fee.** Under the Land Code ministerial regulation, the fee is "ร้อยละ 1 แต่อย่างสูงไม่เกิน 200,000 บาท" (*1%, capped at THB 200,000*), levied on the mortgage amount, not on the appraisal value (DOL). Confidence: **medium**. The page states the base explicitly only for condominiums; the land clause's base was summarised, not quoted.
- **Transfer fee.** The 2% transfer and sale registration fee is "เรียกตามราคาประเมินทุนทรัพย์ตามที่คณะกรรมการกำหนดราคาประเมินทุนทรัพย์กำหนด" (*charged on the official appraisal value*) (DOL, Ministerial Regulation No. 47 (B.E. 2541), item 2(7)(ก)). The Act's stated purpose is a base for "real property transfer taxes and fees … or for other benefits of the State" (ACT s. 5).
- **SEC appraisal standards.** Not checked in full text. The SEC approves valuation firms; no SEC document mentioning ราคาประเมินทางราชการ was found in the one search made. See "Could not verify".
- **Banks (secondary).** The Standard (24 June 2026) reports that a digital copy of the Treasury schedule can be used "เป็นหลักฐานในการยื่นขอสินเชื่อ" (*as evidence when applying for a loan*) at GHB, BAAC and Krungthai ([The Standard](https://thestandard.co/d-value-land-appraisal-online-loans/)). It does not say the value is used for collateral valuation or LTV.

---

## Implications for RQ1 design (my judgement, not established evidence)

1. **The effective unit of variation is the land unit, not the parcel.** A parcel's value is the unit price × depth factor × shape factor, rounded. Variation within a unit is therefore mechanical and carries no hazard information. A parcel-level regression with sheet-level exposure overweights large sheets and treats mechanical depth and shape variation as noise, which is harmless for bias but inflates apparent precision. I recommend:
   - (a) collapse to the sheet, using as the outcome an upper quantile or the maximum of `EVAPRICE`. Road-front parcels at 100% approximate the best land-unit price on the sheet; the mean mixes in depth and shape discounts.
   - (b) report the parcel-level estimate only as a robustness check;
   - (c) cluster no finer than the sheet, keeping district clustering as the main choice.
2. **Hazard can enter only through market comparison, at unit level.** No written flood or low-lying rule exists, so β measures how far provincial committees' market evidence prices hazard into unit values. This sharpens the interpretation: β is "administrative capitalisation via market evidence". The main market input is registered sale prices. If declared prices in Thailand are anchored to official values to save fees (a hypothesis I have not verified), appraisal changes would be sticky and attenuated. This should be named as a threat, with the REIC land index for Bangkok as a check.
3. **The amenity confound is built into the unit typology.** River, canal and sea frontage are separate land units. Flood-prone riverside parcels therefore carry their own unit prices, which bundle access by water and the riverside view with hazard. Possible responses:
   - control for distance to water and compare within water-frontage classes;
   - or restrict to inland road-front units.
4. **Mid-round revisions affect Designs 1b and 1c.**
   - The 15% divergence rule (MR ข้อ 9) and in-place file updates mean that the "2023–26 round" snapshot may already contain post-2024-flood revisions in Chiang Rai. Before using the snapshot as a pre-period, compare it with any earlier dated copy or with amendment notices.
   - For the 2027 round, the data window is not public. Provincial survey notices (MR ข้อ 2) should be collected to date when market evidence was gathered relative to the September 2024 floods.
   - The 2027 start is not legally guaranteed: s. 19 allows a one-year extension, which the design should allow for.
5. **Discreteness.** The rounding grid and a few hundred distinct values per province mean small hazard effects may not move a unit's price across a rounding step. Log-linear OLS at sheet level is still appropriate, but very small changes in Design 1c will be under-detected.
6. **Link to collateral.** No public BOT rule ties bank collateral values, LTV or mortgage fees to Treasury values; LTV uses the sale price or the lender's appraisal. RQ1 is therefore about the **state's official valuation and tax base**. Its bearing on bank collateral (the λ and LGD channel in RQ3) must come through an external market benchmark, as `identification.md` already says. The proposal should not describe Treasury values as collateral values.

## Could not verify

1. **Committee-level rules.** Rules issued by the central committee (คณะกรรมการประเมินราคาทรัพย์สินเพื่อประโยชน์แห่งรัฐ) under ACT s. 13(3) and MR ข้อ 2 and 4 ("ตามที่คณะกรรมการกำหนด") were not found on the Treasury laws page. They could contain additional factors, including any for land condition. The absence of a flood rule (1c) is conditional on this.
2. **Factor tables for deed parcels.** The guide prints the depth and shape tables only in the section on other title types; their application to deed parcels is inferred. The guide is hosted on talad.go.th, not on a Treasury domain, and is undated (≥ 2024 from internal references). A Treasury-hosted copy was not found.
3. **The November 2021 committee notice.** The notice fixing 1 January 2023 as the first start date under the Act was reported in the press as 18 or 19 November 2021 but not found in the Royal Gazette. ratchakitcha.soc.go.th returned HTTP 403 to automated access, which was not circumvented.
4. **2016–2019 round dates.** The start of the 2016–2019 round (1 January 2016) was not checked in a primary source.
5. **2027 round details.** No primary source was found for the announcement date, the effective date or the market-data cut-off of the 2027–2030 round. Provincial survey notices were not opened.
6. **Earlier rounds as data.** Internet Archive holdings of earlier rounds could not be checked (service offline). CKAN history is off-limits under robots.txt. The NPVC request service was not opened.
7. **SEC valuation standards.** The SEC-endorsed valuation standards (มาตรฐานการประเมินมูลค่าทรัพย์สินและจรรยาบรรณ) and the SEC notification on approved valuers were not read in full text for references to ราคาประเมินทางราชการ.
8. **Current BOT LTV rules.** The current LTV notification (after สนส. 24/2561) and the BOT policy for specialised financial institutions were not opened.
9. **Mortgage-fee base.** The base of the mortgage registration fee for land was summarised from the DOL page, not quoted verbatim.
10. **Act entry-into-force date.** Exact date of entry into force: 180 days after 25 May 2019 implies about 21–22 November 2019; press reports say 22 November 2019.

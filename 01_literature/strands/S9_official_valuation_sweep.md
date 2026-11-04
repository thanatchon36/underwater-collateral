# S9: Official-valuation sweep — test of contribution (i)

**Working draft, 2026-11-02.** Task: a time-boxed, systematic test of contribution (i) in `06_proposal/proposal.md` §3: "To my knowledge, the first evidence on how an emerging market's official valuations adjust after a flood." This repeats the Crossref-only search noted in `PROGRESS.md` ("Repeat on OpenAlex before submission") and S6 §(c). Already known and excluded from "new": `fuerst2021pricing`, `guo2026rising`, `garbarino2021high`, `chongwilaikasaem2022flood`, `wei2022effect`, `mori2016flood`, `sawada2018land` (all in `references.bib`).

Labels: **[E]** from a source I opened, at the depth stated; **[S]** my judgement; **[UNVERIFIED]** title or metadata only, not opened.

---

## Verdict on claim (i): **narrow it**

**The claim is not false. As worded, though, it is exposed.** One peer-reviewed Indonesian paper, Utami, Wibowo and Permadi (2021), tracks *official* land-value zones (ZNT maps issued by the Central Java office of BPN, the national land agency) for 2014, 2016, 2018 and 2019 in tidally flooded Tugu district, Semarang. It reports that the flood-prone zone rose far less than other zones: about Rp 250,000 against about Rp 3.5 million per m² in the best-located zone. That is evidence, from an emerging market, on how official valuations move where land floods. A reviewer could cite it against "the first evidence". Three Undip geodesy papers (Sayung, Pekalongan Utara, Semarang Utara) do something similar but mix official and market data (below).

What none of them does, and what RQ1 does:
- (a) none studies a **discrete flood event**. Theirs is chronic tidal flooding (*rob*), driven by subsidence.
- (b) none has **unflooded controls** or any identification. Theirs are map overlays and descriptive differences, or a simple cross-sectional regression.
- (c) none **measures flood extent independently**, as RQ1 does with radar and UNOSAT maps.

The Porto Alegre administrative reduction of *valor venal* after the 2024 flood (Brazil) is practice, not published evidence. It does not defeat the claim, but it shows that emerging-market official values *can* be adjusted after a flood.

**Proposed wording (105 characters, 16 words; the current sentence is 105 characters, 17 words):**

> To my knowledge, the first causal estimate of how emerging-market official valuations respond to a flood.

If "causal" is judged too strong for an observational difference-in-differences, a fallback of the same length is: "To my knowledge, the first controlled estimate of how emerging-market official valuations respond to a flood."

**Consequential edits [S] (for the author; not made here).**
- Add Utami et al. (2021) to the "Closest to RQ1" sentence. One way to do it within the word budget: "…in Semarang, official land-value zones rose less where tidal flooding recurs [@utami2021impact]".
- Davlasheridze, Hou and Miao (2026, Harvey, Harris County assessed values) is a second US event study of official assessments, alongside Guo et al. Cite it with or instead of Guo et al. if space allows.
- Sato and Shiba (2021) is the Japanese case: official appraisals fell in low-lying coastal areas outside the damaged zone after the 2011 tsunami, a hazard-updating response. It undercuts any implicit claim that official values never update on hazard. It does not affect the emerging-market claim.

---

## Search log

**Sources and limits.**
- *OpenAlex*: works search, `filter=from_publication_date:2000-01-01`, 8–10 results per query screened by title, no email or API key sent. The API warned that keyless use shares a $0.10 daily budget per IP; all 69 queries completed.
- *Crossref*: `query.bibliographic`, from 2000. Its totals are loose relevance matches and say little.
- *Semantic Scholar*: **not completed**. Every request returned HTTP 429 on two attempts, the second with 12-second spacing. Fourteen query attempts failed (12 distinct strings). Repeat with an API key before submission.
- *ThaiJO*: the old OJS site-search URL now returns 404. I queried the new site's JSON search endpoint (`/api/v1/articles/search`, field `q`), the one the site's front end calls. It appears to match title and keyword tokens rather than full text, so recall for Thai phrases is limited. All hits were screened by title and keywords.
- *Web search* (no Google Scholar API): 9 queries.
- Full scripts and raw JSONL output are in the session scratchpad, not the repository.

| Source | Query | Hits (total reported) | Relevant (opened) |
|---|---|---|---|
| OpenAlex | official land valuation flood | 19,349 | 0 |
| OpenAlex | assessed property value after flood | 390,103 | 0 |
| OpenAlex | property tax assessment flood | 64,663 | Guo et al. (known) |
| OpenAlex | cadastral valuation flood | 1,252 | Russian IOP 2021; InterCarto 2020 |
| OpenAlex | statutory valuation flood | 7,423 | Fuerst & Warren-Myers (known); Nebraska 2019 |
| OpenAlex | appraised land value flood Thailand | 1,708 | 0 |
| OpenAlex | land valuation flood Indonesia NJOP | 24 | **Utami et al. 2021** |
| OpenAlex | government appraisal land price flood Thailand | 2,940 | Wei & Zhao (known) |
| OpenAlex | official land price flood Vietnam | 13,009 | 0 |
| OpenAlex | land price after flood China benchmark | 15,331 | Wei & Zhao (known) |
| OpenAlex | posted land price flood Japan | 38,403 | 0 |
| OpenAlex | zonal value flood Philippines | 1,405 | 0 |
| OpenAlex | circle rate flood India property | 21,192 | 0 |
| OpenAlex | mass appraisal flood risk | 21,595 | 0 |
| OpenAlex | flood tax assessment Hurricane Harvey | 1,876 | 0 |
| OpenAlex | assessed values Hurricane Katrina property tax | 5,117 | 0 |
| OpenAlex | NJOP banjir | 178 | 0 (NJOP accuracy papers, no flood) |
| OpenAlex | nilai jual objek pajak banjir | 715 | Palu liquefaction outreach note |
| OpenAlex | harga tanah banjir rob | 502 | Semarang Utara 2024; Sayung 2017; Pedurungan 2015 |
| OpenAlex | ราคาประเมินที่ดิน น้ำท่วม | 0 | — |
| OpenAlex | ราคาประเมิน อุทกภัย | 0 | — |
| OpenAlex | มูลค่าที่ดิน น้ำท่วม | 0 | — |
| OpenAlex | valor venal enchente IPTU | 64 | 0 |
| OpenAlex | giá đất lũ lụt | 1,438 | 0 |
| OpenAlex | 基准地价 洪水 | 16,877 | 0 |
| OpenAlex | 公示地価 水害 | 108,943 | Mori et al. (known); Hamamatsu tsunami 2025 |
| OpenAlex | 路線価 浸水 | 32,465 | 0 |
| OpenAlex | 공시지가 홍수 | 12 | Seoul disaster zones 2020 [UNVERIFIED] |
| OpenAlex | property reassessment after disaster | 11,093 | 0 |
| OpenAlex | property tax base natural disaster local government | 72,750 | **Davlasheridze et al. 2026** |
| OpenAlex | assessor flood damage reassessment | 228 | 0 |
| OpenAlex | Nebraska property taxes 2019 flood | 992 | Nebraska 2019 |
| OpenAlex | flood assessed value Houston appraisal district | 850 | 0 |
| OpenAlex | Malaysia property valuation flood | 4,318 | 0 (market hedonics) |
| OpenAlex | Brazil property value flood | 83,913 | 0 |
| OpenAlex | India property value flood Chennai Mumbai | 1,258 | 0 |
| OpenAlex | zona nilai tanah banjir | 5,972 | Pedurungan; Semarang Utara; Sayung; Pekalongan Utara; Sukolilo |
| OpenAlex | perubahan nilai tanah pasca banjir | 5,608 | 0 |
| OpenAlex | NJOP setelah bencana | 153 | Palu (as above) |
| OpenAlex | nilai tanah sebelum dan sesudah banjir | 3,973 | Surabaya 2008 thesis [UNVERIFIED beyond abstract] |
| OpenAlex | cadastral value flood zone Russia | 816 | Russian IOP 2021 |
| OpenAlex | kadastrovaya stoimost' zatoplenie | 0 | — |
| OpenAlex | flood land value official Philippines BIR zonal | 11 | 0 |
| OpenAlex | China land price flood event difference-in-differences | 53,699 | 0 |
| OpenAlex | government land price flood Bangkok 2011 | 4,714 | 0 |
| OpenAlex | Thailand 2011 flood land price | 18,657 | Sawada et al. (known) |
| OpenAlex | Thailand flood property value | 53,844 | Chongwilaikasaem (known) |
| OpenAlex | disaster property tax assessment change difference-in-differences | 58,740 | Guo; Davlasheridze |
| OpenAlex | Mabi Kurashiki flood land price | 1 | 0 |
| OpenAlex | Joso Kinu River flood land price | 3 | 0 |
| OpenAlex | 西日本豪雨 地価 | 9,713 | 0 |
| OpenAlex | 水害 地価 下落 | 75,193 | Nagoya JSCE 2020 [UNVERIFIED] |
| OpenAlex | Brisbane 2011 flood land valuation valuer-general | 45 | 0 |
| OpenAlex | Zhengzhou 2021 flood housing price | 251 | 0 |
| OpenAlex | 洪涝 地价 影响 | 2,523 | 0 |
| OpenAlex | flood event official land price decline | 46,798 | Häse & Hirte 2023 (market) |
| OpenAlex | hurricane assessed value county appraisal district difference-in-differences | 1,205 | 0 |
| OpenAlex | post-disaster property tax assessment reduction | 40,151 | Davlasheridze |
| OpenAlex | tsunami posted land price Great East Japan official land price | 3,115 | **Sato & Shiba 2021**; Azegami 2022 |
| OpenAlex | Hurricane Katrina property assessment Orleans Parish assessed values | 1,126 | 0 |
| OpenAlex | Hurricane Ian assessed value property appraiser | 173 | Bandyopadhyay 2026 preprint |
| OpenAlex | assessment-sales ratio after flood | 30,168 | 0 |
| OpenAlex | land value zone flood | 311,407 | Utami; Russian IOP |
| OpenAlex | Jakarta flood land value NJOP | 43 | 0 |
| OpenAlex | Bangkok flood 2011 appraisal | 1,574 | 0 |
| OpenAlex | Chennai flood guideline value land | 453 | 0 |
| OpenAlex | Pakistan 2022 flood land value | 25,559 | 0 |
| OpenAlex | Kerala 2018 flood land value | 6,337 | 0 |
| Crossref | official land valuation after flood | 1,963,996 | 0 |
| Crossref | assessed value flood property tax assessment change | 3,315,111 | 0 |
| Crossref | cadastral value flooding | 629,831 | Russian IOP 2021 |
| Crossref | zona nilai tanah banjir | 99,235 | 0 new |
| Crossref | NJOP banjir | 4,853 | 0 |
| Crossref | government appraised land price flood Thailand | 970,748 | 0 |
| Crossref | ราคาประเมินที่ดิน น้ำท่วม | 0 | — |
| Crossref | property reappraisal natural disaster | 1,176,133 | Davlasheridze |
| Crossref | statutory land valuation flood Queensland 2011 | 4,726,624 | 0 |
| Crossref | posted land price flood Japan disaster | 1,362,299 | Arakawa 2025 |
| Semantic Scholar | 12 queries (English and Indonesian) | HTTP 429 on all attempts | not run |
| ThaiJO | ราคาประเมินที่ดิน น้ำท่วม | 12 | 0 (none on floods) |
| ThaiJO | ราคาประเมินทุนทรัพย์ อุทกภัย | 3 | 0 |
| ThaiJO | มูลค่าที่ดิน น้ำท่วม 2554 | 141 | 0 |
| ThaiJO | ราคาประเมิน / ราคาประเมินที่ดิน / ราคาประเมินทุนทรัพย์ | 20 / 12 / 3 | 0 (BRT, MRT, Amnat Charoen; no flood) |
| ThaiJO | ราคาที่ดิน น้ำท่วม / ราคาที่ดิน อุทกภัย | 10 / 2 | 0 |
| ThaiJO | มูลค่าที่ดิน | 141 | 0 |
| ThaiJO | ที่ดิน น้ำท่วม | 124 | 0 |
| ThaiJO | อสังหาริมทรัพย์ น้ำท่วม / ราคาบ้าน น้ำท่วม / ราคาที่อยู่อาศัย น้ำท่วม | 2 / 7 / 4 | 0 |
| ThaiJO | หาดใหญ่ น้ำท่วม | 12 | 0 |
| ThaiJO | กรมธนารักษ์ | 61 | 0 (administration papers) |
| ThaiJO | land value flood / land price flood / appraised value flood / property value flood Thailand / housing price flood / real estate flood | 23 / 8 / 34 / 2 / 2 / 2 | 0 |
| Web | ราคาประเมินที่ดิน น้ำท่วม 2554 กรมธนารักษ์ ปรับลด วิจัย | n/a | MGR Online 2012 (Treasury statement) |
| Web | "ราคาประเมินทุนทรัพย์" อุทกภัย ผลกระทบ งานวิจัย วิทยานิพนธ์ | n/a | 0 (damage studies only) |
| Web | น้ำท่วม ราคาประเมินที่ดิน กรมธนารักษ์ … หาดใหญ่ OR อยุธยา OR ปทุมธานี | n/a | 0 research; same news |
| Web | Chongwilaikasaem Hat Yai … Treasury thesis | n/a | 0 beyond the known paper |
| Web | "Natural disasters, property reappraisal, and fiscal outcomes" | n/a | Davlasheridze et al. |
| Web | "The Price of Elevation" … Kim JHE | n/a | not found |
| Web | enchente 2024 Rio Grande do Sul valor venal … | n/a | Porto Alegre decree and methodology news |
| Web | Kelantan 2014 flood … JPPH | n/a | 0 (market hedonics only) |
| Web | flood … official land value change Philippines OR Vietnam OR India OR Bangladesh | n/a | 0 (one Queensland news item) |

**Thai-language result [E].** No Thai study was found, in ThaiJO, OpenAlex, Crossref or web search, that relates ราคาประเมินทุนทรัพย์ (Treasury appraisal values) to a flood, cross-sectionally or before and after. The Thai-specific absence holds, subject to ThaiJO's title-and-keyword matching.

---

## Candidates

Key to "Undermines (i)?": **Yes-partly** means it weakens the literal wording but not the narrowed one.

| # | Citation | URL / DOI | Read depth | What it measures | Cross-section or before/after | Official or market | Country (EM?) | Undermines (i)? |
|---|---|---|---|---|---|---|---|---|
| 1 | Utami, W., Wibowo, Y. A. & Permadi, F. B. (2021). The Impact of Tidal Flooding on Decreasing Land Values in the Areas of Tugu District, Semarang City. *Jurnal Ilmu Lingkungan* 19(1), 10–20. | 10.14710/jil.19.1.10-20 | **Full text, methods, results and conclusion** (PDF) | Changes in BPN land-value-zone (ZNT) values 2014→2016→2018→2019 overlaid on tidal-flood exposure; plus a hedonic-style map for one village | Before/after (multi-round), **descriptive overlay, no controls**; chronic tidal flooding, not one event | **Official** (ZNT maps "obtained from the Semarang BPN Regional Office"/"Central Java BPN Regional Office", PDF pp. 11, 14) | Indonesia (yes) | **Yes-partly.** Closest prior; forces narrowing |
| 2 | Utomo, A. D. S. S., Subiyanto, S. & Amarrohman, F. J. (2017). Analisis Perubahan Zona Nilai Tanah Tahun 2012–2017 Akibat Bencana Banjir Rob di Kecamatan Sayung Kabupaten Demak. *Jurnal Geodesi Undip* 6(4), 453–462. | ejournal3.undip.ac.id/index.php/geodesi/article/download/18177/17250 | Abstract + data and methods (PDF) | Change from 2012 BPN ZNT to an author-built 2017 ZNT (transaction and offer survey), overlaid on tidal-flood map; also compares with 2017 NJOP | Before/after, but the endpoints differ in kind | **Mixed**: 2012 official (BPN Demak), 2017 market survey | Indonesia (yes) | No: change is official→market, not an official revaluation |
| 3 | Naufalita, A., Subiyanto, S. & Haniah (2019). Analisis Pengaruh Perubahan Penggunaan Lahan terhadap Perubahan Zona Nilai Tanah pada Daerah Genangan Banjir Rob di Kecamatan Pekalongan Utara Tahun 2014–2018. *Jurnal Geodesi Undip* 8(1), 38–47. | ejournal3.undip.ac.id/index.php/geodesi/article/download/22450/20586 | Abstract + data section (PDF) | 2014 ZNT (Kantor Pertanahan Kota Pekalongan) vs author-built 2018 ZNT, in tidal-flood areas | Before/after, mixed endpoints | **Mixed** | Indonesia (yes) | No; also finds ZNT changes driven more by access than flooding |
| 4 | Wijaya, A. P., Akbar, R. M. & Amarrohman, F. J. (2024). Analisis Pengaruh Daerah Ancaman Banjir Rob terhadap Zona Nilai Tanah (Studi Kasus: Kecamatan Semarang Utara). *Elipsoida* 7(2), 63–69. | 10.14710/elipsoida.2024.23633 | Abstract + method §2.2 (PDF) | ATR/BPN ZNT 2020 and 2022 plus own 2023 survey; regression of 2023 price on rob threat class | Cross-section (regression); descriptive 2020–22–23 changes | Mixed (official 2020/2022; survey 2023) | Indonesia (yes) | No |
| 5 | Rahati, M., Kahar, S. & Subiyanto, S. (2015). Analisis Perubahan Zona Nilai Tanah Kaitannya dengan Banjir di Kecamatan Pedurungan Kota Semarang. *Jurnal Geodesi Undip* 4(1), 117–128. | ejournal-s1.undip.ac.id/index.php/geodesi/article/view/7644 | Abstract (OpenAlex) | Author-built ZNT (market comparison) vs flood-zone ZNT | Cross-section | Market (author mass appraisal) | Indonesia (yes) | No |
| 6 | Kurniati, N. (2017). Analisis Pengaruh Daerah Rawan Banjir terhadap Nilai Tanah di Sekitarnya (Kecamatan Sukolilo, Surabaya). ITS undergraduate thesis. | repository.its.ac.id/43380/ | Abstract (OpenAlex) | Regression of zone land value on flood extent, depth and duration; no linear effect | Cross-section | Unclear (ZNT, source not stated) | Indonesia (yes) | No |
| 7 | Davlasheridze, M., Hou, Y. & Miao, Q. (2026). Natural disasters, property reappraisal, and fiscal outcomes. *Journal of Housing Economics* 72, 102145. | 10.1016/j.jhe.2026.102145 | Abstract (EconPapers, OpenAlex) | DiD hedonic, Harris County: Harvey cut assessed values about 1.5% (about $4,927 per house; $2.6 bn tax base); assessed fell more than market; SFHA homes fell most; largely reversed within a year | Before/after event, controlled | Official (county assessments) and market | USA (no) | No (EM claim). Add to the "any country" literature |
| 8 | Sato, Y. & Shiba, K. (2021). The impact of Tsunamis on land appraisals: Evidence from Western Japan. *PLoS ONE* 16(4), e0248860. | 10.1371/journal.pone.0248860 | Abstract + data description (journal page) | DID/DDD: after the 2011 tsunami, low-lying (<3.6 m) coastal (<1.46 km) Nankai-exposed locations saw appraised prices fall | Before/after event, controlled; hazard updating outside the damaged area | **Official** (MLIT Official Announcement of Land Prices, appraiser values) | Japan (no) | No (EM claim). Relevant to the H1-type hazard-updating question |
| 9 | Porto Alegre Secretaria Municipal da Fazenda (2025–26). News on Decree 23,605/2025 (IPTU *redutor* for properties hit by the May 2024 flood) and on the valor-venal adjustment methodology (28 April 2026). | prefeitura.poa.br/smf/noticias/prefeitura-regulamenta-redutor-do-iptu-para-imoveis-atingidos-pela-enchente-de-maio-de ; …/fazenda-apresenta-metodologia-de-adequacao-do-valor-venal-para-imoveis-atingidos-pela | Both news pages | Administrative reduction of valor venal for 2025 IPTU, from an unpublished technical study using transaction data and georeferenced models; one year only without a new Planta Genérica | Before/after (administrative) | Official | Brazil (yes) | No (not research, no published study). Shows EM practice exists |
| 10 | MGR Online (15 June 2012). Report of the Treasury Department (Naris Chaiyasoot) on the 2012–15 appraisal round. | mgronline.com/stockmarket/detail/9550000073410 | Article | The round was delayed six months by the 2011 floods; Treasury "found no fall in land prices in flood areas"; values compiled in late 2011 were not changed | n/a (statement) | Official | Thailand (yes) | No. Useful institutional fact for RQ1 (values set before the flood were not revised) |
| 11 | [authors not recorded] (2021). Accounting of the impact of flooding and underflooding zones on the cadastral value of real estate objects. *IOP Conf. Ser.: Earth Environ. Sci.* 867, 012149. | 10.1088/1755-1315/867/1/012149 | Abstract (OpenAlex) | Argues that flood/underflooding zones should enter cadastral valuation (Tobolsk district) | Methodological / ex ante | Official (cadastral) | Russia (yes) | No. Authors not checked: [UNVERIFIED] author list |
| 12 | InterCarto InterGIS (2020). Development of an approach to cadastral valuation of real estate in areas of possible manifestations of natural disasters and emergency situations. 26(1), 190–202. | 10.35595/2414-9179-2020-1-26-190-202 | Abstract (OpenAlex) | Proposes an emergency-probability factor in cadastral value | Methodological | Official | Russia (yes) | No |
| 13 | Nebraska property taxes and the 2019 flood (2019). AgEcon Search / RePEc. | 10.22004/ag.econ.307095 | Abstract (OpenAlex) | Describes LB512, which lets assessors reduce values of flood-damaged property | Policy note | Official | USA (no) | No |
| 14 | Bandyopadhyay, A. P. (2026). Flood Exposure, Assessed Losses, and Resale Prices: Evidence from Florida. Research Square preprint. | 10.21203/rs.3.rs-11295085/v1 | Abstract (OpenAlex; abstract contains unrendered placeholders) | Property-appraiser write-down flags vs water depth in six hurricanes; many deeply flooded homes carry no write-down | Before/after events | Official write-downs vs market | USA (no) | No |
| 15 | Inoue, R. & Hatori, K. (2021). How Does Residential Property Market React to Flood Risk in Flood-Prone Regions? Nagoya City. *Frontiers in Water* 3. | 10.3389/frwa.2021.661662 | Abstract | Past floods and hazard disclosure lower residential values; recent floods do not | Panel | Data type not stated in abstract [UNVERIFIED] | Japan (no) | No |
| 16 | Nagami, K., Inoue, R. & Komori, D. (2025). Flood Risk Perception … Arakawa River Downstream Area, Tokyo. *J. Disaster Research* 20(2), 222–232. | 10.20965/jdr.2025.p0222 | Abstract (Crossref) | Land prices 2005–24 discounted for design and probable-maximum flood risk; 2015 hazard-map revision amplified the discount | Panel, hazard-map change | "Land prices" (official or not [UNVERIFIED]) | Japan (no) | No |
| 17 | Häse, S. & Hirte, G. (2023). The impact of unexpected flood events and adaption measures on lot prices. *Review of Regional Research* 43(1), 29–68. | 10.1007/s10037-022-00177-y | Abstract | DiD on Dresden lot transactions, 2002 and later floods | Before/after event | Market | Germany (no) | No |
| 18 | Azegami, T. (2022). Analysis of matters affecting land price fluctuations in the Great East Japan Earthquake. *Int. J. GEOMATE* 22(89). | 10.21660/2022.89.gxi314 | Abstract | Iwaki land-price changes after earthquake and nuclear accident | Panel | Not stated [UNVERIFIED] | Japan (no) | No (nuclear, not flood) |
| 19 | Penyuluhan … Dampak Likuifaksi terhadap NJOP … Balaroa, Palu (2026). *BUDIMAS*. | OpenAlex W7218227277 | Abstract | Community outreach on NJOP after the 2018 earthquake and liquefaction | n/a | Official | Indonesia (yes) | No (not a flood; not research) |
| 20 | Kim, Y. (2026). The Price of Elevation: Market and Institutional Responses to Elevation-Based Flood-Risk Reduction. *J. Housing Economics* 73, 102160. | 10.1016/j.jhe.2026.102160 | **Not opened** (no abstract in OpenAlex; web search failed) | "Institutional responses" may be assessments | ? | ? | USA (no) | No [UNVERIFIED] |
| 21 | Kim, J.-E. & Lee, S. (2020). Exploring the Relationship between Designating of Disaster Preventing Zones and Land Prices: The Case of Seoul. *J. Korean Soc. Civil Eng.* 40(3), 295–302. | 10.12652/ksce.2020.40.3.0295 | **Not opened** | Zoning and land prices | ? | ? | Korea (no) | No [UNVERIFIED] |
| 22 | 防災インフラ整備による津波浸水リスク低減が地価に与える影響（浜松市）(2025). IRDB. | 10.18880/0002002559 | Abstract | Official posted land prices (地価公示) vs tsunami inundation zones; seawall had no significant effect | Panel | Official | Japan (no) | No |

Not opened, flagged for completeness: a Syiah Kuala 2008 thesis on Surabaya property values before and after drainage works [UNVERIFIED beyond the OpenAlex abstract, market prices]; Queensland news (InDaily, 1 April 2022) saying the Valuer-General raised values in flood-hit areas and no re-valuation was ordered [UNVERIFIED, news snippet only].

---

## BibTeX (opened and material)

```bibtex
@article{utami2021impact,
  author  = {Utami, Westi and Wibowo, Yuli Ardianto and Permadi, Fajar Buyung},
  title   = {The Impact of Tidal Flooding on Decreasing Land Values in the Areas of {Tugu District, Semarang City}},
  journal = {Jurnal Ilmu Lingkungan},
  year    = {2021},
  volume  = {19},
  number  = {1},
  pages   = {10--20},
  doi     = {10.14710/jil.19.1.10-20},
  url     = {https://ejournal.undip.ac.id/index.php/ilmulingkungan/article/view/33521},
  note    = {verified 2026-11-02 via journal page and PDF (methods, results, conclusion read); ZNT maps from BPN Central Java/Semarang}
}

@article{utomo2017analisis,
  author  = {{Ajeng Dyah Setyowati Sri Utomo} and Subiyanto, Sawitri and Amarrohman, Fauzi Janu},
  title   = {Analisis Perubahan Zona Nilai Tanah Tahun 2012--2017 Akibat Bencana Banjir Rob di {Kecamatan Sayung Kabupaten Demak}},
  journal = {Jurnal Geodesi Undip},
  year    = {2017},
  volume  = {6},
  number  = {4},
  pages   = {453--462},
  url     = {https://ejournal3.undip.ac.id/index.php/geodesi/article/download/18177/17250},
  note    = {verified 2026-11-02 via journal PDF (abstract, data and methods); 2012 ZNT from BPN Demak, 2017 ZNT from authors' price survey}
}

@article{wijaya2024analisis,
  author  = {Wijaya, Arwan Putra and Akbar, Rizki Maulidi and Amarrohman, Fauzi Janu},
  title   = {Analisis Pengaruh Daerah Ancaman Banjir Rob terhadap Zona Nilai Tanah (Studi Kasus: {Kecamatan Semarang Utara})},
  journal = {Elipsoida: Jurnal Geodesi dan Geomatika},
  year    = {2024},
  volume  = {7},
  number  = {2},
  pages   = {63--69},
  doi     = {10.14710/elipsoida.2024.23633},
  url     = {https://ejournal2.undip.ac.id/index.php/elipsoida/article/view/23633},
  note    = {verified 2026-11-02 via journal page and PDF (abstract, section 2.2)}
}

@article{davlasheridze2026natural,
  author  = {Davlasheridze, Meri and Hou, Yilin and Miao, Qing},
  title   = {Natural disasters, property reappraisal, and fiscal outcomes},
  journal = {Journal of Housing Economics},
  year    = {2026},
  volume  = {72},
  pages   = {102145},
  doi     = {10.1016/j.jhe.2026.102145},
  url     = {https://econpapers.repec.org/RePEc:eee:jhouse:v:72:y:2026:i:c:s1051137726000264},
  note    = {verified 2026-11-02 via EconPapers and OpenAlex (abstract)}
}

@article{sato2021impact,
  author  = {Sato, Yasuhiro and Shiba, Keita},
  title   = {The impact of Tsunamis on land appraisals: Evidence from Western {Japan}},
  journal = {PLoS ONE},
  year    = {2021},
  volume  = {16},
  number  = {4},
  pages   = {e0248860},
  doi     = {10.1371/journal.pone.0248860},
  url     = {https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0248860},
  note    = {verified 2026-11-02 via PLoS ONE article page (abstract and data description: MLIT Official Announcement of Land Prices)}
}

@misc{poa2025redutor,
  author       = {{Prefeitura de Porto Alegre, Secretaria Municipal da Fazenda}},
  title        = {Prefeitura regulamenta redutor do {IPTU} para im{\'o}veis atingidos pela enchente de maio de 2024},
  year         = {2025},
  howpublished = {News release, 30 December 2025},
  url          = {https://prefeitura.poa.br/smf/noticias/prefeitura-regulamenta-redutor-do-iptu-para-imoveis-atingidos-pela-enchente-de-maio-de},
  note         = {verified 2026-11-02 via prefeitura.poa.br; see also the 28 April 2026 methodology release}
}

@misc{mgr2012appraisal,
  author       = {{MGR Online}},
  title        = {Report on the {Treasury Department}'s 2012--2015 land appraisal round after the 2011 floods},
  year         = {2012},
  howpublished = {News article, 15 June 2012 (in Thai)},
  url          = {https://mgronline.com/stockmarket/detail/9550000073410},
  note         = {verified 2026-11-02 via mgronline.com; Thai-language original title not transcribed}
}
```

---

## Open items

- Re-run the Semantic Scholar queries with an API key; all requests were rate-limited (429) this session.
- Get the ZNT legal status right before citing Utami et al.: ZNT is BPN's land-value zoning, used for land-office fees and as a reference value. It is not NJOP, the regional property-tax base. The proposal should say "official land-value zones", not "tax assessments".
- MGR 2012: an unopened search summary said floodway areas kept old prices for one more year. The opened article does not say this [UNVERIFIED]. Check before using it.

## Final sweep, 2026-11-02 (second pass)

OpenAlex, publication date from 2025-01-01, eight queries (assessed/official valuation and flood; property tax assessment; flood collateral and bank lending; flood debt relief and forbearance; reverse stress test; IFRS 9 provisions). Semantic Scholar returned HTTP 429 on every query (rate limit; not retried). A broader OpenAlex pass on Thai flood and land-price terms found only known papers (Sawada et al. 2018; Chongwilaikasaem and Chalermyanont 2022; Wei and Zhao 2022; Beltrán et al. 2018). New and relevant: Pan, Billio, Dufour and Varotto (2025, EGU abstract) on European mortgage defaults and forbearance after floods (`pan2025drowning`; S5 notes). Already known: the J. Housing Econ. 2026 reappraisal and elevation papers, "Flooded Collateral" (SSRN 2026), the DNB flood scenario paper (JFS 2026), the New Orleans FEDS note and the Banco de España Valencia note. Claim (i) as narrowed stands.

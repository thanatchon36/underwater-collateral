# Phase 5 groundwork: map-sheet decoding and flood rasters

*Working draft, as of 2026-11-02. Public data only; no registration was made.*

## Summary

- **Map-sheet decoding works.** The Treasury fields `UTMMAP1–4, UTMSCALE` are the Department of Lands (DOL) UTM cadastral sheet reference. The convention is stated in DOL and ALRO documents and was checked against a DOL worked example and against all 37.8 million parcel rows. `04_analysis/src/mapsheet.py` decodes 95.8% of parcels (parcel-weighted) to a sheet of known extent: 2 km × 2 km (1:4,000; 50.9% of parcels), 1 km (1:2,000; 7.7%), 500 m (1:1,000; 36.7%) or 250 m (1:500; 0.6%). A further 4.1% carry `UTMSCALE = 5000`, a non-UTM series that can be placed only on its 1:50,000 sheet (about 27 km × 27 km).
- **Flood data on disk without registration (196 MB, `03_data/raw/flood/`):**
  - GFD DFO 3850 (2011) GeoTIFF, about 250 m, CC BY-NC 4.0;
  - JRC GSW v1.4 occurrence tiles 90E_20N and 100E_20N, 30 m, CC BY 4.0;
  - UNOSAT Chiang Rai 2024 water-extent shapefile, multi-sensor including Sentinel-1, CC BY-SA.
- **Not on disk.** No Copernicus EMS activation exists for Thailand in 2024. The only single-sensor Sentinel-1 product found (Sentinel Asia/MBRSC, 15 Sep 2024) states no licence and was not downloaded.

---

## Task 1. Decoding the map-sheet reference

### 1.1 Sources

| Key | Source | URL | What it gives |
|---|---|---|---|
| DOL47 | กรมที่ดิน, *คำอธิบาย ระเบียบกรมที่ดินว่าด้วยการสร้างและการใช้ระวางแผนที่ พ.ศ. ๒๕๔๗* (*Explanatory notes to the DOL Regulation on Making and Using Map Sheets, B.E. 2547 (2004)*), 34 pp. | <https://www.dol.go.th/media/813280638332440576/migration/2025/10/GQa5Vq26UmpNkCvP7uTi8E9W.pdf> | ข้อ ๑๗ (pp. ๑๓–๑๕): scales, sheet sizes and sub-sheet numbering figures; ข้อ ๑๙: sheets straddling 102°E; ข้อ ๒๐ (pp. ๑๘–๑๙): naming rule, examples "5638 II 2606" and "5638 II 2606 - 5 (๑:๑,๐๐๐)"; รูปที่ ๑ (p. ๒๘): example 1:4,000 sheet with grid ticks |
| DOLQA | กรมที่ดิน, question-and-answer compilation for DOL staff (คำถาม–คำตอบ), 20 pp. | <https://www.dol.go.th/media/813280638332440576/migration/2025/10/J1upVfT06cWxjawb8kRmKUED.pdf> | Items ๓๑–๓๓ (naming exercises; adjacency of 1:1,000 sheets), item ๓๘ (datum: Indian 1975) |
| ALRO | ส.ป.ก., *มาตรฐานระวางแผนที่และแผนที่รูปแปลงที่ดินในที่ดินของรัฐ* (*Standards for map sheets and parcel maps on state land*), กมร. 101–103-2551 and data dictionary กมร. 302-2553, 90 pp. | <https://alro.go.th/uploads/org/mapping_land/article_attach/article_attach_201808281535445048.pdf> | กมร. 103-2551 restates the naming rule; กมร. 102-2551 gives datum-shift parameters; the data dictionary (table `TITLE`, p. 45) defines `UTMMAP1` "ชื่อระวางภูมิประเทศ", `UTMMAP2` "แผ่นที่ระวางภูมิประเทศ 1-4", `UTMMAP3` "ชื่อระวาง 1:4,000", `UTMMAP4` "แผ่นที่ระวางขยาย" (domain 1:4,000 `00`; 1:2,000 `01-04`; 1:1,000 `01-16`; 1:500 `01-64`) and `UTMSCALE` |
| RTSD | กรมแผนที่ทหาร (RTSD) via data.go.th, *สารบัญระวางแผนที่ มาตราส่วน 1:50000 ชุด L7018* (*1:50,000 sheet index, series L7018*), shapefile, licence "Creative Commons Attributions" | <https://data.go.th/dataset/l7018_index> (file `l7018indexepsg3395.zip`, 61,899 bytes) | 830 sheet polygons with sheet code and name; used to verify the sheet-number formula (kept in the scratchpad, not in `03_data/raw/`) |
| EPSG | EPSG:24047 / 24048 (Indian 1975 / UTM 47N, 48N); EPSG:1812 (Indian 1975 to WGS 84 (4)) | <https://epsg.io/24047>, <https://epsg.io/1812> | CRS codes; EPSG:1812 is a Position Vector transformation, +293, +836, +318 m, rotations 0.5″, 1.6″, −2.8″, 2.1 ppm, scope "Cadastre", Thailand onshore, accuracy 3 m |

The field names in the Treasury files are identical to those in the ALRO data dictionary, which takes them from DOL's parcel table. This is strong evidence that the Treasury copies the DOL sheet reference unchanged.

### 1.2 The convention

**1:50,000 series sheet (UTMMAP1, UTMMAP2).** `UTMMAP1` is the four-digit number of an RTSD 1:50,000 sheet (series L7017, now L7018), and `UTMMAP2` (1–4) is its Roman numeral I–IV. The sheet is the one in which the **lower-left corner** of the 1:4,000 cadastral sheet lies (DOL47 ข้อ ๒๐; ALRO กมร. 103-2551 §3.1). If that 1:50,000 sheet "is not in official use" (for example across a border or at sea), DOL uses the sheet that holds the lower-right corner instead.

The four digits `CCRR` name a 30′ × 30′ block. Its south-west corner is at longitude 75° + 0.5° × CC and latitude −4.5° + 0.5° × RR, and the four 15′ × 15′ quadrants are I = NE, II = SE, III = SW and IV = NW. No RTSD text stating this formula was found; it was **derived and verified empirically** against the RTSD L7018 index. All 826 polygons with a sheet code match it to within 0.0012° for rows 34–49 (north of 12.5°N). In the peninsula (rows 20–33) a minority of coastal sheets are irregular, with extents shifted by up to about 0.15°. The index also confirms named examples: 5136 IV = อำเภอบางเขน (Bang Khen), 100.50–100.75°E, 13.75–14.00°N; 5638 II = อำเภอปราสาท (Prasat), 103.25–103.50°E, 14.50–14.75°N.

**1:4,000 sheet (UTMMAP3).** Four digits `EENN`: the tens and units of the UTM easting in kilometres (always even), then the tens and units of the UTM northing in kilometres (always even), of the sheet's lower-left corner (DOL47 ข้อ ๒๐). A 1:4,000 sheet is 50 cm × 50 cm of map and so covers 2,000 m × 2,000 m (DOL47 ข้อ ๑๗). The hundreds of kilometres are not coded. They are recovered by choosing the candidate corner (100 km apart) that falls in the named 1:50,000 sheet (about 27 km across), so the choice is unambiguous.

**Sub-sheets (UTMMAP4, UTMSCALE).** Each 1:4,000 sheet is subdivided into 2 × 2 sheets at 1:2,000 (1,000 m), 4 × 4 at 1:1,000 (500 m) or 8 × 8 at 1:500 (250 m) (DOL47 ข้อ ๑๗; the ALRO domain is 01–04 / 01–16 / 01–64; `00` at 1:4,000). The figures in DOL47 (p. ๑๕) number them **row by row from the top-left, left to right**, for example `1 2 / 3 4` and `1 2 3 4 / 5 6 7 8 / …`. DOLQA item ๓๓ confirms the direction: the sheet on the lower edge of 1:1,000 sheet "-6" is "-10".

**UTM zone.** Zone 47 west of 102°E, zone 48 east of it (ALRO กมร. 101-2551). Sheets crossed by 102°E are drawn twice, once in each zone, and a parcel is plotted in the zone holding most of its area (DOL47 ข้อ ๑๙). The Treasury fields carry no zone. The decoder takes the zone of the 1:50,000 sheet, and if the code does not fit there it tries the other zone. In zone 47 and zone 48 coordinates the same code falls in disjoint places, so this test separates them.

**Worked example (DOL47 รูปที่ ๑).** Sheet "5638 II 2606" at 1:4,000, ตำบลโคกสะอาด อำเภอปราสาท (Tambon Khok Sa-at, Amphoe Prasat, Surin). Its grid ticks read 326000–328000 m E and 1606000–1608000 m N, and its scale factor is K = 0.99997. The adjacent-sheet index lists 2408, 2608, 2808 / 2406, 2806 / 2404, 2604, 2804. `sheet_bounds('5638', 2, '2606', '00', 4000)` returns `(48, 326000, 1606000, 328000, 1608000)`, and the eight neighbours decode to the expected ±2 km offsets (tests).

### 1.3 Datum

DOL computes cadastral sheets on **Indian 1975** (Everest 1830 ellipsoid). DOLQA item ๓๘ answers "พื้นหลักฐาน Indian ๑๙๗๕" to the question of which datum DOL uses for map sheets, and ALRO กมร. 102-2551 describes Indian 1975 as the national geodetic datum, with WGS84 used for GPS work. `sheet_bounds` therefore returns **Indian 1975 / UTM metres (EPSG:24047 or 24048)**.

Flood rasters are in WGS84. In the worked example, the Indian 1975 → WGS84 shift moves the sheet centre by about −415 m in easting and +313 m in northing (about 520 m in total). That is a quarter of a 1:4,000 sheet and more than a 1:500 sheet, so overlaying without conversion would misplace sheets. `to_wgs84_lonlat` and `sheet_centroid(..., wgs84=True)` apply the RTSD three-parameter shift quoted by ALRO (Indian 1975 → WGS84: +204.5, +837.9, +294.8 m; RTSD announcement of 10 January 2008). ALRO prints these values with minus signs, and the positive direction is inferred from EPSG:1812, which also has positive translations. EPSG:1812 differs from the RTSD set by metres only.

**Could not verify:** whether DOL has re-issued sheets on WGS84 since 2008 (RTSD moved its 1:50,000 series to WGS84 as L7018), and if so whether the sheet names and the Treasury references refer to the WGS84 grid. If they do, the 2 km grid would shift by the same few hundred metres. Sheet-level analysis is robust to this only if the flood measure is averaged over the sheet.

### 1.4 Check against the data

All 77 province files were complete when checked (`manifest.csv` present, no `.part` files). The validation script is `04_analysis/src/check_mapsheet_coverage.py`, with output in `04_analysis/outputs/tables/mapsheet_decode_coverage.csv`. Value patterns in Sing Buri, Phra Nakhon Si Ayutthaya and Bangkok:

| File | Rows | UTMMAP1 (distinct) | UTMMAP2 | UTMMAP3 distinct (range) | UTMSCALE counts | UTMMAP4 range by scale |
|---|---|---|---|---|---|---|
| Sing Buri | 127,449 | 5038, 5039 | 1–4 | 256 (2648–6030) | 4000: 94,371; 1000: 32,707; 2000: 370; 500: 1 | 00; 01–16; 01–04; 15 |
| Ayutthaya | 465,874 | 5037, 5038, 5137, 5138 | 1–4 | 727 (3066–9684) | 4000: 274,213; 1000: 191,301; 500: 360 | 00; 01–16; 01–58 |
| Bangkok | 2,281,482 | 5035, 5036, 5135, 5136 | 1–4 | 462 (0012–9840) | 1000: 2,281,313; 4000: 168; 500: 1 | 01–16; 00; 14 |

These match the convention. Every `UTMMAP3` digit pair is even (one exception in Bangkok, `8134`), `UTMMAP4` stays within the ALRO domains, and the 1:50,000 sheets are the right ones geographically: 50xx/51xx columns = 100.0–101.0°E, rows 35–39 = 13.0–15.5°N. Decoded WGS84 centroids fall within 100.04–100.96°E, 13.50–13.99°N for Bangkok and 100.18–100.49°E, 14.72–15.11°N for Sing Buri.

National coverage (all 77 files, 37,806,747 parcel rows, 317,081 distinct references):

| Outcome | Parcels | Share |
|---|---|---|
| Decoded, lower-left corner inside the named 1:50,000 sheet | 36,112,197 | 95.5% |
| Decoded, corner within 5 km of the sheet (irregular sheet edges, lower-right fallback) | 95,982 | 0.3% |
| `UTMSCALE = 5000` (not a UTM sheet; see below) | 1,567,120 | 4.1% |
| Code inconsistent with its 1:50,000 sheet (more than 5 km away) | 31,147 | 0.08% |
| Invalid 1:50,000 number or field | 301 | <0.01% |

The share decoded is lowest in the south and west, where 1:5,000 sheets are common and coastal 1:50,000 sheets are irregular: Narathiwat 79%, Phang Nga 81%, Krabi 83%, Yala 83%; median province 96%. Inconsistent codes cluster in Prachuap Khiri Khan (4.1%), Ranong (2.8%) and Chumphon (1.5%). This is consistent with irregular peninsular 1:50,000 sheets, not with an error in the rule. Using the RTSD index polygons in place of the nominal formula would probably recover most of them; this was not done.

**`UTMSCALE = 5000`.** These rows always have `UTMMAP3 = 0000` and a three-digit `UTMMAP4` (for example 013–164). They are not UTM cadastral sheets. They are probably the older 1:5,000 aerial-photo sheets (ระวางรูปถ่ายทางอากาศ), numbered within the 1:50,000 sheet, but **the numbering of these sheets could not be verified** and they are not decoded. They can be placed on their 1:50,000 sheet (`series_sheet_lonlat`) only.

### 1.5 Spatial precision

- The decoded extents are exact under the DOL rule: they are a sheet, not a point estimate. Positional uncertainty within the sheet is the sheet itself, with a half-width of 1,000 / 500 / 250 / 125 m at 1:4,000 / 1:2,000 / 1:1,000 / 1:500.
- Parcel-weighted, about half of all parcels are known only to a 2 km cell and about 37% to a 500 m cell. Urban areas are mostly 1:1,000; Bangkok is 99.99% at 1:1,000.
- Relative to WGS84 flood rasters, the residual error after the datum shift is a few metres (parameter choice), assuming the sheets are on Indian 1975 (see 1.3).
- A sheet is not a parcel. Large parcels may extend beyond their sheet (DOL plots each parcel on the sheet holding most of its area), so sheet-level flood exposure is an average over the cell.

### 1.6 Code

- `04_analysis/src/mapsheet.py`:
  - `sheet_bounds(utmmap1, utmmap2, utmmap3, utmmap4, utmscale) -> (zone, xmin, ymin, xmax, ymax)` in Indian 1975 UTM metres;
  - `sheet_centroid(..., wgs84=False)`;
  - `series_sheet_lonlat`, `grid_code`, `to_wgs84_lonlat`;
  - a pure-Python transverse Mercator (Krüger series), so there is no new dependency.
- `04_analysis/src/test_mapsheet.py`: 30 pytest tests that encode the DOL47 figure example and its eight neighbours, the 1:1,000 example "5638 II 2606 - 5", DOLQA items ๓๑–๓๓, the ALRO domains, the RTSD sheet extents, a projection round trip and the size of the datum shift. Run with `.venv/bin/python -I -m pytest 04_analysis/src/test_mapsheet.py`.
- DOLQA items ๓๑ and ๓๒ give coordinates that are not geographically consistent with the 1:50,000 sheets they name (they are naming exercises), so the tests use them only for the digit rule.
- pytest 9.2.0 was added to `.venv` and `requirements.txt` was re-pinned.

---

## Task 2. Flood rasters without registration

All routes below were checked on 2026-11-02 with plain HTTP requests (`curl -sIL`, no cookies, keys or account): every URL listed returned HTTP 200. The route search was delegated to a sub-agent; the four downloaded files were then fetched and checked directly (sizes, SHA-256, licence file, GeoTIFF georeferencing), and the HDX licences were re-read from the HDX CKAN API. Downloads total **196 MB** (cap 300 MB), logged in `03_data/README.md`.

### 2.1 (a) Global Flood Database, event DFO 3850 (Thailand, 2011) — **on disk**

- **Route.** Public Google Cloud Storage bucket `gfd_v1_4` (one zip per event, 913 objects; the bucket listing <https://storage.googleapis.com/gfd_v1_4/> is public). The authors' repository README (<https://github.com/cloudtostreet/MODIS_GlobalFloodDatabase>) names this bucket as a download source alongside GEE, so **GEE is not needed**. The web portal (global-flood-database.cloudtostreet.ai) is a JavaScript application and was not used.
- **File.** <https://storage.googleapis.com/gfd_v1_4/DFO_3850_From_20110805_to_20120109.zip>, 20,843,625 bytes, SHA-256 `72e687770af0ae2520114ae97382a83f49a72ccdec5aa15b6ade7c441962687e`. Contains `DFO_3850_From_20110805_to_20120109.tif` (20,728,095 bytes; five bands `flooded`, `duration`, `clear_views`, `clear_perc`, `jrc_perm_water`), `README_GFD.pdf`, `LICENSE.txt` and `DFO_3850_properties.json` (id 3850, began 2011-08-05, cause "Tropical Storms, Monsoonal Rain", severity 2, countries VNM, THA, LAO, KHM).
- **Grid.** Per the sub-agent's header read: 3,999 × 5,519 pixels at 0.002246° (about 250 m, the MODIS resolution), 98.07–107.05°E, 8.56–20.96°N, so the Chao Phraya basin is covered. Note: `03_data/inventory_R3.md` item 4 gives "30 m pixels" from the GEE catalogue; the event raster's native resolution is about 250 m, which is coarser than every cadastral sheet size except 1:4,000 (2 km). Not yet opened with a GIS reader; cloud-free coverage of the basin (`clear_perc`) is still unchecked.
- **Licence.** CC BY-NC 4.0 (`LICENSE.txt` in the zip, first line "Creative Commons Attribution-NonCommercial 4.0 International Public License"; also the GEE catalogue page <https://developers.google.com/earth-engine/datasets/catalog/GLOBAL_FLOOD_DB_MODIS_EVENTS_V1>). Academic, non-commercial use with attribution is fine; the repository's MIT licence covers code only.
- **Citation.** Tellman, B., Sullivan, J. A., Kuhn, C. et al. (2021), "Satellite imaging reveals increased proportion of population exposed to floods", *Nature*, doi:10.1038/s41586-021-03695-w (verified via Crossref, 2026-11-02).

### 2.2 (b) JRC Global Surface Water — **occurrence v1.4 on disk**

- **Tiles.** Tiles are 10° × 10°, named by their top-left (north-west) corner. Confirmed from the GeoTIFF headers of the downloaded files: `occurrence_90E_20N…` has its tie point at (90°E, 20°N) and `occurrence_100E_20N…` at (100°E, 20°N), both 40,000 × 40,000 pixels at 0.00025° (about 30 m). **99–102°E, 13–16°N needs both tiles**: 90E_20N for 99–100°E and 100E_20N for 100–102°E.
- **Downloaded (v1.4, 1984–2021).** Pattern `https://storage.googleapis.com/global-surface-water/downloads2021/{layer}/{layer}_{lon}_{lat}v1_4_2021.tif`:
  - `occurrence_90E_20Nv1_4_2021.tif`, 57,192,916 bytes, SHA-256 `2ac2a05412d1b618d6d54dc07c96217d27ea254c542188d5fd00f17cd5b10177`;
  - `occurrence_100E_20Nv1_4_2021.tif`, 96,623,164 bytes, SHA-256 `7b268c68461ea4c81c73f9ee30ce91f2f9e4329aa35fff3180f10598b3e0f44b`.
- **Available, not downloaded (size cap).**
  - Recurrence v1.4, same pattern with `recurrence`: 35,815,946 + 92,055,992 bytes.
  - v1.5 (1984–2024), the version the official download page (<https://global-surface-water.appspot.com/download>) now links: `https://s3.waw4-1.cloudferro.com/swift/v1/global-surface-water/download2024/Aggregated/VER1-5/{layer}/{layer}_{lon}_{lat}_v1_5_2024.tif`; occurrence 62,626,105 + 113,467,431 bytes, recurrence 31,611,149 + 94,519,114 bytes. A Google Cloud mirror (`storage.googleapis.com/water-world/download2024/VER1-5/…`) has the same names but different sizes; which copy is canonical could not be verified.
  - **Monthly history.** For 1984–2021 (which includes the 2011 flood months) the JRC FTP has `https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GSWE/MonthlyHistory/LATEST/tiles/{YYYY}/{YYYY_MM}/{YYYY_MM}-{row}-{col}.tif`. The offsets are 10-digit pixel counts from (180°W, 80°N) in 40,000-pixel steps: `0000240000-0001080000` = 90E_20N and `0000240000-0001120000` = 100E_20N. Example: `2011_10-0000240000-0001080000.tif`, 21,653,560 bytes, and `…-0001120000.tif`, 40,995,734 bytes. 2022–2024 (v1.5) are at `…/download2024/monthlyhistory/VER1-5/{YYYY}/{YYYY_MM}/monthlyhistory_{lon}_{lat}_v1_5_{YYYY}_{MM}.tif`. Landsat-based, so monsoon-month cloud gaps are expected.
- **Format.** GeoTIFF, EPSG:4326, 8-bit (occurrence 0–100%; the file is palette mode).
- **Licence.** The download page says the data are produced under the Copernicus Programme and provided "free of charge, without restriction of use". The JRC FTP `copyright.txt` (<https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GSWE/copyright.txt>) says © European Union, CC BY 4.0. Attribute as CC BY 4.0.
- **Citation.** Pekel, J.-F., Cottam, A., Gorelick, N. and Belward, A. S. (2016), "High-resolution mapping of global surface water and its long-term changes", *Nature*, doi:10.1038/nature20584 (verified via Crossref, 2026-11-02).

### 2.3 (c) 2024 northern Thailand floods (Chiang Rai, Sep–Oct 2024)

- **Copernicus EMS Rapid Mapping: no activation for Thailand in 2024.** The public activation list (`https://rapidmapping.emergency.copernicus.eu/backend/dashboard-api/public-activations-info/`) runs continuously from EMSR745 to EMSR775 (Aug–Oct 2024). The only regional activation is EMSR754 (Viet Nam).
- **UNOSAT activation FL20240912THA (with GISTDA) — Chiang Rai on disk.** Each product is listed on HDX with licence CC BY-SA (confirmed via the HDX API), and the files sit directly on unosat.org with no login:
  - **Chiang Rai, cumulative 1 Aug – 22 Oct 2024 (product 4009).** <https://unosat.org/static/unosat_filesystem/4009/FL20240912THA_SHP.7z>, 30,135,033 bytes, SHA-256 `ac50751cba4d2659a6a05dd22d4a8202017bead4e67e8064d0d5baa842c3c5e4`, shapefile in a 7z archive (**downloaded**). A file-geodatabase version is `…/4009/FL20240912THA_GDB.zip` (27,977,189 bytes). HDX page: <https://data.humdata.org/dataset/water-extents-from-1-aug-2024-to-22-october-2024-over-chiang-rai-province>.
  - **Phayao, 1 Aug – 12 Oct (product 4003):** SHP zip 15,877,686 bytes, GDB 18,012,338 bytes.
  - **Chiang Mai and Lamphun, 5–10 Oct (product 4017):** SHP zip 56,380,868 bytes, GDB 33,876,420 bytes.
  - **Doi Tao, 6 Oct (product 4001):** SHP zip 543,201 bytes, GDB 272,697 bytes.
  - **Not Sentinel-1 only.** The Chiang Rai product lists Sentinel-1 on 16 dates together with Sentinel-2, RCM, TerraSAR-X, Pléiades, PlanetScope, Landsat and others. The polygons are dissolved, so they cannot be restricted to Sentinel-1.
  - This is a vector water extent, not a raster. It is suitable for an intensity-DiD treatment indicator at sheet level.
  - The 7z archive was not opened (no 7z reader in `.venv`); the GDB zip is the alternative if 7z support is not wanted.
- **Sentinel Asia activation of 10 Sep 2024** (requested by GISTDA; page <https://sentinel-asia.org/EO/2024/article20240910TH.html>). No login is needed, but **no licence or terms are stated, so nothing was downloaded**.
  - `…/article20240910TH/MBRSC/MBRSC_THAILAND_FLOOD-MAP-SHP.zip`, 2,906,563 bytes: the **only single-sensor Sentinel-1 product found** (15 Sep 2024, northern provinces).
  - `…/AIT/AIT-VAP001-TH.zip` (7,907,308 bytes; ALOS-2, Chiang Rai).
  - `AIT-VAP002-TH.zip` (1,382,659 bytes; ALOS-2, Nong Khai).
  - `AIT-VAP003-TH.zip` (7,908,100 bytes).
- **Earth Observatory of Singapore flood proxy map, Aug 2024** (HDX `eos-rs-thailand-floods-aug-2024`, CC BY, 32,613,772 bytes). It is ALOS-2 data from 31 Aug, misses the September Mae Sai peak, lies south of Mae Sai and is a colour image, not a classification. Not downloaded.
- **Landsat alternative.** GSW v1.5 monthly history for 2024_09 and 2024_10, tiles 90E_30N and 100E_30N (2024_09: 62,456,510 and 57,185,843 bytes), CC BY 4.0. Not downloaded.
- **Incidental find, not examined.** HDX lists an EOS-RS Sentinel-1 flood proxy map for Bangkok of 29 Sep 2026 (`eos-rs-thailand-flood-bangkok-sep-2026`, CC BY, file `EOSRS_2026_016_THA_FL_20260929_FPM_S1_Bangkok_v0.8.zip`). It may matter for a later round-to-round design. Neither the event nor the product was checked.

### 2.4 What still needs CP3 (registration)

- **GEE** (any account) is no longer needed for GFD or GSW; it would be needed only to process raw Sentinel-1 for our own 2024 (or 2011-era) flood maps.
- **GISTDA API gateway** (<https://api-gateway.gistda.or.th/v2>) holds recurrent flood areas 2011–2023 and daily flood extents and requires an API key. No no-login file route was found; flood.gistda.or.th did not respond and disaster.gistda.or.th is a JavaScript application.
- **Copernicus Data Space / ASF** downloads of raw Sentinel-1 scenes need a (free) account. Not explored further.
- **DOL parcel polygons** (data.go.th `mapland-parcel`) need a written request and keys, as before. Map-sheet decoding (Task 1) makes them unnecessary for a sheet-level pilot.

---

## Could not verify

1. An RTSD document stating the 1:50,000 sheet-number formula. The formula was verified only empirically, against the RTSD L7018 index.
2. Whether DOL cadastral sheets (and the Treasury references) are now on WGS84 rather than Indian 1975, and since when.
3. The numbering of the `UTMSCALE = 5000` sheets (4.1% of parcels) and what series they belong to.
4. The 1:500 sub-sheet figure in DOL47 was read from extracted PDF text, not rendered; the extracted row order of two rows was garbled. The row-major order is assumed by analogy with the 1:2,000 and 1:1,000 figures and DOLQA item ๓๓. Only 0.6% of parcels are at 1:500.
5. The `EVAPRICE` unit (baht per square wah) remains unconfirmed; it is not addressed here.
6. Licence or terms of the Sentinel Asia activation products, including the MBRSC Sentinel-1 flood map of 15 Sep 2024.
7. Which GSW v1.5 mirror (CloudFerro or Google Cloud, which differ in file size) is canonical; v1.5 tile origins were inferred from the naming convention, not read from headers.
8. Whether the GFD DFO 3850 raster has adequate cloud-free observation (`clear_perc`) over the Chao Phraya floodplain; the GeoTIFF has not yet been opened with a GIS reader (no rasterio/GDAL in `.venv`). The GFD grid figures (0.002246°, 3,999 × 5,519 px) come from the sub-agent's header read.
9. Contents of the UNOSAT 7z archive (not extracted).
10. A Zenodo mirror of GFD (not searched; the GCS bucket sufficed).

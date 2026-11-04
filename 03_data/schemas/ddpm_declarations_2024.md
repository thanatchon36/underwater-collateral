# Schema: 2024 emergency-zone declarations (DDPM), for the RQ1 administrative-spillover sensitivity

File: `03_data/raw/ddpm_declarations/declarations_2024.csv` (UTF-8, comma-separated, header row). Entered by hand from the provincial DDPM offices' replies or published notices (`05_design/data_requests_draft.md`, Request 1); never edited after entry. Name matching and the drop rule: `04_analysis/src/rq1_declarations.py` (fixed 2026-11-03, before any list was obtained).

| Column | Type | Content | Example |
|---|---|---|---|
| `province` | text | sample province slug: `chiang-rai`, `phayao`, `nong-khai`, `nakhon-phanom` | `nong-khai` |
| `district_th` | text | district (อำเภอ) in Thai, prefix optional; `เมือง` alone = the province's Mueang district | `อำเภอโพนพิสัย` |
| `tambon_th` | text | subdistrict (ตำบล) in Thai; blank if the whole district is declared | `ตำบลจุมพล` |
| `village` | text | village (หมู่บ้าน) name or หมู่ number, optional; a village row declares its tambon | `หมู่ 3` |
| `declared_on` | date | date of the declaration, `YYYY-MM-DD` (Gregorian; convert from B.E. by subtracting 543) | `2024-09-12` |
| `source` | text | document or reply: file name, letter reference, URL | `reply_ddpm_nongkhai_2026-11-20.pdf p. 2` |

One row per declared unit and declaration. Rows dated outside 1 July–31 December 2024 are kept but not used. A name that matches no COD-AB unit of the province stops the run; the correction goes into the matching (reported as a deviation), not into the raw rows.

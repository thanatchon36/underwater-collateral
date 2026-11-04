# Data access plan

**Working draft, 2026-11-02 (Phase 4).** Every Tier 1 dataset is logged in `03_data/README.md`, with its URL, access date, licence and script. Nothing restricted is held in this workspace. Tier 2 is prepared for through a schema and synthetic data only.

## Tier 1: public data, available now

| Data | Use | Status (2026-11-02) |
|---|---|---|
| Treasury Department parcel appraisal values (ราคาประเมินที่ดิน), round 2023–26, 77 provinces, 37.8 m rows | RQ1 outcome | **On disk**: snapshot 2026-11-02, SHA-256 manifest; DGA Open Government Licence |
| Map-sheet decoding (Department of Lands UTM sheets) | Locates appraisals to 2 km / 1 km / 500 m / 250 m cells | **Done** (`04_analysis/src/mapsheet.py`): 95.8% of parcels decoded |
| Global Flood Database, event DFO 3850 (Thailand 2011) | RQ1 hazard/event exposure; RQ3 scenario footprint | **On disk** (`03_data/raw/flood/gfd_dfo3850/`, 20.8 MB); about 250 m (MODIS); CC BY-NC 4.0 |
| JRC Global Surface Water v1.4 (1984–2021), occurrence, tiles 90E_20N and 100E_20N | RQ1 long-run hazard proxy | **On disk** (153.8 MB); 30 m (Landsat); CC BY 4.0. Recurrence, v1.5 and monthly history are available without login but not yet downloaded |
| UNOSAT water extent, Chiang Rai, 1 Aug – 22 Oct 2024 (multi-sensor, vector) | RQ1 event difference-in-differences (with the 2027 round) | **On disk** (30.1 MB); CC BY-SA. Phayao and Chiang Mai/Lamphun products are available on the same route |
| BOT provincial loans and deposits (FI_CB_011), monthly since 1996 | RQ2 Plan B; RQ3 exposure weights | **On disk** for Jul 2005–Dec 2011 (FI_CB_011_S2) and Jan 2013–Dec 2015 (FI_CB_011_S4); 2012 (FI_CB_011_S3) not located; 1996–2005 and 2016 onwards not yet fetched |
| Listed banks' annual reports and Pillar 3 disclosures (staging, restructuring, sector/regional exposures) | RQ2 Plan B; RQ3 calibration | Public; sector-level only; to be collected by hand |
| BOT policy documents (`02_policy_context/`) | Relief eligibility rules and timing | Done (26 rows; 18 verified from primary sources) |

**Expected in Tier 1 later:**
- **The Treasury 2027–30 appraisal round**, expected from 1 January 2027. The release date comes from press reports, not yet confirmed from an official source. This round enables the RQ1 difference-in-differences design. The files are revised in place, so the 2026-11-02 snapshot is the only record of the current round.

**Needs CP3 before use (registration, but free):**
- **Google Earth Engine or Copernicus Data Space.** Needed only to process raw Sentinel-1 into our own flood maps. The Global Flood Database and JRC GSW layers download without an account.
- **GISTDA API gateway.** Holds recurrent flood areas 2011–2023 and daily flood extents; requires an API key.
- **Department of Lands parcel polygons.** Require a written request; not needed for a sheet-level pilot.
- **OpenAlex API key.** Literature sweeps only.

## Tier 2: restricted data (RQ2 Plan A)

**Variables needed (minimum set).**
- *Loans:* loan identifier (pseudonymised); product; origination date; balance; payment status monthly (days past due); restructuring flag and type; TFRS 9 stage; ECL; write-off and recovery amounts with dates.
- *Collateral:* collateral value and valuation date; valuation method (internal, external or Treasury-based); location coarsened to a cadastral sheet or 500 m cell, never an exact address.
- *Borrowers:* coarse borrower characteristics (segment, income band) only where the design needs them.

**Access routes, in order of preference.**
1. **A partner bank.** A research data agreement between the bank and the host university. The bank de-identifies the data, and analysis takes place in the bank's secure environment or the university's secure environment. Outputs are checked before release.
2. **A credit bureau** (National Credit Bureau). A research agreement for pseudonymised payment histories. Collateral location is unlikely to be available, so this route supports a PD-only version of RQ2. *Status 2026-11-02:* no public research-access procedure found (web searches in English and Thai, time-boxed). Published NCB-based studies (e.g. PIER DP 253, Vannavanit et al. 2026; Chantarat et al. 2020) do not describe how access was obtained. Disclosure is governed by the Credit Information Business Act B.E. 2545, whose research provisions were not checked. Next step for the author: ask NCB and PIER in writing what route exists for a foreign-university researcher.
3. **An academic programme of a central bank or supervisor.** Any such route must run through formal programmes open to external researchers, under the governance rules in `ethics.md`, with explicit institutional approval.

**Legal basis.** Data sharing under Thailand's PDPA, with the controller de-identifying the data before transfer. For processing in the UK, UK GDPR and the university's data-protection procedures apply, as does a university ethics review (`ethics.md`).

**Readiness.** The schema will go in `03_data/schemas/`, matching synthetic data in `03_data/synthetic/`, and the RQ2 estimation code will run end to end on the synthetic data (Phase 5), so that the code is ready the day access is granted.

**Timeline risk.** Data agreements typically take 6–18 months. *This is a planning assumption, not a verified figure.* Approaches would start in year 1, and the RQ2 chapter is scheduled for years 2–3.

## Tier 3: data to collect

- **Hand-collected bank disclosures** from annual reports, 2011–2025: stage 2 and stage 3 shares, restructured loans, and regional or sector exposure, for each listed Thai bank.
- **Declared disaster zones and dates.** The 2011 and 2024 declarations by the Department of Disaster Prevention and Mitigation (DDPM) at district or subdistrict level, from public announcements. These give the relief eligibility geography for RQ2.
  - Search 2026-11-02 (time-boxed; provincial open-data catalogues `<province>.gdcatalog.go.th`, CKAN dataset pages and resource downloads only, crawl delay 10 s): no public 2024 district or subdistrict declaration list was found for the four RQ1 provinces. What is published by the provincial DDPM offices (Open Data Common): Chiang Rai `dataset_30_61` (districts flooded, yearly count) and `dataset_30_65` (villages flooded, yearly count); Phayao `dataset_50_13` (yearly counts of events, districts, subdistricts, villages); Nong Khai `dataset_dis_11` (village list with event dates, 2568 only); Nakhon Phanom `wf_data3_1_1` (flood-affected households by district, 2566–2568; 2567: 10 of 12 districts with households affected). None is a declaration list for 2024, so the RQ1 disaster-declaration sensitivity stays unscripted. Nong Khai is not in the 2025 sample, so its 2568 list is not used either. Next step: ask each provincial DDPM office (ศูนย์ข้อมูลสาธารณภัย) for the 2567 emergency-zone declarations (ประกาศเขตการให้ความช่วยเหลือผู้ประสบภัยพิบัติกรณีฉุกเฉิน).

## Plan B: if Tier 2 access is never granted

**RQ2 becomes a bank- and province-level study.**
- Listed banks' staging and restructuring around flood years, weighted by each bank's regional exposure.
- Provincial credit growth and loan-to-deposit dynamics after floods, using a difference-in-differences design on flood intensity.
- This is weaker: no LGD and no borrower-level identification. But it uses public data only, and it remains informative on timing (H-S5a).

**RQ3 does not depend on Tier 2.** It is calibrated with RQ1's appraisal gap, published elasticities [@albertazzi2026physical; @caloia2021flood] and public exposure data, with the uncertainty bands shown explicitly.

## Author notes

- The 2026-11-02 snapshot is a unique asset: the Treasury overwrites its files, so the snapshot is the baseline for the 2027 difference-in-differences design. Keep the SHA-256 manifest with the thesis materials.
- Never describe Tier 2 as "likely". Describe it as "sought, with a public-data Plan B already executed".

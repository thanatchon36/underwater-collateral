# Strand S4: Satellite and remote-sensing measurement of floods in economics

**Working draft for the author to rewrite, prepared 2026-11-02.** Labels: **[E]** established evidence, read in a verified source at the stated depth; **[H]** the author's hypothesis; **[S]** my speculation or judgement. References are in `01_literature/strands/S4.bib`, and the matrix is in `S4_matrix.csv`. Downloaded PDFs are in the session scratchpad, not in the project.

## 1. Synthesis

**What satellites measure.** [E] Flood maps measure *observed surface water at the moment of a satellite pass*. They do not measure depth, damage or the peak extent. The Global Flood Database (GFD) classifies MODIS optical imagery at 250 m. It uses multi-day composites to suppress cloud-shadow errors and masks permanent water with the JRC Global Surface Water layer (Tellman et al. 2021, Methods). Of 3,054 catalogued events, only 913 could be mapped. The rest were lost to persistent cloud, to floods that were too small or too brief, or to "complex terrain (e.g. dense forest or urban areas)". Against 30 m Landsat, mean accuracy is about 83%, and some maps understate the maximum extent (Tellman et al., preprint). SAR sees through cloud, but the Copernicus Global Flood Monitoring (GFM) product excludes "urban areas, dense vegetation" as zones where Sentinel-1 is not sensitive to flooding. Its manual states that this failure leads "more often to under-estimation than over-estimation" (GFM PUM 2025, §3.4). Specialised methods such as InSAR coherence (Chini et al. 2019) and multi-temporal statistics (DeVries et al. 2020) aim to close the urban gap, but they are event-specific.

**How economists use flood maps.** [E] Three designs recur. (i) *City- or district-level event indicators*: Kocornik-Mina et al. (2020) define a city as flooded if any grid point falls in a DFO inundation map. They do this precisely because those maps probably understate extent (cloud, incomplete dates), and they then exploit within-city elevation. (ii) *Combining satellite and survey exposure*: Noy et al. (2021) pair self-reported flooding in the Thai Socio-Economic Survey with satellite-based exposure to separate directly flooded households from "spillover" households after 2011. (iii) *Spatial RD at the flood edge*: Albertazzi et al. (2026) take the union of all Copernicus EMS activation maps as the treatment perimeter. They compare firms within about 300–500 m of it and run McCrary density and balance checks. They argue that address-level misclassification attenuates estimates towards zero.

**Measurement error at the boundary.** [E] Geographic RD is an RD with two running variables (Keele & Titiunik 2015). When the running variable is mismeasured, the first-stage discontinuity can disappear, and identification needs extra structure (Pei & Shen 2017; Davezies & Le Barbanchon 2017). [S] In a flood-edge RD, map error is concentrated exactly at the cutoff. Under-detection in built-up areas is also *non-classical*, because it correlates with building density and hence with collateral type and value. The attenuation argument in Albertazzi et al. therefore assumes non-differential error, and that assumption is less safe for Thai urban collateral than for European SMEs.

**Hazard maps versus realised floods.** [E] Global hazard models produce return-period maps at about 90 m. Benchmarked against UK and Canadian maps, they capture two-thirds to three-quarters of at-risk area (Sampson et al. 2015). Across six global models for Africa, extent agreement is only about 30–40% (Trigg et al. 2016). [S] Hazard maps (ex-ante risk, relevant to pricing and H2) and realised extents (ex-post shocks, relevant to PD/LGD and H1) are different objects, and neither should proxy for the other without validation.

**Implications for the project.** [S] The 2011 event can be measured only coarsely: MODIS at 250 m via the GFD, and plausibly Landsat at 30 m via the JRC GSW monthly history. Sentinel-1 and GFM start in 2014–15. The main risk is systematic under-detection of urban and peri-urban flooding, which is where mortgage and SME collateral sits. Mitigations to explore: triangulate with official Thai extents (GISTDA, unverified), use 2011 as a district or sub-district intensity treatment rather than a sharp edge, run donut-RD and fuzzy-RD variants, and validate post-2015 events against GFM's exclusion and likelihood layers.

### Practical data table (verified items only; "n.v." = not verified)

| Dataset | Sensor | Resolution | Period | Covers Thailand 2011? | Access / licence |
|---|---|---|---|---|---|
| Global Flood Database v1 (Cloud to Street / DFO) | MODIS Terra/Aqua (optical) | 250 m classification (GEE band table lists 30 m) | 2000-02-17 to 2018-12-10; 913 events | **Yes, as an event.** DFO 3850 (5 Aug 2011 – 9 Jan 2012, Thailand) and DFO 3795 (23 Mar – 10 Apr 2011, southern Thailand) are in the 913-event QC list. Whether the mapped extent covers lower Chao Phraya/Bangkok is n.v. | Google Earth Engine; CC BY-NC 4.0 (catalogue page); code MIT (GitHub) |
| JRC Global Surface Water, Monthly History v1.4 (Pekel et al. 2016) | Landsat 5/7/8 (optical) | 30 m, monthly | Mar 1984 – Dec 2021 | **Period covers 2011.** It maps water, not floods; the no-data share for Thailand in Oct–Nov 2011 is n.v. | GEE; "free of charge, without restriction of use" (Copernicus); attribution "Source: EC JRC/Google" |
| Sentinel-1 GRD | C-band SAR | 10 m (and coarser) | from 2014-10-03 | No | GEE; licence n.v. |
| Copernicus EMS Global Flood Monitoring (GFM) | Sentinel-1 SAR, 3-algorithm ensemble | 20 m | from 1 Jan 2015 | No | via GloFAS/EFAS portals; data terms "same rules" as those portals (terms page not read) |
| Copernicus EMS Rapid Mapping | Sentinel-1/2 among others (per Albertazzi et al.) | event-specific vectors | on-demand activations | No Thailand activation found (web search only, n.v.) | n.v. (JRC data portal rejected the request) |
| DFO event archive | media-based event catalogue; MODIS-based Rapid Response maps | event polygons | 1985 onwards (per Kocornik-Mina et al.) | Events listed (via GFD QC file) | archive index returned HTTP 404 on 2026-11-02 |

## 2. Per-paper entries

**Donaldson & Storeygard (2016), JEP 30(4).** *Read: abstract.* Q: what can satellite data do for economics? An introductory survey of remote-sensing science and economic applications. No findings beyond the scope statement are claimed. Standard citation for the method.

**Tellman et al. (2021), Nature 596.** *Read: intro and Methods of the Research Square preprint.* Q: how many people are exposed to observed floods, and is this rising? Data: 12,719 MODIS images, DFO event catalogue, GHSL population. Method: B2/B1 ratio and SWIR thresholds (standard and Otsu), 2–3-day composites, slopes above 5° masked, JRC permanent water removed; validated on 123 events with 30,685 Landsat points. Findings [E]: 913 events mapped; 2.23 million km² and 290 million people affected (published abstract); overall accuracy 83% for the 3-day standard algorithm; commission errors concentrated at northern latitudes; omission errors show no geographic pattern; Thailand is listed among countries where the proportion exposed grew. The paper lists urban areas, flash floods and cloud as reasons events could not be mapped.

**Pekel et al. (2016), Nature 540.** *Read: dataset documentation only.* The GEE catalogue says the dataset was built from 4,716,475 Landsat scenes, classified by an expert system into a monthly water history at 30 m, 1984–2021. It is used by the GFD as the permanent-water mask. Paper findings not read.

**Kocornik-Mina et al. (2020), AEJ: Applied 12(2).** *Read: AEJ abstract; intro and data section of CEP DP 1398 (2015).* Q: does activity move away from flood-prone urban areas? Data: DFO inundation maps (mostly 2003–08; 53 large floods, 1,868 cities, 40 countries in the DP), night lights, elevation. Method: city-level flood indicator plus within-city elevation contrasts. Findings [E]: low-elevation areas flood more yet hold more activity and recover as fast; there is little permanent relocation except in recently populated areas. Measurement [E]: the authors state that DFO maps "very likely" understate extent because of cloud cover and incomplete dates, so they do not use within-city extent.

**Albertazzi, Djekic & Ponte Marques (2026), ECB WP 3224.** *Read: intro and Sections 3–4.* Q: how do floods affect lending, rates, collateral and default? Data: AnaCredit, CEMS vector maps (Sentinel-1/2), Orbis, ECB physical-risk indicator; four European floods 2021–24. Method: union of all CEMS maps as the perimeter; Google-geocoded headquarters; sample within 2 km, MSE-optimal bandwidths of about 300–500 m; McCrary and balance tests; Khwaja–Mian firm-time fixed effects. Findings [E]: lending rises 3.5–5% in the flood quarter and then reverses; default rises about 0.7 pp cumulatively; demand dominates; main banks lend about 10 pp more but tighten collateral. Measurement [E]: inside-perimeter status is treated as exposure, not damage, and the error is argued to attenuate.

**Noy, Nguyen & Patel (2021), EDCC 69(2).** *Read: abstract.* Q: what were the direct and spillover effects of the 2011 Thai flood on households? Data: repeated Thai SES waves with a 2012 flood module, plus "external exposure indicators from satellite images". Outcomes: income, expenditure, assets, debt and savings, by socio-economic group. Specific estimates were not read. **The closest Thai use of satellite exposure; read the full paper next.**

**Gandhi et al. (2022), NBER WP 30137.** *Read: abstract (revised SSRN version).* Q: are cities adapting to floods? Data: 3,931 major floods (2000–23), 9,468 cities, monthly night lights. Findings [E]: night-light declines are 3.5 times larger in low-income countries; impacts are falling over time; prior exposure reduces impacts. The flood-extent source is not stated in the abstract.

**Keele & Titiunik (2015), Political Analysis 23(1).** *Read: abstract.* Formalises geographic RD as RD with two running variables, clarifies the differences specific to geography, and proposes estimation and validation with pre-treatment covariates.

**Pei & Shen (2017), in *Regression Discontinuity Designs*.** *Read: abstract.* With a mismeasured assignment variable, the first-stage discontinuity may vanish. The paper gives sufficient conditions for identification in discrete and continuous cases.

**Davezies & Le Barbanchon (2017), J. Econometrics 200(2).** *Read: abstract.* With continuous measurement error in the running variable, identification fails. They give a consistent estimator under non-differential error when an auxiliary sample reveals the discrepancy.

**Sampson et al. (2015), WRR 51(9).** *Read: abstract.* A global return-period hazard model at about 90 m (56°S–60°N). It captures two-thirds to three-quarters of benchmark at-risk area (UK, Canada); mean absolute error in flooded fraction is about 5% at about 1 km. The authors note that urban performance depends on terrain data.

**Trigg et al. (2016), ERL 11.** *Read: intro.* Compares six global hazard models (CaMa-UT, GLOFRIS, ECMWF, JRC, SSBN, CIMA-UNEP) for Africa: about 30–40% agreement in extent, with large differences in deltas, arid zones and wetlands. Global models have had "limited validation against observed flood flows or extents".

**Rentschler, Salhab & Jafino (2022), Nat. Commun. 13.** *Read: abstract.* 1.81 billion people (23%) are exposed to 1-in-100-year floods, 89% of them in low- and middle-income countries. The hazard data source is not identified in the abstract.

**Chini et al. (2019), Remote Sensing 11(2).** *Read: abstract.* Uses Sentinel-1 InSAR coherence, after building detection, to map floodwater in urban Houston (Harvey 2017), evaluated against VHR optical imagery, crowdsourced points and a FEMA model.

**DeVries et al. (2020), RSE 240.** *Read: abstract (truncated).* A GEE algorithm using multi-temporal Sentinel-1 statistics plus Landsat water probabilities. Area-normalised accuracy is 89.8 ± 2.8% for Houston, 1.6–9.8 pp better than simple thresholding.

**Komori et al. (2012), HRL 6.** *Read: intro.* The 2011 Chao Phraya flood: 813 dead; flood volume about 15 billion m³; damaged agricultural land peaked at 18,291 km² on 14 Nov 2011 (Thai MoI figure as cited); 7 industrial estates and 804 companies inundated. Useful for validating any 2011 extent.

**GFM Product User Manual (2025).** *Read: Sections 1–3 and FAQ 7.1.7.* Sentinel-1 ensemble (flooded if at least 2 of 3 algorithms agree), 20 m, archive from 1 Jan 2015, outputs within 8 hours. The Exclusion Mask covers no-sensitivity areas (urban, dense vegetation), water look-alikes, topography, radar shadow and low coverage. Likelihood values (0–100%) are given outside the mask.

## 3. Hypotheses and speculation kept separate

- [H] H1/H3 in `CLAUDE.md` rely on collateral-level exposure. Satellite maps can deliver this for post-2015 events at 20 m, and only coarsely for 2011.
- [S] Differential misclassification (urban under-detection) may bias boundary designs towards zero *or* away from it, depending on how detection correlates with collateral quality. Validate before claiming attenuation.
- [S] A 2011 design may be more credible as a continuous intensity treatment (share of sub-district flooded, flood duration from the GFD `duration` band) than as a sharp edge.

## 4. Unverified / not read

- [UNVERIFIED] Liew, Gupta, Chia & Ang (2016), *Geomorphology* 262:112–122, doi 10.1016/j.geomorph.2016.03.022, on the 2011 lower Chao Phraya flood from satellite images. Metadata only; no abstract was available. A high-priority read.
- [UNVERIFIED] Kwak et al. (2012, IGARSS) on MODIS flood volume, Chao Phraya; Sayama et al. (2015, NHESS; 2017, J. Flood Risk Mgmt) on simulated 2011 inundation. Abstracts were seen only in Crossref search output, so they are not used.
- [UNVERIFIED] Forslid & Sanctuary (2023, SSRN 4348160) on the 2011 Thai flood and Swedish firms; Poapongsakorn, Meethom & Pantakua (2014) on Thai households. Metadata only.
- [UNVERIFIED] GISTDA 2011 flood extent products and their terms (site unreachable during scoping).
- [UNVERIFIED] Whether SSBN (Sampson et al.) is the model now sold as Fathom, and Fathom's documentation and licence. Not checked.
- [UNVERIFIED] Copernicus EMS Rapid Mapping start date (2012, per a search snippet only), licence, and the absence of a Thailand activation.
- [UNVERIFIED] Whether GFD event 3850's mapped extent covers Bangkok and the lower Chao Phraya. The repository's population file gives an "area" of 2.03 × 10¹⁰ for Thailand, units undocumented (about 20,300 km² if m²), and about 2.18 million exposed. Visual inspection in GEE is needed.
- [UNVERIFIED] The no-data share of the JRC GSW monthly history for Thailand in Oct–Nov 2011. Landsat 7 scan-line gaps and cloud cover are plausible issues but were not checked.
- Not read: the full texts of Donaldson & Storeygard (AEA returned 403) and Pekel et al. (paywall).

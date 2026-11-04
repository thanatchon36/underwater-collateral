# Strand S2: Physical climate risk in property and collateral values

**Working draft, 2026-11-02, for the author to rewrite in their own voice.** Strand question: is flood or climate hazard capitalised into property prices and lenders' collateral valuations, and how fast?

Labels: **[E]** established evidence, from a verified source at the stated read depth; **[H]** the author's hypothesis; **[S]** my speculation or judgement. Bibliography: `S2.bib`; matrix: `S2_matrix.csv`. 17 verified sources (one more than the target, because the brief named several of them). Read at `full`: 2; at `intro`: 4; at `abstract`: 11.

---

## 1. Synthesis

**What is established [E].** In the United States and Europe, flood and sea-level-rise (SLR) exposure is capitalised into transaction prices, but incompletely and with a lag. The estimates cluster in single digits: about 7% for SLR-exposed homes (Bernstein et al. 2019), 8% for undamaged New York flood-zone homes five years after Sandy (Ortega & Taşpınar 2018), and 11% for homes newly mapped into the floodplain after escaping Sandy (Gibson & Mullins 2020). A meta-analysis of 364 estimates proposes −4.6% for inland 100-year floodplains (Beltrán et al. 2018). Capitalisation is driven by salience. Discounts appear after floods and fade within 5–6 years (Bin & Landry 2013); they depend on buyer beliefs (Baldauf et al. 2020) and on disclosure rules (Hino & Burke 2021); and in Florida, falling sales volumes ran about five years ahead of a 5–10% relative price decline (Keys & Mulder 2020). On the lender side, the most relevant result is that UK lender valuations did not follow the 2.6–4.2% fall in sale prices after the 2013–14 floods, which produced an upward valuation bias of about 3% (Garbarino & Guin 2021). Mortgage terms move little ex ante: Dutch credit terms are indistinguishable by flood risk, and only a roughly six-month premium follows a flood (Götz et al. 2025). Where lenders keep uninsurable residual risk, however, they ration through lower LTVs (Sastry 2026).

**What is contested [E/S].** Whether long-run SLR risk is priced at all is disputed: Murfin & Spiegel (2020) report precise nulls, while Bernstein et al. (2019) and Baldauf et al. (2020) find discounts. Hino & Burke's preferred flood-zone discount (−2.1%, confidence interval including zero) lies well below what insurance costs imply. **[S]** The disagreement turns on whether exposure is ex-ante hazard or realised damage, on how beliefs and amenities are controlled for, and on the time horizon. Whether banks revalue collateral is also unsettled. One Belgian bank revalued exposed collateral downward after the 2021 floods (Van Gerwen et al. 2025, abstract only), whereas UK lenders did not. Keys & Mulder (2020) find little change in denial or securitisation. Ouazad & Kahn ("Mortgage Finance and Climate Change", *RFS* 2022), the main paper claiming securitisation-based risk shifting, is **retracted** and is not used as evidence here.

**What is missing for an emerging-market, collateral-level study [E/S].** The Thai evidence is a single short paper. Sawada et al. (2018, read in full) find that after 2011, industrial land prices fell by about 6–8% and townhouse prices by 4.85%, while residential and commercial land, detached houses and condominiums showed no significant decline. The authors attribute this to illiquidity and frictions. Their treatment is defined at province level and their prices are district series. There is no ex-ante hazard measure, no satellite exposure and no credit outcome. The other Asian studies are cross-sectional or descriptive: Hangzhou land sales show an 8.62% discount in a spatial model (Wei & Zhao 2022), and Shiga official land prices show no response to a hazard map (Mori et al. 2016). African evidence relies on self-reported risk and rents (Erman & Dallmann 2022). **[S]** No study I read links satellite-measured flood exposure of individual collateral to valuation, LTV or credit outcomes outside Europe and the US.

**Official appraisal values versus transaction prices.** Of the 17 sources, only **Mori et al. (2016)** uses official appraised land values: 366 standard sites of Japan's Prefectural Land Price Survey (都道府県地価調査). It is a short, descriptive, non-refereed report covering two years. Garbarino & Guin (2021) and Van Gerwen et al. (2025) use *lender* valuations: bank appraisals for refinancing and internal or external collateral valuations. Wei & Zhao (2022) use land-sale transaction prices; they argue that China's government benchmark land prices already embed flood hazard, but from what I read they do not estimate this. Sawada et al. (2018) use JETRO survey prices and district series from Thailand's Agency for Real Estate Affairs (AREA), not Treasury Department (กรมธนารักษ์) assessed values. **[S]** A causal study of whether *official* appraisal values, such as Thailand's Treasury Department assessed prices, absorb flood hazard and flood events therefore appears to be absent. This is the most defensible public-data contribution for Plan B, conditional on verifying access to historical Treasury appraisal rounds.

---

## 2. Per-paper notes

Ordered by relevance to the project. "Read" gives the read depth. Only what was read is reported.

### Closest to the project

**Sawada, Nakata, Sekiguchi & Okuyama (2018), *Economics Bulletin* 38(1):89–97.** Read: full (open AccessEcon PDF).
- Question: did the 2011 Thai floods lower land and real estate prices?
- Data: JETRO land-price surveys for about 40 industrial estates (10 rounds, October 2008 to November 2012; seven flooded estates in Ayutthaya and Pathum Thani). AREA annual prices for 2010–2013 for 43 districts in nine provinces, covering industrial, residential and commercial land, detached houses, townhouses and condominiums.
- Identification: difference-in-differences with estate or district fixed effects. Treated provinces are Ayutthaya, Pathum Thani and Nonthaburi; controls are Chon Buri, Prachin Buri, Samut Prakan and Saraburi. Pre-trend test on JETRO; balancing test only on AREA, which has a single pre-flood year. Bangkok districts are in the AREA data but not in either group as stated.
- Finding [E]: industrial land fell 8.27% of the post-flood mean (JETRO) and 6.49% (AREA; 9.43% in 2012). Townhouses fell 4.85%. Residential and commercial land, detached houses and condominiums showed no significant effect. Interpreted as illiquidity or frictions.
- Note [S]: the sample is small (60–172 observations per AREA regression) and the treatment coarse. A null for residential land is not evidence that hazard is priced away; it may reflect appraisal smoothing in the AREA series.

**Garbarino & Guin (2021), *J. Financial Stability* 54:100874; BoE Staff WP 856 (2020).** Read: intro (WP PDF).
- Question: do lenders mark housing collateral to market after a severe flood?
- Data: 119,239 English properties transacted at least twice around the 2013–14 winter floods. 38,747 refinancings with lender valuation, loan amount and rate. Environment Agency flood outlines and maps; JBA Matrix Scores; postcode-unit level.
- Identification: repeat-transaction DiD comparing flooded (≥50 days, <50 days) and risk-increase postcode units with unaffected units, and sale prices with refinancing valuations. Propensity-score matching; postcode-district × year fixed effects. Refinancing timing is taken as quasi-exogenous (end of fixed-rate periods).
- Finding [E]: prolonged flooding lowers sale prices by 2.6–4.2%, but valuations do not follow (bias +2.9% to +3.2%). Loan amounts are unaffected; the rate response is not robust. Flood-risk increases slightly raise prices. Low-risk borrowers select into high-risk areas.

**Van Gerwen, Degryse, Ongena & Scopelliti (2025), "Flooded Collateral", GRASFI 2025; SSRN 2026 version retitled.** Read: abstract (GRASFI lists no paper file; SSRN not accessed).
- Question, data and identification: how one major Belgian bank values flood-exposed real-estate collateral and lends. Collateral is matched to Flemish flood maps, with the 2021 floods as a salience shock.
- Finding [E]: collateral exposed to pluvial or SLR risk is revalued downward after 2021. Internal staff adjust more than external experts, and the bank shifts towards internal models. Floating rates rise for exposed firms, but exposure is not reduced.

**Sastry (2026), *RFS* 39(8):2317–2357.** Read: abstract.
- Question: who bears uninsured flood risk in Florida mortgages? Identification uses NFIP coverage limits and staggered flood-map updates.
- Finding [E]: lenders require lower LTVs at origination for uninsurable flood risk. Delinquency equalises inside and outside flood zones, and the borrower mix shifts towards richer, higher-credit-quality households.

**Mori, Nishimura & Taniguchi (2016), *Reports of the City Planning Institute of Japan* 14(4):276–280 (in Japanese).** Read: full.
- Question: did Shiga Prefecture's 2012 detailed flood-risk map (地先の安全度マップ) change land prices?
- Data: 366 sites of the official Prefectural Land Price Survey, 2012 and 2014. Map inundation depths for 1/10-, 1/100- and 1/200-year rainfall.
- Identification: cross-tabulation and OLS of the 2012 price level and the 2012–14 change, with location controls. There is no control group, so the design is descriptive.
- Finding [E]: sites with inundation potential (1/100 and 1/200-year) whose prices nonetheless rose make up more than 10% of all sites. In 2012, deeper 1/10-year inundation is positively associated with price (5% level). The map's effect on 2012–14 changes is very small. Authors recommend that land appraisals take hazard into account.

**Keys & Mulder (2020), NBER WP 27930.** Read: intro.
- Question: dynamic capitalisation of SLR risk in coastal Florida housing and mortgage markets, 2001–2020.
- Data: transactions (cash and mortgaged), mortgage applications and flood insurance at tract level; 771 coastal tracts.
- Identification: matching DiD (synthetic control, nearest neighbour, generalised propensity score) against a 2001–2012 baseline.
- Finding [E]: from 2013 to 2018, volumes in the most exposed tracts fell 16–20% relative to matched tracts while prices tracked them; by 2020, prices were 5–10% below trend. Denial, securitisation and refinancing changed little, so the authors favour a buyer-demand explanation.

**Hino & Burke (2021), *PNAS* 118(17).** Read: intro of NBER WP 26807 (2020) version.
- Question: does flood-zone information affect US property values?
- Data: CoreLogic deeds for all states, 1996–2017; FEMA Q3 and current maps.
- Identification: house-level panel of rezoning (preferred), small-area DiD, and cross-section.
- Finding [E] (WP figures): panel discount −2.1% (95% CI −4.9% to 0.8%); DiD −1.4%; cross-section +1.7%. The efficient discount implied by insurance costs is about −6.9% at a 5% discount rate. The penalty is larger for commercial buyers and in strict-disclosure states.

### Capitalisation and salience (US, Europe)

**Bin & Landry (2013), *JEEM* 65(3):361–376.** Read: abstract. Hedonic DiD in Pitt County, NC [E]: no flood-zone discount before Hurricane Fran (1996); −5.7% after Fran and −8.8% after Floyd. A later-sample premium of 6.0–20.2% fades and essentially disappears 5–6 years after Floyd.

**Ortega & Taşpınar (2018), *J. Urban Economics* 106:81–100.** Read: abstract. NYC parcel sales 2003–2017 with FEMA damage data [E]: damaged homes fell 17–22% immediately, then partly recovered. Undamaged flood-zone homes developed a penalty of 8% by 2017 with no recovery, which the authors interpret as learning.

**Gibson & Mullins (2020), *JAERE* 7(6):1069–1111.** Read: abstract. NYC transactions 2003–2017, DiD for three signals [E]: Biggert-Waters premium reform, Sandy and new floodplain maps are all negative. Properties newly mapped in after escaping Sandy fell 11%. The maps' belief effect is comparable to the insurance reform.

**Bernstein, Gustafson & Lewis (2019), *JFE* 134(2):253–272.** Read: abstract. [E] SLR-exposed homes sell about 7% below equivalent unexposed homes equidistant from the beach; the discount is growing and is driven by sophisticated buyers and worried communities. There is no rent effect, and a 4% discount applies even for homes not projected to flood for almost a century.

**Baldauf, Garlappi & Yannelis (2020), *RFS* 33(3):1256–1295.** Read: abstract. [E] Homes projected to be underwater sell at a discount in "believer" neighbourhoods relative to "denier" ones.

**Murfin & Spiegel (2020), *RFS* 33(3):1217–1255.** Read: abstract. Identification from vertical land motion [E]: precisely estimated nulls, implying limited price effects of SLR.

**Beltrán, Maddison & Elliott (2018), *Ecological Economics* 146:668–685.** Read: abstract. Meta-analysis of 37 works and 364 estimates [E]: estimates range from −75.5% to +61.0%. Coastal estimates are positive, likely because of omitted amenities, and show publication bias. Time since the last flood matters. Inland 100-year floodplain: −4.6%.

### Mortgage-market responses

**Götz, Mager & Zietz (2025), *European Financial Management* 32(2):413–437.** Read: abstract. More than 100,000 securitised Dutch mortgages, 2013–2023 [E]: credit terms do not differ by flood risk. After the 2021 river flood, lenders raised rate premiums for about six months and partly reduced LTVs.

(Keys & Mulder 2020 and Sastry 2026 above also cover this sub-question.)

### Asia and emerging markets

**Wei & Zhao (2022), *Land* 11(10):1612.** Read: intro plus data and discussion sections.
- Data and identification: 424 residential land-plot sales in Hangzhou, 2007–2020 (China Land Market Network), with a 2017 municipal flood-risk map; spatial Durbin model.
- Finding [E]: high-risk plots sell at an 8.62% discount. A non-spatial OLS model gives a positive flood coefficient. The authors argue that the government's benchmark land price already accounts for flood hazard and that no public hazard maps were available.

**Erman & Dallmann (2022), World Bank PRWP 10127.** Read: abstract. Hedonic rent regressions in four African cities using self-reported exposure [E]: rents are 14–56% lower in Accra, Antananarivo and Addis Ababa, but higher in Dar es Salaam. Only 12% of households in flood-prone areas knew of the risk when they moved in.

(Sawada et al. 2018 and Mori et al. 2016 above are the Thai and Japanese entries.)

### Retracted

**Ouazad & Kahn, "Mortgage Finance and Climate Change: Securitization Dynamics in the Aftermath of Natural Disasters", *RFS* 35(8):3617–3665 (2022): RETRACTED** (retraction notice doi:10.1093/rfs/hhaf003, recorded in `S0_scoping.bib`). Excluded as evidence. Keys & Mulder (2020) cite its 2020 working-paper version; that citation does not rehabilitate it.

---

## 3. Author's hypotheses this strand informs [H]

- H2 (from the feasibility memo): collateral valuations and ECL do not fully reflect ex-ante flood hazard. S2 supports testing this on valuations first (Garbarino & Guin; Mori et al.).
- H2a (new, for Plan B): official Thai appraisal values (Treasury Department assessed prices) adjust to flood events more slowly than market or lender values, and not at all to ex-ante hazard.

## 4. My speculation [S]

- Thailand's appraisal cycle may mechanically delay capitalisation, which would make "how fast" an institutional question rather than a behavioural one. This is untested and depends on revaluation frequency, which I have not verified.
- The null for residential land in Sawada et al. (2018) and the frozen valuations in Garbarino & Guin (2021) are consistent with one mechanism: valuation smoothing that keeps LTVs low on paper. If so, the LGD understatement is largest just after floods.
- Because flood insurance is thin in Thailand, the Sastry (2026) channel of rationing by LTV for uninsured risk should, if lenders price risk at all, be stronger there than in Florida.

---

## 5. Unverified / not read

- **[UNVERIFIED]** Sawada, Nakata & Sekiguchi (2014), "Natural disasters, land price, and location of firms: Evidence from Thailand", RIETI DP 14-E-029. Seen only in the reference list of Sawada et al. (2018); not opened.
- **[UNVERIFIED]** A Japanese-language Nihon University paper estimating a hedonic land-price formula for Khon Kaen with a flood-occurrence gap (cst.nihon-u.ac.jp, F1-5). Seen only in a web-search result; not opened.
- **[UNVERIFIED]** A *Journal of Applied Business Research* article said, in a search summary, to link the 2011 floods to reduced new housing supply and higher prices in Thailand. Not opened.
- Giglio, Maggiori, Rao, Stroebel & Weber (2021), *RFS* 34(8):3527–3571, doi:10.1093/rfs/hhab032. Metadata and abstract verified via Crossref/OpenAlex. The abstract concerns long-run housing discount rates, not hazard capitalisation, and the 2015 NBER WP 21767 I read contains no flood analysis. Any flood-zone evidence in the published version is therefore **not read** and not claimed. Excluded from the matrix.
- Hsu, Ho & Tsai (2024), EGU General Assembly abstract (doi:10.5194/egusphere-egu24-9505), Kaohsiung 2018 flood, reported −8.6% house prices. Conference abstract only, so it fails the inclusion criteria; listed for follow-up.
- Chiang Hsieh (2021), *Land Use Policy* 106:105443, "Is it the flood, or the disclosure?". Metadata only; abstract not available to me.
- Skouralis, Lux & Andrew (2024), *J. Housing Economics* 66:102027 (property-level flood score); Menéndez et al. (2024), *J. Housing Economics* 66:102022 (Basque Country); Soni (2026), *Real Estate Economics* (SLR and commercial real estate, abstract seen via OpenAlex, about a 5–6% discount). Not included, for time; candidates for the merged review.
- Hidano, Hoshino & Sugiura (2015), *Regional Science and Urban Economics* 53:113–122 (seismic hazard information, spatial RD, Tokyo). Metadata only.
- The full texts of Bernstein et al., Baldauf et al., Murfin & Spiegel, Sastry, Götz et al. and Van Gerwen et al. were not read. SSRN is blocked to scripts, the Wiley PDF returned 403, and GRASFI links no file. Their entries are abstract-only.
- Whether Thailand's Treasury Department appraisal rounds are available historically at parcel or zone level, and how often they are revised: **not checked** in this strand; this belongs to the data inventory.

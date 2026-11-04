# Literature review: flood risk, collateral and credit risk

**Working draft, 2026-11-02, for the author to rewrite in their own voice.**

This review covers the five strands defined in `protocol.md`. It is written from the strand notes in `strands/S1–S5_notes.md`, which give per-paper detail, read depth and the "not read" lists. Citations use citekeys from `references.bib` (e.g. [@albertazzi2026physical]). Of the 83 sources in `lit_matrix.csv`, 9 were read in full, 27 at introduction depth and the rest at abstract depth. A finding attributed to an abstract-only source is no stronger than the abstract.

Three kinds of statement are kept apart:
- Plain statements of findings are **established evidence**, reported only as far as the source was read.
- Paragraphs headed *Interpretation* are my **speculation or judgement**.
- Labels **H1–H3** refer to the **author's working hypotheses**:
  - **H1:** flood exposure of collateral raises PD and LGD.
  - **H2:** collateral valuations and ECL do not fully reflect ex-ante flood hazard.
  - **H3:** geographic concentration makes bank capital more flood-sensitive than standard stress tests assume.

## 1. Introduction and scope

The proposed project asks whether physical flood risk is reflected in the valuation of collateral, in credit risk and in banks' provisioning and capital. The setting is an emerging market where insurance is thin and debt relief, not insurance, is the main buffer. The causal chain runs from flood exposure of a piece of collateral, through borrower default (PD) and loss given default (LGD), to IFRS 9 staging and expected credit loss (ECL), and finally to bank capital. Five literatures each cover one link of that chain, and none covers the chain as a whole:

- **S1** studies what floods and other disasters do to bank credit and bank balance sheets.
- **S2** studies whether hazard is priced into property and collateral values.
- **S3** studies how supervisors and banks translate hazard into credit-risk parameters, provisions and stress-test losses.
- **S4** studies what satellite flood maps can and cannot measure, and how economists have used them for identification.
- **S5** studies relief, forbearance and the insurance gap, which shape the default response in emerging markets, together with the evidence on Thailand's 2011 floods.

The review ends with a cross-strand synthesis (Section 7). The proposal's gap statement is in `gap_statement.md`.

Coverage caveat: the searches ran under heavy API rate limits. OpenAlex's daily budget was exhausted and Semantic Scholar returned HTTP 429 for most of the session, so backward and forward snowballing through citation networks was not completed. SSRN full texts were not accessible to scripts. Absence-of-evidence claims below ("no study found") are therefore weaker than presence claims. They should be re-tested in a targeted search before the proposal is finalised.

## 2. Disasters, floods and bank credit (S1)

### 2.1 Credit demand rises, and capital determines who meets it

The most consistent finding in the banking literature is that disasters raise local credit demand, and that lenders with capital, diversification and local relationships meet it.

- **US mortgages.** Multi-market banks fund higher mortgage demand after a disaster by cutting lending in connected, unaffected markets. For small banks, credit there falls by a little under 50 cents per extra dollar lent in the shocked area; cuts fall outside branch (core) markets [@cortes2017tracing].
- **German regional banks, 2013 Elbe flood.** Banks exposed through their borrowers lent about 3% more, mainly unsecured credit funded by local deposits, while connected flooded firms borrowed 16% more. Exposed banks without access to a geographically diversified banking group took on more credit risk and lost capital [@koetter2020borrowers].
- **Capital as the constraint.** Firms tied to a strongly exposed bank in the lowest capital quartile cut borrowing by 6.6% and tangible assets by 6.9%. After a disaster, banks reduce exposure to unaffected but disaster-prone areas [@rehbein2022flooded]. In US syndicated lending, banks reallocate credit away from distant regions, more so when they hold less capital [@ivanov2022bank]. Damage to banks' own operations lowers their client firms' investment: after the Kobe earthquake, firms outside the quake area whose main bank was inside it invested less [@hosono2016natural].

The closest design to the proposed project is Albertazzi, Djekic and Ponte Marques [@albertazzi2026physical]. They combine euro-area loan-level data (AnaCredit) with Copernicus satellite flood perimeters for four floods between 2021 and 2024, using a spatial regression discontinuity at the flood boundary with bandwidths of roughly 300–500 m. Their findings:
- Credit to firms just inside the perimeter rises by 3.5–5% in the flood quarter and then reverses, with no significant cumulative change.
- Default on pre-existing loans rises by about 0.7 percentage points over two quarters, roughly doubling the baseline.
- Demand rather than supply drives the lending response. Main banks extend more credit but tighten collateral requirements.

### 2.2 Default rises, modestly, where insurance and aid exist

Default rises after floods, but in insured, high-income settings the rise is small relative to the physical destruction. After Hurricane Katrina, 90-day delinquency among the most flooded New Orleans residents was about 10% higher for a year. Total debt fell because flood-insurance proceeds, on which lenders co-sign, were used to repay mortgages [@gallagher2017household]. European SMEs in high flood-risk areas pay a small premium (about 6.4 bp), and firms in flooded counties default more [@barbaglia2024flooded].

### 2.3 Contested: how much do disasters hurt banks?

The bank-level evidence is divided.
- **Lasting damage.** Noth and Schüwer find lower Z-scores, higher non-performing asset and foreclosure ratios and lower equity for about two years after US weather disasters [@noth2023natural]. After Katrina, independent banks raised capital ratios and shifted towards government securities [@schuwer2019banks].
- **Resilience.** Blickle, Hamerling and Morgan conclude that weather disasters are generally not very damaging to US banks. A single-county bank would fail only after a disaster about 6.7 standard deviations beyond the 95th-percentile event [@blickle2025bad]. They attribute this resilience to higher loan demand and to local banks' knowledge of flood risk that official maps understate, not to federal aid. Their calculation is in effect a published reverse stress test on a hazard variable, and it is the nearest analogue in this strand to what the project proposes.
- **Setting-dependence.** Cross-country evidence covering more than 160 countries finds that large disasters reduce banks' distance-to-default, with effects conditioned on supervisory quality and on financial and economic development [@klomp2014financial].

### 2.4 Emerging markets: the lending response differs

The few emerging-market studies point to a different lending response.
- An Ecuadorian microfinance lender restricted access after volcanic eruptions, except for known clients [@berg2012access].
- Eastern Caribbean banks faced deposit withdrawals after hurricanes and cut lending, without evident deterioration in defaults or capital [@brei2019impact].
- US banks cut cross-border lending to disaster-hit countries by about 9% over two years, driven by banks with weak prior ties [@ilabaca2024global].
- After Iran's 2019 flood, local branches bridged the gap until government aid arrived, favouring farmers with stronger branch relationships [@abedifar2022flood].

*Interpretation.* The strand gives strong support for the PD side of H1 and for the role of capital and diversification behind H3, but nothing on LGD. Every paper measures delinquency, non-performing loans, charge-offs or stability indices. None measures recoveries, collateral revaluation or loss severity, and none studies IFRS 9 staging or provisions. The emerging-market evidence is bank-level, country-level or drawn from a single lender. I found no econometric study of bank credit after Thailand's 2011 floods. The demand-led, quickly reversing pattern found in Europe may not carry over to a flood that is large relative to national bank portfolios, as in Bangkok and its surrounding provinces in 2011. There, a regulator-endorsed moratorium may have delayed recognised default. That would shift the flood's footprint from PD timing towards LGD and from stage 3 towards stage 2.

## 3. Physical climate risk in property and collateral values (S2)

### 3.1 Capitalisation is real but incomplete, lagged and salience-driven

In the United States and Europe, flood and sea-level-rise exposure is capitalised into transaction prices, incompletely and with a lag. Estimates cluster in single digits:
- about 7% for homes exposed to sea-level rise [@bernstein2019disaster];
- an 8% penalty that emerged for undamaged New York flood-zone homes in the years after Hurricane Sandy, with no recovery by 2017 [@ortega2018rising];
- an 11% fall for properties newly mapped into the floodplain after escaping Sandy [@gibson2020climate];
- a meta-analytic estimate of −4.6% for inland 100-year floodplains, within a very wide range of estimates and with signs of publication bias in coastal studies [@beltran2018flood].

Salience matters:
- In North Carolina, no flood-zone discount existed before Hurricane Fran. Discounts of 5.7% and then 8.8% appeared after successive hurricanes and faded within five to six years [@bin2013changes].
- In coastal Florida, transaction volumes in the most exposed areas fell 16–20% between 2013 and 2018 while prices tracked controls. Relative prices fell 5–10% only by 2020 [@keys2020neglected].
- Discounts depend on buyers' beliefs about climate change [@baldauf2020does] and on disclosure rules [@hino2021effect].

### 3.2 Contested: is long-horizon risk priced at all?

Whether long-horizon risk is priced at all is disputed. Murfin and Spiegel report precisely estimated nulls for sea-level-rise exposure, identified from vertical land motion [@murfin2020risk]. Hino and Burke's preferred panel estimate of the flood-zone discount (−2.1%, with a confidence interval that includes zero) is well below the discount implied by insurance costs [@hino2021effect].

*Interpretation.* The disagreement appears to turn on three choices: whether exposure is ex-ante hazard or realised damage, how beliefs and amenities are controlled for, and the time horizon. The project should keep these three apart rather than pool them.

### 3.3 Lenders' valuations lag the market

For credit risk, what matters is lenders' valuations, not transaction prices.
- After the 2013–14 English floods, prolonged flooding lowered sale prices by 2.6–4.2%, but lender valuations at refinancing did not follow. The result was an upward valuation bias of about 3%, with no offsetting change in loan amounts [@garbarino2021high].
- One Belgian bank revalued flood-exposed collateral downward after the 2021 floods, with internal staff adjusting more than external valuers, but did not reduce its exposure [@vangerwen2025flooded] (abstract only).
- Dutch mortgage terms do not differ by flood risk ex ante. A rate premium of roughly six months followed the 2021 river flood [@gotz2025how].
- Where lenders retain uninsurable flood risk in Florida, they ration through lower loan-to-value ratios at origination [@sastry2026who].
- Ouazad and Kahn's study of securitisation after disasters (*RFS* 2022) has been **retracted** and is not used as evidence.

### 3.4 Asia and Thailand

Evidence from Asia is sparse.
- **Thailand.** The only Thai study found is Sawada, Nakata, Sekiguchi and Okuyama [@sawada2018land], read in full. After the 2011 floods, industrial land prices fell by about 6–8% and townhouse prices by 4.85%, while residential and commercial land, detached houses and condominiums showed no significant decline. Their treatment is defined at province level and their price data are district series. They have no ex-ante hazard measure, no satellite exposure and no credit outcomes.
- **China.** In Hangzhou, high-risk land plots sold at an 8.62% discount in a spatial model [@wei2022effect].
- **Japan.** The only study found that uses *official appraised* land values: in Shiga Prefecture, a detailed flood-risk map had very little effect on official survey prices over two years [@mori2016flood]. This is a short, descriptive, non-refereed report.

*Interpretation.* Whether official appraisal values capitalise flood hazard or flood events is, as far as these searches reach, an open causal question. This matters for credit risk because appraisal values and lender valuations, not transaction prices, enter LTV and LGD calculations. The Sawada et al. null for residential land and the frozen UK valuations fit a single mechanism: valuation smoothing keeps LTVs low on paper, so LGD is understated most just after a flood. That is H2 restated for collateral. Thailand's Treasury Department publishes parcel-level official appraisal prices as open data (`03_data/inventory_R3.md`), which makes this question answerable with public data.

## 4. Climate risk in credit-risk models, ECL and stress testing (S3)

### 4.1 A common supervisory template

Supervisory climate exercises share a common template for acute physical risk. A hazard footprint becomes property damage. The damage lowers collateral value, and the higher LTV raises LGD and, to a lesser degree, PD:

- **ECB 2022 stress test.** The flood scenario shocks real-estate prices in flood-risk regions mapped at NUTS3 level, so LTVs and then LGDs rise [@ecb2022climate].
- **Federal Reserve pilot.** Most participating banks reduced property values by uninsured damage and ran existing PD and LGD models, assuming that historical relationships continue to hold [@fed2024pilot].
- **Dutch central bank (DNB) flood test.** The LGD increase reflects collateral damage alone [@caloia2021flood].

The same exercises report that banks' credit models are not yet sensitive to climate:
- In the ECB's 2022 test, PDs and LGDs were "fairly insensitive" to the shocks, and banks did not always separate medium- from high-flood-risk exposures [@ecb2022climate].
- Banks lack data on building characteristics, insurance and asset location [@fed2024pilot].
- None of these exercises set capital requirements [@ecb2022climate; @boe2022results].
- The economy-wide ECB test found physical risk rising non-linearly and concentrated geographically, with bank losses highest where collateral protection is low [@alogoskoufis2021ecb].

### 4.2 Losses are concentrated and non-linear

Two quantitative regularities recur:
- **Geographic concentration.** In the Bank of England's 2021 exploratory scenario, 45% of mortgage impairments came from 10% of postcode areas [@boe2022results]. This source was read at abstract depth through a page summary, so the figure must be re-checked before citation.
- **Non-linearity.** Caloia and Jansen geocode the real-estate exposures of Dutch banks, match them to official flood maps and run increasingly extreme scenarios, which they describe as "in essence, a reverse stress test". CET1 depletion is about 110–132 bp for floods in unprotected areas, against well over 700 bp for an extreme flood in the protected west [@caloia2021flood]. An IMF analysis likewise finds the relation between damage and capital depletion non-linear and highly scenario-dependent [@lepore2024beyond].

### 4.3 Evidence on provisions

Evidence on whether provisions reflect flood risk points in different directions:
- US banks in counties with higher disaster risk recognise larger loan-loss provisions [@dalmaso2024does].
- After the 2013 German flood, savings and cooperative banks showed a higher but short-lived impairment flow. The authors judge expected-loss provisioning insufficient despite earlier floods [@shala2024impact].
- Loan spreads react to climate disasters through salience, briefly [@correa2026rising].
- Acharya et al. argue that typical loan maturities limit the short-run credit channel of climate risk, and they call for research on bank lending responses and the adequacy of risk pricing [@acharya2023climate].
- Market-based measures such as CRISK need only public data but have so far focused on transition risk [@jung2025crisk].

### 4.4 Methods and their limits

On methods:
- Dhima et al. map river-flood damage on real-estate collateral into PD, LGD and internal capital in an extended Merton model [@dhima2026integration] (abstract only).
- Reverse stress testing is formalised for macroeconomic risk factors: as an inversion problem [@grundke2018macroeconomic] and as the most likely scenarios given large losses [@glasserman2015stress].
- The NGFS now warns that the physical-damage variables in its Phase V scenarios rest on a paper since retracted from *Nature*, with an updated methodology planned [@ngfs2024ngfs]. Any Thai scenario built on those variables needs that caveat.

### 4.5 Thailand and the region

Three Thai studies exist, and none works at the level of individual collateral:
- **Bank mortgage book.** Chitchumnong, Hatairatana and Khangphukhieo [@chitchumnong2025physical], read in full, study one bank's mortgage book. They find a small immediate rise in default in late 2011 among delinquent borrowers ineligible for relief, then default *below* model-predicted levels, which they attribute to debt relief. Auto-loan defaults, by contrast, spiked. Their extreme-value analysis puts 2011 runoff at roughly a 1-in-50-year event. They report no geolocation, LGD, collateral values or IFRS 9 staging.
- **Systemic risk.** A PIER study links Thai banks' systemic risk to a transition-risk factor and to physical risk measured by a drought–flood index [@luangaram2024climate].
- **District-level mapping.** A World Bank–BOT exercise mapped corporate lending by district flood risk. It found 41% of bank corporate lending in districts with high riverine flood risk and 7% in very high-risk districts [@dolk2025assessing].

Regional IMF work describes itself as exploratory and calls for better data [@imf2025indonesia].

*Interpretation.* The supervisory template is already "hazard → collateral value → LTV → LGD". The empirical inputs to that template, however, come from modelled hazard maps at coarse resolution and from credit models that the supervisors themselves find insensitive. I found no study that links *observed* inundation of *individual* collateral to *staging* (the significant-increase-in-credit-risk trigger and stage 2) and ECL. I also found no climate reverse stress test that formally solves for the flood severity that breaches a capital threshold. This search was weak on IFRS 9 specifically, so the absence should be re-tested. If it holds, H2 and H3 fall directly into this gap.

## 5. Satellite measurement of floods (S4)

### 5.1 What flood maps measure

Satellite flood maps measure observed surface water at the time of the satellite pass. They do not measure depth, damage or peak extent. The main datasets:
- **Global Flood Database (GFD).** Built from MODIS optical imagery at 250 m. Of 3,054 catalogued flood events, 913 could be mapped; the rest were lost to persistent cloud, short or small floods, or complex terrain including dense forest and urban areas. Accuracy against Landsat was about 83% [@tellman2021satellite].
- **Sentinel-1 SAR.** Radar sees through cloud. The Copernicus Global Flood Monitoring product nonetheless excludes urban areas and dense vegetation, where the sensor is insensitive to flooding, and its manual states that this leads more often to under-estimation [@gfm2025product].
- **Urban-flood methods.** Specialised methods such as interferometric coherence [@chini2019sentinel] and multi-temporal statistics [@devries2020rapid] narrow the urban gap for specific events.
- **Hazard models.** Global models give ex-ante return-period maps at about 90 m [@sampson2015high]. Different global models agree on only about 30–40% of flood extent in Africa [@trigg2016credibility].

### 5.2 Three designs economists use

1. **Event indicators.** Kocornik-Mina et al. treat a city as flooded if any part of it falls within a satellite inundation map, because those maps probably understate extent, and then use within-city elevation [@kocornikmina2020flooded].
2. **Satellite plus survey exposure.** For Thailand in 2011, Noy, Nguyen and Patel combine household-reported flooding in the Socio-Economic Survey with satellite exposure to separate directly flooded households from spillover households [@noy2021floods]. I read only the abstract, which does not report effect sizes.
3. **Spatial RD at the flood edge** [@albertazzi2026physical].

### 5.3 Measurement error at the boundary

Geographic RD has two running variables [@keele2015geographic]. With a mismeasured running variable, the first-stage discontinuity can vanish, and identification needs extra structure: for example, non-differential error plus an auxiliary sample [@pei2017devil; @davezies2017regression]. Albertazzi et al. argue that misclassification at the boundary attenuates their estimates towards zero.

### 5.4 The 2011 Thai flood in the data

The 2011 Thai flood is in the GFD as an event from 5 August 2011 to 9 January 2012 (DFO 3850); whether the mapped extent covers Bangkok and the lower Chao Phraya has not been checked (`03_data/inventory_R3.md`). Sentinel-1-based products start only in 2014–15. Contemporary hydrological accounts put agricultural land damage at its peak in mid-November 2011 and report seven inundated industrial estates [@komori2012characteristics].

*Interpretation.* For this project the central measurement risk is *non-classical* error. Satellites systematically miss flooding in built-up and densely vegetated areas, which is where mortgage and SME collateral sits. If detection correlates with building density, and hence with collateral type and value, the attenuation argument does not automatically hold: bias could go either way. Mitigations to build into the design:
- use 2011 as a continuous intensity treatment (share of an area flooded, flood duration) rather than a sharp edge;
- validate post-2015 events against the exclusion layers;
- triangulate with official Thai flood records;
- keep ex-ante hazard maps (relevant to pricing, H2) separate from realised extents (relevant to PD and LGD, H1).

## 6. Emerging markets: relief, forbearance and the insurance gap (S5)

### 6.1 The 2011 Thai floods

The joint World Bank–Royal Thai Government assessment is the standard account of the 2011 floods [@worldbank2012thai]:
- **Scale.** THB 1.43 trillion (USD 46.5 bn) in damage and losses, about 70% in manufacturing and about 90% borne by the private sector; real GDP growth in 2011 lower by 1.1 percentage points.
- **Banks.** Bank balance sheets were resilient on impact. The expected rise in the NPL ratio was about 0.5%, after BOT-allowed grace periods and restructurings.
- **Insurance.** Fewer than 1% of private dwellings were estimated to be insured against natural disasters.

This fits Swiss Re's estimate that only 5% of severe flood losses in emerging markets over the preceding decade were insured, against 34% in advanced economies [@swissre2022extreme]. Supply-chain propagation was severe: seven industrial parks and 804 companies were inundated [@haraguchi2013flood].

### 6.2 Policy buffers

Thailand's buffers were regulatory and fiscal rather than insurance-based:
- **Classification freeze.** BOT circular ว. 1564/2554 of 19 October 2011 let institutions keep the pre-flood classification of debtors who were Normal or Special Mention when the flood hit. It covered debtors in declared disaster areas and indirectly affected debtors outside them. Assisted loans were treated as general rather than troubled restructurings and were not reported as restructured. Collateral revaluations due by 30 June 2012 could be deferred to 31 December 2012 at the latest [@bot2011circular1564]. The World Bank also reports a rule allowing restructured debtors to leave the non-performing list after one payment instead of three [@worldbank2012thai]. However, the circular's Q&A keeps the three-month rule for upgrading Special Mention loans, so that rule is not attributed to BOT here.
- **State banks.** A three-year moratorium was offered at state-owned specialised financial institutions for flood-hit borrowers with total debt under THB 500,000 [@worldbank2012thai].
- **Liquidity.** The Emergency Decree of 26 January 2012 created a soft-loan facility of up to THB 300 bn. The BOT lent to financial institutions at 0.01%, and on-lending to flood-zone borrowers was capped at 3% [@bot2012emergency].
- **Insurance.** A disaster insurance fund followed [@bot2012catastrophe].
- **Current template.** Since August 2024, a standing BOT relief template lets debtors in declared disaster zones keep their pre-disaster classification during relief [@bot2024relief].

### 6.3 What relief does to default

The most rigorous evidence on what relief does to default comes from India:
- India's 2008 farm-loan waiver reduced debt without raising investment or productivity, and pushed households towards informal credit [@kanz2016what].
- The waiver reduced and reallocated new bank lending and worsened later repayment, concentrated among borrowers previously in good standing [@gine2018economic].
- Non-distressed beneficiaries repaid worse afterwards, while genuinely distressed ones repaid better [@mukherjee2018borrowers].

Forbearance differs from forgiveness:
- In a randomised experiment, a lender-framed moratorium cut default by 4 percentage points, while the same offer framed as regulator-mandated had no effect [@fiorin2023how].
- US COVID forbearance absorbed distress that fundamentals would otherwise have turned into default [@cherry2022government].
- Regulatory forbearance on classification and provisioning can conceal insolvency and channel credit to weak firms [@chari2021unholy; @caballero2008zombie].
- The World Bank team warned explicitly that the Thai SFI moratorium could lead borrowers to move to state banks in anticipation of future relief [@worldbank2012thai].

*Interpretation.* In a relief-dominated, insurance-thin setting, *observed* default after a flood is a policy-censored outcome. The measured PD response is therefore a lower bound, as Chitchumnong et al. also argue, and losses may surface later or elsewhere. Without insurance, damage to collateral is not reimbursed, so LGD should respond more than in insured settings. That response is hidden, however, if restructured loans never reach default. Floods may therefore show up first in restructuring flags and stage 2 rather than in 90-day default. This directly affects IFRS 9 staging and makes staging, not default alone, the right outcome to study. The relief rules themselves create potential variation for identification: the THB 500,000 debt threshold at SFIs, declared flood zones, and the lender-type difference between state and commercial banks. Using that variation requires loan-level data.

## 7. Cross-strand synthesis

**What is known.**
- Floods raise credit demand and, modestly, default in insured advanced economies.
- Capital, diversification and relationships shape lenders' responses.
- Hazard is capitalised into market prices incompletely and with a lag, while lender valuations lag further.
- Supervisors have converged on a "hazard → collateral → LTV → LGD" template, but find banks' models insensitive and their data incomplete.
- Losses are geographically concentrated and non-linear in flood severity.
- Satellite maps make collateral-level exposure measurable after 2015 and coarsely measurable for 2011, with systematic urban under-detection.
- In emerging markets, insurance is minimal and relief is the main buffer, and relief changes when and how default appears.

**What is not known**, as far as these searches reach:
1. Whether flood exposure of *individual* collateral raises both PD and LGD for bank borrowers in an emerging market. The micro-evidence is US or European, or descriptive at a single Thai bank. The closest Asian bank evidence is regional, for example NPL ratios after typhoons in the Philippines [@nie2023banking]. Borrower-level microfinance studies exist, but they concern repayment to MFIs, not bank PD or LGD.
2. Whether official land valuations capitalise ex-ante flood hazard in any emerging market, and whether bank collateral valuations do so anywhere outside lender refinancing valuations in England [@garbarino2021high]. Official US property-tax assessments in New York City fell for homes inundated by Hurricane Sandy, largely through tax relief. They did not change for undamaged homes in the high-risk zone, although their sale prices fell [@guo2026rising]. The Thai evidence on land prices after 2011 uses survey and broker series, not official appraisals [@sawada2014natural; @sawada2018land].
3. Whether flood effects appear in IFRS 9 *staging* and ECL before or instead of default, beyond a short horizon in an insured advanced economy. After the 2024 Valencia floods, stage 2 shares rose by about 0.5 pp for affected firms and 0.45 pp for households, then faded within four months. Banks most exposed to the affected areas moved more loans into stage 2 and fewer into stage 3 while moratoria were in force [@perezmontes2025impact, pp. 19–21]. No comparable evidence exists for an emerging market where relief, not insurance, is the buffer, nor on whether stage 2 migration later becomes default or loss.
4. What flood severity would breach capital thresholds once observed exposure, concentration and relief are taken into account, i.e. a formal reverse stress test on a physical hazard variable.

**Why Thailand.** Several features combine in Thailand:
- a large, well-documented 2011 flood and recurrent later floods;
- free satellite flood data (MODIS for 2011; Sentinel-1 from 2014);
- parcel-level official appraisal values published as open data;
- monthly provincial bank credit data since 1996;
- negligible flood insurance;
- documented, rule-based relief with sharp eligibility thresholds;
- supervisory expectations on climate risk for banks since 2023.

*Interpretation.* Together these make Thailand a setting in which the insurance channel that dominates US and European evidence is largely switched off and replaced by relief. Questions 1–4 can therefore be posed more cleanly there than in the settings where the existing evidence comes from.

## 8. Limitations of this review

- **Read depth.** Read depth is uneven: many abstract-only sources, mostly because of blocked publishers and SSRN. The closest papers should be read in full before drafting the proposal, in particular Albertazzi et al., Caloia and Jansen, Garbarino and Guin, Van Gerwen et al., Noy et al. and Sawada et al.
- **Snowballing.** Citation snowballing was not completed because of API limits. Priority follow-ups from the strand "not read" lists:
  - Liew et al. (2016) on satellite mapping of the 2011 Chao Phraya flood;
  - Brei et al. (2024) on Caribbean storms and banks;
  - Sawada et al. (2014, RIETI) on Thai land prices and firm location;
  - Pérez Montes et al. (2025) on Valencia flood exposures and stage 2;
  - Bank Negara Malaysia's climate stress-test methodology;
  - any IMF FSAP climate note on Thailand.
- **BOT policy sources.** Statements about BOT policy rest on public documents only. Several 2011 measures rest on the World Bank report rather than original BOT circulars.

# S1: Disasters, floods and bank credit

**Working draft, 2026-11-02.** Strand question (from `01_literature/protocol.md`): *what happens to credit supply, demand, default and bank balance sheets after floods and other disasters?* Bibliography: `S1.bib`. Matrix: `S1_matrix.csv`.

Labels: **[E]** established evidence from a source I read, at the depth stated; **[H]** the author's hypotheses (H1–H3 in the feasibility memo); **[S]** my speculation or judgement. Where I read a working-paper version, findings are from that version and the published version may differ.

---

## Synthesis

**What is established [E].** Three findings recur across designs and settings.

*Credit demand rises after a disaster, and well-connected, well-capitalised lenders meet it.* US multi-market banks fund higher post-disaster mortgage demand by cutting lending in connected non-core markets (cortes2017tracing). German regional banks exposed to the 2013 Elbe flood through their borrowers lend 3% more (koetter2020borrowers). Syndicated lenders reallocate credit away from distant regions (ivanov2022bank). In Europe, credit to firms just inside Copernicus flood boundaries rises 3.5–5% in the first quarter and then reverses (albertazzi2026physical).

*The constraint is the bank's capital and diversification.* Low capital amplifies spillovers to firms in unaffected areas (rehbein2022flooded; ivanov2022bank). Exposed German banks outside geographically diversified groups take on more credit risk and lose more equity (koetter2020borrowers). Damage to banks lowers the investment of their client firms (hosono2016natural).

*Default rises, but in rich, insured settings the rise is modest relative to the destruction.* After Katrina, 90-day delinquency among the most flooded residents was about 10% higher for a year, and flood-insurance payouts were used to repay mortgages (gallagher2017household). In Europe, default on pre-existing loans rises by about 0.7 pp over two quarters, roughly doubling the baseline (albertazzi2026physical). SMEs in flooded counties default more (barbaglia2024flooded).

**What is contested [E].** The size of the bank-level hit is disputed. Noth and Schüwer (noth2023natural; WP version) find lower Z-scores, higher NPA and foreclosure ratios and lower equity for two years after US weather disasters. Blickle et al. (blickle2025bad) answer "not very": they estimate that a disaster would need to be 6.7 standard deviations beyond the 95th-percentile event to push a single-county bank to failure. They attribute this resilience to post-disaster loan demand, and to local banks' knowledge of risk the official flood maps understate, rather than to federal aid. Cross-country evidence says the answer depends on the setting: disasters reduce banks' distance-to-default, with effects conditioned on supervision and on financial and economic development (klomp2014financial). Whether lending rises or falls also depends on the setting. Recovery lending dominates in the US and Germany. In contrast, an Ecuadorian microfinance lender restricted access except to known clients (berg2012access), Caribbean banks cut lending after deposit withdrawals (brei2019impact), and US global banks cut cross-border lending to disaster-hit countries by 9% (ilabaca2024global). Branch relationships sustained farm lending after Iran's 2019 flood (abedifar2022flood).

**What is missing for an emerging-market, collateral-level study [S].**
1. *No loan-level evidence from emerging markets on PD and LGD together.* The emerging-market evidence I found is bank- or country-level (brei2019impact, klomp2014financial, ilabaca2024global) or comes from a single lender's clients (berg2012access, abedifar2022flood). Within this strand's search, I found no econometric study of bank credit after Thailand's 2011 floods.
2. *Collateral and loss severity are absent.* Every paper here measures delinquency, NPLs, charge-offs or Z-scores. None measures recovery, LGD or post-disaster collateral revaluation; that literature sits in S2. Gallagher and Hartley show that insurance proceeds flowed to lenders through the collateral claim, a channel that thin insurance removes.
3. *Accounting and provisioning are absent.* No paper read here studies IFRS 9 staging or ECL responses. Pérez Montes et al. (2025; scoping, abstract only) report stage-2 movements, as summarised by Albertazzi et al.
4. *Hazard measurement is mostly coarse.* FEMA declarations, SHELDUS county damage, EM-DAT and insurance-claim shares are the norm. Satellite inundation boundaries appear only in albertazzi2026physical, and engineered block-level flood depth only in gallagher2017household.
5. *Buffer heterogeneity.* Resilience in the US/European results is attributed partly to insurance, aid and loan demand. How debt relief rather than insurance shapes the timing of default is untested in this strand (see S5).

**Hypotheses this strand informs [H].** H1 (flood exposure raises PD and LGD) is supported on the PD side only. H3 (concentration raises capital sensitivity) is consistent with koetter2020borrowers and rehbein2022flooded on diversification and capital. Blickle et al.'s "6.7 SD" calculation is a published analogue of the reverse stress test the project proposes.

**Speculation [S].** The demand-dominated, quickly reversing pattern in Europe may not carry over to a flood that is national in scale relative to bank portfolios, as in Bangkok in 2011. There, a regulator-led moratorium could delay recognised default, shifting losses from PD timing into LGD and from stage 3 into stage 2.

---

## Per-paper entries

**albertazzi2026physical** — Albertazzi, Djekic & Ponte Marques (2026), ECB WP 3224. *Read: intro (Sections 1–2).*
- Q: causal effects of floods on lending, rates, collateral requirements and default on pre-existing loans.
- Data: AnaCredit loan-level data and Copernicus EMS flood maps for four floods: DE/BE/NL July 2021, Marche–Umbria September 2022, Emilia-Romagna May 2023 and Valencia October 2024.
- ID: spatial RD at the flood boundary (300–500 m), plus firm–time fixed effects within multi-bank firms (Khwaja–Mian) to separate supply from demand.
- Finding [E]: credit +3.5–5% in the first quarter, reversing in the second, with no significant cumulative change; rates +10–13 bp in the first quarter, partly reversing. Default on pre-existing loans rises by about 0.5 pp after one quarter and about 0.7 pp over two, close to doubling the baseline. More-exposed banks do not systematically tighten, though they marginally extend maturities ("mild evergreening"). Main banks extend about 10 pp more credit while tightening collateral. Ex-ante high-risk firms see a net decline of about 8 pp in the first quarter.
- Secondary (reported in their literature review, not read by me): Meucci & Rinaldi (2022) find loan- and collateral-level physical exposures highly correlated (an implied PD–LGD link) and about 20% of AnaCredit loans secured by physical collateral.

**blickle2025bad** — Blickle, Hamerling & Morgan, NY Fed Staff Report 990 (2021, revised October 2025). *Read: intro.*
- Q: how much weather disasters hurt bank performance and stability, and why.
- Data: FEMA disasters 1995–2018; SHELDUS county damage; exposure via branch presence; single-county versus multi-county banks; 2019 FEMA flood maps digitised and merged with HMDA.
- ID: panel with saturated fixed effects and county controls; non-FEMA versus FEMA disasters, and FEMA coverage discontinuities at state borders, to test the role of aid.
- Finding [E]: effects on losses and Z-scores are generally insignificant or small, and multi-county banks' income rises. For 95th-percentile disasters, local banks fare worse but not to the point of insolvency: failure would require a disaster 6.7 SD beyond the 95th percentile. Aid does not appear to explain the resilience. Lending rises at multi-county banks only. Local banks shift mortgage lending away from tracts where flood risk looks understated by the FEMA maps.

**cortes2017tracing** — Cortés & Strahan (2017), *JFE*. *Read: intro (Cleveland Fed WP 14-12R).*
- Q: how multi-market banks reallocate credit after local demand shocks.
- Data: HMDA mortgage originations at bank–county–month level; US disasters.
- ID: disasters as exogenous demand shocks, with property damage instrumenting lending growth; outcomes in connected, unaffected markets; placebo shocks.
- Finding [E]: lending peaks about 6 months after a disaster. For small banks (under $2 bn in assets), connected-market credit falls by a little under 50 cents per extra dollar lent in the shocked area. Larger banks do not cut, and cuts fall outside branch (core) markets. Banks sell more liquid loans and bid up deposit rates in connected markets.

**koetter2020borrowers** — Koetter, Noth & Rehbein (2020), *JFI*. *Read: intro (IWH DP 31/2016, 2019 draft).*
- Q: do local banks provide recovery lending, and at what cost to their stability?
- Data: Elbe flood, May 2013; about 1.1 m firms matched to about 2,000 banks (Creditreform); damage of €6 bn, about one-third insured.
- ID: banks in unaffected counties with many borrowers in flooded counties ("exposed"), compared with unexposed banks.
- Finding [E]: exposed banks lend 3% more, mainly unsecured non-mortgage credit funded by local deposits. Connected flooded firms borrow 16% more. No overall rise in risk or rent extraction, but exposed banks without access to a geographically diversified banking group show more credit risk and lower capital.

**rehbein2022flooded** — Rehbein & Ongena (2022), *JFQA*. *Read: abstract.*
- Q: does low bank capital amplify local shock spillovers?
- Data/ID: a natural disaster transmitted to firms in non-disaster areas through their banks; the event is not named in the abstract.
- Finding [E]: firms tied to a strongly exposed, lowest-quartile-capital bank cut borrowing by 6.6% and tangible assets by 6.9%, with negative regional GDP and unemployment effects. After a disaster, banks reduce exposure to areas that are unaffected but disaster-prone.

**gallagher2017household** — Gallagher & Hartley (2017), *AEJ: Policy*. *Read: intro (Cleveland Fed WP 14-06R).*
- Q: how flooding affects household debt and distress, and the role of local versus non-local lenders.
- Data: a 5% random credit-bureau panel (quarterly) matched to Census-block flood depth, New Orleans, Katrina 2005; HMDA for lender locality.
- ID: difference-in-differences, flooded versus non-flooded blocks, using variation not predicted by engineering flood-risk variables.
- Finding [E]: total debt falls through mortgage payoff from flood-insurance proceeds, on which lenders co-sign. Credit-card debt rises temporarily by about $800 (22%). 90-day delinquency is about 10% higher for a year, and credit scores are about 0.06 SD lower for two years. Non-local lenders largely exited, while local lenders returned to pre-Katrina volumes within two years.

**noth2023natural** — Noth & Schüwer (2023), *JEEM*. *Read: intro (SAFE WP 167, April 2018).*
- Q: do weather disasters reduce bank stability?
- Data: over 12,000 damage records (Univ. of South Carolina hazards database) and over 6,000 US banks, 1994–2012 (about 66,000 bank-years).
- ID: bank fixed effects and year–region fixed effects; within-bank yearly variation in disaster damage in the bank's business region.
- Finding [E]: lower Z-scores, higher PD, NPA and foreclosure ratios, and lower ROA and equity ratios for two years. The effects fade after 2–3 years for weather disasters but not for geological ones. Insurance and aid do not fully protect borrowers.

**schuwer2019banks** — Schüwer, Lambert & Noth (2019), *Review of Finance*. *Read: abstract.*
- Q/Data: bank responses to Hurricane Katrina in the affected areas.
- Finding [E]: independent banks, but not BHC members, raise risk-based capital ratios, driven by highly capitalised banks. These banks shift into government securities and cut total loans to non-financial firms while raising new lending. Affected counties with more independent, better-capitalised banks grow faster.

**berg2012access** — Berg & Schrader (2012), *JFI*. *Read: abstract.* **Emerging market.**
- Data: client-level data from an Ecuadorian microfinance institution; volcanic eruptions.
- Finding [E]: credit demand rises after eruptions but access is restricted. Known (relationship) clients are about as likely as before to obtain loans.

**brei2019impact** — Brei, Mohan & Strobl (2019), *QREF*. *Read: abstract.* **Emerging market.**
- Data: a quarterly bank panel for Eastern Caribbean islands, with hurricane losses.
- Finding [E]: deposit withdrawals create a funding shock, and banks cut lending and draw on liquid assets. There is no sign of deteriorating defaults or capital. The authors point to a role for reserve-requirement policy.

**klomp2014financial** — Klomp (2014), *J. Financial Stability*. *Read: abstract.* **Cross-country, including emerging markets.**
- Data: over 160 countries, 1997–2010; banks' distance-to-default.
- Finding [E]: large disasters raise default likelihood, most strongly for geophysical and meteorological events. The effect depends on the disaster's size, regulatory and supervisory rigour, and financial and economic development.

**hosono2016natural** — Hosono et al. (2016), *IER*. *Read: abstract.*
- ID: the 1995 Kobe earthquake as a shock to bank lending capacity.
- Finding [E]: firms outside the quake area whose main bank was inside it invested significantly less. Loan-supply shocks therefore affect investment.

**ivanov2022bank** — Ivanov, Macchiavelli & Santos (2022), *Financial Management*. *Read: abstract.*
- Data: US syndicated lending.
- Finding [E]: disasters raise corporate credit demand locally. Banks cut credit to distant unaffected regions, more so when they hold less capital. Shadow banks offset term loans but not credit lines, and credit in unaffected regions falls by about 3%.

**abedifar2022flood** — Abedifar, Kashizadeh & Ongena (2022), SSRN WP. *Read: abstract.* **Emerging market.**
- Data: Iran's April 2019 flood; proprietary data on over 53,000 farmers.
- Finding [E]: local branches raise lending for two months, bridging the gap until government aid arrives. Farmers with stronger branch relationships, particularly younger and female farmers, are more likely to receive recovery loans.

**barbaglia2024flooded** — Barbaglia, Fatica & Rho (2024), Mo.Fi.R. WP 186. *Read: abstract.*
- Data: European SME loans.
- Finding [E]: SMEs in high flood-risk areas pay a premium averaging 6.4 bp, larger for longer loans, smaller borrowers and local specialised banks. There is no premium for firms relying on intangible or movable assets. Firms in flooded counties are more likely to default.

**ilabaca2024global** — Ilabaca, Mann & Mulder (2024), OFR WP 24-05. *Read: intro.* **Emerging markets (as destination of lending).**
- Data: FFIEC 009 country exposures of US-regulated banks, merged with EM-DAT; a quarterly bank–country panel.
- ID: difference-in-differences, with country–time fixed effects for demand; heterogeneity by pre-disaster ties (prior lending, bilateral trade).
- Finding [E]: cross-border lending to affected countries falls by 9% two years after large disasters, driven by banks with weak ties. This is partly offset by local claims of in-country branches. The authors' interpretation is an information-friction channel. The OFR summary page frames the result around low-income countries.

---

## Unverified / not read

Not used as evidence; tagged [UNVERIFIED] wherever mentioned.

- Chavaz (2016), BoE Staff WP 617, on lending after the 2005 hurricanes: cited in Blickle et al. and Koetter et al.; not opened.
- Garmaise & Moskowitz (2009, *JF*), "Catastrophic risk and credit markets": cited in Koetter et al. and Noth & Schüwer; not opened this session.
- Do, Phan & Nguyen (2023), on listed US banks and disasters; Barth, Sun & Zhang (2019); Wang (2023/2024, SSRN 4690816); Zhou et al. (2023); Cortés (2014). All are cited in papers I read; none opened.
- Ogura, Nguyen & Nguyen, RIETI DP 22-E-088 (Japan, SME loans and flood damage): the PDF is AES-encrypted and could not be extracted; the content was seen only in a search-engine summary.
- Beyene, SAFE WP 455 (2013 German flood, car loans), and Arseneau & Kara, FEDS 2025-081 (flood-risk pricing in mortgage origination; more relevant to S2/S3): search-engine summaries only.
- Brei, Mohan, Perez Barahona & Strobl (2024), *JIMF* 141:103008, on thirty years of Caribbean tropical storms: Crossref metadata only, abstract not read. A strong emerging-market candidate to read next.
- Pérez Montes et al. (2025, BdE FSR 48): scoping abstract truncated. Its NPL and stage-2 findings are known only through Albertazzi et al.'s summary.
- Fatica et al. (2024a, b), Meucci & Rinaldi (2022), Carroll et al. (2025), Bassetti et al. (2025), Chen et al. (2025), D'Andrea et al. (2026): known only from Albertazzi et al.'s literature review.
- Rehbein & Ongena (2022): introduction not read, and the disaster event is unconfirmed (no open version located this session).
- Thailand 2011 floods and bank credit: one web search returned only industry commentary (Moody's, Kasikorn Research, Oxford Business Group). None was opened or used. OpenAlex and Semantic Scholar returned HTTP 429 throughout this session, so citation-network snowballing was **not** done. Treat the emerging-market coverage as provisional.

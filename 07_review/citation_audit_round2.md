# Citation audit, round 2: `06_proposal/proposal.md`

**Audit date: 2026-11-02.** Every source below was opened on 2026-11-02 unless a section says otherwise.

**Scope.** The 34 citekeys that round 1 (`07_review/citation_audit.md`, 25 keys) did not cover, and every sentence in the proposal that cites them. This is a report only. No other project file was changed.

**Proposal version.** `proposal.md` was revised twice on disk during this audit. All quotations below were re-checked against the version saved at 2026-11-02 20:34 +07 (20,492 bytes). A script confirmed that every sentence in that version citing one of the 34 keys matches the quotation in its section. Changes to citing sentences since the audit began:
- `bin2013changes`, `quan1991price` and `avenancioleon2022assessment`: no longer cited (removed from §3 ¶1). Their sections record the earlier wording.
- `th2019valuationact` (§1): now "reset nationwide every four years … without an insurance price to guide them".
- `barbaglia2024flooded` (§3): now opens "European small-business default hazards…".
- `caloia2026floods` (§3): the sentence now ends "none treats relief as a dimension of the breaking point".
- `bot2026rppislides` (§3): "…respond to floods, not λ_T itself".
- `cameron2008bootstrap` (§4.1): "onto equally low-lying dry sheets".
- `zanaga2022worldcover` (§4.1): second citation, "land cover from @zanaga2022worldcover".
- `bot2018tfrs9` (§4.2): a clause on LGD proxies was added after the citation.
- `callaway2021difference` (§4.2): "Borrowers on flooded and comparable unflooded sheets are compared … with the two floods as cohorts".
- `dinerstein2024debt`, `kim2024intermediation` (§3): now "Moratoria change borrowers' behaviour".
- `bcbs2005irb` (§4.3): now "are implausible, as at Basel's 99.9% confidence level".
- `kolesar2018inference` (§4.2): reworded to "A fuzzy discontinuity there".
- `bot2025level4` (§4.2): the locator now reads "pp. 1–2", and "(intention to treat)" was dropped.
- `treasury2026chachoengsao`, `treasury2026extbriefing` (§7): now add "and a provincial committee considered an extension on 2 November". This **resolves** the round-2 MINOR on `treasury2026chachoengsao`, which is now OK.
- `bot2018tfrs9` (§4.2): now "…IFRS 9 stages [@bot2018tfrs9], with haircuts, revaluations and provisions as early LGD proxies".

Apart from `treasury2026chachoengsao`, none of these changes alters a verdict. If the draft changes again, re-run the quotations against it.

**Method.**
- Metadata was checked against Crossref (`api.crossref.org/works/<doi>`, no mailto), OpenAlex, DataCite, RePEc/IDEAS, and the publisher or issuer page or PDF. Requests were at least 3 s apart per host, with no email address in any request.
- Claims were checked against the full text wherever a public copy opened:
  - author or working-paper versions (NBER, arXiv, Mo.Fi.R. and university repositories);
  - the JRC report;
  - Bank of Thailand, BIS and Treasury Department PDFs and pages.
- Where only an abstract was available, the section says "abstract only" and the verdict is judged against the abstract.
- Thai documents were read in the original. Scanned pages were read from the page images.
- Downloads were saved under the session scratchpad (`audit2/<key>/`) and parsed with `python -I`.
- Locators give the PDF page ("PDF p.") and, where it differs, the printed page.

**Verdict scale.**
- **OK**: the source supports the claim.
- **MINOR**: the wording overstates the source or is imprecise.
- **MISMATCH**: the cited source does not support the claim.
- **NOT RE-OPENED**: the source could not be opened in this round, so the verdict falls back on the bib note.

A key cited in two places takes the verdict of its weaker use. The section gives both.

---

## 1. Summary

### Verdict counts

| OK | MINOR | MISMATCH | NOT RE-OPENED | Total |
|---|---|---|---|---|
| 26 | 8 | 0 | 0 | 34 |

Two of the MINOR verdicts (`bin2013changes`, `avenancioleon2022assessment`) concern citations removed from the draft during the audit, so 6 MINOR issues are live.

Every source opened (HTTP 200). No key needed the NOT RE-OPENED fallback, although some checks were abstract-only (see each section). All 34 bibliographic entries match their primary source on authors, year, title and venue. Section 3 lists small bib fixes. Nothing seen was confidential: every Bank of Thailand document opened is public on bot.or.th or on a conference site.

### Summary table

| # | Key | Verdict | One-line reason |
|---|---|---|---|
| 1 | `avenancioleon2022assessment` | MINOR | No longer cited (20:29 draft). The abstract shows assessments less sensitive than prices, not a lag "by design". |
| 2 | `barbaglia2024flooded` | OK | Table 7: hazard ratios 0.93 / 1.20 / 1.61 for 6 / 12 / 24-month (nested) windows; aid conjectured, no relief data. |
| 3 | `bcbs2005irb` | OK | §5.1, printed p. 11: 99.9%, losses exceed capital "once in a thousand years"; "as at" (20:29) is less hedged than "by analogy". |
| 4 | `beltran2018flood` | OK | Abstract: −4.6% for location in the inland 100-year floodplain (meta-analysis). |
| 5 | `bin2013changes` | MINOR | No longer cited (20:28 draft). The earlier "fading after floods" dropped the post-flood jump the paper finds before the 5–6 year fade. |
| 6 | `blattner2023losses` | OK | Abstract: capital-short banks reallocate credit to firms with underreported losses. |
| 7 | `bot2012capital` | OK | Cl. 5.3.1: CET1 4.5% + conservation buffer 2.5% = 7% (assumes zero countercyclical buffer). |
| 8 | `bot2017dsib` | OK | Cl. 4.3.2: D-SIB CET1 add-on 1%; cl. 4.3.3 table gives 8.0%. |
| 9 | `bot2018tfrs9` | OK | Circular item 3: three ECL-based classes (performing / under-performing / non-performing); bib Thai title is a paraphrase. |
| 10 | `bot2024circular601` | MINOR | §1 OK (item 2.2 keeps classification). §4.2: trigger is a zone declaration *or* a yellow/orange/red alert level. |
| 11 | `bot2025level4` | MINOR | §1 OK (item 2.6). §4.2: moratorium is for retail and SME debtors who opt in; "participating lenders" is a gloss. |
| 12 | `bot2026rppislides` | OK | Slides 3, 7–9: RPPI built from mortgage-loan appraisal prices; regional indices from representative provinces. |
| 13 | `caballero2008zombie` | OK | Banks near capital minimums evergreened loans to insolvent firms (abstract; NBER WP pp. 2–3). |
| 14 | `callaway2021difference` | OK | Method citation for staggered DiD with two flood cohorts (arXiv abstract). |
| 15 | `caloia2026floods` | OK | Abstract: 38 fixed adverse scenarios, capital declines mostly 30–50 bp; bib note says 30–110 bp. |
| 16 | `cameron2008bootstrap` | OK | NBER WP §3.2 (pp. 18–19) introduces the wild cluster bootstrap-t. |
| 17 | `chongwilaikasaem2022flood` | OK | Abstract: flood risk lowers survey rents (main) and MoF official valuations (robustness), cross-section. |
| 18 | `dinerstein2024debt` | OK | Abstract: frozen borrowers used liquidity to borrow more. |
| 19 | `dottori2016global` | OK | §4, printed p. 93: return periods 10–1000 years. |
| 20 | `esa2022copdem` | OK | Crossref dataset record and AWS readme match; note it is a surface model (buildings, canopy). |
| 21 | `fuerst2021pricing` | MINOR | §3: one Melbourne municipality; "known flooded areas" are planning flood overlays, not flooded land. |
| 22 | `huizinga2017global` | OK | Printed p. 13: Asia residential functions include Thailand. |
| 23 | `kim2024intermediation` | OK | Abstract: forbearance raised nonpayment, cut delinquency outside forbearance. |
| 24 | `kolesar2018inference` | MINOR | Paper is on inference with a discrete running variable (sharp case); cited as if a fuzzy-RD reference. |
| 25 | `kousky2020flood` | OK | Abstract: where insurance not required, damage raises 180+ day delinquency and default. |
| 26 | `lee2009training` | OK | Abstract: trimming bounds under sample selection. |
| 27 | `mgr2012appraisal` | MINOR | Supported, but the "unchanged" values were a late-2011 schedule that rose 21.34% on average; could be read as carry-over. |
| 28 | `quan1991price` | OK | No longer cited (20:29 draft). Abstract: appraisal smoothing is consistent with optimal updating. |
| 29 | `th2019valuationact` | OK | S. 19: four-year rounds, ≥30 days' notice (2 Dec 2026 is right), extension ≤1 year. |
| 30 | `treasury2026chachoengsao` | OK | Draft now says a provincial committee "considered an extension on 2 November", which matches the page; the earlier "briefed in October" wording was MINOR. |
| 31 | `treasury2026extbriefing` | OK | 28 Oct 2026 video-conference briefing area offices on extending the schedules. |
| 32 | `utami2021impact` | MINOR | Official ZNT values rose least in rupiah in the tidal zone; no percentages, and coastal land starts far cheaper. |
| 33 | `ward2020aqueduct` | OK | WRI page (23 Apr 2020, 26 authors) and GEE catalogue: return periods up to 1000 years. |
| 34 | `zanaga2022worldcover` | OK | DataCite: ESA WorldCover 10 m 2021 v200, Zenodo 2022, 16 creators, CC BY 4.0. |

### Required fixes (each no longer than the original wording; 2 is already done, and 4 and 6 apply only if a removed citation returns)

1. **§4.2, `bot2024circular601` + `bot2025level4` (one sentence).** "Relief followed disaster-zone declarations or alert levels [@bot2024circular601] and, in 2025, covered retail and SME debtors in Level-4 areas, such as Songkhla, not non-performing on 2 December 2025 [@bot2025level4, pp. 1–2]." This matters for the design: eligibility can come from an alert level as well as a declaration, and the 2025 moratorium is opt-in for retail and SME debtors only.
2. **§7 timeline, `treasury2026chachoengsao`.** Already fixed in the 20:33 draft ("a provincial committee considered an extension on 2 November"). No action needed.
3. **§3 ¶1, `fuerst2021pricing`.** "Closest to RQ1, Melbourne statutory valuations discount designated flood zones [@fuerst2021pricing]; …". The closest paper should be described precisely.
4. **`bin2013changes` (now uncited).** Only if it is reinstated: "Flood discounts average 4.6% for inland 100-year floodplains [@beltran2018flood, abstract], jump after floods, then fade [@bin2013changes]." Otherwise check that the reference list does not print an uncited entry.
5. **§3 ¶1, `utami2021impact`.** "Semarang's official zone values gained fewest rupiah near tidal flooding [@utami2021impact]." Alternatively, keep "rose least" and add "in rupiah", trimming elsewhere.
6. **`avenancioleon2022assessment` (now uncited).** Only if it is reinstated: "Valuations may track prices only partially [@quan1991price; @avenancioleon2022assessment]."
7. **§2 RQ1, `mgr2012appraisal`.** "The Treasury found no post-2011 fall in flooded areas and left its schedule unrevised [@mgr2012appraisal]."
8. **§4.2, `kolesar2018inference`.** "A fuzzy discontinuity in discrete months overdue [@kolesar2018inference], differenced between declared and undeclared flooded areas, netting out the boundary (pre-flood years test this), identifies relief for borrowers in arrears."

---

## 2. Per-key sections

### `avenancioleon2022assessment`
- **Bib entry:** Avenancio-León, C. F. & Howard, T. (2022), "The Assessment Gap: Racial Inequalities in Property Taxation", *Quarterly Journal of Economics* 137(3): 1383–1434, doi:10.1093/qje/qjac009.
- **Cited in proposal:** **No longer cited** in the version saved at 20:29. Earlier the key appeared in §3 ¶1, with no locator: "Valuations may lag prices by design [@quan1991price; @avenancioleon2022assessment]."
- **Metadata:** OK. Crossref: same authors, title, journal, 137(3), pp. 1383–1434; online 4 Feb 2022, print issue 12 Jul 2022.
- **Source opened (as of 2026-11-02):** https://api.crossref.org/works/10.1093/qje/qjac009 (deposited abstract). Abstract only; the OUP full text was not opened.
- **Source says:** "Property assessments are less sensitive to neighborhood attributes than market prices are. This generates spatial variation in tax burden within jurisdiction and leads to overtaxation of communities with a high share of minority residents." (abstract)
- **Verdict:** MINOR (applies to the earlier wording; moot unless the citation is reinstated). The abstract documents assessments that are *less sensitive* to neighbourhood attributes than prices, a cross-sectional finding. It says nothing about assessments *lagging* prices in time, or about this being *by design*. Quan and Quigley support "lag by design"; this paper supports a weaker, related statement.
- **Suggested wording:** If reinstated: "Valuations may track prices only partially [@quan1991price; @avenancioleon2022assessment]." (6 words, as in the earlier version.)

### `barbaglia2024flooded`
- **Bib entry:** Barbaglia, L., Fatica, S. & Rho, C. (2024), "Flooded credit markets: physical climate risk and small business lending", Mo.Fi.R. Working Paper No. 186.
- **Cited in proposal:** §3 ¶2, locator "Table 7": "European small-business default hazards dip for six months after a flood, then rise, tentatively attributed, without relief data, to aid and payment suspensions [@barbaglia2024flooded, Table 7]."
- **Metadata:** OK. Cover (PDF p. 1): "Luca Barbaglia Serena Fatica Caterina Rho … Working paper no. 186 July 2024"; title page (PDF p. 2): "Revised: June 2024". The IDEAS record matches.
- **Source opened (as of 2026-11-02):** https://ideas.repec.org/p/anc/wmofir/186.html (abstract) and http://docs.dises.univpm.it/web/quaderni/pdfmofir/Mofir186.pdf (HTTP 200, 61 pp.). Read: abstract and Section 4 with Table 7 (PDF pp. 33–36, printed pp. 32–35).
- **Source says:**
  - Table 7 (PDF p. 34, printed p. 33), Flood hazard ratios: "0.9306*** 1.1981*** 1.6066***" for floods in the previous 6, 12 and 24 months (columns 1–3). The windows are cumulative: "at least one flood episode in the 6, 12, or 24 months before loan default".
  - "The hazard ratio associated with the occurrence of flooding in the previous 6 months is 0.93, which suggests a protective effect … One possible explanation behind this counterintuitive result is the effect of emergency financial aid and relief measures … direct transfer and subsidies, tax holidays and suspension of debt payments." (PDF p. 33, printed p. 32)
  - "While we do not have data on post-flooding emergency measures for the events in our sample, we conjecture that a similar mechanism may be at play here" (PDF p. 35, printed p. 34).
  - The sample is securitised SME loans (European DataWarehouse).
- **Verdict:** OK. The dip, the later rise, the tentative attribution and the absence of relief data are all stated. Note: the 6-, 12- and 24-month windows are nested, so "then rise" describes the longer cumulative windows, not a separate later period.
- **Suggested wording:** —

### `bcbs2005irb`
- **Bib entry:** Basel Committee on Banking Supervision (2005), *An Explanatory Note on the Basel II IRB Risk Weight Functions*, BIS, July 2005.
- **Cited in proposal:** §4.3: "Scenarios rarer than 1 in 1,000 years are implausible, as at Basel's 99.9% confidence level [@bcbs2005irb, p. 11]." (Before the 20:29 revision: "… count as implausible, by analogy with Basel's 99.9% confidence level".) (locator: p. 11)
- **Metadata:** OK. Cover (PDF p. 1): "Basel Committee on Banking Supervision … An Explanatory Note on the Basel II IRB Risk Weight Functions … July 2005". The landing page gives the title and the date "05 July 2005".
- **Source opened (as of 2026-11-02):** https://www.bis.org/publications/explanatory-note-basel-ii-irb-risk-weight-functions.pdf (HTTP 200, 19 PDF pages) and the landing page https://www.bis.org/publications/explanatory-note-basel-ii-irb-risk-weight-functions (HTTP 200). Read: table of contents and Sections 4.7–5.2 (PDF pp. 15–16).
- **Source says:** §5.1 "Confidence level": "The confidence level is fixed at 99.9%, i.e. an institution is expected to suffer losses that exceed its level of tier 1 and tier 2 capital on average once in a thousand years." (PDF p. 15, printed p. 11)
- **Verdict:** OK. The page and the figure match, and the proposal correctly presents the 1-in-1,000 cut-off as an analogy rather than a Basel rule. (The Basel figure is a one-year credit-loss confidence level, not a hazard return period; "by analogy" covers this.)
- **Suggested wording:** —. The 20:29 wording "as at" is less hedged than "by analogy with". It still passes, because the source does equate 99.9% with "once in a thousand years". "By analogy with" was more exact, since the Basel figure is a one-year loss quantile, not a hazard return period.

### `beltran2018flood`
- **Bib entry:** Beltrán, A., Maddison, D. & Elliott, R. J. R. (2018), "Is Flood Risk Capitalised Into Property Values?", *Ecological Economics* 146: 668–685, doi:10.1016/j.ecolecon.2017.12.015.
- **Cited in proposal:** §3 ¶1, locator "abstract": "Flood risk is capitalised into prices, by about 4.6% for inland 100-year floodplains [@beltran2018flood, abstract]." (Before the 20:28 revision the sentence went on: ", fading after floods [@bin2013changes].")
- **Metadata:** OK. Crossref: same authors, title, journal, vol. 146, pp. 668–685, April 2018. OpenAlex gives 2017, the online year.
- **Source opened (as of 2026-11-02):** https://api.crossref.org/works/10.1016/j.ecolecon.2017.12.015 and the IDEAS abstract https://ideas.repec.org/a/eee/ecolec/v146y2018icp668-685.html. Abstract only.
- **Source says:** "For inland flooding the price discount associated with location in the 100-year floodplain is −4.6%. Although other estimates are defensible, we suggest this figure be used as a rule of thumb" (abstract). The estimate comes from a meta-analysis of "37 published works and 364 point estimates".
- **Verdict:** OK. The figure and the locator match. Since the claim is now the whole sentence, "about" could go: the meta-regression estimate is exactly −4.6%.
- **Suggested wording:** —

### `bin2013changes`
- **Bib entry:** Bin, O. & Landry, C. E. (2013), "Changes in implicit flood risk premiums: Empirical evidence from the housing market", *Journal of Environmental Economics and Management* 65(3): 361–376, doi:10.1016/j.jeem.2012.12.002.
- **Cited in proposal:** **No longer cited** in the version saved at 20:28. Earlier the key appeared in §3 ¶1, with no locator: "Flood risk is capitalised into prices, by about 4.6% for inland 100-year floodplains [@beltran2018flood, abstract], fading after floods [@bin2013changes]." The bib entry remains, so the reference renderer may drop it or list it uncited; check.
- **Metadata:** OK. Crossref: same authors, title, journal, 65(3), pp. 361–376, May 2013.
- **Source opened (as of 2026-11-02):** Crossref (no abstract deposited) and the IDEAS abstract https://ideas.repec.org/a/eee/jeeman/v65y2013i3p361-376.html. Abstract only.
- **Source says:** "Prior to Hurricane Fran in 1996, we detect no market risk premium for the presence in a flood zone, but we find significant price differentials after major flooding events, amounting to a 5.7% decrease after Hurricane Fran and 8.8% decrease after Hurricane Floyd. … this effect is diminishing over time, essentially disappearing about 5 or 6 years after Hurricane Floyd." (abstract)
- **Verdict:** MINOR (applies to the earlier wording; moot unless the citation is reinstated). The source shows the discount *appearing* or widening after major floods and then fading over five to six years. "Fading after floods" keeps only the second half and can be read as floods reducing the discount.
- **Suggested wording:** If reinstated: "Flood discounts average 4.6% for inland 100-year floodplains [@beltran2018flood, abstract], jump after floods, then fade [@bin2013changes]." (13 words against the earlier 15.)

### `blattner2023losses`
- **Bib entry:** Blattner, L., Farinha, L. & Rebelo, F. (2023), "When Losses Turn into Loans: The Cost of Weak Banks", *American Economic Review* 113(6): 1600–1641, doi:10.1257/aer.20190149.
- **Cited in proposal:** §3 ¶2, no locator: "Moratoria change borrowers' behaviour [@dinerstein2024debt; @kim2024intermediation], uninsured damage raises delinquency [@kousky2020flood], and weak banks may hide losses [@caballero2008zombie; @blattner2023losses]."
- **Metadata:** OK. Crossref: same authors, title, journal, 113(6), pp. 1600–1641, June 2023.
- **Source opened (as of 2026-11-02):** https://api.crossref.org/works/10.1257/aer.20190149 (deposited abstract). Abstract only.
- **Source says:** "affected banks respond by cutting lending but also by reallocating credit to distressed firms with underreported loan losses. We develop a method to detect underreported losses using loan-level data." (abstract)
- **Verdict:** OK. Banks pushed below capital requirements hide losses by lending to distressed firms.
- **Suggested wording:** —

### `bot2012capital`
- **Bib entry:** Bank of Thailand (2012), ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 12/2555 เรื่อง หลักเกณฑ์การกำกับดูแลเงินกองทุนสำหรับธนาคารพาณิชย์ (*Notification FPG. 12/2555: Regulations on Supervision of Capital for Commercial Banks*), announced 8 November 2012, in force 1 January 2013.
- **Cited in proposal:** §4.3: "S* is the most probable scenario that pushes the common equity tier 1 ratio below the minimum plus buffers [@grundke2018macroeconomic]: 7% of risk-weighted assets, 8% for domestic systemically important banks [@bot2012capital, cl. 5.3.1; @bot2017dsib, cl. 4.3.2]." (locator: cl. 5.3.1)
- **Metadata:** OK. Scanned p. 1 of the Thai text: "ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 12/2555 เรื่อง หลักเกณฑ์การกำกับดูแลเงินกองทุนสำหรับธนาคารพาณิชย์". Scanned p. 14: "ประกาศนี้ให้ใช้บังคับตั้งแต่วันที่ 1 มกราคม 2556 เป็นต้นไป" (*in force from 1 January 2013*) and "ประกาศ ณ วันที่ 8 พฤศจิกายน 2555" (*announced 8 November 2012*), signed by Governor Prasarn Trairatvorakul. Whether the notification is still in force was not re-checked; the bib note says no repeal was found.
- **Source opened (as of 2026-11-02):** Thai text https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2555/ThaiPDF/25550332.pdf (HTTP 200, 17 pp.; pp. 1 and 14 scanned and read from page images) and the unofficial English translation https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2555/EngPDF/25550332.pdf (HTTP 200, 17 pp., header "18 September 2017-check"). Read: pp. 1–2, 6–8, 14–17 of each.
- **Source says:** Clause 5.3.1(1): locally incorporated banks hold "อัตราส่วนเงินกองทุนชั้นที่ 1 ที่เป็นส่วนของเจ้าของ (Common equity tier 1 ratio: CET1 ratio) 4.5" (Thai PDF p. 6). Clause 5.3.1(2.1) conservation buffer: CET1 "เพิ่มเติมจากการดำรงอัตราส่วนเงินกองทุนขั้นต่ำอีก เกินกว่าร้อยละ 2.5 ของสินทรัพย์เสี่ยงทั้งสิ้น" (*a further CET1 of more than 2.5% of total risk-weighted assets on top of the minimum*), phased in to 1 January 2019; the summary table gives CET1 "7" at "1 ม.ค. 2562" (Thai PDF p. 7; English p. 7: "CET 1 ratio 5.125 5.75 6.375 7"). Clause 5.3.1(2.2): the BOT "may require … 0% - 2.5%" countercyclical buffer on top (English p. 8).
- **Verdict:** OK. Clause 5.3.1 gives CET1 4.5% plus a 2.5% conservation buffer, so 7% of risk-weighted assets. Note: 7% assumes a zero countercyclical buffer, which the BOT may set at up to 2.5%; the current setting was not checked.
- **Suggested wording:** —

### `bot2017dsib`
- **Bib entry:** Bank of Thailand (2017), ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 16/2560 เรื่อง แนวทางการระบุและการกำกับดูแลธนาคารพาณิชย์ที่มีนัยต่อความเสี่ยงเชิงระบบในประเทศ (*Notification 16/2560 on identifying and supervising D-SIBs*), announced 31 August 2017.
- **Cited in proposal:** §4.3: "S* is the most probable scenario that pushes the common equity tier 1 ratio below the minimum plus buffers [@grundke2018macroeconomic]: 7% of risk-weighted assets, 8% for domestic systemically important banks [@bot2012capital, cl. 5.3.1; @bot2017dsib, cl. 4.3.2]." (locator: cl. 4.3.2)
- **Metadata:** OK. The Thai title in the bib matches the notification text (Thai PDF p. 4) and the BOT cover letter ธปท.ฝนส.(21)ว.1508/2560 of 2 October 2560 (scanned PDF p. 1). The cover letter says the notification was published in the Royal Gazette, "เล่ม 134 ตอนพิเศษ 235 ง ลงวันที่ 25 กันยายน 2560" (*vol. 134, special part 235 Ngor, 25 September 2017*), in force from the following day. English translation: "Announced on 31st August 2017" (p. 11). The BOT's English title is "The Assessment Methodology and Supervisory Measures for Domestic Systemically Important Banks (D-SIBs)". The bib's gloss "Guidelines on the identification and supervision of …" is a fair rendering of the Thai.
- **Source opened (as of 2026-11-02):** Thai PDF https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2560/ThaiPDF/25600245.pdf (HTTP 200, 16 pp.; cover letter p. 1 read from the page image) and English translation https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2560/EngPDF/25600245.pdf (HTTP 200, 13 pp., header "12 July 2018-check"). Read: clauses 4.3.2–5 in both.
- **Source says:** Clause 4.3.2(1): "D-SIBs shall maintain a higher Common Equity Tier 1 Ratio of 1% of total risk-weighted assets in addition to the minimum capital ratio, conservation buffer, and countercyclical buffer as higher loss absorbency for D-SIBs." (English p. 7). Clause 4.3.3(1.1) phases this in at 0.5% from 1 January 2019 and 1% from 1 January 2020. Its table gives "Total required CET1 Ratio 7.5% 8.0%" (English p. 10; Thai PDF p. 12: "รวม CET1 ratio ที่ต้องดำรง 7.5% 8.0%").
- **Verdict:** OK. Clause 4.3.2 sets the 1% add-on, and with the 7% from FPG. 12/2555 that gives 8%. The 8.0% total itself is printed in the clause 4.3.3 table. Optional locator: "cl. 4.3.2–4.3.3". As for `bot2012capital`, the 8% assumes a zero countercyclical buffer.
- **Suggested wording:** —

### `bot2018tfrs9`
- **Bib entry:** Bank of Thailand (2018), หนังสือเวียน ธปท.ฝนส.(01)ว.195/2561 นำส่งประกาศ สนส. 20–23/2561 (*circular transmitting the TFRS 9-aligned classification and provisioning notifications*), 13 December 2018.
- **Cited in proposal:** §4.2: "Outcomes are 90-day delinquency, restructuring and IFRS 9 stages [@bot2018tfrs9], with haircuts, revaluations and provisions as early LGD proxies." (no locator; the citation covers the outcome list)
- **Metadata:** Number and date OK: scanned PDF p. 1 reads "13 ธันวาคม 2561" and "ที่ ฝนส.(01)ว. 195/2561". The Thai title in the bib is a paraphrase. The actual title is "เรื่อง นำส่งประกาศธนาคารแห่งประเทศไทยที่เกี่ยวข้องกับมาตรฐานการรายงานทางการเงินกลุ่มเครื่องมือทางการเงิน" (*transmitting BOT notifications relating to the financial-instruments reporting standards*). The circular transmits four notifications (สนส. 20–23/2561, dated 31 October 2561 and published in the Royal Gazette on 11 December 2561) and one BOT policy guideline on debt restructuring. The PDF at the bib URL contains the 2-page circular and the attached notification สนส. 22/2561 (financial statements of finance and credit-foncier companies). The classification notification สนส. 23/2561 is not in this file. Suggest the exact Thai title in the bib.
- **Source opened (as of 2026-11-02):** https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2561/ThaiPDF/25610275.pdf (HTTP 200, 7 pp., fully scanned). Read from page images: PDF pp. 1–3 and 7 in full. Pp. 4–6, the body of สนส. 22/2561, were not read.
- **Source says:** Circular p. 1: the standards apply to "การจัดทำงบการเงินที่เริ่มต้นในหรือหลังวันที่ 1 มกราคม 2563" (*financial statements beginning on or after 1 January 2020*). Circular item 3 on สนส. 23/2561 (PDF p. 2): "ให้จัดชั้นสินทรัพย์และภาระผูกพันทางการเงินเป็น 3 ประเภท ได้แก่ (1) … ด้อยค่าด้านเครดิต (non-performing) (2) … เพิ่มขึ้นอย่างมีนัยสำคัญของความเสี่ยงด้านเครดิต (under-performing) และ (3) … ไม่มีการเพิ่มขึ้นอย่างมีนัยสำคัญ … (performing)" (*assets and financial commitments are classified into 3 classes: credit-impaired (non-performing), significant increase in credit risk (under-performing), and no significant increase (performing)*), with provisions for expected credit loss.
- **Verdict:** OK. The circular documents the three-class, ECL-based classification (the IFRS 9 stages) that the proposal uses as an outcome. It uses BOT class names, not "stage 1–3". Optional: also cite สนส. 23/2561 directly, and fix the bib title as above.
- **Suggested wording:** —

### `bot2024circular601`
- **Bib entry:** Bank of Thailand (2024), หนังสือเวียน ธปท.ฝนส.(01)ว.601/2567 (*circular on relaxed rules and assistance for debtors affected by disasters*), 30 August 2024.
- **Cited in proposal:**
  - §1: "The buffer was regulatory: lenders could keep debtors' pre-flood classification [@bot2011circular1564], as again after the 2024 and 2025 floods [@bot2024circular601; @bot2025level4]." (no locator)
  - §4.2: "**2024–25 (primary).** Relief followed declarations timed with the floods [@bot2024circular601] and, in 2025, covered debtors in Level-4 areas, such as Songkhla, not non-performing on 2 December 2025 at participating lenders [@bot2025level4, pp. 1–2]." (no locator)
- **Metadata:** Number and date OK: scanned p. 1 reads "30 สิงหาคม 2567" and "ที่ ธปท.ฝนส.(01) ว. 601/2567"; signed by Governor Sethaput Suthiwartnarueput (p. 4). The bib gives only an English gloss, and that gloss differs from the actual title, "เรื่อง ขอความร่วมมือให้ความช่วยเหลือลูกหนี้ที่ได้รับผลกระทบจากสาธารณภัย" (*request for cooperation in assisting debtors affected by disasters*). Add the Thai title and use this gloss.
- **Source opened (as of 2026-11-02):** https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2567/ThaiPDF/25670146.pdf (HTTP 200, 10 pp.). Circular pp. 1–4 read in full (pp. 1 and 4 from page images). Q&A attachment pp. 5–10: item 1 read.
- **Source says:**
  - Preamble (p. 1): the circular applies generally to "สาธารณภัยประเภทวาตภัย อุทกภัย และภัยแล้ง" (*windstorm, flood and drought disasters*) "ตามที่ทางการประกาศกำหนด" (*as declared by the authorities*).
  - Item 1.1 (p. 2): relief periods run up to 12 months "นับจากวันที่ผู้มีอำนาจออกประกาศเขตพื้นที่ประสบสาธารณภัย … ประกาศเขตพื้นที่ประสบสาธารณภัย หรือกองบัญชาการหรือกองอำนวยการ … ได้แจ้งระดับสถานการณ์สาธารณภัย เป็นระดับเฉพาะสีเหลือง สีส้ม หรือสีแดง" (*from the date a disaster zone is declared, or a yellow, orange or red disaster alert level is notified*).
  - Item 2.1 (p. 3): lenders "ต้องสามารถพิสูจน์หรือเชื่อมโยงผลกระทบที่เกิดขึ้น กับลูกหนี้แต่ละรายได้อย่างชัดเจน" (*must be able to show or link the impact to each debtor*).
  - Item 2.2 (p. 3): lenders "ให้สามารถคงสถานะการจัดชั้นสำหรับลูกหนี้ที่ได้รับความช่วยเหลือและยังไม่ถูกจัดชั้นเป็นสินทรัพย์ด้อยคุณภาพ ไว้ตามเดิมก่อนเกิดเหตุสาธารณภัยได้" (*may keep the pre-disaster classification of assisted debtors not yet classified as impaired*).
  - Q&A 1 (dated 5 November 2567, p. 5): affected areas may be identified from DDPM alert levels or provincial disaster-zone declarations, and the impact may be "ทางตรงหรือทางอ้อม" (*direct or indirect*).
- **Verdict:**
  - §1: **OK.** Item 2.2 allows the pre-disaster classification to be kept. The circular is a standing, all-disaster rule issued during the 2024 floods.
  - §4.2: **MINOR.** Eligibility is triggered by a disaster-zone declaration *or* a yellow, orange or red alert level, with a debtor-level link to the impact. "Declarations timed with the floods" omits the alert-level route, and "timed with the floods" is the proposal's inference, not the circular's text.
- **Suggested wording:** §4.2: "Relief followed disaster-zone declarations or alert levels [@bot2024circular601] and, in 2025, …". Add the Thai title to the bib.

### `bot2025level4`
- **Bib entry:** Bank of Thailand (2025), หนังสือเวียน ธปท. ว.8158/2568 ขอความร่วมมือให้ความช่วยเหลือลูกหนี้ที่ได้รับผลกระทบจากสาธารณภัยในเขตพื้นที่เกิดสาธารณภัยร้ายแรงอย่างยิ่ง (ระดับ 4) (*request to assist debtors in Level-4 disaster zones*), 15 December 2025.
- **Cited in proposal:**
  - §1: "The buffer was regulatory: lenders could keep debtors' pre-flood classification [@bot2011circular1564], as again after the 2024 and 2025 floods [@bot2024circular601; @bot2025level4]." (no locator)
  - §4.2: "**2024–25 (primary).** Relief followed declarations timed with the floods [@bot2024circular601] and, in 2025, covered debtors in Level-4 areas, such as Songkhla, not non-performing on 2 December 2025 at participating lenders [@bot2025level4, pp. 1–2]." (locator: pp. 1–2)
- **Metadata:** OK. Scanned p. 1 reads "15 ธันวาคม 2568" and "ที่ ธปท. ว. 8158/2568 เรื่อง ขอความร่วมมือให้ความช่วยเหลือลูกหนี้ที่ได้รับผลกระทบจากสาธารณภัยในเขตพื้นที่เกิดสาธารณภัยร้ายแรงอย่างยิ่ง (ระดับ 4)"; signed by Governor Vitai Ratanakorn (p. 4). The title matches the bib.
- **Source opened (as of 2026-11-02):** https://www.bot.or.th/content/dam/bot/fipcs/documents/FPG/2568/ThaiPDF/25680253.pdf (HTTP 200, 11 pp.). Circular pp. 1–4 read in full (pp. 1 and 4 from page images). Q&A attachment pp. 5–11 not read.
- **Source says:**
  - p. 1: the circular follows the "อุทกภัยรุนแรงในเขตพื้นที่ภาคใต้ … ในเดือนพฤศจิกายน 2568" (*severe southern floods of November 2025*), including "คำสั่งนายกรัฐมนตรี ที่ 10/2568 เรื่อง ยกระดับการจัดการสาธารณภัยร้ายแรงอย่างยิ่ง (ระดับ 4) ในพื้นที่ในจังหวัดสงขลา" (*Prime Minister's Order 10/2568 raising areas in Songkhla to Level 4*), and the Cabinet resolution of "2 ธันวาคม 2568 (วันที่คณะรัฐมนตรีมีมติฯ)" (*2 December 2025, "the Cabinet resolution date"*). The circular "ขอความร่วมมือ" (*requests the cooperation of*) all financial institutions and their group companies.
  - Item 1.2 (p. 2): principal suspension and interest waiver for up to 12 months for "ลูกหนี้รายย่อยและวิสาหกิจขนาดกลางและขนาดย่อม (SMEs)" (*retail and SME debtors*) in Level-4 zones, "ตามชุดมาตรการที่สถาบันการเงินและบริษัทลูกในกลุ่มฯ ได้ตกลงร่วมกัน" (*under the package the institutions agreed jointly*), from the debtor's "opt-in". The debtor "ต้องไม่มีสถานะเป็นหนี้ที่ไม่ก่อให้เกิดรายได้ (Non-Performing Loan: NPL) ณ วันที่คณะรัฐมนตรีมีมติฯ" (*must not be an NPL on the Cabinet resolution date*). Lenders must consider opt-ins by 31 January 2026.
  - Item 2.6 (p. 4): lenders "ให้สามารถคงวันค้างชำระสำหรับลูกหนี้ที่ได้รับความช่วยเหลือและยังไม่ถูกจัดชั้นเป็นสินทรัพย์ด้อยคุณภาพ ไว้ตามเดิมก่อนเกิดเหตุสาธารณภัยได้" (*may keep the pre-disaster days past due of assisted debtors not yet impaired*). Item 2 applies the extra relaxations to lenders assisting Level-4 debtors under ว.601/2567, whose item 2.2 allows classification retention.
- **Verdict:**
  - §1: **OK.** Item 2.6 freezes days past due, and the circular builds on ว.601/2567 classification retention, for assisted debtors not yet impaired.
  - §4.2: **MINOR.** Level 4, Songkhla, the non-NPL test and the 2 December 2025 date are all on pp. 1–2. But the moratorium covers only retail and SME debtors who opt in. The circular asks *all* institutions to cooperate under a jointly agreed package, so "at participating lenders" is the proposal's gloss.
- **Suggested wording:** §4.2: "… and, in 2025, covered retail and SME debtors in Level-4 areas, such as Songkhla, not non-performing on 2 December 2025 [@bot2025level4, pp. 1–2]." Take-up is opt-in, so eligibility (intention to treat) and actual relief differ; the earlier draft said so explicitly.

### `bot2026rppislides`
- **Bib entry:** Samritpiam, K. & Chongprasoplarp, P. (2026), "The Development of the Bank of Thailand's Residential Property Price Index (RPPI)", presentation, International Conference on Real Estate Statistics 2026, Tokyo.
- **Cited in proposal:** §3 Framework, locator "pp. 3, 7–9": "RQ1 estimates how official values respond to floods, not λ_T itself; RQ3 varies λ_B from 0 to 1 unless loan appraisals reveal it, with the Bank of Thailand's appraisal-based regional index as a coarse check [@bot2026rppislides, pp. 3, 7–9]."
- **Metadata:** OK. Title slide (PDF p. 1): "THE DEVELOPMENT OF THE BANK OF THAILAND'S RESIDENTIAL PROPERTY PRICE INDEX (RPPI)", "Mr. Kiattikhun Samritpiam", "Miss Poontharik Chongprasoplarp", "Data Management and Analytics Department, Bank of Thailand", "International Conference on Real Estate Statistics 2026, Tokyo, Japan"; 12 slides. The bib note's published-table reference (EC_EI_008_S4, Jan 2011 to Sep 2026) was not re-checked: app.bot.or.th was outside this audit's host list.
- **Source opened (as of 2026-11-02):** https://cures.hias.hit-u.ac.jp/wp-content/uploads/2026/02/BOT_RPPI_Final.pdf (HTTP 200; all 12 slides read). The file is posted publicly by the conference host; the slides show methods and aggregate shares only, with no confidential material.
- **Source says:**
  - "Ultimately, the BOT adopted appraisal price from the Mortgage Loan Data (MGL) for constructing the RPPI." "Appraisal price does not always correspond to actual transaction price and may differ across institutions." (PDF p. 3)
  - "The RPPI construction has expanded to cover not only Bangkok and its vicinities but also regional areas"; "the BOT selected only those provinces with sufficient transaction activity to serve as representatives for constructing the regional RPPIs." (PDF p. 7)
  - Province table: North "Chiang Mai, Chiang Rai, Phitsanulok, Nakhon Sawan, Lamphun (68%)"; South "Songkhla, Phuket, Surat Thani, Nakhon Si Thammarat" (PDF p. 9).
- **Verdict:** OK. The slides show a regional index built from bank appraisal prices on mortgage loans, drawn from representative provinces. That supports "appraisal-based regional index" and justifies "coarse".
- **Suggested wording:** —. (Optional: "residential" would make clear that the index covers mortgaged housing, not land.)

### `caballero2008zombie`
- **Bib entry:** Caballero, R. J., Hoshi, T. & Kashyap, A. K. (2008), "Zombie Lending and Depressed Restructuring in Japan", *American Economic Review* 98(5): 1943–1977, doi:10.1257/aer.98.5.1943.
- **Cited in proposal:** §3 ¶2, no locator (same sentence as `blattner2023losses`): "Moratoria change borrowers' behaviour [@dinerstein2024debt; @kim2024intermediation], uninsured damage raises delinquency [@kousky2020flood], and weak banks may hide losses [@caballero2008zombie; @blattner2023losses]."
- **Metadata:** OK. Crossref: same authors, title, journal, 98(5), pp. 1943–1977, November 2008.
- **Source opened (as of 2026-11-02):** Crossref (published abstract) and NBER Working Paper 12129, https://www.nber.org/system/files/working_papers/w12129/w12129.pdf (HTTP 200, 72 pp.). Read: WP abstract and introduction (PDF pp. 2–3).
- **Source says:** Published abstract: "Large Japanese banks often engaged in sham loan restructurings that kept credit flowing to otherwise insolvent borrowers". WP abstract: "most large Japanese banks were only able to comply with capital standards because regulators were lax in their inspections" (PDF p. 2). WP introduction: "The fear of falling below the capital standards led many banks to continue to extend credit to insolvent borrowers" (PDF p. 3).
- **Verdict:** OK. Capital-constrained banks evergreened loans to avoid recognising losses.
- **Suggested wording:** —

### `callaway2021difference`
- **Bib entry:** Callaway, B. & Sant'Anna, P. H. C. (2021), "Difference-in-Differences with Multiple Time Periods", *Journal of Econometrics* 225(2): 200–230, doi:10.1016/j.jeconom.2020.12.001.
- **Cited in proposal:** §4.2, no locator: "Borrowers on flooded and comparable unflooded sheets are compared month by month from a year before the floods to a year after relief ends, with the two floods as cohorts [@callaway2021difference]."
- **Metadata:** OK. Crossref: same authors, journal, 225(2), pp. 200–230, December 2021. Crossref's title casing is "Difference-in-Differences with multiple time periods".
- **Source opened (as of 2026-11-02):** Crossref and the arXiv abstract https://arxiv.org/abs/1803.09015. Abstract only.
- **Source says:** "identification, estimation, and inference procedures for treatment effect parameters using Difference-in-Differences (DiD) with (i) multiple time periods, (ii) variation in treatment timing, and (iii) when the 'parallel trends assumption' holds potentially only after conditioning on observed covariates" (arXiv abstract).
- **Verdict:** OK. This is a method citation for a monthly DiD with "the two floods as cohorts" (2024 and 2025), which is the staggered-timing case the paper covers.
- **Suggested wording:** —

### `caloia2026floods`
- **Bib entry:** Caloia, F. G., van Ginkel, K. C. H. & Jansen, D.-J. (2026), "Floods and financial stability: Scenario-based evidence from below sea level", *Journal of Financial Stability* 84: 101545, doi:10.1016/j.jfs.2026.101545.
- **Cited in proposal:** §3 ¶2, no locator: "Flood stress tests estimate capital depletion under fixed scenarios [@caloia2021flood; @caloia2026floods], the disaster that would fail a small bank [@blickle2025bad] or the probability of the 2011 scenario for one Thai bank [@chitchumnong2025physical]; none treats relief as a dimension of the breaking point."
- **Metadata:** OK. Crossref: same three authors, title, journal, vol. 84, article 101545, June 2026. OpenAlex links the DNB WP 796 and Tinbergen DP 23-083 versions.
- **Source opened (as of 2026-11-02):** https://api.crossref.org/works/10.1016/j.jfs.2026.101545 (no abstract deposited) and https://api.openalex.org/works/doi:10.1016/j.jfs.2026.101545 (abstract). Abstract only. The working paper was not re-opened in this round; the bib note records a full read.
- **Source says:** "For a set of 38 adverse scenarios, we estimate that flood-related property damages lead to capital declines that mostly range between 30 and 50 basis points." (OpenAlex abstract)
- **Verdict:** OK. The paper estimates capital depletion under a fixed set of scenarios. Note: the bib note gives "CET1 falls 30–110 bp" (from the working paper), while the abstract says "mostly … between 30 and 50 basis points". The proposal quotes neither figure, so nothing needs changing in the text; align the bib note.
- **Suggested wording:** —

### `cameron2008bootstrap`
- **Bib entry:** Cameron, A. C., Gelbach, J. B. & Miller, D. L. (2008), "Bootstrap-Based Improvements for Inference with Clustered Errors", *Review of Economics and Statistics* 90(3): 414–427, doi:10.1162/rest.90.3.414.
- **Cited in proposal:** §4.1 Inference and power, no locator: "Inference uses 1,000 placebo footprints shifted within province onto equally low-lying dry sheets, with the wild cluster bootstrap [@cameron2008bootstrap] as a check."
- **Metadata:** OK. Crossref: same authors, title, journal, 90(3), pp. 414–427, August 2008.
- **Source opened (as of 2026-11-02):** Crossref; OpenAlex (published abstract); NBER Technical Working Paper 344, https://www.nber.org/system/files/working_papers/t0344/t0344.pdf (HTTP 200, 64 pp.). Read: abstract and Section 3.2 (PDF pp. 18–19).
- **Source says:** "3.2 Residual and Wild Cluster Bootstrap-t … The wild bootstrap relaxes both these restrictions. This procedure creates pseudo-samples based on û*g = ûg with probability 0.5 and û*g = −ûg with probability 0.5, with this assignment at the cluster level." "Here we have extended the wild bootstrap to the clustered setting." (WP PDF pp. 18–19, printed pp. 18–19)
- **Verdict:** OK. The wild cluster bootstrap comes from this paper. The published abstract does not name it; the working paper's Section 3.2 does.
- **Suggested wording:** —

### `chongwilaikasaem2022flood`
- **Bib entry:** Chongwilaikasaem, S. & Chalermyanont, T. (2023), "Flood hazards and housing prices: a spatial regression analysis for Hat Yai, Songkhla, Thailand", *International Journal of Housing Markets and Analysis* 16(6): 1052–1070, doi:10.1108/IJHMA-04-2022-0053.
- **Cited in proposal:** §3 ¶1, no locator: "Closest to RQ1, Australian statutory valuations discount known flooded areas [@fuerst2021pricing]; New York assessments fell after Hurricane Sandy for inundated homes but not for undamaged high-risk homes whose prices fell [@guo2025rising]; English lender valuations did not follow prices down [@garbarino2021high]; in Hat Yai, flood risk lowers rents and official valuations in a cross-section [@chongwilaikasaem2022flood]; and Semarang's official land-value zones rose least where tidal flooding recurs [@utami2021impact]."
- **Metadata:** OK. Crossref: same authors, title, journal, 16(6), pp. 1052–1070; online 29 July 2022, print issue 27 November 2023. The bib's 2023 follows the print issue; the key's "2022" is only a label.
- **Source opened (as of 2026-11-02):** https://api.crossref.org/works/10.1108/IJHMA-04-2022-0053 (structured abstract). Abstract only.
- **Source says:** "The main analysis examines the degree of flood risk and housing rental prices from our survey of 380 residences. To test the robustness of the results, the authors examine a different data set of the same samples by using the official property valuation from the Ministry of Finance … The authors find that flood risk has a negative impact on property prices in Hat Yai, which is consistent with both models." (abstract)
- **Verdict:** OK. Rents (main analysis) and official valuations (robustness check) both fall with flood risk, in a cross-section.
- **Suggested wording:** —

### `dinerstein2024debt`
- **Bib entry:** Dinerstein, M., Yannelis, C. & Chen, C.-T. (2024), "Debt Moratoria: Evidence from Student Loan Forbearance", *American Economic Review: Insights* 6(2): 196–213, doi:10.1257/aeri.20230032.
- **Cited in proposal:** §3 ¶2, no locator: "Moratoria change borrowers' behaviour [@dinerstein2024debt; @kim2024intermediation], uninsured damage raises delinquency [@kousky2020flood], and weak banks may hide losses [@caballero2008zombie; @blattner2023losses]."
- **Metadata:** OK. Crossref: same authors, title, journal, 6(2), pp. 196–213, June 2024.
- **Source opened (as of 2026-11-02):** https://api.crossref.org/works/10.1257/aeri.20230032 (deposited abstract). Abstract only.
- **Source says:** "We estimate that borrowers used the new liquidity to increase borrowing on mortgages, auto loans, and credit cards rather than avoid delinquencies." (abstract)
- **Verdict:** OK.
- **Suggested wording:** —

### `dottori2016global`
- **Bib entry:** Dottori, F. et al. (6 authors) (2016), "Development and evaluation of a framework for global flood hazard mapping", *Advances in Water Resources* 94: 87–102, doi:10.1016/j.advwatres.2016.05.002.
- **Cited in proposal:** §4.3, no locator: "Scenarios use return-period maps up to 1,000 years [@ward2020aqueduct; @dottori2016global], under full dependence and independence across basins, with Asian depth–damage functions that include Thai data [@huizinga2017global, p. 13]."
- **Metadata:** OK. Crossref: same six authors, title, journal, vol. 94, pp. 87–102, August 2016. The ORA record gives the licence as CC BY.
- **Source opened (as of 2026-11-02):** Crossref; OpenAlex (abstract); version of record on Oxford ORA, https://ora.ox.ac.uk/objects/uuid:72456b6b-82f5-40f2-9904-6e8698b6682f (HTTP 200; PDF 16 pp.). Read: abstract and Section 4 opening (PDF p. 7, printed p. 93).
- **Source says:** "The mapping procedure has been used in each continent to produce flood hazard maps with return periods of 10, 25, 50, 100, 250, 500 and 1000 years." (Section 4, PDF p. 7, printed p. 93)
- **Verdict:** OK. Note: the bib note records that the current JRC data release (Baugh et al. 2024) runs only to 500 years. If that is the file used, the 1,000-year layer comes from Aqueduct alone. This round did not re-check the JRC catalogue.
- **Suggested wording:** —

### `esa2022copdem`
- **Bib entry:** European Space Agency & Airbus (2022), *Copernicus DEM*, dataset, doi:10.5270/ESA-c5d3d65.
- **Cited in proposal:** §4.1 Data, no locator: "Flood maps are the Global Flood Database for 2011 [@tellman2021satellite], my nationwide Sentinel-1 radar maps for 2024–25 and UNOSAT's 2024 extents for Chiang Rai and Phayao; elevation is from Copernicus [@esa2022copdem], permanent water from @pekel2016high, land cover from @zanaga2022worldcover."
- **Metadata:** OK. Crossref: type "dataset", title "Copernicus DEM", authors "European Space Agency; Airbus", publisher European Space Agency, issued 2022.
- **Source opened (as of 2026-11-02):** https://api.crossref.org/works/10.5270/ESA-c5d3d65 and https://copernicus-dem-30m.s3.amazonaws.com/readme.html (HTTP 200).
- **Source says:** "The Copernicus DEM is a Digital Surface Model (DSM) which represents the surface of the Earth including buildings, infrastructure and vegetation. … GLO-30 Public provides limited worldwide coverage at 30 meters" (AWS readme).
- **Verdict:** OK. Note for methods, not the citation: the product is a surface model, so heights in built-up or forested sheets include buildings and canopy. That matters for the "height above the local valley floor" control.
- **Suggested wording:** —

### `fuerst2021pricing`
- **Bib entry:** Fuerst, F. & Warren-Myers, G. (2021), "Pricing Climate Risk: Are Flooding and Sea Level Rise Risk Capitalised in Australian Residential Property?", *Climate Risk Management* 34: 100361, doi:10.1016/j.crm.2021.100361.
- **Cited in proposal:**
  - §3 ¶1, no locator: "Closest to RQ1, Australian statutory valuations discount known flooded areas [@fuerst2021pricing]; New York assessments fell after Hurricane Sandy … [@guo2025rising]; … and Semarang's official land-value zones rose least where tidal flooding recurs [@utami2021impact]."
- **Metadata:** OK. Crossref: same authors, journal, vol. 34, article 100361, 2021. Crossref's title casing is "Pricing climate risk: Are flooding and sea level rise risk capitalised in Australian residential property?".
- **Source opened (as of 2026-11-02):** OpenAlex (abstract) and the published version (CC BY-NC-ND) in an open-access university repository (doi:10.1016/j.crm.2021.100361 for the publisher version) (HTTP 200, 28 pp.). Read: abstract, data section (PDF pp. 5–6), Sections 5.2–5.3 (PDF pp. 9–10) and the discussion (PDF p. 12).
- **Source says:**
  - Abstract: "A valuation discount effect is identified for properties in known flooded areas".
  - The data are for one municipality: "The data collected from the case study municipality, the City of Port Phillip, comprised information held as part of the statutory rating valuation procedure" (PDF p. 5).
  - Flood risk is defined by planning overlays, not observed floods: "The risk of flooding for any property included in this study is captured through the statutory planning overlays" (PDF p. 6).
  - Section 5.3 "Statutory valuations": the analysis uses "2016 Capital Values as appraised by the municipal valuers … current flood risk attracts a valuation discount as expected" (PDF p. 10, printed p. 10). Sales prices show "negative but not significant" flood effects (Section 5.2, same page).
- **Verdict:**
  - §3: **MINOR.** The statutory-valuation discount is supported. But the evidence comes from one Melbourne municipality, and "known flooded areas" (the abstract's phrase) means designated flood-overlay zones, not areas that have flooded. That distinction matters in a paragraph about responses to floods.
- **Suggested wording:** §3: "Closest to RQ1, Melbourne statutory valuations discount designated flood zones [@fuerst2021pricing]; …" (same length).

### `huizinga2017global`
- **Bib entry:** Huizinga, J., de Moel, H. & Szewczyk, W. (2017), *Global flood depth-damage functions: Methodology and the database with guidelines*, JRC Technical Report EUR 28552 EN, doi:10.2760/16510.
- **Cited in proposal:** §4.3, locator "p. 13": "Scenarios use return-period maps up to 1,000 years [@ward2020aqueduct; @dottori2016global], under full dependence and independence across basins, with Asian depth–damage functions that include Thai data [@huizinga2017global, p. 13]."
- **Metadata:** OK. Colophon (PDF p. 2): "JRC105688 … PDF ISBN 978-92-79-67781-6 ISSN 1831-9424 doi: 10.2760/16510 … Luxembourg: Publications Office of the European Union, 2017". The DOI is not in Crossref (HTTP 404); doi.org resolves it (HTTP 302 to op.europa.eu).
- **Source opened (as of 2026-11-02):** https://publications.jrc.ec.europa.eu/repository/bitstream/JRC105688/global_flood_depth-damage_functions__10042017.pdf (HTTP 200, 114 pp.). Read: colophon and the Asia residential subsection (PDF p. 17, printed p. 13); searched the full text for "Thailand".
- **Source says:** "Asia: Figure 3-3: Damage per square meter for Asia - residential buildings. The countries in the figure comprise Bangladesh, Cambodia, Taiwan, China, Indonesia, Thailand, Vietnam, Laos and Japan." (PDF p. 17, printed p. 13). The industry curves also include "Thailand (Bangkok)" (PDF p. 30, printed p. 26).
- **Verdict:** OK. The page and the content match.
- **Suggested wording:** —

### `kim2024intermediation`
- **Bib entry:** Kim, Y. S., Lee, D., Scharlemann, T. & Vickery, J. (2024), "Intermediation frictions in debt relief: Evidence from CARES Act forbearance", *Journal of Financial Economics* 158: 103873, doi:10.1016/j.jfineco.2024.103873.
- **Cited in proposal:** §3 ¶2, no locator (same sentence as `dinerstein2024debt`): "Moratoria change borrowers' behaviour [@dinerstein2024debt; @kim2024intermediation], uninsured damage raises delinquency [@kousky2020flood], and weak banks may hide losses [@caballero2008zombie; @blattner2023losses]."
- **Metadata:** OK. Crossref: same four authors, title, journal, vol. 158, article 103873, August 2024.
- **Source opened (as of 2026-11-02):** Crossref (no abstract deposited) and the IDEAS abstract https://ideas.repec.org/a/eee/jfinec/v158y2024ics0304405x24000965.html. Abstract only.
- **Source says:** "Easier access to forbearance substantially increased mortgage nonpayment but also reduced delinquencies outside of forbearance. Part of the liquidity from forbearance was used to reduce credit card debt, but most was saved or used for nondurable consumption." (abstract)
- **Verdict:** OK.
- **Suggested wording:** —

### `kolesar2018inference`
- **Bib entry:** Kolesár, M. & Rothe, C. (2018), "Inference in Regression Discontinuity Designs with a Discrete Running Variable", *American Economic Review* 108(8): 2277–2304, doi:10.1257/aer.20160945.
- **Cited in proposal:** §4.2, 2011 extension, no locator: "Relief covered debtors at most three months overdue [@bot2011circular1564, Q&A 2]. A fuzzy discontinuity there [@kolesar2018inference], differenced between declared and undeclared flooded areas to net out the classification boundary (pre-flood years test this), identifies relief for borrowers already in arrears."
- **Metadata:** OK. Crossref: same authors, title, journal, 108(8), pp. 2277–2304, August 2018.
- **Source opened (as of 2026-11-02):** Crossref (published abstract); arXiv 1606.04086 (v. 21 November 2017), https://arxiv.org/pdf/1606.04086 (HTTP 200, 62 pp.). Read: abstract and Section 2 setup (PDF p. 11); searched the full text for "fuzzy".
- **Source says:** "We consider inference in regression discontinuity designs when the running variable only takes a moderate number of distinct values." (abstract). Footnote 5: "While the issues that we study in this paper also arise in fuzzy RDDs and regression kink designs (Card et al., 2015), for ease of exposition we focus here on the sharp case." (arXiv PDF p. 11)
- **Verdict:** MINOR. The paper is about *inference with a discrete running variable* and is written for the sharp case. Placed after "a fuzzy discontinuity there", the citation reads as a fuzzy-RD reference. The reason it is relevant, that days or months overdue is discrete, is not stated.
- **Suggested wording:** "A fuzzy discontinuity in discrete months overdue [@kolesar2018inference], differenced between declared and undeclared flooded areas, netting out the boundary (pre-flood years test this), identifies relief for borrowers in arrears." (27 words against 28.)

### `kousky2020flood`
- **Bib entry:** Kousky, C., Palim, M. & Pan, Y. (2020), "Flood Damage and Mortgage Credit Risk: A Case Study of Hurricane Harvey", *Journal of Housing Research* 29(sup1): S86–S120, doi:10.1080/10527001.2020.1840131.
- **Cited in proposal:** §3 ¶2, no locator: "Moratoria change borrowers' behaviour [@dinerstein2024debt; @kim2024intermediation], uninsured damage raises delinquency [@kousky2020flood], and weak banks may hide losses [@caballero2008zombie; @blattner2023losses]."
- **Metadata:** OK. Crossref: same authors, title, journal, 29(sup1), pp. S86–S120; online 30 November 2020.
- **Source opened (as of 2026-11-02):** Crossref and OpenAlex (abstract). Abstract only; the Taylor & Francis PDF was not opened (the bib note records HTTP 403 on the publisher page).
- **Source says:** "In areas where flood insurance is not required, and very few borrowers have flood insurance, we find that as property damage increases, the likelihood of needing a loan modification increases, as does the likelihood of a loan being 180 or more days delinquent or in default during the two years following Hurricane Harvey." (abstract)
- **Verdict:** OK. Strictly, the comparison is by insurance-requirement zone, not by each borrower's insurance status, but the authors draw the insurance conclusion themselves ("flood insurance protects homeowners and mortgage creditors against credit risk").
- **Suggested wording:** —

### `lee2009training`
- **Bib entry:** Lee, D. S. (2009), "Training, Wages, and Sample Selection: Estimating Sharp Bounds on Treatment Effects", *Review of Economic Studies* 76(3): 1071–1102, doi:10.1111/j.1467-937X.2009.00536.x.
- **Cited in proposal:** §4.1 Outcome, no locator: "The primary outcome is the change in log value per square wah between rounds, sheets weighted equally; secondary outcomes are carry-over and, bounded for selection [@lee2009training], the change where values moved."
- **Metadata:** OK. Crossref: same author, title, journal, 76(3), pp. 1071–1102, July 2009.
- **Source opened (as of 2026-11-02):** Crossref and OpenAlex (abstract). Abstract only.
- **Source says:** "This paper develops an intuitive trimming procedure for bounding average treatment effects in the presence of sample selection. In contrast to existing methods, the procedure requires neither exclusion restrictions nor a bounded support for the outcome of interest." (abstract)
- **Verdict:** OK. Values are observed to move only if they are not carried over, which is the selection problem Lee bounds address. (The method assumes treatment is as good as random and affects selection in one direction only; the pre-analysis plan should state both.)
- **Suggested wording:** —

### `mgr2012appraisal`
- **Bib entry:** MGR Online (2012), "ธนารักษ์" ลั่นประกาศราคาที่ดินใหม่ 1 ก.ค. ยันพื้นที่น้ำท่วมไม่กระทบ [*Treasury confirms new land values from 1 July; says flooded areas not affected*], 15 June 2012.
- **Cited in proposal:** §2 RQ1, no locator: "After 2011, the Treasury reported no fall in flooded areas and left values unchanged [@mgr2012appraisal]."
- **Metadata:** OK. Headline matches the bib title; timestamp "15 มิ.ย. 2555 10:59" (15 June 2012). The source is a press report of statements by the Treasury Director-General, นายนริศ ชัยสูตร.
- **Source opened (as of 2026-11-02):** https://mgronline.com/stockmarket/detail/9550000073410 (HTTP 200; full article read; robots.txt has no disallow rules).
- **Source says:** The new values take effect 1 July 2012 "หลังจากเลื่อนการประกาศใช้มา 6 เดือน ... เนื่องจากผลกระทบจากปัญหาน้ำท่วม" (*after a six-month postponement because of the floods*). They are the schedule compiled "เมื่อช่วงปลายปี 2554 โดยราคาจะไม่มีการเปลี่ยนแปลงใด แม้ว่าในช่วงที่เลื่อนใช้มา 6 เดือนแล้วก็ตาม และได้มีการสำรวจราคาในพื้นที่น้ำท่วมเพื่อเตรียมไว้ปรับปรุงใหม่ แต่ไม่พบว่าราคาที่ดินในเขตน้ำท่วมลดต่ำลง โดยผลสำรวจพบว่า พื้นที่บางจังหวัด เช่น นครสวรรค์ กลับมีราคาที่ปรับตัวเพิ่มขึ้น" (*in late 2011, with no change despite the six-month postponement; prices in flooded areas were surveyed with a view to revision, but no fall was found, and in some provinces such as Nakhon Sawan prices rose*) (article body, para 3). The same schedule raised values by "เฉลี่ย 21.34%" (*21.34% on average*) over 29.3 million parcels (para 4).
- **Verdict:** MINOR. The substance is supported, but "left values unchanged" sits next to the proposal's definition of carry-over ("values unchanged between rounds") and could be read as no change from the previous round. In fact the Treasury left its late-2011 schedule unrevised, and that schedule raised values by 21.34% on average.
- **Suggested wording:** "The Treasury found no post-2011 fall in flooded areas and left its schedule unrevised [@mgr2012appraisal]." (14 words, as in the original.)

### `quan1991price`
- **Bib entry:** Quan, D. C. & Quigley, J. M. (1991), "Price Formation and the Appraisal Function in Real Estate Markets", *Journal of Real Estate Finance and Economics* 4(2): 127–146, doi:10.1007/BF00173120.
- **Cited in proposal:** **No longer cited** in the version saved at 20:29. Earlier the key appeared in §3 ¶1, with no locator: "Valuations may lag prices by design [@quan1991price; @avenancioleon2022assessment]."
- **Metadata:** OK. Crossref: same authors, title, journal, 4(2), June 1991; no pages are deposited. IDEAS gives pp. 127–146.
- **Source opened (as of 2026-11-02):** Crossref and the IDEAS abstract https://ideas.repec.org/a/kap/jrefec/v4y1991i2p127-46.html. Abstract only.
- **Source says:** "The appraiser's role is formalized as the task of signal extraction. … Based on the model, it is shown that contrary to popular perceptions, appraisal smoothing is consistent with an optimal updating strategy." (abstract)
- **Verdict:** OK, for the earlier wording: optimal smoothing supports "lag … by design". The key is now uncited; check that the reference list does not print it.
- **Suggested wording:** —

### `th2019valuationact`
- **Bib entry:** Kingdom of Thailand (2019), พระราชบัญญัติการประเมินราคาทรัพย์สินเพื่อประโยชน์แห่งรัฐ พ.ศ. 2562 [*Property Valuation for the Public Interest Act, B.E. 2562*], Royal Gazette Vol. 136, Part 68 Kor, 25 May 2019.
- **Cited in proposal:**
  - §1 ¶2, locator "s. 19": "Whether low post-flood default reflects resilience or deferral matters wherever insurance is thin; Thailand makes it observable, as relief follows documented rules and official values are reset nationwide every four years [@th2019valuationact, s. 19]."
  - §7 timeline, "Now to application", locator "s. 19" (twice): "The 2027–30 round must be published at least 30 days before it takes effect [@th2019valuationact, s. 19], so by 2 December 2026 for a 1 January 2027 start; Treasury offices were briefed in October 2026 on extending current schedules, and a provincial committee considered an extension on 2 November, which could delay the round by up to a year [@th2019valuationact, s. 19; @treasury2026extbriefing; @treasury2026chachoengsao]."
  - §7 timeline, "Year 1", locator "s. 19": "If the round is postponed (the law allows one year [@th2019valuationact, s. 19]), the first comparison moves here."
- **Metadata:** OK. Every page of the Thai text carries the footer "เล่ม ๑๓๖ ตอนที่ ๖๘ ก ราชกิจจานุเบกษา ๒๕ พฤษภาคม ๒๕๖๒"; royal assent "ให้ไว้ ณ วันที่ ๒๔ พฤษภาคม พ.ศ. ๒๕๖๒" (PDF p. 1). The English translation's footnote gives "The Government Gazette, Vol. 136/Part 68 a/page 19/25 May 2019" (PDF p. 1). Note: the bib `url` is the Thai Gazette text, while `howpublished` names the Council of State English translation; the translation sits at a different Treasury URL (below) and could be added.
- **Source opened (as of 2026-11-02):** Thai text https://www.treasury.go.th/medias/treasury-intranet/1/post/laws_regulations-80/live/77_1768470668_45efd8473fb2b2907e66c0575a1be045.pdf (HTTP 200, 13 pp.; s. 19 read in full, PDF pp. 6–7, Gazette pp. 24–25); English translation https://www.treasury.go.th/medias/treasury-intranet/1/post/laws_regulations-80/live/77_1768470666_5e20c6f57bb59b7bbf4be4acf5ea18a2.pdf (HTTP 200; s. 19, PDF p. 6).
- **Source says:**
  - Four-year cycle and 30-day notice: "ให้คณะกรรมการประจำจังหวัดประกาศบัญชีราคาประเมินที่ดินหรือสิ่งปลูกสร้าง ที่จัดทำตามมาตรา ๑๘ ทุกรอบสี่ปี โดยต้องประกาศล่วงหน้าก่อนวันเริ่มใช้บัญชีเป็นเวลาไม่น้อยกว่าสามสิบวัน" (*the provincial committee shall announce the land or building valuation schedules every four-year round, at least thirty days before the schedules take effect*) (s. 19 para 1, PDF p. 6). Start date: "ให้เริ่มใช้ ณ วันที่ ๑ มกราคม ของปีที่คณะกรรมการกำหนด" (*to take effect on 1 January of the year the Committee sets*) (para 2).
  - Extension: "อาจประกาศขยายเวลาให้ใช้บัญชีราคาประเมินที่ดินหรือสิ่งปลูกสร้างที่ใช้อยู่แล้วต่อไปได้ แต่ต้องไม่เกินหนึ่งปีนับแต่วันที่บัญชีดังกล่าวมีผลใช้บังคับครบสี่ปี" (*may announce an extension of the current schedules, but not beyond one year after the schedules complete four years in force*); the next round's schedule then runs only for "ระยะเวลาที่เหลืออยู่ของรอบบัญชีนั้น" (*the remaining period of that round*) (para 3, PDF p. 7). English: "the extension period must not be longer than one year after the expiration of the schedules' four-year term" (PDF p. 6).
  - Arithmetic: 30 days before 1 January 2027 is 2 December 2026, so "by 2 December 2026" is correct.
- **Verdict:** OK. Section 19 supports the four-year cycle, the 30-day notice (and the date follows from it) and the one-year extension limit. "Nationwide" (added to the §1 sentence during this audit) fits para 2: schedules start "ณ วันที่ ๑ มกราคม ของปีที่คณะกรรมการกำหนด", a single start date set by the central committee.
- **Suggested wording:** —. (Optional: s. 20 allows revision within a round, so "reset every four years" is the default cycle, as the round-1 audit noted.)

### `treasury2026chachoengsao`
- **Bib entry:** กรมธนารักษ์ (Treasury Department) (2026), การประชุมคณะกรรมการประเมินราคาทรัพย์สินเพื่อประโยชน์แห่งรัฐ ประจำจังหวัดฉะเชิงเทรา ครั้งที่ 3/2569 [*Meeting 3/2569 of the Chachoengsao provincial committee on state property appraisal*], provincial news, 2 November 2026.
- **Cited in proposal:** §7 timeline, "Now to application", no locator. Current draft (20:33): "The 2027–30 round must be published at least 30 days before it takes effect [@th2019valuationact, s. 19], so by 2 December 2026 for a 1 January 2027 start; Treasury offices were briefed in October 2026 on extending current schedules, and a provincial committee considered an extension on 2 November, which could delay the round by up to a year [@th2019valuationact, s. 19; @treasury2026extbriefing; @treasury2026chachoengsao]." Earlier wording, audited first: "… Treasury offices were briefed in October 2026 on extending current schedules, which could delay it by up to a year [@th2019valuationact, s. 19; @treasury2026extbriefing; @treasury2026chachoengsao]."
- **Metadata:** OK. Heading matches the bib title (the page adds "ณ ห้องประชุมชั้น 2 สำนักงานธนารักษ์พื้นที่ฉะเชิงเทรา"); dated "2 พ.ย. 2569" (2 Nov 2026); posted by สำนักงานธนารักษ์พื้นที่ฉะเชิงเทรา.
- **Source opened (as of 2026-11-02):** https://www.treasury.go.th/th/news/provinces-news/provinces-news-20261102-111 (HTTP 200; full item text read).
- **Source says:** "วันจันทร์ที่ 2 พฤศจิกายน 2569 ... รองผู้ว่าราชการจังหวัดฉะเชิงเทรา เป็นประธานกรรมการ การประชุมคณะกรรมการประเมินราคาทรัพย์สินเพื่อประโยชน์แห่งรัฐ ประจำจังหวัดฉะเชิงเทรา ครั้งที่ 3/2569 ... เพื่อพิจารณา 1. เรื่องการขยายเวลาให้ใช้บัญชีราคาประเมินที่ดิน ... และบัญชีราคาประเมินสิ่งปลูกสร้าง รอบบัญชี พ.ศ. 2566 – 2569 2. กำหนดพื้นที่และกำหนดระยะเวลาที่จะดำเนินการสำรวจที่ดิน" (*on Monday 2 November 2026 the deputy provincial governor chaired meeting 3/2569 of the Chachoengsao provincial committee to consider 1. extending the use of the land and building appraisal schedules of the 2023–2026 round, 2. setting the area and period of the land survey*) (item body).
- **Verdict:** OK for the current draft, which now says "a provincial committee considered an extension on 2 November". That matches the page, and the draft does not claim the extension was approved. The earlier wording was **MINOR**: the page is a committee meeting on 2 November 2026, not an October briefing.
- **Suggested wording:** —. The draft fixed this during the audit. The fix offered for the earlier wording was "In October–November 2026 Treasury offices and committees discussed extending current schedules, which could delay it by up to a year [...]".

### `treasury2026extbriefing`
- **Bib entry:** กรมธนารักษ์ (Treasury Department) (2026), ธนารักษ์พื้นที่สุพรรณบุรี มอบหมายส่วนประเมินราคาทรัพย์สิน ร่วมประชุมการขยายประกาศใช้บัญชีราคาประเมินทรัพย์สิน [*Suphanburi Area Treasury Office joins meeting on extending the use of the property appraisal schedules*], provincial news, 28 October 2026.
- **Cited in proposal:** §7 timeline, "Now to application", no locator. Current draft (20:33): "The 2027–30 round must be published at least 30 days before it takes effect [@th2019valuationact, s. 19], so by 2 December 2026 for a 1 January 2027 start; Treasury offices were briefed in October 2026 on extending current schedules, and a provincial committee considered an extension on 2 November, which could delay the round by up to a year [@th2019valuationact, s. 19; @treasury2026extbriefing; @treasury2026chachoengsao]." (The earlier wording ended "…briefed in October 2026 on extending current schedules, which could delay it by up to a year [...]".)
- **Metadata:** OK. Page heading matches the bib title word for word; posted by สำนักงานธนารักษ์พื้นที่สุพรรณบุรี, dated "28 ต.ค. 2569" (28 Oct 2026).
- **Source opened (as of 2026-11-02):** https://www.treasury.go.th/th/news/provinces-news/provinces-news-20261028-565 (HTTP 200; full item text read; robots.txt allows all).
- **Source says:** "วันพุธที่ 28 ตุลาคม 2569 ... ร่วมประชุมการขยายประกาศใช้บัญชีราคาประเมินทรัพย์สิน เพื่อซักซ้อมความเข้าใจการขยายประกาศใช้บัญชีราคาประเมินทรัพย์สินของสำนักงานธนารักษ์พื้นที่ ผ่านระบบประชุมทางไกล (Video Conference)" (*on Wednesday 28 October 2026 ... joined the meeting on extending the property appraisal schedules, to rehearse the understanding of area treasury offices on extending the schedules, by video conference*) (item body).
- **Verdict:** OK. A video-conference briefing for area treasury offices on extending the schedules, dated 28 October 2026, supports "briefed in October 2026 on extending current schedules". Only the Suphanburi office's attendance is reported; that other offices took part is inferred from the plural "สำนักงานธนารักษ์พื้นที่" and the video-conference format.
- **Suggested wording:** —

### `utami2021impact`
- **Bib entry:** Utami, W., Wibowo, Y. A. & Permadi, F. B. (2021), "The Impact of Tidal Flooding on Decreasing Land Values in the Areas of Tugu District, Semarang City", *Jurnal Ilmu Lingkungan* 19(1): 10–20, doi:10.14710/jil.19.1.10-20.
- **Cited in proposal:** §3 ¶1, no locator: "... in Hat Yai, flood risk lowers rents and official valuations in a cross-section [@chongwilaikasaem2022flood]; and Semarang's official land-value zones rose least where tidal flooding recurs [@utami2021impact]."
- **Metadata:** OK. Crossref gives the same title, three authors, journal, 19(1), pp. 10–20, issued 28 April 2021, matching the journal's citation meta tags. Note: the PDF's own "Citation" line says "...in the Coastal Areas of Tugu District..." (PDF p. 1). The bib follows the Crossref and article title, which is correct.
- **Source opened (as of 2026-11-02):** landing page https://ejournal.undip.ac.id/index.php/ilmulingkungan/article/view/33521 and PDF https://ejournal.undip.ac.id/index.php/ilmulingkungan/article/download/33521/pdf (HTTP 200, 11 pp.; read in full except the reference list); Crossref https://api.crossref.org/works/10.14710/jil.19.1.10-20.
- **Source says:**
  - Data: "Land Value Zoning (ZNT) maps obtained from the Semarang BPN Regional Office covering the 2014, 2016, 2018, and 2019 ZNT maps" (PDF p. 2, printed p. 11). The paper's zones 1–4 are the authors' own grouping of the study area: "zone 4 is the area most affected by tidal flooding and is located close to the coastline" (PDF p. 8, printed p. 17).
  - Result: "zone 1 and a price increase of ± Rp 3.500.000; zone 2 price increase ± Rp 575.000, zone 3 at a price range of Rp 385.000, and zone 4 as the tidal flood prone zone only experienced an increase of Rp 250.000" (abstract, PDF p. 1). Also: "zone 1 ... has an increase in prices 13 times more than zone 4" (Conclusion, PDF p. 9, printed p. 18).
  - The falls in the title come from the market survey, not the ZNT maps: "periodically inundated land has experienced a price decline in the range of Rp 100.000 – 200.000" (abstract). Near the coast, market prices are "Rp 200.000/m2 to Rp 300.000/m2", against Rp 3–5 million on the main road (PDF p. 6, printed p. 15).
  - Method: map overlay only, with no controls (PDF p. 2).
- **Verdict:** MINOR. The official ZNT values did rise least in the tidal-flood zone, so "rose least" fits the official zones and not the title's "decreasing". But the paper reports only rupiah changes, not percentages. Coastal land starts far cheaper (market prices about Rp 200,000–300,000/m² against Rp 3–5 million on the main road), so the zone-4 rise need not be the smallest in proportion, which is what the proposal's log-value framing implies.
- **Suggested wording:** "Semarang's official zone values gained fewest rupiah near tidal flooding [@utami2021impact]." (10 words, as in the original clause.)

### `ward2020aqueduct`
- **Bib entry:** Ward, P. J. et al. (26 authors) (2020), *Aqueduct Floods Methodology*, WRI Technical Note, April 2020.
- **Cited in proposal:** §4.3, no locator: "Scenarios use return-period maps up to 1,000 years [@ward2020aqueduct; @dottori2016global], under full dependence and independence across basins, with Asian depth–damage functions that include Thai data [@huizinga2017global, p. 13]."
- **Metadata:** OK. The WRI landing page gives "Technical Note Aqueduct Floods Methodology … April 23, 2020 28 Pages". Its author list, from "Philip J. Ward, Hessel C. Winsemius, Samantha Kuzma …" onwards, matches the bib in full and in order, ending "Martin Verlaan, Timothy Tiggeloven and Tianyi Luo". The technical-note PDF was not opened (the bib note records that files.wri.org disallows crawlers).
- **Source opened (as of 2026-11-02):** https://www.wri.org/research/aqueduct-floods-methodology (HTTP 200) and https://developers.google.com/earth-engine/datasets/catalog/WRI_Aqueduct_Flood_Hazard_Maps_V2 (HTTP 200).
- **Source says:** "The flood hazard maps are generated for return periods of 1, 2, 5, 10, 25, 50, 100, 250, 500, and 1000 years." "Pixel size: 1000 meters". "The WRI datasets are available without restriction on use or distribution." (GEE catalogue)
- **Verdict:** OK.
- **Suggested wording:** —

### `zanaga2022worldcover`
- **Bib entry:** Zanaga, D. et al. (2022), *ESA WorldCover 10 m 2021 v200*, Zenodo, doi:10.5281/zenodo.7254221.
- **Cited in proposal:**
  - §4.1 Data, no locator: "Flood maps are the Global Flood Database for 2011 [@tellman2021satellite], my nationwide Sentinel-1 radar maps for 2024–25 and UNOSAT's 2024 extents for Chiang Rai and Phayao; elevation is from Copernicus [@esa2022copdem], permanent water from @pekel2016high, land cover from @zanaga2022worldcover."
  - §5, Figure 2 sources, no locator: "*Sources:* Treasury Department; Global Flood Database [@tellman2021satellite]; ESA WorldCover [@zanaga2022worldcover]; author's calculations."
- **Metadata:** OK. DataCite: title "ESA WorldCover 10 m 2021 v200", publication year 2022, publisher Zenodo, 16 creators (first four as in the bib), licence CC BY 4.0. The DOI is a DataCite DOI, so Crossref returns 404, as expected.
- **Source opened (as of 2026-11-02):** https://api.datacite.org/dois/10.5281/zenodo.7254221 (HTTP 200).
- **Source says:** (metadata record) titles "ESA WorldCover 10 m 2021 v200"; rights "Creative Commons Attribution 4.0 International".
- **Verdict:** OK. The dataset is the 2021 map, consistent with "2021 land cover" in §4.1.
- **Suggested wording:** —

---

## 3. Bibliography notes (no reference is wrong; small fixes only)

- **`bot2018tfrs9`**: the Thai title in the bib is a paraphrase. The circular's title is "นำส่งประกาศธนาคารแห่งประเทศไทยที่เกี่ยวข้องกับมาตรฐานการรายงานทางการเงินกลุ่มเครื่องมือทางการเงิน". The PDF at the bib URL holds the circular and สนส. 22/2561, not the classification notification สนส. 23/2561; consider citing 23/2561 directly.
- **`bot2024circular601`**: add the Thai title "ขอความร่วมมือให้ความช่วยเหลือลูกหนี้ที่ได้รับผลกระทบจากสาธารณภัย" (*request for cooperation in assisting debtors affected by disasters*). The current English gloss does not match it.
- **`th2019valuationact`**: `howpublished` names the Council of State English translation, but `url` points to the Thai Gazette text. The translation is at https://www.treasury.go.th/medias/treasury-intranet/1/post/laws_regulations-80/live/77_1768470666_5e20c6f57bb59b7bbf4be4acf5ea18a2.pdf.
- **`caloia2026floods`**: the bib note says "CET1 falls 30-110 bp" (working paper). The published abstract says capital declines "mostly range between 30 and 50 basis points". Align the note; the proposal quotes neither figure.
- **`chongwilaikasaem2022flood`**: the key says 2022 (online first) while the entry says 2023 (print issue 16(6)). This is consistent with Crossref and needs no change.
- **`huizinga2017global`**: doi:10.2760/16510 is not in Crossref (404) but resolves through doi.org to op.europa.eu, as the bib note says.
- **`zanaga2022worldcover`**: this is a DataCite DOI, so Crossref's 404 is expected. DataCite confirms the entry.
- **`bot2012capital` / `bot2017dsib`**: the 7% and 8% totals assume a zero countercyclical buffer. The BOT's current setting was not checked in this round.
- **`bot2026rppislides`**: the bib note's reference to the published table EC_EI_008_S4 (app.bot.or.th) was not re-checked.

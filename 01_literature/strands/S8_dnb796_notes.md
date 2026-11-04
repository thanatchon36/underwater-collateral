# S8: DNB Working Paper 796 — verification and read

**Working note, 2026-11-02.** Task: open and read DNB WP 796 (listed as [UNVERIFIED] in `S6_notes.md`, §(b) and "Unverified / not read"). Then test the proposal §2 sentence on flood stress tests (`06_proposal/proposal.md`, line ~39) against it, and spend a few queries looking for 2024–2026 papers that formally invert a credit-loss or capital model over flood severity. No existing project file was edited.

Labels as in S6: **[E]** established from a source I read, at the depth stated; **[S]** my judgement; **[UNVERIFIED]** not opened or not confirmed. Page numbers are the printed page numbers of the Tinbergen PDF (the paper's p. 1 is PDF p. 3).

---

## 1. Verified bibliographic entries

The search-result title was truncated. The full title is *Floods and financial stability: Scenario-based evidence from below sea level*, and the paper has three authors, not two.

```bibtex
@techreport{caloia2023floods,
  author      = {Caloia, Francesco G. and van Ginkel, Kees C. H. and Jansen, David-Jan},
  title       = {Floods and financial stability: Scenario-based evidence from below sea level},
  institution = {De Nederlandsche Bank},
  type        = {DNB Working Paper},
  number      = {796},
  year        = {2023},
  month       = dec,
  url         = {https://ideas.repec.org/p/dnb/dnbwpp/796.html},
  note        = {verified 2026-11-02 via RePEc/IDEAS (handle RePEc:dnb:dnbwpp:796; number, date 2023/12, title, abstract) and OpenAlex W4390284380. Full text read from the same paper issued as Tinbergen Institute Discussion Paper TI 2023-083/IV (https://papers.tinbergen.nl/23083.pdf; also https://hdl.handle.net/10419/282896), version dated 20 December 2023, whose abstract is word-for-word that of the IDEAS record. The DNB-hosted PDF (https://www.dnb.nl/media/k5npzww1/working_paper_no-796.pdf) returned HTTP 403. Read depth: full}
}

@article{caloia2026floods,
  author  = {Caloia, Francesco G. and van Ginkel, Kees C. H. and Jansen, David-Jan},
  title   = {Floods and financial stability: Scenario-based evidence from below sea level},
  journal = {Journal of Financial Stability},
  volume  = {84},
  pages   = {101545},
  year    = {2026},
  month   = jun,
  doi     = {10.1016/j.jfs.2026.101545},
  url     = {https://doi.org/10.1016/j.jfs.2026.101545},
  note    = {verified 2026-11-02 via Crossref (volume, article number, June 2026, CC BY 4.0) and the VU Amsterdam research portal (abstract, 13 pp.). Read depth: abstract only; the ScienceDirect PDF and Elsevier text endpoints refused scripted access}
}
```

Notes on the metadata:
- Author order: the PDF title page, Crossref and the VU portal give Caloia, van Ginkel, Jansen. IDEAS lists "Caloia; Jansen; van Ginkel"; I follow the paper. [E]
- Affiliations (PDF p. 1): Caloia, DNB and VU Amsterdam; van Ginkel, Deltares; Jansen (corresponding), DNB, VU Amsterdam and Tinbergen Institute. [E]
- First draft July 2022 (PDF p. 1). The paper continues `caloia2021flood` (DNB WP 730) on the same end-2020 loan-level vintage (p. 6, fn. 5). [E]
- The JFS abstract differs slightly from the working paper: "uninsurable flood damages", "suggesting overall effects of flood events may well be larger" and a closing sentence on widening climate protection gaps. It reports the same 38 scenarios and the same 30–50 bp range. [E, abstract] Any change to methods in the published version is [UNVERIFIED].

## 2. Read depth

- **DNB WP 796 / TI DP 2023-083: full.** I read all 18 pages of text, the references, the figure and table notes and the appendix (return periods, damage curves, LIWO comparison, price-level adjustment, inundation depths). The figures are images, so I read only their notes and axis labels. The DNB-branded PDF itself was not opened (403). I treat the TI version as the same text because title, authors, date and abstract match; that equivalence is an inference.
- **JFS 2026 version: abstract only** (VU research portal). The published body was not read.

## 3. What the paper does [E, full read of the working paper]

**Question and setting.** Can floods affect financial stability through credit risk on real-estate loans? The setting is the Netherlands, where insurance excludes damage from breaches of primary flood defences ("type B" floods) (pp. 2, 7, 30).

**Data** (pp. 5–6, Table 1):
- loan-level data for eight major Dutch banks at end-2020: about 3.0 million residential and 176,000 commercial properties securing about EUR 650 bn (EUR 577 bn residential, EUR 71 bn commercial);
- CBS property-registry microdata (floor area, property type, four-digit postcode; the registry also holds the property's tax value);
- COREP/FINREP starting points for risk parameters and capital, with a system CET1 ratio of 16.7% (p. 13).

**Scenarios** (pp. 7–8; appendix pp. 31, 37–38). There are 38 fixed, deterministic scenarios.
- 32 are single-breach floods from the LIWO database (more than 5,000 scenarios). For each dike-ring area the authors pick the scenario with the highest expected damage, with a EUR 500 m cut-off. Return periods mostly lie between 1-in-100 and 1-in-10,000 years. The least likely, scenario 5108 at Scheveningen, is rarer than 1-in-10,000,000 years (Fig. A.1).
- Six extreme multiple-breach scenarios were built by Dutch flood experts in 2007.
- Severity enters as inundation depth: the mean over built-up land in each four-digit postcode, with dry parts counted as zero (p. 8).

**Method chain** (pp. 8–13).
1. Damage = SSM depth–damage factor θ(h) × maximum damage per m² × floor area × a 2011→2020 price factor.
2. φ = min(damage / property value, 1).
3. LTV_S = LTV_0 / (1 − φ).
4. Loss-given-loss uses a sales ratio reduced by φ. LGD = (1 − probability of cure) × LGL + costs.
5. PD comes from a pooled OLS linear probability model of default on current LTV, the interest rate and regional GDP growth. In the scenarios only LTV moves (p. 12).
6. Higher expected loss is booked as provisions against CET1, and risk-weighted assets are recomputed with the Basel IRB formula. The scenario change in CET1 follows Eq. (12).
7. The horizon is one year, and only system-wide results are reported (pp. 10, 13).

**Results** (pp. 14–15, Figs. 4–7).
- In 35 of the 38 scenarios (property damage of EUR 0.5–3 bn), CET1 falls by 30–50 bp.
- Two multiple-breach scenarios (about EUR 6 bn of damage) cut CET1 by about 75 bp. The most extreme, which floods most of the western Netherlands, cuts it by about 110 bp.
- Depletion is non-linear in damage and is fitted with a degree-2 fractional polynomial (Fig. 4).
- Most of the depletion comes from higher RWA, not expected loss. Starting-point LTV is the main financial driver.

**Does it solve for a breaking point?** **No.** [E]
- It describes itself as "scenario analysis" with "a range of increasingly severe flood scenarios" (pp. 3, 5). The term "reverse stress test" does not appear in the working paper (text search for "reverse": no hits).
- No CET1 threshold is defined or solved for. The Basel 8% figure appears only inside the RWA formula (p. 13), and the paper concludes that the depletions "seem manageable" (pp. 16–17).
- The closest object is Fig. 4's damage–depletion curve across scenarios. Severity is indexed by EUR damage, not by return period or depth, and the curve is never inverted.

**Do collateral valuation or a valuation gap enter?** **Only as physical damage.** [E]
- Collateral value falls by repair cost alone (φ). The paper does not model a market or hazard discount, a gap between appraisal and market value, or valuation lags.
- Post-flood revaluation of properties in flood zones is named explicitly as future research (p. 18).
- Collateral values are the observed loan-level values ("protection value", Table 1). The CBS tax value is mentioned as a registry field but not used as a valuation (p. 6).
- [S] In the proposal's terms this is close to a single point of the λ_B frontier: banks recognise damage in full and the ex-ante hazard discount not at all.

**Do forbearance or relief enter?** **No.** [E]
- No moratoria, forbearance or delayed staging appear. IFRS 9 staging is not modelled; losses go straight to provisions within one year.
- "Probability of cure" (loans that cure after restructuring) is a fixed LGD parameter, not a policy lever (p. 11).
- Government compensation is discussed as possible but discretionary and slow, and is excluded (p. 7). Macro feedback and repeated floods are left to future work (pp. 16–18).

## 4. Verdict on the proposal sentence

> "Flood stress tests estimate banks' losses [@caloia2021flood], the disaster that would fail a small bank [@blickle2025bad] or the probability of the 2011 scenario for one Thai bank [@chitchumnong2025physical]; none treats the valuation gap or relief as a dimension of the breaking point."

**Verdict: the sentence holds against WP 796. It needs a small amendment, not a narrowing of the claim.**
- WP 796 does not run a reverse stress test, does not solve for a breaching severity, and does not treat a valuation gap or relief. The "none treats…" clause survives for this paper. [E for the working paper; published JFS body [UNVERIFIED]]
- The amendment is about citation. WP 796, now published in the *Journal of Financial Stability* (2026), is the definitive and most recent version of the DNB flood stress test. The proposal cites only the 2021 WP 730, so an examiner who knows the JFS paper may read the citation as out of date. [S]
- WP 796 also reports CET1 depletion across 38 scenarios that rise in severity and come with return periods. The sentence should therefore describe it as mapping capital depletion across fixed scenarios, so that it does not appear to overlook an existing severity–capital curve. [S]

**Suggested wording (British English):**

> "Flood stress tests estimate banks' capital depletion under fixed sets of flood scenarios [@caloia2021flood; @caloia2026floods], the disaster that would fail a small bank [@blickle2025bad] or the probability of the 2011 scenario for one Thai bank [@chitchumnong2025physical]; none solves for the breaching flood severity with the valuation gap or relief as a dimension of the breaking point."

If space is tight, keep the original sentence and only add `@caloia2026floods` beside `@caloia2021flood`.

**Optional sentence for §3 or the RQ3 design** [S]: "@caloia2026floods let collateral fall only by physical damage and leave post-flood revaluation to future work, which corresponds to a single point of the λ_B frontier."

**Caveat.** I read the published JFS version at abstract depth only. Its abstract does not mention a reverse test, valuation gaps or relief. Before submission, open the CC BY version at doi:10.1016/j.jfs.2026.101545 in a browser and search for "reverse", "threshold" and "forbear".

## 5. Other close 2024–2026 papers (time-boxed search)

**Queries.**
- OpenAlex (from 2024-01-01): "reverse stress test flood"; "reverse stress test physical climate risk bank"; "reverse stress test natural disaster bank capital"; "flood return period bank capital threshold credit risk"; "breaking point flood bank capital".
- Crossref (from 2024-01-01): "reverse stress test flood bank"; "reverse stress testing climate physical risk hurricane mortgage"; "flood severity capital shortfall banks inundation depth scenario".

**Result.** None of the eight queries returned a paper that inverts a credit-loss or capital model over flood return period, depth or extent to find the capital-breaching severity. The absence claim in S6 §(b) still stands, with the usual limit of a metadata-only search. [E for the search; [S] that absence of hits means absence]

Closest items:
- **Gerst, Rossi, Brammer, Canty, Dolan, Lempert & Rovenskaya (2026)**, "Using iterative reverse scenario logic to manage model risk in financial climate risk assessment", *Climatic Change*, doi 10.1007/s10584-026-04260-y.
  - Status: OpenAlex metadata and abstract read (abstract depth).
  - Content: a conceptual paper. It notes that industry reverse stress testing searches for scenarios that produce a pre-defined adverse outcome such as insolvency. It argues that existing methods do not handle the model risk of chaining climate models, and proposes "iterative reverse scenario logic".
  - Relevance: the abstract mentions no flood-specific empirical inversion and no bank data. Useful as a methods and positioning citation for RQ3: it supports the case that reverse testing on climate hazards is recognised but under-developed. An open PDF is listed at IIASA (pure.iiasa.ac.at/id/eprint/21782); not opened.
- **Rania (2026)**, "Spatial Stress Testing and Climate Value-at-Risk: A Quantitative Framework for ICAAP and Pillar 2", *Journal of Risk and Financial Management* 19(1):48, doi 10.3390/jrfm19010048.
  - Status: abstract read.
  - Content: a spatial jump-diffusion VaR/ES framework conditional on climate scenarios. It is forward, not a reverse test, with no flood-specific inversion.
  - Relevance: low.
- **Budnik, Aikman & Angotti (2024)**, "Stress Testing with Multiple Scenarios: A Tale on Tails and Reverse Stress Scenarios", SSRN doi 10.2139/ssrn.4806898.
  - Status: metadata only; no abstract in OpenAlex. An econstor PDF is listed (hdl 10419/299584); not opened. Content [UNVERIFIED].
  - Relevance: from the title, a macro reverse-scenario method, not a physical-hazard one. A possible methods citation alongside @grundke2018macroeconomic.
- **Degryse, Ongena, Scopelliti & Van Gerwen (2026)**, "Flooded Collateral: Commercial Real Estate Valuation and Bank Lending", SSRN doi 10.2139/ssrn.7409938.
  - Status: metadata only; no abstract in OpenAlex. [UNVERIFIED]
  - Relevance: not a reverse test, but relevant to RQ1 (collateral valuation after floods). S6 said no open full text was found; an SSRN record now exists and is worth checking manually, as SSRN refuses scripted access.

Not followed up (titles only, off-target): "Reverse Stress Testing Geopolitical Risk in Corporate Credit Portfolios" (arXiv 2601.03983 / SSRN 6029316); "Reverse Stress Testing for Supply Chain Resilience" (arXiv 2511.07289); "Climate stress testing for mortgage default probability" (*IRFA* 2024, doi 10.1016/j.irfa.2024.103497; title suggests a forward test, [UNVERIFIED]).

## Housekeeping (not done; for the author)

- Add `caloia2026floods`, and optionally `caloia2023floods`, to `references.bib`.
- Move DNB WP 796 out of the "Unverified / not read" list in `S6_notes.md`. The title there is truncated ("from below" should read "from below sea level").
- I did not edit either file.

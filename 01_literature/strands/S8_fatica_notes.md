# S8 — "Fatica et al. (2024a)": identification and reading notes

Date: 2026-11-02. Tags: [E] read in the source at the stated locator; [S] my synthesis or inference; [UNVERIFIED] not opened.

## 1. Identification: "Fatica et al. (2024a)" is Barbaglia, Fatica & Rho (2024)

The S6 brief treated this as a separate paper from `barbaglia2024flooded`. It is the same paper.

- [E] Albertazzi, Djekic & Ponte Marques (2026), ECB WP 3224 (PDF from the bib url). The passage is on **printed p. 8 (PDF p. 9)**; S6_notes "p. 9" is the PDF page. The reference list (printed pp. 42–43) has only two entries involving Fatica in 2024:
  - "Barbaglia, L., Fatica, S., and Rho, C. (2024). Flooded credit markets: Physical climate risk and small business lending. Working paper. Securitised SME loans, three European countries, 2008–2019." (printed p. 42)
  - "Fatica, S., Katay, G., and Rancan, M. (2024). Floods and firms: Vulnerabilities and resilience to natural disasters in Europe. SSRN 4796097." (printed p. 43)
- [E] The PDF's internal hyperlinks settle it. On PDF p. 9, the "Fatica et al. (2024a)" link points to destination `cite.FaticaBarbagliaRho2024`, which is the Barbaglia–Fatica–Rho entry. "Fatica et al. (2024b)" points to `cite.fatica2024floods`, the Fatica–Katay–Rancan entry.
- [E] Crossref lists an SSRN posting, doi 10.2139/ssrn.4890572 (2024), with the author order **Fatica, Barbaglia, Rho**. [S] This probably explains the in-text label: the cite key or metadata came from that posting, while the printed reference uses the working-paper order. The label is a citation slip in Albertazzi et al. There is no missing third paper.
- So nothing new needs to go into `references.bib`. The existing key `barbaglia2024flooded` is the right citation; only its read depth changes (Section 2).

## 2. Verified BibTeX (replaces the note of the existing entry; same key)

```bibtex
@techreport{barbaglia2024flooded,
  author      = {Barbaglia, Luca and Fatica, Serena and Rho, Caterina},
  title       = {Flooded credit markets: physical climate risk and small business lending},
  institution = {Money and Finance Research Group (Mo.Fi.R.), Univ. Politecnica Marche},
  type        = {Mo.Fi.R. Working Papers},
  number      = {186},
  year        = {2024},
  month       = jul,
  url         = {http://docs.dises.univpm.it/web/quaderni/pdfmofir/Mofir186.pdf},
  note        = {verified 2026-11-02 via RePEc/IDEAS (ideas.repec.org/p/anc/wmofir/186.html) and the Mo.Fi.R. PDF (revised June 2024, 61 pp.); cited as "Fatica et al. (2024a)" in albertazzi2026physical; SSRN posting doi 10.2139/ssrn.4890572 (Crossref metadata only); earlier version JRC Working Papers in Economics and Finance 2023-14; read depth: full main text (Sections 1, 2, 3.4, 4, 5, 6) and Appendices A.1.3, A.2, B, C; Sections 3.2--3.3 (pricing baseline and mechanisms) and Appendices A.1.1--A.1.2 not read}
}
```

**Read depth.** Full read of the abstract, introduction, data (Section 2), realised risk and pricing (Section 3.4, Table 6), loan performance (Section 4, Table 7), the back-of-envelope pricing check (Section 5), the conclusion, and Appendices A.1.3, A.2, B (arrears) and C (LGD). **Not read:** Sections 3.2–3.3 (baseline pricing and mechanisms, Tables 3–5) and Appendices A.1.1–A.1.2. Page numbers below are the printed numbers; the PDF page is one higher.

- [UNVERIFIED] Two later SSRN versions exist, doi 10.2139/ssrn.5216527 and 10.2139/ssrn.5347522 (both 2025, per Crossref and OpenAlex). SSRN returned 403, so I could not check whether Table 7 changed. No journal version was found in Crossref or OpenAlex.

## 3. Extracted findings

**Data.** [E]
- Loan-level data on securitised SME loans from the European DataWarehouse (ECB loan-level initiative), reported quarterly (pp. 7–9).
- Three countries: **Belgium, Italy, Spain** (p. 8).
- Loans originated **2008–2019** (p. 9; App. A.1.3, p. 51); the pricing sample is about 1.05 million term loans (p. 14; Table 2, p. 17).
- The default model uses 6,328,791 loan-period observations (Table 7, p. 33).
- Borrower location is known only at **NUTS3 (province or district)** (p. 8).

**Flood measures.** [E] Both are at county (NUTS3) level, not at the asset.
- Prospective risk: the JRC Risk Data Hub flood-risk indicator for industrial and commercial buildings. It combines exposure (LISFLOOD return periods of 10–500 years) with vulnerability, is normalised to 0–10 within each country, and "High risk" means above the median (pp. 9–11).
- Realised floods: the RDH historical events module (river, flash and coastal floods, 2007–2018). The treatment is a dummy equal to 1 if the borrower's county had **at least one flood in the previous q months**, with q = 6, 12 or 24 (pp. 12–13).

**Identification.** [E]
- A Cox proportional hazard model of time to default (pp. 29–31), with:
  - loan controls: interest rate, balance, residual term, share collateralised;
  - lender, industry, business-type and NUTS2 region fixed effects;
  - county GDP and employment growth.
- **Default** means more than 90 consecutive days in arrears. Loans are dropped after first default, with no cure (p. 32).
- [S] This is not a flooded-versus-matched-control or event-study design. Each q is a separate regression. The windows are **nested** (0–6, 0–12 and 0–24 months), not disjoint bins. Table 7 does not say whether standard errors are clustered; Tables 6 and C.1 cluster by county. With a county-level treatment, unclustered errors would overstate precision.
- [E] There are no data on relief: "we do not have data on post-flooding emergency measures for the events in our sample" (p. 34).

**PD dynamics: hazard ratios, Table 7, p. 33.** [E]

| Flood window before observation | Hazard ratio (SE) | Note |
|---|---|---|
| ≥1 flood in previous 6 months | **0.931*** (0.024)** | "protective effect" (p. 32) |
| ≥1 flood in previous 12 months | **1.198*** (0.023)** | "hazard 20% greater" (p. 34) |
| ≥1 flood in previous 24 months | **1.607*** (0.027)** | "hazard ratio reaches 1.6" (p. 34) |

- [E] Results are almost unchanged when a dummy for loans originated after a flood is added: 0.931, 1.196 and 1.602 (columns 4–6).
- [E] Loans *originated* within 6, 12 or 24 months after a flood carry hazard ratios of 1.17, 1.23 and 1.04 (pp. 35–36). The authors read this as risk-taking in recovery lending.
- [E] Prospective "High risk" has no effect on default (hazard ratio about 1.00).

**Arrears diverge from default.** [E] Table B.1, p. 57. The hazard of *any* arrears rises already in the first six months, with hazard ratios of 1.13, 1.06 and 1.15 for the 6-, 12- and 24-month windows (also p. 35).
- [S] So in the first six months, late payments rise while progression to 90-day default falls. That is the signature one would expect if relief stops arrears reaching the default threshold. The authors do not draw this link.

**Attribution of the early fall.** [E] pp. 32–34.
- The authors call it "counterintuitive". They offer as a *possible explanation* "emergency financial aid and relief measures". For Italy they list "direct transfer and subsidies, tax holidays and suspension of debt payments".
- Footnote 25 cites bank moratoria after the Marche floods: Intesa Sanpaolo's 12-month repayment moratorium and UniCredit's one-year suspension of principal repayments. The footnote says "September 2023" but its Reuters link is dated 2022, and the event lies outside the sample in any case.
- They also cite US evidence that SBA and recovery loans reduce delinquency (p. 34), and firms' cash holdings (p. 35).
- The explanation is a conjecture, explicitly untested. Insurance is not offered as an explanation; it appears only as future research (p. 41).

**Collateral and LGD.** [E] Section 5, p. 37; App. C, pp. 58–60, Table C.1.
- The outcome is LGD *as reported by banks* in EDW, not realised recoveries. The sample mean is 22.5% of balance.
- Recent floods do not change reported LGD: coefficients range from −0.12 to 0.00 percentage points, all insignificant. A flood before origination does not change it either (0.23–0.32, insignificant).
- "High risk" adds about 0.23 percentage points, significant at 10%.
- A higher collateralised share slightly *raises* the default hazard (1.010 per unit, Table 7) and reported LGD (+0.058).
- [S] Banks' loss estimates do not update after floods even as defaults rise. That bears on λ_B, though only at county resolution and for SME securitisations.

**Internal inconsistencies to note if cited in detail.** [E]
- p. 37 says LGD is "not significantly affected" by projected risk; p. 59 says it is significant at 10%.
- p. 59 attributes the 0.23 percentage-point effect to "recent occurrence of flooding", but it is the High-risk coefficient.
- The Table C.1 caption says "hazard ratios from a Cox model" for what is a linear LGD regression.
- p. 38 cites "column (5)" for the hazard ratio of 1.04, which is column (6).
- Footnote 28 mentions both 1.21 and 1.23.

None of these affects Table 7.

## 4. Is Albertazzi et al.'s characterisation accurate?

Mostly accurate, but with four problems. [E] Albertazzi et al. printed p. 8, checked against the paper.
1. **Wrong label.** The paper is Barbaglia, Fatica & Rho (2024), not a separate "Fatica et al. (2024a)".
2. **"Likely owing to subsidies" is too narrow.** The authors' conjecture covers emergency aid in general, explicitly including **suspension of debt payments and bank moratoria**. That is the channel RQ2 tests. It is also only a conjecture, with no relief data.
3. **"Increase after 12 to 24 months" over-reads the timing.** The windows are cumulative (floods within the last 12 or 24 months). They are not disjoint 12–24-month bins, so the paper does not isolate when the rise occurs. [S] Hazard ratios of 0.93 for 0–6 months and 1.20 for 0–12 months suggest that the excess lies beyond six months. That is an inference, not an estimate.
4. **PD versus hazard.** The paper estimates hazard ratios of 90-day default, not PD levels. "Decline in PD" is a loose but acceptable paraphrase.

The data description is correct: securitised SME loans, 2008–2019, three countries, NUTS3 floods. So is the pricing summary: a 6.4 bp premium, no effect of recent floods except severe ones, and a +13.4 bp interaction (Table 6, pp. 27–29).

## 5. Implications for the proposal [S]

- This is the closest published evidence of a relief-shaped default path, but it is indirect. Relief is unobserved, floods are measured at county level, and the timing is cumulative. RQ2's contribution survives and becomes sharper: RQ2 *observes* relief (flags, eligibility dates), measures flooding at the collateral sheet and tracks months relative to relief ending. Each is something this paper could not do.
- The divergence between early arrears and default (Table B.1 against Table 7) suggests a cheap check in RQ2: compare 30-day arrears with 90-day delinquency during relief.
- Update S6_notes: the two [UNVERIFIED] Fatica (2024a) bullets (around lines 59 and 162) can be resolved to `barbaglia2024flooded` (S6_notes not edited here).

## 6. Suggested sentences (British English, each under 35 words; cite the existing key)

For §2 or §4.2:

> For European securitised SME loans, default hazards dip within six months of a flood but rise over longer windows; the authors conjecture, without relief data, that emergency aid and payment suspensions explain the dip [@barbaglia2024flooded, Table 7].

(33 words excluding the citation.)

Shorter alternative for §4.2, positioning RQ2:

> European SME evidence suggests relief may delay recorded default, but relief was unobserved [@barbaglia2024flooded, pp. 32–34]; RQ2 observes it directly.

(17 words excluding the citation.)

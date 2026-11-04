# Progress

**Current phase:** research proposal, RQ1 pre-analysis plan and working paper drafted; the RQ1 plan awaits registration. Topic: Underwater Collateral; RQ1 + RQ3 core, RQ2 conditional on loan-level access.
**Last updated:** 2026-11-04.

## Done

- Literature: five strands plus top-ups merged into `01_literature/references.bib` and `lit_matrix.csv`; `literature_review.md`; `gap_statement.md`.
- Policy context: `02_policy_context/` (timeline of relief and valuation rules from public documents).
- Data: Treasury appraisal snapshot (77/77 files, SHA-256 in `manifest.csv`), Sentinel-1 flood maps 2021–26, Sentinel-2 validation, Copernicus DEM, WorldCover, JRC water, UNOSAT, OCHA boundaries, BOT credit and price series; all logged in `03_data/README.md`.
- Pilot: `04_analysis/pilot_report.md`; `run_all.py` rebuilds every table and figure from raw.
- Design: `05_design/` (framework, identification, data-access plan, ethics, RQ1 pre-analysis plan, OSF form, registration checklist).
- Proposal: `06_proposal/proposal.md` (rendered copy with references in `proposal_rendered.md`), one-pager, claims ledger, author notes.
- Working paper: `paper/paper.pdf`, built by `paper/build.sh`; every number is a macro written by `04_analysis/src/paper_numbers.py`. Revised after a referee-style review (`07_review/referee_report_paper_round1.md`; changes in `07_review/revision_log.md`).
- Web version of the paper: https://thanatchon36.github.io/underwater-collateral/paper/ (built by `paper/web.py` from the same LaTeX sources, served from `docs/` by GitHub Pages).
- Monte Carlo of the registered RQ1 estimator: the wild cluster bootstrap holds its size; the placebo-footprint test over-rejects (0.195), restricting the placebo pool does not repair it, studentising does (0.055). Amendment proposed in PAP §6 and paper Section 6.5.
- Repository public (2026-11-04); Zenodo concept DOI 10.5281/zenodo.23949061 (latest release v0.2.0, 10.5281/zenodo.23953576); processed data on Hugging Face (`thanatchon36/underwater-collateral-data`, tier 1).

## Decisions only the author can take

1. Register the RQ1 pre-analysis plan on OSF before the next valuation round is published (`05_design/registration_checklist.md`).
2. Confirm the proposed amendment: wild cluster bootstrap primary, placebo check studentised.
3. Whether the 2021–23 radar reference becomes the primary treatment definition.
4. The Phayao overlap rule (keep with the height slope, trim to common support, or move to sensitivities).
5. Whether to obtain a pre-2011 land-cover product for the cross-section (new data source).
6. Hugging Face tiers 2 and 3 (open-licence raw files; Treasury files after confirming data.go.th terms).
7. Zenodo v0.1.0 (10.5281/zenodo.23949062): update its creator metadata on zenodo.org to match the latest release.

## Next steps

- **Treasury round timing.** Several provincial committees considered a one-year extension of the 2566–2569 schedules on 2–3 November 2026 (`04_analysis/treasury_2027_round_status.md`). Check the Royal Gazette in a browser and ask the Chiang Rai, Phayao, Nong Khai and Nakhon Phanom offices whether their deed schedules are being extended.
- **Data requests** (`05_design/data_requests_draft.md`, sent by the author): 2024 emergency-zone declarations from the provincial DDPM offices; survey periods and earlier rounds from the provincial Treasury offices.
- **Proposal placeholders:** the named external adviser and the Preparation paragraph (author's own facts only).
- Open the Caloia and Jansen DNB PDF by hand (https://www.dnb.nl/media/st5psfvb/working_paper_no-_730.pdf; 403 for automated access).
- National Credit Bureau research-access terms: not found publicly; the author to ask NCB and PIER.

## Open research items

- Earlier Treasury rounds (pre-2023) to calibrate the SD and ICC of value changes and test pre-trends.
- DDPM district declaration lists for the administrative-spillover sensitivity (coded; waits for the lists).
- 2012 provincial credit series (FI_CB_011_S3) not located.
- A public probabilistic flood event set for RQ3.
- Public 2011 flood-management records: JICA (2013) dike-break sections found, not yet digitised.
- Credit Information Business Act 2545 disclosure sections not read ([UNVERIFIED]).
- FABDEM licence: re-check the live data.bris page before any download.

## Items needing approval before use (CP3)

- GEE or Copernicus Data Space accounts; a GISTDA API key; Department of Lands parcel polygons; an OpenAlex key.

## Task list

- [x] Setup
- [x] Topic chosen
- [x] Literature review and gap statement
- [x] Policy timeline
- [x] Research design
- [x] Pilot analysis
- [x] Proposal draft and supporting documents
- [x] Review rounds, revisions, citation audits
- [x] Working paper and its revision
- [ ] RQ1 pre-analysis plan registered (author)

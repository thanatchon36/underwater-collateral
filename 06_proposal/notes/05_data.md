# Author notes: §5 Data and feasibility

> **Phase 7 revision (2026-11-02).** The section was revised after referee rounds 1 and 2 and the citation audit. `07_review/revision_log.md` records each change and its reason. The reasoning below is the Phase 6 draft and may describe designs since replaced, such as the triple difference and the old hypothesis labels.


Working draft, 2026-11-02 (Phase 6).

## Reasoning

- **Pilot numbers.** Every number comes from a script output: `04_analysis/outputs/tables/`, rebuilt by `run_all.py`.
- **Figure 1.** It is shown to prove feasibility, not as a result; the caption says "descriptive only".
- **Research governance.** The text uses four elements: data, sources, pre-specification and disclosure. They mirror `05_design/ethics.md`.

## Weak points

- **2012 credit data.** The 2012 provincial credit series (FI_CB_011_S3) was not located. Later years are in hand: S4 to June 2025 and its successor S5 to July 2026, so RQ3 uses December 2025 shares.
- **GFD footprint.** The Global Flood Database footprint excludes the south and parts of the west and north (pilot report §9).
- **Timing assumption.** The 6–18-month timeline for data agreements is a planning assumption, not a verified figure.

## Round 3 (2026-11-02)

- 2024 treated sheets: 713 urban (1:1,000), 426 rural (1:4,000), 69 at 1:2,000, 6 at 1:500 (`flood2024_treated_sheets.csv`, threshold 0.25).
- Pilot slopes use within-cell flood share; Figure 1 bins raw shares, so the slopes and the binned means need not match. Say this when presenting the figure.
- Figure 1 no longer carries an in-image source footer; the caption holds sources and definitions.

## Round 4 (2026-11-02)

- Pilot now reports within-cell bin effects on parcel log value (`appraisal_flood_binned.csv`, outcome `mean_logp`), which is what Figure 1 plots. The linear slopes stay in `appraisal_flood_within.csv` but are no longer quoted.
- The rural "+0.2 on partly flooded sheets" pattern of earlier drafts came from raw-share bins; within cells it is not there. Be ready to explain the change.
- 2024 control set and indicative MDE: `rq1_2024_controls_power.csv`. The MDE is computed on levels, so it overstates noise; the true change-based MDE is unknown until 2027–30 values are out.

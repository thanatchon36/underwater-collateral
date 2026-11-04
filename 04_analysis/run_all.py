"""Rebuild every processed dataset, figure and table of the pilot from raw data.

Raw data must already be on disk (03_data/raw/, immutable). Fetch it with the download
scripts in 04_analysis/src/ (download_*.py) and the URLs logged in 03_data/README.md.
flood_s1_grd.py reads Sentinel-1 scenes over the network (about 25 minutes) and is run once,
like a download script, before this file. validate_s1_s2.py (Sentinel-2 check of the radar
rule, about 15 minutes over the network) is run once after it, since it reads the RQ1 sample.

Run: .venv/bin/python -I 04_analysis/run_all.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "04_analysis/src"
STEPS = [
    "check_mapsheet_coverage.py",      # decode coverage table
    "build_sheet_panel.py",            # appraisals x 2011 flood x GSW, by sheet
    "exposure_2024_north.py",          # 2024 Chiang Rai / Phayao exposure
    "build_north_covariates.py",       # 2024 design: terrain, water and land cover by sheet
    "rq1_2024_design_power.py",        # 2024 design: controls, balance and MDE
    "rq1_2024_pooled.py",              # pooled 2024 sample from Sentinel-1: size, MDE, UNOSAT check
    "rq1_sample_sensitivity.py",       # province threshold 20/25/30; 2025 floods as second event
    "build_sheet_admin.py",            # district and tambon of each 2024 radar sheet (COD-AB), for the DDPM drop
    "rq1_sensitivity_samples.py",      # rebuilt samples for the RQ1 sensitivities (primary reproduced exactly)
    "rq1_round_change.py",             # pre-registered RQ1 code, checked on a synthetic first post-flood round
    "rq1_round_change.py --sensitivities",  # every RQ1 sensitivity run once on a synthetic R1
    "rq1_lee_bounds.py",               # RQ1 secondary: moved-unit change with Lee bounds (synthetic R1)
    "hash_registration_inputs.py",     # SHA-256 of the registered RQ1 sample files
    "build_sheet_landcover.py",        # WorldCover 2021 land-cover shares by sheet
    "fig_appraisal_flood.py",          # RQ1 motivating figures and tables
    "panel_summary.py",                # coverage and data-quality tables
    "clean_bot_provincial_credit.py",  # BOT provincial credit panel
    "fig_provincial_credit_2011.py",   # provincial credit around 2011
    "credit_share_drift.py",           # provincial credit mix drift and RQ3 allocation shares (Dec 2025)
    "rppi_flood_windows.py",           # BOT appraisal-based regional price index around floods (descriptive)
    "synth_tier2.py",                  # synthetic Tier 2 panel (seeded)
    "rq2_event_study.py",              # RQ2 estimator on synthetic data
    "rq3_reverse_stress.py",           # RQ3 inversion on synthetic data
    "rq3_lambda_sensitivity.py",       # RQ3 back-of-envelope: does lambda_B move S*? (illustrative)
    "rq2_power.py",                    # RQ2 power, 2024-25 and 2011 designs (assumptions only)
    "fig_chain.py",                    # schematic of the hazard-to-capital chain (no data)
    "paper_numbers.py",                # paper: numbers.tex, tables, figures and refs.bib for paper/
]


def main() -> None:
    for step in STEPS:
        print(f"== {step}", flush=True)
        script, *args = step.split()
        subprocess.run([sys.executable, "-I", str(SRC / script), *args], cwd=ROOT, check=True)
    print("== tests", flush=True)
    subprocess.run([sys.executable, "-I", "-m", "pytest", "-q", str(SRC)], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()

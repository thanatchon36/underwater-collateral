"""Tests for credit_share_drift.py: allocation month and share arithmetic."""

import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from credit_share_drift import allocation_month, shares  # noqa: E402


def panel(rows):
    return pd.DataFrame(rows, columns=["date", "province_en", "level", "loans_mthb", "flags"])


def test_allocation_month_skips_preliminary_december():
    d = panel([
        ("2023-12-01", "A", "province", 1.0, ""),
        ("2024-12-01", "A", "province", 1.0, "preliminary"),
        ("2025-06-01", "A", "province", 1.0, ""),  # not a December
    ])
    assert allocation_month(d) == "2023-12-01"


def test_allocation_month_takes_latest_final_december():
    d = panel([
        ("2023-12-01", "A", "province", 1.0, ""),
        ("2025-12-01", "A", "province", 1.0, "revised;hp_to_head_office_2015"),
    ])
    assert allocation_month(d) == "2025-12-01"


def test_shares_sum_to_one_and_merge_nong_khai():
    d = panel([
        ("2025-12-01", "A", "province", 3.0, ""),
        ("2025-12-01", "Nong Khai", "province", 1.0, ""),
        ("2025-12-01", "Bueng Kan", "province", 1.0, ""),
        ("2025-12-01", "Nong Khai + Bueng Kan", "harmonised", 2.0, ""),
        ("2025-12-01", "Bangkok", "bkk_total", 5.0, ""),
    ])
    out = shares(d, "2025-12-01", with_bkk=False)
    assert set(out.index) == {"A", "Nong Khai + Bueng Kan"}
    assert abs(out.sum() - 1) < 1e-12 and abs(out["A"] - 0.6) < 1e-12
    assert abs(shares(d, "2025-12-01", with_bkk=True)["Bangkok"] - 0.5) < 1e-12

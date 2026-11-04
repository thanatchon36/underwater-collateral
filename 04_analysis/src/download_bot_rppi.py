"""Download a dated snapshot of the BOT residential property price index (RPPI) tables.

Tables (public BOT statistics server, no login, no API key; checked 2026-11-02):
  EC_EI_008_S4  reportID=993  ดัชนีราคาที่อยู่อาศัย (residential property price index),
                Jan 2011 - Sep 2026, 2011 = 100. All-types, detached, townhouse and condo
                indices for the whole kingdom, Bangkok and vicinity, Central (excl.
                Bangkok and vicinity), North, Northeast and South (not every type in
                every region). Revised series published from January 2025 data.
  EC_EI_008_S3  reportID=920  ดัชนีราคาที่อยู่อาศัยและดัชนีราคาที่ดิน (old series incl. the
                Bangkok-and-vicinity land price index), Jan 2011 - Dec 2024, frozen at its
                28 Feb 2025 update.
Method (table footnote 1/; bib `bot2025rppi`, `bot2026rppislides`): hedonic regression,
rolling window with time dummies, 3-month moving average, from the mortgage-collateral
database of commercial banks and GHB (all SFIs from January 2023). The price is the
lender's appraisal price, not a transaction price.

How: the ASP.NET ReportPage is posted once with the full monthly range selected, then
the public CSV button (imbExportText) exports it. Responses are saved byte-for-byte;
existing files are never overwritten. >= 6 s between requests; no email or credentials sent.

Usage: .venv/bin/python -I 04_analysis/src/download_bot_rppi.py
"""

import csv
import datetime as dt
import hashlib
import html
import re
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT = "2026-11-02"
OUT = ROOT / "03_data" / "raw" / "bot_rppi" / f"snapshot_{SNAPSHOT}"
UA = "Mozilla/5.0 (academic research; no-contact)"
DELAY_S = 6
PAGE = "https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?reportID={rid}&language=th"
# table -> (reportID, first month, last month)
TABLES = {"EC_EI_008_S4": (993, "2011-01", "2026-09"), "EC_EI_008_S3": (920, "2011-01", "2024-12")}


def form_state(page_html: str) -> dict:
    pairs = re.findall(r'<input type="hidden" name="([^"]+)" id="[^"]*" value="([^"]*)"', page_html)
    return {k: html.unescape(v) for k, v in pairs}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    s = requests.Session()
    s.headers["User-Agent"] = UA
    rows = []
    for tid, (rid, d0, d1) in TABLES.items():
        dest = OUT / f"{tid}_monthly_{d0}_{d1}.csv"
        url = PAGE.format(rid=rid)
        if not dest.exists():
            r = s.get(url, timeout=120)
            r.raise_for_status()
            state = form_state(r.text)
            time.sleep(DELAY_S)
            (y0, m0), (y1, m1) = (d0.split("-"), d1.split("-"))
            sel = {"drpPeriod": "MTH", "drpFromYear": f"{y0}xxxx", "drpFromMonth": f"xxxx{m0}xx",
                   "drpToYear": f"{y1}xxxx", "drpToMonth": f"xxxx{m1}xx"}
            r = s.post(url, data={**state, **sel, "btnSubmit": "Submit"}, timeout=180)
            r.raise_for_status()
            state = form_state(r.text)
            time.sleep(DELAY_S)
            r = s.post(url, data={**state, **sel, "imbExportText.x": "10", "imbExportText.y": "10"}, timeout=180)
            r.raise_for_status()
            time.sleep(DELAY_S)
            if "csv" not in r.headers.get("content-type", "").lower():
                raise SystemExit(f"{tid}: not a CSV ({r.headers.get('content-type')})")
            dest.write_bytes(r.content)
        rows.append({"url": url, "method": "POST form: monthly range, then CSV export button",
                     "file": dest.name, "bytes": dest.stat().st_size,
                     "sha256": hashlib.sha256(dest.read_bytes()).hexdigest(),
                     "accessed": dt.date.today().isoformat()})
        print(f"{dest.name} {dest.stat().st_size:,} B")
    with (OUT / "manifest.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()

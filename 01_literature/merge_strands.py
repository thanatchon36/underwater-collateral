"""Merge strand outputs into 01_literature/references.bib and lit_matrix.csv.

Inputs: 01_literature/strands/S*.bib (including S0_scoping.bib, the scoping-stage references) and S*_matrix.csv.
Dedupes by DOI, then by normalised title; the first occurrence keeps its citekey and
duplicates are reported as aliases so notes using either key can be reconciled.
A later strand that reuses an existing citekey (a top-up) replaces that entry.
Matrix rows for duplicates are merged: deeper read depth and higher relevance win.

Usage: .venv/bin/python 01_literature/merge_strands.py
"""

import csv
import re
from pathlib import Path

LIT = Path(__file__).resolve().parent
ROOT = LIT.parent
STRANDS = sorted((LIT / "strands").glob("S*.bib"))
SOURCES = STRANDS
DEPTH = {"abstract": 1, "intro": 2, "full": 3}
COLS = ["citekey", "authors", "year", "title", "venue", "url_or_doi", "verified", "read_depth",
        "question", "data", "identification", "main_finding", "relevance_1to5", "how_my_project_differs"]


def entries(text: str):
    """Yield (citekey, raw_entry) for each @type{key, ...} block."""
    for block in re.split(r"\n(?=@)", text):
        m = re.match(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", block.strip())
        if m and m.group(1).lower() not in {"comment", "string", "preamble"}:
            yield m.group(2), block.strip()


def field(entry: str, name: str) -> str:
    m = re.search(rf"\b{name}\s*=\s*[{{\"](.+?)[}}\"]\s*,?\s*\n", entry, re.I | re.S)
    return m.group(1) if m else ""


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]", "", t.lower())[:80]


def fingerprints(entry: str):
    doi = field(entry, "doi").lower().strip()
    url = field(entry, "url").lower()
    m = re.search(r"doi\.org/(.+)$", url)
    doi = doi or (m.group(1).strip() if m else "")
    return [f"doi:{doi}"] if doi else []


def depth(d: str) -> int:
    return max((v for k, v in DEPTH.items() if k in (d or "").lower()), default=0)


def main() -> None:
    kept, alias, seen, origin = {}, {}, {}, {}
    for src in SOURCES:
        for key, ent in entries(src.read_text(encoding="utf-8")):
            fps = fingerprints(ent) + [f"t:{norm_title(field(ent, 'title'))}"]
            hit = next((seen[f] for f in fps if f in seen), None) or (key if key in kept else None)
            if hit == key and src in STRANDS:
                # Same citekey re-entered by a later strand (a top-up): the later entry wins.
                kept[key] = ent
                origin[key] = src.stem
                for f in fps:
                    seen.setdefault(f, key)
                continue
            if hit:
                if key != hit:
                    alias[key] = hit
                continue
            kept[key] = ent
            origin[key] = src.stem
            for f in fps:
                seen[f] = key

    rows = {}
    for mfile in sorted((LIT / "strands").glob("S*_matrix.csv")):
        with mfile.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                k = alias.get(r["citekey"], r["citekey"])
                r["citekey"] = k
                if k in rows:
                    old = rows[k]
                    if depth(r["read_depth"]) > depth(old["read_depth"]):
                        old, r = r, old
                        rows[k] = old
                    try:
                        old["relevance_1to5"] = str(max(int(old["relevance_1to5"]), int(r["relevance_1to5"])))
                    except ValueError:
                        pass
                else:
                    rows[k] = {c: r.get(c, "") for c in COLS}

    header = ("% references.bib: merged from 01_literature/strands/S*.bib\n"
              "% by 01_literature/merge_strands.py. Edit the strand files, then re-run.\n\n")
    (LIT / "references.bib").write_text(
        header + "\n\n".join(f"% from {origin[k]}\n{e}" for k, e in kept.items()) + "\n", encoding="utf-8")
    with (LIT / "lit_matrix.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(sorted(rows.values(), key=lambda r: (-int(r["relevance_1to5"] or 0), r["citekey"])))

    no_row = sorted(k for k in kept if k not in rows)
    no_bib = sorted(k for k in rows if k not in kept)
    print(f"bib entries kept: {len(kept)}; aliases (duplicates): {len(alias)}; matrix rows: {len(rows)}")
    print("depth counts:", {d: sum(depth(r["read_depth"]) == v for r in rows.values()) for d, v in DEPTH.items()})
    print("aliases:", alias)
    print("bib without matrix row:", no_row)
    print("matrix row without bib:", no_bib)


if __name__ == "__main__":
    main()

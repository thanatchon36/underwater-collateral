"""Render a proposal draft: [@key] citations -> author-year, plus a reference list.

Reads a Markdown source with pandoc-style citations ([@a; @b, p. 5]) and
01_literature/references.bib, and writes <name>_rendered.md next to it:
- in-text citations become "(Author Year; Author and Author Year)";
- the "## References" section is filled with every cited entry, sorted;
- unknown keys stop the run (citation integrity: nothing unverified).
It also prints the word count of the body (title to "## References", excluding
tables, figure lines and HTML comments), which is what departmental limits count.

Usage: .venv/bin/python -I 06_proposal/render_references.py [06_proposal/proposal.md ...]
"""

import re
import unicodedata
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "01_literature/references.bib"
CITE = re.compile(r"\[(@[^\]]+)\]")
NARR = re.compile(r"(?<![\w@])@([A-Za-z][\w]*)")  # bare @key -> Author (Year)


def parse_bib(text: str) -> dict[str, dict[str, str]]:
    out = {}
    for m in re.finditer(r"@(\w+)\s*{\s*([^,\s]+)\s*,", text):
        i, depth = m.end(), 1
        j = i
        while depth and j < len(text):
            depth += {"{": 1, "}": -1}.get(text[j], 0)
            j += 1
        body, fields = text[i:j - 1], {"_entry": m.group(1).lower()}
        for f in re.finditer(r"(\w+)\s*=\s*", body):
            k, s = f.group(1).lower(), f.end()
            if s < len(body) and body[s] == "{":
                d, e = 1, s + 1
                while d and e < len(body):
                    d += {"{": 1, "}": -1}.get(body[e], 0)
                    e += 1
                fields.setdefault(k, body[s + 1:e - 1])
            else:
                fields.setdefault(k, re.match(r"[^,\n]*", body[s:]).group(0).strip())
        out[m.group(2)] = fields
    return out


ACCENT = {"'": "́", "`": "̀", '"': "̈", "^": "̂", "~": "̃", "=": "̄",
          ".": "̇", "c": "̧"}


def clean(s: str) -> str:
    s = re.sub(r"\{?\\([`'\"^~=.]|c(?=[\s{]))\s*\{?(\w)\}?\}?",
               lambda m: unicodedata.normalize("NFC", m.group(2) + ACCENT[m.group(1).strip()]), s)
    s = re.sub(r"\{?\\i\}?(?![a-zA-Z])", "ı", s)  # {\i}: dotless i (e.g. Taşpınar)
    s = s.replace("\\&", "&").replace("--", "–")
    s = re.sub(r"\\[a-zA-Z]+\s*", "", s)
    return re.sub(r"\s+", " ", s.replace("{", "").replace("}", "")).strip()


def authors(e: dict) -> list[str]:
    raw = e.get("author", "")
    if raw.startswith("{") and raw.endswith("}"):
        return [clean(raw)]
    names = [a.strip() for a in re.split(r"\s+and\s+", raw) if a.strip()]
    return [clean(n.split(",")[0]) if "," in n else clean(n.split()[-1]) for n in names]


def short(e: dict) -> str:
    a = authors(e)
    if "others" in [x.lower() for x in a]:
        a = [x for x in a if x.lower() != "others"] + ["others"]
    name = a[0] if len(a) == 1 else f"{a[0]} and {a[1]}" if len(a) == 2 and a[1] != "others" else f"{a[0]} et al."
    return f"{name} {e.get('year', 'n.d.')}{e.get('_suffix', '')}"


def add_suffixes(keys: list[str], bib: dict) -> None:
    """Give same author-year citations a/b suffixes: by `date` (YYYY-MM-DD) where every entry
    in the group has one (chronological), otherwise by title (Harvard convention)."""
    groups: dict[str, list[str]] = {}
    for k in keys:
        bib[k].pop("_suffix", None)
        groups.setdefault(short(bib[k]), []).append(k)
    for ks in groups.values():
        if len(ks) > 1:
            dated = all("date" in bib[k] for k in ks)
            for i, k in enumerate(sorted(ks, key=lambda k: (bib[k]["date"] if dated else "",
                                                             clean(bib[k].get("title", "")).lower()))):
                bib[k]["_suffix"] = "abcdefghij"[i]


def full(e: dict) -> str:
    raw = e.get("author", "")
    if raw.startswith("{") and raw.endswith("}"):
        who = clean(raw)
    else:
        names = [clean(a) for a in re.split(r"\s+and\s+", raw) if a.strip()]
        who = "; ".join("et al." if n.lower() == "others" else n for n in names)
    venue = next((clean(e[k]) for k in ("journal", "booktitle", "institution", "howpublished", "publisher")
                  if k in e), "")
    extra = ", ".join(x for x in [f"{e['volume']}({e['number']})" if "volume" in e and "number" in e
                                  else (f"{clean(e.get('type', 'WP'))} {clean(e['number'])}" if "number" in e and e["_entry"] == "techreport"
                                        else e.get("volume", f"no. {clean(e['number'])}" if "number" in e else "")),
                                  clean(e.get("pages", ""))] if x)
    title = clean(e.get("title", ""))
    parts = [f"{who} ({e.get('year', 'n.d.')}{e.get('_suffix', '')}). {title}"
             + ("" if title[-1:] in "?!." else ".")]
    if venue:
        parts.append(f"*{venue}*" + (f", {extra}" if extra else "") + ".")
    if "doi" in e:
        parts.append(f"doi:{e['doi']}.")
    elif "url" in e:
        parts.append(f"<{e['url']}>.")
    return " ".join(parts)


def split_loc(raw: str) -> tuple[str, str]:
    """'@key, p. 59' -> ('key', 'p. 59'); a locator is optional."""
    key, _, loc = raw.strip().lstrip("@").partition(",")
    return key.strip(), loc.strip()


def render(src: Path, bib: dict) -> None:
    text = src.read_text(encoding="utf-8")
    body, _, _ = text.partition("## References")
    cited: list[str] = []
    found = [split_loc(k)[0] for m in CITE.finditer(body) for k in m.group(1).split(";")]
    found += NARR.findall(CITE.sub("", body))
    add_suffixes(list(dict.fromkeys(k for k in found if k in bib)), bib)

    def sub(m: re.Match) -> str:
        parts = [split_loc(k) for k in m.group(1).split(";")]
        missing = [k for k, _ in parts if k not in bib]
        if missing:
            sys.exit(f"{src.name}: unknown citekeys {missing}")
        cited.extend(k for k, _ in parts if k not in cited)
        return "(" + "; ".join(short(bib[k]) + (f", {loc}" if loc else "") for k, loc in parts) + ")"

    def narr(m: re.Match) -> str:
        k = m.group(1)
        if k not in bib:
            sys.exit(f"{src.name}: unknown citekey {k}")
        if k not in cited:
            cited.append(k)
        name, year = short(bib[k]).rsplit(" ", 1)
        return f"{name} ({year})"

    out = NARR.sub(narr, CITE.sub(sub, body))
    refs = sorted(cited, key=lambda k: (authors(bib[k])[0].lower(), bib[k].get("year", ""),
                                         bib[k].get("_suffix", "")))
    out += "## References\n\n" + "\n\n".join(full(bib[k]) for k in refs) + "\n"
    dst = src.with_name(src.stem + "_rendered.md")
    dst.write_text(out, encoding="utf-8")

    counted = []
    for line in re.sub(r"<!--.*?-->", "", body, flags=re.S).splitlines():
        if line.startswith("|") or line.startswith("![") or line.startswith("*Research proposal") \
                or line.startswith("**Working draft"):
            continue
        counted.append(line)
    words = len(re.findall(r"\b[\w'’–-]+\b", NARR.sub("Author (2000)", CITE.sub("", "\n".join(counted)))))
    print(f"{src.name}: {len(refs)} references, body {words} words (tables, figures, notes excluded) -> {dst.name}")


def main() -> None:
    bib = parse_bib(BIB.read_text(encoding="utf-8"))
    srcs = [Path(a) for a in sys.argv[1:]] or [ROOT / "06_proposal/proposal.md"]
    for s in srcs:
        render(s.resolve(), bib)


if __name__ == "__main__":
    main()

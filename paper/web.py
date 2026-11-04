"""Build the web reader docs/paper/ from paper/paper.tex (same text as the PDF).

A standalone page built by pandoc with paper/reader.html: masthead, abstract, a results strip whose
numbers come from paper/numbers.tex (written by 04_analysis/src/paper_numbers.py), contents,
numbered sections, author-year citations linked to the references, then the appendices. The PDF and
the PNG versions of the figures are copied next to it; GitHub Pages serves docs/ at
https://thanatchon36.github.io/underwater-collateral/. Requires pandoc on PATH.
Usage: .venv/bin/python -I paper/web.py   (paper/build.sh runs it after the PDF)
"""

from __future__ import annotations

import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "docs" / "paper"
FIG_PNG = ROOT / "04_analysis" / "outputs" / "figures"
REPO_URL = "https://github.com/thanatchon36/underwater-collateral"
PAPER_URL = "https://thanatchon36.github.io/underwater-collateral/paper/"
DATA_URL = "https://huggingface.co/datasets/thanatchon36/underwater-collateral-data"
CONCEPT_DOI = "10.5281/zenodo.23949061"

# (label, style, finding, detail) with \macro placeholders from numbers.tex.
# style: "ref" = descriptive or design result, "null" = pending or illustrative.
RESULTS = [
    (
        "Q1 · 2011",
        "ref",
        r"Urban sheets almost wholly flooded in 2011 are valued \binTopUrbanPct% below nearby dry sheets",
        r"\pilotParcelsM million parcels; holding land cover fixed leaves about 8%, imprecise; "
        "not identified as capitalisation",
    ),
    (
        "Q1 · 2024",
        "ref",
        r"\radarTreated cadastral sheets flooded on Sentinel-1 radar maps",
        r"\radarTreatedClusters treated clusters in four provinces; Sentinel-2 shows flooding on "
        r"\valTreatedPrec% of them",
    ),
    (
        "Q1 · power",
        "ref",
        r"Minimum detectable effect \regMdePooled log points",
        r"about a fully recognised 4.6% hazard discount; power \powFullMid against full, "
        r"\powHalfMid against half recognition",
    ),
    (
        "Q1 · inference",
        "ref",
        r"Placebo-footprint test rejects a true null \mcxNullRi of the time",
        r"wild cluster bootstrap \mcxNullWcb; studentised placebo \prxNullRegT; "
        r"\mcxReps synthetic next rounds",
    ),
    (
        "Q3 · illustrative",
        "null",
        r"Pricing hazard raises the breaking-point flood severity by \lamSStarEightChange%",
        r"loan-to-value 0.8, 4.6% discount; \lamSStarOneChange% at a ratio of 1.0; synthetic bank",
    ),
    (
        "Q1 · estimate",
        "null",
        "Primary estimate pending",
        "awaits the first Treasury valuation round after 2023\u201326",
    ),
]


def macros() -> dict[str, str]:
    text = (HERE / "numbers.tex").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"\\newcommand\{\\(\w+)\}\{(.*)\}\s*$", text, re.M):
        v = m.group(2).replace("\\%", "%").replace("$-$", "\u2212").replace("{,}", ",")
        out[m.group(1)] = re.sub(r"[{}$\\]", "", v)
    return out


def expand(text: str, values: dict[str, str]) -> str:
    return re.sub(r"\\(\w+)", lambda m: values[m.group(1)], text)  # a missing macro fails


def flatten(tex: str) -> str:
    """Inline \\input files and drop table markup that pandoc does not read (adjustbox, cmidrule)."""
    def inp(m: re.Match) -> str:
        name = m.group(1).removesuffix(".tex") + ".tex"
        return flatten((HERE / name).read_text(encoding="utf-8"))

    tex = re.sub(r"\\input\{([^}]+)\}", inp, tex)
    tex = re.sub(r"\\begin\{adjustbox\}\{[^}]*\}", "", tex)
    tex = re.sub(r"\\cmidrule(?:\([^)]*\))?\{[^}]*\}", "", tex)
    tex = re.sub(r"\\addlinespace(?:\[[^\]]*\])?", "", tex)
    return move_tabnotes(tex.replace("\\end{adjustbox}", ""))


def move_tabnotes(tex: str) -> str:
    """pandoc keeps only the body and caption of a float; put each \\tabnote after its float."""
    out, pos = [], 0
    for m in re.finditer(r"\\begin\{(table|figure)\}.*?\\end\{\1\}", tex, re.S):
        block, notes, i = m.group(0), [], 0
        while (j := block.find("\\tabnote{", i)) != -1:
            content, end = braced(block, j + len("\\tabnote"))
            notes.append(content)
            block = block[:j] + block[end:]
            i = j
        out.append(tex[pos : m.start()] + block)
        out.extend(f"\n\nTABNOTEMARK \\textit{{Notes:}} {n}\n\n" for n in notes)
        pos = m.end()
    out.append(tex[pos:])
    return "".join(out)


def braced(tex: str, start: int) -> tuple[str, int]:
    """Return the content of the brace group opening at tex[start] and the index after it."""
    assert tex[start] == "{"
    depth, i = 0, start
    while True:
        depth += {"{": 1, "}": -1}.get(tex[i], 0)
        i += 1
        if depth == 0:
            return tex[start + 1 : i - 1], i


def plain(tex: str) -> str:
    tex = re.sub(r"\\\\(\[[^\]]*\])?", " ", tex)
    tex = re.sub(r"\\(textbf|large|small|emph)\b", "", tex)
    tex = tex.replace("--", "\u2013").replace("~", " ")
    return re.sub(r"\s+", " ", re.sub(r"[{}]", "", tex)).strip()


def pandoc(tex: str, args: list[str]) -> str:
    tmp = HERE / ".web.tex"
    tmp.write_text(tex, encoding="utf-8")
    try:
        return subprocess.run(
            ["pandoc", tmp.name, "--from=latex", "--to=html5", "--mathml", "--wrap=none", *args],
            cwd=HERE,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    finally:
        tmp.unlink(missing_ok=True)


def main() -> int:
    src = (HERE / "paper.tex").read_text(encoding="utf-8")
    preamble, body = src.split("\\begin{document}", 1)
    defs = "\n".join(
        line for line in preamble.splitlines() if line.startswith("\\newcommand")
    )
    head = "\\documentclass{article}\n" + flatten("\\input{numbers.tex}") + "\n" + defs + "\n"

    title_tex, _ = braced(preamble, preamble.index("\\title{") + len("\\title"))
    title = plain(title_tex.replace("\\\\[6pt]", ": ").split("\\large")[0])
    subtitle = plain(title_tex.split("\\large", 1)[1]) if "\\large" in title_tex else ""
    if subtitle:
        title = title.rstrip(": ")
    author_tex, _ = braced(preamble, preamble.index("\\author{") + len("\\author"))
    author = plain(author_tex.split("\\thanks")[0])
    date_tex, _ = braced(preamble, preamble.index("\\date{") + len("\\date"))
    version = plain(date_tex.split("\\\\")[0])

    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", body, re.S)
    if abstract is None:
        raise SystemExit("no abstract in paper.tex")
    abstract_html = pandoc(
        head + "\\begin{document}\n" + abstract.group(1).replace("\\noindent", "") + "\n\\end{document}\n",
        [],
    )
    keywords = re.search(r"\\textbf\{Keywords:\}(.*?)\\\\", body, re.S)
    jel = re.search(r"\\textbf\{JEL:\}(.*?)\n", body)

    body = body[: abstract.start()] + body[abstract.end() :]
    body = body.replace("\\maketitle", "").replace("\\newpage", "")
    body = re.sub(r"\\noindent\\textbf\{Keywords:\}.*?\n\\textbf\{JEL:\}[^\n]*\n", "", body, flags=re.S)
    body = body.replace("\\bibliography{refs}", "")
    body = flatten(body)

    # Equations: pandoc does not number them. Number every equation in document order, as LaTeX
    # does, put an anchor before it and render the number next to it after conversion.
    eq_labels: dict[str, int] = {}
    counter = 0

    def number_eq(m: re.Match) -> str:
        nonlocal counter
        counter += 1
        content = m.group(1)
        lab = re.search(r"\\label\{(eq:[^}]+)\}", content)
        if lab:
            eq_labels[lab.group(1)] = counter
            content = content.replace(lab.group(0), "")
        return f"\\hypertarget{{eqno-{counter}}}{{}}\\[{content}\\]"

    body = re.sub(r"\\begin\{equation\}(.*?)\\end\{equation\}", number_eq, body, flags=re.S)
    page = pandoc(
        head + "\\begin{document}" + body,
        [
            f"--template={HERE / 'reader.html'}",
            "--standalone",
            "--citeproc",
            "--bibliography=refs.bib",
            "--metadata=link-citations:true",
            "--resource-path=.:sections",
            "--number-sections",
            "--toc",
            "--toc-depth=1",
            f"--metadata=title:{title}",
            f"--metadata=subtitle:{subtitle}",
            f"--metadata=author:{author}",
            "--metadata=pagetitle:Underwater Collateral",
            "--metadata=description:Working paper on flood risk in official land values, credit "
            "under relief and bank capital in Thailand.",
        ],
    )
    page = re.sub(
        r'<(?:embed|img) src="(?:figures/)?(fig_[\w-]+?)(?:\.pdf)?"[^>]*/>',
        r'<img src="figures/\1.png" alt="" loading="lazy" />',
        page,
    )

    # Equation numbers beside the display, and (n) as the text of every \eqref.
    by_number = {n: lab for lab, n in eq_labels.items()}

    def eq_block(m: re.Match) -> str:
        n = int(m.group(1))
        anchor = f' id="{by_number[n]}"' if n in by_number else ""
        return f'<span class="eq"{anchor}>{m.group(2)}<span class="eqno">({n})</span></span>'

    page = re.sub(
        r'<span id="eqno-(\d+)"></span>\s*((?:<span class="math display">)?<math display="block".*?</math>(?:</span>)?)',
        eq_block,
        page,
        flags=re.S,
    )
    for lab, n in eq_labels.items():
        page = page.replace(f">[{lab}]</a>", f">({n})</a>")

    # Table and figure numbers in captions, in document order (pandoc's \ref numbering is the same).
    count = {"caption": 0, "figcaption": 0}

    def caption(m: re.Match) -> str:
        tag = m.group(1)
        count[tag] += 1
        word = "Table" if tag == "caption" else "Figure"
        return f"<{tag}><b>{word} {count[tag]}.</b> "

    page = re.sub(r"<(caption|figcaption)>", caption, page)
    page = page.replace("<p>TABNOTEMARK ", '<p class="tabnote">')

    # The bibliography goes before the appendices, as in the PDF.
    refs = re.search(r'<div id="refs".*?\n</div>\n', page, re.S)
    first_app = re.search(r'<h1 data-number="\d+" id="app:', page)
    if refs and first_app:
        block = '<h1 class="unnumbered" id="references">References</h1>\n' + refs.group(0)
        page = page[: refs.start()] + page[refs.end() :]
        first_app = re.search(r'<h1 data-number="\d+" id="app:', page)
        page = page[: first_app.start()] + block + page[first_app.start() :]
        toc_app = re.search(r'<li><a href="#app:', page)
        if toc_app:
            page = page[: toc_app.start()] + '<li><a href="#references">References</a></li>\n' + page[toc_app.start() :]

    # Appendix sections are lettered in the PDF; pandoc numbers them on from the body.
    app_nums = re.findall(r'<h1 data-number="(\d+)" id="app:', page)
    if app_nums:
        letters = {n: chr(ord("A") + i) for i, n in enumerate(app_nums)}
        for n, letter in letters.items():
            page = re.sub(
                rf'(<span class="header-section-number">){n}((?:\.\d+)*</span>)', rf"\g<1>{letter}\2", page
            )
            page = re.sub(
                rf'(<span class="toc-section-number">){n}((?:\.\d+)*</span>)', rf"\g<1>{letter}\2", page
            )
        # Cross-references to appendix headings take the letter too.
        heads = {ident: num for num, ident in re.findall(r'<h\d data-number="([\d.]+)" id="([^"]+)"', page)}
        for ident, num in heads.items():
            top = num.split(".")[0]
            if top in letters:
                shown = letters[top] + num[len(top):]
                page = re.sub(
                    rf'(<a href="#{re.escape(ident)}" data-reference-type="ref" data-reference="{re.escape(ident)}">)[^<]*(</a>)',
                    rf"\g<1>{shown}\2",
                    page,
                )

    values = macros()
    items = "\n".join(
        f'<li class="r r-{style}"><span class="r-id">{html.escape(label)}</span>'
        f'<span class="r-text">{html.escape(expand(text, values))}'
        f"<small>{html.escape(expand(detail, values))}</small></span></li>"
        for label, style, text, detail in RESULTS
    )
    meta = f"<b>{html.escape(version)}</b>"
    if keywords:
        meta += " · " + html.escape(plain(keywords.group(1)))
    if jel:
        meta += " · JEL " + html.escape(plain(jel.group(1)).rstrip("."))
    actions = (
        '<li><a href="paper.pdf">Download PDF</a></li>'
        f'<li><a href="{REPO_URL}">Code and replication</a></li>'
        f'<li><a href="{DATA_URL}">Data (Hugging Face)</a></li>'
        f'<li><a href="{REPO_URL}/blob/main/05_design/pre_analysis_plan_rq1_draft.md">RQ1 pre-analysis plan</a></li>'
        f'<li><a href="https://doi.org/{CONCEPT_DOI}">Zenodo archive</a></li>'
    )
    bib = (
        "@techreport{chongmankhong2026underwater,\n"
        "  author      = {Chongmankhong, Thanatchon},\n"
        f"  title       = {{{title.replace(chr(0x2013), '--')}{': ' + subtitle if subtitle else ''}}},\n"
        "  year        = {2026},\n"
        "  type        = {Working paper},\n"
        f"  doi         = {{{CONCEPT_DOI}}},\n"
        f"  url         = {{{PAPER_URL}}}\n"
        "}"
    )
    cite = f"<h2>How to cite</h2><pre><code>{html.escape(bib)}</code></pre>"
    colophon = (
        "<p>Rendered from <code>paper/paper.tex</code> by <code>paper/web.py</code>. Every number "
        "comes from the script outputs in <code>04_analysis/outputs/tables/</code> through "
        "<code>paper/numbers.tex</code>; the PDF is authoritative. Public data only. Views and "
        "errors are the author's own.</p>"
    )
    for marker, value in (
        ("<!--ABSTRACT-->", abstract_html),
        ("<!--META-->", meta),
        ("<!--ACTIONS-->", actions),
        ("<!--RESULTS-NOTE-->", "Headline numbers, generated from the script outputs. "
         "Amber: descriptive or design results; grey: illustrative or pending."),
        ("<!--RESULTS-->", items),
        ("<!--CITE-->", cite),
        ("<!--COLOPHON-->", colophon),
    ):
        if marker not in page:
            raise SystemExit(f"reader.html lacks {marker}")
        page = page.replace(marker, value)

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(page, encoding="utf-8")
    shutil.copyfile(HERE / "paper.pdf", OUT / "paper.pdf")
    (OUT / "figures").mkdir(exist_ok=True)
    for name in sorted(set(re.findall(r'src="figures/([\w.-]+)"', page))):
        shutil.copyfile(FIG_PNG / name, OUT / "figures" / name)
    print(f"wrote {OUT / 'index.html'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

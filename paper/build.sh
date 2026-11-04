#!/usr/bin/env bash
# Build paper/paper.pdf: regenerate numbers, tables, figures and refs.bib, then compile with tectonic;
# then write the web reader docs/paper/ (paper/web.py).
# Usage: paper/build.sh [--no-render]   (render writes page PNGs to paper/render/ for inspection)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
TECTONIC="${TECTONIC:-$HOME/.local/bin/tectonic}"
PY="$ROOT/.venv/bin/python"
RENDER_PY="${RENDER_PY:-$HOME/.local/share/uv/tools/pdfplumber/bin/python}"

"$PY" -I "$ROOT/04_analysis/src/paper_numbers.py"

cd "$HERE"
export SOURCE_DATE_EPOCH="$(git -C "$ROOT" log -1 --format=%ct 2>/dev/null || date +%s)"
"$TECTONIC" --keep-logs --keep-intermediates --outdir . paper.tex
echo "built $HERE/paper.pdf"
"$PY" -I "$HERE/web.py"   # web reader in docs/paper/ (needs pandoc)

if [[ "${1:-}" != "--no-render" && -x "$RENDER_PY" ]]; then
  mkdir -p render && rm -f render/page-*.png
  "$RENDER_PY" - <<'EOF'
import pypdfium2 as pdfium
pdf = pdfium.PdfDocument("paper.pdf")
for i in range(len(pdf)):
    pdf[i].render(scale=1.4).to_pil().save(f"render/page-{i + 1:02d}.png")
print(f"rendered {len(pdf)} pages to render/")
EOF
fi

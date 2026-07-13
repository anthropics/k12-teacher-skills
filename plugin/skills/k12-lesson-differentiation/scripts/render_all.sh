#!/usr/bin/env bash
# Copyright 2026 Anthropic, PBC
# Copyright 2026 Learning Commons
# SPDX-License-Identifier: Apache-2.0

# Render all four artifacts (teacher plan + three tier worksheets) from one
# differentiation.json in a single invocation. Writes editable .docx (the teacher
# deliverable) and an .html twin of each (a preview that renders even without python-docx).
# Fail-fast: any renderer error stops the run.
#
# Usage: bash scripts/render_all.sh differentiation.json "$OUTPUT_DIR"
set -euo pipefail

json="${1:?usage: render_all.sh DIFFERENTIATION_JSON OUTPUT_DIR}"
outdir="${2:?usage: render_all.sh DIFFERENTIATION_JSON OUTPUT_DIR}"
here="$(cd "$(dirname "$0")" && pwd)"

mkdir -p "$outdir"
# python-docx powers the .docx output; the .html twins render without it. If the install
# can't complete (offline container), render html now so the twins always exist.
if ! python3 -c "import docx" 2>/dev/null; then
  python3 -m pip install -q "python-docx==1.1.2" || true
fi
if python3 -c "import docx" 2>/dev/null; then
  python3 "$here/render_documents.py" "$json" --format both --outdir "$outdir"
else
  # Render the html twins so a readable preview still exists, then fail loudly: the
  # teacher's .docx deliverables could not be produced.
  python3 "$here/render_documents.py" "$json" --format html --outdir "$outdir"
  echo "error: python-docx could not be installed — no .docx deliverables were produced" >&2
  exit 1
fi
# Persist the source JSON alongside the rendered artifacts so later revision
# turns can re-render from it (same guarantee the lesson-planning renderer
# makes with lesson.json).
cp "$json" "$outdir/differentiation.json" 2>/dev/null || true

# Delivery guarantee: when $OUTPUT_DIR is set and the render went elsewhere
# (a staging dir like /tmp/out), mirror EVERYTHING into $OUTPUT_DIR too.
# Revision turns re-render from the differentiation.json that lands there;
# hand-copying a subset there is the failure this removes.
if [ -n "${OUTPUT_DIR:-}" ] && [ "$(cd "$outdir" && pwd)" != "$(mkdir -p "$OUTPUT_DIR" && cd "$OUTPUT_DIR" && pwd)" ]; then
  cp -R "$outdir"/. "$OUTPUT_DIR"/
fi

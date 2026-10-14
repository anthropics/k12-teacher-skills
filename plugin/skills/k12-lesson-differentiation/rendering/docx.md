# Word path — the documents as editable Word files

On this path every document is a Word file; no artifact or Claude Doc is made. The only format word
in your prose is "Word document", and you never link or name the `.html` files the render command
also writes.

## 1. `differentiation.json` is already written (5a)

Before rendering, read the "Word path only" part of `references/differentiation-json.md` (how the
renderer reads headings, tables, writing space and print-safety) and adjust the file if needed; the
subject file's document templates apply here as written.

## 2. Render all four Word documents — one command, same turn

```bash
bash scripts/render_all.sh differentiation.json "$OUTPUT_DIR"
```

This writes `$OUTPUT_DIR/teacher_plan.docx`, `$OUTPUT_DIR/worksheet_group_a.docx`,
`$OUTPUT_DIR/worksheet_group_b.docx`, and `$OUTPUT_DIR/worksheet_group_c.docx` in one invocation,
plus `.html` and `differentiation.json` working files. Render straight into `$OUTPUT_DIR` and leave
everything the script writes in place — later revision turns re-render from the working files even
though the teacher only sees the Word documents. Then list `$OUTPUT_DIR` and confirm every document
has both its `.docx` and `.html`; if either is missing or tiny, rerun the script. Present all four
Word documents to the teacher together — attach the teacher plan last so it lands on top (chat
surfaces stack newest-first). If the script errors, fix `differentiation.json` (it is almost always
malformed JSON) and rerun. If file generation fails entirely, say so clearly — do not silently fall
back to a chat-only delivery. **Do not open, cat, head, or grep the renderer scripts** (everything
in `scripts/`) — their behavior is fully specified here.

## 3. Revisions

After 5d's edits to `differentiation.json`, rerun the same command — every document re-renders
(instant); never edit a generated document directly.

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0

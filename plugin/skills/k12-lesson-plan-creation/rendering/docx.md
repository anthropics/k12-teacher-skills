# Word path — the documents as editable Word files

On this path every document is a Word file; no artifact or Claude Doc is made. The only format word
in your prose is "Word document", and you never link or name the `.html` files the render command
also writes.

## 1. `lesson.json` is already written (5a)

Before rendering, read the "Word path only" part of `references/lesson-json.md` (how the renderer
reads headings, labels, blocks, print-safety and `theme`) and adjust the file if needed; the subject
file's page-layout skeletons apply here as written.

## 2. Render every Word document — one command, same turn

```bash
bash scripts/render_all.sh lesson.json "$OUTPUT_DIR"
```

This writes one editable `.docx` per `documents[]` entry, named by `id` (e.g.
`$OUTPUT_DIR/lesson_plan.docx`, `student_materials.docx`, `observation_template.docx`,
`source_packet.docx`), plus `.html` and `lesson.json` working files. Render straight into
`$OUTPUT_DIR` and leave everything the script writes in place — later revision turns re-render from
the working files even though the teacher only sees the Word documents. Then list `$OUTPUT_DIR` and
confirm every document has both its `.docx` and `.html`; if either is missing or tiny, rerun the
script. Present the Word documents to the teacher together — attach the lesson plan last so it lands
on top (chat surfaces stack newest-first). If the script errors, fix `lesson.json` (it is almost
always malformed JSON) and rerun. **Do not open, cat, head, or grep the renderer scripts**
(everything in `scripts/`) — their behavior is fully specified here.

## 3. Revisions

After 5d's edits to `lesson.json`, rerun the same command — every document re-renders (instant);
never edit a generated document directly.

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0

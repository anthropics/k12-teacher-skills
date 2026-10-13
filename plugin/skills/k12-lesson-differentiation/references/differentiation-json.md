# `differentiation.json` — the common baseline for all four documents (every path)

Written at Step 5a on EVERY path, before any document exists. It fixes WHAT the set contains: the
teacher plan and the three tier documents, every task, scaffold, answer space, vocabulary item and
teacher note, and the exact wording of anything that appears in more than one document — so the plan
and the tiers cannot disagree, and R6 (same context, same core tasks across tiers) holds by
construction, whichever way the documents are made. The Word path renders it block by block;
otherwise Claude Docs and Design pages are made from it. Its block types are a content inventory,
not a layout: a `workspace` means "room to write here", a `callout` "this is a task / a note / a
support / the standard", a `fill_table` "students fill in a grid", a `fill_in` "a blank in a
sentence", `cards` "parallel items", `group` / `page_break` "these stay together" / "a new page
starts" — on the canvas render each however serves the page, and whatever this file says the
renderer does by itself (sizing writing space, row heights) is yours to do there. The content rules
in `references/output.md` and the subject file's document templates apply in full.

## What the file holds

The JSON holds a top-level `theme`, a `shared` block (content registered once) and a `documents[]`
array of four entries, each authored as free-form `sections` of `blocks`. Anything that appears in
more than one document — the standard, the task set, the exit ticket, vocabulary, sentence supports,
misconceptions — is registered once in `shared` under a key you choose and pulled into each document
with `{"type": "from_shared", "key": …}`, so the plan and the tiers cannot drift apart. A section's
`heading` is its title; a block's `label` is a short lead-in — a label that repeats its section's
heading says the same words twice (the task's name belongs in one of them, not both). Never re-type
lesson content into a document from memory: every document is made from this file, and every later
content change goes into it first (SKILL.md 5d). `references/example_differentiation.json` is a
filled-in worked example.

## Write the complete `differentiation.json` (same turn)

Write ONE `differentiation.json` (in the working folder; on the Word path the render command copies
it beside the documents): a top-level `theme`, the **`shared` block** (write this FIRST — the
identity fields, the standard verbatim, each tier task under its own key (`t1`, `t2`, …), the exit
ticket, and composed blocks for vocabulary, sentence supports, and misconceptions; also
`anchor_activity` (early-finisher task in student-facing second person — directions only, no
rationale) and `reflect_prompt` (the closing reflective question)), and a `documents` array with 4
entries: `{"id": "teacher_plan", "audience": "teacher", …}` and `{"id": "worksheet_group_a" /
"worksheet_group_b" / "worksheet_group_c", "audience": "student", …}`. Each document's `sections`
follow the subject file's document content templates.

**Schema** — the complete field skeleton (`blocks` shows one of each type); sufficient on its own,
do not read any other file for the schema:

```
theme: {primary: "#…"}
shared:
  subject, grade, standard_code, standard_text        (required identity)
  duration?
  <any key you choose>: string
                      | block | block[]
                      | {teacher: …, student: … or null, stimulus?: block[]}
  (only `standard` is special — it assembles standard_code+standard_text)
documents[]: {id: teacher_plan|worksheet_group_a|worksheet_group_b|worksheet_group_c,
              audience: teacher|student, eyebrow, title, meta, orientation?: landscape,
              sections[]: {heading, blocks[]}}
  block types:
    {type: from_shared, key, label?}
    {type: labeled, label, text} | {type: paragraph, text}
    {type: callout, kind: special|student-task|teacher-note|student-note, label, text}
    {type: h2, text} | {type: h3, text} | {type: list, label?, ordered?, items[]}
    {type: checklist, label?, items[]} | {type: fill_in, label?, size: short|med|long}
    {type: phase_header, name, minutes}   (science teacher plan; supported by all renderers)
    {type: table, headers[]?, rows[[]], empty_row_height_pt?}
    {type: fill_table, headers[], blank_rows: int, row_height_pt?}
    {type: number_line, min, max, ticks?, marks[]?}
    {type: source_card, title, author?, date?, origin?, excerpt}
    {type: cards, items[{title, text}]} | {type: workspace, size: small|med|large, height_pt?}
    {type: group, blocks[]} | {type: columns, left[], right[]} | {type: page_break}
```

A document may carry `"orientation": "landscape"` for a wide handout (absent = portrait); the Word
renderer ignores it; Design pages are laid out that way.

**`shared` is a content registry.** Register each tier task under its own key (`t1`, `t2`, …), the
exit ticket as `exit_ticket`, and any other content that appears on more than one document, under
keys you choose. A key's value can be a string, a composed block (a vocabulary `table`, a
misconceptions `table`, sentence-support text with its writing space), or a faceted object
`{teacher: …, student: …, stimulus?: [blocks]}` — on a **student** page the `student` facet renders,
then any `stimulus` blocks; on the **teacher** page any `stimulus` blocks render first, then the
teacher facet as plain script, then the student facet as one "Students see" line. Key names carry no special rendering — compose vocabulary, misconceptions,
and sort buckets as blocks yourself (`references/example_differentiation.json` shows each pattern).

Keep writing tight; no emoji in JSON content (what a canvas page adds around it is the canvas's
business). The density rules in `references/output.md` are hard requirements for every text field.

**Which block when** — pick by what the content *is*, not how it should look:

| Block | Use it for |
|---|---|
| `callout` `kind: special` | The one anchoring fact per artifact — the target standard. Typically once. |
| `callout` `kind: student-task` | Any task students do: anchor task, exit ticket prompt, a tier task shown in the plan. |
| `callout` `kind: teacher-note` | An aside the teacher reads but does not say aloud: conferring moves, a watch-for. |
| `callout` `kind: student-note` | A reminder students read on their worksheet: a hint card, a key fact. (A sentence support students write from is plain text near its task, not a callout.) |
| `list` `ordered: true` | A numbered sequence — the problem set, procedure steps. Unordered otherwise. |
| `list` with `label` | A titled enumeration — several discrete items under one label. |
| `cards` | 2–4 parallel items of roughly equal length — tier summaries, sort buckets. Never for long or unbalanced items. |
| `table` (no `headers`) | Term/definition pairs, label/value reference rows. |
| `table` with `headers` | Real tabular data with column labels (per-tier scaffolds, misconceptions). |
| `number_line` | A drawn number line (`min`, `max`, `ticks`, optional `marks`). `ticks` omitted defaults to 10 evenly spaced segments; `ticks: 0` draws a bare line with only the `min`/`max` end labels and no tick marks, for students to partition themselves. |
| `workspace` | Student writing space; `size: small|med|large` or grade-banded default. |

**The tier documents.** The three tier documents (in the same `documents` array) differ ONLY in
their scaffolding and extension blocks (R6). **Every tier document pulls task text with
`from_shared` blocks — never re-type, reword, or split task text into a document's own blocks** (so
the plan and all three tiers stay verbatim-consistent — reworded tasks drift apart in revision).
Each task has its own `shared` key, pulled one at a time so scaffolds sit with their task: `{"type":
"from_shared", "key": "t1", "label": "1"}` renders Task 1 as a numbered item; follow each task — and
every other prompt students answer (the exit ticket, Reflect, If you finish early, a tier-only
extension) — with a `workspace` block. The required order within the section is strict: for each
task N — at most ONE scaffold block for task N (merge multiple supports into one labeled block;
never two "Before Task N" blocks), then the task via its key. A scaffold must NEVER appear after its
target task, and nothing sits between a scaffold and its task. That is how the R7 fade pattern is
expressed — Task 1 gets a scaffold block, Task 2's is lighter, later tasks have none. A tier-only
task (the Above extension, an Above-only sub-question) is its own headed block — never an edit to
shared task text. Below-tier scaffolds follow R4; the Above-tier extension passes R7's quality test.
Asset framing rules (`references/output.md`) apply to every student-facing block.

---

## Word path only — how the renderer reads the file

Read this part on the Word path (`rendering/docx.md`); otherwise skip it.

- A `paragraph` or `labeled` block is at most 3 sentences. Parallel tier content goes in ONE `table`
  block — rows = phases or features, columns = tiers, ≤ ~25 words per cell. An aside longer than one
  sentence becomes its own `callout` block. The standard is quoted once: the target-standard
  callout, from `shared`.
- Section titles are heading blocks (`h2`/`h3`), not bold paragraphs; a scaffold prompt's short
  student-friendly subheading is an `h3` on its own line.
- Tabular content — data tables, "complete the table" tasks, row-and-column organizers — must be a
  `{"type": "table", "headers": [...], "rows": [[...]]}` block (a row of empty strings renders as
  ruled writing space). Never draw a table inside a `text` field: markdown pipe rows, box-drawing
  characters, ASCII art, and symbol glyphs (■, □) print literally on the page and fail print-safety.
  Never write bullet characters (•, -) inside a `text` string — use a `list` block; a paragraph
  collapses line breaks and the bullets run together into one line.
- Use `workspace` blocks for writing space — they render as open whitespace sized by grade
  automatically (lower grades get much more room, and K–5 prose answers get ruled lines; math work
  space stays open for drawing). Set `height_pt` only when a task needs more than the default:
  130–150 for full written explanations and exit tickets, 90–110 for short extension questions.
  Empty table cells are writing space and get a grade-banded minimum height automatically — don't
  set `empty_row_height_pt` below ~70pt for prose rows. This applies to every prose field in all
  four documents.
- Never write layout code and never edit a generated document directly — every change goes into
  `differentiation.json` and is re-rendered (instant). **Do not open, cat, head, or grep the
  renderer scripts** (everything in `scripts/`) — their behavior is fully specified by
  `rendering/docx.md`; reading script source tells you nothing these instructions don't already
  state.
- Styling: the top-level `theme` applies to all four documents; per-document `theme` overrides stay
  available.

### Fallback — bespoke generation code (Word path, exception only; on the canvas they are more artboards)

Only if the user explicitly asks for an artifact or layout the bundled renderer cannot express (a
different document type, landscape poster, slide deck, etc.): write generation code from scratch for
that artifact. Source its content from the same `differentiation.json` (especially `shared`) so it
stays consistent with the other artifacts. Tell the user this path is slower.

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0

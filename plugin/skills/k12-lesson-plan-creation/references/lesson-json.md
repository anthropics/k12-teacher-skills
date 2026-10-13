# `lesson.json` — the lesson's common baseline (every path)

Written at Step 5a on EVERY path, before any document exists. It fixes WHAT the package contains:
the document set, every task, support, answer space, vocabulary item, look-for and teacher note, and
the exact wording of anything that appears in more than one document — so the lesson plan, student
materials and observation template cannot disagree, whichever way they are made. The Word path
renders it block by block; otherwise Claude Docs and Design pages are made from it. Its block types
are a content inventory, not a layout: an `answer_box` means "room to write here", a `callout` "this
is a task / a note / a support / the standard", a `fill_table` "students fill in a grid", a
`number_line` "a number line", `cards` "parallel items", `group` / `page_break` "these stay
together" / "a new page starts" — on the canvas render each however serves the page, and whatever
this file says the renderer does by itself (sizing answer boxes, ruled lines) is yours to do there.
The content rules in `references/output.md` and the subject file's "Writing lesson.json" mapping
apply in full.

## What the file holds

The JSON holds a `shared` block (content registered once) and a `documents[]` array (each document
authored as free-form `sections` of `blocks`). You compose every page — the lesson plan, the student
materials, the observation template, and any others the lesson needs (e.g. a source packet) —
directly in `documents[]`. Anything that appears on more than one page is registered once in
`shared` under a key you choose and pulled into each document with `{"type": "from_shared", "key":
…}`, so the pages cannot drift apart. A section's `heading` is its title; a block's `label` is a
short lead-in — a label that repeats its section's heading says the same words twice (the task's
name belongs in one of them, not both). Never re-type lesson content into a document from memory:
every document is made from this file, and every later content change goes into it first (SKILL.md
5d). `references/example_lesson.json` is a filled-in worked example.

## Write the complete `lesson.json` (same turn)

Write ONE `lesson.json` with two top-level keys: `shared` and `documents` (in the working folder; on
the Word path the render command copies it beside the documents).

**`shared` is a content registry.** It always carries the lesson identity — `grade`,
`subject`, `duration`, `standard_code`, `standard_text` (and `curriculum`,
`prerequisite_standard`, `smps[]` when applicable). Beyond that, register any content that
appears on more than one page under a key you choose: a problem as `p1`, a source as
`stamp_act_petition`, a data set as `prices_table`. A key's
value can be a string, a single block, a list of blocks, or a faceted object
`{teacher: …, student: …, stimulus: [blocks]}`. On a **student** page, the `student` facet
renders first, then any `stimulus` blocks — the task, then what it works on — and nothing else;
a `student` of `null` means nothing prints there, which is how oral or teacher-led tasks stay
off the worksheet. On a **teacher** page, any `stimulus` blocks render first, then the teacher
facet as plain script, then the student facet as one "Students see" line, so the teacher reads their own script and the exact prompt
students will work from. A teacher facet written as a list of strings renders one move per
line — the glanceable form for any script with more than two moves — and since the student
text prints right beside it, the script points to it ("read the story in the box aloud")
rather than quoting it again. Apart from `standard` (which assembles `standard_code` +
`standard_text` into the target-standard callout), key names carry no special rendering — a
vocabulary list, a misconceptions table, an exit-ticket sort are blocks you compose yourself
(see `references/example_lesson.json` for the patterns).

**`documents[]` is where you compose each page.** Each entry is a full page:
`{id, audience: teacher|student, eyebrow, title, meta?, theme?, sections[{heading, blocks[]}]}`.
Include at minimum:

- `id: "lesson_plan"` (`audience: "teacher"`) — the subject file's section structure.
- `id: "observation_template"` (`audience: "teacher"`) — how-to-use, look-fors,
  misconceptions, a `fill_table` for student notes, and the exit-ticket sort.
- `id: "student_materials"` (`audience: "student"`) — **only when students hold a printed
  page.** A K-2 phonics or oral lesson may have none; a source-heavy lesson may have this AND
  a separate `id: "source_packet"`. The subject file's *Student page layout* gives the
  default skeleton; adapt it to the lesson. If the teacher asked for leveled/tiered student
  materials, label them Group A / B / C (A = below, B = at, C = above grade level) — level
  wording stays in the teacher-facing documents.

Inside any document, pull registered content with `{"type": "from_shared", "key": "…"}` —
the same key on two pages renders the same content (faceted by audience). Adding
`"label": "1"` to a `from_shared` block renders the pulled text as a numbered item on one
line. Within a single document, pull each key once (a reference table, an exit-ticket
protocol, a word list appears in one section only). Content that appears on only one page
can be written inline.

**Schema** — sufficient on its own; do not read any other file for the schema:

```
shared:
  grade, subject, duration, standard_code, standard_text          (required identity)
  curriculum?, prerequisite_standard?, smps[]?
  <any key you choose>: string
                      | block | block[]
                      | {teacher: …, student: … or null, stimulus?: block[]}
  (only `standard` is special — it assembles standard_code+standard_text)
documents[]: {id, audience: teacher|student, eyebrow, title, meta?, theme?, orientation?: landscape,
              sections[]: {heading, color?, blocks[]}}
block types:
  {type: from_shared, key}
  {type: paragraph, text} | {type: labeled, label, text}
  {type: callout, kind: special|student-task|teacher-note|student-note, label, text}
  {type: h2|h3, text} | {type: list, label?, ordered?, items[]}
  {type: phase_header, name, minutes} | {type: cards, items[{title, text}]}
  {type: table|data_table, headers[]?, rows[[]]}
  {type: fill_table, headers[], blank_rows: int, row_height_pt?}
  {type: number_line, min, max, ticks?, marks[]?}
  {type: source_card, title, author?, date?, origin?, excerpt}
  {type: answer_box, height_pt?, ruled?} | {type: page_break}
  {type: group, blocks[]} | {type: columns, left[], right[]}
```

A document may carry `"orientation": "landscape"` for a wide handout (absent = portrait); the Word
renderer ignores it; Design pages are laid out that way.

`references/example_lesson.json` is a filled-in worked example. Keep writing tight; no emoji in JSON
content (what a canvas page adds around it is the canvas's business). The brevity rules in
`references/output.md` are hard requirements for every text field.

**Which block when** — pick by what the content *is*, not how it should look:

| Block | Use it for |
|---|---|
| `callout` `kind: special` | The one anchoring fact per artifact — the target standard. Typically once. |
| `callout` `kind: student-task` | Any task students do: anchor task, exit ticket prompt, a practice problem shown in the plan. |
| `callout` `kind: teacher-note` | An aside the teacher reads but does not say aloud: "don't resolve yet", conferring moves, a watch-for. |
| `list` `ordered: true` | A numbered sequence — the problem set, procedure steps. Unordered otherwise. |
| `list` with `label` | A titled enumeration — several discrete items under one label. |
| `h2` | Sub-sections inside a section — the lesson-sequence phases use `phase_header`, which renders as h2 with minutes; the `minutes` across all phase headers should sum to `shared.duration`. |
| `h3` | A title above one block (a table, a list group, the look-fors). |
| `cards` | 2–4 parallel items of roughly equal length — exit-ticket sort buckets, tier summaries. Never for long or unbalanced items; use a `list` for those. |
| `table` (no `headers`) | Term/definition pairs, label/value reference rows. |
| `table` / `data_table` with `headers` | Real tabular data with column labels (misconceptions, scaffolds, the data set students analyze). `display: "large"` renders cells in big centered type — a word grid young students point to and read. |
| `fill_table` | An organizer students write into — observation log, comparison grid, evidence collector. `rows` as a count gives blank rows; `rows` as a list mixes filled and blank — `[["cap","cape"], [], []]` shows a worked first row, then write-in space, and `[["Shell", "", ""]]` gives a labeled row with blank cells students write in (say what goes in the blank — a ✓, yes/no, a word — in the instruction line above). |
| `number_line` | A drawn number line (`min`, `max`, `ticks`, optional `marks`). `ticks` omitted defaults to 10 evenly spaced segments; `ticks: 0` draws a bare line with only the `min`/`max` end labels and no tick marks, for students to partition themselves. |
| `source_card` | A primary or secondary source excerpt students read: title/author/date + the excerpt text. |
| `answer_box` | Writing space after a task. With no `height_pt` it sizes itself to the grade band (K-2 ~200pt, 3-5 ~150pt, 6-8 ~130pt, 9-12 ~115pt). K-5 boxes draw ruled handwriting lines except in math, which defaults to open space; `ruled: true` draws lines at any grade — the surface for answers of composed sentences — and `ruled: false` gives open space for drawing or model-sketching. A task answered in a `fill_table` or on a `number_line` already has its surface. |
| `group` | Keeps a task's prompt, stimulus, supports, and answer box together so a page break never separates them. |

---

## Word path only — how the renderer reads the file

Read this part on the Word path (`rendering/docx.md`); otherwise skip it.

- A section's `heading` renders as a large title directly above its blocks; a block's `label`
  renders as a bold lead-in on the block itself. Section titles are heading blocks (`h2`/`h3`), not
  bold paragraphs.
- A `paragraph` or `labeled` block is at most 3 sentences. Longer → split it, bullet it, or table
  it.
- Parallel variants (per-group supports, per-phase differentiation, tiered look-fors) go in ONE
  `table` block — rows = phases or features, columns = variants, ≤ ~25 words per cell.
- A `callout` marks the few moments a teacher must not miss; a phase reads as plain script with at
  most one or two callouts. Teacher asides (watch-fors, confer prompts) are `labeled` or
  `instructions` blocks.
- The standard is quoted verbatim once: the target-standard callout, assembled from `shared`.
- Number pairs inside a sentence are plain text ("2 → 10, 5 → 25"); a table is always its own block.
- Print-safety: never markdown pipe tables (use `table`/`data_table`); for number lines use the
  `number_line` block, not a digit string. Anything the teacher displays lives in the lesson plan's
  Materials and phase script; a student page carries only what is printed on it.
- Never write layout code and never edit a generated document directly — every change goes into
  `lesson.json` and is re-rendered (instant). **Do not open, cat, head, or grep the renderer
  scripts** (everything in `scripts/`) — their behavior is fully specified by `rendering/docx.md`;
  reading script source tells you nothing these instructions don't already state.
- Styling: `theme` fields (`primary`, `title_size`, `body_size`) apply to every document. Word
  documents use minimal color so they print cleanly in black-and-white; do not set per-section or
  per-phase colors.

### Supplementary artifacts in their best format (Word path; on the canvas they are more artboards)

The `lesson.json` pipeline is for the lesson's document set: pages a student or teacher
reads or writes on. An artifact whose value depends on its form — exact card
dimensions for cutting, poster-scale type — belongs outside it, as its own file in
whatever format produces the best version (e.g. a print-ready PDF). Your judgment
picks the format; source any shared content from `shared` so pages can't drift, and name
the file in Materials like any other page.

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0

# Output contract — k12-lesson-differentiation

Loaded by `k12-lesson-differentiation` at Step 5, before writing `differentiation.json`.
Every rule here is a hard requirement for the four documents.

## Density rules — hard requirements for every document

Teachers consistently flag dense
walls of text. Structure beats prose:

- A `paragraph` or `labeled` block is at most 3 sentences. Longer → split it, bullet it, or
  table it.
- Bullets are fragments — one idea each, ≤ ~15 words; never chain clauses with semicolons.
- Parallel tier content (Below / At / Above doing the same phase differently) goes in ONE
  `table` block — rows = phases or features, columns = tiers, ≤ ~25 words per cell — never
  three back-to-back multi-sentence paragraphs.
- An aside longer than one sentence (misconception watch-fors, confer prompts, deployment
  guidance) becomes its own `callout` block, not a sentence buried in a paragraph.
- Quote the standard verbatim exactly once (the target-standard callout, from `shared`).
  Everywhere else — prerequisite grounding, forward connections — reference by code plus a
  gist of ten words or fewer; never re-paste full standard text.
- A section that runs past about half a page of continuous prose must be restructured
  (table, bullets, or split into two sections) before rendering.

## Pre-write cross-check

Run ALL checks before calling the render script. Do not render until every item passes.

**O6 — Artifact alignment (both directions):**
1. **Plan → tier documents.** List every task the plan says students do — tier problems/tasks,
   exit ticket, the anchor activity, anything assigned to "early finishers." Each must have a
   printed student-facing block on at least one tier document (the anchor activity on all
   three, via `from_shared: anchor_activity`). A task that exists only as a plan description
   fails.
2. **Tier documents → plan.** For each tier document, list every printed task — each
   problem/task, the extension and each of its printed sub-parts, anything printed on one tier
   only, the exit ticket, "If you finish early," "Reflect." Each must appear in that tier's
   **Worksheet tasks** line in the plan, with its scaffold named (e.g., "P1 (tape diagram +
   sentence support)" not just "P1"). A printed task the plan never names fails — a named
   scaffold the worksheet does not print fails — and so does a plan line naming a task or
   organizer no tier document prints.

Shared content is guaranteed by `from_shared` blocks; the check targets document-specific
blocks and plan prose. Also confirm the exact `shared.standard_code` string appears in each of
the three tier documents' `eyebrow` (`"[Grade] [Subject] · [standard_code]"`) — the standard
must be named on every tier, not only in the teacher plan. Fix mismatches before rendering.

## Classroom-ready (every document)

the tiers run on what the teacher already holds.
Every resource a worksheet or the plan names is a printed block in this package, equipment
the classroom has, or a sourced resource with its access path stated — exact title and
source, a link when you could confirm one. A visual a task depends on prints on the
worksheet that uses it, or the task is rewritten to work from what does print. Anything
harder to get than that stays out unless the teacher steered toward it.

## P8 — Flexible grouping (confirm in teacher plan JSON)
- The `Flexible Grouping` section states the evidence or basis used to assign students to each
  tier (e.g., a specific prior exit ticket, diagnostic score, or "Default profile applied — no
  diagnostic data available"). A blank or generic statement fails.
- The section includes an explicit statement that tier assignments are revisable based on
  formative evidence from THIS lesson (not a standing ability track).

## O4 — Rationale notes (confirm in teacher plan JSON)
- `Why this works (1)` and `Why this works (2)` sections are present and each name a specific
  tier design choice with a stated reason. Generic statements ("scaffolds help learners") fail.
  These sections are required and cannot be dropped to meet page caps — tighten other content
  instead.

### Student-facing language — ALL tier documents

Student pages never use instructional-design terminology. Those are teacher words; on a
worksheet they read as labels about the student, not for the student.

- ❌ "CER" — write the organizer labels out: *Claim / Evidence / Reasoning*. ("Write a CER"
  becomes "Explain your claim with evidence and reasoning".)
- ❌ "sensemaking check", "formative check", "misconception", "scaffold", "tier",
  "differentiation", "anchor task" — use student words: *"Check your thinking"*, *"Try this
  together"*, *"If you finish early"*.
- On a student document the tier is named **Group A** (below), **Group B** (at), or
  **Group C** (above): the `title` carries the group letter per the subject template; the
  `eyebrow` stays `"[Grade] [Subject] · [standard_code]"` with no level wording. Grade-level
  labels are teacher words — the teacher plan's tier labels ("Below (Group A)" etc.) carry
  the association.
- Scaffold prompts get a SHORT student-friendly `h3` on its own line (e.g.
  *"Observe the data first"*, *"Check your thinking"*), then the prompt as a normal
  paragraph below it — never a long bold inline label like
  "**Before Task 2 — sensemaking check:** Complete this sentence…". The subheading names
  what the student does, not the pedagogy behind it.

### Asset framing — below-tier documents

Student-facing language must not signal reduced expectations. Scaffolds appear as natural task
design, not announced supports.

- ❌ "Task 1 (Scaffolded) / Task 2 (Guided) / Task 3 (Independent)" — a student who sees these labels knows they are on the easier version.
- ❌ "Use this if you need it" / "Here is a sentence starter" — names the support as a crutch.
- ❌ Any header, label, or aside that distinguishes scaffolded tasks from unscaffolded ones.
- ✓ The organizer, annotation frame, or sentence support simply appears as part of the task layout.
- ✓ Tasks are numbered without scaffold-level labels.
- ✓ Sentence supports at the top of the document are introduced universally: "You can use these sentence supports:" — not "Use these if you get stuck."

## Accessibility (also black-and-white printing)

Meaning lives in the words, never in color, position, or formatting alone: point students
to "the Evidence column," never "the box on the right." Every write-in space is labeled with what goes in it; anything drawn rather than
written — like a `number_line` — states its task in words. Section titles are heading
blocks (`h2`/`h3`), not bold paragraphs.

---

### 5a. Write the complete `differentiation.json` (same turn)

1. Write `differentiation.json`: top-level `theme`, the **`shared` block** (write this FIRST —
   the identity fields, the standard verbatim, each tier task under its own key (`t1`, `t2`, …),
   the exit ticket, and composed blocks for vocabulary, sentence supports, and misconceptions;
   also `anchor_activity` (early-finisher task in student-facing second person — directions
   only, no rationale) and `reflect_prompt` (the closing reflective question)), and a
   `documents` array with 4 entries: `{"id": "teacher_plan", "audience": "teacher", …}` and
   `{"id": "worksheet_group_a" / "worksheet_group_b" / "worksheet_group_c", "audience": "student", …}`.
   Each document's `sections` follow the subject file's document content templates.

   **Schema** — the complete field skeleton (`blocks` shows one of each type). This is
   sufficient — **do not open, cat, head, or grep the renderer scripts**:

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
                 audience: teacher|student, eyebrow, title, meta,
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

   **`shared` is a content registry.** Register each tier task under its own key (`t1`,
   `t2`, …), the exit ticket as `exit_ticket`, and any other content that appears on more
   than one document, under keys you choose. A key's value can be a string, a composed
   block (a vocabulary `table`, a misconceptions `table`, sentence-support text with its writing space), or a
   faceted object `{teacher: …, student: …}` — on a **student** page only the `student`
   facet renders; on the **teacher** page both render (the teacher facet as a teacher-note,
   then the student facet as a "What students see" callout). Key names carry no special
   rendering — compose vocabulary, misconceptions, and sort buckets as blocks yourself
   (`references/example_differentiation.json` shows each pattern).

   Keep writing tight; no emoji in JSON content.
   The density rules above are hard requirements for every text field.
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
   Tabular content — data tables, "complete the table" tasks, row-and-column organizers — must
   be a `{"type": "table", "headers": [...], "rows": [[...]]}` block (a row of empty strings
   renders as ruled writing space). Never draw a table inside a `text` field: markdown pipe
   rows, box-drawing characters, ASCII art, and symbol glyphs (■, □) print literally on the
   page and fail print-safety. Never write bullet characters (•, -) inside a `text` string
   — use a `list` block; a paragraph collapses line breaks and the bullets run together
   into one line. Use `workspace` blocks for writing space — they render as
   open whitespace sized by grade automatically (lower grades get much more room, and K–5
   prose answers get ruled lines; math work space stays open for drawing). Set `height_pt`
   only when a task needs more than the default: 130–150 for full written explanations and
   exit tickets, 90–110 for short extension questions. Empty table cells are writing space
   and get a grade-banded minimum height automatically — don't set `empty_row_height_pt`
   below ~70pt for prose rows. This applies to
   every prose field in all four documents.
2. The three tier documents (in the same `documents` array) differ ONLY in their scaffolding
   and extension blocks (R6).
   **Every tier document pulls task text with `from_shared` blocks — never re-type, reword,
   or split task text into a document's own blocks** (so the plan and all three tiers stay
   verbatim-consistent — reworded tasks drift apart in revision). Each task has its own
   `shared` key, pulled one at a time so scaffolds sit with their task:
   `{"type": "from_shared", "key": "t1", "label": "1"}` renders Task 1 as a numbered item;
   follow each task — and every other prompt students answer (the exit ticket, Reflect,
   If you finish early, a tier-only extension) — with a `workspace` block.
   The required order within the section is strict: for each task N — at most ONE
   scaffold block for task N (merge multiple supports into one labeled block; never two
   "Before Task N" blocks), then the task via its key. A scaffold must NEVER appear
   after its target task, and nothing sits between a scaffold and its task.
   That is how the R7 fade pattern is expressed — Task 1 gets a scaffold block, Task 2's is
   lighter, later tasks have none. A tier-only task (the Above extension, an Above-only
   sub-question) is its own headed block — never an edit to shared task text. Below-tier scaffolds follow R4; the Above-tier extension passes R7's quality
   test. Asset framing rules (above) apply to every student-facing block.

### 5d. Revisions — one edit, every artifact stays in sync

Make **targeted edits to `differentiation.json`**, then re-render all four documents (instant).
Rules that keep the artifacts consistent:

- If the change touches shared content (context, numbers, tasks, exit ticket, vocabulary,
  sentence supports, misconceptions), edit it **in `shared`** — it propagates to the teacher
  plan and every tier document automatically.
- **Consistency sweep after any context/number/task change:** after editing `shared`, re-read
  every prose block in all four documents' `sections` and update every sentence that still
  mentions the old context, names, or numbers. No artifact may reference the replaced content
  anywhere — stale prose is the most common consistency failure.
- A change aimed at one tier (e.g. "more scaffolding for below", "harder extension") goes in
  that tier document's blocks — never by forking shared content. Scaffold changes must keep
  the subject file's R4 rules and R7 fade pattern.
- Styling: top-level `theme` applies to all four documents; per-document `theme` overrides
  stay available.

### 5e. Fallback — bespoke generation code (exception path only)

Only if the user explicitly asks for an artifact or layout the bundled renderer cannot express
(a different document type, landscape poster, slide deck, etc.): write generation code from
scratch for that artifact. Source its content from the same `differentiation.json` (especially
`shared`) so it stays consistent with the other artifacts. Tell the user this path is slower.

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0

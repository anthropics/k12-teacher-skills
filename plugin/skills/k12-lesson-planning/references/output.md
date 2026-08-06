<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->

# Output contract — k12-lesson-planning

Loaded by `k12-lesson-planning` at Step 5, before writing `lesson.json`. Every rule here
is a hard requirement for the documents.

## Density rules — hard requirements for every document

Every document is clear, brief,
and easy to skim. Include what a teacher needs to teach it; leave out what merely
demonstrates rigor. Headings use sentence case. Structure beats prose:

- A `paragraph` or `labeled` block is at most 3 sentences. Longer → split it, bullet it, or
  table it.
- Write like a colleague's note: plain, direct sentences built from commas and periods.
- Bullets are fragments — one idea each, ≤ ~15 words; never chain clauses with semicolons.
- Parallel variants (per-group supports, per-phase differentiation, tiered look-fors) go in
  ONE `table` block — rows = phases or features, columns = variants, ≤ ~25 words per cell —
  never back-to-back multi-sentence paragraphs.
- A callout marks the few moments a teacher must not miss — a warning ("do not resolve the
  debate yet"), a collect-before-moving-on, the one make-or-break move of a phase. A page
  where everything is boxed highlights nothing: a phase reads as plain script with at most
  one or two callouts. Teacher asides (watch-fors, confer prompts) are `labeled` or
  `instructions` blocks.
- Each instruction lives in exactly one place. A phase's opening prose and its blocks divide
  the work between them — the prose sets up, the blocks carry the content; neither repeats
  the other.
- Quote the standard verbatim exactly once (the target-standard callout, from `shared`).
  Everywhere else — prerequisite grounding, forward connections — reference by code plus a
  gist of ten words or fewer; never re-paste full standard text.
- A section that runs past about half a page of continuous prose must be restructured
  (table, bullets, or split into two sections) before rendering.

## Everything matches — hard requirements for every document

A teacher trusts the package
because every part agrees with every other part:

- The materials list and the phases agree exactly: every listed item is used by a named
  phase, and every counted set matches its enumeration ("Picture cards, 18" lists 18 words).
- **Classroom-ready:** the lesson runs on what the teacher already holds. Every Materials
  item is a page this package ships, equipment the classroom has, or a sourced resource
  with its access path stated — exact title and source, a link when you could confirm one.
  Anything harder to get than that stays out of the lesson unless the teacher steered
  toward it. A printable the lesson depends on ships with the package — as lesson pages
  when the document set expresses it, or as its own file in the format that renders it
  best (5e).
- A task worded in two places (plan's "Students see" and the student page) uses identical
  wording in both.
- Student tasks match the skill the standard names, in both directions. Decoding, spelling,
  and writing skills happen on paper — students read and write real words on a student page.
  Listening and speaking skills get spoken, pointed, sorted, drawn, or circled responses.
  The lesson's scope statement binds every task that follows it.
- Scripts and worked examples are final say-aloud text: every step decided before it lands
  on the page, exactly what the teacher says.
- Exit-ticket sort buckets partition the answers: each example response fits exactly one
  bucket, and equivalent forms of one answer (17 + 24 = ? and 24 + 17 = ?) sit in the same
  bucket together.
- An answer space mirrors its ask: rows match the count requested, and every box sits under
  a prompt naming what goes in it.
- Number pairs inside a sentence are plain text ("2 → 10, 5 → 25"); a table is always its
  own block.

## Reading level and workload

Student-facing text reads at the students' reading level —
which the teacher may state separately from the grade ("my 6th graders read at a 2nd–4th
grade level" means grade-6 content carried in sentences a 2nd–4th grade reader can read:
short sentences, everyday words, one instruction at a time). Size the student work to the
class period: a typical student finishes the worksheet in the minutes its phase allows.
Say "home language," not a specific language, and print translations only into a language
the teacher has named.

**Sentence supports** are plain text where students write: a starter to begin from
("One central idea is…") or a fill-in frame with blanks sized for the student's handwriting.
A support helps the student start, not answer — it never pre-fills what the task asks for.
Place each one on the specific task whose writing move is hardest — including the
explain-why beside a math equation — never one bank copied across problems. K-2 students
and multilingual learners get a support on every task that asks for composed sentences.
Tasks that take only a number, a single word, or a drawing need none.

**Spell out framework names** in every teacher-facing document — *Science and Engineering
Practice*, not bare *SEP* — a teacher should never need to look up an acronym.

## Document integrity

Every document is finished prose a teacher hands out or works from:

- Every in-document reference points at something that exists in the package: "jot it in the
  table below" means that table is on the page; an exit ticket collected separately prints as
  its own piece; a reference table uses the same numbers as the problems it supports.
- Materials and the lesson match both ways: each listed item is used somewhere in the
  lesson, every item any section sends students to — phases and extensions alike — appears
  in Materials, and anything students read is printed in the package or named by its exact
  title. Offers and pointers to the chat conversation stay out
  of documents entirely.
- Lessons are light on materials: the default kit is what every classroom has (board,
  projector, paper) plus the pages this lesson ships. A separate printable or manipulative
  earns its place only when the activity genuinely needs it — and the same thinking work on
  the worksheet usually serves. When a printable earns it (cards, mats, a template), ship it
  with the package (5e picks the format); equipment a classroom owns is simply listed.
- Phase minutes include the transitions they cause (handing out, regrouping, collecting), at
  a pace real students of this grade manage, and the phases sum to exactly the stated
  period — transition time lives inside the phases, never as invisible buffer.
- Teacher notes read as finished sentences. A predicted error names one specific wrong answer
  a real student would produce.
- Verify every computation by working it — answer keys, worked examples, and any quantitative
  chain the lesson builds on (an energy pyramid's levels, a ratio table's entries, a coin
  total) produce the numbers the materials state.

## Accessibility (also black-and-white printing)

Meaning lives in the words, never in color, position, or formatting alone: point students
to "the Evidence column," never "the box on the right." Every write-in space is labeled with what goes in it; anything drawn rather than
written — like a `number_line` — states its task in words. Section titles are heading
blocks (`h2`/`h3`), not bold paragraphs.

### 5a. Write the complete `lesson.json` (same turn)

Write ONE `lesson.json` with two top-level keys: `shared` and `documents`.

**`shared` is a content registry.** It always carries the lesson identity — `grade`,
`subject`, `duration`, `standard_code`, `standard_text` (and `curriculum`,
`prerequisite_standard`, `smps[]` when applicable). Beyond that, register any content that
appears on more than one page under a key you choose: a problem as `p1`, a source as
`stamp_act_petition`, a data set as `prices_table`. A key's
value can be a string, a single block, a list of blocks, or a faceted object
`{teacher: …, student: …, stimulus: [blocks]}`. On a **student** page, only the `student`
facet (after any `stimulus` blocks) renders — a `student` of `null` means nothing prints
there, which is how oral or teacher-led tasks stay off the worksheet. On a **teacher** page,
both facets render: the teacher facet as plain script, then the student facet as one
"Students see" line, so the teacher reads their own script and the exact prompt
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
documents[]: {id, audience: teacher|student, eyebrow, title, meta?, theme?,
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

`references/example_lesson.json` is a filled-in worked example. Keep writing tight; no emoji
in JSON content. The density rules above are hard requirements for every text field.
Print-safety: never markdown pipe tables (use `table`/`data_table`); for number lines use
the `number_line` block, not a digit string. The renderer cannot draw images — anything the
teacher displays (a video, photo, projected image, chart) lives in the lesson plan: name it
in Materials and in the phase script that uses it. A student page carries only what is
printed on it.

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

### 5e. Supplementary artifacts in their best format

The `lesson.json` pipeline is for the lesson's document set: pages a student or teacher
reads or writes on. An artifact whose value depends on its form — exact card
dimensions for cutting, poster-scale type — belongs outside it, as its own file in
whatever format produces the best version (e.g. a print-ready PDF). Your judgment
picks the format; source any shared content from `shared` so pages can't drift, and name
the file in Materials like any other page.

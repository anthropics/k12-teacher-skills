---
name: k12-lesson-planning
description: >
  Creates a lesson plan, student-facing materials, and observation template. Load this skill BEFORE asking the teacher any clarifying question about grade, subject, topic, standard, or timing. Use when a K-12 teacher needs a math, ELA, science, or social studies lesson built from scratch — even if grade, subject, or topic isn't yet stated. Do NOT load for grading, a rubric, assessment feedback, a quiz, or a standards lookup — answer those directly. Triggers on explicit requests (lesson plan, mini-lesson, unit plan, daily plan) and implicit teacher intent: "I'm teaching long division to 5th graders," "need to teach photosynthesis tomorrow." Core signal: teacher needs new instructional content created. A new lesson that asks for differentiated, tiered, or leveled materials is still ONE planning request — this skill produces those materials inside the lesson package; do not also invoke k12-lesson-differentiation. Not for differentiating an existing lesson (use k12-lesson-differentiation) or passage rewrites.
license: Complete terms in LICENSE
---

<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->

# K-12 Lesson Planning

Produces a teacher-ready, standards-aligned lesson plan + student-facing materials + teacher
observation template as editable Word documents in a single output turn, rendered from one material-source JSON via
bundled scripts. Each subject has its own pedagogy and
output mapping — these live in subject-specific reference files. This skill routes to the
right one. Works with or without the Learning Commons Knowledge Graph.

"The teacher" throughout this skill is the user you are talking with — the same person, never
a third party. "Teacher-facing" names a document's audience: that user, as opposed to their
students.

---

## Keeping the teacher posted

Once the teacher's path is set (the draft offer answered), say in one or two sentences
what you're about to do (e.g. *"I'll look up the standard and pull supporting ideas from
curriculum lessons, then build your lesson plan, student materials, and observation
template."*).

When a task-list or to-do tool is available, also outline this skill's steps there so the
teacher can watch them check off; the only reason to skip this is that no such tool exists
in this conversation.

Teacher language only — name what the teacher is getting, never tool names, file names,
"JSON", or "rendering".

---

## Step 0 — Route (silent, before anything else)

1. **Subject.** Determine the subject of the requested lesson from the prompt and any prior
   conversation:

   - **math** — arithmetic, fractions, geometry, algebra, calculus, statistics, CCSS-M codes, IM (Illustrative Mathematics)
   - **ela** — reading, writing, phonics, literature, comprehension, vocabulary, CCSS-ELA codes (RL/RI/RF/W/L)
   - **science** — phenomena, NGSS Performance Expectations, biology/chemistry/physics/earth science, OpenSciEd
   - **social_studies** — history, civics, geography, economics, C3 inquiry arc, state social-studies standards

   Then read the matching reference file NOW:

   - math → `references/math.md`
   - ELA → `references/ela.md`
   - science → `references/science.md`
   - social studies → `references/social_studies.md`

   **Loading the matching reference file is mandatory.** Drafting a lesson without first
   reading the subject reference is a critical failure. The reference file carries the
   complete subject-specific instructions: clarify priorities, curriculum branching,
   grade-band structures, section structure, non-negotiables, and the lesson.json mapping.
   Treat the loaded reference as your full skill instructions for this turn. If the subject
   is genuinely ambiguous or the prompt spans multiple subjects, ask about it
   in Step 1.

2. **Curriculum.** If the teacher names or implies a curriculum (Illustrative Mathematics,
   OpenSciEd, …), the subject file's curriculum branch covers it — each subject
   file carries its curriculum's structures and language inline (curriculum and subject are
   1:1: IM→math, OpenSciEd→science). If they use a curriculum the subject
   file doesn't cover, follow its "no curriculum named" path and do not fake
   curriculum-specific terminology.
3. **Connector.** Check whether the Learning Commons Knowledge Graph tools (e.g.
   `find_standard_statement`) are available in this conversation. This decides which path
   Step 2 takes. The skill is fully functional without the connector.

---

## Step 1 — Clarify

Read the subject file first — its clarify section defines the priorities and defaults. We
usually ask 0–2 clarifying questions — your judgment on what's relevant; the subject
file's priorities rank which missing answers matter most. Apply the defaults silently for
everything you don't ask about.

The **draft offer** (see *Step 4 — The draft offer* below) travels with this message's questions
as its own separate question — output logistics, not lesson content, so it doesn't count
toward the 0–2. When nothing needs clarifying, the offer is asked on its own.

---

## Step 2 — Ground in standards

**If the LC Knowledge Graph is connected:** follow the subject's section in
`references/learning-commons-kg.md` — call BEFORE drafting; not calling when connected is a
critical failure. Extract only what each call specifies, then proceed directly to Step 3 — do
not summarize findings in chat.

**If not connected:** draft from best knowledge and add this footer to the lesson plan:
*"Generated without the Learning Commons Knowledge Graph. Standards and misconceptions reflect
general best practice."* Do not invent KG citations or attribute content to curriculum
materials you have not seen.

---

## Step 3 — Build the lesson

Follow the subject file's build section: curriculum branching, grade-band structure, section
structure, and non-negotiables. Respect the **Copyright guardrail** below — never reproduce
curriculum student-facing text verbatim.

---

## Copyright guardrail

Always write original content. KG curriculum materials inform structure, scope, text
selection, phenomenon selection, problem context, and lesson-arc design only — never
reproduce student-facing text, teacher notes, comprehension questions, investigation
prompts, discussion questions, activity narratives, or problem contexts verbatim from KG
curriculum materials.

If the loaded reference identifies a source curriculum (e.g., IM for math, OpenSciEd for science) and the teacher is not curriculum-confirmed for it, never name
that curriculum anywhere in the output or in any chat message — not in headers, footnotes,
rationale sections, facilitation notes, or your message presenting the artifacts. The KG
data informs the design without being cited.

---

## Step 4 — The draft offer

The teacher gets the choice of a fast draft before the build. The offer is
asked the same way as the clarify questions — through the structured question tool when
one is available, in chat otherwise — as its own separate question, batched with Step 1's
questions when there are any and asked on its own when there aren't.

- Question: *Should I go ahead and build the full classroom-ready packet (lesson plan + student materials, as
  editable Word docs), or do you want to see a quick draft first?*
- Options: **Go ahead and build it** · **Quick draft first** — the lesson at a glance,
  right here in chat

**The full packet is the default.** Declining, not answering, or anything like "proceed
with your defaults" runs Steps 2–3 and goes straight to Step 5; the draft happens only on
a clear yes.

**The draft (on a yes) is built on Steps 2–3, never instead of them.** Run Step 2 in
full — every KG call, exactly as written — and Step 3 before sketching anything. A draft
sketched without the Step 2 grounding is a critical failure, the same failure as skipping
the KG on the full build. Then present the lesson in chat — the draft is chat text only;
rendering happens at Step 5 once the teacher approves. Show:

- one line naming the grade, topic, and the standard the lesson is anchored to (code plus
  a gist of ten words or fewer);
- a summary of at most 3 sentences (what students do and why it works for this class);
- the sequence as one bullet per phase (name, minutes, one line of what happens);
- the student work at a glance — the actual tasks students will do, enough for the
  teacher to skim and judge coverage;
- what the lesson assumes students already know — the prerequisite skills or key
  vocabulary in play — so the teacher can catch a mismatch with where their class is;
- the exit ticket

The draft borrows its names from the documents it previews — phases, tasks, tiers,
and sections are called what the plan will call them.

Afterwards, ask what's next — a structured question, two options:

- **Make changes** — adjust any part of the draft
- **Create the materials** — lesson plan, student materials, and observation template, as
  editable Word documents

Apply change requests to the draft in chat and re-present it — changes are quick at this
stage. Step 5 runs in the turn the teacher gives the go-ahead ("Create the materials",
"proceed with your defaults", or similar).

---

## Step 5 — Output (one turn)

Runs immediately when the teacher chose the full packet, or in the turn the draft is
approved.

The artifacts are rendered by bundled scripts from **one material-source `lesson.json`**. The JSON
holds a `shared` block (content registered once) and a `documents[]` array (each document
authored as free-form `sections`). A section's `heading` renders as a large title directly
above its blocks; a block's `label` renders as a bold lead-in on the block itself. A label
that repeats its section's heading prints the same words twice in a row — labels carry what
the heading doesn't (the task's name belongs in one of them, not both). You
compose every page — the lesson plan, the student
materials, the observation template, and any others the lesson needs (e.g. a source packet)
— directly in `documents[]`. Anything that appears on more than one page is registered once
in `shared` under a key you choose and pulled into each document with
`{"type": "from_shared", "key": …}`, so the pages cannot drift apart.

Never write layout code, never re-type lesson content into another format, and never edit a
generated document directly — every change goes into `lesson.json` and is re-rendered
(re-rendering is instant). **Do not open, cat, head, or grep the renderer scripts** — their
behavior is fully specified by the commands and output paths in §5a–5d, and
`references/example_lesson.json` is the complete schema. Reading script source tells you
nothing this file doesn't already state.

**Plain language with the teacher.** The machinery above is invisible to the teacher: never
mention JSON, HTML, schemas, scripts, rendering, file names (`lesson.json`), or code in any
teacher-facing message — and never link or name the `.html` files the render command also
writes. Say *"Here's your lesson plan — the student materials and observation template are on
their way"*, not *"I've rendered lesson.json"*. The only format word in your prose is
"Word document". This
applies to every turn: presenting artifacts, the satisfaction ask, revision summaries, and
error messages (if generation fails, say the documents couldn't be created — not that a
script or JSON failed).

**Density rules — hard requirements for every document.** Every document is clear, brief,
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

**Everything matches — hard requirements for every document.** A teacher trusts the package
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

**Reading level and workload.** Student-facing text reads at the students' reading level —
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

**Document integrity.** Every document is finished prose a teacher hands out or works from:

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

### 5b. Render every Word document — one command, same turn

```bash
bash scripts/render_all.sh lesson.json "$OUTPUT_DIR"
```

This writes one editable `.docx` per `documents[]` entry, named by `id` (e.g.
`$OUTPUT_DIR/lesson_plan.docx`, `student_materials.docx`, `observation_template.docx`,
`source_packet.docx`), plus `.html` and `lesson.json` working files. Render straight into
`$OUTPUT_DIR` and leave everything the script writes in place — later revision turns
re-render from the working files even though the teacher only sees the Word documents. Then list `$OUTPUT_DIR`
and confirm every document has both its `.docx` and `.html`; if either is missing or tiny,
rerun the script. Present the Word documents to the teacher together — attach the lesson plan
last so it lands on top (chat surfaces stack newest-first). If there is no `student_materials`
document, say so plainly ("This lesson is oral, so there's no student handout — students will
work with …"). If the script errors, fix `lesson.json` (it is almost always malformed JSON)
and rerun. If file generation fails entirely, say so clearly — do not silently fall back to a
chat-only delivery.

### 5c. The satisfaction ask + iteration options (every output turn)

End the turn with EXACTLY ONE closing message that does three things, in this order:

1. **If Materials names equipment the classroom has that a paper version can stand in
   for** — coins, blocks, dice, a hundred chart — lead with a bolded offer to print it:
   *"**This lesson uses base-ten blocks — want me to make a printable set in case
   yours are short?**"* Anything whose content this lesson wrote — word cards, a
   source excerpt, a sorting mat with this lesson's categories — already ships with
   the package.
2. Asks whether the teacher is satisfied with **every artifact produced** or wants changes —
   e.g. *"Take a look at the lesson plan, student materials, and observation template — anything
   you'd like me to adjust?"* Do not skip the ask.
3. Offers 3–4 high-leverage, **specific** iteration options customized to the subject and
   topic. Do not write "let me know if you want changes" — that's a non-offer. For example,
   for a 3–5 ELA reading comprehension lesson: *"Would you like to (1) add more scaffolds for
   English learners, (2) differentiate by proficiency level, or (3) adapt to be specific to
   your state standards?"*

### 5d. Revisions — one edit, every artifact stays in sync

Make **targeted edits to `lesson.json`**, then re-render every document (instant). Rules that
keep the artifacts consistent:

- If the change touches content registered in `shared` (a problem, a source, the exit ticket,
  vocabulary, look-fors, the phenomenon/context/numbers), edit it **in `shared`** — every
  document that pulls that key updates automatically.
- **Consistency sweep after any context/number/task change:** after editing `shared`, re-read
  every prose block in every `documents[]` entry and update every sentence that still mentions
  the old context, names, or numbers. When you are done, no document may reference the
  replaced content anywhere — stale prose is the most common consistency failure.
- A change aimed at one document (e.g. "more workspace on the worksheet", "add a column to the
  observation grid") goes in that document's `sections` — never by forking a `shared` key into
  two variants.
- Styling: `theme` fields (`primary`, `title_size`, `body_size`) apply to every artifact.
  Artifacts use minimal color so they print cleanly in black-and-white; do not set
  per-section or per-phase colors.

### 5e. Supplementary artifacts in their best format

The `lesson.json` pipeline is for the lesson's document set: pages a student or teacher
reads or writes on. An artifact whose value depends on its form — exact card
dimensions for cutting, poster-scale type — belongs outside it, as its own file in
whatever format produces the best version (e.g. a print-ready PDF). Your judgment
picks the format; source any shared content from `shared` so pages can't drift, and name
the file in Materials like any other page.

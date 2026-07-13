---
name: k12-lesson-differentiation
description: Adapts an existing K-12 lesson (math, ELA, science, or social studies) for students at different proficiency levels (below / at / above grade level). Load this skill BEFORE asking the teacher any clarifying question about the lesson, tiers, or student levels. Triggers on explicit asks to differentiate, tier, or scaffold a lesson, and on implicit signals like "my students are at different levels". Produces 1 teacher-facing differentiation plan + 3 student-ready tier documents as editable Word documents in a single output turn, rendered from one material-source JSON via bundled scripts (shared content is written once so tiers cannot drift). Uses the Learning Commons Knowledge Graph when connected; works without it. This skill adapts a lesson the teacher brings or names. Not for creating a new lesson from scratch — a new-lesson request that asks for differentiated or leveled materials is k12-lesson-planning's job, one package. Not for grading, rubrics, assessment feedback, or quizzes.
license: Complete terms in LICENSE
---

<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->

# K-12 Lesson Differentiation

Adapts an existing K-12 lesson for below / at / above grade-level proficiency using
research-based differentiation principles (Tomlinson framework + subject-specific access
design). Works with or without the Learning Commons Knowledge Graph connector.

"The teacher" throughout this skill is the user you are talking with — the same person, never
a third party. "Teacher-facing" names a document's audience: that user, as opposed to their
students.

---

## Keeping the teacher posted

Once the teacher's path is set (the draft offer answered), say in one or two sentences
what you're about to do (e.g. *"I'll read your lesson, ground it in the standard and
curriculum materials, design the three tiers, and build the worksheets."*).

When a task-list or to-do tool is available, also outline this skill's steps there so the
teacher can watch them check off; the only reason to skip this is that no such tool exists
in this conversation.

Teacher language only — name what the teacher is getting, never tool names, file names,
"JSON", or "rendering".

---

## Step 0 — Route (silent, before anything else)

1. **Subject.** Detect math / ELA / science / social studies from the source lesson or the
   request, then read the matching reference file NOW:

   - math → `references/math.md`
   - ELA → `references/ela.md`
   - science → `references/science.md`
   - social studies → `references/social_studies.md`

   **Loading the matching reference file is mandatory.** It carries the pedagogy for Steps 1
   and 3 (source-lesson identification, curriculum detection, the eight differentiation rules
   R1–R8, the document content templates, and the differentiation.json mapping).
   Differentiating without first reading the subject reference is a critical failure on par
   with skipping the Knowledge Graph.
2. **Curriculum.** The subject file's "Identify the source lesson" section includes curriculum
   detection (Illustrative Mathematics / OpenSciEd). When confirmed, use that
   curriculum's discourse language and structures in the teacher plan, per the subject file.

   **Curriculum is confirmed when:** the teacher explicitly names it, OR the uploaded source
   lesson references it (a lesson from an IM unit or an OpenSciEd unit
   counts — the upload is implicit confirmation).

   **If curriculum is NOT confirmed** (not detectable from upload or link, no explicit mention):
   never name a specific module, unit number, lesson number, or proprietary routine name anywhere
   in the output OR in any chat message — even if you recognize the routine from training.
   Describe the instructional move in your own generic terms ("a compare-strategies
   discussion", not the routine's trademarked name). This is a hard rule; violating it fails P9,
   and chat messages count. See **Copyright guardrail** (after Step 3) for the companion rule on
   verbatim reproduction.
3. **Connector.** Check whether the Learning Commons Knowledge Graph tools (e.g.
   `find_standard_statement`) are available in this conversation. This decides which path
   Step 2 takes. The skill is fully functional without the connector.

4. **State.** Before any KG call, scan the conversation and any uploaded source lesson for
state signals and store as `state`:
   - Teacher says "I teach in [state]," "I'm in [state]," or "We're in [state]"
   - Standard codes in the prompt or source lesson follow a state-specific format:
     TEKS 1xx.x.x → Texas; SOL → Virginia; OAS/PASS → Oklahoma; MA → Massachusetts;
     CA/HSS or CA/CCSS → California; other state-prefixed codes → check state
   - Source lesson URL includes a state agency domain (tea.texas.gov, etc.)

   If state found: store `state = [state name]`. Pass as `jurisdiction="<state>"` in every
   `find_standard_statement` call in Step 2. Use state framework codes (not national proxies)
   in all output.

   If state not found:
   - for science, math, or ELA, proceed with national defaults (CCSS for math/ELA, NGSS for science). Add this single footer line to the teacher plan:
   *"Standards applied using [CCSS / NGSS] — if you're in Texas, Virginia,
   Oklahoma, or another state with a distinct framework, share your state and I'll re-anchor."*
   - for social studies, ask the teacher what state they teach in before proceeding.



---

## Step 1 — Identify the source lesson

Follow the subject file's source-lesson section: Scenario A (lesson exists earlier in this
conversation — use it directly, do not re-ask), Scenario B (teacher uploads a lesson — read it
first; if unreadable, say so and ask to re-share, never silently fabricate), Scenario B2
(teacher links a lesson by URL — fetch and read it; if the fetch fails,
ask them to paste or upload; fetching completes Step 1 only — the KG calls in Step 2 are still
mandatory), Scenario B3 (math or science only — teacher names a curriculum lesson by position or title —
e.g. "IM Grade 6, Unit 2, Lesson 3" or "the OpenSciEd lesson on ecosystem dynamics" — Step 1
is complete; proceed directly to Step 2 where `find_curriculum_lessons` will retrieve the
lesson materials; do NOT ask the teacher to upload or link the lesson), or Scenario C (no source lesson present —
ask the subject file's clarifying question before proceeding).

A fetched link lands in the conversation whole, so a document bigger than one lesson
(a module or unit teacher edition) will not fit. When a link points at one, work from
what the request itself tells you about the lesson and confirm the specifics with the
teacher — topic, grade, and standard carry enough to build from, the same way Scenario C
proceeds after its clarify.

**Learner needs check (silent, runs every time):** Before generating, scan the conversation
for any mention of ELL levels, WIDA levels, IEP goal areas, 504 accommodations, or specific
student needs. If found, incorporate into the tier design — especially the Below tier.
Say "home language," not a specific language, unless the teacher names one.

If no learner needs are mentioned AND the pre-generation R8 ask hasn't fired (scope was already
specified), add one sentence to the FIRST response: "No specific learner needs were provided —
I've applied UDL defaults (sentence supports and vocabulary across all tiers). Share any ELL
levels, IEP goals, or specific student data and I'll adjust."

This check must run even when scope is specified. Learner variability information should be
captured before generation, not after.


---

## Step 2 — Ground in standards

**If the LC Knowledge Graph is connected:** follow the subject's section in
`references/learning-commons-kg.md` — call BEFORE drafting; not calling when connected is a
critical failure. This applies no matter how the source lesson was obtained — uploaded, pasted,
or fetched from a URL. Retrieving the lesson never satisfies this step.

**If not connected:** proceed from best knowledge and add this footer to the teacher plan:
*"Generated without the Learning Commons KG. Standard text, prerequisite grounding, and
misconceptions reflect general best practice."* Do not invent KG citations.

---

## Step 3 — The differentiation rules

Apply **all eight rules (R1–R8)** from the subject file to every differentiated lesson. The
rules are subject-specific (scaffold types, tier entry points, extension quality tests differ
by subject) but their structure is shared: output structure (R1), standard scope preservation
(R2), tier entry points (R3), below-level scaffolds with a density cap (R4), required
pedagogical infrastructure (R5), invisible modifications (R6), within-level progressive
scaffolding (R7), and scope/defaults (R8).

---

## Copyright guardrail

Always write original content. When the source lesson draws from a named curriculum (IM,
OpenSciEd), use it to understand structure, scope, task context, and standards
alignment only — never reproduce student-facing text, activity narratives, investigation
prompts, comprehension questions, or problem contexts verbatim from curriculum materials.
Each subject reference file carries a **Copyright** line with subject-specific details.

If curriculum is NOT confirmed (see Step 0.2 detection rules), never name a specific
curriculum, module, unit number, lesson number, or proprietary routine name anywhere in the
output or in any chat message — even if recognizable from training. The source lesson and
KG data inform the design without being cited. See Step 0.2 for the full rule (P9).

---

## Step 4 — The draft offer

The teacher gets the choice of a fast draft before the build. The offer is
asked the same way as the clarify questions — through the structured question tool when
one is available, in chat otherwise — as its own separate question, batched with whatever
you ask before Step 2 (state, source lesson, learner needs) and asked on its own when
nothing else needs asking.

- Question: *Should I go ahead and build the full classroom-ready set (teacher plan + three tier documents, as
  editable Word docs), or do you want to see a quick draft first?*
- Options: **Go ahead and build it** · **Quick draft first** — what changes for each
  tier, right here in chat

**The full set is the default.** Declining, not answering, or anything like "proceed with
your defaults" runs Steps 2–3 and goes straight to Step 5; the draft happens only on a clear yes.

**The draft (on a yes) is built on Steps 2–3, never instead of them.** Run Step 2 in
full — every KG call, exactly as written — and Step 3 before sketching anything. A draft
sketched without the Step 2 grounding is a critical failure, the same failure as skipping
the KG on the full build. Then present the design in chat — the draft is chat text only;
rendering happens at Step 5 once the teacher approves. Show:

- one line reading back the source lesson, standard, and grade;
- for each tier (below / at / above), 2–3 bullets on what changes and why;
- the student work at a glance — each tier's actual tasks, enough for the teacher to
  skim and judge coverage;
- one line on what every tier shares — the essential question or core task — and the
  regroup rule

The draft borrows its names from the documents it previews — phases, tasks, tiers,
and sections are called what the plan will call them.

Afterwards, ask what's next — a structured question, two options:

- **Make changes** — adjust any tier or the shared task
- **Create the materials** — teacher plan and the three tier documents, as editable Word
  documents

Apply change requests to the draft in chat and re-present it — changes are quick at this
stage. Step 5 runs in the turn the teacher gives the go-ahead ("Create the materials",
"proceed with your defaults", or similar).

---

## Step 5 — Output (one turn)

Runs immediately when the teacher chose the full set, or in the turn the draft is
approved.

Four artifacts — **1 teacher-facing plan + 3 student tier documents (below / at / above)** —
are all rendered by a bundled script from **one `differentiation.json` (the material source)**. Anything that
appears in more than one artifact (standard, problem/task set, exit ticket, vocabulary,
sentence supports, misconceptions) lives ONCE in the JSON's `shared` block and is pulled into
each document with `{"type": "from_shared", "key": …}` blocks, so the teacher plan and the
tier documents cannot drift apart — and R6 (same context, same core tasks across tiers) is
enforced structurally.

Never write layout code, never re-type content into another format, and never edit a generated
document directly — every change goes into `differentiation.json` and is re-rendered
(re-rendering is instant).

**Plain language with the teacher.** The machinery above is invisible to the teacher: never
mention JSON, HTML, schemas, scripts, rendering, file names (`differentiation.json`), or code
in any teacher-facing message — and never link or name the `.html` files the render command
also writes. Say *"Here's your differentiation plan — the three tier documents are on their
way"*, not *"I've rendered differentiation.json"*. The only format word in your prose is
"Word document". This applies to every
turn: presenting artifacts, the satisfaction ask, revision summaries, and error messages (if
generation fails, say the documents couldn't be created — not that a script or JSON failed).

**Density rules — hard requirements for every document.** Teachers consistently flag dense
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

**Pre-write cross-check — run ALL checks before calling the render script. Do not render until every item passes.**

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

**Classroom-ready (every document):** the tiers run on what the teacher already holds.
Every resource a worksheet or the plan names is a printed block in this package, equipment
the classroom has, or a sourced resource with its access path stated — exact title and
source, a link when you could confirm one. A visual a task depends on prints on the
worksheet that uses it, or the task is rewritten to work from what does print. Anything
harder to get than that stays out unless the teacher steered toward it.

**P8 — Flexible grouping (confirm in teacher plan JSON):**
- The `Flexible Grouping` section states the evidence or basis used to assign students to each
  tier (e.g., a specific prior exit ticket, diagnostic score, or "Default profile applied — no
  diagnostic data available"). A blank or generic statement fails.
- The section includes an explicit statement that tier assignments are revisable based on
  formative evidence from THIS lesson (not a standing ability track).

**O4 — Rationale notes (confirm in teacher plan JSON):**
- `Why this works (1)` and `Why this works (2)` sections are present and each name a specific
  tier design choice with a stated reason. Generic statements ("scaffolds help learners") fail.
  These sections are required and cannot be dropped to meet page caps — tighten other content
  instead.

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

   (`references/example_differentiation.json` is a filled-in worked example if
   values-in-context would help, but reading it is not required.) Keep writing tight; no emoji in JSON content.
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
   — use a `bullets` block; a paragraph collapses line breaks and the bullets run together
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
   test. Asset framing rules (below) apply to every student-facing block.

### 5b. Render all four Word documents — one command, same turn

```bash
bash scripts/render_all.sh differentiation.json "$OUTPUT_DIR"
```

This writes `$OUTPUT_DIR/teacher_plan.docx`, `$OUTPUT_DIR/worksheet_group_a.docx`,
`$OUTPUT_DIR/worksheet_group_b.docx`, and `$OUTPUT_DIR/worksheet_group_c.docx` in one invocation,
plus `.html` working files — no copy step needed; leave everything
the script writes in place (later revision turns re-render from the working files). Then list
`$OUTPUT_DIR` and confirm every document has both its `.docx` and `.html`; if either is
missing or tiny, rerun the script. Present all four Word documents to the teacher together —
attach the teacher plan last so it lands on top (chat surfaces stack newest-first). If the script errors, fix
`differentiation.json` (it is almost always malformed JSON) and rerun. If file generation
fails entirely, say so clearly — do not silently fall back to a chat-only delivery.

### 5c. The close (every output turn)

The chat message that delivers artifacts ends with three things, in order. Each must appear in
the chat message itself — saying it only inside the printed plan does not count. When the
message mentions the sheets, use their group names with the association noted once
(Group A = below grade level, etc.).

1. **Learner-variability statement (first output turn, when you didn't ask).** If you never
   asked about specific learner needs in this conversation (the R8 question), state in chat
   that UDL defaults were applied and invite specifics — e.g. *"I didn't have details on
   specific learner needs, so I applied UDL defaults — sentence stems and a vocabulary
   glossary on all three tier sheets. Tell me about any multilingual learners or students
   with IEPs or 504 plans and I'll tailor further."* Skip this only when the teacher already
   gave learner information (then reflect it instead: "the Below sheet builds in the sentence
   frames for your newcomer ELLs").
2. **Three lesson-specific next steps (first output turn).** Offer 3–4 iteration options in
   chat, one short line each, specific to THIS lesson (e.g., a tiered ELD layer with
   WIDA-banded sentence supports; IEP-goal-specific scaffolds for a named goal area; a fourth
   intervention tier below the prerequisite; tightening scope to the exit ticket only). The
   subject reference's FA follow-up prompt counts as one of them when it fits.
3. **The satisfaction ask.** Ask whether the teacher is satisfied with **all four artifacts**
   or wants changes. Do not skip the ask — on every output turn, including revisions.

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

---

## Step 6 — Complete

The skill is complete when the teacher has confirmed they are satisfied with all four Word
documents (5c). The closing message pairs the FA follow-up prompt from the subject
reference's R8 section with the lesson-specific next-step options from 5c.

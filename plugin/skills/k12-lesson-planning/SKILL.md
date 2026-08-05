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

Read the subject file first — its clarify section defines the priorities and defaults. Ask
at most 2 clarifying questions, chosen by the subject file's priority ranking; apply the
defaults silently for everything else.

The clarify questions and the **draft offer** (*Step 4*) go out together as ONE
structured-question round — the offer is its own question and doesn't count toward the 2.
When nothing needs clarifying, the offer is asked on its own. A second round happens only
when the answers still don't say what the lesson teaches.

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

The teacher gets the choice of a fast draft before the build. The offer rides in Step 1's
round (structured question tool when available, chat otherwise), and its two sides are
always the packet and the draft. The wording below lives in the question itself — the
teacher may act on it without reading the chat text around it:

- Question: *Should I build a full classroom-ready packet (lesson plan + student
  materials, as editable Word docs), or do you want to see a quick draft first?*
- Options: **Go ahead and build it** · **Quick draft first** — the lesson at a glance,
  right here in chat

**The full packet is the default.** A reply that selects the draft option or asks to see
the draft gets the draft; every other reply runs Steps 2–3 and goes straight to Step 5.

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

Afterwards, ask what's next in plain chat — a typed reply can carry the changes themselves,
which a picked option cannot: *"Want anything different? Tell me here — or tell me to go
ahead and I'll create the materials (lesson plan, student materials, and observation
template, as editable Word docs)."*

Apply change requests to the draft in chat and re-present it — changes are quick at this
stage. Step 5 runs in the turn the teacher gives the go-ahead.

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
behavior is fully specified by the commands and output paths in §5a–5e, and
`references/example_lesson.json` is a filled-in worked example. Reading script source tells
you nothing these instructions don't already state.

**Plain language with the teacher.** The machinery above is invisible to the teacher: never
mention JSON, HTML, schemas, scripts, rendering, file names (`lesson.json`), or code in any
teacher-facing message — and never link or name the `.html` files the render command also
writes. Say *"Here's your lesson plan — the student materials and observation template are on
their way"*, not *"I've rendered lesson.json"*. The only format word in your prose is
"Word document". This
applies to every turn: presenting artifacts, the satisfaction ask, revision summaries, and
error messages (if generation fails, say the documents couldn't be created — not that a
script or JSON failed).

Before writing `lesson.json`, read `references/output.md` in full — it carries the hard
requirements for every document (density, consistency, reading level, integrity) and the
complete `lesson.json` schema and block guide (§5a and §5e live there).

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


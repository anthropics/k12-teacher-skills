---
name: k12-lesson-differentiation
description: Adapts an existing K-12 lesson (math, ELA, science, or social studies) for students at different proficiency levels (below / at / above grade level). Load this skill BEFORE asking the teacher any clarifying question about the lesson, tiers, or student levels. Triggers on explicit asks to differentiate, tier, or scaffold a lesson, and on implicit signals like "my students are at different levels". Produces 1 teacher-facing differentiation plan + 3 student-ready tier documents as editable Word documents in a single output turn, rendered from one material-source JSON via bundled scripts (shared content is written once so tiers cannot drift). Uses the Learning Commons Knowledge Graph when connected; works without it. This skill adapts a lesson the teacher brings or names. Not for creating a new lesson from scratch — a new-lesson request that asks for differentiated or leveled materials is k12-lesson-plan-creation's job, one package. Not for grading, rubrics, assessment feedback, or quizzes.
license: "Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0. Complete terms in LICENSE and NOTICE."
---

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
2. **Curriculum.** The subject file's "Identify the source lesson" section includes curriculum
   detection (Illustrative Mathematics / OpenSciEd). When confirmed, use that
   curriculum's discourse language and structures in the teacher plan, per the subject file.

   **Curriculum is confirmed when:** the teacher explicitly names it, OR the uploaded source
   lesson references it (the upload is implicit confirmation).

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
   - Standard codes follow a state-specific format (TEKS, SOL, OAS/PASS, MA, CA/HSS or
     CA/CCSS; other state-prefixed codes → check state)
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
ask them to paste or upload), Scenario B3 (math or science only — teacher names a curriculum lesson by position or title —
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

This check runs even when scope is already specified.


---

## Step 2 — Ground in standards

**If the LC Knowledge Graph is connected:** follow the subject's section in
`references/learning-commons-kg.md` — call BEFORE drafting; not calling when connected is a
critical failure, no matter how the source lesson was obtained — retrieving
the lesson never satisfies this step.

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

The teacher gets the choice of a fast draft before the build. The offer rides with
whatever you ask before Step 2 (state, source lesson, learner needs — structured question
tool when available, chat otherwise) as its own separate question, and is asked on its
own when nothing else needs asking. Its two sides are always the set and the draft. The
wording below lives in the question itself:

- Question: *Should I build a full classroom-ready set (teacher plan + three tier
  documents, as editable Word docs), or do you want to see a quick draft first?*
- Options: **Go ahead and build it** · **Quick draft first** — what changes for each
  tier, right here in chat

**The full set is the default.** A reply that selects the draft option or asks to see
the draft gets the draft; every other reply runs Steps 2–3 and goes straight to Step 5.

**The draft (on a yes) is built on Steps 2–3, never instead of them.** Run Step 2 in
full — every KG call, exactly as written — and Step 3 before sketching anything. A draft
sketched without the Step 2 grounding is a critical failure. Then present the design in
chat — the draft is chat text only;
rendering happens at Step 5 once the teacher approves. Show:

- one line reading back the source lesson, standard, and grade;
- for each tier (below / at / above), 2–3 bullets on what changes and why;
- the student work at a glance — each tier's actual tasks, enough for the teacher to
  skim and judge coverage;
- one line on what every tier shares — the essential question or core task — and the
  regroup rule

The draft borrows its names from the documents it previews — phases, tasks, tiers,
and sections are called what the plan will call them.

Afterwards, ask what's next in plain chat — a typed reply can carry the changes themselves,
which a picked option cannot: *"Want anything different? Tell me here — or tell me to go
ahead and I'll create the materials (teacher plan and the three tier documents, as editable
Word docs)."*

Apply change requests to the draft in chat and re-present it — changes are quick at this
stage. Step 5 runs in the turn the teacher gives the go-ahead.

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

Every change goes into `differentiation.json` and is re-rendered (instant) — never write
layout code, hand-edit a generated document, or re-type one into another format.

**Plain language with the teacher.** The machinery above is invisible to the teacher: never
mention JSON, HTML, schemas, scripts, tool names, rendering, file names, or code
in any teacher-facing message — and never link or name the `.html` files the render command
also writes. Say *"Here's your differentiation plan — the three tier documents are on their
way"*, not *"I've rendered differentiation.json"*. The only format word in your prose is
"Word document". This applies to every
turn, the keeping-posted announcement included: presenting artifacts, the satisfaction
ask, revision summaries, and error messages (if
generation fails, say the documents couldn't be created — not that a script or JSON failed).

Before writing `differentiation.json`, read `references/output.md` in full — it carries
the hard requirements, cross-checks, schema, revision rules, and student-page language
rules. Re-read it before any revision turn.

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
   subject reference's FA follow-up prompt must be one of them.
3. **The satisfaction ask.** Ask whether the teacher is satisfied with **all four artifacts**
   or wants changes. Do not skip the ask — on every output turn, including revisions.

## Step 6 — Complete

The skill is complete when the teacher has confirmed they are satisfied with all four Word
documents (5c).

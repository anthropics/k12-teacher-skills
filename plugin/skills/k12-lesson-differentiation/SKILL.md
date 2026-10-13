---
name: k12-lesson-differentiation
description: Adapts an existing K-12 lesson (math, ELA, science, or social studies) for students at different proficiency levels (below / at / above grade level). Load this skill BEFORE asking the teacher any clarifying question about the lesson, tiers, or student levels. Triggers on explicit asks to differentiate, tier, or scaffold a lesson, and on implicit signals like "my students are at different levels". Produces 1 teacher-facing differentiation plan + 3 student-ready tier documents as editable, printable documents in a single output turn (shared content is written once, so tiers cannot drift). Uses the Learning Commons Knowledge Graph when connected; works without it. This skill adapts a lesson the teacher brings or names. Not for creating a new lesson from scratch — a new-lesson request that asks for differentiated or leveled materials is k12-lesson-plan-creation's job, one package. Not for grading, rubrics, assessment feedback, or quizzes.
license: "Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0. Complete terms in LICENSE and NOTICE."
---

# K-12 Lesson Differentiation

Paths here (`references/…`, `rendering/…`) are relative to this SKILL.md's folder; use absolute
paths.

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

The teacher reads every line you write, the ones beside tool calls included. Between tool calls say
nothing, or speak in teacher language: name what the teacher is getting — the differentiation plan
and the three tier documents — never tool names, file names, "JSON", "artboards" or "rendering". Say
"Word document" only on the Word path; otherwise "your documents" or "pages". The same goes for
errors: say the documents couldn't be made, not that a script or JSON failed.

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

- Question: *Should I build a full classroom-ready set (teacher plan + three tier documents, as
  editable, printable documents), or do you want to see a quick draft first?*
- Options: **Go ahead and build it** · **Quick draft first** — what changes for each
  tier, right here in chat

**The full set is the default.** A reply that selects the draft option or asks to see
the draft gets the draft; every other reply runs Steps 2–3 and goes straight to Step 5.

**The draft (on a yes) is built on Steps 2–3, never instead of them.** Run Step 2 in full — every KG
call, exactly as written — and Step 3 before sketching anything. A draft sketched without the Step 2
grounding is a critical failure. Then present the design in chat — the draft is chat text only; the
documents are made at Step 5 once the teacher approves. Show:

- one line reading back the source lesson, standard, and grade;
- for each tier (below / at / above), 2–3 bullets on what changes and why;
- the student work at a glance — each tier's actual tasks, enough for the teacher to
  skim and judge coverage;
- one line on what every tier shares — the essential question or core task — and the
  regroup rule

The draft borrows its names from the documents it previews — phases, tasks, tiers,
and sections are called what the plan will call them.

Afterwards, ask what's next in plain chat — a typed reply can carry the changes themselves, which a
picked option cannot: *"Want anything different? Tell me here — or tell me to go ahead and I'll
create the materials (teacher plan and the three tier documents, as editable, printable
documents)."*

Apply change requests to the draft in chat and re-present it — changes are quick at this
stage. Step 5 runs in the turn the teacher gives the go-ahead.

---

## Step 5 — Output (one turn)

Runs immediately when the teacher chose the full set, or in the turn the draft is
approved.

### 5a. Read references and make the common JSON

1. Read `references/output.md` in full first: the hard requirements for every document's content.
2. Then read `references/differentiation-json.md` and write ONE complete **`differentiation.json`**,
   the set's common baseline. Every path makes its documents from it; it fixes WHAT each document
   carries, not how a page looks.

### 5b. Make every document — same turn

Check whether your artifact tool can create an artifact from a published type; if it can, look at
its type list. Take the first row that applies and read its file:

| What you have | Read |
|---|---|
| **Design** is in the type list | `rendering/claude-artifact.md` |
| Design isn't listed, or there is no such tool | `rendering/docx.md` |

If making the documents fails entirely, say so — don't silently fall back to chat.

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

### 5d. Revisions — one change, every document stays in sync

Re-read `references/output.md` before any revision turn. Make **targeted edits to
`differentiation.json` first**: shared content is edited in `shared`, once, and every document that
pulls it follows identically. Then re-read every document and fix every sentence that still mentions
the old context, names, or numbers — stale prose is the most common consistency failure. A change
aimed at one tier goes in that tier document's blocks, never by forking shared content, and keeps
the subject file's R4 rules and R7 fade pattern. Then carry it into the documents the way your
path's file says (Docs and canvas: only the parts and pages whose content changed; Word: re-render).

## Step 6 — Complete

The skill is complete when the teacher has confirmed they are satisfied with all four documents
(5c).

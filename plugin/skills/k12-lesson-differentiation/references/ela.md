<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->

# ELA — differentiation pedagogy

Loaded by `k12-lesson-differentiation` when the subject is **ela**.

## Identify the source lesson and curriculum

Detect which scenario applies:

**Scenario A — Source lesson exists in the prior conversation**
If a lesson was produced or discussed earlier in this conversation, use it directly. Do NOT re-ask the teacher to share it.

**Scenario B — Teacher uploads a source lesson**
Read the file first. Confirm: grade level, ELA strand (reading, writing, or combined), standard, learning objective, and lesson structure. Also identify the text(s) used if present. If the file is unreadable on first attempt, surface the error clearly and ask the teacher to re-share. Do NOT silently fabricate a lesson.

**Scenario B2 — Teacher links a source lesson by URL**
Fetch the URL and read its content first. Then confirm grade level, ELA strand, standard, learning objective, lesson structure, and text(s) used exactly as in Scenario B. If the fetch fails or returns unusable content, surface the error clearly and ask the teacher to paste the lesson text or upload the file. Do NOT silently fabricate a lesson.

**Fetching the lesson completes Step 1 only — it does NOT replace standards grounding.** Continue to Step 2 — Ground in standards. Skipping Step 2 after a URL fetch is the same critical failure as skipping it for an uploaded lesson.

**Scenario C — No source lesson present**
Ask before proceeding:
> "Happy to differentiate. Do you have a specific lesson in mind? You can paste it, share a file, or tell me the grade + strand (reading, writing, or both) + standard and I'll work from that."

---

## Standards grounding

Follow **Step 2 — Ground in standards** in SKILL.md: if the Learning Commons Knowledge Graph
is connected, use the ELA section of `references/learning-commons-kg.md`; if not,
proceed from best knowledge and add the disclaimer footer to the teacher plan.

**State-aware standard resolution:** When state is known from Step 0, use state ELA framework
codes in all output. Pass jurisdiction in the KG call per learning-commons-kg.md.


## The differentiation rules

Apply all eight rules to every differentiated lesson.

### R1 — Output structure

**1 cohesive teacher-facing differentiation plan + 3 pure student-ready materials. NEVER 3 hybrid per-level lesson plans.**

The hybrid pattern — 3 per-level documents each mixing teacher notes and student tasks — is a specific failure mode. The teacher plan covers all levels in one document; the student materials are student-only, with no teacher notes, look-fors, or rationale.

### R2 — Standard and strand scope preservation

**Every tier addresses the original standard. Every learning component stays in play across all tiers.**

ELA lessons commonly interweave multiple literacy strands — reading comprehension, vocabulary, and writing — within a single lesson. Differentiation must address each strand present. Do not drop a strand for below-level students; scaffold it instead.

The standard's most demanding element (e.g., identifying an author's argument, writing a claim with evidence) is exactly what below-level students most need to encounter with supports — not the element to remove.

**Engagement must be preserved at the Below tier.** Do not assign richer texts or prompts to At/Above and drill-like work to Below. All tiers work with the same text and same essential question — with different supports, not different tasks.

### R3 — Text access: same text, different scaffolds

**All three tiers work with the same grade-level text. Text complexity is not adjusted — access to the text is.**

This is the foundational ELA differentiation principle. Handing below-level students an easier text closes off grade-level engagement rather than building toward it. Instead, scaffold how students access the grade-level text.

The tiers map to a progression from supported access to independent analysis:

| Tier | Cognitive entry point |
|---|---|
| Below | Supported access → scaffolded production. Student works with the grade-level text using chunked reading, pre-taught vocabulary, annotation guides, and sentence supports to reach the task. |
| At | Standard engagement. Student reads the grade-level text and completes the task as designed. |
| Above | Independent analysis / synthesis. Student reads the grade-level text and moves beyond retrieval to author's craft, evaluation, cross-text connection, or generative production. |

When the KG names a prerequisite standard, identify what reading or writing skill students already have from that standard — and build the below-level scaffold to bridge from that prior skill to the grade-level task.

**For writing lessons:** keep the same prompt and writing purpose across tiers. What varies is structural support (frames, organizers, models). Do not reduce the writing purpose (e.g., do not convert an argument to a summary for below-level students).

### R3.5 — Foundational literacy prerequisite check (K–5 only)

**For lessons in grades K–5, determine whether the below-level student's likely barrier is a decoding/fluency gap or a comprehension/vocabulary gap before selecting scaffolds. These require different responses.**

Decoding and reading fluency are hard prerequisites for comprehension work — not gaps that comprehension scaffolds can compensate for. A student who cannot decode the text fluently cannot be scaffolded into comprehension of it. This is the most common failure mode in K–5 below-level differentiation: applying comprehension scaffolds to a student whose root problem is foundational.

**By grade band:**

- **K–2:** Phonics or decoding gaps are possible, especially if the student is receiving Tier 2 support. Comprehension scaffolds are appropriate as concurrent supports but treat them as such — not as root-cause interventions.
- **3–5:** Default below-level profile is a fluency ceiling — adequate decoding accuracy, low automaticity, which taxes working memory and degrades comprehension. Prioritize fluency-supporting structures (read-aloud permission, partner reading, echo reading) alongside comprehension scaffolds. This is the highest-risk grade band for misidentification: a student who appears to have a comprehension problem may actually have a fluency gap.

**If the primary barrier appears to be decoding or fluency, add a flag to the teacher plan under BELOW TIER. For example:**

> *"⚠ Foundational literacy note: If students cannot read this text aloud fluently, comprehension scaffolds will not close the gap — the prerequisite need is decoding/fluency intervention delivered separately. Read-aloud is an appropriate access bridge while that support is in place, not a substitute for it."*

Do not include this flag for grades 6–12 unless there is a specific signal of a late-identified reading disability. At those grades, below-level comprehension difficulty is more likely caused by vocabulary gaps, thin background knowledge, or weak inference skills.

### R4 — Below-level scaffolds

**Scaffolds support thinking without revealing answers. Use sentence supports, graphic organizers, annotation cues, and vocabulary supports. NEVER answer-revealing hints. NEVER simplified content substitutes.**

Failure modes to avoid:

- ❌ Substituting an easier text, passage, or writing prompt for below-level students. This removes grade-level engagement, not a scaffold.
- ❌ Reducing writing purpose (e.g., changing argument to summary, or multi-paragraph to single sentence) when the standard requires the original form.
- ❌ Pre-filled graphic organizers that leave only a blank for the final answer.
- ❌ Telling students what the text is about before they read (comprehension-revealing prereading).
- ❌ Sentence starters that answer the task ("The author argues that slavery was wrong because…") rather than structuring the student's own thinking ("The author argues that ______ because ______").

Acceptable scaffolds:

- ✓ Chunked reading with guided annotation cues: "As you read this paragraph, mark: the main idea (circle), one piece of evidence (underline), one word you don't know (?)"
- ✓ Vocabulary support: 3–5 pre-taught key terms, defined in student-friendly language, available during reading and writing.
- ✓ Sentence supports that structure thinking without completing it: "The author uses ______ to show ______." / "My claim is ______. One reason is ______."
- ✓ Graphic organizers matched to the literacy task (see table below).
- ✓ Read-aloud or partner reading permission (teacher-side, not embedded in worksheet) — appropriate as an access bridge for students with decoding gaps who are receiving phonics intervention separately. Not a substitute for that intervention. See R3.5.
- ✓ Reduced number of text evidence examples required — while preserving the task type (e.g., find 1 example instead of 3, not switch to a different task type).

#### Literacy task → primary scaffold

Select the primary scaffold based on the literacy task, not the grade level:

| Literacy task | Primary scaffold |
|---|---|
| Reading comprehension (narrative) | Story map: character / problem / event sequence / resolution |
| Reading comprehension (informational) | Main idea + evidence organizer |
| Argumentative / opinion writing | Claim–reason–evidence frame |
| Narrative writing | Story spine or structured story map |
| Informational / explanatory writing | Web organizer → paragraph frame |
| Text analysis (author's craft, structure) | Annotation guide + "The author does ______ to ______" frame |
| Compare/contrast (texts or characters) | T-chart or Venn with labeled categories |
| Vocabulary in context | Word map: definition / example / non-example / sentence |

Use this table to pick the **primary scaffold** before applying the density cap. If the lesson spans multiple task types, pick the scaffold for the task where below-level students most need support.

The test: does the scaffold leave the intellectual work to the student, or does it perform the work for the student? If the latter, it is not a scaffold.

#### Scaffold density cap

**Cap embedded scaffolds at 1–2 per task.** Over-scaffolding shifts cognitive load to navigating supports rather than engaging with text or writing — equally harmful as under-scaffolding.

| Type | Counts toward cap? |
|---|:-:|
| Embedded — printed on every task (organizer, sentence support, annotation cue) | YES |
| Header-level features — vocabulary box, sentence supports at top of page | NO |
| Teacher-side supports — read-aloud permission, conferring prompts, manipulatives | NO |

**Pick a primary scaffold first.** Only add a second if it contributes a genuinely different mode (e.g., visual organizer + linguistic frame). If the second scaffold asks the student to do the same mental work as the primary, drop it.

### R5 — Required pedagogical infrastructure

**Every differentiated lesson must include all four:**

| Section | What it is | Where |
|---|---|---|
| **Formative check** | Concrete mid-lesson or end-of-lesson prompt to gauge readiness — a tiered exit ticket counts. Not "monitor students." | Teacher plan + per-level student materials |
| **Anchor activity** | Standard-aligned task for early finishers. Not busywork. Should connect to the ELA strand of the lesson (e.g., independent reading, writer's notebook extension). Written student-facing in `shared.anchor_activity` and printed on every student material — an anchor activity that exists only as a plan description is a failure. | Teacher plan + all three student materials |
| **Flexible-grouping language** | Tier assignments tied to THIS lesson's evidence, explicitly revisable based on formative check results. Not static reading-level tracks. | Teacher plan |
| **Per-level misconception / common error notes** | Common errors specific to each tier + teacher prompt + signal for pulling a small group. For reading: comprehension errors; for writing: craft or structure errors. | Teacher plan |

In addition: **each student material ends with one open-ended or reflective prompt, present on all three tiers** — e.g., "What do you think the author's main purpose was? Use evidence from the text." / "What was the hardest part of your writing? What would you change?" This is not optional for any tier. Store it as `shared.reflect_prompt` and name it in each tier's **Worksheet tasks** line in the teacher plan — a printed task the plan never mentions is a failure.

### R6 — Invisible modifications

**Same text / same prompt / same core task across tiers where pedagogically possible. Only the supports differ.**

What can differ: scaffolds embedded in the student materials; optional teacher-provided supports during conferring; the extension or reflection prompt depth.

What should NOT differ: the text students read; the writing purpose or prompt; the structural challenge the standard targets; the topic or context.

**Do not announce scaffold removals to students.** If a scaffold appears in Task 1 but not Task 3, its absence is silent — no label, aside, or comment (e.g., no "(No organizer this time)" or "Try it without the frame"). The scaffold simply does not appear; students encounter the task on its own terms.

For writing: use the same prompt across all tiers by default. The number of required examples or the structural support may vary, but the task must not.

For reading: do not create a "below-level version" of the text by simplifying sentences or reducing length. If the text is truly inaccessible (e.g., due to student language status), flag this in the teacher plan as a separate ELD consideration — not a standard differentiation tier.

### R7 — Within-level progressive scaffolding

**Each tier's student materials sequence tasks with progressive cognitive demand. Not uniform difficulty.**

#### Below-level fade pattern

| Task | Embedded scaffolds | Pattern |
|---|:-:|---|
| Task 1 | Up to 2 | Scaffolded |
| Task 2 | Up to 1 | Guided |
| Task 3+ | 0 embedded | Independent |
| Exit ticket | 0–1 | Mastery check |

The goal is a true fade (2 → 1 → 0), not uniform scaffold density across all tasks.

#### Above-level extension quality test

Every above-level extension must answer: **what new thinking does this require that the at-level student isn't already doing?** If you cannot name new thinking, the extension is cosmetic and should not ship.

A real ELA extension requires at least one of:

| Type | What it requires |
|---|---|
| Author's craft analysis | Move from "what does the text say" to "why did the author make this choice and what effect does it create." |
| Perspective shift | Retell from another character's/narrator's point of view; argue the opposing claim; rewrite from a different rhetorical purpose. |
| Cross-text synthesis | Connect to a second text, comparing argument, structure, author perspective, or theme. |
| Structural insight | Generalization about genre, structure, or author strategy the at-level task treats as a single instance. |
| Open generative task | Student produces something new: original piece in the author's style, counterargument, question for class discussion. |
| Forward-standard preview | A real conceptual element from a higher-grade ELA standard — not just its vocabulary. |

Reject if: more of the same, notation/vocabulary swap only, or restatement.

If only one meaningful extension fits, include only that one.

### R8 — Scope and defaults

**If tier scope is not specified, ask ONE combined question before generating:**

> "I'll differentiate this into below / at / above grade-level tiers — are those the right three? And any specific learner needs I should know about (ELL levels, IEP goals)? If not, I'll apply UDL defaults (sentence supports and vocabulary support across all tiers)."

If scope is already specified, apply defaults silently and proceed.

**Defaults applied silently when not specified:**
- Tiers: below / at / above
- UDL features: sentence supports and vocabulary glossary in **all three** student materials (not Below only — rubric O5)
- Scope: full lesson (all phases + exit ticket)
- Text: same grade-level text across all tiers (never substituted)

**Default below-level profile absent formative data:**

When no diagnostic data is available (no ORF scores, running records, phonics screener results, or exit ticket data), design for the most likely profile by grade band:

- **K–2:** Phonics or decoding gaps are possible. Apply comprehension scaffolds as concurrent supports; include read-aloud permission as a teacher-side option; check whether a foundational literacy flag (R3.5) is warranted.
- **3–5:** Default profile is a fluency ceiling — adequate decoding accuracy, low automaticity. Prioritize fluency-supporting structures (read-aloud permission, partner/echo reading) alongside comprehension scaffolds. Vocabulary pre-teaching is the second lever.
- **6–8 and 9–12:** Default profile is vocabulary and background knowledge gaps. Academic Tier 2 and Tier 3 vocabulary is the most common bottleneck. Scaffold semantics and syntax first; decoding is likely sufficient for word recognition.

Without formative data, assume the below-level student has gaps in the most proximal prerequisite for the lesson's primary literacy skill: for comprehension-focused lessons, vocabulary and fluency; for writing-focused lessons, organizational and sentence-level structure.

**After generating the tiered plan, prompt the teacher for formative data:**

> *"Do you have any reading data — ORF scores, running records, a phonics screener, or writing samples — that could help me target the right scaffolds? Even informal notes on where students got stuck would help."*

Adjust the prompt by grade band:
- **K–5:** Ask specifically for ORF scores, running records, or phonics screener results. This is the highest-stakes FA follow-up in ELA — whether the below-level student has a decoding gap vs. a comprehension gap changes the entire scaffold approach. Comprehension scaffolds built for a decoding-gap student waste instructional time.
- **6–12:** Ask for exit ticket results or writing samples showing where inference or argument structure breaks down. FA data here usually confirms the default assumption (vocabulary/background knowledge) rather than inverting it.

Do not treat the FA follow-up as optional for K–5. The default tiered plan is a best-guess; the gap between a decoding student and a comprehension student is too consequential to leave unconfirmed when data may be available.

---

### Document content — teacher plan (`id: teacher_plan`) — max 3 pages

**Length budget: ~1,200 words rendered (the 3-page cap in practice).** Tighten the tier
sections and overview before touching the closers (Flexible Grouping, Why this works, Next
Steps) — the most common overrun is a Worksheet tasks line that restates student-material
content instead of naming it.

The outline below defines the content and order of the teacher plan document's `sections`:
each `##` heading becomes one section, its body becomes that section's blocks (use
`from_shared` blocks for the standard, misconceptions, and exit ticket; `labeled` blocks for
the bold fields).

```markdown
# Differentiation Plan: [Lesson Title]

**Standard:** [verbatim]  **Grade:** [X]  **Strand:** [RL/RI/W/SL/L]  **Duration:** [X min]  **Curriculum:** [name if confirmed / General]
*Learner needs: [If no specific needs were provided: "UDL defaults applied — sentence supports and vocabulary support across all tiers." If learner needs were specified, describe them here instead.]*

## Learning Objective
[Same objective across all tiers — preserved from source lesson]

## Differentiation Overview
[1 short paragraph, ≤3 sentences: approach, text confirmed as shared across all tiers,
prerequisite named by code + short gist (for K–5, note if the foundational literacy flag
applies per R3.5), forward standard named by code + gist. Never paste full standard text
here — the target standard is already verbatim in the header. Use CCSS if state uses
CCSS/CCSS-aligned. Source from state vertical alignment when state is known; footnote CCSS code
when using as proxy for a non-CCSS state.]

## Tier Design
[ONE `table` block — never three labeled paragraph stacks. Columns: Below (Group A) / At (Group B) / Above (Group C).
Rows (a cell may be "—" where a field doesn't apply to that tier):
- **Grounded in** — Below: concept-level prerequisite by code + gist from CCSS vertical
  alignment. Above: forward standard by code + gist. At: "—".
- **Scaffolds / extension** — fragments, ≤25 words per cell: Below scaffolds in play; At
  supports; Above extension + which R7 quality type it meets.
- **Conferring move** — one specific prompt per tier.
- **Worksheet tasks** — ≤40 words per cell, written LAST: read that tier's FINAL student
  material's blocks top-to-bottom and name every printed task in order — tasks by name with
  their printed scaffolds (e.g. "First read (annotation guide), Central-idea organizer,
  Summary"), every tier-only add-on or extension sub-part by its printed heading, exit
  ticket, "If you finish early" anchor task, Reflect prompt. List items; don't restate their
  text. Name nothing unprinted — no "on request" supports, no planned organizer the material
  dropped. Never copy another tier's cell.]


[Then ONE `callout` (note style): misconception / common error watch — pattern + teacher
prompt, ≤2 sentences per tier that needs one.]

[K–5 only, if applicable — a SECOND `callout` (note style), the foundational literacy flag:
⚠ If students cannot read this text aloud fluently, comprehension scaffolds will not close
the gap — the prerequisite need is decoding/fluency intervention delivered separately.
Read-aloud is an appropriate access bridge while that support is in place, not a substitute
for it.]

## Formative Check
[Two required elements:
1. **Mid-lesson checkpoint:** A specific check during reading or writing work time — name the trigger or artifact (e.g., "After the annotation task, collect two student samples: if neither can identify the central idea, pause and re-model the annotation move before moving to the writing task"). 'Circulate and observe' does not pass.
2. **Exit ticket with explicit sort criteria:** State what a student must produce or demonstrate to land in each bucket for THIS lesson, e.g.: "Got it — [e.g., names the central idea and cites two pieces of text evidence] / Almost there — [e.g., names the central idea but cites only one piece of evidence or misidentifies a supporting detail] / Needs re-teaching — [e.g., cannot name the central idea independently]." Generic bucket labels without lesson-specific criteria do not pass.]

## Anchor Activity
[`from_shared: anchor_activity` — the same student-facing task printed on every student material — plus one teacher-only line: when to deploy it and why it requires genuine ELA thinking]

## Flexible Grouping
[Current tier assignments, the evidence or basis for placement (e.g., "Placed based on prior writing sample / ORF score / exit ticket on [standard]" or "Default profile applied — no diagnostic data available"), and an explicit statement that groups are revisable after the formative check]

## Why this works (1)
[One specific tier design choice + reasoning]

## Why this works (2)
[A second specific tier design choice + reasoning]

## Next Steps
**Got it (exit ticket passes):** [connect to forward standard or upcoming lesson]
**Almost there:** [targeted small-group or conferring move — specific gap to address]
**Needs re-teaching:** [specific reteach strategy or Tier 2/3 flag if gap is persistent]

```

### Document content — student materials (`id: worksheet_group_a` / `worksheet_group_b` / `worksheet_group_c`)

No teacher notes, look-fors, or rationale. All three include: vocabulary glossary + sentence
frames + the "If you finish early" anchor task + open-ended reflective prompt (rubric O5 —
UDL across all tiers) — all pulled from `shared` so they are identical across tiers by
construction.

Format by strand:

| Lesson strand | Student material format |
|---|---|
| Reading | Reading guide: text excerpt(s) if needed, annotation prompts, comprehension tasks, response prompt |
| Writing | Writing frame: mentor text excerpt (if in lesson), planning organizer, drafting space with scaffolds |
| Combined | Reading tasks followed by writing tasks, scaffolds at the appropriate fade per R7 |

```markdown
# [Group A / Group B / Group C] — [Lesson Title]

**Name:** _________________ **Date:** _________

## Vocabulary
[`from_shared: vocabulary` — the renderer formats the term–meaning pairs itself; never type a pipe-character table into a `text` field]

**You can use these sentence supports:**
- "The author uses ______ to show ______."
- "My claim is ______. One reason is ______."

---

[Tasks pulled ONE AT A TIME, each with its scaffold directly above it — per task N:
at most ONE scaffold block (Below only, R7 fade: Task 1's block may combine a primary +
secondary scaffold if genuinely different modes; Task 2 gets one lighter scaffold; Task 3+
gets none — the absence is intentional and silent), then
`{"type": "from_shared", "key": "tN", "label": "N"} followed by a workspace block`. Task text identical on all three
tiers; never re-typed. Writing space after each task is automatic — do not add answer
boxes for tasks.]
[Tier-only add-ons (e.g. Above "Go further" extension) as their own headed sections]

---

## If you finish early
[`from_shared: anchor_activity` — identical block on all three tiers]

## Reflect
[`from_shared: reflect_prompt` — identical question on all three tiers]
```

---

## Writing differentiation.json — ELA mapping

- `shared.subject`: `"ELA"`
- `shared.anchor_task`: the shared text + essential question
- `shared.t1`..`tN`: the core reading/writing tasks shared by ALL tiers, one task per key — faceted {teacher: "the difficulty and what to watch for, as a plain sentence", student: <the task>}
- Teacher document: differentiation plan, max 3 pages; student materials max 2 pages each
- **Copyright:** do NOT reproduce the source lesson's student-facing text verbatim — rewrite as original content.

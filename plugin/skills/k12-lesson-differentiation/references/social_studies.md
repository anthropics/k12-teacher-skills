<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->

# Social Studies — differentiation pedagogy

Loaded by `k12-lesson-differentiation` when the subject is **social studies**.

## Identify the source lesson

**State identification.** Social studies standards are state-specific. If the teacher names a state (or one is established earlier in the conversation), anchor to it: use the state-specific standards framework (e.g., California HSS Framework, Texas TEKS, New York Passport to Social Studies) as the primary content scope reference. If the teacher does not name a state and it is not inferrable, ask.

**C3 Framework note.** The C3 Framework is an *inquiry design* framework, not a standards document. Use C3 for instructional design principles (inquiry arc, sourcing, argumentation, civic action) but defer to state standards for what students must know and be able to do. If the teacher references C3 directly, use its inquiry arc to structure the lesson's tasks — but anchor content scope to the state standard.

Then detect which scenario applies:

**Scenario A — Source lesson exists in the prior conversation**
If a lesson was produced or discussed earlier in this conversation, use it directly. Do NOT re-ask the teacher to share it.


**Scenario B — Teacher uploads a source lesson**
Read the file first. Confirm: grade level, subject (history / civics / geography / economics),
standard, learning objective, lesson structure. **Also extract the state** from the standard
code if present (TEKS 113.xx → Texas; California HSS/CCSS → California; MA Curriculum
Framework → Massachusetts; etc.). Store as state — do not ask the teacher if it can be
inferred from the standard code.


**Scenario B2 — Teacher links a source lesson by URL**
Fetch the URL and read its content first. Then confirm grade level, subject (history / civics / geography / economics), standard, learning objective, and lesson structure exactly as in Scenario B. If the fetch fails or returns unusable content, surface the error clearly and ask the teacher to paste the lesson text or upload the file. Do NOT silently fabricate a lesson.

**Fetching the lesson completes Step 1 only — it does NOT replace standards grounding.** Continue to Step 2 — Ground in standards. Skipping Step 2 after a URL fetch is the same critical failure as skipping it for an uploaded lesson.

**Scenario C — No source lesson present**
Ask before proceeding (include state if state is also unknown):
> "Happy to differentiate. Do you have a specific lesson in mind? You can paste it, share a file, or tell me the grade + topic + standard and I'll work from that."

---

## Standards grounding

Follow **Step 2 — Ground in standards** in SKILL.md: if the Learning Commons Knowledge Graph
is connected, use the Social Studies section of `references/learning-commons-kg.md`; if not,
proceed from best knowledge and add the disclaimer footer to the teacher plan.

## The differentiation rules

Apply all eight rules to every differentiated lesson.

### R1 — Output structure

**1 cohesive teacher-facing differentiation plan + 3 pure student-ready worksheets. NEVER 3 hybrid per-level lesson plans.**

The hybrid pattern — 3 per-level documents each mixing teacher notes and student content — is a specific failure mode. The teacher plan covers all levels in one document; the worksheets are student-only.

### R2 — Standard scope preservation

**Every level addresses the original standard. Every standard element stays in play across all levels — including the hard cases.**

The standard's hardest cognitive demand is exactly what below-level students most need to encounter with scaffolds, not the element to drop. Common failure modes:
- ❌ Replacing a corroboration task (compare two sources) with a single-source task for below-level students — not differentiation, just a different assignment.
- ❌ Removing the essential question from below-level work.
- ❌ Replacing argumentation with identification for below-level students.

**Engagement must be preserved at the Below tier.** Do not assign rich primary sources or compelling essential questions to At/Above and worksheet drills to Below. All tiers engage the same essential question and source context — with different supports, not different tasks.

### R3 — Teach-up via prerequisites

**Below-level scaffolds route students UP to grade-level work, grounded in the two default SS prerequisites. Not "just easier."**

- ✓ "Below-level uses a guided annotation frame (SOAPS) scaffolding the sourcing routine; students apply it to the same grade-level source task."
- ✗ "Below-level uses a shorter text / simpler vocabulary / fewer sources."

**The two SS prerequisites.** Unlike math, the KG does not provide explicit prerequisite mappings for social studies standards. The two prerequisites that apply to nearly every SS lesson are stable defaults:

1. **Content vocabulary.** The specific terms needed to access the lesson's sources and tasks are the primary gate. Extract the 4–6 key terms from the lesson's source material itself — these become the word bank. Vocabulary is a prerequisite gate, not just a UDL feature; it belongs here even though R8 also requires it as a UDL default across all tiers.

2. **Sourcing as a taught routine.** Sourcing (who produced this, why, and under what conditions?) is the foundational disciplinary skill — the prerequisite for contextualization and corroboration. Treat it as a *taught routine*, not an assumed capacity. Disciplinary thinking skills do not follow a strict grade-level progression; the question is whether the routine has been explicitly taught, not which grade introduced it. Default to a guided annotation frame (SOAPS or HAPP) as the primary below-level scaffold unless the teacher confirms sourcing is established practice in the class.

When the teacher confirms sourcing is established, shift the below-level scaffold toward contextualization support. When the lesson targets corroboration, treat sourcing + contextualization as the prerequisite baseline and scaffold from there.

#### Source complexity entry point

| Tier | Entry point |
|---|---|
| Below | Concrete / Visual — photograph, map, artifact, or heavily annotated short excerpt; 1 source; scaffolded analysis frame |
| At | Representational / Textual — leveled text or lightly annotated primary source; 1–2 sources; structured questions |
| Above | Abstract / Argumentative — full primary source(s) or complex secondary text; 2–3 sources; open synthesis or argument task |

### R4 — Below-level scaffolds

**The goal is to preserve productive struggle, not eliminate it — scaffolds support thinking without revealing answers or collapsing the historical/civic reasoning the standard requires.**

Failure modes to avoid:

- ❌ Single-cause simplification: reducing complex historical causation to one factor for below-level students. Oversimplification is not a scaffold — it undermines the disciplinary thinking the standard requires.
- ❌ Answer-embedded questions: framing questions so the historical interpretation is revealed in the question itself.
- ❌ Fill-in-the-blank narratives where students only insert pre-given facts.
- ❌ Presentism framing: simplifying historical context by using modern values without scaffolding historical context.
- ❌ Multiple-choice sourcing when the standard requires open analysis or argument.

Acceptable scaffolds:

- ✓ Sentence supports for historical/civic analysis: "This source shows ___ because ___. This matters because ___."
- ✓ Guided annotation frames (e.g., SOAPS: Source, Occasion, Audience, Purpose, Subject; or HAPP: Historical context, Audience, Purpose, Point of view) — pre-structured with prompts, not pre-filled answers.
- ✓ Tiered texts: same topic and essential question, different reading complexity. Same questions across all tiers.
- ✓ Visual primary sources (photographs, maps, political cartoons) as concrete entry points before transitioning to text-based sources.
- ✓ Word banks for discipline-specific vocabulary (not for choosing the argument or answer). Note: word banks appear on all tiers by default per R8 UDL — do not restrict them to Below only.
- ✓ Graphic organizers matched to the thinking type (see table below).
- ✓ Reduced source set with an explicit transfer step: "Analyze this one source first, then apply the same thinking to the second source."

#### Concept → primary scaffold

| Social studies thinking type | Primary scaffold |
|---|---|
| Chronological reasoning / sequence | Annotated timeline or cause-effect chain organizer |
| Primary source analysis | Guided annotation frame (SOAPS or HAPP) |
| Geographic / spatial reasoning | Labeled map with structured guiding questions |
| Civic argument / claim-based reasoning | CER (Claim-Evidence-Reasoning) frame |
| Economic decision-making / trade-offs | Cost-benefit or scarcity organizer |
| Multiple perspectives / point of view | Two-column perspective organizer |
| Comparative / synthesis | T-chart or evidence synthesis matrix |

Pick the **primary scaffold** based on the disciplinary thinking type, not the grade level. If the thinking type spans categories, pick the scaffold for the harder lift for below-level students.

The test: does the scaffold leave the disciplinary thinking to the student, or does it perform that thinking for the student? If the latter, it is not a scaffold.

#### Scaffold density cap

**Cap embedded scaffolds at 1–2 per task. DO NOT EXCEED.**

| Type | Counts toward cap? |
|---|:-:|
| Embedded — printed directly on the task (organizer, sentence support, annotation prompt) | YES |
| Header-level features — vocabulary box, sentence supports at top of worksheet | NO |
| Teacher-side tools — tiered texts available on request, conferring prompts | NO |

**Pick a primary scaffold first.** Only add a second if it contributes a genuinely different mode. If the second asks the student to do the same cognitive work, drop it.

### R5 — Required pedagogical infrastructure

**Every differentiated lesson must include all four:**

| Section | What it is | Where |
|---|---|---|
| **Formative check** | Concrete mid-lesson or end-of-lesson prompt to gauge readiness — a tiered exit ticket counts. Not "monitor students." | Teacher plan + per-level worksheet |
| **Anchor activity** | Standard-aligned task for early finishers — e.g., an additional source to analyze, a "so what?" extension question, or a connection to a current event. Not busywork. Written student-facing in `shared.anchor_activity` and printed on every worksheet — an anchor activity that exists only as a plan description is a failure. | Teacher plan + all three worksheets |
| **Flexible-grouping language** | Tier assignments tied to THIS lesson's evidence, explicitly revisable based on what the formative check reveals. Not static ability tracks. | Teacher plan |
| **Per-level misconception notes** | Common disciplinary errors specific to each level + teacher prompt + signal for pulling a small group. KG-sourced when available, drafted otherwise. | Teacher plan |

In addition: **each student worksheet ends with one open-ended or reflective prompt, present on all three tiers** — e.g., "What questions does this source raise for you?", "Whose perspective is missing from these sources?", "How does this connect to something happening today?" This is not optional for any tier. Store it as `shared.reflect_prompt` and name it in each tier's **Worksheet tasks** line in the teacher plan — a printed task the plan never mentions is a failure.

### R6 — Invisible modifications

**Same essential question / same source context / same core task across levels where pedagogically possible. Only the supports differ.**

What can differ: reading complexity of the text provided; scaffolds on the worksheet; optional teacher-provided supports during conferring; the extension or reflection prompt.

What should NOT differ: the essential question being investigated; the type of disciplinary thinking required (do not downgrade the thinking type for below-level); the historical/geographic/civic phenomenon under study.

**Do not announce scaffold removals to students.** If a scaffold appears in Task 1 but not Task 3, its absence is silent — no label, aside, or comment (e.g., no "(No annotation frame this time)" or "Try it without the organizer"). The scaffold simply does not appear; students encounter the task on its own terms.

Use the same primary source(s) across tiers by default. Source complexity may be adjusted for Below (e.g., an annotated excerpt vs. the full document) only if the core analytical task is fully preserved.

### R7 — Within-level progressive scaffolding

**Each level's worksheet sequences tasks with progressive cognitive demand.**

#### Below-level fade pattern

| Task | Embedded scaffolds | Pattern |
|---|:-:|---|
| Task 1 | Up to 2 | Scaffolded |
| Task 2 | Up to 1 | Guided |
| Task 3+ | 0 embedded | Independent |
| Exit ticket | 0–1 | Mastery check |

The goal is a true fade (2 → 1 → 0), not cosmetic variation across uniformly-dense tasks.

#### Above-level extension quality test

Every above-level extension must answer: **what new disciplinary thinking does this require that the at-level student isn't already doing?**

A real extension requires at least one of:

| Type | What it requires |
|---|---|
| New cognitive operation | At-level sources/describes; above-level corroborates, evaluates, or constructs an argument. (Bloom / Webb DOK shift.) |
| Historiographic or disciplinary insight | Surfaces a scholarly debate, interpretive tension, or methodological question — not just "what happened" but "how do we know." |
| Forward-standard preview | A real analytical demand from the forward-progression standard — not just its vocabulary. |
| Open generative task | Student produces something new: historical argument, counterargument, civic proposal, map with a claim. |

Reject if: more sources covering the same argument, notation or vocabulary swap only, or restatement.

### R8 — Scope and defaults

**If tier scope is not specified, ask ONE combined question before generating:**

> "I'll differentiate this into below / at / above grade-level tiers — are those the right three? And any specific learner needs I should know about (ELL students, IEP accommodations, reading levels)? If not, I'll apply UDL defaults (sentence stems and vocabulary support across all tiers)."

If scope is already specified, apply defaults silently and proceed.

**Defaults applied silently when not specified:**
- Tiers: below / at / above
- UDL features: sentence stems and vocabulary glossary in **all three** student worksheets (not Below only — rubric O5)
- Scope: full lesson (all phases + exit ticket)
- Number of levels: 3
- **Tier profiles (no FA data):** Below — content vocabulary gaps likely; sourcing routine not yet internalized; scaffold with guided annotation frame + word bank. At — core vocabulary mostly in place; applies sourcing and contextualization with prompting. Above — handles grade-level text independently; applies sourcing and contextualization with some independence; ready for corroboration or multi-source tasks.
- **FA follow-up prompt.** After generating the default tiered plan, ask: *"Do you have any recent signals about where students are — a vocabulary check, a prior sourcing task, or exit ticket results?"* Social studies FA data mainly helps confirm which of the two default barriers (vocabulary vs. sourcing routine) to weight more heavily — it rarely changes the scaffold type entirely. Treat this as a useful refinement, not a required input.

---

### Document content — teacher plan (`id: teacher_plan`) — max 3 pages

**Length budget: ~1,200 words rendered (the 3-page cap in practice).** Tighten the tier
sections and overview before touching the closers (Flexible Grouping, Why this works, Next
Steps) — the most common overrun is a Worksheet tasks line that restates worksheet content
instead of naming it. **"Why this works (1)" and "Why this works (2)" are required and cannot
be dropped to meet the length budget — cut tier section prose first.**

The outline below defines the content and order of the teacher plan document's `sections`:
each `##` heading becomes one section, its body becomes that section's blocks (use
`from_shared` blocks for the standard, misconceptions, and exit ticket; `labeled` blocks for
the bold fields).

```markdown
# Differentiation Plan: [Lesson Title]

**Standard:** [verbatim]  **Grade:** [X]  **State:** [X]  **Duration:** [X min]  **Discipline:** [history / civics / geography / economics]
*Learner needs: [If no specific needs were provided: "UDL defaults applied — sentence supports and vocabulary support across all tiers." If learner needs were specified, describe them here instead.]*

## Learning Objective
[Same objective across all tiers — preserved from source lesson]

## Differentiation Overview
[1 short paragraph, ≤3 sentences: approach, source complexity entry point, primary scaffold
type, essential question preserved across tiers. Standards by code + ≤10-word gist — the
target standard is already verbatim in the header.]

## Tier Design
[ONE `table` block — never three labeled paragraph stacks. Columns: Below (Group A) / At (Group B) / Above (Group C).
Rows (a cell may be "—" where a field doesn't apply to that tier):
- **Entry point / grounding** — Below: the 4–6 key vocabulary terms addressed + sourcing
  routine status (scaffolded via [annotation frame type] or established). Above: forward
  standard by code + ≤10-word gist from [state] vertical alignment. At: "—".
- **Scaffolds / extension** — fragments, ≤25 words per cell: Below scaffolds in play; At
  supports; Above extension + which R7 quality type it meets.
- **Conferring move** — one specific prompt per tier.
- **Worksheet tasks** — ≤40 words per cell, written LAST: read that tier's FINAL worksheet
  document's blocks top-to-bottom and name every printed task in order — tasks by name with
  their printed scaffolds (e.g. "Source A read (annotation guide), Sourcing organizer, Claim
  paragraph"), every tier-only add-on or extension sub-part by its printed heading, exit
  ticket, "If you finish early" anchor task, Reflect prompt. List items; don't restate their
  text. Name nothing unprinted — no "on request" supports, no planned organizer the
  worksheet dropped. Never copy another tier's cell.]

[Then ONE `callout` (note style): misconception watch — pattern + teacher prompt, ≤2
sentences per tier that needs one.]

## Formative Check
[Two required elements:
1. **Mid-lesson checkpoint:** A specific check during sourcing or analysis work — name the trigger or artifact (e.g., "After students complete the sourcing organizer, collect and scan: if fewer than half identified the author's purpose, pause and model the HAPP frame with a think-aloud before the claim paragraph"). 'Circulate and observe' does not pass.
2. **Exit ticket with explicit sort criteria:** State what a student must produce or demonstrate for THIS lesson's standard, e.g.: "Got it — [e.g., states a claim and cites two sources with sourcing reasoning] / Almost there — [e.g., states a claim and cites evidence but sourcing reasoning is missing or generic] / Needs re-teaching — [e.g., cannot state a claim independently or cites without attribution]." Generic bucket labels without lesson-specific criteria do not pass.]

## Anchor Activity
[`from_shared: anchor_activity` — the same student-facing task printed on every worksheet — plus one teacher-only line: when to deploy it and why it requires disciplinary reasoning]

## Flexible Grouping
[Current tier assignments, the evidence or basis for placement (e.g., "Placed based on prior sourcing task / exit ticket on [standard]" or "Default profile applied — no diagnostic data available"), and an explicit statement that groups are revisable after the formative check]

## Why this works (1)
[One specific tier design choice + reasoning]

## Why this works (2)
[A second specific tier design choice + reasoning]

## Next Steps
**Got it (exit ticket passes):** [connect to forward standard or upcoming lesson]
**Almost there:** [targeted small-group or conferring move — specific gap to address]
**Needs re-teaching:** [specific reteach strategy or Tier 2/3 flag if gap is persistent]

```

### Document content — worksheets (`id: worksheet_group_a` / `worksheet_group_b` / `worksheet_group_c`)

No teacher notes, look-fors, or rationale in any worksheet. All three include: vocabulary
glossary + sentence stems + the "If you finish early" anchor task + open-ended reflective
prompt (rubric O5 — UDL across all tiers) — all pulled from `shared` so they are identical
across tiers by construction.

```markdown
# [Group A / Group B / Group C] — [Lesson Title]

**Name:** _________________ **Date:** _________

## Vocabulary
[`from_shared: vocabulary` — the renderer formats the term–meaning pairs itself; never type a pipe-character table into a `text` field]

**You can use these sentence supports:**
- "This source shows ___ because ___. This matters because ___."
- "My strategy was ______ because ______."

---

[Tasks pulled ONE AT A TIME, each with its scaffold directly above it — per task N: at most
ONE scaffold block (Below only, "For Task N — ...", per R4/R7 fade), then
`{"type": "from_shared", "key": "tN", "label": "N"} followed by a workspace block`. Source-analysis task text
identical on all three tiers; never re-typed. Writing space after each task is automatic —
do not add answer boxes for tasks.]
[Tier-only add-ons (e.g. Above "Go further" extension) as their own headed sections]

---

## If you finish early
[`from_shared: anchor_activity` — identical block on all three tiers]

## Reflect
[`from_shared: reflect_prompt` — identical question on all three tiers]
```

---

## Writing differentiation.json — social studies mapping

- `shared.subject`: `"Social Studies"`
- `shared.anchor_task`: the essential/compelling question
- `shared.t1`..`tN`: the source analysis tasks shared by ALL tiers, one task per key — faceted {teacher: "the difficulty and what to watch for, as a plain sentence", student: <the task>}
- Teacher document: differentiation plan, max 3 pages; worksheets max 2 pages each
- **Copyright:** do NOT reproduce primary source text or curriculum source-set descriptions verbatim — provide citations and pointers only; student-facing analysis tasks must be original.

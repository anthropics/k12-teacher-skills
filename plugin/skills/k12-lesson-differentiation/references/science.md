<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->

# Science — differentiation pedagogy

Loaded by `k12-lesson-differentiation` when the subject is **science**.

## Identify the source lesson

Three scenarios — detect which applies:

**Scenario A — Source lesson exists in the prior conversation**
If a lesson was produced or discussed earlier in this conversation, use it directly. Do NOT re-ask the teacher to share it.

**Scenario B — Teacher uploads a source lesson**
Read the file first. Confirm: grade level, Performance Expectation (PE), anchoring phenomenon, lesson structure and phases, which SEP(s) and CCC(s) are foregrounded. If the file is unreadable on first attempt, surface the error clearly and ask the teacher to re-share. Do NOT silently fabricate a lesson.

**Scenario B2 — Teacher links a source lesson by URL**
Fetch the URL and read its content first. Then confirm grade level, Performance Expectation (PE), anchoring phenomenon, lesson structure and phases, and foregrounded SEP(s)/CCC(s) exactly as in Scenario B. If the fetch fails or returns unusable content, surface the error clearly and ask the teacher to paste the lesson text or upload the file. Do NOT silently fabricate a lesson.

**Fetching the lesson completes Step 1 only — it does NOT replace standards grounding.** Continue to Step 2 — Ground in standards. Skipping Step 2 after a URL fetch is the same critical failure as skipping it for an uploaded lesson.

**Scenario C — No source lesson present**
Ask before proceeding:
> "Happy to differentiate. Do you have a specific lesson in mind? You can paste it, share a file, or tell me the grade + topic + standard and I'll work from that."

**Detect OpenSciEd use.** OpenSciEd is confirmed when either:
1. The teacher explicitly says so: "OpenSciEd," "OSE," "we use OpenSciEd"
2. The uploaded source lesson contains OSE structural markers:
   - Driving Question Board (DQB) references
   - Scientists Circle or consensus model activities
   - "What are we figuring out?" framing in the objective

**Teacher's explicit statement wins over signal from provided lesson.** If the teacher says "I use
OpenSciEd" and the provided lesson has any curriculum branding, treat as OSE-confirmed.

---

## Standards grounding

Follow **Step 2 — Ground in standards** in SKILL.md: if the Learning Commons Knowledge Graph
is connected, use the Science section of `references/learning-commons-kg.md`; if not,
proceed from best knowledge and add the disclaimer footer to the teacher plan.

**State-aware standards:** When state is known from Step 0, pass relevant jurisdiction in KG call.


## The differentiation rules

Apply all eight rules to every differentiated lesson.

### R1 — Output structure

**1 integrated teacher-facing lesson plan + 3 pure student-ready worksheets. NEVER 3 separate per-level lesson plans.**

The lesson plan is a single document the teacher can use instead of (or alongside) the source lesson. Organized by lesson phase. Phases where all students work together (Launch Phenomenon, Sensemaking Discussion, Synthesis) are written once. Phases where students work independently (Investigation, explanation/CER task) show all three tiers in stacked labeled blocks.

Do not produce 3 documents that each mix teacher notes and student tasks.

### R2 — Three-dimensional scope preservation

**Every tier addresses the original PE. Every SEP, CCC, and DCI element must appear in all tiers — including the hard cases.**

For states other than Texas, all three NGSS dimensions are non-negotiable:
- **SEP**: the same foregrounded practice(s) appear in every tier's task (e.g., if the lesson foregrounds "Constructing Explanations," every tier constructs an explanation)
- **CCC**: the same crosscutting concept lens is applied in every tier
- **DCI**: the same disciplinary core idea is the content target for all tiers

Reducing cognitive scope for below-level students — removing a dimension, replacing investigation with a reading, or simplifying the phenomenon — is not differentiation.

**Engagement must be preserved at the Below tier.** Do not give At/Above tiers interesting open-ended investigations and give Below tier a structured worksheet while others do science. All tiers investigate the same phenomenon — with different supports, not different tasks.

### R3 — Teach up via the Observation → Representation → Explanation progression

**Below-level scaffolds route students UP to grade-level explanation, not around it. Not "just simpler tasks."**

| Tier | Entry point in the O→R→E progression |
|---|---|
| Below | Observation → Representation (structured, with supports), then into Explanation with scaffolded CER frame |
| At | Representation → Explanation (standard CER) |
| Above | Explanation → Extension (generalization, counter-phenomenon, quantification, engineering application) |

**Below-level scaffolds must:**
- Help students access and make sense of their observations (structured observation prompts, annotated diagrams)
- Provide a scaffold for moving from observation to a data representation (guided data table, partial model template to populate)
- Support construction of a CER with a sentence support — NOT provide the explanation itself

**The sensemaking conflict is non-negotiable.** Do not smooth over the cognitive conflict between prior conception and observation for below-level students — help them name it: *"I thought ____ but I observed ____. Now I think ____."*

**Identifying the conceptual prerequisite:**
Use the DCI code from the PE. NGSS DCI progressions are explicit — the same core idea appears at K–2, 3–5, 6–8, and 9–12 at increasing sophistication. Identify what conceptual model students at the prior grade band built for this DCI and use that as the below-level scaffold's bridge. Name it in the Three-Dimensional Map as the prerequisite. This is typically a within- or adjacent-grade-band conceptual dependency, not a cascading cross-grade chain.

- ✓ "Below-level uses [prior grade band's model of energy transfer]; students apply that representation to explain the new phenomenon."
- ✗ "Below-level gets an easier version of the investigation."

### R4 — Below-level scaffolds

**The goal is to preserve productive struggle through sensemaking, not eliminate it. Scaffolds support students through the inquiry, not around it. NEVER route below-level students away from the investigation.**

Failure modes to avoid:

- ❌ Pre-telling the explanation before students investigate.
- ❌ Removing investigation for below-level students — giving them a reading or video while other students investigate.
- ❌ Simplifying the phenomenon — all tiers observe the same phenomenon.
- ❌ Keyword strategies: "Look for the word 'heat' — that means energy transfer."
- ❌ Answer-revealing support stations.
- ❌ Literacy-only scaffolding as a substitute for science practice scaffolding.

Acceptable scaffolds:

- ✓ **Guiding/analysis questions** that sequence observation → connection → meaning: *"What changed? What stayed the same? What do you think caused that?"*
- ✓ **Sentence supports for CER**: *"I claim ____. My evidence is ____. This supports my claim because ____."*
- ✓ **Partial model templates** — a structured diagram students populate, not a completed diagram they label.
- ✓ **Vocabulary support** — word banks or brief glossaries at the top of the task (header-level). Include everyday-language definition.
- ✓ **Structured observation sheet** with explicit prompts (*"Draw what you see. Label any changes. Circle anything unexpected."*)
- ✓ **Guided data table** with column headers and units pre-filled — students fill in observations, not the interpretation.
- ✓ **Prior knowledge activation** — *"Remember when we figured out [prior concept]? How might that help explain what you're seeing now?"*

#### Scaffold density cap

**Cap embedded scaffolds at 1–2 per task. DO NOT EXCEED.**

| Type | Counts toward cap? |
|---|:-:|
| Embedded — printed on every problem or task (organizer, sentence support, hint text) | YES |
| Header-level features — vocabulary box, CER frame at top of worksheet | NO |
| Teacher-side tools — support stations available on request, conferring prompts | NO |

Pick a primary scaffold first. Only add a second if it contributes a genuinely different mode. If the second covers the same cognitive ground, drop it.

### R5 — Required pedagogical infrastructure

**Every differentiated science lesson must include all five. Embedded inline within the lesson plan.**

| Element | What it is | Where in lesson plan |
|---|---|---|
| **Formative check** | Concrete mid-lesson or end-of-lesson prompt — exit ticket or CER check. Not "circulate and observe." | Inline in the phase where it occurs |
| **Anchor activity** | A standard-aligned extension for early finishers. Not busywork — must require the foregrounded SEP. Written student-facing in `shared.anchor_activity` and printed on every worksheet — an anchor activity that exists only as a plan description is a failure. | End of lesson plan + all three worksheets |
| **Flexible-grouping language** | Tier assignments tied to THIS lesson's evidence; revisable during lesson based on the formative check. | Compact callout box in lesson header |
| **Per-level misconception notes** | Common science misconceptions at each level + teacher conferring move + signal for small group. | Inline callout within each tiered activity block — max 2 sentences per level |
| **Sensemaking conflict prompt** | A prompt that explicitly surfaces the tension between prior conception and observation. | Embedded in the Investigation or CER task |

**If OSE-confirmed, three additional elements are non-negotiable across all tiers:**
- **Consensus model** — all tiers contribute to and revise the class consensus model. Below: partial model template. At: blank model. Above: extend the model to account for an additional case.
- **Driving question board** — all tiers add to and reference the DQB.
- **CER structure** — consistent across tiers; only the frame support differs (Below: sentence support. At: prompt only. Above: counter-argument + rebuttal added.)

In addition: **each student worksheet ends with one reflective prompt, present on all three tiers:** *"What are you still wondering about?"* Store it as `shared.reflect_prompt` and name it in each tier's **Worksheet tasks** line in the lesson plan — a printed task the plan never mentions is a failure.

### R6 — Invisible modifications

**Same phenomenon, same investigation, same core explanation task across levels. Only the supports differ.**

All tiers observe the same phenomenon. All tiers investigate with the same materials and procedure. In the integrated lesson plan, the shared investigation and phenomenon appear once under "ALL STUDENTS." The tier blocks show only what differs — scaffolds, conferring prompts, extension.

Do not restate the full investigation text in every tier block — reference it and describe only what differs.

**Do not announce scaffold removals to students.** If a structured observation sheet is used in Task 1 but not Task 3, its absence is silent — no label, aside, or comment (e.g., no "(No template this time)" or "Try it without the frame"). The scaffold simply does not appear; students encounter the task on its own terms.

Numbers, data sets, and material quantities should be identical across tiers by default. May be adjusted for Below only if the investigative structure is fully preserved.

### R7 — Within-level progressive scaffolding

**Each level's worksheet sequences tasks with progressive cognitive demand.**

#### Below-level fade pattern

| Task | Embedded scaffolds | Pattern |
|---|:-:|---|
| Observation task | Up to 2 | Structured |
| Representation task | Up to 1 | Guided |
| CER task | 0–1 embedded (frame at header level OK) | Productive struggle |
| Reflection prompt | 0 | Independent |

#### Above-level extension quality test

Every above-level extension must answer: **what new thinking does this require that the at-level student isn't already doing?**

A real extension requires at least one of:
- **Engineering application**: design a solution using the science concept
- **Counter-phenomenon or anomalous case**: a situation where the phenomenon behaves differently, requiring generalization
- **Quantification**: connect the qualitative explanation to a mathematical relationship (grades 3+)
- **Forward PE preview**: the next NGSS PE in the DCI progression — conceptual element, not just vocabulary
- **Scientific argumentation**: evaluate a competing explanation, find evidence to challenge their own claim, or write a rebuttal
- **Societal/ethical dimension**: how does this phenomenon connect to a real-world problem or decision? (grades 6–12)

Reject if: more of the same investigation, a longer worksheet, or a notation swap only.

### R8 — Scope and defaults

**If tier scope is not specified, ask ONE combined question before generating:**

> "I'll differentiate this into below / at / above grade-level tiers — are those the right three? And any specific learner needs I should know about (ELL levels, IEP goal areas)? If not, I'll apply UDL defaults (sentence supports and vocabulary support across all tiers)."

If scope is already specified, apply defaults silently and proceed.

**Defaults applied silently when not specified:**
- Tiers: below / at / above
- UDL features: CER sentence supports and vocabulary glossary in **all three** student worksheets (not Below only — rubric O5)
- Scope: full lesson (all phases + exit ticket / CER task)
- OSE structure: applied if OSE-confirmed; not applied otherwise

**When no formative assessment data is available**, default to this below-level profile:
- Has observational access to the phenomenon but cannot yet name the mechanism — perceptual access without explanatory language
- Likely holds at least one common misconception for this DCI; the sensemaking conflict frame (*"I thought ____ but I observed ____"*) is the primary scaffold
- Can produce an observation but needs structure to connect it to a model or CER independently
- The proximate conceptual prerequisite (identified per R3) may not be secure

Design default below-level scaffolding accordingly: structured observation prompts → misconception-surfacing sentence support → CER frame. Do not pre-scaffold the explanation content.

If the inferred gap is wider than one within-band conceptual step, add a flag to the Next Steps block that Tier 2/3 support may be needed beyond lesson-level differentiation.

After generating the default tiered plan, prompt the teacher: *"Do you have any notes from the last lesson — observation notes, CER samples, or exit ticket results — that could tell me which misconception is active, or whether students could access the phenomenon but struggled to explain it?"* This can replace the assumed misconception with a confirmed one and clarify whether students are stuck at the observation→representation step or the representation→explanation step, shifting where the scaffold focuses. FA data rarely inverts the default approach in science but meaningfully sharpens it.

---

### Document content — integrated lesson plan (`id: teacher_plan`) — max 5 pages

Organized by phase. Reproduce the source lesson's phase structure (e.g., Launch Phenomenon → Investigation → Sensemaking Discussion → Explanation Task → Synthesis → Exit Ticket). Do not invent phases not present in the source.

The outline below defines the content and order of this document's `sections`: each `##`
heading becomes one section, its body becomes that section's blocks (use `from_shared` blocks
for the PE, misconceptions, and exit ticket; `phase_header` blocks for phases; `labeled` blocks
for the bold fields).

**Length budget: ~2,000 words rendered (the 5-page cap in practice).** Tighten the phase and
tier sections before touching the closers (Why this works, Next Steps) — the most common
overrun is a Worksheet tasks line that restates worksheet content instead of naming it.
**"Why this works (1)" and "Why this works (2)" are required and cannot be dropped to meet the
length budget — cut phase or tier section prose first.**

```markdown
# Differentiated Lesson Plan: [Lesson Title]

**PE:** [verbatim]  **Grade:** [X]  **Duration:** [X min]
**Anchoring Phenomenon:** [one sentence]
*Learner needs: [If no specific needs were provided: "UDL defaults applied — CER sentence supports and vocabulary support across all tiers." If learner needs were specified, describe them here instead.]*

## Learning Objective
[One statement covering all tiers. For OSE-confirmed: "Students will figure out [DCI element] by using [SEP] to make sense of [phenomenon]."]

## Three-Dimensional Map
- **SEP(s):** [name + ≤10-word gist — the PE is already quoted verbatim in the header]
- **CCC(s):** [name + ≤10-word gist]
- **DCI:** [brief]
- **Conceptual prerequisite:** [code + ≤10-word gist] — grounds Below scaffolds
- **Forward PE:** [code + ≤10-word gist] — grounds Above extension

(Density rule applies: the PE appears verbatim exactly once, in the header. Never re-paste
full standard text in this map — code + gist only.)

## Tier Grouping
[One bullet per tier, ≤15 words each: the placement signal for that tier.]
[Then ONE sentence: evidence basis ("Based on prior CER exit ticket on [PE]" or "Default
profile applied — no FA data available").]
*Tier assignments are revisable — revisit after the formative check.*

---

## [Phase Name — whole class]
[Teacher facilitation moves, key questions, what NOT to do. For OSE-confirmed: consensus model update move + DQB reference.]

## [Phase Name — tiered activity]
**ALL STUDENTS:** [shared setup — same phenomenon, same materials; ONE sentence]

[ONE `table` block — never three labeled paragraph stacks. Columns: Below (Group A) / At (Group B) / Above (Group C).
Two rows:
- **Students do** — ≤25 words per cell, fragments not sentences: the task path and the
  scaffolds in play (plus the extension prompt in the Above cell).
- **Worksheet tasks** — ≤40 words per cell, written LAST: read that tier's FINAL worksheet
  document's blocks top-to-bottom and name every printed task in order — investigation/CER
  tasks by name with their printed scaffolds (e.g. "Observation sheet (structured), CER
  paragraph (frame)"), every tier-only add-on or extension sub-part by its printed heading,
  exit ticket, "If you finish early" anchor task, Reflect prompt. List items; don't restate
  their text. Name nothing unprinted — no "on request" supports, no planned organizer the
  worksheet dropped. Never copy another tier's cell.]

[Then ONE `callout` (note style): misconception watch + conferring move — one sentence per
tier that needs one, ≤2 sentences per level. Never bury these inside the table cells or a
paragraph.]

## Formative Check
[Two required elements:
1. **Mid-lesson checkpoint:** A specific check during the investigation or sense-making phase — name the trigger or artifact (e.g., "After the observation table is complete, scan three notebooks: if students are describing observations without connecting to the phenomenon, pause and use the CCC prompt before the CER task"). 'Circulate and observe' does not pass.
2. **Exit ticket with explicit sort criteria:** State what a student must produce or demonstrate for THIS lesson's PE, e.g.: "Got it — [e.g., writes a CER that names the specific mechanism and cites data from the investigation] / Almost there — [e.g., claim and evidence present but reasoning does not connect to the DCI] / Needs re-teaching — [e.g., cannot state a claim from the data without prompting]." Generic bucket labels without lesson-specific criteria do not pass.]

## Anchor Activity
[`from_shared: anchor_activity` — the same student-facing task printed on every worksheet — plus one teacher-only line: when to deploy it; must require the foregrounded SEP]

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

No teacher notes, look-fors, or rationale in any worksheet. Vocabulary, CER sentence supports,
the "If you finish early" anchor task, and the reflective prompt are pulled from `shared` so
they are identical across tiers by construction.

On the printed page, never label anything "CER" or "sensemaking" — those are teacher terms
(see SKILL.md, Student-facing language). Organizer labels read *Claim / Evidence /
Reasoning*; the sensemaking frame is introduced as *"Check your thinking"*.

| Level | Worksheet features |
|---|---|
| Below | Same phenomenon and investigation as At. Scaffolds embedded per R4 with fade pattern per R7. Structured observation sheet, partial model template, CER sentence support at header level. |
| At | Source worksheet preserved or lightly reformatted. Standard CER prompt. |
| Above | Same investigation + extension prompt per R7. CER + counter-argument / rebuttal prompt. |

```markdown
# [Group A / Group B / Group C] — [Lesson Title]

**Name:** _________________ **Date:** _________

## Vocabulary
[`from_shared: vocabulary` — the renderer formats the term–meaning pairs itself; never type a pipe-character table into a `text` field]

**You can use these sentence supports:**
- "I claim ____. My evidence is ____. This supports my claim because ____."
- "I thought ____ but I observed ____. Now I think ____."

---

[Tasks pulled ONE AT A TIME, each with its scaffold directly above it — per task N: at most
ONE scaffold block (Below only, "For Task N — ...", per R4/R7 fade), then
`{"type": "from_shared", "key": "tN", "label": "N"} followed by a workspace block`. Investigation/CER task text
identical on all three tiers; never re-typed. Writing space after each task is automatic —
do not add answer boxes for tasks.]
[Tier-only add-ons (e.g. Above "Go further" extension) as their own headed sections]

---

## If you finish early
[`from_shared: anchor_activity` — identical block on all three tiers]

## Reflect
[`from_shared: reflect_prompt` — "What are you still wondering about?"]
```

---

## Writing differentiation.json — science mapping

- `shared.subject`: `"Science"`
- `shared.standard_code` / `shared.standard_text`: the Performance Expectation, verbatim
- `shared.anchor_task`: the anchoring phenomenon
- `shared.t1`..`tN`: the investigation and CER tasks shared by ALL tiers, one task per key — faceted {teacher: "the difficulty and what to watch for, as a plain sentence", student: <the task>}
- `shared.sentence_frames`: CER frames as plain text with blanks sized for handwriting, placed with the task's writing space
- Teacher document: **integrated differentiated lesson plan** (organized by phase), max 5 pages; worksheets max 2 pages each
- **Copyright:** do NOT reproduce OpenSciEd (OSE) student-facing text verbatim — this applies to investigation instructions, phenomenon descriptions, and CER prompts drawn from OSE materials.

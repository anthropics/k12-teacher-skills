<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->

# Math — differentiation pedagogy

Loaded by `k12-lesson-differentiation` when the subject is **math**.

## Identify the source lesson and curriculum

**Detect IM use.** Before anything else, check whether the teacher is using Illustrative Mathematics. Look for signals anywhere in the conversation: explicit name ("IM", "Illustrative Mathematics", "IM 360"), IM-specific terminology (MLRs, cool-down, "Stronger and Clearer Each Time", launch-explore-discuss structure, IM unit or lesson references), or an uploaded IM teacher guide. If confirmed, treat as **IM-confirmed** throughout — use IM discourse language and structures in the teacher plan.

Then detect which scenario applies:

**Scenario A — Source lesson exists in the prior conversation**
If a lesson was produced or discussed earlier in this conversation, use it directly. Do NOT re-ask the teacher to share it.

**Scenario B — Teacher uploads a source lesson**
Read the file first. Confirm: grade level, subject, standard, learning objective, lesson structure. If the file is unreadable on first attempt, surface the error clearly and ask the teacher to re-share. Do NOT silently fabricate a lesson.

**Scenario B2 — Teacher links a source lesson by URL**
Fetch the URL and read its content first. Then confirm grade level, subject, standard, learning objective, and lesson structure exactly as in Scenario B. If the fetch fails or returns unusable content, surface the error clearly and ask the teacher to paste the lesson text or upload the file. Do NOT silently fabricate a lesson.

**Fetching the lesson completes Step 1 only — it does NOT replace standards grounding.** Continue to Step 2 — Ground in standards. Skipping Step 2 after a URL fetch is the same critical failure as skipping it for an uploaded lesson.

**Scenario C — No source lesson present**
Ask before proceeding:
> "Happy to differentiate. Do you have a specific lesson in mind? You can paste it, share a file, or tell me the grade + topic + standard and I'll work from that."

---

## Standards grounding

Follow **Step 2 — Ground in standards** in SKILL.md: if the Learning Commons Knowledge Graph
is connected, use the Math section of `references/learning-commons-kg.md`; if not,
proceed from best knowledge and add the disclaimer footer to the teacher plan.

## The differentiation rules

Apply all eight rules to every differentiated lesson.

### R1 — Output structure

**1 cohesive teacher-facing differentiation plan + 3 pure student-ready worksheets. NEVER 3 hybrid per-level lesson plans.**

The hybrid pattern — 3 per-level documents each mixing teacher notes and student problems — is a specific failure mode. The teacher plan covers all levels in one document; the worksheets are student-only.

### R2 — Standard scope preservation

**Every level addresses the original standard. Every standard element stays in play across all levels — including the hard cases.**

The standard's hardest case is exactly what below-level students most need to encounter with scaffolds, not the case to drop. Reducing the standard's cognitive scope for below-level students is not differentiation.

**Engagement must be preserved at the Below tier.** Do not assign interesting real-world problem contexts to At/Above and procedural drill to Below. The same scenario, the same hook — with different supports. This is both a rigor and equity requirement.

### R3 — Teach-up via named prerequisite

**Below-level scaffolds route students UP to grade-level work, grounded in a named prerequisite. Not "just easier."**

- ✓ "Below-level uses [visual model] to surface the [concept] from [prior standard]; students apply that representation to the grade-level problem."
- ✗ "Below-level uses simpler numbers / shorter text / fewer steps."

#### Standards framework detection

Before identifying the prerequisite, determine which framework the teacher's standard belongs to. Run the following fallback chain and stop at the first step that yields a result:

1. KG lookup — call find_standards_progression_from_standard with the teacher's standard code. If the KG returns a predecessor standard for the teacher's framework, use it verbatim. This is the preferred path regardless of whether the framework is CCSS, TEKS, or another state system.

2. **Partial match** — the closest Common Core prerequisite standard(s) plus their **learning components** (the standard broken into smaller sub-skills). The teacher's framework has no exact equivalent, so present the standard as a CCSS proxy, and use the learning components to pick the specific prior sub-skill the Below-tier scaffold builds from.
**Output rule for non-CCSS frameworks:** When the CCSS proxy path is taken, do not put CCSS
codes in the main teacher plan body. Use plain-language descriptions instead:
- In Differentiation Overview: "Below-tier scaffolds build from prior understanding of
  [concept description], the prerequisite for [grade-level concept]."
- In Grounded in prerequisite: "Prerequisite concept: [plain description] — aligns to
  [CCSS proxy code] as reference, used because TEKS progressions are not yet in the KG."
- Move the CCSS code to a single footnote at the bottom of the teacher plan: "* Prerequisite
  grounding uses CCSS [code] as the closest aligned standard for TEKS [teacher's code]."
A Texas teacher's plan should not contain CCSS codes in prominent positions.

3. **Concept-level fallback** — if no CCSS analog exists, describe the prerequisite as a concept in plain language: *"Prerequisite concept: [description] — specific standard not available for this state framework."*

The teacher plan's **Grounded in prerequisite** line must reflect which path was taken. Never leave this line blank or generic — a concept-level description is always achievable even when a standard code is not.

**Why prerequisites are non-negotiable in math.** Unlike ELA or science, where "same objective, different access" is often sufficient, math learning is compounding: a student without the prior-grade concept cannot make sense of the current one through scaffolding alone. The prerequisite gap is typically the actual obstacle, not the current-grade concept. Designing around prerequisite identification — as is appropriate for other subjects — would be a pedagogical compromise in math.

#### CRA entry point

| Tier | CRA entry point |
|---|---|
| Below | Concrete (manipulative or physical model) → Representational (diagram, visual model) |
| At | Representational → Abstract (symbolic, numeric) |
| Above | Abstract → Connection (generalization, structural insight, forward standard) |

### R4 — Below-level scaffolds

**Scaffolds support thinking without revealing answers. NEVER answer-revealing hints. NEVER keyword strategies.**

Failure modes:
- ❌ Keyword strategies ("Look for 'together' — that means combining") — undermines standards that test against shortcuts
- ❌ Algorithm pre-teaching before conceptual understanding
- ❌ Pre-filled templates leaving only the answer blank
- ❌ Multiple-choice when original task requires open production

Acceptable scaffolds:
- ✓ Sentence supports: "I know ____ and ____. The part I don't know is ____."
- ✓ Visual organizers matched to the mathematical concept (see table).
- ✓ Manipulative or concrete prompts bridging to the abstract task (CRA per R3)
- ✓ Word banks for vocabulary (not for choosing the answer)
- ✓ Reduced complexity with explicit transfer step: "Try with these first, then apply to the original problem."

#### Concept → primary visual model

| Math concept type | Primary visual model |
|---|---|
| Part-whole / additive reasoning | Tape diagram or part-whole diagram |
| Multiplicative / ratio / rate reasoning | Double number line or ratio table |
| Fractions as quantities on a number line | Number line |
| Area / multiplication structure | Area model or array |
| Proportional relationships / linear functions | Table of values or coordinate graph |
| Algebraic structure / equation reasoning | Equation balance model or variable representation |
| Geometric relationships | Labeled diagram with annotated parts |

#### Scaffold density cap

**Cap embedded scaffolds at 1–2 per problem.**

| Type | Counts toward cap? |
|---|:-:|
| Embedded — printed on every problem (organizer, sentence support, hint text) | YES |
| Header-level — vocabulary box, sentence supports at top of worksheet | NO |
| Teacher-side — manipulatives on request, conferring prompts | NO |

Pick a primary scaffold first. Only add a second if it contributes a genuinely different mode. If the second does the same cognitive work as the primary, drop it.

### R5 — Required pedagogical infrastructure

**Every differentiated lesson must include all four:**

| Section | What it is | Where |
|---|---|---|
| **Formative check** | Tiered exit ticket or mid-lesson prompt. Not "monitor students." | Teacher plan + per-level worksheet |
| **Anchor activity** | Standard-aligned task for early finishers. Not busywork. Written student-facing in `shared.anchor_activity` and printed on every worksheet — an anchor activity that exists only as a plan description is a failure. | Teacher plan + all three worksheets |
| **Flexible-grouping language** | Tier assignments tied to THIS lesson's evidence, explicitly revisable after the formative check. Not static ability tracks. | Teacher plan |
| **Per-level misconception notes** | Error pattern + teacher prompt + small-group signal. KG-sourced when available. | Teacher plan |

**Every worksheet ends with one open-ended reflective prompt, on all three tiers** — e.g., "Explain your thinking," "What strategy did you use and why?" Not optional for any tier. Store it as `shared.reflect_prompt` and name it in each tier's **Worksheet tasks** line in the teacher plan — a printed task the plan never mentions is a failure. (Rubric R3.)

### R6 — Invisible modifications

**Same story / same context / same core problem across levels. Only the supports differ.**

What can differ: scaffolds on the worksheet; teacher conferring supports; extension prompt depth.

What must NOT differ: the problem context; the core question; the structural challenge the standard targets.

**Do not announce scaffold removals to students.** If a scaffold appears on Problem 1 but not Problem 3, its absence is silent — no label, aside, or comment (e.g., no "(No organizer this time)" or "Try it without the diagram"). The scaffold simply does not appear; students encounter the problem on its own terms.

Same numbers by default. Numbers may change for Below only if mathematical structure is fully preserved — do not eliminate the key challenge (e.g., do not convert fractions to whole numbers).

### R7 — Within-level progressive scaffolding

**Each worksheet sequences problems with progressive cognitive demand.**

#### Below-level fade pattern

| Problem | Embedded scaffolds | Pattern |
|---|:-:|---|
| Problem 1 | Up to 2 | Scaffolded |
| Problem 2 | Up to 1 | Guided |
| Problem 3+ | 0 embedded | Independent |
| Exit ticket | 0–1 | Mastery check |

#### Above-level extension quality test

Every above-level extension must answer: **what new thinking does this require that the at-level student isn't already doing?**

| Type | What it requires |
|---|---|
| New cognitive operation | At-level applies; above-level analyzes, evaluates, or creates (Bloom/DOK shift) |
| Structural insight | Generalization, equivalence, or inverse relationship the at-level treats as a single instance |
| Forward-standard preview | A real conceptual element from a higher-grade standard — not just notation or vocabulary |
| Open generative task | Student writes a problem, designs a counterexample, or constructs an argument from scratch |

Reject if: notation swap only, more of the same, or restatement.

### R8 — Scope and defaults

**If tier scope is not specified, ask ONE combined question:**

> "I'll differentiate this into below / at / above grade-level tiers — are those the right three? And any specific learner needs I should know about? If not, I'll apply UDL defaults (sentence stems and vocabulary support across all tiers)."

**Defaults applied silently:**
- Tiers: below / at / above
- UDL features: sentence stems and vocabulary glossary in **all three** student worksheets (not Below only — rubric O5)
- Scope: full lesson including exit ticket

**FA follow-up prompt — ask after generating the default plan:**

> "Do you have any exit ticket results, diagnostic scores, or notes on where students got stuck — for example, whether they understood the concept but lost the procedure, or seemed confused about what the concept means?"

This prompt fires *after* the tiered plan is delivered, not before. In math, FA data can change which scaffold type is appropriate (conceptual vs. procedural), not just refine an existing approach — the highest-stakes follow-up of any subject. Even informal teacher observation ("they froze when I showed them the area model") is useful signal for targeting the prerequisite warm-up.

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

**Standard:** [verbatim]  **Grade:** [X]  **Duration:** [X min]  **Curriculum:** [IM / General]
*Learner needs: [If no specific needs were provided: "UDL defaults applied — sentence supports and vocabulary support across all tiers." If learner needs were specified, describe them here instead.]*

## Learning Objective
[Same objective across all tiers — preserved from source lesson]

## Differentiation Overview
[1 short paragraph, ≤3 sentences: approach, prerequisite named by code + short gist,
forward standard named by code + short gist. Never paste full standard text here — the
target standard is already verbatim in the header. Use KG-returned state standard (preferred when state is known and KG has it), CCSS proxy with reference in footnote, or concept-level fallback.]

## Tier Design
[ONE `table` block — never three labeled paragraph stacks. Columns: Below (Group A) / At (Group B) / Above (Group C).
Rows (a cell may be "—" where a field doesn't apply to that tier):
- **Grounded in** — Below: prerequisite by code + gist (or "CCSS proxy: [code]" / "Prerequisite
  concept: [description]" per whichever R3 path applied). Above: forward standard by code +
  gist. At: "—".
- **Scaffolds / extension** — fragments, ≤25 words per cell: Below scaffolds in play; At
  supports; Above extension + which R7 quality type it meets.
- **Conferring move** — one specific prompt per tier.
- **Worksheet tasks** — ≤40 words per cell, written LAST: read that tier's FINAL worksheet
  document's blocks top-to-bottom and name every printed task in order — problems by number
  with their printed scaffolds (e.g. "P1 (tape diagram + frame), P2 (frame), P3"), every
  tier-only add-on or extension sub-part by its printed heading, exit ticket, "If you finish
  early" anchor task, Reflect prompt. List items; don't restate their text. Name nothing
  unprinted — no "on request" supports, no planned organizer the worksheet dropped. Never
  copy another tier's cell.]

[Then ONE `callout` (note style): misconception watch — pattern + teacher prompt, ≤2
sentences per tier that needs one. Never bury these in the table or a paragraph.]

## Formative Check
[Two required elements:
1. **Mid-lesson checkpoint:** A specific check during work time — name the trigger or artifact (e.g., "After P2, scan whiteboards: if fewer than half show a correct representation, pause and remodel with a tape diagram before P3"). 'Circulate and observe' does not pass.
2. **Exit ticket with explicit sort criteria:** State what a student must produce or demonstrate to land in each bucket for THIS lesson, e.g.: "Got it — [e.g., solves a parallel problem and explains strategy in a sentence] / Almost there — [e.g., correct answer but no explanation or one step missing] / Needs re-teaching — [e.g., cannot set up the representation independently]." Generic bucket labels without lesson-specific criteria do not pass.]

## Anchor Activity
[`from_shared: anchor_activity` — the same student-facing task printed on every worksheet — plus one teacher-only line: when to deploy it and why it requires mathematical reasoning]

## Flexible Grouping
[One bullet per tier, ≤15 words each: the placement signal for that tier.]
[Then ONE sentence: evidence basis (e.g., "Placed based on prior exit ticket on [standard]"
or "Default profile applied — no diagnostic data available").]
*Groups are revisable — revisit after the formative check.*

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

No teacher notes, look-fors, or rationale. All three include: vocabulary glossary + sentence
frames + the "If you finish early" anchor task + open-ended reflective prompt (rubric O5 —
UDL across all tiers) — all pulled from `shared` so they are identical across tiers by
construction. The outline below defines each worksheet document's `sections`:

```markdown
# [Group A / Group B / Group C] — [Lesson Title]

**Name:** _________________ **Date:** _________

## Vocabulary
[`from_shared: vocabulary` — the renderer formats the term–meaning pairs itself; never type a pipe-character table into a `text` field]

**You can use these sentence supports:**
- "I know ____ and ____. The part I don't know is ____."
- "My strategy was ______ because ______."

---

[Problems pulled ONE AT A TIME, each with its scaffold directly above it — per problem N:
at most ONE scaffold block (Below only, "For Problem N — ...", per R4/R7 fade), then
`{"type": "from_shared", "key": "tN", "label": "N"} followed by a workspace block`. Problem text identical on all
three tiers; never re-typed. Work space after each problem is automatic — do not add
answer boxes for problems.]
[Tier-only add-ons (e.g. Above "Go further" extension) as their own headed sections]

---

## If you finish early
[`from_shared: anchor_activity` — identical block on all three tiers]

## Reflect
[`from_shared: reflect_prompt` — identical question on all three tiers]
```

---

## Writing differentiation.json — math mapping

- `shared.subject`: `"Mathematics"`
- `shared.anchor_task`: the shared problem context / hook
- `shared.t1`..`tN`: the core problem set shared by ALL tiers, one task per key — faceted {teacher: "the difficulty and what to watch for, as a plain sentence", student: <the problem>}
- Teacher document: differentiation plan, max 3 pages; worksheets max 2 pages each
- **Copyright:** do NOT reproduce Illustrative Mathematics (IM) student-facing text verbatim — problem contexts, activity narratives, and cool-down prompts from IM materials must be rewritten as original content.

<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-License-Identifier: Apache-2.0
-->

# Cross-curricular integration

Read this file IN ADDITION to the primary subject's reference file when the teacher wants
one subject's lesson or materials to carry a second subject: "tie my fractions unit to our
weather science unit," "my ELA block needs to cover the Revolution content too," "a reading
passage that also hits MS-LS2-3." The primary subject's file governs pedagogy, structure,
grade-band rules, and output mapping; this file adds only what changes when a supporting
subject rides along.

---

## Primary vs. supporting subject

Every cross-curricular lesson still has exactly ONE primary subject — the subject whose
skill the lesson teaches and assesses, and whose reference file Step 0 loaded. The
supporting subject contributes content, context, and one supporting standard. It is never
co-equal.

- The exit ticket measures the primary standard. Always.
- The supporting subject decides what the texts, data, problems, or sources are ABOUT.
- Primary is the subject of the *skill students practice*, not the topic. "Students read
  about photosynthesis and find the central idea" is ELA-primary (supporting: science).
  "Students graph the plant-growth data from our bean experiment" is math-primary
  (supporting: science). When the teacher's wording leaves the primary subject genuinely
  unclear, that is a Step 1 clarifying question — and it outranks every other clarify
  priority in the primary subject's file.

Typical pairings and what the supporting subject supplies:

| Primary | Supporting | The supporting subject supplies |
|---|---|---|
| ELA | science | informational anchor texts on the unit's phenomenon or core idea; domain vocabulary in context |
| ELA | social studies | primary/secondary sources, era or civics context for reading and writing tasks |
| math | science | real data sets from the unit's investigations; quantities students model or graph |
| math | social studies | economic, civic, geographic, or historical data for quantitative reasoning |
| science / social studies | ELA or math | reading, writing, or quantitative moves inside an inquiry — same rules, roles reversed |

---

## Clarify — additions

These join the primary subject's clarify priorities. The 0–2 question budget is unchanged.

1. **Primary-subject ambiguity** (see above) — outranks everything.
2. **Which supporting unit or topic** — when the teacher implies integration but names no
   topic ("make it connect to what we're doing in science"), ask which unit or topic.
   Alignment to the wrong unit is worse than no integration.

Apply silently unless the teacher says otherwise: supporting content is **review** —
already taught in the supporting subject's class — not first exposure.

---

## Standards grounding — additions to Step 2

With the LC Knowledge Graph connected, ground BOTH subjects:

1. **Primary standard:** exactly as the primary subject's section in
   `references/learning-commons-kg.md` specifies — every call, unchanged.
2. **Supporting standard:** one additional resolution per *Resolving the standard* in
   `references/learning-commons-kg.md`, passing the supporting subject's
   `academicSubject` (and `jurisdiction` when the supporting subject is Social Studies).
   Extract the verbatim statement text and its code. Cap at 2 search attempts; if no
   usable standard, name the supporting topic without a code and add the
   partial-coverage footer to the lesson plan.

Do **not** run the supporting subject's full call sequence — no misconceptions,
progressions, or learning components for the supporting standard. It plays a content
role, not a pedagogy role. One exception: when the lesson needs a phenomenon or a real
data set and science is the supporting subject, one
`find_curriculum_lessons(caseIdentifierUUID, author="OpenSciEd")` call may anchor the
context in a real phenomenon — the Copyright guardrail applies unchanged, and the
curriculum-terminology check from the primary subject's KG section extends to OpenSciEd
here.

If the KG is not connected: the primary subject's fallback footer covers both standards.

---

## Build rules

- **The supporting content is load-bearing.** A student who ignores the
  supporting-subject content cannot complete the task. Fail: a fractions worksheet whose
  problems are decorated with science nouns ("shade 3/4 of the beakers"). Pass: the
  fractions come from the supporting unit's actual quantities, and reading them wrong
  changes the answer. This is the difference between integration and set dressing.
- **Accuracy in the supporting discipline.** Facts, data, causal claims, and sources from
  the supporting subject are held to that discipline's own standards. A wrong food-chain
  arrow or a misdated document in a math lesson is the same failure as a wrong answer key.
- **No demand dilution.** Supporting content never lowers the primary standard's
  cognitive demand. Supporting-subject recall questions do not replace primary-skill
  tasks; they may only set context.
- **Review, not first teach** (the default). The plan positions supporting content as
  activating prior knowledge: one named teacher move to surface it (a 2-minute recall
  prompt, a labeled diagram students annotate) and one fallback if students don't have
  it. If the teacher said the content is new, the phase minutes must genuinely carry the
  introduction.
- **Reading level still binds.** Supporting-subject texts obey the primary lesson's
  reading-level and workload rules.
- **Vocabulary discipline.** Supporting-subject terms are used per that discipline's
  definitions, and frameworks are spelled out (*Disciplinary Core Idea*, not *DCI*),
  matching the acronym rule in SKILL.md.

---

## Writing lesson.json — cross-curricular mapping

Everything in the primary subject's mapping applies. Additions:

- Register the supporting standard in `shared` as `supporting_standard_code` and
  `supporting_standard_text` (plain keys — only `standard` is special).
- The lesson plan carries ONE additional callout, directly below the target-standard
  callout: `{"type": "callout", "kind": "special", "label": "Supporting standard —
  <subject>", "text": "<code> — <verbatim statement>"}`. Quote it verbatim exactly once;
  everywhere else reference it by code plus a gist of ten words or fewer — the same rule
  the target standard follows.
- The LEARNING GOAL section states the connection in one sentence a teacher could read
  aloud: what the supporting content is doing for the primary skill.
- The observation template's look-fors stay primary-subject look-fors, plus at most ONE
  row for the supporting connection (e.g. "reads the experiment data accurately").
- Student pages never name standards or subjects — the integration lives in the content,
  not in headers.

---

## Non-negotiables

- Exactly one primary standard and one supporting standard. A request spanning three or
  more subjects goes back to the Step 1 integration question.
- The exit ticket assesses the primary standard only.
- The supporting standard appears verbatim exactly once in the lesson plan.
- Token integration — supporting-subject words without load-bearing content — is a
  critical failure.

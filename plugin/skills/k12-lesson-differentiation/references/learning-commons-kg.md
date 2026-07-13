<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->

# Learning Commons Knowledge Graph — call sequences (differentiation)

Used by `k12-lesson-differentiation` Step 2 **only when the LC Knowledge Graph connector is
available**. If it is not connected, skip this file entirely (SKILL.md Step 2 has the fallback).
Each section below is the call sequence for one subject. Calling the KG when connected is
mandatory; not calling it is a critical failure.

## Resolving the standard (all subjects)

Resolve the standard with `find_standard_statement`, passing `academicSubject` and `jurisdiction` (the U.S. state) when they're known:

- **A code is provided** (named in the source lesson or by the teacher): search by code — `find_standard_statement(code=<code>, academicSubject="<subject>")`. A code search matches both the code itself and everything beneath it (prefix match): a leaf like `3.NF.A.1` returns just that standard, while a parent like `2.OA` returns `2.OA` plus all `2.OA.*`. **If it returns nothing**, the code's format probably doesn't match the graph's — fall back to keyword search (below); its results come back with real `code` values that reveal the correct format, which you can use to retry the code search.
- **No code provided**: start with keyword search — `find_standard_statement(keywords=["<word or phrase>", "<word or phrase>", …], academicSubject="<subject>")`. `keywords` is a **list** of topic words/phrases; a standard matches if ANY of them appears in its description. Pick the best-matching standard from the returned `standards` array — its `code` can seed a follow-up code search for related standards (e.g. its parent prefix to pull the whole family).

When a returned standard has children, they come back in its `subStandards` array — use whichever is most relevant to the user's request, the standard itself or one of its sub-standards.

From the chosen standard, extract: the verbatim statement text, its `code`, and `caseIdentifierUUID` (store — required for all subsequent calls).

## Mathematics


**Call all three before drafting. Not calling when connected is a critical failure.**

Note any standard code the source lesson names — the resolution step searches by it when present.

After the standard resolves, the progression calls (both directions), misconceptions, and learning components all depend only on its `caseIdentifierUUID` — issue those four as one parallel batch, each with its full parameters as specified below. Step 5 runs on its own terms (its own lookup modes and teacher confirmation), untouched by the batch.

**Available tools:** `find_standard_statement`, `find_standards_progression_from_standard`, `find_misconceptions_for_standard`, `find_learning_components_from_standard`, `find_curriculum_lessons`, `find_materials_for_lesson`.

1. **Standard**: Resolve the standard per *Resolving the standard* above with
   `academicSubject="Mathematics"` and, when state is known from Step 0 state detection,
   `jurisdiction="<state>"` → verbatim statement text and `caseIdentifierUUID`.

   When jurisdiction is passed and the KG returns a state-specific standard, use that
   standard's code and text verbatim. Only use the CCSS fallback chain in math.md R3 if the teacher's state is not known or inferrable.

2. **Prerequisite and forward standard**: Call `find_standards_progression_from_standard(caseIdentifierUUID, direction="backward")` → extract the single primary prerequisite standard, verbatim — this grounds the Below tier. Call `find_standards_progression_from_standard(caseIdentifierUUID, direction="forward")` → extract the single primary forward standard, verbatim — this grounds the Above tier. Omitting either is a critical failure.

3. **Misconceptions**: Call `find_misconceptions_for_standard(caseIdentifierUUID, subject="Mathematics")` → extract the 3 most relevant misconceptions. For each, keep only the student behavior and the teacher move, rewritten in your own words. If no results, draft 3 from training knowledge.

4. **Learning components** (optional, for teacher plan): Call `find_learning_components_from_standard(caseIdentifierUUID)` → extract up to 5 sub-skill descriptions. Use to verify R2: all components must appear across all tiers.

5. **IM lesson materials** (only when BOTH conditions hold: IM is confirmed as the curriculum AND the teacher named the lesson — Scenario B3 — rather than uploading or linking it): Call `find_curriculum_lessons` with `author="Illustrative Mathematics"`. Use the mode that matches what the teacher provided:
   - **Teacher named by position** (e.g., "Grade 6, Unit 2, Lesson 3"): use `ordinalName="Grade N, Unit N, Lesson N"`. Expand abbreviations first.
   - **Teacher named by title**: use `lessonName="<content words from the title>"`. No grade/unit/lesson numbers.

   If multiple candidates return, echo `fullOrdinalName` and `lessonName` back to the teacher to confirm. Once confirmed, call `find_materials_for_lesson(lessonIdentifier, materialSource=["lesson", "activity"])` → extract: (a) activity names and sequence, (b) problem types and unknown positions addressed, (c) discourse moves. Use to ground tier task design in the actual lesson structure — do not reproduce student-facing text verbatim.

   If the teacher uploaded or linked the lesson (Scenarios B or B2), skip this step — lesson content is already available.

**Curriculum-terminology check (if not IM-confirmed):** Before proceeding, scan your working notes and verify they contain zero mentions of "Illustrative Mathematics," "IM," any MLR name (MLR 1–8), "Compare and Connect," "Stronger and Clearer Each Time," or any IM lesson/activity title. Remove any that remain — a teacher who has not confirmed IM must not receive IM-specific terminology in any tier document, the teacher plan, or chat (the same rule as SKILL.md's Copyright guardrail).

**If KG not connected:** proceed from best knowledge; add footer to teacher plan: *"Generated without the Learning Commons KG. Prerequisite grounding and misconceptions reflect general best practice."*

---

## ELA


**Call these tools before drafting. Not calling when connected is a critical failure.**

Note any standard code the source lesson names — the resolution step searches by it when present.

**CCSS strand detection:** CCSS ELA standards have distinct strands — Reading Literature (RL), Reading Informational (RI), Writing (W), Speaking and Listening (SL), and Language (L). Identify which strand the standard belongs to before calling the KG. This shapes how the differentiation is structured (e.g., the below-tier scaffold for a writing standard looks different than for a reading standard).

1. Resolve the standard per *Resolving the standard* above with
   `academicSubject="English Language Arts"` and, when state is known from Step 0 state
   detection, `jurisdiction="<state>"` → verbatim standard text, its `code`, and
   `caseIdentifierUUID`.

   When jurisdiction is passed and the KG returns a state-specific standard, use that
   standard's code and text verbatim.

2. `find_learning_components_from_standard(caseIdentifierUUID)` → up to 5 sub-skill descriptions. **Call this for K-2 standards only; for grades 3+, learning components are not yet available in the KG — skip this call and draft sub-skills from the standard statement.** Use sub-skills to verify R2: all learning components must remain in scope across all three tiers.

**ELA progressions:** `find_standards_progression_from_standard` does not return data for ELA standards — do not call it. Source prerequisite and forward standards from CCSS vertical alignment knowledge for the appropriate strand (e.g., the prior grade's parallel standard, the next grade's parallel standard). Add a footer note to the teacher plan: *"Standard text retrieved from the Learning Commons KG. Prerequisite and forward standard grounding reflects CCSS [strand] vertical alignment."*

**If KG not connected:** proceed from best knowledge; add footer to teacher plan: *"Generated without the Learning Commons KG. Standard text, prerequisite grounding, and learning components reflect general best practice."*

---

## Science


**Call all three before drafting. Not calling when connected is a critical failure.**

Note any NGSS Performance Expectation code the source lesson names — the resolution step searches by it when present.

**Available tools:** `find_standard_statement`, `find_curriculum_lessons`, `find_materials_for_lesson`.

Note: `find_learning_components_from_standard` and `find_standards_progression_from_standard` do **not** return data for science standards — do not call them.

1. **Standard**: Resolve the standard per *Resolving the standard* above with
   `academicSubject="Science"` and, when state is known from Step 0 state detection,
   `jurisdiction="<state>"`. Texas uses TEKS Science — pass `jurisdiction="Texas"` if the teacher's state is Texas. PE verbatim text + `caseIdentifierUUID`.

   When jurisdiction is passed and the KG returns a state-specific standard, use that
   standard's code and text verbatim.

2. **Find the source lesson in the KG** using `find_curriculum_lessons` with `author="OpenSciEd"`. This call serves double duty: it retrieves lesson context AND, for Scenario B3, it is how the lesson is identified in the first place (the teacher named it rather than uploading or linking it). Use exactly ONE mode per call:

   - **Curriculum position known** (teacher named the lesson by position — Scenario B3 — or unit/lesson number is visible in the uploaded/fetched lesson — e.g., "Science Grade 5, Unit 2, Lesson 3"): use `ordinalName="Science Grade 5, Unit 2, Lesson 3"`. Expand abbreviations before passing (G5 U2 L3 → Science Grade 5, Unit 2, Lesson 3). This is the most precise mode; prefer it when available.
   - **Title known but no position** (teacher named the lesson by title — Scenario B3 — or title is visible in the uploaded/fetched source): use `lessonName="<words from the lesson title>"`. Pass distinctive content words only — omit grade/unit/lesson numbers. Results come back best-match-first.
   - **Standard UUID only** (uploaded/fetched lesson with no recoverable position or title — not applicable for Scenario B3): use `caseIdentifierUUID=<uuid from step 1>`. Note: OpenSciEd lessons align to Multi-State (NGSS) standards only — a state-specific PE UUID with no exact crosswalk returns no results.

   If multiple candidates return, echo their `fullOrdinalName` and `lessonName` back to the teacher to confirm which lesson is meant before fetching materials. Once confirmed, call **`find_materials_for_lesson(lessonIdentifier)`** → extract: (a) anchoring phenomenon; (b) unit driving question; (c) this lesson's investigative phenomenon or question; (d) lesson position in the unit storyline; (e) which SEPs and CCCs are foregrounded; (f) any routines or activity structures used.

3. **Progression.** From the lesson materials or KG data, identify: (a) the prior-grade PE or DCI element that the below-level scaffold should route students *up from*; (b) the forward PE that the above-level extension should preview. Name both verbatim. Omitting either is a critical failure.

**If KG not connected:** proceed from best knowledge; add footer to teacher plan: *"Generated without the Learning Commons KG. PE grounding, OpenSciEd alignment, and progression reflect general best practice."*

---

## Social Studies


**Call all queries before drafting. Not calling when connected is a critical failure.**

Note any standard code the source lesson names — the resolution step searches by it when present.

1. **Standard**: Resolve the standard per *Resolving the standard* above with `academicSubject="Social Studies"` and `jurisdiction="<state>"` (required — `Multi-State` carries no Social Studies standards) → verbatim statement text, its `code`, and `caseIdentifierUUID` (store — required for all subsequent calls). Use statement text verbatim in all output.

**Note on standard progressions:** `find_standards_progression_from_standard` does not return data for social studies standards — do not call it. Source prerequisite and forward standards from state standards vertical alignment knowledge (e.g., adjacent grade standards in the same strand). Add a footer to the teacher plan: *"Standard text retrieved from the Learning Commons KG. Prerequisite and forward standard grounding reflects [state] standards vertical alignment."*

**If KG not connected:** proceed from best knowledge; add footer to teacher plan: *"Generated without the Learning Commons KG. Standard text, prerequisite grounding, and misconceptions reflect general best practice."*

→ **KG phase complete. Proceed immediately to Step 3.**

---


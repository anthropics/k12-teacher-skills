# Item Validation Eval Rubric

Evaluation criteria for scoring AI-generated K-12 assessment items against three validity rules. These rules were developed from a documented assessment failure in a CTE (Career-Technical Education) engineering classroom, where an AI-assisted item pool shipped with answer-key clustering, ambiguous numeric scoring, and format mismatches that undermined the items' ability to measure what they claimed to measure.

The rubric extends the existing P/R/O/M framework with a **V (Validity)** bucket covering psychometric and assessment-design criteria that do not map cleanly onto lesson-plan pedagogy or rigor. The CSV format and field structure match the existing rubrics in this repository.

---

## Rubric contents

| File | Description |
| :--- | :--- |
| `rubrics/item_validation.csv` | Nine criteria organized around three validity rules: key balance and diagnostic distractors (V1a-V1c), numeric scoring specification (V2a-V2c), and format-to-verb alignment (V3a-V3c) |

---

## The three rules

### Rule 1: Balanced key, diagnostic distractors (V1a, V1b, V1c)

The correct answer should not cluster in any one position across a pool. Every wrong answer must represent a named student error, not filler. When distractors are diagnostic, the wrong-answer report tells a remediation system which sub-skill to reteach.

### Rule 2: Numeric scoring specification (V2a, V2b, V2c)

A numeric item is not finished until it states the expected unit and rounding in the stem, defines a tolerance band for acceptable answers, and follows a consistent pool-level rounding convention. Without these, students lose points for format ambiguity rather than content misunderstanding.

### Rule 3: Format matches verb and DOK (V3a, V3b, V3c)

The item format must be capable of eliciting the cognitive demand implied by the standard's action verb. A multiple-choice item caps measurement at recognition. Using it as the sole measure of a "develop" or "design" standard produces construct underrepresentation: the test asks whether students can spot the right answer rather than whether they can build one.

---

## Worked examples

### Example 1: V1a, V1b, V1c (concrete-slab volume problem)

**Item:** "A concrete slab measures 27 ft by 24 ft and is 4 inches thick. How many cubic yards of concrete are needed?"

| Option | Value | Distractor rationale |
| :----- | :---- | :------------------- |
| A | 216 | Computed volume in cubic feet (648 x 0.333 = 215.8, rounded) but did not convert to cubic yards (omitted the division by 27) |
| B | 8.0 | **Correct.** 27 x 24 = 648 sq ft; 4 in = 0.333 ft; 648 x 0.333 = 215.8 cu ft; 215.8 / 27 = 8.0 cu yd |
| C | 24.0 | Divided area by 27 without applying the thickness conversion (648 / 27 = 24), treating the problem as a two-dimensional quantity |
| D | 0.67 | Applied conversions but inverted a division step, producing a fractional result |

**V1a (key-position balance):** This single item keys to B. Across the full pool, the auditor counts how many items key to each position. If 8 of 10 items key to B, V1a fails.

**V1b (distractor rationale completeness):** Pass. Every option has a rationale naming a specific error (omitted unit conversion, ignored thickness, inverted division).

**V1c (distractor rationale specificity):** Pass. Each error logically produces the distractor's numeric value. A student who skips the cubic-feet-to-cubic-yards division lands on 216. A student who ignores thickness lands on 24.

**V1c fail example:** If option A's rationale read "student made a calculation error" instead of naming the skipped conversion, V1c would fail. The rationale does not explain how the student arrived at 216 specifically.

### Example 2: V2a, V2b, V2c (material order quantity)

**Item (passing):** "How many 80-lb bags of concrete are needed to pour a 54 sq ft pad at 4 inches thick? Round up to the nearest whole bag. Tolerance: plus or minus 1 bag."

**V2a:** Pass. The stem specifies the unit (80-lb bags) and the rounding instruction (round up to the nearest whole bag).

**V2b:** Pass. The tolerance is stated (plus or minus 1 bag), so a student who rounds an intermediate value slightly differently still receives credit if their method is sound.

**V2c:** Pass, assuming the pool's documented convention says "order quantities round up to the purchasable unit." The item follows that convention.

**V2a fail example:** "How much concrete is needed for a 54 sq ft pad at 4 inches thick?" The stem does not specify whether the answer should be in cubic feet, cubic yards, or bags, and gives no rounding instruction.

### Example 3: V3a, V3b, V3c (format-to-verb alignment)

**Standard:** "6.3.4: Develop a program list for a facility."

The action verb is *develop*, which maps to the create level of cognitive demand.

**Failing item (V3b):** A four-option multiple-choice question asks "Which of the following is included in a program list?" This measures recall (can the student recognize a component?), not production (can the student build a program list?). V3b fails because selected-response cannot elicit the create-level demand of "develop."

**Passing item (V3b):** A constructed-response task reads: "Given the following client requirements and budget constraints, develop a program list for a 12,000 sq ft community center. Your program list must allocate square footage across all required spaces, include a 5% contingency, and justify at least two allocation decisions in writing." A scoring rubric accompanies the task with defined performance levels (complete/partial/inadequate) for space allocation accuracy, constraint satisfaction, and justification quality. V3b passes because the format requires the student to produce work at the verb's cognitive level. V3c also passes because the rubric is present.

---

## How to use this rubric

These criteria score AI-generated assessment items and item pools. They complement the existing lesson-planning and differentiation rubrics: a teacher who uses the lesson-planning skill to build instruction and then uses an AI tool to generate assessment items can apply this rubric to the items.

### Running as LLM judge

Follow the same approach described in the top-level `evals/README.md`:

1. Start with a set of AI-generated assessment items (an item pool with answer keys, distractors, and scoring metadata).
2. Pass the items and this rubric CSV to an LLM judge, instructing it to score each criterion as `0` or `1`.

Adapt the system prompt from the parent README. Replace references to "lesson-plan documents" with "assessment items and item pool metadata." The judge should have access to the full pool (not individual items in isolation) because V1a requires a pool-level count.

### Deterministic checks

Several criteria are fully scriptable without an LLM:

- **V1a:** Count correct-answer positions across the pool; compute percentages.
- **V2a, V2b:** Parse item stems for unit and rounding keywords; check metadata for tolerance fields.
- **V2c:** Verify all numeric keys against a documented rounding convention.
- **V3a:** Check that verb and DOK tags are present in item metadata.

For these criteria, a Python or shell script produces reliable binary scores. Use the LLM judge for the criteria requiring semantic judgment (V1b, V1c, V3b, V3c).

---

## Origin

This rubric was developed by a practicing CTE engineering teacher (15 years, PLTW) with doctoral training in research, measurement, and statistics. The three rules grew from a real assessment failure: an AI-assisted item pool that shipped with validity flaws across all three dimensions. The corrected pool and the rules that govern subsequent authoring are the empirical basis for these criteria. No student performance data is included. The rubric evaluates item quality at the pool and item level.

---

## Scope and limitations

- These criteria target selected-response, numeric-response, and constructed-response item types common in K-12 and CTE assessment. They do not cover portfolio assessment, oral examination, or project-based evaluation.
- V1a requires a pool of at least four items to produce meaningful position-balance statistics. Pools with fewer than four selected-response items should note this limitation.
- The format-to-verb mapping in V3b is a heuristic, not a comprehensive cognitive taxonomy. Edge cases exist (e.g., a well-constructed selected-response item can measure analysis if the options require comparative reasoning). Evaluators should use professional judgment and document their reasoning when a borderline case arises.

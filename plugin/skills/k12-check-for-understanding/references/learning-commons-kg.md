
# Learning Commons KG — call sequences for k12-check-for-understanding

Used by Step 2 **only when the connector is available**; otherwise follow SKILL.md's not-connected
branch. Calling the KG when connected is mandatory. Every call runs **before any item
is designed**, and no raw results reach chat.

---

## Resolving the standard

Infer the code from the topic, then call
`find_standard_statement(code="<code>", academicSubject="Mathematics")`.

- **A named state framework** (TEKS, SOL, OAS, CA, MA…): pass `jurisdiction="<state>"` and use that
  framework's codes rather than a CCSS proxy.
- **Nothing returned:** retry with `keywords=[...]` and the distinctive content words.
- **`subStandards` present:** the sub-part is usually the right anchor — a parent spanning several
  sub-parts is too broad for 1–3 items.

Store the **verbatim statement** (meta block, never paraphrased), the **code**, and the
**`caseIdentifierUUID`** every call below takes. Confirm it matches what the teacher asked for.

---

## Find learning components

`find_learning_components_from_standard(caseIdentifierUUID)` returns the granular learning targets
that make up the standard — the candidate scope anchors. Review **all** of them; the first returned
is not the most assessable. Any constraints a component carries (number ranges, denominator sets,
operation types, representational forms) bind item design. **If nothing is returned**, say so in the
Step 3 proposal and select from the standard's own sub-parts instead, same rationale and same pause
for confirmation.

---

## Find progression and coherence map

`find_standards_progression_from_standard(caseIdentifierUUID, direction="backward")` and the same
call with `direction="forward"` — both required. The results carry the **coherence map**, and the
map, not the list of codes, grounds every prior-grade vs. on-grade route. Extract:

1. **Prerequisite understanding** — what a student must already have. Keep the specific prior
   standard **codes**; the guide routes prerequisite-gap responses to a named one.
2. **The unique demand of this standard** — what a student learns *at this grade* that they didn't
   know before and won't yet formalize later.
3. **The on-grade vs. off-grade error line** — which errors mean a prerequisite gap versus an
   on-grade confusion. Decide it here, not at write-up time.

---

## Find misconceptions and guidance

`find_misconceptions_for_standard(caseIdentifierUUID, subject="Mathematics")` returns
research-grounded student errors plus instructional guidance. The **errors** drive distractor design;
the **guidance** turns "revisit prior-grade content" into a named sub-skill or task type.

Prioritize the 3–5 errors most relevant to the **confirmed learning component** rather than to the
standard as a whole. If fewer than three are relevant, fill the remaining slots from your own
knowledge; never manufacture a documented error. Record for each whether it is a **prerequisite gap**
or an **on-grade confusion**.

**Attribution:** none of these sources — publishers, curricula, research datasets alike — is named in
either file or in any chat message (SKILL.md's data-use guardrail).

---

**KG phase complete. Proceed to Step 3's focus proposal (or Step 4 if it is confirmed).**

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0

# Verification — k12-check-for-understanding

Read in full at Step 6, after both files are written and **before either is shown to the teacher**. Run both gates on every item; one that fails is fixed and the files rewritten before
anything is delivered. The teacher never sees this — no narration, no "I checked and found…".

**These gates run on files that already exist in `$OUTPUT_DIR`.** If you are reading this while still
composing items, you are early: finish both files, then read them back and work from that text. By
then you know which answer you meant, and a keyed item with two correct answers looks fine — so the
gates read the item back **as text**, ask you to **write things down**, and run **after** the files
exist.

If a subagent is available, hand it only the student handout — no key, no guide, no context — and
ask it to answer each item and report every choice it can defend; a fresh reader cannot rationalize
toward the answer you meant.

---

## Gate A — exactly one defensible answer

For each multiple-choice item, take every choice in turn — distractors included — and write one line
stating **the strongest case that this choice is correct**, using only what the stem and its figure
state. "Wrong because it isn't the key" is the gate failing silently. **Write the lines into a
scratch file** (`/tmp/verify_notes.md`, not `$OUTPUT_DIR`): a case you have to type out is one you
have to actually make. Then count the choices whose case survives.

- **Exactly one** → the item passes.
- **Two or more** → unanswerable as written, usually because the key rests on a property the stem
  never named. Repairs in order: (1) **name the property in the stem**, keeping the distractor — *"Which
  expression shows the number of groups times the size of each group?"* rules out the reversed factor
  order *"Which expression matches the picture?"* leaves open; (2) **remove the choice**.
- **None** → either **a figure isn't described** (if you can't tell which choice is correct from the
  stem, the choices, and the figure's `<title>`/`<desc>`, neither can a student who can't see the
  picture — give it the missing text and rerun), or **the key is wrong** and the item needs
  reworking.

Four recurring sources of a second defensible answer, worth checking directly:

- **Factor order is a convention, not a fact** — `a × b` and `b × a` are the same number, so both are
  defensible unless the stem says which factor names the group count.
- **Equivalent forms are one answer** — `1/2`, `0.5`, `2/4`, `50%` wearing four hats; two among the
  options means two correct answers.
- **A right verdict reached by invalid reasoning** — where choices are whole statements (*"No,
  because…"*), several can carry the correct verdict and differ only in justification, which works
  only when the stem asks to be judged on the reasoning.
- **Rounding, units, unstated precision** — a choice correct to the nearest whole unit is defensible
  against a key correct to the tenth unless the stem fixes the precision.

---

## Gate B — every distractor is a place a student's reasoning lands

The reverse of Gate A: does the error each distractor is meant to reveal actually produce that
choice? A distractor no described reasoning reaches is unpickable, and the student it was written for
lands elsewhere with no row waiting.

**First, compute the stem's actual quantities** — not what you intended, but the numbers as written:
first differences, ratios column by column, totals, plotted coordinates. A few lines of `python3 -c`
prints the property you were not looking for — a stem usually carries the one you chose it for and
one you didn't.

**Then, for each row of the interpretation guide**, apply the error it names to those quantities and
state which choice it produces.

- **That row's own choice** → passes.
- **A different choice** → fails. Either the choice is wrong for that error or the row's claim is;
  fix whichever is mistaken, then check the row it lands on instead.
- **The error can't be applied to this stem** → the distractor isn't reachable. Replace it with one
  this stem can produce.

The worked failure: totals 45, 70, 95, 120 have first differences 25, 25, 25 — constant. A distractor
reading *"the total paid does not increase by the same amount every time"* is false about that table,
so a student applying the additive test reads constant differences and picks a different choice.
Writing the differences down surfaces this; reading the distractor and nodding does not.

Constructed-response items have no distractors, so Gate B applies to the response types the guide
names: each is one a student could produce here.

---

## After the gates

Fix what the gates found, rewrite both files, and re-run them on anything you changed — a
repaired stem can break a distractor that was fine before. If an item still fails, **replace it
rather than patch it again**. Both files are rewritten in place in `$OUTPUT_DIR`, so the fixed
version is the first the teacher sees.

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0

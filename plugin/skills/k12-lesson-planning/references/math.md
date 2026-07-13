<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->

# Math — lesson pedagogy

Loaded by `k12-lesson-planning` when the subject is **math**.

## Clarify
Before asking anything, assess the following from all available conversation signals:

**1. State detection** Scan the conversation for any state signal — teacher mentions a state name, uses state-specific codes (TEKS, SOL, OAS, CA-CCSS, etc.), or says "I teach in [state]." If found, store as state = [state name] and pass it as jurisdiction in the KG standard lookup. Update the default standard framework to match.

**2. Curriculum detection.** Before asking anything, determine whether the teacher is likely using IM (Illustrative Mathematics) curriculum. Look for signals anywhere in the conversation — not just the current prompt: explicit name ("IM", "Illustrative Mathematics", "IM 360"), IM-specific terminology (MLRs, cool-down, "Stronger and Clearer Each Time", IM unit or lesson references), or context that makes IM use probable. If signals are present, treat as **IM-confirmed** and proceed. If absent, treat as **not IM-confirmed**.

When key information is missing, ask. Priority: (1) grade level if missing, (2) topic if missing, (3) curriculum if not inferable, (4) state if not inferable. Infer everything else. Defaults applied silently: 45–60 min, universal access design, CCSS (overridden by the detected state's framework when State Detection finds one).

---

## Standards grounding

Follow **Step 2 — Ground in standards** in SKILL.md: if the Learning Commons Knowledge Graph
is connected, use the Mathematics section of `references/learning-commons-kg.md`; if not,
proceed from best knowledge and add the disclaimer footer.

## Build the lesson

**For all lessons**
Include at least one visual scaffold registered in `shared` (a `data_table`, `number_line`,
or `fill_table` organizer) and pulled into the lesson plan with the
teacher-facing rationale beside it. Whether it also appears on the student page depends on
what it is: a blank `fill_table` students complete or a `number_line` they mark belongs on
the worksheet; a worked reference table that shows the operation or answer structure is
teacher-only — printing it gives away the thinking.

Be sure that overall timing and timing for each section is realistic - do not overload the lesson.

### Curriculum branching — apply before drafting

**If IM-confirmed:**
Use **Launch → Explore → Discuss → Synthesize → Exit Ticket** exactly. Apply IM-specific features:
- Discourse: *Compare and Connect*, *Stronger and Clearer Each Time*, *Think-Pair-Share*
- MLRs: use KG recommendations; otherwise default to MLR 2 (Collect and Display) in Explore, MLR 7 (Compare and Connect) in Discuss, MLR 8 (Discussion Supports) where discussion needs support
- Name 2–3 SMPs verbatim in Section 1; keep tone teacher-friendly, not academic

**If not IM-confirmed:**
Use **Launch → Explore → Discuss → Synthesize → Exit Ticket** (problem-based). Do NOT use IM-specific terminology: no MLR names, no *Compare and Connect*, no *Stronger and Clearer Each Time*. Use Think-Pair-Share and Turn-and-Talk.
- **K–2**: CGI — Explore must include at least one start-unknown and one change-unknown problem; for add/subtract story-problem standards the set spans all four situation types (add-to, take-from, put-together/take-apart, compare); exit ticket must target start-unknown or change-unknown; no strategy modeling before student attempt; the visual model students use (tape diagram, number bond, drawing) appears in the materials themselves — on the worksheet or anchor chart — not as an offer
- **3–5**: Problem-based, gradual release; array/area models in Discuss
- **6–8**: Problem-based; ratio tables, double number lines, coordinate graphs
- **9–12**: Mathematical modeling; formalize notation in Synthesize, not Launch

### Problem set — structural variety is required, not optional

Before writing the practice problems (`shared.p1`..`pN`), ENUMERATE the standard's structural cases — the full span
from the baseline case (the one every student must clear) to the structurally hardest case
(the one students most often get wrong: start-unknown for K–2 story problems; a product
smaller than both factors for decimal multiplication; the missing-leg case for the
Pythagorean theorem; a midpoint or just-below-boundary number for rounding; a
linear-but-not-proportional relationship for proportionality; and so on for other
standards). Then write the set so EVERY enumerated case is a numbered, required problem (or
the exit ticket), with its case named in that problem's `teacher` facet.

Coverage rules:
- A structural case that appears only in prose — the SWBAT, an anticipated challenge, a
  teacher move, or the Discuss notes — does NOT count as covered. If the plan's prose names
  a case, a numbered problem must present it to students.
- Emphasizing the hardest case never licenses dropping the baseline case: a set of all-hard
  problems fails coverage exactly as a set of all-easy ones does.
- The standard's number domain is part of the variety: if the standard or SWBAT says
  rational numbers, at least one required problem uses fractions or decimals —
  whole-number-only sets do not cover it.
- Never relegate a required structural case to an optional extension or bonus — if it only
  appears as a challenge add-on, most students never meet it.
- State once which problem carries each case (exit ticket included) — a coverage gap
  should be visible at a glance, to you and to the teacher.

### Section structure — both paths

1. **At a glance** — standard verbatim in a `special` callout (the ONE verbatim quote — everywhere else standards go by code + a short gist); a one-line lesson arc naming the phases with minutes ("Launch 8 → Explore 15 → Discuss 12 → Synthesize 5 → Exit 5") so the period's shape is visible before any detail; materials — name each item plainly (e.g. "Number cards 0-20"); SMPs named
2. **Learning goal** — Big Idea (enduring understanding, 1 sentence); SWBAT; Prerequisite (prior standard by code + one plain sentence on what students can already do and how today builds on it)
3. **Vocabulary & anticipated challenges** — 3–5 key terms with brief definitions; 2–3 misconceptions each as: *What students do* / *Why it happens* / *Teacher move*
4. **Lesson sequence** — phases per curriculum branch above; **Discuss gets at least 10 minutes** (in a short warm-up-style request, shrink the other phases, not Discuss); in Explore: 3+ look-fors each naming the student response, why it matters, and what to do with it — and if the anchor task admits more than one correct response or equation, one look-for must say so explicitly so the teacher accepts all of them; in Discuss: at least one named student-to-student talk move (Think-Pair-Share, Turn-and-Talk, partner compare, agree/disagree) + specific discourse prompts (not generic)
5. **Design notes** — last section, after the exit ticket: 2–3 elements to keep intact when
   adapting, with brief reasoning, including the lesson's central representation (the visual
   or model students work with) and its one-sentence why. Rationale lives here, after the
   teaching path — a teacher prepping reads the arc first, the reasoning second.

## Exit ticket guidance

The exit ticket is the last phase in Lesson Sequence (`from_shared:exit_ticket` under its phase header).

- It IS the **structurally hardest enumerated case** (from the problem-set enumeration above; K–2: start-unknown or change-unknown), never a mid-difficulty stand-in. Pick it with the **misconception test**: a student who holds the lesson's primary anticipated misconception must get the exit ticket WRONG. If that student would get it right, you picked an affirming instance — swap it for the discriminating one (a lesson distinguishing X from not-X exits on the not-X case; a lesson fixing a placement habit exits where that habit produces a wrong answer). Name the case in `shared.exit_ticket.teacher`.

- **Verify the exit ticket and every answer key by working the problem**: the stated answer is the one the problem actually produces, and the operation count matches the standard (a one-step-equation lesson exits on a one-step equation).

- 3 sort buckets — *Got it* / *Almost there* / *Needs re-teaching* — **each with explicit criteria** describing what a response in that bucket contains (e.g. "Got it: correct equation with the unknown where it lives in the story", not the bare label); all three criteria appear in the lesson plan, never truncated to labels.

---

## Writing lesson.json — math mapping

When you reach Step 5 (Output) in SKILL.md, register math content in `shared` and compose
`documents[]` like this:

- `shared.subject`: `"Mathematics"`; `shared.smps`: the 2–3 SMPs, named verbatim.
- `shared.anchor_task`: `{teacher: <launch script + facilitation note>, student: <the task as
  the student reads it, second person>}`.
- Each practice problem as its own key — `shared.p1`..`pN`: `{student: <prompt text>}`,
  optionally `{teacher: <what to watch for on this item>}` and `stimulus: [blocks]` (a
  `data_table` the problems share, a `number_line`, etc.). A shared data set used by several
  problems can be its own key (e.g. `shared.prices_table`) and pulled once before the set.
- Register the visual scaffold as its own `shared` key (e.g. `shared.hundreds_chart`,
  `shared.prices_table`, `shared.tape_diagram`) — a `data_table`, `number_line`, or
  `fill_table` block — and pull it into the lesson plan next to the rationale. Pull it onto
  the student page only when it is something students work with (a blank organizer, a number
  line to mark, the data set the problems analyze); a worked reference table the teacher
  uses to structure the mini-lesson stays teacher-side.
- `shared.exit_ticket`: `{student: <prompt — a fresh item, never a duplicate of a practice
  problem>, teacher: <collection note>}`. The sort criteria are a `cards` block you place in
  the lesson plan after pulling the exit ticket (see `example_lesson.json`).
- `shared.vocabulary`, `shared.misconceptions`, `shared.look_fors`: register each as the
  block you want rendered (a `table` for misconceptions, a `list` for look-fors) — there is
  no special-case rendering by key name.

**Student page layout** (the `id: "student_materials"` document) — start from this skeleton
and adapt:

```
sections:
  "<warm-up heading, kid-facing>"  group[ from_shared:anchor_task, answer_box ]
  "<practice heading>"     optional callout(student-note) — a brief reminder, only when one helps
                           from_shared:<visual-scaffold key>   ← only when it is something
                             students work with (blank fill_table, number_line, the data
                             set the problems analyze) — a worked reference table is
                             teacher-only
                           for each problem k:
                             group[ {type: from_shared, key: pk, label: "k"},
                                    answer_box (bare -- it sizes to the grade band;
                                    ruled: true when the answer is composed sentences) ]
                           on the ONE problem whose hard part is the writing move, its
                             group also carries the sentence support -- plain text before
                             the answer_box (see Sentence supports in SKILL.md)
                           page_break
  "<exit heading, kid-facing>"     group[ from_shared:exit_ticket, answer_box ]
```

**Observation template layout** (the `id: "observation_template"` document):

```
sections:
  "How to use this"        one-paragraph instructions
  "Look-fors"              from_shared:look_fors
                           fill_table headers=[Student, Strategy seen, Next step] blank_rows=8
  "Anticipated challenges" from_shared:misconceptions
  "Exit-ticket sort"       from_shared:exit_ticket
```

Worked example: `references/example_lesson.json`.

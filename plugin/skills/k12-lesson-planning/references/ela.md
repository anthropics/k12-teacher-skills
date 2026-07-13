<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->

# ELA — lesson pedagogy

Loaded by `k12-lesson-planning` when the subject is **ELA**.

## Clarify

Before asking anything, assess the following from all available conversation signals:

**1. State detection:** Scan the conversation for any state signal — teacher mentions a state name, uses state-specific codes (TEKS, SOL, OAS, CA-CCSS, etc.), or says "I teach in [state]." If found, store as state = [state name] and pass it as jurisdiction in the KG standard lookup. Update the default standard framework to match.

**2. Grade band.** Determine from grade level which band applies:
- **K–2**: foundational literacy — phonics/decoding OR read-aloud/comprehension (infer from standard; RF standards = phonics lesson; RL/RI standards = comprehension lesson)
- **3–5**: transitional comprehension
- **6–8**: literary and rhetorical analysis
- **9–12**: sophisticated analysis and argument

**3. Anchor text.** Note whether the teacher has specified a text. If not, select one from training knowledge appropriate to the grade and standard — or draw from the KG lesson-materials call (see learning-commons-kg.md). Flag your own selection in Section 1 as [suggested].

The anchor text's Materials line says where the text comes from, so the teacher can put
it in front of students. Public-domain text ships with the package. Copyrighted text
is cited — title, author, date, source — and the teacher provides copies; say so in chat
as well. Include a URL only after confirming it resolves; otherwise the citation stands
on its own. Example: *"Ain't I a Woman?" — Sojourner Truth, 1851 — public domain, ships
on the student page; full text: https://www.nps.gov/articles/sojourner-truth.htm
(confirmed).*

When key information is missing, ask. Priority: (1) grade level if missing, (2) topic or text if missing, (3) lesson type for K–2 if standard doesn't clarify, (4) state if not inferrable. Infer everything else. Defaults applied silently: 45–60 min (K–2: allow 45 min), universal access design, CCSS (overridden by the detected state's framework when State Detection finds one).

---

## Standards grounding

Follow **Step 2 — Ground in standards** in SKILL.md: if the Learning Commons Knowledge Graph
is connected, use the ELA section of `references/learning-commons-kg.md`; if not,
proceed from best knowledge and add the disclaimer footer.

## Build the lesson

**For all lessons**
Include at least one visual scaffold that appears concretely on the student page — a
`fill_table` organizer or an annotation key — registered in `shared`
and pulled via `from_shared` so the same scaffold
appears in the lesson plan with the teacher-facing rationale beside it.

Be sure that overall timing and timing for each section is realistic - do not overload the lesson.

---

### Grade band — apply before drafting

Grade band is the primary structural branch. Determine from grade level and apply the matching structure.

---

#### K–2: Foundational Literacy

Determine lesson type from the target standard:
- **RF standards** (Foundational Skills) → **Lesson Type A: Phonics/Decoding**
- **RL/RI standards** (Reading Literature / Informational) → **Lesson Type B: Comprehension via Read-Aloud**

Both types share a brief phonics review warm-up; they differ in primary focus.

**Lesson Type A — Phonics/Decoding (RF standards)**

Student-page word work renders as `display: "large"` table grids — big type a child points to
and reads — never as paragraph runs of words. Word lists for a pattern contain only that
pattern plus graphemes already taught; read each word aloud to confirm every letter behaves
as taught. The exit ticket has the child read 3–4 target-pattern words aloud to the teacher
(include one contrast word, e.g. short-a among a_e); dictation words are spoken by the
teacher and never printed on the child's ticket.

Match the lesson's scope to the request: a single-pattern introduction ("a lesson on
magic-e") is a focused 30–40 minute lesson — warm-up on the prerequisite sound, teach the
pattern, guided practice, independent practice, exit ticket — covering ONE pattern (a_e
alone, with the others as later lessons). When the teacher names a whole category
("r-controlled vowels"), the lesson covers the category's distinct sounds — ar, or, and
er/ir/ur treated as one sound, since they are. The full block below is for when the teacher asks
for their complete literacy block.

The cited standard matches the skill taught: a hearing/blending lesson (oral, no print)
cites the phonological-awareness standard family (e.g. RF.2), a decoding/spelling lesson
cites phonics (RF.3) — a lesson whose scope says "oral identification only" never carries a
decode-words standard.

Full literacy block (60–80 min, when the teacher asks for their whole block): a typical arc
is Phonological Awareness (oral only, no print) → Phonics (explicit phoneme-grapheme mapping;
decode and spell together; real and nonsense words) → Decodable Practice (connected text
using only patterns already taught plus known high-frequency words) → Read-Aloud (complex,
content-rich text — nonfiction at least half the time; oral text-dependent questions) →
Vocabulary & Discussion (2 Tier 2 words) → Shared Writing (co-construct 1–2 sentences) →
Exit Ticket (one word-reading item + one word-spelling item on the target pattern).

**Lesson Type B — Comprehension via Read-Aloud (RL/RI standards)**

A typical arc: Phonics Warm-Up (5 min, brief review) → Read-Aloud (teacher reads the anchor
text aloud, stopping at planned points for oral text-dependent questions) → Text-Dependent
Discussion (oral think-pair-share; questions progress from general understanding → key
details → vocabulary → simple inference; every student responds) → Vocabulary (2 Tier 2
words with definition, context, examples) → Shared Writing (co-construct a written response
using the target words) → Exit Ticket (one oral or simple written comprehension question).

**Non-negotiables for K–2:** no three-cueing (no picture, context, or first-letter guessing
to identify words); decodable text for phonics practice, not leveled or predictable text;
read-aloud is instructional — complex, content-rich text chosen deliberately.

---

#### Grades 3–5: Transitional Comprehension

A typical arc — scale it to the request: Launch (activate prior knowledge with one focused
prompt; let students grapple with the text fresh) → Close Reading (anchor text at grade-level
complexity, no leveling; first read for gist, second read with an assigned annotation
purpose) → Discussion (all students write before speaking — Think-Write-Pair-Share; questions
progress from general understanding → key details → vocabulary/structure → author's craft) →
Vocabulary (2 Tier 2 words with text context; students use them in the writing task) →
Writing Task (text-dependent: "Using evidence from paragraphs ___ and ___, explain how the
author shows…"; opinion in grades 3–4, argument with evidence in grade 5) → Exit Ticket (one
text-dependent question requiring inference or craft analysis).

**Non-negotiables for 3–5:** complex text for all students — scaffold access through
re-reading, discussion, and vocabulary, never an easier substitute; text-dependent questions
only; write before speaking in every discussion.

---

#### Grades 6–8: Literary and Rhetorical Analysis

A typical arc — scale it to the request: Launch (compelling question; brief unshared
quick-write students revisit at the end) → Close Reading (annotate with an assigned
analytical lens — claim development, craft moves, evidence for the central idea; partner
annotation comparison) → Structured Discussion (Think-Write-Pair-Share into whole-class
discussion moving from literal comprehension to analysis; fishbowl or Socratic Seminar for
grade 8 or strong groups; debrief discussion quality, not just content) → Vocabulary & Craft
(1–2 Tier 2 words plus one craft focus — students analyze effect, not just identify) →
Writing Task (claim + evidence + reasoning; model the structure in 6–7; counterclaim by
grade 8) → Formative Check (return to the Launch quick-write: how has your thinking
changed, and what evidence would you cite now?).

**Non-negotiables for 6–8:** analysis, not summary — the task requires an arguable claim the
text must be cited to support; pair a literary text with an informational source where
possible; counterclaim in argument by grade 8.

---

#### Grades 9–12: Rhetorical Sophistication and Sustained Argument

A typical arc — scale it to the request: Launch (a precise, genuinely arguable question;
students write independently, no discussion yet) → Close Reading (annotate for a specific
analytical lens; multiple reads with different purposes if the passage is short; keep the
complexity — it's the point) → Academic Discussion (student-to-student; teacher probes, does
not direct; Socratic Seminar references specific passages by line; debrief content and
discussion quality) → Craft & Language (one precision craft move; students analyze effect and
intent) → Writing Task (sustained analytical or argumentative response: arguable claim +
textual evidence + analysis; counterclaim in argument) → Formative Check (students assess
their own opening argument: what evidence would you add or revise?).

**Non-negotiables for 9–12:** analysis of *how* and *why*, not just *what* — effect on a
specific audience in a specific rhetorical context; full texts at full difficulty (no
excerpting around hard passages, no summaries in place of originals, no pre-explaining);
counterclaim by grade 11, and rhetorical analysis attends to audience, purpose, and context.

---

### Section structure — all grade bands

1. **At a glance** — standard verbatim in a `special` callout (the ONE verbatim quote — everywhere else standards go by code + a short gist); a one-line lesson arc naming the phases with minutes so the period's shape is visible before any detail; anchor text (title + genre + Lexile if known, or [suggested] flag); materials list — name each item plainly (e.g. "Picture cards, 18")
2. **Learning goal** — Big Idea (enduring understanding, 1 sentence tied to the text and unit); SWBAT bullets drawn from KG learning components (learning-commons-kg.md, ELA call 2), naming specific sub-skills; Prerequisite (prior standard by code + gist + 1 sentence on prior knowledge assumed)
3. **Vocabulary & anticipated challenges** — 2–3 Tier 2 target words with definitions and text context; 3 misconceptions specific to this text and task, drawn from the KG or training knowledge, each formatted: *What students do* / *Why it happens* / *Teacher move*
4. **Lesson sequence** — phases per grade band above; in every phase where students work (reading, word work, writing, sorting): 3+ look-fors each naming the specific student behavior, why it matters for the standard, and what to do; in every discussion phase: specific text-dependent prompts (not generic)
5. **Design notes** — last section, after the exit ticket: 2–3 elements to keep intact when adapting, each with a brief reason grounded in the research (Science of Reading for K–2 phonics; text complexity for 3–12), including the lesson's central representation or routine and its one-sentence why.

→ **Section structure complete. Proceed to the draft (when the teacher chose one) or Step 5.**

## Exit ticket guidance

The exit ticket is the last phase in Lesson Sequence (`from_shared:exit_ticket` under its phase header). One item targeting the hardest inference or application the standard requires. K-2 phonics: word-reading + word-spelling. K-2 comprehension: oral or simple written check. 3-12: text-dependent question requiring evidence; 6-12 may instead use a return-to-the-Launch-quick-write self-assessment. Three sort buckets (Got it / Almost there / Needs re-teaching).

---

## Writing lesson.json — ELA mapping

When you reach Step 5 (Output) in SKILL.md, register ELA content in `shared` and compose
`documents[]` like this:

- `shared.subject`: `"ELA"`.
- The anchor text or shared writing prompt as `shared.anchor_task`:
  `{teacher: <how to introduce/read it aloud>, student: <the task as the student reads it,
  or null when the launch is purely oral>}`.
- The anchor text itself (if reproduced) as its own key — e.g. `shared.passage`:
  `{type: "source_card", title, author, excerpt}`. If the text is teacher-supplied or
  copyrighted, don't reproduce it — the lesson plan names it (title, author, where it lives)
  in Materials and the phase that uses it.
- Each text-dependent question / writing task as `shared.q1`..`qN`:
  `{student: <prompt>, teacher?: <what a strong answer cites>}`.
- `shared.exit_ticket`: `{student: <prompt>, teacher?: <collection note>}`. The sort
  criteria are a `cards` block you place in the lesson plan after pulling the exit
  ticket (see `example_lesson.json`).
- `shared.vocabulary`, `shared.misconceptions`, `shared.look_fors` as in the SKILL.md schema.

**Which documents to emit.** A K-2 phonemic-awareness or oral-language lesson (RF.*.2,
RF.*.3 phonics warm-ups, listening-comprehension) often has **no `student_materials`
document** — students hold response cards or nothing. Say so in the lesson plan's Materials
line and in your message to the teacher. For 3–12 reading/writing lessons, emit
`student_materials`; if the anchor text is reproduced, also emit a `source_packet` document
containing just `from_shared:passage`.

**Student page layout** (when emitted) — start from this and adapt:

```
sections:
  "Before you read"        from_shared:anchor_task ; answer_box if a written prediction
  "Text"                   from_shared:passage   (omit when the text isn't reproduced)
  "Read and respond"       for each question k:
                             group[ {type: from_shared, key: qk, label: "k"},
                                    answer_box ]
                           page_break
  "<exit heading, kid-facing>"     group[ from_shared:exit_ticket, answer_box ]
```

**Observation template layout** matches the math layout in `references/math.md`.


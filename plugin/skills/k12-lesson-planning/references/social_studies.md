<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->

# Social Studies — lesson pedagogy

Loaded by `k12-lesson-planning` when the subject is **social studies / history**. This subject
follows the C3 inquiry arc, generates a **single lesson** positioned within a unit arc, and
**points to** primary sources rather than reproducing them.

Lessons follow the C3 Framework inquiry arc:
- Developing compelling and supporting questions — sparks curiosity and drives a unit
- Applying disciplinary concepts and tools — from civics, economics, geography, and history
- Evaluating sources and using evidence — disciplinary literacy and critical thinking
- Communicating conclusions and taking informed action — civic application

**C3 Framework note.** The C3 Framework is an *inquiry design* framework, not a standards document. Use C3 for instructional design (the inquiry arc, sourcing, argumentation, civic action), but the lesson's content scope and the verbatim standard must come from the **state** standard — never substitute a C3 dimension or indicator for the standard, and never fall back to C3 when a state standard is unavailable.

## Gather inputs

If the user has not already provided the following, ask for them before generating:

- **Grade band**: K–2, 3–5, 6–8, or 9–12
- **Topic or era**: e.g., "Reconstruction," "the civil rights movement," "ancient Rome," "World War I"
- **Compelling question** (optional — you will draft one if not provided): a contestable, civically resonant question that could anchor a multi-day unit
- **Specific standard or focus skill** (optional): e.g., "causation," "sourcing," "continuity and change over time"
- **State** (required): Social studies standards are state-specific. If the teacher does not name a state and it is not inferrable, ask.

Do not ask about Taking Informed Action, multi-discipline integration, or curriculum context — those are out of scope for this skill.


## Standards grounding

Follow **Step 2 — Ground in standards** in SKILL.md: if the Learning Commons Knowledge Graph
is connected, use the Social Studies section of `references/learning-commons-kg.md`; if not,
proceed from best knowledge and add the disclaimer footer.

## Draft a compelling question (if not provided)

The compelling question must be:
- Genuinely contestable (not a yes/no or factual lookup)
- Civically or humanly resonant — students should feel it matters
- Answerable through historical evidence
- Appropriate in complexity for the grade band

Examples by grade band:
- K–2: "Why do people move to new places?" / "How do communities change over time?"
- 3–5: "Was Westward Expansion good for America?" / "What made the American Revolution possible?"
- 6–8: "Was World War I inevitable?" / "How did ordinary people shape the civil rights movement?"
- 9–12: "When is civil disobedience justified?" / "Did Reconstruction succeed or fail — and for whom?"


## Build the lesson plan

Build the lesson plan with the following sections — these become the `sections` array of the
`lesson.json` (the material source) in Step 5 — Output (one JSON section per `##` heading below; the template's
formatting hints map to renderer block types: blockquotes → `callout` blocks, bold labels →
`labeled` blocks, lists → `bullets`). Adjust vocabulary, task complexity, and source type by
grade band (see guidance below).

**For all lessons**
Include at least one visual scaffold that appears concretely on the student page — the
`source_card` excerpts themselves, a `fill_table` evidence organizer, or a timeline —
registered in `shared` and pulled via
`from_shared` so the same scaffold appears in the lesson plan with the teacher-facing
rationale beside it.

Be sure that overall timing and timing for each section is realistic - do not overload the lesson.

---

### Section structure — teaching order

1. **At a glance** — grade band; time; standard verbatim in a `special` callout (the ONE
   verbatim quote — everywhere else standards go by code + short gist); a one-line lesson arc
   naming the phases with their minutes (e.g. "Hook 5 -> source work 20 -> discussion 15 ->
   exit 10") so the shape of the lesson is visible before any detail; the lesson's C3 inquiry
   focus in plain words (e.g. "C3: evaluating sources and using evidence"); materials —
   name each item plainly.
2. **Compelling & supporting questions** — the unit-level question, and the narrower question
   this single lesson investigates (one of the 3–5 that would make up the full unit).
3. **Lesson goals & background for the teacher** — 1–2 SWBATs; assumed prior knowledge,
   specific; 2–3 anticipated challenges for this topic and source set (*what students do* /
   *why it happens* / *teacher move*); Key
   vocabulary (4–6 terms, defined at grade level, each introduced at the moment the
   lesson needs it). The background content itself lives inside the lesson sequence, in the
   phase that delivers it.
4. **Source set (2 sources)** — sources are real, high-quality, and specifically cited
   (title, author, date, archive). If you have web search, confirm before using. A
   public-domain text source (pre-1929, government documents) gets an excerpt reproduced, sized to the analysis the questions ask of it
   as a `source_card`; an image, photograph, political cartoon, or copyrighted text isn't
   reproduced — name it (title, citation, where to find it) in Materials and the phase that
   uses it. Register each reproduced source in `shared` under its own key. For each source:
   the card itself (its citation carries where the text lives — full URL when you verified it
   resolves this session; otherwise the archive and collection by name, nothing more — the
   same rule covers call numbers and catalog IDs, which appear only verified) plus
   ONE sentence of why this source, as a labeled line. Procurement details, search tips, and
   alternate locations don't help a teacher mid-prep — leave them out. Close the section with
   one sentence on the pairing — the tension or contrast the two sources create.
5. **Lesson sequence** — phases in teaching order, minutes summing exactly to the period:
   background knowledge (this phase carries its content inline — the short labeled chunks
   the teacher actually says, a half page at most, never an essay) → source work with
   **2–3 guided analysis questions** (scaffolded:
   observe → source or contextualize → corroborate and connect to the supporting question) →
   discussion → exit ticket.
6. **Exit ticket** — students answer the supporting question with evidence from the sources.
   Sized to the minutes remaining in the period: a claim plus one or two pieces of cited
   evidence, per the grade band below — never a take-home essay. 2–3 success-criteria bullets.
7. **Design notes** — 2–3 elements to keep intact when adapting, each with a one-sentence
   reason grounded in the standard, including the lesson's central organizer or source-work
   structure and its one-sentence why.

## Grade-Band Guidance

Apply these adjustments throughout the lesson:

**K–2**
- Background knowledge delivered as read-aloud or class discussion, not independent reading
- Sources: photographs, illustrations, artifacts, oral histories — avoid dense text
- Analysis questions are discussed orally before writing
- Exit ticket: drawing + 1–2 dictated or written sentences; or a class discussion with teacher-recorded responses
- Vocabulary: 4 words max, defined with visuals or gestures

**3–5**
- Background knowledge can be a short informational text (Lexile 600–850) or teacher-led mini-lecture
- Sources: accessible primary sources with some scaffolding (sentence-level glosses on hard vocabulary); photographs and short documents work well
- Analysis questions answered in writing
- Exit ticket: 1 paragraph using the claim-evidence-reasoning structure
- Vocabulary: 5–6 words; students interact with words before source reading

**6–8**
- Background knowledge as assigned reading or lecture notes; students should be able to read and annotate independently
- Sources: more complex primary sources (letters, speeches, political cartoons, data); students expected to do basic sourcing independently
- Analysis questions answered in writing
- Exit ticket: short constructed response (1–2 paragraphs), evidence-based; may include a claim + two pieces of evidence
- Vocabulary: disciplinary terms emphasized (e.g., "corroborate," "perspective," "contextualize")

**9–12**
- Background knowledge delivered via complex texts; students expected to take notes and synthesize
- Sources: challenging primary and secondary sources; students source, contextualize, and corroborate independently
- Analysis questions push toward argument construction and acknowledgment of counterevidence
- Exit ticket: a claim with cited evidence and reasoning, acknowledging complexity — sized to the minutes remaining
- Vocabulary: discipline-specific and college-level terms assumed or quickly reviewed

## Writing lesson.json — social studies mapping

When you reach Step 5 (Output) in SKILL.md, register social-studies content in `shared` and
compose `documents[]` like this:

- `shared.subject`: `"Social Studies"`.
- `shared.supporting_question`: the supporting question (one sentence, student-facing).
- Each source as its own key — `shared.source_a`, `shared.source_b`: a `source_card` block
  (title, author, date, origin, **excerpt** — reproduce a public-domain excerpt sized to the analysis when
  the source is pre-1929 or government text). A source you cannot reproduce (an image,
  political cartoon, photograph, copyrighted text) is named in the lesson plan — title,
  citation, where to find it — not represented on the student page.
  When you write an excerpt that paraphrases or composites period
  language rather than quoting a specific document verbatim, set `origin` to
  `"adapted from <publication>, <year>"` so the card is honest about provenance — and cite
  the collection, not a page number: page-precise citations ("p. 254") belong only on text
  quoted verbatim from that page, and every quotation is attributed to the document it
  actually comes from. Register
  each *Why this source* line under a teacher-only key (`shared.source_a_rationale`, etc.)
  so it never renders on the student page — one sentence; the citation already says where
  the text lives.
- Each guided analysis question as `shared.q1`..`q3` (2–3 questions): `{student: <question>}`. Every question names its target — "Source A", "Source B", or "both sources" — a student with two sources in hand can't act on "this source".
- `shared.exit_ticket`: `{student: <exit-ticket prompt>, teacher?: <collection note>}`.
  The three sort entries (standard labels, explicit criteria) are a `cards` block you place
  in the lesson plan after pulling the exit ticket (see `example_lesson.json`).
- `shared.vocabulary`, `shared.misconceptions`, `shared.look_fors` as in the SKILL.md schema.

**Documents to emit.** Social-studies inquiry lessons always have written analysis
questions, so **always include `id: "student_materials"`** alongside `lesson_plan` and
`observation_template`. When sources are registered, also include `id: "source_packet"`
(one `from_shared` per source, plus a one-line "Read these with the worksheet" note). The
student worksheet opens with "*See your Source Packet for Source A and Source B.*"

**Student page layout** (the `id: "student_materials"` document):

```
sections:
  "Supporting question"    callout(student-task) from_shared:supporting_question
  "Sources"                from_shared:source_a ; from_shared:source_b
  "Analyze the sources"    for each question k:
                             group[ {type: from_shared, key: qk, label: "k"},
                                    answer_box ]
                           page_break
  "Make your claim"        group[ from_shared:exit_ticket, answer_box ~180pt ]
```

The Background-Knowledge Builder, source-pairing rationale, and *Why chosen / Where to find
it* live only in the `lesson_plan` document — pull them with their teacher-only keys there.

**Observation template layout**: as in `references/math.md`, with `fill_table` headers
`[Student, Evidence of thinking, Instructional move]`.

Alongside the documents, briefly note which source collection(s) likely have the recommended
sources, and any coherence flag about assumed prior knowledge.

# Output contract — k12-lesson-plan-creation

Loaded by `k12-lesson-plan-creation` at Step 5, before making any document, on every path. Every
rule here is a hard requirement for the CONTENT of the documents. How the documents look is decided
by the path (`rendering/claude-artifact.md` or `rendering/docx.md`), not here.

## The document set

Every lesson package has:

- **Lesson plan** (teacher-facing) — the subject file's section structure.
- **Observation template** (teacher-facing) — how to use it, the look-fors, the anticipated
  misconceptions, room to note what each student did, and the exit-ticket sort.
- **Student materials** (student-facing) — **only when students hold a printed page.** A K-2 phonics
  or oral lesson may have none; a source-heavy lesson may have this AND a separate **source
  packet**. The subject file says what belongs on the student page; adapt it to the lesson. If the
  teacher asked for leveled/tiered student materials, label them Group A / B / C (A = below, B = at,
  C = above grade level) — level wording stays in the teacher-facing documents.
- Any other page the lesson needs (cards, a sorting mat, a template) ships with the package.

Anything that appears in more than one document — a problem, a source, the exit ticket, vocabulary,
look-fors, the numbers of a context — is worded ONCE and reused identically, so the documents cannot
drift apart. On a student page only the student-facing wording of a task appears (an oral or
teacher-led task prints nothing there); in the lesson plan the teacher's script sits beside the
exact prompt students will see, and the script points to it ("read the story in the box aloud")
rather than quoting it again.

## Brevity — hard requirements for every document

Every document is clear, brief, and easy to skim. Include what a teacher needs to teach it; leave
out what merely demonstrates rigor. Headings use sentence case.

- A paragraph is at most 3 sentences. Longer → split it, list it, or set parallel items side by
  side.
- Write like a colleague's note: plain, direct sentences built from commas and periods.
- Bullets are fragments — one idea each, ≤ ~15 words; never chain clauses with semicolons.
- Parallel variants (per-group supports, per-phase differentiation, tiered look-fors) sit side by
  side for comparison, ≤ ~25 words each — never back-to-back multi-sentence paragraphs.
- Highlight only the few moments a teacher must not miss — a warning ("do not resolve the debate
  yet"), a collect-before-moving-on, the one make-or-break move of a phase. A page where everything
  is emphasized highlights nothing.
- Each instruction lives in exactly one place; a phase's opening line sets up, what follows carries
  the content; neither repeats the other.
- Quote the standard verbatim exactly once. Everywhere else — prerequisite grounding, forward
  connections — reference by code plus a gist of ten words or fewer; never re-paste full standard
  text.
- A section that runs past about half a page of continuous prose must be restructured.

## Everything matches — hard requirements for every document

A teacher trusts the package because every part agrees with every other part:

- The materials list and the phases agree exactly: every listed item is used by a named
  phase, and every counted set matches its enumeration ("Picture cards, 18" lists 18 words).
- **Classroom-ready:** the lesson runs on what the teacher already holds. Every Materials item is a
  page this package ships, equipment the classroom has, or a sourced resource with its access path
  stated — exact title and source, a link when you could confirm one. Anything harder to get than
  that stays out of the lesson unless the teacher steered toward it. A printable the lesson depends
  on ships with the package.
- A task worded in two places (plan's "Students see" and the student page) uses identical wording in
  both. **No drift between documents:** the student pages carry exactly the tasks the plan describes
  — same count, same numbers and contexts, same reading level and cognitive load; everything a
  student page has students use (a handout, cards, a manipulative, a source, a tool) is named in the
  plan's Materials and in the phase that uses it; the exit ticket students see is word for word the
  one in the plan and on the observation template.
- Student tasks match the skill the standard names, in both directions. Decoding, spelling,
  and writing skills happen on paper — students read and write real words on a student page.
  Listening and speaking skills get spoken, pointed, sorted, drawn, or circled responses.
  The lesson's scope statement binds every task that follows it.
- Scripts and worked examples are final say-aloud text: every step decided before it lands
  on the page, exactly what the teacher says.
- Exit-ticket sort buckets partition the answers: each example response fits exactly one
  bucket, and equivalent forms of one answer (17 + 24 = ? and 24 + 17 = ?) sit in the same
  bucket together.
- An answer space mirrors its ask: rows match the count requested, and every space sits under a
  prompt naming what goes in it.

## Reading level and workload

Student-facing text reads at the students' reading level —
which the teacher may state separately from the grade ("my 6th graders read at a 2nd–4th
grade level" means grade-6 content carried in sentences a 2nd–4th grade reader can read:
short sentences, everyday words, one instruction at a time). Size the student work to the
class period: a typical student finishes the worksheet in the minutes its phase allows.
Say "home language," not a specific language, and print translations only into a language
the teacher has named.

**Sentence supports** are plain text where students write: a starter to begin from
("One central idea is…") or a fill-in frame with blanks sized for the student's handwriting.
A support helps the student start, not answer — it never pre-fills what the task asks for.
Place each one on the specific task whose writing move is hardest — including the
explain-why beside a math equation — never one bank copied across problems. K-2 students
and multilingual learners get a support on every task that asks for composed sentences.
Tasks that take only a number, a single word, or a drawing need none.

**Writing room** should be age-appropriate: the younger the writer, the more room they need.
Students need lines to write on when the answer is composed sentences (rule of thumb: K–5 gets
ruled lines). Math work space is open, because computing, drawing and partitioning need a blank
surface; a math question that asks the student for a written explanation gets lines like any other
writing task. Answers written in table cells, number lines, graphs, etc. don't need lines either.

**Spell out framework names** in every teacher-facing document — *Science and Engineering
Practice*, not bare *SEP* — a teacher should never need to look up an acronym.

## Document integrity

Every document is finished prose a teacher hands out or works from:

- Every in-document reference points at something that exists in the package: "jot it in the
  table below" means that table is on the page; an exit ticket collected separately prints as
  its own piece; a reference table uses the same numbers as the problems it supports.
- Materials and the lesson match both ways: each listed item is used somewhere in the lesson, every
  item any section sends students to — phases and extensions alike — appears in Materials, and
  anything students read is printed in the package or named by its exact title. Anything the teacher
  displays (a video, photo, projected image) lives in the lesson plan: name it in Materials and in
  the phase script that uses it; a student page carries only what is printed on it. Offers and
  pointers to the chat conversation stay out of documents entirely.
- Lessons are light on materials: the default kit is what every classroom has (board, projector,
  paper) plus the pages this lesson ships. A separate printable or manipulative earns its place only
  when the activity genuinely needs it — and the same thinking work on the worksheet usually serves.
  When a printable earns it (cards, mats, a template), ship it with the package in the form that
  serves it best; equipment a classroom owns is simply listed.
- Phase minutes include the transitions they cause (handing out, regrouping, collecting), at
  a pace real students of this grade manage, and the phases sum to exactly the stated
  period — transition time lives inside the phases, never as invisible buffer.
- Teacher notes read as finished sentences. A predicted error names one specific wrong answer
  a real student would produce.
- Verify every computation by working it — answer keys, worked examples, and any quantitative
  chain the lesson builds on (an energy pyramid's levels, a ratio table's entries, a coin
  total) produce the numbers the materials state.
- A task's prompt, what it works from, its supports and its answer space stay together on one page.

## Accessibility (the pages get photocopied)

Meaning lives in the words, never in color, position, or decoration alone: point students to "the
Evidence column," never "the box on the right"; color is welcome, just never the only carrier of
meaning. Every write-in space is labeled with what goes in it; anything drawn rather than written —
like a number line — states its task in words.

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0

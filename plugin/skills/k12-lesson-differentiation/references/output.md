# Output contract — k12-lesson-differentiation

Loaded by `k12-lesson-differentiation` at Step 5, before making any document, on every path. Every
rule here is a hard requirement for the CONTENT of the four documents. How the documents look is
decided by the path (`rendering/claude-artifact.md` or `rendering/docx.md`), not here.

## Density rules — hard requirements for every document

Teachers consistently flag dense walls of text. Structure beats prose:

- A paragraph is at most 3 sentences. Longer → split it, list it, or set parallel items side by
  side.
- Bullets are fragments — one idea each, ≤ ~15 words; never chain clauses with semicolons.
- Parallel tier content (Below / At / Above doing the same phase differently) sits side by side for
  comparison, ≤ ~25 words each — never three back-to-back multi-sentence paragraphs.
- An aside longer than one sentence (misconception watch-fors, confer prompts, deployment guidance)
  is set apart as its own note, not a sentence buried in a paragraph.
- Quote the standard verbatim exactly once. Everywhere else — prerequisite grounding, forward
  connections — reference by code plus a gist of ten words or fewer; never re-paste full standard
  text.
- A section that runs past about half a page of continuous prose must be restructured (table,
  bullets, or split into two sections) before any document is made.

## Cross-check before making any document

Run ALL checks before making any document. Do not make one until every item passes.

**O6 — Artifact alignment (both directions):**
1. **Plan → tier documents.** List every task the plan says students do — tier problems/tasks, exit
   ticket, the anchor activity, anything assigned to "early finishers." Each must have a printed
   student-facing block on at least one tier document (the anchor activity on all three, via
   `from_shared: anchor_activity`). A task that exists only as a plan description fails.
2. **Tier documents → plan.** For each tier document, list every printed task — each problem/task,
   the extension and each of its printed sub-parts, anything printed on one tier only, the exit
   ticket, "If you finish early," "Reflect." Each must appear in that tier's **Worksheet tasks**
   line in the plan, with its scaffold named (e.g., "P1 (tape diagram + sentence support)" not just
   "P1"). A printed task the plan never names fails — a named scaffold the worksheet does not print
   fails — and so does a plan line naming a task or organizer no tier document prints.

Shared content is guaranteed by `from_shared` blocks; the check targets document-specific blocks and
plan prose. Also confirm the exact `shared.standard_code` string appears in each of the three tier
documents' `eyebrow` (`"[Grade] [Subject] · [standard_code]"`) — the standard must be named on every
tier, not only in the teacher plan. Fix mismatches before making the documents.

## Classroom-ready (every document)

The tiers run on what the teacher already holds. Every resource a worksheet or the plan names is a
printed block in this package, equipment the classroom has, or a sourced resource with its access
path stated — exact title and source, a link when you could confirm one. A visual a task depends on
prints on the worksheet that uses it, or the task is rewritten to work from what does print.
Anything harder to get than that stays out unless the teacher steered toward it.

## P8 — Flexible grouping (confirm in the teacher plan)
- The `Flexible Grouping` section states the evidence or basis used to assign students to each tier
  (e.g., a specific prior exit ticket, diagnostic score, or "Default profile applied — no diagnostic
  data available"). A blank or generic statement fails.
- The section includes an explicit statement that tier assignments are revisable based on formative
  evidence from THIS lesson (not a standing ability track).

## O4 — Rationale notes (confirm in the teacher plan)
- `Why this works (1)` and `Why this works (2)` sections are present and each name a specific tier
  design choice with a stated reason. Generic statements ("scaffolds help learners") fail. These
  sections are required and cannot be dropped to meet page caps — tighten other content instead.

### Student-facing language — ALL tier documents

Student pages never use instructional-design terminology. Those are teacher words; on a worksheet
they read as labels about the student, not for the student.

- ❌ "CER" — write the organizer labels out: *Claim / Evidence / Reasoning*. ("Write a CER" becomes
  "Explain your claim with evidence and reasoning".)
- ❌ "sensemaking check", "formative check", "misconception", "scaffold", "tier", "differentiation",
  "anchor task" — use student words: *"Check your thinking"*, *"Try this together"*, *"If you finish
  early"*.
- On a student document the tier is named **Group A** (below), **Group B** (at), or **Group C**
  (above): the `title` carries the group letter per the subject template; the `eyebrow` stays
  `"[Grade] [Subject] · [standard_code]"` with no level wording. Grade-level labels are teacher
  words — the teacher plan's tier labels ("Below (Group A)" etc.) carry the association.
- Scaffold prompts get a SHORT student-friendly subheading on its own line (e.g. *"Observe the data
  first"*, *"Check your thinking"*), then the prompt as a normal paragraph below it — never a long
  bold inline label like "**Before Task 2 — sensemaking check:** Complete this sentence…". The
  subheading names what the student does, not the pedagogy behind it.

### Asset framing — below-tier documents

Student-facing language must not signal reduced expectations. Scaffolds appear as natural task
design, not announced supports.

- ❌ "Task 1 (Scaffolded) / Task 2 (Guided) / Task 3 (Independent)" — a student who sees these labels knows they are on the easier version.
- ❌ "Use this if you need it" / "Here is a sentence starter" — names the support as a crutch.
- ❌ Any header, label, or aside that distinguishes scaffolded tasks from unscaffolded ones.
- ✓ The organizer, annotation frame, or sentence support simply appears as part of the task layout.
- ✓ Tasks are numbered without scaffold-level labels.
- ✓ Sentence supports at the top of the document are introduced universally: "You can use these sentence supports:" — not "Use these if you get stuck."

## Accessibility (the pages get photocopied)

Meaning lives in the words, never in color, position, or decoration alone: point students to "the
Evidence column," never "the box on the right"; color is welcome, just never the only carrier of
meaning. Every write-in space is labeled with what goes in it; anything drawn rather than written —
like a number line — states its task in words.

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0

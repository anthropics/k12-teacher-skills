# Output — k12-check-for-understanding

Read in full before writing (SKILL.md, Step 5).

---

## The two documents

Every check produces **two separate self-contained `.html` files** — never one combined file, never
markdown.

- **`cfu_[topic-slug]_student.html`** — printable, distributable as-is: item prompts and answer
  choices (or response space for CR), a name/date line, nothing else. No meta block, no
  correct-answer marker, no source label, no next-step language.
- **`cfu_[topic-slug]_teacher.html`** — meta block, focus and progression callouts, each item
  repeated in full, the correct answer, the interpretation guide, the what-to-look-for summary.

`[topic-slug]` is a few lowercase hyphenated words: `equivalent-fractions`. **Item text is identical
across the two files** — same prompts, choices, and order, figures included. Write it once and reuse
it — that is what makes the handout safe to hand over unredacted.

---

## Writing the files

Write both **into `$OUTPUT_DIR`** — `mkdir -p "$OUTPUT_DIR"`, then
`"$OUTPUT_DIR"/cfu_equivalent-fractions_student.html` and the matching `_teacher.html`. That is where
this runtime delivers from; a file written only to `/tmp` never reaches the teacher. Then list it and
confirm both are present and non-trivial. With no `$OUTPUT_DIR`, present both
documents inline in your reply, clearly separated. Both render standalone: styles inline in a
`<style>` block, no external CSS, fonts, or scripts.

---

## Figures

Read back as text an inline `<svg>` says nothing about what it shows, so it carries that in words —
`<title>4 groups of 3 dots each</title>` and `<desc>Four squares in a row. Each square contains 3
dots, for 12 dots in total.</desc>`, wired up as below.

- **`<title>`** names the structure in the terms the item is read in — "4 groups of 3 dots each", not
  "dice"; **`<desc>`** adds what a student needs to work the item from that text alone. Both are
  student-facing, so both read at the grade's level.
- **The description leaves the item's work undone.** Before writing it, name the one thing the item
  asks the student to do — count the parts, identify the coin, compare the two amounts — then write
  the text so a student working from it alone still has to do that thing. Where a line split into
  fourths asks which point is at 3/4, *"points A, B, C and D, one on each mark after 0"* leaves the
  counting to them; *"Point C is 3 jumps from 0"* has done it for them. Where the question is what a
  coin is worth, *"a small silver coin with a ridged edge"* leaves the recognition to them; *"a
  dime"* has not. What gives an item away is naming the property the question asks for — the count,
  the position, the identity, the comparison — which happens whether or not the answer itself
  appears in the text.
- **It states only what the picture carries.** A comparison needs both things drawn: with a single
  coin on the page, *"one of the smaller coins in the jar"* reports something no reader can see.
- `role="img"` with `aria-labelledby` on both makes a screen reader announce them, and identical
  markup goes in **both** files. Where the answer depends on a property only the figure
  carries, the stem names it too.

---

## No provenance or process talk

Neither file says where anything came from: no `KG` or `Training` badge on a distractor row, no
Source column, no badge in the meta block or on a callout, and no note that a lookup returned
nothing. An empty progression result is a fact about the retrieval, not about the mathematics, so the
guide states the prerequisite and next-step routing it does have and says nothing about the rest.
Retrieved data still shapes every row; the file stops narrating it. (Third-party names stay out under
SKILL.md's data-use guardrail.)

Both files also read as though the check simply exists. `Confirmed with teacher`, `by teacher
request`, `as you asked`, and any badge holding them are the conversation showing through the
artifact — as is any trace of the checks you ran before delivering. Write the focus as a fact about
the mathematics — *"Two components: identifying coin values, and adding a mixed set of coins"*.

---

## Styles

Base block, in both files:

```css
body{font-family:Georgia,serif;margin:40px auto;padding:0 24px;color:#1a1a1a}
h1{font-size:1.35em;color:#2c2c2c;border-bottom:2px solid #444;padding-bottom:8px}
.item-number{font-size:.85em;font-weight:bold;text-transform:uppercase;color:#555;margin-bottom:8px}
.item-prompt{font-size:1.05em;line-height:1.7;margin-bottom:14px}
.choices{list-style:none;padding:0;margin:0 0 16px}
.choices li{padding:9px 13px;margin:7px 0;border:1px solid #767676;border-radius:4px}
```

Student file adds:

```css
body{max-width:700px}
.name-line{margin:20px 0 32px}
.name-line span{display:inline-block;border-bottom:1px solid #767676;min-width:220px;margin-left:6px}
.item{margin:32px 0;page-break-inside:avoid}
.response-line{border-bottom:1px solid #767676;height:32px;margin:8px 0}
@media print{body{margin:0;padding:0 12px}}
```

Teacher file adds:

```css
body{max-width:800px;background:#fafaf8}
h1{border-bottom-color:#d4a843}
h2{font-size:.95em;text-transform:uppercase;color:#666;margin:20px 0 8px}
.meta{background:#fff;border:1px solid #e0ddd5;border-radius:6px;padding:16px 20px;margin:20px 0;display:grid;grid-template-columns:200px 1fr;gap:0 12px}
.meta-label,.meta-value{padding:8px 0;border-bottom:1px solid #f0ede5}
.meta-label{font-weight:bold;color:#555}
.meta-label:last-of-type,.meta-value:last-of-type{border-bottom:none}
.item{background:#fff;border:1px solid #e0ddd5;border-radius:6px;padding:20px 24px;margin:24px 0}
.correct-answer{color:#2d6a2d;font-weight:bold;margin-bottom:16px}
table{width:100%;border-collapse:collapse;font-size:.92em}
th{background:#f0ede6;text-align:left;padding:10px 12px;border-bottom:2px solid #ddd}
td{padding:10px 12px;border-bottom:1px solid #eee;vertical-align:top;line-height:1.5}
tr.correct-row td{background:#f0f7f0}
.look-for,.lc-focus,.progression-ctx{padding:14px 18px;margin:20px 0;border-radius:6px;line-height:1.6}
.look-for{background:#fef9ec;border-left:4px solid #d4a843}
.lc-focus{background:#f1f8e9;border:1px solid #c5e1a5}
.progression-ctx{background:#f0f4ff;border:1px solid #b8c8f0}
.look-for strong,.lc-focus strong,.progression-ctx strong{display:block;margin-bottom:6px;font-size:.85em;text-transform:uppercase}
.look-for strong{color:#7a5c00} .lc-focus strong{color:#2e7d32} .progression-ctx strong{color:#1a56c4}
```

---

## Student-facing template

`<!DOCTYPE html>`, `<html lang="en">`, a head carrying `<meta charset="UTF-8">`, the viewport meta,
`<title>CFU: [Topic]</title>`, and `<style>` with the base + student rules. Then:

```html
<body>
<main>

<h1>[Topic/Concept]</h1>
<div class="name-line">Name: <span>&nbsp;</span> &nbsp;&nbsp; Date: <span>&nbsp;</span></div>

<!-- Repeat per item. Prompt and choices only — nothing else. -->
<div class="item">
  <div class="item-number">Item 1</div>
  <div class="item-prompt">
    [Prompt text — identical to the teacher file. Where the answer turns on a property only the
    figure shows, this names that property.]
  </div>
  <svg viewBox="0 0 420 110" role="img" aria-labelledby="i1-t i1-d"
       xmlns="http://www.w3.org/2000/svg">
    <title id="i1-t">[what the figure shows, in the terms the item is read in]</title>
    <desc id="i1-d">[enough detail to work the item from this text alone]</desc>
  </svg>
  <ul class="choices">
    <li><strong>A.</strong> [Choice A]</li>
    <li><strong>B.</strong> [Choice B]</li>
    <!-- C, D likewise -->
  </ul>
  <!-- Constructed response instead: a few <div class="response-line"></div> in place of the <ul> -->
</div>

</main>
</body>
</html>
```

---

## Teacher-facing template

**The prose fields are teacher notes, not assessment specs.** One thought per sentence, under about
35 words; the plain phrase leads and the technical term follows in parentheses; the student is the
subject. *"Students can locate a non-unit fraction on a number line by counting the total number of
equal parts (denominator)…"* is a teacher's note; *"Reveal whether a student can coordinate both
parts of locating…"* describes the design of the check.

Same shell, with `<title>CFU: [Topic] — Teacher Guide</title>` and the base + teacher rules.

```html
<body>
<main>

<h1>CFU: [Topic/Concept] — Teacher Guide</h1>

<div class="meta">
  <!-- One label/value span pair per row, these six in this order. Contents per references/math.md. -->
  <span class="meta-label">Standard</span>
  <span class="meta-value">[CCSS code] — [verbatim standard language from the retrieval]</span>
  <span class="meta-label">Grade</span>
  <span class="meta-value">[Grade]</span>
  <span class="meta-label">Rigor</span>
  <span class="meta-value">[Conceptual / Procedural / Application / Mixed]</span>
  <span class="meta-label">Learning goal</span>
  <span class="meta-value">[Two sentences, one thought each, under about 30 words. First: what a student who has this can do — "Students can …", scoped to the confirmed focus. Second: how that shows up in these items. Not "students understand [standard]".]</span>
  <span class="meta-label">Prerequisite standards</span>
  <span class="meta-value">[1–3 codes, each with a short gist]</span>
  <span class="meta-label">Leads to</span>
  <span class="meta-value">[1–2 codes]</span>
</div>

<div class="lc-focus">
  <strong>Focus</strong>
  [Three or four short sentences, students as the subject, one thought each: what students do in a teacher's words; the constraints the confirmed focus carries (number range, denominator set, operation, representational form) in a sentence of their own; why this focus now. A fact about the mathematics, not how it was settled.]
</div>

<div class="progression-ctx">
  <strong>Progression &amp; coherence context</strong>
  [2–3 sentences: what prerequisite understanding this assumes, what makes this standard's demand distinctive at this grade, and how that decides whether a response routes prior-grade or on-grade.]
</div>

<!-- Repeat per item -->
<div class="item">
  <!-- the same item-number / item-prompt / figure / choices markup as the student file, verbatim -->
  <h2>Correct answer &amp; interpretation guide</h2>
  <div class="correct-answer">✓ Correct answer: [Answer]</div>

  <table>
    <thead>
      <tr><th scope="col" style="width:22%">Response</th><th scope="col" style="width:40%">What it suggests</th><th scope="col">Suggested next step</th></tr>
    </thead>
    <tbody>
      <tr class="correct-row">
        <td>[Correct answer]</td>
        <td>Student [what they can now do, per the confirmed focus]</td>
        <td>[What extends or advances this]</td>
      </tr>
      <tr>
        <td>A. [Distractor]</td>
        <td>[What the student did, observably] — prerequisite gap: [prior-grade content not yet secure]</td>
        <td>[The specific prior standard code and the sub-skill to revisit]</td>
      </tr>
      <tr>
        <td>B. [Distractor]</td>
        <td>[What the student did, observably] — on-grade confusion: [which part of this demand]</td>
        <td>[Sub-skill or representation — distinct from every other row]</td>
      </tr>
      <!-- One row per remaining choice, same shape -->
    </tbody>
  </table>
</div>

<div class="look-for">
  <strong>What to look for across responses</strong>
  [2–3 sentences, grounded in the coherence map: whether a shared pattern points to one prior-grade gap those students can all be routed to, versus scattered on-grade confusions each needing different handling. Asset-based.]
</div>

</main>
</body>
</html>
```

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0

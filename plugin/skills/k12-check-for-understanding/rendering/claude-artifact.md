# Make the check as Claude slides

Use this when Step 5 found a **Slides** type. The check becomes a slide deck the teacher projects,
and the teacher guide becomes a Claude Doc.

`references/output.md` still sets the content: the items and their exact wording and order, what a
figure's description may say, the guide's sections, and no provenance. Its file names, styles and
HTML templates are only for the file path.

## The deck

Create it from the Slides type with the topic as its title, then follow the Slides type's own
instructions for writing and formatting it. Give each item its own slide: the prompt, any figure,
and the choices, large enough to read from the back of the room. Nothing else goes on the deck — no
answers, no notes for the teacher.

Draw a figure that has to be exact with a short Python script (matplotlib, or plain SVG), and give it
alt text by the same rule as a figure's `<desc>`: enough to work the item, never the item's work done.

## The teacher guide

Make it a Claude Doc, following Claude Docs' own instructions, with the sections of the teacher
template: each item word for word as on its slide, its answer and interpretation table, and what to
look for. Without Claude Docs functionality, write the guide as the teacher `.html` file instead.

## If it can't be made

If the deck can't be created or written, write both `.html` files as `references/output.md` says and
don't mention slides.

## Hand it over

Give the teacher the links in plain words. Don't talk about tools or formats. To revise, change the
affected slide and its place in the guide, and nothing else.

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0

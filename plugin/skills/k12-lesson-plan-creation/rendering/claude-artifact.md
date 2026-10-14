# Make the Claude Docs and the Design canvas

Use this when 5b found a **Design** type. One canvas per lesson holds the Design pages as US-Letter
pages the teacher edits in place in Claude and exports as a PDF to print.

`lesson.json` is the content. Everything in a document goes into its Doc or onto its pages, and
shared wording is used word for word. Its blocks say what a thing is, not how it looks. An answer
box, for example, just means room to write, so design each block in whatever way serves the page.

## Decide what each document becomes

Each `lesson.json` document becomes either a Claude Doc or Design pages on one Design canvas. Go by
what the document needs, not what it's called. Make it a Claude Doc when exact format and style
don't matter to its reader, such as notes, a prep sheet, or a plan an adult reads. Make it Design
pages as soon as element placement, spacing, font size or blank space matter, or it must print
exactly as laid out — e.g. a worksheet students write on, a sheet an adult fills in by hand. The
observation template is something the teacher writes on during class, so make it Design pages.
Without Claude Docs functionality, make every document Design pages. When uncertain, go with Design
pages.

## Create the canvas

Create it from the Design type with just the lesson title; you write the artboards afterwards. Skip
the canvas if no document became Design pages. The reply gives you the Design type's own
instructions and the canvas link. From then on, follow those instructions for how to write the
canvas's data and format each artboard. Reading and writing the canvas's data may need a second
tool; load it before deciding you can't write to it. If you can't create the canvas or can't write
to it, make every document a Word file with `rendering/docx.md` and don't mention a canvas.

If a design system is marked as the default, or the teacher names one, use it. Otherwise don't ask
about one.

## Give every printed page its own artboard

Give each document its own canvas page with a plain name, such as "Lesson plan", "Student materials"
or "Observation template". Keep all of a document's artboards on its page, and open the canvas on
the first document's page. That way exporting one page's artboards gives exactly that document.

Every printed page is its own fixed US-Letter artboard, 816 × 1056, one artboard per sheet of paper,
laid out left to right in reading order. Name each one for its document and page number, like
`student_materials-p1`, `student_materials-p2`, and use the plain name as its title. Student pages
and the observation template are always fixed pages, never tall or flowing ones.

Plan each page's height before you write it and budget element heights well. Don't render anything
past a page's limits, which will result in cut-off content. Fill each page before starting the next:
a new page begins when the next task or section will not fit, or where `lesson.json` starts one. A
writing space or grid that is last on a page runs down to the bottom margin, with the extra height
going to the space someone writes in, never to a header.

Write the canvas's settings first: the full list of artboards in order, the canvas pages — one per
document, named for it — and which canvas page it opens on. Then write the artboards, one batch per
document, each on its document's canvas page.

## Design freely

These are real classroom handouts. Make them the way a gifted teacher with a designer's eye would:
warm, visual, generous, and instantly clear about what to do first. Use big, friendly type for young
readers. Color, illustration, picture cues and emoji are welcome. (The Design type's "never emoji"
rule is about icons in polished design work; picture cues on a child's page are fine, and they print
fine.) Put a home-language gloss beside key words when the teacher named a language. Give the rule
or big idea a place of honor. Leave open room to write. Vary the layout to fit the task, not the
other way round.

## Draw math figures with Python

A figure that has to be exact — ticks on the lines, labels that don't collide, true size on paper —
is drawn by a short Python script you write and run each time, not by hand in HTML. Use matplotlib
if the sandbox has it (it lays out axes, ticks, labels and charts, and writes both formats:
`fig.savefig("figure.svg")`, `fig.savefig("figure.png")`); otherwise write plain SVG from the
standard library. Size the figure in inches (`figsize`, or 96 px per inch in SVG) so it prints at
true size, and put the `<svg>` element on the artboard. A Claude Doc takes an uploaded picture, not
pasted SVG (an uploaded SVG drops out of its Word and PDF exports), so save a PNG for a Doc. Draw a
figure once and reuse it wherever it appears.

Figures worth drawing this way: coordinate planes (blank, or with a plotted line, points, or a
polygon and its reflected image), number lines (ticks, arrows, marked points, relabeled ticks), grid
or dot paper, bar and line charts (blank or filled in), fraction bars, clock faces (with or without
hands), labelled shapes (side labels, vertex letters, angle arcs, right-angle marks, a dashed height
or diagonal), circles (radius, diameter, chord), and angles (two rays, an arc, its measure).
Anything else is built from lines, polygons, circles, arcs, dots and text.

Draw in black on white so it photocopies. Grid cells are square and at least a quarter inch (−8 to 8
needs about 4 inches), and a number line students mark runs most of the page's width. A figure
students plot or mark on is drawn blank.

## Keep them printable

The pages will be printed in black and white and often photocopied. Color may appear, but nothing
may depend on it. Every page's background must be plain white (#ffffff). Titles and table headers
are dark text (never white text on a filled bar, which photocopies as a black block). Keep a print
margin. Body text is at least 12 point, and a label on a writing space is the same size as the
question it answers.

An answer space is white space under its prompt with nothing drawn around it: no border, however
faint, no rounded corners, no fill. Size it based on grade — a 2nd grader's answer needs close to
three inches, a 10th grader's at least an inch and a half.

A blank within a sentence is writing space for students, not a placeholder: make it as long as the
words that go there, about 2 inches for one word and the rest of the line for a phrase, longer for
younger students. Set a height on every row someone writes in: about an inch and a half for a
student's cell, up to two for the youngest, 1+ inches on the observation grid. A row left to size
itself around empty cells collapses to almost nothing. The observation grid starts a page of its own
and its rows share that page.

Handwriting lines go only under full-sentence answers: by default in K–5, and from grade 6 up where
`lesson.json` marks the answer box `ruled: true` or the teacher asks for them. Students do their
math work in open space. But a math task whose answer is a written response follows the regular
rules for handwriting lines. When drawing lines, ensure they are all the same distance apart.

A number line or other drawing keeps its end labels and marks inside its own box with room to spare
since whatever touches the edge is cut off. Put Name and Date where students expect them.

Tiers, translations or an extra printable go on their own page of the same canvas as another series
of artboards.

Draw cut-outs at true size.

Put nothing on a page that only works on a screen.

A graphic the teacher projects goes instead on its own Design canvas page, "Teacher figures"

## Write the Claude Docs

Claude Docs' own instructions tell you how to create and edit a Doc. Make a Doc for each document
that became one, lesson plan first, titled with the lesson and the document's name. Put everything
from that document in `lesson.json` into the Doc, in the same order. For example, a phase heading
keeps its minutes. A `number_line` goes into the Doc as a picture the way Claude Docs'
instructions say. Read the first Doc back before writing the rest. If a Doc can't be created, make
that document Design pages instead and don't mention Docs to the teacher.

A `callout` is something the teacher has to find at a glance in the middle of a lesson, so in a Doc
it stands apart from the script around it: a block of its own (a quote block or a one-cell table)
with its label in bold on the first line.

## Check before you hand it over

Read the Docs and artboards back and compare them with `lesson.json`. The student pages should set
the same tasks as the plan: the same number of tasks, with the same numbers, reading level and level
of thinking. Everything a student page uses should be named in the plan's materials list and in the
phase that uses it. The exit ticket should read the same everywhere it appears. A figure or number
line the plan talks about is there to see, in the Doc or on the Teacher figures page. Nothing
students read or use belongs on a page unless it's in the file, decoration aside. If you added
something while designing, put it in `lesson.json` and the plan first. Fix any mismatch.

## Tell the teacher

Say in plain words what you made and where, with the links. Tell them they can print after exporting
to PDF. Ask them for any changes they want to make. Don't talk about tools or formats.

## Revise later

Change `lesson.json` first (5d). In a Claude Doc, edit just that part. If part of the Doc reads
differently from what you wrote, a person changed it; leave it alone unless it's the part you were
asked to change. On the canvas, read each affected artboard and keep the teacher's edits. Change
only what was asked and rewrite just that one; never recreate the canvas.

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0

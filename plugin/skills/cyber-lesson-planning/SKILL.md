---
name: cyber-lesson-planning
description: >
  Create safe, instructor-ready cybersecurity lessons, learner activities, hands-on labs, assessments, and standards or workforce alignment maps. Use for K-12 cyber education, digital citizenship, cybersecurity career exploration, college or adult workforce training, educator professional development, defensive-security labs, and certification-aligned instruction. Trigger on requests to teach cybersecurity concepts or build cyber curriculum, workshops, classroom activities, tabletop exercises, or authorized lab experiences. Do not use to operate against real or unauthorized systems, obtain real credentials, deploy malware, or facilitate harmful cyber activity; convert those requests into safe simulations or defensive analysis exercises.
---

# Cyber Lesson Planning

Create a complete Ready Force Cyber OpenED instructional packet from one source JSON. Preserve
technical rigor while adapting delivery for K-12 learners, college students, career changers,
working professionals, or educators.

## Required references

Read only the references needed for the request:

- Always read `references/safety-policy.md`.
- Read `references/learner-pathways.md` to select the audience and support profile.
- Read `references/framework-alignment.md` when standards, careers, competencies, or
  certifications matter.
- Read `references/lab-design.md` for any hands-on activity, demonstration, cyber range, VM,
  terminal, network, log, packet, or code exercise.
- Read `references/assessment.md` before writing the performance task and rubric.
- Use `references/example_cyber_lesson.json` as the rendering schema example.

Do not claim a framework mapping from memory when a current official source is available.

## Workflow

### 1. Route the request

Determine:

- Learner type: K-5, grades 6-8, grades 9-12, college, career changer, professional, or educator.
- Experience: first exposure, beginner, intermediate, or advanced.
- Delivery: in person, live online, self-paced, train-the-trainer, or blended.
- Activity: concept lesson, tabletop, static artifact analysis, guided lab, challenge lab, or
  assessment.
- Environment: no lab, browser sandbox, local VM, container, cyber range, or instructor demo.
- Alignment: CYBER.ORG, state/district standard, NICE, certification objective, employer
  competency, or teacher-provided curriculum.

Ask at most two content questions when missing information would materially change safety or
the instructional design. The highest priorities are learner level and lab environment. Apply
reasonable defaults for everything else and state them in the instructor guide.

### 2. Apply the safety gate

Follow `references/safety-policy.md` before drafting technical procedures.

For hands-on work, require an owned, supplied, or explicitly authorized environment. Record the
authorization scope in the packet. Never instruct learners to test public targets, school
production systems, third-party accounts, or systems outside the lab.

If authorization or containment is unclear, create a safe alternative using synthetic logs,
offline packet captures, supplied code, screenshots, tabletop cards, or a toy local service.

### 3. Define the outcome

Write one observable outcome using this pattern:

> Given [safe environment or artifact], the learner will [observable action], producing
> [evidence], meeting [success criteria].

For workforce lessons, assess work at the task level. For K-12 lessons, preserve the selected
grade-band standard and make the performance age appropriate.

### 4. Ground the lesson

Use current primary sources for volatile technical claims, tool syntax, vulnerabilities,
framework components, and certification objectives. Record source names, links, versions, and
verification dates in the instructor guide. Never invent a standard identifier, NICE statement,
CVE, command, tool output, or certification objective.

Use CYBER.ORG for K-12 cybersecurity outcomes when no district framework is supplied. Use NICE
Task, Knowledge, and Skill statements for workforce alignment. Treat certification objectives as
additional mappings, not substitutes for performance evidence.

### 5. Build the learning sequence

Use this default arc:

1. **Connect** - establish relevance, prior knowledge, and career context.
2. **Model** - demonstrate the concept or analysis process safely.
3. **Practice** - guide learners through the first evidence-producing task.
4. **Perform** - require an independent or collaborative performance.
5. **Debrief** - discuss decisions, ethics, limitations, and transfer.
6. **Assess** - collect the specified evidence with the rubric.

For educator professional development, add facilitation moves, expected misconceptions,
troubleshooting, and a rehearsal or teach-back.

### 6. Differentiate without lowering the target

Use support profiles rather than ability labels:

- **Guided** - vocabulary, worked example, checkpoints, command explanations, and templates.
- **Standard** - normal instructions and reference material.
- **Challenge** - less scaffolding, ambiguous evidence, tradeoff analysis, or extension constraints.

Keep the same observable outcome and core evidence across profiles. Add an offline or no-command-
line alternative when technology access could exclude learners.

### 7. Compose the packet

Create one JSON source with a `shared` registry and these `documents` entries:

- `instructor_guide` - objectives, alignment, setup, safety, sequence, facilitation,
  troubleshooting, expected evidence, and answer guidance.
- `learner_activity` - scenario, authorized scope, tasks, evidence capture, reflection, and cleanup.
- `performance_rubric` - criteria with observable proficiency descriptors.
- `alignment_map` - standards or workforce mappings, career connection, sources, versions, and
  verification dates.

Add `lab_setup` as a fifth document when tools, accounts, images, VMs, containers, or reset steps
are required. Add a separate `answer_key` when placing answers in the instructor guide would make
it unwieldy.

Use synthetic people, domains, organizations, credentials, IP addresses, and logs. Use reserved
example domains and documentation address ranges where applicable.

### 8. Validate before rendering

Confirm all of the following:

- The learner activity states the authorized target and stop conditions.
- No real credentials, personal data, public targets, or production identifiers appear.
- Every command matches the stated operating system and tool version.
- Expected observations and recovery steps are present.
- Every assessment criterion points to evidence learners actually produce.
- Framework identifiers and quotations are sourced and current.
- Guided, Standard, and Challenge supports preserve the same competency.
- Instructions include accessibility and low-bandwidth alternatives where relevant.
- Instructor and learner documents do not contradict each other.
- Every normalized document ID is unique.

### 9. Render and deliver

Write the source as `cyber_lesson.json`, then run:

```bash
bash scripts/render_all.sh cyber_lesson.json "$OUTPUT_DIR"
```

Confirm that every document has both `.docx` and `.html` output and is non-empty. Deliver the
Word documents together. Keep the JSON and HTML files for revision turns.

## Revision rules

Edit the source JSON and re-render the full packet. When the user changes the scenario, tools,
operating system, audience, or standard, search every document for stale references. Re-run the
safety gate whenever the target or environment changes.

Never present a technically uncertain procedure as verified. State the limitation and offer a
safe, source-grounded substitute.

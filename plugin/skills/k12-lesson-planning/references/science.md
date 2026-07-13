<!--
SPDX-FileCopyrightText: 2026 Anthropic, PBC
SPDX-FileCopyrightText: 2026 Learning Commons
SPDX-License-Identifier: Apache-2.0
-->

# Science — lesson pedagogy

Loaded by `k12-lesson-planning` when the subject is **science**.

## Clarify

Before asking anything, assess the following from all available conversation signals:

**1. State detection:** Scan the conversation for any state signal — teacher mentions a state name, uses state-specific codes (TEKS, SOL, OAS, CA-NGSS, etc.), or says "I teach in [state]." If found, store as state = [state name] and pass it as jurisdiction in the KG standard lookup. Update the default standard framework to match.

**2. Curriculum detection.** Look for signals that the teacher is using OpenSciEd anywhere in the conversation — not just the current prompt: explicit name ("OpenSciEd", "OSE"), OSE-specific terminology (anchoring phenomenon, driving question, consensus model, "figuring out"), or context that makes OSE use probable. If signals are present, treat as **OSE-confirmed** and proceed. If absent, treat as **not OSE-confirmed**.

**3. Grade band.** Determine from grade level which band applies:
- **K–2**: concrete phenomena, teacher-facilitated sensemaking, oral and drawn models
- **3–5**: transitional — written Claim-Evidence-Reasoning (CER) begins, mechanistic models, simple data analysis
- **6–8**: integrated across disciplines, quantitative reasoning, formal argumentation
- **9–12**: mathematical modeling, extended investigations, societal/ethical dimensions

**4. Standard and phenomenon context.** Note whether the teacher has specified a state or NGSS Performance Expectation code (e.g., `MS-LS2-3`) or a topic. Note whether they've specified an anchoring phenomenon or unit context. If not, draw from the KG calls (see learning-commons-kg.md). Flag any selections in Section 1 as suggested.

When key information is missing, ask. Priority: (1) grade level if missing, (2) topic or standard if missing, (3) unit position if helpful context (4) state if not inferable. Infer everything else. Defaults applied silently: NGSS, 45–60 min, universal access design.

---

## Standards grounding

Follow **Step 2 — Ground in standards** in SKILL.md: if the Learning Commons Knowledge Graph
is connected, use the Science section of `references/learning-commons-kg.md`; if not,
proceed from best knowledge and add the disclaimer footer.

## Build the lesson

**For all lessons** 
include at least one visual scaffold with a teacher-facing rationale justifying the choice. 

Also be sure that overall timing and timing for each section is realistic - do not overload the lesson.

### Curriculum branching — apply before drafting

**If OSE-confirmed (OpenSciEd):**
The teacher already has the OpenSciEd curriculum. Write a **distinct lesson** that complements rather than duplicates what they already have — do not replicate or lightly adapt any OSE lesson. Use the KG OSE materials (learning-commons-kg.md, Science call 2) to understand what phenomenon, practices, and routines OSE uses for this standard, then design an original investigation and discussion sequence that covers the same three-dimensional learning differently.

Use OSE format and language throughout, on top of the grade-band structure below:
- Learning targets stated as "Students will figure out…" or "Students will use [SEP] to [DCI/CCC]"
- Driving question posted and returned to at lesson close
- Consensus model revision as the primary explanation-building move
- Class tracking board or "what we know / what we're still figuring out" updated each lesson
- CER (Claim–Evidence–Reasoning) as the formative writing structure

**If not OSE-confirmed:**
Use the KG OSE materials (learning-commons-kg.md, Science call 2) as an HQIM design exemplar — draw on phenomenon selection, practice foci, and task logic to calibrate quality, then write original content. Do NOT use OSE-specific terminology: no "consensus model", no driving question framing, no OSE unit or lesson references in the plan.

---

### Grade band — apply before drafting

Grade band is the primary structural branch. Determine from grade level and apply the matching structure.

---

#### K–2: Concrete Phenomena, Teacher-Facilitated Sensemaking

Phases: Launch Phenomenon → Investigation → Sensemaking Discussion → Model/Representation → Exit Ticket

- **Launch Phenomenon — 5–10 min**: Show or do the phenomenon directly — something students can observe, touch, or watch. Do NOT explain it. Ask: "What do you notice? What do you wonder?" Record student observations and questions. Post the lesson's driving question in simple language.
- **Investigation — 15–20 min**: Hands-on exploration. Students observe, sort, measure, or build. Activity generates concrete data or observations relevant to the phenomenon. Instructions are brief, visual, and modeled. Students record through drawing + simple labels — not fill-in-the-blank worksheets.
- **Sensemaking Discussion — 10 min**: Teacher facilitates whole-class discussion using students' observations as raw material. Ask students to share what they noticed and connect it to the driving question. Teacher does NOT reveal the explanation — students construct it. Record emerging ideas on board.
- **Model/Representation — 5–10 min**: Students draw a model to explain what they think is happening. For OSE-confirmed: students update a class consensus model displayed on the wall. Focus on: what you can see AND what you can't see but infer.
- **Exit Ticket — 3–5 min**: One drawing or oral prompt: "Draw what you think is happening and tell me why."

**Non-negotiables for K–2:**
- Phenomena must be directly observable — no abstract explanations, no videos of distant phenomena as the primary hook.
- Investigation before explanation — students collect data first; teacher does not explain the phenomenon before they investigate.
- Models are the primary representation — drawings that show mechanism, not just illustration.

---

#### Grades 3–5: Written Claim-Evidence-Reasoning Begins, Mechanistic Models

Phases: Launch Phenomenon → Investigation → Sensemaking Discussion → Claim-Evidence-Reasoning Writing → Model Update → Exit Ticket

- **Launch Phenomenon — 5–10 min**: Present a specific, puzzling observable event. Do NOT reveal the explanation. Ask: "What do you notice? What do you wonder? What questions do we need to answer to explain this?" Post the driving question. Connect explicitly to prior lessons: "Last time we figured out ___. Does that help us here?"
- **Investigation — 15–20 min**: Students carry out an investigation (lab, data analysis, or scientific text analysis) to gather evidence. Assign a clear SEP role: are they planning an investigation, analyzing data, or constructing an explanation from a text? Students record data in a structured format. Look-fors: 3+ named, with specific student behaviors and teacher moves.
- **Sensemaking Discussion — 10–15 min**: Think-Write-Pair-Share → whole class. Teacher sequences student responses from simple observations toward mechanistic explanations. Push explicitly toward the CCC: "What pattern do you notice in your data? What does that tell us about cause and effect here?"
- **Claim-Evidence-Reasoning Writing — 10 min**: Students write a structured response. Claim–Evidence–Reasoning format required.
- **Model Update — 5 min**: Students add to or revise their model to incorporate today's new understanding. What changed? What does the model now show that it didn't before?
- **Exit Ticket — 3–5 min**: A new small phenomenon (not the one investigated). Students apply today's CCC/DCI: "Use what you figured out today to explain why ___." Sort: *Got it* / *Almost there* / *Needs re-teaching*.

**Non-negotiables for 3–5:**
- CER every lesson that involves investigation. If a student's response doesn't include evidence from the investigation and reasoning that connects it to a science idea, it is not complete.
- Models must be mechanistic — show how and why, not just label what. A labeled diagram that could have been drawn before the lesson is not a model revision.
- Crosscutting concepts must be named explicitly by students, not just implied. Teachers should post the relevant CCC and require students to use it in discussion and writing.

---

#### Grades 6–8: Integrated, Quantitative, Formal Argumentation

Phases: Launch Phenomenon → Investigation → Argumentation Discussion → Claim-Evidence-Reasoning Explanation → Model Revision → Formative Check

- **Launch Phenomenon — 5–10 min**: Present a specific, complex observable event. Students write a brief initial explanation before investigating (they will return to this). Post the unit driving question. Connect to the unit storyline: "We've been trying to explain ___. Last lesson we figured out ___. Here's something new that our model needs to be able to explain."
- **Investigation — 20–25 min**: Students carry out a quantitative investigation or data analysis. Assign the SEP explicitly. Mathematical reasoning is central — graphs, rates, proportions, computational models as appropriate. Students should be analyzing, interpreting, and making sense of data — not just recording it. Look-fors: 3+ named, with specific behaviors and teacher moves for both the SEP in use and the foregrounded CCC.
- **Argumentation Discussion — 15 min**: Students defend claims with data. Teacher facilitates evidence-based argumentation — not just sharing answers. Require students to cite specific data points, not just patterns. Push toward the CCC explicitly: "What does your data tell us about [energy and matter / systems / cause and effect]?" For OSE-confirmed: update class consensus model or tracking board as part of discussion.
- **Claim-Evidence-Reasoning Explanation — 10 min**: Written evidence-based explanation. Grades 6–7: Claim-Evidence-Reasoning format. Grade 8: introduce competing explanations — students must address and rebut an alternative explanation.
- **Model Revision — 5–10 min**: Revise the explanatory model (individual and/or class consensus) to reflect new understanding. What does the model now explain that it couldn't before? What does it still not explain?
- **Formative Check — 5 min**: Students compare their opening quick-write to their revised explanation: "What changed in your thinking? What specific evidence caused that change?"

**Non-negotiables for 6–8:**
- Quantitative reasoning is not optional. If the data is quantitative, students must use numbers — not just qualitative descriptions — in their claims and CERs.
- Argumentation requires evidence from the investigation, not from prior knowledge. "I already knew that" is not scientific evidence.
- Model revision is cumulative. By the end of the unit, the class consensus model should visibly show the progression of understanding across lessons.

---

#### Grades 9–12: Mathematical Modeling, Societal Dimensions, Sustained Investigation

Phases: Launch Phenomenon → Investigation → Scientific Argumentation → Explanation/Modeling → Science-Society Connection → Formative Check

- **Launch Phenomenon — 5–10 min**: A complex, socially or scientifically relevant observable phenomenon. Students write an initial mechanistic explanation independently — silence is productive. Post the unit driving question. Connect to the unit's developing explanatory model: what piece of the big puzzle does this lesson investigate?
- **Investigation — 20–25 min**: Extended, student-directed investigation. Students may be designing their own procedures, analyzing real-world data sets, using computational simulations, or evaluating competing models. Mathematical modeling is central where relevant — equations, graphs, computational tools as explanatory tools. Look-fors: 3+ named for both the primary SEP and the CCC.
- **Scientific Argumentation — 15 min**: Student-to-student discourse. Teacher probes; does not direct. Students cite specific data and quantitative evidence. Surface competing explanations or models and evaluate them. Require: "What evidence would make you change your mind?" Always debrief argumentation quality, not just content: "Did we distinguish between a claim and evidence? Whose idea changed because of someone else's evidence?"
- **Explanation/Modeling — 15 min**: Sustained written explanation or formal model construction. Uses SEPs at full sophistication: develop a mathematical model, construct a scientific explanation citing quantitative evidence, design a solution with engineering justification. Counterclaim or alternative-model acknowledgment required.
- **Science-Society Connection — 5 min**: Explicit discussion of implications: how does this scientific understanding connect to a real-world decision, policy, or ethical question? This is not optional enrichment — it is part of the NGSS vision for high school science.
- **Formative Check**: Students return to opening quick-write. Self-assess: "What in your original explanation was correct? What was incomplete or wrong? What specific evidence revised your thinking?"

**Non-negotiables for 9–12:**
- Mathematical models are explanatory, not decorative. An equation or graph that a student cannot connect to a physical mechanism is not modeling — it is calculation. Students must explain what each variable represents and why the relationship takes the form it does.
- Scientific uncertainty is explicit. High-quality HS science acknowledges where models break down, where data is limited, and what remains genuinely unknown. Treating scientific knowledge as settled facts undercuts the epistemic goal of the standards.
- Science–society connections are substantive, not tacked on. Require students to reason from the science to the social/ethical implication — not just name a "real-world connection."

---

### Section structure — all grade bands

1. **At a glance** — standard verbatim in a `special` callout; a one-line lesson arc naming the phases with minutes so the period's shape is visible before any detail; anchoring phenomenon (title / brief description, or [suggested] flag); materials list — name each item plainly (e.g. "Data-recording cards")
2. **Three-dimensional learning targets** — state each dimension explicitly and separately, with framework names spelled out: Science and Engineering Practice ("Students will [practice verb] to [purpose]"); Disciplinary Core Idea ("Students will understand that [specific content idea]"); Crosscutting Concept ("Students will apply [named concept] to [specific use]"). Do not merge dimensions into a single vague objective.
3. **Unit storyline context** — 2–3 sentences. When the teacher has said where this lesson sits in a unit, place it: what students figured out last time, how today advances the explanation. When they haven't, write the lesson to stand alone and connect it by concept, not by position — name the ideas it builds on and the ones it pairs with ("builds on what students know about living things; pairs naturally with cells whenever you teach them"). Schools sequence topics their own way; a placement guess from the standards' canonical order is only right for schools that follow it.
4. **Vocabulary** — a reference list of the terms this lesson introduces, with
   student-friendly definitions. A term is here because a phase teaches it (anchored to
   something concrete — the diagram, an analogy, what students just observed); a term on a
   student page that no phase teaches is a gap in the lesson, not in this list.
5. **Anticipated student ideas & misconceptions** — up to 3 entries from the KG OSE-materials call or training knowledge, each formatted: *What students think* / *Why it persists* / *Teacher move*
6. **Lesson sequence** — phases per grade band above; in every investigation phase: 3+ look-fors each naming the specific student behavior, why it matters for the 3D standard, and what to do; in every discussion phase: specific science-based prompts (not generic)
7. **Design notes** — last section, after the exit ticket: 2–3 elements to keep intact when adapting, each with a brief reason grounded in three-dimensional learning, including the lesson's central representation (model, diagram, or data display) and its one-sentence why.

→ **Section structure complete. Proceed to the draft (when the teacher chose one) or Step 5.**

## Exit ticket guidance

The exit ticket is the last phase in Lesson Sequence (`from_shared:exit_ticket` under its phase header). One item that requires students to apply today's DCI using a SEP and the lesson's CCC. K-2: a drawing or oral prompt. 3-5: a new small phenomenon (not the one investigated) that students explain using what they figured out today. 6-12: return to the opening quick-write and self-assess what evidence changed your thinking. Three sort buckets (Got it / Almost there / Needs re-teaching).

---


## Writing lesson.json — science mapping

When you reach Step 5 (Output) in SKILL.md, map science content to the material-source JSON like this:

- `shared.subject`: `"Science"`
- `shared.standard_code` / `shared.standard_text`: the Performance Expectation, verbatim
- `shared.anchor_task`: the anchoring phenomenon —
  `{teacher: <how to present it without explaining it>, student: <what students observe/do>}`.
- Each investigation or explanation task as `shared.t1`..`tN`:
  `{teacher: <facilitation script>, student: <the task as students read it>, stimulus?: [data
  table or diagram blocks both pages show]}`.
- `shared.exit_ticket`: `{student: <prompt>, teacher?: <collection note>}`. The sort
  criteria are a `cards` block you place in the lesson plan after pulling the exit
  ticket (see `example_lesson.json`).
- Three-dimensional learning targets: three separated bullets, one per dimension, each
  labeled with the spelled-out name (Science and Engineering Practice / Disciplinary Core
  Idea / Crosscutting Concept).
- In the observation template, prefix each look-for with its dimension so the teacher sees
  which one they're watching for.
- `shared.vocabulary`, `shared.misconceptions`, `shared.look_fors` as in the SKILL.md schema.
- Student-page section headings in plain inquiry language ("What do you notice?",
  "Investigation") — you compose them directly in the document's sections.


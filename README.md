# Agent Skills for K-12 Teachers
Source code and evaluation framework for the agent skills that are included with [Claude for Teachers](https://claude.com/solutions/teachers). 

Included are four skills:
- `k12-lesson-plan-creation`: Builds classroom-ready, standards-aligned lesson plans, optionally aligned to a teacher's curriculum
- `k12-lesson-differentiation`: Adapts an existing lesson into tiered versions (below / at / above proficiency-level) and for specific student needs, keeping core content consistent across tiers
- `k12-lesson-prep`: A prep partner for a lesson the teacher already has; works through the key student task with them and leaves a short teacher-only prep note
- `k12-check-for-understanding`: Builds a 1–3 item formative check for a math standard, with distractors drawn from documented misconceptions and a teacher guide routing each response to a next step

Where noted, materials in this repo were co-developed between Anthropic and Learning Commons, who collaborated to help Claude create classroom materials that are grounded in academic standards and follow best practices from learning science research.

The skills are written to make effective use of the Learning Commons Knowledge Graph [Claude connector](https://claude.com/connectors/learning-commons-knowledge-graph) that is included for all teachers using Claude for Teachers. This connector provides Claude with access to academic standards across all 50 states and progressions beneath them; adapt the skills if your environment does not have access to these tools.

## Quick start
There are two options to use these skills:

**In Claude for Teachers:**
If you have a Claude for Teachers account, there is no extra install needed. These skills are already installed for you.

**In other places:**
Load the plugin or skills manually. For instance, in Claude Code:

```
git clone https://github.com/anthropics/k12-teacher-skills
claude plugin marketplace add ./k12-teacher-skills
claude plugin install k12-education@k12-teacher-skills
```

## Layout

- `plugin/` - Main skill content bundled as a plugin; also includes teacher-focused 3rd party MCP servers that are available for users to enable
- `evals/` - Contains our evaluation framework and how to adapt them for your use case

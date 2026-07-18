# Safe Lab Design

## Select the least risky environment that meets the outcome

1. Static artifact analysis
2. Tabletop simulation
3. Browser sandbox or toy service
4. Local container or VM
5. Managed cyber range

Do not add a live lab merely to make a lesson feel hands-on. The learner must produce evidence tied
to the outcome.

## Lab contract

Document:

- Environment type and owner
- Operating system and version
- Required tools and versions
- Network requirements
- Privilege requirements
- Authorized target
- Explicit out-of-scope targets
- Starting state
- Expected observations
- Stop conditions
- Cleanup/reset procedure
- Offline alternative

## Procedure quality

- Test or verify commands against the stated platform.
- Explain consequential flags and expected outputs.
- Use placeholders that cannot be mistaken for real targets.
- Separate learner commands from expected output.
- Include recovery after likely mistakes.
- Avoid piping downloaded content directly into a shell.
- Avoid runtime dependency installation when a prepared image or locked environment is practical.
- Do not require learners to weaken their host operating system.

## Evidence patterns

Prefer durable work samples:

- Annotated log excerpt
- Incident timeline
- Detection query and explanation
- Hardening checklist with verification
- Packet or protocol analysis table
- Risk decision with evidence
- Help-desk or incident ticket
- Short defensive script with tests
- Executive or peer briefing

Screenshots alone are weak evidence unless paired with explanation and a verifiable result.

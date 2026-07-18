# Cyber Instruction Safety Policy

Apply this policy to every cyber lesson, including apparently benign demonstrations.

## Authorization gate

Permit technical interaction only with:

- A local machine owned by the learner and intentionally configured for the lesson.
- An instructor-supplied VM, container, cyber range, toy service, or browser sandbox.
- A static artifact such as synthetic logs, a supplied packet capture, screenshots, or code.
- A system for which the user has clearly stated authorization and scope.

If scope is missing or ambiguous, do not provide operational steps against a target. Convert the
activity to a static analysis, simulation, tabletop, toy local service, or instructor demonstration.

## Prohibited lesson content

Do not create activities that require learners to:

- Scan, probe, exploit, disrupt, or evade controls on public or third-party systems.
- Use real passwords, access tokens, session cookies, student accounts, or staff accounts.
- Collect personal data, employee addresses, or identifiable student records.
- Deploy self-propagating code, persistence, destructive payloads, credential theft, or covert
  collection.
- Disable security controls outside a contained lab.
- Contact real victims, threat actors, or external infrastructure.

When a requested objective overlaps these areas, teach the defensive concept using inert samples,
synthetic evidence, pseudocode, detection logic, or a contained emulation.

## Required lab framing

Every learner-facing lab must state:

1. The authorized environment and target.
2. What is outside scope.
3. Stop conditions.
4. Data-handling requirements.
5. Reset, cleanup, and recovery steps.
6. How to report unexpected behavior.

## Privacy

Request only anonymized learner needs. Never request names, student IDs, email addresses,
credentials, identifiable IEP or 504 records, or identifiable work samples. Describe accommodations
functionally, such as "requires chunked directions" or "uses a screen reader."

Use synthetic identities and `example.com`, `example.org`, or `example.net`. For documentation IP
addresses, use ranges reserved for examples rather than routable addresses.

## Age appropriateness

- K-5: emphasize protective habits, help-seeking, privacy, and ethical choices; avoid operational
  attack procedures.
- Grades 6-8: use simulations and defensive reasoning with tightly bounded tools.
- Grades 9-12: permit contained technical practice with explicit authorization and reset steps.
- Adults: preserve the same containment rules even when the content is advanced.

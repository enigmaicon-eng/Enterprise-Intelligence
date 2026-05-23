# Architecture Critique Prompts
## Version: v1.0

---

## Full Architecture Critique

```
Read: [path to architecture document]
Also read:
  knowledge/technical/context-engineering.md
  knowledge/technical/reliability.md
  knowledge/technical/deployment-patterns.md
  knowledge/systems/systems-thinking.md

Apply 5 lenses:

LENS 1 — PRINCIPLE COMPLIANCE
For each key design decision in the document:
  State the decision in one sentence.
  Identify the relevant principle from the knowledge files.
  Verdict: Aligns | Violates | Tension
  If violates or tension: cite exact principle (file:section) + what specifically conflicts.

LENS 2 — COVERAGE GAPS
Using knowledge/technical/reliability.md failure mode taxonomy:
  What failure modes does this architecture address?
  What failure modes are not addressed?
  List unaddressed modes + their severity if they occur.

LENS 3 — INTERNAL CONSISTENCY
  Are there contradictions between sections of this document?
  Does any constraint in one section undermine an approach in another?

LENS 4 — LEVERAGE LEVEL (from systems/systems-thinking.md)
  At what level of Meadows' hierarchy is this architecture intervening?
  Is this the right level, or is it a high-level problem solved with a low-level intervention?

LENS 5 — TOKEN/CONTEXT BUDGET (if applicable)
  Does the architecture state overhead targets?
  Do they align with knowledge/technical/context-engineering.md budget model?
  (Green <3,500 tokens | Yellow 3,500-4,000 | Red >4,000)

Score each finding: P0 | P1 | P2 | PASS
Output: findings table + highest-priority finding with specific remediation.
```

---

## Quick Consistency Check

```
Read: [path to architecture document]

Check only:
1. Internal consistency — does section A contradict section B anywhere?
2. Stated vs. actual scope — does the document's "purpose" match what it actually specifies?
3. Missing sections — what would a reader need that isn't here?

Output: 3-bullet findings. This is a 5-minute check, not a full critique.
```

---

## Post-Build Architecture Review

```
A new system phase was just completed.
Primary architecture document: [path]
Supporting documents: [list any other new architecture files]

Load all new architecture files.
Check against the 4-layer context contract from architecture/CONTEXT-ARCHITECTURE.md:
  Layer 1 (CLAUDE.md): does any new content belong in CLAUDE.md but isn't there?
  Layer 2 (memory/): does any new state content belong in memory files?
  Layer 3 (skills): are new skills registered in CLAUDE.md routing table?
  Layer 4 (knowledge): are new knowledge entries in KNOWLEDGE-INDEX.md?

Also check: does the new system create any routing ambiguity with existing skills?
List any signals that could trigger both the new skill and an existing skill.

Output: layer contract compliance + routing conflicts.
```

---

## Principle Extraction (New Domain)

```
A system has been built and documented in: [path]
No formal knowledge entry exists for this domain yet.

Read the architecture document and extract:
1. The 3-5 most important design principles the document implies (even if not stated explicitly)
2. For each: the mechanism — why does this principle matter?
3. The failure mode if the principle is violated

These principles are candidates for a new knowledge entry.
Format each as: "Principle: [statement]. Mechanism: [why]. Failure if violated: [what happens]."
```

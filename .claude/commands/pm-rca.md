---
name: pm-rca
description: Run a root cause analysis on a product problem, execution failure, or metric anomaly. Uses 5-why discipline to reach causal root, not symptomatic fixes.
version: "1.0"
changed: 2026-05-20
---

# PM Root Cause Analysis

**Input:** Problem description inline — can be a metric anomaly, execution failure, stakeholder complaint, or recurring pattern.

**Output:** Written to `decision-frameworks/decisions-log.md` (as a RCA entry) and displayed in terminal.

---

## Steps

1. **Read context.** Load `knowledge/pm/discovery-intelligence.md` (5-why section). If the problem involves metrics, also read `knowledge/pm/metrics-experimentation.md`.

2. **Define the symptom precisely.** Vague problems produce vague root causes. Precise the problem:
   - What is happening? (Observable, specific)
   - What is the magnitude? (How often? How much? Compared to what baseline?)
   - When did it start? (Point in time, or gradual drift?)
   - Where does it occur? (All users? Specific segment? Specific surface?)
   - What doesn't have this problem? (The contrast case often contains the cause)

3. **Run the 5-why chain.** For each why:
   - State the answer as a specific, observable claim — not a theory
   - Ask: is there evidence for this answer, or is it an assumption?
   - If it's an assumption, flag it and note what would prove or disprove it
   - Stop when: the next why leads outside the system, or when fixing the cause would prevent all upstream symptoms

4. **Distinguish contributing factors from root cause.** A root cause is the condition whose removal would prevent the problem. Contributing factors make the problem more likely or more severe but are not the cause.

5. **Apply systems thinking check.** Load `knowledge/pm/systems-thinking-pm.md` if the problem shows signs of a systemic pattern:
   - Is this a reinforcing loop (problem compounds itself)?
   - Is this a balancing loop that's been disrupted?
   - Does fixing the symptom create pressure elsewhere (shifting the burden archetype)?

6. **Produce recommended actions.** Distinguish:
   - Immediate fix: what stops the bleeding now?
   - Root cause fix: what prevents recurrence?
   - System fix: what changes the structure that produced the root cause?

7. **Write the output.**

---

## Output Format

```markdown
# Root Cause Analysis — [Problem Name] — [Date]

## Problem Definition (precise)
**What:** [Observable symptom]
**Magnitude:** [Quantified — compared to baseline]
**When:** [Point in time or drift period]
**Where:** [Scope — users, surfaces, segments affected]
**Contrast case:** [What does NOT have this problem — important clue]

## 5-Why Chain

**Symptom:** [Precise statement]

Why 1: [Answer] — Evidence: [Source] — Assumption flag: [Yes/No]
  Why 2: [Answer] — Evidence: [Source] — Assumption flag: [Yes/No]
    Why 3: [Answer] — Evidence: [Source] — Assumption flag: [Yes/No]
      Why 4: [Answer] — Evidence: [Source] — Assumption flag: [Yes/No]
        Why 5: [Root cause statement]

## Root Cause
[One precise statement. Fixing this would prevent the symptom and all intermediate causes.]

## Contributing Factors
- [Factor] — [How it amplifies the problem but is not the root]

## Systems Dynamics (if applicable)
[Reinforcing loop / Balancing loop disruption / Archetype — describe the structural pattern]

## Unvalidated Assumptions in This Analysis
- [Assumption] — [What would confirm or refute it]

## Recommended Actions

**Immediate (this week):**
- [Action] — Owner: [name]

**Root cause fix (this quarter):**
- [Action] — Owner: [name] — [Prevents recurrence by...]

**System fix (strategic):**
- [Action] — [Changes the structure that produced this root cause]

## What Would Make This Analysis Wrong
[What assumption, if incorrect, would change the root cause conclusion?]
```

---

## Quality Gate

- Problem is precise and quantified before any whys are run
- Each why is a specific, observable claim — not a generic theory
- Assumption flags noted where evidence is absent
- Root cause statement is specific enough that someone could fix it
- Actions distinguish immediate fix from root cause fix from system fix
- At least one "what would make this wrong" challenge included

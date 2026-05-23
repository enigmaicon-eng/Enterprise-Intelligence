---
name: pm-retro
description: Facilitate a sprint retrospective or initiative post-mortem. Produces structured reflection with root cause analysis on what slipped, pattern identification, and 1-2 actionable commitments.
version: "1.0"
changed: 2026-05-20
---

# PM Retro

**Input:** Sprint number / initiative name, brief description of what happened (what shipped, what didn't, any notable events). Optional: team notes if available.

**Output:** Written to `reviews/weekly/YYYY-WW-retro.md`

**Use for:** Sprint retrospectives (recurring, bi-weekly) AND initiative post-mortems (major milestones, launches, failures).

---

## Steps

1. **Read context.** Load the sprint workflow from `workflows/pm/sprint-workflow.md` (retro section). If this is an initiative post-mortem, also read `decision-frameworks/pm/risk-radar.md`.

2. **Distinguish retrospective from post-mortem:**
   - **Sprint retro:** Improve the team's way of working. Focus on process, collaboration, and mechanics.
   - **Initiative post-mortem:** Learn from a major outcome. Focus on decisions made, assumptions held, and what would have changed the outcome.

3. **For sprint retro:**
   - What went well? (Preserve these deliberately)
   - What was hard? (Root cause, not just description)
   - What should change? (Specific mechanic, not principle)
   - Generate 2-3 potential action items; team picks 1-2 with clear owners

4. **For initiative post-mortem:**
   - What happened? (Timeline of key events — factual)
   - What decisions were made and on what information?
   - What assumptions were we making that turned out to be wrong?
   - What signals were present that we didn't act on?
   - What would we do differently?
   - What should the organization learn from this? (Systemic insight, not individual blame)

5. **Apply root cause discipline.** For the most important "what was hard" or failure: run at least two levels of why. Surface the structural cause, not just the proximate cause.

6. **Generate action items.** Maximum 2. Named owner. Specific mechanic. Testable in the next sprint.

7. **Write the output.**

---

## Output Format — Sprint Retro

```markdown
# Sprint Retro — Sprint [N] — [Date]

**Team:** [Team name]  **Facilitated by:** [PM name]

---

## What Went Well (preserve deliberately)
- [Specific thing — name what to keep doing and why]
- [Specific thing]

## What Was Hard (with root cause)
- [Problem description] → Root cause: [one level deeper — what caused this?]
- [Problem description] → Root cause: [why did this happen?]

## What One Thing Would Have Made This Sprint Better?
[Team's single most important answer — synthesized if discussed in group]

---

## Action Items (max 2)

| Action | Owner | How we'll know it worked | Try in |
|---|---|---|---|
| [Specific mechanic — not "communicate better"] | [Name] | [Observable change] | Next sprint |
| [Specific mechanic] | [Name] | [Observable change] | Next sprint |

---

## Sprint Metrics
- Commitment rate: [N]% ([N] of [N] stories shipped)
- Sprint goal achieved: Yes / No / Partial
- Carry-forwards: [N] stories → [disposition: split / de-scope / carry]
```

---

## Output Format — Initiative Post-Mortem

```markdown
# Post-Mortem — [Initiative Name] — [Date]

**Participants:** [Names]  **PM author:** [name]  
**Initiative scope:** [Brief: what was this initiative trying to achieve?]  
**Outcome:** [What actually happened?]

---

## Timeline of Key Events
[Chronological. Facts only. No interpretation yet.]

- [Date]: [Event]
- [Date]: [Event]
- [Date]: [Event]

---

## Key Decisions and Their Basis
| Decision | Made on [date] | Information available at the time | Outcome |
|---|---|---|---|
| [Decision] | [Date] | [What we knew] | [What happened] |

---

## Assumptions That Turned Out Wrong
- [Assumption] — What we believed: [X] — What was actually true: [Y]
- [Assumption] — What we believed: [X] — What was actually true: [Y]

---

## Signals We Missed or Ignored
- [Signal] — Available on: [date] — Why not acted on: [reason]

---

## What We'd Do Differently
[Specific decisions or processes that would change — not "we'd communicate more"]

---

## Systemic Learnings
[What does this tell us about how we work, how we make decisions, or what assumptions we carry? These belong in process or knowledge, not just in this document.]

---

## Action Items
| Action | Owner | Due |
|---|---|---|
| [Specific change to process or knowledge] | [Name] | [Date] |
```

---

## Quality Gate

**Sprint retro:**
- "What was hard" includes at least one root cause (not just description)
- Action items have specific mechanics (not principles like "better communication")
- Action items have named owners and a way to verify success

**Post-mortem:**
- Decisions section separates decision from information available at the time (no hindsight bias)
- Assumptions that were wrong are named explicitly
- Systemic learnings are distinguished from individual blame
- Action items update a process or knowledge artifact (not just "do better next time")

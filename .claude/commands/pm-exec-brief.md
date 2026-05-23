---
name: pm-exec-brief
description: Draft an executive brief using Situation-Complication-Resolution structure. Produces async doc, verbal opening, or escalation brief depending on purpose.
version: "1.0"
changed: 2026-05-20
---

# PM Executive Brief

**Input:** Situation context, purpose, audience, and medium provided inline.

**Output:** Displayed in terminal. If async format, optionally appends to `notes/raw/YYYY-MM-DD-HHmm-exec-brief.md` for editing before sending.

---

## Steps

1. **Read context.** Load `knowledge/pm/org-dynamics.md` (executive communication section). If this is an escalation, also load `decision-frameworks/pm/escalation-framework.md`.

2. **Identify purpose:** Update / Escalation / Decision request / Go/no-go / Risk flag. Each has different output requirements.

3. **Structure using Situation-Complication-Resolution:**
   - Situation: current state + what's at stake. Facts only. No editorializing.
   - Complication: the tension, trade-off, constraint, or risk requiring executive attention. Do not soften.
   - Resolution: options + recommendation (decisions), status + next step (updates), explicit ask (escalations).

4. **Apply format rules by medium:**
   - Async (doc/email): subject line contains topic + action needed. 200 words max.
   - Verbal (meeting): three sentences. Situation. Complication. What you need.
   - Escalation: use the full brief structure with explicit ask and deadline.

5. **Check quality gates before output:**
   - First sentence contains the most important information (not background)
   - Complication is named precisely — not softened
   - Ask is specific and time-bound
   - Trade-offs are honest (not one real option + one straw man)

6. **Produce output.**

---

## Output Format

**Async:**
```
SUBJECT: [Topic — action needed]

[Situation: 2-3 sentences. Current state. What's at stake.]

[Complication: 2-3 sentences. The tension. Why this needs attention now.]

[Resolution: Options with trade-offs (decision) OR status + next step (update) OR explicit ask (escalation).]

ASK: [Specific decision or action needed, by specific date — if applicable]
```

**Verbal (meeting opening):**
```
"Here's where we are: [situation in one sentence].
The challenge is [complication in one sentence].
I need [specific ask in one sentence]."
```

**Escalation brief:**
```
SITUATION:
[One paragraph. Current state. What's at stake. Why now.]

WHAT I'VE TRIED:
- [Action taken and why it didn't resolve it]
- [Action taken and why it didn't resolve it]

OPTIONS:
A. [What we do, what we gain, what we give up]
B. [What we do, what we gain, what we give up]

MY RECOMMENDATION: [One option. Two-sentence rationale.]

WHAT I NEED FROM YOU: [Specific decision or unblocking action. Named. By [date].]
```

---

## Quality Gate

- First sentence is the most important sentence (not background)
- Complication is precise — no softening language
- Every escalation has an explicit ask with a date
- Options presented honestly — no straw man alternatives
- Length fits stated medium constraint (200 words async, 3 sentences verbal)

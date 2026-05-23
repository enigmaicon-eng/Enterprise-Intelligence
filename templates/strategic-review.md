---
title: Strategic Review — [YYYY-MM or YYYY-QN]
period: monthly | quarterly
date: YYYY-MM-DD
facilitator: [name]
bets_reviewed: [BET-YYYY-NNN, ...]
verdicts: [N continue, N adjust, N double-down, N kill]
---

## Period in One Sentence
The most important truth about this period, stated as a claim not a description.

---

## Bet Portfolio Review

*For each active bet: read the kill condition first, then look at evidence.*

### BET-YYYY-NNN — [Bet Name] | [H1/H2/H3]

**Kill condition**: [from the bet file — state it before reviewing evidence]
**Kill condition triggered?**: Yes / No

**Evidence this period:**
- Confirming: [specific observations]
- Disconfirming: [specific observations — write "none observed" if genuinely none, but ask: why not?]

**Signal quality**: Is the evidence I'm seeing actually measuring what the thesis claims?

**Verdict**: [ ] Continue  [ ] Adjust  [ ] Double down  [ ] Kill

**Rationale**: One sentence.

**If Adjust**: What specifically changes about the thesis, investment, or horizon?
**If Kill**: → Schedule postmortem within 7 days. Note: `strategy/postmortems/[bet-id].md`

---

*(Repeat block for each active bet)*

---

## OKR Progress

*For each active objective:*

### Objective: [Title]
**Linked bet**: BET-YYYY-NNN

| Key Result | Target | Current | Signal Quality |
|-----------|--------|---------|---------------|
| [KR 1] | [X] | [Y] | Reliable / Noisy / Lagging |
| [KR 2] | [X] | [Y] | Reliable / Noisy / Lagging |
| [KR 3] | [X] | [Y] | Reliable / Noisy / Lagging |

**Signal quality flag**: [If any KR has a noisy or lagging signal, state what better metric would look like]

**Recommendation**: On track | Needs adjustment | Objective should be retired

---

## Horizon Scan

### H1 (0-90 days) — Execution Zone
What must happen in the next 90 days to stay on strategy? Any H1 bet at risk of missing its window?

### H2 (90 days – 12 months) — Build Zone
What is changing in the environment that affects H2 bets?
- Threats: [specific, not generic]
- Opportunities: [emerging windows that didn't exist last review]

Any H2 bet ready to activate (move to H1)?

### H3 (12+ months) — Options Zone
What long-horizon signals are moving? Are we holding the right options?

Any new H3 bet worth opening? Any H3 bet whose option value has collapsed (should be closed)?

---

## Cross-Domain Connections
What non-obvious pattern connects things from different parts of this period? Strategy ↔ execution ↔ knowledge ↔ market.

---

## What I Was Wrong About
*(This section is mandatory. If nothing was wrong, the review is incomplete.)*

**Prediction from last review**: [what was expected]
**What actually happened**: [what occurred]
**Update to my model**: [what this changes about how I think]

---

## Updated 90-Day Priorities
Reordered from last review. Call out any item that moved significantly with the reason.

1. [Priority] — [why it's #1]
2. ...
3. ...

---

## One Question to Sit With
The most important unresolved strategic question heading into the next period. Not a to-do — a question that needs genuine thinking.

---

## Decisions Made in This Review

| Decision | Rationale | Review Date |
|----------|-----------|------------|
| [Bet X: Kill] | [one sentence] | — |
| [OKR Y: Retire] | [one sentence] | — |

→ Log decisions via `/decide` to create traceable records in `decision-frameworks/decisions-log.md`

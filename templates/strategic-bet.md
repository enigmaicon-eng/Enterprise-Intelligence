---
title: Strategic Bet — [Bet Name]
bet_id: BET-YYYY-NNN
horizon: H1 | H2 | H3
status: forming | active | paused | won | cut
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
close_by: YYYY-MM-DD
owner: [name]
tags: [tag1, tag2]
connections: [related-bet-id, related-decision-id]
---

## Thesis
One paragraph. Why is this bet worth making? What belief about how the world works — about your users, your market, your capabilities, your competitors — makes this bet rational? Write it as a falsifiable claim, not a hope.

The thesis must be written at bet creation. Do not rewrite it retroactively to match outcomes.

## Investment
What is being committed to this bet? Be specific.
- **Time**: [hours/week or % of capacity]
- **Attention**: [what competing priorities this displaces]
- **Opportunity cost**: [what you're NOT doing because of this bet]

## Horizon Classification
**Horizon**: H1 (0-90 days: execute) | H2 (90d-12mo: build) | H3 (12mo+: hold option)

**Activation criteria** (H2/H3 only): What conditions must be true before this bet moves to active execution?

## Success Signal
What evidence would tell you this bet is paying off? Be specific enough that you could recognize it.

Primary signal: [the most important indicator]
Secondary signals:
- [signal 2]
- [signal 3]

## Kill Condition
What evidence would tell you to cut this bet? Be specific — a kill condition of "if results are disappointing" is not a kill condition.

**Kill if**: [specific observable condition]
**Kill by**: [date — the latest this bet can remain active without a clear winning signal]

If the kill condition is triggered, the verdict at the next review is Kill, not "reassess."

## Assumptions
What must be true for this bet to pay off? Each assumption is a potential kill condition trigger.

1. We assume [X]...
2. We assume [Y]...
3. We assume [Z]...

---

## Evidence Log
*(Running log — append each review cycle. Never delete entries — even disconfirming ones.)*

### YYYY-MM-DD
**Confirming**: [evidence that supports the thesis]
**Disconfirming**: [evidence that challenges the thesis — if none, write "none observed" not blank]
**Verdict**: Continue | Adjust | Double down | Kill
**Rationale**: One sentence.

---

## Closure Record
*(Filled when bet closes — won or cut)*

**Outcome**: Won | Cut
**Close date**: YYYY-MM-DD
**What happened**: What actually occurred vs. what the thesis predicted.
**Kill condition triggered?**: Yes / No — if No and bet was cut anyway, explain why.
**Primary learning**: The single most useful thing to carry forward.

→ Postmortem: `strategy/postmortems/[bet-id].md`
→ Pattern extracted: `knowledge/decisions/decision-patterns.md` entry: [pattern name]

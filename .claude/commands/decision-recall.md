---
name: decision-recall
description: >-
  Retrieval-enhanced deciding: surfaces relevant past decisions and applicable
  judgment rules before making a new one. Reads decisions-log.md and
  decision-patterns.md, scores for relevance, and presents a concise briefing.
  Trigger on: "what did I decide before about X", "have I faced this before",
  "recall past decisions on Y", "decision recall [context]", "what patterns apply
  to this decision". Do NOT use for full pre-decision analysis (use /pre-decide)
  or for reviewing decision quality (use /decision-review).
version: 1.0
output: terminal
---

# /decision-recall

Surface relevant past decisions and judgment rules before deciding. Like `/trace-recall` for decisions — prevents re-making decisions already made, and brings pattern library evidence to bear before the choice is logged.

## When to Use

- Before making any significant decision, as the first pre-decision step
- When a decision feels familiar but you can't recall the prior context
- When you want to know: "what does my judgment rule library say about this?"

**Do NOT use for:**
- Full structured pre-decision analysis → `/pre-decide`
- Reviewing decision quality retrospectively → `/decision-review`
- Searching all decisions by keyword → read decisions-log.md directly

## Inputs Required

- Decision context: a natural language description of the upcoming decision

## Workflow

**Step 1 — Read the decision history.**

Read `decision-frameworks/decisions-log.md`. Parse all decision entries.

**Step 2 — Score for relevance.**

For each logged decision, score relevance to the operator's description:
- Domain/topic overlap (keywords in the decision field match the context)
- Decision type match (strategic/commitment/technical/etc.)
- Outcome visibility (prefer decisions where outcome is known, not "pending")
- Recency (recent decisions score slightly higher, all else equal)

Select the top 1-3 most relevant past decisions. If no decisions score as clearly relevant, say so.

**Step 3 — Load the pattern library.**

Read `knowledge/decisions/decision-patterns.md` (if it exists). Identify any judgment rules whose "when [conditions]" clause matches the current decision context. Select up to 3 applicable rules.

**Step 4 — Surface the briefing.**

```
Decision Recall — [context, one sentence]
══════════════════════════════════════════

Relevant Past Decisions ([N] found)

1. "[decision]"  —  [date]  —  reversibility: [level]
   Chosen    : [what was chosen]
   Rationale : [key rationale from the log entry]
   Outcome   : [outcome field — or "pending"]
   Lesson    : [what to carry forward — inferred from rationale + outcome]

2. "[decision]"  ...

Applicable Judgment Rules
  • [Rule, as stated in decision-patterns.md]
    Applies because: [one sentence on why this rule is relevant here]
  • [Rule]
    Applies because: [one sentence]
  [— or "No patterns codified yet for this domain."]

[If no relevant past decisions:]
No similar past decisions found. This may be novel territory.
Consider running /pre-decide before logging with /decide.
```

**Step 5 — Offer next steps.**

```
Next steps:
  /pre-decide [context]  — full option analysis, bias check, pre-mortem
  /decide                — log when ready
```

## Quality Gate

- [ ] decisions-log.md read before any scoring is done
- [ ] decision-patterns.md checked — absence noted if file does not yet exist
- [ ] Relevance scoring based on domain/type/outcome, not just recency
- [ ] "Lesson" is inferred from both the rationale AND the outcome — not just restating the rationale
- [ ] If no relevant past decisions: says so clearly — does not invent relevance
- [ ] At most 3 past decisions shown — not a full log dump

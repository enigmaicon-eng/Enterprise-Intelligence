---
name: pre-decide
description: >-
  Structured pre-decision analysis: generates the option set, checks applicable
  cognitive biases, surfaces relevant past decisions and judgment rules, and runs
  a pre-mortem. Feeds directly into /decide. Trigger on: "help me decide",
  "pre-decision analysis", "think through this decision", "what are my options for",
  "pre-decide [context]". Do NOT use for claim stress-testing (use /think), for
  strategic bets (use /bet), or for trivial reversible choices — run /decide directly.
version: 1.0
output: terminal
---

# /pre-decide

Structured pre-flight before a significant decision. Generates options, surfaces biases, checks the pattern library, and runs a pre-mortem — so when you log with `/decide`, the reasoning is already solid.

## When to Use

- Before logging any decision that is irreversible or low-reversibility
- Before a decision with 3+ real options (otherwise it's probably not a decision)
- When you notice yourself defaulting to one option without examining alternatives

**Do NOT use for:**
- Stress-testing a single claim → `/think`
- Strategic bets (separate lifecycle) → `/bet`
- Trivial reversible choices → go straight to `/decide`
- Looking up what you've decided before → `/decision-recall`

## Inputs Required

- Decision context (inline): what choice is being faced and why it matters now

## Workflow

**Step 1 — Parse the decision.**

Identify: what is the core choice? Strip it to one sentence. If multiple decisions are entangled, name the most load-bearing one.

**Step 2 — Classify the decision type.**

Identify the type:
- **Strategic** — direction, market entry, defining a bet
- **Commitment** — build vs. buy, hire, invest, partner
- **Technical/Architecture** — technology choice, design pattern, approach
- **Resource allocation** — budget, time, headcount
- **Timing** — when to launch, when to pivot, when to stop
- **People** — hiring, promotion, restructure
- **Comparative** — vendor selection, tool choice, framework

Assess reversibility: high (easy to undo) / medium / low / irreversible.

**Step 3 — Generate the option set.**

Generate at minimum 3 options. Always include:
- The "obvious" option (what the operator seems to be leaning toward)
- A meaningfully different alternative
- "Do nothing / defer" as a named option

For each option: one-sentence description + the key trade-off (what you gain, what you give up).

**Step 4 — Apply the bias check.**

Select 2-3 biases most applicable to this decision type:

| Decision Type | Watch For |
|--------------|-----------|
| Strategic | Confirmation bias (seeking confirming info only), status quo bias (preferring inaction), sunk cost fallacy |
| Commitment | Sunk cost fallacy (past investment warping the decision), IKEA effect (overvaluing what you built), planning fallacy (underestimating cost/time) |
| Technical | Not-invented-here syndrome (rejecting external solutions), complexity bias (preferring elaborate solutions), recency bias (overweighting recent incidents) |
| Resource | Planning fallacy, anchoring (first estimate dominates), scope creep blindness |
| Timing | FOMO (acting before conditions are right), analysis paralysis (refusing to act), optimism bias |
| People | Halo effect (one trait colors all assessment), affinity bias (favoring similar profiles), attribution error |
| Comparative | Feature comparison trap (features over fit), sunk cost in current option, analysis paralysis |

For each selected bias: name it and state specifically how it might be distorting this decision.

**Step 5 — Check the decision history and pattern library.**

Read `decision-frameworks/decisions-log.md`. Scan for entries with similar decision type, domain, or keywords. Surface the 1-2 most relevant past decisions (goal, choice made, outcome).

Read `knowledge/decisions/decision-patterns.md` (if it exists). Surface any judgment rules that apply to this decision type or domain.

**Step 6 — Run a pre-mortem.**

Ask: assume this decision was made today and it went badly 6 months from now. What is the most plausible failure scenario? Work backwards:
- What specifically went wrong
- What the root cause was
- What early signal would have been visible within 30 days

Keep this to 3 lines. The goal is one specific plausible failure, not an exhaustive list.

**Step 7 — Surface the pre-decision brief.**

```
Pre-Decision Analysis — [decision, one sentence]
══════════════════════════════════════════════════

Type         : [type]
Reversibility: [high | medium | low | irreversible]

Options
  A. [option]
     Trade-off: [gain X, give up Y]
  B. [option]
     Trade-off: [gain X, give up Y]
  C. Do nothing / defer
     Trade-off: [what this preserves, what it risks]
  [D. if a fourth is genuinely distinct]

Bias Check
  ⚠ [Bias]: [how it might apply here — specific to this decision, not generic]
  ⚠ [Bias]: [how it might apply here]
  [⚠ third if warranted]

Past Decisions
  [Decision title] ([date]) — chosen: [X], outcome: [Y]
  [— or "No similar decisions found in history."]

Applicable Patterns
  • [Judgment rule from decision-patterns.md]
  [— or "No patterns codified for this type yet."]

Pre-Mortem
  Failure: [what went wrong]
  Root cause: [why]
  Early signal: [what you'd see within 30 days]

[If one option is clearly indicated by past decisions or patterns:]
Indicated direction: [option + reason]
[If genuinely ambiguous:]
Key uncertainty: [the one thing you'd need to know to decide with confidence]
```

**Step 8 — Offer next steps.**

```
Next steps:
  /consequence-map [option A or B]  — map downstream effects before committing
  /decision-recall [context]        — load more past decisions on this topic
  /decide                           — log when ready
```

## Quality Gate

- [ ] Decision parsed to one sentence before analysis begins
- [ ] At minimum 3 options generated — "do nothing" always included
- [ ] Bias check is specific to this decision — not generic platitudes
- [ ] Past decisions loaded from decisions-log.md before the brief is written
- [ ] Pre-mortem identifies one specific plausible failure, not a generic list
- [ ] "Indicated direction" only stated when pattern evidence actually supports it
- [ ] `/decide` offered as next step — this skill does not log the decision itself

# Decision Intelligence System

Structured support for the full decision lifecycle — from pre-decision analysis through pattern extraction. Four skills that make decisions better before they're made and more useful after they're reviewed.

## What This Is

Conversational decision support for ONE operator. Skills that read decision history and pattern libraries to surface relevant context, generate options, check biases, and map consequences — all before the decision is logged. And one skill that keeps the review queue from silently filling up.

## What This Is NOT

- Automated decision engines
- Enterprise decision governance
- Approval workflow systems
- ML-based recommendation systems

## Decision Lifecycle

```
Pre-decision                At-decision          Post-decision
─────────────────────────   ──────────────────   ──────────────────────────
/decision-recall            /decide              /decision-due  (surfaces due reviews)
/pre-decide                 ↓                    /decision-review  (quality retrospective)
/consequence-map            decisions-log.md     ↓
                                                 decision-patterns.md  (judgment rules)
```

## Skill Map by Lifecycle Stage

| Stage | Skill | What It Does |
|-------|-------|-------------|
| Pre-decision | `/decision-recall` | Surfaces relevant past decisions and judgment rules |
| Pre-decision | `/pre-decide` | Options, bias check, pre-mortem, applicable patterns |
| Pre-decision | `/consequence-map` | First and second-order effects of each option |
| At-decision | `/decide` | Logs the decision (existing) |
| Post-decision | `/decision-due` | Surfaces decisions approaching review date |
| Post-decision | `/decision-review` | 5-check quality retrospective, extracts judgment rules (existing) |

## Existing Skills (Do Not Duplicate)

| Existing Skill | What It Covers |
|----------------|---------------|
| `/decide` | Logs a decision with options, rationale, assumptions, reversibility, review_date |
| `/decision-review` | 5-check retrospective; extracts judgment rules; updates decision-patterns.md |
| `/think` | Adversarial stress-test of a single claim (empirical/causal/normative/predictive) |
| `/bet` | Strategic bet lifecycle (open/update/close/postmortem) |
| `/exec-checkpoint` | Continue/pivot/stop checkpoint for active execution |
| `/exec-prioritize` | Work prioritization by commitment, leverage, reversibility |

## New Skills (P23)

| Skill | Fills Gap |
|-------|----------|
| `/pre-decide` | Option generation + bias check + pre-mortem before logging |
| `/decision-recall` | Relevant past decisions + judgment rules surfaced before deciding |
| `/decision-due` | Review queue management — overdue and upcoming reviews surfaced |
| `/consequence-map` | First/second-order consequence mapping before committing |

## Decision Type Taxonomy

Used by `/pre-decide` to select applicable bias checks and framing:

| Type | Examples |
|------|---------|
| Strategic | Direction change, entering a market, defining a bet |
| Commitment | Build vs. buy, hire, invest, partner |
| Technical/Architecture | Technology choice, design pattern, API design |
| Resource allocation | Budget, time, headcount |
| Timing | When to launch, when to pivot, when to stop |
| People | Hiring, promotion, team restructure |
| Comparative | Vendor selection, tool choice, framework |

## Cognitive Bias Registry (Built Into /pre-decide)

Applied by decision type — 2-3 most applicable biases per type:

| Decision Type | Primary Biases |
|--------------|---------------|
| Strategic | Confirmation bias, status quo bias, sunk cost fallacy |
| Commitment | Sunk cost fallacy, IKEA effect, planning fallacy |
| Technical | Not-invented-here syndrome, complexity bias, recency bias |
| Resource | Planning fallacy, anchoring, scope creep blindness |
| Timing | FOMO (acting too fast), analysis paralysis, optimism bias |
| People | Halo effect, affinity bias, attribution error |
| Comparative | Feature comparison trap, sunk cost in current option, analysis paralysis |

## Data Sources

```
decision-frameworks/
  decisions-log.md          ← primary decision record (read by all 4 new skills)

knowledge/decisions/
  decision-patterns.md      ← judgment rules library (read by /pre-decide + /decision-recall)
```

## Pre-Decision Workflow (Recommended Sequence)

For any significant decision (irreversible or high-stakes):

1. `/decision-recall [context]` — have I faced this before? What patterns apply?
2. `/pre-decide [context]` — generate options, check biases, run pre-mortem
3. `/consequence-map [options]` — map the downstream effects of top options
4. `/decide` — log with full rationale

For lower-stakes reversible decisions: skip to `/decide` directly.

## Anti-Patterns

| Anti-pattern | Why it fails |
|-------------|-------------|
| Running `/pre-decide` on trivial reversible decisions | Decision overhead should match decision stakes |
| Using `/consequence-map` instead of acting | Analysis paralysis — consequence maps inform, they don't decide |
| Treating `/decision-recall` output as a prescription | Past patterns are evidence, not rules; context always differs |
| Skipping `/decision-due` for months | Review debt compounds; decisions made without outcome data can't generate judgment rules |
| Running `/think` as a substitute for option generation | `/think` stress-tests; it does not generate — they are different operations |

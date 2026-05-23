# Prompt: Horizon Scan

You are conducting a structured horizon scan across H1/H2/H3 time zones. Your job is to surface specific, actionable signals — not generic trends.

## Rules

**Specificity discipline**: Generic observations ("AI is advancing rapidly," "competition is increasing") are not signals — they're background noise. Every observation must name a specific event, company, user behavior, or data point. Generic observations are flagged and returned for specification.

**Disconfirmation discipline**: For each H2/H3 bet, ask: "What would tell me this bet's window has closed or its thesis has been invalidated?" The scan must surface threats, not just opportunities.

**H3 mandatory check**: At least one H3 bet must exist. If the portfolio is all H1/H2, flag the absence of an options position as a finding — it's a strategic risk.

---

## Output Structure

### H1 Scan (0-90 days)
- Windows closing: [specific execution windows with dates]
- H1 bets at risk: [named bets, named risk signals]
- H1 bets ready to resolve: [named bets approaching kill-or-win threshold]

### H2 Scan (90d-12mo)
For each category (market, technology, regulatory, user behavior, organizational):
- What changed: [specific, observable]
- Direction of change: [favorable / unfavorable / ambiguous]
- Bet affected: [BET-ID or "new bet candidate"]

H2 bets ready to activate (activation criteria met):
- [Bet | criteria status | recommended action]

New H2 signals worth a thesis:
- [Signal | tentative thesis | what would confirm it]

### H3 Scan (12+ months)
Long-horizon signals:
- [Signal | direction | option action: open / strengthen / close]

H3 option inventory health:
- [Each H3 bet | option value: increasing / stable / collapsing]

### Threat Map
| Threat | Horizon | Specificity | Action |
|--------|---------|------------|--------|
| [H1 act now] | H1 | [specific] | [action] |
| [H2 prepare] | H2 | [specific] | [preparation] |
| [H3 watch] | H3 | [specific] | [watch signal] |

### Opportunity Map
| Opportunity | Window opens | Window closes | Bet |
|-------------|-------------|---------------|-----|
| | | | |

### Portfolio Adjustments Recommended
| Action | Bet | Rationale |
|--------|-----|-----------|
| Open | [name + horizon] | [one sentence] |
| Activate | [BET-ID] | [activation trigger met] |
| Adjust | [BET-ID] | [what changes] |
| Close | [BET-ID] | [why option value collapsed] |

---

## Input

**Current bet portfolio**: {{BET_PORTFOLIO}}
**Recent environmental observations**: {{OBSERVATIONS}}
**Last scan output**: {{PREVIOUS_SCAN}}

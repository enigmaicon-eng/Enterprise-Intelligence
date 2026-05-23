# Strategic Operating System
## How This Workspace Reasons About Strategy

---

## The Strategic Stack

```
Annual Themes (knowledge/strategy/annual-themes.md)
    — the 3 strategic priorities shaping the year
        │
        ▼
Bet Portfolio (strategy/active-bets.md + strategy/bets/)
    — explicit commitments with theses and kill conditions
    — H1 bets → OKRs → execution
    — H2 bets → horizon monitoring
    — H3 bets → option holding
        │
        ▼
OKRs (strategy/OKRs.md)
    — tactical expression of H1 bets
    — 3 objectives max, 3 KRs per objective
    — each KR traces to a bet
        │
        ▼
Monthly Strategy Review (strategy/reviews/)
    — bet verdicts: Continue | Adjust | Double down | Kill
    — OKR signal quality check
    — horizon scan (abbreviated)
    — what I was wrong about
        │
        ▼
Bet Lifecycle (strategy/bets/ + strategy/postmortems/)
    — bets open, accumulate evidence, close
    — postmortems extract decision patterns
    — patterns compound into knowledge/decisions/
```

---

## Directory Map

```
strategy/
├── STRATEGY-OS.md              ← This file
├── active-bets.md              ← Live portfolio register
├── OKRs.md                     ← Current objectives and key results
├── bet-log.md                  ← Historical bet outcomes (one-row summaries)
├── bets/                       ← Full bet files (templates/strategic-bet.md)
│   └── BET-YYYY-NNN.md
├── postmortems/                ← Closed bet postmortems (templates/bet-postmortem.md)
│   └── BET-YYYY-NNN.md
├── reviews/                    ← Periodic strategy reviews
│   ├── YYYY-MM.md              ← Monthly
│   └── YYYY-QN.md              ← Quarterly
└── horizons/                   ← Horizon scan outputs
    └── YYYY-QN.md
```

---

## Skill Map

| Intent | Skill |
|--------|-------|
| Open, update, or close a bet | `/bet` |
| Run monthly/quarterly strategy review | `/strategy-review` |
| Articulate or stress-test strategic posture | `/strategy-posture` |
| Scan H1/H2/H3 horizons | `/horizon` |
| Set annual strategic themes | `/strategy-posture annual` |
| Log a strategic decision | `/decide` |
| Deep cross-domain synthesis | `/synthesize` |

---

## Review Cadence

| Review | Cadence | Skill | Output |
|--------|---------|-------|--------|
| Bet evidence update | Per observation | `/bet update` | Updated bet file |
| Monthly strategy review | Month end | `/strategy-review` | `strategy/reviews/YYYY-MM.md` |
| Quarterly horizon scan | Quarter end | `/horizon` | `strategy/horizons/YYYY-QN.md` |
| Quarterly strategy review | Quarter end | `/strategy-review quarterly` | `strategy/reviews/YYYY-QN.md` |
| Annual theme setting | Year start | `/strategy-posture annual` | `knowledge/strategy/annual-themes.md` |
| Bet postmortem | On bet close | `/bet postmortem` | `strategy/postmortems/BET-ID.md` |

---

## Bet Portfolio Rules

1. **3-5 active bets maximum.** More dilutes attention; fewer concentrates risk dangerously.
2. **At least one H3 bet at all times.** An all-H1 portfolio is executing without an options position.
3. **Every bet has a kill condition.** Non-negotiable. Bets without kill conditions are zombie commitments.
4. **Kill conditions are read before evidence at every review.** This prevents confirmation bias from overriding the original stopping rule.
5. **Every killed bet gets a postmortem within 7 days.** Not a celebration, not a blame session — a structured learning extraction.

---

## Decision Traceability

Strategic decisions link three things:
- The **bet** they serve
- The **assumption** they depend on
- The **review date** when that assumption will be checked

This makes strategy auditable. "We decided X" has no compounding value. "We decided X because we believed Y, and we'll check Y at Z" creates a learning loop.

All significant strategic decisions are logged via `/decide` in `decision-frameworks/decisions-log.md`.

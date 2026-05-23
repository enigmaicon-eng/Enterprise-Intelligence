# Strategic Intelligence System
## Bet-Driven Strategy, Horizon Thinking, Decision Compounding

---

## Design Philosophy

Strategy compounds through **bet learning**, not through planning artifacts. Three things make strategy genuinely intelligent:

1. **Bet explicitness**: Every strategic commitment has a thesis, a time horizon, and a kill condition. Without kill conditions, bets never close — they become zombie commitments that consume attention indefinitely.
2. **Signal discipline**: The system tracks confirming AND disconfirming evidence. Confirmation bias is the primary strategic failure mode. A review that only finds supporting evidence isn't a review.
3. **Decision traceability**: Strategic patterns emerge from reviewing closed bets, not from making new ones. The pipeline `bet → bet-postmortem → decision-patterns` is the compounding mechanism.

Three anti-patterns this system is designed against:

1. **Vision theater**: Beautiful long-term narratives that never get falsified because success criteria are undefined.
2. **OKR washing**: Key results that measure activity ("completed 3 interviews") rather than outcomes ("retention improved by X%").
3. **Strategic drift**: Priorities that shift without a documented decision, so the organization is executing against an unstated strategy that differs from the stated one.

---

## System Map

```
Strategic Posture (annual themes, positioning)
        │
        ▼
Bet Portfolio (active-bets.md)
  ├── H1 bets → OKRs → execution tasks (execution OS)
  ├── H2 bets → horizon-scan monitoring
  └── H3 bets → option holding (watch, don't act)
        │
        ▼
Monthly Strategy Review (/strategy-review)
  ├── Bet portfolio: Continue | Adjust | Double down | Kill
  ├── OKR progress: signal quality check
  ├── Horizon scan: threats and opportunities
  └── "What I Was Wrong About" — mandatory
        │
        ▼
Bet Closure (/bet close)
  └── Bet postmortem → decision-patterns.md (knowledge)
        │
        ▼
Decision Patterns (compounding)
  └── knowledge/decisions/decision-patterns.md
```

---

## The Bet Protocol

A bet is the atomic unit of strategy — not a goal, not a theme, not a project. Goals describe desired states. Bets express a commitment of resources under uncertainty toward a thesis.

**A valid bet has six components:**

| Component | What It Is | Why Required |
|---|---|---|
| **Thesis** | Why this bet is worth making — the belief about how the world works | Without a thesis, you can't evaluate evidence |
| **Horizon** | H1 / H2 / H3 time classification | Determines review cadence and activation criteria |
| **Investment** | What is being committed (time, attention, capital, opportunity cost) | Bets without named costs are wishes |
| **Success signal** | What evidence would tell you the bet is paying off | Without this, you're always "on track" |
| **Kill condition** | What evidence would tell you to cut the bet | Without this, bets never close |
| **Evidence log** | Running record of confirming and disconfirming observations | The audit trail that makes reviews real |

**Kill conditions must be specific**: "if results are disappointing" is not a kill condition. "If [metric X] doesn't reach [threshold Y] by [date Z]" is.

---

## The Three-Horizon Model

Horizons structure time. Each horizon has different review cadence, different action posture, and different type of intelligence needed.

| Horizon | Timeframe | Posture | Review Cadence | Action |
|---------|----------|---------|----------------|--------|
| **H1** | 0–90 days | Execute | Weekly (via exec-review) | Do the work |
| **H2** | 90 days – 12 months | Build | Monthly (via strategy-review) | Develop capabilities |
| **H3** | 12+ months | Hold option | Quarterly | Watch, don't act yet |

**Horizon transitions**: A bet moves from H3 → H2 when: the option value increases enough to justify building. From H2 → H1 when: capabilities are ready and the window to execute is open. These transitions require a checkpoint, not just a calendar date.

**The H3 trap**: Most organizations have no H3 discipline — all thinking is H1. H3 bets aren't plans; they're **option positions**: small investments that preserve the right to act if conditions change. The cost is attention, not execution.

---

## OKR Design Protocol

OKRs are the tactical expression of H1 bets — not separate from strategy, but derived from it.

**Structure:**
- 3 Objectives maximum (focus beats coverage)
- 3 Key Results per Objective maximum
- Each KR has a signal quality check: *is this metric telling us what we think it's telling us?*

**Valid Key Results:**
- Measurable at the end of the period without interpretation
- Outcome-based, not activity-based ("X users activate feature" not "we shipped feature")
- Owned by one person (the one who can actually move the metric)

**OKR-to-Bet mapping**: Every Objective should trace to an H1 bet. If an Objective doesn't trace to a bet, either add the bet or cut the Objective — phantom objectives (work that exists but isn't a strategic bet) are a sign of strategic drift.

---

## Strategic Review Protocol

Monthly reviews answer: **are our bets still right?**

That question breaks into four sub-questions:

1. **Bet signals**: What evidence arrived? Is it confirming or disconfirming?
2. **OKR signal quality**: Are our key results measuring what we think they're measuring?
3. **Horizon shifts**: What changed in H2 or H3 that affects H1?
4. **What were we wrong about?** — mandatory. If nothing was wrong, the review is incomplete.

Review output is always one of four verdicts per bet: **Continue | Adjust | Double down | Kill**

"Keep an eye on it" is not a verdict. "Monitor and reassess" is not a verdict. A review that produces no verdicts was a discussion, not a review.

---

## Decision Traceability Protocol

Every strategic decision links to:
1. The bet it serves (or the bet it creates)
2. The assumption it depends on (named, so it can be falsified)
3. A review date (when to check if the assumption held)

Closed bets generate bet postmortems. Postmortems extract decision patterns. Decision patterns are the compounding intelligence — they make the next bet better than the last one.

**The compounding loop:**
```
Make bet (explicit thesis + kill condition)
    → Gather evidence (confirming and disconfirming)
    → Monthly review (verdict: continue/adjust/double-down/kill)
    → Bet closes (won or cut)
    → Postmortem (what did we learn?)
    → Decision pattern (add to knowledge/decisions/)
    → Next bet is informed by the pattern
```

Without postmortems, you make the same strategic mistakes twice. Without decision patterns extracted from postmortems, the learning stays local to the person who ran the bet.

---

## Prioritization in Strategic Context

Strategic prioritization is different from operational prioritization (`/exec-prioritize`):

| Operational | Strategic |
|-------------|----------|
| What do I do today? | What do I commit to for the next 90 days? |
| Commitment → leverage → reversibility | Conviction × asymmetry × optionality |
| 7-item ranked list | 3-5 bet portfolio |
| Changes weekly | Changes monthly at most |

**Strategic prioritization criteria:**
1. **Conviction**: How strong is the thesis? What would need to be true for this bet to pay off — and how likely is that?
2. **Asymmetry**: What's the upside if the bet works vs. the downside if it fails? Good bets have bounded downside and open upside.
3. **Optionality**: Does making this bet expand or contract future options? Bets that open future options are worth more than bets that close them.

---

## Anti-Pattern Catalog (Strategy-Specific)

| Anti-Pattern | Symptom | Fix |
|---|---|---|
| Kill condition amnesia | Bets that are always "active" regardless of evidence | Every bet review requires reading the kill condition first |
| Retrospective thesis | The thesis is written to justify what was done, not what was believed | Thesis must be written at bet creation, not at review |
| Symmetric risk blindness | Only success signals are tracked | Every bet log must have a disconfirming evidence section |
| OKR activity inflation | Key results that measure output, not outcome | Each KR gets a signal quality check: "does this metric prove the thing we care about?" |
| Horizon collapse | All thinking is H1 — no H2 or H3 | Force H3 attention: at least one H3 bet must exist at all times |
| Strategy/execution disconnect | OKRs don't trace to bets | Every objective maps to a bet, or it shouldn't exist |
| Review without verdict | Strategic reviews that produce observations but no decisions | Each bet must exit every review with an explicit verdict |

---

## Intelligence Layer (P24)

Three skills that add continuous environmental intelligence gathering between structured horizon scans. The existing strategy stack processes intelligence on a cadence (monthly/quarterly). These skills capture intelligence as it arrives.

### New Skills

| Skill | What It Does | Writes To |
|-------|-------------|-----------|
| `/signal` | Captures and reviews strategic signals between horizon scans | `strategy/signals/YYYY-MM.md` |
| `/assumption-register` | Surfaces and tracks implicit assumptions underlying each active bet | Read-only (reads bet files) |
| `/competitive-radar` | Logs competitor moves and assesses their bet-level implications | `strategy/competitive/radar.md` |

### Information Flow

```
External environment
        ↓
/signal capture          ← any time a signal arrives (threat/opportunity/noise/uncertain)
/competitive-radar log   ← any time a competitor makes a specific observable move
        ↓
/signal review           ← weekly, surfaces signals approaching review-by date
/competitive-radar review← weekly, surfaces disconfirming moves first
        ↓
/assumption-register     ← before monthly strategy-review, checks which bet assumptions are at risk
        ↓
/bet update              ← logs evidence from signals/moves against specific bets
/horizon                 ← quarterly, reads accumulated signals as input
/strategy-review         ← monthly, portfolio verdicts informed by surfaced assumptions
```

### Signal Classification

| Category | Definition | Review-by Default |
|----------|-----------|------------------|
| Threat | Could harm a bet thesis or portfolio position | 7 days (H1), 30 days (H2), 90 days (H3) |
| Opportunity | Could strengthen a bet or open a new one | 14 days (H1), 30 days (H2), 90 days (H3) |
| Noise | No strategic relevance — log to close the loop | 90 days |
| Uncertain | Strategic relevance unclear, needs more evidence | 30 days |

### Assumption Status Taxonomy

| Status | Definition |
|--------|-----------|
| Untested | No evidence in the bet's evidence log touches this assumption |
| Tested-held | Evidence log has observations on this assumption; it still holds |
| At risk | Disconfirming evidence challenges this assumption |
| Violated | The assumption has been observably falsified |

### Competitive Implication Types

| Implication | Definition |
|------------|-----------|
| Confirms | Move provides evidence the bet thesis is directionally correct |
| Disconfirms | Move provides evidence against the bet thesis |
| Neutral | Move is in the domain but doesn't affect the thesis directly |
| Uncertain | Implications for the thesis are unclear |

### Data Architecture

```
strategy/
  signals/
    YYYY-MM.md            ← monthly signal log files
  competitive/
    radar.md              ← single append-only competitive move log
  bets/
    BET-YYYY-NNN.md       ← read by /assumption-register (thesis + evidence log)
```

### Intelligence Layer Anti-Patterns

| Anti-pattern | Why it fails |
|-------------|-------------|
| Logging every news item as a signal | Noise floods the log; signals require strategic relevance, not just interest |
| Using /signal instead of /bet update | Signals feed bets — /bet update logs evidence against the thesis directly |
| Checking radar instead of running /horizon | Radar tracks discrete moves; horizon scans structural shifts — both needed |
| Running /assumption-register without the evidence log | Assumption status requires evidence; outputs are meaningless without it |
| Logging "competitor expanded" without specifics | "/competitive-radar log" requires specific observable action, not direction |

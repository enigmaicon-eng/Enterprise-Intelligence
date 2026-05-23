# /horizon — Horizon Scan

Run a structured horizon scan across H1/H2/H3 time zones. Surfaces threats, opportunities, and signals that should affect the bet portfolio.

## Trigger
`/horizon` — quarterly or on-demand full scan
`/horizon [domain]` — focused scan on a specific domain (e.g., market, technology, organization)
`/horizon brief` — abbreviated 5-minute version for monthly strategy reviews

## When to Use
- Quarterly (full scan)
- When a significant external event happens that might affect H2 or H3 bets
- When a bet's assumptions are under review and broader context is needed
- As input to a new bet formation

## Protocol

### Step 0: Load strategic context
Read in order:
1. `strategy/active-bets.md` — what bets exist and their horizons
2. `strategy/OKRs.md` — current objectives (what's in execution)
3. Most recent strategy review in `strategy/reviews/` — what threats/opportunities were noted last time?

### Step 1: H1 scan — Execution zone (0-90 days)

**Windows closing**: Are there execution windows (market timing, competitive response windows, resource availability) that close within 90 days? A closing window = either activate the bet or cut it.

**H1 bets at risk**: For each H1 bet, is there any environmental signal that threatens its execution? Name specific signals, not generic risks.

**H1 bets ready to resolve**: Any bet that should reach its kill-or-win threshold within 90 days?

### Step 2: H2 scan — Build zone (90 days–12 months)

**Environmental changes since last scan**: What has shifted in the following categories?
- Market structure: new competitors, pricing changes, consolidation, exits
- Technology: new capabilities that affect what's buildable or what users expect
- Regulatory / policy: changes that create constraints or open spaces
- User behavior: shifts in what users are doing, expecting, or tolerating
- Organizational: team changes, capability gains, resource shifts

**H2 bets ready to activate**: For each H2 bet, check its activation criteria (from the bet file). Has anything in the environment met those criteria?

**New H2 signals**: What emerging signals might warrant a new H2 bet? Name the signal, tentative thesis, and what would need to be true to form a bet.

### Step 3: H3 scan — Options zone (12+ months)

**Long-horizon signals**: What is shifting slowly at the 1-3 year horizon?
Apply the "what would I need to believe" framing: if X is happening, what would I need to believe to act on it now vs. wait?

**Option inventory health**: For each H3 bet, is the option value increasing, stable, or collapsing? Collapsing option value = either activate or close.

**Mandatory H3 check**: Does at least one H3 bet exist? If the H3 inventory is empty, the organization is executing without an options portfolio — surface this.

### Step 4: Threat map

Three-tier classification:
- **Act now** (H1 threat): materializes within 90 days, no action means damage
- **Prepare now** (H2 threat): arrives in 90d-12mo, preparation starts in H1
- **Watch** (H3 threat): real but distant, goes on the radar not the action list

For each threat: name it specifically. Generic threats ("competition could increase") are not tracked here.

### Step 5: Opportunity map

Same three-tier classification for opportunities. An opportunity without a time window is a wish — name when the window opens and when it closes.

### Step 6: Portfolio adjustments

Based on the scan, recommend specific bet actions:
- New bets to open (with initial thesis and horizon)
- Bets to activate (H2 → H1, with activation trigger met)
- Bets to adjust (thesis, investment, or kill condition changes)
- Bets to close (H3 options whose value has collapsed)

### Step 7: Write the horizon scan
Use `templates/horizon-scan.md`.
Write to: `strategy/horizons/[YYYY-QN].md`

### Step 8: Integrate with strategy review
If this scan is part of a strategy review, pass the output as context to `/strategy-review`. The horizon scan feeds the H2/H3 section of the review.

## Quality Bar
The scan fails if:
- H3 inventory is empty with no flag
- Threats are generic ("competition, regulation, technology") with no specificity
- No bet portfolio adjustments are recommended (if nothing changed, state that explicitly rather than producing an empty scan)

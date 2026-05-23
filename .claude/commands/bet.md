# /bet — Strategic Bet Lifecycle Management

Open, update, close, or review the bet portfolio. Manages the full lifecycle of a strategic bet from formation to postmortem.

## Trigger
`/bet open [bet description]` — open a new strategic bet
`/bet update [bet-id]` — add evidence to an existing bet's log
`/bet close [bet-id] [won|cut]` — close a bet and schedule postmortem
`/bet portfolio` — review the full portfolio: health, horizon distribution, evidence gaps
`/bet postmortem [bet-id]` — run a structured postmortem on a closed bet

---

## Protocol — Open a Bet

### Step 0: Load context
Read `strategy/active-bets.md`. Count active bets. If there are already 5 active bets, surface this before proceeding — adding a 6th requires retiring one or articulating why the portfolio should expand.

### Step 1: Elicit bet components
If the user description doesn't include all six components, ask (one round):
- "What's the thesis — the specific belief about how the world works that makes this bet rational?"
- "What horizon is this: H1 (execute now), H2 (build capability), or H3 (hold option)?"
- "What's the kill condition — the specific observable event that would tell you to cut this?"

Do not proceed without a kill condition. A bet without a kill condition will never close.

### Step 2: Assign bet ID
Format: `BET-YYYY-NNN` — sequential within the year.
Read `strategy/active-bets.md` to get the next available number.

### Step 3: Build the bet file
Use `templates/strategic-bet.md`.
Write to: `strategy/bets/[bet-id].md`

### Step 4: Register in active-bets.md
Read `strategy/active-bets.md`. Add entry to the Active Bets section:
```
### BET-YYYY-NNN — [Bet Name] | [H1/H2/H3]
- Thesis: [one sentence]
- Kill condition: [specific condition]
- Kill by: [date]
- Last reviewed: [today]
- Status: forming | active
```

### Step 5: Check OKR linkage
For H1 bets: does an OKR objective exist that expresses this bet tactically? If not, prompt: "This H1 bet doesn't have a corresponding OKR objective. Add one to `strategy/OKRs.md` or confirm this bet will operate without an OKR."

---

## Protocol — Update a Bet

### Step 1: Read the bet file
Read `strategy/bets/[bet-id].md`. Read the kill condition first.

### Step 2: Check kill condition
Is the new evidence triggering the kill condition? If yes, surface this immediately before logging evidence.

### Step 3: Log evidence
Append to the Evidence Log section:
```
### YYYY-MM-DD
**Confirming**: [observations]
**Disconfirming**: [observations — never blank, write "none observed" if genuinely none]
**Verdict**: Continue | Adjust | Double down | Kill
**Rationale**: One sentence.
```

---

## Protocol — Close a Bet

### Step 1: Read the bet file
Read the full bet file, especially the thesis and kill condition.

### Step 2: Log closure
Add to the Closure Record section of the bet file.

### Step 3: Update active-bets.md
Move the bet from Active to Archive. Record: outcome (won/cut), close date, primary learning.

### Step 4: Schedule postmortem
Add to `execution/action-items.md`:
```
- [ ] Bet postmortem: [BET-ID] | strategy/postmortems/ | Due: [7 days from today]
```

---

## Protocol — Portfolio Review

Load all active bets. For each, surface:
- Horizon distribution (H1/H2/H3 counts) — flag if no H3 bets exist
- Evidence recency — bets not updated in 30+ days
- Kill-by dates approaching — bets whose kill-by date is within 30 days
- Evidence gaps — bets with no disconfirming evidence ever logged

Output a portfolio health table:
```
| Bet | Horizon | Last updated | Kill-by | Evidence gaps | Health |
```

---

## Protocol — Postmortem

Use `templates/bet-postmortem.md`.
Write to: `strategy/postmortems/[bet-id].md`

The postmortem must extract at least one decision pattern.
Pattern goes to: `knowledge/decisions/decision-patterns.md`
Bet summary goes to: `knowledge/strategy/bets-history.md`

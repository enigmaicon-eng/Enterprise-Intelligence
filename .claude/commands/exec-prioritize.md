# /exec-prioritize — Operational Prioritization

Produce a ranked priority list for workspace-level work — across initiatives, tasks, and open threads. Applies the commitment → leverage → reversibility stack to cut through competing priorities.

## Trigger
`/exec-prioritize` — prioritize everything currently open
`/exec-prioritize [scope]` — prioritize within a specific initiative or domain

## Distinct from /pm-prioritize
`/pm-prioritize` scores and ranks product initiatives using RICE or similar PM frameworks.
`/exec-prioritize` ranks operational work — tasks, initiatives, follow-ups — using execution-level criteria.

## Protocol

### Step 0: Load the execution picture
Read in order:
1. `execution/action-items.md` — all open tasks
2. `execution/active-initiatives.md` — all in-flight initiatives
3. `execution/follow-ups.md` — pending async threads
4. `execution/risks.md` — triggered or imminent risks (these may generate tasks)
5. `memory/MEMORY.md` — active project context

### Step 1: Build the full inventory
Enumerate every open item. Do not filter yet. Group by type:
- **Overdue tasks** (past due date)
- **Active initiative milestones** (in-progress with target dates)
- **Pending follow-ups** (async threads waiting for response)
- **Risk mitigations** (actions from the risk register)
- **Queued work** (ready to start, not yet started)

### Step 2: Apply the three-criterion stack

Apply in this exact order — criterion 1 sorts first, criterion 2 breaks ties:

**Criterion 1 — Commitment**: Is this work committed to someone else? Explicit commitments (to a person, a deadline, a contract) rank above everything uncommitted. Order committed items by commitment date ascending.

**Criterion 2 — Leverage**: Does completing this item unblock other work or compound forward? Items that unblock 2+ other tasks or create durable artifacts rank above isolated work with the same urgency.

**Criterion 3 — Reversibility**: Is the cost of delay rising? Items where waiting another week makes the situation meaningfully worse rank above items where delay is neutral. Apply this as a tiebreaker between items that are equal on commitment and leverage.

**Tie-breaking rule**: When two items score equally on all three criteria, prioritize the shorter one (lower time cost to complete and clear the queue).

### Step 3: Produce the ranked list
Output a ranked list of the top 7 items (maximum). More than 7 is false precision — if you can't act on all 7 this week, the list is too long.

Format per item:
```
[N]. [Item description] | [type] | [Criterion that ranked it here] | [Est. effort]
```

### Step 4: Surface conflicts
Are any high-priority items blocked by each other? Name the conflict and the resolution:
- "Item 2 is blocked by Item 4 — complete Item 4 first"
- "Item 1 and Item 3 both require 4+ hours — cannot do both today"

### Step 5: Recommend the first move
Based on the ranked list: what is the single best next action to take right now? State it as a concrete first step, not a direction.

### Step 6: Write to briefing (optional)
If the user runs `/exec-prioritize` at session start, offer to incorporate the ranked list into the daily briefing output. Do not auto-write — ask.

## Quality Bar
The priority list fails if:
- It contains more than 7 items
- Any item doesn't have an effort estimate
- "Everything is a priority" would be a fair characterization of the output
- The #1 item is something the user is already doing (then the list is useless)

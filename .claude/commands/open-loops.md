---
name: open-loops
description: >-
  Scans all inbox and pending states across the workspace to surface every
  unresolved thread: raw captures, unprocessed meetings, unreviewed signals,
  pending decisions, unresolved knowledge contradictions, stalled workflows.
  Returns a complete inventory by category with staleness and routing
  recommendations. Distinct from /briefing (today's priorities from
  action-items.md) and /cognitive-load (aggregate load level). Use when you
  want to see exactly what's in flight and where each item belongs.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (open loops inventory)
---

# /open-loops — Open Loop Inventory

## When to Use

- Start of week to see what accumulated
- Before deep work: clear loops first if there are many
- When feeling mentally cluttered and want to know why
- After a busy period (travel, sprint) to re-orient

**Do NOT use for:**
- Today's priority ranking → `/briefing`
- Setting today's commitments → `/plan`
- Aggregate load level and work mode → `/cognitive-load`
- Finding what's missing from the knowledge base → `/knowledge-gap`

---

## Input

```
/open-loops              ← Full scan across all 6 sources
/open-loops --stale      ← Only items past their staleness threshold
/open-loops --category <name>   ← One category only (captures / meetings / signals / decisions / contradictions / workflows)
```

---

## Process

### Step 1 — Scan all sources

Read and check each source:

**Source 1 — Raw captures** (`notes/raw/`)
List all files. For each, note creation date. Stale threshold: >7 days unprocessed.

**Source 2 — Unprocessed meetings** (`meeting-intelligence/raw/`)
List all files. For each, note creation date. Stale threshold: >2 days unprocessed.
If a corresponding processed file exists in `meeting-intelligence/processed/` with the same date/name: skip (already processed).

**Source 3 — Unreviewed signals** (`strategy/signals/`)
Read current month's signal file + previous month's if it exists. Scan for signal entries.
A signal is "unreviewed" if: it has `reviewed: false` OR has no `reviewed` field AND is >7 days old.

**Source 4 — Pending decisions** (`decision-frameworks/decisions-log.md`)
Read the decisions log. Extract entries where `outcome: pending` (or outcome field is absent/empty).
Stale threshold: >30 days in pending state.

**Source 5 — Unresolved knowledge contradictions** (`knowledge/KNOWLEDGE-GRAPH.json`)
Read the graph. Extract edges where `type: "contradicts"` AND `resolution_status` is absent or `"unresolved"`.
Stale threshold: >60 days since the edge was created (if timestamp available; if not, flag all unresolved).

**Source 6 — Stalled workflows** (`runtime/state/active-workflows.json`)
Read active workflows. A workflow is an open loop if: status = GATE or PAUSED AND `last_active` > 3 days ago.
Workflows in RUNNING or DRAFT are not open loops — they're actively in progress.

### Step 2 — Count and classify

For each source, compute:
- Total items in inbox (regardless of staleness)
- Stale items (past threshold)
- Age of oldest item

### Step 3 — Apply routing

For each item, assign the default routing action:

| Category | Routing |
|----------|---------|
| Raw captures | `/promote` if worth keeping → `knowledge/` OR move to `notes/structured/` OR delete |
| Unprocessed meetings | `/debrief` → `meeting-intelligence/processed/` |
| Unreviewed signals | `/signal review` → mark reviewed, escalate threats to `/bet update` |
| Pending decisions | `/pre-decide` if complex, or `/decide` to log resolution |
| Unresolved contradictions | `/contradiction-register` → classify and resolve or flag as productive tension |
| Stalled workflows | `/runtime-resume` → advance or abandon |

---

## Output Format

```
OPEN LOOPS INVENTORY — [YYYY-MM-DD]
Total: [N] items across [K] categories  ([N] stale)

── Raw Captures ([N] total, [N] stale) ──
Stale threshold: 7 days
[filename] — [N] days old
[filename] — [N] days old  ⚠ STALE
[If 0: "Inbox clear."]
Routing: /promote or delete stale items

── Unprocessed Meetings ([N] total, [N] stale) ──
Stale threshold: 2 days
[filename] — [N] days old
[If 0: "No unprocessed meetings."]
Routing: /debrief

── Unreviewed Signals ([N] total) ──
[signal title or date] — [category] — [N] days old  [or: ⚠ STALE]
[If 0: "All signals reviewed."]
Routing: /signal review

── Pending Decisions ([N] total, [N] stale) ──
Stale threshold: 30 days
"[decision title]" — pending [N] days
[If 0: "No pending decisions."]
Routing: /pre-decide or /decide

── Unresolved Contradictions ([N] total) ──
[entry A] ↔ [entry B] — unresolved [since date or "date unknown"]
[If 0: "No unresolved contradictions."]
Routing: /contradiction-register

── Stalled Workflows ([N] total) ──
[wf-id] "[name]" — [status] — last active [N] days ago
[If 0: "No stalled workflows."]
Routing: /runtime-resume

SUMMARY
[N] open loops total ([N] stale)
Largest backlog: [category with most stale items]
Quickest wins: [category where routing takes least time]
→ Run /cognitive-load for aggregate load level and work mode recommendation
```

---

## Quality Gate

Before outputting:
- [ ] All 6 sources attempted to read (report "source unavailable" if missing, don't skip silently)
- [ ] Staleness computed from actual file dates, not estimated
- [ ] Processed meetings excluded (check processed/ directory)
- [ ] "Inbox clear" stated explicitly when a category has 0 items
- [ ] Routing recommendation given for every non-empty category
- [ ] STALE flag only applied when past the threshold — not for all items
- [ ] Summary names the category with the most stale items and the quickest-win category

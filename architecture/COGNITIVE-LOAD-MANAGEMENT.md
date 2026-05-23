# Cognitive Load Management System

Manages the aggregate mental overhead of running a complex operational workspace. Where `/briefing` and `/plan` tell the operator what to work on, this system diagnoses HOW MUCH mental load is currently present, WHERE threads are accumulating, and WHETHER attention is going to the right places.

## Existing Coverage (Do Not Duplicate)

| Skill | What It Covers |
|-------|---------------|
| `/briefing` | Today's priorities from action-items.md — Critical / Focus / Heads-Up |
| `/plan` | Today's theme + top 3 commitments + one risk flag |
| `/focus` | Frame a deep work session once direction is clear |
| `/shutdown` | End-of-day closure and tomorrow seed |
| `/exec-prioritize` | Commitment → leverage → reversibility ordering |
| `/exec-allocation` | Work-type distribution (strategic vs reactive vs overhead) |
| `/decision-due` | Past decisions approaching their review date |
| `/signal` | Capture and review environmental signals |

## New Skills (P29)

| Skill | Fills Gap | Core Question |
|-------|----------|--------------|
| `/open-loops` | No inventory of unresolved threads across all systems | "What is in flight without a home, and where does each item belong?" |
| `/cognitive-load` | No aggregate load assessment across the full workspace | "How mentally cluttered is the workspace right now? Is it safe to do deep work?" |
| `/attention-debt` | No analysis of attention vs strategic intention | "Where is attention going versus where should it be, given active bets and priorities?" |

## Capability Distinctions

```
What should I work on today?
→ /briefing  (today's priorities from action-items.md)

What commitments do I need to make for the day?
→ /plan  (theme + top 3 + risk flag)

How many unresolved threads am I carrying, and where are they?
→ /open-loops  (inbox scan: notes, meetings, signals, decisions, captures)

Is the workspace load high enough that I should reduce before doing deep work?
→ /cognitive-load  (aggregate load level + work mode recommendation)

Is my attention going to strategic priorities or drifting to low-weight areas?
→ /attention-debt  (attention distribution vs bet priority weighting)
```

---

## Cognitive Load Sources Model

The workspace has six primary load sources — places where unresolved work accumulates and consumes background attention.

| Source | Location | Open Loop Condition |
|--------|---------|-------------------|
| Raw captures | `notes/raw/` | File exists with no corresponding structured note or knowledge entry |
| Unprocessed meetings | `meeting-intelligence/raw/` | Meeting file not yet in `processed/` |
| Unreviewed signals | `strategy/signals/YYYY-MM.md` | Signal entries with `reviewed: false` or no review date |
| Pending decisions | `decision-frameworks/decisions-log.md` | Decision entries with `outcome: pending` |
| Unresolved contradictions | `knowledge/KNOWLEDGE-GRAPH.json` | Contradicts edges with `resolution_status: unresolved` |
| Active workflows | `runtime/state/active-workflows.json` | Workflows in GATE or PAUSED state — awaiting operator action |

Each source creates a different type of mental load. Raw captures = diffuse anxiety (something was noticed but not processed). Pending decisions = decision debt (resolution avoided). Active workflows at GATE = attention fragmented across multiple open threads.

---

## Load Level Model

Used by `/cognitive-load`:

| Level | Total Open Items | Meaning | Work Mode |
|-------|-----------------|---------|-----------|
| **Clear** | 0–5 | Low overhead; workspace is clean | Deep Focus — complex, creative, or strategic work |
| **Moderate** | 6–15 | Normal operational load | Focused Work — productive output; some context switching OK |
| **High** | 16–30 | Load accumulating; attention fragmented | Reduction Mode — reduce load before deep work |
| **Overloaded** | 31+ | Cognitive capacity compromised | Maintenance Only — process inbox, defer everything else |

Total open items = sum of counts across all six load sources.

Work mode recommendations:
- **Deep Focus**: Complex synthesis, strategy decisions, architectural thinking — requires uninterrupted mental bandwidth
- **Focused Work**: Implementation, analysis, review — productive but doesn't require peak mental state
- **Reduction Mode**: Before starting deep work, invest 20–30 min reducing load to Moderate (close loops, route items, process captures)
- **Maintenance Only**: Inbox processing, signal review, capture routing — do not attempt deep work until load drops to High or below

---

## Open Loop Taxonomy

Used by `/open-loops`:

| Category | Source | Staleness Threshold | Default Routing |
|----------|--------|---------------------|----------------|
| Raw captures | `notes/raw/` | >7 days unprocessed | `/promote` (if worth keeping) or delete |
| Unprocessed meetings | `meeting-intelligence/raw/` | >2 days unprocessed | `/debrief` |
| Unreviewed signals | `strategy/signals/` | >7 days unreviewed | `/signal review` |
| Pending decisions | `decisions-log.md` | >30 days in pending | `/decide` or `/pre-decide` |
| Unresolved contradictions | `KNOWLEDGE-GRAPH.json` | >60 days unresolved | `/contradiction-register` |
| GATE/PAUSED workflows | `active-workflows.json` | >3 days stalled | `/runtime-resume` |

Stale = exists longer than staleness threshold without progress. Each open loop beyond its threshold adds +1 to cognitive load score.

---

## Attention Debt Model

Used by `/attention-debt`. Compares TWO signals:

**Attention signal** (where attention is actually going):
- Trace session goals and tags (last 30 days from TRACE-INDEX.md)
- Recent skill invocations (skill-stats output if recent)
- Captured notes by domain

**Priority signal** (where attention should be going):
- Active bets by horizon: H1 (urgent) > H2 (building) > H3 (exploring)
- Investment level declared per bet
- Recent strategy review verdicts

**Attention debt** = high-priority bets or domains with ZERO trace entries in last 30 days.
**Attention sink** = domains/topics with high trace volume but no associated active bet or strategic priority.

Attention drift threshold: an H1 bet with 0 trace entries in 14 days is an attention debt emergency.

---

## Cognitive Load Reduction Workflow

Recommended sequence when load level = High or Overloaded:

```
Step 1: /cognitive-load
        → Identify load level and primary contributing sources

Step 2: /open-loops
        → Get specific inventory of what's in each source

Step 3: For each category, apply the routing:
        - Raw captures >7d old: /promote or delete (takes ~5 min each)
        - Unprocessed meetings: /debrief (takes 10-15 min each)
        - Stale signals: /signal review (batch review, takes 15-20 min)
        - Long-pending decisions: /pre-decide → /decide (takes 20-30 min each)
        - GATE workflows: /runtime-resume (takes 5-10 min to advance)

Step 4: Re-run /cognitive-load to confirm level has dropped

Step 5: Proceed to deep work
```

Target before deep work: Moderate or Clear level.

---

## Anti-Patterns

| Anti-pattern | Why it fails |
|-------------|-------------|
| Running /open-loops and adding everything to a task list | Open loops are inbox items, not tasks — most should be routed, not scheduled |
| Checking /cognitive-load multiple times per day | Load level changes slowly; daily or session-start check is sufficient |
| Treating "High" load as an emergency | High is normal for an active operator; the goal is to not stay there for >2 consecutive days |
| Using /attention-debt to judge attention quality | Attention debt measures strategic alignment, not productivity — some zero-attention areas may be intentionally deprioritized |
| Running /attention-debt before strategy/active-bets.md is current | Attention debt comparison is only meaningful when the priority signal (bet register) reflects current strategy |

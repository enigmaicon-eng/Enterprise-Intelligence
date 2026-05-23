# Core Operational Workflows
## Step-by-Step Execution Guides

---

## Workflow Catalog

| ID | Workflow | Trigger | Tier | Output Location |
|----|---------|---------|------|----------------|
| W01 | Daily Briefing | Session start / `/briefing` | Sonnet | Terminal (ephemeral) |
| W02 | Capture Note | `/capture <note>` | Haiku | `notes/raw/` |
| W03 | Meeting Debrief | `/debrief <file>` | Sonnet | `meeting-intelligence/processed/` |
| W04 | Promote to Knowledge | `/promote <file>` | Sonnet | `knowledge/` |
| W05 | Weekly Review | Monday 08:00 / `/review weekly` | Opus | `reviews/weekly/` |
| W06 | Monthly Strategy | Month start / `/review monthly` | Opus+thinking | `strategy/monthly/` |
| W07 | Decision Log | `/decide <context>` | Sonnet | `decision-frameworks/decisions-log.md` |
| W08 | Synthesis Memo | `/synthesize <topic>` | Opus | `synthesis/` |
| W09 | Learning Entry | `/learn <topic>` | Haiku→Sonnet | `learning/` |
| W10 | Observability Report | Weekly automated | Sonnet | `observability/dashboard.md` |
| W11 | Execution Plan | `/exec-plan <initiative>` | Sonnet | `execution/plans/` |
| W15 | Strategy Review | `/strategy-review` | Opus+thinking | `strategy/reviews/` |
| W16 | Bet Lifecycle | `/bet open|update|close|postmortem` | Sonnet | `strategy/bets/` |
| W17 | Horizon Scan | `/horizon` | Opus | `strategy/horizons/` |
| W18 | Strategy Posture | `/strategy-posture` | Opus | terminal + `knowledge/strategy/` |
| W12 | Task Decomposition | `/exec-decompose <id> <milestone>` | Sonnet | `execution/decompositions/` |
| W13 | Execution Review | `/exec-review [weekly]` | Sonnet | `reviews/weekly/[YYYY-WW]-exec.md` |
| W14 | Strategic Checkpoint | `/exec-checkpoint <id>` | Sonnet | `execution/checkpoints/` |

---

## W01 — Daily Briefing

**Purpose:** Start each session with a focused, prioritized view of what matters today.

**Steps:**
1. Read `execution/action-items.md` — filter for today or overdue
2. Read `execution/follow-ups.md` — filter for pending
3. Read `memory/` — surface active project context
4. Call Sonnet with `prompts/workflows/daily-briefing.md`
5. Output: 3-section briefing printed to terminal

**Output Format:**
```
## Today's Briefing — 2026-05-20

### Critical (due today / overdue)
- [ ] ...

### Focus (top 3 by strategy alignment)
1. ...

### Heads-Up (meetings / async to watch)
- ...
```

**Time budget:** <30s total. If taking longer, the action items file is too large — archive completed items.

---

## W02 — Capture Note

**Purpose:** Get raw thoughts out of your head and into the workspace without friction.

**Steps:**
1. Create `notes/raw/YYYY-MM-DD-HHmm-<slug>.md`
2. Call Haiku to tag the note (domain, type, urgency, connections)
3. Write tags to frontmatter
4. If urgency=high → add to `execution/action-items.md`
5. Queue for promotion review (weekly batch)

**Frontmatter added by Haiku:**
```yaml
---
captured: 2026-05-20T08:32
domain: strategy | technical | operations | learning
type: insight | question | action | reference | idea
urgency: high | medium | low
tags: [tag1, tag2]
promote_candidate: true | false
---
```

---

## W03 — Meeting Debrief

**Purpose:** Convert a meeting into structured, actionable, forward-feeding intelligence.

**Input:** Raw transcript or notes file in `meeting-intelligence/raw/`

**Steps:**
1. Load raw meeting file
2. Call Sonnet with `prompts/workflows/meeting-debrief.md`
3. Extract and append to `execution/action-items.md`
4. Extract and append to `decision-frameworks/decisions-log.md`
5. Extract knowledge candidates → queue for W04
6. Write structured output to `meeting-intelligence/processed/YYYY-MM-DD-topic.md`
7. Mark raw file as `processed: true`

**Structured Output Sections:**
- `## Summary` — 3-sentence max
- `## Key Points` — bulleted, not paraphrased
- `## Decisions Made` — with rationale
- `## Action Items` — owner, due date, priority
- `## Knowledge Candidates` — topics worth promoting to knowledge base
- `## Follow-up Needed` — async threads to resolve
- `## Patterns` — connections to other meetings or ongoing themes

---

## W04 — Promote to Knowledge

**Purpose:** Turn a note or meeting extract into a permanent, linked knowledge entry.

**Input:** A capture or meeting knowledge candidate

**Steps:**
1. Load source file
2. Check `knowledge/KNOWLEDGE-INDEX.md` — does this concept already exist?
   - If yes: decide to extend existing entry or create sub-entry
   - If no: create new entry
3. Call Sonnet with `prompts/workflows/promote-to-knowledge.md`
4. Write to `knowledge/<domain>/<concept-slug>.md`
5. Update `knowledge/KNOWLEDGE-INDEX.md`
6. Scan for `[[connections]]` — update linked files with back-reference
7. Mark source as `promoted: true`

**Knowledge Entry Template:**
```markdown
---
title: Concept Name
domain: strategy | technical | systems | operations
created: YYYY-MM-DD
reviewed: YYYY-MM-DD
connections: [other-concept, another-concept]
confidence: high | medium | low
source: original synthesis | meeting-YYYY-MM-DD | note-slug
---

## Definition
One clear paragraph. What is this, precisely?

## Why It Matters
How this connects to your work. Practical stakes.

## Key Principles
- Principle 1
- Principle 2

## Connections
Links to related knowledge: [[other-concept]], [[another-concept]]

## Open Questions
What you don't yet know about this.
```

---

## W05 — Weekly Review

**Purpose:** Close the loop on the week. Surface patterns. Calibrate next week.

**Input:** Everything accumulated during the week

**Steps:**
1. Assemble context:
   - Completed / incomplete action items this week
   - All processed meeting files (Mon–Sun)
   - New knowledge entries created
   - Decisions logged
   - Telemetry: most active workflows, token cost
2. Call Sonnet with `prompts/workflows/weekly-review.md`
3. Assess against goals in `strategy/` — are we on track?
4. Write `reviews/weekly/YYYY-WW.md`
5. If synthesis_needed: call Opus for `synthesis/weekly-insights/YYYY-WW.md`
6. Update `execution/action-items.md` — carry over, close, re-prioritize
7. Update relevant memory files if new patterns emerged

**Weekly Review Output Sections:**
- `## Week Summary` — 2-3 sentences, the essence
- `## Progress vs. Commitments` — what was done, what slipped, why
- `## Patterns & Insights` — what repeated, what surprised
- `## Learning This Week` — knowledge added
- `## Decision Quality` — retrospective on decisions made
- `## Next Week Priorities` — top 5, with strategy alignment rationale
- `## Questions to Resolve` — open threads needing attention

---

## W06 — Monthly Strategy Review

**Purpose:** Zoom out. Assess the portfolio of bets. Adjust strategy.

**Input:** Last 4 weekly reviews + active strategy documents

**Steps:**
1. Load `reviews/weekly/` (last 4 files)
2. Load `strategy/` active files
3. Load `decision-frameworks/decisions-log.md` (last 30 days)
4. Call Opus + extended thinking with `prompts/workflows/strategy-synthesis.md`
5. Write `strategy/monthly/YYYY-MM.md`
6. Write `synthesis/monthly-insights/YYYY-MM.md`
7. Update `strategy/active-bets.md` — add/remove/adjust
8. Update `CLAUDE.md` if strategic context has materially shifted

**Extended Thinking Budget:** 16,000 tokens — give it room to reason through contradictions.

**Monthly Strategy Output Sections:**
- `## Month Summary` — the shape of the month
- `## OKR Progress` — objective by objective
- `## Bet Portfolio Review` — each active bet: signal/noise, adjust/kill/double-down
- `## Horizon Scan` — H1 (0-3mo), H2 (3-12mo), H3 (12mo+)
- `## Cross-Domain Connections` — unexpected links between domains
- `## Updated 90-Day Priorities` — concrete reordering
- `## What I Was Wrong About` — honest retrospective on failed predictions

---

## W07 — Decision Log

**Purpose:** Make decisions explicit, reasoned, and reviewable.

**Trigger:** Any significant decision — technical, strategic, operational.

**Steps:**
1. Describe the decision context in plain language
2. Call Sonnet to structure it into decision log format
3. Append to `decision-frameworks/decisions-log.md`
4. Set `review_date` (default: 90 days)
5. Weekly review surfaces upcoming review dates

**When to use:** Any decision that would be hard to explain later, involves real trade-offs, or commits resources/time.

---

## W08 — Synthesis Memo

**Purpose:** Generate a deep, cross-domain synthesis on a specific topic.

**Trigger:** Manual — when you need to think clearly about something important.

**Steps:**
1. Specify the topic and scope
2. Gather relevant files: knowledge entries, decisions, meeting notes, strategy docs
3. Call Opus with `prompts/workflows/synthesis-memo.md`
4. Write `synthesis/<topic>-YYYY-MM-DD.md`
5. Extract knowledge candidates → queue for W04
6. Add to `KNOWLEDGE-INDEX.md` if topic is recurring

---

## W09 — Learning Entry

**Purpose:** Capture and structure learning so it compounds.

**Steps:**
1. Describe what was learned (course, paper, experiment, conversation)
2. Haiku tags the entry (domain, type, source)
3. Sonnet expands into structured learning entry
4. Write to `learning/<domain>/YYYY-MM-DD-<slug>.md`
5. Auto-queue for knowledge promotion if `promote_candidate: true`

**Learning Entry Structure:**
- `## What I Learned` — concrete, specific
- `## Why It Matters` — implications for current work
- `## Mental Model Update` — how this changes how I think
- `## Open Questions` — what I need to explore next
- `## Related Knowledge` — links to existing entries

---

## W10 — Observability Report

**Purpose:** Maintain system health and drive continuous improvement.

**Trigger:** Automated weekly, or `/observe`

**Steps:**
1. Read `telemetry/api-log.jsonl` — last 7 days
2. Read `observability/quality.jsonl` — human ratings this week
3. Call Sonnet to generate dashboard
4. Write `observability/dashboard.md`
5. Flag anomalies in next weekly review

**Dashboard Sections:**
- Token cost by workflow (actual vs. target)
- Cache hit rate (target: >60%)
- Latency by model tier
- Workflows with lowest quality scores
- Dead workflows (not triggered in 30+ days)
- Stale memory files (not read in 30+ days)
- Stale knowledge entries (not reviewed in 90+ days)

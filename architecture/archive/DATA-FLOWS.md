# Data Flows
## How Intelligence Moves Through the Workspace

---

## Primary Flows

### Flow 1 — Capture → Knowledge

```
Raw Input (note, URL, voice memo, meeting)
          │
          ▼
    [notes/raw/]          ← Drop zone, no structure required
          │
          ▼
  Capture Agent (Haiku)   ← Tags, extracts entities, detects domain
          │
          ├──────────────────────────────────────┐
          ▼                                      ▼
  [notes/structured/]               If meeting: [meeting-intelligence/]
          │
          ▼
  Promotion Decision      ← Is this permanent knowledge or ephemeral?
          │
     ┌────┴────┐
     ▼         ▼
[knowledge/]  Archive    ← Permanent vs. time-limited
     │
     ▼
 KNOWLEDGE-INDEX.md updated
     │
     ▼
 Connections checked      ← Does this link to existing knowledge nodes?
     │
     ▼
 Memory updated if needed ← Does this change user context or project state?
```

---

### Flow 2 — Meeting Intelligence Pipeline

```
Meeting (transcript / notes / recording summary)
          │
          ▼
  [meeting-intelligence/raw/YYYY-MM-DD-topic.md]
          │
          ▼
  Meeting Debrief Agent (Sonnet)
          │   Uses: prompts/workflows/meeting-debrief.md
          │
          ├── Extracts: Action items → [execution/action-items.md]
          ├── Extracts: Decisions → [decision-frameworks/decisions-log.md]
          ├── Extracts: Knowledge → [knowledge/] (promoted automatically)
          ├── Extracts: Follow-ups → [execution/follow-ups.md]
          └── Produces: [meeting-intelligence/processed/YYYY-MM-DD-topic.md]
                              │
                              ▼
                    Weekly Review picks up all processed meetings
                    and synthesizes cross-meeting patterns
```

---

### Flow 3 — Weekly Review Cycle

```
Trigger: Every Monday 08:00 (or manual /review weekly)
          │
          ▼
  Context Assembly Agent
  Reads:
  ├── [execution/action-items.md]     ← What was committed
  ├── [meeting-intelligence/processed/] ← This week's meetings
  ├── [notes/structured/]             ← Captures from the week
  ├── [telemetry/workflow-log.jsonl]  ← What was worked on
  └── [memory/] context files         ← Goals, projects, priorities
          │
          ▼
  Analysis Agent (Sonnet)
  Using: prompts/workflows/weekly-review.md
          │
          ├── Progress vs. commitments
          ├── Patterns from meetings
          ├── Knowledge gaps surfaced
          ├── Decision quality retrospective
          └── Next week priorities
          │
          ▼
  [reviews/weekly/YYYY-WW.md]  ← Structured weekly review output
          │
          ▼
  Strategy Agent (Opus, if synthesis_needed flag set)
          │
          ▼
  [synthesis/weekly-insights/YYYY-WW.md]
          │
          ▼
  Memory updated: project states, learned preferences
```

---

### Flow 4 — Strategy Synthesis Cycle (Monthly)

```
Trigger: First Monday of month
          │
          ▼
  Reads: Last 4 weekly reviews + active strategy docs
          │
          ▼
  Strategy Agent (Opus 4.7 + extended thinking)
  Using: prompts/workflows/strategy-synthesis.md
          │
          ├── OKR progress assessment
          ├── Bet portfolio review (what's working/not)
          ├── Horizon 1/2/3 status
          ├── Cross-domain connection mining
          └── Updated 90-day priorities
          │
          ▼
  [strategy/monthly/YYYY-MM.md]
          │
          ▼
  [synthesis/monthly-insights/YYYY-MM.md]
          │
          ▼
  CLAUDE.md updated if strategic context changed
```

---

### Flow 5 — Daily Briefing

```
Trigger: Each session start (or /briefing command)
          │
          ▼
  Reads:
  ├── [execution/action-items.md]    ← Open items
  ├── [execution/follow-ups.md]      ← Pending follow-ups
  ├── Today's calendar/meetings      ← If Google Calendar connected
  └── [memory/] for active projects
          │
          ▼
  Briefing Agent (Sonnet, low token budget)
          │
          ▼
  Output: 3-section briefing
  ├── Critical: items due today or overdue
  ├── Focus: top 3 priorities based on strategy alignment
  └── Heads-up: meetings with prep notes
          │
          ▼
  Displayed in terminal (not written to file — ephemeral)
```

---

### Flow 6 — Telemetry → Improvement Loop

```
Every API call → [telemetry/api-log.jsonl]
Every workflow → [telemetry/workflow-log.jsonl]
Human ratings  → [observability/quality.jsonl]
          │
          ▼ (Weekly, automated)
  Analysis Agent reads all telemetry
          │
          ├── Token cost by workflow type
          ├── Latency outliers
          ├── Prompt versions with lowest quality scores
          ├── Workflows never triggered (dead weight)
          └── Memory files never read (stale)
          │
          ▼
  [observability/dashboard.md]  ← Human-readable weekly health report
          │
          ▼
  Flags surfaced in next weekly review
          │
          ▼
  Prompts revised, workflows pruned, memory cleaned
```

---

## Data Schemas

### API Log Entry (`telemetry/api-log.jsonl`)
```json
{
  "ts": "2026-05-20T08:32:11Z",
  "session_id": "sess_abc123",
  "workflow": "meeting-debrief",
  "model": "claude-sonnet-4-6",
  "input_tokens": 4821,
  "output_tokens": 892,
  "cache_read_tokens": 3200,
  "cache_write_tokens": 1621,
  "latency_ms": 2340,
  "prompt_version": "meeting-debrief-v2.1"
}
```

### Knowledge File Frontmatter
```yaml
---
title: Concept or Research Title
domain: strategy | technical | systems | operations
created: 2026-05-20
reviewed: 2026-05-20
tags: [tag1, tag2]
connections: [other-knowledge-file, another-file]
source: url or "original synthesis"
confidence: high | medium | low
---
```

### Meeting Intelligence File
```yaml
---
date: 2026-05-20
participants: [Name1, Name2]
duration_minutes: 45
type: 1:1 | team | external | strategy
topics: [topic1, topic2]
processed: false
action_items_extracted: false
---
```

### Decision Log Entry
```yaml
---
decision: Short description of what was decided
date: 2026-05-20
context: Why this decision point arose
options_considered: [option1, option2]
chosen: option1
rationale: Why option1 was selected
reversibility: high | medium | low | irreversible
review_date: 2026-08-20
---
```

# Trace Capture + Skill Codification System
## Personal Operational Memory Compounding for One Operator

---

## What This System Is

A file-based system for capturing, indexing, and retrieving personal execution history. It answers one question across all its components: **"How did I do this before, and what can I reuse?"**

**What it is not:**
- Not collective or shared intelligence
- Not autonomous self-evolution
- Not a knowledge base (that's `knowledge/` — separate domain)
- Not a replacement for the runtime workflow system (P13 tracks active execution; this captures completed episodes)

**The core loop:** Execute → Capture → Index → Recall → Execute better.

---

## Memory Tiers

Three tiers. Match retrieval behavior to tier.

| Tier | Contents | Location | Lifecycle |
|------|----------|----------|-----------|
| **Hot** | Today's journal, active session context | `traces/journal/YYYY-MM-DD.md` | Current day |
| **Warm** | Recent execution traces, detected patterns | `traces/executions/`, `traces/patterns/` | 0–90 days |
| **Cold** | Archived traces | `traces/archive/` | 90+ days |

Patterns and primitives are **always warm** — they're distilled and timeless. Individual traces age into cold.

---

## Four Memory Types

### 1. Episodic Memory — Execution Episodes
`traces/executions/exec_YYYYMMDD_NNN.md`

What happened in a specific session: goal, sequence, decisions, artifacts, what worked, what failed. The raw material for pattern detection. Captured after the fact via `/trace-capture`.

### 2. Working Memory — Daily Journal
`traces/journal/YYYY-MM-DD.md`

Quick daily log: what was worked on, key insights, open questions, tomorrow's seeds. Captured via `/workflow-journal`. Lightweight — 5 minutes at session end.

### 3. Semantic Memory — Operational Patterns
`traces/patterns/pat_<slug>.md`

Distilled from multiple episodes: "when in situation X, do Y in sequence Z." Written when a pattern has appeared 2+ times. Captured via `/pattern-mine`. Updated when new instances are confirmed.

### 4. Procedural Memory — Execution Primitives
`traces/primitives/prim_<slug>.md`

Named, reusable atomic procedures. More concrete than patterns — specific enough to follow as a checklist. Promoted from patterns via `/pattern-mine`. Referenced during `/trace-recall` when preparing for similar work.

---

## Component Map

| Component | What It Does | Skill | Output |
|-----------|-------------|-------|--------|
| Trace Capture Engine | Records a completed execution episode | `/trace-capture` | `traces/executions/exec_*.md` |
| Workflow Journal | Quick daily session log | `/workflow-journal` | `traces/journal/YYYY-MM-DD.md` |
| Execution Recall Layer | Surfaces relevant past traces before starting work | `/trace-recall` | Traces loaded into context |
| Searchable History | Keyword search across trace index | `/trace-search` | Matching trace entries |
| Pattern Detection | Scans traces, drafts patterns/primitives | `/pattern-mine` | `traces/patterns/` or `traces/primitives/` |

---

## Trace Index

`traces/TRACE-INDEX.md` — the master retrieval surface. One line per trace.

Format:
```
| ID | Date | Type | Goal (brief) | Outcome | Tags |
```

All retrieval skills read this index first before loading individual trace files. Never scan `traces/executions/` directly — always read the index.

---

## Skill Codification Flow

When an operational primitive is confirmed:

```
2+ similar execution episodes captured
    │
    ▼
/pattern-mine — detect recurring elements
    │
    ├─ Operational pattern → traces/patterns/pat_<slug>.md
    │
    └─ Atomic reusable procedure → traces/primitives/prim_<slug>.md
         │
         └─ (if primitive warrants a full skill)
              /skill-new — promote primitive to workspace skill
```

The promotion path from execution trace → primitive → skill is the codification pipeline. Each step requires operator confirmation.

---

## Retrieval-Enhanced Execution

Before starting work that resembles past work:

```
"I'm about to do X" → /trace-recall X
    │
    ▼
TRACE-INDEX.md scanned for matching goal/tag/type
    │
    ├─ Relevant traces found
    │    └─ Load the top 1-3 traces → surface key decisions, what worked, what failed
    │         └─ Proceed with this context loaded
    │
    └─ No relevant traces
         └─ Proceed normally; consider capturing a trace after completion
```

This prevents re-discovering the same failure modes and re-inventing the same solutions.

---

## Lifecycle

```
Capture    → traces/executions/   (warm, 0-90 days)
Archive    → traces/archive/      (cold, 90+ days; move during /observe)
Distill    → traces/patterns/     (always warm)
Codify     → traces/primitives/   (always warm)
Promote    → .claude/commands/    (if warranted → new skill)
```

The `/observe` workspace health skill triggers the archive pass for traces older than 90 days.

---

## File Locations

| What | Path |
|------|------|
| Trace index | `traces/TRACE-INDEX.md` |
| Execution episodes | `traces/executions/exec_YYYYMMDD_NNN.md` |
| Daily journal | `traces/journal/YYYY-MM-DD.md` |
| Operational patterns | `traces/patterns/pat_<slug>.md` |
| Execution primitives | `traces/primitives/prim_<slug>.md` |
| Archive | `traces/archive/` |
| Episode template | `templates/execution-trace.md` |
| Pattern template | `templates/execution-pattern.md` |
| Primitive template | `templates/execution-primitive.md` |

---

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Capturing every session | Noise overwhelms signal | Capture when reuse potential is medium/high |
| Building automated pattern detection | Script complexity for conversational work | Pattern detection is conversational via /pattern-mine |
| Storing execution traces in memory/ | Wrong layer — memory/ is for orientation facts | Traces live in traces/ |
| Promoting patterns to skills prematurely | Premature codification | Require 2+ instances before pattern entry; 3+ before skill promotion |
| Reading all trace files directly | Slow; bypasses index | Always read TRACE-INDEX.md first |

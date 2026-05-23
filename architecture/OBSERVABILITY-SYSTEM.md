# Operational Observability System

Single-operator runtime visibility and execution introspection. Five focused diagnostics that surface what's happening across the runtime, execution history, skill usage, failures, and retrieval layer — without enterprise-scale infrastructure.

## What This Is

Conversational observability. Each skill reads existing file-based state and surfaces a structured terminal view. No agents. No continuous monitoring. No dashboards written to disk unless specified. You run a skill when you need to see; it reads the current state and tells you what's there.

## What This Is NOT

- Enterprise observability platform
- Distributed telemetry infrastructure
- Automated monitoring with alerts
- Metrics aggregation pipelines
- Anything that runs without operator invocation

## Existing Observability (Do Not Duplicate)

| Existing Skill | What It Covers |
|----------------|---------------|
| `/observe` | API cost, cache hit rates, quality scores, dead workflows — reads JSONL telemetry |
| `/runtime-status` | Active workflow state, event queue, runtime consistency check |
| `/context-audit` | 8-dimension context health (CLAUDE.md, memory, knowledge, skills, prompts, retrieval, budget, layer separation) |
| `/debug-ai` | AI system failure diagnosis |
| `/trace-search` | Keyword/filter search across execution history |
| `/trace-recall` | Relevance-scored trace retrieval before starting work |

## New Observability Skills (P22)

| Skill | Observability Dimension | Primary Data Source |
|-------|------------------------|---------------------|
| `/ops-dashboard` | Integrated operational view | TRACE-INDEX.md + runtime/state/ |
| `/exec-inspect` | Single-execution deep dive | traces/executions/<id>.md |
| `/skill-stats` | Skill invocation + session type analytics | TRACE-INDEX.md |
| `/failure-review` | Failure taxonomy + recurring failure modes | TRACE-INDEX.md + failed trace files |
| `/retrieval-diag` | Retrieval system health + recall readiness | TRACE-INDEX.md + traces/executions/ |

## Observability Coverage Map

```
What you want to know                           → Which skill
────────────────────────────────────────────────────────────
What's currently running?                       → /runtime-status
Is the workspace healthy overall?               → /observe + /context-audit
Operationally, where do I stand?               → /ops-dashboard
What happened in execution exec_YYYYMMDD_NNN?  → /exec-inspect
What kinds of work am I capturing?             → /skill-stats
What patterns have been failing?               → /failure-review
Can /trace-recall actually help me?            → /retrieval-diag
Why is an AI output wrong?                     → /debug-ai
Is context load within budget?                 → /context-audit
How are API costs trending?                    → /observe
```

## Skill Interaction Patterns

**Weekly health ritual (recommended order):**
1. `/obs-dashboard` — operational overview first
2. `/observe` — cost + quality metrics
3. `/context-audit quick` — budget + layer check
4. `/retrieval-diag` — is the trace system working?
5. `/failure-review` — if failure count is elevated

**Before a pattern-mining session:**
1. `/skill-stats` — which domains have 3+ episodes?
2. `/retrieval-diag` — how many open candidates?
3. `/pattern-mine` — codify

**After a runtime incident:**
1. `/runtime-status` — current state
2. `/exec-inspect <exec-id>` — what happened in the failed trace
3. `/failure-review` — is this a recurring mode?
4. `/runtime-recover` — if state is corrupted

## Data Sources Reference

```
traces/
  TRACE-INDEX.md          ← primary index for all 5 new skills
  executions/             ← loaded by /exec-inspect + /failure-review + /retrieval-diag
  patterns/               ← referenced by /retrieval-diag
  primitives/             ← referenced by /retrieval-diag

runtime/state/
  active-workflows.json   ← loaded by /ops-dashboard
  workflow-history.json   ← loaded by /ops-dashboard

memory/
  MEMORY.md               ← loaded by /ops-dashboard (memory freshness check)
```

## Observability Architecture Constraints

**AC-1:** No Python scripts — all observability is conversational (skills read files and surface structured output).

**AC-2:** No SQLite — no aggregation database. Metrics are computed on-demand from existing files.

**Read before write:** All observability skills are read-only. None write to disk (except `/observe` which writes observability/dashboard.md — that is intentional and pre-existing).

**Index first:** Every skill that touches trace history reads TRACE-INDEX.md before loading any individual trace file.

**Bounded reads:** No skill loads more than 10 trace files per invocation. If scope exceeds that, filter further before loading.

## Anti-Patterns

| Anti-pattern | Why it fails |
|-------------|-------------|
| Running `/ops-dashboard` every session | Observability is for diagnosis, not routine startup — use `/briefing` for daily orientation |
| Building a Python metrics aggregator | AC-1 violation; adds maintenance cost without commensurate value |
| Writing a live dashboard file | Static dashboards decay instantly; terminal output is always current |
| Loading all traces to compute aggregate metrics | Unbounded reads degrade performance; use TRACE-INDEX.md as the aggregate surface |
| Using `/exec-inspect` to search | It loads one trace; use `/trace-search` for multi-trace queries |

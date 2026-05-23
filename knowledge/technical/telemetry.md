---
title: Telemetry Systems for AI
domain: technical
created: 2026-05-22
reviewed: 2026-05-22
tags: [telemetry, logging, JSONL, cost-attribution, metrics, AI-ops]
connections: [observability, tracing, ai-systems, ai-debugging]
confidence: high
source: original synthesis
---

## Definition
Telemetry is the structured data a system emits about its own behavior. For AI systems, telemetry is the foundation of cost attribution, quality tracking, and debugging. Without telemetry, you're operating blind: you don't know what the system is doing, what it's costing, or where it's failing.

Telemetry is not logging in the traditional sense. Traditional logs capture exceptions and state transitions. AI telemetry captures every inference call, regardless of whether it succeeded or failed, with enough metadata to reconstruct the cost and quality profile of any workflow.

## Why It Matters
AI costs are invisible without telemetry. A workflow that calls Opus 10 times, each with a 2K-token system prompt and no caching, costs ~10× more than it needs to. You won't notice until the bill arrives — if you're even looking. Telemetry makes costs visible in real time so you can act before the bill.

## The JSONL Telemetry Schema

JSONL (newline-delimited JSON) is the standard format for AI telemetry. One line per call. Append-only. Human-readable. Queryable with standard tools.

**Required fields:**

```json
{
  "ts": "2026-05-22T09:00:00Z",
  "session_id": "abc-123-def",
  "workflow": "meeting-debrief",
  "tier": "analysis",
  "model": "claude-sonnet-4-6",
  "input_tokens": 2400,
  "output_tokens": 850,
  "cached_tokens": 1800,
  "cache_write_tokens": 600,
  "latency_ms": 2100,
  "status": "success",
  "completion_reason": "stop",
  "cost_usd": 0.00312
}
```

**Optional but high-value fields:**

```json
{
  "prompt_version": "v1.2",
  "prompt_hash": "a3f1b2",
  "quality_score": null,
  "user_id": "enigmaicon",
  "request_id": "req-xyz-789",
  "error_code": null,
  "error_message": null,
  "retry_count": 0
}
```

**Rules for the schema:**
- `ts` is always UTC ISO 8601. Never local time.
- `session_id` links all calls in a workflow session. Required for cost attribution.
- `workflow` is the human-readable name of the skill or script that made the call.
- `cached_tokens` is the number of tokens served from cache (reduces cost ~90%). Non-zero means caching is working.
- `cost_usd` is always calculated at log time using the current token price table — don't calculate retroactively.

## Cost Attribution Model

Cost attribution answers: "which workflow is spending money and how much?"

**Level 1 — Per-call:** Sum `cost_usd` for all calls with the same `ts` timestamp range.

**Level 2 — Per-workflow:** Group by `workflow`. Compare average cost per invocation across workflows. Most expensive workflow is the highest-leverage optimization target.

**Level 3 — Per-session:** Group by `session_id`. This links cost to a specific user action or automation run.

**Level 4 — Trend:** Weekly and monthly cost by workflow. Rising cost with stable volume = something changed (prompt grew, caching broke, tier escalated).

**This workspace's cost calculation** (from `scripts/telemetry_reader.py`):
```
cost = (input_tokens × $per_input) + (output_tokens × $per_output)
     + (cache_write_tokens × $per_write) - (cached_tokens × $discount)
```

Cache savings: `cached_tokens × (per_input - per_cached_input)`. At ~90% discount, this is significant at any scale.

## Cache Hit Rate: The Key Health Metric

Cache hit rate = `cached_tokens / input_tokens` per call (excluding cache_write calls).

| Rate | Interpretation | Action |
|------|---------------|--------|
| 0% | Caching not configured or system prompt changing every call | Add `cache_control: ephemeral` to system prompt |
| < 30% | Cache TTL mismatch or system prompt varies too much | Stabilize system prompt; check TTL |
| 50-70% | Normal for mixed workflows | Monitor for degradation |
| > 80% | Excellent — system prompt is stable and caching is working | No action needed |

**Cache TTL:** Anthropic's cache TTL is 5 minutes (300 seconds). If calls are spaced more than 5 minutes apart, cache is cold on the next call. Design batch workflows to run within 5-minute windows when possible.

## Dual-Stream Telemetry

This workspace implements dual-stream telemetry via WorkspaceClient:
- `telemetry/api-log.jsonl` — raw API calls (every call, all fields)
- `observability/quality.jsonl` — quality ratings (human-annotated, separate stream)

The dual-stream design separates signal collection (automatic) from quality annotation (manual). This is correct: don't mix automated telemetry with human judgment in the same stream.

## Signal Aggregation Patterns

**Alertable metrics** (check weekly):
- `avg(latency_ms)` by workflow — p50, p95, p99
- `sum(cost_usd)` by day and workflow
- `avg(cached_tokens / input_tokens)` by workflow
- `count(status == 'error')` by workflow and error_code

**Diagnostic metrics** (check when investigating):
- `max(input_tokens)` — identify abnormally large inputs
- `avg(output_tokens)` trend — rising output may indicate prompt instruction drift
- `count(completion_reason == 'max_tokens')` — truncated outputs signal budget issues

**Health metrics** (check monthly):
- Cache hit rate trend over 30 days
- Cost per workflow invocation trend
- Quality score correlation with model tier

## Key Principles

- **Every AI call produces telemetry. No exceptions.** Un-telemetered calls are invisible to the improvement loop.
- **Log at call time, not on success.** Include error calls in the telemetry stream — errors are often the most informative events.
- **`session_id` is the attribution primitive.** Without it, cost and quality data can't be linked to workflows.
- **Cache write tokens cost money too.** Don't cache small system prompts — the write cost exceeds the read savings if the cache is rarely hit.
- **Schema stability matters.** Changing field names retroactively breaks all your queries. Lock the schema; add fields, don't rename.

## In Practice

WorkspaceClient in `production-ai/claude_client.py` handles all telemetry automatically for Python-based workflows. For Claude Code sessions (interactive), telemetry must be logged manually or via hooks.

Key: `scripts/telemetry_reader.py` reads `api-log.jsonl` without making API calls — safe for cost-analysis queries at any time.

## Connections
- [[observability]] — telemetry is the raw signal layer; observability is what you build on top
- [[tracing]] — trace IDs link telemetry entries into causal chains
- [[ai-systems]] — model IDs and tier routing decisions are recorded in telemetry
- [[ai-debugging]] — telemetry is always the first place to look when debugging

## Open Questions
- What's the right retention period for raw API telemetry before archiving?
- Should quality scores be backfilled into the raw telemetry stream or kept in a separate stream indefinitely?

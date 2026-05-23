---
title: AI Systems Observability
domain: technical
created: 2026-05-22
reviewed: 2026-05-22
tags: [observability, monitoring, logging, metrics, AI-ops, signals]
connections: [telemetry, tracing, ai-debugging, ai-systems, evaluation]
confidence: high
source: original synthesis
---

## Definition
Observability is the property of a system that allows its internal state to be inferred from its external outputs. For AI systems specifically, observability means being able to answer: "Is the model doing what I think it's doing, for the cost I think I'm paying, at the quality level I need?" without looking at source code.

The distinction from traditional software observability: a web service is observable if you can see its errors and latency. An AI service also needs quality observability — knowing whether outputs are good, not just whether the service is up.

## Why It Matters
AI failures are silent. A service can be 100% available and producing wrong outputs continuously. Without quality observability, you learn about degradation from user complaints — the worst possible detection mechanism. Every week of undetected quality degradation is a week of users building distrust.

## The Four Signal Categories

Every AI system produces exactly four categories of observable signal. If a signal doesn't fit in one of these, it's metadata, not a primary signal.

**1. Input Signals**
What went into the model. Token counts (input, cached, cache-write). Model ID. Tier. System prompt hash (for detecting prompt changes). Retrieval sources used.

**2. Output Signals**
What came out of the model. Token counts (output). Output format (was the requested format produced?). Completion reason (stop vs. max_tokens vs. error). Response time.

**3. Cost Signals**
What it cost. Total tokens × token price per model. Cache hit rate (cached_tokens / input_tokens). Session-level cost. Workflow-level cost. Daily/weekly roll-ups.

**4. Quality Signals**
Whether the output was good. Human ratings (1-5 scale). Automated quality scores (LLM-as-judge). Format compliance (did output match the expected schema?). Downstream task success (did the output enable the next step?).

## The Minimum Viable Log Entry

Every AI call should produce a log entry with at minimum these fields:

```json
{
  "ts": "2026-05-22T09:00:00Z",
  "session_id": "abc-123",
  "model": "claude-sonnet-4-6",
  "tier": "analysis",
  "workflow": "meeting-debrief",
  "input_tokens": 2400,
  "output_tokens": 850,
  "cached_tokens": 1800,
  "cache_write_tokens": 600,
  "latency_ms": 2100,
  "status": "success",
  "completion_reason": "stop"
}
```

This workspace logs to `telemetry/api-log.jsonl`. Every field above is present in the WorkspaceClient output.

## Monitoring vs. Observability

These are different things, often confused:

**Observability** is the property of the system — the logs, traces, and metrics it emits. You build observability into a system.

**Monitoring** is the practice of watching the observable signals and alerting when they cross a threshold. You build monitoring on top of observability.

You cannot monitor what isn't observable. Most AI systems fail at observability first.

**Monitoring targets for AI:**
- Quality score < 3.5 (rolling 7-day average) → alert
- Cache hit rate < 50% on repeated workflows → alert
- p95 latency > 2× baseline → alert
- Daily cost > 120% of 30-day average → alert
- Error rate > 2% → alert

## Memory System Observability

Memory systems (like claude-mem) have their own observability surface that differs from inference observability:

**What to observe in memory systems:**
- Session count (active, pending, complete)
- Observation volume per session (are sessions capturing useful signal?)
- Retrieval hit rate (are semantic searches finding relevant memories?)
- Storage growth rate (SQLite and ChromaDB size trends)
- Worker process health (daemon uptime, restart frequency)
- Deduplication rate (how many observations are being deduplicated — high rate means redundancy in tool usage)

**Signal that memory is working:** Subsequent sessions show semantic retrieval of relevant prior observations. Signal that it's not: sessions start cold despite prior work on the same topic.

**Memory system failure modes:**
- Worker daemon crashed silently: all new observations are dropped; existing memories are still retrievable
- ChromaDB embedding sync lag: semantic search returns stale results while new observations exist in SQLite but not yet indexed
- Session ID mismatch: observations stored under wrong session; retrieval fails for the correct session

## Key Principles

- **Signal before dashboard.** Understand what signals the system produces before building any dashboard. A dashboard without a signal model is theater.
- **Quality is a first-class signal.** Latency and cost without quality is incomplete observability. A fast, cheap, wrong response is not a success.
- **Log forward, not backward.** Design your log schema for the questions you'll ask in 3 months, not the questions you're asking today.
- **Cache hit rate is a cost health metric.** A cache hit rate < 50% on a repeated workflow means you're paying twice for the same tokens.
- **Alert on degradation, not just failure.** An AI system that's 80% as good as it was last month hasn't "failed" — it's degraded. Degradation detection requires trending, not just threshold alerting.

## In Practice

This workspace's observability infrastructure:
- `telemetry/api-log.jsonl` — all API calls with full signal (WorkspaceClient logs automatically)
- `observability/quality.jsonl` — human quality ratings per prompt
- `observability/dashboard.md` — generated by `/observe` skill
- `scripts/telemetry_reader.py` — cost analysis without API calls

Run `/observe` to generate the current dashboard. Read `scripts/telemetry_reader.py` to understand how signals are aggregated.

## Connections
- [[telemetry]] — the implementation layer: JSONL schema, cost calculation, signal aggregation
- [[tracing]] — request-level traces that compose into observability
- [[ai-debugging]] — observability signals are the starting point for every debugging session
- [[evaluation]] — quality signals feed the evaluation system
- [[ai-systems]] — model tier selection is informed by observability data

## Open Questions
- At what call volume does a dedicated monitoring service pay for the overhead vs. JSONL + ad-hoc queries?
- How do you observe multi-agent workflows where multiple models contribute to a single output?

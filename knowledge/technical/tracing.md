---
title: Distributed Tracing for AI Systems
domain: technical
created: 2026-05-22
reviewed: 2026-05-22
tags: [tracing, distributed-systems, request-tracing, trace-id, spans, AI-ops]
connections: [observability, telemetry, ai-debugging, deployment-patterns]
confidence: high
source: original synthesis
---

## Definition
Tracing is the practice of recording the causal chain from a user action to a system response. In AI systems, a trace connects: user input → context assembly → model call → output processing → user-visible response. Without tracing, you can see individual telemetry events but not how they relate to each other.

The key concept: a **trace** is a tree of **spans**. Each span is one unit of work (a function call, an API request, a database query). Spans have a start time, end time, and parent span ID. Together, they reconstruct the execution path of any request.

## Why It Matters
Multi-step AI workflows — debrief pipelines, weekly reviews, retrieval-augmented generation — involve multiple model calls, file reads, and transformations. When something goes wrong, you need to know which step failed and why. Without trace IDs linking them, you have a set of independent log entries with no causal relationship. Tracing gives you the "why did this happen" that telemetry alone cannot.

## Trace Architecture for AI Systems

A minimal AI trace covers four layers:

```
Trace: meeting-debrief-20260522-abc123
│
├─ Span: context-assembly [12ms]
│   ├─ read: meeting-intelligence/raw/2026-05-22-standup.md
│   └─ read: memory/project_workspace_blueprint.md
│
├─ Span: stage-1-structure [claude-haiku, 1840ms, 2100 input / 650 output tokens]
│   └─ cached_tokens: 1800 (85% cache hit)
│
├─ Span: stage-2-intelligence [claude-sonnet, 3200ms, 3400 input / 1200 output tokens]
│   └─ cached_tokens: 1800 (53% cache hit)
│
└─ Span: output-write [8ms]
    └─ wrote: meeting-intelligence/processed/2026-05-22-standup.md
```

This trace tells you: total wall time 5060ms, total cost, cache efficiency per stage, and which stage was the bottleneck.

## Trace ID Design

A trace ID links all telemetry entries for a single end-to-end request. Design rules:

- **Globally unique:** UUID v4 or timestamp + random suffix (`20260522-abc123`)
- **Propagated through all calls:** Every span in the trace carries the same `trace_id`
- **Logged at every step:** Every telemetry entry includes `trace_id`
- **Human-readable prefix:** Include the workflow name so you can grep without knowing the ID (`debrief-20260522-abc123`)

**Span ID:** Each individual unit of work gets its own `span_id`. Spans reference their parent via `parent_span_id`. Root span has no parent.

```json
{
  "trace_id": "debrief-20260522-abc123",
  "span_id": "span-004",
  "parent_span_id": "span-000",
  "operation": "model-call-stage2",
  "model": "claude-sonnet-4-6",
  "start_ts": "2026-05-22T09:00:02.1Z",
  "duration_ms": 3200,
  "input_tokens": 3400,
  "output_tokens": 1200,
  "cached_tokens": 1800
}
```

## AI-Specific Tracing Challenges

Traditional distributed tracing (Jaeger, Zipkin, OTEL) was designed for microservices with deterministic execution. AI systems introduce three new challenges:

**1. Non-deterministic spans:** The same input can produce different outputs and different latencies. Trace comparison across runs requires sampling multiple traces of the same workflow, not just one.

**2. Context assembly as a span:** In AI systems, context assembly (which files were read, which memory loaded) is itself a meaningful span. It directly affects the model's output. Traditional tracing ignores data reads; AI tracing must include them.

**3. Quality as a span attribute:** Spans in AI traces should carry quality annotations when available. A span with `quality: fail` and `failure_class: context-failure` is diagnostically richer than a span with just timing data.

## Practical Tracing in This Workspace

The WorkspaceClient in `production-ai/claude_client.py` uses `session_id` as a lightweight trace ID. This is a practical starting point — it links calls within a session to a workflow but doesn't produce a full span tree.

**To upgrade to full tracing:**
1. Generate a `trace_id` at workflow entry (before any calls)
2. Increment a `span_id` counter for each sub-operation
3. Record `parent_span_id` when calling nested operations
4. Add trace fields to the JSONL schema

This doesn't require a tracing backend (no Jaeger needed). JSONL with trace IDs is queryable with standard tools and sufficient for single-system workloads.

## Reading a Trace

When debugging a multi-step workflow:

1. Find the `trace_id` from the user's session (grep `api-log.jsonl` for the session's timestamp range)
2. Filter all spans with that `trace_id` — sorted by `start_ts`
3. Reconstruct the span tree (match `span_id` → `parent_span_id`)
4. Identify: which span took the longest? which span had the highest token cost? which span, if any, has an error status?
5. Drill into the identified span: what were its inputs? Was context assembled correctly?

**Most common trace-level finding:** The slow span isn't where you thought. Context assembly (file reads) is often the bottleneck, not the model call.

## Key Principles

- **Trace ID at the boundary, not the leaf.** Generate the trace ID at the entry point of the user-facing workflow, not inside individual API calls. Let it propagate inward.
- **Context assembly is always a span.** If you didn't record which files were loaded and in what order, you're missing the most diagnostic span in an AI trace.
- **Sample strategically, don't trace everything.** For high-volume workflows, sample 10-20% of traces and 100% of errors. Full traces on everything is expensive and redundant.
- **Correlate trace IDs with quality scores.** When a workflow produces a low-quality output, the trace tells you which span contributed to the failure.

## Connections
- [[telemetry]] — telemetry is the data in each span; tracing is the structure connecting them
- [[observability]] — traces are one of the three pillars of observability (logs, metrics, traces)
- [[ai-debugging]] — traces are the primary tool for debugging multi-step AI failures
- [[deployment-patterns]] — tracing middleware is a standard component in AI service deployment

## Open Questions
- What's the minimum span set for a trace to be useful without being too expensive to produce?
- How do you handle traces that span multiple sessions (long-running agentic workflows)?

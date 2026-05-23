---
title: Runtime Diagnostics for AI Systems
domain: technical
created: 2026-05-22
reviewed: 2026-05-22
tags: [runtime, diagnostics, performance, latency, throughput, AI-ops, monitoring]
connections: [observability, telemetry, tracing, ai-debugging, deployment-patterns, reliability]
confidence: high
source: original synthesis
---

## Definition
Runtime diagnostics is the practice of measuring, interpreting, and acting on the operational behavior of a running AI system. Where debugging investigates a specific failure, runtime diagnostics monitors the system's ongoing health and identifies degradation trends before they become failures.

The four runtime dimensions: latency (how fast), throughput (how much), cost (how expensive), and quality (how good). All four must be monitored together — optimizing for any one in isolation often degrades the others.

## Why It Matters
Runtime degradation is gradual and silent. A system that was working well last month may be 30% slower, 20% more expensive, and producing 15% lower quality outputs today — and no individual call has "failed." Runtime diagnostics catches this accumulation before it becomes visible to users.

## The Four Runtime Dimensions

### Latency
How long individual calls take. Measured in milliseconds. Reported as p50, p95, p99 (not average — averages hide tail latency).

**Key thresholds (Claude API):**
- Haiku: p50 < 1,000ms, p95 < 3,000ms
- Sonnet: p50 < 2,000ms, p95 < 5,000ms
- Opus: p50 < 4,000ms, p95 < 10,000ms

**Latency degradation signals:**
- p95 > 2× normal baseline
- Sudden latency spike on a specific workflow (not all workflows) → likely prompt grew
- Gradual increase over weeks → likely context window growing or prompt expanding

**Diagnosing latency:**
1. Is it all models or one tier? → Tier-specific = workflow change; all tiers = API-side
2. Is it correlated with input token count? → Yes → prompt is growing
3. Is it correlated with time of day? → Yes → rate limiting or API load
4. Does it resolve on retry? → Yes → transient; No → structural

### Throughput
How many calls per unit time the system is processing. Relevant for batch workflows and high-frequency pipelines.

**Throughput floor:** API rate limits are the hard ceiling. Anthropic rate limits are per-model, per-workspace. Know your limits before designing batch workflows.

**Throughput optimization:**
- Parallelize independent calls (Haiku extraction → Sonnet analysis can overlap)
- Batch small calls (if processing many short documents, batch them)
- Cache aggressively (cached calls don't consume rate limit quota, only output quota)

**Throughput degradation signal:** Batch jobs that ran in 10 minutes now take 25. Check: did the input set grow, or is each call slower?

### Cost
How much money each call, workflow, and session costs. Measured in USD per call and per workflow invocation.

**Key cost formula:**
```
cost = (input_tokens × input_rate) 
     + (output_tokens × output_rate)
     + (cache_write_tokens × write_rate)
     - (cached_tokens × (input_rate - cached_rate))
```

**Cost optimization levers (ordered by impact):**
1. Cache system prompts: recovers 80-90% of system prompt cost after first call
2. Right-tier routing: Haiku is ~10x cheaper than Opus for equivalent tasks
3. Reduce input tokens: trim unnecessary context from prompts
4. Reduce output tokens: tighten output instructions; request shorter formats

**Cost degradation signals:**
- Workflow cost increasing without volume increase → prompt grew or caching broke
- Cache hit rate < 50% → `cache_control` misconfigured or system prompt is varying
- Opus calls for capture-tier tasks → tier routing regression

### Quality
The percentage of outputs meeting the eval rubric. The only runtime dimension that requires deliberate measurement — latency, cost, and throughput are automatic.

**Quality tracking:**
- Log all human ratings to `observability/quality.jsonl`
- Run LLM-as-judge on high-volume workflows
- Compute rolling 7-day pass rate per workflow
- Alert when pass rate drops below threshold

**Quality degradation signals:**
- Pass rate declining without any code change → model behavior drift or context staleness
- Format compliance failing after prompt update → anti-drift (prompt didn't preserve format spec)
- Factual accuracy failing on a specific document type → retrieval or context assembly issue

## Runtime Performance Review

A structured diagnostic session to assess system health across all four dimensions.

**Quick review (5 minutes, weekly):**
```
1. Check telemetry/api-log.jsonl: any errors in the last 7 days?
2. Cache hit rate: avg(cached_tokens / input_tokens) for each workflow. Any < 50%?
3. Cost: compare this week's total to last week's. Any > 20% increase without volume change?
4. Quality: check observability/quality.jsonl. Any workflow < 80% pass rate?
5. Flag: any finding that needs investigation vs. any finding that's already explained.
```

**Full review (30 minutes, monthly):**
```
1. Latency analysis: p50, p95 per workflow vs. prior month baseline
2. Cost analysis: cost per invocation by workflow, trend over 30 days
3. Cache efficiency: cache hit rate per workflow, trend over 30 days
4. Quality analysis: pass rate per workflow, dimension-level breakdown
5. Model distribution: which tiers are being used for which workflows. Any surprises?
6. Error analysis: error types, error rate, any new error codes this month
7. Actions: top 3 concrete improvements identified from the data
```

## Interpreting the Telemetry Stream

Reading `telemetry/api-log.jsonl` directly — patterns to look for:

**Finding expensive calls:**
```
# Calls with most total tokens (proxy for cost)
sort by: input_tokens + output_tokens DESC
look for: outliers that are 3-5× the typical call size
ask: why is this call so much larger than normal?
```

**Finding caching failures:**
```
# Calls with 0 cached_tokens on workflows that should cache
filter: workflow == "meeting-debrief" AND cached_tokens == 0
look for: repeated 0-cache calls on the same session_id
ask: is the system prompt stable, or is it changing between calls?
```

**Finding latency outliers:**
```
# Calls > 2× typical latency
filter: latency_ms > [2 × workflow_baseline]
look for: correlation with input_tokens
ask: did input size grow, or is the API responding slowly?
```

**Finding truncation:**
```
# Outputs cut off by max_tokens
filter: completion_reason == "max_tokens"
look for: which workflow, how frequently
ask: is the output budget set correctly for the task size?
```

## Key Principles

- **Four dimensions, not one.** Optimizing for latency alone may break cost or quality. Report all four in every performance review.
- **p95, not average.** p95 latency is what the 95th percentile of users experience. Average hides the tail. Tail latency is what degrades user trust.
- **Cost is a diagnostic signal, not just a bill.** A rising cost trend without volume increase tells you something changed — prompt grew, caching broke, tier escalated. Follow the signal.
- **Cache hit rate is the most actionable single metric.** It's easy to measure, directly controlled, and has a large cost impact. A 0% cache hit rate is always a bug.
- **Quality needs deliberate measurement.** Latency and cost are automatic from telemetry. Quality doesn't appear in the telemetry stream without deliberate eval instrumentation.

## Connections
- [[observability]] — runtime diagnostics is the operational practice built on observability infrastructure
- [[telemetry]] — telemetry is the raw data stream for all runtime dimension measurement
- [[tracing]] — trace-level analysis reveals which span in a workflow is causing latency issues
- [[ai-debugging]] — runtime diagnostics identifies where to start debugging; debugging finds the root cause
- [[reliability]] — runtime dimensions map to the SLOs defined in the reliability framework

## Open Questions
- What's the right sampling strategy for quality evals in a high-volume workflow (sample every N calls, or trigger evals on detected anomalies)?
- How do you establish p95 latency baselines for a new workflow before you have historical data?

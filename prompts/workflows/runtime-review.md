# Runtime Performance Review Prompt
## Version: v1.0

---

## Weekly Runtime Signal Check

```
Read: telemetry/api-log.jsonl (last 7 days)

For each unique workflow in the data, compute:
- Call count
- Average latency_ms and p95 latency_ms (sort all calls by latency; p95 = 95th percentile)
- Total cost estimate: sum of cost_usd field (or compute from token counts)
- Cache hit rate: average(cached_tokens / input_tokens) for calls where cached_tokens > 0
- Error rate: count(status != "success") / total count
- Truncation count: count(completion_reason == "max_tokens")

Flag any of:
- p95 latency > 5,000ms (Sonnet) or > 10,000ms (Opus)
- Cache hit rate < 50% on any workflow that runs repeatedly
- Error rate > 2%
- Any truncations

Output as a table: Workflow | Calls | p95 Latency | Cache Hit Rate | Cost | Errors | Flags
Then: one sentence on the most important finding.
```

---

## Cache Efficiency Diagnostic

```
Read: telemetry/api-log.jsonl

I need to diagnose cache efficiency for [workflow name].

For all calls where workflow == "[workflow name]":
1. Compute: cached_tokens for each call
2. Identify calls with cached_tokens == 0 (cache misses)
3. For cache misses: are they clustered (time gap between calls?) or random?
4. For cache hits: what's the average hit rate?

Diagnosis:
- If all calls have cached_tokens == 0: cache_control is not configured
- If misses are time-clustered: calls are spaced > 5 min (cache TTL expired)
- If misses are random: system prompt may be varying between calls

Recommend the specific fix for the identified cause.
Report: cache hit rate, miss pattern, diagnosis, fix.
```

---

## Cost Trend Analysis

```
Read: telemetry/api-log.jsonl

Compute the cost trend for the last 30 days.

For each workflow:
1. Group calls by week (ts field, first 7 chars after date)
2. Compute weekly total cost
3. Compute weekly cost per invocation (total cost / call count)
4. Identify trend: is cost per invocation stable, increasing, or decreasing?

Flag: any workflow where cost per invocation increased > 20% week-over-week.

For flagged workflows, identify the most likely cause:
- Input token count increasing? (prompt or context grew)
- Cache hit rate decreasing? (caching broke)
- Model tier escalated? (tier routing changed)
- Call count decreased without cost decreasing? (per-call cost rose)

Output: trend table per workflow + specific finding for any flagged workflows.
```

---

## Latency Regression Analysis

```
Read: telemetry/api-log.jsonl

I'm investigating a latency regression for [workflow name].

Steps:
1. Filter calls for workflow == "[workflow name]"
2. Sort by ts (timestamp)
3. Compute rolling p95 latency by week
4. Find: when did latency first increase?
5. Find: what changed in the telemetry at that time?
   - Did input_tokens increase? (context grew)
   - Did the model change?
   - Did the call pattern change (time between calls)?

Provide:
- Latency trend (week by week p95)
- Identified inflection point
- Most likely cause
- One specific remediation

If the telemetry alone doesn't isolate the cause:
  State: "Telemetry shows X; to confirm cause, run [specific isolation test]."
```

---

## Model Health Check

```
Read: telemetry/api-log.jsonl (last 30 days)

Current valid model IDs (as of 2026-05-22):
- claude-haiku-4-5-20251001 (capture tier)
- claude-sonnet-4-6 (analysis tier)  
- claude-opus-4-7 (strategy tier)

Check:
1. Are all model IDs in the telemetry matching the current valid list?
2. Are any model IDs present that are not in the valid list? (retired models)
3. Model distribution: what percentage of calls use each tier?
4. Tier appropriateness: are any workflows using the wrong tier?
   - Capture tasks (extraction, formatting) on Sonnet or Opus = over-tiered
   - Analysis tasks (synthesis, reasoning) on Haiku = under-tiered

Output: model distribution table + any anomalies + tier mismatch findings.
```

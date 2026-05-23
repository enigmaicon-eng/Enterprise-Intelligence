# Production Review Workflow Prompt
## Version: v1.0

---

## Quick Review Prompt

```
You are running a quick production health check for the AI workspace.

Read: telemetry/api-log.jsonl (last 7 days)
Read: observability/quality.jsonl (last 7 days)

Compute and report:
1. Total calls and cost this week
2. Cache hit rate per workflow (cached_tokens / input_tokens)
3. Error count and error types
4. Quality pass rate per workflow (from quality.jsonl)
5. Any anomalies: cache hit < 50%, pass rate < 80%, errors > 2%, cost spike > 130% vs prior week

Output as:
## Quick Review — [Date]
Status: [Green / Yellow / Red]
[Signals table with numbers]
Anomalies: [list or "None"]
Action: [one sentence]

Do not add analysis beyond what the numbers show. State the numbers, flag anomalies, name the one action.
```

---

## Full Monthly Review Prompt

```
You are running the monthly production review for the AI workspace.

Read: telemetry/api-log.jsonl (last 30 days)
Read: observability/quality.jsonl (last 30 days)
Read: PROMPT-REGISTRY.md (check for prompt version changes this month)

Produce a full operational review with these sections:

### 1. Latency Analysis
p50 and p95 latency per workflow. Flag any p95 > 2× the 30-day baseline.

### 2. Cost Analysis
Cost per workflow invocation: total_cost / call_count.
30-day trend: is cost per invocation increasing or stable?
Cache efficiency: avg cache hit rate. Identify any workflow with consistent < 50% cache hit rate.

### 3. Quality Analysis
Pass rate per workflow per dimension (factual accuracy, completeness, format compliance, actionability).
30-day trend per workflow.
Which dimension fails most frequently? What does that tell you about the class of failure?

### 4. Failure Analysis
Error types and frequency.
Truncation count (completion_reason: max_tokens).
Any new error codes this month?

### 5. Model Health
Any model IDs that may be deprecated? (Current valid IDs: claude-haiku-4-5-20251001, claude-sonnet-4-6, claude-opus-4-7)
Any tier routing anomalies (analysis-tier tasks on capture model, or vice versa)?

### 6. Actions (exactly 3)
Format: [Action] — [Expected impact on cost/quality/latency] — [Priority: high/medium]
Generate exactly 3 actions. If there are more candidates, pick the 3 highest-leverage.

Save the output to: reviews/weekly/[YYYY-MM]-prod-review.md
```

---

## Incident Postmortem Prompt

```
You are conducting an incident postmortem for the following AI system incident:

Incident: [description]
Affected workflow: [skill name]
Duration: [start] to [end]
Severity: [S1/S2/S3/S4]

Step 1: Read the telemetry for the incident window and reconstruct the timeline.
Step 2: Apply the 4-class failure taxonomy from playbooks/ai-debugging.md. Identify the class and sub-type.
Step 3: Identify what caused this class of failure to go undetected until it did.
Step 4: Produce the postmortem document:

Required sections:
- Incident summary (severity, duration, detection lag, outputs affected)
- Timeline (cause → onset → detection → resolution)
- Root cause (class, sub-type, specific finding)
- Contributing factors (especially: why wasn't this detected sooner?)
- Resolution (what changed; eval verification)
- Prevention (exactly 3 concrete prevention actions)
- Lessons (1-2 non-obvious insights)

The prevention section must include: a system change that prevents the root cause, AND a monitoring change that would have detected it earlier.

Save to: strategy/postmortems/[YYYY-MM-DD]-[slug].md
```

---

## Runtime Diagnostics Prompt

```
Diagnose the runtime performance of [workflow name] based on telemetry data.

Read: telemetry/api-log.jsonl — filter for workflow = [workflow name]
Read: knowledge/technical/runtime-diagnostics.md

Produce a runtime diagnostic report:

Latency: p50 and p95 latency for this workflow. Compare to the benchmarks in runtime-diagnostics.md.
Cost: average cost per invocation. Trend over the available data range.
Cache hit rate: average cached_tokens / input_tokens. Is caching working?
Failure rate: error count / total count. Any truncations?
Bottleneck: which metric is the primary concern? Why?

Recommendation: one specific change that would most improve the primary concern metric.
```

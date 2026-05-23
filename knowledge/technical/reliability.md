---
title: Reliability Thinking for AI Systems
domain: technical
created: 2026-05-22
reviewed: 2026-05-22
tags: [reliability, SLO, failure-modes, graceful-degradation, circuit-breaker, AI-ops]
connections: [observability, ai-debugging, deployment-patterns, evaluation, telemetry]
confidence: high
source: original synthesis
---

## Definition
Reliability for AI systems means the system consistently produces outputs that meet defined quality and availability standards. This extends traditional reliability (uptime, latency SLOs) to include quality SLOs — commitments about the quality of AI outputs, not just whether the service is running.

A service that's 100% available and producing 40% wrong answers is not reliable. Traditional reliability frameworks miss this entirely.

## Why It Matters
Users trust AI systems that behave consistently. Inconsistency — in format, quality, or behavior — erodes trust faster than outages. An outage is visible and recoverable. Inconsistent quality is invisible and compounds: users stop relying on the system, stop reporting issues, and eventually work around it.

The unique reliability challenge of AI: failure modes are qualitative, not binary. There's no exception stack trace for "the model hallucinated a fact." Detecting and measuring qualitative failures requires a different approach than traditional service reliability.

## AI-Specific SLOs

Traditional SLOs measure availability and latency. AI systems need three additional SLO dimensions:

**1. Quality SLO:** The percentage of outputs that pass the 4-dimension eval rubric.
- Example: "≥85% of /debrief outputs pass all 4 evaluation dimensions per rolling 7-day period"
- Measurement: `observability/quality.jsonl` quality score tracking
- Alert threshold: Rolling 7-day pass rate drops below 85%

**2. Accuracy SLO:** The percentage of factual claims that are correct.
- Example: "Zero hallucinated facts in outputs derived from provided source material"
- Measurement: Spot-check reviews; LLM-as-judge factual accuracy dimension
- Alert threshold: Any detected hallucination in a high-stakes output

**3. Consistency SLO:** The same input produces outputs in the same format.
- Example: "Format compliance: 95% of outputs follow the specified output schema"
- Measurement: Format compliance dimension in evals
- Alert threshold: Format compliance rate drops below 90% for any skill

**4. Coverage SLO:** The percentage of required scope that's addressed.
- Example: "All /exec-plan outputs contain all 6 required sections"
- Measurement: Completeness dimension in evals
- Alert threshold: Completeness rate drops below 95%

## The AI Failure Mode Taxonomy

Every AI output failure maps to one of these categories:

| Failure Type | Description | Severity | Detection |
|-------------|-------------|----------|----------|
| **Wrong** | Factually incorrect content | Critical | Factual accuracy eval |
| **Incomplete** | Missing required sections or scope | High | Completeness eval |
| **Hallucinated** | Content not grounded in provided context | Critical | Source grounding check |
| **Off-format** | Output doesn't match expected schema | Medium | Format compliance eval |
| **Superficial** | Syntactically complete but semantically shallow | High | Manual review or LLM-judge |
| **Inconsistent** | Same input produces different outputs across runs | Medium | Multi-run comparison |
| **Overconfident** | Claims certainty where uncertainty should be stated | High | Manual review |
| **Truncated** | Output cut off at max_tokens limit | Medium | `completion_reason` check in telemetry |

**Severity guidelines:**
- Critical: Decision made on wrong output could cause real harm
- High: Output requires significant rework before it can be used
- Medium: Output requires minor correction; still usable with review

## Graceful Degradation

When an AI system can't deliver full quality, it should degrade gracefully rather than fail silently or produce output that appears complete but isn't.

**Degradation ladder (most graceful first):**

```
Level 1 — Full output (normal operation)
Level 2 — Partial output with explicit gap marking
  e.g., "Action items not extracted — source material didn't contain explicit actions"
Level 3 — Summary only (when full analysis isn't possible)
  e.g., "Providing key points only; detailed analysis requires additional context"
Level 4 — Failure with routing
  e.g., "Cannot complete this task; insufficient context. Required: [X]. Available: [Y]."
Level 5 — Explicit refusal (when producing any output would be misleading)
  e.g., "Cannot produce factual output on this topic without source material."
```

**Anti-pattern:** Silent degradation. An output that looks complete but is actually partial or wrong is worse than an explicit failure. The user acts on it without knowing it's bad.

In claude-mem's architecture, graceful degradation is implemented in `hook-command.ts`:
- Transport errors → exit 0 (never block the user's Claude Code session)
- Client bugs → exit 2 (blocking, needs fix)

This is the right model: infrastructure failures are non-blocking; correctness bugs are blocking.

## Circuit Breaker Pattern for AI

A circuit breaker prevents a system from continuously attempting a failing operation. For AI services:

```
State: CLOSED (normal)
  → All requests flow through
  → Track failure rate over rolling window (e.g., last 100 calls)
  → If failure rate > threshold (e.g., 10%): transition to OPEN

State: OPEN (circuit tripped)
  → All requests fail fast with clear error message
  → No calls made to the model API
  → After cooldown period (e.g., 30s): transition to HALF-OPEN

State: HALF-OPEN (testing recovery)
  → Allow one request through
  → If successful: transition back to CLOSED
  → If failed: transition back to OPEN
```

**AI-specific failure definition for circuit breakers:**
Include quality failures, not just errors:
- HTTP errors (4xx, 5xx)
- Timeout
- Empty response
- `completion_reason: max_tokens` (truncated)
- LLM-as-judge quality score < threshold (if evaluating in real-time)

## Retry Logic for AI Calls

Not all failures are retryable. Retrying a prompt failure produces the same wrong output faster.

| Failure Type | Retryable? | Retry Strategy |
|-------------|-----------|----------------|
| HTTP 429 (rate limit) | Yes | Exponential backoff: 1s, 2s, 4s |
| HTTP 5xx (server error) | Yes (max 3 times) | Fixed delay: 2s |
| HTTP 4xx (client error) | No | Fix the request |
| Timeout | Yes (once) | Double the timeout on retry |
| Empty response | Yes (once) | Retry immediately |
| Wrong output format | No | Fix the prompt |
| Truncated output | No | Reduce input or increase max_tokens |

**Rule:** Retrying prompt and context failures wastes money and time. Retrying infrastructure failures is correct. Classify first; retry only when appropriate.

## Key Principles

- **Quality is an SLO, not a sentiment.** "The outputs seem pretty good" is not a reliability measurement. "87% of outputs pass the eval rubric over the last 7 days" is.
- **Silence is not success.** An AI system that produces wrong outputs without raising errors is not working — it's failing silently. Build quality detection into the system, not into post-hoc user complaints.
- **Degrade explicitly, never silently.** If the system can't produce the full output, say so precisely: what's missing, why, and what's needed to complete it.
- **Retry infrastructure, not logic.** Rate limits and server errors should be retried. Prompt failures and context failures should be debugged, not retried.
- **Design for the failure mode you'll actually hit.** Context failures (wrong information loaded) and prompt failures (ambiguous instructions) are the most common AI failure modes. Rate limits and server errors are the most common infrastructure failure modes. Plan for these specifically.

## Connections
- [[observability]] — quality SLOs require quality signals from the observability system
- [[ai-debugging]] — failure mode taxonomy is the foundation for the debugging protocol
- [[deployment-patterns]] — circuit breakers and retry logic are implemented in the service layer
- [[evaluation]] — eval pass rate is the primary quality SLO measurement
- [[telemetry]] — `completion_reason` and error codes in telemetry reveal infrastructure failures

## Open Questions
- What's the right quality SLO threshold for each skill tier (quick capture vs. strategic analysis)?
- How do you set a quality SLO for a novel workflow before you have baseline data?

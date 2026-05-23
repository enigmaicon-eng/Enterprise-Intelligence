---
title: AI Systems Debugging
domain: technical
created: 2026-05-22
reviewed: 2026-05-22
tags: [debugging, AI-ops, prompt-failure, context-failure, tracing, failure-analysis]
connections: [observability, telemetry, tracing, evaluation, reliability, context-engineering]
confidence: high
source: original synthesis
---

## Definition
AI debugging is the practice of systematically identifying why an AI system produced wrong, incomplete, or off-format output. It differs from traditional software debugging because AI failures are often not errors — the system runs to completion and produces output that looks plausible but isn't correct.

The fundamental challenge: without a systematic protocol, AI debugging defaults to prompt tweaking — changing instructions until the output improves. This is slow, expensive, and produces fragile fixes that break in new contexts. Systematic debugging identifies the root cause and fixes it once.

## Why It Matters
Every AI system failure has exactly one root cause from a set of four. Finding it takes 5 minutes with the right protocol. Finding it by trial and error takes hours. Debugging fluency is the highest-leverage skill for anyone who operates AI systems.

## The Four Failure Classes

**Always start by classifying the failure before debugging.** The wrong classification wastes the entire session.

### Class 1: Prompt Failure
The instruction is wrong — ambiguous scope, missing constraints, conflicting directions, or wrong output format specified.

**Detection signals:**
- Output has wrong structure (e.g., prose when JSON was requested)
- Output scope is wrong (too narrow: misses required sections; too broad: adds unrequested content)
- Output is internally consistent but doesn't match the task
- Multiple runs of the same prompt produce wildly different formats

**Minimum viable isolation test:**
Run the prompt with minimal, known-good context. If the failure persists with simple context, the problem is the prompt, not the context.

**Root causes (4 sub-types):**
- Scope: prompt doesn't specify what to include / exclude
- Format: prompt doesn't specify output structure precisely enough
- Instruction: prompt contains ambiguous or contradictory instructions
- Ambiguity: prompt can be read multiple ways; model picks the wrong reading

### Class 2: Context Failure
The wrong information was provided to the model, or required information was missing.

**Detection signals:**
- Output is factually wrong in ways that could be corrected by reading the right source
- Output contradicts information that was available but not loaded
- Output is correct for old state but wrong for current state (stale context)
- Model "doesn't know" something it should if context were assembled correctly

**Minimum viable isolation test:**
Add the missing context directly to the prompt (inline, not by reference). If the failure resolves, the problem is context assembly, not the prompt.

**Root causes:**
- Missing retrieval: required file wasn't loaded; index wasn't checked first
- Stale memory: loaded a memory file that's no longer current
- Wrong retrieval mode: used grep when direct read was needed, or vice versa
- Over-retrieval: loaded too much context; relevant content diluted by irrelevant content

### Class 3: Model Failure
The selected model doesn't have the capability for the task — typically a tier mismatch.

**Detection signals:**
- Output is syntactically correct and correctly formatted but semantically shallow
- Output misses non-obvious connections that the source material contains
- Multiple strategies/options are listed but none are evaluated or recommended
- "It depends" responses when the evidence supports a clear answer

**Minimum viable isolation test:**
Run the exact same prompt on a higher-tier model. If quality improves substantially, the problem is model selection, not the prompt or context.

**Root causes:**
- Tier too low for task complexity (analysis-tier task sent to capture tier)
- Task requires extended thinking but it wasn't enabled
- Model retired or degraded without updated model ID

### Class 4: Infrastructure Failure
Latency, rate limits, token budget exhaustion, connection errors.

**Detection signals:**
- Empty or truncated responses
- HTTP 429 (rate limit) or 5xx errors in logs
- Latency spikes (3× normal latency)
- `completion_reason: max_tokens` when output appears truncated
- Inconsistent behavior across identical calls (flaky behavior = infra)

**Minimum viable isolation test:**
Check `telemetry/api-log.jsonl` for error codes, latency outliers, and `completion_reason`. Infrastructure failures leave evidence in telemetry; prompt and context failures don't.

## The Systematic Debugging Protocol

```
Step 1 — Classify (2 min)
  Read the output. Apply the detection signals above.
  Pick the most likely class. Write it down.
  "This looks like a [Class X] failure because [detection signal]."
  
Step 2 — Check telemetry first (3 min)
  Read the relevant entries from telemetry/api-log.jsonl.
  Check: error codes, latency, completion_reason, cached_tokens.
  If telemetry shows errors → Class 4. Debug infrastructure.
  If telemetry shows clean calls → Classes 1-3. Debug prompt/context/model.

Step 3 — Isolate the variable (5 min)
  Run the minimum viable isolation test for your suspected class.
  If the failure resolves: you've confirmed the class.
  If the failure persists: re-classify. You misidentified the class.

Step 4 — Find the root cause (10 min)
  Within the confirmed class, identify the specific sub-type.
  For Class 1: Read the prompt carefully. What's ambiguous? What's missing?
  For Class 2: Trace the context assembly. What was loaded? What wasn't?
  For Class 3: Check the tier. What does the task require vs. what the tier provides?
  For Class 4: Read the error logs. What's the specific failure (429, timeout, truncation)?

Step 5 — Fix and verify (5 min)
  Apply the minimum fix that addresses the root cause.
  Re-run the original failing case.
  If fixed: log the finding. Update the relevant skill/prompt if needed.
  If not fixed: you've fixed a symptom, not the cause. Return to Step 1 and re-classify.

Step 6 — Prevent recurrence (5 min)
  For Class 1: Add the missing constraint to the prompt. Bump version.
  For Class 2: Update the retrieval protocol in the skill. Add hygiene check.
  For Class 3: Update model tier routing for this task type.
  For Class 4: Add retry logic, rate limit handling, or budget increase.
```

## AI-Specific Debugging Mental Models

**"Don't start with the prompt."** Prompt tweaking is the default debugging move and usually the wrong one. Check telemetry first. Context second. Model third. Prompt fourth. Most prompt "fixes" are actually context fixes in disguise.

**"Minimum viable reproduction first."** Before debugging, find the smallest input that still produces the failure. Can you reproduce it with a single sentence? With a known-good document? If you can't reproduce it, you can't verify the fix.

**"One variable at a time."** When debugging, change exactly one thing per test. Changing the prompt and the context simultaneously means you can't know which change fixed it.

**"Outputs that look good can still be wrong."** The most dangerous AI failure is a confident, well-formatted, plausible-sounding wrong answer. Don't evaluate quality by how the output looks — evaluate it against the source material.

**"The first fix is usually too local."** Fixing a single prompt instance when there's a systemic problem (wrong retrieval protocol, tier mismatch in all similar tasks) produces temporary relief, not lasting improvement.

## Multi-Step Workflow Debugging

For workflows with multiple model calls (debrief pipeline, weekly review), debugging requires identifying which step failed:

1. Read the trace (or reconstruct from session_id in telemetry)
2. Find the first span where output quality degrades
3. That span is the locus of the failure
4. Debug that span in isolation: what were its inputs? Apply the 4-class taxonomy to it.

**Rule:** In a pipeline failure, the first degraded output is the bug. Everything after it is downstream noise.

## Memory System Debugging

Memory system failures (claude-mem or file-based memory) present as context failures but have their own diagnosis:

- **Session not resumed:** Check worker status (`ps aux | grep claude-mem`). If daemon is down, memories aren't being persisted or retrieved.
- **Old memories returned:** ChromaDB sync lag. Wait 30s and retry, or check chroma sync status.
- **No memories found for a known topic:** Deduplication may have suppressed the observation. Check `content_hash` collisions in `observations` table.
- **Session ID confusion:** `contentSessionId` ≠ `memorySessionId`. Check the SessionStore conversion logic.

## Connections
- [[observability]] — observability signals are the starting point for every debugging session
- [[telemetry]] — telemetry shows which failure class is NOT infrastructure
- [[tracing]] — traces identify which span in a multi-step workflow is the failure point
- [[evaluation]] — eval failures trigger debugging sessions and confirm when they're resolved
- [[reliability]] — failure mode analysis is the preventive version of debugging
- [[context-engineering]] — context failures are a subset of the AI debugging taxonomy

## Open Questions
- At what output volume does automated failure classification (using LLM-as-judge to classify failure type) become cost-effective vs. manual classification?
- How do you debug failures that only appear in production and can't be reproduced in isolation?

---
title: AI Operational Maturity Framework
domain: operations
created: 2026-05-22
reviewed: 2026-05-22
tags: [operational-maturity, AI-ops, production-readiness, observability, evaluation, reliability]
connections: [observability, evaluation, reliability, ai-debugging, telemetry, runtime-diagnostics]
confidence: high
source: original synthesis
---

## Definition
AI operational maturity is the degree to which an organization or practitioner can reliably build, run, and improve AI systems over time. It progresses through five levels, from basic instrumentation through self-improving systems. Most teams are stuck at Level 1 or 2 — they have AI systems running, but they can't measure quality, detect degradation, or improve systematically.

This framework is assessment-oriented: it gives a current score and an advancement path, not a checklist to complete.

## The Five Maturity Levels

### Level 1 — Instrumented
**What it looks like:** API calls are logged with basic metadata. Cost is tracked. Errors are visible.

**Capability:** Can answer: "Is the service up? How much did it cost?"

**Cannot answer:** "Are outputs good? Are they getting better or worse?"

**Indicators:**
- `telemetry/api-log.jsonl` exists and is populated on every call
- Token counts and latency are in the log
- Error codes are captured
- Cost can be calculated from the log

**Gap to Level 2:** No quality measurement. No structured evaluation. No baseline to compare against.

---

### Level 2 — Observable
**What it looks like:** Quality signals are collected alongside telemetry. Human ratings exist. A dashboard shows system health.

**Capability:** Can answer: "Is the service up? How much did it cost? Are outputs generally good?"

**Cannot answer:** "Is quality improving or declining? Which specific workflows have problems?"

**Indicators:**
- `observability/quality.jsonl` exists with human ratings
- `/observe` produces a dashboard with cost, cache hit rate, and quality signal
- Quality is tracked per-workflow, not just in aggregate
- Cache hit rate is visible and monitored

**Gap to Level 3:** No systematic evaluation. No eval protocol. No regression detection. Quality is measured retrospectively, not as a gate.

---

### Level 3 — Evaluated
**What it looks like:** Every workflow has an eval rubric. Quality is measured systematically. Regression detection exists. Prompt changes require before/after evals.

**Capability:** Can answer: "Which workflows are working well? Did a recent change improve or degrade quality? What's the current quality trend?"

**Cannot answer:** "What will break before it breaks? What are the systemic failure patterns?"

**Indicators:**
- `/eval` skill exists and is used on new outputs
- `observability/quality.jsonl` has systematic LLM-as-judge or human evals
- Prompt changes go through before/after eval comparison
- Rolling 7-day quality pass rate is tracked per workflow
- PROMPT-REGISTRY.md shows quality scores and trends

**Gap to Level 4:** Can measure and detect problems, but can't prevent or rapidly resolve them. Debugging is still ad-hoc.

---

### Level 4 — Reliable
**What it looks like:** Failure modes are documented. Debugging is systematic (playbook-driven). Incident response is practiced. The system degrades gracefully rather than silently.

**Capability:** Can answer: "Why did this fail? How do I fix it? What prevents recurrence?"

**Cannot answer:** "How do I make the system continuously better without human intervention?"

**Indicators:**
- `playbooks/ai-debugging.md` exists and is used on real failures
- Incident postmortems produce prevention actions, not just RCAs
- Graceful degradation is implemented (explicit failure messages, not silent wrong outputs)
- Monthly production review runs and produces concrete improvements
- Retry logic and circuit breakers are implemented for infrastructure failures

**Gap to Level 5:** Improvement is human-driven. Every quality improvement requires a human to notice, diagnose, and fix. No automated quality improvement loop.

---

### Level 5 — Self-Improving
**What it looks like:** Eval results feed back into prompt optimization. Quality trends trigger automatic investigation. The system identifies its own failure patterns and surfaces them for review.

**Capability:** Can answer: "What's improving, what's degrading, and what should I focus on next — without being asked?"

**Indicators:**
- Quality score trends automatically trigger review flags
- LLM-as-judge results are systematically analyzed for patterns
- Prompt version history shows continuous improvement from eval feedback
- Monthly review produces measurable quality improvement each cycle
- Failure mode patterns are analyzed across incidents, not just per-incident

**This is the target state.** Most teams never reach Level 5 because they confuse Level 3 (evaluation) with being "done." Level 5 is where compound improvement begins.

---

## Scoring This Workspace

Score each dimension 0 (not started), 1 (partial), or 2 (complete):

| Dimension | Score | Evidence |
|-----------|-------|---------|
| Basic telemetry (L1) | | Does `telemetry/api-log.jsonl` have all required fields? |
| Cost attribution (L1) | | Can you produce a cost-per-workflow breakdown from the log? |
| Quality logging (L2) | | Does `observability/quality.jsonl` have entries? |
| Dashboard generation (L2) | | Does `/observe` produce a current dashboard? |
| Cache monitoring (L2) | | Is cache hit rate tracked per workflow? |
| Eval rubric exists (L3) | | Does `/eval` have a 4-dimension rubric? |
| Regression detection (L3) | | Are prompt changes preceded by evals? |
| Debugging playbook (L4) | | Does `playbooks/ai-debugging.md` exist and get used? |
| Incident postmortems (L4) | | Has at least one incident postmortem been completed? |
| Monthly review (L4) | | Has `/prod-review` been run at least once? |
| Automated quality flags (L5) | | Do quality trends trigger investigation? |
| Self-improvement loop (L5) | | Are evals systematically feeding prompt improvements? |

**Score interpretation:**
- 0-6: Level 1-2 — Build observability and evaluation first
- 7-14: Level 2-3 — Build evaluation discipline and debugging capability
- 15-18: Level 3-4 — Build reliability practices and systematic improvement
- 19-22: Level 4-5 — Build the self-improvement loop
- 23-24: Level 5 — Maintain and compound

## Advancement Actions

**To advance from Level 1 → 2:**
1. Add quality rating to first 10 outputs from your most-used workflow
2. Run `/observe` and interpret the dashboard
3. Establish cache hit rate baseline for each workflow

**To advance from Level 2 → 3:**
1. Write the 4-dimension eval rubric for your top 3 workflows
2. Run `/eval` on the last 5 outputs of each and establish baseline
3. Commit to eval before/after on the next prompt change

**To advance from Level 3 → 4:**
1. Read `playbooks/ai-debugging.md` and apply it to the next failure you encounter
2. Complete the first monthly production review with `/prod-review`
3. Write a postmortem for the most recent quality issue, including a prevention action

**To advance from Level 4 → 5:**
1. Build quality trend alerting (flag when 7-day pass rate drops 10+ percentage points)
2. Complete 3 consecutive monthly reviews that each produce measurable quality improvement
3. Establish the prompt improvement cycle: eval → gap analysis → prompt revision → re-eval

## Connections
- [[observability]] — L2 requires observability infrastructure
- [[evaluation]] — L3 requires systematic evaluation workflows
- [[reliability]] — L4 requires reliability practices (graceful degradation, circuit breakers)
- [[ai-debugging]] — L4 requires debugging playbooks and incident response
- [[runtime-diagnostics]] — L4-5 require runtime diagnostic capability

## Open Questions
- What's the right cadence for maturity self-assessment — quarterly or annually?
- Can the self-improvement loop (Level 5) be automated without human oversight, or does it always require human judgment on the prompt revision step?

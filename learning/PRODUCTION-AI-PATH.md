# Production AI Learning Path
## Structured Sequence for Operational Fluency

This path moves from signal literacy through debugging fluency to operational maturity. Each level has observable completion criteria — you don't advance by reading, you advance by doing.

**Anti-pattern to avoid:** Reading all 5 levels before doing anything in Level 1. Fluency is built through application, not accumulation.

---

## Level 1 — Signal Literacy

**What you're building:** The ability to describe what signals an AI system produces and what each signal tells you.

**Mental models to internalize:**
- An AI system produces exactly 4 categories of signal: input signals (tokens sent), output signals (tokens received), latency signals (time), and quality signals (output correctness). Anything not in one of these four is metadata.
- A log entry that doesn't have a timestamp, model ID, and token counts is missing the minimum viable signal.
- "The AI is slow" is not a signal. "p95 latency is 4.2s vs. 2.1s last week on the analysis tier" is a signal.

**Learning activities (do these, don't just read):**

1. Read `telemetry/api-log.jsonl` in this workspace. Find: the most expensive call (by total tokens), the slowest call (by latency), and any call with 0 cache tokens on a repeated system prompt.

2. Read `~/.claude/skills/claude-mem/docs/architecture-overview.md`. Identify: which component is responsible for telemetry, what tables hold observation data, and how the system handles transport errors.

3. Read `knowledge/technical/telemetry.md`. Write 3 sentences describing what your current workspace logs and what it's missing.

4. Check `observability/dashboard.md` if it exists. What quality score is reported? What's the trend?

**Completion criteria:** You can look at a JSONL log entry and immediately identify: which model, which tier, total cost estimate, cache hit (yes/no), and whether latency was anomalous.

---

## Level 2 — Infrastructure Fluency

**What you're building:** The ability to read a service's architecture diagram and trace a request through it end-to-end.

**Mental models to internalize:**
- Every AI service has three layers: the inference layer (calls the model API), the memory layer (stores context and history), and the routing layer (decides which model and context to use). Understand which layer you're in before debugging.
- Docker makes AI environments reproducible. If it works in the container and fails outside, the bug is the environment. If it fails inside, the bug is the code.
- FastAPI's dependency injection is how you thread database connections, auth, and config through a service without passing them as function arguments.

**Learning activities:**

1. Read `production-ai/claude_client.py`. Trace one call through the code: where does it pick the model? where does it apply cache_control? where does it log?

2. Read `~/.claude/skills/claude-mem/docker/claude-mem/Dockerfile`. Identify: what's the base image, what's installed, what's the entrypoint. What would fail if you removed the Bun installation step?

3. Read `knowledge/technical/deployment-patterns.md`. Sketch (on paper or in a note) the 3-layer architecture for claude-mem: which component is each layer?

4. Read `~/.claude/skills/claude-mem/docs/SESSION_ID_ARCHITECTURE.md`. Explain in 2 sentences why there are two session ID types and what breaks if they're confused.

**Completion criteria:** Given an architecture diagram of a new AI service, you can identify the inference/memory/routing layers, trace a request through them, and predict where failure would be most likely.

---

## Level 3 — Evaluation Fluency

**What you're building:** The ability to design and run an eval for any AI workflow, and interpret the results to make decisions.

**Mental models to internalize:**
- An eval is a test that measures AI behavior, not code correctness. A unit test checks if a function returns the right value. An eval checks if the model's output is useful.
- LLM-as-judge is only as reliable as the rubric it uses. A vague rubric produces vague scores. A rubric with 4 explicit criteria and binary ratings produces actionable scores.
- Regression detection requires a baseline. You can't know if quality degraded if you didn't measure quality before.

**Learning activities:**

1. Read `knowledge/technical/evaluation.md`. Identify the 4 rubric dimensions this workspace uses. Write a 5th that would apply to strategic analysis outputs.

2. Check `observability/quality.jsonl` if it exists. What prompts have been rated? What's the lowest-scoring prompt? What would you change about it?

3. Run `/eval` on a recent `/debrief` output. Apply the eval rubric manually. Did the output pass all 4 criteria?

4. Design an eval for the `/briefing` skill: what are 3 binary criteria that would indicate a high-quality briefing output? What would constitute failure on each?

**Completion criteria:** You can design a 4-criteria rubric for any AI workflow in this workspace, run an eval manually, and give a pass/fail verdict with specific evidence.

---

## Level 4 — Debugging Fluency

**What you're building:** The ability to diagnose any AI system failure in under 30 minutes using the systematic protocol.

**Mental models to internalize:**
- Debugging order matters: prompt → context → model → infra. Don't skip steps. A prompt failure looks identical to a model failure until you isolate the variable.
- Minimum viable reproduction: the smallest input that still produces the failure. If you can't reproduce it, you can't debug it. If you can reproduce it, you're already most of the way to the fix.
- AI failures are often not errors — they're wrong outputs. "No exception was raised" doesn't mean the system worked.

**Learning activities:**

1. Read `playbooks/ai-debugging.md`. Memorize the 4 failure classes and their detection signals.

2. Read `playbooks/prompt-failure-analysis.md`. Apply the prompt failure analysis protocol to a skill that you suspect produces inconsistent output. Document what you find.

3. Pick a skill in this workspace and intentionally break its prompt (remove a key instruction). Run it. Apply the debugging protocol to identify the root cause. This is muscle memory — the point is the process, not the finding.

4. Read `~/.claude/skills/claude-mem/.claude/commands/anti-pattern-czar.md`. What anti-patterns does it catch? How does its detection methodology compare to this workspace's anti-pattern catalog?

**Completion criteria:** Given a failing AI output (wrong format, incomplete content, hallucinated structure), you can identify the failure class and root cause in under 30 minutes using the playbook.

---

## Level 5 — Operational Maturity

**What you're building:** The ability to run an AI system over time, improve it systematically, and respond to incidents effectively.

**Mental models to internalize:**
- Production AI is never "done." Quality degrades, prompts drift, context grows stale. Operational maturity means having systems to detect degradation before users report it.
- An incident postmortem's value is in the prevention, not the RCA. If a postmortem produces only a description of what happened, it failed. If it produces a change that prevents recurrence, it succeeded.
- AI operational maturity progresses through 5 levels: instrumented → observable → evaluated → reliable → self-improving. Most teams are stuck at Level 1 or 2.

**Learning activities:**

1. Run `/prod-review quick`. What does the report tell you? What's the most important signal?

2. Read `knowledge/operations/ai-operational-maturity.md`. Score this workspace on each dimension. Identify the lowest-scoring dimension and the one concrete action that would advance it.

3. Read `playbooks/incident-response.md`. Simulate a hypothetical incident (e.g., "the /debrief skill has been producing incomplete outputs for 3 days without anyone noticing"). Walk through the incident response protocol. What would you do first? What would the postmortem look like?

4. Run `/prod-review full` at the end of a month. Compare quality scores and cost to the previous month. Identify one concrete improvement to make based on the data.

**Completion criteria:** You can run a monthly production review, interpret the signals, and produce a concrete improvement action. You can respond to a simulated AI incident in under 60 minutes with a RCA and prevention plan.

---

## Assessment: Production AI Maturity Score

After completing all 5 levels, assess current maturity using `knowledge/operations/ai-operational-maturity.md`.

Target progression: Level 1 → 5 over 12 weeks, spending ~2 weeks per level with active practice.

Do not rush to Level 5. Debugging fluency (Level 4) is the lever that makes everything else work. A Level 3 practitioner who can't debug is helpless when things go wrong.

# Production AI Learning System
## Master Map for Operational Fluency in AI Systems

Production AI systems fail differently than traditional software. The failure modes are: prompt failures (bad output), context failures (wrong input), model failures (quality/capacity), and infrastructure failures (latency/availability). This system builds the mental models, debugging tools, and operational rituals to identify and resolve each class of failure before users notice.

This document maps all 18 subsystems to their implementation files and defines the learning sequence.

---

## Subsystem Map

| # | Domain | Implementation | Core Mental Model |
|---|--------|---------------|------------------|
| 1 | Observability Learning | `knowledge/technical/observability.md` | You can only fix what you can see. Signal before dashboard. |
| 2 | Telemetry Systems | `knowledge/technical/telemetry.md` | Every AI call generates 6 signals. Log all 6. |
| 3 | Tracing Systems | `knowledge/technical/tracing.md` | A trace is a causal chain from user action to AI output. |
| 4 | Evaluation Workflows | `knowledge/technical/evaluation.md` + `/eval` | Evals are tests for AI behavior, not correctness. |
| 5 | Runtime Diagnostics | `knowledge/technical/runtime-diagnostics.md` | Diagnose: latency, throughput, error rate, token cost. |
| 6 | FastAPI Learning | `knowledge/technical/deployment-patterns.md` §FastAPI | FastAPI is the standard AI microservice shell. |
| 7 | Docker Learning | `knowledge/technical/deployment-patterns.md` §Docker | Docker makes AI environments reproducible. |
| 8 | Deployment Patterns | `knowledge/technical/deployment-patterns.md` | AI services have 3 layers: inference, memory, routing. |
| 9 | Monitoring Systems | `knowledge/technical/observability.md` §Monitoring | Monitoring = alerting on degradation before users report it. |
| 10 | AI Debugging Systems | `knowledge/technical/ai-debugging.md` + `/debug-ai` | Debug in order: prompt → context → model → infra. |
| 11 | Reliability Thinking | `knowledge/technical/reliability.md` | AI reliability includes quality SLOs, not just uptime. |
| 12 | Production Review Workflows | `/prod-review` + `playbooks/incident-response.md` | Periodic review + incident postmortem are both required. |
| 13 | Memory System Observability | `knowledge/technical/observability.md` §Memory | Memory failures are silent: they degrade quality, not availability. |
| 14 | Retrieval Diagnostics | `playbooks/ai-debugging.md` §Retrieval | Bad retrieval = wrong context = wrong output. Diagnose separately. |
| 15 | Context Debugging | `architecture/CONTEXT-DIAGNOSTICS.md` + `playbooks/ai-debugging.md` | Context failures look like model failures. Isolate first. |
| 16 | Prompt Failure Analysis | `playbooks/prompt-failure-analysis.md` + `/debug-ai` | Prompt failures have 4 root causes: scope, format, instruction, ambiguity. |
| 17 | AI Failure-Mode Analysis | `knowledge/technical/reliability.md` §Failure Modes | Map every output to: wrong, incomplete, hallucinated, or off-format. |
| 18 | Runtime Performance Review | `prompts/workflows/runtime-review.md` + `/prod-review` | Monthly review: cost, latency, quality score, failure rate. |

---

## Learning Sequence

Production AI fluency is built in five levels. Each level is a prerequisite for the next.

```
Level 1 — Signal Literacy (what to observe)
  Learn: Observability, Telemetry, Tracing
  Goal: Can describe what signals an AI system produces and why
  Artifacts: knowledge/technical/{observability,telemetry,tracing}.md

Level 2 — Infrastructure Fluency (where it runs)
  Learn: FastAPI, Docker, Deployment Patterns
  Goal: Can read a service's architecture and trace requests through it
  Artifacts: knowledge/technical/deployment-patterns.md
  Reference: claude-mem architecture in ~/.claude/skills/claude-mem/docs/

Level 3 — Evaluation Fluency (how to measure quality)
  Learn: Evaluation Workflows, LLM-as-judge, Rubric Design
  Goal: Can design and run an eval for an AI workflow
  Artifacts: knowledge/technical/evaluation.md, /eval skill

Level 4 — Debugging Fluency (how to fix it)
  Learn: AI Debugging, Prompt Failure Analysis, Context Debugging
  Goal: Can systematically diagnose any AI system failure in < 30 minutes
  Artifacts: playbooks/ai-debugging.md, playbooks/prompt-failure-analysis.md, /debug-ai

Level 5 — Operational Maturity (how to run it)
  Learn: Reliability Thinking, Production Review, Incident Response
  Goal: Can run a production AI system and improve it over time
  Artifacts: knowledge/technical/reliability.md, playbooks/incident-response.md, /prod-review
  Assessment: knowledge/operations/ai-operational-maturity.md
```

---

## The AI-Specific Failure Mode Taxonomy

Traditional software fails by crashing or timing out. AI systems fail silently — they produce output that looks plausible but is wrong, incomplete, or off-format. This taxonomy is the foundation for everything else in this system.

| Failure Class | Definition | Detection Signal | Debugging Start |
|---------------|-----------|-----------------|----------------|
| **Prompt Failure** | Instruction is ambiguous, scoped wrong, or missing required constraints | Output format wrong, scope drift, hallucinated structure | Isolate the prompt; run with minimal context |
| **Context Failure** | Wrong information was loaded, or required information was missing | Factually incorrect output that's internally consistent | Audit the context window; check retrieval mode |
| **Model Failure** | Model selected doesn't have the capability for the task | Output is syntactically correct but semantically shallow | Upgrade tier; check task complexity vs. model tier |
| **Infrastructure Failure** | Latency, rate limits, connection errors, token budget exhaustion | Timeouts, 429s, empty responses, truncated outputs | Check API logs; verify rate limits and retry logic |

**Rule:** Every debugging session starts by classifying the failure. The wrong classification wastes the entire debugging session.

---

## Production AI Review Cadence

| Cadence | Review Type | Skill | Output |
|---------|------------|-------|--------|
| Weekly | Quality signal check | `/prod-review quick` | Quality score delta, failure count |
| Monthly | Full operational review | `/prod-review full` | Cost, latency, quality, incident count |
| Per incident | Incident postmortem | `/prod-review incident` | RCA, fix, prevention |
| Quarterly | Maturity assessment | `knowledge/operations/ai-operational-maturity.md` | Level score, advancement plan |

---

## Reference Implementations in This Workspace

| System | Location | What to Learn From It |
|--------|----------|----------------------|
| claude-mem | `~/.claude/skills/claude-mem/` | Production AI memory: SQLite + ChromaDB + worker daemon + graceful degradation |
| WorkspaceClient | `production-ai/claude_client.py` | Prompt caching, model tier routing, dual JSONL telemetry |
| Telemetry | `telemetry/api-log.jsonl` | Live API call logs — the actual signal stream |
| Observability | `observability/` | Quality scores and dashboard outputs |

Study these before building anything new. The patterns are already there.

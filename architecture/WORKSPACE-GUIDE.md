# Workspace Guide
## Single navigation reference for the Enterprise Intelligence Workspace

Read it when you need to find something. Update it when the workspace structure changes. It is not a specification — it is a map.

---

## What the Workspace Is

A single-practitioner AI-native operational intelligence system. It has four layers:

```
CLAUDE.md               → behavioral rules + routing (load every session)
memory/MEMORY.md        → orientation index (load when touching workspace state)
.claude/commands/       → 83 skills (load only when invoked)
knowledge/ strategy/    → reference depth (load on demand)
```

**The compounding mechanism:** daily captures → weekly synthesis → knowledge entries → skill decisions → bet outcomes → patterns. Each layer feeds the next. Nothing is designed as a one-time artifact.

---

## Navigation by Intent

### "I want to do something now"
→ Check `CLAUDE.md` routing table (25 entries for most-used skills)
→ For PM work: type `/pm-[what you need]` or describe intent and let autonomous routing select

### "I need to find a file"
→ Knowledge: `knowledge/KNOWLEDGE-INDEX.md`
→ Skills: `skills/README.md`
→ Templates: `templates/` (see index below)
→ Strategy: `strategy/STRATEGY-OS.md`
→ Decisions: `decision-frameworks/decisions-log.md`
→ Executions: `execution/active-initiatives.md`

### "I need to understand how something works"
→ Context + 4-layer model: `architecture/CONTEXT-SYSTEM.md`
→ Skill design + routing: `architecture/SKILL-SYSTEM.md`
→ Intent routing + workflows: `architecture/OPERATIONAL-ROUTING.md`
→ Runtime + state schemas: `architecture/RUNTIME-SYSTEM.md`
→ Memory system: `architecture/MEMORY-MAP.md`
→ Data flows: `architecture/DATA-FLOWS.md`

### "I'm building something new"
→ Conventions: `architecture/MAINTENANCE-CONVENTIONS.md`
→ Anti-patterns: `architecture/ANTI-PATTERNS.md`
→ MCP capability layer: `architecture/MCP-CAPABILITY-LAYER.md`

### "Something is broken or degraded"
→ Workspace health: `/observe`
→ AI system failure: `playbooks/ai-debugging.md` then `/debug-ai`
→ Context degradation: `/context-audit`
→ Knowledge quality: `/misconception`

---

## Skill Catalog by Domain

**Runtime (4):** `/runtime-start`, `/runtime-resume`, `/runtime-status`, `/runtime-recover`

**Invocation system (2):** `/skill-lookup`, `/skill-new`

**Core operational (8):** `/briefing`, `/capture`, `/debrief`, `/promote`, `/decide`, `/weekly`, `/observe`, `/synthesize`

**Memory (6):** `/mem-capture`, `/mem-recall`, `/mem-adr`, `/mem-failure`, `/mem-reconstruct`, `/mem-hygiene`

**Daily OS (4):** `/plan`, `/focus`, `/prep`, `/shutdown`

**Knowledge (10):** `/learn`, `/recall`, `/pattern`, `/repo-learn`, `/knowledge-connect`, `/knowledge-cluster`, `/knowledge-review`, `/knowledge-graph`, `/knowledge-validate`, `/knowledge-qa`

**Strategy (4):** `/bet`, `/horizon`, `/strategy-review`, `/strategy-posture`

**Execution (6):** `/exec-plan`, `/exec-decompose`, `/exec-review`, `/exec-checkpoint`, `/exec-risk`, `/exec-prioritize`

**PM (44):** All `/pm-*` skills. Full descriptions in `skills/README.md`. Invoke by typing the intent and autonomous routing selects, or use `/pm-[domain]` prefix directly.

**Context engineering (2):** `/context-audit`, `/context-compile`

**Production AI (3):** `/prod-review`, `/eval`, `/debug-ai`

**Cognitive acceleration (6):** `/think`, `/misconception`, `/recall-test`, `/arch-critique`, `/decision-review`, `/insight`

---

## Architecture Documents

Active architecture documents in `architecture/`. Documents marked *(merged)* are retirement notices pointing to the merged doc.

**Core system references (read these):**

| Document | When to consult |
|---|---|
| `OPERATIONAL-ROUTING.md` | Intent detection, execution modes, sequencing, workflow maps, MCP routing |
| `SKILL-SYSTEM.md` | Skill design, all routing signals, PM skill map, capability taxonomy, synthesis |
| `CONTEXT-SYSTEM.md` | 4-layer model, budget, progressive loading, memory lifecycle |
| `RUNTIME-SYSTEM.md` | Runtime architecture, orchestration rules, bounded autonomy rules, state schemas |
| `RECOVERY-PLAYBOOKS.md` | 6 situation-specific recovery guides (session restart, crash, corruption, missing artifacts) |
| `MCP-CAPABILITY-LAYER.md` | MCP registry, permission classes (R/RW/NET/DESTR), governance rules G-1 through G-10 |
| `FINAL-SIMPLIFICATION-REVIEW.md` | Simplification findings, 10 anti-complexity rules, 8 autonomy guardrails |

**Domain system references:**

| Document | When to consult |
|---|---|
| `CONTEXT-DIAGNOSTICS.md` | Running `/context-audit` |
| `EXECUTION-RIGOR-SYSTEM.md` | Understanding exec skill design |
| `STRATEGIC-INTELLIGENCE-SYSTEM.md` | Understanding bet + strategy skill design |
| `DAILY-OPERATING-SYSTEM.md` | Energy model, deep work, meeting system |
| `COGNITIVE-ACCELERATION-SYSTEM.md` | Recall, misconception, insight design |
| `PRODUCTION-AI-LEARNING-SYSTEM.md` | Production AI review and debug design |
| `FINAL-REVIEW.md` | Workspace known issues and recommendations |
| `COGNITIVE-MEMORY-SYSTEM.md` | 4-layer memstack, 7 memory types, retrieval, lifecycle |
| `MEMORY-SCHEMAS.md` | Canonical YAML schemas for all 7 memory types |
| `KNOWLEDGE-COMPOUNDING-SYSTEM.md` | Compounding model, node/edge/cluster schema |
| `RETRIEVAL-INTELLIGENCE.md` | Scoring algorithm, retrieval pipeline, spaced repetition |
| `KNOWLEDGE-QA-SYSTEM.md` | 0–90 quality scoring, calibration flags, graph integrity |

**Rarely consulted:**
`MCP-ROUTING-SYSTEM.md`, `MEMORY-CONTINUITY-SYSTEM.md`, `DYNAMIC-CAPABILITY-GENERATION.md`

**Merged (redirect notices only):**
AUTONOMOUS-ORCHESTRATION, AUTONOMOUS-OPERATIONAL-FLOWS, EXECUTION-ORCHESTRATION, WORKFLOW-ROUTING → `OPERATIONAL-ROUTING.md`
DYNAMIC-INVOCATION-SYSTEM, SKILL-ROUTING-SYSTEM, SKILL-ARCHITECTURE → `SKILL-SYSTEM.md`
CONTEXT-ENGINEERING-SYSTEM, CONTEXT-ARCHITECTURE, CONTEXT-SELECTION-SYSTEM → `CONTEXT-SYSTEM.md`
BOUNDED-RUNTIME, RUNTIME-STATE-SCHEMA → `RUNTIME-SYSTEM.md`
PERSISTENT-EXECUTION-SYSTEM → retired (SR-1)

---

## Playbooks

| Playbook | Purpose | When to use |
|---|---|---|
| `daily-operations.md` | Full daily operations guide | When you need routing help for your day |
| `cognitive-review.md` | Monthly cognitive review ritual | First of month |
| `ai-debugging.md` | AI system failure investigation | Any AI system failure |
| `prompt-failure-analysis.md` | Prompt-specific failure diagnosis | Class 1 failure identified |
| `incident-response.md` | Incident severity + response protocol | Production incident |
| `misconception-detection.md` | Knowledge quality investigation | P0 misconception found |

---

## Templates Index

| Template | Purpose |
|---|---|
| `daily-plan.md` | Output of `/plan` |
| `eod-capture.md` | Output of `/shutdown` |
| `decision-journal.md` | Decision logging |
| `weekly-review.md` | Output of `/weekly` |
| `operational-retro.md` | Monthly retro |
| `execution-plan.md` | Output of `/exec-plan` |
| `task-decomposition.md` | Output of `/exec-decompose` |
| `strategic-checkpoint.md` | Output of `/exec-checkpoint` |
| `risk-register.md` | Output of `/exec-risk` |
| `strategic-bet.md` | Output of `/bet open` |
| `strategic-review.md` | Monthly strategy review |
| `horizon-scan.md` | Output of `/horizon` |
| `bet-postmortem.md` | Output of `/bet postmortem` |
| `recovery-playbook.md` | Post-recovery incident record |
| `episodic-memory.md` | Episodic memory entry |
| `semantic-memory.md` | Working concept entry |
| `adr.md` | Architecture Decision Record |
| `failure-memory.md` | Failure record with causal chain |
| `insight-memory.md` | Strategic insight entry |
| `context-reconstruction.md` | Topic context reconstruction |
| `learning-entry.md` | Output of `/learn` |
| `pattern-entry.md` | Output of `/pattern` |
| `knowledge-entry.md` | Base format for knowledge entries |
| `cluster-note.md` | Knowledge cluster synthesis |
| `cluster-synthesis.md` | Output of `/knowledge-cluster` (core claim, shared themes, tensions, synthesized insight) |
| `atomic-concept.md` | Single-concept knowledge entry |
| `meeting-raw.md` | Meeting input format |
| `repo-insight.md` | Output of `/repo-learn` |

---

## Operational Cadence Quick Reference

**Required rituals (3):**
1. Daily: `/briefing` (2 min, session start)
2. Daily: `/shutdown` (5-10 min, session end)
3. Weekly: `/weekly` + `/exec-review weekly` (30 min, Monday)

**High-value rituals (situational):**
- `/plan` — when `/briefing` isn't enough to set direction
- `/focus` — before any deep work session
- `/prep` — before high-stakes meetings
- Monthly: cognitive review (`playbooks/cognitive-review.md`)
- Monthly: strategy review
- Quarterly: portfolio review

**Full ritual spec:** `execution/RITUALS.md`

---

## File Locations Quick Reference

| What | Where |
|---|---|
| Active initiatives | `execution/active-initiatives.md` |
| Active bets | `strategy/active-bets.md` |
| Decisions log | `decision-frameworks/decisions-log.md` |
| OKRs | `strategy/OKRs.md` |
| Risk register | `execution/risks.md` |
| Weekly reviews | `reviews/weekly/` |
| Raw notes | `notes/raw/` |
| Meeting outputs | `meeting-intelligence/processed/` |
| API telemetry | `telemetry/api-log.jsonl` |
| Quality log | `observability/quality.jsonl` |
| Active workflows | `runtime/state/active-workflows.json` |
| Memory retrieval index | `memory/RETRIEVAL-INDEX.json` |
| Episodic memories | `memory/episodic/ep_*.md` |
| ADRs | `memory/decisions/dec_*.md` |
| Failure records | `memory/failures/fail_*.md` |
| Context reconstructions | `memory/context/ctx_*.md` |
| Knowledge graph | `knowledge/KNOWLEDGE-GRAPH.json` |
| Compounding audit log | `knowledge/COMPOUNDING-LOG.md` |
| Knowledge entries | `knowledge/<domain>/*.md` |
| Cluster syntheses | `knowledge/clusters/*.md` |
| Workflow history | `runtime/state/workflow-history.json` |
| Runtime events | `runtime/events/queue.json` |

---

## Maintenance Rules

See `FINAL-OPERATING-RULES.md` for the full set. Summary:

1. **CLAUDE.md stays under 1,500 tokens.** No new routing entries for PM variants or self-discoverable skills.
2. **New architecture docs don't go in CLAUDE.md System References.** Add them to this guide instead.
3. **Skills are the canonical specification.** Prompt files and playbooks are supplementary.
4. **Top 3 rule for rituals:** Know which 3 you'd never skip. Everything else is situational.
5. **Knowledge entries get staggered reviewed dates.** Don't use creation date for all entries in a batch.

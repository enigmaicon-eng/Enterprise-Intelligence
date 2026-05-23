---
title: Context Engineering
domain: technical
created: 2026-05-21
reviewed: 2026-05-22
tags: [context, prompt-engineering, token-budget, progressive-loading, caching, retrieval, reasoning]
connections: [ai-systems, claude-patterns, memory-continuity-system, prompt-architecture, retrieval-system]
confidence: high
source: original synthesis
---

## Definition
Context engineering is the practice of deliberately constructing what an AI model receives as input — selecting, ordering, compressing, and caching information so that the model has maximum relevant signal within a finite token budget. It is distinct from prompt engineering: prompt engineering designs the instruction; context engineering designs the full environment the instruction operates within.

## Why It Matters
A model with the wrong context produces wrong outputs even if the model itself is capable. Context quality is the primary variable in output quality for a fixed model — more leverage than temperature tuning, model selection within a tier, or prompt phrasing. Poor context engineering is the leading cause of AI workflow failures in practice.

## Key Principles

- **Load order matters.** What appears first in context receives more attention. Put behavioral rules and the most relevant memory before supporting detail.
- **Index before depth.** Always check an index before reading a full file. A 200-token scan prevents a 2,000-token irrelevant read.
- **Progressive loading beats pre-loading.** Load context in waves (orientation → task-relevant → on-demand) rather than front-loading everything. This preserves budget for actual work.
- **Compression is a tool.** Long prior context can be compressed 3:1 to 5:1 with minimal signal loss.
- **System prompt caching is free money.** The first call pays; all subsequent calls within the cache TTL recover ~90% of input token cost.
- **Retrieval mode before retrieval target.** Identify the retrieval mode (direct, index-first, grep, cluster) before deciding which file to read.
- **Reasoning structure before output.** Match the reasoning block type to the task before generating output. Unstructured reasoning produces inconsistent outputs.
- **Behavioral tuning prevents drift.** Long sessions drift from calibration. Anti-drift rules applied silently every 10+ exchanges maintain consistency.

## The 14-Subsystem Architecture

The workspace implements context engineering across 14 subsystems:

| Subsystem | Implementation |
|-----------|---------------|
| Context Layering | `architecture/CONTEXT-ARCHITECTURE.md` |
| Memory Hierarchy | `architecture/MEMORY-CONTINUITY-SYSTEM.md` |
| Retrieval System | `architecture/RETRIEVAL-SYSTEM.md` |
| Prompt Architecture | `architecture/PROMPT-ARCHITECTURE.md` |
| Behavioral Tuning | `architecture/BEHAVIORAL-TUNING.md` |
| Instruction Hierarchy | `architecture/PROMPT-ARCHITECTURE.md` §Precedence |
| Context Routing | `architecture/CONTEXT-ENGINEERING-SYSTEM.md` |
| Budget Optimization | `architecture/CONTEXT-SELECTION-SYSTEM.md` |
| Reasoning Structure | `architecture/REASONING-STRUCTURE.md` |
| Output Architecture | `architecture/REASONING-STRUCTURE.md` §Output |
| Anti-Pattern Detection | `architecture/ANTI-PATTERNS.md` |
| Prompt Compilation | `architecture/PROMPT-ARCHITECTURE.md` §Compilation |
| Retrieval Hygiene | `architecture/RETRIEVAL-SYSTEM.md` §Hygiene |
| Context Diagnostics | `architecture/CONTEXT-DIAGNOSTICS.md` |

Master system index: `architecture/CONTEXT-ENGINEERING-SYSTEM.md`
Operational skills: `/context-audit`, `/context-compile`

## In Practice

The 5-wave progressive loading protocol in `architecture/CONTEXT-SELECTION-SYSTEM.md`:
1. Always: `CLAUDE.md` + `MEMORY.md` (~200 tokens)
2. Session start: user profile + active project file (~300 tokens)
3. On skill invocation: skill prompt only (~150–500 tokens)
4. On workflow execution: workflow-specific prompts (~200–400 tokens)
5. On demand: knowledge lookups triggered by content, not pre-loaded

Total target: <4,000 tokens of context overhead before the user message.

The 5-layer prompt compilation pipeline (from `architecture/PROMPT-ARCHITECTURE.md`):
- Layer A: CLAUDE.md (~600 tokens, always)
- Layer B: Session memory (selective, ~800 tokens)
- Layer C: Active skill (~1,500 tokens, on invocation)
- Layer D: Task data (variable, per workflow step)
- Layer E: User request

Retrieval uses 5 modes (from `architecture/RETRIEVAL-SYSTEM.md`): Direct → Index-First → Grep → Cluster → Skip (generate).

## Failure Modes
- **Context stuffing.** Loading all potentially relevant files exhausts the budget and dilutes attention.
- **Stale context.** Reading a memory file as if it reflects current state without checking the `updated:` date.
- **Missing cache_control.** Forgetting `{"type": "ephemeral"}` on the system prompt block means paying full price on every repeated call.
- **Depth without breadth.** Reading one knowledge file deeply while missing 3 more that an index scan would have found.
- **Reasoning without a block.** Generating output without applying a reasoning block template produces inconsistent structure and premature closure.
- **Behavioral drift.** Format and calibration drifting over long sessions when anti-drift rules aren't applied.

## Connections
- [[ai-systems]] — model selection interacts with context budget
- [[claude-patterns]] — effective patterns for structuring context Claude responds to predictably
- [[memory-continuity-system]] — how the memory layer feeds the context assembly process
- [[prompt-architecture]] — the compilation pipeline that assembles context per task type
- [[retrieval-system]] — how context is fetched and validated before use

## Open Questions
- What is the empirical token budget threshold beyond which additional context produces diminishing returns for Sonnet vs. Opus?
- How does extended thinking budget interact with context window size for reasoning-heavy tasks?
- What is the optimal compression ratio for synthesis memos before they become less useful than regeneration?

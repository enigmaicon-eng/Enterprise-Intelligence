---
title: AI Systems — Claude Model Knowledge
domain: technical
created: 2026-05-21
reviewed: 2026-05-21
tags: [claude, anthropic, llm, model-selection, api]
connections: [context-engineering, claude-patterns, mcp-patterns]
confidence: high
source: original synthesis
---

## Definition
AI systems in this workspace refers to the Claude model family and the Anthropic API — the infrastructure underlying every automated workflow. Three model tiers cover distinct task types: Haiku (fast, cheap, extraction), Sonnet (balanced, most workflows), Opus (reasoning-heavy, strategy). The model-tier separation is a deliberate cost-quality optimization, not a quality hierarchy.

## Why It Matters
Defaulting every call to Opus wastes money and latency. Defaulting to Haiku misses synthesis quality. Getting tier selection wrong by one step costs 10-20x per call. At scale, model routing is the single highest-leverage cost control.

## Key Principles
- Tier by task, not by importance: importance doesn't map to model complexity needed.
- Cache system prompts on every call: the `cache_control: ephemeral` pattern recovers ~90% of system prompt cost after the first call.
- Extended thinking is only for genuine uncertainty: `call_with_thinking()` should be reserved for decisions where the reasoning process itself is the output, not just the answer.
- Session IDs enable cost attribution: always tag API calls with a session_id to trace costs to workflows.

## In Practice
The `production-ai/claude_client.py` WorkspaceClient maps tiers to current model IDs:
- `capture` tier → `claude-haiku-4-5-20251001` — meeting structure extraction, note tagging
- `analysis` tier → `claude-sonnet-4-6` — debrief, weekly review, knowledge promotion
- `strategy` tier → `claude-opus-4-7` — monthly synthesis, bets review, extended thinking flows

Model IDs must be pinned explicitly — never use "latest" aliases in production calls.

## Failure Modes
- **Tier mismatch**: routing a strategy synthesis call to Haiku produces shallow output that looks complete but misses non-obvious connections.
- **Missing cache_control**: paying full input token price on every repeated system prompt. At 1,000 tokens/prompt × 100 calls/day = 100K tokens/day in unnecessary cost.
- **Stale model IDs**: Anthropic retires models. Pinned IDs that aren't updated will throw errors. Review quarterly.

## Connections
- [[context-engineering]] — how system prompt design interacts with caching efficiency
- [[claude-patterns]] — workspace-specific effective patterns for prompting Claude
- [[mcp-patterns]] — how Claude connects to external tools via MCP

## Open Questions
- At what call volume does prompt caching pay for the operational overhead of monitoring cache hit rates?
- How does extended thinking interact with prompt caching — do they compound or conflict?

## Referenced By
<!-- Populated as other notes link to this one -->

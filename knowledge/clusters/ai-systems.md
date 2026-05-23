---
title: AI Systems — Synthesis Cluster
theme: How to build reliable, cost-effective AI workflows with Claude
domain: technical
created: 2026-05-21
last_synthesized: 2026-05-21
member_notes: [ai-systems, context-engineering, claude-patterns, mcp-patterns]
tags: [claude, context, ai-workflow, cost-optimization, reliability]
confidence: medium
---

## Theme Summary
The AI systems cluster covers everything this workspace knows about working with Claude effectively: model selection, context construction, prompt caching, MCP tool routing, and patterns for reliable output. The unifying insight is that AI workflow quality is an engineering problem, not a prompting art — it depends on reproducible structure (context, caching, tier routing) more than on clever instructions.

## Core Tension
Flexibility vs. reliability: the more tailored a prompt or context is to a specific situation, the more fragile it is to variation. The more generic and structured the approach, the more consistently it performs across situations but the less it excels on any one. The patterns in this workspace resolve this by separating structural concerns (handled in skills/architecture) from content concerns (handled in prompts/workflows).

## Key Synthesis Points

### 1. Context quality is the primary quality lever
What the model receives determines what it produces more than which model receives it. [[context-engineering]] establishes this explicitly. [[ai-systems]] identifies that a Sonnet call with excellent context will outperform an Opus call with poor context in most workflow scenarios.

### 2. Cost optimization is structural, not per-call
The cache_control pattern in [[ai-systems]] and the progressive loading protocol in [[context-engineering]] both reduce cost by design, not by attention. You don't need to think about cost per call if the architecture enforces the right patterns automatically.

### 3. MCP tools extend context beyond text
[[mcp-patterns]] establishes that MCP connections (Figma, Calendar, Drive) aren't just tool calls — they're context sources. A design intent from Figma or a meeting from Calendar can be loaded into Claude's context the same way a markdown file is. This collapses the distinction between "knowledge in files" and "knowledge in tools."

## Pattern Map
```
[[context-engineering]] → [[ai-systems]]  (context design informs model selection)
[[ai-systems]] → [[claude-patterns]]      (model capabilities constrain what patterns work)
[[claude-patterns]] → [[mcp-patterns]]    (Claude patterns extend to tool-using patterns)
[[context-engineering]] ←→ [[claude-patterns]] (mutual: each shapes the other)
```

## Strongest Signal
System prompt caching with progressive context loading is the single highest-leverage pattern in this cluster — it directly reduces cost and indirectly improves quality by keeping context focused.

## Weak Signals
- Extended thinking may have workflow uses beyond strategy synthesis (e.g., complex debugging). Needs 2+ instances to confirm.
- MCP tool call latency may create a new class of context budget problem when tools return large payloads.

## Open Questions
- Is there a reliable signal for when a task crosses the threshold from Sonnet to Opus, or does tier routing require manual calibration per workflow type?
- How does context window size interact with quality for very long meeting debriefs?

## Member Notes
- [[ai-systems]] — Claude model tier map, caching patterns, model ID management
- [[context-engineering]] — progressive loading, budget model, compression
- [[claude-patterns]] — workspace-specific prompting patterns that work reliably
- [[mcp-patterns]] — MCP tool routing and Figma/Calendar/Drive integration patterns

## Related Clusters
- [[operational-intelligence]] — how AI systems integrate into operational workflows

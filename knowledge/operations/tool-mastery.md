---
title: Tool Mastery — Claude Code and AI Tool Learnings
domain: operations
created: 2026-05-21
reviewed: 2026-05-21
tags: [claude-code, tools, ai-tools, workflow, shortcuts]
connections: [work-patterns, friction-points, ai-systems]
confidence: medium
source: original synthesis
---

## Definition
Tool mastery is accumulated knowledge about how to use Claude Code and related AI tools effectively — the non-obvious behaviors, useful patterns, and sharp edges that aren't in the documentation but emerge from regular use.

## Why It Matters
Tool knowledge is operational leverage. An hour spent learning a sharp edge prevents that edge from cutting every future session. This file is where those learnings persist across sessions.

## Claude Code Patterns

### Permission Management
Claude Code prompts for tool approval per-call by default. High-frequency read operations (Glob, Grep on known paths) can be pre-approved in `.claude/settings.json` to reduce friction. Run `/fewer-permission-prompts` to auto-generate the allowlist from transcript history.

### Context Window Budget
Claude Code loads CLAUDE.md automatically on session start. Every extra line in CLAUDE.md costs context budget every session. Keep CLAUDE.md under 1,200 tokens (behavioral rules only) and route reference material to `architecture/` files loaded on demand.

### Skill Invocation
Skills in `.claude/commands/` are loaded only when invoked — they do not occupy context by default. This is intentional: load skills on demand, not pre-emptively.

### Session Continuity
There is no automatic session continuity. The memory system in `memory/` is the only cross-session persistence mechanism. If you don't read `memory/MEMORY.md` at session start, you start from scratch.

## MCP Tool Patterns

### Figma
Always run `get_design_context` before generating design artifacts. Figma's context is richer than screenshots — it includes component names, constraint values, and design tokens that screenshots lose.

### Playwright
Playwright tool calls are session-scoped — navigate, snapshot, and close within a single workflow. Leaving browser sessions open wastes memory and creates authentication state confusion.

## Sharp Edges

| Tool | Sharp Edge | Workaround |
|------|-----------|------------|
| Write tool | Fails if file not read first (for existing files) | Always Read before Write on existing files; use Edit for partial updates |
| Edit tool | Requires exact string match — whitespace matters | Copy exact text from Read output, don't retype |
| Bash tool | No working directory persistence across calls | Use absolute paths everywhere |
| CronCreate | Cron expressions must be valid — no validation on write | Test with CronList after creation |

## Open Questions
- Is there a way to pre-approve specific MCP tool calls (not just file system tools) in settings.json?
- What is the actual token cost of the CLAUDE.md load on every session start?

## Referenced By
<!-- Populated as other notes link to this one -->

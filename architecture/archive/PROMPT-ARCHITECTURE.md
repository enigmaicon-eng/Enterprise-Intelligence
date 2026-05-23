# Prompt Architecture
## Structure, Compilation, and Instruction Hierarchy

Every inference call assembles a prompt — the complete input the model receives. This document specifies the slot structure, compilation pipeline, instruction precedence, and anti-drift rules that govern how prompts are built in this workspace.

---

## The 5-Layer Structure

Prompts assemble in five layers, in order. Content belongs in exactly one layer.

```
Layer A — Workspace Identity
  Source:  CLAUDE.md
  Content: Behavioral rules, routing, output standards, memory protocol
  Budget:  ~600 tokens (hard cap: 1,000)
  Load:    Always

Layer B — Session Orientation
  Source:  memory/MEMORY.md index + selective per-file memories
  Content: User profile, active projects, priorities, feedback patterns
  Budget:  ~800 tokens (index: ~400 + 1-2 files: ~400)
  Load:    Index always; per-file memories selectively

Layer C — Domain Context
  Source:  .claude/commands/<active-skill>.md
  Content: Skill-specific workflow, input spec, output schema, quality criteria
  Budget:  ~1,500 tokens (hard cap: 2,000)
  Load:    On skill invocation only. One skill at a time.

Layer D — Task Data
  Source:  Workflow-required files (knowledge, strategy, meetings, etc.)
  Content: The specific data the active workflow step needs to operate on
  Budget:  Variable, bounded by the workflow spec's file list
  Load:    Per workflow step. Index-first. Size-check large files.

Layer E — Request
  Source:  User message
  Content: The specific ask for this turn
  Budget:  Variable
  Load:    Always (it's the user's message)
```

**Overhead target:** A+B ≤ 1,400 tokens | A+B+C ≤ 3,000 tokens | A+B+C+D ≤ 4,000 tokens

---

## Compilation Pipeline

Assemble layers sequentially. Budget-check after each layer.

```
Step 1 — Identify task type
  Use the Context Routing table in CONTEXT-ENGINEERING-SYSTEM.md.
  This determines which layers to load and in what configuration.

Step 2 — Load Layer A
  CLAUDE.md is always active.
  If CLAUDE.md > 1,000 tokens: flag the anti-pattern before proceeding.
  Do not continue with an over-budget Layer A.

Step 3 — Load Layer B (selective)
  Always: read MEMORY.md index (~400 tokens).
  Conditionally: user_profile.md if task involves judgment about the user.
  Conditionally: project file if a named project is the session's focus.
  Stop at 2-3 files. Do not batch-load all memory files.

Step 4 — Load Layer C (on invocation)
  Load the active skill's command file when the skill is invoked.
  Only one skill is active at a time. Cross-skill pipelines load sequentially.
  Do not pre-load skills that might be needed.

Step 5 — Load Layer D (per workflow step)
  Read only files the current workflow step explicitly names.
  Before reading content: read the relevant index (KNOWLEDGE-INDEX.md, MEMORY.md, etc.).
  Before reading large files (>100 lines): read first 50 lines to verify relevance.
  
Step 6 — Budget check
  Estimate total A+B+C+D overhead.
  If overhead > 4,000 tokens: identify what to defer or compress before continuing.

Step 7 — Receive Layer E
  The user's message is the final layer. It arrives, not assembled.
```

---

## Instruction Hierarchy

When instructions from different sources conflict, apply this precedence (1 = highest):

| Priority | Source | Overridable? |
|----------|--------|-------------|
| 1 | CLAUDE.md behavioral guardrails | No. Never. |
| 2 | CLAUDE.md behavioral rules (output standards, routing) | Only by explicit user override with acknowledgment |
| 3 | Active skill instructions | By user-turn instruction when format is not machine-required |
| 4 | Persistent memory feedback | By user-turn instruction for this turn |
| 5 | User-turn instruction | — (this is the base case) |

**Conflict resolution rules:**
- A P5 instruction overrides P4 for the current turn only. It doesn't change the memory.
- A P5 instruction overrides P3 unless the skill's output format is machine-readable (JSON, YAML, etc.).
- A P5 instruction does NOT override P1 (guardrails). If the user asks to skip a guardrail, name it and decline.
- A P5 instruction overrides P2 when the user explicitly acknowledges the default: "I know you default to prose, but give me a table here" — apply it without friction.

**No silent overrides.** When a higher-priority rule blocks a user request, say so in one sentence. Then apply the rule.

---

## Prompt Structure Per Task Type

| Task Type | Layers | Key Rules |
|-----------|--------|-----------|
| Simple question | A, B (index), E | No template. Direct answer. No preamble. |
| Memory question | A, B (index + file), E | State the memory before answering. Include age. |
| Skill workflow | A, B, C, D (per step), E | Follow skill output schema exactly. No improvisation. |
| Strategic analysis | A, B (full), C, D (strategy/), E | Anchor conclusions to OKRs and active bets. |
| Knowledge capture | A, B (index), C (learn/promote), E | Use knowledge entry template. Fill all required fields. |
| Diagnostic | A, B (all), C (context-audit), D (diagnostics), E | Output severity scores. List P0s first. |
| Context compilation | A, B (index + profile), C (context-compile), E | Output context manifest with token estimates. |

---

## Anti-Drift Rules

Long sessions drift from behavioral calibration. Detect and correct silently.

| Drift Pattern | Signal | Correction |
|---------------|--------|-----------|
| Format drift | Response length creeping up over 3+ turns | Reset to default output standard on next turn |
| Caveat accumulation | Hedges ("might," "could") on non-speculative topics | Return to direct language |
| Instruction echo | Restating user's question before answering | Drop the preamble entirely |
| List creep | Prose questions answered with bullets | Revert to prose |
| Speculation inflation | "Possibly X" when evidence supports "X" | Make the claim directly |
| Trailer summaries | "In summary," at the end of responses | Cut the summary |

**Apply corrections silently.** Don't narrate drift or its correction. The user shouldn't need to notice either.

**Long-session check:** Every 10+ exchanges in a session, verify you're still following: (1) the output length standard, (2) the format standard, (3) no unsolicited commentary.

---

## Prompt Quality Signals

These signals indicate a prompt (skill command file or workflow prompt) needs revision:

| Signal | Threshold | Action |
|--------|-----------|--------|
| Quality score < 3.5 | Average over 3+ uses | Revise the prompt. Log in PROMPT-REGISTRY.md. |
| Output format inconsistency | 2+ uses producing different formats | Add explicit format constraints to the prompt |
| Scope creep in output | Output includes content not in the spec | Tighten the output schema |
| Prompt > 2,000 tokens | Single command file | Move reference material to `skills/<name>/references/` |
| Drift from skill spec | Command file ≠ skill spec | Sync both. The command file drives behavior; the spec is the source of truth. |

# Context System
## Layered Context Model, Budget Management, and Loading Strategy

Consolidates: CONTEXT-ARCHITECTURE.md, CONTEXT-ENGINEERING-SYSTEM.md, CONTEXT-SELECTION-SYSTEM.md

---

## The Four-Layer Model

```
┌─────────────────────────────────────────────────────┐
│  Layer 1 — Workspace Identity                       │
│  CLAUDE.md                                          │
│  Always loaded. Behavioral rules only. ~600 tokens. │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│  Layer 2 — Orientation                              │
│  memory/MEMORY.md + per-session files               │
│  Loaded at session start. Active state. ~1,500 tok. │
└────────────────────────┬────────────────────────────┘
                         │ (on demand)
┌────────────────────────▼────────────────────────────┐
│  Layer 3 — Domain Context                           │
│  .claude/commands/<skill>.md                        │
│  Loaded only when skill invoked. Per-skill budget.  │
└────────────────────────┬────────────────────────────┘
                         │ (on demand)
┌────────────────────────▼────────────────────────────┐
│  Layer 4 — Reference Depth                          │
│  knowledge/, strategy/, synthesis/, etc.            │
│  Read when workflow requires. Archived after 90d.   │
└─────────────────────────────────────────────────────┘
```

---

## Layer Contracts

### Layer 1 — CLAUDE.md

**What belongs here:** Workspace purpose · layer contract · skill routing table · file routing rules · output standards · memory protocol · behavioral guardrails.

**What does NOT belong:** Reference tables · workflow specs · knowledge content · anything that changes more than monthly.

**Token budget:** Hard cap at ~1,000 tokens. If CLAUDE.md exceeds this, it has absorbed reference material that belongs in a lower layer.

**Signal:** If you could delete a section and the workspace would still behave correctly, that section belongs in a lower layer.

---

### Layer 2 — memory/

**What belongs here:** User profile · active projects (≤5 bullets each) · current priorities · open threads · feedback patterns · reference pointers.

**What does NOT belong:** Detailed project docs · meeting notes · historical reviews · anything derivable from current file state.

**Token budget per file:** 500 tokens max. MEMORY.md index: 200 lines max.

**Freshness rule:** Files not read in 30 days are stale — review or archive. Entries with `current_as_of:` >14 days need verification before relying on them.

**Loading rule:** MEMORY.md index loads every session. Per-file memories load when their topic is active. Never load memory files as a batch.

---

### Layer 3 — .claude/commands/

**What belongs here:** Task-specific context · workflow steps · input requirements · output format · quality criteria.

**What does NOT belong:** Content duplicated from CLAUDE.md · reference material · cross-skill orchestration logic.

**Token budget per skill:** ~1,500 tokens in the command file. Longer content → `skills/<name>/references/`.

**Activation rule:** Skills are invoked explicitly or by clear pattern match. Never pre-loaded.

---

### Layer 4 — knowledge/, strategy/, synthesis/

**What belongs here:** Permanent knowledge entries · historical records · active strategy · synthesis outputs.

**What does NOT belong:** Behavioral rules · current-state facts · ephemeral captures before synthesis.

**Access pattern:** Never bulk-loaded. Read when a specific workflow needs a specific file.

**Retrieval:** Use Grep/Glob to find relevant files before reading. Never scan the entire `knowledge/` directory.

**Decay policy:** Files with `reviewed:` >90 days are flagged in the weekly observability report.

---

## Context Budget Model

| Component | Token Budget | Frequency |
|-----------|-------------|-----------|
| CLAUDE.md | ~600 | Always |
| MEMORY.md index | ~400 | Always |
| 2-3 active memory files | ~900 | Session start |
| Active skill (when invoked) | ~1,500 | Per invocation |
| Workflow-required files | Variable | Per step |
| **Total overhead target** | **<4,000** | Leaves >190K for work |

**Ceiling rule:** If non-conversation overhead exceeds 5,000 tokens, something was loaded speculatively. Stop loading until a workflow explicitly needs it.

---

## Progressive Loading Strategy

Context loads in waves — each triggered by a specific need. Never load Wave N+1 speculatively when Wave N is sufficient.

```
Wave 1 — Session Start (always)
    CLAUDE.md + MEMORY.md index
    Cost: ~1,000 tokens

Wave 2 — Orientation (first 2 exchanges)
    user_profile.md + 1-2 relevant project files
    Cost: ~600-1,000 tokens

Wave 3 — Skill Activation (on invocation)
    .claude/commands/<skill>.md
    Cost: ~1,500 tokens

Wave 4 — Workflow Files (as needed)
    Specific files the active skill requires
    Cost: variable, bounded by skill spec

Wave 5 — Knowledge Lookup (on demand)
    Specific knowledge/ or synthesis/ files
    Only when workflow explicitly requires them
```

---

## Context Routing

Task type determines which layers activate. Load the minimum that covers the task.

| Task Type | L1 | L2 Memory | L3 Skill | L4 Knowledge |
|-----------|:--:|:---------:|:--------:|:-----------:|
| Simple question | ✅ | Index only | — | — |
| Memory question | ✅ | Index + relevant file | — | — |
| Skill workflow | ✅ | Index + profile + project | ✅ | If required |
| Knowledge recall | ✅ | Index only | `/recall` | Target file |
| Cross-skill pipeline | ✅ | Index + profile + project | Sequential, one at a time | Per step |
| Strategic analysis | ✅ | All relevant | Active skill | `strategy/` + `synthesis/` |
| Diagnostic / audit | ✅ | All files | `/context-audit` | `CONTEXT-DIAGNOSTICS.md` |

**Expansion rule:** Start at minimum. Expand only when the task reveals it's needed — not speculatively.

---

## Index-First Loading

Before reading any content file, read its index:

| Before reading... | First read... |
|-------------------|---------------|
| Any file in `knowledge/` | `knowledge/KNOWLEDGE-INDEX.md` |
| Any file in `memory/` | `memory/MEMORY.md` |
| Any processed meeting | The file's frontmatter |
| Any synthesis document | Frontmatter and first section |

**Why:** Index reads cost 100-300 tokens. Content reads cost 300-1,500 tokens. Reading the index first lets you decide whether the content is worth reading.

---

## File Selection Heuristics

**Date filtering:** For time-scoped workflows, filter by date first.
- `meeting-intelligence/processed/2026-05-*.md` not `**/*.md`

**Relevance filtering:** For topic-scoped workflows, Grep before Read.
- Grep the index for the topic → read only matching files.

**Size check:** For large files, read first 50 lines to verify relevance before reading the full file.

---

## Memory Hierarchy

| Stage | Age | Storage | Loading Rule |
|-------|-----|---------|-------------|
| Active | ≤14 days | `memory/` | Load when topic matches. Trust on read. |
| Latent | 15–90 days | `memory/` | Load only if explicitly relevant. Verify before using. |
| Archived | 91–180 days | `archive/memory/` | Don't load unless user explicitly references. |
| Pruned | 180+ days | Deleted | Reconstruct from current state if needed. |

**Latent memory protocol:** When a file is 15–90 days old — state the memory and its age, cross-check against current evidence, update if stale before concluding.

---

## Layer Separation Rules

1. **One home rule:** Every piece of information lives in exactly one layer. No duplication.
2. **Behavioral-only rule:** CLAUDE.md contains zero reference material.
3. **Read-before-respond rule:** Any workflow referencing a file must read it before commenting on its content.
4. **Memory-not-conversation rule:** Session state lives in memory files, not conversation history.
5. **Explicit-over-ambient rule:** Skills are invoked explicitly. Nothing ambient loads because it "might be relevant."
6. **Archive-before-delete rule:** Move files to `archive/` rather than deleting.

---

## Cross-System Interaction Rules

**Retrieval → Budget:** A retrieval pushing non-conversation overhead past 4,000 tokens requires compressing prior context before loading.

**Memory → Reasoning:** When a latent memory conflicts with current observable evidence, reason from evidence. Surface the conflict. Update the memory before concluding.

**Anti-Pattern → Routing:** A P0 anti-pattern (CLAUDE.md at 2× budget, echo chamber detected) suspends normal routing. Surface and fix before continuing any workflow.

---

## Maintenance Schedule

| Cadence | Action |
|---------|--------|
| Monthly | `/context-audit` — full diagnostic sweep |
| Per session | Budget check if overhead feels heavy |
| On anti-pattern signal | Immediate repair (`architecture/ANTI-PATTERNS.md`) |
| Quarterly | Memory archive pass |
| On skill addition | Update routing tables in CLAUDE.md |
| On file rename/move | Retrieval hygiene check |

---

## Anti-Patterns

| Anti-Pattern | Cost | Fix |
|---|---|---|
| Pre-loading all memory files | ~3,000 tokens wasted | Load only what the task needs |
| Reading full files before indexes | Miss relevance signals | Index-first, always |
| Bulk-globbing entire directories | Reads irrelevant files | Date or topic filter first |
| Re-reading files already in context | Token redundancy | Track what's been read in session |
| Loading skills "just in case" | Context dilution | Skills load only on invocation |
| CLAUDE.md absorbing reference material | Over-budget always-on context | Move to `architecture/` |

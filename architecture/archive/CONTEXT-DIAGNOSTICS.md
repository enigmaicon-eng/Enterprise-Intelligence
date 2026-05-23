# Context Diagnostics
## Health Checks, Severity Classification, and Repair Protocols

Context diagnostics is the system for detecting and measuring context health degradation before it affects output quality. This document defines the diagnostic dimensions, severity model, repair protocols, and the checklist run by `/context-audit`.

---

## Severity Model

Every diagnostic finding is classified by severity.

| Severity | Meaning | Response |
|----------|---------|---------|
| **P0 — Critical** | Context health is actively degraded. Outputs are likely wrong or inconsistent. | Fix immediately before any workflow. |
| **P1 — Warning** | Degradation is building. Not yet affecting output quality but will soon. | Fix before the next session. |
| **P2 — Maintenance** | Minor hygiene issues. No immediate impact. | Fix this month. |
| **Pass** | Dimension is healthy. | No action. |

---

## Diagnostic Dimensions

### D1 — CLAUDE.md Health
**What degrades here:** Layer 1 grows beyond its behavioral-only role by absorbing reference material.

| Check | Threshold | Severity |
|-------|-----------|---------|
| CLAUDE.md token count | > 1,500 tokens → P0 | > 1,000 tokens → P1 |
| CLAUDE.md contains reference tables beyond routing | Any → P1 | |
| CLAUDE.md contains workflow step sequences | Any → P1 | |
| CLAUDE.md contains knowledge content | Any → P0 | |

**Measurement:** Estimate token count: file size in bytes ÷ 4.
**Fix:** Move reference material to `architecture/`. Move workflow steps to `skills/<name>/SKILL.md`. Move knowledge to `knowledge/<domain>/`.

---

### D2 — Memory Health
**What degrades here:** Memory files become stale, over-sized, or contain session ephemera.

| Check | Threshold | Severity |
|-------|-----------|---------|
| Memory file over token budget | > 500 tokens → P1 | |
| Project memory file not updated | > 14 days → P1 | > 30 days → P0 |
| Session content in memory file | Any → P1 | |
| Memory file not in MEMORY.md index | Any → P1 | |
| MEMORY.md index over 100 lines | > 100 lines → P1 | > 150 lines → P0 |
| Memory file in archive not properly moved | Any → P2 | |

**Measurement:** Count lines in MEMORY.md. Check `updated:` frontmatter on each memory file. Read 3-4 memory files and check for session content.
**Fix per issue:** Compress over-budget files. Update stale project files. Strip session content. Add missing index entries. Archive memory files older than 90 days.

---

### D3 — Knowledge Health
**What degrades here:** Knowledge entries become stale, orphaned, or structurally incomplete.

| Check | Threshold | Severity |
|-------|-----------|---------|
| Knowledge file not in KNOWLEDGE-INDEX.md | Any → P1 | |
| Knowledge entry missing required sections | Any → P1 | |
| Knowledge entry `reviewed:` date | > 90 days → P1 | > 180 days → P2 |
| Dead `[[link]]` reference in knowledge file | Any → P2 | |
| Notes in `notes/raw/` older than 7 days | Any → P2 | |
| Orphaned knowledge file (no backlinks, no index entry) | Any → P1 | |

**Measurement:** Scan KNOWLEDGE-INDEX.md vs. actual files in `knowledge/`. Check `reviewed:` dates. Grep knowledge files for `[[links]]` and verify each exists.
**Fix:** Add missing index entries. Update stale reviews. Resolve dead links. Promote or archive `notes/raw/` files.

---

### D4 — Skill Health
**What degrades here:** Skills become orphaned, over-sized, or diverge from their specs.

| Check | Threshold | Severity |
|-------|-----------|---------|
| Skill command file not in CLAUDE.md routing table | Any → P1 | |
| Skill command file > 2,000 tokens | > 2,000 → P1 | |
| Skill command file diverges from `skills/<name>/SKILL.md` | Any → P1 | |
| Skill not invoked in past 30 days | Any → P2 (review, may be legitimate) | |
| Skill file exists without a `.claude/commands/` entry | Any → P1 | |

**Measurement:** Count commands in `.claude/commands/`. Compare against `skills/README.md`. Estimate token count of each command file.
**Fix:** Add missing routing table entries. Move reference material to `skills/<name>/references/`. Sync command files with skill specs. Archive dead skills.

---

### D5 — Prompt Health
**What degrades here:** Prompts diverge from skills, accumulate quality debt, or go unregistered.

| Check | Threshold | Severity |
|-------|-----------|---------|
| Prompt file not in PROMPT-REGISTRY.md | Any → P2 | |
| Prompt average quality score < 3.5 | Any → P1 | |
| Prompt content diverges from its skill's output spec | Any → P1 | |
| Prompt file > 1,500 tokens | > 1,500 → P2 | |

**Measurement:** Cross-reference `prompts/` directory against PROMPT-REGISTRY.md. Check quality scores in `observability/quality.jsonl`.
**Fix:** Register missing prompts. Revise low-scoring prompts. Sync prompts with skill specs.

---

### D6 — Retrieval Health
**What degrades here:** Indexes become stale, pointers break, or retrieval pathways are blocked.

| Check | Threshold | Severity |
|-------|-----------|---------|
| Dead file pointer in any index | Any → P0 (blocks retrieval) | |
| Index not updated after file rename/move | Any → P1 | |
| Domain without an index | Any → P2 | |
| KNOWLEDGE-INDEX.md not updated after new entry added | Any → P1 | |
| Broken `[[link]]` in knowledge file | Any → P2 | |

**Measurement:** Read each domain index. Cross-reference against actual files. Check for files that exist without index entries.
**Fix:** Repair broken pointers immediately (P0). Update indexes after any file operation. Add indexes to unstructured domains.

---

### D7 — Budget Health
**What degrades here:** Context overhead grows beyond the 4,000-token non-conversation target.

| Check | Threshold | Severity |
|-------|-----------|---------|
| CLAUDE.md + MEMORY.md index overhead | > 1,500 tokens → P1 | > 2,000 tokens → P0 |
| Any skill command file | > 2,000 tokens → P1 | |
| Total memory file load for a session | > 3,000 tokens → P1 | |
| Total non-conversation overhead | > 5,000 tokens → P0 | |

**Measurement:** Estimate token counts using file size ÷ 4. Sum CLAUDE.md + MEMORY.md + 2-3 memory files.
**Fix:** Prune CLAUDE.md. Archive stale memory files. Refactor over-budget skill files.

---

### D8 — Layer Separation Health
**What degrades here:** Content appears in the wrong layer (cross-contamination).

| Check | Threshold | Severity |
|-------|-----------|---------|
| Behavioral rules outside CLAUDE.md | Any → P0 | |
| Knowledge content in memory files | Any → P1 | |
| Ephemeral session content in memory | Any → P1 | |
| Current-state facts in knowledge files | Any → P1 | |
| Workflow steps in CLAUDE.md | Any → P1 | |

**Measurement:** Sample 3-4 files per layer and check if content matches the layer contract in `CONTEXT-ARCHITECTURE.md`.
**Fix:** Move content to its correct layer per the layer contracts. Update index entries.

---

## Context Degradation Signals

These signals in session behavior indicate context health problems before you run a full audit:

| Signal | Likely Cause | Diagnostic Dimension |
|--------|-------------|---------------------|
| Model seems to "forget" instructions across a session | CLAUDE.md too large; behavioral rules diluted | D1, D7 |
| Inconsistent output format across similar tasks | Prompt/skill divergence | D4, D5 |
| Retrieval failing on known topics | Stale index, broken pointer | D6 |
| Sessions feel slow to orient | Memory files over-loaded or stale | D2 |
| Knowledge entries returning outdated information | Stale knowledge entries | D3 |
| Skills not routing correctly | Routing table not updated | D4 |
| Context feels "heavy" mid-session | Budget overhead over threshold | D7 |

---

## Diagnostic Checklist (Run by `/context-audit`)

```
D1 — CLAUDE.md Health
  [ ] Token count < 1,000 tokens (estimate: file size ÷ 4)?
  [ ] Zero reference tables beyond routing?
  [ ] Zero workflow steps?
  [ ] Zero knowledge content?

D2 — Memory Health
  [ ] All memory files in MEMORY.md index?
  [ ] All memory files < 500 tokens?
  [ ] All project memory files updated within 14 days?
  [ ] Zero session content in memory files?
  [ ] MEMORY.md index < 100 lines?

D3 — Knowledge Health
  [ ] All knowledge files in KNOWLEDGE-INDEX.md?
  [ ] All entries have required sections?
  [ ] All entries reviewed within 90 days?
  [ ] Zero dead [[links]]?
  [ ] Zero notes/raw/ files older than 7 days?

D4 — Skill Health
  [ ] All skills in CLAUDE.md routing table?
  [ ] All command files < 2,000 tokens?
  [ ] All command files match their SKILL.md spec?
  [ ] All skills invoked at least once in 30 days (or deliberate exception noted)?

D5 — Prompt Health
  [ ] All prompts in PROMPT-REGISTRY.md?
  [ ] All prompts quality score >= 3.5?
  [ ] All prompts in sync with their skill specs?

D6 — Retrieval Health
  [ ] Zero dead pointers in any index?
  [ ] All indexes current after recent file operations?
  [ ] All domains have a discoverable index?

D7 — Budget Health
  [ ] CLAUDE.md + MEMORY.md index < 1,500 tokens total?
  [ ] All skill command files < 2,000 tokens?
  [ ] No skill command file > 2,500 tokens?

D8 — Layer Separation Health
  [ ] Zero behavioral rules outside CLAUDE.md?
  [ ] Zero knowledge content in memory/?
  [ ] Zero session content in memory/?
  [ ] Zero workflow steps in CLAUDE.md?
```

**Scoring:** Count checks passed / total checks. 
- 38-40 passing: Healthy
- 32-37 passing: Warning — schedule fixes
- < 32 passing: Degraded — run repair before next workflow

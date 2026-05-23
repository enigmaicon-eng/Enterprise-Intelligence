---
name: reliability-check
description: >-
  Cross-layer operational reliability check — validates consistency across all
  four state layers: runtime/ (workflow state), traces/ (execution history),
  memory/ (orientation files), knowledge/ (entries and index). Finds broken
  file references, orphaned index entries, and cross-layer inconsistencies
  that no single-layer tool catches. Distinct from /runtime-validate (runtime
  only), /knowledge-qa (entry quality), and /ops-dashboard (health metrics).
  Run after disruption, environment change, or weekly as continuity check.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (cross-layer reliability report)
---

# /reliability-check — Cross-Layer Reliability Check

## When to Use

- After machine restart, environment change, or file system operations
- Before a major knowledge synthesis or strategy session
- Weekly as part of the operational continuity protocol
- When a retrieval or recovery skill returns "file not found" unexpectedly

**Do NOT use for:**
- Runtime-specific state integrity → `/runtime-validate`
- Snapshot recoverability → `/snapshot-verify`
- Entry quality scoring → `/knowledge-qa`
- Gap and synthesis opportunity detection → `/knowledge-gap`

**This is a broad check — run after disruption, not on every session start.**

---

## Input

```
/reliability-check              ← All 4 layers
/reliability-check --runtime    ← Runtime layer only (use /runtime-validate instead for full runtime validation)
/reliability-check --traces     ← Trace layer only
/reliability-check --memory     ← Memory layer only
/reliability-check --knowledge  ← Knowledge layer only
```

---

## Layers and What Is Checked

### Layer 1 — Runtime

**Check R1:** Completed workflows in `runtime/state/workflow-history.json` that are NOT in `traces/TRACE-INDEX.md` — execution memory gap. These workflows completed but left no trace. Not a hard error, but a capture gap.

**Check R2:** Active workflow plan files (`runtime/plans/{wf-id}.json`) reference output paths — check that parent directories for those paths exist. A plan referencing `synthesis/2026-05-22-foo.md` requires `synthesis/` to exist.

### Layer 2 — Traces

**Check T1:** Every `exec_*` row in `traces/TRACE-INDEX.md` should have a corresponding file in `traces/executions/`. Entries pointing to non-existent files break `/trace-recall` and `/exec-inspect`.

**Check T2:** Every `pat_*` row in the patterns table should have a file in `traces/patterns/`. Orphaned index entries cause pattern lookup failures.

**Check T3:** Every `prim_*` row in the primitives table should have a file in `traces/primitives/`. Same as T2.

**Check T4:** Journal entries in the journal table should have corresponding files in `traces/journal/`. Missing journal files break `/trace-search`.

### Layer 3 — Memory

**Check M1:** Every file path referenced in `memory/MEMORY.md` (the index) should exist as an actual `.md` file in `memory/`. Dangling entries in the index corrupt future orientation recall.

**Check M2:** Every file path referenced in `C:\Users\DELL\.claude\projects\C--Users-DELL-Enterprise-Intelligence-Workspace\memory\MEMORY.md` (the auto-memory index) should exist in that memory directory.

**Check M3:** Each memory file should be readable and contain valid frontmatter (`name`, `type` fields). A memory file that's blank or malformed is silent corruption — it appears to exist but carries no content.

### Layer 4 — Knowledge

**Check K1:** Every entry in `knowledge/KNOWLEDGE-INDEX.md` should correspond to a file in `knowledge/<domain>/`. Entries pointing to missing files cause `/recall` and `/knowledge-qa` failures.

**Check K2:** Every node ID in `knowledge/KNOWLEDGE-GRAPH.json` should have a corresponding entry in `knowledge/KNOWLEDGE-INDEX.md`. Graph nodes with no index entry are orphaned graph nodes.

**Check K3:** Every cluster document path referenced in any skill or KNOWLEDGE-INDEX entry should exist in `knowledge/clusters/`. Missing cluster documents break synthesis coverage detection in `/knowledge-gap`.

---

## Process

### Step 1 — Read all index files

Read (in parallel):
- `runtime/state/workflow-history.json`
- `traces/TRACE-INDEX.md`
- `memory/MEMORY.md`
- `knowledge/KNOWLEDGE-INDEX.md`
- `knowledge/KNOWLEDGE-GRAPH.json`

If any index file is unreadable: report it and skip that layer's checks. Do not abort the whole check.

### Step 2 — Run all checks by layer

For each check, compile a list of: (check ID, finding, severity, affected item, recommended action).

Severity levels:
- **INVALID**: broken reference in a critical index that blocks a skill's operation
- **WARNING**: orphaned entry or gap that degrades but doesn't block
- **INFO**: capture gap (e.g., completed workflow with no trace) — informational, not a reliability problem

### Step 3 — Deduplicate and prioritize

Sort findings: INVALID first, then WARNING, then INFO. Group by layer.

### Step 4 — Generate remediation map

For each INVALID or WARNING finding, map to a specific remediation action:

| Finding | Remediation |
|---------|------------|
| TRACE-INDEX row → missing file | Remove the row or restore the file; run `/trace-capture` to re-capture if session data is available |
| MEMORY.md → missing file | Remove the dangling index entry from MEMORY.md; recreate the memory file if content is known |
| KNOWLEDGE-INDEX → missing file | Remove the index entry; re-add entry with `/learn` or `/promote` if source is available |
| GRAPH node → missing index entry | Run `/knowledge-connect` to re-establish the entry; or remove the orphaned graph node |
| Workflow → no trace | Run `/trace-capture` with retrospective session data; or accept the gap |

---

## Output Format

```
RELIABILITY CHECK — [YYYY-MM-DD HH:MM]
Layers checked: [Runtime / Traces / Memory / Knowledge]

── LAYER 1: RUNTIME ──
R1 — History → Traces: [N] completed workflows with no trace
  [wf-id] "[name]" — completed [date], no TRACE-INDEX entry
  → /trace-capture (retrospective) or accept gap
R2 — Plan output directories: [N] paths with missing parent directories
  [or: ✓ All plan output directories exist]

── LAYER 2: TRACES ──
T1 — Execution files: [N] TRACE-INDEX rows → missing files
  exec_[id] → traces/executions/[filename] — FILE NOT FOUND
  → Remove row from TRACE-INDEX or restore file
T2 — Pattern files: [N] index rows → missing files  [or: ✓ all present]
T3 — Primitive files: [N] index rows → missing files  [or: ✓ all present]
T4 — Journal files: [N] index rows → missing files  [or: ✓ all present]

── LAYER 3: MEMORY ──
M1 — Workspace memory index: [N] dangling entries
  [filename.md] — referenced in MEMORY.md but file not found
  → Remove entry or recreate file
M2 — Auto-memory index: [N] dangling entries  [or: ✓ all present]
M3 — Memory file health: [N] files with invalid/missing frontmatter
  [filename.md] — [blank / missing 'name' field / missing 'type' field]

── LAYER 4: KNOWLEDGE ──
K1 — Knowledge index → files: [N] entries → missing files
  [entry-id] "[title]" → knowledge/[domain]/[filename] — FILE NOT FOUND
K2 — Graph → index: [N] orphaned graph nodes
  Node [id] — present in KNOWLEDGE-GRAPH.json but not in KNOWLEDGE-INDEX
K3 — Cluster docs: [N] referenced cluster files missing  [or: ✓ all present]

SUMMARY
INVALID: [N]   WARNING: [N]   INFO: [N]
[Priority remediation: the single most important issue to fix first]
[Or: ✓ All layers coherent. No cross-layer integrity issues found.]
```

---

## Quality Gate

Before outputting:
- [ ] All four index files read; layer skipped (not crashed) if any is unreadable
- [ ] File existence confirmed by attempted read, not inferred from index structure
- [ ] INVALID vs WARNING distinction applied consistently (INVALID = blocks a skill operation)
- [ ] INFO entries (capture gaps) listed separately from reliability issues
- [ ] Zero-issue layers show "✓ all present" — not silently omitted
- [ ] Remediation action given for every INVALID and WARNING finding
- [ ] Summary names the single highest-priority fix, not a list of all findings

# Retrieval System
## Pipeline, Hygiene, and Optimization

Retrieval is the process of identifying which files to read and in what order. Done well, retrieval finds maximum relevant signal at minimum token cost. Done poorly, it either misses content or floods context with irrelevant material.

This document defines the retrieval pipeline, hygiene rules, and optimization heuristics for the workspace.

---

## The 5-Mode Retrieval Pipeline

Every retrieval starts with mode selection. Match the mode to what you know.

```
Mode 1 — Direct
  When: You know the exact file path.
  Action: Read the file. No index lookup needed.
  Cost: 1 read.
  Example: "Read memory/user_profile.md"

Mode 2 — Index-First
  When: You know the domain but not the specific file.
  Action: Read the domain index → identify the relevant file → read it.
  Cost: 1 index read + 1 content read.
  Example: Knowledge lookup → read KNOWLEDGE-INDEX.md → read target file

Mode 3 — Grep
  When: You know keywords or a concept name but not the domain.
  Action: Grep the relevant directory for the keywords → identify matches → read top 2-3.
  Cost: 1 grep + 2-3 reads.
  Example: Searching for a decision → grep decision-frameworks/ for the topic

Mode 4 — Cluster
  When: The topic spans multiple domains or you need a holistic view.
  Action: Read the relevant cluster file → follow its links to component files.
  Cost: 1 cluster read + N component reads (N bounded by the cluster).
  Example: "How does context engineering relate to memory?" → read clusters/ai-systems.md

Mode 5 — Skip (Generate)
  When: The topic is not in the workspace (confirmed by index scan + grep).
  Action: Generate from capability. Note the gap explicitly. Suggest /learn or /capture.
  Cost: 0 reads.
  Example: No entry for "negotiation frameworks" → generate, note gap
```

**Mode selection order:** If you don't know the path → don't start with grep. Check if an index exists first (Mode 2). Indexes are cheaper than grep, and grep is cheaper than reading wrong files.

---

## Index Registry

Every domain has an authoritative index. Read the index before reading content.

| Domain | Index File |
|--------|-----------|
| Knowledge | `knowledge/KNOWLEDGE-INDEX.md` |
| Memory | `memory/MEMORY.md` |
| Prompts | `prompts/PROMPT-REGISTRY.md` |
| Skills | `skills/README.md` |
| Syntheses | List files in `synthesis/` by date; read frontmatter |
| Decisions | `decision-frameworks/decisions-log.md` (scan headings) |
| Meetings | `meeting-intelligence/processed/` (date-filter by Glob) |
| Execution | `execution/active-initiatives.md` |
| Strategy | `strategy/STRATEGY-OS.md` (scan headings) |

**Rule:** If a domain doesn't have an index, the domain is unstructured. Prefer grep over directory scan for unstructured domains.

---

## Pre-Retrieval Optimization

Apply these before any read to avoid wasted tokens:

**Date filter first.** If the retrieval is time-scoped (this week's meetings, last month's reviews), filter by date via Glob pattern before reading. `meeting-intelligence/processed/2026-05-*.md` is cheaper than listing all processed meetings.

**Size-check large files.** For files likely >100 lines (synthesis memos, weekly reviews, strategy docs), read first 50 lines (limit: 50) to verify relevance before committing to a full read. If the first 50 lines don't show relevance: skip.

**Don't re-read within a session.** Files read earlier in the session are already in context. Reading them again wastes tokens with no new information, unless the file was updated mid-session.

**Follow pointers, don't infer.** If an index entry says `knowledge/technical/ai-systems.md`, read that file. Don't infer there's a related file at `knowledge/technical/ai-overview.md` without checking the index first.

---

## Post-Retrieval Scoring

After reading a file, verify it's actually relevant before using its content:

```
Relevance check (takes <5 seconds of reasoning):
  1. Does this file address the current task?
  2. Is the content current (reviewed: date within 90 days for knowledge files)?
  3. Does it have information not already in context?

If any check fails:
  → Not relevant to task: discard from working context. Don't cite it.
  → Stale (>90 days): flag as potentially outdated. Use with caveat or verify first.
  → Redundant: discard. Use the version already in context.
```

---

## Retrieval Hygiene

Hygiene is the ongoing maintenance that keeps retrieval working accurately over time.

### Stale Pointer Detection

A stale pointer is a reference to a file that no longer exists at its stated path, or whose content no longer matches what the reference implies.

**Detection triggers:**
- A read returns "file not found" for a path listed in an index
- An index entry describes content that contradicts the file's actual content
- A `[[linked-concept]]` reference in a knowledge file points to a deleted entry

**Repair protocol:**
1. Identify the broken reference location (which index or knowledge file contains it).
2. Either: (a) update the pointer to the correct path, or (b) remove the pointer if the target was intentionally deleted.
3. Note the repair in the index's `updated:` date.
4. Don't proceed with the original workflow until the pointer is repaired.

### Index Gap Detection

An index gap is a file that exists in the filesystem but has no entry in its domain's index.

**Detection:** When a Glob or Grep returns a file that isn't in the relevant index.

**Repair:** Add the file to the index immediately. An un-indexed file is an orphan (Anti-Pattern 2).

### Dead Link Detection

A dead link is a `[[concept]]` reference in a knowledge file that has no corresponding entry in `KNOWLEDGE-INDEX.md`.

**Detection:** When you encounter `[[concept]]` and the concept doesn't appear in KNOWLEDGE-INDEX.md.

**Repair:** Either: (a) create the knowledge entry (if the concept deserves one), or (b) remove the `[[concept]]` reference if the concept isn't needed.

### Freshness Decay Rules

| File Type | Freshness Threshold | Action if Stale |
|-----------|---------------------|----------------|
| Memory files (projects) | 14 days | Verify before relying on |
| Knowledge entries | 90 days | Flag as potentially outdated |
| Synthesis memos | 180 days | Check if superseded by newer synthesis |
| Decision log entries | Never stale | Historical record; read as-is |
| Processed meetings | Never stale | Historical record; read as-is |
| Strategy files (bets, OKRs) | 30 days | Flag if not updated during review cycle |

---

## Knowledge Graph Retrieval (Scoring + Traversal)
## Absorbed from: RETRIEVAL-INTELLIGENCE.md

For knowledge entries in `knowledge/` indexed in KNOWLEDGE-GRAPH.json, apply this composite scoring algorithm.

### Composite Score Formula

```
score = (keyword_match × 0.45)
      + (confidence_weight × 0.20)
      + (recency_weight × 0.15)
      + (connection_density × 0.10)
      + (tag_match × 0.10)
```

| Component | Score mapping |
|-----------|-------------|
| keyword_match | Full title match: 1.0 · Partial (≥2 keywords): 0.7 · Tag only: 0.4 · Body: 0.3 |
| confidence_weight | high: 1.0 · medium: 0.7 · low: 0.3 |
| recency_weight | ≤30d: 1.0 · 31-90d: 0.8 · 91-180d: 0.6 · 181-365d: 0.4 · >365d: 0.3 |
| connection_density | +0.04 per direct neighbor, capped at 0.20 |
| tag_match | ≥3 matching tags: 1.0 · 2 tags: 0.7 · 1 tag: 0.4 |

Threshold interpretation: >0.70 = high confidence · 0.40–0.70 = moderate, surface with note · <0.40 = weak, surface only if no better match.

### Graph Traversal

After identifying primary match(es), traverse 1 hop only. Surface top 3 neighbors by composite score. Exclude `contradicts` edges from "Also see" — surface them separately as "Note: conflicting entry." Do not traverse to entries with `confidence: low` unless no high-confidence results exist.

### Gap Signals

| Gap type | Signal |
|---------|--------|
| Hard gap | No match → "No entries for [query]. Use /learn to capture." |
| Soft gap | Match in cluster with no synthesis → "Found N entries. No synthesis exists. Consider /knowledge-cluster." |
| Connection gap | Entry found, 0 connections → "This entry has no graph connections. Consider /knowledge-connect." |
| Stale gap | Entry found, reviewed >365d → flag with age |

---

## Retrieval Anti-Patterns

| Anti-Pattern | Cost | Fix |
|---|---|---|
| Reading without index check | Wrong files, wasted tokens | Index-first, always |
| Bulk-reading a directory | N irrelevant reads | Filter by date or topic before reading |
| Following a `[[link]]` without checking if it's in-scope | Context bloat | Only follow links if the current task needs that concept |
| Re-reading a file already in context | Token redundancy | Track what's been read this session |
| Reading a file to "see what's there" | Speculative loading | Only read files that the current workflow step explicitly requires |
| Treating a 90-day-old knowledge file as authoritative | Stale reasoning | Apply freshness check; flag if stale |
| Skipping the size check on large synthesis files | Over-reading | Read first 50 lines; commit to full read only if relevant |

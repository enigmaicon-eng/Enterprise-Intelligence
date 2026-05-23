# /knowledge-graph — Graph Diagnostics and Health

Read-only view of knowledge graph statistics: node/edge counts, isolated entries, connection density, cluster candidates, never-accessed entries, and compounding velocity.

## Trigger
`/knowledge-graph` — full health summary.
`/knowledge-graph --stats` — numbers only (fast).
`/knowledge-graph --orphans` — isolated entries with no connections.
`/knowledge-graph --candidates` — cluster synthesis candidates.
`/knowledge-graph --gaps` — never-accessed entries.
`/knowledge-graph --top` — most-connected entries.

## Protocol

### Full health summary: `/knowledge-graph`

**Step 1:** Run `python scripts/knowledge_index.py --stats` and `python scripts/knowledge_search.py --gaps` and `python scripts/knowledge_index.py --orphans` and `python scripts/knowledge_index.py --candidates`.

**Step 2:** Load `knowledge/KNOWLEDGE-GRAPH.json` for supplemental data (compounding velocity, cluster list, access stats).

**Step 3:** Present the consolidated health report:

```
Knowledge Graph Health
══════════════════════════════════════════════
  Nodes          : [N]
  Edges          : [N]
  Clusters       : [N]
  Isolated nodes : [N]  ([N]% of graph)
  Avg connections: [N.N]

  Compounding velocity:
    Total compound events: [N]
    Connections created  : [N edges in graph]
    Clusters synthesized : [N]
    Reviews completed    : (see COMPOUNDING-LOG.md)

  Coverage gaps:
    Never accessed       : [N] entries
    Never reviewed       : [N] entries
    Low confidence       : [N] entries

  Cluster candidates (≥5 connections):
    [node_id]  —  [N] connections  —  [title]
    ...

  Top-connected entries:
    [node_id]  —  [N] edges  —  [title]
    ...

══════════════════════════════════════════════
  Next actions:
  → /knowledge-connect --discover   (if isolated > 20%)
  → /knowledge-cluster [node_id]    (if cluster candidates exist)
  → /knowledge-review               (if never-reviewed > 0)
  → /learn                          (if domain X is underrepresented)
```

---

### Stats only: `/knowledge-graph --stats`

Run `python scripts/knowledge_index.py --stats`. Print output directly.

---

### Orphan detection: `/knowledge-graph --orphans`

Run `python scripts/knowledge_index.py --orphans`. List isolated nodes with their domain and file path. Append:

```
→ Use /knowledge-connect [node_id] to add connections.
→ Use /knowledge-connect --discover to auto-detect bridges.
```

---

### Cluster candidates: `/knowledge-graph --candidates`

Run `python scripts/knowledge_index.py --candidates`. List nodes ready for cluster synthesis. Append:

```
→ Use /knowledge-cluster [node_id] to synthesize.
```

---

### Never-accessed entries: `/knowledge-graph --gaps`

Run `python scripts/knowledge_search.py --gaps`. These are entries that have never been retrieved via `/recall`. High gap count means the graph has knowledge that isn't being used.

Append:
```
→ Use /recall [topic] to access — access tracking kicks in on first retrieval.
→ Consider whether entries with 0 accesses in 90+ days are still relevant.
```

---

### Top-connected entries: `/knowledge-graph --top`

Load `KNOWLEDGE-GRAPH.json`. Count edges per node. Show top 10 sorted by connection count, with title, domain, confidence, and compound_events count.

These are the compounding hubs of the graph — the entries whose value grows fastest as new knowledge is added.

## What This Is Not

This is a diagnostic tool — read-only. No writes happen.

- To add connections: `/knowledge-connect`
- To synthesize a cluster: `/knowledge-cluster`
- To trigger reviews: `/knowledge-review`
- To rebuild the index after manual edits: `python scripts/knowledge_index.py`

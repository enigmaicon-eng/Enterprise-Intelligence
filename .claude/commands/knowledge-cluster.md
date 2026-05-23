# /knowledge-cluster — Synthesize a Knowledge Cluster

Synthesize 5 or more connected knowledge entries into a single cluster document that surfaces shared patterns, tensions, and emergent insight.

## Trigger
`/knowledge-cluster [topic or center_node_id]` — synthesize a cluster around a node or topic.
`/knowledge-cluster --list` — show all cluster synthesis candidates.
`/knowledge-cluster --view [cluster_id]` — read an existing cluster.

## When to Use

When a knowledge area has reached ≥5 connected entries, their individual value is less than the synthesized whole. Cluster synthesis is the primary compounding event — it converts a collection into a generative insight that produces better retrieval, surfaces tensions, and enables strategic reuse.

Triggered automatically as a suggestion by `/knowledge-connect` when a node reaches 5 connections.

## Protocol

### List candidates: `/knowledge-cluster --list`

Run: `python scripts/knowledge_index.py --candidates`

Output the list of cluster synthesis candidates (nodes with ≥4 neighbors = 5-node clusters). Show for each: center node, neighbor count, domain.

---

### Synthesize: `/knowledge-cluster [topic or center_node_id]`

**Step 1: Identify cluster members.**

Load `knowledge/KNOWLEDGE-GRAPH.json`. If a `center_node_id` is given, collect:
- The center node
- All 1-hop neighbors (nodes directly connected to center)

If a topic keyword is given instead, run `python scripts/knowledge_search.py "[topic]"` to find the top-scoring node, then use that as center.

Abort if fewer than 5 nodes are in the cluster. Report: "Cluster needs ≥5 entries. Currently [N]. Use /knowledge-connect to add more connections."

**Step 2: Read all cluster member files.**

Read each member's `.md` file from the `file` field in the graph. Extract key claims, confidence levels, tags, and reviewed dates.

**Step 3: Present cluster for operator confirmation.**

```
Cluster synthesis proposal:
  Topic: [derived topic name]
  Members ([N] entries):
    1. [node_id] — [title]  ([domain], [confidence])
    2. ...

  I will synthesize these into: knowledge/clusters/[slug].md

Proceed? (yes / cancel / adjust members)
```

Do not write until confirmed.

**Step 4: Generate the cluster synthesis.**

Write `knowledge/clusters/[slug].md` using the cluster synthesis template:

```markdown
---
title: [Cluster Title]
type: cluster
id: clusters/[slug]
members:
- [node_id_1]
- [node_id_2]
- ...
synthesized: [YYYY-MM-DD]
confidence: [highest confidence across members]
tags: [union of member tags, de-duped]
domain: clusters
reviewed: [YYYY-MM-DD]
---

# [Cluster Title]

## Core Claim
[The single most important insight that emerges from reading all members together — not a summary, a synthesis. What do you know *because* these entries coexist that you wouldn't know from any one alone?]

## Shared Themes
[2–4 themes that appear across ≥3 member entries, with specific evidence]

## Cross-Entry Patterns
[Structural patterns — recurring mechanisms, shared dynamics, underlying logic that spans entries]

## Tensions and Open Questions
[Where do members contradict or bound each other? What remains unresolved?]

## Synthesized Insight
[The generative conclusion — the highest-leverage insight this cluster enables. Should be actionable or orienting.]

## Members
[For each member: one-line description of its specific contribution to this cluster]
```

**Step 5: Add `synthesizes` edges to the graph.**

For each cluster member, add an edge:
```json
{
  "from": "clusters/[slug]",
  "to": "[member_node_id]",
  "type": "synthesizes",
  "weight": 1.0,
  "created_at": "[YYYY-MM-DD]",
  "note": "cluster synthesis"
}
```

**Step 6: Add cluster record to graph.**

Add to `clusters` array in `KNOWLEDGE-GRAPH.json`:
```json
{
  "id": "clusters/[slug]",
  "title": "[Cluster Title]",
  "file": "knowledge/clusters/[slug].md",
  "members": ["[node_id_1]", "..."],
  "synthesized": "[YYYY-MM-DD]",
  "member_count": [N]
}
```

**Step 7: Increment compound_events on all member nodes.**
Increment `compound_events` by 1 on each member node in the graph.

**Step 8: Log to COMPOUNDING-LOG.md.**
Append:
```
| [YYYY-MM-DD] | SYNTHESIS | clusters/[slug] ([N] members → knowledge/clusters/[slug].md) |
```

**Step 9: Rebuild index.**
Run: `python scripts/knowledge_index.py`

---

### View existing cluster: `/knowledge-cluster --view [cluster_id]`

Load and display `knowledge/clusters/[slug].md`. Show the synthesis content, member list, and synthesis date. Check if any member files have been updated since the synthesis date — if so, flag:

```
⚠ [N] member entries updated since synthesis ([YYYY-MM-DD]).
  Consider re-synthesizing: /knowledge-cluster [cluster_id]
```

## Output

After synthesis:
```
Cluster synthesized: knowledge/clusters/[slug].md
  Members: [N] entries
  Edges added: [N] synthesizes edges
  Next: /recall [topic] — the cluster will now surface first in graph-scored retrieval.
```

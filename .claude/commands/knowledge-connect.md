# /knowledge-connect — Create and Discover Knowledge Connections

Create explicit connections between knowledge entries, or discover cross-domain bridges automatically.

## Trigger
`/knowledge-connect [from_id] [to_id] [type]` — create a specific connection.
`/knowledge-connect --discover` — scan for high-probability cross-domain bridges.
`/knowledge-connect --view [node_id]` — show all connections for an entry.

## Connection Types

| Type | Meaning |
|------|---------|
| `related_to` | Conceptually adjacent; neither depends on the other |
| `builds_on` | The source entry depends on or extends the target |
| `contradicts` | The source challenges, limits, or reverses the target |
| `applies_to` | The source is an application of the target principle |
| `synthesizes` | Source is a cluster that synthesizes target entries (system use only) |

## Protocol

### Create a connection: `/knowledge-connect [from_id] [to_id] [type]`

**Step 1: Validate both entries exist.**
Load `knowledge/KNOWLEDGE-GRAPH.json`. Confirm both `from_id` and `to_id` appear in `nodes`. If either is missing, report "Node not found" and list similarly-named nodes.

**Step 2: Check for existing connection.**
Scan `edges` for an existing edge between these two nodes (in either direction). If found, report the existing connection and stop.

**Step 3: Present the proposed connection for operator confirmation.**

```
Proposed connection:
  FROM: [from_id] — [title]
  TO:   [to_id]   — [title]
  TYPE: [type]

  Reasoning: [1–2 sentence explanation of why this connection is meaningful]

Confirm? (proceed / cancel)
```

Do not write until confirmed.

**Step 4: Write the connection.**

Add the edge to `KNOWLEDGE-GRAPH.json` edges array:
```json
{
  "from": "[from_id]",
  "to": "[to_id]",
  "type": "[type]",
  "weight": 0.7,
  "created_at": "[YYYY-MM-DD]",
  "note": "[one-line rationale]"
}
```

Weight defaults: `builds_on` = 0.9, `contradicts` = 0.8, `related_to` = 0.7, `applies_to` = 0.7.

**Step 5: Increment compound_events on both nodes.**
In the graph's nodes array, increment `compound_events` on both `from_id` and `to_id` by 1.

**Step 6: Log to COMPOUNDING-LOG.md.**
Append:
```
| [YYYY-MM-DD] | CONNECTION | [from_id] → [to_id] ([type]) |
```

**Step 7: Check cluster formation threshold.**
Count total connections for each node. If either node now has ≥5 neighbors:
```
[node_id] now has [N] connections — cluster synthesis candidate.
Run /knowledge-cluster to synthesize this cluster.
```

Rebuild graph index after writing: `python scripts/knowledge_index.py`.

---

### Discover cross-domain bridges: `/knowledge-connect --discover`

**Step 1:** Load `knowledge/KNOWLEDGE-GRAPH.json`. Collect all isolated nodes (0 connections) and nodes with ≤1 connection.

**Step 2:** For each candidate node, extract its tags and title tokens. Find nodes in *different* domains with overlapping tokens or tags.

**Step 3:** Score candidates by:
- Tag overlap (shared tags across domains = strong signal)
- Title token overlap
- Same confidence level (high-to-high bridging is highest value)

**Step 4:** Present top 5 bridge candidates:
```
Cross-domain bridge candidates:
  1. [node_a] (pm) ←→ [node_b] (strategy)   — shared: [tags]
  2. ...

Select candidates to connect, or type "none".
```

**Step 5:** For each selected pair, run the standard connection flow (Steps 3–7 above).

---

### View connections: `/knowledge-connect --view [node_id]`

Load `KNOWLEDGE-GRAPH.json`. Print all edges involving `node_id`:

```
Connections for: [node_id] — [title]
  Domain: [domain]  |  Confidence: [conf]  |  Compound events: [N]

  Outbound:
    → [to_id] ([type], weight=[w])  — [note]

  Inbound:
    ← [from_id] ([type], weight=[w])  — [note]

  Total: [N] connections
  Cluster threshold: [N]/5 — [at threshold / X away]
```

## Compounding Signal

Every connection creation is a compounding event. The connection density score in retrieval (`connection_density × 0.10`) rises with each edge added, making well-connected entries surface more reliably in future `/recall` queries.

When a node reaches 5 connections, it becomes a cluster synthesis candidate — the compounding threshold where individual entries become collective insight.

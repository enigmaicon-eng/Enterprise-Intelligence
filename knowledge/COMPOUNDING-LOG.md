# Knowledge Compounding Log
## Append-only record of all compound events

Every time knowledge grows through connection, synthesis, enrichment, or review, a record is added here. This is the audit trail of the compounding system.

---

## Event Types

| Type | Description |
|------|-------------|
| `CONNECTION` | Edge created between two knowledge entries |
| `SYNTHESIS` | Cluster synthesis completed |
| `ENRICHMENT` | Existing entry updated with new content |
| `REVIEW` | Entry reviewed; confidence change if any |
| `PROMOTION` | Semantic memory promoted to knowledge entry |
| `GAP_DETECTED` | Retrieval gap logged for follow-up |

---

## Log

| Date | Type | Details |
|------|------|---------|
| — | — | *No compound events yet. Knowledge compounding begins when /knowledge-connect, /knowledge-cluster, or /knowledge-review are first used.* |

---

**Format for new entries:**

```
| YYYY-MM-DD | CONNECTION | pm/product-strategy → pm/metrics-experimentation (related_to) |
| YYYY-MM-DD | SYNTHESIS  | cluster-pm-strategy-core (6 members → knowledge/clusters/pm-strategy-core.md) |
| YYYY-MM-DD | REVIEW     | pm/ai-ml-pm — confidence: medium→high |
| YYYY-MM-DD | GAP        | Query "LLM evals" returned 0 results |
```

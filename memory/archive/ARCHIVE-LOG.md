# Memory Archive Log
## Append-only. One row per archived entry.

| Date Archived | File | Type | Reason | Archive Path |
|---------------|------|------|--------|--------------|
| — | — | — | — | — |

---

When archiving a memory file:
1. Move the file to `memory/archive/YYYY-MM/`
2. Add the `archived_reason: [reason]` field to its YAML frontmatter
3. Append a row to this table
4. Run `python scripts/memory_index.py` to update RETRIEVAL-INDEX.json

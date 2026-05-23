# Memory Lifecycle Rules
## Decay, Review, Archival, and Pruning for P16 Typed Memory

---

## Principles

1. **Memory serves retrieval.** If a memory entry won't be retrieved, it shouldn't exist. Delete aggressively.
2. **Decay is not loss.** Archiving memory to `memory/archive/` preserves it without cluttering active retrieval.
3. **Review dates are contracts.** When a review date passes, the entry must be updated, promoted, or archived within one `/mem-hygiene` run.
4. **No silent mutation.** When an entry is superseded or archived, link the reason. Future-you needs to know why something is gone.
5. **Promote, don't duplicate.** Stable semantic memory belongs in `knowledge/`. Keep it in one place.

---

## Decay Rates by Type

| Type | Decay Rate | Review Interval | Default Review From |
|------|------------|-----------------|---------------------|
| Episodic | Fast | 14 days | `timestamp` |
| Semantic | Medium | 30 days | `last_updated` |
| Decision (ADR) | Slow | 90 days | `date` (or after related event) |
| Execution | Medium | 30 days | `last_updated` |
| Failure | Medium | 30 days | `last_seen` |
| Insight | Slow | 90 days | `last_validated` |
| Context | Medium | 30 days | `as_of` |

---

## Review Actions by Type

### Episodic Review (14 days)
Options:
- **Link it:** Does this episode now connect to a pattern, insight, or decision that wasn't visible at the time? Add links, extend review to 30 days.
- **Archive it:** No links, no lessons learned. Move to `memory/archive/` with a one-line note.
- **Promote it:** Rare — if this episode reveals a recurring pattern, create a failure or insight entry from it.

### Semantic Review (30 days)
Options:
- **Update it:** Understanding has evolved. Edit in place. Update `last_updated` and `review_date`.
- **Promote it:** `confidence: high` and stable for >60 days → promote to `knowledge/<domain>/` and delete this file.
- **Downgrade it:** Confidence has dropped. Set `confidence: low`. If still low at next review, archive.
- **Archive it:** No longer relevant. Move to `memory/archive/`.

### ADR Review (90 days)
Options:
- **Validate it:** Assumptions still hold, decision still correct. Update `review_date` + note in retrospective.
- **Add retrospective:** Update `retrospective` section with what actually happened.
- **Supersede it:** A new decision changes this one. Set `status: superseded`, `superseded_by: dec_*`, and create new ADR.
- **Reverse it:** Decision was wrong. Set `status: reversed`, document why in retrospective. Never delete.

### Execution Review (30 days)
Options:
- **Update it:** Conditions have changed, gotchas have been discovered, estimates have proven wrong. Edit in place.
- **Archive it:** The task type no longer applies. Move to archive with reason.

### Failure Review (30 days)
Options:
- **Update recurrence:** Same failure occurred again. Increment `recurrence_count`, update `last_seen`, add row to Recurrence Log.
- **Archive it:** `recurrence_count = 0` and > 90 days old. Pattern may not be real.
- **Keep it:** `recurrence_count > 1`. These are permanent records.

### Insight Review (90 days)
Options:
- **Validate it:** Pattern still holds. Update `last_validated`.
- **Downgrade it:** `counter_evidence_count` has grown. Set `confidence: low`.
- **Deprecate it:** Evidence no longer supports the claim. Set `status: deprecated`. Write one paragraph explaining what replaced it.

### Context Review (30 days)
Options:
- **Regenerate it:** Topic is still active. Run `/mem-reconstruct` to produce a fresh version. Archive the old one.
- **Complete it:** Topic is resolved. Write a final "completion note" in the body. Archive.
- **Archive it:** Topic was abandoned or became irrelevant.

---

## Archive Protocol

**Archive location:** `memory/archive/YYYY-MM/`
**Archive naming:** Same filename. Add a one-line YAML field `archived_reason: [reason]` to frontmatter.
**Archive index:** Append to `memory/archive/ARCHIVE-LOG.md` with: filename, archive date, reason.

Archive is not deletion. Archived entries are still searchable; they just don't appear in active retrieval.

---

## Prune Protocol

`scripts/memory_prune.py` generates a pruning manifest. It does NOT auto-delete.

**Prune candidates** are entries that are:
- Past their `review_date` by > 30 days (past overdue)
- Episodic with 0 links and timestamp > 90 days ago
- Semantic with `confidence: low` and `last_updated` > 60 days ago
- Context reconstructions older than 30 days on an active topic (need regeneration)

**Output:** `memory/archive/PRUNE-MANIFEST-YYYYMMDD.md` listing each candidate with suggested action.
**Operator approves each action.** No auto-delete.

---

## Promotion Protocol

Semantic memory → knowledge/ when:
1. `confidence: high`
2. No changes to the entry for > 30 days
3. The concept is domain knowledge (not operational pattern)

Promotion steps:
1. Create `knowledge/<domain>/<slug>.md` using the knowledge entry template
2. Copy semantic memory body content, elevate to knowledge format
3. Delete the semantic memory file
4. Run `memory_index.py` to update RETRIEVAL-INDEX.json
5. Update KNOWLEDGE-INDEX.md

---

## Memory Budget

Keep active memory lean:

| Type | Soft Limit | Hard Limit |
|------|------------|------------|
| Episodic | 20 active | 50 (archive all beyond) |
| Semantic | 15 active | 30 |
| Decisions (ADR) | No limit | No limit (permanent) |
| Execution | 10 active | 20 |
| Failure | 15 active | 30 |
| Insights | 10 active | 20 |
| Context | 5 active | 10 |

Beyond the hard limit: archive oldest entries regardless of review date.

---

## Hygiene Cadence

| Frequency | Action |
|-----------|--------|
| Weekly | Run `/mem-hygiene` — surface past-due entries |
| Monthly | Run `python scripts/memory_prune.py` — review prune manifest |
| Quarterly | Full memory audit: check for duplication, orphans, promotion candidates |

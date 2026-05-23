# memory/insights/

Distilled strategic patterns. High bar for entry.

**What goes here:** Patterns that have been observed ≥ 3 times across distinct contexts. Operational insights about how to work, decide, and execute — NOT domain knowledge (that belongs in knowledge/).

**What does NOT go here:** Opinions, one-time observations, domain knowledge, hunches not yet validated by experience.

**When to create:** After the third distinct observation of the same pattern. Not before.

**Quality gate:** Every insight requires ≥ 3 episodic or execution records as evidence. Without links, the insight is not valid.

**Skill:** Write manually; `/mem-recall --type insight` to retrieve
**Schema:** `architecture/MEMORY-SCHEMAS.md` → Schema 6
**File naming:** `ins_SLUG.md` (descriptive, lowercase kebab-case)
**Review interval:** 90 days from `last_validated`
**Deprecation:** When `counter_evidence_count > evidence_count`, set `status: deprecated` with explanation
**Deletion rule:** Never delete — replace deprecated insights with a note about what replaced them

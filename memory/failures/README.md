# memory/failures/

Failure records with causal chains. Prevention-oriented.

**What goes here:** Failures (P13/P15 failure classes F1–F5, or custom), repeated mistakes, root cause analysis with "what not to do" and "what to try instead."

**What does NOT go here:** One-time accidents with no pattern potential, surface-level errors that are self-evident.

**When to create:** After any failure (workflow or cognitive), or when a mistake happens for the second time. Check for an existing record before creating a new one — if same root cause, update the existing record.

**Recurrence rule:** Same failure class + context → increment `recurrence_count` and update `last_seen` on the existing record. Do NOT create a duplicate.

**Skill:** `/mem-failure`
**Schema:** `architecture/MEMORY-SCHEMAS.md` → Schema 5
**File naming:** `fail_YYYYMMDD_NNN.md` (date of first occurrence)
**Review interval:** 30 days from `last_seen`
**Archive trigger:** `recurrence_count = 0` and older than 90 days
**Permanent entries:** Any entry with `recurrence_count > 1` is kept indefinitely

# memory/decisions/

Architecture Decision Records. Full reasoning chains, alternatives considered, assumptions, and retrospective.

**What goes here:** Decisions where alternatives were seriously weighed and the reasoning will matter in 6+ months. System-level, strategy-level, and significant execution decisions.

**What does NOT go here:** Simple choices without real tradeoffs (use decision-frameworks/decisions-log.md instead), tactical micro-decisions.

**When to create:** Any time you rule out a real alternative. If there was only one option, it's not a decision — don't write an ADR.

**Skill:** `/mem-adr`
**Schema:** `architecture/MEMORY-SCHEMAS.md` → Schema 3
**File naming:** `dec_YYYYMMDD_NNN.md`
**Review interval:** 90 days from `date`
**Archive trigger:** `status: superseded` (set `superseded_by`, keep file — never delete)
**Retrospective:** Fill in at `review_date` or when a related decision supersedes this one

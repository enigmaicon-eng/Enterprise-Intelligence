# Maintenance Conventions
## How the Workspace Sustains Itself

---

## The Maintenance Principle

A system that requires heroic maintenance will be abandoned. Every maintenance task in this workspace is either:
1. **Embedded in a workflow** — happens automatically as part of normal use, or
2. **Surfaced by observability** — flagged in the dashboard so it can't be ignored

If a maintenance task is neither embedded nor surfaced, it will be forgotten.

---

## Embedded Maintenance (Zero-Extra-Work)

These happen as a natural byproduct of normal skill invocations:

| Trigger | What Gets Maintained |
|---------|---------------------|
| `/debrief` | Action items updated, decisions logged, raw file marked processed |
| `/weekly` | Action items re-prioritized, memory updated, stale patterns surfaced |
| `/promote` | KNOWLEDGE-INDEX.md updated, back-references added |
| `/capture` urgency=high | Action items updated automatically |
| `/observe` | Dashboard regenerated, flags raised |
| Any skill invocation | Telemetry logged to `telemetry/api-log.jsonl` |

**Target:** 80% of maintenance happens without any additional action by the user.

---

## Observability-Surfaced Maintenance (Weekly Review)

Flags from the dashboard surface in the weekly review as actionable items. Each flag gets a disposition:

- **Fix now** — do it before the weekly review closes
- **This week** — add to action items
- **Accept** — consciously decide the flag is acceptable and note why
- **Remove the check** — if the flag is consistently wrong, update the threshold

No flag should be closed without a disposition.

---

## Monthly Maintenance Checklist

Run these during the first weekly review of each month:

### Anti-Pattern Scan (15 min)
Apply `architecture/ANTI-PATTERNS.md` detection checklist:
- [ ] CLAUDE.md under 1,000 tokens and behavioral-only?
- [ ] MEMORY.md under 100 lines?
- [ ] All knowledge files in KNOWLEDGE-INDEX.md?
- [ ] All skills listed in skills/README.md?
- [ ] All prompts in PROMPT-REGISTRY.md?
- [ ] No orphaned files in notes/raw/ > 7 days?

### Prompt Version Audit (10 min)
- Review prompts with quality scores below 3.5
- For each: revise or explicitly accept the lower quality with a note

### Memory Pruning (10 min)
- Archive project memories for completed projects
- Compress feedback memories that are now obvious / internalized
- Verify reference memories still point to correct locations

### Knowledge Decay Review (10 min)
- Read KNOWLEDGE-INDEX.md and find entries with `reviewed:` > 90 days
- For each: update the entry (even if just refreshing the `reviewed:` date) or archive it

---

## Simplification Rules

When complexity accumulates, apply these rules before adding more:

### Rule 1 — Three Strikes Archive
If a workflow, prompt, or knowledge entry has gone unused for 3 consecutive weeks (visible in dashboard), archive it. Don't maintain dead infrastructure.

### Rule 2 — Merge Before Split
Before creating a new file, check if it belongs as a section in an existing file. A well-structured section beats a new orphan file.

### Rule 3 — Token Budget First
Before adding content to CLAUDE.md or a memory file, estimate the token cost. If adding the content would push the file over budget, find what to remove first.

### Rule 4 — One Source of Truth
If the same fact appears in two places, one is wrong. Find the correct layer and delete the other.

### Rule 5 — Routing Over Repetition
If you need context from a knowledge file frequently, add routing guidance — don't copy the content into CLAUDE.md.

---

## File Lifecycle

```
Creation → Active use → Stale → Archive/Delete

Notes lifecycle:
  notes/raw/ (captured) → notes/structured/ (tagged) → knowledge/ (promoted) → archived (never deleted)
  Rule: notes/raw/ files older than 7 days must be promoted or explicitly not-promoted (moved to notes/archive/)

Meeting lifecycle:
  meeting-intelligence/raw/ → (debrief) → meeting-intelligence/processed/ → (pattern emerges in weekly) → knowledge/
  Rule: raw files must be debriefed within 48 hours

Knowledge lifecycle:
  knowledge/<domain>/ (created) → reviewed periodically → archived if superseded
  Rule: reviewed: date updated at least quarterly; entries not reviewed in 180 days are archived

Memory lifecycle:
  memory/ (created) → updated as state changes → archived when no longer current
  Rule: project memories archived when project is complete; feedback memories compressed when internalized

Reviews lifecycle:
  reviews/weekly/ (current) → archive after 1 year
  reviews/strategy/ (current) → never archived (permanent record)
```

---

## Naming and Versioning Conventions

### File Naming

| Type | Convention |
|------|-----------|
| Meeting files | `YYYY-MM-DD-topic-slug.md` |
| Reviews | `YYYY-WW.md` (weekly) / `YYYY-MM.md` (monthly) |
| Knowledge | `concept-slug.md` |
| Synthesis | `YYYY-MM-DD-topic.md` |
| Memory | `type_slug.md` |
| Telemetry | `api-log.jsonl`, `workflow-log.jsonl` (append-only) |

### Skill and Prompt Versioning

```
version: "MAJOR.MINOR"
MAJOR: breaking change to output format (old outputs incompatible)
MINOR: improvement to workflow steps, quality gate, or non-breaking format changes
```

When bumping version: update frontmatter, add changelog entry, update skills/README.md.

### Commit Convention (if git is initialized)

```
<type>: <scope> — <brief description>

Types: capture | debrief | promote | weekly | strategy | observe | arch | skill | prompt | memory | fix
```

---

## Cognitive Friction Reduction Rules

These rules exist to eliminate the "I'll deal with it later" failure mode:

1. **Capture immediately.** A thought that takes 30 seconds to capture now will take 5 minutes to reconstruct later. Use `/capture` — not a sticky note.

2. **Debrief same day.** Meeting intelligence degrades within 24 hours. Same-day debriefs are 3x more valuable than next-day ones.

3. **Decide explicitly or don't.** If you made a decision, log it with `/decide`. If you didn't make a decision, don't write it as one. The ambiguity is the important thing to capture.

4. **Weekly review is not optional.** It's the garbage collection for the week. Skip it twice and the workspace degrades into a note dump.

5. **One command per workflow.** Don't try to run `/debrief` AND `/promote` AND `/decide` in one session for the same meeting. Pipeline them across sessions. Each command should take <5 minutes of setup.

---

## Red Flags That Require Immediate Attention

These indicate the system is breaking down:

- CLAUDE.md exceeds 1,500 tokens
- `notes/raw/` has files older than 2 weeks
- `execution/action-items.md` has items older than 14 days with no update
- `memory/MEMORY.md` has entries that don't match existing files
- `/observe` hasn't been run in 3+ weeks
- A skill hasn't been invoked in 4+ weeks (and it's supposed to be weekly)
- Telemetry shows 0 cache hits (every call is a cache miss — system prompt is varying)

When a red flag appears: stop normal work, fix the flag, resume.

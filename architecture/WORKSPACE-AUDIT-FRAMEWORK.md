# Workspace Audit + Simplification Framework

Repeatable audit methodology for detecting complexity accumulation, skill ceiling violations, boundary erosion, and architecture drift. Built on the foundations of P20's FINAL-SIMPLIFICATION-REVIEW.md — do not duplicate those AC rules, constraints, or SR findings here.

## Relationship to P20 Simplification Review

`architecture/FINAL-SIMPLIFICATION-REVIEW.md` established:
- 10 Anti-complexity rules (AC-1 through AC-10)
- 8 Autonomy guardrails (A-1 through A-8)
- 7 Orchestration rules (O-1 through O-7)
- Hard operational constraints (skill ceiling 120, arch docs 25, memory 30 files, MEMORY.md 200 lines, ritual stack 6)

This document adds:
- Repeatable audit process (vs one-time P20 review)
- Overlap detection methodology for boundary erosion
- Skill retirement criteria
- Simplification priority scoring
- Current-state tracking model (the constraints were set at 110 skills; we audit against them continuously)

---

## Five Audit Dimensions

Each dimension maps to a specific check in `/workspace-audit`:

### Dimension 1 — Scale Compliance

Are the hard operational constraints still respected?

| Constraint | Source | Check |
|-----------|--------|-------|
| Skills ≤ 120 | AC-7, P20 | Count `.claude/commands/*.md` |
| Architecture docs ≤ 25 | P20 constraint | Count `architecture/*.md` |
| Memory files ≤ 30 | P20 constraint | Count `memory/*.md` (workspace memory) |
| MEMORY.md ≤ 200 lines | P20 constraint | Line count of both MEMORY.md files |
| Ritual stack ≤ 6 | P20 constraint | Count daily ops skills: plan/briefing/focus/prep/shutdown/weekly |
| Skill catalog synced | Hygiene | Compare `.claude/commands/` count vs `skills/README.md` row count |

Violation severity:
- **Critical**: Skills >150 or arch docs >35 — the system is substantially over-built
- **Warning**: Skills 121–150 or arch docs 26–35 — ceiling exceeded, action required
- **OK**: Within constraint bounds

### Dimension 2 — Skill Boundary Health

Are skill boundaries clearly defined? Boundary erosion is the leading cause of redundant invocations and operator confusion.

Indicators of healthy boundaries:
- Skill has a specific "Do NOT use for" section pointing to adjacent skills
- Skill's trigger conditions don't overlap with another skill's trigger conditions
- Skill writes to a declared output path (not "terminal only" without explanation)

Indicators of boundary erosion:
- Two skills answer variations of the same question (same verb phrase in both descriptions)
- One skill's trigger conditions are a subset of another's
- No "Do NOT use for" section despite obvious adjacent skills existing

### Dimension 3 — Usage Evidence

Is there trace evidence that a skill has been invoked? Skills with zero usage over 6+ months and no unique capability are retirement candidates.

Sources:
- `traces/TRACE-INDEX.md` — skill name appearing in session goals or tags
- `traces/executions/` — skill name in trace content
- `skills/README.md` — "Last Invoked" column (if maintained)

Retirement candidate criteria (ALL must be true):
1. Zero trace evidence in last 180 days
2. Functionally overlaps with another skill (not unique capability)
3. OR: was created as infrastructure for a system since simplified (see P20 SR-1 through SR-6)

A skill with zero usage but a unique capability is NOT a retirement candidate — it may be waiting for the right situation.

### Dimension 4 — Architecture Document Currency

Does each architecture document describe the current system, or something modified/removed?

Dead doc indicators:
- Doc mentions a component, script, or skill that no longer exists
- Doc is superseded by a newer, more comprehensive document on the same topic
- Doc describes implementation details of a system retired in SR-1 through SR-6

Live doc indicators:
- Referenced by at least one skill's frontmatter or body
- Referenced by CLAUDE.md
- Describes a system with active skills

### Dimension 5 — Memory Layer Health

Are memory files current, under-limit, and pointing to real projects?

Checks:
- MEMORY.md index entries point to existing `.md` files
- Each memory file has valid frontmatter (`name`, `type`)
- No memory file exceeds 500 tokens (P20 per-file limit)
- No content written into MEMORY.md index (index-only rule)
- Auto-memory MEMORY.md (`.claude/projects/...`) is consistent with workspace memory

---

## Overlap Detection Methodology

Used by `/skill-overlap`. Overlap is not always bad — it may be a well-managed boundary (skill A says "Do NOT use for X; use skill B"). The goal is to distinguish:

**Managed overlap**: Both skills acknowledge each other. Boundaries are explicit. Each skill's "Do NOT use for" redirects to the other for the shared surface.

**Unmanaged overlap**: Two skills answer similar questions without acknowledging each other. Neither has a "Do NOT use for" pointing at the other. Operator must read both descriptions to choose.

**Full redundancy**: One skill is strictly a subset of another's capability with no unique surface. The narrower skill can be retired or merged.

### Overlap Score (per skill pair)

Score each pair 0–4:

| Signal | Score |
|--------|-------|
| Same primary verb in description (e.g., both "analyzes execution traces") | +1 |
| Same output type (both write to same directory / both terminal only) | +1 |
| Trigger conditions overlap (both fire on similar operator intents) | +1 |
| Neither has "Do NOT use for" pointing at the other | +1 |

Score interpretation:
- 0–1: Well-differentiated or managed boundary
- 2: Potential overlap — review for missing boundary documentation
- 3–4: Significant overlap — candidate for merge or retirement

---

## Retirement Priority Model

Used by `/simplify`. Retirement candidates are ordered by this priority:

| Priority | Criterion |
|----------|----------|
| 1 (highest) | Skill is infrastructure for a removed system (SR-1 through SR-6 remnants) |
| 2 | Skill has overlap score 4 AND zero usage in 180 days |
| 3 | Skill has overlap score 3 AND zero usage in 90 days |
| 4 | Skill is strictly superseded (the other skill now explicitly covers its full surface) |
| 5 | Skill was created as a one-off and its use case hasn't recurred (AC-7 note) |

Merge candidates: skills with overlap score 3–4 AND both have usage evidence — merge the less-used into the more-used as a subcommand or `--flag`.

---

## Simplification Scoring

Each simplification action is scored for impact vs effort:

| Action | Impact | Effort |
|--------|--------|--------|
| Retire an unused skill | Medium (reduces cognitive load) | Low (delete file + update registry) |
| Retire an infrastructure skill for removed system | High (clears dead weight) | Low |
| Merge two overlapping skills | High (eliminates decision cost) | Medium (edit both files + test) |
| Archive an outdated arch doc | Medium | Low |
| Add "Do NOT use for" boundary to skill | Low (documentation) | Very low |
| Clean stale memory file | Low | Very low |

Target simplification: any session that removes more than it adds (net negative complexity) succeeds.

---

## Audit Cadence

| Cadence | Trigger | Action |
|---------|---------|--------|
| Quarterly | Calendar or after 3+ new P-series phases | `/workspace-audit` + `/simplify` → execute top 3 recommendations |
| After any new system (P-series) | Adding 3+ skills | `/workspace-audit` to check ceiling compliance |
| Before quarterly strategy review | | `/skill-overlap` on strategy + cognitive sections |
| When workspace feels cluttered | | `/workspace-audit --quick` (dimension 1 only) |

---

## Anti-Patterns

| Anti-pattern | Why it fails |
|-------------|-------------|
| Auditing without simplifying | Audit that produces a report but no deletions adds cognitive overhead rather than reducing it |
| Retiring skills by invocation count alone | A skill invoked once per quarter may be the most important skill in the workspace; usage rate ≠ value |
| Merging skills prematurely | Merging two skills with clear use cases into one with two `--modes` increases complexity, not reduces it |
| Running /workspace-audit after every session | The system changes slowly enough that weekly auditing is noise; quarterly is the right cadence |
| Treating the skill ceiling as a hard floor | The ceiling is 120; reaching 115 is not a problem. Treat it as a budget, not a target to fill |

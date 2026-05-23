---
name: simplify
description: >-
  Synthesizes findings from /workspace-audit and /skill-overlap into a
  prioritized, concrete simplification action plan. Each recommendation names
  the exact file, action, and expected count reduction. Priority order: retire
  infrastructure remnants (P1), retire overlapping zero-usage skills (P2),
  merge overlapping used skills (P3), archive stale arch docs (P4), add
  boundary documentation (P5). Outputs a delta summary: "workspace drops from
  X to Y skills." Distinct from /workspace-audit (diagnosis) and /skill-overlap
  (pairwise analysis). Run after both audits; do not run first.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (simplification plan) — no files written; operator executes
---

# /simplify — Workspace Simplification Action Plan

## When to Use

- After running `/workspace-audit` + `/skill-overlap` — synthesizes their findings into actionable steps
- When skill count is above 120 ceiling and concrete retirement targets are needed
- Quarterly, following the audit pair

**Do NOT use for:**
- Running the underlying audit → `/workspace-audit` first
- Pairwise overlap scoring → `/skill-overlap` first
- Executing the deletions — this skill outputs a plan; operator executes it

**Prerequisite:** Run `/workspace-audit` and `/skill-overlap` in the same session before calling `/simplify`. If their outputs are not in the current context, run them now.

---

## Input

```
/simplify            ← Full prioritized plan from current session's audit findings
/simplify --dry-run  ← Same output but explicitly labeled "for review only"
```

---

## Process

### Step 1 — Collect findings from session context

Gather all findings from `/workspace-audit` and `/skill-overlap` outputs in this session:
- Scale violations (current counts vs ceilings)
- Score 3-4 overlap pairs with usage evidence
- Score 3-4 overlap pairs with zero-usage skills
- Stale arch docs identified
- Memory layer issues

If audit outputs are not in context: output "Run /workspace-audit and /skill-overlap first, then re-run /simplify."

---

### Step 2 — Apply the Retirement Priority Model

Order recommendations by priority (from `architecture/WORKSPACE-AUDIT-FRAMEWORK.md`):

**P1 — Infrastructure remnants for removed systems:**
Skills that were created as infrastructure for systems retired in SR-1 through SR-6 (P15 persistent execution, mem-* skills that duplicated P13, dynamic invocation registry, knowledge-validate/qa if overlapping with knowledge-review, mcp-register/capability-audit if unused).

Check for these specific patterns:
- Skills referencing SQLite, Python scripts, or database state
- Skills that form pairs where the P13/P20 simplified version now covers the surface
- Skills with names matching patterns from SR-1 through SR-6 retirement decisions

**P2 — Overlap score 4 AND zero usage:**
Full redundancy with no invocation evidence. These are safe retirements with minimal risk of disrupting live workflows.

**P3 — Overlap score 3 AND zero usage (>90 days):**
High overlap, no recent usage. Lower certainty than P2, but strong retirement case when zero usage confirms the surface is covered elsewhere.

**P4 — Merge: overlap score 3-4, both used:**
Both skills have evidence, but significant overlap. Recommend merging the less-used into the more-used as an `--option` or flag. Concrete: "Merge /cmd-b into /cmd-a. Add `--mode b` flag to /cmd-a. Archive /cmd-b."

**P5 — Archive stale architecture docs:**
Docs that reference retired components. These are low-risk to move to `architecture/archive/` — they don't affect skill functionality.

**P6 — Add boundary documentation:**
Score 2 pairs (potential overlap, but differentiated). No retirement, just documentation. Low effort, reduces operator decision cost.

---

### Step 3 — Compute the delta

For each P1/P2/P3 retirement recommendation: -1 skill, -1 skills/README.md row.
For each P4 merge: -1 skill net.
For each P5 archive: -1 arch doc.

Report: "Implementing all recommendations drops workspace from [current] to [projected] skills ([N] below / [N] above the 120 ceiling)."

---

## Output Format

```
SIMPLIFICATION PLAN — [date]
Based on: /workspace-audit [date] + /skill-overlap [date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CURRENT STATE
Skills: [N] (ceiling: 120, [N] over)
Arch docs: [N] (ceiling: 25, [N] over / under)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRIORITY 1 — INFRASTRUCTURE REMNANTS ([N] actions)

[ ] Retire /[skill-name]
    File: .claude/commands/[skill-name].md
    Reason: Infrastructure for [removed system]; [what now covers this surface]
    Also remove: row from skills/README.md, entry from CLAUDE.md routing table

[Repeat for each P1 retirement]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRIORITY 2 — FULL REDUNDANCY, ZERO USAGE ([N] actions)

[ ] Retire /[skill-name]
    File: .claude/commands/[skill-name].md
    Reason: Overlap score 4 with /[other-skill]; zero usage in trace history
    Surface covered by: /[other-skill]
    Also remove: row from skills/README.md

[Repeat for each P2 retirement]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRIORITY 3 — HIGH OVERLAP, ZERO USAGE ([N] actions)

[ ] Retire /[skill-name]
    File: .claude/commands/[skill-name].md
    Reason: Overlap score 3 with /[other-skill]; no usage in last [N] days
    Note: Confirm /[other-skill] covers [specific surface] before deleting
    Also remove: row from skills/README.md

[Repeat for each P3 retirement]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRIORITY 4 — MERGE CANDIDATES ([N] actions)

[ ] Merge /[less-used] into /[more-used]
    Edit: .claude/commands/[more-used].md — add --[mode] flag covering [less-used surface]
    Delete: .claude/commands/[less-used].md after editing
    Also remove: row from skills/README.md for /[less-used]

[Repeat for each merge]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRIORITY 5 — STALE ARCHITECTURE DOCS ([N] actions)

[ ] Archive architecture/[filename].md
    Move to: architecture/archive/ (create dir if absent)
    Reason: References [retired component/skill from SR-X]

[Repeat for each P5 archive]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRIORITY 6 — BOUNDARY DOCUMENTATION ([N] actions)

[ ] Add "Do NOT use for → /[other-skill]" to /[skill-name]
    And: Add "Do NOT use for → /[skill-name]" to /[other-skill]

[Up to 5 listed; "N more identified" if larger]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECTED DELTA

P1 retirements:  -[N] skills
P2 retirements:  -[N] skills
P3 retirements:  -[N] skills
P4 merges:       -[N] skills
P5 archives:     -[N] arch docs
─────────────────────────────
Skills:    [current] → [projected] ([N above/below] 120 ceiling)
Arch docs: [current] → [projected] ([N above/below] 25 ceiling)

[If still above ceiling after all recommendations:]
⚠  Additional retirements needed to reach 120. Run /skill-overlap --section <largest section>
   for deeper analysis.

[If at or below ceiling after recommendations:]
✓  Implementing all recommendations brings workspace within operational constraints.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXECUTION ORDER

Start with Priority 1 (infrastructure remnants) — zero ambiguity, high impact.
Verify each retirement by confirming the covering skill works before deleting.
Run /workspace-audit --quick after each batch to track count progress.
```

---

## Quality Gate

Before outputting:
- [ ] Recommendations sourced from this session's /workspace-audit + /skill-overlap outputs — not from memory or assumptions
- [ ] Each retirement names the specific file and what covers its surface after retirement
- [ ] P4 merges specify which skill absorbs the other and what flag/mode to add
- [ ] Delta arithmetic is correct: each retirement = -1, each merge = -1 net
- [ ] If workspace is still above ceiling after all recommendations: say so explicitly
- [ ] If /workspace-audit or /skill-overlap outputs are absent from context: refuse with redirect
- [ ] P6 boundary doc tasks are listed but never prioritized above retirements

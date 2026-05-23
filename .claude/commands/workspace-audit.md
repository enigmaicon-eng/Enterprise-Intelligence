---
name: workspace-audit
description: >-
  Five-dimension audit of workspace health against P20 operational constraints:
  scale compliance (skill count, arch docs, memory files, MEMORY.md line count,
  ritual stack), skill boundary health, usage evidence, architecture document
  currency, and memory layer integrity. Returns a structured report with
  violation severity (Critical/Warning/OK) and specific counts. Distinct from
  /skill-overlap (pairwise boundary analysis) and /simplify (action plan
  synthesis). Run quarterly or after adding 3+ new skills.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (audit report)
---

# /workspace-audit — Five-Dimension Workspace Health Audit

## When to Use

- Quarterly maintenance — check that the workspace hasn't drifted past constraint ceilings
- After implementing a new P-series phase (3+ skills added)
- Before a `/strategy-review` — want to know if workspace overhead is degrading clarity
- When the workspace feels cluttered or skill routing feels ambiguous

**Do NOT use for:**
- Pairwise overlap analysis between specific skills → `/skill-overlap`
- Generating a concrete retirement/merge action plan → `/simplify`
- Checking a single skill's output quality → `/exec-inspect`

---

## Input

```
/workspace-audit           ← Full 5-dimension audit
/workspace-audit --quick   ← Dimension 1 only (scale compliance counts)
```

---

## Process

### Dimension 1 — Scale Compliance

Count files against P20 hard constraints:

**Check 1 — Skill count:**
Count `.claude/commands/*.md` files. Constraint: ≤120.
- Critical: >150
- Warning: 121–150
- OK: ≤120

**Check 2 — Architecture docs:**
Count `architecture/*.md` files. Constraint: ≤25.
- Critical: >35
- Warning: 26–35
- OK: ≤25

**Check 3 — Workspace memory files:**
Count `memory/*.md` files (exclude MEMORY.md itself). Constraint: ≤30.
- Warning: >30
- OK: ≤30

**Check 4 — MEMORY.md line count:**
Count lines in `memory/MEMORY.md`. Constraint: ≤200.
Also count lines in `.claude/projects/.../memory/MEMORY.md` if accessible.
- Warning: >200
- OK: ≤200

**Check 5 — Ritual stack:**
Count daily operations skills: `/plan`, `/focus`, `/prep`, `/shutdown`, `/briefing`, `/weekly`. Constraint: ≤6.
- Warning: >6
- OK: ≤6

**Check 6 — Skill catalog sync:**
Compare count of `.claude/commands/*.md` with row count of Active Skills table in `skills/README.md`.
- Warning: counts differ by >5
- OK: counts match or differ by ≤5

If `--quick` flag: stop here and output Dimension 1 results only.

---

### Dimension 2 — Skill Boundary Health (sample)

Read `skills/README.md` Active Skills table. Group skills by CLAUDE.md routing section.

For each routing section with >5 skills, select the 3 most recently added skills (bottom of section or highest version).

For each selected skill file, check:
- [ ] Has "Do NOT use for" section
- [ ] "Do NOT use for" names at least one adjacent skill by command name
- [ ] Description contains trigger conditions (not just "does X")

Count: skills with healthy boundaries / skills sampled.

Flag as warning if >30% of sampled skills lack boundary documentation.

---

### Dimension 3 — Usage Evidence (sample)

Read `traces/TRACE-INDEX.md`.

Extract skill names mentioned in goals, tags, or session types from the last 180 days.

Cross-reference against `.claude/commands/*.md` file list.

Identify skills with zero trace evidence in 180 days.

Report:
- Count of skills with zero usage evidence
- Names of zero-usage skills that also lack unique capability signals in their description
- Do NOT flag skills with zero usage that have a clearly unique capability surface

---

### Dimension 4 — Architecture Document Currency (sample)

List `architecture/*.md` files.

For each, check if it references any component, skill, or system that was retired in SR-1 through SR-6 (P15 persistent execution, mem-* skills, dynamic invocation registry, knowledge-validate/qa, mcp-register/capability-audit).

Also check: does the doc reference a skill that no longer exists in `.claude/commands/`?

Report: count of potentially stale arch docs with specific filenames.

---

### Dimension 5 — Memory Layer Health

Read `memory/MEMORY.md` index. For each listed `.md` file, verify the file exists in `memory/`.

Read `memory/*.md` files (sample up to 10). Verify each has valid frontmatter with `name` and `type` fields.

Flag:
- Broken index pointers (MEMORY.md line points to non-existent file)
- Memory files missing required frontmatter fields

---

## Output Format

```
WORKSPACE AUDIT — [date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DIMENSION 1 — SCALE COMPLIANCE
Constraint                 | Count | Limit | Status
---------------------------|-------|-------|--------
Skills (.claude/commands/) |  [N]  |  120  | [OK/WARNING/CRITICAL]
Architecture docs          |  [N]  |   25  | [OK/WARNING/CRITICAL]
Workspace memory files     |  [N]  |   30  | [OK/WARNING]
MEMORY.md line count       |  [N]  |  200  | [OK/WARNING]
Ritual stack               |  [N]  |    6  | [OK/WARNING]
Skill catalog sync         | ±[N]  |   ±5  | [OK/WARNING]

[Critical violations listed individually, e.g.:]
⚠  CRITICAL: Skills at [N] — [N] over the 120 ceiling. Run /skill-overlap + /simplify.
⚠  WARNING: Architecture docs at [N] — [N] over the 25 limit. Review for stale docs.

DIMENSION 2 — SKILL BOUNDARY HEALTH (sampled [N] skills)
[N]/[N] sampled skills have "Do NOT use for" sections with named adjacent skills.
[If boundary gaps:] Gaps found in: [list skill names]
[If clean:] ✓  Boundary documentation healthy in sampled set.

DIMENSION 3 — USAGE EVIDENCE (last 180 days)
[N] skills have zero trace evidence in the last 180 days.
[If any:] Zero-usage skills without unique capability signals:
  - /[skill-name] — [description excerpt]
  [up to 5 listed; note "N more" if larger]
[If clean:] ✓  All skills have usage evidence or unique capability surfaces.

DIMENSION 4 — ARCHITECTURE DOCUMENT CURRENCY (sampled)
[N] arch docs may reference retired components:
  - [filename] — references [retired component/skill]
[If clean:] ✓  No stale arch doc references detected in sample.

DIMENSION 5 — MEMORY LAYER HEALTH
[N] broken MEMORY.md index pointers detected.
[N] memory files missing required frontmatter fields.
[If clean:] ✓  Memory layer intact.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUMMARY
[Critical violations requiring immediate action]: [N]
[Warnings to address this quarter]: [N]

[If all clear:] Workspace is within all operational constraints. No action required.
[If violations:] Run /simplify for a prioritized action plan.
```

---

## Quality Gate

Before outputting:
- [ ] `.claude/commands/` file count is an actual directory listing, not an estimate
- [ ] `architecture/` file count is an actual directory listing
- [ ] Memory file count excludes MEMORY.md itself
- [ ] Dimension 1 results output even if `--quick` stops here
- [ ] Skill ceiling violation classified as Critical (>150) or Warning (121–150), not OK at any level above 120
- [ ] Zero-usage skills not flagged as retirement candidates if they have unique capability surfaces
- [ ] If `--quick`: output Dimension 1 only with a note that full audit skipped

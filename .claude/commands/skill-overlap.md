---
name: skill-overlap
description: >-
  Pairwise semantic overlap analysis for skills within a routing section or
  across the full workspace. Scores each pair 0-4 on: shared primary verb,
  shared output type, overlapping trigger conditions, missing mutual "Do NOT
  use for" references. Score 3-4 = significant overlap candidate for merge or
  retirement. Also surfaces zero-usage skills by section. Distinct from
  /workspace-audit (constraint compliance counts) and /simplify (action plan).
  Run before /simplify or when a section feels redundant.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (overlap report)
---

# /skill-overlap — Skill Pairwise Overlap Analysis

## When to Use

- Before running `/simplify` — identifies which skills to target
- When adding a new skill and unsure if it duplicates an existing one
- Quarterly, on sections that have grown fastest (PM section, cognitive section)
- When two skills keep appearing together in the same routing decision

**Do NOT use for:**
- Full workspace constraint audit → `/workspace-audit`
- Generating a retirement/merge action plan → `/simplify`
- Checking skill output quality → `/exec-inspect`

---

## Input

```
/skill-overlap                      ← Full workspace scan, grouped by CLAUDE.md section
/skill-overlap --section <name>     ← One routing section only (e.g., "pm", "cognitive", "execution")
/skill-overlap --pair <cmd1> <cmd2> ← Score a specific pair
```

---

## Process

### Step 1 — Load the skill roster

Read `skills/README.md` Active Skills table to get the full skill list with command names.

Group by CLAUDE.md routing section. Sections:
- Daily operations
- Cognitive load
- Capture & synthesis
- Knowledge
- Strategy
- Execution
- PM work
- Cognitive (think/misconception/recall-test/insight)
- Decision intelligence
- Trace & recall
- Observability
- Reliability

If `--section` flag: load only skills in that section.
If `--pair` flag: load only those two skill files and skip to Step 3.

---

### Step 2 — Within-section pair enumeration

For sections with N skills, generate all N×(N-1)/2 pairs.

Limit: sections with >20 skills (PM section) — sample the 10 most recently added only to keep the analysis tractable.

---

### Step 3 — Score each pair (0-4)

Read both skill files for each pair. Apply the overlap score rubric:

| Signal | +1 if |
|--------|-------|
| **Same primary verb** | Both descriptions lead with the same action verb (e.g., both "analyzes", both "captures", both "reviews") |
| **Same output type** | Both write to same directory, OR both are terminal-only inline reports, OR both produce the same artifact type |
| **Trigger overlap** | One skill's trigger conditions ("When to Use") are a subset of the other's, or they share ≥2 identical trigger scenarios |
| **Missing mutual boundary** | Neither skill's "Do NOT use for" section names the other by command |

Score interpretation:
- **0–1**: Well-differentiated or managed boundary — no action needed
- **2**: Potential overlap — review for missing boundary documentation
- **3–4**: Significant overlap — retirement or merge candidate

---

### Step 4 — Usage evidence overlay

Read `traces/TRACE-INDEX.md`. Extract skill command names mentioned in goals or tags over all recorded history.

For each pair with score ≥2, annotate:
- Which of the two has usage evidence
- Which has zero evidence

This informs whether the recommendation is "retire" (zero usage) vs "merge" (both used).

---

### Step 5 — Classify findings

For each pair with score ≥2:

**Score 2 — Managed boundary gap**: Both skills are differentiated, but neither documents it. Recommendation: add "Do NOT use for" to both.

**Score 3 — Merge candidate (both used)**: Skills cover overlapping ground, both invoked. Recommendation: merge less-used into more-used as a flag or sub-mode.

**Score 3 — Retirement candidate (one unused)**: One skill has zero usage AND the other covers its surface. Recommendation: retire the unused one.

**Score 4 — Full redundancy**: One skill is a strict subset of the other. Recommend immediate retirement of the narrower skill.

---

## Output Format

```
SKILL OVERLAP ANALYSIS — [date]
[Section: all / <section-name> / pair analysis]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION: [section name] ([N] skills, [N] pairs evaluated)

Score 3-4 pairs (significant overlap):
┌─────────────────────────────────────────────────────────────────┐
│ /[cmd-a] × /[cmd-b]                                  Score: [N] │
│ Signals: [list which of the 4 signals fired]                    │
│ Usage: /[cmd-a] = [used/unused], /[cmd-b] = [used/unused]       │
│ → [Retire /cmd-b | Merge /cmd-b into /cmd-a | Document boundary]│
└─────────────────────────────────────────────────────────────────┘

[Repeat for each score 3-4 pair]

Score 2 pairs (boundary gap only):
  - /[cmd-a] × /[cmd-b]: add "Do NOT use for" to both pointing at each other
  [up to 5 listed; note "N more" if larger]

[If section is clean:] ✓  No significant overlap in [section name].

---

SECTION: [next section] ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUMMARY
Score 4 pairs (full redundancy):    [N]
Score 3 pairs (significant overlap): [N]
Score 2 pairs (boundary gap only):  [N]

Retirement candidates (score 3-4, zero usage):  [N] skills
Merge candidates (score 3-4, both used):        [N] skill pairs
Boundary documentation gaps:                    [N] pairs

Run /simplify to generate the prioritized action plan.
```

---

## Quality Gate

Before outputting:
- [ ] Overlap score derived from actually reading both skill files — not from description alone
- [ ] "Same primary verb" checked against description first sentence, not command name
- [ ] Usage evidence from actual TRACE-INDEX scan, not assumed
- [ ] Score 2 pairs only recommended for documentation, not retirement
- [ ] Managed overlap (skill A says "Do NOT use for → /cmd-b" and vice versa) scores 0 on the fourth signal — do not penalize well-documented overlaps
- [ ] PM section limited to 10 most recent skills if section has >20 skills
- [ ] If `--pair`: output a single pair scorecard, not the full summary

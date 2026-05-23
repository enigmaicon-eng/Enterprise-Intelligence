---
name: exec-friction
description: >-
  Execution friction analysis — identifies recurring non-failure impediments:
  dependency blocks, clarity blocks, scope creep, context switches, energy
  depletion, tool friction. Reads traces for blocked states, pivots, and
  replanning events. Distinct from /failure-review (which covers failed/partial/
  abandoned outcomes only) — friction includes slowdowns and pivots in sessions
  that completed. Answers "What keeps slowing me down, and what's the structural
  pattern?" Run monthly or before making structural workflow changes.
version: "1.0"
changed: "2026-05-23 — initial"
output: inline (friction register)
---

# /exec-friction — Execution Friction Analysis

## When to Use

- Monthly friction audit: what recurring impediments have accumulated?
- Before making a structural change to a workflow: confirm what you're actually fixing
- After a period of feeling slowed down even though work is completing
- Pre-`/exec-checkpoint`: is declining throughput caused by friction or by strategy?

**Do NOT use for:**
- Failure root causes (non-completed outcomes) → `/failure-review`
- Throughput trend → `/exec-throughput`
- Codifying a pattern from friction events → `/pattern-mine` (use after this)
- A single trace analysis → `/exec-inspect`

**Friction ≠ failure.** Many friction events end in completion — just slower. The signal is pivots, blocks, and replanning notes, not outcome codes.

---

## Input

```
/exec-friction              ← Full friction register (last 90 days)
/exec-friction --30         ← Last 30 days only
/exec-friction --type <friction-type>   ← Filter to one friction type
```

---

## Friction Taxonomy

| Type | Definition | Signal in Traces |
|------|-----------|-----------------|
| **Dependency block** | Work halted waiting for external input | Blocked state noted; partial outcome, resumed separately |
| **Clarity block** | Work replanned because requirements were unclear | Pivot noted; goal changed during session |
| **Scope creep** | Session expanded well beyond original goal | Actual work significantly exceeds stated goal; partial or long overrun |
| **Context switch** | Session redirected unexpectedly to different work | Two distinct goals in one trace; unplanned work appears |
| **Energy depletion** | Work abandoned despite no external block | Abandoned without citing tool/dependency/clarity; repeated at similar times |
| **Tool friction** | Delays from tooling or environment issues | Failure/blocker notes cite tool, environment, or access problems |

---

## Process

### Step 1 — Read trace history

Read `traces/TRACE-INDEX.md`. Identify episodes in the target period.

Load trace files. To stay bounded, load max 15 most recent traces. If the period contains more, note "Showing [N] most recent of [total] episodes."

### Step 2 — Detect friction signals per trace

For each loaded trace, scan for friction signals:

**Dependency block signals:** "waiting for", "blocked on", "pending", "need input from", "depends on", blocker fields populated, outcome = partial with no internal cause

**Clarity block signals:** "unclear", "ambiguous", "replanned", "changed direction", "goal shifted", pivot or replan events noted, mid-session goal change

**Scope creep signals:** "expanded", "took longer than expected", "more than planned", "turned into", actual duration significantly exceeds stated duration, additional goals added mid-session

**Context switch signals:** two unrelated goals in one trace, "interrupted", "switched to", "urgent came up", unplanned session tag

**Energy depletion signals:** abandoned without external cause, "low energy", "couldn't focus", "deferred", outcomes abandoned with no blocker cited

**Tool friction signals:** "tool issue", "env problem", "couldn't access", "timed out", "crashed", environment/access failures noted in blockers

### Step 3 — Classify and count

For each friction event detected, assign its type from the taxonomy. One trace may have multiple friction events of different types.

Recurring friction type: appears in 3+ traces (lower threshold than /failure-review because friction is softer signal than failure).

### Step 4 — Map to patterns

Check `traces/patterns/` — do any codified patterns already address the recurring friction? If yes, note the existing pattern. If no pattern exists for a recurring type (3+ instances), flag for `/pattern-mine`.

### Step 5 — Generate structural mitigations

For each recurring friction type, suggest a structural mitigation:

| Friction Type | Structural Mitigation |
|--------------|----------------------|
| Dependency block | Map dependencies explicitly before starting; /exec-risk |
| Clarity block | Add a 5-minute requirements check at session start; /pre-decide for ambiguous goals |
| Scope creep | Time-box the session explicitly; note the boundary at start |
| Context switch | Designate protected blocks; surface interrupts as explicit /capture entries |
| Energy depletion | Audit session scheduling; match work type to energy state in /plan |
| Tool friction | Document the tool issues; fix environment as a tracked work item |

---

## Output Format

```
EXECUTION FRICTION ANALYSIS
Period: [date range]  |  [N] traces analyzed ([N] of [total] if truncated)

FRICTION INVENTORY

── Dependency Block ([N] events) ──
[trace ID] [date]: [brief description of the block]
[trace ID] [date]: [brief description]
[Recurring (3+): YES / NO]

── Clarity Block ([N] events) ──
[same structure]

── Scope Creep ([N] events) ──
[same structure]

── Context Switch ([N] events) ──
[same structure]

── Energy Depletion ([N] events) ──
[same structure]

── Tool Friction ([N] events) ──
[same structure]

[Omit any type with 0 events]

RECURRING FRICTION (≥3 instances)
⚠  [friction type]: [N] instances
   Structural mitigation: [specific suggestion]
   → /pattern-mine to codify as a friction anti-pattern

[If no recurring types:]
No recurring friction types. Most friction appears situational.

EXISTING PATTERNS COVERING THIS FRICTION
[List any existing traces/patterns/ entries that address a recurring type]
[Or: "No existing patterns for recurring friction types."]

SUMMARY
Total friction events: [N] across [K] types
Most frequent: [type] ([N] events)
[1-2 sentences: what the dominant friction pattern means structurally]
```

---

## Quality Gate

Before outputting:
- [ ] TRACE-INDEX.md read before loading individual traces
- [ ] Max 15 traces loaded; truncation noted if applicable
- [ ] Friction signals detected from actual trace content (blocked/pivot/replan text)
- [ ] Friction ≠ failure: completed-outcome traces also scanned for friction signals
- [ ] Recurring threshold = 3+ instances (lower than /failure-review's 2+ for non-completed outcomes)
- [ ] Existing patterns/ checked before recommending /pattern-mine
- [ ] Structural mitigation is a specific, actionable suggestion — not "avoid this"
- [ ] Zero-event friction types omitted from output entirely

# /exec-risk — Risk Surfacing and Tracking

Surface, log, and manage risks for active work. Maintains `execution/risks.md` as the single source of active risk intelligence.

## Trigger
`/exec-risk surface [initiative-id]` — proactively identify risks for an initiative
`/exec-risk log [risk description]` — log a specific risk immediately
`/exec-risk review` — review all open risks, flag stale or triggered ones
`/exec-risk close [risk-id]` — close a risk with resolution

## When to Use
- After creating an execution plan (surface risks before work starts)
- When something unexpected happens during execution
- Weekly as part of the exec-review ritual
- When a dependency changes or an assumption is invalidated

Do NOT use this to log background noise. If the risk has no named owner or no actionable trigger, it doesn't belong here.

## Protocol — Surface Risks

### Step 0: Load context
Read `execution/plans/[initiative-id].md`. Focus on:
- Assumptions (each assumption is a potential risk if it fails)
- Dependencies (each dependency is a risk if it's not available on time)
- Milestones with tight timelines
- Out-of-scope items that might be pulled in

### Step 1: Generate risk candidates
Apply four lenses:
1. **Assumption failure**: What if [assumption X] turns out to be wrong?
2. **Dependency slip**: What if [dependency Y] is delayed or unavailable?
3. **Scope creep vector**: What adjacent work is likely to be pulled in?
4. **Resource constraint**: What if [person or tool] becomes unavailable?

### Step 2: Filter candidates
Keep only risks that:
- Have a realistic (not merely theoretical) probability of materializing
- Would cause a checkpoint-level decision if they materialized
- Have a specific trigger condition that can be monitored
- Have an action someone can take to mitigate or respond

Discard: generic risks, risks with no owner, risks where the only mitigation is "hope for the best."

### Step 3: Assign risk IDs
Format: `RISK-YYYY-NNN` — sequential within the year.
Read `execution/risks.md` to get the next available number.

### Step 4: Write risk entries
Append to `execution/risks.md`. Each entry requires:
- Description (specific, not generic)
- Probability and Impact (H/M/L with rationale)
- Owner (one person)
- Trigger condition (observable event that means the risk is materializing)
- Mitigation (pre-planned response, not "deal with it when it happens")

### Step 5: Cross-reference
Update the initiative plan's Top Risks section if the surfaced risks are higher priority than what's already listed.

### Step 6: Report
- Number of risks surfaced
- Top risk (highest P×I)
- Any risks that require immediate action before work proceeds

---

## Protocol — Review Risks

Read `execution/risks.md`. For each open risk:

**Flag triggered**: Any risk whose trigger condition has been observed. Escalate to exec-checkpoint.
**Flag stale**: Any risk open for 30+ days with no update. Either close it or update it.
**Flag owner gap**: Any risk with no named owner. Either assign an owner or close it.

Write the review summary to `execution/risks.md` under a `## Last Review` header.

---

## Risk vs. Issue Distinction
A **risk** is something that might happen. It lives in `execution/risks.md`.
An **issue** is something that has happened and is blocking work. It becomes an action item in `execution/action-items.md` immediately — do not file a triggered risk as a continuing risk entry.

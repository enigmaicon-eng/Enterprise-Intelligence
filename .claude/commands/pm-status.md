---
name: pm-status
description: Generate a weekly stakeholder status update. Produces structured RAG (Red/Amber/Green) update with key metrics, progress, risks, and asks. Written for clarity, not completeness.
version: "1.0"
changed: 2026-05-20
---

# PM Status

**Input:** Initiatives to report on, week number, any notable developments or risks — provided inline. Reads action items and execution audit if available.

**Output:** Written to `reviews/weekly/YYYY-WW-status.md`

**Also reads:** `execution/action-items.md` (for carry-forward items)

---

## Steps

1. **Read context.** Load `execution/action-items.md` and any execution audit from the current week if it exists.

2. **Classify each initiative by RAG status:**
   - **Green:** On track. Delivery expected as committed. No blockers.
   - **Amber:** At risk. May miss timeline or scope target without intervention. Mitigation in progress.
   - **Red:** Off track. Will miss commitment without executive action or scope change. Decision needed.

3. **For each initiative, extract:**
   - What moved this week (progress)
   - What didn't move (slips)
   - What's at risk (threats to plan)
   - What's needed from stakeholders (asks)

4. **Apply the "news, not noise" filter.** Stakeholders need to know: what changed from last week, what they need to decide, and what they should worry about. They do not need a complete status of every task.

5. **Write key metrics section.** For each initiative with a measurable success metric: current reading vs. baseline vs. target. One number per initiative — not a metrics dump.

6. **Identify the one thing that most needs stakeholder attention.** Lead with it. Don't bury the most important update in the middle.

7. **Write the output.**

---

## Output Format

```markdown
# Status Update — Week [WW] — [YYYY-MM-DD]
**Author:** [PM]  **Distribution:** [Stakeholder list or group]

---

## Summary (3 sentences max)
[What's most important this week. What's changed. What decision or action is needed from stakeholders.]

---

## Initiative Status

### [Initiative 1] — 🟢 GREEN | 🟡 AMBER | 🔴 RED

**Status:** On track / At risk / Off track  
**Key metric:** [Metric]: [Current] vs. [Target] (baseline: [N])

**Progress this week:**
- [What moved — specific]

**Slips / concerns:**
- [What didn't move or is at risk — specific]

**Ask (if any):** [Specific decision or action needed from stakeholders, by date]

---

### [Initiative 2] — 🟢 | 🟡 | 🔴

[Same structure]

---

## Risks This Week

| Risk | Priority | Owner | Status |
|---|---|---|---|
| [Risk description] | P0/P1 | [name] | Active / Mitigated |

---

## Decisions Needed

| Decision | Needed by | Owner | Context |
|---|---|---|---|
| [Decision] | [Date] | [name] | [1-line context] |

---

## Carry-Forwards from Last Week
- [Action item] — Status: [Done / In progress / Blocked — reason]
- [Action item] — Status: [Done / In progress / Blocked — reason]

---

## Next Week's Key Focus
1. [Most important outcome for next week]
2. [Second priority]
3. [Third priority]
```

---

## Quality Gate

- Each initiative has a RAG status (not "in progress" — green/amber/red)
- Amber and Red initiatives have a specific risk stated (not "timeline concerns")
- Every "ask" is specific and time-bound (not "need feedback")
- Summary is ≤3 sentences and contains the most important update
- Key metrics show current + target (not just current reading)
- No initiative is reported as Green if it has an unresolved blocker

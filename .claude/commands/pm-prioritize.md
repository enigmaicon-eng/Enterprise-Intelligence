---
name: pm-prioritize
description: Score a set of initiatives using RICE++ and produce a ranked recommendation with explicit trade-off record. Surfaces assumption divergences and strategic multiplier flags.
version: "1.0"
changed: 2026-05-20
---

# PM Prioritize

**Input:** List of initiatives with descriptions, context on optimization target and available capacity.

**Output:** Written to `decision-frameworks/decisions-log.md` (appended) and `reviews/prioritization/YYYY-MM-DD-prioritization.md`

---

## Steps

1. **Read context.** Load `decision-frameworks/pm/prioritization-playbook.md`. Read `execution/action-items.md` for carry-forward context.

2. **Strategic alignment gate first.** Before scoring, run each initiative through:
   - Which strategy assumption does this test or advance?
   - Which horizon does it belong to (H1/H2/H3)?
   - If the strategy is wrong, does this still create value?
   - Items that fail this gate belong on the parking lot, not the scored list. Flag them explicitly.

3. **Score each initiative on RICE++:**
   - Reach: users affected per period (real data, not aspirations)
   - Impact: 1 (minimal) / 3 (moderate) / 10 (transformational — must be rare)
   - Confidence: 100%=proven / 80%=strong evidence / 50%=intuition / 20%=speculation
   - Effort: total person-weeks across all functions
   - Strategic multiplier: 2x (compounds position) / 1x (neutral) / 0.5x (fragments focus)
   - Reversibility: High (<1 sprint to undo) / Medium (1-3 sprints) / Low (costly or irreversible)
   - Trade-off declaration: top 2 things NOT doable if this is funded

4. **Score formula:** (Reach × Impact × Confidence × Strategic multiplier) ÷ Effort

5. **Flag anomalies:**
   - High multiplier + low score: hidden strategic upside, reconsider
   - High score + 0.5x multiplier: focus risk, deliberate choice needed
   - Score divergence if multiple scorers: name the hidden assumption difference

6. **Produce trade-off record.** For the recommended top N: explicitly name what is NOT being done and why.

7. **Capacity check.** Confirm top N items fit available person-weeks. Adjust if not.

8. **Write the output.**

---

## Output Format

```markdown
# Prioritization — [Date] — [Quarter/Sprint]

**Optimizing for:** [Primary metric or strategic objective]
**Available capacity:** [N person-weeks]
**Decision owner:** [Name]

## Parking Lot (failed strategic alignment gate)
- [Initiative] — [Why it failed the gate]

## Scored Initiatives

| Rank | Initiative | R | I | C% | E | Strat | Score | Rev |
|---|---|---|---|---|---|---|---|---|
| 1 | [Name] | [N] | [1/3/10] | [%] | [pw] | [x] | [N] | H/M/L |
...

## Flags
**High multiplier / low score:** [Initiative] — strategic value exceeds score
**Focus risk (0.5x):** [Initiative] — high score but fragments strategy
**Divergence:** [Initiative] — [assumption disagreement surfaced]

## Trade-Off Record
**Funding:** [Top initiatives]
**NOT doing:**
- [Initiative] — [reason]
- [Initiative] — [reason]
- [Initiative] — [reason]

**Capacity check:** [N pw required / N pw available — fits/doesn't fit]

## Recommendation
Fund: [list]
Defer: [list with rationale]
Kill/park: [list with rationale]

**Review date:** [When to reassess]
```

---

## Quality Gate

- All initiatives passed or failed strategic alignment gate before scoring
- Confidence scores require evidence justification above 50%
- 0.5x strategic multiplier applied where appropriate (not avoided to protect rankings)
- Trade-off record complete — funded list AND explicit deferral list
- Capacity check completed
- Score divergences named with underlying assumption identified

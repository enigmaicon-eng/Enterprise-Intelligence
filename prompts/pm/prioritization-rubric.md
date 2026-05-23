# Prioritization Rubric Prompt
## Structured Scoring for Roadmap Trade-Off Decisions

**Use when:** Running a prioritization session, scoring a batch of initiatives against each other, or preparing a recommendation for a prioritization meeting.

**Principle from `decision-frameworks/pm/prioritization-playbook.md`:** The purpose of prioritization is not to rank things — it is to make trade-offs explicit and get the right people aligned on them. A scoring output without trade-off record has failed.

---

## The Prompt — RICE++ Scoring Session

```
Score the following initiatives using RICE++ and produce a ranked list with trade-off reasoning.

CONTEXT:
- Optimization target: [What are we maximizing for this quarter? Name ONE metric or strategic objective.]
- Time horizon: [Sprint / Quarterly / Annual]
- Decision owner: [Who makes the final call?]
- Available capacity: [Engineering person-weeks this planning period]

INITIATIVES TO SCORE:
[List each initiative with: name, one-line description, and any known data]

FOR EACH INITIATIVE, SCORE:

1. Reach: How many users affected per period? (Use real data. Aspirational numbers require explicit flagging.)
   
2. Impact: Magnitude of change on the primary metric?
   1 = minimal change | 3 = moderate, measurable | 10 = transformational (10s must be rare — justify)

3. Confidence: How sure are we?
   100% = proven by data | 80% = strong evidence | 50% = well-reasoned intuition | 20% = speculation
   
4. Effort: Total person-weeks across PM + design + engineering + QA + data

5. Strategic multiplier:
   2x = compounds our position (builds moat, enables next bet, platform-creating)
   1x = neutral (valuable but standalone)
   0.5x = fragments focus (good idea that pulls us off strategy)
   
6. Reversibility:
   High = can undo in <1 sprint | Medium = 1-3 sprints | Low = not reversible or very costly
   
7. Trade-off declaration:
   Name the top 2 things we CANNOT do if we do this initiative

SCORE FORMULA: (Reach × Impact × Confidence × Strategic multiplier) ÷ Effort

SYNTHESIS INSTRUCTIONS:
After scoring:
1. Produce ranked list by RICE++ score
2. Flag any low-score items with high strategic multiplier that deserve a closer look
3. Flag any high-score items with a 0.5x multiplier — high scores on focus-fragmenting work are warnings
4. Identify the trade-off record: "If we fund #1, #2, #3 — what's explicitly NOT happening?"
5. Flag items where individual scores diverged significantly — these represent hidden assumption differences
6. Note capacity check: do the top N items fit within available person-weeks?
```

---

## Output Template

```markdown
# Prioritization Session — [Date] — [Quarter/Sprint]

**Optimizing for:** [Primary metric or strategic objective]
**Available capacity:** [N person-weeks]
**Decision owner:** [Name]

---

## Scored Initiatives

| Rank | Initiative | Reach | Impact | Conf | Effort | Strat | Score | Rev | Trade-offs |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [Name] | [N] | [1/3/10] | [%] | [pw] | [0.5/1/2x] | [score] | H/M/L | [A, B] |
| 2 | ... | | | | | | | | |
| ... | | | | | | | | | |

---

## Flags

**High multiplier / low score (hidden upside):**
- [Initiative] — strategic multiplier 2x suggests this punches above its score. Consider.

**High score / low multiplier (focus risk):**
- [Initiative] — score is high but 0.5x multiplier means funding this pulls us off strategy. Deliberate choice?

**Score divergence (hidden assumption disagreement):**
- [Initiative] — PM scored impact 10, engineering scored impact 3. Root assumption: [what explains this gap?]

---

## Trade-Off Record

**If we fund:** [#1], [#2], [#3]

**We are NOT doing:**
- [Item] — [one-sentence rationale for the deferral]
- [Item] — [one-sentence rationale]
- [Item] — [one-sentence rationale]

**Capacity check:** Top [N] funded items require [X] person-weeks. Available: [Y]. [Fits / Does not fit — adjust by: ...]

---

## Recommendation

**Fund:** [Initiative names]
**Defer:** [Initiative names with brief rationale]
**Kill or park:** [Initiative names with brief rationale]

**Decision review date:** [When will we reassess the top items?]
```

---

## Strategic Alignment Gate

Before scoring, run each initiative through the strategic alignment test:

| Initiative | Which strategy assumption does this test or advance? | Horizon (H1/H2/H3) | If strategy is wrong, does this still create value? |
|---|---|---|---|
| [Name] | [Assumption] | [H1/H2/H3] | Yes / No |

**Items that can't answer column 2 belong on the parking lot, not the scored list.**

---

## Quality Gates

- [ ] Each item's confidence score is justified — not rounded up to feel better about the initiative
- [ ] Strategic multipliers are honest — 0.5x applied when appropriate, not avoided because it drops the score
- [ ] Trade-off record is complete — not just a ranked list without named deferrals
- [ ] Score divergences between team members are surfaced and the underlying assumption is named
- [ ] Capacity check completed — funded items fit available person-weeks

---

## Common Failures

**Confidence inflation:** Everyone marks 80% confidence to avoid looking uncertain. Require explicit evidence for anything above 50%.

**Strategic multiplier avoidance:** Everyone marks 1x because 0.5x would make their initiative rank lower. If the item fragments focus, it should rank lower.

**Scoring theater:** Scores are produced but the outcome was decided before scoring. If this is happening, the framework is being used as post-hoc justification. Name this explicitly and either trust the framework or explicitly override it with documented rationale.

**Missing the trade-off record:** The session produces a rank-ordered list without naming what's being cut. This is the most common failure. The cut list is as important as the funded list.

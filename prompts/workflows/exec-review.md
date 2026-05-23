# Prompt: Execution Review

You are conducting a structured review of a deliverable or an execution period. Your job is to produce a verdict and a concrete change list — not a narrative assessment.

## Mode A: Deliverable Review

Given the deliverable and its quality criteria, score it and produce a change list.

**For each criterion, produce:**
- Pass / Fail / Partial
- One sentence explaining why
- If Fail or Partial: the specific gap (not "could be better" — name what's missing or wrong)
- If Fail or Partial: the specific change required to close the gap
- Effort to fix: <30min / 1-2hr / half-day+

**Verdict** (choose one):
- **Ship**: All criteria pass
- **Refine**: [N] criteria fail — use refinement-cycle.md to manage
- **Rewrite**: Structural failure — criteria can't be met with incremental changes
- **Kill**: The deliverable's purpose is no longer valid

Do NOT produce a verdict of "mostly good with some improvements to make." That is Refine.

---

## Mode B: Weekly Execution Review

Given the week's action items, initiative status, and risk register, produce:

**Week in One Line**: The essential character of the week in one sentence.

**Initiative Status Table**:
| Initiative | Plan This Week | Actual | Health |
Each initiative gets one of: On Track / Slipping / Blocked / At Risk / Complete

**Action Item Audit**:
- Completed on time: [N]
- Completed late: [N] — root cause (one per pattern, not per item)
- Overdue: [N] — what's blocking
- Added mid-week: [N] — were they planned or reactive?

**Top Risk This Week**: The single risk most likely to materialize in the next 7 days.

**Next Week Top 5** (ranked list): Using commitment → leverage → reversibility stack.
Format: `[N]. [Item] | [Commitment/Leverage/Reversibility — which criterion placed it here] | [Effort]`

**One Change to Make**: The single process or workflow change that would most improve next week's execution. Specific and actionable — not "be more focused."

---

## Input

**Mode**: {{deliverable_review | weekly_review}}
**Criteria / Initiative list**: {{CRITERIA_OR_INITIATIVES}}
**Deliverable or week summary**: {{CONTENT}}

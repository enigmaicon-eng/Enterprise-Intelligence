# Prompt: Bet Postmortem

You are conducting a structured postmortem on a closed strategic bet. Your job is to extract genuine learning — not to explain why the outcome was inevitable, not to assign blame, not to celebrate. To learn.

## The Prime Directive

**The thesis is read verbatim. It is not rewritten.**

Postmortem value collapses when the thesis is retroactively adjusted to match what happened. Read the original thesis exactly as written at bet creation. Evaluate it against what actually occurred. The discomfort of reading a wrong thesis is exactly the signal that produces learning.

---

## Structure of Output

### Bet Summary (2 sentences)
What the bet was and how it closed. Written for someone who hasn't read the bet file.

### Thesis Audit
Original thesis: [verbatim]

Was it correct? Yes / Partially / No

If No or Partially: Name the specific belief that was wrong. Not "the market" or "timing" — the specific falsified claim.

Was it wrong at creation (bad reasoning) or did conditions change? Distinguish these — they generate different lessons.

### Evidence Audit
**Confirming evidence observed**: [what happened that supported the thesis]
**Disconfirming evidence observed**: [what happened that challenged it]

**Disconfirmation discipline check**: Did we actively look for disconfirming evidence? If we only found confirming evidence, was it because none existed or because we weren't looking?

### Kill Condition Audit
Kill condition stated: [verbatim]
Was it triggered? Yes / No / Ambiguous

If triggered and the bet was cut → Did we act quickly enough, or did we delay?
If not triggered and the bet was cut anyway → What actually caused the cut? This is the "real kill condition" — it may be better than the stated one.
If the bet was won and the kill condition was never close → Was it too strict (would have killed a winner) or was it just never relevant?

**Kill condition improvement**: What would a better kill condition have looked like?

### Assumption Audit
For each assumption from the bet file:
- Was it confirmed, invalidated, or never tested?
- Which assumption most determined the outcome?

If the most important assumption was never tested → That's a process failure. What would have tested it earlier?

### Decision Quality Audit
Review the monthly verdict sequence (Continue / Adjust / etc.).

In hindsight: which verdict was wrong, and what evidence was available at that time that should have changed it?

Systematic bias check: Were the verdicts consistently too optimistic? Too slow to call Kill? Too quick to Adjust (indicating thesis uncertainty)?

### What Would You Do Differently
Not "work harder." Specific decision points where a different choice had a better expected value.

### Pattern Extraction (mandatory)
Every postmortem must extract at least one generalizable pattern.

**Pattern name**: [short, memorable]
**Context**: When this pattern applies
**Lesson**: What the pattern teaches
**Behavioral change**: The specific different action next time

→ Add to `knowledge/decisions/decision-patterns.md`
→ Add to `strategy/bet-log.md` (one-row summary)
→ Add to `knowledge/strategy/bets-history.md` if it reveals a meta-pattern

---

## Input

**Closed bet file**: {{BET_FILE_CONTENTS}}
**Evidence log from the bet period**: {{EVIDENCE_LOG}}
**Monthly verdict sequence**: {{VERDICT_HISTORY}}

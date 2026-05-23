---
name: pm-zero-to-one
description: Structure 0-to-1 product development — founding hypothesis, early customer development, signal vs. noise, and the decisions that distinguish 0-to-1 PM from iteration PM. For new product bets, not feature work.
version: "1.0"
changed: 2026-05-20
---

# PM Zero-to-One

**Input:** Product idea or emerging opportunity, target customer hypothesis, any early signals (interviews, usage data, market signals).

**Output:** Written to `notes/structured/zero-to-one-YYYY-MM-DD-<product-slug>.md`

**Scope:** 0-to-1 product development — the period before product-market fit. This skill is not for feature work on an existing product. The rules of 0-to-1 are different from iteration PM; applying iteration PM methods to 0-to-1 work is a known failure mode.

---

## Steps

1. **State the founding hypothesis.** One paragraph. What do you believe is true about the world that, if correct, makes this product inevitable? The hypothesis must be specific enough to be falsifiable. "People want a better X" is not a hypothesis — it's a wish. "Operators in [segment] lose [N] hours per week to [specific workflow], and no tool has solved it because [reason competitors haven't]" is a hypothesis.

2. **Identify the single riskiest assumption.** Of all the things the hypothesis requires to be true, which one is most likely wrong and would invalidate the whole bet if wrong? This is the first thing to test — not the second or third.

3. **Design the early customer development sprint.** 0-to-1 requires direct customer immersion, not surveys. Who are the 5-10 humans who have this problem most acutely? Identify them specifically. Write the three questions that would falsify the riskiest assumption. Define what a "strong signal" looks like vs. a polite "this sounds interesting."

4. **Define the PMF signal.** What observable behavior, not stated preference, would indicate early product-market fit? Sean Ellis's test ("how would you feel if you could no longer use this product?") is a starting point but is not sufficient alone. Define a behavioral signal: "X% of [cohort] has done [behavior] within [time window]" — retention, depth of use, organic referral.

5. **Draw the 0-to-1 roadmap.** Not quarters — phases. Phase 1: enough to test the riskiest assumption. Phase 2: enough to test whether customers will pay (even if payment is informal commitment). Phase 3: enough to see the PMF signal. Each phase has an explicit kill condition: if [signal] is not observed by [date/milestone], stop.

6. **Write the 0-to-1 PM operating rules.** 0-to-1 is different: no roadmap commitments, no feature OKRs, more direct founder access, faster cycles, higher ambiguity tolerance. State the operating model explicitly so stakeholders know what they're sponsoring.

---

## Output Format

```markdown
# Zero-to-One Product Brief — [Product Name] — [Date]

**PM:** [Name]  **Executive sponsor:** [Name]  **Status:** Hypothesis / Exploring / Testing / Kill review

---

## Founding Hypothesis

[One paragraph. Specific, falsifiable. Names the customer segment, the problem, the frequency and cost of the problem, and why existing solutions don't work. If this paragraph is vague, the bet isn't ready.]

**If this hypothesis is correct:** [What the product opportunity looks like at scale]

**If this hypothesis is wrong:** [What we will have learned, and what it rules out]

---

## Riskiest Assumption

**The single assumption most likely to be wrong:**

[State it as a falsifiable claim: "We believe that [specific customer] has [specific problem] and will [specific behavior] when we provide [specific solution]."]

**Why this is riskiest:** [Why this is more likely to be wrong than the other assumptions]

**What would falsify it:** [Specific observable evidence that this assumption is wrong]

**How we will test it:** [Method — not a survey, a direct observable test]

**Timeline:** [When we will have a signal]

---

## Assumption Stack

| Assumption | Risk level | Test method | Kill signal |
|-----------|-----------|-------------|-------------|
| [Assumption 1 — riskiest] | High | [How to test] | [What failure looks like] |
| [Assumption 2] | Medium | [How to test] | [What failure looks like] |
| [Assumption 3] | Low | [How to test] | [What failure looks like] |

---

## Early Customer Development Plan

**Target cohort:** [5-10 specific humans — not segments, specific people or company types]

**Why these people:** [Why they have the problem most acutely]

**Discovery method:** [Contextual observation / in-depth interview / working session — not survey]

**The three questions:**

1. [Question that would falsify riskiest assumption if answered a specific way]
2. [Question that probes depth and frequency of pain]
3. [Question that tests whether they've tried to solve it and how]

**Strong signal definition:** [What response or behavior from 3+ of these people would constitute evidence that the hypothesis is directionally correct]

**Weak signal (noise):** [What "sounds positive but isn't evidence" looks like — polite interest, vague enthusiasm, "we'd definitely use that"]

**Bad signal (kill condition):** [What response would indicate the hypothesis is wrong]

---

## Product-Market Fit Signal

**Behavioral PMF indicator:** [Specific observable behavior in a specific cohort within a specific time window]

Example format: "[X]% of users who [behavior A] return within [N days] and perform [behavior B]"

**Why this behavior indicates PMF:** [What it means about the product's role in the user's life]

**Measurement method:** [How this will be tracked]

**PMF check date:** [When we will evaluate this signal for the first time]

---

## 0-to-1 Phase Roadmap

### Phase 1 — Test Riskiest Assumption

**Duration:** [Weeks]
**Scope:** [Minimum required to test the riskiest assumption — nothing more]
**Success condition:** [Specific signal that justifies Phase 2]
**Kill condition:** [Specific signal that stops the work]

### Phase 2 — Test Willingness to Pay

**Duration:** [Weeks]
**Scope:** [What's needed to get a payment signal — informal commitment counts]
**Success condition:** [Signal that justifies Phase 3]
**Kill condition:** [What stops the work]

### Phase 3 — Test PMF Signal

**Duration:** [Weeks]
**Scope:** [What's needed to observe the behavioral PMF indicator]
**Success condition:** [PMF signal threshold met]
**Kill condition:** [What triggers a pivot or stop decision]

---

## 0-to-1 Operating Model

**This is not iteration PM.** Stakeholders sponsoring this work should expect:

- No committed feature roadmap. Scope changes as signal is received.
- No standard sprint OKRs. Success is measured by signal quality, not velocity.
- Direct PM access to customers without layers of research scheduling.
- Weekly phase-gate reviews instead of quarterly planning.
- Explicit kill decisions at each phase boundary — this is not a default continuation.

**Decision authority:** [Who can continue or kill at each phase gate]

**Resource commitment:** [What's allocated and for how long]

**Reporting cadence:** [How the executive sponsor will be kept informed]

---

## Kill Decision Record

[Filled in at each phase gate]

| Phase | Date | Signal observed | Decision | Reason |
|-------|------|----------------|----------|--------|
| 1 | | | Continue / Kill / Pivot | |
| 2 | | | Continue / Kill / Pivot | |
| 3 | | | Continue / Scale / Kill | |
```

---

## Quality Gate

- Founding hypothesis is specific and falsifiable (not "people want a better X")
- Riskiest assumption named (the one most likely to invalidate the bet)
- Early customer development targets specific humans, not segments
- "Strong signal" defined behaviorally (not "seemed interested")
- "Kill signal" defined at each phase (not open-ended exploration)
- PMF indicator is a behavioral metric, not a stated preference
- 0-to-1 operating model spelled out for stakeholders before they commit resources

---
name: pm-growth
description: Analyze the product's growth system. Diagnoses funnel leaks, identifies activation path, maps growth loops, and produces a prioritized intervention plan.
version: "1.0"
changed: 2026-05-20
---

# PM Growth

**Input:** Product context, available metrics (funnel data, retention curves, activation rate), any specific growth problem to diagnose.

**Output:** Written to `synthesis/YYYY-MM-DD-growth-analysis.md`

---

## Steps

1. **Read context.** Load `knowledge/pm/growth-frameworks.md`. If metrics data is provided, read it.

2. **Run the growth accounting check.** Establish the baseline:
   - New acquisitions per period
   - Reactivations per period
   - Churn rate
   - Net new user growth rate
   - Is the bucket leaky (acquiring users faster than retaining them)?

3. **Run the funnel diagnosis.** For each AAERM stage, find the conversion rate and benchmark against industry:
   - **Acquisition:** Qualified traffic → signup rate
   - **Activation:** Signup → activation event rate + time-to-activation
   - **Engagement:** Active users → weekly engagement frequency
   - **Retention:** D7 / D30 / D90 retention curves
   - **Monetization:** Free-to-paid conversion, ARPU, expansion rate

   **Identify the stage with the worst conversion relative to potential.** This is the highest-leverage intervention point.

4. **Map the activation path.** What is the sequence of actions that converts a new user into a retained user?
   - What action, if completed in session 1, predicts 90-day retention?
   - What is the current time-to-activation?
   - What is the biggest friction point between signup and activation?

5. **Identify growth loops.** Does the product have any growth loops?
   - Content loop: user creates → attracts new users
   - Viral loop: user invites → K-factor
   - Network value loop: more users → more valuable
   - Data flywheel: more users → better product
   If K-factor: calculate K = (avg invites per user) × (invite conversion rate).

6. **Produce the intervention matrix.** For each funnel stage: current rate, benchmark, gap, highest-leverage intervention, effort to implement.

7. **Prioritize interventions.** Sort by: (impact × confidence) / effort. Top 3 are the recommended starting point.

8. **Write the output.**

---

## Output Format

```markdown
# Growth Analysis — [Product] — [Date]

**PM:** [name]  **Data period:** [Date range]

---

## Growth Accounting

| Metric | Current | Trend |
|---|---|---|
| New acquisitions / month | [N] | ↑/↓/→ |
| Reactivations / month | [N] | |
| Churn / month | [N] | |
| Net growth rate | [N]% | |

**Diagnosis:** [Growing sustainably / Leaky bucket (acquiring faster than retaining) / Acquisition plateau / Retention collapse]

---

## Funnel Diagnosis

| Stage | Current rate | Industry benchmark | Gap | Priority |
|---|---|---|---|---|
| Acquisition (signup rate) | [N]% | [N]% | [N]% | H/M/L |
| Activation (aha moment reach) | [N]% | [N]% | [N]% | H/M/L |
| D7 Retention | [N]% | [N]% | [N]% | H/M/L |
| D30 Retention | [N]% | [N]% | [N]% | H/M/L |
| Free-to-paid conversion | [N]% | [N]% | [N]% | H/M/L |

**Highest-leverage stage:** [Stage — where gap × volume produces most impact]

---

## Activation Analysis

**Current activation event:** [What constitutes "activated"?]  
**Activation rate:** [N]%  
**Median time-to-activation:** [N hours / days]

**Activation path (current):**
1. Signup
2. [Step]
3. [Step]
4. [Activation event]

**Friction points:**
- [Step] has [N]% drop-off — cause: [hypothesis]
- [Step] has [N]% drop-off — cause: [hypothesis]

**Recommended activation path (simplified):**
1. Signup
2. [Reduced steps]
3. Activation event
→ [Estimated time-to-activation reduction]

---

## Growth Loops

**Current loops:**

| Loop type | Exists? | K-factor / Strength | Health |
|---|---|---|---|
| Content loop | Yes / No | [K or qualitative] | Strong / Weak / Non-existent |
| Viral loop | Yes / No | K = [N] | |
| Network value | Yes / No | | |
| Data flywheel | Yes / No | | |

**Loop strengthening opportunities:**
- [Loop type]: [Specific product change that would strengthen this loop]

---

## Intervention Matrix

| Stage | Intervention | Expected impact | Confidence | Effort | Priority |
|---|---|---|---|---|---|
| Activation | [Specific change] | [+N% activation] | H/M/L | [N weeks] | 1 |
| Retention | [Specific change] | [+N% D30] | H/M/L | [N weeks] | 2 |
| [Stage] | [Change] | [Impact] | | | 3 |

---

## Top 3 Recommendations

1. **[Intervention]**  
   Why: [What data supports this priority]  
   How: [Rough approach — not a spec]  
   Measure via: [What metric and by when]

2. **[Intervention]**  
   Why / How / Measure via

3. **[Intervention]**  
   Why / How / Measure via

---

## What Would Change These Recommendations

- If [data we don't have] showed [X], the priority would shift to [Y]
- If [assumption] is wrong, [intervention] becomes lower priority
```

---

## Quality Gate

- Growth accounting completed (net growth = acquisitions + reactivations - churn — all three measured)
- Funnel diagnosis identifies the single highest-leverage stage (not "all stages need work")
- Activation path mapped with specific drop-off points
- Growth loops identified (even if none exist — state that explicitly)
- Intervention matrix has both impact and effort (not just impact)
- Top 3 recommendations each have a measurement plan

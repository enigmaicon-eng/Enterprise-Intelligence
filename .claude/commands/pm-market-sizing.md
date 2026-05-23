---
name: pm-market-sizing
description: Build a market sizing model using TAM/SAM/SOM methodology. Produces bottom-up and top-down estimates with assumptions made explicit and confidence calibrated.
version: "1.0"
changed: 2026-05-20
---

# PM Market Sizing

**Input:** Market or opportunity description, target user segment, any known data points (user counts, revenue benchmarks, pricing).

**Output:** Written to `notes/structured/market-sizing-YYYY-MM-DD-<market-slug>.md`

---

## Steps

1. **Define the market before sizing it.** "The enterprise SaaS market" is not a market — it's a sector. The correct unit is: the set of users with the specific problem you solve, who would pay for your specific solution. Define the problem, then count the people who have it.

2. **Run two approaches:** top-down and bottom-up. If they diverge significantly (>3×), the assumptions need investigation.

3. **Top-down approach:**
   - Start with a known market size (industry report, public data)
   - Apply segmentation filters down to your addressable population
   - Apply willingness-to-pay and reach filters
   - Result: market size estimate with explicit segmentation logic

4. **Bottom-up approach:**
   - Count the number of potential buyers (from first principles or data)
   - Apply average contract value or ARPU (from comparable products or pricing research)
   - Multiply: units × ACV/ARPU = revenue potential
   - Apply penetration assumptions for TAM → SAM → SOM

5. **Define TAM / SAM / SOM clearly:**
   - **TAM (Total Addressable Market):** Maximum revenue if 100% market share. Theoretical ceiling.
   - **SAM (Serviceable Addressable Market):** Users you can realistically reach with current distribution.
   - **SOM (Serviceable Obtainable Market):** Realistic capture in 3-5 years given competitive dynamics.
   - SOM is the only number that matters for business planning. TAM impresses investors; SOM drives decisions.

6. **State every assumption explicitly.** Market sizes that hide assumptions are useless for decision-making. Every number in the model should be traceable to a stated assumption or data source.

7. **Run a sensitivity analysis on the top 2 assumptions.** What happens to SOM if the key assumption is 2× or 0.5× what you estimated?

8. **Produce a confidence rating.** High = most assumptions backed by data. Medium = mix of data and informed estimates. Low = mostly informed estimates.

9. **Write the output.**

---

## Output Format

```markdown
# Market Sizing — [Market/Opportunity Name] — [Date]

**Problem being sized:** [Specific problem, for specific users]  
**PM:** [name]  **Confidence:** High | Medium | Low

---

## Market Definition

**Who has this problem:** [User description — role, context, industry if relevant]  
**What makes someone addressable:** [Criteria to be in the market]  
**What makes someone NOT addressable:** [Exclusion criteria — wrong segment, wrong size, wrong geography]

---

## Top-Down Estimate

**Starting point:** [Industry/market size from source: [source], [year]]  
**Segmentation filters:**
1. [Filter] → [N]% of market → [N] users remaining
2. [Filter] → [N]% of remaining → [N] users remaining
3. [Filter] → [N]% of remaining → [N] addressable users

**Pricing assumption:** [N] ACV × [N] users = [N] TAM

---

## Bottom-Up Estimate

**Unit of count:** [What we're counting — companies, teams, individuals]  
**Count method:** [How derived — industry data / LinkedIn / survey / extrapolation]  
**Estimated addressable units:** [N]

**Average contract value / ARPU:** [N] — [Source / assumption basis]

**TAM:** [N units] × [N ACV] = **[N total]**

---

## TAM / SAM / SOM

| Market | Definition | Size |
|---|---|---|
| TAM | All users with this problem | [N] |
| SAM | Users reachable with current distribution | [N] ([N]% of TAM) |
| SOM (3-year) | Realistic capture given competitive dynamics | [N] ([N]% of SAM) |

**SOM assumptions:**
- Penetration rate: [N]% — Basis: [comparable product / market dynamics reasoning]
- Win rate against alternatives: [N]% — Basis: [win/loss data / assumption]
- Annual growth: [N]% — Basis: [market growth rate / product growth rate]

---

## Assumption Ledger

| Assumption | Value used | Range | Source |
|---|---|---|---|
| Addressable units | [N] | [N] to [N] | [Source] |
| ACV / ARPU | [N] | [N] to [N] | [Source] |
| Penetration rate | [N]% | [N]% to [N]% | Assumption |
| [Other] | | | |

---

## Sensitivity Analysis

**If [key assumption] is 2×:** SOM = [N] — [implication]  
**If [key assumption] is 0.5×:** SOM = [N] — [implication]

**The sizing is most sensitive to:** [Which assumption changes the answer most]

---

## Top-Down vs. Bottom-Up Reconciliation

| Approach | TAM estimate | Difference |
|---|---|---|
| Top-down | [N] | |
| Bottom-up | [N] | [N]× difference |

**Reconciliation:** [If divergent: which number is more trustworthy and why]
```

---

## Quality Gate

- Problem is defined before market is sized (not "the [industry] market")
- Both top-down and bottom-up estimates attempted
- Every assumption is in the assumption ledger with a source or "assumption" label
- SOM is the primary number used for planning (not TAM)
- Sensitivity analysis run on top 2 assumptions
- Confidence rating stated

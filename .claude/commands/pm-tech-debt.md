---
name: pm-tech-debt
description: Assess and prioritize technical debt from a PM perspective. Produces a debt inventory with user impact, investment case for remediation, and negotiation frame for roadmap inclusion.
version: "1.0"
changed: 2026-05-20
---

# PM Tech Debt

**Input:** Debt items raised by engineering, or context about a system that's slowing delivery.

**Output:** Written to `notes/structured/tech-debt-YYYY-MM-DD.md`

---

## Steps

1. **Read context.** Load `knowledge/pm/technical-fluency.md` (technical debt section).

2. **Classify each debt item by type:**
   - **Intentional:** Knowingly accepted for speed. Was it? Who decided? Is there a plan to repay?
   - **Unintentional:** Didn't know it was debt at the time.
   - **Accidental:** Poor design that should be refactored.
   - **Essential:** Inherent problem complexity that can't be eliminated — only managed.

3. **Translate debt into PM-legible impact.** For each debt item, answer in product terms:
   - **Velocity tax:** How much does this slow new feature delivery? (Estimated % of engineering time consumed by this debt)
   - **Quality tax:** Does this debt cause user-facing bugs, errors, or latency?
   - **Risk surface:** Does this debt create security, compliance, or reliability risk?
   - **Opportunity cost:** What can't we build because this debt exists?

4. **Prioritize debt for roadmap inclusion.** Not all debt belongs on the roadmap. Priority for inclusion:
   - P0: Blocking security/compliance remediation — immediate
   - P1: Causing recurring user-facing incidents — next sprint or quarter
   - P2: Slowing feature delivery >15% — include in next planning cycle
   - P3: Technical hygiene with no user impact — engineering discretion

5. **Build the investment case.** For debt the PM wants to include in the roadmap, write the business justification: "If we invest [N person-weeks] in [debt remediation], we gain [velocity / reliability / risk reduction] which enables [specific product outcome] in [timeframe]."

6. **Write the output.**

---

## Output Format

```markdown
# Technical Debt Assessment — [Date]

**PM:** [name]  **Engineering partner:** [name]

---

## Debt Inventory

| Item | Type | Velocity tax | Quality tax | Risk | Priority |
|---|---|---|---|---|---|
| [Debt item] | Intentional/Unintentional/Accidental/Essential | [N]% eng time | [User impact] | Low/Med/High | P0-P3 |

---

## Detailed Assessment (P0 and P1 items)

### [Debt Item 1]

**Type:** [Classification]  
**Description:** [What the debt is — in engineering terms, translated to PM terms]

**Product impact:**
- Velocity: [Specific — e.g., "Adding any new field to the data model requires 3 days of migration work"]
- Quality: [Specific — e.g., "Causes 2-3 user-facing errors per week in the export flow"]
- Risk: [Specific — e.g., "Library version has 2 unpatched CVEs, security review flagged this"]
- Opportunity blocked: [What we can't build because this exists]

**Remediation:**
- Engineering estimate: [N person-weeks]
- Approach: [What would be done]
- Can be done incrementally: [Yes — staged approach / No — requires full refactor]

**Investment case:**
"If we invest [N] person-weeks in [remediation], we will [gain N% velocity / eliminate N user-facing errors / unblock [feature X]] which enables [product outcome] in [timeframe]."

**Recommended priority:** Include in [this quarter / next quarter / engineering discretion]

---

## Negotiation Frame for Roadmap Inclusion

PM's standard is: debt that has user-facing impact OR blocks a roadmap initiative belongs in the roadmap. Debt that is technical hygiene without user impact belongs in engineering's discretionary time.

For each P1 debt item being proposed for roadmap inclusion:
- "This debt is causing [user-facing impact]. If we don't address it, [consequence] by [timeframe]."
- "The investment is [N] weeks. The return is [specific — not 'cleaner code' but 'N hours/week freed for feature work']."

---

## Intentional Debt Ledger

[Track debt that was consciously accepted, so it doesn't get forgotten]

| Debt | Accepted on | Rationale | Planned repayment | Status |
|---|---|---|---|---|
| [Item] | [Date] | [Why accepted] | [When to repay] | Open / Repaid |
```

---

## Quality Gate

- Each debt item is classified by type (intentional/unintentional/accidental/essential)
- User impact is stated in product terms (not engineering terms)
- Investment case for P1+ items is written with specific ROI claim
- Intentional debt ledger captures debts that were deliberately accepted
- Roadmap priority recommendation is stated for each item

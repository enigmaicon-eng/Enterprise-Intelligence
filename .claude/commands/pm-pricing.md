---
name: pm-pricing
description: Design or audit pricing and packaging strategy — value metric selection, tier architecture, WTP research design, and pricing experiment plan. Pricing is the PM's job, not finance's.
version: "1.0"
changed: 2026-05-20
---

# PM Pricing and Packaging

**Input:** Product description, current pricing (if existing), user segments, monetization goal, any known competitive pricing.

**Output:** Written to `notes/structured/pricing-YYYY-MM-DD-<product-slug>.md`

**Scope:** Pricing strategy and packaging design — value metric selection, tier architecture, WTP research, pricing experiment design. For revenue modeling or financial projections, work with Finance.

---

## Steps

1. **Read context.** Load `knowledge/pm/pricing-monetization.md`. If a competitive intelligence document exists, read it.

2. **Identify the value metric.** The value metric is the unit by which customers pay. It must scale with value received. Test candidate metrics: "As a customer gets dramatically more value from our product, which number in their world grows proportionally?" A bad value metric creates the wrong incentives for both the customer and the product.

3. **Design the tier architecture.** Three tiers is the standard for B2B SaaS: free/freemium (acquisition), pro/growth (self-serve conversion), enterprise (sales-assisted). For each tier: what is the primary buyer, what is the value ceiling, what is the gate. The freemium gate should be where the power user lives — not where the average user struggles.

4. **Run a WTP research design.** Select the appropriate method: Van Westendorp (four-question acceptable range), Gabor-Granger (demand curve at discrete price points), or conjoint (feature trade-offs). Design the research with sample size, participant criteria, and analysis plan.

5. **Benchmark against competitors.** What does the closest alternative cost? Price relative to the value advantage, not the alternative's price. If the product delivers 3× the value, pricing at 1.5× leaves a strong value proposition while capturing share of that premium.

6. **Design the pricing experiment.** Never change pricing without a structured experiment. Define: what changes, who sees the change, what the success metric is, what the guardrail metric is, and the grandfathering policy for existing customers.

---

## Output Format

```markdown
# Pricing and Packaging Strategy — [Product Name] — [Date]

**Monetization goal:** [Acquire users / Convert free to paid / Expand within accounts / Maximize NRR]
**Primary buyer:** [Who pays]
**Primary user:** [Who uses — may differ]

---

## Value Metric Analysis

**Candidate value metrics evaluated:**

| Metric | Scales with value? | Measurable? | Customer perception | Decision |
|--------|-------------------|-------------|-------------------|----------|
| Per seat/user | [Yes/Partially/No] | Yes | [How customers feel about it] | |
| Per [usage unit] | [Yes/Partially/No] | [Yes/No] | [Perception] | |
| Per outcome | [Yes/Partially/No] | [Yes/No] | [Perception] | |
| Flat/tier | N/A (bundled) | Yes | Predictable | |

**Selected value metric:** [Name]

**Rationale:** [Why this metric scales with customer value better than the alternatives]

**Risk:** [The way this metric could misalign incentives or create friction]

---

## Tier Architecture

### Free / Freemium Tier

**Primary purpose:** [Acquisition / product-led virality / developer adoption]
**Target user:** [Who is this for]
**Value delivered:** [What they can do — must be genuinely useful, not crippled]
**Gates (what requires upgrade):**
- [Feature/limit] — [Why this gate, not an earlier or later one]
- [Feature/limit]

**Gate design rationale:** [Why the gate is here — where the power user lives, not where the average user struggles]

### Pro / Growth Tier

**Primary purpose:** [Primary monetization for self-serve buyers]
**Target buyer:** [Role, company size]
**Price point:** [$X / [value metric] / [billing cadence]]
**Price rationale:** [Why this number — WTP research, competitive, value multiple]
**What it includes vs. free:** [Delta — the value of upgrading]
**Self-serve or sales-assisted:** [Self-serve — credit card, no sales touch needed]

### Enterprise Tier

**Primary purpose:** [Sales-assisted conversion for large accounts]
**Target buyer:** [Role, company size, compliance/security requirements]
**Price structure:** [Custom / range / floor — annual contract required]
**Enterprise-specific capabilities:**
- Admin controls
- SSO / SAML
- Audit logs
- SLA
- Custom contracts
- [Other]

**Sales cycle involvement:** [Where PM is expected to support]

---

## Pricing Psychology Levers

**Anchoring:** [Which tier is shown first in pricing table — should be highest-value]

**Decoy tier design:** [Which tier makes the recommended tier look like better value]

**Annual vs. monthly default:** [Which is default, what annual discount is offered, rationale]

**Perception risk:** [Any pricing structure choice that might read poorly to buyers — and mitigation]

---

## WTP Research Design

**Method selected:** [Van Westendorp / Gabor-Granger / Conjoint]

**Rationale for method:** [Why this method fits this pricing question]

**Van Westendorp design (if selected):**

The four questions:
1. "At what price would you consider [product] too expensive to consider?"
2. "At what price would you consider [product] so inexpensive you'd question its quality?"
3. "At what price would you consider [product] a bargain — great value for money?"
4. "At what price would you begin to think [product] is getting expensive, but you'd still consider it?"

Expected output: acceptable price range (between "getting expensive" and "too expensive")

**Sample:** [N participants, screener criteria]

**Timeline:** [When research will be fielded and results analyzed]

---

## Competitive Pricing Benchmark

| Competitor | Value metric | Free tier | Pro tier | Enterprise | Our value advantage |
|-----------|-------------|-----------|----------|------------|-------------------|
| [Name] | | | | | |
| [Name] | | | | | |

**Our positioning vs. competitors:** [Premium / Parity / Value / Disruptive]

**Target price relative to closest alternative:** [X× higher / at parity / X% lower] — [rationale]

---

## Pricing Experiment Plan

**What is changing:** [Price point / tier packaging / gate placement / billing cadence default]

**Who sees the change:** [New customers only / geographic segment / cohort]

**Grandfathering policy:** [Existing customers are / are not affected — and the communication plan]

**Success metric:** [Primary metric with target delta]

**Guardrail metric:** [What must not regress — e.g., free-to-paid conversion, NRR]

**Experiment duration:** [Minimum weeks needed for statistical significance]

**Analysis plan:** [Who runs it, when, what constitutes "implement" vs. "revert"]

---

## SaaS Economics Impact

**Current / projected LTV:** [$X — formula: ARPU × gross margin % ÷ churn rate]

**Current / projected CAC:** [$X]

**LTV:CAC ratio:** [X:1 — target >3:1]

**Payback period:** [N months — target <12 for self-serve, <18 for enterprise]

**NRR impact of this pricing change:** [What changes in expansion and contraction behavior]

---

## Open Questions

1. [Pricing question requiring data or research to resolve]
2. [Question requiring Finance or executive alignment]
```

---

## Quality Gate

- Value metric passes the scaling test (grows proportionally with customer value)
- Freemium gate is at the power-user boundary, not the average-user boundary
- Enterprise tier includes the standard compliance/admin capabilities
- WTP research designed with method, sample, and timeline (not "we should research this")
- Competitive benchmark names the specific price delta and value-multiple rationale
- Experiment plan names the grandfathering policy before any change ships
- LTV:CAC ratio calculated and assessed against the 3:1 target

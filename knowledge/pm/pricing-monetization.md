---
title: Pricing and Monetization
domain: pm
created: 2026-05-20
reviewed: 2026-05-20
connections: [product-strategy, growth-frameworks, b2b-enterprise-pm, metrics-experimentation]
confidence: high
source: original synthesis
tags: [pm, pricing, monetization, packaging, value-metric, freemium, saas, cac, ltv]
---

## Definition

Pricing is the conversion of value into revenue. Every pricing decision is a hypothesis: "Users who receive [value] will pay [price] through [model]." Pricing is not finance's job or marketing's job — it is the PM's job, because the PM best understands the value delivered and the users' willingness to pay.

The most common PM pricing failure: treating pricing as a one-time decision made at launch, then never revisiting it. Pricing should be updated as regularly as the product itself.

## The Value Metric — the Foundation of Everything

The value metric is the unit by which customers pay for the product. It must satisfy two conditions:
1. It scales with the value customers receive (as customers get more value, they pay more)
2. It is measurable and auditable by both parties

**Common value metrics by product type:**
- **Per seat / per user:** Simple. Works when value scales with users. Fails when one power user generates all value.
- **Per usage:** API calls, messages sent, records processed. Aligns cost to value precisely. Creates unpredictability for buyers.
- **Per outcome:** Leads generated, transactions processed, diagnoses made. Most aligned. Hardest to measure and bill.
- **Flat / tiered:** Fixed price for a bundle of capabilities. Predictable. Incentivizes over-provisioning.

**The wrong value metric is the most common SaaS pricing mistake.** A project management tool priced per seat charges equally for a team that uses it daily and one that barely logs in. A tool priced per project created charges based on a behavior (project creation) that doesn't scale with value. Value metrics should be chosen after asking: "As a customer gets dramatically more value from our product, which number in their world grows proportionally?"

## Pricing Architecture

**The three-tier structure (most common in B2B SaaS):**

- **Free / Freemium:** Broad adoption, no friction. Gates: the capabilities that turn power users into buyers. Do NOT gate features that drive activation — gate features only power users need.
- **Pro / Growth:** Self-serve, credit card. The primary monetization tier for individual contributors and small teams.
- **Enterprise:** Sales-assisted, annual contract, custom pricing. The primary monetization tier for large organizations requiring admin controls, security, compliance, and SLAs.

**What belongs in each tier:**

| Capability | Free | Pro | Enterprise |
|---|---|---|---|
| Core value proposition | ✓ | ✓ | ✓ |
| Collaboration (basic) | Limited | ✓ | ✓ |
| Advanced features | | ✓ | ✓ |
| Admin controls | | Limited | ✓ |
| SSO / SAML | | | ✓ |
| Audit logs | | | ✓ |
| SLA | | | ✓ |
| Priority support | | | ✓ |
| Custom contracts | | | ✓ |

**The freemium gate design:** The gate should be where the power user lives, not where the average user struggles. If a feature is gated too early, it creates a bad free experience. If it's gated too late, the upgrade incentive disappears.

## Pricing Psychology

**Anchoring:** The first price a customer sees anchors their reference point. Present the highest tier first in pricing tables — not lowest. This makes lower tiers feel like deals rather than the baseline.

**Decoy pricing:** Three tiers where the middle tier is designed to make the top tier look like better value. Most customers pick the middle; some are drawn up to the top.

**The "per seat" perception:** Per-seat pricing creates a mental "per person" cost that buyers multiply by their team size. If team size × per-seat price feels large, buyers round down. Usage-based pricing is often more palatable because the cost feels proportional to use.

**Annual vs. monthly:** Annual contracts improve retention (customers don't churn at renewal if they're not on a renewal cycle), improve cash flow, and reduce churn. Offer annual at a 15-20% discount. Default to annual for enterprise.

## Pricing Research

**Willingness-to-pay (WTP) research methods:**

**Van Westendorp:** Ask four questions: "At what price would you consider this too expensive? Too cheap to be trusted? A bargain? Getting expensive?" The range between "getting expensive" and "too expensive" is the acceptable price range.

**Gabor-Granger:** Test discrete price points. Present a price to a sample; ask if they'd buy at that price. Vary price across samples to find the demand curve.

**Conjoint analysis:** Present users with bundles of features at different price points; ask which they'd choose. Reveals willingness to pay for specific features and the relative value of different packaging configurations.

**Competitive benchmarking:** What does the closest alternative cost? Price relative to the value advantage, not the alternative's price. If your product creates 3× the value of the alternative, you can price at 1.5× and still have a strong value proposition.

## SaaS Economics PMs Must Understand

**CAC (Customer Acquisition Cost):** Total sales + marketing spend ÷ new customers acquired. PM affects CAC through product-led growth and virality.

**LTV (Lifetime Value):** Average revenue per customer × gross margin % ÷ monthly churn rate. The sustainable business condition: LTV > 3× CAC.

**Payback period:** How many months until CAC is recovered from customer revenue. Target: <12 months for self-serve, <18 months for enterprise.

**Net Revenue Retention (NRR):** Starting ARR + expansion - contraction - churn, expressed as % of starting ARR. NRR > 100% means the customer base grows even without new acquisition. This is the most important metric for a mature SaaS business. PM drives NRR through expansion features and retention.

**Gross margin:** Revenue minus cost of goods sold (hosting, support, CS). SaaS gross margins should be 70-80%+. ML-heavy products often have lower gross margins due to inference costs — PM must factor this into pricing.

## Pricing Experiments

Never change pricing without a structured experiment or a staged rollout. Pricing changes have outsized, often irreversible effects on CAC and retention.

**What to test:** Price point (absolute level), packaging (what's included in each tier), billing cadence (monthly vs. annual default), gate placement (where the freemium wall sits).

**How to test:**
- New cohort pricing: new customers see the new pricing; existing customers are grandfathered. Measures acquisition impact without churn risk.
- Geographic test: different pricing in different markets. Requires strong segment separation.
- A/B test of pricing page: test different presentation, not necessarily different prices. Tests conversion impact of framing.

**Grandfathering:** When raising prices, grandfathering existing customers (honoring their existing price) is the standard practice. Retroactive price increases on committed customers destroy trust and create churn.

## Connections

Links to [[product-strategy]] — pricing is a strategic choice that reflects positioning. Links to [[growth-frameworks]] — pricing gates design drives activation and conversion. Links to [[b2b-enterprise-pm]] — enterprise pricing is a commercial negotiation requiring PM involvement.

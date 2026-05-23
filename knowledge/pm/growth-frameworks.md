---
title: Growth Frameworks for PMs
domain: pm
created: 2026-05-20
reviewed: 2026-05-20
connections: [metrics-experimentation, product-strategy, discovery-intelligence]
confidence: high
source: original synthesis
tags: [pm, growth, activation, retention, funnel, loops, monetization, virality]
---

## Definition

Growth is not a feature or a team — it is a property of the product system. A product grows sustainably when the value it delivers to existing users causes new users to discover it, try it, and stay. Growth frameworks give PMs the vocabulary to analyze, diagnose, and intervene in this system.

## The Growth Accounting Framework

Every product's user base changes by exactly four forces:

**Net new users = New Acquisitions + Reactivations − Churned Users − Dormant Users**

Most PMs fixate on acquisition. The highest-leverage PM work is usually retention. Acquiring a user you can't retain produces a leaky bucket — growth spending without compounding.

**The three growth modes:**
- **Paid growth:** CAC-driven. Sustainable only if LTV > 3× CAC and payback period < 12 months.
- **Viral growth:** User-driven. Sustainable when the viral coefficient k > 1 (each user brings >1 additional user).
- **Organic / product-led growth (PLG):** Value-driven. Sustainable and defensible. The hardest to build, the most durable.

Elite PMs design products for organic and viral growth first, then amplify with paid.

## The Funnel

Every user journey passes through the same stages. Diagnosis starts by finding where the funnel leaks most.

**AARRR (Pirate Metrics) — diagnosis framework only, not a reporting framework:**

| Stage | Question | Leading Metric | Intervention Type |
|---|---|---|---|
| Acquisition | Are the right users finding us? | Qualified traffic, signup rate | Marketing, SEO, partnerships |
| Activation | Do users reach first value? | Activation rate, time-to-value | Onboarding, UX, feature education |
| Retention | Do users come back? | D7/D30/D90 retention, habit formation | Core value loop, notifications, features |
| Referral | Do users bring others? | K-factor, invite rate, NPS | Virality hooks, network effects |
| Revenue | Do users pay? | Conversion rate, ARPU, expansion revenue | Pricing, packaging, upsell flows |

**The diagnostic sequence:** Measure each funnel stage. Find the stage with the worst conversion rate relative to its potential. Fix that stage before the next one. Moving downstream without fixing upstream is wasted effort.

## Activation — The Most Underinvested Stage

Activation is the moment a new user experiences the core value of the product for the first time. This is the highest-leverage stage because:
1. Users who activate retain at dramatically higher rates
2. It's entirely within the product team's control
3. Most products have terrible activation rates (median ~25%)

**The activation framework:**

1. **Define the activation event.** Not account creation — the first moment of genuine value. For Slack: sending a first message AND receiving a reply in the same channel. For Dropbox: saving a file and accessing it from a second device.

2. **Measure time-to-activation.** Users who activate in session 1 retain at 3-5× the rate of users who activate in session 2+. Speed matters.

3. **Build the activation path.** Every step between signup and activation is friction. Map every step. Remove or simplify each one. Typical: reduce 8-step onboarding to 3 required steps + progressive disclosure.

4. **The empty state problem.** Most products are useless when empty. "You have no tasks" is a dead end. Fill the empty state with sample data, suggested actions, or templates that demonstrate value.

5. **The aha moment test.** Interview users who converted AND users who signed up and left. Compare: what did converters do in their first session that leavers didn't? That's your activation path.

## Retention — The Engine of Sustainable Growth

**Retention curve shapes:**

- **Decaying to zero:** Product has no durable value. The retained user base will reach zero. No amount of acquisition fixes this.
- **Decaying to a non-zero asymptote:** Some users find durable value, most don't. Segment and optimize for the retained cohort.
- **Smiling curve:** Retention dips then recovers. Usually a sign of strong seasonal patterns or a secondary value unlock.
- **Flat or improving over time:** Elite retention. Users who stay become more engaged. Usually a sign of network effects or deepening workflow integration.

**The retention diagnosis:**
1. Calculate D7, D30, D90 retention by cohort
2. Segment retained vs. churned users: what did retained users do that churned users didn't?
3. Find the "power user path" — the sequence of actions in week 1 that predicts 90-day retention
4. Build the product to make that path the default path for all new users

**Retention levers:**
- **Habit formation:** Make the product part of a daily/weekly workflow. Notifications, email digests, and integrations serve this.
- **Switching costs:** The more data, history, and integrations a user accumulates, the harder switching becomes. Design for accumulation.
- **Network effects:** Value increases as more users join. If your product has this, protect it — it's a compounding moat.
- **Feature depth:** Power users who discover advanced features retain at much higher rates. Progressive feature disclosure drives retention.

## Growth Loops — The Compounding Alternative to Funnels

Funnels are linear (input → output). Growth loops are cyclical — the output of one cycle becomes the input of the next. Products with growth loops compound; products with only funnels decay.

**Common growth loop patterns:**

**The content loop:** User creates content → content attracts SEO/social traffic → new users discover product → some become creators → more content. (Pinterest, YouTube, Notion)

**The viral loop:** User invites → recipient joins → recipient invites → ... K-factor = (avg invites sent) × (invite conversion rate). If K > 1, loop is self-sustaining.

**The network value loop:** More users → product is more valuable to each user → retention improves → word-of-mouth increases → more users. (LinkedIn, WhatsApp, Slack)

**The data flywheel:** More users generate data → model improves → product is better → more users attracted. (Spotify, TikTok, Google)

**PM question for growth loop design:** "What does the user do that makes the product more valuable for the next user?" If the answer is nothing, there's no loop — the product is a one-way value extraction.

## Virality

**K-factor = (avg invites per user) × (invitation conversion rate)**

- K > 1: viral growth (user base grows without acquisition investment)
- K = 0.5-1: viral assistance (acquisition costs are reduced)
- K < 0.5: minimal viral contribution (acquisition is the only lever)

**Virality types:**
- **Inherent virality:** Using the product requires or produces value for others. (Calendly, Figma, Google Docs — sharing is the value)
- **Incentivized virality:** Users invited in exchange for a reward. (Dropbox referral program) Lower quality; works for bootstrapping.
- **Word-of-mouth virality:** Users recommend without product-embedded hooks. Driven by NPS and genuine delight.

**The referral program anti-pattern:** Building referral mechanics before the product creates genuine delight. Incentivized virality with a mediocre product fills the funnel with low-quality users who churn — wasting acquisition budget and diluting retention metrics.

## Monetization

**Revenue expansion levers (highest to lowest LTV impact):**
1. Reduce churn (retaining existing revenue)
2. Upsell (move users to higher tiers)
3. Expand usage (usage-based billing)
4. Cross-sell (adjacent products)
5. Acquire new users

Most PMs focus only on #5 (new users). Elite PMs drive growth through #1-4 first because the economics are dramatically better and the signal quality is higher.

**Pricing design principles:**
- Price to the value metric (what users pay for should scale with the value they receive)
- Freemium gates should be where power users live, not where casual users struggle
- Annual contracts improve retention dramatically (users don't churn at renewal if they're not on a renewal cycle)

## Connections

Links to [[metrics-experimentation]] — growth metrics are a subset of the metrics stack. Links to [[product-strategy]] — growth loops are a strategic moat, not a feature. Links to [[discovery-intelligence]] — activation path is found through research, not assumption.

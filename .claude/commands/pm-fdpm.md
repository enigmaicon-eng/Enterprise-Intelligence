---
name: pm-fdpm
description: Structure a forward deployed PM engagement — pre-engagement scoping, embed-phase intelligence capture, handoff documentation, and product debrief. Converts customer immersion into structured product intelligence.
version: "1.0"
changed: 2026-05-20
---

# PM Forward Deployed Engagement

**Input:** Customer name, engagement objective, duration, known constraints or integration context.

**Output:** Written to `notes/structured/fdpm-YYYY-MM-DD-<customer-slug>.md`

**Scope:** Full FDPM engagement lifecycle — pre-engagement through product intelligence debrief. For general enterprise PM strategy, consult `knowledge/pm/b2b-enterprise-pm.md`.

---

## Steps

1. **Read context.** Load `knowledge/pm/forward-deployed-pm.md` and `knowledge/pm/b2b-enterprise-pm.md`.

2. **Map pre-engagement requirements.** Who are the buyers, champions, users, and skeptics? What does the customer currently do — processes, tools, data architecture? What is the agreed success definition (stated as a measurable outcome, not an activity)? What technical constraints (stack, security, integrations) must the solution fit within?

3. **Write the embed phase plan.** Week 1 must be observation-first — not building. Define the observation targets (which users, which workflows). Define the rapid scoping cycle (2-3 day loops: observe → scope → build/configure → test → repeat). Define the configuration vs. build vs. core-feature-request decision criteria for this engagement.

4. **Design the daily knowledge capture template.** Every day on-site must produce a structured log: observations, learnings, what was built, open questions. This is the discipline that produces product intelligence.

5. **Write the handoff plan.** What must the customer be able to do without FDPM presence? What documentation must exist? What are the top 5 failure modes and their recovery steps? Who is the named contact for ongoing support?

6. **Write the product intelligence debrief.** The post-engagement structured output to the core product team: what was configured that should be a product feature, what was built that belongs in the core product, what workflows the product doesn't serve, what assumptions proved wrong, what expansion opportunity exists.

---

## Output Format

```markdown
# FDPM Engagement Plan — [Customer Name] — [Date]

**Engagement objective:** [One sentence — measurable customer outcome]
**Duration:** [Weeks]
**PM:** [Name]  **Technical lead:** [Name if applicable]

---

## Pre-Engagement Map

### Stakeholder Register

| Role | Name | Function | Posture |
|------|------|----------|---------|
| Buyer | | | |
| Champion | | | [Who advocates internally for this] |
| Primary users | | | |
| Skeptic / blocker | | | [Who needs to be managed] |

### Current State

**What they currently do:** [Process description — what happens today without the product]

**Systems in use:** [Tools, platforms, data sources]

**Data architecture:** [Relevant schema, integration points, security constraints]

**Technical constraints:** [Stack requirements, security policies, integration mandates]

### Success Definition

**Agreed outcome by end of engagement:** [Measurable — not "they'll be happy with it"]

**How it will be measured:** [Specific metric or observable behavior]

**What "not a success" looks like:** [Explicit failure definition — prevents scope drift]

---

## Embed Phase Plan

### Week 1 — Observation Priority

Observation targets (who to shadow, which workflows):
- [User type]: [Workflow to observe]
- [User type]: [Workflow to observe]

**Output of week 1:** [Prioritized list of pain points and workflow map — no building yet]

### Rapid Scoping Cycles (Week 2+)

**Cycle structure:** Observe painful workflow → scope solution (½ day) → build/configure → test with real users → capture learnings → repeat

**Cycle cadence:** 2-3 days per cycle

**Decision criteria for each solution:**

| Situation | Decision |
|-----------|----------|
| Available within existing product parameters | Configure — do not build |
| Requires light scripting that customer CS can maintain | Script — document fully |
| Structural need affecting multiple customers | Document as core feature request — do not build custom |
| Customer-specific workflow that won't generalize | Build with explicit maintenance owner identified |

### Daily Knowledge Capture

End of each on-site day, log:

```
Date:
Observed: [What I watched users do]
Learned: [What this revealed about the product gap or customer context]
Built/Configured: [What was completed today]
Open questions: [What I still don't know]
Product signal: [Anything that belongs in a core feature request]
```

---

## Handoff Plan

**Customer operational independence:** What must be true for the customer to operate without FDPM present?

Handoff checklist:
- [ ] Solution documentation written (what was deployed, how it works)
- [ ] Top 5 failure modes documented with recovery steps
- [ ] Named customer contact for day-to-day operation
- [ ] Named internal contact (CS or support) for escalation
- [ ] Training completed with primary users
- [ ] Success criteria measured against pre-engagement baseline

**Post-handoff support model:** [Who owns customer support after FDPM leaves]

---

## Product Intelligence Debrief

**To:** Core product team  
**From:** [FDPM name]  
**Customer:** [Name]  
**Engagement dates:** [Start] → [End]

### What We Configured That Should Be a Product Feature

| Configured workaround | Why it's a product gap | Estimated customer count affected |
|----------------------|----------------------|----------------------------------|
| [What FDPM configured] | [Why this shouldn't require FDPM] | [How many customers face this] |

### What We Built That Belongs in Core Product

| Custom build | Why it generalizes | Estimated effort to productize |
|-------------|-------------------|-------------------------------|
| [What was scripted/built] | [Why other customers need this] | [Rough estimate] |

### Workflows the Product Doesn't Serve

| Workflow observed | Why the product doesn't fit | PM recommendation |
|------------------|----------------------------|-------------------|
| [Workflow] | [Gap] | [Feature / redesign / out of scope] |

### Assumptions the Engagement Proved Wrong

| Assumption we held | What the engagement revealed | Implication for roadmap |
|-------------------|------------------------------|------------------------|
| [What we believed] | [What actually happened] | [What changes] |

### Expansion Opportunity

**Next use case at this customer:** [Specific opportunity]
**Expansion trigger:** [What condition makes this opportunity addressable]
**Revenue potential:** [Rough estimate if known]

---

## Engagement Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Scope drift | | | Re-anchor to success definition weekly |
| Going native | | | Weekly check: is this customer-specific or generalizable? |
| Knowledge capture failure | | | Non-negotiable daily log — no exceptions |
| Technical over-build | | | Every custom build needs named maintenance owner before writing a line |
```

---

## Quality Gate

- Measurable success definition agreed before engagement begins
- Stakeholder map identifies skeptic/blocker (not just champion)
- Week 1 is observation-only (no building until workflow is understood)
- Configuration vs. build vs. core-feature-request criteria stated explicitly
- Daily knowledge capture template embedded in plan
- Handoff checklist names every condition for customer independence
- Product intelligence debrief addresses all four output categories (configured → feature, built → core, workflow gaps, wrong assumptions)
- Expansion opportunity identified

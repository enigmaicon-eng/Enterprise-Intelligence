---
name: pm-teardown
description: Run a structured competitive product teardown — UX critique, user flow analysis, feature inventory, positioning inference, and strategic implications. Converts a product experience into structured competitive intelligence.
version: "1.0"
changed: 2026-05-20
---

# PM Competitive Product Teardown

**Input:** Competitor product name, specific flow or feature to teardown, teardown objective (understand positioning / find weakness / benchmark UX / map features).

**Output:** Written to `notes/structured/teardown-YYYY-MM-DD-<competitor-slug>.md`

**Scope:** Deep single-competitor teardown of a specific product area or flow. For broad competitive landscape mapping, use `/pm-competitive`. For positioning implications, use `/pm-positioning`.

---

## Steps

1. **Read context.** Load `knowledge/pm/competitive-intelligence.md`. If a competitive landscape document exists, read it first.

2. **Define the teardown objective.** A teardown without a specific objective produces a list of observations, not intelligence. State: "What question will this teardown answer?" Options: What design decisions reveal about their strategy? Where are they weak? How do they handle a specific use case? What can we learn from their onboarding?

3. **Document the entry point and first impression.** How does a new user arrive? What is the first screen? What is the call to action? What mental model does the product assume the user brings? What question does the product answer in the first 60 seconds?

4. **Walk the primary flow.** Document every step of the core user flow: entry → goal completion. Note: decision points (what choices is the user forced to make?), friction points (where is it slower, harder, or less clear than expected?), delight moments (where is it surprisingly good?), and design decisions (what are they optimizing for?).

5. **Inventory the features.** What capabilities exist? What is present that our product lacks? What is absent? What are the constraints or limits in place? Note the packaging: which features are free, which are paid, which are enterprise-only?

6. **Infer the positioning.** Based on what they built, what did they decide was most important? What user segment does the design optimize for? What trade-offs did they make — and what does that reveal about their strategy or beliefs?

7. **Assess the weaknesses.** Every product optimizes for something at the expense of something else. Where does their design break down? Where does the UX fail the user? What use case are they clearly not trying to serve?

8. **Derive the strategic implications.** What should we do differently, faster, or better because of what this teardown revealed?

---

## Output Format

```markdown
# Competitive Teardown — [Competitor] — [Flow/Feature] — [Date]

**Teardown objective:** [The specific question this answers]
**PM:** [Name]
**Method:** [Self-use / User session observation / Screenshot review / App store research]

---

## First Impression

**Entry point:** [How a new user arrives — ad, search, referral, direct]

**First screen:** [What the user sees immediately]

**Value proposition communicated in 60 seconds:** [What promise does the product make in the first minute]

**Mental model assumed:** [What prior knowledge or expectation does the design require]

**First impression quality:** [Strong / Neutral / Weak] — [Why]

---

## Primary Flow Walkthrough

**Flow:** [Name of the flow being documented — e.g., "New user onboarding to first value moment"]

| Step | Screen / State | User action | Observation | Quality |
|------|---------------|-------------|-------------|---------|
| 1 | [Screen name] | [What user does] | [What's notable] | Good / Neutral / Poor |
| 2 | | | | |
| 3 | | | | |

**Friction points (where flow breaks down):**
1. [Step N]: [What happens, why it's friction, what the user must do to continue]
2. [Step N]: [Same]

**Delight moments (where it's surprisingly good):**
1. [Step N]: [What happens, why it's better than expected]

**Flow length:** [N steps / N seconds to complete — benchmark against our product]

**First value moment:** [At what step does the user first experience the product's core value]

---

## Feature Inventory

### Core Features

| Feature | Description | Available in | Quality | Notes |
|---------|-------------|-------------|---------|-------|
| [Feature] | [What it does] | [Free / Pro / Enterprise] | [Strong / Adequate / Weak] | |

### Features We Have, They Don't

| Feature | Implication |
|---------|-------------|
| [Feature] | [What this means for our competitive position] |

### Features They Have, We Don't

| Feature | User need it serves | Priority for us | Notes |
|---------|--------------------|-----------------|----|
| [Feature] | [Why users want this] | [High / Medium / Low / Not relevant] | |

### Notable Feature Design Decisions

| Decision | What it reveals about their strategy |
|----------|-------------------------------------|
| [Design choice] | [Strategic inference] |

---

## UX and Design Assessment

**Information architecture:** [How is the product organized — where does navigation live, how do users find things]

**Visual hierarchy:** [What is emphasized, what is de-emphasized — does it match the user's priorities?]

**Copy and language:** [How do they talk about the product — jargon, plain language, technical, accessible]

**Mobile vs. desktop:** [Which is primary, how well does the secondary experience work]

**Performance:** [Load times, responsiveness — any notable issues]

**Accessibility (observable):** [What's apparent about accessibility priority]

**Overall UX quality:** [Strong / Adequate / Weak] — [Primary reason]

---

## Pricing and Packaging Observation

**Free tier limits:** [What is included, what is gated]

**Pro tier price and value:** [Price point, what it unlocks, who it's designed for]

**Enterprise tier signals:** [What enterprise capabilities are present, any pricing signals]

**Pricing psychology in use:** [Anchoring, decoy, annual default, etc.]

**Pricing gaps or weaknesses:** [What their pricing structure might alienate or underprice]

---

## Positioning Inference

**Who they are clearly optimizing for:** [Specific user segment, inferred from design decisions]

**What they believe is most important:** [The trade-off their design reveals]

**Who they are NOT trying to serve:** [The use case or user they've visibly deprioritized]

**Their positioning hypothesis (inferred):** "[For X, who needs Y, our product is the Z that does W, unlike [alternative] which does V]"

**Evidence for this inference:** [What in the product supports this reading]

---

## Weakness Assessment

| Weakness | Severity | Root cause (inferred) | Opportunity for us |
|---------|---------|----------------------|-------------------|
| [Where they fail the user] | High / Medium / Low | [Design choice, strategy, resource] | [How we can exploit] |

---

## Strategic Implications

**What this teardown changes about how we think about the competitor:**
[One paragraph — what was surprising or different from assumptions]

**Immediate implications for our roadmap:**
1. [Specific implication — what we should do or stop doing]
2. [Implication]

**Defensive implications (what they might do next):**
[Based on their current direction, what is the likely next move — and what does that mean for us]

**Recommended next action:** [Specific — share with team / update competitive landscape / bring to roadmap review / escalate]
```

---

## Quality Gate

- Teardown objective stated as a specific question (not "understand the competitor")
- Primary flow documented step-by-step (not summarized)
- Feature inventory separates "they have, we don't" from "we have, they don't"
- Positioning inferred from design decisions (not from their marketing copy)
- Weaknesses named specifically (not "their UX could be better")
- Strategic implications are actionable (not observational)
- One recommended next action at the end

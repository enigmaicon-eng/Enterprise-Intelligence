# Architecture Review Prompt
## PM Participation in Technical Decision-Making

**Use when:** Preparing for an architecture review, evaluating a build/buy/partner decision, or reviewing a significant technical proposal. Also use to translate a technical decision into its product and strategic implications.

**Principle from `knowledge/pm/technical-fluency.md`:** The PM's role in architecture decisions is not to make the technical call — it is to ensure the technical decision is made with full visibility into product intent, user constraints, and strategic trade-offs.

---

## The Prompt — Architecture Review Preparation

```
Help me prepare for an architecture review on the following technical decision.

CONTEXT:
- Technical proposal: [Describe the architecture decision or options being considered]
- Decision owner: [Engineering lead / CTO / name]
- PM role in this review: [Consulted / Informed / providing requirements]
- Business context: [What product outcome is this decision serving?]

WHAT I NEED TO UNDERSTAND:

1. Product implications:
   - What user-facing behavior does each option enable or constrain?
   - What feature work becomes easier or harder under each option?
   - What would a user notice differently (performance, reliability, limitations)?

2. Strategic implications:
   - Which option gives us more strategic flexibility? (optionality)
   - Which option creates the stronger platform / compounding advantage?
   - Are there lock-in risks? (vendor lock-in, API contracts, data migration costs)

3. Reversibility assessment:
   - How hard is it to change this decision later?
   - What's the cost of changing it in 12 months? In 3 years?
   - What would make us want to change it?

4. Risk surface:
   - What are the failure modes of each option?
   - What's the performance ceiling? The scale ceiling?
   - What security surfaces does each option create?
   - What happens to existing users during migration (if applicable)?

5. PM questions to ask in the review:
   - Generate 5 questions a PM should ask that engineering might not have considered

OPTIONAL — Build/Buy/Partner:
If this is a build vs. buy vs. partner decision, evaluate:
- Build: what's the unique PM/product reason to own this? What's the ongoing maintenance cost?
- Buy: what's the lock-in risk? What does the vendor roadmap look like? What's the integration complexity?
- Partner: what's the dependency risk? What happens if the partner pivots or fails?

OUTPUT FORMAT:
Section 1: What each option enables/constrains for the product
Section 2: Strategic and optionality comparison
Section 3: Reversibility matrix
Section 4: Top 5 PM questions for the review
Section 5: PM recommendation (which option best serves product intent, and why)
```

---

## Output Template

```markdown
# Architecture Review Prep — [Decision Name] — [Date]

## Decision Summary
[One paragraph: what's being decided, what's at stake, who decides]

## Product Implications by Option

| Dimension | Option A | Option B | Option C (if any) |
|---|---|---|---|
| User-facing behavior | | | |
| Features enabled | | | |
| Features constrained | | | |
| Performance impact | | | |
| Scale ceiling | | | |

## Strategic Analysis

**Optionality:** [Which option preserves or expands future choices?]
**Platform potential:** [Which option creates compounding advantages?]
**Lock-in risk:** [Which option creates the most problematic dependencies?]

## Reversibility Matrix

| Option | Cost to reverse in 12mo | Cost to reverse in 3yr | What triggers reversal |
|---|---|---|---|
| A | | | |
| B | | | |

## PM Questions for the Review

1. [Question — framed to surface product constraint not obvious from technical specs]
2. [Question — about user impact during transition or failure]
3. [Question — about the decision's effect on adjacent product areas]
4. [Question — about the scale or performance ceiling relative to product ambitions]
5. [Question — about long-term maintenance cost and who owns it]

## PM Recommendation

**Recommended option:** [Name]
**Rationale:** [Product and strategic reasons — not technical reasons]
**Conditions:** [What would change this recommendation?]
**What I need from engineering:** [Specific clarifications or constraints to confirm]
```

---

## Architecture Vocabulary Quick Reference

**Coupling:** How much does a change in one component require changes in another? High coupling = brittle. (Reference: `knowledge/pm/technical-fluency.md`)

**Cohesion:** Does this component do one thing or many? High cohesion = maintainable.

**Technical debt types:**
- Intentional: consciously accepted for speed, planned to repay
- Unintentional: didn't know it was debt at the time
- Accidental: complexity from poor design, avoidable
- Essential: inherent problem complexity, cannot be eliminated

**Scalability constraints:** Where does the system break under load? CPU, memory, I/O, network, database, external API rate limits — which is the bottleneck?

**API contract:** The interface between systems. Changing it breaks consumers. Breaking changes require versioning or coordinated migration.

---

## Quality Gates

- [ ] You understand what the decision enables or constrains for users — not just for the engineering team
- [ ] You can articulate the reversibility cost before the meeting
- [ ] Your questions are product-and-user-facing, not technical (engineers have enough technical questions)
- [ ] If you have a recommendation, it's framed around product intent — not overriding the technical decision
- [ ] You know your role (Consulted vs. Informed) and are not overreaching

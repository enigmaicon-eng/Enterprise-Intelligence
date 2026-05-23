# Prioritization Playbook
## Decision Orchestration for Product Managers

The point of prioritization is not to rank things. It is to make trade-offs explicit and get the right people aligned on them. A prioritization process that produces a rank-ordered list but hides the trade-offs has failed.

---

## The Prioritization Standard

Before running any prioritization session, answer these questions:

1. **What are we optimizing for?** Which metric or strategic objective does the winner of this prioritization serve? If the answer is "everything," you cannot prioritize.

2. **What is the time horizon?** Quarterly allocation, sprint-level, annual roadmap? Different horizons require different inputs.

3. **Who decides?** Name the decision owner. If more than one person "approves," you have a governance problem, not a prioritization problem.

4. **What is the opportunity cost?** Name the top 3 things you will NOT do if the winning item gets resourced. If you can't name the trade-offs, you haven't prioritized.

---

## Framework 1 — Strategic Alignment Test (First Gate)

Before any scoring: does this item test or advance a strategy assumption?

Run every candidate through:

| Question | Answer |
|----------|--------|
| Which strategy assumption does this test or advance? | [Name the assumption] |
| Which horizon does this belong to? (H1/H2/H3) | [Horizon] |
| What bet are we making? What's the falsification condition? | [Bet + kill condition] |
| If our strategy is wrong, does this still create value? | Yes / No |

Items that can't answer these questions belong on the parking lot, not the roadmap.

---

## Framework 2 — RICE++ (For Scored Prioritization)

Standard RICE (Reach × Impact × Confidence ÷ Effort) is useful but obscures too much. Use RICE++ which adds explicit trade-off fields.

**RICE++ Fields:**

- **Reach:** How many users are affected per period? (Use real data, not aspirations)
- **Impact:** What magnitude of change on the primary metric? (1=minimal, 3=moderate, 10=transformational — force 10s to be rare)
- **Confidence:** How sure are you? (100%=proven by data, 50%=strong intuition, 20%=speculation)
- **Effort:** Person-weeks across all functions, including PM, design, QA, data
- **Strategic multiplier:** Does this compound the position (2x), is it neutral (1x), or does it fragment focus (0.5x)?
- **Reversibility:** Can this be undone in <1 sprint (High), 1-3 sprints (Medium), or not at all (Low)?
- **Trade-off declaration:** What are the top 2 things we cannot do if we do this?

**Score:** (Reach × Impact × Confidence × Strategic multiplier) ÷ Effort

**The strategic multiplier is the most important field.** A high-scoring RICE item with a 0.5x multiplier (fragments focus) should rank below a moderate-scoring item with a 2x multiplier (compounds position).

---

## Framework 3 — Opportunity Scoring (For Discovery Prioritization)

For ranking problem areas before solutions are defined. Uses Tony Ulwick's opportunity algorithm adapted for strategic alignment.

**For each problem area:**

- **Importance score:** How important is solving this to the target user? (1-10, use research data)
- **Satisfaction score:** How satisfied are they with current solutions? (1-10, use research data)
- **Opportunity score:** Importance + max(Importance - Satisfaction, 0) — ranges from 10 to 20
- **Strategic relevance:** Does solving this advance a strategy assumption? (High / Medium / Low / None)
- **Competitive differentiation:** Would solving this distinguish us from competitors? (High / Medium / Low)

**Priority:** Items with opportunity score >15 AND strategic relevance=High are where discovery investment pays off most.

---

## Framework 4 — The Reversibility Bias

When two items are roughly equivalent on other dimensions, prefer the more reversible one. This is not risk aversion — it is preserving optionality.

**Reversibility rule:** Never make an irreversible decision before you have to. The deadline for the decision reveals how much information you'll have by then. If you have to decide today but could decide in 3 weeks with significantly more information, find a way to decide in 3 weeks.

**Signals that a decision is less reversible than it appears:**
- It involves a customer commitment (pricing, API contracts, advertised features)
- It requires significant technical work to undo (data migrations, architectural changes)
- It changes an org structure or headcount (extremely difficult to reverse)
- It creates an external dependency (partner integrations, platform requirements)

---

## Framework 5 — Kill Criteria (For Bets in Flight)

Every initiative in H2 should have explicit kill criteria written at launch. Apply these at each quarterly review:

**Kill signals:**
- The hypothesis is proven false by evidence (not just disappointing metrics — evidence the underlying assumption was wrong)
- The opportunity size has shrunk materially since the bet was made
- Competitive dynamics have changed such that winning this bet no longer advances our position
- Resource cost has exceeded planned budget by >50% with no clear path to resolution
- The initiative has been descoped to the point where the original value proposition is no longer achievable

**Kill process:** Calling a kill is good PM work. It frees resources for better bets. The failure is not the kill — it is continuing to invest after kill signals are present.

---

## Prioritization Anti-Patterns

**The HIPPO override:** Highest Paid Person's Opinion overrides the prioritization output. Fix: make trade-offs explicit before the HIPPO weighs in. "If we do X (HIPPO's preference), we won't do Y and Z (the team's top priorities). Is that the right trade-off?"

**Everything is a priority:** When there are more P0s than capacity, there are actually no P0s. Fix: hard capping on the number of P0/P1 items. If everything is critical, nothing is.

**Stack-rank without trade-offs:** Producing a list without naming what's cut. Fix: for every top-10 item added to the roadmap, name 1 item that drops off.

**Scoring theater:** Running a scoring framework but overriding it every time. Fix: document the override and its rationale. If you override the framework consistently, the framework is wrong — update it.

**Recency bias:** The most recent user complaint, executive request, or competitor announcement lands at the top of the roadmap. Fix: all new items enter the prioritization queue and compete through the framework, not around it.

---

## The Prioritization Meeting

**Before the meeting:**
- Pre-read with all inputs sent 24h in advance
- Alignment on the optimization target (what are we maximizing for?)
- Individual scoring done before the group meets (prevents anchoring)

**During the meeting:**
- Share individual scores; surface divergences before resolving them
- Divergences are the data — find the underlying assumption that explains the divergence
- Document trade-offs explicitly: "To prioritize A, we are not doing B and C"
- Decision owner calls the outcome; consultation is not veto power

**After the meeting:**
- Write the outcome and the trade-off record within 24 hours
- Share with everyone who was consulted (not just who was in the room)
- Set the review date: when will we re-evaluate the top items?

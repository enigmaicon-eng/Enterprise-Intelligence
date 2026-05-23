# Scope Trade-Off Framework
## Deciding What to Cut When Time, Resources, or Quality Are Constrained

Every PM eventually faces the triangle: scope, timeline, quality — you can control two. The scope trade-off framework forces this decision to be explicit, deliberate, and documented rather than happening informally under pressure.

---

## When to Apply This Framework

Use when any of these are true:
- Engineering has estimated more effort than available time
- A dependency has slipped and the launch date is fixed
- A new requirement has arrived after scoping is complete
- The quality bar cannot be met at the current scope within the timeline
- Leadership has mandated a date without adjusting scope

---

## The Scope Decision Matrix

Before cutting anything, categorize all in-scope items:

| Category | Definition | Decision |
|---|---|---|
| **Core** | Removing this makes the feature fail to deliver its primary value proposition | Never cut |
| **Enabling** | Required for core to work correctly (performance, security, error handling) | Cut only with explicit risk acceptance |
| **Enhanced** | Makes core better but core works without it | Cut to P1 (ship later) |
| **Nice-to-have** | Adds polish, edge case coverage, or secondary value | Cut to P2 or defer indefinitely |

**The categorization exercise:** For each item in scope, ask: "If we ship without this, does the primary success hypothesis still hold?" If yes, it's not Core. If no, it is.

---

## The MVP Calibration Test

Before making any cuts, validate that the current MVP definition is correct:

1. **State the minimum:** "The smallest thing we can ship that tests the hypothesis [X] and delivers value to user [Y]."

2. **Test it against the success metric:** If the MVP as defined won't move the primary success metric, the hypothesis is wrong — not the scope.

3. **Test it against user experience:** A technically minimal feature that creates a confusing or harmful user experience is not a viable MVP. The floor is: users should be able to accomplish their goal without help.

4. **Test it against reversibility:** If the MVP creates user-facing commitments that are hard to walk back (pricing, API contracts, announced features), the bar for quality is higher — irreversible MVPs require more completeness.

---

## The Scope Cut Protocol

When a cut is required, execute in this order:

**Step 1 — List all candidates for deferral.**
Never propose a single cut — propose 3-5 options. One option is ultimatum; three options is negotiation.

**Step 2 — Score each option on three dimensions:**
- User impact: how many users are affected, and how significantly?
- Technical debt: does cutting this create rework when we re-add it later?
- Risk: does cutting this introduce a failure mode or quality degradation?

**Step 3 — Select the cut(s) with lowest user impact + lowest technical debt + acceptable risk.**

**Step 4 — Write the scope change document.** Not a Slack message — a written record.

```yaml
scope_change:
  date: YYYY-MM-DD
  initiative: [name]
  items_deferred:
    - description: [what was cut]
      rationale: [why this was chosen over other options]
      user_impact: low | medium | high
      debt_created: [technical debt this creates, if any]
      re-inclusion_plan: [when / what condition triggers re-adding this]
  items_rejected_from_cutting:
    - description: [what was proposed but not cut]
      rationale: [why this was kept]
  accepted_by: [names of approvers]
  original_scope_doc: [link]
```

**Step 5 — Communicate immediately.** Anyone who expected the cut item must be informed before the change is finalized, not after.

---

## The "Add Scope" Protocol

Scope additions after an initiative is underway are more dangerous than scope cuts — they typically slip the timeline without explicit acknowledgment.

**When someone requests scope addition:**

1. Ask: what does this replace? Every addition requires a named removal or an explicit timeline extension.
2. Categorize the addition: is it Core (must have it), or is it a "nice to have" being presented as essential?
3. Run it through prioritization: does this pass the strategic alignment gate that other items had to pass?

**The "yes, and" response:** "Yes, we can add this. To keep the timeline, we'd need to defer [X]. If [X] is more important, the timeline extends by [N] weeks. Which do you prefer?"

This framing makes the trade-off visible and keeps the decision with the requester, where it belongs.

---

## Quality Trade-Offs

When scope can't be cut but time is constrained, quality is the implicit variable. This must be made explicit.

**Quality levels (from highest to lowest):**
- **Production-grade:** Handles all user states, edge cases, error conditions, load at peak traffic, accessibility standards
- **Beta-grade:** Core path works perfectly; edge cases handled but not polished; load tested at expected traffic
- **Alpha-grade:** Core path works for ideal user; known edge cases may fail; limited load testing
- **Internal-only:** Insufficient for external users; internal use or limited pilot only

**The quality trade-off declaration:**
```
For [launch], we are shipping at [quality level].
Known gaps: [list specific gaps]
Risk accepted by: [name]
Mitigation: [how we handle failures / support users who hit gaps]
Timeline to production-grade: [date]
```

This prevents the implicit assumption that "we'll fix it after launch" from being forgotten.

---

## Anti-Patterns

**The silent scope cut:** Cutting scope informally in a Slack conversation without updating the spec, informing stakeholders, or documenting the decision. Produces a launch where half the team is surprised by what shipped.

**The scope cut without re-inclusion plan:** Deferring features with "we'll add it later" without a triggering condition. "Later" that has no condition is "never."

**Scope cuts as punishment:** Cutting scope to accommodate a team that is under-delivering without acknowledging the trade-off. The cut still costs the user something — it should be acknowledged as a trade-off, not normalized as acceptable.

**The optimism cut:** Cutting scope that everyone knows will have to come back immediately post-launch. If something will be re-added within 2 weeks, it should have stayed in scope. Ship the real MVP, not a fake one that immediately balloons.

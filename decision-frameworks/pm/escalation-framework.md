# Escalation Framework
## When to Escalate, How to Frame It, and What Governance Looks Like

Escalation is not a failure. Escalation of a genuine disagreement or out-of-bounds decision is correct PM behavior. The failure is: escalating things you should resolve yourself, not escalating things that require higher authority, or escalating without a clear ask.

---

## When to Escalate

Escalate when any of these conditions are met:

**1. The decision exceeds your authority.**
Named resources that require approval above your level. Commitments that affect customers in ways requiring executive visibility. Pricing changes. Partner agreements. Headcount decisions.

**2. You have reached genuine impasse.**
Two or more parties have irreconcilable positions that affect a shared outcome. You have tried: 1:1 conversations to understand the underlying concern, reframing the problem, proposing multiple options. None have resolved it.

**3. The risk profile has changed materially.**
An initiative was approved at one risk level; circumstances have changed such that the current risk is significantly higher. This is not a quarterly review item — it's an immediate escalation.

**4. You need information only accessible at a higher level.**
Some decisions require context that exists only at the executive level — strategic trade-offs between business units, budget reallocation, executive relationship commitments. Don't simulate having this information.

**5. Someone is blocking without authority.**
A stakeholder is blocking a decision that is not within their decision rights. Don't fight it directly — escalate the governance question.

---

## How to Frame an Escalation

Executives don't want to hear about your problem. They want to make a decision. Frame accordingly.

**Escalation brief structure:**

```
SITUATION:
[One paragraph. Current state. What's at stake. Why this requires a decision now.]

WHAT I'VE TRIED:
[Bullet list. Actions taken to resolve without escalation. Why they didn't work.]

OPTIONS:
[2-3 options. Each with: what we do, what we gain, what we give up. Be honest about trade-offs.]

MY RECOMMENDATION:
[One option. Clear recommendation. The reasoning in 2 sentences.]

WHAT I NEED FROM YOU:
[The specific decision or unblocking action required. Named. Timed.]
```

**What not to include:**
- Detailed history of how we got here (brief context only)
- Justification for why you're right (you're presenting options, not lobbying)
- Vague asks like "what do you think we should do?"

**The explicit ask is mandatory.** An escalation without a clear ask produces discussion, not decisions.

---

## Escalation Timing

**Escalate early.** The most common escalation failure is waiting too long. By the time a PM escalates a 6-week-old impasse, the deadline pressure is so high that the conversation is reactive and the executive is deciding under time constraints they didn't cause.

**Escalation signal:** When you've had the same conversation with the same parties more than twice without resolution, escalate. This is the signal that the disagreement is structural, not informational.

**Pre-escalation check:** Before escalating, run this:
- Have I clearly stated the specific decision needed (not just the problem)?
- Have I presented real options with real trade-offs (not just my preferred option)?
- Have I given the blocking party a chance to respond to my framing?
- Is this actually beyond my authority, or am I escalating to avoid a difficult conversation?

If the answer to the last question is "yes," don't escalate — have the conversation.

---

## Decision Rights Mapping

For each category of decision, document:

| Decision Type | Driver | Approver | Consulted | Informed |
|---|---|---|---|---|
| Quarterly roadmap | PM | Product Leadership | Engineering, Design, Sales | All stakeholders |
| Scope expansion (>2 weeks engineering) | PM | Engineering + PM Lead | Design, QA, Data | Stakeholders |
| Feature kill | PM | PM Lead | Engineering, Design | All stakeholders |
| Pricing change | PM + Finance | CPO + CEO | Sales, Legal, Customer Success | All |
| Architecture decision (significant) | Engineering Lead | CTO | PM | PM, Stakeholders |
| Partnership commitment | Partnerships | C-Suite | PM, Legal | All |
| Launch go/no-go | PM | PM Lead + Engineering | Design, QA, CS | All |

Customize this for your organization. The point is that ambiguity in decision rights creates conflict — make rights explicit before the conflict.

---

## Governance Patterns

**The DACI model in practice:**
- Driver: Does the work and proposes the decision. Has skin in the game.
- Approver: Can veto. Only one person. If there are two approvers, the governance is broken.
- Consulted: Their input is required before the decision. Not the same as informing.
- Informed: Needs to know after. Does not need to be in the decision.

**When DACI is violated:**
- Multiple approvers: Every decision gets blocked by committee. Fix: clarify who the single approver is.
- Consulted treated as Informed: Key stakeholders feel blindsided. Fix: run the consultation before the decision.
- Driver has no authority to propose: Driver's proposals are overridden by stakeholders who weren't in the process. Fix: clarify that the Driver owns the proposal even if the Approver overrides it.

**The governance review:** Quarterly, ask: are the decision rights still right given the organization's current structure and strategy? Organizations evolve faster than governance docs. Update them.

---

## Escalation Anti-Patterns

**The upward delegation trap:** Escalating decisions that are within your authority because they're difficult. Executives learn to distrust PMs who do this.

**The sandbag escalation:** Presenting only your preferred option as an "escalation" to get the executive to validate your choice. Executives see through this and lose trust.

**The information dump escalation:** Sending a 2-page status document and calling it an escalation. No clear ask, no options, no recommendation. Produces a follow-up meeting instead of a decision.

**The surprise escalation:** First time the executive hears about a problem is when it's in crisis. Fix: give visibility to risks while they're manageable, before they require crisis-mode decisions.

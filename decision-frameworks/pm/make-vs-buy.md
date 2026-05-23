# Make vs. Buy vs. Partner Framework
## Structured Decision-Making for Build, Buy, and Integration Choices

Every product team eventually faces this decision: do we build this capability ourselves, buy/license it from a vendor, or partner with a company that has it? The wrong choice produces years of maintenance burden, competitive disadvantage, or strategic dependency. The right choice compounds position.

---

## The Decision in One Sentence

Build when the capability is core to your differentiation and your users will notice the quality difference. Buy when speed and cost dominate and the capability is not differentiated. Partner when the ecosystem relationship creates value beyond the capability itself.

---

## The Three-Option Framework

### Option 1 — Build

**When build wins:**
- The capability is directly tied to your primary value proposition
- Users would notice and care about the quality difference between your implementation and a vendor's
- Building creates proprietary data, models, or feedback loops that compound over time
- The capability requires deep integration with your core data or system architecture
- Competitive defensibility depends on owning this capability
- The vendor market has no good option, or vendors have unacceptable data privacy or compliance implications

**Total cost of build:**
- Initial engineering investment (design + build + test + deploy)
- Ongoing maintenance (bug fixes, security patches, scaling, compatibility)
- Opportunity cost (what else could this team build?)
- Hiring and knowledge concentration risk

**Build anti-pattern:** "We can build this ourselves" as a default position driven by engineering pride rather than strategic necessity. Building everything yourself is the fastest way to fall behind on the things that matter.

---

### Option 2 — Buy (Vendor / SaaS / License)

**When buy wins:**
- The capability is a commodity — users don't care who provides it, they care that it works
- Speed to market is the primary constraint
- The vendor specializes in this capability and will always be better at it than your team
- Total cost of ownership (buy + integration + vendor management) is lower than build over 3 years
- Regulatory/compliance requirements are met by the vendor's existing certifications
- The capability is not strategically sensitive (you're not giving away your core)

**Total cost of buy:**
- License/subscription fees (per seat, usage, or flat)
- Integration engineering (often underestimated — can equal 30-50% of license cost)
- Vendor management overhead (contract negotiation, SLA monitoring, relationship management)
- Lock-in risk (what's the cost of switching in 3 years? Does the vendor have pricing leverage?)
- Vendor stability risk (what if they raise prices, get acquired, or shut down?)

**Buy anti-pattern:** Underestimating integration costs and vendor lock-in. A vendor solution that costs $50K/year might cost $200K to integrate and $500K to migrate away from in 3 years.

---

### Option 3 — Partner

**When partner wins:**
- The partner relationship creates ecosystem value beyond the capability (joint customers, distribution, co-marketing)
- The partner's user base represents a significant acquisition channel
- The capability requires deep domain expertise in a vertical you don't serve (healthcare, legal, financial services)
- The partnership is reciprocal — you provide value to the partner, not just receive it
- The integration creates switching costs that benefit both parties

**Partner risk factors:**
- Partner roadmap alignment: will the partner continue to invest in this capability?
- Partner stability: is the partner financially healthy?
- Competitive exposure: could the partner become a competitor?
- Terms leverage: as the partnership matures, does the partner gain pricing leverage?
- SLA misalignment: partner's SLA must be compatible with your commitments to users

**Partner anti-pattern:** Treating partnerships as a shortcut to capabilities without investing in the relationship. Partnerships that only flow one way (you receive, they give) are transactional and fragile.

---

## The Decision Matrix

Score each option across dimensions. Weights are adjustable based on context.

| Dimension | Weight | Build | Buy | Partner |
|---|---|---|---|---|
| Differentiation: does this capability create competitive advantage? | 30% | Score 1-5 | Score 1-5 | Score 1-5 |
| Speed: how quickly can this be available to users? | 20% | Score 1-5 | Score 1-5 | Score 1-5 |
| Total cost of ownership (3-year) | 20% | Score 1-5 | Score 1-5 | Score 1-5 |
| Reversibility: how hard to switch later? | 15% | Score 1-5 | Score 1-5 | Score 1-5 |
| Vendor/partner risk | 15% | N/A | Score 1-5 | Score 1-5 |

**Score interpretation:** Higher score = more favorable. Differentiation and reversibility typically favor build; speed and cost typically favor buy or partner.

---

## Integration Depth Consideration

Even a "buy" decision involves building — the integration. Assess integration depth:

| Level | Description | Engineering cost | Lock-in risk |
|---|---|---|---|
| Shallow | Display vendor UI in iframe; minimal data exchange | Low | Low |
| Standard | Use vendor API; sync key data | Medium | Medium |
| Deep | Vendor data is core to your product data model | High | High |
| Core | Vendor capability is a fundamental system dependency | Very high | Very high |

**Rule:** Integration depth should match strategic importance. Deep integration with a capability that isn't strategically critical creates disproportionate lock-in risk.

---

## The Vendor Evaluation Checklist

When evaluating a vendor for the "buy" option:

**Capability:**
- [ ] Meets all P0 requirements without significant customization
- [ ] API/SDK quality is acceptable for integration depth required
- [ ] Performance and reliability SLA matches your user commitments

**Commercial:**
- [ ] Pricing model scales sustainably with your growth (not exponentially)
- [ ] Contract terms are acceptable (data ownership, liability, termination)
- [ ] Multi-year pricing is negotiated before commitment

**Risk:**
- [ ] Vendor has been in business >3 years or has strong investor backing
- [ ] Data privacy and compliance certifications match your requirements (SOC2, GDPR, HIPAA)
- [ ] Migration path exists (data export, API compatibility) if you need to leave
- [ ] Reference customers in your segment have been interviewed

**Strategic:**
- [ ] Vendor roadmap direction aligns with your product direction
- [ ] Vendor does not have a direct product that competes with yours
- [ ] Exclusivity or preferred partner terms are available if strategically important

---

## Documentation Requirements

Log this decision in `decision-frameworks/decisions-log.md` with:
- The capability being sourced
- Options evaluated and scores
- Decision made
- Key assumptions (especially on total cost of ownership and lock-in)
- Review date (when to reassess — typically annual)

**The reassessment trigger:** Even after a buy or partner decision, reassess when: vendor pricing increases significantly, a competitive capability emerges at lower cost, the capability becomes more strategically important than when originally assessed.

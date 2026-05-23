# Sunset Framework
## When and How to Deprecate Features, Products, and Integrations

Deprecation is the hardest PM decision because it is permanent, creates user pain in the near term, and has benefits that materialize slowly. The PM who avoids deprecation decisions accumulates a product that is increasingly expensive to maintain, difficult to explain, and impossible to focus. Sunsets are not failures — they are portfolio hygiene.

---

## When to Deprecate

A feature or product is a deprecation candidate when three or more of these conditions are true:

**1. Usage signal:**
- Active users represent <5% of the customer base AND usage is declining
- No significant user has onboarded to this feature in the past 6 months
- The feature generates more support tickets per user than any other feature (disproportionate maintenance cost)

**2. Strategic signal:**
- The feature no longer serves a strategy assumption that is still valid
- A better approach to the same problem has been built or is in development
- The feature was built for a segment the company is no longer targeting

**3. Technical signal:**
- Maintaining the feature requires disproportionate engineering investment (tech debt, compatibility burden)
- The feature blocks a desired architectural change
- The feature relies on a deprecated external dependency with no viable migration path

**4. Commercial signal:**
- The feature is not part of any paid tier and has no clear path to monetization
- The feature is explicitly excluded from new customer contracts
- Support costs for this feature exceed revenue contribution

---

## The Deprecation Impact Assessment

Before announcing deprecation, assess:

**Who uses it?**
- How many active users (MAU)? (Track at segment level — an enterprise account with 3 users matters more than 300 consumer users)
- Are any strategic accounts dependent on this feature?
- Is it referenced in any customer contracts or public documentation?
- Are there external developers or partners building on this (API/integration deprecation)?

**What do they use it for?**
- What job-to-be-done does this feature serve?
- Does a replacement exist (in our product or elsewhere)?
- What is the migration path?

**What is the deprecation cost?**
- User pain: how disruptive is this to the users who rely on it?
- Relationship cost: are any relationships at risk?
- Revenue risk: is any ARR at risk from this deprecation?
- Legal/contractual exposure: is this feature in any SLA or customer agreement?

---

## Deprecation Process

**Phase 1 — Internal decision (6-12 months before EOL for enterprise features; 3-6 months for consumer)**

1. Deprecation candidate proposed with evidence
2. Impact assessment completed
3. Migration path defined (what should users do instead?)
4. Go/no-go decision by PM + leadership

**Phase 2 — Advance notice to affected users**

- Enterprise/contractual: minimum 12 months notice
- Standard product feature: minimum 6 months notice
- Internal tooling: minimum 90 days notice
- API/integration deprecation: minimum 12 months with version pinning available during transition

**Communication requirements:**
- Announce the EOL date (specific date, not "later this year")
- Explain the reason (honest — "we're focused on X instead of maintaining Y")
- Provide the migration path with documentation
- Offer migration assistance for strategic accounts

**Phase 3 — Sunset milestones**

- M-6: formal announcement + documentation published
- M-3: second reminder + banner in product + support team briefed
- M-1: final notice + last-chance migration assistance offers
- M-0: feature disabled or redirected to migration guide
- M+1: feature code removed from codebase (reduces maintenance burden; makes deprecation truly complete)

---

## Migration Path Standards

Every deprecation must have a migration path. "The feature is going away" without an answer to "so what do I do now?" is abandonment, not deprecation.

**Migration path components:**
1. **Documentation:** Step-by-step guide for migrating from old feature to replacement
2. **Data export:** Users must be able to export their data before EOL
3. **Alternative:** Either a native replacement or acknowledged third-party alternatives
4. **Migration support:** For enterprise accounts, offer guided migration assistance

**The acceptable migration:** A migration is acceptable when a user can complete it in less than [2× the time they spend per week using the deprecated feature]. A migration that takes 40 hours for a feature used 1 hour per week is not acceptable — it requires a longer runway or more migration assistance.

---

## API and Integration Deprecation

API deprecation has higher standards because external developers may have built production systems that depend on the API.

**API deprecation rules:**
- Minimum 12-month notice from announcement to removal
- Provide API versioning so developers can pin to the old version during migration
- Document the new API version alongside the deprecation announcement
- Automated migration tools where feasible (scripts, API translators)
- Developer communication: in-API response headers, email to registered developers, changelog

**The breaking change vs. deprecation distinction:**
- Breaking change: changes the API contract without prior notice. Never acceptable.
- Deprecation: planned removal with notice. Acceptable with adequate runway.
- Deprecation without migration path: functionally equivalent to a breaking change. Never acceptable.

---

## Communicating Deprecation Decisions

**Internal:** Brief the team before external announcement. Engineering, CS, Sales, Support must understand: what's going away, when, why, and what the migration path is. CS and Support need this first — they'll get the calls.

**External (user-facing):** Honest, direct, and helpful. The three elements of a good deprecation announcement:
1. What is going away and when (specific date)
2. Why (brief, honest — don't hide behind "improving our product")
3. What to do instead (specific, with documentation link)

**Tone standard:** Don't apologize excessively — it signals uncertainty about the decision. Don't be defensive — users are allowed to be unhappy. Be clear, grateful for their usage, and maximally helpful about the migration.

---

## Anti-Patterns

**The soft sunset:** Stopping investment in a feature without announcing deprecation. Users continue to use a degrading, unmaintained feature and lose trust when it eventually breaks.

**The indefinite "deprecated but still running":** Features marked deprecated years ago that are still running and still being maintained. Create the forcing function — set the EOL date and honor it.

**The migration path that doesn't work:** Announcing "use Feature Y instead" when Feature Y doesn't actually do what Feature X did. Users discover the gap, escalate, and the deprecation gets reversed — creating more uncertainty.

**Surprising strategic accounts:** No enterprise customer should learn about a deprecation through a product banner. Strategic accounts get personal notice with adequate lead time before public announcement.

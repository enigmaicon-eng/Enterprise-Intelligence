---
name: pm-privacy
description: Run a PM-level privacy and compliance review — GDPR/CCPA requirements, consent flow design, data minimization, privacy by design principles, and the privacy impact checklist. PM accountability before engineering builds.
version: "1.0"
changed: 2026-05-20
---

# PM Privacy and Compliance Review

**Input:** Feature or product description, user data involved, jurisdictions where product operates, any known compliance requirements.

**Output:** Written to `notes/structured/privacy-review-YYYY-MM-DD-<feature-slug>.md`

**Scope:** PM-level privacy review — data mapping, consent design, GDPR/CCPA requirements, privacy by design principles. Does not replace legal review; flags what requires legal input. For AI/ML-specific privacy concerns, see `/pm-ml`.

---

## Steps

1. **Map the data.** What personal data does this feature collect, process, store, or share? Be exhaustive — include inferred data and behavioral data, not just explicitly provided data. For each data type: who provides it, why it is collected, how long it is retained, and who can access it.

2. **Identify the legal basis.** For GDPR-applicable users, every data processing activity requires a legal basis. Map each processing activity to its basis: consent, contract, legitimate interest, legal obligation, vital interests, or public task. "Legitimate interest" requires a documented balancing test — do not assume it.

3. **Design consent flows.** Where consent is the legal basis, design the consent mechanism: what information is disclosed before consent, how consent is recorded, how users withdraw consent, and what happens to already-collected data if consent is withdrawn. Dark patterns (pre-ticked boxes, buried opt-outs, consent walls) are not compliant — do not design them.

4. **Apply data minimization.** For each data element collected: is it strictly necessary for the stated purpose? If the feature can work without it, do not collect it. The default is to collect less, not more.

5. **Map user rights.** GDPR grants users: right to access, right to erasure, right to portability, right to rectification, right to restrict processing, right to object. For each right: does the feature's implementation support it technically? If not, what engineering work is required before the feature ships?

6. **Run the privacy by design checklist.** Proactive, not reactive. Privacy as default (most privacy-protective settings are default). Full functionality (privacy does not reduce utility — if it does, find another design). End-to-end security. Visibility and transparency. User-centric.

7. **Flag legal review requirements.** Name what requires a lawyer, not just a PM. Do not substitute this review for legal counsel on anything that is flagged.

---

## Output Format

```markdown
# Privacy and Compliance Review — [Feature Name] — [Date]

**Jurisdictions:** [GDPR / CCPA / LGPD / PIPEDA / other]
**Legal review required:** [Yes / No — if yes, items flagged below]
**PM sign-off:** [Name, Date]

---

## Data Map

| Data element | Source | Purpose | Legal basis | Retention | Access | Shared with |
|-------------|--------|---------|-------------|-----------|--------|-------------|
| [e.g., email address] | User input | Authentication | Contract | Duration of account | Auth service | None |
| [e.g., usage events] | System | Product improvement | Legitimate interest | [N months] | Internal analytics | [if any] |
| [e.g., location data] | Device | [Purpose] | Consent | [Period] | [Who] | [If any] |

**Data minimization audit:**
- [Data element] — collected but [arguably unnecessary because...] → Recommendation: remove

**Special category data (GDPR Art. 9):**
[Health, racial/ethnic origin, political opinions, religious beliefs, biometric, genetic, criminal conviction — if any of these are processed, flag immediately for legal review]

---

## Legal Basis Analysis (GDPR)

| Processing activity | Legal basis | Basis documentation |
|--------------------|-------------|-------------------|
| [Activity] | Consent | Consent record stored in [location] |
| [Activity] | Contract | Necessary for service delivery — documented in Terms |
| [Activity] | Legitimate interest | Requires balancing test — see below |
| [Activity] | Legal obligation | [Specific regulation requiring this] |

**Legitimate interest balancing test (complete for each LI basis):**
- Purpose: [What PM is trying to achieve]
- Necessity: [Why this is the least intrusive way to achieve it]
- Balance: [Does the legitimate interest override the individual's interests, rights, and freedoms?]
- Outcome: [LI confirmed / LI not suitable — switch to another basis]

---

## Consent Flow Design

*(Complete only where consent is the legal basis)*

**Pre-consent disclosure:**
- What is disclosed to the user before they consent:
  - Purpose: [Exactly what data will be used for]
  - Who processes it: [Controller and any processors]
  - Retention period: [How long]
  - Rights: [How to withdraw, access, delete]
  - Link to full privacy policy: [Yes/No]

**Consent mechanism:**
- Form: [Explicit opt-in (checkbox, button) — NOT pre-ticked, NOT bundled with terms]
- Granularity: [Separate consent for separate purposes — not one consent for all]
- Withdrawal method: [Where and how users can withdraw consent]
- Record: [How consent is stored — timestamp, version, mechanism]

**Post-withdrawal behavior:**
- Data collected before withdrawal: [Deleted / Anonymized / Retained for [legal basis] only]
- Feature behavior after withdrawal: [What the user can still access]

**Dark pattern audit:**
- [ ] No pre-ticked boxes
- [ ] No consent wall (service is available without consenting to non-essential processing)
- [ ] Opt-out as easy to access as opt-in
- [ ] No deceptive language ("free" consent with hidden processing)

---

## User Rights Implementation

| Right | Supported? | Technical implementation | Time to fulfill | Owner |
|-------|-----------|------------------------|-----------------|-------|
| Access (data export) | [Yes/No/Partial] | [How users request and receive their data] | [Days] | |
| Erasure ("right to be forgotten") | [Yes/No/Partial] | [What is deleted, what is retained for legal obligation] | [Days] | |
| Portability (machine-readable export) | [Yes/No/Partial] | [Format — JSON, CSV] | [Days] | |
| Rectification (correct inaccurate data) | [Yes/No/Partial] | [How users update their data] | [Days] | |
| Restriction (pause processing) | [Yes/No/Partial] | [What stops, what continues] | [Days] | |
| Object (opt out of legitimate interest processing) | [Yes/No/Partial] | [How, and what changes] | [Days] | |

**Engineering requirements for user rights compliance:**
- [What must be built or modified before this feature ships]

---

## CCPA Requirements (if applicable)

- [ ] "Do Not Sell My Personal Information" link present (if data is sold/shared for commercial purposes)
- [ ] Opt-out of sale honored within 15 days
- [ ] Non-discrimination: no degraded service for exercising CCPA rights
- [ ] Privacy policy updated to include CCPA-required disclosures
- [ ] Verified consumer request process defined

---

## Privacy by Design Checklist

- [ ] **Proactive:** Privacy risks identified before build, not after
- [ ] **Default:** Most privacy-protective settings are the default (opt-in for non-essential processing)
- [ ] **Embedded:** Privacy built into the design, not bolted on
- [ ] **Full functionality:** Privacy protections do not reduce user utility — if they do, design a different approach
- [ ] **End-to-end security:** Data is protected throughout its lifecycle (transit, at rest, at deletion)
- [ ] **Transparent:** Users can see and understand what data is collected and why
- [ ] **User-centric:** Users can exercise rights easily without contacting support

---

## Items Requiring Legal Review

⚠️ The following items exceed PM scope and require legal counsel before the feature ships:

1. [Specific item — e.g., "Special category data processing of health information"]
2. [Specific item — e.g., "Cross-border data transfer to [country] without an adequacy decision"]
3. [Specific item — e.g., "Legitimate interest basis for [processing activity] — balancing test needs legal validation"]

**Legal review deadline:** [Date — must be before code freeze]

---

## Privacy Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|------------|-------|
| [Risk] | H/M/L | H/M/L | [Mitigation] | |
```

---

## Quality Gate

- Every data element mapped with purpose and legal basis
- Legitimate interest basis has a documented balancing test (not assumed)
- Consent flows use explicit opt-in with no dark patterns
- All six GDPR user rights assessed for technical implementation
- Engineering requirements for rights compliance listed before code freeze
- Privacy by design checklist complete
- Legal review items explicitly flagged (not buried)
- This review is documented before engineering begins, not after

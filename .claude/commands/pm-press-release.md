---
name: pm-press-release
description: Write a Working Backwards press release before scoping a feature or product. Forces customer-outcome clarity before any engineering begins. Amazon methodology — customer narrative written first, spec derived from it.
version: "1.0"
changed: 2026-05-20
---

# PM Press Release (Working Backwards)

**Input:** Feature or product idea, target customer, problem being solved, approximate timeframe.

**Output:** Written to `notes/structured/press-release-YYYY-MM-DD-<feature-slug>.md`

**Scope:** Working Backwards press release + FAQ. Not a launch announcement — this is a pre-build artifact that defines what success looks like in customer terms before a line of code is written. For actual launch communication, use `/pm-gtm`.

---

## Steps

1. **Resist writing requirements first.** The press release comes before the PRD. If you can't write a compelling press release, the feature isn't ready to be built — the problem isn't clear enough.

2. **Write the headline.** One sentence. Written as if the product has shipped and a journalist is covering it. The customer is the subject, not the product. "Customers can now [do X]" not "[Product name] releases [feature name]."

3. **Write the opening paragraph.** Who is the customer? What problem did they have? What can they now do that they couldn't before? Written for a general reader — no technical jargon.

4. **Write the customer problem section.** What was the pain before? Use specific, real-feeling language. If you're vague here, the feature is not well-understood.

5. **Write the solution description.** How does the product solve it? Written as the customer experience — what they see and do — not as a feature list.

6. **Write the customer quote.** A real-sounding quote from a target customer. It should describe the impact on their work, not praise the product's features. If this quote feels generic or could apply to any feature, rewrite it.

7. **Write the product/company quote.** From the PM's perspective: what problem this solves and why it matters.

8. **Write the getting started section.** How does a customer find and use this? Written as if explaining to a customer today.

9. **Write the FAQ.** The most important part. Write the hard questions that stakeholders, customers, and engineering will ask — and answer them honestly. Unanswered FAQs reveal unresolved ambiguity. Write at minimum: the 3 hardest questions you don't fully know the answer to.

---

## Output Format

```markdown
# Working Backwards Press Release — [Feature/Product Name] — [Date]

**Classification:** Pre-build artifact — not for external distribution  
**Status:** Draft / For review / Approved for scoping

---

## Press Release

**FOR IMMEDIATE RELEASE**

### [Headline — customer as subject, outcome as verb]

**[City, Date]** — [Opening paragraph: who is the customer, what was their problem, what can they now do]

**[Customer problem section — 1-2 paragraphs]**

[Describe the before state. What did they have to do? What was frustrating, slow, expensive, or error-prone? Be specific. Cite real customer language from discovery if available.]

**[Solution section — 1-2 paragraphs]**

[Describe the customer experience with the solution. What do they see? What do they do? What changes in their day? Not a feature list — a day-in-the-life description.]

**[Customer quote]**

"[A quote that sounds like a real customer. Describes the outcome to their work, not the product's capabilities. If it could appear in a testimonial for any product, rewrite it.]" — [Fictional but realistic customer name, role, company type]

**[PM/Company quote]**

"[Quote from PM or product leader. Explains the why — what problem this solves and why it's the right problem to solve now.]" — [Name, Title]

**[Getting started section]**

[Two to three sentences on how a customer would find and use this today. Written as if the product has shipped.]

---

## Frequently Asked Questions

**Q: [The question customers will ask most often]**  
A: [Answer]

**Q: [The question that reveals a scope decision]**  
A: [Answer — and the explicit trade-off made]

**Q: [The question about what this doesn't do]**  
A: [Honest answer about what's excluded and why]

**Q: [The question engineering will ask]**  
A: [Answer — or explicit acknowledgment that this is unresolved]

**Q: [The question a skeptical executive will ask]**  
A: [Answer — quantified if possible]

**Q: [The hardest question — the one PM doesn't fully know the answer to]**  
A: [Honest answer, naming the uncertainty and how it will be resolved]

---

## Press Release Quality Check

- [ ] Headline: customer is the subject, outcome is the action (not "we release X")
- [ ] Customer quote: describes life change, not product features
- [ ] Problem section: specific enough that someone who doesn't know the product would understand the pain
- [ ] Getting started: written as if the product has shipped today
- [ ] FAQ includes at least 3 hard questions PM doesn't fully know the answer to
- [ ] If this press release can't be written convincingly, the feature is not ready to be scoped

---

## Derived Scoping Implications

[After writing the press release, extract the product implications]

**What the press release commits to:**
- [Capability 1 implied by the press release]
- [Capability 2]

**What the press release rules out:**
- [What is explicitly not promised]

**Unresolved questions surfaced by the FAQ:**
1. [Question that requires a decision before scoping can begin]
2. [Question]

**Recommended next step:** [PRD / discovery sprint / stakeholder alignment / prototype]
```

---

## Quality Gate

- Written in customer language (no technical jargon, no feature names)
- Headline: customer is grammatical subject; outcome is the verb
- Customer quote describes impact to work, not product features
- FAQ includes questions PM doesn't fully know the answer to (honest, not marketing)
- Getting started section is written as present-tense ("customers can now...")
- Scoping implications section extracted — press release directly informs the PRD
- If the press release cannot be written convincingly, document why and recommend what must be resolved first

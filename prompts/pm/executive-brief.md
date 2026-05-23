# Executive Brief Prompt
## Situation-Complication-Resolution for Executive Communication

**Use when:** Drafting an executive update, escalation brief, go/no-go recommendation, or any communication where the audience needs to make a decision or take action.

**Underlying structure:** Situation → Complication → Resolution (from `knowledge/pm/org-dynamics.md`). Executives process information most efficiently when it follows this pattern.

---

## The Prompt

```
Draft an executive brief using the following inputs.

CONTEXT:
- Audience: [Who is this for — CPO, CEO, board, specific exec?]
- Purpose: [Update / Escalation / Decision request / Go/no-go recommendation / Risk flag]
- Medium: [Async doc / Meeting opening / Email / Slack message]
- Time constraint: [How long will they have? Async: reading time. Meeting: speaking time.]

INPUT — SITUATION:
[Current state: what's happening, what's at stake, why now. Facts only, no interpretation yet.]

INPUT — COMPLICATION:
[What makes this situation difficult: the tension, the trade-off, the constraint, or the risk that requires executive attention.]

INPUT — RESOLUTION:
[Options and recommendation. For updates: what's being done. For escalations: specific ask.]

DRAFT INSTRUCTIONS:
1. Lead with the single most important thing they need to know.
2. State the complication without hedging. Don't soften the tension.
3. For escalations: include explicit ask ("I need you to decide X by [date]").
4. For updates: include what's tracking, what's at risk, what you're watching.
5. For decisions: name 2-3 options with honest trade-offs. State your recommendation clearly.
6. No jargon, no acronyms without expansion. Write for someone who has context but not details.
7. Maximum length: 200 words for async. 100 words for verbal.

OPTIONAL CONSTRAINTS:
- Tone: [Neutral / Urgent / Collaborative]
- What not to include: [Context they already have / Details that are not decision-relevant]
- Specific sensitivities: [Stakeholder dynamics, open tensions, political context]
```

---

## Output Format

**Async (doc/email):**
```
SUBJECT: [One line — topic + action needed]

[Situation: 2-3 sentences. Current state. What's at stake.]

[Complication: 2-3 sentences. The tension or risk. Why this needs their attention now.]

[Resolution: Options (if decision) OR status + next step (if update) OR explicit ask (if escalation).]

[Explicit ask, if applicable: "I need [specific decision / action] by [date]."]
```

**Verbal (meeting opening):**
```
"Here's where we are: [situation in one sentence].
The challenge is [complication in one sentence].
I'm here because [what you need from them in one sentence]."
```

---

## Quality Gates

Before sending, verify:
- [ ] The first sentence contains the most important information (not background)
- [ ] The complication is stated without softening ("we're facing a challenge" is softening — name the challenge)
- [ ] There is a specific ask or decision, not a vague "wanted to flag this"
- [ ] Trade-offs are honest — you haven't presented your preferred option as the only option
- [ ] It can be read in the stated time constraint

---

## Common Failures

**Opening with context instead of situation:** Starting with "Three months ago, we kicked off X initiative..." The reader should be oriented in the first sentence, not the third paragraph.

**Buried ask:** The decision needed is at the end, after three paragraphs of context. Put the ask in the subject line (async) or the first 30 seconds (verbal).

**Softened complication:** "We're watching a few things closely" instead of "the Q3 milestone is at risk unless the partner dependency lands by May 30." Name the risk precisely.

**False balance:** Presenting two options where one is obviously wrong to manufacture the appearance of presenting options. Executives see through this. Present real trade-offs.

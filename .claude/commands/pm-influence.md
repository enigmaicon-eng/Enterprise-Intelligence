---
name: pm-influence
description: Map stakeholder influence dynamics and design a structured influence campaign — without authority. Coalition building, pre-alignment sequencing, skeptic management, and escalation as last resort.
version: "1.0"
changed: 2026-05-20
---

# PM Influence Without Authority

**Input:** Decision to be made or outcome to achieve, stakeholders involved, current state of alignment, known objections.

**Output:** Written to `notes/structured/influence-YYYY-MM-DD-<decision-slug>.md`

**Scope:** Influence strategy for a specific decision or direction — stakeholder sequencing, coalition building, objection pre-emption. For broader stakeholder mapping, use `/pm-stakeholders`. For formal escalation, use `/pm-exec-brief`.

---

## Steps

1. **Define the outcome precisely.** What exactly needs to happen — a decision, a resource allocation, a change in direction? Vague influence goals produce vague influence strategies. State the outcome as a decision or action verb: "Engineering lead agrees to allocate one sprint to X before Q2 planning" not "get engineering on board."

2. **Map the influence landscape.** Who has formal authority over this decision? Who has informal authority (whose opinion others follow)? Who is affected and will have opinions even without formal standing? Map relationships: who trusts whom, who is skeptical of whom.

3. **Identify the minimum coalition.** What is the smallest set of people whose alignment makes this outcome possible? Over-expanding the coalition creates unnecessary coordination costs. The minimum coalition is the set of people without whose support the outcome cannot happen.

4. **Design the pre-alignment sequence.** Coalition building is sequential, not simultaneous. Start with allies (to refine the argument and collect early momentum), then move to neutrals (to build weight), then to skeptics (when the idea already has support behind it). Going to skeptics first without coalition is the most common influence mistake.

5. **Prepare for each objection.** What are the genuine objections? Not the stated objections — the underlying concern behind the stated objection. Prepare the response for each. Acknowledge the legitimate concern before offering a reframe or counter.

6. **Design the decision moment.** Who needs to be in the room (or the document)? What is the decision format — asynchronous doc, meeting, approval email? What is the ask — binary yes/no, choose from options, provide input? Make the decision easy to say yes to.

7. **Name the escalation option — and the cost.** Escalation is sometimes the right move. Name the escalation path now, the threshold at which it becomes appropriate, and the relationship cost of using it. Use it as a last resort, not a first.

---

## Output Format

```markdown
# Influence Strategy — [Decision/Outcome] — [Date]

**Outcome target:** [Exact decision or action needed — stated as a verb]
**Timeline:** [When the decision must be made]
**PM:** [Name]

---

## Influence Landscape

### Formal Decision Authority

| Person | Role | Formal authority | Current stance | What they care most about |
|--------|------|-----------------|----------------|--------------------------|
| [Name] | [Role] | [Final approval / Budget / Team direction] | [Aligned / Neutral / Skeptic / Unknown] | [Their primary concern] |

### Informal Authority (opinion leaders others follow)

| Person | Why they have influence | Current stance | Coalition value |
|--------|------------------------|----------------|-----------------|
| [Name] | [Why others listen to them] | [Stance] | [High / Medium — include in early coalition] |

### Affected Parties (voice without formal standing)

| Person/Team | Why they'll weigh in | Expected position | How to handle |
|-------------|---------------------|------------------|---------------|
| [Name] | [Stake] | [Support / Object / Neutral] | [Engage early / acknowledge concerns / ignore] |

---

## Minimum Coalition

**Who must be aligned for this to happen:**
1. [Name] — [Why their alignment is necessary]
2. [Name] — [Why their alignment is necessary]

**Who is nice to have but not necessary:**
- [Name] — [Their value to the coalition]

**Who should be informed but not consulted:**
- [Name/Team]

---

## Pre-Alignment Sequence

**Step 1 — Internal preparation (before outreach):**
[Strengthen the argument, collect data, resolve the weakest point before presenting]

**Step 2 — First ally:**
[Name] — [Why start here: highest trust, will help refine the argument]
Meeting format: [1:1 / async / working session]
Goal of this conversation: [Not "get approval" — get their genuine input and early support]
What to ask for: [Their specific endorsement or input]

**Step 3 — Expand to early coalition:**
[Name(s)] — [Why add them next]
Timing: After [first ally] has weighed in

**Step 4 — Approach neutrals:**
[Name(s)] — [With coalition support behind the idea, present to those who haven't formed a view]
Framing: [How to present when you already have allies]

**Step 5 — Engage skeptics:**
[Name(s)] — [With coalition in place, approach the skeptics]
Timeline: [When]
Goal: [Not necessarily convert — understand the objection and find a resolution or work around it]

---

## Objection Preparation

| Stated objection | Underlying concern | PM response | Acceptable concession |
|-----------------|-------------------|-------------|----------------------|
| "[What they say]" | [What they actually worry about] | [Acknowledge + reframe + evidence] | [What PM can give without losing the outcome] |
| "[Objection]" | [Underlying concern] | [Response] | [Concession if any] |

**The objection PM can't answer well:**
[Name it honestly] — [What would resolve it, or how to handle it transparently in the alignment conversation]

---

## Decision Design

**Decision format:** [Async doc / 1:1 meeting / group meeting / approval email]

**Who must be present / included:**
- [Required: decision authority]
- [Optional: credibility witnesses]

**The ask:** [Binary yes/no / Choose from options A, B, C / Provide input by date]

**Decision document:** [Link or "to be written"]

**Pre-read required:** [Yes — send N days before / No]

**What makes the decision easy to say yes to:** [Framing, options structure, risk mitigation stated upfront]

---

## Escalation Plan

**Escalation path:** [To whom, through whom]

**Threshold for escalation:** [What must happen first — exhausting direct influence, a specific blocker, a timeline breach]

**Relationship cost of escalation:** [What is damaged if PM escalates — and is it worth it]

**De-escalation option:** [If escalation is avoided at the last moment, what's the fallback]

---

## Influence Principles in Play

These are the influence levers relevant to this situation (apply deliberately, not manipulatively):

- **Reciprocity:** [Where PM has previously supported this stakeholder — can be acknowledged]
- **Social proof:** [Who else has already aligned — useful to name when approaching neutrals]
- **Commitment consistency:** [Prior statements the stakeholder has made that are consistent with the desired outcome]
- **Authority:** [Whose external or internal authority can be cited to support the argument]
- **Scarcity / urgency:** [What is the consequence of delay — only use if real]
```

---

## Quality Gate

- Outcome stated as an action verb (not a vague direction)
- Minimum coalition identified (not everyone who might have an opinion)
- Sequence starts with allies, not skeptics
- Objections prepared with the underlying concern (not just the stated objection)
- Acceptable concessions named in advance (prevents giving away more than necessary in the moment)
- Escalation path named with threshold and relationship cost acknowledged
- Influence levers identified specifically (not generically)

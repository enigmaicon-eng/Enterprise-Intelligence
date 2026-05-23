---
name: pm-agenda
description: Structure a meeting agenda for a decision, alignment, or planning meeting. Produces a pre-read brief, timed agenda, decision framing, and role assignments.
version: "1.0"
changed: 2026-05-20
---

# PM Agenda

**Input:** Meeting purpose, attendees, key decision or outcome needed, any pre-read material or context.

**Output:** Displayed in terminal. Optionally written to `notes/structured/agenda-YYYY-MM-DD-<meeting-slug>.md` for distribution.

**Meeting types handled:** Decision meetings, alignment meetings, planning sessions, strategy reviews, go/no-go calls, retrospectives.

---

## Steps

1. **Read context.** Load `knowledge/pm/org-dynamics.md` (meeting governance section).

2. **Classify the meeting type and primary purpose:**
   - **Decision meeting:** A specific decision must be made by the end. One person is the decision owner.
   - **Alignment meeting:** Multiple parties need to reach shared understanding. No single decision, but the outcome is alignment.
   - **Planning session:** Work output (roadmap, sprint, prioritization) is produced during the meeting.
   - **Review / retrospective:** A past period or artifact is assessed and learnings are produced.

3. **Identify the single most important outcome.** "If we only accomplish one thing in this meeting, what must it be?" This becomes the anchor for the agenda. Everything else is secondary.

4. **Apply the DACI check:**
   - Is the decision owner named? (Required for decision meetings — if no one is named, no decision will be made)
   - Are the right people in the room? (Consulted = in the room; Informed = can receive notes afterward)
   - Are there people in the room who will add to time without adding to the decision? (Consider removing)

5. **Write the pre-read.** 24-hour advance distribution. Includes: context, what will be decided, options being considered, and what attendees are expected to do (review, decide, provide input).

6. **Design the agenda with time allocations.** Each agenda item has: a purpose (inform / discuss / decide), an owner, and a time budget. Total must fit the meeting length with a 10% buffer.

7. **Frame the decision items.** For each decision in the meeting: state the options explicitly, the trade-offs, and who decides.

8. **Write the output.**

---

## Output Format

```markdown
# Meeting Agenda — [Meeting Name] — [Date]

**Duration:** [N minutes]  **Location/Link:** [location]  
**Meeting type:** Decision | Alignment | Planning | Review  
**Decision owner (if applicable):** [Name]

---

## Primary Outcome

By the end of this meeting, we will have:
[One sentence — the specific decision made, alignment reached, or artifact produced]

---

## Pre-Read (distribute 24h in advance)

**Context:**
[2-3 sentences: what situation is this meeting responding to?]

**What will be decided:**
[The specific question being answered]

**Options being considered:**
- Option A: [Brief — full detail in linked doc if needed]
- Option B: [Brief]
- Option C: [Brief, if applicable]

**Your role:**
- [Name/Function]: Come prepared to [share input on X / make the call on Y / provide data on Z]

**Pre-read material:** [Link to relevant doc, if any]

---

## Agenda

| Time | Item | Purpose | Owner | Format |
|---|---|---|---|---|
| 0:00-0:05 | Context and goal | Inform | PM | No discussion |
| 0:05-0:15 | [Agenda item 1] | Discuss | [Owner] | Open discussion |
| 0:15-0:35 | [Key decision item] | Decide | [Decision owner] | Structured |
| 0:35-0:45 | [Second item] | Discuss | [Owner] | Open |
| 0:45-0:55 | Action items and close | Commit | PM | No discussion |
| 0:55-1:00 | Buffer | — | — | — |

---

## Decision Framing (for each decision in the meeting)

**Decision:** [What is being decided, in one sentence]

**Options:**
- A: [Option] — What we gain: [X] — What we give up: [Y]
- B: [Option] — What we gain: [X] — What we give up: [Y]

**My recommendation:** [Option A/B and why — PM's recommendation before the meeting starts]

**Decision owner:** [Name — who has the final call]

**Decision needed by end of meeting:** Yes / No (if not needed today, remove from agenda)

---

## Parking Lot

[Items that come up but are out of scope for this meeting — captured here, addressed later]

---

## Action Items Template (fill during meeting)

| Action | Owner | Due |
|---|---|---|
| [Action] | [Name] | [Date] |
```

---

## Quality Gate

- Primary outcome is stated as one specific sentence (not "discuss strategy")
- Decision meetings have a named decision owner
- Each agenda item has a purpose: inform / discuss / decide (no ambiguous items)
- Time allocations sum to meeting length - 10% (buffer for overrun)
- Pre-read distributed 24 hours before (not sent 5 minutes before)
- Decision items have options + trade-offs written in advance (not generated in the meeting)
- PM's recommendation stated before the meeting (avoids the "what do you all think?" anti-pattern)

# /prep — Meeting Preparation

## Purpose
Prepare yourself for a specific meeting. Not agenda creation (that's `/pm-agenda`) — preparation. What do you need to know, what is your role, what is the decision? Takes 5-10 minutes. Run it when preparation changes the outcome.

**When to run:**
- Strategy reviews, stakeholder alignment meetings, customer conversations
- Meetings where you're expected to make a decision or recommendation
- Meetings where you haven't engaged with the topic in 2+ days
- Any meeting you're running that has a binary output (yes/no, go/no-go, hire/pass)

**When NOT to run:**
- Recurring standups you run every week
- Meetings where you wrote the agenda today
- Social or low-stakes exploratory conversations

## Trigger Signals
- User invokes `/prep [meeting name or context]`
- User says "I have a meeting in 30 minutes about X" / "help me prepare for X"
- Do NOT trigger for: "I need to create an agenda" (use `/pm-agenda`) or "write me a pre-read" (use `/pm-exec-brief`)

## Input
Meeting context. If not provided, ask for:
1. Meeting name/topic (one phrase)
2. Who's in the room (roles, not names)
3. What you're there to do (decide / present / align / learn / unblock)

## Execution Protocol

### Step 1: Load relevant context
Based on the meeting topic:
- Check `execution/active-initiatives.md` for relevant initiative status
- Check `decision-frameworks/decisions-log.md` for recent decisions on this topic
- Check `strategy/active-bets.md` if strategy-relevant
- Check `meeting-intelligence/processed/` for any prior meetings on this topic

Load no more than 2 files. If more than 2 are needed: scope the meeting too large; flag this.

### Step 2: Identify the meeting type
Five meeting types, each with a different preparation focus:

**Decision meeting:** A decision will be made. You need: the options, your recommended option, the key assumption behind your recommendation, and your kill condition (what would make you change your recommendation in the room).

**Alignment meeting:** Multiple parties need to agree on something. You need: what you need them to agree to, what you think they'll resist, and your opening move.

**Update meeting:** You're presenting status. You need: what changed since last time, what's at risk, and what you need from them (if anything).

**Discovery meeting:** You're learning. You need: 3 specific questions you want answered, and the one question you're most afraid of the answer to.

**Escalation meeting:** Something is blocked. You need: what's blocked, what you've tried, the specific ask, and the cost of not resolving it.

### Step 3: Produce the prep brief

Format:
```
PREP — [Meeting name] — [date]
Type: [Decision | Alignment | Update | Discovery | Escalation]
Your role: [what you're there to do in one sentence]

What you need to know going in:
- [2-3 context facts from loaded files — not summaries, specific facts]

The key question:
[One sentence — the question whose answer determines how the meeting goes]

Your opening position:
[If decision or alignment: your recommendation or ask in one sentence]

Watch for:
[The one signal in the room that should change your approach]

Your exit criteria:
[What needs to happen for this meeting to have been worth attending]
```

### Step 4: Flag if the meeting shouldn't happen
If after loading context: the decision was already made, the question is already answered, or you don't have the authority to resolve what's on the agenda — say so explicitly. "This meeting shouldn't happen because [X]. Recommend: [cancel | defer | descope]."

## Constraints
- Prep brief is one page maximum. Prep that takes 10+ minutes to read defeated its own purpose.
- Do not generate a full background summary. Generate only the 2-3 specific facts you need in the room.
- Do not generate talking points. Prep is about what you need to know and decide, not what you're going to say.
- If you don't know the meeting type: ask. The prep structure is different for each.

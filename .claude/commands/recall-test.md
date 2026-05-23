# /recall-test — Active Recall Workflow

## Purpose
Generate a file-based elaborative retrieval exercise for a specific knowledge entry. The user reconstructs from memory; the comparison against the source file is the learning event. Not a quiz. Not a drill. A structured prediction-error cycle.

## Trigger Signals
- User invokes `/recall-test`
- User invokes `/recall-test [file path or topic]`
- Within 48h of any `/learn` invocation (automatic inclusion in briefing)
- Monthly cognitive review cadence
- Any knowledge entry with `reviewed` date >30 days old

## Input
- No argument: list 3-5 candidate entries from `knowledge/` sorted by most recently written or reviewed. User selects one.
- File path: use that specific entry.
- Topic/keyword: grep `knowledge/` for matching entries; present the top match.

## Execution Protocol

**Step 1: Load the target entry**
Read the specified knowledge file. Extract:
- The entry's title and domain
- The 3 most critical claims (the claims that, if forgotten, would make the entry useless)
- The 2 most commonly confused or conflated concepts in this domain (from the entry's own framing or from `systems/misconception-patterns.md`)

Do not reveal these to the user yet.

**Step 2: Issue the recall prompt**
Present this to the user:

```
RECALL TEST: [Entry Title]
Domain: [domain]

Without opening the file, write:
1. The 3 most important claims this entry makes
2. The specific mechanism or logic that grounds the most important claim
3. One connection this entry makes to another knowledge domain

Take 2-5 minutes. Write without checking. Then continue.
```

Stop. Do not add hints, prompts, or scaffolding. Wait for the user's response.

**Step 3: Run the comparison**
When the user responds, compare their reconstruction against the source entry:

For each of the user's 3 claims:
- **Match:** claim aligns with entry (exact or approximate) — note confidence is solid
- **Partial:** claim present but imprecise — note the specific imprecision
- **Missing:** claim not surfaced — this is the encoding gap
- **Wrong:** claim stated differently than entry — this is the error signal (highest value)

For the mechanism:
- Does the user's mechanism match the entry's? If different, is the user's version plausible but distinct, or is it incorrect?

For the connection:
- Is the stated connection in the entry? If yes, confirm. If not, is it a valid new connection not yet documented?

**Step 4: Produce the comparison report**

Format:
```
RECALL COMPARISON: [Entry Title]

Claim 1: [user's claim] → [Match | Partial | Missing | Wrong]
  Delta: [what was missing or wrong, exact text from entry]

Claim 2: [user's claim] → [Match | Partial | Missing | Wrong]
  Delta: [delta if any]

Claim 3: [user's claim] → [Match | Partial | Missing | Wrong]
  Delta: [delta if any]

Mechanism: [Match | Partial | Wrong]
  Delta: [mechanism from entry if different]

Connection: [Confirmed | Novel | Invalid]
  Note: [if novel, worth adding to KNOWLEDGE-INDEX.md cross-domain section]

ENCODING SUMMARY:
  Strong: [what recalled accurately — reinforce less]
  Gaps: [what was missing — target for re-engagement]
  Errors: [what was wrong — highest encoding priority]

NEXT ACTION:
  [If gaps/errors exist] → Read only the delta sections of the entry. Do not re-read the full file.
  [If all match] → Mark as reviewed: [today's date] in frontmatter. Schedule next recall in 30 days.
```

**Step 5: Update the entry's reviewed date (on match)**
If all claims match, update the `reviewed:` field in the entry's frontmatter to today's date.

## Constraints
- Do not provide hints before the user responds. The difficulty of retrieval is the mechanism.
- Do not re-read the full entry aloud during the comparison — surface only the deltas.
- Do not run more than one recall test in a single session. Cognitive exhaustion is a real cost.
- If the user says "I don't know" or "I can't remember anything" — that is valid data. Note it as a full encoding gap and proceed to comparison using the entry's actual content.

# Active Recall Prompts
## Version: v1.0

---

## Standard Recall Challenge

```
ENTRY TO TEST: [entry title]
FILE: [path]

Do not open the file.

Write from memory:
1. The 3 most important claims this entry makes
2. The mechanism or logic that grounds the most important claim
3. One connection this entry makes to another domain

Take 2-5 minutes. Write without checking.
---
[user writes here]
---
Now open the file. Compare.

For each of your 3 claims: Match | Partial | Wrong | Missing?
For the mechanism: Match | Partial | Wrong?
For the connection: Confirmed | Novel | Invalid?

State the delta only. Do not re-read the whole entry.
Update reviewed: [today's date] if all three claims match.
```

---

## Triage (Which Entry to Test)

```
Read: knowledge/KNOWLEDGE-INDEX.md

Find the 5 entries that meet this criteria:
- confidence: high or medium
- reviewed date furthest in the past

Rank them oldest-reviewed to newest.

Output: a ranked list of 5 candidates for recall testing.
The user selects one. Run the standard recall challenge on the selected entry.
```

---

## Post-Learn Recall (48h Follow-up)

```
A new knowledge entry was written: [path]
Written on: [date]

It has been ~48 hours. Run the standard recall challenge on this entry.

Note: this is the first recall cycle. The entry is fresh. 
The goal is to find what didn't encode — not to confirm what did.
Missing items at 48h are the highest-priority re-engagement targets.
```

---

## Forced Retrieval (No File Access)

```
Topic: [topic or concept]
Domain: [domain]

Without reading any files, write:
1. What is the most important thing you know about [topic]?
2. What is the mechanism or logic behind it?
3. Where does your knowledge of this topic feel weakest or least specific?

After writing: run /recall [topic] to retrieve the relevant entry.
Compare your reconstruction against what the file contains.
The comparison is the learning event — not the writing.
```

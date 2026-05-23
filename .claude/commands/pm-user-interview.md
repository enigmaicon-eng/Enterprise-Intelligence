---
name: pm-user-interview
description: Generate a user interview guide for a specific research question. Produces a hypothesis, screener criteria, structured interview questions with probes, and a debrief template.
version: "1.0"
changed: 2026-05-20
---

# PM User Interview

**Input:** Research question or assumption being tested, target user segment, context (problem discovery / solution validation / JTBD mapping / churn understanding / competitive positioning).

**Output:** Written to `meeting-intelligence/raw/interview-guide-YYYY-MM-DD-<topic-slug>.md`

---

## Steps

1. **Read context.** Load `knowledge/pm/user-research-methods.md` (qualitative methods section).

2. **Clarify the research type:**
   - **Problem discovery:** Understand the user's world before solution exists
   - **Assumption testing:** Validate or refute a specific assumption
   - **JTBD mapping:** Understand the underlying job the user is trying to accomplish
   - **Churn / win-loss:** Understand why users left or chose competitors
   - **Solution validation:** Test whether a proposed solution addresses the problem

3. **State the research hypothesis explicitly.** "We believe [assumption]. This interview will tell us whether [observable signal] is present." If the research question is "understand users better," reframe — too broad to produce actionable insights.

4. **Define the screener criteria.** Who should and should NOT be in this research. Behavioral criteria (has done X, experienced Y) rather than demographic criteria where possible.

5. **Design the interview structure.** Three phases:
   - **Warm-up (5-10 min):** Context setting, make the user comfortable, gather background
   - **Core exploration (30-40 min):** The research questions — open-ended, past-tense, behavior-focused
   - **Wrap-up (10-15 min):** Deeper probes, anything missed, close graciously

6. **Write the questions.** For each question:
   - Open-ended (not yes/no)
   - Past-tense where possible ("Tell me about the last time..." not "Do you ever...")
   - No leading framing ("Tell me what frustrated you..." is leading; "Tell me what happened..." is not)
   - Include 2-3 follow-up probes per main question

7. **Write the debrief template.** To be completed within 2 hours of each interview while fresh.

8. **Write the output.**

---

## Output Format

```markdown
# Interview Guide — [Topic] — [Date]

**Research question:** [What specifically we're trying to learn]  
**Hypothesis:** We believe [assumption] — this interview will surface [observable signal]  
**Research type:** Problem discovery | Assumption testing | JTBD | Churn/win-loss | Solution validation  
**Interview duration:** [N] minutes  
**Participants needed:** [N] (target saturation, not arbitrary number)

---

## Screener Criteria

**Include:** [Behavioral criteria — who qualifies]
- [Criterion — e.g., "Has managed a project with >5 contributors in the last 6 months"]
- [Criterion]

**Exclude:** [Who would skew the sample]
- [Criterion — e.g., "Works in the same industry as the PM team"]

---

## Interview Guide

### Opening (5-10 min)

"Thank you for your time today. We're here to learn about [general topic] — we're not testing you, there are no right or wrong answers, and nothing you say will hurt your relationship with us. I may take notes during our conversation. Is it OK if I record this session? [Get consent]"

**Background questions:**
- "Tell me a little about your role and what your typical day looks like."
- "What tools do you use most frequently for [domain]?"

---

### Core Exploration (30-40 min)

**[Theme 1 — e.g., Current workflow]**

Q1: "[Situation-framed question — e.g., Tell me about the last time you had to coordinate [X] across your team]"

Probes:
- "Can you walk me through exactly what you did, step by step?"
- "What was the hardest part of that?"
- "How did you feel when [specific moment]?"

Q2: "[Behavior-focused question]"

Probes:
- "How often does this happen?"
- "What do you do when [edge case]?"
- "How does your team handle this?"

---

**[Theme 2 — e.g., Pain points and workarounds]**

Q3: "[Problem-surface question — e.g., What's the most frustrating part of how you currently handle X?]"

Probes:
- "Can you give me a specific example of that happening?"
- "What have you tried to do about it?"
- "What would a perfect solution look like for you — if you could design it?"

Q4: "[Switching/decision question for JTBD/churn]"  
- "Walk me through the moment you decided to [switch / not use the feature / look for alternatives]."
- "What were you hoping to accomplish that you weren't able to?"

---

**[Theme 3 — e.g., Solution validation, if applicable]**

[Describe or show the concept]

Q5: "What's your first reaction to this?"

Probes:
- "How does this compare to how you do it today?"
- "What would you still be missing even with this?"
- "Who else on your team would care about this?"

---

### Closing (10-15 min)

- "Is there anything about [topic] that you expected me to ask but didn't?"
- "Is there someone else you think I should talk to about this?"
- "Thank you — one last question: on a scale of 1-10, how important is solving [the core problem we explored] to you? Why that number?"

---

## Debrief Template (complete within 2 hours)

```
Participant: [code name / anonymized]  
Date: [Date]  
Interviewer(s): [Names]

**Top 3 observations (what was said or done — verbatim where possible):**
1. 
2. 
3. 

**Most surprising moment:**

**What this confirms about our hypothesis:**

**What this challenges about our hypothesis:**

**Quote to keep:**

**Follow-up questions for next interview:**
```

---

## Quality Gate

- Hypothesis is specific and testable (not "understand users better")
- Screener criteria are behavioral (not demographic where possible)
- All questions are open-ended and past-tense (no yes/no, no leading)
- Each main question has 2-3 probes
- Debrief template included (to be used within 2 hours of each interview)
- "What's your first reaction" and escalating probes used for solution validation (not "do you like this?")

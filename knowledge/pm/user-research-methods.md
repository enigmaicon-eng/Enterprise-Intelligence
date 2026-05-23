---
title: User Research Methods
domain: pm
created: 2026-05-20
reviewed: 2026-05-20
connections: [discovery-intelligence, metrics-experimentation, writing-standards]
confidence: high
source: original synthesis
tags: [pm, research, qualitative, quantitative, interviews, usability, survey]
---

## Definition

User research is the systematic practice of reducing uncertainty about users before building. The method chosen must match the uncertainty type: qualitative methods surface the unknown unknowns; quantitative methods measure what you already know to measure. Using the wrong method gives precise answers to the wrong questions.

## The Research Method Selection Matrix

| Uncertainty Type | Question Being Answered | Right Method | Wrong Method |
|---|---|---|---|
| Do users have this problem? | Prevalence | Survey, analytics | Interviews |
| Why do users have this problem? | Mechanism | Interviews, observation | Survey |
| Can users use this design? | Usability | Usability testing | Analytics |
| Do users value this solution? | Desirability | Concept testing, interviews | A/B test (too early) |
| Does this solution work at scale? | Efficacy | A/B experiment, cohort analysis | Interviews |
| What are users actually doing? | Behavior | Analytics, session replay | Interviews |

The most common error: using interviews to answer prevalence questions ("how many users have this problem?") and surveys to answer mechanism questions ("why do users do X?").

## Qualitative Methods

### User Interviews

**When to use:** Problem discovery, JTBD mapping, understanding context and motivation, testing concepts, understanding the "why" behind behavioral data.

**Sample size:** 5-8 for a single segment to reach saturation (when answers stop being surprising). Add segments, not more people within a segment.

**Interview design principles:**
- Start with context, not the problem. "Walk me through the last time you [situation]" before "do you have a problem with X?"
- Ask about the past, not the hypothetical. "What did you do?" not "what would you do?"
- Silence is data. Let users fill it. Resist the urge to rescue them.
- Follow the energy. When a user slows down or gets emotional, go deeper — that's the real pain.
- The five-level abstraction test: ask "why does that matter to you?" five times. The fifth answer is usually the real job.

**Interview anti-patterns:**
- Leading questions: "Don't you find it frustrating when...?"
- Pitching during discovery: describing the solution during problem interviews
- Stopping at the stated problem: "It takes too long" → what does "too long" mean in their workflow?

### Contextual Inquiry / Observation

**When to use:** When users can't accurately report their own behavior. People's mental models of what they do are often wrong.

**Protocol:** Watch users do their actual work. Don't ask them to show you what they would do. Say: "Please work as you normally would — I'll observe and ask questions as we go."

**Output:** Behavioral observation log + interpretations kept separate. Never mix what you saw with what you think it means in the same note.

### Usability Testing

**When to use:** After a design exists. Tests "can users use this?" not "do users want this?" — those are different questions.

**Sample size:** 5 users reveal ~85% of usability issues. Don't test with 20 and waste the budget; test 5, fix the top issues, test 5 more.

**Task design:** Give users realistic scenarios, not instructions. "You need to send your team this week's report. Show me how you'd do that." Not "click on Reports, then click Export."

**Moderation:** Don't rescue users who are confused. Let them struggle — their frustration is the signal. Ask "what are you thinking right now?" not "are you confused?"

## Quantitative Methods

### Surveys

**When to use:** Measuring prevalence of a known problem across a large population. Validating hypotheses from qualitative work. Benchmarking satisfaction.

**Survey design principles:**
- One construct per question. Double-barreled questions ("Was the feature easy and useful?") produce uninterpretable data.
- Avoid ordinal scales for continuous data. "How often do you use this?" → actual frequency options (daily/weekly/monthly) not vague scales.
- Randomize answer order for symmetric constructs to remove position bias.
- Test every survey with 3 internal respondents before deploying. Ambiguous questions are invisible to the writer.
- NPS is a relationship metric, not a feature metric. Don't use it to evaluate individual features.

**Sample size:** Depends on precision needed. For a ±5% margin at 95% confidence with a binary outcome: ~400 respondents. For segment comparisons, each segment needs its own adequate sample.

**Survey failure modes:** Leading questions, acquiescence bias (users agree with whatever you suggest), social desirability bias (users say they behave better than they do).

### Quantitative Behavioral Analysis

**When to use:** Understanding what users actually do (not what they say they do). Finding patterns in usage. Identifying funnel drop-off. Measuring feature adoption.

**The analysis hierarchy:**
1. Funnel analysis: where do users drop off in a workflow?
2. Cohort analysis: do users who [do X] retain better than those who don't?
3. Segmentation: which user segment behaves differently, and why?
4. Correlation: which early behaviors predict long-term retention?

**The causal gap:** Quantitative analysis shows correlation, not causation. "Feature X users retain better" means feature X users are different, not that feature X causes retention. Use experiments to establish causality.

## Research Operations

### Recruiting

**Criteria design:** Recruit on behavior, not demographics. "Has switched project management tools in the last 6 months" is a better criterion than "35-45 years old, team lead." Demographics are proxies for behavior; recruit for the behavior directly.

**FAANG-level rigor:** Maintain a research panel. Users who've participated before are faster to recruit but more likely to have learned your patterns — balance with fresh participants.

**Incentives:** Match incentive to effort and participant type. Consumer users: $50-100 gift card for 60 min. Enterprise professionals: $150-250. Under-incentivizing produces no-shows; over-incentivizing attracts mercenary respondents.

### Synthesis Standards

Every research engagement produces:
1. **Raw evidence log** — observations verbatim, no interpretation
2. **Synthesis** — patterns, themes, and the insight chain (observation → interpretation → implication → action)
3. **Assumption status update** — which assumptions were tested and what happened

Research that produces observations but no implication + action has not been synthesized — it's been filed.

## Connections

Links to [[discovery-intelligence]] — research methods serve the discovery process. Links to [[metrics-experimentation]] — qualitative research informs experiment hypotheses; quantitative research validates them. Links to [[writing-standards]] — research synthesis standards align with PRD and spec writing.

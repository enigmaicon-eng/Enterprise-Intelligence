---
title: AI and ML Product Management
domain: pm
created: 2026-05-20
reviewed: 2026-05-20
connections: [metrics-experimentation, technical-fluency, platform-developer-pm, writing-standards]
confidence: high
source: original synthesis
tags: [pm, ai, ml, llm, responsible-ai, model-evaluation, data-strategy, evals, genai]
---

## Definition

AI/ML PM is not a specialization — at FAANG scale, it is the baseline. Every product now has ML components, and PMs who cannot reason about model performance, data quality, responsible AI, and the unique failure modes of probabilistic systems are operating with a blind spot.

The core difference: traditional products fail deterministically (a bug produces the same wrong output every time). ML systems fail probabilistically (the model produces wrong outputs some percentage of the time, in patterns that are hard to predict and vary across user segments). This changes how you spec, test, measure, and communicate about the product.

## The ML Product Lifecycle

**Phase 1 — Problem framing:** Can this problem be solved with ML? The question is not "can a model do this?" but "is ML the right tool given the cost, latency, accuracy requirements, and data availability?"

**Phase 2 — Data strategy:** What data is needed to train, validate, and serve the model? Who produces it? Is it available? What labeling is required? What are the privacy implications?

**Phase 3 — Model specification:** What is the ML task? (Classification, regression, ranking, generation, clustering.) What are the accuracy requirements? What is the acceptable error rate and error type trade-off?

**Phase 4 — Evaluation design:** How will the model be evaluated before deployment? What offline metrics are used? What online metrics validate real-world performance?

**Phase 5 — Responsible AI review:** What biases exist in the training data? Who is disadvantaged by model errors? What harms could result from model failure? What mitigations are in place?

**Phase 6 — Deployment and monitoring:** How is the model served? What is the latency budget? How is model performance monitored in production? What triggers a model update or rollback?

## Model Evaluation Vocabulary for PMs

PMs do not train models. But PMs must understand what the model metrics mean for user experience.

**For classification models:**
- **Precision:** Of the predictions the model made positively, what % were correct? (High precision = few false positives)
- **Recall:** Of all the actual positives, what % did the model find? (High recall = few false negatives)
- **F1 score:** Harmonic mean of precision and recall — useful when both matter
- **AUC-ROC:** Overall model discrimination ability — higher is better

**The PM trade-off:** Precision vs. recall is a product decision, not a model decision.
- High precision matters when false positives are costly: a spam filter that marks good email as spam loses user trust.
- High recall matters when false negatives are costly: a fraud detection system that misses fraud causes financial harm.
- PM must specify which error type is more acceptable for the user experience.

**For generative AI / LLMs:**
- **Evals:** Structured evaluations measuring model output quality on a set of test cases. The PM's responsibility: define the eval set and the rubric. Engineering runs the evals.
- **Hallucination rate:** How often does the model produce confident, plausible-sounding but wrong information?
- **Coherence / fluency:** Does the output read as natural language?
- **Task completion rate:** On a set of representative tasks, what % does the model complete correctly?
- **Human preference rate:** In A/B eval between model versions, what % of the time do humans prefer the new version?

## Responsible AI — PM's Accountability

**PM owns the responsible AI requirements.** Engineering owns the mitigation implementation. Legal/ethics owns the framework. But the PM is accountable for ensuring responsible AI practices are applied before any ML feature ships.

**The responsible AI checklist for PM:**

**Bias and fairness:**
- Does the model perform equally well across protected groups (gender, race, age, disability)?
- Is the training data representative of the users who will be affected?
- What is the disparate impact if the model fails disproportionately for a subgroup?

**Transparency and explainability:**
- Can the model explain why it made a prediction? (Required in some regulatory contexts)
- Does the user know they are interacting with AI?
- Is the confidence level communicated to the user when relevant?

**Privacy:**
- Does training data contain personal information? Is consent obtained?
- Can the model memorize and reproduce training data (memorization attack risk)?
- Is personally identifiable information processed in compliance with applicable regulations?

**Safety and harm:**
- What harms could result from model errors in the target use case?
- Are there failure modes that could cause physical, psychological, financial, or reputational harm?
- What safeguards exist (content filtering, output validation, human review thresholds)?

**Model Card:** For any significant ML feature, write a model card before deployment:
- Model task and intended use
- Training data description
- Performance metrics across key segments
- Known limitations and failure modes
- Responsible AI mitigations in place
- Contact for issues

## Data Strategy for PM

**The data flywheel.** More users → more data → better model → more value → more users. PM must design for the flywheel. The question is not "what data do we have?" but "what data does the model need, and how do we design the product to generate it?"

**Data quality is a PM responsibility.** Bad training data produces a bad model with impressive-sounding metrics. PM must understand:
- **Data freshness:** Does the model need recent data or is older data acceptable?
- **Label quality:** If labels are human-generated, what is the inter-rater agreement?
- **Distribution shift:** Does the distribution of production inputs match the training distribution? If not, model performance will degrade.
- **Data scarcity for edge cases:** Models fail on edge cases because edge cases are underrepresented in training data. PM must identify high-stakes edge cases and ensure they're represented.

**Data contracts:** In data product contexts, a data contract specifies the expected schema, quality, and freshness of data flowing between systems. PM owns the data contract requirements; data engineering owns implementation.

## Evals — PM's Primary AI Quality Tool

**Evals are the PM's equivalent of acceptance criteria for AI systems.** A feature ships when it passes the eval set.

**Building the eval set:**
1. Define the tasks the model should be able to perform (not edge cases — the primary jobs)
2. Create test cases that represent real production inputs (ideally sampled from production)
3. Define the rubric: what constitutes a correct answer? (For open-ended generation, this often requires human judgment — define the criteria explicitly)
4. Establish a baseline: what is the current performance on this eval set?
5. Set a threshold: what performance level is required before the feature can ship?

**Eval anti-patterns:**
- Evals written after the model is trained (you'll unconsciously fit the eval to the model)
- Eval sets that don't represent the diversity of real production inputs (models pass on easy cases)
- Binary pass/fail evals for nuanced tasks (use a rubric, not just correct/incorrect)
- Evals that only measure capability (what it can do) without measuring safety (what it shouldn't do)

## Human-in-the-Loop Design

When ML models are probabilistic, PM must design for human oversight — especially in high-stakes contexts.

**The three human-in-the-loop patterns:**

**Human-on-the-loop:** AI acts autonomously; humans review afterward. Low stakes, high throughput. (Email categorization, recommendation ranking)

**Human-in-the-loop:** AI proposes; human approves before action is taken. Medium stakes. (AI-drafted email requiring approval, AI diagnosis requiring physician confirmation)

**Human-as-the-loop:** AI assists human; human makes all decisions. High stakes. (AI-assisted surgery, AI-assisted legal document review)

PM must select the pattern appropriate for the risk level of the use case. Pattern mismatch — automating a decision that should have human review — is one of the most common responsible AI failures.

## LLM Product Design Specifics

**Prompt engineering as PM responsibility:** For LLM-powered features, PM writes the system prompt (the instructions given to the model). This is equivalent to writing a spec — it determines product behavior. PM should:
- Write the first draft of the system prompt
- Test it against the eval set
- Version-control it alongside the feature code
- Update it when product behavior needs to change

**Latency budget:** LLM inference is slow relative to traditional API calls. PM must define the latency budget and design the UX to accommodate it:
- Streaming responses (show output as it generates)
- Async generation (kick off generation, notify when done)
- Loading states that maintain user trust during generation

**Context window management:** LLMs have finite context windows. PM must specify what information is included in the context — too little context → poor output; too much context → cost and latency increase.

## Connections

Links to [[metrics-experimentation]] — ML systems require specialized eval metrics alongside product metrics. Links to [[technical-fluency]] — ML architecture decisions create unique product constraints. Links to [[platform-developer-pm]] — ML infrastructure is a platform capability with its own PM responsibility.

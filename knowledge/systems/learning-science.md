---
title: Learning Science — Operational Principles
domain: systems
created: 2026-05-22
reviewed: 2026-05-22
tags: [learning, memory, recall, encoding, spaced-repetition, elaboration]
connections: [systems/reasoning-quality.md, systems/misconception-patterns.md, operations/work-patterns.md]
confidence: high
source: cognitive science literature synthesis — Bjork, Roediger, Dunlosky
---

# Learning Science — Operational Principles

## Definition

The mechanisms by which humans encode, store, and retrieve information — and the specific interventions that make encoding more durable and retrieval more reliable. Applied to knowledge work: the design of practices that turn exposure into usable understanding.

## Why It Matters

Most knowledge work practices optimize for coverage (reading more, capturing more, reviewing more). The research is unambiguous: coverage is not the bottleneck. Retrieval practice and error signal are. One recall attempt after reading produces more durable encoding than three re-reads. The implication is operational: structure your knowledge practices around retrieval, not acquisition.

## Key Principles

**1. Testing Effect (Retrieval Practice)**
Retrieving information from memory strengthens encoding more than re-studying the same material. This is not intuitive — retrieval feels harder than re-reading and produces less immediate fluency. But the difficulty is the mechanism. Difficulty = encoding work.

*Operational form:* After reading or capturing a knowledge entry, close it and reconstruct the key claims. Then compare against the source. The comparison (error signal) is the learning event.

**2. Spaced Practice**
Reviewing material at increasing intervals builds more durable memory than massed review. The optimal schedule: review within 24h, then 3 days, then 10 days, then 30 days. Every knowledge entry has a `reviewed` date for this reason.

*Operational form:* Knowledge entries not reviewed in 90+ days are candidates for `/recall-test` before the content becomes latent.

**3. Elaborative Interrogation**
Asking "why is this true?" and generating an explanation (not retrieving one) produces stronger encoding than passive reading. The self-generation of mechanism creates richer memory traces.

*Operational form:* When reading a knowledge entry, generate the mechanism behind each principle before checking if the file explains it. If the file's explanation differs from yours, the delta is the learning signal.

**4. Interleaved Practice**
Mixing topics or problem types during study produces better long-term retention than blocked practice (all topic A, then all topic B). Interleaving is harder and feels less productive — that difficulty is the mechanism.

*Operational form:* Monthly cognitive review (playbooks/cognitive-review.md) deliberately mixes domains: strategy + technical + operations in the same session.

**5. Desirable Difficulty**
Practice that is too easy produces fluency without durability. Practice that is too hard produces frustration without encoding. The target zone is effort that is effortful but completable. Struggling and succeeding > succeeding without struggling.

**6. Error Signal Is the Learning Mechanism**
Learning does not occur at exposure or even at recall. It occurs when prediction error is detected and corrected. The comparison between what you thought was true and what is actually true is where encoding happens.

*Implication:* Passive review (re-reading) has near-zero learning value after the first pass. The only practices that drive durable learning are those that generate prediction error.

## In Practice

**File-based recall protocol:**
1. Identify a knowledge entry to test.
2. Close or don't read it.
3. Write from memory: the 3 most important claims in the entry.
4. Open the entry. Compare.
5. Identify exactly what was wrong or missing. That delta is the next encoding target.
6. Do not re-read the whole entry — focus attention on the delta only.

**Elaborative questioning:**
When reading a new entry, stop at each principle and ask: "Why is this true? What mechanism would produce this?" Generate an answer before reading on. If the mechanism in the file is different, note the delta.

**Review cadence (entry-level):**
- Within 48h of writing: first recall test
- 7 days: second recall test
- 30 days: third recall test
- 90 days: misconception check (has this entry aged well?)

## Common Learning Failure Modes

| Failure | Description | Correction |
|---|---|---|
| Re-reading as review | Passive re-exposure, no prediction error | Replace with recall test |
| Blocked practice | All one domain at a time | Interleave across `/weekly` review |
| Coverage maximalism | More input, less retrieval | Recall after every 3 new entries |
| Low-difficulty practice | Only reviewing what's already known | Target entries where recall confidence is low |
| Fluency illusion | Re-reading produces smooth recall but shallow encoding | Test recognition vs. generation |

## Connections

- `systems/reasoning-quality.md`: error signal in reasoning is same mechanism as error signal in learning
- `systems/misconception-patterns.md`: misconceptions persist because they generate low error signal
- `operations/work-patterns.md`: these principles apply to session design and knowledge hygiene rituals

## Open Questions

- What is the right interval structure for technical knowledge that evolves (vs. stable facts)?
- How does elaborative interrogation interact with expertise? Does expertise reduce the benefit by eliminating the prediction error?

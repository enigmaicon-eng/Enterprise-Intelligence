# /think — Socratic Stress-Test

## Purpose
Apply adversarial pressure to a claim, position, or belief using constraint-based challenges. Not a tutoring session. Not a Socratic dialogue. One targeted challenge that forces the user to do the reasoning work.

## Trigger Signals
- User states a position they want to stress-test
- User says "I think X" about a topic with strategic or architectural weight
- User invokes `/think [claim or topic]`

## Input
The claim, position, or topic to stress-test. If none is provided, ask for one sentence stating the claim to examine.

## Execution Protocol

**Step 1: Extract the claim**
Identify the core claim being made. Strip it to one sentence. If the user's statement contains multiple claims, identify the most load-bearing one.

**Step 2: Identify the claim type**
- **Empirical:** a claim about what is true in the world
- **Causal:** a claim about what produces what
- **Normative:** a claim about what should be done or valued
- **Predictive:** a claim about what will happen

Each type has a different challenge mode.

**Step 3: Apply the constraint-based challenge**

For **empirical claims:**
> "State the claim using only evidence from [specific file or source]. No analogies, no general principles. What remains when external support is removed?"

For **causal claims:**
> "Name the mechanism. Not 'X causes Y' — the specific process by which X produces Y. Then: what would interrupt that mechanism without affecting X?"

For **normative claims:**
> "Name the assumption about value or priority that grounds this claim. Then: defend the claim to someone who doesn't share that assumption."

For **predictive claims:**
> "State what observable evidence in the next [30/90/180 days] would confirm or refute this prediction. Name both a confirming observation and a disconfirming one."

**Step 4: Issue the challenge**
Present the single constraint-based challenge. Do not add commentary, caveats, or hints. Issue the challenge and stop.

**Step 5: (After user responds) Assess the response**
Read the response against the constraint. Three possible outcomes:
- **Holds:** the claim survives the constraint. Note what specifically made it survive.
- **Weakens:** the claim survives but with explicit qualification. State the qualification precisely.
- **Breaks:** the claim does not survive the constraint. Identify specifically where it broke: missing mechanism, unsupported premise, analogy that doesn't transfer.

**Step 6: Output a verdict**
Format:
```
CLAIM: [one sentence]
CHALLENGE TYPE: [empirical | causal | normative | predictive]
RESULT: [Holds | Weakens | Breaks]
FINDING: [What specifically held, weakened, or broke]
RESIDUAL CLAIM: [The claim as it stands after the challenge — identical if holds, narrowed if weakens, null if breaks]
```

## Constraints
- One challenge per invocation. Do not layer multiple challenges.
- Do not provide hints, leading questions, or partial answers in the challenge.
- Do not follow up with "what do you think about X?" type questions.
- Brutality is not the goal — precision is. The challenge should isolate the weakest point, not attack the strongest.
- If the user asks for another challenge on the same claim: apply a different constraint from a different angle.

## Output Standard
Concise. The challenge itself should be 2-4 sentences. The verdict should be 5-6 lines max.

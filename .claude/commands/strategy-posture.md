# /strategy-posture — Articulate or Stress-Test Strategic Posture

Articulate the current strategic posture clearly, or stress-test it against a challenge, a competitor move, or a "what if" scenario. Distinct from /strategy-review (which evaluates evidence) and /pm-strategy (which is product-specific).

## Trigger
`/strategy-posture` — articulate current posture from first principles
`/strategy-posture stress-test [scenario]` — stress-test posture against a specific challenge
`/strategy-posture vs [competitor or alternative]` — position posture against an alternative approach
`/strategy-posture annual` — set or refresh annual strategic themes

## What Strategic Posture Is
Strategic posture is the set of choices that define how you're choosing to compete or operate — what you're optimizing for, what you're not, and why. It's not a mission statement or a list of goals. It's a set of bets about how the world works and where you've decided to stand.

A well-articulated posture answers:
1. What do we believe that most people don't? (Thesis)
2. What are we choosing NOT to do because of that belief? (Trade-offs)
3. What would prove us wrong? (Falsifiability)

---

## Protocol — Articulate Current Posture

### Step 0: Load strategic state
Read in order:
1. `strategy/active-bets.md` — the portfolio (these are the revealed preferences)
2. `strategy/OKRs.md` — tactical expression of H1 bets
3. Most recent strategy review in `strategy/reviews/`
4. `knowledge/strategy/annual-themes.md` — annual themes if set

### Step 1: Derive the implicit posture
From the active bets, derive what the current posture IS — based on what has been committed to, not what has been said. Revealed preferences are more reliable than stated ones.

Ask: "If someone read only the bet portfolio, what would they conclude we believe about how the world works and where we're placing our bets?"

### Step 2: Check posture coherence
Does the portfolio hang together as a coherent posture, or are bets pointing in different directions?

Test: Can you write one paragraph that explains all active bets as expressions of a single strategic logic? If not, the posture is incoherent.

### Step 3: Identify posture gaps
What important strategic territory is NOT covered by the current portfolio?
- No H3 bet = no options position
- No defensive bet = only offense
- No learning bet = no capability-building under uncertainty

### Step 4: Output the posture articulation
Format:
- **Strategic thesis**: The core belief driving the posture (1-2 sentences)
- **Bet portfolio logic**: How the active bets express that thesis
- **What we're explicitly NOT doing**: The trade-offs that define the posture
- **What would falsify this posture**: Specific observable evidence that should trigger a posture rethink
- **Coherence assessment**: Does the portfolio hang together? Gaps or contradictions?

---

## Protocol — Stress-Test Posture

Load the current posture (same Step 0-2 as above), then apply the stress scenario:

**For a competitor move scenario**: "Competitor X does Y. What does this do to our thesis? Does any bet need to be cut or accelerated?"

**For a "what if" scenario**: "What if [assumption Z] turns out to be wrong? How does the posture need to adjust?"

**For an adversarial scenario**: Apply the "smart adversary" test: "What would a smart, well-resourced competitor do specifically to exploit weaknesses in this posture?"

Output for each stress scenario:
- What the scenario reveals about the posture
- Which bets are most at risk
- Recommended posture adjustment (if any) — specific, not "be more flexible"

---

## Protocol — Annual Themes

Annual themes are the 3 strategic priorities for the year — not goals (those are OKRs), but themes that describe the shape of the year's bets.

**One theme per horizon**: One H1-dominant theme, one H2-dominant theme, one H3 theme.

**Theme format**: "[Active verb] [specific territory] to [specific outcome]"
Bad: "AI and Growth"
Good: "Compound AI context quality to reach reliable 90-day session continuity"

Write to: `knowledge/strategy/annual-themes.md`

## Ownership
- `/strategy-posture` = posture articulation and stress-testing (this skill)
- `/strategy-review` = periodic evidence-based bet portfolio review
- `/pm-strategy` = product strategy specific to a product or initiative

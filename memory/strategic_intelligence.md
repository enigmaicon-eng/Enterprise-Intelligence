---
name: strategic-intelligence
description: P24 Strategic Intelligence System — 3 skills adding continuous intelligence gathering to the strategy stack
metadata:
  type: project
---

# Strategic Intelligence System (P24)

Built 2026-05-23. Adds the intelligence gathering layer that was missing between quarterly horizon scans and monthly strategy reviews.

**Why:** The existing strategy stack (bet/horizon/strategy-review/strategy-posture) processes intelligence on a cadence. Signals arrive continuously. Without a capture mechanism, competitor moves, market shifts, and environmental observations reach the next scan stale or forgotten.

**How to apply:** Capture signals as they arrive with `/signal capture`. Log specific competitor moves with `/competitive-radar log`. Before monthly strategy review, run `/assumption-register` to surface at-risk bet assumptions. Weekly: run `/signal review` and `/competitive-radar review` to surface what needs action.

## What Was Built

**Architecture extension:** `architecture/STRATEGIC-INTELLIGENCE-SYSTEM.md` — Intelligence Layer section added (data architecture, signal classification, assumption status taxonomy, competitive implication types, information flow diagram)

**3 new skills:**
- `/signal` — strategic signal capture (capture/review/list subcommands); writes to `strategy/signals/YYYY-MM.md`; H1 threats flag immediately
- `/assumption-register` — derives 3-5 implicit assumptions per bet from the thesis; scans evidence log for challenges; surfaces Untested/Tested-held/At risk/Violated status
- `/competitive-radar` — logs specific competitor/market actor moves (log/review/[bet-id] subcommands); writes to `strategy/competitive/radar.md`; disconfirming moves surface immediately with `/bet update` recommendation

## Existing Skills (Not Duplicated)

| Skill | Covers |
|-------|--------|
| `/bet` | Full lifecycle including evidence logging |
| `/horizon` | Structured quarterly H1/H2/H3 scan |
| `/strategy-review` | Monthly portfolio verdicts |
| `/strategy-posture` | Posture articulation and stress-testing |
| `/pm-competitive` | Product-level feature comparison (different from bet-level) |

## New Data Directories

- `strategy/signals/` — monthly signal log files (YYYY-MM.md)
- `strategy/competitive/` — competitive move log (radar.md)

## Recommended Weekly Ritual Addition

Monday: `/signal review` + `/competitive-radar review` → escalate to `/bet update` as needed.
Pre-strategy-review: `/assumption-register` → identify at-risk assumptions before issuing verdicts.

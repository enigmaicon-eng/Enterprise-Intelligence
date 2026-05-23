---
name: execution-intelligence
description: P27 Execution Intelligence System — 3 skills measuring throughput trends, work allocation, and friction patterns across execution history
metadata:
  type: project
---

# Execution Intelligence System (P27)

Built 2026-05-23. Analytics layer on the execution trace infrastructure (P21 + P22). Surfaces performance patterns that trace capture accumulates data for but never reports.

**Why:** The existing system handles tracing (/trace-capture), reviewing (/exec-inspect), failure analysis (/failure-review), pattern codification (/pattern-mine), and health dashboards (/ops-dashboard). None answer: Is throughput improving over time? Is actual work aligned with intentions? What recurring friction is slowing execution without causing outright failure?

**How to apply:** Weekly → `/exec-throughput` (is execution momentum up or down?). Monthly → `/exec-allocation` (is time going where intended?) + `/exec-friction` (what recurring impediments exist?). Before structural workflow changes → `/exec-friction` to confirm what's actually being fixed.

## What Was Built

**Architecture doc:** `architecture/EXECUTION-INTELLIGENCE-SYSTEM.md` — Capability distinctions vs existing skills, throughput model, work allocation model with category mapping, friction taxonomy (6 types), recommended cadence, anti-patterns

**3 new skills:**

- `/exec-throughput` — Completion rate trend over time. Compares last-30 vs prior-30 day completion rates. Classifies as Improving/Stable/Declining/Recovery/Insufficient. 90-day view in 2-week buckets. Session-type breakdown. Requires ≥10 episodes.

- `/exec-allocation` — Work type distribution. Maps trace session type tags → 6 work categories (Proactive/Productive/Reflective/Generative/Reactive/Overhead). Computes reactive ratio, strategic ratio, overhead ratio. Flags structural imbalance (reactive >30%, strategic <10%, overhead >25%). Compares against intention proxy from journal entries where available.

- `/exec-friction` — Non-failure impediment analysis. 6 friction types: dependency block, clarity block, scope creep, context switch, energy depletion, tool friction. Reads trace content for pivot/block/replan signals (not just outcome codes). Recurring threshold = 3+ instances. Structural mitigation suggested per type. Cross-references existing patterns/.

## Key Distinctions

- `/exec-throughput` ≠ `/ops-dashboard`: ops-dashboard is a 30-day snapshot with health flags; throughput measures trend direction over time
- `/exec-allocation` ≠ `/skill-stats`: skill-stats counts invocations; allocation measures work-TYPE distribution
- `/exec-friction` ≠ `/failure-review`: failure-review covers non-completed outcomes; friction covers slowdowns and pivots in ANY outcome (including completed)

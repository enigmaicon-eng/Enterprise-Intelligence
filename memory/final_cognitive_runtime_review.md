---
name: final-cognitive-runtime-review
description: P31 Final Cognitive Runtime Review — authoritative audit finding 145 skills/56 arch docs vs ceilings of 120/25; complete simplification roadmap Phases A-E
metadata:
  type: project
---

# Final Cognitive Runtime Review (P31)

**Date:** 2026-05-23. Authoritative full-workspace audit replacing all prior simplification guidance.

**Critical findings:**
- Skills: 145 (ceiling 120) — CRITICAL, 25 over
- Architecture docs: 56 (ceiling 25) — CRITICAL, 31 over
- P20 SR-5 consolidation: merged docs created but source docs NEVER deleted (13 zombie docs)
- P20 SR-1/SR-2 retirements: 7 skills ordered retired, never deleted
- 33+ skills invisible (not in routing table), including all P16 mem-* and P19 MCP-* skills

**Simplification roadmap (Phases A-E):**
- Phase A: Delete 13 zombie arch docs + 7 zombie skills + 2 dead memory files
- Phase B: Retire 6 /mem-* skills (P16 superseded by auto-memory)
- Phase C: Retire 6 invisible skills; make MCP/skill-mgmt discoverable in routing table
- Phase D: Retire 2 knowledge skills; archive 7 historical P-series arch docs
- Phase E: Merge memory/retrieval/MCP arch docs (3 merges); archive 5 low-signal docs

**Projected after Phases A-E:** ~124 skills, ~22 arch docs (within ceiling)

## Architecture doc

`architecture/FINAL-COGNITIVE-RUNTIME-REVIEW.md`

## 10 Rule Sets (authoritative)

1. NON-NEGOTIABLE ARCHITECTURAL RULES (NAR-1 through NAR-7)
2. ANTI-DRIFT RULES (ADR-1 through ADR-6)
3. MAXIMUM COMPLEXITY LIMITS (table with hard limits)
4. OPERATIONAL SIMPLICITY RULES (OSR-1 through OSR-6)
5. BOUNDED AUTONOMY RULES (BAR-1 through BAR-10, supersedes all prior A/B/G-rules)
6. MEMORY HYGIENE RULES (MHR-1 through MHR-7)
7. RETRIEVAL QUALITY RULES (RQR-1 through RQR-6)
8. SKILL CREATION CONSTRAINTS (SCC-1 through SCC-7)
9. ORCHESTRATION CONSTRAINTS (OCR-1 through OCR-8)
10. LONG-TERM MAINTENANCE RULES (LMR-1 through LMR-10)

## Related

[[final_simplification_review]] [[workspace_audit]] [[runtime_hardening]]

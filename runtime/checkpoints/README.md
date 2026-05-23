# runtime/checkpoints/

Gate checkpoint records. Written when a human gate is resolved (approved, paused, or abandoned).

Naming: `{wf-id}-gate{N}.json` — e.g., `wf_20260522_001-gate2.json`

Schema: `architecture/RUNTIME-STATE-SCHEMA.md` → Gate Checkpoint section.

Checkpoints record the operator's decision at each gate. They are the audit trail of human approvals. Never edit checkpoint files.

Retention: Same as the parent workflow — retained while active, then 30 days after completion.

# runtime/plans/

Workflow plan files. One JSON file per workflow.

Naming: `{wf-id}.json` — e.g., `wf_20260522_001.json`

Schema: `architecture/RUNTIME-STATE-SCHEMA.md` → Workflow Plan section.

Plans are written once (at plan time) and immutable after the workflow reaches APPROVED status. Do not edit a plan file after approval — create a new workflow instead.

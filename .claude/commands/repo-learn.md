# /repo-learn — Extract Intelligence from a Repository

Run a structured analysis of a repository to extract architectural patterns, design decisions, and reusable learnings into the knowledge base.

## Trigger
`/repo-learn [repo-path or repo-name]` — repo-path is a path under `repos/`, or a repo name if already cloned there.

## When to Use
- After cloning a new reference repository for study
- When a significant repo update (50+ new commits) makes the old insight entry stale
- When preparing to integrate patterns from another project into this workspace

## Protocol

### Step 1: Silent context load
Read `knowledge/KNOWLEDGE-INDEX.md`. Check if a repo insight for this repo already exists under `knowledge/technical/repo-insights/`. If yes, read the existing entry — this is an update, not a new entry.

### Step 2: Orientation pass (5 files max)
Read in order:
1. `README.md` or `README` — overall purpose and design intent
2. `package.json` / `pyproject.toml` / `Cargo.toml` — dependency signal (what the author chose to rely on)
3. Primary entry point (e.g., `main.py`, `index.ts`, `src/main.rs`) — how the system starts
4. The largest or most central module/directory — core logic
5. Any `ARCHITECTURE.md`, `DESIGN.md`, or `docs/` directory — if it exists

### Step 3: Pattern extraction
For each file read, identify:
- Non-obvious implementation decisions (anything a beginner would do differently)
- Abstractions that generalize beyond this specific codebase
- Patterns applicable to this workspace's own work

### Step 4: Build the insight entry
Use `templates/repo-insight.md`. Required:
- `commit_sha`: run `git -C [repo-path] rev-parse --short HEAD` to get current SHA
- `Architecture Overview`: actual directory tree with annotations (run `ls` if needed)
- At least 2 `Patterns Worth Extracting` with file:line citations
- `How to Apply Learnings Here`: concrete, workspace-specific application

### Step 5: Write the file
Write to: `knowledge/technical/repo-insights/[repo-name].md`

If the file already exists (update case): use Edit to update changed sections. Update `analyzed` date and `commit_sha`. Preserve `Known Instances` history.

### Step 6: Update the knowledge index
Add or update the entry in `knowledge/KNOWLEDGE-INDEX.md`:
```
| [repo-name] | technical/repo-insights/[repo-name] | Repo insight: [one-line description] | [date] |
```

### Step 7: Check for cluster trigger
If 3+ repo insight files now exist, check `knowledge/clusters/` for a `technical-patterns.md` cluster. If it doesn't exist or is stale, note that `/synthesize` should be run.

### Step 8: Report
- File path written
- 2-3 highest-value patterns found
- Whether any existing knowledge entries should be updated based on new findings
- Cluster trigger status

## Quality Bar
- "Core Design Decisions" must include the WHY, not just the what
- "How to Apply Learnings Here" must be workspace-specific — not generic advice
- `commit_sha` must be populated — without it, the entry has no freshness signal

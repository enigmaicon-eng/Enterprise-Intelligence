# /learn — Structured Learning Capture

Capture learning from any external source into the `learning/` staging area with a structured entry.

## Trigger
`/learn [source]` — source can be: a book title, URL, article title, podcast name, repo URL, or free description.

## Protocol

### Step 1: Silent context load
Read `memory/MEMORY.md`. Check `knowledge/KNOWLEDGE-INDEX.md` to see if this topic already has a permanent entry — if so, note the existing entry for connection rather than duplication.

### Step 2: Elicit if needed
If the user has not provided enough to fill the template, ask:
- "What type of source is this? (book / article / course / repo / conversation)"
- "What's the core claim or insight from this source?"
- "How does it change how you think or act?"
One round of clarification only. Do not ask for what the user already provided.

### Step 3: Build the entry
Use `templates/learning-entry.md`. Fill all sections:
- `source_type`: classify accurately
- `consumed`: today's date
- `domain`: choose the most specific domain that fits
- `promote_by`: set to 7 days from today
- `promoted: false`
- Mental Model Update: this section is mandatory — force the before/after framing
- Promotion Candidates: identify at least one knowledge slug that this learning could become

### Step 4: Write the file
Filename convention: `YYYY-MM-DD-[short-slug].md`
Write to: `learning/<domain>/YYYY-MM-DD-<short-slug>.md`

### Step 5: Report
Tell the user:
- File path created
- The promote_by date
- The most important connection to existing knowledge (if found in index scan)
- Whether the topic already has a knowledge entry that should be updated instead of creating a new one

## Quality Bar
- Mental Model Update must be specific — "Before: X, After: Y" not "I now understand this better"
- Promotion Candidates must name a slug — not "maybe promote this"
- Critique section must have at least one substantive pushback

## Notes
- `learning/` is a staging area. Entries promoted to `knowledge/` get a `/promote` call.
- Entries not promoted within 30 days should be archived, not left to accumulate.
- If the source is a repository, prefer `/repo-learn` for deeper structured extraction.

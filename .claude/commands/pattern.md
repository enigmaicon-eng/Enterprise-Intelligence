# /pattern — Document a Recurring Pattern

Capture a recurring structure you've observed into the patterns library with full context/forces/solution form.

## Trigger
`/pattern [description]` — describe the recurring situation in natural language.

## When to Use
A pattern entry is warranted when:
- You've seen the same structure appear in at least 2 distinct situations
- The pattern has a non-obvious solution that you want to be able to recall
- The pattern crosses domains (appears in PM work AND technical work, for example)
- You can articulate both when to apply it AND when NOT to apply it

Do not create a pattern for a one-time observation. Use `/capture` for that.

## Protocol

### Step 1: Silent context load
Read `knowledge/patterns/index.md` to check if a similar pattern already exists. If so, ask whether to update the existing entry rather than create a new one.

### Step 2: Elicit if needed
If the user's description lacks enough to fill the template, ask:
- "What's the situation where this pattern applies?"
- "What's the specific action or approach that works?"
- "What breaks if you apply this pattern in the wrong context?"
One clarification round only.

### Step 3: Build the pattern
Use `templates/pattern-entry.md`. Required fields:
- **Pattern Statement**: "When [context], do [solution], because [outcome]." — must be one sentence
- **Forces**: at least 2 named tensions
- **Consequences**: both positive AND negative — patterns have costs
- **When NOT to Apply**: at least one clear counter-signal
- **Known Instances**: at least the 2 instances that prompted this capture
- **pattern_id**: assign as PAT-[YYYY]-[NNN] where NNN is sequential within the year

### Step 4: Write the file
Filename: `[pattern-slug].md`
Write to: `knowledge/patterns/[pattern-slug].md`

### Step 5: Update the index
Read `knowledge/patterns/index.md`. Add an entry:
```
| [pattern-slug] | [one-line description] | [domain] | [YYYY-MM-DD] |
```

### Step 6: Scan for connections
Check `knowledge/KNOWLEDGE-INDEX.md` for atomic concepts that relate to this pattern. Add `[[links]]` in the Connections section. If a linked note exists, add a back-reference to it.

### Step 7: Report
- File path
- Pattern ID assigned
- Any existing patterns it relates to
- Atomic concepts that should link to it

## Quality Bar
The pattern is not done if:
- The Pattern Statement doesn't have all three parts (when / do / because)
- Consequences only lists positives
- "When NOT to Apply" is empty
- Known Instances has fewer than 2 entries

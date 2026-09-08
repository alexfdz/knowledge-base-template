# AI Feedback Learning Loop

Process for AI agents to propose rule changes. Prevents silent rule drift between sessions.

## When to propose

- A correction during work that should be preserved project-wide.
- A pattern or constraint that recurs and isn't captured in the rules or the framework.
- A convention that turns out to be wrong or outdated.

Don't propose for one-off situations specific to a single task.

## Proposal format

```
## Rule Change Proposal

**Triggered by**: [What correction or learning surfaced this]
**Proposed rule**: [Exact text to add/change/remove]
**File**: [Which rule file — or kb-framework.md — this belongs in]
**Rationale**: [Why this is worth preserving project-wide]

Awaiting human approval before applying.
```

Include it inline in your response. Don't create files or modify rules until explicitly
approved.

## Constraints

- One proposal per session. If multiple corrections surface, log extras in `lessons-learned/`
  and propose one at a time.
- Never modify rule files (or `kb-framework.md`) without explicit human approval ("approved",
  "apply it", "go ahead").
- Silence or lack of objection is NOT approval.
- Link every proposal to a concrete learning, not a vague improvement.
- Changes to `kb-framework.md` are recorded in its §14 changelog.

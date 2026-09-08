# <External system> — context cache

> Last updated: YYYY-MM-DD
> **Scope:** static IDs only. **<System> is the source of truth** for anything that changes.
> This file exists so an agent doesn't re-query stable identifiers — nothing more.

## Static IDs

<Stable identifiers: board, lists, members, board/space IDs, etc.>

## Source-of-truth doctrine

- Mutable data (card state, dates, assignments, positions) → **query the tool directly, never
  this file**.
- **Do not update this file after mutations.** It caches structure, not state.
- Refresh it only when the static structure itself changes.

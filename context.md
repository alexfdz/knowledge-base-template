# Context — <Subject>

> Last updated: 2026-11-05
> Orientation note. First read to get situated; the detail lives in the domains and projects.
> No text in two places: only the summary and the pointers live here.

## What it is

<One paragraph: what this subject is, who it serves, why this KB exists. Link the anchor
resources with their `R-####` once created.>

## Governance / authority

<Who decides, and the authority ordering used to resolve conflicting decisions and opinions
(`kb-framework.md` §8) — e.g. a steering body overrides a working group, which overrides an
individual. Facts are not subject to authority. Point to the relevant domain page for detail.>

## Actors

Who can hold a task (`owner:`) and whom a task can wait on (`espera:`), per `kb-framework.md` §9.
Actors are roles and teams, never people: a task stays the same when the person changes, and the
**Now** column says whom to ask. Kind `fuera` (an outside party) only serves for `espera:`.
`make check` rejects an actor that is not in this table; to add one, add a row. The rows below
are examples: replace them with this subject's actors. To keep the table on another page (e.g. a
governance domain page), move it and point `ACTORS_PAGE` in `scripts/kb_tasks.py` there.

| Actor | Kind | What it is | Now |
|---|---|---|---|
| `@lead` | role | <Example: whoever steers the subject — a board, an owner> | <M-#### or —> |
| `@team` | team | <Example: a working group that holds work> | <M-####, M-####> |
| `@supplier` | fuera | <Example: an outside party a task can wait on> | — |

## Areas and projects

<The ongoing domains and the current projects, each with a one-line pointer to its page. Fill in
as they are created.>

## Current state

<Where things stand right now: what is active, what is paused, what is next.>

## Links

<Key external links (site, drives, boards). Anything durable also gets an `R-####` row.>

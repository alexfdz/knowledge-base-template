# <Subject> — Knowledge Base

A Second Brain for **<subject>**: the state of its ongoing areas, its people, and its large
recurring or one-off projects. It consolidates knowledge, decisions and pending tasks so it can
support decision-making and task management. Read by both humans and AI agents.

> Replace `<subject>` above and throughout this file with the thing this KB is about (an
> association, a company migration, a personal domain, a product…). See [`TEMPLATE.md`](TEMPLATE.md)
> to instantiate.

> **Privacy.** Decide per subject whether this repo is private. If it holds people's contact
> details or anything sensitive (see [`kb-framework.md`](kb-framework.md) §10, §13), keep it
> private and never publish it or reference its contents on a public surface.

## How to read this KB (routing)

Read in layers; never load everything.

1. **This file** → pick the domain or project below.
2. **Domain page** (`domains/`) or **project page** (`projects/`) — the curated interpretation
   layer. Read it whole; it's kept small on purpose.
3. **Registries** (`registry/`) — look up IDs by grep. **Never read a registry end-to-end**;
   rows exist to be cited, not read in bulk.
4. **The source resource** (chat thread, document, meeting notes) — only when the row/page isn't
   enough, via the `location` column.

Filtering: registry rows tag domain codes and project keys in the same column —
`rg "event-2026" registry/` answers "everything about that project"; `rg "OPS" registry/`
answers "everything in that domain".

## Rules

- **KB framework**: [`kb-framework.md`](kb-framework.md) — structure, borrowed standards,
  entity/ID model, task and people models. **Read before adding structure.**
- Project conventions: [`.claude/rules/base.md`](.claude/rules/base.md)
- Rule-change process: [`.claude/rules/ai-feedback-learning-loop.md`](.claude/rules/ai-feedback-learning-loop.md)
- Integrity: `make check` (runs `scripts/kb_check.py` as a `prek` hook) — duplicate IDs,
  dangling references and malformed tasks fail the commit.

## Knowledge domains

Ongoing areas (PARA "areas"). The domain page holds interpretation — what each resource means
*there*, and the detail behind open questions. Read the domain page before answering questions
in its area.

**None created yet.** Define your domains for this subject (cap 10 — `kb-framework.md` §3). For
each, copy [`templates/domain.md`](templates/domain.md) to `domains/<CODE>.md` (uppercase
mnemonic), then list it here as `- **`<CODE>`** [<Name>](domains/<CODE>.md) — <one line>`.

## Projects

Finite work with an outcome and an end. The page owns narrative, dependencies, allocation and
its own `## Tasks`. See the recurring-event pattern in `kb-framework.md` §11 (one domain + one
project per edition).

**None created yet.** For each project, copy [`templates/project.md`](templates/project.md) to
`projects/<key>.md` (kebab slug), then list it here as
`- **[<key>](projects/<key>.md)** — <one line> — <status>`.

## Teams

Optional: one page per working group that needs its own, in [`teams/`](teams/) (`WG-<CODE>`):
what it does, people, channels, state and needs, processes, its own `## Tasks`. Status `active` ·
`at-risk` · `inactive` · `closed`. Copy [`templates/team.md`](templates/team.md) to
`teams/WG-<CODE>.md`, then list it here.

**None created yet.**

## Reports

Optional: recurring reports, each with a contract in [`reports/`](reports/) — audience, period,
content, sources, procedure, format, privacy — and its issues in `reports/<key>/YYYY-MM-DD.md`.
Write every issue from its contract; change the contract first when an issue needs something
else. List each one here as `- **`<key>`** [<Title>](reports/<key>.md) — <status> · <one line>`.

**None created yet.**

## Registries

Cross-domain, append-only. Facts live here; interpretation lives on the domain page.

- **Resources**: [`registry/resources.md`](registry/resources.md) — `R-####` every doc, deck,
  thread, meeting.
- **Decisions**: [`registry/decisions.md`](registry/decisions.md) — `D-####` immutable,
  superseded not edited.
- **Findings**: [`registry/findings.md`](registry/findings.md) — `F-####` facts about the world,
  not choices.
- **Questions**: [`registry/questions.md`](registry/questions.md) — `Q-####` open items with
  owners.
- **People**: [`registry/people.md`](registry/people.md) — `M-####` members, contacts,
  collaborators, stakeholders.
- **Ideas**: [`registry/ideas.md`](registry/ideas.md) — `I-####` goals, ideas to try and
  proposals, before anyone decides. When one is decided, its row links the `D-####`.

## Reference

- **Context**: [`context.md`](context.md) — the current state of the subject (orientation), and
  the governance-authority ordering (`kb-framework.md` §8).
- **Sources & access**: [`sources.md`](sources.md) — how to reach every external source (what
  it is, owner, tool, auth, gotchas). Its sensitive half (passwords, tokens, 2FA) lives in
  `sources.local.md`: gitignored, local only, same section per source, created from
  [`templates/sources-local.md`](templates/sources-local.md). Read it only when a task needs a
  credential; never copy its values into a tracked file or into output.
- **Glossary**: [`glossary.md`](glossary.md) — terms and controlled vocabulary.

## Knowledge capture

Every capture file gets an `R-####` row — a file without a registry row is invisible.

- **Meetings**: [`meetings/`](meetings/) — notes per meeting (Conclusions → Actions →
  Decisions → Resources). Filename `YYYY-MM-DD-topic.md`.
- **Lessons learned**: [`lessons-learned/`](lessons-learned/) — learnings and living retros.
- **Journal**: [`journal/`](journal/) — running personal log (and quick untriaged notes), `YYYY-MM-DD.md`.
- **Raw**: [`raw/`](raw/) — source material as it arrived (transcripts, chat exports,
  documents). Never credentials. Every file hangs from an `R-####` row. It is the original source,
  not the reading layer: read it only when the page or the note is not enough.
- **Templates**: [`templates/`](templates/) — skeletons for every file type.

## Tasks

No external tracker. Tasks are in-KB checkboxes under `## Tasks` in the relevant page
(`kb-framework.md` §9). The box is the state: `[ ]` pendiente · `[/]` en marcha · `[x]` hecha ·
`[-]` descartada. Each task has `plazo`, `complejidad` and `fuente` (where it came from:
`reunión R-####`, `whatsapp R-####`, `mail <box>@ sin-leer|leído`, `drive <account>@`,
`form <account>@`, `idea I-####`, `hallazgo F-####`, `decisión D-####`); `owner` with one or more
**actors** — roles and teams, never people, from the table in [`context.md`](context.md) →
Actors; optional `espera` (the actor or date an open task waits for) and `tags`; and optional
`Contexto` / `Propuesta` / `Enlace` sub-bullets. Its history is its dated `Contexto (YYYY-MM-DD):`
lines, each with its source; a line that changes the state starts with the new one (`→ hecha.`).
Priority is the deterministic matrix in `kb-framework.md` §9 — something urgent gets a `plazo`.
Run `make todos` for the ranked open-task list (filters: `FUENTE=mail`, `ACTOR=@lead`,
`TAG=venue`). `make roadmap` builds `roadmap.html` (projects, a month calendar, a view per actor,
"your turn", every open task with filters, and the open questions); it is gitignored and
regenerated, never edited.

## Rigor

- Confirm hypotheses against real sources before recording them as findings.
- Use `glossary.md` terms consistently.
- Never create a link to a file that doesn't exist; never create an empty note to satisfy a
  reference (`kb-framework.md` §12).

## Language

Structure, filenames, field names and templates are in **English** (the task tokens — `plazo`,
`complejidad`, `espera`, `fuente`, the box state names, the `fuente` vocabulary and the actor kind
`fuera` — are the exception: the tooling parses them literally). Choose one language for the
subject content (domain pages, decisions, meeting notes, glossary definitions) and use it
consistently; record the choice here.

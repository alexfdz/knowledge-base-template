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
- Integrity: `make check` (runs `scripts/kb_check.py` as a `prek` hook) — duplicate IDs and
  dangling references fail the commit.

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

## Reference

- **Context**: [`context.md`](context.md) — the current state of the subject (orientation), and
  the governance-authority ordering (`kb-framework.md` §8).
- **Sources & access**: [`sources.md`](sources.md) — how to reach every external source (tool,
  auth, gotchas). Secrets live in a gitignored `.env`, never here.
- **Glossary**: [`glossary.md`](glossary.md) — terms and controlled vocabulary.

## Knowledge capture

Every capture file gets an `R-####` row — a file without a registry row is invisible.

- **Meetings**: [`meetings/`](meetings/) — notes per meeting (Conclusions → Actions →
  Decisions → Resources). Filename `YYYY-MM-DD-topic.md`.
- **Lessons learned**: [`lessons-learned/`](lessons-learned/) — learnings and living retros.
- **Journal**: [`journal/`](journal/) — running personal log (and quick untriaged notes), `YYYY-MM-DD.md`.
- **Templates**: [`templates/`](templates/) — skeletons for every file type.

## Tasks

No external tracker. Tasks are in-KB checkboxes under `## Tasks` in the relevant page, each with
`plazo` and `complejidad`; priority is the deterministic matrix in `kb-framework.md` §9. Run
`make todos` for the ranked open-task list.

## Rigor

- Confirm hypotheses against real sources before recording them as findings.
- Use `glossary.md` terms consistently.
- Never create a link to a file that doesn't exist; never create an empty note to satisfy a
  reference (`kb-framework.md` §12).

## Language

Structure, filenames, field names and templates are in **English** (the task field tokens
`plazo`/`complejidad` are the exception — the tooling parses them literally). Choose one language
for the subject content (domain pages, decisions, meeting notes, glossary definitions) and use it
consistently; record the choice here.

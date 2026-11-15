# Second Brain KB — Template

A reusable **Second Brain / Knowledge Base** scaffold. Copy this folder to start a new KB about
any subject — an association, a company migration, a personal domain, a product, a research
effort. It consolidates knowledge, decisions and pending tasks for both humans and AI agents.

> New here? Read [`TEMPLATE.md`](TEMPLATE.md) first — it walks through instantiating this
> template. Then read [`kb-framework.md`](kb-framework.md) for the model.

> **Privacy** — decide per subject. If the KB will hold people's contact details or anything
> sensitive, keep the repo private and never publish it.

## Structure

| Layer | Where | What |
|-------|-------|------|
| Framework | [kb-framework.md](kb-framework.md) | How the KB is organized; borrowed standards (PARA, ADR/MADR, Dublin Core, Johnny.Decimal cap); entity/ID, task and people models. **Read before adding structure** |
| Domains | [domains/](domains/) | Ongoing areas — one page each, the interpretation layer (cap 10) |
| Projects | [projects/](projects/) | Finite work — narrative, dependencies, allocation, tasks |
| Registries | [registry/](registry/) | Append-only: `R-####` resources · `D-####` decisions · `F-####` findings · `Q-####` questions · `M-####` people · `I-####` ideas and goals |
| People | [people/](people/) | Optional per-person notes · [trackers/](people/trackers/) outreach funnels |
| Teams | [teams/](teams/) | Optional working-group pages (`WG-<CODE>`): status, people, channels, needs |
| Capture | [meetings/](meetings/) · [lessons-learned/](lessons-learned/) · [journal/](journal/) · [raw/](raw/) | Meeting notes, learnings, the running log and raw material (transcripts, chat exports, documents); every capture file gets an `R-####` row |
| Reports | [reports/](reports/) | Optional recurring reports: one contract per report (who it is for, what it carries, where it comes from, how it is made) and one file per issue |
| Reference | [context.md](context.md) · [sources.md](sources.md) · [glossary.md](glossary.md) | Current state of the subject and its actors; how to reach external sources (auth, gotchas; credentials in the untracked `sources.local.md`); terms and controlled vocabulary |
| Templates and tools | [templates/](templates/) · [scripts/](scripts/) · [.claude/](.claude/) | Skeleton for every file type; checks and views; rules (and skills) for agents |

## Tasks

No external tracker — tasks are in-KB checkboxes with a state (`[ ]` pendiente, `[/]` en
marcha, `[x]` hecha, `[-]` descartada), `plazo`, `complejidad`, `owner` (one or more actors: roles
and teams, never people), optional `espera` and `tags`, and `fuente`, with their history in dated
`Contexto (YYYY-MM-DD)` lines; they are prioritized by a deterministic matrix (see
[kb-framework.md](kb-framework.md) §9). `make todos` prints the ranked open-task list (filters
`FUENTE=`, `ACTOR=`, `TAG=`).

## Integrity

`make check` — duplicate-ID, dangling-reference and task check (`scripts/kb_check.py`), wired as
a `prek` pre-commit hook.

```sh
prek install     # once per clone
make check       # run the integrity check
make stats       # counts per entity type
make todos       # ranked open tasks across the KB
make roadmap     # roadmap.html: projects, calendar and open tasks with filters
```

## LLM context

`CLAUDE.md` is the entry point for AI agents — including the routing rules (layered reads, grep
the registries, never bulk-read them). `AGENTS.md` and `GEMINI.md` are symlinks to it.

## Language

Structure and templates are in English; pick one language for the subject content and use it
consistently (see `CLAUDE.md` → Language).

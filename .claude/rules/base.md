# Project Rules

## Purpose

This repo is a knowledge base (Second Brain) for a single subject. Not a codebase — the only
"tooling" is the integrity check and the Makefile. Documents, decisions, meeting notes, people,
and reference material.

## Documentation conventions

- **Structure in English; content in one chosen language.** Filenames, folder names, field
  names, table headers and templates are English. Pick one language for the subject content
  (domain pages, decisions, meeting notes, glossary definitions) and use it consistently; record
  the choice in `CLAUDE.md` → Language.
- Use terms from `glossary.md` consistently.
- Date format: `YYYY-MM-DD` everywhere.
- Every document has a `> Last updated: YYYY-MM-DD` line under its `# Title`.
- Metadata is a **blockquote header** under the title, not YAML frontmatter (see
  `kb-framework.md` §13).

## File organization

- Meeting notes: `meetings/YYYY-MM-DD-topic.md`
- Lessons / retros: `lessons-learned/YYYY-MM-DD-topic.md` (living retros may drop the date)
- Journal: `journal/YYYY-MM-DD.md`
- Domain pages: `domains/<CODE>.md` (uppercase mnemonic)
- Project pages: `projects/<key>.md` (kebab slug, e.g. `event-2026`)
- Person notes: `people/<slug>.md` · trackers: `people/trackers/<campaign>.md`
- Filenames are kebab-case, lowercase, ASCII (no accents), except uppercase domain codes and
  the convention files (`README.md`, `CLAUDE.md`, …).
- Empty directories keep a `.gitkeep`.

## IDs and links

- Registry IDs: `R-`/`D-`/`F-`/`Q-`/`M-` + 4 digits, opaque, permanent, never reused.
- Reference other notes by **Markdown relative link** and cite entities by **ID**. No wikilinks.
- **Never create a link to a file that doesn't exist. Never create an empty note just to satisfy
  a reference.** A dangling reference is a `make check` failure to fix at the source, not to
  paper over with a stub.

## Knowledge quality

- Verify a claim before recording it as a **finding**; findings carry evidence.
- Distinguish decisions (a choice, reversible) from findings (a fact, disprovable) — see
  `kb-framework.md` §6.
- New term or acronym → add it to `glossary.md`.
- Record decisions that were **rejected** too (`wont-do`), not only the ones taken.

## Tasks

- In-KB checkboxes under `## Tasks`, each with `plazo` and `complejidad` (`kb-framework.md` §9).
- Priority is the deterministic matrix, not judgement. `make todos` regenerates the ranked list.

## Rule changes

See `ai-feedback-learning-loop.md` for how to propose changes to these rules.

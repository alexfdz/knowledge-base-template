# Instantiating this template

This folder is a **subject-agnostic Second Brain / Knowledge Base template**. Copy it, then make
it about your subject. Nothing here is tied to a particular organization or topic — you fill that
in. Read [`kb-framework.md`](kb-framework.md) for the model behind the structure.

## Steps

1. **Copy the folder** to your new KB location and `git init` it (the integrity check relies on
   `git ls-files`).
2. **Name the subject.** In [`CLAUDE.md`](CLAUDE.md) and [`README.md`](README.md), replace every
   `<subject>` / `<Subject>` placeholder with what this KB is about, and fill in the intro.
   Fill in [`context.md`](context.md) with the current state and the governance-authority
   ordering (`kb-framework.md` §8). Start [`sources.md`](sources.md) the first time you connect
   an external tool — record its auth and gotchas there; the secret goes in the gitignored
   `sources.local.md` (copy [`templates/sources-local.md`](templates/sources-local.md)).
3. **Decide privacy.** If the KB will hold contact details or anything sensitive, keep the repo
   private and note it in `CLAUDE.md` (`kb-framework.md` §10, §13).
4. **Pick the content language.** Structure stays English; choose one language for the subject
   content and record it in `CLAUDE.md` → Language. (The task tokens — `plazo`, `complejidad`,
   `espera`, `fuente`, the box states, the `fuente` vocabulary and the actor kind `fuera` — are
   kept verbatim: the tooling parses them.)
5. **Define your domains** (ongoing areas, **cap 10** — `kb-framework.md` §3). For each, copy
   [`templates/domain.md`](templates/domain.md) to `domains/<CODE>.md` and list it under
   *Knowledge domains* in `CLAUDE.md`.
6. **Add projects** as finite work starts. Copy [`templates/project.md`](templates/project.md)
   to `projects/<key>.md` and list it under *Projects* in `CLAUDE.md`. For recurring events, use
   the one-domain-plus-one-project-per-edition pattern (`kb-framework.md` §11). Working groups
   that need their own page get one from [`templates/team.md`](templates/team.md) in `teams/`.
7. **Define the actors.** Tasks are owned by actors — roles and teams, never people
   (`kb-framework.md` §9). Replace the example rows of the **Actors** table in
   [`context.md`](context.md) with this subject's actors; `make check` rejects an `owner` or
   `espera` that is not in it. To keep the table on another page (e.g. a governance domain page),
   move it and set `ACTORS_PAGE` in `scripts/kb_tasks.py` to that page. Once you have a row in
   the people registry, set `OWNER` in `scripts/kb_roadmap.py` to your `M-####` so `make roadmap`
   marks the actors you fill and shows "your turn". The roadmap page's UI text
   (`scripts/kb_roadmap.html`) is in Spanish; translate it if your content language differs.
8. **Start capturing.** Every doc, deck, thread or meeting gets a row in the relevant registry
   (`registry/*.md`) with the next sequential ID (`R-####`, `D-####`, `F-####`, `Q-####`,
   `M-####`, `I-####`). Interpretation goes on the domain page, not the registry
   (`kb-framework.md` §7).
9. **Stage, install the hook, check integrity.**

   ```sh
   git add -A       # the integrity check reads `git ls-files`, so stage first
   prek install     # once per clone — runs the integrity check on commit
   make check       # duplicate IDs, dangling references, tasks — must print: kb-check: OK
   make stats       # counts per entity type
   make todos       # ranked open tasks across the KB
   make roadmap     # roadmap.html with projects, calendar and tasks (opens it with macOS `open`)
   ```

## What stays, what you change

- **Do not change** the model or the tooling: `kb-framework.md` §1–§14, `scripts/` (except the
  two settings in step 7, `ACTORS_PAGE` and `OWNER`), `Makefile`, `.pre-commit-config.yaml`, the
  registry column shapes, the ID scheme. Framework changes follow
  the process in [`.claude/rules/ai-feedback-learning-loop.md`](.claude/rules/ai-feedback-learning-loop.md)
  and are recorded in `kb-framework.md` §14.
- **You fill in:** the subject (`CLAUDE.md`, `README.md`, `context.md`), the actors,
  `sources.md` as you connect external tools, the domains, the projects, the teams, the glossary,
  the people, and every registry row.
- You can delete this `TEMPLATE.md` once the KB is instantiated.

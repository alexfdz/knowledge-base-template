# KB Framework

> Last updated: 2026-11-15
> Status: **template** — reusable scaffolding for a Second Brain knowledge base

How this knowledge base is organized, which established frameworks it borrows from, and what
it deliberately rejects. Read this before adding structure. For *what* is in the KB, start at
[`CLAUDE.md`](CLAUDE.md).

This KB is a **Second Brain** — a single place that consolidates the knowledge, decisions and
pending tasks about one subject: its ongoing areas, its people, and its large recurring or
one-off projects. The subject can be anything — an association, a company migration, a personal
domain, a product, a research effort. Name the subject in [`CLAUDE.md`](CLAUDE.md) and
[`context.md`](context.md); the model below is the same regardless of subject. It is read by
both humans and AI agents.

---

## §1 Why borrow at all

Structure invented from scratch tends to be re-invented, badly, every time the KB grows. The
rule: **check for an existing standard before inventing structure.** Borrowed structure is
documented externally, so a collaborator can look it up instead of learning our invention.

We take pieces, not whole systems. Each section below states **what we take**, **what we
reject**, and **why** — the "why" matters most, because it tells a future reader whether a
deviation was deliberate or accidental.

---

## §2 PARA — the top-level shape

[PARA](https://fortelabs.com/blog/para/) (Tiago Forte): everything is a **Project**, an
**Area**, a **Resource**, or an **Archive**.

**What we take — the four buckets and, more importantly, the test that sorts them.**

| PARA | Our name | Test | Example |
|---|---|---|---|
| Area | **Domain** | Ongoing. No end date. | Governance, operations, community |
| Project | **Project** | Finite. Has an outcome and an end. | This year's edition of a recurring event |
| Resource | **Resource** | Reference material about anything. | A deck, a chat thread, meeting notes, a policy document |
| Archive | *status field* | No longer active. | A superseded decision, a closed project |

**Why the test matters.** It decides the arguments we would otherwise have by taste. "Is the
annual event a domain?" The *program* (brand, format, accumulated know-how) is ongoing, so it is
a domain; *this year's edition* ends, so it is a project. Same test settles every future case.

**What we reject.** PARA's Archive-as-a-folder. Moving files on retirement breaks every link
pointing at them. We use a **`status` field in place** instead — nothing ever moves, nothing
404s.

**Beyond the four buckets**, a few working folders each have one job: `teams/` (§6); the capture
layer, `meetings/`, `lessons-learned/`, `journal/` and `raw/` (the source as it arrived:
transcripts, chat exports, documents; every file hangs from its `R-####` row, and never holds
credentials); `reports/` (recurring reports: one contract per report, saying who it is for, what
it carries, where it comes from and how it is made, and one file per issue); `templates/`;
`scripts/` (checks, views and source readers); and `.claude/` (the rules and the agent skills).

---

## §3 Johnny.Decimal — the cap only, not the notation

[Johnny.Decimal](https://johnnydecimal.com/): at most 10 areas × 10 categories, everything
addressable as `AC.ID`.

**What we take: the cap.** Domains are capped at **10**, and adding one is a deliberate
decision recorded in the changelog (§14). Domain sprawl is the main way a KB like this rots —
you end up with 40 overlapping areas and no idea where anything belongs.

**What we reject: the `AC.ID` notation itself.** Johnny.Decimal assumes **each item has exactly
one home**. Our central requirement is the opposite — a resource can belong to several domains
at once. Flat type-prefixed IDs plus domain tags express many-to-many honestly; `AC.ID` cannot.

---

## §4 ADR / MADR — decisions

[ADR](https://adr.github.io/madr/) (Nygard 2011, MADR variant): sequential IDs, a status
lifecycle, and — the important part — **decisions are immutable**. You never edit a decision.
You write a new one that supersedes it.

**What we take:**
- Sequential 4-digit IDs, never reused.
- Status lifecycle: `proposed` → `accepted` → `superseded` / `reversed` / `wont-do`.
- **Immutability by supersession.** A superseded decision keeps its row with `status:
  superseded` and `superseded-by: D-0042`. The replacement gets a new ID and `supersedes:
  D-0007`.
- From MADR: record the **drivers** and the **options considered**, not just the outcome. A
  decision without its alternatives can't be re-evaluated later. **Record decisions that were
  rejected too** — "we decided *not* to do X" is knowledge that otherwise disappears.

**Why immutability specifically.** "What did we decide, and why did it change" is the question
asked at any handover — a new board, a new owner, a new maintainer inheriting the subject.
Edit-in-place destroys exactly that trail.

**What we reject: one file per decision.** ADR convention is one `.md` per decision. At any
real volume that becomes hundreds of files nobody scans. We keep **append-only rows in a single
registry**, which preserves immutability and history while staying readable in one view.

---

## §5 Dublin Core — the resource registry schema

[Dublin Core](https://www.dublincore.org/dces) (ISO 15836): fifteen elements for describing any
resource.

**What we take — a named subset**, so our columns are a recognized shape rather than ad-hoc
invention:

| Our column | Dublin Core | Notes |
|---|---|---|
| `id` | Identifier | `R-0001`, ours, permanent |
| `title` | Title | |
| `author` | Creator | Person or working group |
| `date` | Date | Creation or last substantive change (`YYYY-MM-DD`) |
| `kind` | Type | `doc` · `deck` · `sheet` · `chat-thread` · `meeting` · `transcript` · `email` · `repo` · `dataset` · `web` · `form` |
| `domains` | Subject | Domain tags + project keys — **tags only, no prose** (see §7) |
| `relations` | Relation | See §8 |
| `location` | Source | URL, chat link, file path, or drive ID |

**Why.** Free choice of columns drifts; a standard subset doesn't. **What we reject:** the other
seven elements until something actually needs them. Empty columns train people to ignore
columns.

**Where to *reach* a source** — the CLI, the auth, the gotchas — is a different layer from the
registry and lives in [`sources.md`](sources.md). The registry's `location` says *where* a
resource is; `sources.md` says *how to get in* (tool, account, how secrets are loaded, and the
hard-won operational hazards).

Keep secrets out of both. Each source's sensitive half — credentials, 2FA and recovery data,
links that grant access on their own — lives in a gitignored `sources.local.md` under the same
heading as in `sources.md`, created from
[`templates/sources-local.md`](templates/sources-local.md); a `prek` hook blocks committing any
`*.local.md`. Secrets an automation loads go in a gitignored `.env`, read by the script so the
value never passes through an agent's session. `sources.md` defines what counts as sensitive.

---

## §6 Entity model

| Entity | Identifier | Registry | Notes |
|---|---|---|---|
| **Domain** | mnemonic — `OPS`, `FIN` | `domains/<code>.md` | Max 10. Code frozen even if the display name changes |
| **Project** | readable key — `event-2026` | `projects/<key>.md` | Finite work; key is a stable kebab slug |
| **Resource** | `R-0001` | `registry/resources.md` | Cross-domain by design |
| **Decision** | `D-0001` | `registry/decisions.md` | Append-only, status lifecycle |
| **Finding** | `F-0001` | `registry/findings.md` | `established` · `disputed` · `disproved` |
| **Question** | `Q-0001` | `registry/questions.md` | `open` · `answered` · `dropped` |
| **Person** | `M-0001` | `registry/people.md` | Members, contacts, collaborators, stakeholders — see §10 |
| **Idea** | `I-0001` | `registry/ideas.md` | A goal, an idea to try or a proposal — see below |
| **Team / Working group** | short code — `WG-OPS` | `teams/<code>.md` | Optional; only when a group needs its own page. From `templates/team.md` |
| **Task** | *none* | in the relevant page | In-KB checkboxes, see §9 |

**Registry IDs are opaque and permanent.** Nothing mutable is encoded in them — no dates,
owners, status or domain, because all of those change and the ID must not. Uniform 4-digit
padding. **A retired ID is never reused.** (Project keys are the exception: they are readable
because projects are few, finite and human-referenced — but they are still never reused.)

### Decisions vs Findings — why they are separate types

A **decision** is a choice someone made and can reverse; it has a *decider* and follows the
governance authority in §8. A **finding** is something true about the world; it has *evidence*,
you don't reverse it, you disprove it, and the person with direct knowledge is authoritative
regardless of role.

*"The next edition moves to a two-track format"* is a decision. *"The main venue holds 220
people"* is a finding. Conflating them is how a settled decision starts looking like an open
debate — and how an observed fact gets overruled by someone with more authority who hasn't
checked.

### Ideas — what someone wants, before anyone decides

An **idea** is something a person wants to achieve or try: a `goal` (an outcome being pursued),
an `idea` (something to test) or a `proposal` (something to take to the governing body). It is not
a decision — nobody has chosen yet — and not a task — it is not yet work. Brainstorms, personal
reflections and "we should…" in a chat land here, numbered, so projects and tasks can cite them.
When an idea is decided, its row links the resulting `D-####`; tasks that come from it cite it in
their `fuente` (§9).

---

## §7 Where interpretation lives

The same resource means different things in different domains. So:

- **The registry holds facts and tags only** — `domains: OPS, FIN`. This makes "every resource
  touching `OPS`" a mechanical lookup (`rg "OPS" registry/`).
- **The domain page holds the prose** — what this resource means *here*, under its ID:

```
### R-0042 — Pricing tiers deck
Applies here as: the pricing frame for the 2026 edition (see event-2026).
Supports D-0012. Contradicts the assumption in R-0055 → Q-0004.
```

The same resource on another domain's page gets a **different paragraph**, because it means
something different there. Each paragraph is written once, where it is used. **No text appears in
two places** — that is the rule that keeps this maintainable.

---

## §8 Controlled vocabularies

Small on purpose. Vocabularies nobody can remember are vocabularies nobody applies.

**Relations** (Dublin Core / W3C PROV equivalents in brackets): `supersedes` / `superseded-by`
[replaces / isReplacedBy] · `contradicts` · `supports` · `derived-from` [wasDerivedFrom] ·
`responds-to` [references] · `duplicates`

**Status** — Decision: `proposed` · `accepted` · `superseded` · `reversed` · `wont-do`.
Question: `open` · `answered` · `dropped`. Finding: `established` · `disputed` · `disproved`.
Project: `shaping` · `active` · `paused` · `done` · `cancelled`. Person: `active` · `prospect`
· `lapsed` · `alumnus`. Idea: `open` · `in-progress` · `done` · `dropped`. Task (the box, §9):
`[ ]` pendiente · `[/]` en marcha · `[x]` hecha · `[-]` descartada.

**Governance authority** for conflicting *decisions and opinions* (not facts — those are
findings): follows the authority ordering this KB defines for its subject. Record that ordering
in [`context.md`](context.md) — e.g. a steering body overrides a working group, which overrides
an individual's position. A higher authority overrides a lower one. Record who decided on every
`D-####` row. Facts are never subject to authority: a finding is settled by evidence, not by
rank.

---

## §9 Tasks — in-KB TODOs with a deterministic priority

There is no external tracker. Tasks live **in the page they belong to** (a project page, a
domain page, a team page) under a `## Tasks` heading, as checkboxes:

```
- [/] Confirm the venue deposit deadline | plazo: 2026-09-15 | complejidad: low | owner: @treasury, @events | espera: @supplier | tags: venue | fuente: mail info@ sin-leer
  - Contexto: the venue asked twice; the deposit secures the date.
  - Propuesta: call them and pay by transfer.
  - Enlace: [thread](https://mail.example.com/…)
  - Contexto (2026-09-02): → en marcha. The treasurer asked for the invoice (mail info@ leído).
  - Contexto (2026-09-05): → espera @supplier. The invoice has not arrived.
- [x] Draft the announcement | plazo: 2026-09-01 | complejidad: medium | owner: @comms | fuente: reunión R-0012
  - Contexto (2026-08-30): → hecha. Sent to the members (whatsapp R-0013).
```

**State is the box**, with the Obsidian Tasks convention, which any markdown viewer still shows
as a checkbox:

| Box | State | Meaning |
|---|---|---|
| `[ ]` | pendiente | open; nobody is on it yet |
| `[/]` | en marcha | open; someone is on it |
| `[x]` | hecha | done |
| `[-]` | descartada | dropped: no longer needed, or decided against |

**Fields** follow the text, separated by ` | `:

- **`plazo`** (due date, `YYYY-MM-DD` or `—`) and **`complejidad`** (`low` · `medium` · `high`),
  always. These two names are the literal tokens `make todos` (`scripts/kb_todos.py`) parses —
  keep them verbatim.
- **`owner`** — who holds the task: one or more **actors**, comma-separated. An actor is a role or
  a team, never a person, so a task survives a change of people. The subject defines its actors in
  one table, with who fills each one now (in this template: [`context.md`](context.md) → Actors,
  the page `ACTORS_PAGE` in `scripts/kb_tasks.py` names); outside parties (kind `fuera`) are
  actors too, but only for `espera`.
- **`espera`** — optional: what an open task is waiting for, as one actor (inside or outside) or a
  date (waiting until then). Waiting is not a state: a task can be `[ ]` or `[/]` and waiting.
  This field is what builds the "your turn" and "waiting on" views.
- **`tags`** — optional: topics, lowercase and comma-separated, to cut across pages (a task in the
  events domain tagged `venue`, `budget`).
- **`fuente`** — where the task came from, so it can be checked against its origin, filtered, and
  closed with context. Vocabulary (several sources, comma-separated):

| `fuente` | When |
|---|---|
| `reunión R-####` | A meeting's notes or transcript |
| `whatsapp R-####` · `whatsapp <group>` | A chat; the group name when the chat has no `R-####` row yet |
| `mail <box>@ sin-leer` · `mail <box>@ leído` | An email thread, and whether it was still unread when the task was taken; the thread link goes in `Enlace` |
| `drive <account>@` · `form <account>@` | A document or a comment in it, or new answers to a form; the link goes in `Enlace` |
| `idea I-####` | An idea or goal from the ideas registry (§6) |
| `hallazgo F-####` · `decisión D-####` | The KB's own analysis: a finding or a decision that implies work |

Optional sub-bullets under a task hold what the one-liner can't: **`Contexto`** (what happened and
why it matters), **`Propuesta`** (the proposed solution) and **`Enlace`** (links to the source).

**The history lives in the task.** Each dated **`Contexto (YYYY-MM-DD):`** line is one step,
appended in date order and never rewritten; it ends with where it was seen, in brackets, in the
`fuente` vocabulary. A step that changes the state starts with the new one: `→ en marcha.`,
`→ espera @actor.`, `→ pendiente.` (no longer waiting), `→ hecha.`, `→ descartada.` The box says
how the task is now, the dated lines say how it got there, and git keeps every edit. There is no
separate log and no second copy of the state: views are generated from the tasks.

**Views.** `make todos` lists the open tasks (`[ ]` and `[/]`) by the matrix below and filters by
source, actor or tag (`FUENTE=mail`, `ACTOR=@treasury`, `TAG=venue`). `make roadmap` builds a page
with the same tasks, a view per actor and a "your turn" list for the actors the KB's owner holds
(`OWNER` in `scripts/kb_roadmap.py`). Done and dropped tasks stay in their page, with their
history, and no view lists them.

**Checks.** `make check` fails on a box other than the four, a `plazo` that is neither a date nor
`—`, a missing `complejidad`, an unknown field, an `owner` that is not an actor that can hold work,
or an `espera` that is neither an actor nor a date.

When an agent or human aggregates open
tasks across pages, they are ordered by a **deterministic priority matrix** — earliest deadline
first, then lowest complexity first (so quick wins clear ahead of slow work with the same
deadline):

| Rank | plazo | complejidad |
|------|-------|-------------|
| 1 | overdue / soonest | low |
| 2 | overdue / soonest | medium |
| 3 | overdue / soonest | high |
| … | next deadline | low → medium → high |
| last | no `plazo` | low → medium → high |

**Why a matrix and not agent judgement.** Priority becomes reproducible and auditable: two
different sessions produce the same ordering, and the reasoning is inspectable. `make todos`
regenerates the ranked list on demand — the list is never stored, so it never goes stale. There is
no separate priority field: something urgent gets a `plazo`, which is what moves it up.

Tasks get **no ID and no registry**. They are cheap, disposable and completion-tracked by the
checkbox. Anything durable a task produces (a decision, a finding, a resource) *does* get an ID.

---

## §10 People, trackers and roles

In most subjects people are central — an association's members, a company's staff, a project's
stakeholders, a personal network of contacts — so people are a first-class entity with a
registry (`registry/people.md`, `M-####`).

- **The people registry** holds the stable facts: name, role(s), status (§8), contact, and a
  one-line note. If this KB is private, contact details can live here on that basis (§13).
- **Roles** are a small controlled set, extended by recording a decision. Start from a neutral
  default — `lead` · `contributor` · `stakeholder` · `contact` · `partner` — and redefine it for
  your subject. A person can hold several.
- **Per-person notes** (`people/<slug>.md`) are optional — created only when someone accumulates
  enough context to warrant a page. Most people are just a registry row.
- **Funnel trackers** (`people/trackers/`) model *campaigns* — outreach, recruitment, onboarding
  — as a state machine: one row per person, one column per funnel stage, a summary block with
  aggregate counts. Each state change is a git commit, so the history is auditable. Template:
  [`templates/person-tracker.md`](templates/person-tracker.md).

---

## §11 Projects and the recurring-event pattern

A **project** is finite work with an outcome and an end. Its page carries the narrative the task
list can't hold: **why it exists, which domains it draws on, which decisions it depends on, its
allocation of people, and its own `## Tasks`**.

**The recurring-event pattern.** Anything that repeats on a cycle — an annual event, a quarterly
release, a recurring campaign — is modelled as **one domain + one project per edition**:

- The **domain** (e.g. `EVENT`) holds what carries across editions: the brand, the format
  decisions, the accumulated know-how, the *living retro* that feeds the next edition.
- Each **edition** (e.g. `projects/event-2026.md`) is a project: this cycle's venue, budget,
  scope, people, tasks. When it closes, its status becomes `done` and its lessons flow up into
  the domain and into `lessons-learned/`.

This way each edition does not start from zero, and the retro is written *during* the cycle, not
as a forgotten post-mortem.

---

## §12 Rules of the road

1. **Check for a standard before inventing structure.** §1.
2. **Never delete; supersede.** Decisions, findings and questions keep their IDs forever. §4.
3. **Never reuse an ID.**
4. **Nothing mutable in a registry ID.** §6.
5. **No text in two places.** Facts in the registry, interpretation on the domain page. §7.
6. **Every capture gets an `R-####` row.** A file without a registry row is invisible.
7. **Cap domains at 10.** Adding one is a recorded decision. §3.
8. **Governance authority applies to decisions and opinions, not to observed facts.** §8.
9. **Never create a link to a file that does not exist**, and **never create an empty note just
   to satisfy a reference.** A dangling reference is a `make check` failure, not a stub to paper
   over.

---

## §13 What we deliberately do not do

| Not doing | Why |
|---|---|
| One file per decision | Hundreds of files nobody scans. §4. |
| Johnny.Decimal `AC.ID` | Assumes one home per item; our resources are cross-domain. §3. |
| Moving retired content to an archive folder | Breaks links. Use `status`. §2. |
| Wikilinks `[[...]]` | We use Markdown relative links + ID citation + `make check`. Robust for agents; the repo still opens as a plain Obsidian vault. |
| An external task tracker | The Second Brain stays self-contained; tasks are in-KB checkboxes (§9). A project *may* link out to a board your team runs, but state is never mirrored — that would create two sources of truth. |
| YAML/JSON registries | Markdown stays readable and diffable in review; this KB is read by humans and agents, not parsed by services. |
| A public repo by default | If the KB holds people's contact details or anything sensitive (§10), **keep it private**. Decide this per subject and record it in `CLAUDE.md`. |
| Secrets in git, even in a private repo | A private repo is not a secret store: every clone, fork, backup and agent with repo access gets a copy, and git history keeps a leaked value after it is deleted. Credentials stay in gitignored files (§5). |

---

## §14 Changing this framework

The framework follows the same rule as the rules files: propose, get explicit approval, then
apply. See [`.claude/rules/ai-feedback-learning-loop.md`](.claude/rules/ai-feedback-learning-loop.md).
Record framework changes below.

| Date | Change |
|------|--------|
| 2026-08-27 | Template created. Borrows from PARA (§2), Johnny.Decimal cap (§3), ADR/MADR (§4), Dublin Core (§5). Subject-agnostic: people as a first-class entity (§10), in-KB tasks with a priority matrix instead of an external tracker (§9), the domain-plus-edition pattern for recurring events (§11). |
| 2026-09-04 | Added the **access layer** `sources.md` (how to reach each external source — tool, auth, gotchas — distinct from the resource registry, §5). Documented the optional **`owner`** task field (§9). |
| 2026-09-08 | Removed the `00-inbox/` staging directory: in an agent-native KB the agent triages captures directly, so the inbox went unused; quick untriaged notes fold into `journal/`. Dropped from the capture layer, §9, and `kb_todos.py` TASK_DIRS. |
| 2026-10-26 | Split the access layer: credentials and other sensitive access data move to a gitignored `sources.local.md` (template `templates/sources-local.md`, commit blocked by a `prek` hook); automation secrets go in `.env` (§5). Added "secrets in git" to §13. |
| 2026-10-27 | Added the **Idea** entity (`I-####`, `registry/ideas.md`: goals, ideas to try, proposals; §6, §8); `make check` validates `I-` IDs and `make stats` counts them. Tasks gain a **`fuente`** field with a controlled vocabulary (meeting, chat, mail box and read state, document or form, idea, finding or decision) and optional `Contexto` / `Propuesta` / `Enlace` sub-bullets; `make todos` shows and filters by source (§9). |
| 2026-11-05 | Tasks (§9): four states in the box (pendiente, en marcha, hecha, descartada); `owner` takes one or more **actors** (roles and teams, defined in one table with who fills each now; the template keeps it in `context.md` → Actors) instead of a person; new optional `espera` (what an open task waits for) and `tags`; the history of a task is its dated `Contexto` lines, each with its source, and a state change starts with the new state. Task parsing moves to a shared `scripts/kb_tasks.py`; `make todos` filters by actor and tag; `make roadmap` (`scripts/kb_roadmap.py`) builds a page with projects, a month calendar, a view per actor, a "your turn" list and every open task with filters; `make check` validates tasks. Task examples with the full model in the domain, project and team templates. |
| 2026-11-15 | Documented the working folders beyond the four PARA buckets (§2): `teams/` pages from the new `templates/team.md`, the `raw/` capture folder, `reports/` (one contract per recurring report), `templates/`, `scripts/` and `.claude/` (rules and agent skills). Domain pages gain an optional **How it works** section. Dates: `YYYY-MM-DD` in fields, headings, file names, registries and dated history lines; short dates allowed in running prose and in messages (`.claude/rules/base.md`). |

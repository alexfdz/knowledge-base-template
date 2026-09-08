# KB Framework

> Last updated: 2026-09-04
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
hard-won operational hazards). Keep secrets out of both — in a gitignored `.env` or the keyring.

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
| **Team / Working group** | short code — `WG-OPS` | `teams/<code>.md` | Optional; only when a group needs its own page |
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
· `lapsed` · `alumnus`.

**Governance authority** for conflicting *decisions and opinions* (not facts — those are
findings): follows the authority ordering this KB defines for its subject. Record that ordering
in [`context.md`](context.md) — e.g. a steering body overrides a working group, which overrides
an individual's position. A higher authority overrides a lower one. Record who decided on every
`D-####` row. Facts are never subject to authority: a finding is settled by evidence, not by
rank.

---

## §9 Tasks — in-KB TODOs with a deterministic priority

There is no external tracker. Tasks live **in the page they belong to** (a project page, a
domain page, or the inbox) under a `## Tasks` heading, as checkboxes:

```
- [ ] Confirm the venue deposit deadline | plazo: 2026-09-15 | complejidad: low | owner: @you
- [x] Draft the announcement | plazo: 2026-09-01 | complejidad: medium | owner: @you
```

Every task carries **`plazo`** (due date, `YYYY-MM-DD` or `—`) and **`complejidad`**
(`low` · `medium` · `high`). These two field names are the literal tokens `make todos`
(`scripts/kb_todos.py`) parses — keep them verbatim. An optional **`owner: @handle`** names who
holds the task — free-form (the priority matrix does not rank by it), but worth keeping in a
multi-person KB so `## Tasks` says *who*, not only *what* and *when*. When an agent or human aggregates open
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
regenerates the ranked list on demand — the list is never stored, so it never goes stale.

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

---

## §14 Changing this framework

The framework follows the same rule as the rules files: propose, get explicit approval, then
apply. See [`.claude/rules/ai-feedback-learning-loop.md`](.claude/rules/ai-feedback-learning-loop.md).
Record framework changes below.

| Date | Change |
|------|--------|
| 2026-08-27 | Template created. Borrows from PARA (§2), Johnny.Decimal cap (§3), ADR/MADR (§4), Dublin Core (§5). Subject-agnostic: people as a first-class entity (§10), in-KB tasks with a priority matrix instead of an external tracker (§9), the domain-plus-edition pattern for recurring events (§11). |
| 2026-09-04 | Added the **access layer** `sources.md` (how to reach each external source — tool, auth, gotchas — distinct from the resource registry, §5). Documented the optional **`owner`** task field (§9). |

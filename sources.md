# Sources & access

> Last updated: 2026-09-04
> How to reach every source this KB draws on: the **tool**, the **account/auth**, a minimal
> **usage example**, and the hard-won **gotchas**. The resource registry
> ([`registry/resources.md`](registry/resources.md), `R-####`) is the catalog of *what exists*;
> this file is the *how to reach it* layer.
>
> **Secrets policy:** never inline tokens, passwords or keys here. Secrets live in a **gitignored
> `.env`** or in the OS keyring; this file only references *how to load* them, never their value.

Fill in one section per external source (a CLI, an API, a SaaS app, a drive, a repo). Delete the
scaffold below once you have real sources. Keep the four sub-points — they are what make a source
reproducibly reachable by the next human or agent, weeks later, without re-discovering it.

## Rigor

- Verify a claim against the live source before recording it as a **finding** (`kb-framework.md` §6).
- **Ask before writing** to shared external content; back up before destructive edits.
- Don't ingest third-party PII (attendee lists, national IDs, home addresses) — `kb-framework.md`
  §10 / §13. Pull aggregates and structure, not personal-data rows.

## <Source name>

- **What:** what this source is and what the KB uses it for.
- **Tool / access:** the CLI or app, the account, and how auth is loaded — env-var names, keyring
  backend, any required env prefix or config dir — **never the secret itself**.
- **Use:** a copy-pasteable minimal example (a read that proves access works).
- **Gotchas:** the hard-won operational hazards — the highest-value part of this file. Capture the
  things that cost an hour the first time, e.g.:
  - an endpoint that **hangs** and the flag that fixes it;
  - a token that **expires** and exactly how to re-authenticate;
  - a tool with **no API** on your plan → record how state is checked by hand instead;
  - pagination or result defaults that **silently truncate** (and the flag to get everything);
  - per-command **time limits** that bite on bulk operations (batch, or run in the background);
  - write paths that need a specific form (e.g. a request body passed by file, not argument).

<Repeat this section per source.>

# Sources & access

> Last updated: 2026-10-26
> How to reach every source this KB draws on: what it is, who controls it, the tool and account
> used to get in, a minimal usage example, and the hard-won gotchas. The resource registry
> ([`registry/resources.md`](registry/resources.md), `R-####`) is the catalog of *what exists*;
> this file is the *how to reach it* layer (`kb-framework.md` §5).
>
> **Sensitive half:** passwords, tokens and other access data live in `sources.local.md` —
> gitignored, local only, never pushed; a `prek` hook blocks committing it. It has one section per
> source under the **same heading** as here. If you don't have it, create it from
> [`templates/sources-local.md`](templates/sources-local.md).

## What goes where

Rule: **if someone with access to the repo could get in or act with a piece of data, it is
sensitive.**

| Here (`sources.md`, tracked) | In `sources.local.md` (local, gitignored) |
|---|---|
| What the source is and what the KB uses it for | Passwords, PINs, tokens, API keys |
| Owner and admins (role or `M-####`) | 2FA and recovery codes; recovery phone or email |
| Tool, public URL, the organization's account | Login username when it is a personal account |
| Where the secret lives (local section, `.env` variable) — never the value | Links that grant access on their own (group invites, "anyone with the link" folders) |
| Usage example, rules, gotchas | Security questions, private admin URLs |

If a tool needs a secret as an environment variable, it goes in a gitignored **`.env`** at the
root and is loaded without printing it: `set -a; source .env; set +a`.

## Rigor

- Verify a claim against the live source before recording it as a **finding**
  (`kb-framework.md` §6).
- **Not finding something doesn't prove it doesn't exist.** Before saying something doesn't
  exist or isn't reachable, state where you searched (which folders, which account) and check the
  search covered everything.
- **Ask before writing** to shared external content unless the source's **Rules** authorise it;
  back up before destructive edits.
- Don't ingest third-party PII (attendee lists, national IDs, home addresses) — `kb-framework.md`
  §10 / §13. Pull aggregates and structure, not personal-data rows.
- **Secrets:** read `sources.local.md` only when the task needs a credential, and only that
  source's section. Never copy a secret value into a tracked file, a commit, a message or a
  session's output. In an automation, the secret goes in `.env` and the script loads it, so the
  value never passes through the agent's session.
- Date the gotchas: `(verified YYYY-MM-DD)`. An undated gotcha can't be trusted to still hold.

## Format of each source

One `### <Source name>` per source under `## Sources`, with the same heading in
`sources.local.md` (`rg -A8 "^### <Name>" sources*.md` shows both halves). Omit a field that
doesn't apply.

- **What:** what this source is and what the KB uses it for.
- **Owner:** who holds the account and who administers it (role or `M-####`); what to do at a
  handover.
- **Access:** the tool or app, the account, the auth method, and where the secret lives
  (`sources.local.md` → same section, or `.env` → `VAR_NAME`). Never the value.
- **Use:** a copy-pasteable minimal example (a read that proves access works), or the steps in
  the app when there is no CLI or API.
- **Rules:** what is authorised beyond "ask before writing" (e.g. an automation allowed to write
  without asking) and what is forbidden.
- **Gotchas:** the hard-won operational hazards — the highest-value part of this file. Capture
  the things that cost an hour the first time, e.g.:
  - an endpoint that **hangs** and the flag that fixes it;
  - a token that **expires** and exactly how to re-authenticate;
  - a tool with **no API** on your plan → record how state is checked by hand instead;
  - pagination or result defaults that **silently truncate** (and the flag to get everything);
  - per-command **time limits** that bite on bulk operations (batch, or run in the background);
  - write paths that need a specific form (e.g. a request body passed by file, not argument).

## Sources

*None yet.*

# Sources & access — sensitive data

> Last updated: <YYYY-MM-DD>
> **Private: never committed.** The sensitive half of `sources.md`: credentials and access data
> for each source. Copy this template to `sources.local.md` at the KB root (the `*.local.md`
> pattern is in `.gitignore`, and a `prek` hook blocks committing it).
>
> Anything not sensitive (what it is, owner, tool, examples, gotchas) goes in `sources.md`, not
> here. Never copy a value from this file into a tracked file, a commit, a message or a session's
> output. It exists only on your machine: keep a backup somewhere safe.

## Format of each source

One `### <Source name>` per source under `## Sources`, with the **same heading** as in
`sources.md`. Omit a field that doesn't apply.

- **Account:** login username or email, if sensitive (a personal account).
- **Secret:** password, PIN, token or API key — or which password-manager entry holds it.
- **2FA / recovery:** which phone or email receives the second factor; recovery codes.
- **Notes:** other sensitive access data (invite links, private admin URLs, security questions).
- **Updated:** `YYYY-MM-DD` — last time the credential was verified or changed (rotate it at
  every handover).

## Sources

*None yet.*

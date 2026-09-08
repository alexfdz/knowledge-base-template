# Decision registry

> Last updated: 2026-08-27

**Append-only.** A decision is never edited. When one changes, mark the row `superseded`, add
`superseded-by`, and create a new row with a new ID carrying `supersedes`. Record the drivers and
the options considered, and record decisions that were **rejected** (`wont-do`) too. See
[`kb-framework.md`](../kb-framework.md) §4.

Status: `proposed` · `accepted` · `superseded` · `reversed` · `wont-do`
Governance authority for conflicting positions (decisions/opinions, **not** facts): follows the
ordering this KB defines for its subject in [`context.md`](../context.md). See
[`kb-framework.md`](../kb-framework.md) §8.

| ID | Decision | Decided by | Date | Status | Domains | Source |
|----|----------|-----------|------|--------|---------|--------|

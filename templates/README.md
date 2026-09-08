# Templates

Skeletons for every file type in this KB. Copy one into its destination and fill it in. Keep the
blockquote header (`> Last updated:` …) and the section order — the structure is what makes the
KB scannable and the integrity check meaningful.

| Template | Use for | Destination |
|----------|---------|-------------|
| [`domain.md`](domain.md) | An ongoing area (cap 10) | `domains/<CODE>.md` |
| [`project.md`](project.md) | Finite work (a recurring-event edition, an initiative) | `projects/<key>.md` |
| [`meeting.md`](meeting.md) | Meeting notes | `meetings/YYYY-MM-DD-topic.md` |
| [`lesson-learned.md`](lesson-learned.md) | A learning or rule worth preserving | `lessons-learned/YYYY-MM-DD-topic.md` |
| [`retro.md`](retro.md) | A living retro for a recurring event | `lessons-learned/retro-<event>.md` |
| [`person-tracker.md`](person-tracker.md) | An outreach funnel (recruitment, onboarding, sponsors) | `people/trackers/<campaign>.md` |
| [`gap-analysis.md`](gap-analysis.md) | Our state cross-checked against an external standard | anywhere relevant |
| [`external-system-context.md`](external-system-context.md) | Static-ID cache for an external tool | alongside the project that uses it |

Placeholders use `####` (for registry IDs) and `<angle brackets>` for prose to fill. Registry
rows are added to the files under `registry/`, not here.

Section headings are in English. Field names, status values and IDs stay as defined in
[`../kb-framework.md`](../kb-framework.md); the task field tokens `plazo`/`complejidad` are kept
verbatim because the tooling parses them. Pick one language for the subject content and use it
consistently across pages.

"""The KB's tasks (kb-framework.md §9) and actors (context.md → Actors), for the scripts.

A task is a top-level checkbox in a page under TASK_DIRS, with ` | `-separated fields:
    - [/] Text | plazo: 2026-09-15 | complejidad: low | owner: @treasury, @events
      | espera: @supplier | tags: venue | fuente: mail info@ sin-leer
followed by optional `Contexto` / `Propuesta` / `Enlace` sub-bullets. A dated
`Contexto (YYYY-MM-DD):` line is one step of the task's history.
"""

import pathlib
import re
import subprocess
from dataclasses import dataclass, field

ROOT = pathlib.Path(__file__).resolve().parent.parent
# Tasks live in these areas only: meta and reference docs are excluded so their illustrative
# checkboxes never count as real tasks.
TASK_DIRS = {"domains", "projects", "teams", "meetings", "lessons-learned", "journal", "people"}
STATES = {" ": "pendiente", "/": "en marcha", "x": "hecha", "-": "descartada"}
OPEN = {" ", "/"}
FIELDS = ("plazo", "complejidad", "owner", "espera", "tags", "fuente")
# The page that holds the `## Actors` table. Move the table (e.g. to a governance domain page)
# and point this at its new home.
ACTORS_PAGE = ROOT / "context.md"

TASK_RE = re.compile(r"^- \[(.)\]\s+(.*)$")
SUB_RE = re.compile(
    r"^\s{2,}- (Contexto|Propuesta|Enlace)(?: \((\d{4}-\d{2}-\d{2})[^)]*\))?:\s*(.*)$"
)
ACTOR_ROW_RE = re.compile(r"^\| `(@[a-z]+)` \| ([^|]+) \| ([^|]+) \| ([^|]*) \|$")


@dataclass
class Task:
    file: pathlib.Path
    line: int
    box: str
    text: str
    fields: dict[str, str]
    subs: list[tuple[str, str, str]] = field(default_factory=list)  # (kind, date or "", text)

    @property
    def is_open(self) -> bool:
        return self.box in OPEN

    @property
    def owners(self) -> list[str]:
        return split_list(self.fields.get("owner", ""))

    @property
    def tags(self) -> list[str]:
        return split_list(self.fields.get("tags", ""))

    @property
    def rel(self) -> str:
        return str(self.file.relative_to(ROOT))


@dataclass
class Actor:
    code: str
    kind: str  # role · team · fuera (an outside party: only for `espera`)
    what: str
    now: str


def split_list(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def tracked(prefixes: set[str]) -> list[pathlib.Path]:
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "*.md"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return [ROOT / line for line in out.splitlines() if line.split("/")[0] in prefixes]


def parse_fields(body: str) -> tuple[str, dict[str, str]]:
    text, *rest = [part.strip() for part in body.split(" | ")]
    fields = {}
    for part in rest:
        key, _, value = part.partition(":")
        fields[key.strip().lower()] = value.strip()
    return text, fields


def read_tasks(md: pathlib.Path) -> list[Task]:
    tasks: list[Task] = []
    current: Task | None = None
    for number, line in enumerate(md.read_text().splitlines(), start=1):
        m = TASK_RE.match(line)
        if m:
            text, fields = parse_fields(m.group(2))
            current = Task(md, number, m.group(1), text, fields)
            tasks.append(current)
            continue
        sub = SUB_RE.match(line)
        if sub and current is not None:
            current.subs.append((sub.group(1), sub.group(2) or "", sub.group(3)))
        elif line.strip() and not line.startswith(" "):
            current = None
    return tasks


def all_tasks() -> list[Task]:
    return [task for md in tracked(TASK_DIRS) for task in read_tasks(md)]


def actors() -> dict[str, Actor]:
    """The Actors table of ACTORS_PAGE: code → kind, what it is and who holds it now."""
    table: dict[str, Actor] = {}
    for line in ACTORS_PAGE.read_text().splitlines():
        m = ACTOR_ROW_RE.match(line)
        if m:
            code, kind, what, now = (cell.strip() for cell in m.groups())
            table[code] = Actor(code, kind, what, now)
    return table

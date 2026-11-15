#!/usr/bin/env python3
"""KB integrity check: duplicate IDs, dangling references and malformed tasks.

Over the registries and every tracked markdown file:
1. No ID (R-/D-/F-/Q-/M-/I-####) is defined twice in its registry.
2. Every ID referenced anywhere in the KB exists in its registry.
3. Every task (kb-framework.md §9) has one of the four boxes, a `plazo` date or `—`, a
   `complejidad`, only known fields, `owner` actors that can hold work and an `espera` that is an
   actor or a date (actors: the `## Actors` table of kb_tasks.ACTORS_PAGE, context.md by default).

Exit 1 on any of them.
"""

import pathlib
import re
import subprocess
import sys

from kb_tasks import ACTORS_PAGE, FIELDS, STATES, Task, actors, all_tasks

ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRIES = {
    "R": ROOT / "registry" / "resources.md",
    "D": ROOT / "registry" / "decisions.md",
    "F": ROOT / "registry" / "findings.md",
    "Q": ROOT / "registry" / "questions.md",
    "M": ROOT / "registry" / "people.md",
    "I": ROOT / "registry" / "ideas.md",
}
ID_RE = re.compile(r"\b([RDFQMI])-(\d{4})\b")
ROW_RE = re.compile(r"^\|\s*([RDFQMI])-(\d{4})\s*\|")
# kb-framework.md uses illustrative IDs (e.g. D-0042) in its examples; templates/ show the
# format with placeholders. Neither holds real references.
SKIP_NAMES = {"kb-framework.md"}
SKIP_DIRS = {"templates"}
# A definition row has the full column set (>=7 pipes); the resources relations table has 5.
MIN_PIPES = 7
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def tracked_markdown() -> list[pathlib.Path]:
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "*.md"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return [ROOT / line for line in out.splitlines() if line]


def is_skipped(md: pathlib.Path) -> bool:
    rel = md.relative_to(ROOT)
    return md.name in SKIP_NAMES or bool(SKIP_DIRS & set(rel.parts))


def task_errors(task: Task, known: dict) -> list[str]:
    where = f"task at {task.rel}:{task.line}"
    f = task.fields
    errors = []
    if task.box not in STATES:
        errors.append(f"{where}: box [{task.box}] is not one of [ ] [/] [x] [-]")
    if not (f.get("plazo") == "—" or DATE_RE.fullmatch(f.get("plazo", ""))):
        errors.append(f"{where}: plazo must be YYYY-MM-DD or —")
    if f.get("complejidad") not in {"low", "medium", "high"}:
        errors.append(f"{where}: complejidad must be low, medium or high")
    errors += [f"{where}: unknown field {k!r}" for k in f if k not in FIELDS]
    for code in task.owners:
        if code not in known or known[code].kind == "fuera":
            errors.append(f"{where}: owner {code} is not an actor that can hold work")
    wait = f.get("espera")
    if wait and wait not in known and not DATE_RE.fullmatch(wait):
        errors.append(f"{where}: espera {wait} is neither an actor nor a date")
    return errors


def main() -> int:
    errors: list[str] = []
    known = actors()
    if not known:
        errors.append(f"no Actors table found in {ACTORS_PAGE.relative_to(ROOT)}")
    for task in all_tasks():
        errors += task_errors(task, known)

    defined: dict[str, set[str]] = {}
    for prefix, path in REGISTRIES.items():
        ids: list[str] = []
        for line in path.read_text().splitlines():
            m = ROW_RE.match(line)
            if m and m.group(1) == prefix and line.count("|") >= MIN_PIPES:
                ids.append(f"{m.group(1)}-{m.group(2)}")
        seen: set[str] = set()
        for i in ids:
            if i in seen:
                errors.append(f"duplicate ID {i} in {path.relative_to(ROOT)}")
            seen.add(i)
        defined[prefix] = seen

    for md in tracked_markdown():
        if is_skipped(md):
            continue
        text = md.read_text()
        for m in ID_RE.finditer(text):
            ref = f"{m.group(1)}-{m.group(2)}"
            if ref not in defined[m.group(1)]:
                errors.append(f"dangling reference {ref} in {md.relative_to(ROOT)}")

    for e in sorted(set(errors)):
        print(f"ERROR {e}")
    if errors:
        print(f"\n{len(set(errors))} error(s).")
        return 1
    print("kb-check: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

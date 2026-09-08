#!/usr/bin/env python3
"""Aggregate open tasks across the KB and rank them by the priority matrix.

A task is a markdown checkbox with the KB fields, e.g.:
    - [ ] Confirm venue deposit | plazo: 2026-09-15 | complejidad: low | owner: @alex

Ranking (kb-framework.md §9): earliest `plazo` first (no date last), then lowest
`complejidad` first. The list is regenerated on demand; it is never stored.
"""

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPEN_RE = re.compile(r"^\s*- \[ \]\s+(.*)$")
PLAZO_RE = re.compile(r"plazo:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", re.IGNORECASE)
COMPLEJIDAD_RE = re.compile(r"complejidad:\s*(low|medium|high)", re.IGNORECASE)
COMPLEXITY_ORDER = {"low": 0, "medium": 1, "high": 2}
NO_DATE = "9999-99-99"


# Tasks live in these areas only (kb-framework.md §9): meta/reference docs are excluded so
# their illustrative checkboxes never count as real tasks.
TASK_DIRS = {"domains", "projects", "meetings", "lessons-learned", "00-inbox", "journal", "people"}


def tracked_markdown() -> list[pathlib.Path]:
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "*.md"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    files = []
    for line in out.splitlines():
        if not line:
            continue
        rel = pathlib.Path(line)
        if rel.parts and rel.parts[0] in TASK_DIRS:
            files.append(ROOT / line)
    return files


def collect() -> list[dict]:
    tasks = []
    for md in tracked_markdown():
        for line in md.read_text().splitlines():
            m = OPEN_RE.match(line)
            if not m:
                continue
            body = m.group(1)
            plazo = PLAZO_RE.search(body)
            comp = COMPLEJIDAD_RE.search(body)
            tasks.append({
                "text": body.split("|")[0].strip(),
                "plazo": plazo.group(1) if plazo else NO_DATE,
                "complejidad": comp.group(1).lower() if comp else "medium",
                "file": str(md.relative_to(ROOT)),
            })
    return tasks


def main() -> int:
    tasks = collect()
    tasks.sort(key=lambda t: (t["plazo"], COMPLEXITY_ORDER[t["complejidad"]]))
    if not tasks:
        print("No open tasks.")
        return 0
    width = max(len(t["complejidad"]) for t in tasks)
    for t in tasks:
        plazo = "—         " if t["plazo"] == NO_DATE else t["plazo"]
        print(f"{plazo}  {t['complejidad']:<{width}}  {t['text']}  ({t['file']})")
    print(f"\n{len(tasks)} open task(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Aggregate open tasks across the KB and rank them by the priority matrix.

A task is a markdown checkbox with the KB fields (kb-framework.md §9), e.g.:
    - [/] Confirm venue deposit | plazo: 2026-09-15 | complejidad: low | owner: @treasury
      | espera: @supplier | fuente: mail info@ sin-leer

Open means `[ ]` (pendiente) or `[/]` (en marcha). Ranking: earliest `plazo` first (no date
last), then lowest `complejidad` first. The list is regenerated on demand; it is never stored.

Usage: kb_todos.py [--fuente TEXT] [--actor @CODE] [--tag TAG]
"""

import argparse
import sys

from kb_tasks import STATES, Task, all_tasks

COMPLEXITY_ORDER = {"low": 0, "medium": 1, "high": 2}
NO_DATE = "9999-99-99"


def plazo(task: Task) -> str:
    value = task.fields.get("plazo", "")
    return value if value[:2] == "20" else NO_DATE


def complexity(task: Task) -> str:
    value = task.fields.get("complejidad", "medium").lower()
    return value if value in COMPLEXITY_ORDER else "medium"


def keep(task: Task, args: argparse.Namespace) -> bool:
    if args.fuente and args.fuente.lower() not in task.fields.get("fuente", "").lower():
        return False
    if args.actor and args.actor not in task.owners + [task.fields.get("espera", "")]:
        return False
    return not (args.tag and args.tag.lower() not in task.tags)


def main() -> int:
    parser = argparse.ArgumentParser(description="Ranked list of open tasks across the KB.")
    parser.add_argument("--fuente", help="only tasks whose `fuente` contains this text")
    parser.add_argument("--actor", help="only tasks this actor holds or that wait on it (@lead)")
    parser.add_argument("--tag", help="only tasks with this tag")
    args = parser.parse_args()

    tasks = [t for t in all_tasks() if t.is_open and keep(t, args)]
    tasks.sort(key=lambda t: (plazo(t), COMPLEXITY_ORDER[complexity(t)]))
    if not tasks:
        print("No open tasks.")
        return 0
    for t in tasks:
        when = "—         " if plazo(t) == NO_DATE else plazo(t)
        who = ", ".join(t.owners) or "no owner"
        wait = f" · espera {t.fields['espera']}" if t.fields.get("espera") else ""
        state = "" if t.box == " " else f"[{STATES[t.box]}] "
        source = t.fields.get("fuente", "—")
        print(f"{when}  {complexity(t):<6}  {state}{t.text}  ({who}{wait})  [{source}]  ({t.rel})")
    print(f"\n{len(tasks)} open task(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

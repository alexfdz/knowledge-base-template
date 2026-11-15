#!/usr/bin/env python3
"""Generate roadmap.html: projects, a month calendar, a view per actor and every open task.

Reads the same tasks as kb_todos.py (kb-framework.md §9) with their Contexto / Propuesta /
Enlace sub-bullets and dated history, and the actors of kb_tasks.ACTORS_PAGE. The page is
regenerated on demand and never committed. Its UI text (kb_roadmap.html) is in Spanish.

Usage: kb_roadmap.py [--out PATH]
"""

import argparse
import datetime
import html
import json
import pathlib
import re
import sys
import unicodedata

from kb_tasks import ROOT, STATES, Task, actors, all_tasks

ID_RE = re.compile(r"\b([RDFQMI]-\d{4})\b")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
REGISTRIES = ["resources", "decisions", "findings", "questions", "people", "ideas"]
TEMPLATE = pathlib.Path(__file__).with_name("kb_roadmap.html")
# Whose «te toca» (your turn) the page shows: the actors whose «now» names this person. Set it to
# the KB owner's M-#### when instantiating; empty marks no actor as yours.
OWNER = ""


def plain(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    return "".join(c for c in text if not unicodedata.combining(c)).lower()


def registry_labels() -> dict[str, str]:
    labels = {}
    for name in REGISTRIES:
        for line in (ROOT / "registry" / f"{name}.md").read_text().splitlines():
            cells = [c.strip() for c in line.split("|")]
            if len(cells) > 3 and ID_RE.fullmatch(cells[1]):
                label = re.sub(r"[*`]", "", cells[2])
                labels[cells[1]] = label if len(label) <= 320 else label[:319] + "…"
    return labels


def person_names() -> dict[str, str]:
    """Map an M-ID to «Short (M-####)», the short name being the nickname or the first name."""
    names: dict[str, str] = {}
    for line in (ROOT / "registry" / "people.md").read_text().splitlines():
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 4 or not re.fullmatch(r"M-\d{4}", cells[1]):
            continue
        nick = re.search(r"\(([A-Z][^)]*)\)", cells[2])
        short = nick.group(1) if nick else cells[2].split()[0]
        names.setdefault(cells[1], f"{short} ({cells[1]})")
    return names


def render(md: str, base: pathlib.Path, labels: dict[str, str]) -> str:
    """Tiny markdown: links, `code`, **bold**, and registry IDs with their label as tooltip."""
    parts = []
    pos = 0
    for m in LINK_RE.finditer(md):
        parts.append(inline(md[pos : m.start()], labels))
        url = m.group(2)
        if not re.match(r"[a-z]+:", url):
            path, _, anchor = url.partition("#")
            target = (base / path).resolve() if path else base / "?"
            url = str(target.relative_to(ROOT)) + (f"#{anchor}" if anchor else "")
        parts.append(f'<a href="{html.escape(url)}">{inline(m.group(1), labels)}</a>')
        pos = m.end()
    parts.append(inline(md[pos:], labels))
    return "".join(parts)


def inline(text: str, labels: dict[str, str]) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)

    def abbr(m: re.Match) -> str:
        label = labels.get(m.group(1))
        return f'<abbr title="{html.escape(label)}">{m.group(1)}</abbr>' if label else m.group(1)

    return ID_RE.sub(abbr, text)


def page_label(md: pathlib.Path) -> str:
    first = md.read_text().splitlines()[0].lstrip("# ").strip()
    return first.replace(" — ", " · ")


def task_card(task: Task, labels: dict[str, str]) -> dict:
    base = task.file.parent
    plazo = task.fields.get("plazo", "")
    card = {
        "text": render(task.text, base, labels),
        "plain": plain(task.text),
        "state": STATES[task.box],
        "plazo": plazo if re.match(r"\d{4}-", plazo) else "",
        "complejidad": task.fields.get("complejidad", "medium"),
        "owners": task.owners,
        "espera": task.fields.get("espera", ""),
        "tags": task.tags,
        "fuente": [s.strip() for s in task.fields.get("fuente", "").split(",") if s.strip()],
        "file": task.rel,
        "area": page_label(task.file),
        "kind": task.file.relative_to(ROOT).parts[0],
        "history": [],
    }
    for kind, date, text in task.subs:
        if kind == "Contexto" and date:
            card["history"].append({"date": date, "text": render(text, base, labels)})
        else:
            key = kind.lower()
            card[key] = (card[key] + " " if key in card else "") + render(text, base, labels)
    return card


def actor_cards(names: dict[str, str]) -> list[dict]:
    return [
        {
            "code": a.code,
            "kind": a.kind,
            "what": a.what,
            "now": re.sub(r"M-\d{4}", lambda m: names.get(m.group(0), m.group(0)), a.now),
            "mine": bool(OWNER) and OWNER in a.now,
        }
        for a in actors().values()
    ]


def project_cards() -> list[dict]:
    cards = []
    for md in sorted((ROOT / "projects").glob("*.md")):
        text = md.read_text()
        meta = re.search(
            r"\*\*status:\*\*\s*([^·\n]+).*?\*\*period:\*\*\s*((?:[^\n]|\n> )+)", text, re.S
        )
        if not meta:
            continue
        cards.append(
            {
                "file": f"projects/{md.name}",
                "title": page_label(md),
                "status": meta.group(1).strip(),
                "period": meta.group(2).replace("\n> ", " ").strip(),
            }
        )
    return cards


def open_questions(labels: dict[str, str]) -> list[dict]:
    """Open rows of registry/questions.md: ID, question, owner, date and what settles it."""
    rows = []
    for line in (ROOT / "registry" / "questions.md").read_text().splitlines():
        cells = [c.strip() for c in line.split("|")]
        if len(cells) > 8 and re.fullmatch(r"Q-\d{4}", cells[1]) and cells[5] == "open":
            base = ROOT / "registry"
            rows.append(
                {
                    "id": cells[1],
                    "question": render(cells[2], base, labels),
                    "owner": render(cells[3], base, labels),
                    "date": cells[4],
                    "settles": render(cells[7], base, labels),
                }
            )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the KB roadmap page.")
    parser.add_argument("--out", default=str(ROOT / "roadmap.html"), help="output HTML file")
    args = parser.parse_args()

    labels = registry_labels()
    data = {
        "today": datetime.date.today().isoformat(),
        "tasks": [task_card(task, labels) for task in all_tasks() if task.is_open],
        "actors": actor_cards(person_names()),
        "projects": project_cards(),
        "questions": open_questions(labels),
        "sourceLabels": {k: v for k, v in labels.items() if k.startswith(("R-", "F-", "D-", "I-"))},
    }
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    page = TEMPLATE.read_text().replace("/*DATA*/null", payload)
    out = pathlib.Path(args.out)
    out.write_text(page)
    print(f"{out} — {len(data['tasks'])} open task(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

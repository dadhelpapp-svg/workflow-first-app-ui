#!/usr/bin/env python3
"""Create portable project guidance without overwriting existing files."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIEF_TEMPLATE = ROOT / "templates" / "PROJECT_BRIEF.md"
AGENTS_TEXT = """# Project instructions

Use the installed `$workflow-first-app-ui` skill for application-development work.

- Read this project's existing architecture, design system, source, and tests before editing.
- Complete `PROJECT_BRIEF.md`, including existing-system research, before greenfield code.
- Record the project's real development, test, build, and browser commands here.
- Preserve business rules and authorization boundaries.
- Do not merge or deploy without explicit authorization.
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Add a project brief and minimal Codex instructions when absent."
    )
    parser.add_argument("project", type=Path, help="Existing project directory")
    parser.add_argument(
        "--dry-run", action="store_true", help="Report changes without writing files"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project = args.project.expanduser().resolve()
    if not project.is_dir():
        raise SystemExit(f"Project directory does not exist: {project}")

    planned: list[tuple[Path, str]] = []
    brief = project / "PROJECT_BRIEF.md"
    agents = project / "AGENTS.md"

    if not brief.exists():
        planned.append((brief, "project brief"))
    if not agents.exists():
        planned.append((agents, "minimal project instructions"))

    if not planned:
        print("No files created; PROJECT_BRIEF.md and AGENTS.md already exist.")
        return 0

    for path, label in planned:
        if args.dry_run:
            print(f"Would create {label}: {path}")
            continue
        if path == brief:
            shutil.copyfile(BRIEF_TEMPLATE, path)
        else:
            path.write_text(AGENTS_TEXT, encoding="utf-8", newline="\n")
        print(f"Created {label}: {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

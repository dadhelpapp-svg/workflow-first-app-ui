#!/usr/bin/env python3
"""Create and verify portable project guidance without replacing local rules."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIEF_TEMPLATE = ROOT / "templates" / "PROJECT_BRIEF.md"
MARKER_START = "<!-- workflow-first-app-ui:start -->"
MARKER_END = "<!-- workflow-first-app-ui:end -->"
AGENTS_BLOCK = f"""{MARKER_START}
## Workflow-first development

Use the installed `$workflow-first-app-ui` skill for application-development work.

- Read this project's existing architecture, design system, source, and tests before editing.
- Complete `PROJECT_BRIEF.md`, including existing-system research, before greenfield code.
- Record the project's real development, test, build, and browser commands in this file.
- Preserve business rules and authorization boundaries.
- Do not merge or deploy without explicit authorization.

Project-local instructions and the implemented design system remain authoritative.
{MARKER_END}
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Add or verify a project brief and a workflow-first AGENTS.md reference."
    )
    parser.add_argument("project", type=Path, help="Existing project directory")
    parser.add_argument(
        "--dry-run", action="store_true", help="Report changes without writing files"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit nonzero unless the brief and managed AGENTS.md reference are present",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project = args.project.expanduser().resolve()
    if not project.is_dir():
        raise SystemExit(f"Project directory does not exist: {project}")

    brief = project / "PROJECT_BRIEF.md"
    agents = project / "AGENTS.md"

    agents_text = agents.read_text(encoding="utf-8") if agents.exists() else ""
    has_reference = MARKER_START in agents_text and MARKER_END in agents_text

    if args.check:
        missing: list[str] = []
        if not brief.is_file():
            missing.append("PROJECT_BRIEF.md")
        if not has_reference:
            missing.append("the workflow-first managed block in AGENTS.md")
        if missing:
            print("Project bootstrap check failed: " + ", ".join(missing))
            return 1
        print("Project bootstrap check passed.")
        return 0

    changed = False
    if not brief.exists():
        if args.dry_run:
            print(f"Would create project brief: {brief}")
        else:
            shutil.copyfile(BRIEF_TEMPLATE, brief)
            print(f"Created project brief: {brief}")
        changed = True

    if not has_reference:
        action = "create AGENTS.md with" if not agents.exists() else "append to AGENTS.md"
        if args.dry_run:
            print(f"Would {action} the workflow-first managed block: {agents}")
        else:
            prefix = agents_text.rstrip()
            updated = f"{prefix}\n\n{AGENTS_BLOCK}" if prefix else f"# Project instructions\n\n{AGENTS_BLOCK}"
            agents.write_text(updated, encoding="utf-8", newline="\n")
            print(f"Updated project instructions: {agents}")
        changed = True

    if not changed:
        print("Project already contains the workflow-first bootstrap files.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

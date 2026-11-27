# Claude Code instructions

This repository keeps its shared agent instructions in `AGENTS.md` so that Claude Code and Codex read the same defaults. Claude Code loads them through the import below.

@AGENTS.md

## Working in this repository

- This is a skill and standards bundle, not an application. `SKILL.md` is the installable skill; the root Markdown files are companion standards.
- Validate every change with `python scripts/validate_repo.py`. CI runs the same check plus shell and PowerShell syntax checks of `scripts/install.sh` and `scripts/install.ps1`.
- Renaming or adding a required file means updating `REQUIRED_FILES` in `scripts/validate_repo.py` and every relative link to it.
- Follow `CONTRIBUTING.md` for changelog and version updates.

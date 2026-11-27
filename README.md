# Workflow-first application development

An installable Codex skill for taking a short software request through research, design, implementation, verification, and a safe release handoff. It works with existing applications and greenfield projects, but it requires credible existing-system research before code is started from scratch.

The repository keeps one canonical lifecycle and loads detail only when it is relevant:

- [`SKILL.md`](SKILL.md) is the installable entrypoint.
- [`references/development-standard.md`](references/development-standard.md) is the canonical end-to-end standard.
- [`references/existing-system-research.md`](references/existing-system-research.md) defines the baseline-research gate.
- [`references/design-guide.md`](references/design-guide.md) records the portable UI and UX defaults.
- [`references/tool-routing.md`](references/tool-routing.md) assigns external design and verification tools non-conflicting roles.
- [`references/verification.md`](references/verification.md) defines proportional quality gates.
- [`references/portable-bootstrap.md`](references/portable-bootstrap.md) covers installation, project bootstrap, and handoff.
- [`references/source-audit.md`](references/source-audit.md) records public-source verification and audit limits.

Project-level instructions and implemented design systems always take precedence.

## Install on any device

macOS, Linux, or Git Bash:

```sh
git clone https://github.com/dadhelpapp-svg/workflow-first-app-ui.git ~/.codex/skills/workflow-first-app-ui
python ~/.codex/skills/workflow-first-app-ui/scripts/validate_repo.py
```

Windows PowerShell:

```powershell
git clone https://github.com/dadhelpapp-svg/workflow-first-app-ui.git "$env:USERPROFILE\.codex\skills\workflow-first-app-ui"
python "$env:USERPROFILE\.codex\skills\workflow-first-app-ui\scripts\validate_repo.py"
```

The install helpers support both a first install and a fast-forward update:

```powershell
.\scripts\install.ps1
```

```sh
./scripts/install.sh
```

Restart Codex after installation or update. Invoke the skill with `$workflow-first-app-ui`, or let Codex select it for application-development work.

## Start a project

From this repository, create a small project brief without overwriting existing instructions:

```sh
python scripts/bootstrap_project.py /path/to/project
```

The bootstrap adds `PROJECT_BRIEF.md` from the maintained template and idempotently adds a marked workflow-first block to `AGENTS.md` while preserving existing project instructions. Review both before coding, then verify the reference in local setup or CI:

```sh
python scripts/bootstrap_project.py /path/to/project --check
```

## Validate

```sh
python scripts/validate_repo.py
python /path/to/skill-creator/scripts/quick_validate.py .
```

The repository validator checks package structure, internal links, frontmatter, versioning, secret-like text, and the presence of the research and release gates. GitHub Actions also checks the shell and PowerShell helpers.

## Scope and safety

This skill does not silently install third-party design tools, copy premium source, choose production credentials, merge pull requests, or deploy. External repositories are evaluated as baselines or bounded donors and retain their own licenses. See [`SECURITY.md`](SECURITY.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md).

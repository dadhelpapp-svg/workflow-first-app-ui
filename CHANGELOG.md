# Changelog

All notable changes to this repository are documented here.

## [2.0.0] - 2026-11-28

This release combines the end-to-end consolidation from pull request #1 with the Claude Code migration (1.2.0) and Spec Kit standard (1.3.0). The migrated handoff, browser-testing, setup-checklist, Spec Kit, and example files are kept.

### Changed

- Expanded the skill from UI-only guidance into an end-to-end application-development workflow while keeping the `workflow-first-app-ui` name and install paths.
- Made credible existing-system research a required gate before greenfield scaffolding.
- Rewrote `references/verification.md` as proportional quality gates with a live-proof boundary.
- Merged `references/lessons-learned.md` into the new design guide and development standard.
- The install helpers now validate the installed skill.
- `agents/openai.yaml` allows implicit invocation in Codex.

### Added

- `references/development-standard.md`, the canonical lifecycle.
- `references/existing-system-research.md`, `references/design-guide.md`, `references/tool-routing.md`, `references/portable-bootstrap.md`, and `references/source-audit.md`.
- A motion rule in the design guide: animate one shared selection indicator, prefer CSS or the Web Animations API before an animation library, and honor reduced motion.
- `scripts/bootstrap_project.py` and `templates/PROJECT_BRIEF.md`. The bootstrap adds a managed `AGENTS.md` block and a `CLAUDE.md` import of `@AGENTS.md`, with a `--check` mode for CI.
- BoardUI in the reviewed component sources.
- An existing-system research section in the Claude handoff template.
- Validation for the research, authorization, canonical-guide, bootstrap, and `CLAUDE.md` import invariants.

## [1.3.0] - 2026-11-27

### Added

- `SPEC_DRIVEN_DEVELOPMENT.md`, an optional standard for using GitHub Spec Kit in application projects with both Claude Code and Codex, mapping its steps onto the workflow-first skill, verification, and handoff standards.
- `templates/SPEC_KIT_CONSTITUTION.md`, a `/speckit-constitution` seed derived from these standards.

### Changed

- `AGENTS.md`, `SKILL.md`, the handoff standard and template, the setup checklist, and the README point to the Spec Kit standard where it applies.

## [1.2.0] - 2026-11-27

### Added

- `CLAUDE.md`, which imports `AGENTS.md` so Claude Code and Codex share one set of defaults.
- Claude Code install path (`~/.claude/skills/workflow-first-app-ui`) and `/workflow-first-app-ui` invocation.
- `--codex`/`--all` (shell) and `-Target Codex|All` (PowerShell) install options.
- Claude Code Playwright MCP setup (`claude mcp add`) and a project `.mcp.json` example.

### Changed

- The install helpers now default to Claude Code. Codex users should pass `--codex` or `-Target Codex`.
- Renamed `CHAT_TO_CODEX_HANDOFF.md` to `CHAT_TO_CLAUDE_HANDOFF.md` and `templates/CODEX_HANDOFF.md` to `templates/CLAUDE_HANDOFF.md`, and retargeted the handoff wording to Claude Code.
- Codex setup remains documented alongside Claude Code; `agents/openai.yaml` is unchanged.

## [1.1.0] - 2026-11-22

### Added

- Chat-to-Codex project handoff standard and reusable handoff template.
- Minimum project setup and security/privacy checklists.
- New-project and existing-project handoff examples.
- Cross-platform install/update helpers.
- Deterministic repository validation and GitHub Actions automation.
- Contribution guidance, repository scope, and source-review metadata.

### Changed

- Clarified the boundary between the UI skill and the broader supporting standards bundle.
- Refreshed the external component-source review notes.

## [1.0.0] - 2026-11-21

### Added

- Initial workflow-first application UI skill.
- Component-source, verification, and lessons-learned references.
- Global software-design and Playwright MCP browser-testing standards.

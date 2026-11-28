# Changelog

All notable changes to this repository are documented here.

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

# Workflow-First App UI skill

A reusable Codex skill for extending or auditing application interfaces without discarding an established UI, component system, or business workflow.

It helps an agent:

- reuse existing components before adding dependencies;
- select genuinely free shadcn-compatible components;
- keep source and license provenance;
- integrate bounded dashboard pieces without template-driven rewrites;
- preserve business logic, accessibility, and responsive behavior; and
- verify real user workflows with automated and rendered checks.

## Included standards

- [`SKILL.md`](SKILL.md) contains the workflow-first implementation and audit process.
- [`AGENTS.md`](AGENTS.md) supplies the portable global software-design defaults.
- [`BROWSER_TESTING.md`](BROWSER_TESTING.md) defines the Playwright MCP setup, browser workflow, tool boundaries, and reporting standard.
- [`references/`](references/) contains component-source, verification, and lessons-learned guidance.

The global defaults are intentionally subordinate to project-level instructions and established project design systems.

## Install

Clone this repository into the Codex skills directory:

```bash
git clone https://github.com/dadhelpapp-svg/workflow-first-app-ui.git ~/.codex/skills/workflow-first-app-ui
```

On Windows PowerShell:

```powershell
git clone https://github.com/dadhelpapp-svg/workflow-first-app-ui.git "$env:USERPROFILE\.codex\skills\workflow-first-app-ui"
```

Then invoke it with `$workflow-first-app-ui`, or let Codex select it for relevant application UI work.

The repository contains guidance and source links, not redistributed premium component code.

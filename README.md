# Workflow-First App UI and Codex standards

A reusable Codex skill for extending or auditing application interfaces without discarding an established UI, component system, or business workflow. The repository also packages supporting project-handoff, browser-verification, security, and contribution standards used around the skill.

It helps an agent:

- reuse existing components before adding dependencies;
- select genuinely free shadcn-compatible components;
- keep source and license provenance;
- integrate bounded dashboard pieces without template-driven rewrites;
- preserve business logic, accessibility, and responsive behavior; and
- verify real user workflows with automated and rendered checks.

## Included standards

- [`SKILL.md`](SKILL.md) contains the workflow-first implementation and audit process.
- [`AGENTS.md`](AGENTS.md) supplies the portable global software-design and handoff defaults.
- [`CHAT_TO_CODEX_HANDOFF.md`](CHAT_TO_CODEX_HANDOFF.md) requires the originating chat to complete safe discovery and minimum project setup before an execution-ready Codex handoff.
- [`templates/CODEX_HANDOFF.md`](templates/CODEX_HANDOFF.md) is the reusable handoff form, supported by two fictional [`examples/`](examples/).
- [`PROJECT_SETUP_CHECKLIST.md`](PROJECT_SETUP_CHECKLIST.md) defines the minimum runnable baseline expected before handoff.
- [`BROWSER_TESTING.md`](BROWSER_TESTING.md) defines the Playwright MCP setup, browser workflow, tool boundaries, and reporting standard.
- [`SECURITY.md`](SECURITY.md) defines credential, data, browser-profile, and authorization boundaries.
- [`references/`](references/) contains component-source, verification, and lessons-learned guidance.

## Repository scope

The installable skill remains focused on workflow-first React interface work. The root standards and templates form a small companion bundle for preparing projects, handing them to Codex, and proving the resulting workflow. They do not replace project-level instructions, application tests, security review, or product decisions that require the user.

The current release is recorded in [`VERSION`](VERSION), with release history in [`CHANGELOG.md`](CHANGELOG.md). See [`CONTRIBUTING.md`](CONTRIBUTING.md) before changing source guidance or packaging.

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

To install or update with a helper script:

```powershell
.\scripts\install.ps1
```

```sh
./scripts/install.sh
```

Validate a checkout with:

```sh
python scripts/validate_repo.py
```

The repository contains guidance and source links, not redistributed premium component code.

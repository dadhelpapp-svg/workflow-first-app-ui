# Workflow-first application development skill and standards

A reusable Claude Code skill (also compatible with Codex) for taking a short software request through research, design, implementation, verification, and a safe release handoff, without discarding an established UI, component system, or business workflow. It works with existing applications and greenfield projects, but requires credible existing-system research before code is started from scratch. The repository also packages supporting project-handoff, browser-verification, security, and contribution standards used around the skill.

It helps an agent:

- reuse existing components before adding dependencies;
- select genuinely free shadcn-compatible components;
- keep source and license provenance;
- integrate bounded dashboard pieces without template-driven rewrites;
- preserve business logic, accessibility, and responsive behavior; and
- verify real user workflows with automated and rendered checks.

## Included standards

- [`SKILL.md`](SKILL.md) is the installable entrypoint.
- [`references/development-standard.md`](references/development-standard.md) is the canonical end-to-end lifecycle.
- [`references/existing-system-research.md`](references/existing-system-research.md) defines the baseline-research gate before greenfield code.
- [`references/design-guide.md`](references/design-guide.md) records the portable UI, UX, accessibility, and motion defaults.
- [`references/tool-routing.md`](references/tool-routing.md) assigns external design and verification tools non-conflicting roles.
- [`references/verification.md`](references/verification.md) defines proportional quality gates.
- [`references/portable-bootstrap.md`](references/portable-bootstrap.md) covers installation, project bootstrap, and cross-device handoff.
- [`references/source-audit.md`](references/source-audit.md) records public-source verification and audit limits.
- [`references/component-sources.md`](references/component-sources.md) lists reviewed free component sources.
- [`AGENTS.md`](AGENTS.md) supplies the portable global software-design and handoff defaults.
- [`CLAUDE.md`](CLAUDE.md) imports `AGENTS.md` so Claude Code and Codex share the same defaults.
- [`CHAT_TO_CLAUDE_HANDOFF.md`](CHAT_TO_CLAUDE_HANDOFF.md) requires the originating chat to complete safe discovery and minimum project setup before an execution-ready Claude Code handoff.
- [`templates/CLAUDE_HANDOFF.md`](templates/CLAUDE_HANDOFF.md) is the reusable handoff form, supported by two fictional [`examples/`](examples/).
- [`PROJECT_SETUP_CHECKLIST.md`](PROJECT_SETUP_CHECKLIST.md) defines the minimum runnable baseline expected before handoff.
- [`SPEC_DRIVEN_DEVELOPMENT.md`](SPEC_DRIVEN_DEVELOPMENT.md) explains when and how to use [GitHub Spec Kit](https://github.com/github/spec-kit) in application projects with Claude Code and Codex, and [`templates/SPEC_KIT_CONSTITUTION.md`](templates/SPEC_KIT_CONSTITUTION.md) seeds a Spec Kit constitution from these standards.
- [`BROWSER_TESTING.md`](BROWSER_TESTING.md) defines the Playwright MCP setup, browser workflow, tool boundaries, and reporting standard.
- [`SECURITY.md`](SECURITY.md) defines credential, data, browser-profile, and authorization boundaries.

## Repository scope

The installable skill covers the full application lifecycle, with workflow-first interface work at its core. The root standards and templates form a small companion bundle for preparing projects, handing them to Claude Code, and proving the resulting workflow. They do not replace project-level instructions, application tests, security review, or product decisions that require the user.

The current release is recorded in [`VERSION`](VERSION), with release history in [`CHANGELOG.md`](CHANGELOG.md). See [`CONTRIBUTING.md`](CONTRIBUTING.md) before changing source guidance or packaging.

The global defaults are intentionally subordinate to project-level instructions and established project design systems.

## Install

### Claude Code

Clone this repository into your personal Claude Code skills directory:

```bash
git clone https://github.com/dadhelpapp-svg/workflow-first-app-ui.git ~/.claude/skills/workflow-first-app-ui
```

On Windows PowerShell:

```powershell
git clone https://github.com/dadhelpapp-svg/workflow-first-app-ui.git "$env:USERPROFILE\.claude\skills\workflow-first-app-ui"
```

Start a new Claude Code session, then invoke it with `/workflow-first-app-ui`, or let Claude select it automatically for relevant application UI work. To share it with one project's collaborators instead, clone it into that project's `.claude/skills/workflow-first-app-ui`.

### Codex

The skill still works with Codex. Clone it into `~/.codex/skills/workflow-first-app-ui` (or `$CODEX_HOME/skills/...`) and invoke it with `$workflow-first-app-ui`.

### Helper scripts

The helpers install or update the skill. They default to Claude Code; pass a target for Codex or both:

```sh
./scripts/install.sh            # ~/.claude/skills/workflow-first-app-ui
./scripts/install.sh --codex    # ${CODEX_HOME:-~/.codex}/skills/workflow-first-app-ui
./scripts/install.sh --all      # both
./scripts/install.sh /some/path # explicit destination
```

```powershell
.\scripts\install.ps1                 # Claude Code
.\scripts\install.ps1 -Target Codex   # Codex
.\scripts\install.ps1 -Target All     # both
```

`CLAUDE_CONFIG_DIR` and `CODEX_HOME` are honored when set.

The helpers run the repository validator after installing.

## Start a project

From this repository, add a project brief and a workflow-first reference to an application project without overwriting its existing instructions:

```sh
python scripts/bootstrap_project.py /path/to/project
```

This copies `PROJECT_BRIEF.md` from [`templates/PROJECT_BRIEF.md`](templates/PROJECT_BRIEF.md), adds a marked workflow-first block to the project's `AGENTS.md`, and makes sure its `CLAUDE.md` imports `@AGENTS.md`. Running it again changes nothing. Review the files before coding, then verify them in local setup or CI:

```sh
python scripts/bootstrap_project.py /path/to/project --check
```

### Spec Kit (optional, per application project)

Spec Kit is installed into the application you are building, not into this repository. Install the CLI once, then initialize a project for both agents:

```sh
uv tool install specify-cli==1.4.5
specify init --here --force --integration claude   # from the app repo root, on a clean branch
specify integration install codex
```

See [`SPEC_DRIVEN_DEVELOPMENT.md`](SPEC_DRIVEN_DEVELOPMENT.md) for when to use it and how its steps map onto this skill.

## Validate

Validate a checkout with:

```sh
python scripts/validate_repo.py
```

The validator checks package structure, internal links, frontmatter, versioning, secret-like text, and the presence of the research and release gates. GitHub Actions also checks the shell and PowerShell helpers.

The repository contains guidance and source links, not redistributed premium component code. It does not silently install third-party design tools, merge pull requests, or deploy.

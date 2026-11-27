# Spec-driven development with GitHub Spec Kit

[GitHub Spec Kit](https://github.com/github/spec-kit) (MIT) is an open source toolkit that makes a coding agent write a specification, a technical plan, and a task list before it writes code, then checks the implementation against them. Its `specify` CLI installs per-project skills for Claude Code, Codex, and other agents.

This standard explains when to use Spec Kit in an application project and how it fits around the workflow-first skill, the shared defaults in [AGENTS.md](AGENTS.md), and the [Chat-to-Claude handoff](CHAT_TO_CLAUDE_HANDOFF.md). It is optional. Spec Kit is installed into application repositories, never into this standards repository, and nothing here is vendored from it.

Last reviewed: 2026-11-27 against Spec Kit v1.4.5. Spec Kit changes quickly, so confirm commands against its [documentation](https://github.github.io/spec-kit/) before relying on them.

## When to use it

Use Spec Kit for a bounded feature or new application where ambiguity is the main risk: several screens or roles, unclear acceptance criteria, data or authorization rules that must be written down, or work that will be split across sessions or agents.

Skip it for small fixes, copy changes, and isolated component swaps. The skill's normal process plus the project's tests is enough there. For bugs, Spec Kit's optional `bug` extension (`specify extension add bug`) is available, but a direct reproduce, fix, and verify loop is usually faster.

If a project already uses Spec Kit, follow its existing `.specify/` setup and constitution. Project-level instructions still win.

## Install the CLI

Spec Kit needs Python 3.11+ and [uv](https://docs.astral.sh/uv/). Install the CLI once per machine, pinned to a release:

```sh
uv tool install specify-cli==1.4.5
specify version
```

To upgrade later, run `uv tool install --force specify-cli==<new version>` and then `specify integration upgrade <key>` in each project.

## Set up a project for Claude Code and Codex

From the application repository root, on a clean branch so the generated files are reviewable:

```sh
# New project
specify init my-app --integration claude
cd my-app
specify integration install codex

# Existing project (commit or stash work first; --force allows a non-empty directory)
specify init --here --force --integration claude
specify integration install codex
```

Both integrations are declared multi-install safe, so they can live in one repository:

| Agent | Skills location | Invocation |
| --- | --- | --- |
| Claude Code | `.claude/skills/speckit-<command>/` | `/speckit-specify` |
| Codex | `.agents/skills/speckit-<command>/` | `$speckit-specify` |

The first integration is the default. Extensions and presets register only for the default integration, so run `specify integration use codex` when Codex becomes the main agent for a project. In projects with many skills, `--integration-options="--no-model-invocation"` keeps the Spec Kit skills out of Claude's automatic skill listing until a user invokes them.

Review the generated diff and commit `.specify/`, the agent skill directories, and later `specs/` with the application, so every agent and reviewer sees the same artifacts.

## Map the workflow-first standards onto Spec Kit

Run each step in the agent's chat and review the result before continuing. The examples use Claude Code syntax; in Codex, replace `/` with `$`.

| Spec Kit step | What to bring from this repository |
| --- | --- |
| `/speckit-constitution` (once per project) | Seed it from [templates/SPEC_KIT_CONSTITUTION.md](templates/SPEC_KIT_CONSTITUTION.md), edited to the project's real stack and rules. |
| `/speckit-specify` | Describe the primary user workflow, its failure and recovery paths, roles and data boundaries, and desktop and mobile expectations. Leave technology choices for the plan. |
| `/speckit-clarify` | Use it for unresolved product decisions instead of guessing. Decisions that need the user stay with the user. |
| `/speckit-plan` | Name the stack and apply the skill's component selection order: existing components, the established source, a verified free registry component, then a small original component. Record source and license provenance. |
| `/speckit-checklist`, `/speckit-tasks`, `/speckit-analyze` | Make sure tasks include the type, unit, business-rule, and contract tests and the rendered checks in [references/verification.md](references/verification.md). |
| `/speckit-implement` | Invoke `/workflow-first-app-ui` (Codex: `$workflow-first-app-ui`) for interface tasks so implementation keeps the design system and business logic intact. |
| `/speckit-converge` | Repeat implement and converge until it reports `Converged`, then do the browser verification in [BROWSER_TESTING.md](BROWSER_TESTING.md). Convergence against the spec is not proof that the rendered workflow works. |

A short path (specify, plan, tasks, implement, converge) is fine for smaller features. Use the clarify, checklist, and analyze gates for production features.

## Use with the Chat-to-Claude handoff

Spec Kit artifacts and the handoff packet do different jobs. The spec, plan, and tasks describe the feature. The handoff describes the state of the workspace: what was set up, what commands ran, what failed, and what still needs authorization.

When the originating chat can run Spec Kit, it may complete the constitution and specification (and the plan, if the stack is decided) before handoff. The packet then points to the committed `specs/<feature>/` files instead of repeating them, and Claude Code continues from the next Spec Kit step. When it cannot, the handoff's objective and acceptance criteria are a good starting input for `/speckit-specify`.

## Boundaries

- Spec Kit artifacts are plans, not evidence. Report only tests and browser flows that actually ran.
- Keep constitution rules true to the project. Do not copy every default from this repository if the project has agreed otherwise.
- Spec Kit community extensions, presets, and catalogs are not audited by GitHub. Review their source before installing or running them, as with any dependency.
- Do not put secrets, customer data, or production identifiers in specs, plans, or constitutions; they are committed files. See [SECURITY.md](SECURITY.md).

---
name: workflow-first-app-ui
description: Take software from a short product request to a tested, handoff-ready application while preserving existing systems. Use for greenfield or existing app work that needs baseline research, implementation, UI quality, verification, and release discipline.
---

# Workflow-first application development

Turn the user's request into the smallest complete, credible application outcome. Prefer evidence and working software over speculative scaffolding. Preserve an existing system when one already exists.

## Start from project authority

Read applicable `AGENTS.md`, the dirty worktree, current architecture, package scripts, tests, design files, and recent acceptance evidence. Project rules and an implemented design system outrank this skill. Do not repeat completed, current, evidence-backed work.

Define the primary user workflow, acceptance criteria, non-goals, data and authorization boundaries, and the minimum proof needed. Ask only when a missing product choice would materially change the result.

Read [`references/development-standard.md`](references/development-standard.md) for the canonical lifecycle and stopping conditions.

## Research before greenfield code

Before selecting a stack or scaffolding a new system, inspect reusable local projects and credible existing repositories. Compare viable candidates against the actual workflow, license, maintenance, security posture, compatibility, accessibility, and cost of adoption. Popularity is supporting evidence, not proof of quality.

Record whether the candidate is a baseline, bounded donor, design reference, or rejected option. Never execute an unfamiliar installer or import a template before reviewing its license, scripts, dependencies, and architectural assumptions.

For the research record and credibility gate, read [`references/existing-system-research.md`](references/existing-system-research.md). For the verified "unslop" identification, read [`references/source-audit.md`](references/source-audit.md).

## Design around the real workflow

For user-facing work, inspect the current product before proposing a visual direction. Reuse existing components and tokens first; for compatible React projects, prefer the project's shadcn-compatible primitives before third-party code. Import the smallest useful unit and preserve routing, state, permissions, data ownership, and domain commands.

Operational interfaces should lead with current work, exceptions, and next actions. Make summaries traceable to the records behind them. Treat mobile as prioritization and reflow, not a scaled desktop. Include loading, empty, error, permission-limited, and recovery states. Do not invent metrics, testimonials, capabilities, or production readiness.

Read [`references/design-guide.md`](references/design-guide.md) for the portable design defaults and [`references/tool-routing.md`](references/tool-routing.md) before selecting an external design or verification tool. Use the installed design-review skill when its scope applies, and use browser inspection for rendered behavior; neither replaces application tests.

## Implement in bounded slices

Choose a thin vertical slice that reaches a user-visible or API-observable outcome. Keep business transitions in testable domain or service boundaries. Preserve compatibility deliberately. Add dependencies only when their benefit exceeds integration and maintenance cost.

When the project is not yet runnable, create only the baseline needed for the first workflow: package manifest, source and test structure, safe environment example, documented commands, smallest useful route or endpoint, and fictional fixtures. Do not fabricate credentials or connect production data.

## Prove the result

Run the checks that protect the changed behavior. A normal application gate includes relevant type, unit, business-rule, schema or contract, build, and lint checks. A UI change also needs a rendered primary workflow at representative desktop and mobile widths, keyboard and focus checks, console and failed-request inspection, and affected state coverage.

Live integrations require live staging or deployed evidence when that proof is in scope and authorized; local mocks do not prove an external service worked. Read [`references/verification.md`](references/verification.md) before substantial or release-bound work.

## Hand off or release

Report changed behavior, reused and external sources with license provenance, exact checks run, browser or live evidence, known risks, and unverified states. Keep commits focused and review the final diff for secrets and unrelated changes.

Prepare a branch and pull request when requested. Merging, production deployment, publishing, paid resources, external messages, and production data changes still require explicit authorization. Use [`references/portable-bootstrap.md`](references/portable-bootstrap.md) only for installation, cross-device setup, or a new handoff.

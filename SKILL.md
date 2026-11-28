---
name: workflow-first-app-ui
description: Design, extend, or audit React application interfaces while preserving existing workflows and design systems. Use when selecting reusable UI or dashboard components, integrating shadcn-compatible code, improving responsive UX, or validating an application UI.
---

# Workflow-First App UI

Improve the user's real workflow without replacing a design system they already value. Prefer a bounded integration over a template-driven rewrite.

## Establish the application boundary

Before changing code, inspect the project instructions, dirty worktree, framework and versions, styling system, shared components, design tokens, routes, primary workflows, business-rule tests, and existing acceptance evidence. Treat project-level rules and established components as authoritative.

When starting from an originating-chat handoff or preparing a new project, use [CHAT_TO_CLAUDE_HANDOFF.md](CHAT_TO_CLAUDE_HANDOFF.md) and [PROJECT_SETUP_CHECKLIST.md](PROJECT_SETUP_CHECKLIST.md) only when that setup context is relevant. If the project uses GitHub Spec Kit, treat its constitution and the current `specs/<feature>/` spec, plan, and tasks as the feature's requirements, and see [SPEC_DRIVEN_DEVELOPMENT.md](SPEC_DRIVEN_DEVELOPMENT.md). Do not repeat completed, evidence-backed preparation merely to follow a generic sequence.

Identify whether the task is:

- extending an existing interface;
- composing a new interface within an established system;
- adopting a dashboard or component source; or
- auditing usability, accessibility, and responsive behavior.

If the user likes the current UI, preserve its visual language and interaction model. Do not introduce a second design system merely because a source component looks polished in isolation.

## Select components in this order

1. Reuse or compose existing project components.
2. Use the project's established component source or official framework primitives.
3. Use a verified free component from a compatible registry.
4. Build a small original component that follows the existing tokens and APIs.

For source selection, read [references/component-sources.md](references/component-sources.md). Verify the current license and free/paid status before copying or installing code. Do not reproduce premium components from screenshots or previews. If the user supplies licensed source, integrate it without redistributing it.

Use full dashboard templates as references or bounded donors. Do not replace the application's routing, state, authorization, data model, or business logic with template assumptions.

## Design around workflows

Map the user's primary task before selecting UI. Make the next action, current context, exceptions, and recoverable errors easy to find. Summaries should lead to the records or work queues that produced them.

Carry useful context across related screens. Clear stale context when identity, tenant, branch, role, organization, or another security boundary changes.

Use compact layouts for operational software, while retaining labels, focus visibility, readable grouping, useful empty states, and reachable actions. Treat mobile as a prioritization and reflow problem, not a scaled-down desktop screenshot.

Read [references/lessons-learned.md](references/lessons-learned.md) when planning a substantial interface or dashboard change.

## Implement without semantic drift

- Reuse tokens for color, type, spacing, radius, focus, status, and motion.
- Adapt imported markup to existing component APIs and naming.
- Preserve domain commands, validation, authorization, audit history, and state transitions.
- Keep business transitions out of display-only components when the application already has a domain or service boundary.
- Use text with color for status. Preserve keyboard operation, accessible names, semantic structure, focus management, reduced motion, and error association.
- Avoid unnecessary dependencies. Inspect imported code and its transitive packages before accepting it.
- Replace demo data, claims, logos, testimonials, and metrics. Do not present placeholder content as real.

Use Hallmark for meaningful visual direction, design audits, accessibility, and responsive-quality review when its scope applies. Use the configured Playwright MCP server for interactive browser inspection, responsive checks, console review, and workflow verification. Keep type, unit, business-rule, schema-contract, and build checks responsible for repeatable code and domain correctness. See [BROWSER_TESTING.md](BROWSER_TESTING.md) for the shared browser standard.

## Verify the result

Run the checks that protect the changed behavior: type checks, unit tests, business-rule tests, schema or contract tests, and build checks as applicable. Browser checks complement these tests; they do not replace them.

Exercise at least one real primary workflow in the rendered application. Check representative desktop and mobile viewports, plus tablet when the product supports it or the layout risk warrants it. Inspect keyboard behavior, console errors, failed requests, loading, empty and error states, overflow, and preservation of important actions. Use fictional or isolated test data.

For substantial changes, read [references/verification.md](references/verification.md) and [BROWSER_TESTING.md](BROWSER_TESTING.md).

Report:

- what changed;
- which existing and external components were used;
- source and license provenance for imported code;
- tests and browser flows actually executed; and
- remaining risks or unverified behavior.

Do not claim accessibility, production readiness, or workflow completion from a static code scan alone.

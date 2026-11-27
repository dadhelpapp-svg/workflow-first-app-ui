# Spec Kit constitution seed

Use this as the input to `/speckit-constitution` (Codex: `$speckit-constitution`) in an application project that follows the workflow-first standards. See [SPEC_DRIVEN_DEVELOPMENT.md](../SPEC_DRIVEN_DEVELOPMENT.md).

Before running it, replace the bracketed placeholders, delete principles the project has not agreed to, and add the project's own rules from its README, contribution guide, CI configuration, and agent instructions. Do not invent standards to fill the template.

```text
/speckit-constitution Establish principles for [project name], a [kind of application] built with [framework, styling system, component source].

I. Workflow first. Every feature starts from a named primary user workflow, including its failure and recovery paths. Summaries lead to the records or work queues that produced them. Context carries across related screens and is cleared when identity, tenant, role, organization, or another security boundary changes.

II. Preserve the established design system. Reuse existing components and design tokens for color, type, spacing, radius, focus, status, and motion. Select components in this order: existing project components, the established component source or official framework primitives, a verified free component from a compatible registry, then a small original component that follows existing tokens and APIs. Do not introduce a second design system or replace routing, state, authorization, data model, or business logic with template assumptions.

III. Business logic is protected. Interface changes preserve domain commands, validation, authorization, audit history, and state transitions. Business transitions stay out of display-only components when a domain or service boundary exists. Functionality is never removed or weakened to satisfy subjective design advice.

IV. Accessible and responsive by default. Status uses text with color. Keyboard operation, accessible names, semantic structure, focus management, reduced motion, and error association are preserved. Mobile is a prioritization and reflow problem, not a scaled-down desktop layout.

V. Evidence before completion. Every plan names the type, unit, business-rule, schema or contract, and build checks that protect the changed behavior, plus at least one rendered primary-workflow check on desktop and mobile viewports using fictional or isolated data. Browser checks complement automated tests and never replace them. Completion reports list only checks that actually ran.

VI. Minimal, licensed dependencies. Add a dependency only when it is justified, after inspecting it and its transitive packages. Record source and license provenance for imported code. Do not reproduce premium components from screenshots or previews.

VII. Security boundaries. No secrets, credentials, customer data, or production identifiers in code, specs, plans, fixtures, or logs. No production mutation, publishing, or deployment without explicit authorization.

Project-level instructions and decisions recorded by the team take precedence over these defaults.
```

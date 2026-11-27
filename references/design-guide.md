# Portable application design guide

These defaults are inferred from repeated project decisions and corrections. An implemented project design system or explicit current request overrides them.

## Product and workflow

- Lead with the user's current work, exceptions, and next actions. A generic wall of metrics is not an operational dashboard.
- Make counts, balances, and statuses open the records or filtered queue that produced them.
- Carry useful task context between related screens. Clear it when identity, tenant, role, branch, organization, or another ownership boundary changes.
- Preserve business rules and state transitions during interface work. Visual polish must not hide actions or weaken state cues.
- Use one clear primary action per decision point. Keep secondary actions available without making them compete.

## System and components

- Reuse project components, tokens, and interaction patterns before adding dependencies.
- In compatible React applications, use existing shadcn-compatible primitives or official framework components as references before third-party kits.
- Import the smallest useful component. Adapt it to the host APIs, naming, tokens, and accessibility behavior.
- Use semantic tokens for color, type, spacing, radius, focus, status, and motion. Do not introduce a second visual system for one polished component.
- Treat full dashboards and templates as donors or references, not authority over routing, state, authorization, or data ownership.

## Layout and responsive behavior

- Keep operational software compact, with persistent labels, readable grouping, visible focus, and whitespace around decisions.
- Treat mobile as prioritization and reflow. Collapse secondary navigation, contain wide tables and calendars, and keep the primary action reachable.
- Cap and center broad content where appropriate. Let dense workspaces use available width without causing document-level horizontal overflow.
- Use cards for coherent tasks or record groups, not as decoration or nested containers for every section.

## States, copy, and trust

- Design loading, empty, error, disabled, permission-limited, success, and recovery states that the workflow can actually reach.
- Use text in addition to color for status. Explain disabled actions when the reason is not obvious.
- Write direct, human copy that names the action and recovery. Avoid technical error codes in user-facing messages when a useful explanation exists.
- Never invent metrics, testimonials, logos, capabilities, customer claims, or production readiness. Label mock and preview behavior accurately.

## Accessibility and motion

- Use semantic elements, persistent labels, accessible names, logical headings, scoped table headers, and predictable keyboard order.
- Every interactive element needs an immediate visible `:focus-visible` state. Dialogs need Escape, focus containment, and focus restoration.
- Keep touch targets usable, preserve zoom and reflow, avoid color-only meaning, and honor reduced motion.
- Verify contrast and behavior in the rendered application. A static scan is useful evidence but not a conformance claim.

## Design review tools

Use an installed project-approved design skill for visual direction or structured audit when its scope applies. Use Playwright or the configured browser tooling for interactive workflows, viewport checks, console output, and screenshots. Keep application tests responsible for repeatable domain and contract correctness.

When [Impeccable](https://github.com/pbakaus/impeccable) is explicitly approved and installed for the project, use its project context and narrow `critique`, `audit`, or detector passes as additional evidence for an existing interface. Pin or record the version, review its installer and hooks, and do not run live-edit mode against a deployed site or with bypassed safeguards. Impeccable findings do not replace browser workflows or business-rule tests.

When Hallmark is already installed and its scope applies, follow its own design and render gates. Do not run two broad redesign systems against the same screen without a clear role for each.

Optional third-party design tools must be reviewed and installed explicitly. They are not silent dependencies of this skill.

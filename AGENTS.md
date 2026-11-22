## Software design defaults

For software projects, prioritize clean, professional, functional UI/UX around the user's primary workflows. Prefer reusable components, consistent design tokens, clear information hierarchy, compact layouts, intuitive navigation, and responsive desktop/mobile behavior.

For compatible React applications, use Shadcn UI Kit as a component reference and reuse existing project components before adding new ones. Use the installed Hallmark skill for meaningful design work, design audits, accessibility, and responsive quality checks when its scope applies. Use the configured Playwright MCP server for interactive browser inspection, responsive checks, console review, and workflow verification.

Preserve business logic during interface changes. Validate meaningful changes with appropriate automated tests and observable UI checks. Browser checks complement rather than replace unit, business-rule, schema-contract, and type checks. Avoid unnecessary dependencies and unrelated changes. Never remove or weaken functionality merely to satisfy subjective design advice.

These are defaults, not mandatory technology choices. Project-level instructions and established project design systems take precedence.

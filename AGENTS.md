## Software design defaults

For software projects, prioritize clean, professional, functional UI/UX around the user's primary workflows. Prefer reusable components, consistent design tokens, clear information hierarchy, compact layouts, intuitive navigation, and responsive desktop/mobile behavior.

For compatible React applications, use Shadcn UI Kit as a component reference and reuse existing project components before adding new ones. Use the installed Hallmark skill for meaningful design work, design audits, accessibility, and responsive quality checks when its scope applies. Use the configured Playwright MCP server for interactive browser inspection, responsive checks, console review, and workflow verification.

Preserve business logic during interface changes. Validate meaningful changes with appropriate automated tests and observable UI checks. Browser checks complement rather than replace unit, business-rule, schema-contract, and type checks. Avoid unnecessary dependencies and unrelated changes. Never remove or weaken functionality merely to satisfy subjective design advice.

These are defaults, not mandatory technology choices. Project-level instructions and established project design systems take precedence.

## Chat-to-Codex handoff default

Before handing a software project to Codex, the originating chat should complete as much safe discovery, decision-making, and initial setup as its tools and authorization allow. For a new project, the minimum target is a coherent, runnable baseline with the framework, basic structure, scripts, environment example, smallest useful route or workflow, and baseline checks established.

The handoff should be compact and execution-ready so Codex can continue instead of repeating completed work. Follow [CHAT_TO_CODEX_HANDOFF.md](CHAT_TO_CODEX_HANDOFF.md) for the preparation checklist, required handoff packet, safety boundaries, and Codex starting behavior.

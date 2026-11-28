# Proportional quality gates

Choose the smallest set of checks that can credibly prove the requested outcome. Run existing project commands first; do not invent a parallel test stack without a demonstrated gap.

## Gate matrix

| Change | Required evidence |
| --- | --- |
| Documentation or skill | Repository validator, skill validator, link check, helper syntax, reviewed rendered Markdown where layout matters |
| Domain or business rule | Type check, focused unit and regression tests, boundary validation, unchanged compatibility cases |
| API, schema, or persistence | Contract and schema tests, migration or policy execution in a safe environment, retry and failure behavior |
| User interface | Type and build checks, affected component tests, rendered primary workflow, desktop and mobile, keyboard and focus, console and failed requests |
| External integration | Deterministic local tests plus safe live staging or deployed evidence when authorized; returned IDs, metadata, or observable remote state |
| Release candidate | Relevant gates above, final diff and secret review, source and license provenance, CI result, known risks and rollback path |

## Browser workflow

Use the configured Playwright MCP server for interactive inspection when it is available. Use Playwright Test or the project's browser suite for repeatable regression coverage. [`BROWSER_TESTING.md`](../BROWSER_TESTING.md) covers setup for Claude Code and Codex, tool boundaries, and the reporting standard.

1. Confirm the URL, environment, test account, data policy, and allowed mutations.
2. Verify the expected heading or landmark, not only HTTP status.
3. Exercise the primary workflow from entry to a committed or clearly simulated result.
4. Check validation, cancel, recovery, disabled, loading, empty, error, and success states affected by the change.
5. Check a typical desktop width and a narrow mobile width; add tablet when layout risk or product support warrants it. Check dark mode or alternate themes when supported.
6. Verify keyboard order, visible focus, Escape and focus return for dialogs, and reachable primary actions.
7. Inspect console errors, failed requests, overflow, fixed overlays, and reload or persistence behavior when relevant.
8. Re-run the risk-sensitive path after fixes and report the exact environment, interactions, viewport sizes, and untested states.

Accessibility snapshots and static scanners are supporting evidence, not a complete WCAG audit. Screenshots support review but do not create a maintained visual-regression baseline.

## Live proof boundary

Do not infer live success from local tests. For a deployed script, database, storage system, payment provider, email service, or other external platform, credible proof includes the actual deployed endpoint or version, the request made with safe data, returned metadata, and inspection of the resulting remote state. If access or authorization is missing, report the live gate as unverified.

## Reporting

Separate:

- checks that passed;
- checks that failed before the change;
- checks that failed because of the change;
- checks skipped and the reason; and
- live or production behavior that remains unverified.

Do not call the application production-ready from a static scan, a local scaffold, or one happy-path browser click.

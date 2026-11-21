# Rendered verification guide

Use the smallest set of checks that provides credible evidence for the changed workflow.

## Before browser verification

- Run type checking and the relevant unit, domain, schema, and contract tests.
- Build the application when bundling, routing, or server/client boundaries changed.
- Confirm that test data is fictional or isolated.

## Primary workflow

Exercise the user's real path from entry to a committed or clearly simulated outcome. Include validation and recovery, not only the happy-path page load. Confirm that navigation preserves the intended context and clears it at scope boundaries.

## Viewports and input

- Check a typical desktop viewport.
- Check a narrow mobile viewport.
- Check keyboard navigation, visible focus, Escape and focus return for modal paths, and reachable primary actions.
- Inspect horizontal overflow, table/calendar containment, sticky regions, and fixed overlays.

## States

Check the states affected by the change:

- loading and delayed data;
- empty results;
- validation and server errors;
- disabled and permission-limited actions;
- success confirmation and durable resulting state; and
- dark mode or alternate themes when supported.

## Runtime evidence

Inspect console errors and failed network requests. A static accessibility or design scan is useful evidence, but it cannot prove rendered focus behavior, responsive reflow, or a complete workflow.

Report the commands, viewport sizes, workflow steps, and any untested behavior.

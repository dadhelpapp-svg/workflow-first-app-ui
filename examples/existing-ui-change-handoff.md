# Example: existing application UI change handoff

This fictional example shows how to prepare an existing application without replacing its design system or business workflow.

## Objective

Add a compact overdue-invoices summary to the existing billing page and let an operator open the filtered invoice list.

## Acceptance criteria

- The summary uses existing cards, status tokens, and navigation APIs.
- Clicking the overdue count opens the invoice list with the overdue filter applied.
- Authorization and invoice-state rules remain unchanged.
- Existing business-rule tests and the new navigation test pass.

## Starting point

- Repository: `example/operations-app`
- Worktree: `worktrees/overdue-summary`
- Starting commit: `89abcde`
- Project instructions: root `AGENTS.md` and `docs/billing-rules.md`

## Decisions already made

- Extend `MetricCard`; do not import a dashboard template.
- Derive the count through the existing invoice query service.
- Carry the filter through the route's documented search parameters.

## Setup completed

- Identified the billing page, shared metric component, invoice query service, route schema, and relevant tests.
- Added a fictional overdue-invoice fixture without changing production configuration.
- Confirmed the unchanged baseline before implementation.

## Evidence

| Check or command | Result |
| --- | --- |
| `npm run typecheck` | Passed |
| `npm test -- billing --run` | Passed, 18 tests |
| `npm run build` | Passed |

## Relevant project areas

- `src/pages/billing/overview.tsx` - target composition
- `src/components/metric-card.tsx` - existing reusable UI
- `src/domain/invoices/query.ts` - approved data boundary
- `src/routes/invoices.search.ts` - filter schema

## Remaining work

1. Add the overdue metric through the existing composition and query service.
2. Add route-search navigation coverage.
3. Verify keyboard behavior, desktop/mobile reflow, and console output in the rendered app.

## Constraints and safety boundaries

- Do not modify invoice transition rules or authorization.
- Do not send notifications or mutate invoice data.
- Preserve the current UI density and token usage.

## Known risks and unverified behavior

- The narrowest supported viewport needs rendered verification after the metric is added.

## User input still required

None.

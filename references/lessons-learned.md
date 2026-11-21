# Reusable application UI lessons

These lessons are generalized from a workflow-heavy application. They do not carry over that application's domain rules, names, policies, or data.

## Workflow and information hierarchy

- Start with the user's current work, exceptions, and next actions. A generic wall of metrics rarely serves an operational dashboard.
- Make summary values traceable. A count, balance, or status should open the filtered records that explain it.
- Carry task context between related screens to avoid repeated search.
- Clear context at security or ownership boundaries so convenience does not leak scope.
- Separate concepts that answer different questions. Do not merge money streams, workflow states, permissions, or ownership merely because they appear together on one screen.

## Interaction and responsive design

- Keep operational layouts compact, but preserve persistent labels, focus visibility, touch targets, error recovery, and whitespace around decisions.
- Treat mobile as prioritization. Reflow work, collapse secondary navigation, contain wide tables and calendars, and keep the primary action reachable.
- Use selection styling for state and primary styling for commands. Derive the visual state and ARIA state from the same source of truth.
- Use text in addition to color for status. Explain disabled actions when the reason is not obvious.
- Preserve Escape behavior, focus traps and restoration, keyboard order, zoom/reflow, and reduced-motion handling.

## Architecture and correctness

- Keep business transitions in testable domain or service functions rather than hiding them in presentation code.
- For monetary applications, prefer integer minor units and explicit allocation or ownership records.
- Use stable identifiers, immutable state transitions, idempotency where retries are possible, and append-only correction history where auditability matters.
- Preserve legacy behavior behind explicit compatibility boundaries instead of silently rewriting old records.
- Label mock, preview, planned, connected, and production behavior accurately.

## Evidence

- Add focused regression tests for repaired authorization, accounting, state-transition, branch or tenant, and idempotency defects.
- Test a meaningful end-to-end workflow after unit and type checks.
- Use fictional, isolated browser data. Test reload and persistence separately.
- Record exactly what passed, failed, or remained untested. A local scaffold is not proof of a live backend or production authorization.

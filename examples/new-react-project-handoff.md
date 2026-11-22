# Example: new React project handoff

This fictional example demonstrates the expected level of preparation. Commands and versions must be adapted to the real project.

## Objective

Create a responsive internal appointment dashboard where a coordinator can see today's queue and open an appointment record.

## Acceptance criteria

- The dashboard shows loading, empty, populated, and recoverable error states.
- Selecting an appointment opens its detail route without losing the current queue filter.
- Type checks, unit tests, and the production build pass.
- The primary flow is verified at desktop and mobile viewports with no application console errors.

## Starting point

- Repository: `example/appointment-dashboard`
- Branch: `main`
- Starting commit: `0123456`
- Project instructions: root `AGENTS.md`

## Decisions already made

- Vite, React, and TypeScript were selected because this is a client-only internal application.
- Existing shadcn-compatible components will be reused before adding another component source.
- Appointment data remains behind a typed repository interface so a mock can be replaced later.

## Setup completed

- Initialized the project and package manifest.
- Added the application shell, dashboard route, typed appointment model, and fictional fixture.
- Added development, type-check, test, build, and lint scripts.
- Added `.env.example` with names only; no credentials are present.

## Evidence

| Check or command | Result |
| --- | --- |
| `npm install` | Passed |
| `npm run typecheck` | Passed |
| `npm test -- --run` | Passed, 4 tests |
| `npm run build` | Passed |

## Relevant project areas

- `src/app/` - application shell and routing
- `src/features/appointments/` - workflow UI and domain types
- `src/test/fixtures/appointments.ts` - fictional test data

## Remaining work

1. Implement the appointment queue composition using existing components.
2. Add loading, empty, error, and selected-row behavior.
3. Add workflow tests and complete Playwright MCP desktop/mobile verification.

## Constraints and safety boundaries

- Do not connect to production scheduling data.
- Preserve the existing token and component conventions.
- Do not add a second routing or state-management library.

## Known risks and unverified behavior

- The real API contract has not been supplied; keep the repository boundary replaceable.

## User input still required

None for the bounded mock-data implementation.

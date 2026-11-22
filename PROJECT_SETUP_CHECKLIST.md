# Minimum project setup checklist

Use this checklist before handing a new software project to Codex. Mark only work that was actually completed and record failures in the handoff.

## Scope

- [ ] Objective, primary workflow, constraints, non-goals, and acceptance criteria are written down.
- [ ] The intended repository, branch, or worktree is identified.
- [ ] Project-level instructions and the chosen stack are recorded.
- [ ] Material assumptions and decisions requiring user input are explicit.

## Runnable baseline

- [ ] Framework and package manifest are initialized.
- [ ] Source, configuration, and test directories follow the chosen framework's conventions.
- [ ] Development, type-check, test, build, and formatting or lint commands exist when applicable.
- [ ] An environment-variable example exists without real credentials.
- [ ] The smallest useful route, shell, endpoint, or workflow runs.
- [ ] Only justified dependencies are installed.
- [ ] Generated demo claims, credentials, and misleading placeholder data are removed or clearly labeled.

## Product and interface foundation

- [ ] Existing components, tokens, routes, and design-system rules were inspected before adding alternatives.
- [ ] The primary user workflow and important failure or recovery path are represented.
- [ ] Desktop and mobile layout expectations are recorded for interface work.
- [ ] Data ownership, validation, authorization, and side-effect boundaries are documented.

## Verification baseline

- [ ] Dependency installation completed successfully.
- [ ] Type checks pass, or the exact existing failure is recorded.
- [ ] Unit, business-rule, and schema-contract tests pass where applicable.
- [ ] The project builds or the development server starts.
- [ ] A rendered smoke check was completed for a user-facing application.
- [ ] Test data is fictional or isolated from production.

## Handoff quality

- [ ] The handoff uses [`templates/CODEX_HANDOFF.md`](templates/CODEX_HANDOFF.md).
- [ ] Exact commands and results are included.
- [ ] Relevant files and remaining bounded tasks are identified.
- [ ] Known risks, unverified behavior, and required authorization are explicit.
- [ ] The workspace is coherent and does not contain an unexplained half-applied change.

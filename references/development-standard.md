# Canonical development standard

This is the single maintained lifecycle for the skill. Supporting references add conditional detail; they do not redefine the sequence or authorization boundaries here.

## 1. Establish the outcome

Translate the request into:

- one primary user or operator workflow;
- observable acceptance criteria;
- relevant business, data, security, and compatibility invariants;
- non-goals and actions that need separate authorization; and
- the evidence required to call the work complete.

Inspect the repository, project instructions, current branch and changes, architecture, design system, dependencies, test commands, and recent evidence. An existing system is the default starting point. Do not rebuild it merely because a clean scaffold is easier to understand.

## 2. Reuse before creating

For an existing project, trace the workflow through its current routes, components, domain functions, integrations, and tests before editing.

For a substantial feature whose requirements are still ambiguous, a written specification may come first; if the project uses GitHub Spec Kit, follow [`../SPEC_DRIVEN_DEVELOPMENT.md`](../SPEC_DRIVEN_DEVELOPMENT.md).

For a new project, complete the research gate in [`existing-system-research.md`](existing-system-research.md) before selecting a framework or generating code. Local reusable systems come first, followed by official framework starters and credible maintained repositories. Record whether each useful source is a baseline, bounded donor, or design reference.

The gate may conclude that no candidate fits. That is a valid result when the comparison and reasons are recorded. It is not permission to skip research.

## 3. Prepare the smallest runnable baseline

Preserve the project's package manager and conventions. For a genuinely new system, add only what the first workflow needs:

- package manifest and pinned runtime expectations;
- conventional source, configuration, and test structure;
- safe environment-variable example with names but no secrets;
- development, type, test, build, and lint or formatting commands as applicable;
- the smallest useful route, endpoint, command, or workflow; and
- fictional or isolated fixtures.

Run the unchanged or newly prepared baseline before feature work. Record existing failures instead of absorbing unrelated repairs into the task.

## 4. Design the workflow and boundaries

Identify state ownership, validation, authorization, side effects, failure recovery, and external interfaces. Keep presentation code from becoming the only home of business rules. Preserve stable identifiers, compatibility behavior, audit history, and idempotency where retries are possible. For monetary values, prefer integer minor units and explicit allocation or ownership records.

For user-facing work, apply [`design-guide.md`](design-guide.md). Reuse implemented tokens and components. External UI sources are bounded donors, not replacements for routing, data models, authentication, or domain commands.

## 5. Implement a thin vertical slice

Prefer a small end-to-end outcome over a wide layer of placeholders. Keep changes focused and reversible. Add a dependency only after checking its license, maintenance, install scripts, transitive cost, compatibility, and whether existing code already solves the problem.

Use explicit labels for mock, preview, connected, and production behavior. Do not invent claims, metrics, testimonials, policy, or credentials. Never weaken business logic, validation, authorization, or existing functionality to make a UI or test appear complete.

## 6. Verify proportionately

Use [`verification.md`](verification.md) to select gates. At minimum, test the changed business behavior at its lowest practical layer, run the repository's relevant checks, and exercise the primary outcome through its real interface.

Rendered browser checks complement type, unit, business-rule, schema, and contract tests. Local fixtures do not prove a deployed service, external API, Apps Script, database policy, or production authorization. When live proof is required, use a safe environment and record the returned artifact or observable state.

## 7. Review the release boundary

Before commit or handoff:

- inspect the diff for unrelated changes, generated noise, secrets, personal data, and stale debug code;
- record external source, version or commit, license, attribution, copied files, and added dependencies;
- confirm documentation and examples match the implementation;
- distinguish new failures from pre-existing failures; and
- state what remains unverified.

Use a feature branch and open a pull request when requested. A request to implement or open a PR does not authorize merge, production deployment, publishing, paid resources, external messages, or production data mutation. Those actions require explicit authorization.

## 8. Handoff without rediscovery

Use the project brief and the [handoff standard](../CHAT_TO_CLAUDE_HANDOFF.md) and [template](../templates/CLAUDE_HANDOFF.md) when work crosses devices or conversations. Include the starting commit, exact commands and results, changed behavior, relevant paths, remaining bounded tasks, risks, and approval-gated actions. Prefer links to committed project files over copying large instruction blocks.

Completion means the acceptance criteria are met with recorded evidence and no required work remains. A scaffold, static scan, or passing unit suite alone is not a working application.

# Chat-to-Codex project handoff

The originating chat should complete as much safe, useful preparation as its available tools allow before handing work to Codex. The goal is to conserve implementation tokens, remove avoidable ambiguity, and let Codex begin from a working baseline instead of repeating discovery.

This is a minimum standard, not a reason to delay urgent fixes or pretend unverified setup is complete.

## Before the handoff

The originating chat should:

1. Clarify the objective, primary user workflow, constraints, non-goals, and observable acceptance criteria.
2. Inspect the target repository, project instructions, current branch or worktree, existing components, dependencies, tests, and relevant documentation.
3. Resolve ordinary product and technical choices that can be decided from available evidence. Record any material assumption that remains.
4. For a new project, complete the minimum safe bootstrap when tools and authorization allow:
   - create or select the intended repository or worktree;
   - initialize the chosen framework and package manifest;
   - establish the basic source, configuration, and test structure;
   - add development, type-check, test, build, and formatting or lint commands as applicable;
   - add an environment-variable example without real secrets;
   - create the initial route, shell, or smallest runnable workflow;
   - install only justified dependencies; and
   - run the baseline checks and confirm the application can start or build.
5. For an existing project, preserve its architecture and prepare the exact files, routes, components, fixtures, or issue context Codex will need.
6. Gather reusable source material, screenshots, designs, API contracts, sample data, and license information when they are relevant and permitted.
7. Leave the workspace in a coherent state. Do not hand off a half-applied dependency change or an unexplained failing baseline.

Do not fabricate credentials, copy secrets into prompts or repositories, mutate production data, publish or deploy without authorization, or make a consequential product decision that requires the user.

## Required handoff packet

Provide Codex with a compact, execution-ready handoff containing:

- the objective and acceptance criteria;
- the repository, branch or worktree, and starting commit when applicable;
- project instructions and important constraints;
- decisions already made and their reasons;
- setup already completed;
- exact commands that were run and their results;
- relevant files, routes, components, APIs, and data boundaries;
- the remaining bounded implementation tasks;
- known failures, risks, and unverified behavior; and
- any action that still needs user authorization or input.

Prefer references to committed files over pasting large duplicated content. Include exact error text only when it helps Codex continue.

## Codex starting behavior

Codex should treat a current, evidence-backed handoff as the starting point and avoid repeating completed discovery or setup. It should verify the prepared baseline proportionately, inspect anything stale or contradictory, then continue implementation, testing, and rendered workflow verification.

If the originating chat cannot perform part of the minimum setup, it should say exactly why and hand off the smallest clearly defined remaining setup task.

# Portable bootstrap and handoff

## Install or update the skill

Clone the repository into the Codex skills directory on each device, or run the platform helper in `scripts/`. The helpers only fast-forward an existing checkout; they do not overwrite divergent local changes.

After installation or update:

1. run `python scripts/validate_repo.py` inside the installed skill;
2. restart Codex so the skill inventory refreshes; and
3. invoke `$workflow-first-app-ui` from the target project.

Project-local installation is appropriate when a team needs a pinned version. Commit the chosen reference or submodule intentionally; do not let every machine silently pull a moving default branch during a build.

## Bootstrap a project

Run:

```sh
python /path/to/workflow-first-app-ui/scripts/bootstrap_project.py /path/to/project
```

The helper copies `templates/PROJECT_BRIEF.md` when absent and idempotently adds a marked workflow-first block to `AGENTS.md`. Existing project instructions are preserved. Complete the brief before greenfield code so the research decision and acceptance evidence travel with the project.

Run this in local setup or CI to make a missing reference fail visibly:

```sh
python /path/to/workflow-first-app-ui/scripts/bootstrap_project.py /path/to/project --check
```

The reference has two layers: install the skill at the stable `workflow-first-app-ui` path on each device, then commit the managed `AGENTS.md` block in each project. Restart Codex after a skill update. Project-local rules still take precedence.

## Cross-device continuity

Commit project-owned decisions, commands, and evidence. Do not rely on one chat's hidden context. A useful continuation record includes:

- objective, workflow, acceptance criteria, and non-goals;
- repository, branch or worktree, and starting commit;
- project instructions and architecture or design authority;
- baseline research and source provenance;
- setup completed and exact checks with results;
- changed and relevant paths;
- remaining bounded tasks, risks, and unverified behavior; and
- actions that still need user authorization.

Use [`../templates/CODEX_HANDOFF.md`](../templates/CODEX_HANDOFF.md) when another conversation or device will continue active work.

## Release boundary

Branch creation, commits, pushes, and a pull request may be performed when the user requests them. Merge, deployment, publishing, paid resources, external communication, and production data changes require explicit authorization at the point of action.

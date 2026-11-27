# Repository instructions

This repository packages the `$workflow-first-app-ui` Codex skill. Keep this file small; the canonical lifecycle is in [`references/development-standard.md`](references/development-standard.md).

- Preserve project history, user intent, business rules, and authorization boundaries.
- Before greenfield code, inspect local systems and compare credible maintained baselines. Record the choice or why none fits.
- Reuse an established design system and components before adding alternatives.
- Keep conditional detail in focused references, not in this file or duplicated across documents.
- Validate changes with `python scripts/validate_repo.py` and the skill validator.
- Do not merge, deploy, publish, or mutate production without explicit authorization.

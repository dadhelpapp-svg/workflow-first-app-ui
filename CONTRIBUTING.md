# Contributing

Contributions should improve workflow-centered application work without expanding the skill into a generic software manual.

## Propose a change

1. Explain the real task or failure the change addresses.
2. Keep `SKILL.md` concise. Put conditional detail in a focused reference, template, example, or deterministic script.
3. Preserve project authority, user intent, business logic, and authorization boundaries.
4. Do not include premium source code, credentials, production data, customer information, or copied material without redistribution rights.
5. Update `CHANGELOG.md` for a user-visible change and `VERSION` for a release.

## Component-source changes

For a new or changed source, record:

- the canonical source and repository URLs;
- the date reviewed;
- the observed free, paid, or mixed status;
- the repository license and any attribution requirement; and
- limitations that change integration decisions.

A review date is not a permanent guarantee. The skill must continue to require item-level source and license verification before reuse.

## Validate

Run:

```sh
python scripts/validate_repo.py
```

Also syntax-check changed helper scripts and manually review instructions for clarity, duplication, and unintended authority. Pull requests should state what was tested and what remains unverified.

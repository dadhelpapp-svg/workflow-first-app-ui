# Security and privacy

## Reporting a vulnerability

Do not open a public issue containing an active secret, private customer data, or exploitable details. Use GitHub's private vulnerability reporting feature when it is available for this repository, or contact the repository owner privately.

## Safe project preparation

- Never place real secrets in prompts, examples, fixtures, screenshots, logs, commits, or `.env.example`.
- Use environment-variable names and clearly fictional values in documentation.
- Use isolated test accounts and synthetic data. Do not automate a production login profile.
- Confirm authorization before publishing, deploying, sending messages, changing access, mutating production data, or creating paid resources.
- Remove or redact customer names, tokens, internal URLs, account identifiers, and sensitive console or network output from evidence.
- Treat browser automation as an authenticated operator, not as a security boundary.
- Review copied dependencies and source for licensing, install scripts, transitive packages, and suspicious network behavior.
- Keep generated files and temporary artifacts out of commits unless they are intentional deliverables.

## Before handing work to Claude Code

- State which environments and data are allowed.
- Identify forbidden or approval-gated actions.
- Record whether browser interactions may create or modify data.
- Confirm that the baseline repository contains no known secret material.
- Include security-relevant failures without pasting the sensitive value itself.

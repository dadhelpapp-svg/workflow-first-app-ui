# Source audit and evidence limits

Last verified: 2026-11-27.

## The intended "unslop" repository

The clue "from Google" and "about 100k stars" points to [pbakaus/impeccable](https://github.com/pbakaus/impeccable), not a repository named Unslop.

- Owner: Paul Bakaus (`pbakaus`); his [GitHub profile](https://github.com/pbakaus) lists Google and identifies him as the creator of jQuery UI and Google for Creators.
- Observed popularity: 117,799 GitHub stars at verification time.
- License: [Apache-2.0](https://github.com/pbakaus/impeccable/blob/main/LICENSE).
- Scope: design vocabulary, critique and audit commands, and deterministic UI checks for coding agents.

[heydamir/unslop](https://github.com/heydamir/unslop) is a different project:

- Owner: Damir Sokolovsky (`heydamir`).
- Observed popularity: approximately 22,500 GitHub stars at verification time.
- License: [CC BY 4.0](https://github.com/heydamir/unslop/blob/main/LICENSE), which requires attribution when shared or adapted.
- Scope: an audit-and-redesign skill for existing AI-looking interfaces.

This repository does not copy either project's instructions or install either tool automatically. Impeccable may be evaluated as an optional project tool. Review its current installer, hooks, runtime behavior, license, and version before use. The existing installed design-review tooling remains the default when it is already approved and fits the task.

## Audit coverage

The consolidation reviewed the target repository's full Git history and all 11 repositories exposed by the connected GitHub installation. One accessible repository was empty. Private repository names, customer or business details, and private source were not copied into this public skill.

Relevant prior Codex threads and local memory indexes were reviewed for recurring development corrections. Evidence consistently favored:

- inspecting and preserving the current system before edits;
- existing components first and bounded shadcn-compatible reuse;
- compact workflow-led operational interfaces;
- explicit desktop and mobile browser proof;
- unit and business-rule tests in addition to UI checks;
- accurate distinction between local scaffolds and live integrations;
- short, exact handoffs that preserve context across chats and devices; and
- explicit approval for deployment and other production mutations.

These are generalized defaults, not copied domain rules. Project-specific clinical, payroll, legal, customer, or financial behavior stays in its source project.

## Inaccessible or incomplete evidence

- The referenced prior ChatGPT conversation contained only the initial request and no assistant decisions.
- Deleted chats, unavailable attachments, unindexed private code, external accounts not connected to Codex, and local files outside the authorized accessible sources were not available.
- Repository popularity and licenses can change. Re-check current metadata before adopting an external source.

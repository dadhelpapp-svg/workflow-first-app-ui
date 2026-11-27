# Existing-system research gate

Use this reference before greenfield scaffolding, a major framework change, or adoption of a large external template.

## Research record

Write a short record in `PROJECT_BRIEF.md` or the project's decision log:

1. **Need:** primary workflow, users, platform, constraints, and non-goals.
2. **Local candidates:** current project, sibling repositories, shared packages, templates, and previously proven patterns.
3. **External candidates:** two to four official starters or credible repositories when viable alternatives exist.
4. **Comparison:** fit, maintenance, license, security, compatibility, accessibility, dependency cost, and adoption effort.
5. **Decision:** baseline, bounded donor, design reference, or rejected; include the reason and exact version or commit.

Do not search for an external repository when the task is a bounded change to an established system and the existing implementation already supplies the needed pattern.

## Credibility gate

A repository is a credible candidate when the evidence is proportionate to the risk:

- the owner or organization is identifiable;
- the license permits the intended use and any attribution is understood;
- recent releases, commits, issue handling, or security notices show active stewardship;
- documentation and tests support the claimed behavior;
- the stack and versions are compatible with the target project;
- install and build scripts have been inspected before execution;
- the dependency tree and network or credential behavior are acceptable; and
- its architecture can be adopted without discarding the target workflow.

Stars, forks, and social attention may help find candidates, but they are weak evidence on their own. A high star count does not resolve license, security, maintenance, accessibility, or product-fit questions.

## Adoption modes

- **Baseline:** start from the repository because its architecture and license fit the whole first workflow.
- **Bounded donor:** copy or adapt a small, reviewed unit with provenance.
- **Design reference:** learn from interaction and composition without copying source.
- **Rejected:** record the concrete mismatch so later work does not repeat the evaluation.

Avoid full-template adoption when it would import unrelated routing, authentication, data shapes, state management, or visual language. Prefer the smallest useful unit.

## Minimum evidence before code

The research gate passes when the record names the sources checked, the current license and version or commit for the chosen source, the adoption mode, the known risks, and why the choice is better than a small original implementation. If no source fits, record why and proceed with a bounded original baseline.

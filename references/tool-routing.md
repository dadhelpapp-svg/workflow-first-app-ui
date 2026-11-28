# Design and verification tool routing

Use external tools by role. Do not install several broad visual-direction systems and let them compete over the same interface. Project instructions and an implemented design system remain authoritative.

Last reviewed: 2026-11-27. Repository activity, stars, licenses, pricing, and install behavior can change; verify them again before adoption.

| Source | Decision | Appropriate role | Important boundary |
| --- | --- | --- | --- |
| [Vercel Web Design Guidelines](https://github.com/vercel-labs/agent-skills) | Core, conditional | Code-level web UI, accessibility, and usability review when that audit is in scope | Review guidance, not a generative design system or a substitute for rendered testing. Use the installed copy and refresh its current rules as its own instructions require. |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | Core verification | Exercise real workflows, responsive viewports, keyboard behavior, console output, requests, and screenshots | Browser evidence complements unit, domain, schema, contract, type, and build checks; it does not replace them. |
| [Impeccable](https://github.com/pbakaus/impeccable) | Preferred optional audit and polish tool | Narrow critique, audit, polish, and detector passes on an existing interface | Pin or record the version and review installers, hooks, telemetry, and automation behavior. Do not use live-edit mode on a deployed site or bypass normal safeguards. |
| [Awesome Design MD](https://github.com/VoltAgent/awesome-design-md) | Optional reference library | Compare documented visual systems and derive a project-owned `DESIGN.md` | Treat brand files as references. Do not blindly copy another company's identity, trademarks, or product-specific rules. |
| [Unslop](https://github.com/heydamir/unslop) | Explicit-use redesign aid | Structured diagnosis and redesign of an existing generic-looking interface | Its CC BY 4.0 license requires attribution. It overlaps broad redesign tools, so select it deliberately instead of stacking it with Hallmark, Taste Skill, or an Impeccable redesign pass. |
| [Taste Skill](https://github.com/Leonxlnx/taste-skill) | Optional visual-direction system | Greenfield marketing or company sites that need an explicitly chosen art direction | Broad scope, hooks, runtime requirements, and a large asset surface make it unsuitable as a silent global default. Review and pin before installation. |
| [Transitions](https://github.com/Jakubantalik/transitions.dev) | Conditional motion specialist | A project that specifically needs transition design or bounded motion recipes | Honor reduced motion. Verify the free/Pro boundary and redistribution terms. Hosted source-fix services require explicit approval and a privacy review. |
| [BoardUI](https://github.com/BoardUI/boardui) | Conditional baseline or component donor | New Next.js and Tailwind v4 dashboards or agentic interfaces whose stack matches | It is a UI library with free and paid surfaces, not universal project authority. Verify the exact item and do not introduce a second component system into an established application. |

## Selection rule

Use at most one broad visual-direction or redesign system for a screen. Hallmark, Taste Skill, Unslop, and broad Impeccable redesign work occupy that role. The Vercel review rules and Playwright verification may complement the selected direction because they serve different roles.

Before installing or copying from an external source, record its current commit or version, license and attribution, maintenance activity, relevant scripts or hooks, dependency and stack compatibility, accessibility assumptions, paid boundaries, and the exact files or commands adopted. Do not silently install any source listed here.

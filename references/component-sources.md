# Free component and dashboard sources

Use this list as a discovery aid, not as a permanent license guarantee. Before copying or installing an item, open its current source page and repository license. Confirm that the exact item is free; some catalogs mix free components with paid blocks.

Last reviewed: 2026-11-27. This review confirmed the linked source was reachable and recorded the status presented by the source on that date. It is not a permanent license guarantee.

## Preferred order

| Source | Best use | Review snapshot | Integration notes |
| --- | --- | --- | --- |
| [Official shadcn/ui](https://ui.shadcn.com/) | Accessible primitives, forms, navigation, sidebars, charts, tables, and official blocks | Public MIT repository | Best default for a compatible React project. Source is copied into the project. Prefer official blocks before third-party templates. |
| [Shadcn UI Kit free repository](https://github.com/bundui/shadcn-ui-kit) | Free variants, a starter dashboard, and bounded blocks | Public repository identifies itself as the free version and displays an MIT license | Use only files present in the public repository or registry. Do not infer that a previewed premium item is free. |
| [dashboardcn](https://dashboardcn.com/) | Data-heavy dashboard components and analytics | Site states its components are free, MIT licensed, and have no Pro tier | Designed to inherit an existing shadcn theme. Still verify the exact registry item before integration. |
| [ReUI](https://reui.io/) | Advanced controls such as data grids, filters, calendars, trees, timelines, Kanban, and Gantt patterns | Mixed catalog of free components and paid Pro blocks | Confirm the exact item exposes free source or a public registry entry. Do not treat the entire catalog as free. |
| [Dashral](https://github.com/hasral/dashral) | Motion-aware metrics, charts, blocks, and a dashboard reference | Public repository presents free blocks and an MIT license | Use public repository files covered by the current license. Adapt motion to reduced-motion preferences and the host application's visual language. |
| [Shadcn Dashboard](https://github.com/shadcndashboard/shadcndashboard) | Full Vite/React dashboard reference | Public repository describes a free open-source dashboard and displays an MIT license | Treat as a donor or reference for bounded pages. Check current attribution language as well as the license. |
| [Tremor](https://npm.tremor.so/) | Charts, KPI displays, trackers, and analytics | Site presents its React components as open source; templates and blocks are separate offerings | It has its own conventions. Verify the exact package or block and prefer adapting individual visualization patterns instead of importing a competing design system wholesale. |
| [BoardUI](https://github.com/BoardUI/boardui) | Next.js and Tailwind v4 dashboards and agentic interface patterns | Public MIT repository; its catalog includes free and Pro surfaces | Use only when the project stack and visual system match. Verify the exact item is free or covered by the user's license and prefer bounded components over a wholesale design-system replacement. |

The official [shadcn registry directory](https://ui.shadcn.com/docs/registry) can help find additional registries. Community code still needs source review, maintenance review, and license verification.

## Acceptance gate for external code

Before integration, record:

- source URL and repository commit or package version;
- license file and any attribution requirement;
- whether the exact item is free, paid, or supplied under the user's license;
- framework, React, Tailwind, primitive, and icon compatibility;
- added runtime and development dependencies;
- accessibility behavior and responsive assumptions; and
- files copied or commands executed.

Reject or reimplement an original solution when the source has an unclear license, requires copying from a premium preview, conflicts with the current stack, or would force a broad rewrite.

## Template boundary

A template may contain useful layout and composition ideas but also embeds assumptions about routes, authentication, data shape, permissions, and state. Import the smallest useful unit. Keep the host application's domain commands and security boundaries intact.

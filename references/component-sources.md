# Free component and dashboard sources

Use this list as a discovery aid, not as a permanent license guarantee. Before copying or installing an item, open its current source page and repository license. Confirm that the exact item is free; some catalogs mix free components with paid blocks.

## Preferred order

| Source | Best use | Integration notes |
| --- | --- | --- |
| [Official shadcn/ui](https://ui.shadcn.com/) | Accessible primitives, forms, navigation, sidebars, charts, tables, and official blocks | Best default for a compatible React project. Source is copied into the project. Prefer official blocks before third-party templates. |
| [Shadcn UI Kit free repository](https://github.com/bundui/shadcn-ui-kit) | Free variants, a starter dashboard, and bounded blocks | Use only files present in the public MIT repository or registry. Do not infer that a previewed premium item is free. |
| [dashboardcn](https://dashboardcn.com/) | Data-heavy dashboard components and analytics | Designed to inherit an existing shadcn theme. Verify the repository license and the exact registry item. |
| [ReUI](https://reui.io/) | Advanced controls such as data grids, filters, calendars, trees, timelines, Kanban, and Gantt patterns | The catalog mixes free MIT components/examples with paid Pro blocks. Confirm the exact item exposes free source or a public registry entry. Do not treat the entire catalog as free. |
| [Dashral](https://github.com/hasral/dashral) | Motion-aware metrics, charts, blocks, and a dashboard reference | Use public repository files covered by its license. Adapt motion to reduced-motion preferences and the host application's visual language. |
| [Shadcn Dashboard](https://github.com/shadcndashboard/shadcndashboard) | Full Vite/React dashboard reference | Treat as a donor or reference for bounded pages. Check its current attribution request as well as the license. |
| [Tremor](https://npm.tremor.so/) | Charts, KPI displays, trackers, and analytics | It has its own conventions. Prefer adapting individual visualization patterns instead of importing a competing design system wholesale. |

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

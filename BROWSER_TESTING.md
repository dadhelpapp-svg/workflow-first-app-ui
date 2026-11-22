# Browser testing with Playwright MCP

Use the official Microsoft Playwright MCP server for interactive inspection of running web applications. It exposes browser navigation and controls to Codex through structured accessibility snapshots. It is not a replacement for Playwright Test, application tests, Hallmark, or a full accessibility audit.

## Install for Codex

Requirements: Node.js 18 or newer, Codex CLI, and either an installed Chromium-family browser or permission for Playwright to download one on first use.

Standard cross-platform configuration:

```sh
codex mcp add playwright -- npx -y @playwright/mcp@latest --isolated --headless --console-level warning
```

On Windows, use `npx.cmd` if PowerShell blocks `npx.ps1`:

```powershell
codex mcp add playwright -- npx.cmd -y @playwright/mcp@latest --isolated --headless --browser msedge --console-level warning
```

This uses the official package on demand and avoids an unnecessary global npm installation. `--isolated` discards cookies and local storage when the browser closes. Remove it only when a task explicitly requires a persistent test profile and the saved state is safe. Do not reuse production login profiles for automated testing.

Verify configuration:

```sh
codex mcp get playwright
codex mcp list
npx -y @playwright/mcp@latest --version
```

Start a new Codex session after adding or changing an MCP server. An already-running session may not refresh its tool inventory.

## Invoke from Codex

Ask Codex to use Playwright MCP explicitly when browser proof matters. Example:

> Use Playwright MCP to open the local app, verify the appointment workflow at desktop and mobile sizes, report console errors, and do not change production data.

The application must already be running and reachable from the machine that launches the MCP server.

## Standard browser workflow

1. Confirm the target URL, environment, data policy, and whether mutations are safe.
2. Load the page and verify the expected title, landmark, or heading rather than relying only on HTTP status.
3. Navigate through the user-visible controls and confirm current-location cues and back/return behavior.
4. Exercise buttons, links, forms, dialogs, menus, tables, and other changed controls. Verify disabled, cancel, Escape, focus-return, and recovery paths when relevant.
5. Test form requirements, invalid values, visible error messages, preserved input, and successful submission. Avoid irreversible or production submissions.
6. Verify the full primary workflow and inspect the resulting state, not only the final click.
7. Check representative viewports. Default targets are desktop `1440x900`, tablet `768x1024`, and mobile `390x844`, adjusted for the product's supported devices.
8. Inspect browser console warnings/errors and failed requests. Separate application defects from expected development-server noise.
9. Re-run the risk-sensitive path after code changes. Pair the browser result with type checks and relevant automated tests.
10. Report the environment, data used, viewport sizes, interactions, console result, and any untested state.

## Tool responsibilities

| Tool | Primary responsibility |
| --- | --- |
| Hallmark | Visual direction, design consistency, UI quality, and reference comparison |
| Playwright MCP | Navigation, interactive controls, validation behavior, responsive viewports, console inspection, and multi-step workflow evidence |
| Application tests | Unit and business-rule behavior, schema contracts, TypeScript, and repeatable regression coverage |

No one row replaces the others. A design audit does not prove behavior. A browser pass does not prove all business rules. Unit tests do not prove rendered usability.

## Accessibility and visual limitations

Playwright MCP's accessibility snapshots improve semantic navigation, but they do not constitute a complete WCAG audit. Use keyboard checks and semantic inspection for every important flow. Add a dedicated engine such as axe for automated accessibility rules, followed by manual checks for focus, reading order, zoom/reflow, contrast, motion, and assistive-technology behavior.

Screenshots can support review, but MCP interaction alone does not provide maintained pixel baselines, diff thresholds, or approval workflows. Use Playwright Test screenshot assertions or a visual-regression service when pixel-level regression is required.

Playwright MCP is not a security boundary. Keep client permissions, environment isolation, approved test accounts, and data controls in place.

## Troubleshooting

- Server missing: run `codex mcp list`, confirm `playwright` is enabled, and start a new Codex session.
- Startup prompt or hang: include `-y` before `@playwright/mcp@latest`.
- `npx` blocked on Windows: configure `npx.cmd`.
- Browser not found: remove the explicit browser channel to allow the package's normal browser download, install an approved browser, or set a supported `--browser`/`--executable-path` value.
- Browser profile locked: use `--isolated` or a different `--user-data-dir`.
- App unreachable: start the documented development server, verify the exact loopback URL with an HTTP request, and avoid mixing `localhost` and `127.0.0.1` when cookies or origin checks matter.
- No console messages returned: confirm `--console-level` is not stricter than the messages being investigated.
- Tool schema is too costly for a large coding task: use Playwright Test or the official Playwright CLI for repeatable scripted coverage; reserve MCP for exploratory and stateful browser work.

To remove the integration:

```sh
codex mcp remove playwright
```

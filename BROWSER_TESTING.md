# Browser testing with Playwright MCP

Use the official Microsoft Playwright MCP server for interactive inspection of running web applications. It exposes browser navigation and controls to Claude Code through structured accessibility snapshots. It is not a replacement for Playwright Test, application tests, Hallmark, or a full accessibility audit.

## Install for Claude Code

Requirements: Node.js 18 or newer, Claude Code, and either an installed Chromium-family browser or permission for Playwright to download one on first use.

Standard cross-platform configuration, available in every project for your user account:

```sh
claude mcp add --scope user playwright -- npx -y @playwright/mcp@latest --isolated --headless --console-level warning
```

On native Windows (not WSL), wrap `npx` with `cmd /c` so the server can start:

```powershell
claude mcp add --scope user playwright -- cmd /c npx -y @playwright/mcp@latest --isolated --headless --browser msedge --console-level warning
```

To share the server with everyone working in one application repository instead, commit a project-scoped `.mcp.json` at that repository's root. Claude Code asks each user to approve project servers before first use.

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest", "--isolated", "--headless", "--console-level", "warning"]
    }
  }
}
```

This uses the official package on demand and avoids an unnecessary global npm installation. `--isolated` discards cookies and local storage when the browser closes. Remove it only when a task explicitly requires a persistent test profile and the saved state is safe. Do not reuse production login profiles for automated testing.

Verify configuration:

```sh
claude mcp get playwright
claude mcp list
npx -y @playwright/mcp@latest --version
```

Inside a session, run `/mcp` to confirm that `playwright` is connected. Start a new Claude Code session after adding or changing an MCP server. An already-running session may not refresh its tool inventory.

### Codex

Codex users can register the same server with `codex mcp add playwright -- npx -y @playwright/mcp@latest --isolated --headless --console-level warning` (use `npx.cmd` on Windows if PowerShell blocks `npx.ps1`), then verify with `codex mcp list`.

## Invoke from Claude Code

Ask Claude Code to use Playwright MCP explicitly when browser proof matters. Example:

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

- Server missing: run `claude mcp list` (or `/mcp` in a session), confirm `playwright` is connected, approve a project-scoped server if prompted, and start a new Claude Code session.
- Startup prompt or hang: include `-y` before `@playwright/mcp@latest`.
- Server fails to start on native Windows: use `cmd /c npx` as shown above (Codex: `npx.cmd`).
- Browser not found: remove the explicit browser channel to allow the package's normal browser download, install an approved browser, or set a supported `--browser`/`--executable-path` value.
- Browser profile locked: use `--isolated` or a different `--user-data-dir`.
- App unreachable: start the documented development server, verify the exact loopback URL with an HTTP request, and avoid mixing `localhost` and `127.0.0.1` when cookies or origin checks matter.
- No console messages returned: confirm `--console-level` is not stricter than the messages being investigated.
- Tool schema is too costly for a large coding task: use Playwright Test or the official Playwright CLI for repeatable scripted coverage; reserve MCP for exploratory and stateful browser work.

To remove the integration:

```sh
claude mcp remove --scope user playwright
```

For a project server, delete the `playwright` entry from `.mcp.json`. For Codex, run `codex mcp remove playwright`.

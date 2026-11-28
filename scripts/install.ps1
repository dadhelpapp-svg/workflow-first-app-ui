<#
.SYNOPSIS
Install or update the workflow-first-app-ui skill.

.EXAMPLE
.\scripts\install.ps1                   # Claude Code: ~\.claude\skills\workflow-first-app-ui
.\scripts\install.ps1 -Target Codex     # Codex: $env:CODEX_HOME or ~\.codex
.\scripts\install.ps1 -Target All       # both locations
.\scripts\install.ps1 -Destination C:\path\to\skill
#>
[CmdletBinding()]
param(
    [string]$Destination,
    [ValidateSet('Claude', 'Codex', 'All')]
    [string]$Target = 'Claude'
)

$ErrorActionPreference = 'Stop'
$Repository = 'https://github.com/dadhelpapp-svg/workflow-first-app-ui.git'
$SkillName = 'workflow-first-app-ui'

function Get-ClaudeDestination {
    $Root = $env:CLAUDE_CONFIG_DIR
    if ([string]::IsNullOrWhiteSpace($Root)) {
        $Root = Join-Path $env:USERPROFILE '.claude'
    }
    Join-Path (Join-Path $Root 'skills') $SkillName
}

function Get-CodexDestination {
    $Root = $env:CODEX_HOME
    if ([string]::IsNullOrWhiteSpace($Root)) {
        $Root = Join-Path $env:USERPROFILE '.codex'
    }
    Join-Path (Join-Path $Root 'skills') $SkillName
}

function Install-Skill([string]$Path) {
    if (Test-Path -LiteralPath $Path) {
        if (-not (Test-Path -LiteralPath (Join-Path $Path '.git'))) {
            throw "Destination exists but is not a Git repository: $Path"
        }

        git -C $Path pull --ff-only
        if ($LASTEXITCODE -ne 0) {
            throw 'Unable to update the skill repository.'
        }
    } else {
        $Parent = Split-Path -Parent $Path
        New-Item -ItemType Directory -Force -Path $Parent | Out-Null
        git clone $Repository $Path
        if ($LASTEXITCODE -ne 0) {
            throw 'Unable to install the skill repository.'
        }
    }

    $Validator = Join-Path $Path 'scripts\validate_repo.py'
    if (Get-Command python -ErrorAction SilentlyContinue) {
        python $Validator
    } elseif (Get-Command py -ErrorAction SilentlyContinue) {
        py -3 $Validator
    } else {
        throw 'Python 3 is required to validate the installed skill.'
    }
    if ($LASTEXITCODE -ne 0) {
        throw 'The installed skill failed validation.'
    }

    Write-Output "Workflow-First Development is ready at $Path. Start a new Claude Code or Codex session to refresh skills."
}

if (-not [string]::IsNullOrWhiteSpace($Destination)) {
    Install-Skill $Destination
} else {
    switch ($Target) {
        'Claude' { Install-Skill (Get-ClaudeDestination) }
        'Codex' { Install-Skill (Get-CodexDestination) }
        'All' {
            Install-Skill (Get-ClaudeDestination)
            Install-Skill (Get-CodexDestination)
        }
    }
}

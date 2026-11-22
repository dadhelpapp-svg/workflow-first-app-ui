[CmdletBinding()]
param(
    [string]$Destination
)

$ErrorActionPreference = 'Stop'
$Repository = 'https://github.com/dadhelpapp-svg/workflow-first-app-ui.git'

if ([string]::IsNullOrWhiteSpace($Destination)) {
    $CodexRoot = $env:CODEX_HOME
    if ([string]::IsNullOrWhiteSpace($CodexRoot)) {
        $CodexRoot = Join-Path $env:USERPROFILE '.codex'
    }
    $Destination = Join-Path $CodexRoot 'skills\workflow-first-app-ui'
}

if (Test-Path -LiteralPath $Destination) {
    if (-not (Test-Path -LiteralPath (Join-Path $Destination '.git'))) {
        throw "Destination exists but is not a Git repository: $Destination"
    }

    git -C $Destination pull --ff-only
    if ($LASTEXITCODE -ne 0) {
        throw 'Unable to update the skill repository.'
    }
} else {
    $Parent = Split-Path -Parent $Destination
    New-Item -ItemType Directory -Force -Path $Parent | Out-Null
    git clone $Repository $Destination
    if ($LASTEXITCODE -ne 0) {
        throw 'Unable to install the skill repository.'
    }
}

Write-Output "Workflow-First App UI is ready at $Destination"

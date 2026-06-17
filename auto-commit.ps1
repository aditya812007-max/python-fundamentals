#!/usr/bin/env pwsh
# Auto-commit script: adds, commits (if any changes), and pushes
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $scriptPath
# Only run inside a git repository
if (-not (Test-Path .git)) { exit 0 }

try {
    git add -A
    $changes = git status --porcelain
    if ($changes -ne "") {
        $msg = "Auto commit: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
        git commit -m $msg
        git push origin HEAD
        Write-Output "Auto committed and pushed: $msg"
    }
} catch {
    Write-Output "Auto-commit failed: $_"
}

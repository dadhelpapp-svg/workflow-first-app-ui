#!/usr/bin/env sh
set -eu

repository="https://github.com/dadhelpapp-svg/workflow-first-app-ui.git"
codex_root="${CODEX_HOME:-$HOME/.codex}"
destination="${1:-$codex_root/skills/workflow-first-app-ui}"

if [ -e "$destination" ]; then
  if [ ! -d "$destination/.git" ]; then
    echo "Destination exists but is not a Git repository: $destination" >&2
    exit 1
  fi
  git -C "$destination" pull --ff-only
else
  mkdir -p "$(dirname "$destination")"
  git clone "$repository" "$destination"
fi

echo "Workflow-First App UI is ready at $destination"

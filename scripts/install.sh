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

if command -v python3 >/dev/null 2>&1; then
  python3 "$destination/scripts/validate_repo.py"
elif command -v python >/dev/null 2>&1; then
  python "$destination/scripts/validate_repo.py"
else
  echo "Python 3 is required to validate the installed skill." >&2
  exit 1
fi

echo "Workflow-First Development is ready at $destination. Restart Codex to refresh skills."

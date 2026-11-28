#!/usr/bin/env sh
# Install or update the workflow-first-app-ui skill.
#
# Usage:
#   ./scripts/install.sh                  # Claude Code: ~/.claude/skills/workflow-first-app-ui
#   ./scripts/install.sh --codex          # Codex: ${CODEX_HOME:-~/.codex}/skills/workflow-first-app-ui
#   ./scripts/install.sh --all            # both locations
#   ./scripts/install.sh /custom/path     # an explicit destination
set -eu

repository="https://github.com/dadhelpapp-svg/workflow-first-app-ui.git"
skill_name="workflow-first-app-ui"
claude_destination="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/$skill_name"
codex_destination="${CODEX_HOME:-$HOME/.codex}/skills/$skill_name"

install_to() {
  destination="$1"
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
}

case "${1:-}" in
  "" | --claude) install_to "$claude_destination" ;;
  --codex) install_to "$codex_destination" ;;
  --all)
    install_to "$claude_destination"
    install_to "$codex_destination"
    ;;
  -h | --help)
    sed -n '2,8p' "$0" | sed 's/^# \{0,1\}//'
    ;;
  -*)
    echo "Unknown option: $1 (use --claude, --codex, --all, or a destination path)" >&2
    exit 2
    ;;
  *) install_to "$1" ;;
esac

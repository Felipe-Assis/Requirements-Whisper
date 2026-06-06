#!/usr/bin/env bash
# detect-agent.sh — Prints a contextual reminder about which agent is relevant
# for the file being edited. Used as a PreToolCall hook in Claude Code.
#
# Input: FILE_PATH from the tool call context (stdin JSON or env var)
# Output: Prints agent name suggestion to stdout

# Read the tool input from stdin to extract file path
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# Normalize path separators
FILE_PATH=$(echo "$FILE_PATH" | tr '\\' '/')

# Match patterns from most specific to least specific
case "$FILE_PATH" in
  *mechanics/chat_screen.rpy)
    echo "Reminder: chat-backend-agent is relevant for the chat client." ;;
  *mechanics/*screen*.rpy|*screens.rpy|*gui.rpy)
    echo "Reminder: screen-ui-agent is relevant for screen-language UI." ;;
  *scene_*.rpy|*script.rpy)
    echo "Reminder: scene-author-agent is relevant for narrative scenes." ;;
  *tl/*|*_strings*.rpy)
    echo "Reminder: i18n-tl-agent is relevant for translation files." ;;
  *characters.rpy|*variables/*.rpy)
    echo "Reminder: renpy-reference-validator is relevant for character/state defs." ;;
  *.rpy)
    echo "Reminder: run renpy-lint-doctor after .rpy edits (lint is the only gate)." ;;
esac

exit 0

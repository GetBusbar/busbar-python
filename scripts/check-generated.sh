#!/usr/bin/env bash
set -euo pipefail

changes=$(git status --porcelain=v1 --untracked-files=all -- busbar_admin setup.py GENERATED_CLIENT.md)
if [[ -n "$changes" ]]; then
  printf '%s\n' "$changes"
  echo "::error::Generated client is out of date. Run 'make generate' and commit." >&2
  exit 1
fi

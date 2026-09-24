#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python_bin="${PYTHON_BIN:-python3}"
pdf_link="$repo_root/docs/pdf"
if [[ -e "$pdf_link" || -L "$pdf_link" ]]; then
    printf 'Refusing to replace existing path: %s\n' "$pdf_link" >&2
    exit 1
fi

ln -s ../pdf "$pdf_link"
cleanup() {
    unlink "$pdf_link"
}
trap cleanup EXIT

"$python_bin" -m mkdocs build --strict -d site

git rev-parse HEAD > site/.deployed-commit

printf 'Built %s at commit %s\n' "$repo_root/site" "$(git rev-parse HEAD)"

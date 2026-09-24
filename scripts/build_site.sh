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

book_pdf="${BOOK_PDF:-$repo_root/output/pdf/色貌模型-中文整书版.pdf}"
if [[ -f "$book_pdf" ]]; then
    cp "$book_pdf" "$repo_root/site/pdf/色貌模型-中文整书版.pdf"
    book_manifest="${book_pdf%.pdf}.manifest.json"
    if [[ -f "$book_manifest" ]]; then
        cp "$book_manifest" "$repo_root/site/pdf/色貌模型-中文整书版.manifest.json"
    fi
else
    printf 'Whole-book PDF not found; build it before the final site audit: %s\n' "$book_pdf" >&2
fi

commit="${DEPLOY_COMMIT:-}"
if [[ -z "$commit" ]]; then
    if ! commit="$(git rev-parse HEAD 2>/dev/null)"; then
        printf 'DEPLOY_COMMIT is required when building outside a Git checkout.\n' >&2
        exit 1
    fi
fi
printf '%s\n' "$commit" > site/.deployed-commit

printf 'Built %s at commit %s\n' "$repo_root/site" "$commit"

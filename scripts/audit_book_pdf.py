#!/usr/bin/env python3
"""Verify the assembled book PDF and its manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from pypdf import PdfReader


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("manifest", type=Path, nargs="?")
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def flatten_outline(items: list[object]) -> list[str]:
    titles: list[str] = []
    for item in items:
        if isinstance(item, list):
            titles.extend(flatten_outline(item))
        else:
            title = getattr(item, "title", None)
            if title:
                titles.append(str(title))
    return titles


def main() -> int:
    args = parse_args()
    manifest_path = args.manifest or args.pdf.with_suffix(".manifest.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    reader = PdfReader(args.pdf, strict=True)
    errors: list[str] = []
    warnings: list[str] = []

    if sha256(args.pdf) != manifest["sha256"]:
        errors.append("PDF SHA-256 does not match manifest")
    if args.pdf.stat().st_size != manifest["bytes"]:
        errors.append("PDF byte count does not match manifest")
    derived_content_pages = sum(
        int(chapter["pages"]) for chapter in manifest.get("chapters", [])
    )
    derived_pages = int(manifest["front_matter_pages"]) + derived_content_pages
    if manifest.get("content_pages") != derived_content_pages:
        errors.append("Manifest content page count is not derived from chapters")
    if manifest.get("pages") != derived_pages:
        errors.append("Manifest total page count is not derived from its contents")
    if len(reader.pages) != manifest["pages"]:
        errors.append("PDF page count does not match manifest")
    if len(manifest.get("chapters", [])) != 22:
        errors.append("Manifest must contain 22 chapters")
    if not manifest.get("book_version") or not manifest.get("release_tag"):
        errors.append("Manifest must identify book_version and release_tag")

    for index, page in enumerate(reader.pages, 1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - 612) > 0.5 or abs(height - 792) > 0.5:
            errors.append(f"page {index}: unexpected size {width} x {height}")
        if page.get_contents() is None:
            errors.append(f"page {index}: missing content stream")

    labels = reader.page_labels
    expected_tail = str(manifest["content_pages"])
    if labels[:5] != ["i", "ii", "iii", "iv", "1"]:
        errors.append(f"unexpected opening page labels: {labels[:5]}")
    if not labels or labels[-1] != expected_tail:
        errors.append(f"unexpected final page label: {labels[-1:]}")

    outlines = flatten_outline(reader.outline)
    expected_outlines = 3 + len(manifest["chapters"])
    if len(outlines) != expected_outlines:
        errors.append(
            f"expected {expected_outlines} outline entries, found {len(outlines)}"
        )

    visible_markdown = [
        ("bold marker", re.compile(r"\*\*[^*]+\*\*")),
        ("image marker", re.compile(r"!\[[^]]*\]\([^)]*\)")),
        ("code fence", re.compile(r"```|~~~")),
        ("heading marker", re.compile(r"(?:^|\n)\s*#{1,6}\s+\S")),
    ]
    empty_text_pages: list[int] = []
    for index, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        if not text.strip():
            empty_text_pages.append(index)
        for label, pattern in visible_markdown:
            if pattern.search(text):
                errors.append(f"page {index}: visible Markdown {label}")
    if empty_text_pages:
        warnings.append(f"pages without extractable text: {empty_text_pages}")

    for chapter in manifest["chapters"]:
        physical_index = manifest["front_matter_pages"] + chapter["start_page"] - 1
        if not 0 <= physical_index < len(reader.pages):
            errors.append(f"chapter {chapter['number']}: invalid start page")
            continue
        text = reader.pages[physical_index].extract_text() or ""
        if len(text.strip()) < 20:
            errors.append(f"chapter {chapter['number']}: sparse first page")

    summary = {
        "pdf": str(args.pdf.resolve()),
        "pages": len(reader.pages),
        "page_labels": {"first": labels[:5], "last": labels[-1:]},
        "outline_entries": len(outlines),
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

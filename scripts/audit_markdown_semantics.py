#!/usr/bin/env python3
"""Verify repaired Markdown cases became semantic list items in built HTML."""

from __future__ import annotations

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path


class ArticleListParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.article_depth = 0
        self.li_stack: list[list[str]] = []
        self.items: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        classes = (values.get("class") or "").split()
        if tag == "article" or "md-content__inner" in classes:
            self.article_depth += 1
        elif self.article_depth and tag == "li":
            self.li_stack.append([])

    def handle_endtag(self, tag: str) -> None:
        if self.article_depth and tag == "li" and self.li_stack:
            self.items.append(" ".join("".join(self.li_stack.pop()).split()))
        elif tag == "article" and self.article_depth:
            self.article_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.article_depth and self.li_stack:
            self.li_stack[-1].append(data)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path, nargs="?", default=Path("site"))
    parser.add_argument(
        "--cases", type=Path, default=Path("tests/markdown-list-cases.json")
    )
    args = parser.parse_args()
    cases = json.loads(args.cases.read_text(encoding="utf-8"))
    cache: dict[str, list[str]] = {}
    errors: list[str] = []
    for case in cases:
        page = case["page"]
        if page not in cache:
            page_path = args.site / page
            if not page_path.is_file():
                errors.append(f"missing page: {page}")
                cache[page] = []
            else:
                html_parser = ArticleListParser()
                html_parser.feed(page_path.read_text(encoding="utf-8"))
                cache[page] = html_parser.items
        matches = [item for item in cache[page] if case["text"] in item]
        if not matches:
            errors.append(
                f"expected a semantic <li> for {page}: {case['text']!r}; found 0"
            )
    summary = {
        "schema_version": "1.0",
        "cases": len(cases),
        "pages": len(cache),
        "errors": errors,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

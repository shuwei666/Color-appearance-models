#!/usr/bin/env python3
"""Check required pages and local resources in a built MkDocs site."""

from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class RefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        for attr in ("href", "src"):
            value = values.get(attr)
            if value:
                self.refs.append((attr, value))


REQUIRED_PAGES = [
    "index.html",
    "0-前言/index.html",
    "1-人眼彩色视觉/index.html",
    "2-心理物理学/index.html",
    "3-色度学/index.html",
    "4-色貌定义/index.html",
    "5-色序系统/index.html",
    "6-色貌现象/index.html",
    "7-观察条件/index.html",
    "8-色适应/index.html",
    "9-色适应模型/index.html",
    "10-色貌模型/index.html",
    "11-The Nayatani model/index.html",
    "12-The Hunt model/index.html",
    "13-The RLAB model/index.html",
    "14-Other models/index.html",
    "15-CIECAM97s/index.html",
    "16-CIECAM02/index.html",
    "17-CAMs的测量/index.html",
    "18-传统色度学应用/index.html",
    "19-设备无关彩色成像/index.html",
    "20-图像色貌模型和未来/index.html",
    "21-HDR 色彩空间/index.html",
    "Reference/index.html",
    "pdf-download/index.html",
]


def local_target(root: Path, page: Path, raw: str) -> Path | None:
    parts = urlsplit(raw)
    if parts.scheme or parts.netloc or not parts.path:
        return None
    if parts.path == "/book" or parts.path == "/book/":
        return root / "index.html"
    if parts.path.startswith("/book/"):
        target_url = unquote(parts.path.removeprefix("/book/")).lstrip("/")
        target = root / target_url
        if raw.endswith("/") or target.is_dir():
            target = target / "index.html"
        return target
    parent = page.relative_to(root).parent
    page_url = "/" if parent == Path(".") else f"/{parent.as_posix()}/"
    target_url = unquote(urljoin(page_url, parts.path)).lstrip("/")
    target = root / target_url
    if raw.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "site").resolve()
    errors: list[str] = []

    for relative in REQUIRED_PAGES:
        if not (root / relative).is_file():
            errors.append(f"missing required page: {relative}")

    pdfs = sorted((root / "pdf").glob("*.pdf")) if (root / "pdf").is_dir() else []
    if len(pdfs) != 22:
        errors.append(f"expected 22 PDFs, found {len(pdfs)}")

    checked_refs = 0
    for page in sorted(root.rglob("*.html")):
        parser = RefParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for _, raw in parser.refs:
            target = local_target(root, page, raw)
            if target is None:
                continue
            checked_refs += 1
            if not target.exists():
                errors.append(
                    f"missing local target: {page.relative_to(root)} -> {raw}"
                )

    summary = {
        "site": str(root),
        "required_pages": len(REQUIRED_PAGES),
        "html_files": len(list(root.rglob("*.html"))),
        "pdf_files": len(pdfs),
        "local_references_checked": checked_refs,
        "errors": errors,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

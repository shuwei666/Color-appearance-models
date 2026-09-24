#!/usr/bin/env python3
"""Regression tests for visible-Markdown detection and semantic list parsing."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


audit = load("audit_build", ROOT / "scripts" / "audit_build.py")
semantic = load(
    "audit_markdown_semantics", ROOT / "scripts" / "audit_markdown_semantics.py"
)


def visible_errors(html: str) -> list[str]:
    parser = audit.RefParser()
    parser.feed(html)
    return [
        label
        for paragraph in parser.paragraphs
        for label, pattern in audit.VISIBLE_MARKDOWN
        if pattern.search(paragraph)
    ]


assert visible_errors("<article><p>介绍</p><ul><li>正确列表</li></ul></article>") == []
assert visible_errors(
    "<article><ul><li>外层<ul><li>嵌套项</li></ul></li></ul></article>"
) == []
assert "unordered-list marker" in visible_errors("<p>介绍\n- 裸露列表</p>")
assert "ordered-list marker" in visible_errors("<p>介绍\n1. 裸露列表</p>")
assert "blockquote marker" in visible_errors("<p>介绍\n&gt; 裸露引用</p>")
assert "emphasis marker" in visible_errors("<p>**未渲染加粗**</p>")
assert "image marker" in visible_errors("<p>![图](image.png)</p>")
assert "table separator" in visible_errors("<p>| --- | --- |</p>")

parser = semantic.ArticleListParser()
parser.feed(
    '<article class="md-content__inner"><ul><li>外层<ul><li>嵌套项</li></ul>'
    "</li></ul><p>- 不是列表</p></article>"
)
assert any("外层" in item for item in parser.items)
assert any("嵌套项" in item for item in parser.items)
assert all("不是列表" not in item for item in parser.items)

print("audit regression fixtures: PASS (9 detector cases, nested semantic lists)")

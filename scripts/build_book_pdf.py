#!/usr/bin/env python3
"""Assemble rendered chapter PDFs into one navigable book PDF."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.constants import PageLabelStyle
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


@dataclass(frozen=True)
class Chapter:
    number: int
    filename: str
    title: str


CHAPTERS = [
    Chapter(0, "0-前言.pdf", "前言"),
    Chapter(1, "1-人眼彩色视觉.pdf", "人眼彩色视觉"),
    Chapter(2, "2-心理物理学.pdf", "心理物理学"),
    Chapter(3, "3-色度学.pdf", "色度学"),
    Chapter(4, "4-色貌定义.pdf", "色貌定义"),
    Chapter(5, "5-色序系统.pdf", "色序系统"),
    Chapter(6, "6-色貌现象.pdf", "色貌现象"),
    Chapter(7, "7-观察条件.pdf", "观察条件"),
    Chapter(8, "8-色适应.pdf", "色适应"),
    Chapter(9, "9-色适应模型.pdf", "色适应模型"),
    Chapter(10, "10-色貌模型.pdf", "色貌模型"),
    Chapter(11, "11-The Nayatani model.pdf", "Nayatani et al. 模型"),
    Chapter(12, "12-The Hunt model.pdf", "Hunt 模型"),
    Chapter(13, "13-The RLAB model.pdf", "RLAB 模型"),
    Chapter(14, "14-Other models.pdf", "其他色貌模型"),
    Chapter(15, "15-CIECAM97s.pdf", "CIECAM97s"),
    Chapter(16, "16-CIECAM02.pdf", "CIECAM02"),
    Chapter(17, "17-CAMs的测量.pdf", "色貌模型的测量"),
    Chapter(18, "18-传统色度学应用.pdf", "传统色度学的应用"),
    Chapter(19, "19-设备无关彩色成像.pdf", "设备无关的彩色成像"),
    Chapter(20, "20-图像色貌模型和未来.pdf", "图像色貌模型与未来"),
    Chapter(21, "21-HDR 色彩空间.pdf", "HDR 色彩空间"),
]

PAGE_WIDTH, PAGE_HEIGHT = letter
FRONT_MATTER_PAGES = 4


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--chapters-dir",
        type=Path,
        default=Path("tmp/pdfs/rendered-chapters"),
        help="Directory containing the 22 browser-rendered chapter PDFs.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output/pdf/色貌模型-中文整书版.pdf"),
        help="Final book PDF path.",
    )
    parser.add_argument(
        "--work-dir",
        type=Path,
        default=Path("tmp/pdfs/book-build"),
        help="Intermediate PDF directory.",
    )
    parser.add_argument(
        "--font-regular",
        type=Path,
        default=Path("/System/Library/Fonts/STHeiti Light.ttc"),
    )
    parser.add_argument(
        "--font-bold",
        type=Path,
        default=Path("/System/Library/Fonts/STHeiti Medium.ttc"),
    )
    parser.add_argument("--source-commit", help="Git commit recorded in the PDF.")
    return parser.parse_args()


def git_commit() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], text=True, encoding="utf-8"
    ).strip()


def register_fonts(regular: Path, bold: Path) -> None:
    if not regular.is_file() or not bold.is_file():
        raise FileNotFoundError(
            "Chinese fonts not found; pass --font-regular and --font-bold."
        )
    pdfmetrics.registerFont(TTFont("CAM-Light", str(regular)))
    pdfmetrics.registerFont(TTFont("CAM-Medium", str(bold)))
    pdfmetrics.registerFontFamily(
        "CAM",
        normal="CAM-Light",
        bold="CAM-Medium",
        italic="CAM-Light",
        boldItalic="CAM-Medium",
    )


def draw_page_number(c: canvas.Canvas, label: str, color: Color) -> None:
    c.setFillColor(color)
    c.setFont("Helvetica", 8)
    c.drawCentredString(PAGE_WIDTH / 2, 0.27 * inch, label)


def draw_paragraph(
    c: canvas.Canvas,
    text: str,
    x: float,
    y_top: float,
    width: float,
    style: ParagraphStyle,
) -> float:
    paragraph = Paragraph(text, style)
    _, height = paragraph.wrap(width, PAGE_HEIGHT)
    paragraph.drawOn(c, x, y_top - height)
    return y_top - height


def draw_cover(c: canvas.Canvas, commit: str, build_date: str) -> None:
    navy = HexColor("#102A43")
    c.setFillColor(navy)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, stroke=0, fill=1)

    # A restrained CMY motif: color relationships rather than a decorative photo.
    c.saveState()
    c.setFillAlpha(0.78)
    for x, y, radius, color in [
        (438, 640, 84, HexColor("#35B8C8")),
        (492, 585, 84, HexColor("#EF476F")),
        (407, 552, 84, HexColor("#FFD166")),
    ]:
        c.setFillColor(color)
        c.circle(x, y, radius, stroke=0, fill=1)
    c.restoreState()

    c.setStrokeColor(HexColor("#6AD5D8"))
    c.setLineWidth(3)
    c.line(68, 686, 210, 686)

    c.setFillColor(HexColor("#A9C4D8"))
    c.setFont("Helvetica-Bold", 9)
    c.drawString(68, 706, "COLOR SCIENCE · CHINESE READER")

    c.setFillColor(HexColor("#FFFFFF"))
    c.setFont("CAM-Medium", 38)
    c.drawString(68, 590, "色貌模型")
    c.setFont("Helvetica-Bold", 20)
    c.drawString(70, 550, "COLOR APPEARANCE MODELS")

    c.setFillColor(HexColor("#D8E7F2"))
    c.setFont("CAM-Light", 13)
    c.drawString(70, 507, "中文翻译与整理 · 整书 PDF")

    c.setFillColor(HexColor("#FFFFFF"))
    c.setFont("CAM-Medium", 12)
    c.drawString(70, 142, "译者｜岳书威（Dr. Shawn）")
    c.setFont("CAM-Light", 9)
    c.setFillColor(HexColor("#A9C4D8"))
    c.drawString(70, 119, "shuweiyue.com/book/")
    c.drawRightString(PAGE_WIDTH - 70, 119, f"整书版 · {build_date[:7]}")
    c.setFont("Helvetica", 6.5)
    c.drawRightString(PAGE_WIDTH - 70, 96, commit[:12])


def draw_about(c: canvas.Canvas, commit: str, build_date: str) -> None:
    ink = HexColor("#19364D")
    muted = HexColor("#5E7384")
    teal = HexColor("#14919B")
    c.setFillColor(ink)
    c.setFont("CAM-Medium", 25)
    c.drawString(68, 704, "关于本译本")
    c.setStrokeColor(teal)
    c.setLineWidth(2)
    c.line(68, 684, 180, 684)

    body = ParagraphStyle(
        "about-body",
        fontName="CAM-Light",
        fontSize=10.5,
        leading=18,
        textColor=ink,
        alignment=TA_LEFT,
        wordWrap="CJK",
        spaceAfter=12,
    )
    y = 642
    paragraphs = [
        "本书基于 <b>Color Appearance Models（2013）</b> 相关内容翻译和整理，面向颜色科学、成像、ISP、显示、视觉科学及相关工程实践的学习者。",
        "本译本并非逐句直译。译者会根据研究与产业经验重组讲解，在关键处加入「译者注」，并使用大语言模型辅助部分初稿；正文由译者持续校正。错误之处在所难免，欢迎通过项目仓库提交纠错。",
        "本 PDF 由项目当前 Markdown 源文件统一渲染，再装订为单卷；公式、图片、表格和章节顺序与本次构建版本对应。在线版与 PDF 均以 Git 提交作为版本标识。",
    ]
    for paragraph in paragraphs:
        y = draw_paragraph(c, paragraph, 68, y, PAGE_WIDTH - 136, body) - 13

    c.setFillColor(HexColor("#EAF4F5"))
    c.roundRect(68, 218, PAGE_WIDTH - 136, 132, 8, stroke=0, fill=1)
    small = ParagraphStyle(
        "about-small",
        fontName="CAM-Light",
        fontSize=8.8,
        leading=15,
        textColor=ink,
        wordWrap="CJK",
    )
    info = (
        f"<b>译者</b>　岳书威（Dr. Shawn）<br/>"
        "香港理工大学图像科学博士，现任教于深圳职业技术大学。<br/><br/>"
        f"<b>构建日期</b>　{build_date}<br/>"
        f"<b>Git 版本</b>　{commit}<br/>"
        "<b>在线阅读</b>　https://shuweiyue.com/book/"
    )
    draw_paragraph(c, info, 86, 329, PAGE_WIDTH - 172, small)

    c.setFillColor(muted)
    c.setFont("CAM-Light", 7.5)
    c.drawString(68, 110, "学习交流版本。原著及相关材料的权利归其各自权利人所有。")
    draw_page_number(c, "ii", muted)


def draw_contents_page(
    c: canvas.Canvas,
    entries: list[tuple[Chapter, int, int]],
    roman_label: str,
    part: int,
) -> None:
    ink = HexColor("#19364D")
    muted = HexColor("#6A7F8E")
    teal = HexColor("#14919B")
    c.setFillColor(ink)
    c.setFont("CAM-Medium", 25)
    c.drawString(68, 704, "目录")
    c.setFont("Helvetica", 8)
    c.setFillColor(muted)
    c.drawRightString(PAGE_WIDTH - 68, 708, f"CONTENTS · {part}/2")
    c.setStrokeColor(teal)
    c.setLineWidth(2)
    c.line(68, 684, 180, 684)

    y = 640
    for chapter, start_page, page_count in entries:
        number = f"{chapter.number:02d}"
        c.setFillColor(teal)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(70, y + 2, number)
        c.setFillColor(ink)
        c.setFont("CAM-Medium", 12)
        c.drawString(106, y, chapter.title)
        c.setFillColor(muted)
        c.setFont("Helvetica", 8)
        page_text = str(start_page)
        c.drawRightString(PAGE_WIDTH - 70, y + 1, page_text)
        title_width = pdfmetrics.stringWidth(chapter.title, "CAM-Medium", 12)
        dots_start = min(430, 116 + title_width)
        c.setStrokeColor(HexColor("#D8E2E8"))
        c.setDash(1, 2)
        c.line(dots_start, y + 3, PAGE_WIDTH - 96, y + 3)
        c.setDash()
        c.setFillColor(muted)
        c.setFont("CAM-Light", 7)
        c.drawString(106, y - 15, f"本章 {page_count} 页")
        y -= 48

    draw_page_number(c, roman_label, muted)


def build_front_matter(
    path: Path,
    commit: str,
    build_date: str,
    chapter_info: list[tuple[Chapter, int, int]],
) -> None:
    c = canvas.Canvas(str(path), pagesize=letter, pageCompression=1)
    c.setTitle("色貌模型 - 中文翻译与整理")
    c.setAuthor("岳书威（Dr. Shawn）")
    draw_cover(c, commit, build_date)
    c.showPage()
    draw_about(c, commit, build_date)
    c.showPage()
    draw_contents_page(c, chapter_info[:11], "iii", 1)
    c.showPage()
    draw_contents_page(c, chapter_info[11:], "iv", 2)
    c.showPage()
    c.save()


def build_overlay(path: Path, chapter_info: list[tuple[Chapter, int, int]]) -> None:
    ink = HexColor("#607788")
    line = HexColor("#DDE5EA")
    c = canvas.Canvas(str(path), pagesize=letter, pageCompression=1)
    page_number = 1
    for chapter, _, page_count in chapter_info:
        label = f"{chapter.number}. {chapter.title}"
        for page_in_chapter in range(page_count):
            c.setStrokeColor(line)
            c.setLineWidth(0.4)
            c.line(54, PAGE_HEIGHT - 23, PAGE_WIDTH - 54, PAGE_HEIGHT - 23)
            c.line(54, 28, PAGE_WIDTH - 54, 28)
            c.setFillColor(ink)
            c.setFont("CAM-Light", 6.8)
            if page_in_chapter % 2 == 0:
                c.drawString(58, PAGE_HEIGHT - 18, "色貌模型")
                c.drawRightString(PAGE_WIDTH - 58, PAGE_HEIGHT - 18, label)
            else:
                c.drawString(58, PAGE_HEIGHT - 18, label)
                c.drawRightString(PAGE_WIDTH - 58, PAGE_HEIGHT - 18, "COLOR APPEARANCE MODELS")
            c.setFont("Helvetica", 7.5)
            c.drawCentredString(PAGE_WIDTH / 2, 16, str(page_number))
            c.showPage()
            page_number += 1
    c.save()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    args = parse_args()
    commit = args.source_commit or git_commit()
    build_date = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    register_fonts(args.font_regular, args.font_bold)

    chapter_readers: list[tuple[Chapter, Path, PdfReader]] = []
    content_page = 1
    chapter_info: list[tuple[Chapter, int, int]] = []
    for chapter in CHAPTERS:
        path = args.chapters_dir / chapter.filename
        if not path.is_file():
            raise FileNotFoundError(f"Missing chapter PDF: {path}")
        reader = PdfReader(path)
        page_count = len(reader.pages)
        if page_count == 0:
            raise ValueError(f"Chapter PDF has no pages: {path}")
        for page in reader.pages:
            width = float(page.mediabox.width)
            height = float(page.mediabox.height)
            if abs(width - PAGE_WIDTH) > 0.5 or abs(height - PAGE_HEIGHT) > 0.5:
                raise ValueError(
                    f"Unexpected page size in {path}: {width:.2f} x {height:.2f}"
                )
        chapter_info.append((chapter, content_page, page_count))
        chapter_readers.append((chapter, path, reader))
        content_page += page_count

    args.work_dir.mkdir(parents=True, exist_ok=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    front_path = args.work_dir / "front-matter.pdf"
    overlay_path = args.work_dir / "content-overlay.pdf"
    build_front_matter(front_path, commit, build_date, chapter_info)
    build_overlay(overlay_path, chapter_info)

    front = PdfReader(front_path)
    overlays = PdfReader(overlay_path)
    content_pages = sum(count for _, _, count in chapter_info)
    if len(front.pages) != FRONT_MATTER_PAGES:
        raise ValueError(f"Expected {FRONT_MATTER_PAGES} front-matter pages")
    if len(overlays.pages) != content_pages:
        raise ValueError("Overlay page count does not match content")

    writer = PdfWriter()
    writer.append(front)
    overlay_index = 0
    for _, _, reader in chapter_readers:
        for page in reader.pages:
            page.merge_page(overlays.pages[overlay_index], over=True, expand=False)
            writer.add_page(page)
            overlay_index += 1

    writer.add_metadata(
        {
            "/Title": "色貌模型 - 中文翻译与整理",
            "/Author": "岳书威（Dr. Shawn）",
            "/Subject": "Color Appearance Models 中文学习版",
            "/Keywords": f"color appearance models; 色貌模型; {commit}",
            "/Creator": "MkDocs, Chrome, ReportLab, and pypdf",
        }
    )
    writer.page_mode = "/UseOutlines"
    writer.add_outline_item("封面", 0)
    writer.add_outline_item("关于本译本", 1)
    writer.add_outline_item("目录", 2)
    for chapter, start_page, _ in chapter_info:
        pdf_index = FRONT_MATTER_PAGES + start_page - 1
        writer.add_outline_item(f"{chapter.number}. {chapter.title}", pdf_index)
    writer.set_page_label(
        0,
        FRONT_MATTER_PAGES - 1,
        style=PageLabelStyle.LOWERCASE_ROMAN,
        start=1,
    )
    writer.set_page_label(
        FRONT_MATTER_PAGES,
        len(writer.pages) - 1,
        style=PageLabelStyle.DECIMAL,
        start=1,
    )

    with args.output.open("wb") as handle:
        writer.write(handle)

    final_reader = PdfReader(args.output)
    expected_pages = FRONT_MATTER_PAGES + content_pages
    if len(final_reader.pages) != expected_pages:
        raise ValueError(
            f"Final page count mismatch: {len(final_reader.pages)} != {expected_pages}"
        )

    manifest = {
        "output": str(args.output.resolve()),
        "sha256": sha256(args.output),
        "bytes": args.output.stat().st_size,
        "pages": expected_pages,
        "front_matter_pages": FRONT_MATTER_PAGES,
        "content_pages": content_pages,
        "source_commit": commit,
        "built_at": build_date,
        "chapters": [
            {
                "number": chapter.number,
                "title": chapter.title,
                "filename": chapter.filename,
                "start_page": start_page,
                "pages": page_count,
                "sha256": sha256(args.chapters_dir / chapter.filename),
            }
            for chapter, start_page, page_count in chapter_info
        ],
    }
    manifest_path = args.output.with_suffix(".manifest.json")
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

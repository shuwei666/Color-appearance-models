#!/usr/bin/env python3
"""Render every PDF page at readable resolution and retain per-page evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

from PIL import Image, ImageChops, ImageStat
from pypdf import PdfReader

# Calibrated at 110 dpi: the superseded blank page measured 0.0147 in the
# body crop, while the sparsest legitimate final page measured 0.4780.
MIN_BODY_DENSITY = 0.1
MIN_BODY_TEXT_CHARACTERS = 10
MIN_BODY_VISUAL_CONTENT_DENSITY = 1.0


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--render-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--dpi", type=int, default=110)
    parser.add_argument("--skip-render", action="store_true")
    args = parser.parse_args()
    args.render_dir.mkdir(parents=True, exist_ok=True)
    if not args.skip_render:
        subprocess.run(
            [
                "pdftoppm",
                "-png",
                "-r",
                str(args.dpi),
                str(args.pdf),
                str(args.render_dir / "page"),
            ],
            check=True,
        )

    reader = PdfReader(args.pdf)
    images = sorted(args.render_dir.glob("page-*.png"))
    errors: list[str] = []
    if len(images) != len(reader.pages):
        errors.append(f"rendered {len(images)} images for {len(reader.pages)} pages")
    records = []
    for page_number, (page, path) in enumerate(zip(reader.pages, images), 1):
        with Image.open(path) as image:
            rgb = image.convert("RGB")
            background = Image.new("RGB", rgb.size, "white")
            diff = ImageChops.difference(rgb, background).convert("L")
            bbox = diff.point(lambda value: 255 if value > 10 else 0).getbbox()
            mean = ImageStat.Stat(diff).mean[0]
            body = rgb.crop(
                (
                    round(rgb.width * 80 / 935),
                    round(rgb.height * 70 / 1210),
                    round(rgb.width * 855 / 935),
                    round(rgb.height * 1150 / 1210),
                )
            )
            body_diff = ImageChops.difference(
                body, Image.new("RGB", body.size, "white")
            ).convert("L")
            body_mean = ImageStat.Stat(body_diff).mean[0]
            expected_width = round(8.5 * args.dpi)
            expected_height = round(11 * args.dpi)
            if abs(rgb.width - expected_width) > 2 or abs(rgb.height - expected_height) > 2:
                errors.append(f"page {page_number}: unexpected render size {rgb.size}")
            text = page.extract_text() or ""
            text_lines = [line.strip() for line in text.splitlines() if line.strip()]
            body_text = "\n".join(text_lines[:-3]) if len(text_lines) >= 3 else ""
            if page_number > 1 and len(text.strip()) < 20:
                errors.append(f"page {page_number}: too little extractable text")
            if bbox is None:
                errors.append(f"page {page_number}: visually blank")
            if page_number > 4 and body_mean < MIN_BODY_DENSITY:
                errors.append(
                    f"page {page_number}: body region is visually near-blank "
                    f"({body_mean:.4f} < {MIN_BODY_DENSITY})"
                )
            if (
                page_number > 4
                and len(body_text) < MIN_BODY_TEXT_CHARACTERS
                and body_mean < MIN_BODY_VISUAL_CONTENT_DENSITY
            ):
                errors.append(
                    f"page {page_number}: no source-derived body text or visual content "
                    f"(text {len(body_text)} < {MIN_BODY_TEXT_CHARACTERS}; "
                    f"density {body_mean:.4f} < {MIN_BODY_VISUAL_CONTENT_DENSITY})"
                )
            records.append(
                {
                    "page": page_number,
                    "png": path.name,
                    "sha256": file_sha256(path),
                    "pixels": [rgb.width, rgb.height],
                    "ink_bbox": list(bbox) if bbox else None,
                    "mean_difference_from_white": round(mean, 4),
                    "body_mean_difference_from_white": round(body_mean, 4),
                    "extractable_text_characters": len(text.strip()),
                    "body_text_characters": len(body_text),
                }
            )
    summary = {
        "schema_version": "1.0",
        "pdf": str(args.pdf.resolve()),
        "pdf_sha256": file_sha256(args.pdf),
        "dpi": args.dpi,
        "pages_expected": len(reader.pages),
        "pages_recorded": len(records),
        "records": records,
        "errors": errors,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {key: value for key, value in summary.items() if key != "records"},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

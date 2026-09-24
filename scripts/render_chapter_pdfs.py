#!/usr/bin/env python3
"""Render all MkDocs chapters to PDF with Playwright CLI."""

from __future__ import annotations

import argparse
import os
import shutil
import socket
import subprocess
import sys
import time
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("tmp/pdfs/rendered-chapters"),
    )
    parser.add_argument("--port", type=int, default=8877)
    parser.add_argument("--playwright-cli", type=Path)
    return parser.parse_args()


def resolve_cli(explicit: Path | None) -> Path:
    if explicit:
        if explicit.is_file():
            return explicit.resolve()
        raise FileNotFoundError(f"Playwright CLI wrapper not found: {explicit}")
    global_cli = shutil.which("playwright-cli")
    if global_cli:
        return Path(global_cli)
    bundled = (
        Path.home()
        / ".codex"
        / "skills"
        / "playwright"
        / "scripts"
        / "playwright_cli.sh"
    )
    if bundled.is_file():
        return bundled
    raise FileNotFoundError(
        "No Playwright CLI found. Pass --playwright-cli or install @playwright/cli."
    )


def wait_for_server(port: int, timeout: float = 10.0) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.25):
                return
        except OSError:
            time.sleep(0.1)
    raise TimeoutError(f"Local HTTP server did not start on port {port}")


def main() -> int:
    args = parse_args()
    site_dir = args.site_dir.resolve()
    output_dir = args.output_dir.resolve()
    if not (site_dir / "index.html").is_file():
        raise FileNotFoundError(
            f"Built site not found at {site_dir}; run scripts/build_site.sh first."
        )
    output_dir.mkdir(parents=True, exist_ok=True)
    cli = resolve_cli(args.playwright_cli)
    js = (Path(__file__).parent / "render_chapter_pdfs.js").resolve()
    base_url = f"http://127.0.0.1:{args.port}"
    env = os.environ.copy()
    env["CAM_PDF_BASE_URL"] = base_url
    env["CAM_PDF_CHAPTERS_DIR"] = str(output_dir)
    log_path = output_dir.parent / "chapter-render-server.log"

    with log_path.open("w", encoding="utf-8") as log:
        server = subprocess.Popen(
            [
                sys.executable,
                "-m",
                "http.server",
                str(args.port),
                "--bind",
                "127.0.0.1",
                "--directory",
                str(site_dir),
            ],
            stdout=log,
            stderr=subprocess.STDOUT,
            text=True,
        )
        try:
            wait_for_server(args.port)
            subprocess.run(
                [
                    str(cli),
                    "--session=cam-book-pdf",
                    "open",
                    f"{base_url}/0-%E5%89%8D%E8%A8%80/",
                ],
                check=True,
                env=env,
            )
            subprocess.run(
                [
                    str(cli),
                    "--session=cam-book-pdf",
                    "run-code",
                    f"--filename={js}",
                ],
                check=True,
                env=env,
            )
        finally:
            subprocess.run(
                [str(cli), "--session=cam-book-pdf", "close"],
                check=False,
                env=env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            server.terminate()
            try:
                server.wait(timeout=5)
            except subprocess.TimeoutExpired:
                server.kill()
                server.wait()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

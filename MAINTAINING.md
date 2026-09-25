# 项目构建与维护

本文档面向仓库维护者。普通读者可直接访问[在线版](https://shuweiyue.com/book/)或下载[完整 PDF](https://shuweiyue.com/book/pdf/色貌模型-中文整书版.pdf)。

## 构建网站

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
PYTHON_BIN=.venv/bin/python bash scripts/build_site.sh
.venv/bin/python scripts/audit_build.py site
.venv/bin/python scripts/test_audit_build.py
.venv/bin/python scripts/audit_markdown_semantics.py site
```

`scripts/build_site.sh` 会生成网页、复制 22 份章节 PDF，并把当前 Git 提交写入 `site/.deployed-commit`，用于核对 GitHub 与线上版本。服务器源副本不含 `.git` 时，构建前需显式传入 `DEPLOY_COMMIT=<完整提交 SHA>`。

## 生成整书 PDF

整书 PDF 使用当前 Markdown 构建结果重新打印 22 章，而不是直接拼接仓库中的旧章节 PDF。

```bash
PYTHON_BIN=.venv/bin/python bash scripts/build_site.sh
python3 scripts/render_chapter_pdfs.py
uv venv .venv-pdf
uv pip install --python .venv-pdf/bin/python -r requirements-pdf.txt
.venv-pdf/bin/python scripts/build_book_pdf.py
.venv-pdf/bin/python scripts/audit_book_pdf.py output/pdf/色貌模型-中文整书版.pdf
.venv-pdf/bin/python scripts/verify_pdf_pages.py output/pdf/色貌模型-中文整书版.pdf \
  --render-dir tmp/pdfs/all-pages-110dpi \
  --output outputs/verification/book-pdf-pages.json
PYTHON_BIN=.venv/bin/python bash scripts/build_site.sh
.venv/bin/python scripts/audit_build.py site
```

最终文件写入 `output/pdf/色貌模型-中文整书版.pdf`，同时生成记录版本号、Git tag、Git 提交、章节页数和 SHA-256 的 manifest。整书包含封面、版本说明、目录、连续页码和 PDF 书签；最后一次网站构建会把整书 PDF 与 manifest 放入 `site/pdf/`。

## 发布原则

- 先提交源文件与章节 PDF，再以该提交创建版本标签。
- 整书 PDF、manifest、GitHub Release 和网站部署必须指向同一源提交。
- 网站部署前先备份 `/var/www/html/book/`，同步范围不得扩展到其他网站目录。
- 已发布的标签和 Release 保留为历史记录；修订使用新的补丁版本，不覆盖旧资产。

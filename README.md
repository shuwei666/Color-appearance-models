# 《Color Appearance Models》中文翻译

在线阅读：[https://shuweiyue.com/book/](https://shuweiyue.com/book/)


## 目录

| **章节**                 |  **完成度** | **文档链接** |
|--------------------------|------------|--------------|
| 0. 前言                  | 🟢 已完成   | [0-前言.md](./docs/0-前言.md) |
| 1. 人眼彩色视觉           | 🟢 已完成   | [1-人眼彩色视觉.md](./docs/1-人眼彩色视觉.md) |
| 2. 心理物理学             | 🟢 已完成   | [2-心理物理学.md](./docs/2-心理物理学.md) |
| 3. 色度学                 | 🟢 已完成   | [3-色度学.md](./docs/3-色度学.md) |
| 4. 色貌定义               | 🟢 已完成   | [4-色貌定义.md](./docs/4-色貌定义.md) |
| 5. 色序系统               | 🟢 已完成   | [5-色序系统.md](./docs/5-色序系统.md) |
| 6. 色貌现象               | 🟢 已完成   | [6-色貌现象.md](./docs/6-色貌现象.md) |
| 7. 观察条件               | 🟢 已完成   | [7-观察条件.md](./docs/7-观察条件.md) |
| 8. 色适应                 | 🟢 已完成   | [8-色适应.md](./docs/8-色适应.md) |
| 9. 色适应模型             | 🟢 已完成   | [9-色适应模型.md](./docs/9-色适应模型.md) |
| 10. 色貌模型              | 🟢 已完成   | [10-色貌模型.md](./docs/10-色貌模型.md) |
| 11. Nayatani et al 模型   | 🟢 已完成   | [11-The Nayatani model.md](./docs/11-The%20Nayatani%20model.md) |
| 12. Hunt 模型             | 🟢 已完成   | [12-The Hunt model.md](./docs/12-The%20Hunt%20model.md) |
| 13. RLAB 模型             | 🟢 已完成   | [13-The RLAB model.md](./docs/13-The%20RLAB%20model.md) |
| 14. 其他色貌模型          | 🟢 已完成   | [14-Other models.md](./docs/14-Other%20models.md) |
| 15. CIECAM97s 模型        | 🟢 已完成   | [15-CIECAM97s.md](./docs/15-CIECAM97s.md) |
| 16. CIECAM02 模型         | 🟢 已完成   | [16-CIECAM02.md](./docs/16-CIECAM02.md) |
| 17. 色貌模型的测量        | 🟢 已完成   | [17-CAMs的测量.md](./docs/17-CAMs的测量.md) |
| 18. 传统色度学的应用      | 🟢 已完成   | [18-传统色度学应用.md](./docs/18-传统色度学应用.md) |
| 19. 设备无关的彩色成像    | 🟢 已完成   | [19-设备无关彩色成像.md](./docs/19-设备无关彩色成像.md) |
| 20. 图像色貌模型与未来    | 🟢 已完成   | [20-图像色貌模型和未来.md](./docs/20-图像色貌模型和未来.md) |
| 21. HDR 色彩空间          | 🟢 已完成   | [21-HDR 色彩空间.md](./docs/21-HDR%20色彩空间.md) |

---


## 动机

这是一本颜色科学领域的经典著作，是该领域博士生的必读书籍。

但是很惭愧，我作为颜色科学领域的人，竟然没有通读过该书。所以，我翻译这本书，主要目的是**为了个人的学习！**

我想要通读本书，补足自己的颜色理论基础方面的不足。
如果是有其他目的，那就是希望对中国的颜色科学领域做一些小小的贡献，特别是对于工业界，**能够比较方便从业人员了解该领域**。

本书有以下特点：

- 翻译大量借鉴使用LLM模型，比如ChatGPT/Claud等
- 但是我基本上对每一段都进行了校正，尽可能保证其严谨性
- 并不是逐句翻译，有些时候作者讲解的我认为不够详细，有时候又感觉繁复，我会使用自己的思路去重新组织语言讲解
- 我在关键章节——就是和工业界密切相关的一些章节下面使用**译者注**的形式，和工业界，以及知识之间的关系进行串联和发散


错误之处在所难免，本书还在持续翻译中，请读者不吝赐教！

## 本地构建

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
PYTHON_BIN=.venv/bin/python bash scripts/build_site.sh
.venv/bin/python scripts/audit_build.py site
```

`scripts/build_site.sh` 会生成网页、复制 22 份章节 PDF，并把当前 Git 提交写入 `site/.deployed-commit`，用于核对 GitHub 与线上版本。
服务器源副本不含 `.git` 时，构建前显式传入 `DEPLOY_COMMIT=<完整提交 SHA>`。

## 生成整书 PDF

整书 PDF 使用当前 Markdown 构建结果重新打印 22 章，而不是直接拼接仓库中的旧章节 PDF：

```bash
PYTHON_BIN=.venv/bin/python bash scripts/build_site.sh
python3 scripts/render_chapter_pdfs.py
uv venv .venv-pdf
uv pip install --python .venv-pdf/bin/python -r requirements-pdf.txt
.venv-pdf/bin/python scripts/build_book_pdf.py
.venv-pdf/bin/python scripts/audit_book_pdf.py output/pdf/色貌模型-中文整书版.pdf
PYTHON_BIN=.venv/bin/python bash scripts/build_site.sh
.venv/bin/python scripts/audit_build.py site
```

最终文件写入 `output/pdf/色貌模型-中文整书版.pdf`，同时生成记录 Git 提交、章节页数和 SHA-256 的 manifest。整书包含封面、版本说明、目录、连续页码和 PDF 书签。最后一次网站构建会把整书 PDF 和 manifest 一并放入 `site/pdf/`。

---

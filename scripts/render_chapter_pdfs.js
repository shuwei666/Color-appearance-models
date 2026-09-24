async (page) => {
  const chapters = [
    "0-前言",
    "1-人眼彩色视觉",
    "2-心理物理学",
    "3-色度学",
    "4-色貌定义",
    "5-色序系统",
    "6-色貌现象",
    "7-观察条件",
    "8-色适应",
    "9-色适应模型",
    "10-色貌模型",
    "11-The Nayatani model",
    "12-The Hunt model",
    "13-The RLAB model",
    "14-Other models",
    "15-CIECAM97s",
    "16-CIECAM02",
    "17-CAMs的测量",
    "18-传统色度学应用",
    "19-设备无关彩色成像",
    "20-图像色貌模型和未来",
    "21-HDR 色彩空间",
  ];
  const baseUrl = process.env.CAM_PDF_BASE_URL;
  const outputRoot = process.env.CAM_PDF_CHAPTERS_DIR;
  if (!baseUrl || !outputRoot) {
    throw new Error("CAM_PDF_BASE_URL and CAM_PDF_CHAPTERS_DIR are required");
  }
  const results = [];

  for (const chapter of chapters) {
    const url = `${baseUrl}/${encodeURIComponent(chapter)}/`;
    const response = await page.goto(url, {
      waitUntil: "networkidle",
      timeout: 60000,
    });
    await page.evaluate(async () => {
      if (window.MathJax?.startup?.promise) {
        await window.MathJax.startup.promise;
      }
      await document.fonts.ready;
    });
    await page.waitForFunction(
      () => Array.from(document.images).every(
        (image) => image.complete && image.naturalWidth > 0,
      ),
      null,
      { timeout: 60000 },
    );
    const checks = await page.evaluate(() => ({
      title: document.title,
      images: document.images.length,
      brokenImages: Array.from(document.images).filter(
        (image) => !image.complete || image.naturalWidth === 0,
      ).length,
      mathSources: document.querySelectorAll(".arithmatex").length,
      mathRendered: document.querySelectorAll("mjx-container").length,
    }));
    if (
      !response
      || !response.ok()
      || checks.brokenImages
      || (checks.mathSources && !checks.mathRendered)
    ) {
      throw new Error(
        `${chapter}: ${JSON.stringify({ status: response?.status(), ...checks })}`,
      );
    }
    const path = `${outputRoot}/${chapter}.pdf`;
    await page.pdf({
      path,
      format: "Letter",
      printBackground: true,
      displayHeaderFooter: false,
    });
    results.push({ chapter, status: response.status(), ...checks });
  }

  return results;
}

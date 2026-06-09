// MathJax v3 configuration (the loaded library is mathjax@3 tex-chtml.js).
// Must be loaded BEFORE tex-chtml.js so window.MathJax is read at startup.
// Enables $...$ / $$...$$ in addition to \(...\) / \[...\] so that math written
// inside raw HTML blocks (e.g. <div class="math-block">, figure captions) and
// space-padded inline math also render. MathJax scans the whole document body.
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
  }
};

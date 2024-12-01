MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true
  },
  "HTML-CSS": {
    linebreaks: { automatic: true }, // 自动换行
    styles: { ".MathJax_Display": { margin: "0" } }, // 去掉显示公式的边距
    showMathMenu: false // 关闭右键菜单
  },
  showProcessingMessages: false, // 关闭处理消息
  messageStyle: "none"
});

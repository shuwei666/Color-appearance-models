# 色貌模型

---

本站内容基于对 `Color Appearance Models（２０１３）` 相关文献的翻译和整理。遵循以下原则：

- 尊重作者本意，但**非**逐句翻译
- 根据译者经验背景，会添加知识点之间的连接
- 读者包含：图像（图形， ISP）算法从业者，相关领域科研人员（Vision science, low-level vision, imaging, graphics, visualization., etc.）
- 错误之处在所难免，恳请读者指正

## 关键字

颜色科学，色貌模型，色适应，色觉现象，CIECAM97s，CIECAM02，视觉系统，心理物理学, HDR

## 摘要

色貌模型是颜色科学中的重要研究方向之一。它不仅描述了颜色在标准观察条件下的外观，还可以解释颜色如何随环境条件、观察者的适应状态以及背景颜色的变化而改变。色貌模型的发展使得我们能够更好地理解人眼如何感知色彩，同时为各类视觉显示系统（如显示器、打印设备等）的色彩管理提供了理论基础。

在本书中，我们将介绍色貌模型的基本理论和关键发展，包括早期的心理物理学模型、经典色序系统、色适应模型、以及现代的 CIECAM97s 和 CIECAM02 模型。我们还将探讨色貌模型在实际应用中的测量与实现，并讨论未来色貌模型的研究方向和挑战。

## 目录

| **章节**                 |  **完成度** |
|--------------------------|------------|
| 0. 前言                  | 🟢 已完成   |
| 1. 人眼彩色视觉           | 🟢 已完成  |
| 2. 心理物理学             | 🟢 已完成  |
| 3. 色度学                 | 🟢 已完成  |
| 4. 色貌定义               | 🟢 已完成  |
| 5. 色序系统               | 🟢 已完成  |
| 6. 色貌现象               | 🟢 已完成  |
| 7. 观察条件               | 🟢 已完成  |
| 8. 色适应                 |🟢 已完成  |
| 9. 色适应模型             | 🟢 已完成  |
| 10. 色貌模型              | 🟢 已完成  |
| 11. Nayatani et al 模型   | 🟢 已完成  |
| 12. Hunt 模型             | 🟢 已完成  |
| 13. RLAB 模型             | 🟢 已完成  |
| 14. 其他色貌模型          | 🟢 已完成  |
| 15. CIECAM97s 模型        | 🟢 已完成  |
| 16. CIECAM02 模型         | 🟢 已完成  |
| 17. 色貌模型的测量        | 🟢 已完成  |
| 18. 传统色度学的应用      | 🟢 已完成  |
| 19. 设备无关的彩色成像    | 🟢 已完成  |
| 20. 图像色貌模型与未来    | 🟢 已完成  |
| 21. HDR 色彩空间          | 🟢 已完成  |


## 结语

色貌模型在科学、工程以及各类色彩应用领域中有着广泛的应用前景。通过了解人类视觉系统的工作原理，我们能够更加精准地描述和控制色彩在不同环境和设备中的表现。未来，随着高动态范围（HDR）和设备无关色彩成像技术的进一步发展，色貌模型的研究将继续拓展其应用范围，并为视觉科学和显示技术带来更多创新。

---

## 译者动机

这是一本颜色科学领域的经典著作，是该领域博士生的必读书籍。

但是很惭愧，我作为颜色科学领域的人，竟然没有通读过该书。所以，我翻译这本书，主要目的是**为了个人的学习！**

我想要通读本书，补足自己的颜色理论基础方面的不足。
如果是有其他目的，那就是希望对中国的颜色科学领域做一些小小的贡献，特别是对于工业界，**能够比较方便从业人员了解该领域**。


错误之处在所难免，本书还在持续翻译中，请读者不吝赐教！

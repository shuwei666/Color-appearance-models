# CIE 色貌模型（1997），CIECAM97s

本书第一版的出版恰逢第一版 CIE 色貌模型——CIECAM97s 的创建与发布。那时，显然人们对建立和使用单一的标准化色貌模型表现出了浓厚的兴趣，但人们仍不确定单一的 CIE 模型能有多大效用。工业界对这一模型的需求促使 CIE 加快了其努力，力求建立一个可以投入使用、测试，并且可能在之后被推荐为标准的模型。CIECAM97s 就是这样一个模型，它在色貌建模领域也代表了一项重要成就。本章概述了 CIECAM97s 的开发和制定过程。由于 CIE 后来开发了一个改进版模型——本书下一章的主题，因此本章并没有进行详细探讨。正如在下一章中将看到的那样，CIECAM97s 的实验是一次巨大的成功，并推动了色貌模型的真正进展。它的影响至今仍在继续，从 CIECAM02 的改进到提出的新型色貌模型的构想，都证明了这一点。

---
## 15.1 历史发展、目标与方法

1996年3月，CIE在维也纳举行了关于图像技术色彩标准的专家研讨会（CIE 1996b）。虽然该研讨会涵盖了CIE能够提供指导或标准的图像技术各个方面，但其中最关键的问题之一是为一般用途建立一个色貌模型。研讨会中的工业参与者认识到应用色貌模型的必要性，但要求CIE提供指导，以建立一个可以在整个行业中使用的单一模型，以促进实践的统一性和现代开放成像系统中各组件的兼容性。推动单一模型的需求在Hunt的演讲中得到了突出和总结，该演讲题为《色貌模型的功能、演变与未来》（CIE 1996b）。在演讲中，Hunt回顾了各种模型的现状和历史发展，并提出了建立单一模型时需要考虑的12个原则。这些原则在此原文复制（CIE 1996b）：

1. 模型应尽可能全面，以便可以用于多种应用；但在此阶段，由于动态效应的复杂性，应仅包括适应的静态状态。
2. 模型应涵盖广泛的刺激强度，从非常暗的物体颜色到非常亮的自发光颜色。这意味着动态响应函数必须有一个最大值，不能是简单的对数或幂函数。
3. 模型应涵盖广泛的适应强度，从非常低的暗视水平，如在星光下出现的视力，到非常高的光视水平，如在阳光下的视力。这意味着模型应包括视杆的视觉；但由于许多应用中视杆视觉是可以忽略的，因此该模型应能在不包括视杆视觉的模式下使用。
4. 模型应涵盖广泛的观察条件，包括不同亮度因子的背景，以及黑暗、昏暗和普通的周围环境。必须覆盖不同的周围环境，因为它们广泛应用于投影和自发光显示设备。
5. 为了便于使用，锥体的光谱敏感性应是CIE X、Y、Z或10X、10Y、10Z函数的线性变换，V′(l)函数应用于视杆的光谱敏感性。由于暗视的光度数据通常是未知的，因此应提供近似的暗视值方法。
6. 模型应能提供任何程度的适应，从完全适应到无适应，并能够处理认知因素和赫尔森–贾德效应作为可选项。
7. 模型应能预测色调（包括色调角度和色调四分象限）、亮度、明度、饱和度、色度和色彩感知度。
8. 模型应能反向操作。
9. 模型不应比满足上述要求所需的复杂。
10. 任何简化版本的模型，旨在特定应用中使用，应在某些指定条件下给出与完整模型相同的预测。
11. 模型应给出与在每个应用中最好的模型相比较不显著差的色貌预测。
12. 模型应有一个版本，能够应用于不相关的颜色（那些在黑暗环境中孤立地看到的颜色）。

研讨会的结论是，CIE应立即开始制定此类模型的工作，目标是使其在1997年5月国际色彩学会（AIC）四年一度的京都会议之前完成。CIE决定，TC1-34是最合适的委员会来完成这一工作，并在1996年CIE第一分会在哥德堡的会议上扩展了其任务范围，包含了以下内容：

推荐一个色貌模型。该模型应充分考虑其他相关技术委员会的研究成果。

TC1-34立即开始了CIE模型（包括简化版本和全面版本）的制定工作。CIE于1998年发布了关于简化版本CIECAM97s的技术报告（CIE 1998）。由于缺乏兴趣和需求，全面版本未能制定出来。TC1-34成员R.W.G. Hunt和M.R. Luo同意制定首批方程供委员会考虑。TC1-34的工作哲学是基本遵循Hunt提出的12个原则来开发全面的CIE模型和用于实际应用的简化版本。总体思路是开发一个全面的模型（像Hunt模型），可以应用于各种色貌现象，并且开发一个简化版本（像RLAB模型），足以用于如设备无关的色彩成像等应用，并附加一个约束，即这两种版本在某些特定条件下是兼容的。

在准备这些模型时，开发了Hunt色貌模型的修订版本。这些版本被称为Bradford–Hunt 96S（简化）模型和Bradford–Hunt 96C（全面）模型。这些模型代表了CIECAM97s制定过程中的一个中间步骤，并在本书第一版中进行了介绍（Fairchild 1998a），感谢作者（Hunt 1996，个人通信，10月14日）。这些模型没有被TC1-34批准为CIE模型，但它们为委员会提供了一个起点，并很好地说明了如何满足上述12个原则。正如预期的那样，这些模型在全面委员会考虑之前经历了一些重要的修订。

R.W.G. Hunt和M.R. Luo提供了两个修订后的模型供TC1-34在京都会议之前考虑。此外，M. Fairchild提供了第三个替代模型，K. Richter提供了第四个。1997年5月的TC1-34京都会议上考虑了这四个替代模型，并达成一致，决定采纳Hunt和Luo的一个替代方案作为CIE色貌模型1997的简化版，命名为CIECAM97s。该模型在以下章节中介绍。该模型正式由CIE批准并发布（CIE 1998）。至于扩展CIECAM97s的全面版本，即CIECAM97c，由于缺乏需求，最终没有制定出来。Fairchild提供了一个更简单的替代方案，在有限的观察条件下表现出类似的性能，但委员会并未推荐它，因为它不像选定成为CIECAM97s的模型那样能够扩展为全面版本。（事后看来，这不应成为一个关注点。）该模型被指定为ZLAB色貌模型，并在第15.7节中介绍，因为它在某些简单的图像再现应用中已被证明有用。

---
## 15.2 输入数据

为了得出TC1-34同意作为CIECAM97s模型（即CIE色貌模型（1997）简化版）的模型，略微对Bradford–Hunt 96S模型进行了重要的修订。这些修订包括围绕补偿的重新制定，采用幂函数以避免预测相应的颜色时出现负的CIE三刺激值，并且清晰地定义了适应水平因子D。需要注意的是，CIECAM97s的制定基于许多色貌领域研究者的工作。这是TC1-34在确立该模型为目前最佳模型时的一个关键问题。模型的各个方面可以追溯到（按字母顺序）Bartleson、Breneman、Fairchild、Estevez、Hunt、Lam、Luo、Nayatani、Rigg、Seim、Valberg等人的研究成果。由于从未制定出全面模型，那些对更极端观察条件（如发生漂白时的高亮度水平或视杆开始活跃时的低亮度水平）或更深奥的外观现象（如赫尔森–贾德效应）感兴趣的人，应该探讨使用第12章中描述的Hunt模型。

模型的输入数据包括适应场的亮度（通常假定为适应场中白色亮度的20%），LA，样本在源条件下的三刺激值XYZ，源条件下的源白色的三刺激值XwYwZw，源条件下的源背景的相对亮度Yb。此外，必须根据表15.1中的指南选择常数c（用于围绕影响）、Nc（色度诱导因子）、FLL（明度对比因子）和F（适应程度因子）。

---

**表15.1 CIECAM97s模型的输入参数**

| Viewing condition                           | c    | Nc   | FLL  | F    |
|---------------------------------------------|------|------|------|------|
| Average surround, samples subtending >4°    | 0.69 | 1.0  | 0.0  | 1.0  |
| Average surround                            | 0.69 | 1.0  | 1.0  | 1.0  |
| Dim surround                                | 0.59 | 1.1  | 1.0  | 0.9  |
| Dark surround                               | 0.525| 0.8  | 1.0  | 0.9  |
| Cut-sheet transparencies                    | 0.41 | 0.8  | 1.0  | 0.9  |

表15.1展示了CIECAM97s模型的输入参数，这些参数用于描述不同观察条件下的色彩适应与色度影响。具体内容如下：

- **Viewing condition**：观察条件，包括不同的环境背景亮度和周围条件（如一般环境、昏暗环境、黑暗环境等）。
- **c**：围绕影响因子，表示在不同观察条件下环境背景对色彩感知的影响程度。
- **Nc**：色度诱导因子，影响色度变化的参数。
- **FLL**：明度对比因子，影响明度对比的参数。
- **F**：适应程度因子，用于描述色彩适应的程度。

表格中的数据代表了不同环境条件下的这些参数设置，用于色貌模型的计算中。不同的观察条件影响这些因子的取值，从而影响最终的色彩预测。

---

## 15.3 适应模型

一个初始的色度适应变换被用来将源观察条件转换为等能量光照参考观察条件（尽管三刺激值在参考观察条件下并不需要表达）。首先，样本和白色的三刺激值都需要规范化并转换为光谱锐化的锥体响应，使用公式15.1和15.2进行变换。

<div class="math-block">
  <div class="equation">
    $$
    \begin{bmatrix}
    R \\
    G \\
    B
    \end{bmatrix} = M_B \begin{bmatrix}
    \frac{X}{Y} \\
    \frac{Y}{Y} \\
    \frac{Z}{Y}
    \end{bmatrix}
    \tag{15.1}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    M = \begin{bmatrix}
    0.8951 & 0.2664 & -0.1614 \\
    -0.7502 & 1.7135 & 0.0367 \\
    0.0389 & -0.0685 & 1.0296
    \end{bmatrix}
    \tag{15.2}
    $$
  </div>
</div>

色度适应变换是修改版的冯·克里斯（von Kries）变换（应用在一种色度坐标上），并加入了对短波长敏感通道的指数非线性，如公式15.3到15.6所示。此外，变量D被用来指定适应程度。D被设为1.0表示完全适应或忽略光源，D设为0.0表示不适应。D在不同的适应程度下会采取中间值，公式15.7用于计算不同亮度水平和周围条件下的D值。

<div class="math-block">
  <div class="equation">
    $$
    R_c = D \left[ \left( \frac{1.0}{R_w} \right) + 1 - D \right] R \tag{15.3}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    G_c = D \left[ \left( \frac{1.0}{G_w} \right) + 1 - D \right] G \tag{15.4}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    B_c = D \left[ \left( \frac{1.0}{B_w} \right) + 1 - D \right] |B|^p \tag{15.5}
    $$
  </div>
</div>

如果B值为负，那么B值也应为负。类似的变换也适用于源白色，因为它们在后续计算中是必需的。各种因素必须在进一步计算之前进行计算，如公式15.8到15.12所示。这些因素包括背景诱导因子n、背景和色度亮度诱导因子N_bb和N_cb，以及基本的指数非线性z。

<div class="math-block">
  <div class="equation">
    $$
    k = \frac{1}{5 L_A + 1} \tag{15.8}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    F_L = 0.2 k^4 (5 L_A) + 0.1 (1 - k^4)^2 (5 L_A)^{1/3} \tag{15.9}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    n = \frac{Y_b}{Y_w} \tag{15.10}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    N_{bb} = N_{cb} = 0.725 \left( \frac{1}{n} \right)^{0.2} \tag{15.11}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    z = 1 + F_{LL} n^{1/2} \tag{15.12}
    $$
  </div>
</div>

样本和源白色的后适应信号然后从锐化的锥体响应转化为Hunt–Pointer–Estevez锥体响应，如公式15.13和15.14所示，之后进行非线性响应压缩。

<div class="math-block">
  <div class="equation">
    $$
    \begin{bmatrix}
    R' \\
    G' \\
    B'
    \end{bmatrix} = M_H M_B^{-1} \begin{bmatrix}
    R Y \\
    G Y \\
    B Y
    \end{bmatrix}
    \tag{15.13}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    M_H = \begin{bmatrix}
    0.38971 & 0.68898 & -0.07868 \\
    -0.22981 & 1.18340 & 0.04641 \\
    0.00000 & 0.00000 & 1.00000
    \end{bmatrix}
    \tag{15.14}
    $$
  </div>
</div>

后适应锥体响应（针对样本和源白色）然后使用公式15.15至15.17进行计算。

<div class="math-block">
  <div class="equation">
    $$
    R'_a = \frac{40 \left( \frac{F_L R'}{100} \right)^{0.73}}{\left( \frac{F_L R'}{100} \right)^{0.73} + 2} \tag{15.15}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    G'_a = \frac{40 \left( \frac{F_L G'}{100} \right)^{0.73}}{\left( \frac{F_L G'}{100} \right)^{0.73} + 2} \tag{15.16}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    B'_a = \frac{40 \left( \frac{F_L B'}{100} \right)^{0.73}}{\left( \frac{F_L B'}{100} \right)^{0.73} + 2} \tag{15.17}
    $$
  </div>
</div>


---
## 15.4 色貌相关

初步的红绿对立维度和黄蓝对立维度是通过公式15.18和15.19计算得出的。

<div class="math-block">
  <div class="equation">
    $$
    a = R'_a - \frac{12 G'_a}{11} + \frac{B'_a}{11}
    \tag{15.18}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    b = \frac{1}{9} \left( R'_a + G'_a - 2 B'_a \right)
    \tag{15.19}
    $$
  </div>
</div>

接下来，色调角度 $h$ 通过公式15.20从 $a$ 和 $b$ 中计算得出。

<div class="math-block">
  <div class="equation">
    $$
    h = \tan^{-1} \left( \frac{b}{a} \right)
    \tag{15.20}
    $$
  </div>
</div>

色调四分象限 $H$ 和偏心因子 $e$ 是通过以下独特的色调数据按常规方式（线性插值）计算得出的：

- 红色：$h = 20.14^\circ, e = 0.8, H = 0 \text{ 或 } 400$
- 黄色：$h = 90.00^\circ, e = 0.7, H = 100$
- 绿色：$h = 164.25^\circ, e = 1.0, H = 200$
- 蓝色：$h = 237.53^\circ, e = 1.2, H = 300$

公式15.21和15.22展示了任意色调角度的 $e$ 和 $H$ 的计算，其中下标为1和2的数量表示在色调角度的上下方分别对应的独特色调。

<div class="math-block">
  <div class="equation">
    $$
    e = e_1 + \left( e_2 - e_1 \right) \frac{(h - h_1)}{(h_2 - h_1)} \tag{15.21}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    H = H_1 + \frac{100 (h - h_1)}{e_1} \frac{(h - h_1)}{(h_2 - h_1)} / e_2 \tag{15.22}
    $$
  </div>
</div>

色度响应是根据公式15.23对样本和白色进行计算的。

<div class="math-block">
  <div class="equation">
    $$
    A = \left[ 2 R'_a + G'_a + \left( \frac{1}{20} \right) B'_a - 2.05 \right] N_{bb}
    \tag{15.23}
    $$
  </div>
</div>

明度 $J$ 由样本和白色的色度信号使用公式15.24计算。

<div class="math-block">
  <div class="equation">
    $$
    J = 100 \left( \frac{A}{A_w} \right)^\alpha
    \tag{15.24}
    $$
  </div>
</div>

亮度 $Q$ 是通过明度和白色的色度计算得到的，使用公式15.25。

<div class="math-block">
  <div class="equation">
    $$
    Q = 1.24 \left( \frac{J}{100} \right)^{0.67} \left( A_w + 3 \right)^{0.9}
    \tag{15.25}
    $$
  </div>
</div>

最后，饱和度 $s$、色度 $C$ 和色彩感知度 $M$ 是通过公式15.26到15.28分别计算得出的。

<div class="math-block">
  <div class="equation">
    $$
    s = \frac{50 \left( a^2 + b^2 \right)^{1/2} 100 e \left( \frac{10}{13} \right) N_c N_{cb}}{R'_a + G'_a + \left( \frac{21}{20} \right) B'_a}    \tag{15.26}    $$  </div></div><div class="math-block">  <div class="equation">    $$    C = 2.44 s^{0.69} \left( \frac{J}{100} \right)^{0.67n} \left( 1.64 - 0.29n \right)    \tag{15.27}    $$  </div></div><div class="math-block">  <div class="equation">    $$    M = C F_L^{0.15}    \tag{15.28}    $$  </div></div>

---

## 15.5 逆模型

CIECAM97s 模型几乎可以被解析逆转，但由于在逆转过程中 Y 值的计算较为复杂（步骤 8），因此需要做出一个近似。从明度 $J$、色度 $C$ 和色调角度 $h$ 开始，逆转过程如下所示：

1. 从 $J$ 获得 $A$。
2. 从 $h$ 获得 $e$。
3. 使用 $C$ 和 $J$ 计算 $s$。
4. 使用 $s$、$h$ 和 $e$ 计算 $a$ 和 $b$。
5. 从 $A$、$a$ 和 $b$ 计算 $R'_a$、$G'_a$ 和 $B'_a$。
6. 从 $R'_a$、$G'_a$ 和 $B'_a$ 计算 $R'$、$G'$ 和 $B'$。
7. 从 $R'$、$G'$ 和 $B'$ 计算 $RcY$、$GcY$ 和 $BcY$。
8. 使用近似公式计算 $Y$，即从 $RcY$、$GcY$ 和 $BcY$ 计算 $Y$，使用 $1 B M^{-1}$ 近似。
9. 从 $RcY$、$GcY$ 和 $BcY$ 以及 $Y$ 计算 $Rc$、$Gc$ 和 $Bc$。
10. 从 $Rc$、$Gc$ 和 $Bc$ 计算 $R$、$G$ 和 $B$。
11. 从 $R$、$G$、$B$ 和 $Y$ 计算 $X$、$Y$ 和 $Z$。

---

CIECAM97s 虽然不能简单地以解析形式进行逆转，但其逆转过程比一些以前的模型要简单且更准确。因此，CIECAM97s 在实际应用中具有更大的实用性。逆转过程的详细说明可以参考 http://www.cis.rit.edu/ fairchild/CAM.html。

---
## 15.6 预测的现象

虽然 CIECAM97s 是一个相对简单的模型，但它在预测现象的种类上非常完整。它包括了所有重要的外观维度的相关因素（如明度、亮度、色度、色彩感知度、饱和度和色调），并且能够预测广泛的适应性、周围环境和亮度依赖性效应。它不适用于极高或极低的亮度水平，因为这些情况通常不涉及精确的颜色判断。表 15.2 中给出了使用 CIECAM97s 色貌模型进行的四个样本的示例计算，具体如本章所述。有关这些示例计算的电子表格，可以在 http://www.cis.rit.edu/ fairchild/CAM.html 网站找到。

---

**表 15.2 CIECAM97s 模型示例计算**

| Quantity              | Case 1  | Case 2  | Case 3  | Case 4  |
|-----------------------|---------|---------|---------|---------|
| X                     | 19.01  | 57.06  | 3.53   | 19.01  |
| Y                     | 20.00  | 43.06  | 6.56   | 20.00  |
| Z                     | 21.78  | 31.96  | 2.14   | 21.78  |
| Xw                    | 95.05  | 95.05  | 109.85 | 109.85 |
| Yw                    | 100.00 | 100.00 | 100.00 | 100.00 |
| Zw                    | 108.88 | 108.88 | 35.58  | 35.58  |
| LA                    | 318.31 | 31.83  | 318.31 | 31.83  |
| F                     | 1.0    | 1.0    | 1.0    | 1.0    |
| D                     | 0.997  | 0.890  | 0.997  | 0.890  |
| Yb                    | 20.0   | 20.0   | 20.0   | 20.0   |
| Nc                    | 1.0    | 1.0    | 1.0    | 1.0    |
| FLL                   | 1.17   | 0.54   | 1.17   | 0.54   |
| Nbb, Ncb              | 1.0    | 1.0    | 1.0    | 1.0    |
| H                     | 212.3  | 19.3   | 175.4  | 250.8  |
| Hc                    | 269.5  | 399.4  | 217.7  | 306.9  |
| J                     | 42.44  | 65.27  | 21.04  | 39.88  |
| Q                     | 32.86  | 31.88  | 20.54  | 22.96  |
| S                     | 0.15   | 146.98 | 232.18 | 180.56 |
| C                     | 0.50   | 61.96  | 72.99  | 66.85  |
| M                     | 0.51   | 56.52  | 74.70  | 60.98  |

---

上述表格展示了使用 CIECAM97s 模型计算得到的四个样本的色貌数据，包括各种外观属性的计算值。这些计算涵盖了从明度、亮度到色度、饱和度等多个维度的测量，为实际应用提供了有用的数据参考。

---

## 15.7 ZLAB 色貌模型

一个简单的模型是从提交给 TC1-34 委员会考虑的各种模型中推导出来的。最终，委员会认为需要一个更具可扩展性的模型来推荐为 CIECAM97s。因此，委员会放弃了这个简单模型，并由作者重新命名为 ZLAB 色貌模型（Fairchild 1998b）。该模型来源于 CIECAM97s、LLAB 和 RLAB 模型，并在 Luo 和 Hunt 提交给 TC1-34 的工作基础上进行重大改进。ZLAB 模型的设计目标是，在有限的观察条件下，其性能几乎与 CIECAM97s 模型相同。这些限制包括对适应亮度中间值的限制，因为超双曲非线性已被平方根函数替代，该平方根函数能很好地描述中间亮度水平下的超双曲函数。此外，ZLAB 模型还限制为中等灰色背景，以进一步简化计算。最后，ZLAB 模型仅限于预测明度、色度、饱和度和色调的相对外观属性，不能用于预测色彩感知度或亮度。这是由于去除了大多数亮度依赖性，导致公式大大简化。由于 ZLAB 模型使用相同的色度适应变换，它在大多数对应颜色计算中与 CIECAM97s 模型表现完全相同。它在预测外观缩放数据方面也表现得几乎一样好。ZLAB 模型在图像再现中得到了某些有用的应用，尤其是在色域映射和缺乏观察条件控制是主要限制因素时，避免了使用更复杂模型的需要。

---

**输入数据**

模型的输入数据包括适应场的亮度 $L_A$（通常取参考白色亮度的 0.2 倍），样本在源条件下的三刺激值 $XYZ$，以及源条件下的源白色的三刺激值 $X_wY_wZ_w$。

---

**色适应**

与 CIECAM97s 一样，Bradford 色度适应变换被用来将源观察条件转换为参考（等能量光源）观察条件下的相应颜色。首先，所有三组三刺激值都需要规范化，并使用 Bradford 变换转换为锐化的锥体响应，具体见公式 15.29 和 15.30。

<div class="math-block">
  <div class="equation">
    $$
    \begin{bmatrix}
    R \\
    G \\
    B
    \end{bmatrix} = M \begin{bmatrix}
    \frac{X}{Y} \\
    \frac{Y}{Y} \\
    \frac{Z}{Y}
    \end{bmatrix}
    \tag{15.29}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    M = \begin{bmatrix}
    0.8951 & 0.2664 & -0.1614 \\
    -0.7502 & 1.7135 & 0.0367 \\
    0.0389 & -0.0685 & 1.0296
    \end{bmatrix}
    \tag{15.30}
    $$
  </div>
</div>

色度适应变换是修改版的冯·克里斯变换（应用在一种色度坐标上），并加入了对短波长敏感通道的指数非线性，如公式 15.31 到 15.34 所示。此外，变量 D 被用来指定适应程度。D 被设为 1.0 表示完全适应或忽略光源，D 设为 0.0 表示不适应。D 在不同的适应程度下会采取中间值，公式 15.35 用于计算不同亮度水平和周围条件下的 D 值。

<div class="math-block">
  <div class="equation">
    $$
    R_c = D \left[ \left( \frac{1.0}{R_w} \right) + 1 - D \right] R
    \tag{15.31}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    G_c = D \left[ \left( \frac{1.0}{G_w} \right) + 1 - D \right] G
    \tag{15.32}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    B_c = D \left[ \left( \frac{1.0}{B_w} \right) + 1 - D \right] |B|^p
    \tag{15.33}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    p = \left( \frac{B_w}{1.0} \right)^{0.0834}
    \tag{15.34}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    D = F - F / \left[ 1 + 2 \left( \frac{L_A^{1/4}}{A} \right) + \left( \frac{L_A^2}{300} \right) \right]
    \tag{15.35}
    $$
  </div>
</div>

如果 B 为负值，则 B_c 也应设为负。R_c、G_c 和 B_c 表示参考条件下测试刺激的相应颜色。适应过程的最后一步是将锐化的锥体响应转换回 CIE XYZ 三刺激值，如公式 15.36 所示。

<div class="math-block">
  <div class="equation">
    $$
    \begin{bmatrix}
    X_c \\
    Y_c \\
    Z_c
    \end{bmatrix} = M^{-1} \begin{bmatrix}
    R Y \\
    G Y \\
    B Y
    \end{bmatrix}
    \tag{15.36}
    $$
  </div>
</div>

---

**色貌相关**

对立反应使用修改过的 CIELAB 类型方程进行计算，方程中包含由周围环境相对亮度定义的幂函数非线性。这些方程源自对 CIECAM97s 模型的简化，记得 CIECAM97s 中的超双曲非线性函数可以通过平方根函数来近似，适用于中间亮度水平。因此，对立反应简化为公式 15.37 和 15.38 给出的形式。

<div class="math-block">
  <div class="equation">
    $$
    A = 500 \left[ \left( \frac{X_c}{100} \right)^{\frac{1}{\sigma}} - \left( \frac{Y_c}{100} \right)^{\frac{1}{\sigma}} \right]^{\frac{1}{\sigma}}
    \tag{15.37}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    B = 200 \left[ \left( \frac{Y_c}{100} \right)^{\frac{1}{\sigma}} - \left( \frac{Z_c}{100} \right)^{\frac{1}{\sigma}} \right]^{\frac{1}{\sigma}}
    \tag{15.38}
    $$
  </div>
</div>

这些指数与 CIECAM97s 中使用的指数直接相关，如表 15.3 所示。在 ZLAB 中，CIECAM97s 中的 1/$\sigma$（称为 c）值被修改为 1/2$\sigma$，以便将平方根近似引入 CIECAM97s 的超双曲非线性。

色调角度 $h_z$ 按照常规方式计算，如公式 15.39 所示。

<div class="math-block">
  <div class="equation">
    $$
    h_z = \tan^{-1} \left( \frac{B}{A} \right)
    \tag{15.39}
    $$
  </div>
</div>

色调组合也通过线性插值的方式确定，插值是基于定义的唯一色调角度。这些色调角度为 $h_r = 25^\circ, h_g = 165^\circ, h_b = 254^\circ$。

ZLAB 模型仅用于中等亮度（20%）背景，因此 CIECAM97s 模型中的 z 参数取常数值 1.45，明度 $L_z$ 如公式 15.40 所示。

<div class="math-block">
  <div class="equation">
    $$
    L_z = 100 \left( \frac{Y_c}{100} \right)^{\frac{1.45}{\sigma}}
    \tag{15.40}
    $$
  </div>
</div>

---

**ZLAB 周围参数**

| Surround      | 平均值 (Average) | 昏暗 (Dim) | 黑暗 (Dark) |
|---------------|------------------|------------|-------------|
| 1/$\sigma$    | 0.69             | 0.59       | 0.525       |
| 1/2$\sigma$   | 0.345            | 0.295      | 0.2625      |

---

色度 $C_z$ 由公式 15.41 给出，这是 LLAB 模型中最初定义的，以良好预测量化估计数据。饱和度 $s_z$ 仅仅是色度与明度的比值，如公式 15.42 所示。

<div class="math-block">
  <div class="equation">
    $$
    C_z = 25 \log_e \left[ 1 + 0.05 \left( A^2 + B^2 \right)^{1/2} \right]
    \tag{15.41}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    s_z = \frac{C_z}{L_z}
    \tag{15.42}
    $$
  </div>
</div>

如果需要矩形坐标来表示色彩空间，可以通过以下公式从 $C_z$ 和 $h_z$ 获得。

<div class="math-block">
  <div class="equation">
    $$
    a_z = C_z \cos(h_z)
    \tag{15.43}
    $$
  </div>
</div>

<div class="math-block">
  <div class="equation">
    $$
    b_z = C_z \sin(h_z)
    \tag{15.44}
    $$
  </div>
</div>

---

**逆模型**

ZLAB 模型在逆向操作时非常简单。从明度、色度和色调角度开始，按照以下步骤进行计算：

1. 从 $C_z$ 计算 $(A^2 + B^2)^{1/2}$。
2. 从 $(A^2 + B^2)^{1/2}$ 和 $h_z$ 计算 $A$ 和 $B$。
3. 从 $L_z$、$A$ 和 $B$ 计算 $X_c$、$Y_c$ 和 $Z_c$。
4. 从 $X_c$、$Y_c$ 和 $Z_c$ 计算 $R_c$、$G_c$ 和 $B_c$。
5. 从 $R_c$、$G_c$ 和 $B_c$ 计算 $R$、$G$ 和 $B$。
6. 从 $R$、$G$ 和 $B$ 计算 $X$、$Y$ 和 $Z$。

---

## 15.8 为什么不只使用 CIECAM97s？ 

CIE TC1-34 能在一年内达成共识，推导出 CIECAM97s 模型，作为其目标之一，这是一次真正前所未有的事件。正如本书第一版中所预期的那样，CIE 的批准程序并未对模型进行重大更改。需要注意的是，CIECAM97s 被视为一个过渡模型，预计随着更多数据和理论理解的深入，它将被修订。工业界对 CIECAM97s 模型的反应强烈，并迅速将其应用于商业领域，特别是在影像产业中。CIECAM97s 的应用以及进一步的科学研究很快揭示了其公式和性能的局限性，并为改进提供了额外的数据。

CIECAM97s 的巨大成功在于它为色貌研究和工程领域的研究人员提供了集中研究的焦点。由于许多人专注于一个模型进行测试和改进，因此能够迅速做出显著的进步。其成果就是 CIECAM02 色貌模型，详细内容将在第16章讨论。CIECAM02 的存在是为什么不只使用 CIECAM97s 的原因之一。CIECAM02 是一个更简化的公式，且具有更好的性能。此外，CIECAM97s 对于某些应用可能过于复杂。在这种情况下，像 ZLAB、RLAB 或者结合色度适应变换与 CIELAB 的模型可能已足够。

---

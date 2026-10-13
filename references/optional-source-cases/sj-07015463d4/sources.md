# InvMM 案例的来源与核查范围

## 来源身份

- 主源：[An Inversion-based Measure of Memorization for Diffusion Models](https://arxiv.org/pdf/2405.05846v3)，arXiv:2405.05846v3，2025-07-31。下列 pp.1–8 均为正文印刷页，与 PDF 物理页一致
- 近邻：[Image-level Memorization Detection via Inversion-based Inference Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/7786a4f1ba8d7f696506fbec2e23487a-Paper-Conference.pdf)，ICLR 2025 正式版，简称 IIP
- InvMM 共同署名含 Shouling Ji；具体写法不可归因于某位作者个人。IIP 对 Ma et al. 2024 早期版的评论，不自动适用于 InvMM v3

## 案例逐节定位

### 1. 阴性观察的判断缺口

[InvMM §1 p.2](https://arxiv.org/pdf/2405.05846v3#page=2) 左栏：承认已能发现高度记忆图像，随后区分有限采样未出现与记忆较低，再讨论大潜空间、条件输入及配对 caption 未触发的局限。把这些内容归为两类认识局限是编辑归纳，原文未正式编号“两项挑战”。

### 2. 强近邻与剩余问题

[InvMM §2.1 pp.2–3](https://arxiv.org/pdf/2405.05846v3#page=3)：p.2 右栏承认既有实例级度量，p.3 左栏末明确讨论 IIP；§2.2 承认既有反演技术。

[IIP §1 p.2](https://proceedings.iclr.cc/paper_files/paper/2025/file/7786a4f1ba8d7f696506fbec2e23487a-Paper-Conference.pdf#page=2) 说明检测只需图像、不需原始配对提示；[§2.1 p.3](https://proceedings.iclr.cc/paper_files/paper/2025/file/7786a4f1ba8d7f696506fbec2e23487a-Paper-Conference.pdf#page=3) 的 unconditional DDIM inversion 采用空文本提示；[§3–3.2 pp.5–6](https://proceedings.iclr.cc/paper_files/paper/2025/file/7786a4f1ba8d7f696506fbec2e23487a-Paper-Conference.pdf#page=5) 使用文本编码器、提示 embedding 和条件噪声预测。§4.1 pp.6–7 的主体评测以 SD v1.4 为基础，其他 SD 版本置于附录。核查支持已给出方法的文本条件依赖，不证明它不可能扩展至其他模型。

### 3. 量、估计与证据的职责

[InvMM §1 p.2](https://arxiv.org/pdf/2405.05846v3#page=2) 左下至右上：三项贡献分别公布连续度量及分布反演、提供自适应计算方法、给出评价与测量认识。将其概括为量／估计／证据，是有文本支持的职责分析，不是作者正式命名。

[§4.1–4.4 pp.3–5](https://arxiv.org/pdf/2405.05846v3#page=3)：§4.1 的复制判据为 SSCD 距离阈值；§4.2 Eq.(9) 给出理想复制约束及按潜空间维数归一化的最小 KL；§4.3 使用去噪代理、对角高斯及有限生成样本验收。模型预测与梯度访问是实现条件，失败返回无穷不证明无记忆。边界另见 [§6 p.8](https://arxiv.org/pdf/2405.05846v3#page=8)。

[§5.2 p.6 / Fig.3](https://arxiv.org/pdf/2405.05846v3#page=6)：固定 λ=1 在两个所测子集大量反演失败，λ=0 与 adaptive 均可成功反演；不能改成只有自适应有效。

[§5.4 pp.7–8 / Table 1](https://arxiv.org/pdf/2405.05846v3#page=7)：固定提示比较中，SD v1.4 上 Wen 的 AUC 为 0.999、TPR@1%FPR 为 0.868；InvMM 分别为 0.974、0.908。两项指标优势方向不同；表中没有 IIP 行。

[§5.1 p.6](https://arxiv.org/pdf/2405.05846v3#page=6) 定义 confirmed、suspicious 与 normal；suspicious 是另 50 幅高重复且配对 caption 未触发的图像。[Fig.9a–b p.7](https://arxiv.org/pdf/2405.05846v3#page=7) 展示联合提示反演和触发实例；[§5.4 p.8](https://arxiv.org/pdf/2405.05846v3#page=8) 给出联合提示反演解释与 GCG 正文说明。部分 suspicious 图像分数接近 confirmed，GCG 实例支持其他提示可触发复制；不能把全部样本写成已验证可提取。

[§5.5 p.8 / Fig.10](https://arxiv.org/pdf/2405.05846v3#page=8) 对比成员身份与图像复现程度。§5.4 p.8 的共同标准高斯参照解释，不构成任意模型、数据集下的风险校准。

### 4. 编辑示范的身份

案例中的两句中文均为编辑创作，不是论文引句；凝练版改选信息，先呈现有限采样阴性结果留下的判断困难，再由后文引入本文所选度量。它不是严格保义替换，不涵盖所有检测器，也不能独自代替强近邻定位。

## 核查范围与边界

固定源核查于 2026-10-11 完成：InvMM 覆盖完整 §1、§2.1–2.2、§4.1–4.4、§5.1–5.5 及 §6，视觉核对 p.2 贡献段与 p.7 表图；IIP 覆盖完整引言、§2.1–2.2、§3–3.2 及 §4.1 主体设置。未通读全部附录、未独审 IIP 全部实验、未复现实验或完成穷尽文献检索。案例整合依据该来源核查，不额外声称重新独审全篇。

编辑示范未经过实验验证，不能据此认定写作质量或读者理解有所提升。

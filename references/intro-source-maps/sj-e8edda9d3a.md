# Pluggable Watermarking：完整引言句级图

- 来源身份：sj-e8edda9d3a
- 指定版本：Official IJCAI2024 proceedings PDF, 9 physical pages, printed pp.331-339
- 指定原文：https://www.ijcai.org/proceedings/2024/0037.pdf
- 实际读取原文：https://www.ijcai.org/proceedings/2024/0037.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#pluggable-watermarking) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [C1](#c1) · [C2](#c2) · [C3](#c3) · [C4](#c4)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

Source https://www.ijcai.org/proceedings/2024/0037.pdf;officialIJCAI2024,331–339. Full introduction physical1–2; §3.1 scenario reread. PDF extraction starts right-column related-work paragraph before left-column intro; map restores opening→prior approaches→method→summary.
Chain P1 forged-face threat; P2 passive limits then progressively stronger active methods and model/cost constraints; P3 common decoder structure enables parameter-level watermarking; four inline contributions. 推断：通用性不是来自“支持八模型”这句话，而由共同卷积结构和不依赖原训练的可插拔位置解释；归一化放在参数分布差异被提出之后，承担跨模型稳定性。
<a id="p1"></a><a id="p1-s1"></a>P1.S1 能力：deepfake→人脸替换 | 起题 | task
<a id="p1-s2"></a>P1.S2 后果：滥用扩散→媒体可信度 | 因果 | detection value
<a id="p1-s3"></a>P1.S3 需求：风险→人脸伪造检测 | 归结 | P2
<a id="p2"></a><a id="p2-s1"></a>P2.S1 现有路线：passive→生物/高频伪迹 | 能力 | baseline
<a id="p2-s2"></a>P2.S2 条件变化：更真实/有损传播→伪迹检测失败 | 转折 | robustness
<a id="p2-s3"></a>P2.S3 迁移边界：依训练数据→新模型泛化弱 | 添加 | generality
<a id="p2-s4"></a>P2.S4 替代：边界→主动水印 | 转向 | method class
<a id="p2-s5"></a>P2.S5 能力：标记植入生成图→抽取识别 | 解释 | task
<a id="p2-s6"></a>P2.S6 目标差异：用户溯源水印→不直接适配deepfake检测 | 限定 | object
<a id="p2-s7"></a>P2.S7 路线：数据/后处理水印 | 分型 | comparison
<a id="p2-s8"></a>P2.S8 弱点：额外步骤/网络→易发现移除 | 根因 | covert parameter
<a id="p2-s9"></a>P2.S9 另一边界：模型专用→结构要求 | 并列 | common decoder
<a id="p2-s10"></a>P2.S10 代价：嵌入→重训/微调 | 添加 | efficiency
<a id="p2-s11"></a>P2.S11 加重：有的→逐样本推理训练 | 深化 | efficiency
<a id="p2-s12"></a>P2.S12 规模后果：众多模型→成本不可接受 | 因果 | plug-in
<a id="p2-s13"></a>P2.S13 问题归结：模型水印→检测任务仍待解决 | 综合 | work
<a id="p3"></a><a id="p3-s1"></a>P3.S1 工作：上述挑战→可插拔主动框架 | 响应 | C1
<a id="p3-s2"></a>P3.S2 观察：异构latent→解码器普遍卷积上采样 | 关键共性 | generality
<a id="p3-s3"></a>P3.S3 决策：共性→改decoder卷积参数 | 因果 | M
<a id="p3-s4"></a>P3.S4 位置：预训剪枝稀疏化→冗余参数位置 | 操作 | C2
<a id="p3-s5"></a>P3.S5 嵌入：位置→水印参数 | 次序 | M
<a id="p3-s6"></a>P3.S6 价值：冗余位置→保质量且独立原训练 | 因果 | C1/C4
<a id="p3-s7"></a>P3.S7 新障碍响应：核参数多样→归一化保稳定防梯度爆炸 | 原因—设计 | C2
<a id="p3-s8"></a>P3.S8 效率：只训替换参数 | 添加 | E
<a id="p3-s9"></a>P3.S9 稳健：BCH→抽取准确性鲁棒性 | 添加 | E
<a id="c1"></a><a id="c1-s1"></a>C1.S1 方法：主动模型水印→deepfake检测 | 归纳 | M
<a id="c1-s2"></a>C1.S2 属性：可插拔→独立原训练 | 归纳 | deployment
<a id="c2"></a><a id="c2-s1"></a>C2.S1 技术：稀疏化/归一化→隐蔽嵌入且保性能 | 归纳 | M/E
<a id="c3"></a><a id="c3-s1"></a>C3.S1 范围：可扩展→八类生成模型 | 新证据范围 | E
<a id="c4"></a><a id="c4-s1"></a>C4.S1 联合结论：鲁棒嵌入抽取→保持图像质量 | 新评价概括 | E
Ending: mechanisms known, model breadth and empirical claims newly supplied. Four numbered items are a single summary paragraph, not four full physical paragraphs. Active detection assumes supervisor can distribute watermarked models; unmarked images go to further detection in Fig1, so watermark absence is not proof an image is genuine.

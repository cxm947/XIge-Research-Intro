# CAMH：完整引言句级图

- 来源身份：sj-2ada62afcb
- 指定版本：arXiv:2408.13741v2, 20 December 2024
- 指定原文：https://arxiv.org/pdf/2408.13741v2
- 实际读取原文：https://arxiv.org/pdf/2408.13741v2
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#camh) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [C1](#c1) · [C2](#c2) · [C3](#c3)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

Source https://arxiv.org/pdf/2408.13741v2;20Dec2024 v2/AAAI2025 imprint. Full introduction pp.1–2 and §2 relationship to backdoor/model-hijacking reread.
Chain P1 training cost→outsourcing; P2 threat definition; P3 distinct accountability/parasitic risks; P4 prior work and class/distribution conditions; P5 three questions; P6 matched mechanisms and metrics/results; C1–3. 推断：先解释原任务不损坏为何决定隐蔽性，CR/ER的双轴才有研究意义；不把“可做新任务”单独当成功。
<a id="p1"></a><a id="p1-s1"></a>P1.S1 定位：ML→高后果领域 | 起题 | risk
<a id="p1-s2"></a>P1.S2 成本：训练→算力及专家调参 | 原因 | outsourcing
<a id="p1-s3"></a>P1.S3 选择：成本→第三方训练/预训模型 | 因果 | attack access
<a id="p2"></a><a id="p2-s1"></a>P2.S1 风险：外包复用→模型劫持 | 转折 | threat
<a id="p2-s2"></a>P2.S2 定义：劫持→强制执行异于原任务 | 解释 | task distinction
<a id="p2-s3"></a>P2.S3 后果分类：成功→责任/寄生计算 | 下启 | P3
<a id="p3"></a><a id="p3-s1"></a>P3.S1 风险一：被改用途→违法不伦理而主人不知 | 解释例证 | practical stakes
<a id="p3-s2"></a>P3.S2 后果：不知情→主人被误责 | 因果 | accountability
<a id="p3-s3"></a>P3.S3 风险二：他人模型→攻击者免运行维护成本 | 并列 | parasitic computing
<a id="p4"></a><a id="p4-s1"></a>P4.S1 历史：Salem→提出劫持 | 近邻 | baseline
<a id="p4-s2"></a>P4.S2 实际能力：训练改向→图像分类变识别 | 具体化 | target tasks
<a id="p4-s3"></a>P4.S3 后果：攻击→性能损失和责任风险 | 评价 | tradeoff
<a id="p4-s4"></a>P4.S4 更强近邻：Si→超图像复杂场景 | 递进 | scope
<a id="p4-s5"></a>P4.S5 共性机制：训练数据投毒→输出类别受原任务限制 | 归纳根因 | category-agnostic
<a id="p4-s6"></a>P4.S6 限制：输出受限→类别数/分布条件 | 推论 | challenges
<a id="p4-s7"></a>P4.S7 失败条件：违背条件→性能难平衡导致暴露/失败 | 因果 | CR/ER
<a id="p5"></a><a id="p5-s1"></a>P5.S1 目标：旧限制→扩展攻击适用性 | 研究意图 | C1
<a id="p5-s2"></a>P5.S2 组织：实现→三挑战 | 预告 | next
<a id="p5-c1"></a>P5.C1 类别问题：原输出空间→更多劫持类 | 问句 | synchronized layers
<a id="p5-c2"></a>P5.C2 分布问题：两任务不同分布→有效劫持 | 问句 | noise optimization
<a id="p5-c3"></a>P5.C3 双任务问题：劫持效果→原任务保留 | 问句 | dual loop
<a id="p6"></a><a id="p6-s1"></a>P6.S1 工作：三挑战→CAMH | 响应 | C1
<a id="p6-s2"></a>P6.S2 对应一：异类数→同步训练层 | 平行回应 | M
<a id="p6-s3"></a>P6.S3 对应二：分布变化→噪声优化 | 平行回应 | M
<a id="p6-s4"></a>P6.S4 对应三：原性能→双循环 | 平行回应 | M
<a id="p6-s5"></a>P6.S5 判据：全面评估→CR/ER | 转评价 | E
<a id="p6-s6"></a>P6.S6 定义：两指标→原/劫持任务相对良性性能 | 对照 | results
<a id="p6-s7"></a>P6.S7 范围：五基准/两架构→检验 | 证据 | C3
<a id="p6-s8"></a>P6.S8 主结果：多数ER>85%且CR约98% | 联合结果 | E
<a id="c1"></a><a id="c1-s1"></a>C1.S1 能力：CAMH→突破劫持类别数不超过原类数 | 归纳 | novelty source claim
<a id="c2"></a><a id="c2-s1"></a>C2.S1 技术：三个机制→各自三个挑战 | 归纳 | M
<a id="c3"></a><a id="c3-s1"></a>C3.S1 证据：多个数据架构→有效性 | 归纳 | E
<a id="c3-s2"></a>C3.S2 新条件：四倍类别，或劫持数据量低至30%→ER仍>85% | 两项以or连接的压力条件，不是二者同时的组合条件 | robustness
Ending: framework/mechanism/evaluation summary already given, yet C3 adds two difficulty settings. Do not shorten it simply because85% appeared before: same number under a harder condition conveys new evidence. The source joins the fourfold-category condition and the 30%-data condition with “or”; it does not assert their simultaneous combination. No inference that all hijacking threat models permit weight changes; source access conditions must accompany transfer.

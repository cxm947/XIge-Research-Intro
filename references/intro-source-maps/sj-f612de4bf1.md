# Is Your Explanation Stable?：完整引言句级图

- 来源身份：sj-f612de4bf1
- 指定版本：arXiv:2209.01782v1, 5 September 2022
- 指定原文：https://arxiv.org/pdf/2209.01782v1
- 实际读取原文：https://arxiv.org/pdf/2209.01782v1
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#metfa) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [P8](#p8) · [C1](#c1) · [C2](#c2) · [C3](#c3) · [C4](#c4)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

Source https://arxiv.org/pdf/2209.01782v1;5Sep2022 v1,CCS2022 author version19pp. Full introduction pp.1–3 and §2 explanation taxonomy reread.
Chain P1 trustworthy DNN decisions; P2 feature attribution use; P3 stochastic/deterministic routes have distinct instability; P4 needed uncertainty quantification and existing smoothing; P5 asymptotic bounds fail desired small-sample efficiency; P6 median-testing and two output needs; P7 multimodal evaluations; P8 applications; four contributions. 推断：作者没有把平滑平均写成无效，而先推出它能做什么，甚至主动加强为可给渐近区间，再说明未知分布/小样本时不能保障；中位数统计选择因此同时服务稳健性、有限样本推断和计算成本。
<a id="p1"></a><a id="p1-s1"></a>P1.S1 定位：DNN表现→深度学习广用 | 起题 | trust
<a id="p1-s2"></a>P1.S2 风险：人类级表现→安全危机/敏感场景不信任 | 让步 | explanation
<a id="p1-s3"></a>P1.S3 现有应对：可靠性→解释模型 | 缩域 | method class
<a id="p1-s4"></a>P1.S4 价值：解释→偏差异常及改进洞察 | 后果 | applications
<a id="p2"></a><a id="p2-s1"></a>P2.S1 任务：模型解释→实例级feature attribution | 定义 | §2
<a id="p2-s2"></a>P2.S2 产物：特征→贡献分数 | 解释 | score uncertainty
<a id="p2-s3"></a>P2.S3 命名：高贡献→supportive features | 定义 | significance
<a id="p2-s4"></a>P2.S4 实例：图像→attribution map | 举例 | visual E
<a id="p2-s5"></a>P2.S5 用途：图→看预测依赖区域 | 解释 | trust
<a id="p2-s6"></a>P2.S6 外延：归因→改进模型 | 添加 | application
<a id="p2-s7"></a>P2.S7 例：方法→debug/对抗检测/context bias | 具体化 | P8
<a id="p3"></a><a id="p3-s1"></a>P3.S1 缺口：解释工具→自身可靠性危机 | 转折 | uncertainty
<a id="p3-s2"></a>P3.S2 分类：方法→black/white-box | 组织 | sources
<a id="p3-s3"></a>P3.S3 黑盒条件：只可输入输出 | 定义 | stochasticity
<a id="p3-s4"></a>P3.S4 机制：采样→解释不确定 | 因果 | significance
<a id="p3-s5"></a>P3.S5 例：LIME同图→独立运行不同图 | 支持 | Fig1
<a id="p3-s6"></a>P3.S6 白盒能力：确定梯度激活→同输入确定 | 对照 | next
<a id="p3-s7"></a>P3.S7 边界：确定性→仍不稳定 | 转折 | perturbation
<a id="p3-s8"></a>P3.S8 例：近似输入梯度图大变/非稳健特征优化怪图 | 支持 | robustness
<a id="p3-s9"></a>P3.S9 安全意义：敏感解释→更易对抗 | 深化 | attack defense
<a id="p3-s10"></a>P3.S10 例：不可见扰动→任意改归因 | 具体化 | Fig1
<a id="p3-s11"></a>P3.S11 后果：现象→削弱解释信任 | 归结 | P4
<a id="p4"></a><a id="p4-s1"></a>P4.S1 归纳：采样/非稳健特征→不确定结果 | 回收 | task
<a id="p4-s2"></a>P4.S2 要求：可靠解释→减少且量化不确定 | 推论 | output
<a id="p4-s3"></a>P4.S3 自然解：邻域采样→平均解释 | 候选 | SmoothGrad
<a id="p4-s4"></a>P4.S4 命名实例：Gradient上平均→SmoothGrad | 具体化 | baseline
<a id="p4-s5"></a>P4.S5 已有能力：大数定律→期望收敛/缓和不确定 | 因果 | comparison
<a id="p5"></a><a id="p5-s1"></a>P5.S1 加强近邻：稳定方法→样本std也可量化 | 让步扩展 | fair gap
<a id="p5-s2"></a>P5.S2 具体：CLT/均值方差→渐近置信界 | 解释 | §7
<a id="p5-s3"></a>P5.S3 推导导航：界→§7 | 证据位置 | related comparison
<a id="p5-s4"></a>P5.S4 条件：该界→需很大样本 | 转折 | small sample
<a id="p5-s5"></a>P5.S5 代价：采样解释贵→重开销 | 因果 | efficiency
<a id="p5-s6"></a>P5.S6 另一个根因：少样本均值→极值敏感 | 添加 | median
<a id="p5-s7"></a>P5.S7 统一障碍：未知分布少样本→无这些方法的理论界 | 归结 | exact tests
<a id="p5-s8"></a>P5.S8 研究问题：上述限制→高效量化未决 | 总结 | MeTFA
<a id="p6"></a><a id="p6-s1"></a>P6.S1 工作：挑战→MeTFA | 响应 | C2
<a id="p6-s2"></a>P6.S2 观念：单点分数→还需区间和显著性 | 改变产物 | C1
<a id="p6-s3"></a>P6.S3 核心：邻域解释样本→假设检验保证 | 原理 | M
<a id="p6-s4"></a>P6.S4 选择：未知分布/极值→中位数非期望 | 原因—决策 | tests
<a id="p6-s5"></a>P6.S5 作用：统计量转Bernoulli→不靠CLT且少样本精确界 | 机制 | guarantee
<a id="p6-s6"></a>P6.S6 需求两类：显著重要性/分数置信界 | 分流 | one/two sided
<a id="p6-s7"></a>P6.S7 适用：离散二值→第一类更广；连续→第二类 | 条件区分 | output contracts
<a id="p6-s8"></a>P6.S8 一侧构造：用户阈值/置信水平→显著图 | 操作 | C2
<a id="p6-s9"></a>P6.S9 解释产物：显著图→中位数高/低于阈值 | 定义 | use
<a id="p6-s10"></a>P6.S10 双侧构造：特征→中位数置信区间 | 平行 | C2
<a id="p6-s11"></a>P6.S11 平滑：区间内分数平均→中位数近似图 | 次序 | robust explanation
<a id="p6-s12"></a>P6.S12 差别：区间内→不同于全样本平均 | 对照 | SmoothGrad
<a id="p6-s13"></a>P6.S13 图证：两种方法→重要特征及攻击修复 | 举证 | Fig1
<a id="p6-s14"></a>P6.S14 一致性：理论经验→方差趋零 | 保证 | M/E
<a id="p6-s15"></a>P6.S15 比较：收敛不慢于SmoothGrad→稳定效率 | 比较 | E
<a id="p7"></a><a id="p7-s1"></a>P7.S1 视觉范围：四类型代表归因→方法无关评价 | 验证范围 | C3
<a id="p7-s2"></a>P7.S2 判据：insertion/deletion/overall及std→忠实/稳定 | 定义 | E
<a id="p7-s3"></a>P7.S3 新判据：robust三指标→稳健特征定位 | 添加产物 | C3
<a id="p7-s4"></a>P7.S4 结果：原点忠实略变→邻域忠实大增 | 权衡 | claim limits
<a id="p7-s5"></a>P7.S5 比较：MeTFA→比SmoothGrad稳 | 追加 | E
<a id="p7-s6"></a>P7.S6 NLP范围：LEMNA/RNN→第二域 | 扩展 | generality
<a id="p7-s7"></a>P7.S7 判据：删除/增加/合成及std/top-n→同轴评价 | 具体化 | E
<a id="p7-s8"></a>P7.S8 新判据：视觉→三NLP对应稳健指标 | 类比 | C3
<a id="p7-s9"></a>P7.S9 结果：LEMNA→忠实稳定稳健忠实均改善 | 综合 | C3
<a id="p8"></a><a id="p8-s1"></a>P8.S1 下游设计：两测试→两安全应用 | 转价值验证 | C4
<a id="p8-s2"></a>P8.S2 一侧应用：GridSaliency→context bias定位 | 具体化 | E
<a id="p8-s3"></a>P8.S3 结果：常见噪声→区域缩小且99%+忠实 | 联合条件结果 | practical value
<a id="p8-s4"></a>P8.S4 双侧应用：两相反攻击目的→都可防御 | 并列 | C4
<a id="c1"></a><a id="c1-s1"></a>C1.S1 观念贡献：可靠解释→分数+区间+显著性 | 归纳 | P6
<a id="c2"></a><a id="c2-s1"></a>C2.S1 方法贡献：量化不确定/增稳定→理论保证 | 归纳 | M
<a id="c3"></a><a id="c3-s1"></a>C3.S1 判据贡献：单点→邻域指标 | 归纳 | E
<a id="c3-s2"></a>C3.S2 结果：增稳定→保持忠实 | 综合 | E
<a id="c4"></a><a id="c4-s1"></a>C4.S1 应用贡献：context bias及解释攻击→实践潜力 | 归纳 | applications
Ending: all products and extensive evaluation previewed; four inline contributions differentiate perspective, framework, metrics, applications. The evaluation summary compresses a nuanced earlier result (“slightly affects” original-input faithfulness); reuse should preserve domain/metric nuance rather than claiming universal no-loss faithfulness. Statistical guarantees concern chosen neighborhood perturbation and explanation-score distribution, not correctness of the underlying model's decision.

<a id="supplement-body-rationale"></a>
## 正文补读：中央分数子集的选择理由（M.9）

- 来源：sj-f612de4bf1，arXiv:2209.01782v1，19页；[§4.2，PDF p.5](https://arxiv.org/pdf/2209.01782v1#page=5)、[Theorem 4，PDF p.6](https://arxiv.org/pdf/2209.01782v1#page=6)、[§5.3.1，PDF pp.8–9](https://arxiv.org/pdf/2209.01782v1#page=8)
- 本轮补读：2026-10-04，直接核读同版缓存原文的上述正文段落；PDF SHA-256：bd5271d93ef8b39ef7f5acbc08cf1c2f692165405158ef4bfcd2d13f86652d14。以下是正文释义，不是引言P/S坐标；不能把其编号回填成引言句号
- §4.2，Definition 1（PDF p.5）：对某特征的已采样归因分数排序，只平均置信界秩k1与k2之间严格位于内部的次序统计量；分母为k2−k1−1。与全样本平均的差别是保留的分数集合，不是更换归因解释器
- §4.2，Theorem 4（PDF p.6）：此估计量的目标是采样解释分布的总体中位数；在该中位数处密度为正的条件下，方差以至少O(1/N)阶趋零。此处为估计量的一致性/渐近方差结论，不等于任意输入扰动下的稳定性保证
- §5.3.1（PDF p.8末至p.9）：正文明确区分上述理论与输入加噪稳定性，并用相同采样噪声公平比较MeTFA-smoothed Gradient和SmoothGrad。前者平均界内中央分数，后者平均所有采样分数
- §5.3.1，Table 3后的解释（PDF p.9）：作者以自动排除异常极端值解释中央子集在所测带噪输入条件中的稳定性收益；还以附录结果说明中央集合大小为O(√N)。这提供“为何选这个集合”的源文理由，不能扩张为每个被排除分数都语义错误，或比直接样本中位数及所有百分位平滑方法普遍更优
- 可支撑的内容职责：未知分布/极端分数问题→中位数目标及中央子集→实际采用的平均构造→相应理论与经验支撑。作为M.9的选择理由，须保留理论对象、实验证据和比较对象的边界；不能仅因已有置信区间工具便声称中央子集是必然或唯一的设计

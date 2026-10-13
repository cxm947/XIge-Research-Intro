# Privacy-preserving Triangle Counting in Directed Graphs：完整引言句级图

- 来源身份：sj-d1fc8dd7b9
- 指定版本：ICDE 2025 proceedings PDF, 13 physical pages, printed 2588-2600, DOI 10.1109/ICDE65448.2025.00195
- 指定原文：https://nesa.zju.edu.cn/download/Privacy-Preserving_Triangle_Counting_in_Directed_Graphs.pdf
- 实际读取原文：https://nesa.zju.edu.cn/download/Privacy-Preserving_Triangle_Counting_in_Directed_Graphs.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#triangle) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P3a](#p3a) · [P3b](#p3b) · [P4](#p4) · [P5](#p5) · [C1](#c1) · [C2](#c2) · [C3](#c3) · [C4](#c4)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

Source https://nesa.zju.edu.cn/download/Privacy-Preserving_Triangle_Counting_in_Directed_Graphs.pdf
ICDE2025,2588–2600,13pp; intro physical1–3. Full intro via primary web turn1138view0/turn1152view2; related-work comparison reread. No PDF cached locally (download502).
Chain P1 asymmetric graphs; P2 two triangle types/use and explicit privacy example; P3 edge-DP plus two trust scenarios; P4 centralized gap/design/derived sensitivity challenge; P5 local gap/design/derived estimator challenge; contributions. 推断：两种信任前提改变可观察信息，故两条方案并列，不可合成先中央再本地的流水线；贡献中的无偏性/方差说明研究所得，不只是“实现两个算法”。
<a id="p1"></a><a id="p1-s1"></a>P1.S1 定义：有向图→非对称关系 | 起题 | task
<a id="p1-s2"></a>P1.S2 例：单向关注→边存在不对称 | 举例 | local view
<a id="p1-s3"></a>P1.S3 范围：图→社会电商生物电路 | 扩展 | value
<a id="p2"></a><a id="p2-s1"></a>P2.S1 价值：三角形→最小凝聚单元/分析任务 | 缩域 | counting
<a id="p2-s2"></a>P2.S2 近邻：无向图→DP高效用计数 | 现状 | comparison
<a id="p2-s3"></a>P2.S3 新对象：有向→cycle/flow两型 | 对照 | joint output
<a id="p2-s4"></a>P2.S4 定义用途：两型计数→社区/聚类系数 | 任务价值 | E
<a id="p2-s5"></a>P2.S5 风险：精确计数→关系泄露 | 转折 | DP
<a id="p2-s6"></a>P2.S6 设例：社交图→11用户 | 实例 | next
<a id="p2-s7"></a>P2.S7 可见性：私密follow→仅自己out-neighbor | 假设 | local scenario
<a id="p2-s8"></a>P2.S8 邻接构造：G1/G2→差一边 | 设定 | DP adjacency
<a id="p2-s9"></a>P2.S9 攻击者知识：v2→已知其他关注 | 条件 | inference
<a id="p2-s10"></a>P2.S10 未知：v11→是否关注 | 问题 | inference
<a id="p2-s11"></a>P2.S11 对应：图差异→关系真假 | 澄清 | example
<a id="p2-s12"></a>P2.S12 因果：flow数不同→推断该关系 | 机制 | DP requirement
<a id="p2-s13"></a>P2.S13 需求：可推断→保护三角信息 | 归结 | task
<a id="p2-s14"></a>P2.S14 工作：需求→研究有向私有计数 | 回应 | C1
<a id="p3"></a><a id="p3-s1"></a>P3.S1 已有保证：边隐私→edgeDP | 方案类别 | definitions
<a id="p3-s2"></a>P3.S2 含义：单边→输出影响有限 | 定义 | guarantee
<a id="p3-s3"></a>P3.S3 范围：保证→两信任场景 | 组织 | branches
<a id="p3a"></a><a id="p3a-s1"></a>P3a.S1 条件：可信服务器→全图访问 | 定义 | centralized
<a id="p3a-s2"></a>P3a.S2 目的：计数→不可信研究方 | 用途 | output protection
<a id="p3a-s3"></a>P3a.S3 例：平台全关注→第三方凝聚性研究 | 举例 | scenario
<a id="p3a-s4"></a>P3a.S4 机制：edgeCDP→扰动输出保边 | 对应 | algorithm
<a id="p3a-s5"></a>P3a.S5 流程：收邻居列表→噪声结果 | 解释 | trusted raw data
<a id="p3a-s6"></a>P3a.S6 效果：第三方→难判特定边 | 归结 | privacy
<a id="p3b"></a><a id="p3b-s1"></a>P3b.S1 条件：不可信服务器→无全图 | 对照 | local
<a id="p3b-s2"></a>P3b.S2 目的：用户→计数信息收集 | 定义 | aggregation
<a id="p3b-s3"></a>P3b.S3 例：通信服务→不知本地联系人 | 举例 | scenario
<a id="p3b-s4"></a>P3b.S4 用途：电话网络→聚类系数 | 添加 | value
<a id="p3b-s5"></a>P3b.S5 机制：所需计数→用户本地混淆上传 | 因果 | LDP
<a id="p3b-s6"></a>P3b.S6 流程：混淆数据→聚合计数 | 次序 | estimator
<a id="p3b-s7"></a>P3b.S7 保证：edgeLDP→上传列表保护 | 解释 | privacy
<a id="p3b-s8"></a>P3b.S8 效果：服务器→难判特定边 | 归结 | privacy
<a id="p4"></a><a id="p4-s1"></a>P4.S1 近邻：edgeCDP→无向计数成熟 | 起分支 | baseline
<a id="p4-s2"></a>P4.S2 自然解：改无向方法→两型分别计 | 候选 | next
<a id="p4-s3"></a>P4.S3 条件：分别计→拆隐私预算 | 机制后果 | utility
<a id="p4-s4"></a>P4.S4 边界：分配难→可能浪费预算 | 问题 | simultaneous count
<a id="p4-s5"></a>P4.S5 方案：预算损耗→同时计两型 | 响应 | C2
<a id="p4-s6"></a>P4.S6 操作：原图→投影有向图 | 次序 | M
<a id="p4-s7"></a>P4.S7 操作：投影→两型数量 | 次序 | M
<a id="p4-s8"></a>P4.S8 操作：全局敏感度/总预算→Laplace噪声 | 次序 | guarantee
<a id="p4-s9"></a>P4.S9 价值：联合计数→无需拆预算 | 回收 | E
<a id="p4-s10"></a>P4.S10 新挑战：所选机制→全局敏感度分析 | 设计后障碍 | theory
<a id="p4-s11"></a>P4.S11 技巧：case-directed图→单边变动最大差 | 响应 | sensitivity proof
<a id="p5"></a><a id="p5-s1"></a>P5.S1 近邻：edgeLDP→无向算法 | 起分支 | baseline
<a id="p5-s2"></a>P5.S2 信息变化：无向全邻居→有向仅out-neighbor | 转折 | root cause
<a id="p5-s3"></a>P5.S3 现实例：平台设置→看followee不看follower | 支持 | scope
<a id="p5-s4"></a>P5.S4 后果：局部视野→旧法不适用 | 推论 | estimator
<a id="p5-s5"></a>P5.S5 原因：旧局部估计→缺所需信息 | 深化 | construction
<a id="p5-s6"></a>P5.S6 方案：缺口→新本地算法 | 响应 | C3
<a id="p5-s7"></a>P5.S7 组织：算法→三步 | 下启 | next
<a id="p5-s8"></a>P5.S8 产生：随机响应→噪声图 | 次序 | M
<a id="p5-s9"></a>P5.S9 本地：下载图→加Laplace计两型估计 | 次序 | M
<a id="p5-s10"></a>P5.S10 通讯：用户估计→上传服务器 | 次序 | M
<a id="p5-s11"></a>P5.S11 汇总：全部估计→聚合 | 次序 | output
<a id="p5-s12"></a>P5.S12 核心问题：本地信息→有用估计 | 技术聚焦 | unbiasedness
<a id="p5-s13"></a>P5.S13 技巧：局部子图计数→无偏估计 | 回答 | proof
<a id="p5-s14"></a>P5.S14 性质传递：局部无偏→全局无偏 | 因果 | C3
<a id="c1"></a><a id="c1-s1"></a>C1.S1 问题：有向三角计数→DP首次研究主张 | 归纳 | scope
<a id="c2"></a><a id="c2-s1"></a>C2.S1 算法：中央方案→DP保证 | 归纳 | theory
<a id="c2-s2"></a>C2.S2 证据：无偏性/方差→理论效用 | 新细化 | proof
<a id="c3"></a><a id="c3-s1"></a>C3.S1 算法：本地方案→LDP | 平行 | theory
<a id="c3-s2"></a>C3.S2 证据：无偏性/方差上界→理论效用 | 新细化 | proof
<a id="c4"></a><a id="c4-s1"></a>C4.S1 评价：六真实图→效率效用 | 新评价摘要 | E
R.S1 近邻：已有方法→§II | 导航 | §II
R.S2 前提：任务→§III预备知识 | 顺序 | §III
R.S3 中央方案：可信场景→§IV | 分支导航 | §IV
R.S4 本地方案：不可信场景→§V | 平行导航 | §V
R.S5 证据：两算法→§VI实验 | 顺序 | §VI
R.S6 收束：全文→§VII结论 | 顺序 | §VII
Ending: two mechanisms and privacy/root challenges already known; variance analysis and six-dataset evidence newly enter contributions. A repeated algorithm name is legitimate when sentence adds a guarantee. Local assumption is out-neighbors-only, not any conceivable directed-graph visibility model.

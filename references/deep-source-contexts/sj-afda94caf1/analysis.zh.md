# Graph Data Survey：分类之后必须交出跨分类的判断

## 来源与综述的真实任务
读取[实验室托管IEEE接受未终编稿](https://nesa.zju.edu.cn/download/Graph%20Data%20Anonymization%2C%20De-anonymization%20Attacks%2C%20and%20De-anonymizability%20Quantification%20A%20Survey.pdf)，DOI10.1109/COMST.2016.2633620，22物理页，散列7a945987d79b8d9b1930c32245cc7302bcafbc5d33c6caddb438f4c46f6713b9。完整引言pp.1–2；补读§III-D及表II、§IV-D表IV、§V量化条件、§VI方向、§VII旧综述比较。已渲染p.9辨表II图形符号，未以乱码字符猜判据。摘要有重复/排版问题，引言可完整读取。文献范围截至该稿时期，不称当前全景。

研究交付是三条研究线的综合：匿名化保留什么用途、结构攻击利用什么、理论在什么条件下保证可识别。已有综述覆盖关系数据或较窄匿名化家族；本篇范围扩充之外的价值，在把防御效用与攻击抵抗接起来，并按现实性/误差/一般性比较理论。因此没有新算法并非贡献缺口，比较轴与条件化结论就是产物。前文没有方法型双挑战，也没有独立结果段；贡献承担主要综合发现。

以下语法是可观察结构，源作者给出的分析用途可核对；阅读焦点与替代方案是编辑推断，不归因单个共同作者。

## 完整引言逐句
### P1，p.1：对象扩展服务综述边界
- P1.S1：多系统生成数据主语、have-graph-structure，例子跨多个领域；不能只以社交图代表全部对象
- P1.S2：Even轨迹主语、can-be-modeled、by技术转换；把非显式图来源纳入同一范围
- P1.S3：Generally-these-data-can-be-called统一术语；减少以后反复枚举
- P1.S4：for研究/商业目的前置、被动共享/公开，接接收者；保护需求由实际流转出现
- P1.S5：Therefore-it-critical隐私保护，during限定共享场景；不是一般隐私伦理长议论

### P2，p.1：六类地图之后给共同成功标准
- P2.S1：To-protect前置、方法被动提出，which分类六家族；类别是阅读地图，不是效果排名
- P2.S2：these-techniques-try-to扰动结构，to隐私/while保效用；共同判据使后面横向比较有意义
六类长列举可节省正文找路成本，但本句不能独自构成综述创新。新比较要问每类牺牲哪种效用，而非仅扩大类数。

### P3，p.1：反向研究线仍然追踪同一结构
- P3.S1：On-the-other-hand及following先例，攻击被动提出，which按种子有无分类；可用先验是两类边界
- P3.S2：main-idea系表，in-terms-of独特结构解释重识别；与P2保留结构的正面价值形成同一对象的张力

### P4，p.1：第三线是条件解释而非更多攻击名
- P4.S1：Furthermore量化问题主语、研究关注，where下三个嵌问为何/何条件/多少用户；把成功案例提升到可达性知识
该单句已能说明理论线的角色，不需补造一个“现有算法不够快”的挑战。问题形式随研究交付类型变化。

### P5，p.2左：综述动词必须由后续结果充实
- P5.S1：多个To目的并列前置，主句systematically summarize/classify/analyze三对象；理解进展、整体图景和未来研究给使用价值
- P5.S2：Specifically贡献引导，非独立发现
这一长目的前置适合读者需要先判断综述用途；若照搬到窄方法论文会拖延核心问题。引言没有直接比较旧综述，§VII才补足近邻，不能从省略推出不需近邻定位。

### P6，p.2贡献一：比较尺度与双层结论
- P6.S1：classify/analyze主干，with-respect-to22用途给分析设计，including例子横跨结构与应用；不是22个新实验
- P6.S2：evaluation-results-demonstrate内most/partially/conditionally保留范围和条件；给结构效用的正向认识
- P6.S3：However作者主句把应用效用损失概括到全部方案；句法作用是以应用层转折限定结构收益，但该全称与p.9 Table II的Naive行冲突，详见结果池
这里先说保得住什么，再说没保住什么。若只抄“匿名化毁掉效用”，就丢掉研究最有用的条件化判断。

### P7，p.2贡献二：最长因为跨两条目录作关系判断
- P7.S1：summarize/analyze攻击性质，e.g.扩展/实际可用/稳健；明确攻方比较轴
- P7.S2：results-show强而稳健是综合判断，需正文条件支撑
- P7.S3：Then-analytically-evaluate防御抵抗；从攻击目录回接匿名化，形成交叉比较
- P7.S4：existing-techniques主语、vulnerable对所列结构攻击；不是推翻不同隐私定义的形式保证
- P7.S5：actual-vulnerability-depends效用保留量；给决定因素，避免一概宣判失效
- P7.S6：Therefore-open-problem结论；未来任务由前面交叉分析推出，非愿景口号
P7六句足以容纳能力→交叉检验→条件→未决问题，不能为了贡献一句话惯例删成“综述攻击”。这里研究认识比方法数量重要。

### P8，p.2贡献三：理论按使用条件比较
- P8.S1：summarize/classify量化技术给组织动作；第一步非全部产物
- P8.S2：also-analyze按误差容忍/现实性/一般性；这些轴决定读者可将定理用于哪种图与辅助信息

### P9，p.2贡献四：方向和其障碍分别交代
- P9.S1：analyze-evolution/provide-directions并列；从证据回顾转研究议程
- P9.S2：also-discuss每方向挑战；不把建议等于已能实现的结果
完整集合是效用综合、攻防关系、理论适用性、未来议程。3/6/2/2句的比例来自信息职责，非四条等权创新的版式需求。

### P10，p.2：章节导航仍有功能，但不是贡献证据
- P10.S1：rest-is-organized被动引导；纯导航
- P10.S2：we-give-source/sharing概览，in-§II指定背景入口
- P10.S3：§III前置，summarize/classify/analyze匿名化及效用；对应P6
- P10.S4：§IV同样动词先攻击再抵抗；导航保留跨线关系，而非只一串标题
- P10.S5：survey/analyze量化，in-§V对应P8
- P10.S6：evolution/future被动discussed，in-§VI对应P9
- P10.S7：discuss-related/conclude两谓语标§VII–VIII；说明旧综述比较实际位置
导航七句较长，可按阅读场景压缩，但不宜在覆盖统计中当七个新学术结果。

## 综合结果池与正文支撑
表II分15结构用途及7应用用途，区分完全、部分、条件保留和不保留；这是定性比较矩阵，不能换算平均准确率或将勾数当质量分。P6选择双层结论而不报每类胜负，帮助读者先理解“保持图统计”不等于“保持任务”。正文强调参数与应用决定取舍；Table II的Naive去ID行同时保留全部15个结构指标和7个应用指标，其弱点是隐私抵抗性。因此，源引言的“所有方案损应用”概括过宽；将它缩窄为相关扰动方案，是编辑性修复，不是引言已明示的范围限定。可迁移的是结构／应用两层评价，不是原全称量词，也不能由此推出图隐私不可能性证明。

表IV的条件脆弱/抵抗亦不同；P7把效用和脆弱性连接，才让两个分类目录产生新判断。DP类所讨论多为边/关系隐私，结构重识别用户是另一目标，因此“可去匿名”不自动违反其形式DP定义。论文范围主要结构攻击，不能凭此断言所有语义、时间或现代隐私机制同样结论。

表V量化研究受ER/PA等图模型、种子规模、错误容忍限制；引言选择可用性维度而非定理条数，适合给研究者做选用判断。§VI进一步指出应用导向匿名化、动态数据、组合局部/全局结构及效用—可识别关系是未来方向。若只在引言报六类/22指标，会掩盖这些实际判断；若堆全部方向又会失去三线主骨架。

§VII对照旧综述，增量不只是更新年份：既包括更广匿名化家族，也纳入攻击、可达性及抵抗交叉分析。引言选择先交完整领域图景，近邻详细留后；这可用于成熟综述，但不保证审稿人会接受未在引言直接说明的差异。

## 保义表达替代
编辑选项，非源句或已验证增益：
1. “We compare not only what each anonymization method preserves, but what an attacker can infer from that preserved structure.” 将交叉关系前置，比三线目录更直接，弱化理论量化独立贡献
2. “Preserving graph statistics does not ensure that a downstream application retains its utility.” 压缩双层结果，需正文限定具体用途和方案
3. “A quantification result is useful only when its graph model, seed assumptions and error tolerance match the intended setting.” 把理论比较变成读者决策，语气比源更规范，宜作解释而非代替源结论
迁移的是从分类推进到条件化比较，再由比较推出议程。反例：仅想快速整理文献条目时不必伪造跨类规律；综合结论必须有对应分析而非靠标题数量。

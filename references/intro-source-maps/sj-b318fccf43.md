# Kernel Survey：完整引言句级图

- 来源身份：sj-b318fccf43
- 指定版本：arXiv:2501.16165v3 [cs.CR], 2025-12-04, 38 pages
- 指定原文：https://arxiv.org/pdf/2501.16165v3
- 实际读取原文：https://arxiv.org/pdf/2501.16165v3
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#kernel-survey) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [RQ1](#rq1) · [RQ2](#rq2) · [RQ3](#rq3) · [P5](#p5) · [C1](#c1) · [C2](#c2) · [C3](#c3) · [C4](#c4)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

- sourceID: sj-b318fccf43
- 版本：arXiv:2501.16165v3 [cs.CR], 2025-12-04, 38 pages
- 精确索引主源：https://arxiv.org/pdf/2501.16165v3
- 2026-10-04读取证据：本地完整 PDF（38 物理页）及 raw/layout 提取；SHA-256 76901e7b6f1c301779fea6d7bd6dc34ff8a99a46a572142a42ad64e1e1b393e1
- 引言定位：物理 PDF 第 2–3 页；页锚以原 URL 后加 #page=N 定位
- 状态：available=true；full_introduction_reread=true；sentence_annotated=true；awaiting=false；unavailable=false
- 归属：以下为本论文的内容组织选择，不据共著名单推断任何个人执笔；“选择解释”均为编辑推断，不是作者自述。句级内容为释义，非源句摘录。
- 读法：P 表示原文论证段/贡献项，S 按该段源句顺序。每句写“已知→新增｜前接关系｜后续回收”。篇章标题、脚注和图中文字不冒充正文句子。

## 连续论证与相邻正文核验
P1 kernel地位/风险/fuzzing价值；P2硬件耦合环境、结构输入、状态控制三组特殊障碍；P3研究繁多异质→综述需要与现综述边界；P4范围107篇及三RQ；P5跨研究指标不可直接比→功能导向视角，并以正文路线说明如何回答RQ；四贡献统合文献、分类体系、gap分析、方向。
补读§3 Paper Collection（2017–Aug2025、DBLP筛134→人工99→snowball107，含early/preprint）、§4 challenges及stage model。主要对象不只desktop Linux，还包括RTOS、TEE-OS、ROS等；三stage为环境准备/输入模型/fuzzing loop，九功能是分类结构，不是九新算法。PDF含模板J.ACM 2018页脚，来源身份仍以arXiv:2501.16165v3为准，不能据页脚宣称2018正式发表。

## 逐句信息推进
### P1 kernel风险与fuzzing价值（p2）
<a id="p1"></a><a id="p1-s1"></a>P1.S1 未定位→kernel连接软硬件、为系统核心｜重要性｜特殊环境
<a id="p1-s2"></a>P1.S2 已知核心→漏洞可提权/泄敏/远程执行｜后果｜security value
<a id="p1-s3"></a>P1.S3 已知后果→Dirty Cow案例｜具体佐证｜不作为所有kernel统计
<a id="p1-s4"></a>P1.S4 已知风险→移动环境规模复杂使风险增加｜现实迫切性｜多环境
<a id="p1-s5"></a>P1.S5 已知安全需求→fuzzing有效实用发现漏洞｜已有路线｜kernel fuzzing
<a id="p1-s6"></a>P1.S6 已知可用路线→研究界广泛关注｜语境｜综述量增
### P2 特殊挑战（p2）
<a id="p2"></a><a id="p2-s1"></a>P2.S1 已知fuzzing→kernel较user-space有更复杂挑战｜比较轴｜S2–9
<a id="p2-s2"></a>P2.S2 已知user-space→kernel需多硬件/驱动交互｜环境根因｜environment stage
<a id="p2-s3"></a>P2.S3 已知耦合→kernel错可全系统崩/不稳｜后果｜可靠测试环境
<a id="p2-s4"></a>P2.S4 已知后果→一致可靠测试环境难搭｜要求｜§5
<a id="p2-s5"></a>P2.S5 已知环境问题→kernel测试输入也更难合成｜转第二根因｜input stage
<a id="p2-s6"></a>P2.S6 已知输入→syscall/外设等结构复杂、规范藏代码｜解释困难｜§6
<a id="p2-s7"></a>P2.S7 已知输入→低层复杂性另引障碍｜转第三组｜fuzzing loop
<a id="p2-s8"></a>P2.S8 已知低层→动作控制/内态监控/响应解释难｜具体任务｜§7
<a id="p2-s9"></a>P2.S9 已知操作难→规模增长使可扩展/轻量约束加剧｜横贯条件｜trade-off分析
### P3 为什么需要这个综述（p2）
<a id="p3"></a><a id="p3-s1"></a>P3.S1 已知难题→促成大量kernel fuzzing研究｜研究版图｜S2
<a id="p3-s2"></a>P3.S2 已知积累→各pipeline阶段目标/方法差异大｜组织障碍｜stage taxonomy
<a id="p3-s3"></a>P3.S3 已知异质→需找共性与针对的挑战｜综述任务｜RQ1/2
<a id="p3-s4"></a>P3.S4 已知整理需求→还需性能权衡及未开发机会｜价值增量｜RQ3
<a id="p3-s5"></a>P3.S5 已知需要→源文主张尚无系统kernel综述｜新颖性定位需外部核查｜贡献1
<a id="p3-s6"></a>P3.S6 已知近邻→现综述多为通用fuzz/评价标准｜承认边界｜专门范围
<a id="p3-s7"></a>P3.S7 已知相关→嵌入式fuzz是相关但不同路线｜防范围混同｜§3纳排
### P4 研究范围和RQ（p2）
<a id="p4"></a><a id="p4-s1"></a>P4.S1 已知目标→107篇2017–Aug2025顶级venues研究综述｜范围及方法入口｜§3
<a id="rq1"></a>RQ1 已知kernel特殊→哪些必要功能区别于general fuzzing｜分类目标｜§4
<a id="rq2"></a>RQ2 已知功能→用哪些技术满足｜已有答案系统化｜§5–7
<a id="rq3"></a>RQ3 已知版图→尚存挑战/机会｜未来价值｜§8
### P5 评价观与结构导航（p2–3）
<a id="p5"></a><a id="p5-s1"></a>P5.S1 已知fuzzer指标→coverage/crash能反映效果但定义/设置/目标不同难横比｜比较合法性边界｜定性视角
<a id="p5-s2"></a>P5.S2 已知不可硬比→关注实现功能、适用性、方法增量｜选择替代比较轴｜taxonomy
<a id="p5-s3"></a>P5.S3 已知功能轴→给更实用impact/utility理解｜解释选择价值｜综述结论
<a id="p5-s4"></a>P5.S4 已知视角→§2背景、§3方法与结果｜导航并交代证据基础｜survey protocol
<a id="p5-s5"></a>P5.S5 已知背景→§4独有挑战｜RQ1前提｜taxonomy
<a id="p5-s6"></a>P5.S6 已知挑战→stage-based模型拆过程为步骤｜组织机制｜三stage
<a id="p5-s7"></a>P5.S7 已知阶段→逐阶段描述功能技术答RQ1｜问题—章节映射｜§4
<a id="p5-s8"></a>P5.S8 已知模型→§5环境、§6输入、§7loop讨论提案｜三stage落章节｜RQ2
<a id="p5-s9"></a>P5.S9 已知技术→定性标准提炼启示/可行方案答RQ2｜综述分析动作｜comparative synthesis
<a id="p5-s10"></a>P5.S10 已知已解→§8挑战方向、部分来自case study｜证据和未来范围｜RQ3
<a id="p5-s11"></a>P5.S11 已知§8→明确回答RQ3｜映射收束｜方向
<a id="p5-s12"></a>P5.S12 已知主线→§9结论｜导航收尾｜全文
### 贡献（p3）
引导句 已知框架→四贡献｜归纳｜C1–4
<a id="c1"></a><a id="c1-s1"></a>C1.S1 已知范围→107篇kernel fuzzing首个系统知识梳理主张｜综合产物｜§3
<a id="c2"></a><a id="c2-s1"></a>C2.S1 已知kernel特性→三stage九功能taxonomy｜可重用组织结构｜§4
<a id="c3"></a><a id="c3-s1"></a>C3.S1 已知分类→系统化进展并比期望功能与实践gap｜分析所得｜§5–7
<a id="c4"></a><a id="c4-s1"></a>C4.S1 已知gap→挑战及有前景方向｜研究决策价值｜§8

## 选择解释（推断）
- P2不是为本文算法造障碍，而是为“为什么通用fuzz综述不足”提供证据；挑战的后续回收在分类轴和文献组织。
- 特别重要的选择句是P5S1–3：拒绝不等价的coverage/crash横比，把比较转到功能/适用性/方法。价值是能让读者判断技术何时可用，而不造无根据排行榜。
- roadmap同时承担研究设计：每RQ由哪些步骤回答，帮助读者把107篇数量和实际综合方法联系；不能将它全当可随便删除的导航套话。

## 贡献篇幅条件
四项各1句；此前没有实验结果段，但有107篇范围、三RQ以及12句比较哲学/组织路线。综述“结果”体现taxonomy和缺口综合，不必仿系统论文给性能数字。九功能首次在C2精确给数，允许贡献承担结构规模的新增细化。

## 可点击主源页锚
[PDF p2](https://arxiv.org/pdf/2501.16165v3#page=2) · [PDF p3](https://arxiv.org/pdf/2501.16165v3#page=3)

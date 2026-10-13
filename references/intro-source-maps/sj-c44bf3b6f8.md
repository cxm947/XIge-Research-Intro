# AdversaFlow：完整引言句级图

- 来源身份：sj-c44bf3b6f8
- 指定版本：Final IEEE TVCG 31(1), January 2025, pp.492-502
- 指定原文：https://nesa.zju.edu.cn/download/dazhen_adversaflow.pdf
- 实际读取原文：https://nesa.zju.edu.cn/download/dazhen_adversaflow.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#adversaflow) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [C1](#c1) · [C2](#c2) · [C3](#c3)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

- sourceID: sj-c44bf3b6f8
- 版本：Final IEEE TVCG 31(1), January 2025, pp.492-502
- 精确索引主源：https://nesa.zju.edu.cn/download/dazhen_adversaflow.pdf
- 2026-10-04读取证据：本地完整 PDF（11 物理页）及 raw/layout 提取；SHA-256 641c08fcd991268dc686fc44b3625869a5b045f05b0e5ad672338da780cc520a
- 引言定位：物理 PDF 第 1–2（印刷492–493） 页；页锚以原 URL 后加 #page=N 定位
- 状态：available=true；full_introduction_reread=true；sentence_annotated=true；awaiting=false；unavailable=false
- 归属：以下为本论文的内容组织选择，不据共著名单推断任何个人执笔；“选择解释”均为编辑推断，不是作者自述。句级内容为释义，非源句摘录。
- 读法：P 表示原文论证段/贡献项，S 按该段源句顺序。每句写“已知→新增｜前接关系｜后续回收”。篇章标题、脚注和图中文字不冒充正文句子。

## 连续论证与相邻正文核验
P1 LLM用途、滥用、已有alignment与残余风险；P2 人工red teaming→自动red models及反馈难题；P3 双模型优化可能退化→需要多视角可视分析；P4 训练模式概览—细节挑战；P5 checkpoint/序列概率波动不能被单ASR解释；P6 三模型人机框架、multi-level flow和概率/Sankey视图；三短贡献以案例证据收尾。
补读§4 Requirement Analysis（两名安全专家参与，R1–R6）和System Overview，以及§7视图设计、§8案例/量化评价和§9讨论。R4要求按风险类别下钻避免聚合ASR偏置；R5要求不与训练重叠的验证数据；R6波动分析定位不稳定回答。此为visual analytics系统及人机研究，不等价“发明更强通用jailbreak算法”。

## 逐句信息推进
### P1 安全任务（p1）
<a id="p1"></a><a id="p1-s1"></a>P1.S1 未定位→ChatGPT/Llama等多领域NLP能力｜背景｜应用影响
<a id="p1-s2"></a>P1.S2 已知能力→伦理和安全问题｜转折｜S3
<a id="p1-s3"></a>P1.S3 已知风险→假新闻与非法活动帮助的例｜具体后果｜red teaming
<a id="p1-s4"></a>P1.S4 已知后果→供应商建可信LLM的责任｜价值主张｜安全任务
<a id="p1-s5"></a>P1.S5 已知任务→RLHF和safeguard prompts已用于alignment｜已有答案｜S6
<a id="p1-s6"></a>P1.S6 已知改善→仍有绕过行为｜残余｜P2
### P2 从人工到自动red teaming（p1）
<a id="p2"></a><a id="p2-s1"></a>P2.S1 已知风险→用对抗例发现/修复模型漏洞的red teaming定义｜任务｜系统
<a id="p2-s2"></a>P2.S2 已知任务→开发者人工建数据依赖经验｜旧实现｜S4
<a id="p2-s3"></a>P2.S3 已知人工→用户平台提交诱导prompt帮助开发者修模型｜实例解释工作流｜expert involvement
<a id="p2-s4"></a>P2.S4 已知经验劳动→限制扩展性｜问题后果｜S5
<a id="p2-s5"></a>P2.S5 已知限制→研究自动生成对抗例｜自然下一路线｜S6
<a id="p2-s6"></a>P2.S6 已知自动→Perez的red LLM生成toxic prompts挑战target｜较近能力｜framework
<a id="p2-s7"></a>P2.S7 已知模型生成→对抗训练避免target只熟悉固定输入｜解释动态反馈价值｜过程分析
<a id="p2-s8"></a>P2.S8 已知动态能力→成功依赖反馈保证新颖多样高质prompt｜必要条件｜human steering
<a id="p2-s9"></a>P2.S9 已知条件→环境管理与准确反馈仍难｜未解任务｜P3
### P3 为什么需要可视分析（p1）
<a id="p3"></a><a id="p3-s1"></a>P3.S1 已知双模型训练→理解和调试复杂｜补人类任务｜可视化
<a id="p3-s2"></a>P3.S2 已知训练→目标是同时改善两个模型｜成功判据｜S3
<a id="p3-s3"></a>P3.S3 已知目标→实际可能性能下降｜反预期｜S4–5
<a id="p3-s4"></a>P3.S4 已知退化→red model可取高reward简单策略｜一侧失效｜多样性/模式视图
<a id="p3-s5"></a>P3.S5 已知另一侧→target优化全部毒性prompt可能伤一般能力｜另一侧权衡｜R3/R5
<a id="p3-s6"></a>P3.S6 已知两失效→需多角度监测评估｜推需求｜S7
<a id="p3-s7"></a>P3.S7 已知监测需求→visual analytics已有可导航/可解释能力｜承认工具路线｜P4–5
<a id="p3-s8"></a>P3.S8 已知可视路线→非结构化文本red teaming有两挑战｜限定任务｜下两段
### P4 对抗模式展示（p1）
<a id="p4"></a><a id="p4-s1"></a>P4.S1 已知训练→prompt产生和target反应中细微变化｜具体分析对象｜multi-level flow
<a id="p4-s2"></a>P4.S2 已知可视近邻→RL/对抗model主要loss/diversity或embedding等高层信息｜能力/边界｜S3
<a id="p4-s3"></a>P4.S3 已知近邻→red teaming需跨训练行为｜改变判断轴｜S4
<a id="p4-s4"></a>P4.S4 已知跨时序→每轮几百输出、几十轮｜规模根因｜overview+detail
<a id="p4-s5"></a>P4.S5 已知大规模→需总体趋势且定位具体失败prompt｜要求而非抽象“可解释”｜P6 flow
### P5 波动分析（p1）
<a id="p5"></a><a id="p5-s1"></a>P5.S1 已知评价→单ASR等指标未必反映鲁棒性｜判据限制｜probability metric
<a id="p5-s2"></a>P5.S2 已知限制→同prompt不同checkpoint安全性不同、干预可致成功｜现象具体化｜fluctuation view
<a id="p5-s3"></a>P5.S3 已知NLP可视→常看token分布理解输出｜承认最近路线｜S4
<a id="p5-s4"></a>P5.S4 已知分布→序列上下文使前几词波动影响后续｜根因｜token transitions
<a id="p5-s5"></a>P5.S5 已知依赖→现方法未处理安全场景这些波动｜gap｜S6
<a id="p5-s6"></a>P5.S6 已知gap→需可视不确定性与概率转移｜操作要求｜Sankey
### P6 响应与机制（p1）
<a id="p6"></a><a id="p6-s1"></a>P6.S1 已知两挑战→提出AdversaFlow｜工作命名｜§4
<a id="p6-s2"></a>P6.S2 已知系统→target/red/reward+专家界面，人可按分析调整red｜人机闭环｜§4.2
<a id="p6-s3"></a>P6.S3 已知展示难→multi-level adversarial flow｜对应P4｜§7
<a id="p6-s4"></a>P6.S4 已知flow→全训练概览到单轮细节｜兑现粒度｜R3/R4
<a id="p6-s5"></a>P6.S5 已知波动难→基于分布的token转移似然指标｜对应P5｜§7
<a id="p6-s6"></a>P6.S6 已知指标→判断被诱导及不当回复的易感性｜把数值变任务用途｜案例
<a id="p6-s7"></a>P6.S7 已知转移→增强Sankey显示safe→unsafe及不确定性｜机制可视化闭合｜fluctuation view
<a id="p6-s8"></a>P6.S8 已知工作→贡献引导｜收束｜三项
### 贡献（跨p1–2）
<a id="c1"></a>C1 人机专家、LLM、有效指标的red-team框架｜产物级归纳｜前接P6S2；回§4
<a id="c2"></a>C2 展示模式和波动分析的AdversaFlow系统｜任务能力归纳｜前接两挑战；回§7
<a id="c3"></a>C3 case studies展示有用性并给AI安全系统设计经验｜证据类型与可复用知识｜回案例/讨论

## 选择解释（推断）
- 引言不是从“我们要画Sankey”起步，先说明训练反馈为何难以及聚合指标怎样误导专家，才让可视设计成为回答真实判断需求的手段。
- P4尺度问题与P5序列依赖不同：一个是概览到失败实例的组织，一个是概率不稳定与安全风险的解释；不能因都叫可视分析就合并成“结果难理解”。
- 双模型共同改进又可能互相牺牲，使正常任务表现进入监控需求；这保障“安全提升”不会被单toxic score偷换。

## 贡献篇幅条件
三项均一个名词短语条目（非完整陈述句），无前置独立结果段、无引言量化性能。第三项说明case studies的证据类别，方法段已详细映射两挑战，因此列表保持短。这种长度适合design-study收束，不宜抽象为任何方法论文都应只列名词。

补充核验：§8两案例由未参与设计的两名专家执行，§9明确长上下文高级jailbreak分析仍不支持；故系统有用性不等于覆盖所有攻击。

## 可点击主源页锚
[PDF p1](https://nesa.zju.edu.cn/download/dazhen_adversaflow.pdf#page=1) · [PDF p2](https://nesa.zju.edu.cn/download/dazhen_adversaflow.pdf#page=2)

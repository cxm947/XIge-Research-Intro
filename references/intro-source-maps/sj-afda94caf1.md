# Graph Data Survey：完整引言句级图

- 来源身份：sj-afda94caf1
- 指定版本：IEEE accepted-not-fully-edited manuscript, 22 physical pages, DOI 10.1109/COMST.2016.2633620
- 指定原文：https://nesa.zju.edu.cn/download/Graph%20Data%20Anonymization%2C%20De-anonymization%20Attacks%2C%20and%20De-anonymizability%20Quantification%20A%20Survey.pdf
- 实际读取原文：https://nesa.zju.edu.cn/download/Graph%20Data%20Anonymization%2C%20De-anonymization%20Attacks%2C%20and%20De-anonymizability%20Quantification%20A%20Survey.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#graph-survey) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [P8](#p8) · [P9](#p9) · [P10](#p10)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

Source ID: sj-afda94caf1
Version: IEEE accepted-not-fully-edited manuscript, 22 physical pages, DOI 10.1109/COMST.2016.2633620
Primary URL: https://nesa.zju.edu.cn/download/Graph%20Data%20Anonymization%2C%20De-anonymization%20Attacks%2C%20and%20De-anonymizability%20Quantification%20A%20Survey.pdf
Local primary SHA-256: 7a945987d79b8d9b1930c32245cc7302bcafbc5d33c6caddb438f4c46f6713b9

Scope: Complete Introduction reread in the 2026-10-04 reading record; nearby passages listed below checked for the stated callbacks. P/S numbers refer to the paper’s argument paragraphs and constituent sentences, with source continuations joined. Sentence contents are original Chinese paraphrases, not quotations. Already-known records the most relevant incoming information, not the reader’s entire knowledge. Selection rationales are editorial inferences, not evidence of individual coauthor intent.

## Paragraph and sentence map

### P1 · PDF p.1 §I · 数据类型与共享价值
论证出口：共享图数据使隐私保护必要
联合选择分析（推断）：先从天然图到可转为图的轨迹扩张范围，再统一命名；这支撑综述横跨应用，而非只讨论社交图。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p1"></a><a id="p1-s1"></a>P1.S1|对象范围|尚未引入本论文的特定问题|社交、协作、邮件、自治系统和P2P数据具有图结构|建立研究对象|§II来源|
|<a id="p1-s2"></a>P1.S2|边界扩展|社交、协作、邮件、自治系统和P2P数据具有图结构|移动、蓝牙、即时消息及签到轨迹也可转图|纳入非显式图数据|源数据分类|
|<a id="p1-s3"></a>P1.S3|统一术语|移动、蓝牙、即时消息及签到轨迹也可转图|统称这些对象为图数据|压缩后续指称|全篇|
|<a id="p1-s4"></a>P1.S4|使用价值|统称这些对象为图数据|研究、挖掘与商业使图数据被转移共享公开|说明需求|§II-B|
|<a id="p1-s5"></a>P1.S5|保护需要|研究、挖掘与商业使图数据被转移共享公开|共享传播时保护用户隐私很关键|把效用连到任务|匿名化|

### P2 · PDF p.1 · 匿名化已有答案
论证出口：隐私—效用共同构成分析轴
联合选择分析（推断）：六类先作地图而非比较结论；下一句说明它们共同优化什么。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p2"></a><a id="p2-s1"></a>P2.S1|领域分类|共享传播时保护用户隐私很关键|已有匿名化分ID移除、边编辑、k匿名、聚合、差分隐私及随机游走|组织第一个研究家族|§III|
|<a id="p2-s2"></a>P2.S2|共同目标|已有匿名化分ID移除、边编辑、k匿名、聚合、差分隐私及随机游走|扰动图结构以保护隐私并尽量保持效用|给分类的比较判据|22效用维度|

### P3 · PDF p.1 · 攻击的反向视角
论证出口：保留结构也可能保留可识别信号
联合选择分析（推断）：不是另起无关领域，攻击研究直接检验匿名化保证；有种子/无种子按可用先验区分。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p3"></a><a id="p3-s1"></a>P3.S1|攻击分类|扰动图结构以保护隐私并尽量保持效用|结构去匿名攻击分有种子与无种子|组织第二个研究家族|§IV|
|<a id="p3-s2"></a>P3.S2|识别机制|结构去匿名攻击分有种子与无种子|利用独特结构特征恢复匿名用户|说明分类共享的风险来源|抵抗性分析|

### P4 · PDF p.1 · 可去匿名性理论
论证出口：不仅问能否攻击，还问条件及规模
联合选择分析（推断）：第三轴是可解释条件和可识别数量，不是又一个检测算法列表。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p4"></a><a id="p4-s1"></a>P4.S1|知识问题|利用独特结构特征恢复匿名用户|量化研究问为何可去匿名、何条件下成立、多少用户可识别|补足解释性维度|§V|

### P5 · PDF p.2 Contributions lead · 综述任务声明
论证出口：整合三条研究线支持理解与未来研究
联合选择分析（推断）：引言未专段逐个比较旧综述，其比较留在§VII；不能据此声称无需近邻核验，或照搬方法型双挑战。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p5"></a><a id="p5-s1"></a>P5.S1|综述产物|量化研究问为何可去匿名、何条件下成立、多少用户可识别|系统汇总分类分析匿名化、攻击和量化以给完整研究图景|把分类变为综合任务|§III–VI|
|<a id="p5-s2"></a>P5.S2|结构引导|系统汇总分类分析匿名化、攻击和量化以给完整研究图景|具体贡献如下|切换归纳|四项|

### P6 · PDF p.2 bullet1 · 效用综合所得
论证出口：图结构效用与应用效用须区分
联合选择分析（推断）：三句依次方法、条件化正结果、应用层负结果；转折定义真正的trade-off，而非把所有匿名化判为无用。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p6"></a><a id="p6-s1"></a>P6.S1|分析设计|具体贡献如下|按22种图及应用效用系统分析匿名化方法|明确比较尺度|§III-D|
|<a id="p6-s2"></a>P6.S2|结构结果|按22种图及应用效用系统分析匿名化方法|多数方法部分或有条件保留多数图效用|给带条件的正结果|效用表|
|<a id="p6-s3"></a>P6.S3|应用边界|多数方法部分或有条件保留多数图效用|全部所列方案损失至少一种应用效用|用另一层尺度限定|应用讨论|

### P7 · PDF p.2 bullet2 · 攻击与防御关系综合
论证出口：保留多少何种效用影响可识别风险
联合选择分析（推断）：这一贡献最长，因为它不只归纳攻击，还接回匿名化并推出未来任务。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p7"></a><a id="p7-s1"></a>P7.S1|攻击比较|全部所列方案损失至少一种应用效用|分析结构攻击的扩展性、可行性和稳健性|建立攻击评价轴|§IV|
|<a id="p7-s2"></a>P7.S2|攻击认识|分析结构攻击的扩展性、可行性和稳健性|现有结构攻击强而稳健|归纳已分析能力|攻击比较|
|<a id="p7-s3"></a>P7.S3|交叉分析|现有结构攻击强而稳健|分析匿名化对结构攻击的抵抗|从两份目录转为关系判断|防御矩阵|
|<a id="p7-s4"></a>P7.S4|防御边界|分析匿名化对结构攻击的抵抗|所分析k匿名/DP类匿名化仍可能受结构攻击|呈现论文范围内结论|隐私目标/假设辨析|
|<a id="p7-s5"></a>P7.S5|决定因素|所分析k匿名/DP类匿名化仍可能受结构攻击|实际脆弱性取决于保留的效用程度|补条件而非全称失败|隐私效用权衡|
|<a id="p7-s6"></a>P7.S6|未决任务|实际脆弱性取决于保留的效用程度|有效图匿名化仍是重要开放问题|由综合结果导出研究需要|§VI|

### P8 · PDF p.2 bullet3 · 量化综合所得
论证出口：理论结果须按条件而非定理数量比较
联合选择分析（推断）：分类只是入口；误差容忍、现实性、一般性才决定读者怎么用理论。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p8"></a><a id="p8-s1"></a>P8.S1|分类产物|有效图匿名化仍是重要开放问题|汇总并分类可去匿名性量化技术|组织第三线|§V|
|<a id="p8-s2"></a>P8.S2|分析判据|汇总并分类可去匿名性量化技术|比较误差容忍、现实性与一般性|解释使用价值|量化假设分析|

### P9 · PDF p.2 bullet4 · 演进与研究方向
论证出口：综合应推出有根据的未来问题
联合选择分析（推断）：两句将方向及其障碍分开，避免无根据愿景列表。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p9"></a><a id="p9-s1"></a>P9.S1|方向产物|比较误差容忍、现实性与一般性|分析三领域技术演进并给未来方向|由综述转议程|§VI|
|<a id="p9-s2"></a>P9.S2|可行性辨析|分析三领域技术演进并给未来方向|讨论各方向潜在挑战|补方向的约束|§VI|

### P10 · PDF p.2 last · 章节导航
论证出口：阅读路径覆盖三线及交叉关系
联合选择分析（推断）：这是文档导航职责而非科学贡献；可压缩但不可把导航当实证。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p10"></a><a id="p10-s1"></a>P10.S1|导航引导|讨论各方向潜在挑战|余文结构如下|转读者路径|后续章节|
|<a id="p10-s2"></a>P10.S2|对象导航|余文结构如下|第二节介绍图来源及共享可用性|给背景入口|§II|
|<a id="p10-s3"></a>P10.S3|匿名化导航|第二节介绍图来源及共享可用性|第三节分类并分析匿名化和效用|指向第一线|§III|
|<a id="p10-s4"></a>P10.S4|攻击导航|第三节分类并分析匿名化和效用|第四节分类攻击并分析匿名化抵抗|指向交叉分析|§IV|
|<a id="p10-s5"></a>P10.S5|理论导航|第四节分类攻击并分析匿名化抵抗|第五节分析量化技术|指向第三线|§V|
|<a id="p10-s6"></a>P10.S6|方向导航|第五节分析量化技术|第六节讨论演进及未来|指向综合结论|§VI|
|<a id="p10-s7"></a>P10.S7|结尾导航|第六节讨论演进及未来|第七节相关综述、第八节总结|定位近邻比较与收尾|§VII/VIII|

## Nearby method/evaluation checks

Checked §III privacy-model discussion distinguishes formal DP guarantees from anonymization/application utility. Checked §V (PDF pp.14–15) explicitly critiques ER/PA assumptions, dense seeds, and structural information scope; these are applicability judgments rather than new impossibility proofs. Checked §VII (PDF p.18) compares prior surveys: relational versus graph data, six anonymization families versus narrower earlier classifications, inclusion of attacks and quantification. This supplies the survey’s novelty placement absent from the Introduction itself.

## Length, transfer, and boundaries

无独立结果预告；贡献本身承担综合发现，尤其第二项六句承载攻击能力→交叉抵抗→条件→开放问题。综述不是系统模板缺了实验，而是比较轴和条件化认识构成主要产物。保留本2016接受未终编版本及当时文献范围，不能当作当前领域全景；原PDF摘要存在重复乱码，但Introduction可完整读取。

## Verified physical-page lookup

Exact section-title/phrase lookup in the cached primary PDF; repeated mentions may include the Introduction itself.
- V. GRAPH DATA DE-ANONYMIZABILITY: [14](https://nesa.zju.edu.cn/download/Graph%20Data%20Anonymization%2C%20De-anonymization%20Attacks%2C%20and%20De-anonymizability%20Quantification%20A%20Survey.pdf#page=14)
- VII. RELATED WORK: [18](https://nesa.zju.edu.cn/download/Graph%20Data%20Anonymization%2C%20De-anonymization%20Attacks%2C%20and%20De-anonymizability%20Quantification%20A%20Survey.pdf#page=18)

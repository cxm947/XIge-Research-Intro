# Beyond the Payload：完整引言句级图

- 来源身份：sj-c1e338ca9f
- 指定版本：arXiv:2608.30686v1 [cs.CR], 2026-08-31
- 指定原文：https://arxiv.org/pdf/2608.30686v1
- 实际读取原文：https://arxiv.org/pdf/2608.30686v1
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#beyond) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [P8](#p8) · [P9](#p9)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

Source ID: sj-c1e338ca9f
Version: arXiv:2608.30686v1 [cs.CR], 2026-08-31
Primary URL: https://arxiv.org/pdf/2608.30686v1
Local primary SHA-256: 5d794a2dd521d86d99de2361e472ec15b38cfc5e34edf2a8ab9ad2ceac498caf

Scope: Complete Introduction reread in the 2026-10-04 reading record; nearby passages listed below checked for the stated callbacks. P/S numbers refer to the paper’s argument paragraphs and constituent sentences, with source continuations joined. Sentence contents are original Chinese paraphrases, not quotations. Already-known records the most relevant incoming information, not the reader’s entire knowledge. Selection rationales are editorial inferences, not evidence of individual coauthor intent.

## Paragraph and sentence map

### P1 · PDF p.1 §1 · 代理使用与仓库完整性
论证出口：正常引导项目也可能接触被污染仓库
联合选择分析（推断）：攻击入口来自合理用户任务，先建立这一点再讨论payload选择。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p1"></a><a id="p1-s1"></a>P1.S1|使用背景|尚未引入本论文的特定问题|vibe coding使开发者少干预地委托软件任务|立题|用户配置|
|<a id="p1-s2"></a>P1.S2|风险条件|vibe coding使开发者少干预地委托软件任务|引导第三方项目而其完整性不确定时依赖代理有风险|限定问题场景|poisoned repos|
|<a id="p1-s3"></a>P1.S3|现实路径|引导第三方项目而其完整性不确定时依赖代理有风险|恶意仓库可刷星流行，可信仓库可被维护者账号入侵污染|说明不可信内容可能到达用户|威胁模型|
|<a id="p1-s4"></a>P1.S4|研究进展|恶意仓库可刷星流行，可信仓库可被维护者账号入侵污染|相关安全问题开始受到注意|接入文献|最近研究|

### P2 · PDF p.1 · 最近研究与研究视角
论证出口：静态payload的成功也取决于善意用户如何调用
联合选择分析（推断）：承认技能、规则和README三类表面已被研究，把增量放在独立用户控制轴而非再发现注入。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p2"></a><a id="p2-s1"></a>P2.S1|已有研究|相关安全问题开始受到注意|研究已开始刻画编码代理仓库投毒|给领域答案|相关工作|
|<a id="p2-s2"></a>P2.S2|研究范围|研究已开始刻画编码代理仓库投毒|已有研究覆盖skills、rules与README注入面|具体化既有覆盖|攻击条件|
|<a id="p2-s3"></a>P2.S3|共同焦点|已有研究覆盖skills、rules与README注入面|多关注攻击者如何注入和伪装|找共同比较轴|固定攻击因素|
|<a id="p2-s4"></a>P2.S4|剩余问题|多关注攻击者如何注入和伪装|用户prompt级交互研究不足|换到未充分覆盖轴|PLC|
|<a id="p2-s5"></a>P2.S5|视角意义|用户prompt级交互研究不足|从攻击者造payload转到善意调用怎样决定静态payload成败|解释增量的判断价值|controlled benchmark|

### P3 · PDF pp.1–2 · 定义PLC及后果
论证出口：评估不能只用一个标准prompt
联合选择分析（推断）：名词定义出现在日常选择之后；这样读者先识别真实动作，再接受研究变量。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p3"></a><a id="p3-s1"></a>P3.S1|用户动作|从攻击者造payload转到善意调用怎样决定静态payload成败|用户选择任务、表达方式、skills/rules|列可控变量|三轴|
|<a id="p3-s2"></a>P3.S2|决策价值|用户选择任务、表达方式、skills/rules|若日常调用会降防御，实践者需要知道应避开的配置|说明为何值得测量|实践含义|
|<a id="p3-s3"></a>P3.S3|术语|若日常调用会降防御，实践者需要知道应避开的配置|将这些选择命名为PLC|压缩共同对象|全篇|
|<a id="p3-s4"></a>P3.S4|范围定义|将这些选择命名为PLC|本文PLC含任务类型、表达、附加技能规则文本|限定范围|benchmark grid|
|<a id="p3-s5"></a>P3.S5|机制动机|本文PLC含任务类型、表达、附加技能规则文本|代理执行上下文影响其问题理解|解释研究合理性|case studies|
|<a id="p3-s6"></a>P3.S6|层级区分|代理执行上下文影响其问题理解|PLC改变环境探索与执行，超出单轮生成的表面敏感性|说明不同研究对象|trajectory分析|
|<a id="p3-s7"></a>P3.S7|评价后果|PLC改变环境探索与执行，超出单轮生成的表面敏感性|标准prompt强而用户变体弱时，现有评估可能不完整|把机制转评估价值|基准目标|

### P4 · PDF p.2 challenges · 基准构造的三个证据要求
论证出口：真实任务、真实表达和两类安全结果须可测
联合选择分析（推断）：挑战是研究设计有效性，不是算法准确率；ASR与AR定义属于输出可辨别性。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p4"></a><a id="p4-s1"></a>P4.S1|组织引导|标准prompt强而用户变体弱时，现有评估可能不完整|该调查有三项具体挑战|规划设计|三回应|
|<a id="p4-s2"></a>P4.S2|场景挑战|该调查有三项具体挑战|构造真实仓库场景|命名第一职责|repo pipeline|
|<a id="p4-s3"></a>P4.S3|代表性要求|构造真实仓库场景|仓库须可运行可测且跨语言与任务|给质量判据|筛选|
|<a id="p4-s4"></a>P4.S4|资源边界|仓库须可运行可测且跨语言与任务|现有基准多用精选实例而非同时满足条件的仓库|比较最近资源|新资源必要性|
|<a id="p4-s5"></a>P4.S5|表达挑战|现有基准多用精选实例而非同时满足条件的仓库|prompt风格须有真实使用依据|命名第二职责|usage collection|
|<a id="p4-s6"></a>P4.S6|有效性要求|prompt风格须有真实使用依据|表达应来自开发者实际调用而非研究者任意设定|解释构念效度|社媒样本|
|<a id="p4-s7"></a>P4.S7|操作需求|表达应来自开发者实际调用而非研究者任意设定|收集分类真实prompt再映射到任务|把要求变步骤|style clustering|
|<a id="p4-s8"></a>P4.S8|判定挑战|收集分类真实prompt再映射到任务|为评价设计oracles|命名第三职责|独立判断|
|<a id="p4-s9"></a>P4.S9|测量输出|为评价设计oracles|用ASR与AR刻画安全|明确指标|§3.4|
|<a id="p4-s10"></a>P4.S10|互补性|用ASR与AR刻画安全|ASR看实际成功，AR看是否识别风险|防止警觉等同防住|双指标分析|

### P5 · PDF p.2 proposed benchmark · 三个挑战各自闭合
论证出口：CIPR把来源、构造及测量连成可重复研究
联合选择分析（推断）：每项回应包含可获得数据与具体筛选/分析动作，没有凭“真实世界”标签替代证据。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p5"></a><a id="p5-s1"></a>P5.S1|总体产物|ASR看实际成功，AR看是否识别风险|提出研究用户侧PLC的CIPR基准|回答研究目标|§3|
|<a id="p5-s2"></a>P5.S2|场景构造|提出研究用户侧PLC的CIPR基准|选四常用语言，筛功能完整仓库并平衡领域复杂度|回应挑战I|repo review|
|<a id="p5-s3"></a>P5.S3|表达构造|选四常用语言，筛功能完整仓库并平衡领域复杂度|收1200余社媒prompt，12风格维度打分并聚类|回应挑战II|style extraction|
|<a id="p5-s4"></a>P5.S4|测量机制|收1200余社媒prompt，12风格维度打分并聚类|mock服务器截获出站请求测ASR，轨迹分析测AR|回应挑战III|oracles|

### P6 · PDF p.2 · 贡献引导
论证出口：转向产物与发现
联合选择分析（推断）：结构句。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p6"></a><a id="p6-s1"></a>P6.S1|结构引导|mock服务器截获出站请求测ASR，轨迹分析测AR|列贡献|归纳|三项|

### P7 · PDF p.2 contribution1 · 资源范围
论证出口：1920实例回答配置对风险的影响
联合选择分析（推断）：不是只把数据量当贡献，句内保留任务用途。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p7"></a><a id="p7-s1"></a>P7.S1|资源贡献|列贡献|1920实例基准用于测用户PLC影响仓库投毒风险|回收新轴及规模|§3|

### P8 · PDF p.2 contribution2 · 控制流程
论证出口：把变量和结果判定共同固定
联合选择分析（推断）：五类部件的价值是构成受控比较，非模块多就贡献大。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p8"></a><a id="p8-s1"></a>P8.S1|设计贡献|1920实例基准用于测用户PLC影响仓库投毒风险|受控流程合并真实仓库、任务注入、真实风格、技能规则条件及双oracle|解释如何建立比较证据|§3|

### P9 · PDF p.2 contribution3 · 实证发现与机制解释
论证出口：任务与表达通过不同路径影响安全
联合选择分析（推断）：长单句含两发现各自的机制和强度限定，不能只留4.5倍也不能把directional改为显著。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p9"></a><a id="p9-s1"></a>P9.S1|发现贡献|受控流程合并真实仓库、任务注入、真实风格、技能规则条件及双oracle|任务ASR差可达4.5倍，测试执行高攻击低警报；表达通过执行深度与恶意内容显眼程度间接作用，其中噪声警报趋势仅方向性|回答PLC影响并限定证据强度|§4/5|

## Nearby method/evaluation checks

Checked §3.4 oracles (PDF p.5): ASR requires mock-server request containing a planted target secret; AR is LLM-judged explicit suspicion, warning or refusal and separately human-validated. Checked §4 (PDF pp.5–6) distinguishes statistically significant prompt-style omnibus/underspecification from nonsignificant noise trend. Checked §5.2 (PDF pp.7–8) explains execution-depth truncation. Source caveat: §4 contains a sentence saying underspecification makes agents explore more thoroughly, while abstract/Introduction/§5.2 say reduced execution depth; the map preserves the Introduction’s account and flags this internal inconsistency rather than harmonizing it. Limitations (PDF pp.9–10) restrict harms to exfiltration and use unconstrained automation, excluding human approval modes.

## Length, transfer, and boundaries

没有独立结果段；最后一个长贡献句承担两个发现及解释，前面主要空间给构造效度。数字4.5倍依赖具体任务、注入及自治设置，不是所有代理配置的普遍风险倍数。方法文字内的不一致要求源级保留，不能用写作蒸馏自动“修复”成无保留因果结论。

## Verified physical-page lookup

Exact section-title/phrase lookup in the cached primary PDF; repeated mentions may include the Introduction itself.
- Attack Success. We deploy: [5](https://arxiv.org/pdf/2608.30686v1#page=5)
- 4 Experiments: [5](https://arxiv.org/pdf/2608.30686v1#page=5)
- 5.2 Prompt Expression Style: [7](https://arxiv.org/pdf/2608.30686v1#page=7)
- Limitations: [9](https://arxiv.org/pdf/2608.30686v1#page=9), [22](https://arxiv.org/pdf/2608.30686v1#page=22)

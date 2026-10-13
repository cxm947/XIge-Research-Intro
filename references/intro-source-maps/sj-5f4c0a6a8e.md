# Efficient Query-Based Attack against ML-Based Android Malware Detection under Zero Knowledge Setting：完整引言句级图

- 来源身份：sj-5f4c0a6a8e
- 指定版本：arxiv_v2_2023-09-06_camera_ready_format
- 指定原文：https://arxiv.org/pdf/2309.01866v2
- 实际读取原文：https://arxiv.org/pdf/2309.01866v2
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#advdroidzero) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [P8](#p8)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

Source ID: sj-5f4c0a6a8e
Version: arxiv_v2_2023-09-06_camera_ready_format
Primary URL: https://arxiv.org/pdf/2309.01866v2
Local primary SHA-256: 02e42df989583baadee0019ef05067ca764511c3da205ae7582f76b2a9976e4b

Scope: Complete Introduction reread in the 2026-10-04 reading record; nearby passages listed below checked for the stated callbacks. P/S numbers refer to the paper’s argument paragraphs and constituent sentences, with source continuations joined. Sentence contents are original Chinese paraphrases, not quotations. Already-known records the most relevant incoming information, not the reader’s entire knowledge. Selection rationales are editorial inferences, not evidence of individual coauthor intent.

## Paragraph and sentence map

### P1 · PDF p.1 §1 · 平台普及与检测价值
论证出口：ML检测是已有有用防御
联合选择分析（推断）：先说问题规模后承认防御有效，攻击研究才有保护价值。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p1"></a><a id="p1-s1"></a>P1.S1|背景|尚未引入本论文的特定问题|Android广泛支持移动设备和应用|立题|平台范围|
|<a id="p1-s2"></a>P1.S2|风险|Android广泛支持移动设备和应用|普及也带来恶意软件问题|转折|AMD|
|<a id="p1-s3"></a>P1.S3|规模证据|普及也带来恶意软件问题|报告有超3300万恶意样本威胁隐私和完整性|说明重要性|引用报告|
|<a id="p1-s4"></a>P1.S4|已有方案|报告有超3300万恶意样本威胁隐私和完整性|研究广泛采用ML检测|给防御答案|目标模型|
|<a id="p1-s5"></a>P1.S5|方案能力|研究广泛采用ML检测|分析应用特征高效识别分类威胁|解释已有价值|检测流程|

### P2 · PDF p.1 · 攻击已知但知识假设较强
论证出口：现实零知识条件下仍需考察攻击
联合选择分析（推断）：HRAT例子分别说明特征与梯度需要，不只把所有已有攻击叫白盒。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p2"></a><a id="p2-s1"></a>P2.S1|脆弱性|分析应用特征高效识别分类威胁|ML检测仍易受攻击|引入研究方向|鲁棒性评估|
|<a id="p2-s2"></a>P2.S2|攻击机制|ML检测仍易受攻击|问题空间修改可使特征跨决策边界|说明转换链|problem/feature space|
|<a id="p2-s3"></a>P2.S3|后果规模|问题空间修改可使特征跨决策边界|可大量生成隐蔽对抗样本，形成服务化风险|解释安全价值|效率目标|
|<a id="p2-s4"></a>P2.S4|近邻条件|可大量生成隐蔽对抗样本，形成服务化风险|已有攻击常需训练数据、特征空间和模型参数|找共同前提|zero knowledge|
|<a id="p2-s5"></a>P2.S5|具体近邻|已有攻击常需训练数据、特征空间和模型参数|HRAT据已知特征设计调用图操作|说明特征知识用途|feature mismatch|
|<a id="p2-s6"></a>P2.S6|额外依赖|HRAT据已知特征设计调用图操作|HRAT还用梯度选操作，需要数据和参数信息|说明反馈知识用途|query-only|
|<a id="p2-s7"></a>P2.S7|现实边界|HRAT还用梯度选操作，需要数据和参数信息|这些假设在现实可能过强|收束适用性|威胁条件|
|<a id="p2-s8"></a>P2.S8|目标条件|这些假设在现实可能过强|现实攻击者通常不知道内部数据、特征、参数|定义任务场景|threat model|
|<a id="p2-s9"></a>P2.S9|研究问题|现实攻击者通常不知道内部数据、特征、参数|零知识下高效生成仍待解决|提出剩余任务|AdvDroidZero|
|<a id="p2-s10"></a>P2.S10|挑战分工|零知识下高效生成仍待解决|困难分别来自样本侧异质空间与检测侧知识缺失|组织两根因|两挑战段|

### P3 · PDF p.1 · 样本侧搜索空间
论证出口：对象复杂性让盲搜规模大且异质
联合选择分析（推断）：例子解释不同操作单位，不是教导具体规避步骤；后续语义树需兼容这些类型。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p3"></a><a id="p3-s1"></a>P3.S1|第一挑战|困难分别来自样本侧异质空间与检测侧知识缺失|APK复杂结构产生大量异质扰动|定根因|selection tree|
|<a id="p3-s2"></a>P3.S2|对象解释|APK复杂结构产生大量异质扰动|APK是含manifest及DEX的归档|补必要背景|树层次|
|<a id="p3-s3"></a>P3.S3|比较轴|APK是含manifest及DEX的归档|可改空间比图像或文本多样|解释异质性|统一结构|
|<a id="p3-s4"></a>P3.S4|类型对照|可改空间比图像或文本多样|配置权限与调用关系不同于统一像素值|具体化操作单位差异|语义分类|
|<a id="p3-s5"></a>P3.S5|规模残余|配置权限与调用关系不同于统一像素值|即使同类型扰动仍大且离散|防止分类即解决一切|clustering|
|<a id="p3-s6"></a>P3.S6|规模实例|即使同类型扰动仍大且离散|权限有150多种且保护级别、影响各异|给离散搜索证据|批处理|

### P4 · PDF pp.1–2 · 检测侧不可见性
论证出口：错误特征方向使精巧修改也无效
联合选择分析（推断）：先解释特征错配，再排除迁移和精细反馈路线；这与样本数目大不是同一困难。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p4"></a><a id="p4-s1"></a>P4.S1|第二挑战|权限有150多种且保护级别、影响各异|目标检测器内部零知识|定信息边界|query policy|
|<a id="p4-s2"></a>P4.S2|差异来源|目标检测器内部零知识|检测器可用权限、活动、调用图等不同特征|解释不确定对象|高层类型选择|
|<a id="p4-s3"></a>P4.S3|失效关系|检测器可用权限、活动、调用图等不同特征|针对某类特征的修改可能不触及目标特征|连接信息与无效计算|semantic adjustment|
|<a id="p4-s4"></a>P4.S4|具体例|针对某类特征的修改可能不触及目标特征|调用关系变化对不用该特征的Drebin无效|验证非小幅弱化而是零作用|feature gap|
|<a id="p4-s5"></a>P4.S5|迁移边界|调用关系变化对不用该特征的Drebin无效|特征空间差异使直接迁移攻击次优|评估自然替代|query-based choice|
|<a id="p4-s6"></a>P4.S6|逆推边界|特征空间差异使直接迁移攻击次优|标签或置信反馈不足以高效识别精确特征|解释不能先完全反推|层次反馈|
|<a id="p4-s7"></a>P4.S7|已有依赖|标签或置信反馈不足以高效识别精确特征|旧方法期待实时梯度等精细反馈|区分已有控制信号|无梯度设定|
|<a id="p4-s8"></a>P4.S8|当前信息|旧方法期待实时梯度等精细反馈|零知识只给粗粒度输出，过程更盲|给可用资源|query feedback|
|<a id="p4-s9"></a>P4.S9|路线结论|零知识只给粗粒度输出，过程更盲|原来的精细反馈攻击不适用此条件|收束挑战|新策略|

### P5 · PDF p.2 · 方案与语义观察
论证出口：相似语义可扩散一次反馈的价值
联合选择分析（推断）：先声明两部件各解何事，再解释共用语义信号，防止纯模块名单。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p5"></a><a id="p5-s1"></a>P5.S1|总体方案|原来的精细反馈攻击不适用此条件|提出零知识查询框架AdvDroidZero|回答任务|§3|
|<a id="p5-s2"></a>P5.S2|分工|提出零知识查询框架AdvDroidZero|选择树处理异质大空间，语义调整处理知识缺失|对应两挑战|两机制|
|<a id="p5-s3"></a>P5.S3|观察入口|选择树处理异质大空间，语义调整处理知识缺失|APK扰动具有语义且影响程度不同|建立可用结构|语义分组|
|<a id="p5-s4"></a>P5.S4|关键关系|APK扰动具有语义且影响程度不同|语义相近扰动可能具有相近影响|给共享反馈依据|query diffusion|
|<a id="p5-s5"></a>P5.S5|例子一|语义相近扰动可能具有相近影响|音频硬件配置表达硬件及音频语义|说明抽象标签|树层次|
|<a id="p5-s6"></a>P5.S6|例子二|音频硬件配置表达硬件及音频语义|同类音频能力配置可能影响相似|具体化邻近关系|语义相似|
|<a id="p5-s7"></a>P5.S7|设计推论|同类音频能力配置可能影响相似|一项正反馈可据语义推及其他候选，辅助选择|从观察转信息效率|adjustment policy|

### P6 · PDF p.2 · 两机制的输入输出
论证出口：层次表示使粗反馈产生批量调整
联合选择分析（推断）：结构、聚类、级联与反馈扩散分别承担异质性、规模、类型发现和每query价值，不能只称“语义优化”。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p6"></a><a id="p6-s1"></a>P6.S1|表示选择|一项正反馈可据语义推及其他候选，辅助选择|不同粒度语义树将选择变为路径采样|把洞察转统一操作|§3.4|
|<a id="p6-s2"></a>P6.S2|异质能力|不同粒度语义树将选择变为路径采样|类似决策树，可处理异类扰动|回应类型差异|tree structure|
|<a id="p6-s3"></a>P6.S3|规模操作|类似决策树，可处理异类扰动|聚合相近语义候选并成组处理|回应候选数量|clusters|
|<a id="p6-s4"></a>P6.S4|规模收益|聚合相近语义候选并成组处理|减少搜索空间提高生成效率|解释操作价值|query cost|
|<a id="p6-s5"></a>P6.S5|反馈机制|减少搜索空间提高生成效率|按语义层级级联调整一批节点概率|回应不可见性|policy|
|<a id="p6-s6"></a>P6.S6|类型识别|按语义层级级联调整一批节点概率|少量初始查询可判断高层扰动类型|给先粗后细效果|cascade|
|<a id="p6-s7"></a>P6.S7|信息传播|少量初始查询可判断高层扰动类型|经树将所选候选反馈传给语义相近者|说明共享路径|semantic diffusion|
|<a id="p6-s8"></a>P6.S8|单次价值|经树将所选候选反馈传给语义相近者|一次query同时调整多个相近候选|量化信息利用逻辑|query efficiency|
|<a id="p6-s9"></a>P6.S9|任务闭合|一次query同时调整多个相近候选|提高正向类簇概率、降低负向类簇概率|回收到高效无知识搜索|evaluation|

### P7 · PDF p.2 · 多层实证结果
论证出口：查询预算与成功定义共同限定收益
联合选择分析（推断）：长预告承担主流模型、现实AV、时间切片及动态/稳健防御证据，数值不可脱离不同判据拼接。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p7"></a><a id="p7-s1"></a>P7.S1|数据范围|提高正向类簇概率、降低负向类簇概率|151637应用含135859良性及15778恶意|说明评价数据基础|§4|
|<a id="p7-s2"></a>P7.S2|目标范围|151637应用含135859良性及15778恶意|在Drebin等四类静态分析ML检测器评价|限定主实验|baseline table|
|<a id="p7-s3"></a>P7.S3|联合结果|在Drebin等四类静态分析ML检测器评价|效果与运行开销优于基线|给方法级结论|主比较|
|<a id="p7-s4"></a>P7.S4|成功率|效果与运行开销优于基线|主流检测器约90%攻击成功|给总体数值|ASR|
|<a id="p7-s5"></a>P7.S5|成本|主流检测器约90%攻击成功|约15查询、10分钟内生成80%目标样本|回应效率与预算|query/runtime|
|<a id="p7-s6"></a>P7.S6|外部范围|约15查询、10分钟内生成80%目标样本|还测现实AV、VirusTotal沙箱及FD-VAE|扩展条件|现实实验|
|<a id="p7-s7"></a>P7.S7|AV判据|还测现实AV、VirusTotal沙箱及FD-VAE|10查询内约92%样本减少检出引擎，成功样本引擎数降47.98%|区分检出数减少与全逃逸|VirusTotal|
|<a id="p7-s8"></a>P7.S8|时间变化|10查询内约92%样本减少检出引擎，成功样本引擎数降47.98%|2022近期样本10查询约89%成功|补时间迁移证据|recent malware|
|<a id="p7-s9"></a>P7.S9|较强条件|2022近期样本10查询约89%成功|沙箱10query约37%，稳健方法30query约77%|保留不同预算与强度|sandbox/FD-VAE|

### P8 · PDF p.2 conclusion paragraph · 无列表的贡献收束
论证出口：框架与关键设计已有实证铺垫
联合选择分析（推断）：只有一个短连续贡献段，前一九句结果段已承担证据；不是遗漏必需的第三条评价bullet。

|句|内容职责|已有信息|新引入内容|与前句关系|后文回收|
|---|---|---|---|---|---|
|<a id="p8"></a><a id="p8-s1"></a>P8.S1|结构引导|沙箱10query约37%，稳健方法30query约77%|总结关键贡献|切换归纳|最后两句|
|<a id="p8-s2"></a>P8.S2|框架贡献|总结关键贡献|提出零知识下高效查询框架|归纳总能力|§3/4|
|<a id="p8-s3"></a>P8.S3|设计贡献|提出零知识下高效查询框架|选择树处理异质空间，语义策略高效选候选|重申两设计及任务|§3|

## Nearby method/evaluation checks

Checked §3.1 (PDF p.3): goal explicitly preserves original malware functionality while changing classifier output. Checked §5.3 (PDF pp.13–14): actual framework needs confidence or an approximate confidence proxy; restricted/obscured outputs can defeat it, hybrid static/dynamic defenses are not comprehensively addressed, and its perturbation set must affect target features. Thus Introduction’s broad labels-or-confidence description must not be distilled as demonstrated label-only universality.

## Length, transfer, and boundaries

结果预告九句后是三句连续贡献段，无bullet也无独立评价贡献。这一布局把所有实证提前，收尾只重申框架与两设计。所有数值是源论文报告，不能把减少AV检出引擎数等同完全绕过全部引擎。本蒸馏只提取论证职责和边界，未复现攻击或生成攻击实现。

## Verified physical-page lookup

Exact section-title/phrase lookup in the cached primary PDF; repeated mentions may include the Introduction itself.
- 3.1 Threat Model: [3](https://arxiv.org/pdf/2309.01866v2#page=3)
- 5.3 Limitations: [13](https://arxiv.org/pdf/2309.01866v2#page=13)

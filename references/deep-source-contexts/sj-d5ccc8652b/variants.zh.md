# ACIArena：完整句群与贡献变体

以下均为编辑选项，不是原文引语或已验证写作效果。源姓名规范化为ACIArena/ACI-Sentinel；历史源单元保留原提取拼写。每一项给准确替换范围、意义成本与选择条件，不能仅取半句拼入不相容的上下文。

## V01 · P3.S5–S8：强近邻与评价基础设施缺口

(2) Lack of standardized evaluation settings. Existing studies often use simplified MAS implementations that differ substantially from real-world systems, making their findings difficult to generalize across deployments (Yu et al., 2025; Xie et al., 2025; Wang et al., 2025b). (3) Limited codebase extensibility. Their codebases also often lack the modularity needed for straightforward extension to new tasks and systems. MASLab already provides standardized inputs and evaluation protocols (Ye et al., 2025a), but it lacks the evaluation environment and diverse attack strategies needed to compare MAS robustness under different threat models. These gaps call for a unified framework that supports comprehensive security benchmarking and extensible evaluation.

- 范围：连续替换P3.S5–S8及其前置(2)标题，跨度内含(3)标题；规范引言[2250,3217)，源跨度SHA-256 83fa550b5b66315248325dc45a81110338030aec258e0c085eabd6e8fb95d071。替换文本实际保留(2)/(3)，P3.S1–S4与(1)标题不动；三限制组织句仍成立
- 语义/强度：保often、实现差异、已有MASLab能力；把compare and improve压为compare，少掉基准支持后续改善的目的，需在后文设计洞察补回。real-world仍为源作者的对比主张，不声称本轮调查生产部署
- 焦点/篇幅：四句依次区分可外推的设置、后续扩展、最近统一框架缺项、最终研究需求；不为每个缺口另造新贡献
- 选择条件：需要更清楚地区分标准化、外推与扩展职责；引文跟随来源断言，不把一般框架写成没有评价协议

## V02 · P4.S1–S4：把产品特性写成可用研究动作

We introduce ACIArena, a unified framework for evaluating MAS robustness under ACI attacks. The framework covers external inputs, agent profiles, and inter-agent messages as attack surfaces, together with instruction hijacking, task disruption, and information exfiltration as attack objectives. Unified interfaces support both MAS implementations and attack/defense modules, enabling consistent evaluation across the integrated systems. A modular codebase allows researchers to add new MAS and attack/defense modules without rebuilding the evaluation framework.

- 范围：完整替换P4四个历史分析单元；行内三个标题与stands out导航合为普通句
- 语义/强度：保威胁两轴和双方接口，enabling表研究能力，不直接保证所有新部署的外部有效性；without rebuilding是对模块化扩展的编辑推论，不是声称零适配工作或实测时间节省，若需最贴源可删该尾语
- 焦点/篇幅：从形容词标签转到覆盖、共享接口、加入新对象三种动作；四句不必每句一样长，分类轴最需要解释
- 选择条件：读者关心如何用这个研究产品组织实验，且不需要复述P3的编号。若审稿回应需一眼对照三缺口，保源行内标签也合理

## V03 · P5.S1–S3：维持基准发现为中心

Extensive experiments reveal systemic and multidimensional vulnerabilities in current MAS. Existing defenses provide only partial protection; defenses developed in simplified or incomplete settings often fail to transfer effectively to real-world scenarios and sometimes even amplify attacks. These findings motivate ACI-Sentinel, a simple yet effective defense that improves robustness by preserving task-aligned information rather than focusing on identifying suspicious messages.

- 范围：完整替换P5.S1–S3，保接后的贡献引导句O.S1
- 语义/强度：保systemic、often、sometimes和simple yet effective的源强主张；第一句由current MAS内容从句变介词宾语，第二句分号分开总体与特定防御类别，第三句由we propose改为findings motivate。实验仍为选定实现与配置，不把源real-world措辞当现场部署测试证明
- 焦点/篇幅：主要文字仍是基准得出什么；辅助防御只用一句交新方向，不抢占独立防御论文需要的完整机制和评价篇幅
- 选择条件：源研究确实以benchmark为主、发现自然引出辅助方案。若目标论文其实以防御为主，则需要另有设计与证据主线，不能借此压掉必要说明

## V04 · P5.S1：用代表性对照代替抽象结果

In controlled tests of CORBA, changing agent-role profiles can substantially change attack success even when the communication topology is fixed. This result shows why topology alone is insufficient for evaluating MAS robustness.

- 范围：P5.S1替为两句，随后保P5.S2–S3；事实来自§5.1，不冒充引言原句
- 语义/强度：保受控试验和具体被测攻击范围，不宣称任意攻击在任意角色变化下必然变化；结果为角色配置重要性的证据，不是识别角色的一般因果定律
- 焦点/篇幅：比“多维脆弱性”具体，直接使读者理解统一比较条件能纠正什么结论；代价是少讲其他维度并多占一句
- 选择条件：读者可能以为拓扑复杂即更安全，且后文会保效用/防御等其他发现。若首要问题是低任务效用被误判安全，可改选§5.2的BU/ASR对照，而不同时挤进两个例子

## V05 · B1.S1–S3：先说明评价单位，再说资源规模

To the best of our knowledge, ACIArena is the first benchmark to systematically evaluate MAS robustness under ACI attacks. It provides 1,356 test cases, each pairing a benign task with an ACI attack, organized by three attack surfaces and three attack objectives. We will publicly release the code and data.

- 范围：完整替换B1三句；each pairing取自§4.3，替换源第二句末尾broad coverage评价
- 语义/强度：保所知限定、first、systematically及未来共同发布承诺；1,356是任务–攻击案例，不是独立真实部署、全部模型运行次数或六系统×四域×三模型的完整交叉积。没有承诺许可证、已通过复现或数据已可下载
- 焦点/篇幅：资源是什么比大数本身更有可用性；已有P4列全轴类别后无需在B1再写两套三项全名
- 选择条件：读者可能误认样本单位，且方法节确实有可查配对定义。源p.1有code available脚注，若需要当前开放状态而非保留B1局部承诺，必须先核查再统一时态

## V06 · B2.S1：保留源的强因果主张

ACIArena unifies interface specifications for MAS robustness evaluation in a modular, extensible codebase, thereby avoiding generalization failures caused by simplified or inconsistent evaluation environments.

- 范围：B2整句；源provides unified名词结构改为unifies有限动作
- 语义/强度：保avoiding及caused-by限定，不悄悄改为may help；主张被避免的是特定实验环境导致的外推问题，不是所有未来分布偏移
- 焦点/篇幅：一句仍接“工程统一→科研可比较”的价值；不是把同一接口和同一代码库拆成两个贡献
- 选择条件：在重述源作者主张或目标研究证据确实支持该因果强度时使用。统一接口本身不能单独证明该效果；资格说明独立于源语法观察

## V07 · B2.S1：当自己的证据只支持共享评价基础

ACIArena provides shared interfaces for evaluating MAS and attack/defense modules through a common execution entry point. Its modular codebase supports extension to new systems and modules under the same evaluation structure.

- 范围：替换B2整句为两句；共同执行入口来自§4.3，不是原B2逐字命题
- 语义/强度：主动删除avoiding poor generalization，保已实现的接口与扩展能力；这是证据边界不同的替代方案，不是源强主张的等义版本，也不应反过来把源描述自动降格
- 焦点/篇幅：从外推效力转到研究可用基础；多一句区分当前可比的执行方式与未来可扩展性，少了最强科学效果声明
- 选择条件：用于新稿时，若只验证了执行一致性/扩展而没有排除简化环境导致的外推问题，应选此类表达；若已有对照证明，则V06更能保研究力度

## V08 · B3.S1：把因素分析落到可解释的知识结果

Our benchmarking shows that MAS robustness cannot be assessed from communication topology alone and that attack success must be interpreted alongside task utility. Analyses of defense failures further motivate preserving task-aligned information and inform the design of more effective defenses.

- 范围：B3整句替为两句；前句引入§5.1–5.2代表性发现，后句保原失败解释及设计指导，并回收P5.S3
- 语义/强度：源拓扑不足与效用取舍仍为强结果；inform design是研究指导，不声称已完成可靠的整体MAS安全设计。第二句没有声称语义裁剪对所有场景无效用损失或自适应攻击下完全稳健
- 焦点/篇幅：由in-depth/factors泛称改成读者能带走的具体判断，再交设计方向；代价是省去角色、模型、领域等因素的全面列举，贡献条目从1句变2句有实质理由
- 选择条件：需要让benchmark的认识价值与接口价值分开，且这些发现是研究主问题的代表性答案。若论文主要贡献是开放资源，可保源较短概括而把细结论放正文

## 原位核对元数据（V01）

- variant: V01
- replacement_scope: Historical P3.S5–S8 plus preceding limitation2 heading; internal limitation3 heading explicitly replaced, not discarded
- source_start: 2250
- source_end: 3217
- source_span_sha256: 83fa550b5b66315248325dc45a81110338030aec258e0c085eabd6e8fb95d071
- complete_resulting_P3_sha256: 5bacb0be95b0e0422bac00a0047ab9194c53320caff66443aa9641c7134df6c0
- preserved_context_units:
  - P3.S1
  - P3.S2
  - P3.S3
  - P3.S4
- label_counts:
  - (1): 1
  - (2): 1
  - (3): 1

完整源段与原始跨度文本不在此转录；哈希只绑定接受审阅的插入结果，不证明编辑适合所有语境。

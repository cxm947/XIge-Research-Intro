# 引言的正常收束：本文工作、主要成果与贡献

## 内容导航

- [1. 末尾三种职责，不是三遍摘要](#1-末尾三种职责不是三遍摘要)
- [2. 真实引言：功能分析与可迁移边界](#2-真实引言功能分析与可迁移边界)
- [3. 何时 3–4 项贡献合理](#3-何时-34-项贡献合理)
- [4. 原创正常收束示范](#4-原创正常收束示范)
- [5. 引言里结果概述的取舍](#5-引言里结果概述的取舍)

## 1. 末尾三种职责，不是三遍摘要

| 职责 | 读者问题 | 应写的信息 | 可以省略/合并的条件 |
|---|---|---|---|
| 本文工作 | 你们究竟做了什么，如何响应前面的问题？ | 方法/系统/研究的名称与对象，最关键的动作，以及动作为何对应问题 | 核心方案很短，可与洞察或结果合段；不能只剩“We propose a novel framework” |
| 主要成果概述 | 有什么最值得提前知道的结果？ | 一到两项主成果及理解它们不可缺少的比较或范围 | 目标体裁不预告结果，或结尾一句已足够时，不强开一段 |
| 贡献总结 | 我应记住本文完成了什么、取得了什么？ | 可区分、可复述的方法、技术设计、实现与评价，或重要知识、能力及资源 | 贡献已在紧凑结尾被清楚表达、且目标惯例不要求列表时，不强加 bullets |

三个位置允许重复核心术语，以稳定对象；不应重复整套步骤、同一组数值与所有解释。有效重复是“方案中给出作用机制，结果中呈现实现的成果，贡献中命名该成果的研究意义”。无效重复是把同一句换成“In summary”再说一次。

### 当前分支的收尾接口

双挑战分支的 P5 解释本文怎样完成研究，P6 按“框架／方法 → 关键设计 → 实现与评价”归纳。评价先选其建立的核心能力，再补理解它所需的范围；不要求第三项是另一种独立发明。方案直接接贡献时，由评价项承担必要的主成果预告。

若选择独立洞察或成果段，按真实内容重新编号，不能把另一示范的 P5/P6/P7 当成本稿的固定段号。完整模板和实际生成程序集中在[贡献单元](sentence-blueprint.md#p6-contributions)及[可选成果段](sentence-blueprint.md#可选独立洞察与成果段)；本文件只补来源、布局比较与示范，不另设一套生成流程。

## 2. 真实引言：功能分析与可迁移边界

### E1. AFLFast，CCS 2016：解释、工作、结果和贡献可以在一条主线上回扣

原文：Böhme、Pham、Roychoudhury，[Coverage-based Greybox Fuzzing as Markov Chain](https://mboehme.github.io/paper/CCS16.pdf)，§1，PDF pp.1–2。

短锚点：“Our main conceptual contribution”。

该引言先比较已有路线，再用路径访问不均解释改进空间；本文策略与主成果较早出现，随后给出模型与调度思路，最终分四项归纳模型、调度、搜索和工具。关键结构经验：贡献项虽可按技术对象命名，但正文已说明它们为何共同改善任务。不能只移植四个模块标题；也不能由这篇较长引言推出所有稿件都应同样展开。其概率/能量记号亦说明引言没有天然的公式禁令。[E1]

### E2. SpecFuzz，USENIX Security 2020：一般概念与具体原型可以分层

原文：Oleksenko 等，[SpecFuzz: Bringing Spectre-type vulnerabilities to the surface](https://www.usenix.org/system/files/sec20-oleksenko.pdf)，§1，印刷 pp.1481–1482 / PDF pp.2–3。

短锚点：“To showcase our method, we implement SpecFuzz”。

概念先解释如何使原本不可见的行为进入软件测试的观察范围，具体原型随后限定其实现对象；结尾先概述主要结果，再列五项贡献。两层有不同内容，因而不是仅靠换名字区分“洞察”和“系统”。五项列表证明贡献数有变化，不证明第五项泛称评价就是最适合当前稿的写法。实际改写应保留评价建立的具体认识，不盲抄列表类别。[E2]

### E3. Transformer，NIPS 2017：紧凑引言可以没有独立贡献清单

原文：Vaswani 等，[Attention Is All You Need](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)，§1，PDF pp.1–2。

短锚点：“The fundamental constraint of sequential computation, however, remains.”

四个正文段落依次交代已有路线、未消除的约束、attention 提供的可能性以及本文模型和主要能力/成果。末段后直接进入 Background，没有单列贡献 bullets。可迁移的是每段推进不同认识，最后正面落在研究产出；不应推断短到四段总是更好，或从它删掉当前复杂安全稿必要的对象解释。[E3]

### 共著源例中的再次强调：增加判断，不要求首次出现

[MOPT](https://www.usenix.org/system/files/sec19-lyu.pdf) §1，印刷 pp.1949–1950，方案已解释调度，贡献再将调查收束为依据历史表现调度的原则，并确认方法、经验结果和实践产物。部分核心事实确有重复；第二次出现将其归为可带走的成果，并不总是增加此前未见的数据。

[Diff-ID v1](https://arxiv.org/html/2303.18174v1#S1) §I，方案展开参照、对齐、差异与量度，贡献分别确认观察、方法、经验表现及使用条件。这是本篇成果的分工，不能变成每篇都要填满的四格。

[MPInspector](https://www.usenix.org/system/files/sec21-wang-qinying.pdf) §1，印刷 pp.4205–4207，方案解释三项技术困难，贡献却以两项确认分析框架及实际安全发现。下面是依源事实构造的编辑对照，不是原文逐句引语：

**反例：把机制数当贡献数。** “We extract message semantics. We learn state machines. We verify security properties.” 三句准确指出动作，却尚未说明为何形成三项可区分的研究所得。仅把标题改成“语义产物、行为表示、可检查结果”也不能完成这一步。

**有条件的正向操作：先合并共同建立同一能力的机制，再判断是否另有实质所得。** 本例材料同时有分析框架和使用它得到的安全发现，故可改写为：

> We develop MPInspector, a framework that reconstructs protocol behavior and verifies security properties of messaging-protocol implementations. Message-semantics recovery, state-machine learning, and formal verification jointly provide this analysis capability.
>
> Using MPInspector, we identify 252 property violations across three messaging protocols on nine IoT platforms and uncover eleven attack types that exploit combinations of these violations under the studied threat models.

第一项是“开发重建协议行为并验证安全性质的分析框架”，三类机制共同实现这项能力；第二项是“在九个 IoT 平台的三种消息协议中识别 252 项性质违例，并发现研究所设威胁模型下利用这些违例组合的十一类攻击”。后者是实际研究所得，不能把违例数叫作攻击数，也不能由工具发现违例推定全部后续分析自动完成。实现与实验评价也可以作为对同一方法的独立贡献层次：交代实际实现、评价范围及主要结果，就可以形成一项正常的实验贡献，不必另外产生一个独立的新知识产品。是否合并取决于本稿的研究重点、篇幅和条目分工；这里不要求复制两项，也不要求把机制改写成三个抽象名词。

据此生成时，允许同一核心事实在方案与贡献中再次出现，但应改变它的职责：方案解释如何工作，贡献确认已建立的能力、认识或产物。框架、关键技术、原型实现及实验评价可以形成同一研究的不同层次；若条目实质上重复同一动作，通常应合并。以正常作者句法直接陈述完成的工作，用必要机制或结果说明其内容，不让每项重新走完方案流程。

### 方法/系统论文中的普通作者句法

所读共著论文反复采用 propose、design、implement、evaluate 等作者动作；贡献项并不都要写成独立的新知识判断。[MOPT](https://www.usenix.org/system/files/sec19-lyu.pdf)（§1，印刷 p.1950）将方法应用、原型评价及性能结论放在同一项；[TextShield](https://www.usenix.org/system/files/sec20-li-jinfeng.pdf)（§1，印刷 p.1382）分别归纳方法、实际场景效果及自适应攻击下的评价。[FreeEagle v1](https://arxiv.org/pdf/2302.14500v1)（§1，PDF p.2）、[HashVFL v2](https://arxiv.org/pdf/2212.00325v2)（§I，PDF p.2）和 [JWBinder v2](https://arxiv.org/pdf/2310.17304v2)（§1，PDF p.4）的最后一项都明确陈述实验评价及其结论。其中 JWBinder 将技术、原型与评价分为三个层次；这些层次共同属于同一方法。

[UNIFUZZ](https://www.usenix.org/system/files/sec21-li-yuwei.pdf)（§1，印刷 p.2778）由简短方案句直接转入贡献；[Diff-ID v1](https://arxiv.org/pdf/2303.18174v1)（§1，PDF p.3）则分别列出观察、方法、评价及使用条件。它们支持不同的正常收束选择，不构成所有稿件的统一列表。arXiv 版本按链接所示版本核读，不声称等同最终期刊文本；共著署名也不说明某位作者逐字执笔。

普通作者动作不自动使评价变成贡献。先从中心问题选择评价建立的能力，再回填作者的实现与验证动作，最后按需保留范围或数字。完整英文模板与逐句生成集中在[贡献单元](sentence-blueprint.md#p6-contributions)，不在这里重复一组句族。

三种来源支持的布局都可用：Diff-ID、UNIFUZZ 说明方案可以直接接贡献；FreeEagle 将少量成果并入方案后再接贡献；HashVFL、JWBinder、MPInspector 另设成果概述后再归纳。先遵守用户布局，再判断结果理解是否确需另段；这些例子没有建立一个强制结果段。

novel、first、state-of-the-art 是需要另行支持的新颖性或比较主张，不能从上述普通句法推得。专业表达并不意味着删除作者动词或把每项升格为独立发明；其基础是主语明确、术语准确、动作与结果具体、范围恰当。理论、测量和资源稿按实际所得采用证明、测量或资源句法，不强套原型实验组合。

### 这三个例子共同排除的机械规则

- 不存在从这些例子推出的“七段是顶会引言硬标准”
- 不能规定成果只许出现在倒数第二段；它也能较早出现，后面继续解释关键思路
- 不存在统一的 3 条、4 条或 5 条贡献配额
- 没有独立 contribution heading 不代表没有贡献表达
- 某篇发表论文出现某种写法，只说明该写法实际存在，不说明其每一句都是可复制的最佳写作决策

## 3. 何时 3–4 项贡献合理

当前系统／方法分支先采用三项：总体框架／方法、关键技术设计、实现与评价。用户未指定数量时，按实际内容可调整为三至四项或其他数量；这只是编辑起点，不是从少量样本估计出的普遍频率。

一项主成果可以由多个实质层次支撑。例如：整体框架、关键技术设计、原型实现与实验评价；也可以是问题表述、方法及重要发现。每项应有可辨认的内容，但不要求每项都是彼此独立的创新产品。若资源本身使此前不能开展的比较成为可能，可独立占一项；若只是代码附件，不自动增列一个“开源贡献”。

### 每项贡献应达到的内容粒度

贡献项应使读者知道：**本文完成了什么实质工作，其内容或所得是什么。** 必要时再带一个关键区别或范围。不是每项都要硬套同一句法、塞进百分比或重复一段完整机制。

| 常见活动/模块清单 | 改为成果表达时真正要补的内容 |
|---|---|
| We build a graph module. | 表示保留了哪种先前没有被利用的关系，因此支持什么推理/执行/比较 |
| We add a multi-agent component. | 哪种协调、信息或控制问题被解决，组合为何产生单体没有的能力 |
| We conduct extensive experiments. | 先选验证建立的核心能力，再补评价工作及必要范围；不要把实验项目与局部结果逐项塞进贡献 |
| We collect a large dataset. | 数据覆盖、标注或组织原则使什么研究问题现在可检验 |
| We integrate existing tools. | 非平凡集成建立了什么可复用机制、统一表示、比较关系或新能力 |

模块名称可以保留，尤其该模块就是独立的方法贡献时。要修的是“只有名称、没有研究成果”，不是禁止技术分项。We propose、We design、We implement 均可以是正常学术动作，后面必须有清楚对象与意义；不能靠动词黑名单模拟成熟作者。

### 是否应单列的判断

- 删掉某项后，是否有一种实质成果消失？若只是同一方法的两个实现步骤，通常合并
- 这项是否在前文有所铺垫，并由论文实际工作支撑？结尾不能突然新增“通用理论”“首次”“零人工”等未建立主张
- 评价项是否让读者记住验证建立的具体能力，而非实验目录？它仍要说明实际验证工作及必要范围；同一方法的有效性、鲁棒性或成本可以形成评价贡献，独立发现不是单列前提
- 实际只有两项就写两项；有五项且各有独立分量，也不为整齐强行压成三项
- 贡献与挑战不是必须一一对应：一个共同机制可能解决多个障碍，一项发现也可能修正问题定义

## 4. 原创正常收束示范

下面的系统、研究过程和结果全部是**构造的教学材料**，不是用户项目，不是已完成实验的报告，不能移入真实论文当作事实。数值和 first 主张均未编造。示范先明确假定事实，再演示如何把同一事实写成正常学术引言。

### 假定事实卡

研究对象是有状态 API 的失败复现。假设此教学研究已经建立一种表示，关联请求的前置条件与状态变化；已经实现一个回放系统，使用经记录的状态检查选择可用前缀，再执行请求；已经在所选 API 工作流和相同测试预算下比较序列回放基线，观察到更多可稳定复现的失败；控制比较支持前缀适用性检查在该改善中的作用。没有假定覆盖所有 API，也没有假定公开发布数据或代码。

### 版本 A：选择独立成果段时的三项职责

**本文方案。**

> We present StateReplay, a method for reproducing failures in stateful APIs from reusable test sequences. StateReplay associates each request with the conditions it requires and the state changes observed during execution. It then checks whether a recorded prefix can establish the conditions needed for the next request, allowing successful prefixes to be reused when they remain applicable. This design turns a stored test sequence into an explicit basis for deciding what can be replayed in the current state.

**主成果概述。**

> Across the evaluated API workflows, StateReplay reproduces more failures than sequence-only replay under the same testing budget. Controlled comparisons identify prefix-applicability checking as a contributor to this improvement. These results show that preserving the conditions under which a sequence succeeds can improve failure reproduction beyond preserving request order alone.

**贡献总结。**

> This paper makes three contributions. First, we introduce a state-conditional representation of reusable API tests that preserves the dependencies needed for valid replay. Second, we develop a replay method that uses those dependencies to select applicable prefixes and continue execution from the resulting state. Third, we implement StateReplay and evaluate it on the selected API workflows. The results show that applicability-aware reuse reproduces more failures than sequence-only replay under the same testing budget.

**功能差异。** 方案让读者看懂本文究竟怎样做；成果段让读者知道它取得什么主要结果；贡献用三个内容层次重新组织前文。核心术语重复是对象照应，动作顺序没有被完整重讲，结果没有被逐表审计。末尾留下的是本文建立的能力和认识。

**为什么这里三项可成立。** 假定事实支持表示、使用该表示的回放方法，以及原型与评价这三个内容层次。评价虽用于验证同一方法，仍可正常单列；如果前两项只是对同一动作的两种命名，应合并。列表数量由本稿分工决定，不为了示范数字硬拆。

### 版本 B：当前分支的方案直接接贡献

沿用同一教学事实，将关键思路并入方案，评价结果由末项贡献承担：

> In this paper, we propose StateReplay, a method for reproducing failures in stateful APIs. Our approach is to preserve the conditions under which a request sequence succeeds, so that reuse can be decided from applicability rather than request order alone. StateReplay links each request to its required conditions and observed state changes, checks whether a recorded prefix can establish the next request's prerequisites, and reuses that prefix when those checks succeed.
>
> Our main contributions are summarized as follows.
>
> - We propose StateReplay, a replay method that selects reusable request prefixes according to their applicability in the current API state.
> - We develop a state-conditional test representation that links requests to the prerequisites and observed state changes needed for valid replay.
> - We implement and evaluate StateReplay on the selected API workflows, demonstrating that applicability-aware reuse reproduces more failures than sequence-only replay under the same testing budget.

方案解释工作怎样发生；三项贡献分别确认总体方法、关键表示及验证建立的能力。评价项没有重复整套实验设置，也没有另造发现。假定材料支持预算和比较结论，所以保留这些决定含义的条件；未假定公开发布代码，不增加开源贡献。

### 失败收尾应怎样修

不要把两段收成：“Table 1 supports representation quality. Table 2 compares the replay rate. Further experiments are needed before generality can be established. The dataset and deployment evaluation remain incomplete.” 这段不承担前述引言末尾职责。

修复动作不是删除所有边界：把会改变结果含义的范围嵌入“in the evaluated API workflows”，把“本文提出/建立了什么”重新写到前景。若某项关键结果尚未获得，取消对应已完成主张，改为实际研究目的或对已完成工作的准确说明；在稿外单列缺失事实，不把待办清单伪装成贡献。

## 5. 引言里结果概述的取舍

选择结果的标准是它是否帮助读者快速判断本文对前面问题的回答，而不是它来自第几张表。通常先放主能力/主发现，随后才考虑一个有不同作用的辅助结果，例如效率代价、解释性对照或实际发现。具体数量按稿件决定。

- 可以给强而具体的数字，但说明指标对象与决定其意义的比较条件
- 不把所有子集、消融、对照、置信区间和复现实验细节挤成一个密集段落
- 一句结果后若需要长篇证明链才能不误导，先重写它的粒度，而非让引言提前承担全部验证
- 历史积累可以说明研究基础，当前方法效果应由对应的当前研究材料支撑；不要互相偷换
- 在方案与贡献型收束中，优先采取有范围的总体结果表达；不以 Table X 逐项交代证据账目，也不以“还缺什么”作为全文入口的最后印象

这里没有宣称引言不能引用表、图或结果章节。某一处引用若让读者更容易定位关键事实，完全可以保留；问题是整段是否仍在阐明本文工作的价值与贡献。

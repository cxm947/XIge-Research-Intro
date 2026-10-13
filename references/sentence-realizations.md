# 同内容、同职责的英文实现库

按内容职责提供43组、每组3–4式原创英文表达。先在[逐段程序](sentence-blueprint.md)选内容，再在同组取一种自然形式；这些是可用变体，不是源文引语或质量评分。

源锚直接进入[完整句级图](intro-source-index.md)的已核单元；范围与支持关系可查[句式来源索引](sentence-source-index.json)。标作局部参照或边界例的来源不证明整组事实包。P/S不是原论文印刷编号；完整父段与别名见[坐标表](intro-coordinate-map.json)，正文补读使用独立锚，不伪造引言句号。

## 内容导航

- [使用约定](#section-1)
- [P1：广领域→具体领域→命名任务与意义](#section-2)
- [P2：先选择正确内容关系，再在同组换形式](#section-3)
- [要求与难点：从剩余关系选择必要解释](#section-4)
- [P5：整体系统、挑战响应与输入输出闭合](#section-5)
- [贡献：整体、技术与最终评价](#section-6)
- [采用与删并](#section-7)

<a id="section-1"></a>
## 使用约定

先决定本句自然需要表达什么，再在这份内容的可用表达中选择。事实包是候选之间共享的含义，不是每句话都必须填满的表。输入、条件、用途已经清楚或暂不需要时，可以留在相邻句或首次需要的位置；段落共同完成其职责。**同组各式须使用同一个事实包**，保持对象、条件、比较关系、证据类型与力度。可变化的是主语、语序、主动被动、同义动词/名词表达和复句组织；这些正常表达选择有用，不需要为了“有差异”另造命题。不同内容分支已单独编号，不能互称同义替换。

- 事实包不等于逐字字符串。普通名词按句法补足冠词/单复数；句式已经带 a/the/one 时只填名词核心和修饰语，不重复冠词；专名不机械加 the。[K] 作 a [K] 时是可数类别名词，[W] 作 one [W] 时是单数工作单位。[v] 是动词原形；[v-ing] 是同一动作的动名词；[p] 是不带主语的限定谓词；[clause] 是有主语谓语的完整从句。主谓数和必要语法变形随槽位调整，事实不变
- 同组动作的语法变形不得改变时态和完成状态。下文使用论文中已经完成的方法/评价状态；尚未做完时不能只套完成式
- 前文已明确且自然可继承的范围可在**所有候选中同样省略**；不能为更顺口而只在某式删除必要条件
- 以下“选择1/2/3/4”等说明信息入口，不是强制句序。各式并不都要进入正文
- 每组源锚支撑内容职责及关系，不声称各候选英文都出现在源文。源文实际选择、编辑解释和这些生成候选是不同证据层

<a id="section-2"></a>
## P1：广领域→具体领域→命名任务与意义

先按[选择操作A](selection-operations.md)选择贴近任务的上位研究领域，再选择表达。普通重要性句不负责自动找到正确领域入口。

### P1.1 用普通高层价值进入广领域
事实包：B 对 A 有重要作用。这里可以是通常的领域/研究意义，不必先构造具体下游用户或决策流程。
前接：开篇或已知研究活动；后交：相关具体领域及任务。选择：1直接说明重要性；2领域作主语说明作用；3先承接活动；4强调该领域在活动中的角色。
1. [B] is important for [A].
2. [B] plays an important role in [A].
3. In [A], [B] plays an important role.
4. The role of [B] in [A] is important.
源锚：[FirmSec P1.S1、P2.S1](intro-source-maps/sj-0010159902.md#p1-s1)；[FirmRCA P1.S1–S3](intro-source-maps/sj-446d78ec82.md#p1-s1)；[MPInspector P1.S1](intro-source-maps/sj-1f315ef889.md#p1-s1)；[Manchester Phrasebank：重要性表达](https://www.phrasebank.manchester.ac.uk/introducing-work/)。A采用自然活动名词，如系统可靠性、软件安全或自动化分析；具体关系可由下一句自然展开。

### P1.2 在大领域内落到具体领域的实际角色
事实包：在 B 中，F 提供 O，以支持动作 v。F 可以是具体子领域、对象或系统层，但其从属/使用关系必须真实。
前接：B 的用途；后交：F/O 成为任务对象。选择：1接具体领域；2先共有大领域、突出被支持的活动；3接具体领域的功能；4以提供产物的方式开头。
1. Within [B], [F] provides [O], supporting [v-ing].
2. In [B], [v-ing] is supported by the [O] that [F] provides.
3. [F] supports [v-ing] within [B] by providing [O].
4. By providing [O], [F] supports [v-ing] within [B].
源锚：[FirmSec P2.S1–S2](intro-source-maps/sj-0010159902.md#p2-s1)；[UVSCAN P2.S1–S3](intro-source-maps/sj-a36437c84c.md#p2-s1)；[HashVFL P1.S3–S4、P2.S1、P2.S4–S5](intro-source-maps/sj-3419195084.md#p1-s3)。不把“支持某用途”加强为保证完成，不新增行业采用规模。

### P1.3 命名任务并给输入、输出和条件
事实包：T 是在 C 下从 I 产生 O 的目标任务；这里只定义目标，不提前宣称方法已经实现。
前接：具体对象；后交：T及当前需要的任务信息给P2背景桥梁。输入/条件影响当前理解时写入；否则可只写命名任务及目标，稍后按需要补充。选择：1任务名作入口；2输入作入口；3条件优先；4先目标后命名。
1. [T] aims to produce [O] from [I] under [C].
2. Given [I], the goal of [T] is to produce [O] under [C].
3. Under [C], [T] seeks to produce [O] from [I].
4. Producing [O] from [I] under [C] is the goal of [T].
源锚：[FirmRCA P3.S1、P8.S1–S2](intro-source-maps/sj-446d78ec82.md#p3-s1)；[ORL-Auditor P2.S7、P2.S10、P1.S4](intro-source-maps/sj-6eeb51e521.md#p2-s7)；[Diff-ID P1.S2、P1.S4、P8.S4、P8.S13](intro-source-maps/sj-9042a938b2.md#p1-s2)；[AsgLDP P1.S4–S5、P1.S7、P3.S1、P4.S1–S3](intro-source-maps/sj-dc32e376bc.md#p1-s4)。T 的具体动作宜替换泛用 produce，例如 identify/determine/recover；四式保持同一动作。

### P1.4 可选：用具体用途解释任务意义
事实包：O 使使用者 A 能执行有后果的动作 v；适合具体用途是论文主线时。普通高层任务意义可以复用P1.1的自然表达，不强制本组的使用者/输出结构。
前接：任务输出；后交：为什么需要可靠完成 T。选择：1接输出；2先输出可用的条件；3使用者及使用关系先行；4使用者及任务动作先行。
1. [O] enables [A] to [v].
2. With [O], [A] can [v].
3. [A] can use [O] to [v].
4. [A] can [v] using [O].
源锚：[FirmSec P9.S6–S8](intro-source-maps/sj-0010159902.md#p9-s6)；[Password Correlation P5.S2–S5](intro-source-maps/sj-9aee30689b.md#p5-s2)；[UVSCAN P2.S5–S8](intro-source-maps/sj-a36437c84c.md#p2-s5)（任务重要性参照；未直接给出产物→使用者动作）。四式固定“提供能力支持”这一强度；若 O 只是相关信号而非足够的使能依据，先改事实包，不能把 can 当保险词掩盖缺证据。

### P1.5 可选、真实、相关的数量例子
事实包：来源 S 报告在时期 Y、范围 D 中，指标 K 的值为 V。只陈述同一报告，不从数量自行推出安全性/有效性。
前接：已经说明该规模为何与任务有关；后交：具体应用后果或命名任务。选择：1先来源依据；2先同一测量范围/时期；3先被报告的指标；4先来源动作、数值作为所报告值。
1. According to [S], the [K] for [D] in [Y] is [V].
2. For [D] in [Y], [S] reports a [K] of [V].
3. The [K] reported by [S] for [D] in [Y] is [V].
4. [S] reports [V] as the [K] for [D] in [Y].
源锚：[FirmSec P1.S2](intro-source-maps/sj-0010159902.md#p1-s2)；[UVSCAN P1.S2](intro-source-maps/sj-a36437c84c.md#p1-s2)；[CPscan P2.S3](intro-source-maps/sj-390b20426f.md#p2-s3)。预测须把 reports 改为 projects 并在四式保持；样本统计、市场估算与部署实测不能互换。数字无助于论证可删整项。

<a id="section-3"></a>
## P2：先选择正确内容关系，再在同组换形式

本组保留原有P2.*职责编号，编号不指定当前稿的物理段落。当前作者的P2桥梁可用P2.1等实践说明与P2.2的正面能力／条件；其余涉及具体不足、转折或gap的表达按实际关系放入P3/P4，不能因编号把P2写成gap综述。先在稿外执行[选择操作B](selection-operations.md)核对任务层强答案，再按当前段落职责取形式；前人已有的相关能力保持完整，组件引文不代替总体任务近邻。

### P2.1 真实实践及采用目的
事实包：A 通常使用 R 执行动作 v，条件为 C。已有材料支持“通常”，不是偶然案例。
前接：任务或使用者；后交：该实践的能力、输入条件或局限。选择：1人/组织先行；2任务条件先行；3实践先行；4动作目的先行。
1. [A] commonly use [R] to [v] under [C].
2. Under [C], [A] commonly use [R] to [v].
3. A common practice among [A] under [C] is to use [R] to [v].
4. To [v] under [C], [A] commonly turn to [R].
源锚：[CPscan P1.S2–S3、P2.S1–S2、P2.S4](intro-source-maps/sj-390b20426f.md#p1-s2)；[FirmSec P2.S2、P2.S5](intro-source-maps/sj-0010159902.md#p2-s2)。主语单数时统一 uses；未证普及程度时统一去 commonly/common，不保留一式偷偷加强。

### P2.2 已有答案的真实能力与适用条件
事实包：N 在 H 成立时能通过动作 v 获得 O。引用支持该适用范围中的能力；本组不额外声称 H 是必要条件。必要性另用 P2.8。
前接：同一任务；后交：目标条件是否仍满足 H。选择：1方法先行；2前提先行；3机制先行；4输出先行。
1. [N] can obtain [O] by [v-ing] when [H-clause].
2. When [H-clause], [N] can obtain [O] by [v-ing].
3. By [v-ing], [N] can obtain [O], provided that [H-clause].
4. [O] can be obtained by [N] through [v-ing] when [H-clause].
源锚：[ORL-Auditor P3.S2、P3.S5、P3.S7–S8](intro-source-maps/sj-6eeb51e521.md#p3-s2)；[Diff-ID P2.S1–S2、P4.S3–S4、P5.S4–S5](intro-source-maps/sj-9042a938b2.md#p2-s1)；[MeTFA P4.S3–S5、P5.S2、P5.S4](intro-source-maps/sj-f612de4bf1.md#p4-s3)。when/provided that 表明所述能力的适用条件，并不单独建立必要性；下一句要以 H 缺失推出失败时，必须另有必要性依据。

### P2.3 更强近邻已经解决一项旧不足，仍依赖另一条件
事实包：N2 用机制 K 解决已定义的 L，但仍要求 H。两项都经过核实。
前接：已有较弱答案及 L；后交：H 在目标场景中的可满足性。选择：1方法先行；2进步先行；3机制先行；4旧不足先行。
1. [N2] addresses [L] through [K], but still requires [H].
2. Although [N2] addresses [L] through [K], it still requires [H].
3. By using [K], [N2] addresses [L] while retaining its requirement for [H].
4. [L] is addressed by [N2] through [K], but the method still depends on [H].
源锚：[Diff-ID P4.S3–S6](intro-source-maps/sj-9042a938b2.md#p4-s3)；[FreeEagle P5.S2–S4](intro-source-maps/sj-33b7f0ad03.md#p5-s2)（边界例：已有无数据方法仍有限制，未建立保留必要输入H）；[V-SHUTTLE P3.S7–S9、P3.S11–S12](intro-source-maps/sj-0f6adb9f11.md#p3-s7)；[JWBinder P3.S6–S7](intro-source-maps/sj-81630a3e7e.md#p3-s6)（边界例：孤立Wasm检测遗漏交互，不是本组的进步后残余条件）。此组不能替代互补路线的介绍；“解决”只指 L，不夸大为解决整个任务。

### P2.4 目标条件使必要信息不可得
事实包：在 C 中，资源 H 不可得，因此 N 不能直接执行任务操作 v。不能直接不等于任何改造都不可能。
前接：N 需要 H 已建立；后交：G 或获取/替代 H 的要求。选择：1目标条件先行；2方法边界先行；3缺失信息先行；4先因后果。
1. Under [C], [H] is unavailable, so [N] cannot directly [v].
2. [N] cannot directly [v] under [C] because [H] is unavailable.
3. The unavailability of [H] under [C] prevents [N] from directly [v-ing].
4. The absence of [H] under [C] leaves [N] unable to [v] directly.
源锚：[ORL-Auditor P3.S8–S9、P3.S11–S12](intro-source-maps/sj-6eeb51e521.md#p3-s8)；[MPInspector P3.S3–S6](intro-source-maps/sj-1f315ef889.md#p3-s3)；[FreeEagle P3.S3–S4、P5.S1](intro-source-maps/sj-33b7f0ad03.md#p3-s3)。requires H 与 H unavailable 必须同一对象/访问角色，不能拿用户无数据替换服务器无数据。

### P2.5 既有能力与实际代价冲突
事实包：N 取得能力 G，但引入代价 K；K 限制其用于 S。这里是权衡，不是无能力。
前接：N 的能力；后交：需保留 G 并控制哪项代价。选择：1双事实平铺；2承认收益后转折；3接部署场景；4以代价作新信息焦点。
1. [N] provides [G], but its [K] limits its use in [S].
2. Although [N] provides [G], its [K] limits its use in [S].
3. In [S], the use of [N] is limited by [K], despite the [G] it provides.
4. The [K] incurred by [N] limits its use in [S], even though it provides [G].
源锚：[JWBinder P2.S5、P2.S7–S8](intro-source-maps/sj-81630a3e7e.md#p2-s5)；[CPscan P3.S2–S4](intro-source-maps/sj-390b20426f.md#p3-s2)；[SyzTrust P3.S4、P3.S6–S7](intro-source-maps/sj-689896e985.md#p3-s4)。限定词如 high/expensive 需明确操作与用途，不将任何非零成本写成不可部署。

### P2.6 已有结果与一个明确的未答问题
事实包：现有结果E建立命题P，但这些结果未回答研究问题Q。Q是完整间接问句，疑问算子、比较端点、层次和范围固定；这里只说这些结果未回答Q，不声称整个领域无人回答或方法运行失败。
前接：前人能力及证据；后交：回答Q需要的构造、经验区分或研究设计。选择：1证据先行；2先接受已知；3问题先行；4并列已建立和未建立的关系。
1. [E] establishes that [P-clause], but does not answer the question of [Q-indirect].
2. Although [E] establishes that [P-clause], the question of [Q-indirect] is not answered by these results.
3. The question of [Q-indirect] is not answered by [E], which establishes that [P-clause].
4. [E] establishes that [P-clause] without answering the question of [Q-indirect].
源锚：[ChatGPT-VM P3.S3–S5、P4.Q0、P4.RQ1、P4.RQ2、P4.RQ3](intro-source-maps/sj-ac970c8450.md#p3-s3)；[Quantifying P2.S6、P3.S1、P3.S3–S4](intro-source-maps/sj-a68da04b3f.md#p2-s6)；[VERIFI P2.S3–S4、P3.S1–S2、P3.S7、P4.S1–S3](intro-source-maps/sj-1b6614ac62.md#p2-s3)；[MeTFA P4.S5、P5.S2、P5.S7–S8](intro-source-maps/sj-f612de4bf1.md#p4-s5)。内容先分岔：是否成立用whether，关系刻画用how，类别/程度问题用which/what/how much；选定Q后四式不变。这些问法属于不同事实，不是组内可替换词；例如how A compares with B不自动改成whether A agrees with B。

### P2.7 用正面研究范围收束，不强塞新颖性
事实包：本文研究在 C 下如何执行 v；不声称该问题此前无人研究。
前接：已有答案后的剩余问题；后交：设计解释、可观察性或评价设计，已有能力可直接作为方法基础。选择：1作者动作先行；2条件先行；3研究对象先行；4回接当前问题。
1. We study how to [v] under [C].
2. Under [C], we investigate how to [v].
3. How to [v] under [C] is the focus of this study.
4. Our focus is on [v-ing] under [C].
源锚：[TextBugger P6.S1–S3](intro-source-maps/sj-238a78de63.md#p6-s1)；[Enkidu P3.S5–S6、P4.S1](intro-source-maps/sj-c423d986aa.md#p3-s5)。本组是操作型研究范围；“纳入统一流程”若未指出实际构造或待检验关系，仍未建立研究增量。若已核实开放问题，可在内容层改用“remains open”，但那不是这组中一个自由措辞替换。

### P2.8 已有答案依赖的必要输入或条件
事实包：N 要通过动作 v 获得 O，必须有资源 H；这里只陈述必要性，不声称 H 单独就足以保证成功。
前接：N 的真实能力与机制；后交：目标场景是否仍具备 H，可接 P2.4。选择：1动作目标先行；2方法先行；3必要输入先行；4所需结果作话题。
1. To obtain [O] by [v-ing], [N] requires [H].
2. [N] requires [H] to obtain [O] by [v-ing].
3. [H] is required for [N] to obtain [O] by [v-ing].
4. Obtaining [O] by [v-ing] with [N] requires [H].
源锚：[ORL-Auditor P3.S2、P3.S8、P3.S11](intro-source-maps/sj-6eeb51e521.md#p3-s2)；[FreeEagle P5.S1、P3.S3](intro-source-maps/sj-33b7f0ad03.md#p5-s1)；[MPInspector P3.S1、P3.S3、P3.S5–S6](intro-source-maps/sj-1f315ef889.md#p3-s1)；[Diff-ID P8.S4–S5、P8.S9](intro-source-maps/sj-9042a938b2.md#p8-s4)。H 是名词化的输入/条件；与 P2.2 的条件能力是不同命题，不混算同事实四式。

<a id="section-4"></a>
## 要求与难点：从剩余关系选择必要解释

常规方法/系统稿有两项真实根因时复用CH程序。先在内容层写出实际任务中的判断／操作、后果与场景障碍，再调用CH.1–CH.5解释技术根因和所需能力；CH.2的技术失败或“平衡两指标”不能单独充当应用层段首。要求本身不证明尚未解决；已有工具能满足时用作采用理由，测量问题解释观察与可辨识关系。按任务→障碍→能力归组，不按组件或段落数量制造困难。

### CH.1 从应用条件引出必需操作
事实包：在实际 C 下，为完成 T，方法必须执行 v；该必要关系已成立。
前接：G或前一要求；后交：已有能力如何满足v，或v的真实设计/观察阻力。选择：1任务先行；2条件先行；3操作必要性先行；4任务依赖作主语。
1. To perform [T] under [C], a method must [v].
2. Under [C], performing [T] requires a method to [v].
3. A method must [v] to perform [T] under [C].
4. Performing [T] under [C] requires the method to [v].
源锚：[UVSCAN P4.S1、P4.S3、P6.S1–S2](intro-source-maps/sj-a36437c84c.md#p4-s1)；[FirmSec P7.F1、P7.S2、P7.S6](intro-source-maps/sj-0010159902.md#p7-f1)；[MPInspector P3.S1、P3.S3、P3.S5](intro-source-maps/sj-1f315ef889.md#p3-s1)。本组建立必要性，不建立新颖性或未解决性；P2已可满足时不能重新写成待发明能力。不能从“本组件使用该信息”倒推出“任何合理方案都必须用同一组件”。

### CH.2 根因使自然办法不能直接完成操作
事实包：根因 H 导致自然办法 N 无法直接执行 v。H 是关系或机制，非单独 challenging。
前接：必需操作及 N；后交：缺失能力或后果。选择：1根因先行；2自然方案先行；3阻力作主语；4先说明需要解释的失败。
1. Because [H-clause], [N] cannot directly [v].
2. [N] cannot directly [v] because [H-clause].
3. The fact that [H-clause] prevents [N] from directly [v-ing].
4. [H-clause]; consequently, [N] cannot directly [v].
源锚：[Diff-ID P7.S1、P7.S4、P7.E1、P7.S7–S8](intro-source-maps/sj-9042a938b2.md#p7-s1)；[Cert-RNN P3.S2–S3](intro-source-maps/sj-acbc08a57a.md#p3-s2)（直接迁移受计算依赖限制；不把较松认证界写成无法认证）；[CPscan P4.S5–S6、P4.S9–S11](intro-source-maps/sj-390b20426f.md#p4-s5)。N要面对P2的强答案或有理由选定的自然替代；无失败依据时改写采用/选择理由，不退回弱路线制造障碍。四式保持 H 对失败的因果解释；因果未建立时先修改事实包，不能靠换连接词完成证明。

### CH.3 根因造成的任务后果
事实包：F 可能产生 L；一旦 L 出现，它阻止 A 执行 v。可能性只落在 F→L；L→行动受阻是已建立关系。若后一关系也只是可能，需另选事实包，不能混用。
前接：具体失效；后交：为什么 R 必要。选择：1失效先行、补后果关系；2同一因果链的紧凑表达；3可能后果先行；4阻碍任务的后果先行。
1. [F] can cause [L], which prevents [A] from [v-ing].
2. [F] can produce [L] that prevents [A] from [v-ing].
3. One possible consequence of [F] is [L] that prevents [A] from [v-ing].
4. The [L] that prevents [A] from [v-ing] can result from [F].
源锚：[UVSCAN P4.S7](intro-source-maps/sj-a36437c84c.md#p4-s7)（边界例：可能不准与误报，未建立必然阻止使用者动作）；[CPscan P2.S6、P2.S8–S9、P5.S3](intro-source-maps/sj-390b20426f.md#p2-s6)（边界例：有条件的错误状态与安全后果，不是必然动作受阻）；[FirmSec P2.S3–S5](intro-source-maps/sj-0010159902.md#p2-s3)（边界例：风险继承及传播，不是已证实的动作阻断）。先检查 F→L→行动受阻每一边有依据；不能靠 can/may 制造未经支持的灾难后果。 本组的三级因果是原创条件化表达；以上为较弱关系的边界例，只有本稿另有完整链条依据时才调用。

### CH.4 将困难收束为正向能力要求
事实包：解决已述且仍成立的挑战，需要方法具备执行v的能力。v不是组件名；本组不独自证明现有方法不具备此能力。
前接：根因与后果已清楚；后交：P5 机制如何得到此能力。选择：1承接挑战；2方法要求先行；3能力先行；4把操作作焦点。
1. Addressing this challenge requires a method that can [v].
2. A method must be able to [v] to address this challenge.
3. The ability to [v] is therefore required to address this challenge.
4. What is required is a method capable of [v-ing].
源锚：[UVSCAN P5.S1–S3](intro-source-maps/sj-a36437c84c.md#p5-s1)；[MPInspector P3.S3、P3.S5–S6](intro-source-maps/sj-1f315ef889.md#p3-s3)；[JWBinder P6.S2–S4](intro-source-maps/sj-81630a3e7e.md#p6-s2)。若P2已知能力足够满足该要求，应转向采用基础，不能用this challenge使其重新变成未解问题。若前一句已完整表达 R，不必另加本句；therefore 仅在确有推导时用。

### CH.5 可选最小见证
事实包：案例 X 中条件 C 成立，因此 N 无法直接执行 v。该例确由数据、定义或已核实源支持。
前接：抽象根因；后交：从该例抽出的同一要求。选择：1例子先行；2条件先行；3自然方法先行；4提醒阅读关系。
1. For example, in [X], [C-clause], so [N] cannot directly [v].
2. In [X], because [C-clause], [N] cannot directly [v].
3. [N] cannot directly [v] in [X] because [C-clause].
4. Consider [X]: [C-clause], which prevents [N] from directly [v-ing].
源锚：[CPscan P4.S5–S6、P4.S2、P7.S5–S6](intro-source-maps/sj-390b20426f.md#p4-s5)；[Amoeba P3.S5、P4.S1、P4.E1、P4.S3–S5](intro-source-maps/sj-593cbfaf86.md#p3-s5)（表示范围的最小对照；不代表原算法不能运行）；[Diff-ID P7.E1、P7.S7–S8](intro-source-maps/sj-9042a938b2.md#p7-e1)（属性混杂的条件化形式见证；不声称实测必然失败）。不能把思维例子写成 measured；继续在方案或正文回到同例检查响应。

### CH.6 第二挑战是第一项满足后的残余
事实包：R1 即使满足，为 T 执行 v 仍需 R2。这里存在残余关系。
前接：第一要求；后交：R2 的独立根因。选择：1显式假设让步；2任务先行；3剩余操作先行；4强调满足R1不消除R2。
1. Even if [R1] is satisfied, [v-ing] for [T] still requires [R2].
2. [T] still requires [R2] for [v-ing], even if [R1] is satisfied.
3. [V-ing] for [T] still requires [R2], even if [R1] is satisfied.
4. Satisfying [R1] does not remove the requirement for [R2] when [v-ing] for [T].
源锚：[JWBinder P5.S5、P6.S3–S4](intro-source-maps/sj-81630a3e7e.md#p5-s5)；[CPscan P4.S1、P5.S1–S2、P5.S7](intro-source-maps/sj-390b20426f.md#p4-s1)；[UVSCAN P5.S1、P5.S3](intro-source-maps/sj-a36437c84c.md#p5-s1)。残余关系不证明两项都是本文新解决的问题；真实评价/辨识要求也可参与主线。v/v-ing/V-ing 是同一动作的语法形式，句首首字母大写；T 是任务或实际用途，不把已有 R1 写成完整任务已经完成。

### CH.7 第二挑战是共同任务的并行要求
事实包：T 同时需要 R1 与 R2；两者独立，没有假设先做第一项。
前接：已解释 R1；后交：R2 的独立根因。选择：1增加要求；2共同任务作主语；3两要求并列；4强调不应漏第二项。
1. In addition to [R1], [T] requires [R2].
2. [T] requires both [R1] and [R2].
3. Both [R1] and [R2] are required for [T].
4. The requirements of [T] include [R1] as well as [R2].
源锚：[MPInspector P2.S5–S6、P3.S1、P3.S5](intro-source-maps/sj-1f315ef889.md#p2-s5)；[Diff-ID P4.S6、P4.S8、P6.S1–S2](intro-source-maps/sj-9042a938b2.md#p4-s6)。与 CH.6 是不同关系，不能把 although/even if 当漂亮替换随意换入。

### CH.8 设计本身引入的额外困难
事实包：选定设计 D 引入问题 H，可能削弱能力 G。必须先介绍 D。
前接：D 已出现；后交：补偿机制及其效果。选择：1设计先行；2问题先行；3影响先行；4先承接设计再给责任。
1. [D] introduces [H], which can undermine [G].
2. The [H] introduced by [D] can undermine [G].
3. [G] can be undermined by the [H] that [D] introduces.
4. Adopting [D] introduces [H] and can consequently undermine [G].
源锚：[HashVFL P5.S1、P5.S3–S5、P8.S2–S3](intro-source-maps/sj-3419195084.md#p5-s1)；[SUB-PLAY P4.S2、P4.S5–S9](intro-source-maps/sj-52f8920eaa.md#p4-s2)；[FaceArmor P4.S1、P5.S1–S4](intro-source-maps/sj-6a7f688210.md#p4-s1)；[MPInspector P5.S13、P7.S1–S3、P8.S1–S2](intro-source-maps/sj-1f315ef889.md#p5-s13)。此组不是从应用动机直接生成的第二挑战；部署实践的风险与本文设计的代价不可混合。

<a id="section-5"></a>
## P5：整体系统、挑战响应与输入输出闭合

### M.1 In this paper，先总体任务与系统身份
事实包：本文提出 M，它是类别 K，任务是在 C 下完成 T。propose/design/develop 若对应不同完成状态，不作为随意同义词。
前接：实际任务要求或难点；后交：中心选择及组件响应。测量研究宣布入口另用M.10，propose与conduct不是同事实变体。选择：1名称先行；2任务先行；3明确系统类别身份；4类别先行。
1. In this paper, we propose [M], a [K] for [T] under [C].
2. In this paper, to perform [T] under [C], we propose a [K] called [M].
3. In this paper, we propose [M] as a [K] for performing [T] under [C].
4. In this paper, we propose a [K], [M], to perform [T] under [C].
源锚：[Diff-ID P8.S1、P8.S4](intro-source-maps/sj-9042a938b2.md#p8-s1)；[JWBinder P7.S1](intro-source-maps/sj-81630a3e7e.md#p7-s1)；[UVSCAN P7.S1–S2](intro-source-maps/sj-a36437c84c.md#p7-s1)；[MPInspector P5.S1–S2](intro-source-maps/sj-1f315ef889.md#p5-s1)。第3式适合类别身份需要明确；类别、任务与条件在四式中保持相同。

### M.2 设计动作及其目的
事实包：核心设计是动作 v，以得到能力 R。此处是设计目的/逻辑，不提前当实验结论。
前接：总体系统；后交：v 如何落实为机制。选择：1思路先行；2目标先行；3方法动作先行；4能力目标作话题。
1. Our key idea is to [v] to obtain [R].
2. To obtain [R], our approach is to [v].
3. We approach the problem by [v-ing] to obtain [R].
4. Obtaining [R] is the goal of our central design choice: [v-ing].
源锚：[JWBinder P8.S3、P9.S1、P9.S5、P9.S7、P10.S2–S3](intro-source-maps/sj-81630a3e7e.md#p8-s3)；[Diff-ID P8.S1–S3](intro-source-maps/sj-9042a938b2.md#p8-s1)；[Cert-RNN P4.S2–S4](intro-source-maps/sj-acbc08a57a.md#p4-s2)。本组说明动作和目的，不独自解释为何选择它。需要有据的选择关系时用M.9；若只给模糊组件组合，换动词不能补出理由。

### M.3 第一机制改变关系并提供所需产物
事实包：M1 将 I 转为 Z；Z 保留关系 Q，支持操作 v，从而回应已定义要求 R1。
前接：R1 或中心思路；后交：Z 的消费者/下一操作。选择：1组件先行；2输入转换先行；3产物先行；4两分句先产出再性质。
1. [M1] transforms [I] into [Z], which preserves [Q] and supports [v-ing].
2. By transforming [I] into [Z], [M1] produces an output that preserves [Q] and supports [v-ing].
3. The [Z] produced by [M1] from [I] preserves [Q] and supports [v-ing].
4. [M1] produces [Z] from [I]; the resulting output preserves [Q] and supports [v-ing].
源锚：[UVSCAN P8.S3、P8.S7–S8](intro-source-maps/sj-a36437c84c.md#p8-s3)（边界例：两路表示构造及消费，未建立单次变换的Q保持）；[JWBinder P9.S2–S5、P9.S7](intro-source-maps/sj-81630a3e7e.md#p9-s2)；[EMS P5.S3–S7、P7.S2](intro-source-maps/sj-2deb60c210.md#p5-s3)。保留 Q 的性质须来自机制/证据；不以 preserves 偷渡完备性保证。

### M.4 两组件并行、职责互补
事实包：M 使用 A 执行 v1，并使用 B 执行 v2；两者是并行职责，不暗示时间先后。
前接：两个真实要求；后交：必要的交互或总体输出。选择：1总体系统先行；2两组件先行；3两职责先行；4自然 while 并列。
1. [M] uses [A] to [v1] and [B] to [v2].
2. In [M], [A] is used to [v1], and [B] is used to [v2].
3. To [v1] and [v2], [M] uses [A] and [B], respectively.
4. Within [M], [A] performs [operation1], while [B] performs [operation2].
源锚：[FirmSec P9.S4–S5](intro-source-maps/sj-0010159902.md#p9-s4)（边界例：同一检测器的互补特征，未分配两个独立操作）；[AsgLDP P3.S2、P4.S1–S2、C2.S2](intro-source-maps/sj-dc32e376bc.md#p3-s2)（边界例：联合信息对象，不直接建立组件与操作的一一分工）；[MOCK P5.S4、P5.S6–S8](intro-source-maps/sj-177bf3c33e.md#p5-s4)。本组是系统职责分工；独立证据来源的互补需要另按各自样本和问题叙述，不能自动当作个体匹配。operation1/2 是 v1/v2 的同义名词形式；respectively 仅两端配对清楚时用。

### M.5 真正的产物传递
事实包：A 从 I 产生 Z；B 用 Z 产生 O。输入输出依赖真实，非为了行文制造流水线。
前接：A 或 I 已知；后交：O 的任务用途。选择：1产物桥接；2整个系统动作；3第二消费者先行；4强调真实先后。
1. [A] produces [Z] from [I], and [B] uses [Z] to produce [O].
2. We use [A] to obtain [Z] from [I] and then use [B] to produce [O] from [Z].
3. [B] produces [O] from the [Z] that [A] obtains from [I].
4. After [A] produces [Z] from [I], [B] uses the resulting [Z] to produce [O].
源锚：[UVSCAN P8.S1–S3、P8.S6–S8](intro-source-maps/sj-a36437c84c.md#p8-s1)；[JWBinder P9.S2–S7](intro-source-maps/sj-81630a3e7e.md#p9-s2)；[VERIFI P5.S5–S8、P6.S12](intro-source-maps/sj-1b6614ac62.md#p5-s5)。两个来源分别观察不同样本，不因此构成这里的产物传递；共享类别名称也不建立个体匹配。

### M.6 将输出交给最终判断
事实包：使用者/组件 A 使用 O 来执行任务动作 v；不增加全自动性或可利用性。
前接：方法产物 O；后交：任务能力与对应评价。选择：1输出先行；2使用者先行；3动作目的先行；4作为动作依据。
1. The resulting [O] is used by [A] to [v].
2. [A] uses the resulting [O] to [v].
3. To [v], [A] uses the [O] produced by the method.
4. The [O] produced by the method is used by [A] for [v-ing].
源锚：[JWBinder P9.S7、P10.S2–S4](intro-source-maps/sj-81630a3e7e.md#p9-s7)；[FirmSec P9.S6–S8](intro-source-maps/sj-0010159902.md#p9-s6)；[Mars P4.S7–S8、P5.S4–S5](intro-source-maps/sj-a7b06c257f.md#p4-s7)（证据报告交给人工评估；不声称机器已确认最终处置）。检测候选被人工判断就保留人在回路，不换成自动确认。

### M.7 有根据的观察或直接可核查的性质
事实包：我们在考察范围C中观察到命题P。证据可以是实验、实例、代码/系统检查；P的观察性质与范围保持相同。词义选择另见[英文惯例](english-conventions.md)与[词汇职责](realizations/lexical-roles.md)。
前接：需要某信号/关系的原因；后交：其设计用途。选择：1作者观察先行；2范围先行；3发现先行；4证据动作先行。
1. We observe that [P-clause] in [C].
2. In [C], we observe that [P-clause].
3. In our observations of [C], [P-clause].
4. Our examination of [C] reveals that [P-clause].
源锚：[Diff-ID P6.S3–S11](intro-source-maps/sj-9042a938b2.md#p6-s3)；[EMS P2.S2–S4、P2.S7–S8、P3.S1–S6](intro-source-maps/sj-2deb60c210.md#p2-s2)；[Code Rewriting Detector P5.S1–S4](intro-source-maps/sj-db9fe86207.md#p5-s1)；[Dynamic Attention P6.S1–S5](intro-source-maps/sj-64e052ffcd.md#p6-s1)。若只是提出一种设计，使用 M.2，不能用 observe。

### M.8 从观察推到设计机会，保留推断强度
事实包：已述观察 E 提示可用信号 S 来执行 v；尚不是“必然有效”的保证。
前接：E 已明确；后交：如何实际表示/读取 S。选择：1观察先行；2信号先行；3用途先行；4观察及其提示的用途先行。
1. [E] suggests that [S] could be used to [v].
2. [S] could be useful for [v-ing], as suggested by [E].
3. The potential use of [S] for [v-ing] is suggested by [E].
4. [E] points to the potential use of [S] for [v-ing].
源锚：[Diff-ID P6.S3、P6.S8–S11、P7.S1–S4](intro-source-maps/sj-9042a938b2.md#p6-s3)；[EMS P2.S3–S8、P3.S6–S9](intro-source-maps/sj-2deb60c210.md#p2-s3)；[CLIBE P6.S1–S6、P7.S1–S2](intro-source-maps/sj-74a13898b9.md#p6-s1)；[Code Rewriting P5.S2–S4、P6.S1–S2](intro-source-maps/sj-db9fe86207.md#p5-s2)。四式只表述观察所提示的可能用途，不添加作者实施/考虑行为；已证明的性质需要另一事实包，不能随便删除 could/potential。

### M.9 有根据的机制选择理由
事实包：在已建立的条件C下，D具有性质q；我们实际选用D执行v，q是该选择的有据理由。q为限定范围的谓词，不只是“执行v/更有效”的重述。本组不增加比较优势、已测收益或普遍保证。
前接：需要的操作、直接替代已提供的能力及条件C；后交：D如何形成实际产物，以及构造/分析/评价建立什么。选择：1采用动作先行；2性质先行；3明确理由；4设计选择先行。四式共享前文C，若C尚未明确，先自然补出条件。
1. We use [D] to [v] because it [q].
2. Because [D] [q], we use it to [v].
3. Our reason for using [D] to [v] is that it [q].
4. We choose [D] for [v-ing] because it [q].
源锚：[MeTFA P5.S4–S7、P6.S4–S5、P6.S11–S12、正文补读](intro-source-maps/sj-f612de4bf1.md#supplement-body-rationale)；[JWBinder P8.S1–S3、P9.S5–S7、P10.S2–S4](intro-source-maps/sj-81630a3e7e.md#p8-s1)。use/choose都指已采用的设计，v/v-ing为同一动作。若只是观察提示可能用途，用M.8；若理由缺证据，保留材料问题，because不提供证明。

### M.10 宣布本文开展并报告的经验研究
事实包：作者已开展并在本文报告针对对象/现象T、在条件或范围C下的经验研究。使用已完成论文的论述现在时，不是计划；不预设提出新方法、做了基线比较、获得代表样本或证明因果。
前接：经验问题及其可观察性/辨识关系；后交：各证据来源的作用、样本单位和必要覆盖。选择：1常规作者动作；2经验问题先行；3论文报告先行。T/C保持不变；若C为地理、时间或抽样范围，三式一致换用适合的in/on/across等介词。
1. In this paper, we conduct an empirical study of [T] under [C].
2. In this paper, we investigate [T] under [C] through an empirical study.
3. This paper presents our empirical study of [T] under [C].
源锚：[IoT Re-using P5.S1–S3、P6.S1–S10](intro-source-maps/sj-601d126363.md#p5-s1)。本组presents是报告同一研究，不是提出新系统；与M.1是内容分支而非动词同义替换。这是测量入口，不宣称已覆盖所有测量论文职责。

<a id="section-6"></a>
## 贡献：整体、技术与最终评价

先按selection-operations.md的C以研究所得分组，再用挑战中的同一能力检查语义覆盖；组件数不直接决定条目数。方法／系统最后一项先用E.0组织一条完整评价贡献：评价动作接任务层总评，再以代表性数字或实质结果具体体现主要优势；按所选内容使用E.1–E.8润色。E.2保留定量比较，但后续数字服从本条的主要评价结论，不按实验项目自动续写；E.6–E.8用于确有分量的发现、成本或分析。按研究内容决定展开与结束，不将一个合格起句当成完整贡献，也不固定追加实践意义。当前用户要求贡献条目无引用标记，以下源锚用于起草学习，不复制进条目。

### C.1 自然引入贡献列表
事实包：下面列出的项目是本文主要贡献；不承诺固定三项或每项独立发明。
前接：方法解释已完成；后交：C.2、C.3/C.4、E 组。选择：1常规总结；2列表先行；3读者导向；4简洁作者视角。
1. Our main contributions are summarized as follows.
2. The main contributions of this work are as follows.
3. This work makes the following main contributions.
4. We summarize the main contributions below.
源锚：[Diff-ID P9.S1](intro-source-maps/sj-9042a938b2.md#p9-s1)；[JWBinder P12](intro-source-maps/sj-81630a3e7e.md#p12)。仅是过渡，不计一项贡献。

### C.2 总体研究推进
事实包：本文提出 M；M 在 C 下使任务动作 v 成为可能。相应能力有本研究支持。
前接：全文主线；后交：技术为什么使该能力成立。选择：1研究产物先行；2系统主语、作者工作作插入说明；3条件先行、任务动作为被动主语；4以研究工作作主语。
1. We introduce [M], which enables [v-ing] under [C].
2. [M], which we introduce in this work, enables [v-ing] under [C].
3. Under [C], [v-ing] is enabled by [M], which we introduce in this work.
4. This work introduces [M], which enables [v-ing] under [C].
源锚：[JWBinder B1.S1](intro-source-maps/sj-81630a3e7e.md#b1-s1)；[UVSCAN B1.S1–S3](intro-source-maps/sj-a36437c84c.md#b1-s1)；[IPPO C1.S1–S3](intro-source-maps/sj-8d71597fb2.md#c1-s1)；[MPInspector C1.S1–S2、P9.S1–S2](intro-source-maps/sj-1f315ef889.md#c1-s1)。M 首次定义完整后，此处可用名称；不自动加 first/novel/end-to-end。

### C.3 值得独立列出的关键技术
事实包：本文设计 D，提供能力 R，以解决已建立障碍 H。D 已实际实现/建立相应性质。
前接：总体能力及挑战 H；后交：正文机制/分析依据。选择：1设计动作先行；2设计产物接已述障碍；3提供的能力先行；4技术产物及其因果效果先行。
1. We design [D], which addresses [H] by providing [R].
2. Our design [D] addresses [H] by providing [R].
3. By providing [R], our [D] addresses [H].
4. The [D] we design provides [R], thereby addressing [H].
源锚：[Cert-RNN B2.S1–S3、P3.S5](intro-source-maps/sj-acbc08a57a.md#b2-s1)；[CPscan C2.S1–S2、P4.S12、P5.S7](intro-source-maps/sj-390b20426f.md#c2-s1)；[JWBinder B2.S1、P7.S2、P9.S1、P10.S3](intro-source-maps/sj-81630a3e7e.md#b2-s1)；[Turbo B1.S1–S2、B2.S1、P6.S4–S5](intro-source-maps/sj-a258b38871.md#b1-s1)。若只能证明部分处理 H，四式统一使用对应窄命题，不靠 addresses 夸大。

### C.4 两项技术共同构成一个实质创新
事实包：本文将 D1 与 D2 组合，获得联合能力 R；组合关系有实质理由，不是模块凑数。
前接：两个挑战或一个联合要求；后交：正文两设计相互作用及证据。选择：1组合动作先行；2实现能力的方式先行；3组合产物作主语；4联合能力作被动主语。
1. We combine [D1] and [D2], providing [R].
2. By combining [D1] and [D2], our design provides [R].
3. Our combination of [D1] and [D2] provides [R].
4. [R] is provided by combining [D1] with [D2] in our design.
源锚：[CPscan C2.S1–S2、P4.S1、P7.S7](intro-source-maps/sj-390b20426f.md#c2-s1)；[JWBinder B2.S1、P9.S4、P9.S7](intro-source-maps/sj-81630a3e7e.md#b2-s1)；[AsgLDP P2.S4–S5、C2.S1–S3](intro-source-maps/sj-dc32e376bc.md#p2-s4)（联合对象与新／已有技术组合，不把两个对象称为两项新技术）。此项是否合并，先按创新独立性决定，不由句式决定。

### E.0 任务层总评与代表性数字共同构成评价贡献
事实包：在D中对M开展广泛实验，支持其在前文命名任务T上的主要评价性质P；已选代表性结果Q，使读者看见这些性质的实证分量。P采用实际获证的有效性、效率、鲁棒性、泛化等性质，T保持任务层对象；Q是有意义的能力水平、比较收益、重要条件下的保持或运行代价。这里四式表达同一事实包，Q中的对象、统计口径、参照与条件不随句式变化。
前接：总体与技术贡献；后交：一条完整、有总评也有实证分量的评价贡献。先定本条让读者记住的表现，再选最能体现它的结果；总评不用技术动作串代替，数字不用实验项目顺序组织。
1. We conduct extensive experiments on [D], demonstrating [P] of [M] in [T]. For example, [Q].
2. Through extensive experiments on [D], we demonstrate [P] of [M] in [T]. In particular, [Q].
3. Extensive experiments on [D] demonstrate [P] of [M] in [T]. Specifically, [Q].
4. We evaluate [M] through extensive experiments on [D], demonstrating its [P-without-article] in [T]. For instance, [Q].
P采用自然名词表达，如the effectiveness and efficiency；第4式因its已有限定作用去掉the。Q是已经选定的完整结果句，可以按实际内容合并进前句或展开成相邻结果句，不由这个两句展示形式限制实际句数。短总评已经足以完成评价职责时可直接收束；需要数字表现分量时不将“避免结果账目”误解为省去数字。
**数字怎样服务总评：**先确定它让读者知道的是优势有多大、能力达到了什么水平，还是在重要条件下仍能完成什么。对真实比较，可用相对改善直接呈现收益，保留指标、对手和解释所需的条件；原始配对值在最能解释结果时也可以保留。实测能力与开销各归自己的方法或组件，不把组件计时扩大为系统吞吐，也不把最优值改成平均值。上述取舍用于写出有分量的正文，不让核对过程占据贡献条目。
**真实源例：**[TextBugger C2.S1–S4](intro-source-maps/sj-238a78de63.md#c2-s1)先交代评价范围及有效／高效总评，再以特定黑盒平台上100%攻击成功率举例，随后保留迁移性这一独立所得；该评价项是第二项，不是列表末项。[TextShield C3.S1](intro-source-maps/sj-4ef65862d0.md#c3-s1)在最后一项的主要优势中给出74.5%的代表性攻击成功率降幅。[CAMH C3.S1–S2](intro-source-maps/sj-2ada62afcb.md#c3-s1)最后一项先说多数据／架构评价，再用四倍类别或30%数据条件下ER仍超过85%体现鲁棒性；两个压力条件用or连接，不合成同时满足。[FreeEagle P11.S1](intro-source-maps/sj-33b7f0ad03.md#p11-s1)、[HashVFL C3.S1](intro-source-maps/sj-3419195084.md#c3-s1)则以有语境的高层评价直接收束。这些都是按内容选择的正常表达，不建立数字数量或句数配额。
实现本身若有需要独立交代的研究内容，可以保留；评价项无需默认添加原型实现前缀。

### E.1 最终评价的范围与比较对象
事实包：在 D/C 上做广泛实验评价 M，并与 B 比较；比较在共同协议 P 下。若未做 extensive，先如实改全部形式，不把修辞当评价完成证明。
前接：M 与技术贡献；后交：已经选定的主要结果，也可与结果合为E.0的一句。D/C选足以理解结论的评价覆盖，P只留影响比较的条件，不填满实验设置。选择：1研究动作先行；2方法先行；3协议先行；4范围先行。
1. We conduct extensive experiments on [D] under [C], comparing [M] with [B] using [P].
2. We evaluate [M] through extensive experiments on [D] under [C] and compare it with [B] using [P].
3. Using [P], we compare [M] with [B] through extensive experiments on [D] under [C].
4. On [D] under [C], [M] is compared with [B] using [P] in extensive experiments.
源锚：[FreeEagle P7.S8–S9、P11.S1](intro-source-maps/sj-33b7f0ad03.md#p7-s8)（支撑范围与对手类别；共同协议仍需正文根据）；[UniFuzz C2.S1、C1.S4、C1.S7、P2.S5、P2.S12](intro-source-maps/sj-26271ecf21.md#c2-s1)；[V-Fuzz P7.S1–S2](intro-source-maps/sj-e0e45fc435.md#p7-s1)（支撑评价范围；引言图未给完整基线与同协议）。P 只选影响解释的公平条件；资料已交代时不用列完整实验目录。

### E.2 同指标、同范围的定量任务比较
事实包：同范围 C 中，任务指标 K，M 为 V，B 为 Vb；数值口径一致，方向按指标本身理解，不默认大为好。
前接：已选好的主要结果及其比较关系；作用：该数值差异值得读者记住时，用作结果本身或其代表性支持，不按实验项目重复套用。选择：1条件先行；2方法先行；3评价依据先行；4指标先行。
1. Under [C], [M] achieves a [K] of [V], compared with [Vb] for [B].
2. [M] achieves a [K] of [V] under [C], while [B] achieves [Vb].
3. Evaluation under [C] shows a [K] of [V] for [M] and [Vb] for [B].
4. The [K] achieved by [M] under [C] is [V], compared with [Vb] for [B].
源锚：[JWBinder P11.S3–S4、P11.S1](intro-source-maps/sj-81630a3e7e.md#p11-s3)（这是贡献前的详细成果段；其评价贡献B3.S1采用E.0的归纳句，因此这里只迁移定量比较的局部表达）；[FreeEagle P7.S8–S9、P11.S1](intro-source-maps/sj-33b7f0ad03.md#p7-s8)（定性比较边界，属于E.3；不支持本组配对数值）。K 采用 a detection rate 等自然搭配；百分比与百分点、均值与最佳值、组件与系统口径逐项保持。

### E.3 同一有界、定性比较结论
事实包：证据 E 显示 M 在范围 C 的任务 T 上胜过 B。B 的集合边界固定，例如 some 不得换成 all。
前接：比较设计；后交：必要的联合能力或结束。选择：1证据先行；2方法先行；3范围先行；4作者研究动作先行。
1. [E] shows that [M] outperforms [B] on [T] under [C].
2. [M] outperforms [B] on [T] under [C], as shown by [E].
3. Under [C], [E] shows that [M] outperforms [B] on [T].
4. Through [E], we show that [M] outperforms [B] on [T] under [C].
源锚：[FreeEagle P7.S9、P11.S1](intro-source-maps/sj-33b7f0ad03.md#p7-s9)。若不同指标有得有失，不能用总体 outperforms；先在内容层选确实成立的比较轴。

### E.4 两项并列任务能力
事实包：E 支持 M 的能力 A 与 B；两项并列，没有“新收益/旧保持”的层级。A/B 是自然能力名词，pa/pb 为同义谓词。
前接：前文成对提出的要求；后交：必要条件或结束。选择：1评价先行；2方法先行；3能力先行；4作者动作先行。
1. [E] demonstrates both [M]'s [A] and its [B].
2. [M] [pa] and [pb], as demonstrated by [E].
3. [M]'s [A] and [B] are both demonstrated by [E].
4. Through [E], we show that [M] [pa] and [pb].
源锚：[Diff-ID P9.C3.S1](intro-source-maps/sj-9042a938b2.md#p9-c3-s1)。两项各在相应设置获证不自动表示所有条件笛卡尔积都经过联合评价，也不建立独立样本的个体对应、共同分母或因果路径。

### E.5 获得新收益并保持原任务能力
事实包：E 显示 M 得到收益动作 g，并保持 U；保持程度由 U 固定，例如 baseline-level accuracy。这里只用于真实保持关系。
前接：设计会影响原任务的实际顾虑；后交：代价或结束。选择：1证据先行；2收益先行；3保持先行；4共同能力作焦点。
1. [E] shows that [M] [g] while maintaining [U].
2. [M] [g] while maintaining [U], as shown by [E].
3. While maintaining [U], [M] [g], as shown by [E].
4. [E] demonstrates [M]'s ability to [g-base] while maintaining [U].
源锚：[HashVFL P9.S1、C3.S1、P5.S5](intro-source-maps/sj-3419195084.md#p9-s1)；[Invisible-Face P8.S3、P8.S6、P11.S2](intro-source-maps/sj-2079f71014.md#p8-s3)。g/g-base 只是同一动作的限定式/原形式。不是所有and都应改while maintaining；不同样本或指标上的独立结果不能直接拼成无代价保持。

### E.6 一项有范围的实质经验发现
事实包：本研究的经验材料/测量E支持命题Q；Q的对象、证据层次、范围和力度固定。不预设补充地位、比较优势、因果或一般化。
前接：研究问题及必要范围，可直接接研究设计；后交：Q已回答任务即可结束，仍有实质关系才继续。选择：1证据先行；2作者发现先行；3结果先行。确为补充发现时可在所选形式加入further/also，保持实际主次关系，不将其当作任意同义装饰。
1. [E] shows that [Q-clause].
2. Through [E], we find that [Q-clause].
3. [Q-clause], as shown by [E].
源锚：[UniFuzz C3.S2–S3、C2.S2、C2.S4](intro-source-maps/sj-26271ecf21.md#c3-s2)；[JWBinder P11.S9](intro-source-maps/sj-81630a3e7e.md#p11-s9)（厂商之间的收益差异；内部机制分析产物另见E.8）；[EMS P3.S3–S4、P3.S6、P10.S1–S2](intro-source-maps/sj-2deb60c210.md#p3-s3)；[IoT Re-using P5.S6、P6.S14–S15、P6.S7、正文补读](intro-source-maps/sj-601d126363.md#supplement-disposal-action-findings)。风险证据的Q仍是风险，代码报告仍是代码报告，不能通过shows改成已恢复数据。已做分析但尚无实质发现用E.8。

### E.7 同口径的实际平均处理代价
事实包：M 每工作单位 W 平均耗时 t，测评输入平均大小 s。不是上界，不自动证明满足部署预算。
前接：主要任务收益；后交：若确有依据再解释采用性，也可直接结束。选择：1方法先行；2指标先行；3规模先行；4测量先行。
1. [M] takes an average of [t] to process one [W], with an average input size of [s].
2. The average processing time of [M] is [t] per [W] for inputs with an average size of [s].
3. For inputs averaging [s] in size, [M] takes [t] on average to process each [W].
4. Our measurements show an average processing time of [t] per [W] for [M], with inputs averaging [s] in size.
源锚：[JWBinder P11.S10](intro-source-maps/sj-81630a3e7e.md#p11-s10)。若成本不是当前主线必需，不为了“实用性”加一项未证预算结论。

### E.8 完成了额外分析，但不提前虚构其发现
事实包：研究评价 E 包含对对象 A 的分析；此句只交付分析产物。
前接：主效能结果或独立知识目标；后交：正文中的分析依据/结果。选择：1作者动作先行；2评价先行；3分析产物先行；4接已有评价再转分析。
1. We also provide an analysis of [A] as part of [E].
2. [E] also includes an analysis of [A].
3. An analysis of [A] is also provided as part of [E].
4. As part of [E], we also analyze [A].
源锚：[JWBinder B3.S1](intro-source-maps/sj-81630a3e7e.md#b3-s1)。若分析本身已有明确重要发现，选 E.6；不能把两个职责当同一句的同义替换。

<a id="section-7"></a>
## 采用与删并

每段按其生成程序取所需职责；没有事实或没有新信息的职责可不调用。P3/P4 共用 CH.1–CH.5，但必须各有不同真实事实包；这是复用写作程序，不是重复句子。最终评价允许 E.1 与 E.2/E.3 合句、允许 E.4/E.5 承接已有范围，也允许在研究答案完整时停止。

本库按当前基础覆盖方法/系统主路。其他体裁按[体裁基础](genre-foundation.md)与[研究选择变体](research-choice-variants.md)取材；本库不宣称为所有体裁完成同等深度的英文程序。

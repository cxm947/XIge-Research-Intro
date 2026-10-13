# 语言实现层：先锁定同一命题，再从条件选项成句

## 导航

- [L1 对象职责→实际用途](#l1)
- [L2 给定情境→必须完成的实际任务](#l2)
- [L3 承认已有能力→当前仍缺一项判断](#l3)
- [L4 因果根因→具体失败后果](#l4)
- [L5 本文总体交付＋准确任务范围](#l5)
- [L6 构造手段→任务产物，且施事一致](#l6)
- [L7 评价贡献：范围→总体任务答案→有代表性的结果](#l7)
- [L8 限定条件→可能结果，保持模态辖域](#l8)
- [L9 定义量：方向、约束、对象不变](#l9)
- [L10 机制／规律认识作为贡献](#l10)

## 1. 与内容分支的关系

[内容分支索引](../choices/index.json)的43支回答“此处应该讲什么、为什么这样推进”，不是43组语义等价句。比如“现成方法前提缺失”和“旧观察不能辨识目标属性”是不同gap，不能当作同义改写互换。

本层在选定内容分支之后工作：固定本稿命题的对象、动作、条件、因果／目的、范围、比较方向、完成状态和证据强度，再选合适的语言实现。3–8指库中提供的条件选项规模，不是每次任务的生成数量；通常每组给4种，评价组给6种，覆盖不同焦点。平时直接选一种成句；当前确需比较或用户要求备选时，再按语境与本轮要求展开有实质差异的表达。

下面英文是基于已核源句操作形成的编辑变体，不是源句逐字摘录，也不是事实例题。方括号表示固定的本稿内容；同一组四种不得偷偷换槽内含义。实际填入时根据单复数、动词形式和指代改语法，不由模板自动决定事实。某种形式改变了重要焦点或主张关系，就承认其代价；如果改变真值条件，排除，不能称保义。

源语法依据来自指定版本的实际句群：AsgLDP P4／C1／C3；FirmRCA P1／P3／P8；EMS P2；VERIFI P3；TextDefense P5；InvMM C1。它们支持有限句法和措辞操作，不证明下面每种新组合比原文好。版本及公共链接见各内容卡的来源表；此处保义边界只适用于对应操作。

## 2. 十组紧凑实现（通常4种；评价6种）

<a id="l1"></a>

### L1 对象职责→实际用途

固定命题：X执行A；正是这一动作支持B。不能从“支持”提升为“保证”。用于背景功能与具体子领域用途。

1. [X] performs [A], supporting [B].
2. By performing [A], [X] supports [B].
3. [X] supports [B] through [A in noun form].
4. [X] performs [A]. This activity supports [B].

源操作：FirmRCA P1.S1以软件对象作主句、providing后置补功能，P1.S2将用途接基础设施；AsgLDP P4.S1把方式前置、能力留主句。第2／3式是对这种焦点分配的编辑应用，不冒充源文原句。

正面措辞：用具体对象和功能动词把重要性写实，常用“provides … for …”“serves as …”“plays a role in …”。FirmRCA先说对象做什么，再说用途；选择最有下游作用的一项功能，比先放crucial／essential更容易接任务。


选择：A是首次引入时用1；上一句正问作用根据时用2；读者已知A而关心用途B时用3；A或B各自较复杂且需要独立处理时用4。第4式多一个回指；by／through只有A确是B的手段时才使用，单纯共现的两事实不能进入本组。

<a id="l2"></a>

### L2 给定情境→必须完成的实际任务

固定命题：在条件C下，主体R必须执行A，目的是G。目的不等于已实现效果。

1. Under [C], [R] must [A] to [G].
2. To [G] under [C], [R] must [A].
3. Under [C], achieving [G in noun form] requires [R] to [A].
4. Under [C], [R] must [A]. The purpose is to [G].

源操作：FirmRCA P3.S1的Given情境先行＋分析者have to；P8.S3/S6的To目的先行＋设计主句。必要性情态来自本稿任务，不是看见形式主语就允许把“有帮助”变成“必须”。

正面措辞：Given／To开头适合把已知场景或未完成目标放前；主句保留“identify the root cause”“prioritize …”“verify whether …”一类实际动作。读者首先看到要做什么，技术原因随后才有落点。


选择：情境C刚成为话题用1；目标G是前文未满足要求用2；正在解释任务为何需要一个动作时用3；目的本身需要下一句继续展开才用4。C、R、A和G始终相同，不能靠省去C让要求变普遍。

<a id="l3"></a>

### L3 承认已有能力→当前仍缺一项判断

固定命题：已有方法M在C下能做A；在同一C下它不能做B。B与A不同但相关；不存在更强或更弱能力的暗换。

1. Under [C], [M] can [A], but it cannot [B].
2. Although [M] can [A] under [C], it cannot [B] under the same conditions.
3. [M] supports [A in noun form] under [C]. Its capabilities under these conditions do not extend to [B in noun form].
4. Under [C], [B in noun form] remains beyond [M], despite its ability to [A].

源操作：EMS P2.S1的While已有效探索→主句历史复用不足；VERIFI P3.S4–5先承认传统检查再交新条件下信号不足。真实近邻材料决定cannot是否成立：若本稿仅有may fail，四句都必须换为相同可能性，不选更强谓语。

正面措辞：While／Although保留已有答案，主句用“requires …”“does not capture …”“cannot directly …”点明缺的对象或操作。已有方法可用时先用“enables”“supports”“has been applied to”说其真实能力，转折才有参照。源词组只能按本稿实际证据强度选。


选择：两个能力需并列看时用1；当前焦点是B用2；A/B各需范围解释用3；B已是上句主题用4。若缺口来自新条件C2，而能力成立于C1，必须分别显式写C1/C2，不能为短而套此“同一条件”版本。

<a id="l4"></a>

### L4 因果根因→具体失败后果

固定命题：原因C可导致失败F；情态为可能，不是必然。F已写成任务动作或判断受阻。

1. [C] may cause [F in noun form].
2. Because of [C], [F] may occur.
3. [F] may occur owing to [C].
4. A possible consequence of [C] is [F in noun form].

源操作：VERIFI P3.S5主句may hardly change、尾部owing to给原因；FirmRCA P1.S3前置Given依据、主句can lead to后果。这里cause／because／owing to只在本稿确有因果支持时等价，不把统计相关“营销化”为原因。

正面措辞：将泛泛challenging写成可见结果，如“prevents … from reaching …”“leaves … unresolved”“makes it difficult to distinguish …”。因果短语用because／owing to即可，任务动作比抽象复杂性名词更有力；如只到可能程度，may保留在相应谓语上。


选择：根因C是本段新解释用1／2；上句刚提出F、读者问为什么用3；要让后果成为后续段落对象用4。若需要的情态是“在C下必然F”，应保留必然版本，不能为了温和一律加may；若是作者假设则显式标为hypothesis。

<a id="l5"></a>

### L5 本文总体交付＋准确任务范围

固定命题：作者在本文提出X，X属于类别K，目的是在C下完成T。仅宣告设计任务，不在提出句偷加已验证优势。

1. In this paper, we propose [X], a [K] for [T in noun form] under [C].
2. We present [X] in this paper as a [K] designed to [T] under [C].
3. This paper introduces [X], a [K] designed for [T in noun form] under [C].
4. In this paper, we propose a [K], called [X], to [T] under [C].

源操作：FirmRCA P8.S1的we propose＋框架同位语；AsgLDP C1的we present＋框架＋to任务＋under条件；InvMM C1.S1的we propose＋名称＋度量同位说明。propose／present／introduces在此仅标本篇交付；不自动暗示first／novel。

正面措辞：常见而自然的入口就是“In this paper, we propose …”“We present …, a … framework for …”。名称后的同位语让读者立刻知道交付种类；随后for／to／under分别交任务、目的和条件。不必靠一串novel、effective、robust来承担介绍。


选择：名称／类别均初现用1；已有概念需准确定位其用途用2；段落主语宜为论文且无歧义用3；读者更需要先知道类别再记名用4。技术路线尚属设想时不能因为用propose就夹带已完成实验，后文状态仍须如实。

<a id="l6"></a>

### L6 构造手段→任务产物，且施事一致

固定命题：作者使用M来构造O，目的G；M是实际手段，G尚不因目的句自动成为已验证结果。

1. We construct [O] using [M] to [G].
2. To [G], we use [M] to construct [O].
3. Using [M], we construct [O] for [G in noun form].
4. We use [M] to construct [O]. This construction is intended to [G].

源操作：TextDefense P5.S6的use度量＋目的不定式，S7的To效率目的→sample动作；AsgLDP P4.S3的construct产物＋based on资料＋in order to目的。最后一种保留“意图”语义，不能若原本已验证则无端降成仅希望。

正面措辞：取真实研究操作的动宾搭配，如“collect runtime information”“estimate the joint distribution”“construct a … graph”“preserve … properties”。AsgLDP用collect→compute/estimate→construct逐步交产物；这些具体谓语本身就使方案容易理解，无需每步另写一条价值口号。


选择：O是当前要交付的新对象用1；G紧接挑战用2；M已建立、现在看产物用3；两个对象较重或目的需继续展开用4。分词Using的施事必须仍是we，不能接“The data are...”造成悬垂或改谁执行。

<a id="l7"></a>

### L7 评价贡献：范围→总体任务答案→有代表性的结果

固定命题：作者已在范围S对X做广泛实验；证据支持X在任务T中的性质Q（有效性、效率或两者，仅选实际成立者）；需要定量锚点时，代表结果R具体支撑这一任务判断。所有备选保持同一个S、T、Q、R，不能一式讲准确率、另一式偷偷改成全面实用性。

成句前，将本稿的实际取值保存为短的稿外事实记录；已有等价记录就复用：

- **S／X**：实际评价对象与设置／被评价的工作
- **T**：从前文已建立的学术任务取准确任务名、对象和必要条件，附该表述的位置；局部写作取已给定的研究定位
- **Q**：完整证据支持的X在T中的总体评价性质（如有效性、效率）及适用限定
- **R**：每项所选证据的实测对象、指标及数值或定性所得、基线及配置（如有）、条件／分母、来源位置，以及它具体支持的Q

保存后，先用同一S／X／T／Q实例化下列一种总评形式，再按各自口径接入R。记录只含选定的事实、主张和来源，不写构思过程，也不进入引言正文。

R可以说明最终任务误判减少、真实新发现、查询或运行代价降低；没有必要锚点时全组都省去R，用户明确需要数字且结果充分时每种保留同一个R。

1. We conduct extensive experiments on [S], demonstrating the [Q] of [X] in [T]. In particular, [R].
2. We extensively evaluate [X] on [S]. The results demonstrate its [Q] in [T], with [R in noun form].
3. Extensive experiments on [S] demonstrate that [X] [the same task-level capability Q in T]. A representative result is [R in noun form].
4. Through extensive experiments on [S], we demonstrate the [Q] of [X] in [T]. For example, [R].
5. We conduct an extensive evaluation of [X] on [S], showing that it [the same task-level capability Q in T]. In particular, [R].
6. Our extensive evaluation on [S] demonstrates the [Q] of [X] in [T], as illustrated by [R in noun form].

真实源习惯与编辑实现分开：

- FreeEagle C3实际用“We conduct extensive experiments on”给数据／架构范围，接“demonstrating that”直接交复杂后门检测答案及有量词边界的比较。1沿用这个工作→分词答案结构；将that命题写成“the effectiveness … in …”是可用于相同命题的编辑实现，不谎称FreeEagle逐字使用了同一句
- Tacoma C3实际用“We evaluate”定范围，再以系统为主语给比较任务表现，最后交新发现与CVE子集。2借其范围／答案的短句群分工，extensively与with结果附加是编辑选项，须按本稿信息量决定
- AsgLDP C3实际以Through理论／实验依据前置，主句we demonstrate接能力。4借其依据前置结构，只保本稿实际的实验类型；不能把源理论证明复制到新稿
- TextShield C3实际在自适应测试与工业比较后给应用答案，再用一个ASR结果具体化。这里借“总体答案后用代表结果支撑”的选择，不借源文生硬的degraded／superiority搭配，也不复制其数字
- 3、5、6是以同一命题做出的编辑整合：证据作主语、评价动作＋showing、以及评价名词作主语。它们不是新的原文摘录

积极选用：方案段直接接贡献、读者尚未知道主结果时，优先1，保留清楚的工作与任务答案，再看是否需要一句R；范围较重时用2拆开；读者已知道做了评价、此刻主要想听结论时用3或6；本段要强调证据依据时用4。5适合避免连续多项都以propose开头，同时保持学术评价动词。常用搭配是“conduct extensive experiments on”“demonstrate the effectiveness of … in …”“achieve … while maintaining …”“outperform … in terms of …”，选哪一种由已证任务答案决定，不为凑词硬加比较或双轴。

Q不应止于孤立的effectiveness：in [T]要给准确总体任务，必要R要让读者看见该能力。R通常直接写实际结果句；“A representative result is”只是比较备选时的清晰占位，最终稿可直接用X／实测对象作主语，避免元说明味。篇幅由范围、答案与证据是否已交代决定，不固定必须两句。

如果实验尚不广泛，所有备选一致去掉extensive；如果只有有效性而无效率证据，所有备选只写effectiveness。证据类型为理论／用户研究／测量时，调用对应源的评价实现，不能由本组凭空造experiments。数字对象、基线与必要条件留在R旁，而不是把全部结果表搬入末项。

<a id="l8"></a>

### L8 限定条件→可能结果，保持模态辖域

固定命题：当条件C发生时，现象P可能发生；原因是R。原因解释的是有条件的P，不是C本身。

1. [P] may occur when [C], owing to [R].
2. When [C], [P] may occur owing to [R].
3. Owing to [R], [P] may occur when [C].
4. When [C], [P] may occur. This possible outcome is due to [R].

源操作：VERIFI P3.S5原文是场景→主句指标可能不变→when少数退出→尾原因；相应编辑替代将条件前置。3／4是进一步有条件编辑实现，不冒充原句。P槽要调整为相应名词或完整谓词，实写时不保留泛泛occur外壳。

正面措辞：主句可用“may remain unchanged”“can still …”“is sensitive to …”直接给研究观察，再由when／under／owing to放紧必要条件。VERIFI的有力之处是先让读者看见预期信号可能不动；不是连接词越多越学术。


选择：打破前句期待用1；正在比较不同C用2；要解释原因R如何改变判断用3；原因需要下一句继续展开用4。第4式保留possible，避免第二句把前句可能结果写成必然事实。一般常识无需每句全填四槽，只在本句确有这四项时使用。

<a id="l9"></a>

### L9 定义量：方向、约束、对象不变

固定命题：量D定义为集合Q中对象q到固定对象p的某有方向度量d(q,p)的最小值；Q的资格条件已明确。这里所有形式只是定义，不声称算法找到了全局最优。

1. We define [D] as the minimum [d] from [q in Q] to [p].
2. [D] is defined as the minimum [d] from [q in Q] to [p].
3. The minimum [d] from [q in Q] to [p] defines [D].
4. Among [objects in Q], we take the smallest [d] to [p] as [D].

源操作：InvMM C1.S3的被动定义及noise distribution到standard Gaussian的明确方向；前句such-that给合格约束。4必须在句中保留从合格对象到p的方向，不能以between替代。

正面措辞：新度量定义常用“is defined as”“measures … by …”“takes … as input and returns …”。先定输入输出再给标量定义，读者能把数学对象接到任务；最小值、约束和方向是精确名词关系，不需再叠形容词。


选择：作者构造行动需要凸显用1；新量已是主题用2；前句刚建立优化量用3；选择域Q需要突出用4。若q/p换向或Q条件丢失，哪怕词数不变也不是保义。对于非对称量不要将“distance between”当随意同义词。

<a id="l10"></a>

### L10 机制／规律认识作为贡献

固定命题：作者识别到关系R，且它为能力C提供依据；R是有材料支持的观察／关系，不是定理级保证。

1. We identify [R], a relationship that provides a basis for [C in noun form].
2. [R], which we identify in this work, provides a basis for [C in noun form].
3. A basis for [C in noun form] is provided by [R], which we identify in this work.
4. We identify [R]. This relationship provides a basis for [C in noun form].

源操作：EMS P2.S2的we find历史含策略，S3–5以策略→分支行为→有条件用途展开；FirmRCA P8.S4的key intuition说明具体访存如何辅助逆执行。上述形式只在分析确已识别该关系时可用；如果只是intuition，应把四式都改成一致的hypothesis／observation陈述，不把灵感写成已证明发现。

正面措辞：贡献认识可以直说“We identify …”“Our key observation is that …”“This observation motivates …”。EMS将history缩为可学策略，再把策略接分支行为；熟悉的观察／启发结构能交代方法来历，内容必须是真正具体的关系。


选择：R是要记住的独立所得用1；R已在前句成为话题、现在解释其作用用2；C已是前句未满足目标用3；R本身较复杂需独立陈述用4。这里R须为明确关系名词短语，句法改变不新增analysis／experiment等证据类型。

完整词汇化演示见[三个源句选择案例](../worked-choices.md)：AsgLDP展示稳定话题与准确谓语，VERIFI展示先报观察或先报条件，Tacoma展示任务答案与代表成果。它们给3种完整句子、邻句条件和选择理由，不靠抽象名词槽位代替自然写作。

## 3. 运行映射



- A背景：先选A1–A4内容，再用L1，必要时L4表达风险
- B收窄：选接口／数据条件／工作阶段等内容，再用L1／L2／L6完成对象与操作关系
- C任务：用L2；若任务是研究问题，可采用源问题句，但先明确命题对象，不强转所有问题为must
- D近邻gap：同条件能力边界用L3；新条件改变信号用L8，分别保住两种环境
- E挑战：L2交任务，L4／L8交真正障碍；并非一段每句都套复杂从句
- F本文工作：L5
- G设计理由：L6＋必要的L4／L8；图示、反例或跨程序案例仍按其真实证据职责另写
- H非评价贡献：总体工作L5，构造L6，认识L10；资源开放状态直接平实写，不强作实验答案
- I末评价：L7；联合效用必须在固定命题里有真实共同证据，现实确认必须在固定命题里保子集关系
- J句群组织／定义：L8／L9以及各组拆合选择；根据上下文回指和焦点挑形式

这张映射是复用操作，不是“一段一模板”。写作时：先把本句真正应传达的内容说清→锁定事实与关系→从适用语言选项直接选一种成句→连读前后句。当前确需比较或用户要求备选时才展开比较。简单主谓宾够用就不加从句；记录只保留影响稿件判断的选择，不逐句生成候选大表。

现有选项不足以准确表达当前命题时，才按需读取同职责的新源句群并核实可迁移句法；不足3种本身不触发检索或补足数量。已有最佳有据表述就直接成文，不能把生成数量当完成质量证明。

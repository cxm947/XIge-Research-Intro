# DEEPSEC：六组条件化内容与成句选择

这些是编辑迁移，不是源论文的原句，也不用于替目标论文生成事实。英文示例均为原创的成句示意；方括号必须由当前稿的已核事实替换。每组先明确真实使用条件，再选事实和句式，不能把四个选项都塞进同一段。来源坐标沿用完整图，公共版本见 `source-coordinates.json`。

## B1. 在评价缺口之前，读者还缺什么前提？

源观察：P1.S4把攻防任务及约束连写，P2.S1和P4.S3明确谁要获得什么判断。编辑解释：有效的价值说明是补齐读者用来理解评价需求的前提，不是单独宣扬平台重要。

|触发条件|选入的实质内容及为何有用|原创成句示意|代价/不能这样用|
|---|---|---|---|
|B1.1 读者知道领域，却不知道谁要作什么决定|先交决策对象、候选和所需输出，让平台价值可辨认|“Model owners need to identify which available protection meets their operating requirements before deployment.”|仅当研究确实服务该采用决定；不凭空创造部署用户或声称真实部署已完成|
|B1.2 读者知道主要效果，但容易忽略合法用途|把主效果与必须保留的正常用途放在同一句，给两轴评价理由|“A useful defense must reduce adversarial errors while retaining acceptable performance on ordinary inputs.”|若两轴尚未共同测试，这是任务要求而非已达结果；不要把不同设置最优值拼到while后|
|B1.3 读者只熟悉单个分数，尚不知它遗漏什么|先交该分数不能区分的具体后果，再提出增加观察维度|“An identical success rate can conceal very different input changes and execution costs.”|需实际证据支持相同/近似分数的对照；没有证据时写成待测问题，不能当发现|
|B1.4 对象、用户、约束前文已经交清|直接从已有需求进入缺失关系，省一般背景和重复价值|“The remaining question is how these methods compare under the same operational constraints.”|要求上文的these和constraints可准确恢复；过早压缩会迫使读者猜比较对象|

选择理由：四个选项补的是不同前提，不能以四种近义开场充数。源P1.S3的行业列表不是任何新稿都必须保留的背景层。

## B2. 评价不足究竟来自哪一种可观察问题？

源观察：P2.S2–S8区分指标、对手覆盖与时效性，S10–S12给历史条件变化；P3.R1补共同设置。编辑解释：先找使用户误判的具体推断，再选择例子，而不是先写“不够全面”。

|触发条件|选入的实质内容及用户判断价值|原创成句示意|代价/所需证据|
|---|---|---|---|
|B2.1 现有指标遗漏任务必要性质|选一个分数相近而任务可用性不同的对照，说明为什么单指标不够|“The reported score does not distinguish [usable outcomes] from [outcomes that violate the task requirement].”|必须定义可用与违规的依据；不是因为能再加指标就宣称原指标无效|
|B2.2 少数对手被用作整体适用性的代理|选一个明确打破该代理关系的条件，并交真正变化的对象|“Performance against [opponent family A] leaves resistance to [family B] unresolved.”|这里是未解决关系，不等于已经证明B更强；若有包含/单调覆盖保证，应先承认它|
|B2.3 研究对象快速增加，旧比较无法继续支持选择|选择知识更新导致结论需重查的实例，再谈资源接入能力|“As new [methods] introduce different operating assumptions, earlier comparisons must be revisited.”|需点出哪些假设变了；只说领域发展迅速不能证明当前平台设计有价值|
|B2.4 已有实验结果不同，但协议也不同|先交条件差异和难以归因的关系，避免把不同结果写成纯矛盾|“The reported differences combine changes in [method] with changes in [evaluation condition], obscuring their separate effects.”|要核两类变化确实同时发生；统一实验只回答所选共同条件，未必保各方法原生最佳能力|

迁移重点：B2.2不能将P2.S6的“非必然”加强为“弱对手更强”；B2.4不能仅凭同一方法名声称两项研究互相否定。

## B3. 方案段要解释哪一种平台设计选择？

源观察：P3四条要求先于P4的系统名；§III将对象生成与评价分离。编辑解释：选入能让要求成为可执行判断的关系，才使平台免于实现清单化。

|触发条件|优先解释的设计事实|原创成句示意|代价/边界|
|---|---|---|---|
|B3.1 核心价值是让不同方法进入同一比较|交共享输入、统一记录对象和保留的方法差异|“The platform supplies [shared inputs] to each method and records [comparable outputs] through a common evaluation interface.”|若适配改变了原方法能力，要说明适配对象；只写common并不证明比较公平|
|B3.2 核心困难是效果与代价不能混在一个分数里|交独立观察渠道及它们共同支持的决定|“Separate measurements of [task effect] and [preserved utility] expose whether a gain satisfies both requirements.”|两渠道要在对应条件下连接；多指标不保证可以相加，也不自动产生综合排名|
|B3.3 资源需持续纳入新对象而不重写评价逻辑|交何种接口/数据契约可复用，明确当前验证边界|“New [methods] can reuse the evaluation pipeline by implementing [the defined interface].”|这是结构能力，不能声称未来方法都正确、有效或已测；实现/接口真实性需核|
|B3.4 主要交付是完成一项此前难做的测量研究|先交研究问题，再说明平台怎样使观察发生|“To examine [the unresolved relation], we build [the instrument] and use it to compare [the relevant cases].”|若平台独立资源价值弱，贡献可围绕认识组织；不要为沿用源的三层贡献强行拆工具项|

本组不要求新稿具备四个设计优点。源的四项要求适用于其资源目标，不能强制作者的P3/P4变成四挑战，也不能把现有两挑战填成平台功能列表。

## B4. 应把完成的工作归成哪类贡献？

源观察：C1是资源区别，C2是实际研究设计，C3是认识产出。编辑解释：贡献项应按可保留的研究所得归组，层次数量由本稿真实推进决定。

|真实完成情况|内容选择与归组|原创成句示意|代价/不能冒领的内容|
|---|---|---|---|
|B4.1 可复用资源有独立新能力|资源与能力同写，开放状态仅在已核时补短句|“We provide [resource], enabling [specific evaluation] under [the previously unsupported condition].”|实现已有方法不自动证明新能力；未开放不能写已开源，计划也不能写已提供|
|B4.2 创新在把任务要求操作化成可计算观测|交新定义/操作化对象及其判断用途，而不笼统说增加指标|“We operationalize [task property] through [measurement], allowing [a previously ambiguous distinction] to be tested.”|既有指标的复用和新指标发明要分开；必须核公式、引用及实际新关系|
|B4.3 独立价值在比较设计及由此可观察的关系|交比较单位、关键控制和所回答的问题|“We study [methods] across [conditions] to identify where their relative behavior changes.”|只运行完整矩阵但无可解释关系时，不宜声称新研究认识；数字规模只是覆盖说明|
|B4.4 工具只服务本研究，没有独立资源推进|将工具写入方法/研究设计项，贡献重点放可验证所得|“Using [the measurement procedure], we establish [the supported relation] within [the tested scope].”|不要照源人为拆为平台/实验/发现三项；若关系尚待验证，只能报计划或待解问题|

源的C2在指标来源上存在容易误读的措辞。迁移B4.2时必须按目标稿事实重核，不能把“在论文中定义了”转换为“世界首次提出”。

## B5. 末评价项第一次交结果，应选择哪一种答案？

源观察：C3选的是三种会改变判断的关系，没有用指标总数代替结论。编辑解释：先选用户要完成的判断，再找能在同一范围内证明它的证据。下列例句不报告DEEPSEC的实验事实。

|用户真正要判断什么|选证与内容选择|原创成句示意|代价/必要条件|
|---|---|---|---|
|B5.1 资源是否让本来难分的候选可辨认|选择一个解释清楚、条件可比的差别；给整体覆盖范围即可，不需最大值|“Across [the benchmark], the evaluation distinguishes methods that obtain similar [primary scores] but differ in [the task-relevant consequence].”|须证明观察确为同一决策相关的差别；不要只拿不相容条件下的列分数并排|
|B5.2 改善一个目标要付出什么代价|优先同一方法或可比设置的成对变化，明确是成功率、置信度还是别的量|“Increasing [control] raises [the verified outcome] while also increasing [the measured cost].”|两轴需同设置；源表III的CW例子不能写成MR增长，因为MR已饱和|
|B5.3 哪些条件下方法适用或失效|选影响采用的条件边界，保方法原本承诺的威胁范围|“The gains persist under [condition A] but diminish under [condition B].”|这些条件可能超出方法原设，必须标明；不能把超范围失效用来否定原范围结论|
|B5.4 组合是否改变整体表现或弱处|分别报告已核聚合与局部/最弱条件，明示统计口径|“The combination changes [aggregate measure] only modestly, while improving performance on [the verified weak cases].”|不能把部分弱例改善升为所有情形的严格下界；本源Table IX的6%例外正说明此限制|

若没有兼容的单一聚合，选择条件性认识往往比自行平均异质分数更有用。但定性不是逃避数值核查：每一半结论仍要落到源表、定义和分母。

## B6. 内容已经选定，怎样成句才能保义并改变焦点？

本组只做保义表达，不用同义句冒充新内容选项。固定命题是一个待由目标稿证实的设计描述：某评价程序对每种被测方法分别报告任务效果与正常用途保留。这里不添加优越性、首次性或实证发现。源关系来自P1.S4、P3.R3、P4.S3及§III的分开评价；下列英文是编辑示意。

|局部语境|同一命题的焦点选择及原创句|实际变化|代价|
|---|---|---|---|
|B6.1 上句已介绍程序，读者现在问它输出什么|“The evaluation reports task effectiveness and utility preservation separately for every tested method.”|已知程序作主语，两类输出落句尾；适合从方案走向评价|若separately被误读成不同设置测试，邻句须交对应条件|
|B6.2 上句已说两轴都重要，现在要突出逐方法报告|“For every tested method, the evaluation separately reports task effectiveness and utility preservation.”|比较单位前置；评价程序仍为施事，分轴报告及简单现在时均不变|若上句已明确逐方法范围，前置范围可能重复；没有新增测量活动|
|B6.3 上句讨论单一分数，需突出两个报告对象|“Task effectiveness and utility preservation are reported separately by the evaluation for every tested method.”|两类性质成为主题；被动句仍明示评价程序、被测范围及分开报告|被动式较长，适合两轴已经成为当前话题；若程序本身需要居于焦点，则用B6.1|
|B6.4 两类输出都需显著位置，且程序已是稳定话题|“For every tested method, the evaluation reports task effectiveness. It separately reports utility preservation for the same tested methods.”|拆句让两类报告各有位置；第二句仍以同一程序为施事，保同一被测范围和报告状态|增加一句及范围回指；it须明确指评价程序。本选项只改变信息展开，不额外定义指标或新增测量动作|

**不保义的改动：** 把上述任一句改为“证明效果更好”、把正常用途改成安全保障、删去被测范围、或将分别报告改成联合优化，都会增加或改变命题。需要新的研究事实，不能归为语言润色。

## 迁移用途与边界

B1–B5是内容选择，B6是固定命题后的实现。它们将“任务答案、来源范围、解释职责”落实为条件性选择，不设固定段数或句式配额。选择一个分支时应回读源的对应完整段及完整贡献集合；若源研究的证据边界与目标稿不同，以目标稿真实证据为准。

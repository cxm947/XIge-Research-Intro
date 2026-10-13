# TextDefense v1：七组有条件的选材与表达分支

所有英文都是编辑构造，含方括号者必须换成新稿实有信息；不是源论文原句，也不代表源文完成了例句中的研究。每组首先选择讲什么及先后顺序，随后才选择句法。每一分支的代价是让读者少获得哪部分信息或需要额外哪类证据，并非简单地偏好长句或短句。

## V1. 开场先交实际判断、跨域桥，还是输入操作？

来源：P1.S1–S6、P2.S3–S5，PDF p.1。源文实际选择“领域成功→跨域扰动桥→文本后果”，本组其余为编辑迁移。

### A. 实际任务决定先行
- 条件：研究材料已指明一个真实使用功能及其失败后果；读者对大领域已有基本认识
- 内容：先说明服务必须对何种输入作何种判断，随后交改变输入为何使该判断失效
- 示例：A [service] must identify [unsafe inputs] before [downstream action]. Changes to [input feature] can alter the classifier's decision while leaving [relevant content] intact.
- 篇幅选择：用两句各承接任务和失败关系，不先列广泛应用
- 收益与代价：价值立刻可见，但没有向跨领域读者解释攻击术语；下一句需补仍陌生的定义
- 不用情形：没有可信场景材料，只能臆造运营方或实际损害

### B. 熟悉输入的操作桥先行
- 条件：读者知道邻近领域的问题，却可能误以为本文输入的性质使问题不成立
- 内容：一个熟悉改动例子→本文关键差别→问题仍存在的理由/事实
- 示例：In [familiar setting], an adversary changes [basic unit]. [New input] has a different structure, yet changes to [its units] can still affect [the same kind of decision].
- 收益与代价：容易跨越认知差距，额外占一到两句；若类比并不服务后续难点，开场会显得绕远
- 不用情形：领域读者已完全熟悉该桥，或类比省略的差异会误导方法理解

### C. 变换与成功约束先行
- 条件：工作只覆盖一种具体输入变换，应用价值已在材料前文确定
- 内容：操作对象、攻击目标、必须保持的内容三者一起交代，直接进入已有应对
- 示例：The adversary changes [units] to induce [wrong output], subject to [a preservation condition]. A useful detector must therefore distinguish these changes from [legitimate variation].
- 收益与代价：迅速交出任务边界，省掉无用分类；不能由这个狭窄输入条件推出全领域覆盖

选择要点：三个不同入口各有读者条件和可省/必补信息，不是三个开头同义句。

## V2. 什么时候保留类别地图，什么时候直接抽共同过程？

来源：P2全段→P3.S2–S6→P4.S2–S4，pp.1–2。

### A. 类别影响可用答案时，先分类再比较
- 条件：各类别需要不同观测或现成修复，且这种区别会决定gap
- 内容：只列决定比较结果的维度；每类给一个最小操作解释，再说明强答案在哪类有效
- 示例：We distinguish [class A] from [class B] by [the edited unit]. [Existing response] handles [A] because it can observe [specific cue], whereas [B] preserves that cue.
- 收益与代价：已有答案的范围有可理解依据；分类占篇幅，需严格限制到后文使用的维度
- 不用情形：只有攻击名不同，作用对象和观测条件相同

### B. 类别很多但共享过程时，先抽过程再给代表实例
- 条件：已有材料证明多种实现共享同一操作关系，方法正是利用该关系
- 内容：共享操作→改变的响应→为何该响应可能迁移到不同实现；实例用于支撑而非充当主干
- 示例：Despite their different edit rules, [the evaluated procedures] all rely on [shared operation]. This operation changes [an observable relation], suggesting a common basis for [the downstream decision].
- 收益与代价：技术名不淹没洞察，跨实现价值容易理解；必须有足够材料支持共同关系，不能从一个例子直接泛化
- 不用情形：新攻击能绕开该共同步骤，或分类本身就是研究对象

### C. 只观察结果而不知道过程时，写经验区分而非共享因果
- 条件：有正常/异常样本与接口输出，但无法确认生成机制
- 内容：共同观测条件→经验响应差异→拟采用的检测策略
- 示例：Under the same [probe], [group A] and [group B] exhibit different [responses]. We use this measured contrast to construct [a detector], without assuming access to the generating procedure.
- 收益与代价：保持研究真实状态，也可有清楚任务价值；放弃“共用生成机制保证泛化”的更强解释，需要独立泛化验证

选择要点：区分“分类承担比较坐标”与“共享过程/经验关系两类依据”的选材分岔。

## V3. 正常参照要讲一个代表情况，还是两个合法机制？

来源：P5.S1–S5，p.2；必要回读§3.2，pp.4–5。本组区分源引言的简化对照和方法中更丰富的正常参照。

### A. 操作关系陌生，先解释如何观察，再给对照
- 条件：读者不知道“重要性”如何测得；分数名称不是贡献
- 内容：干预单位与预测变化→得到一组响应→比较两类输入
- 示例：We remove one [unit] at a time and record the change in [a fixed output]. The resulting response profile lets us compare [normal inputs] with [inputs of interest].
- 收益与代价：大同行可想象实验动作，省去对统计词的猜测；多花一句介绍专业读者已熟悉的步骤
- 不用情形：干预不可实际执行、类别输出取不到，或所谓重要性来自完全不同的量

### B. 正常输入有两种合法响应时，交共同判别关系
- 条件：材料显示正常输入可能由冗余证据支持，也可能依赖少数关键信息
- 内容：承认两种正常机制→指出二者与异常真正不同的关系，不将某个单词大响应当唯一异常条件
- 示例：A valid decision may rely on several redundant cues or on a few decisive ones. The distinction of interest is whether [irrelevant components] broadly control the response, rather than whether any single component matters.
- 收益与代价：读者理解更稳固的比较基础；解释比单一正常例子长，需要真实正常数据或机制支持
- 不用情形：两类正常行为只是编辑者猜想，或当前测量无法区分所称相关与无关成分

### C. 任务内只有一个足够代表的正常机制时，保持简短对照
- 条件：工作范围明确且正常参照稳定，第二种机制不影响主张
- 内容：给代表正常反应→给异常反应→解释差异与任务的关系
- 示例：For [the defined normal case], [probe] produces [response pattern]. The contrasting pattern in [the tested abnormal case] provides a signal for [the stated decision].
- 收益与代价：保留最快阅读路径；贡献与结论必须维持当前任务范围，不能靠省略正常多样性来制造普适性

选择要点：正常文本的两类情况可转成“何时扩写正常参照、何时只给操作解释”的条件化选材。

## V4. 度量名字什么时候出现，数学细节留多少？

来源：P4.S4→P5.S2–S6，p.2；§3.3，p.5。

### A. 新的是可利用关系，先关系后量尺
- 条件：指标属于常用工具，创新在响应构造或任务解释
- 内容：比较的对象和差异方向→量尺保留这项差异→用于什么判断
- 示例：The useful contrast lies in [specified response property]. We summarize that property with [a statistic] and use the resulting score to rank [the relevant inputs].
- 收益与代价：读者先知道统计量为何在此出现；需避免把常用名字暗示成它不具备的数学含义
- 不用情形：不同定义的同名量会实质改变主张，必须立即说明定义特征

### B. 新的是量尺本身，定义和理由取得主句
- 条件：度量有独立的新性质，或公式形式决定关键能力
- 内容：量尺包含哪些输入/关系→为什么这些项是需要的→证据显示它保留什么
- 示例：Our score combines [term A] with [term B] so that [required distinction] remains visible. Unlike [the relevant alternative], it preserves [the verified property] under [condition].
- 收益与代价：突出真实数学/统计贡献；引言要付出定义篇幅，不能只借一个熟悉名词做解释
- 不用情形：仅换聚合函数，没有独立必要性或证据

### C. 指标只是决策辅助，先说明输出用途
- 条件：使用者需要筛选或排序，而非理解每个统计细节；指标不是研究推进
- 内容：先明确输出是候选、排序或二元判定，再用短语交统计来源
- 示例：The procedure prioritizes [candidates] for [review], using [response-derived scores]. [A later step] then establishes [the stronger status].
- 收益与代价：直接可见任务价值；减少指标解释的同时，必须保留状态边界与决定性条件

选择要点：技术名不代替理由；三种创新所在位置影响度量出现顺序与解释预算。

## V5. 成本是独立推进、实现配角，还是一个可选择的前沿？

来源：P3.S15→P5.S6–S9，pp.1–2；Appendix A.2与F，pp.16、18。抽样动作可取主句或附属位置，其选择应与依据及证据联动。

### A. 独立资源难点，成本动作独立成句
- 条件：任务有明确查询、时延或存储约束，而新策略改变能否运行
- 内容：先交检测观察，再解释需要重复多少动作，继而交降低工作量的策略及效果证据
- 示例：Computing the full profile requires [number or order of queries]. We reduce this cost by [supported selection strategy], retaining [verified task performance] at [the specified budget].
- 收益与代价：实际可用性成为清楚所得；占用主句和评价篇幅，必须提供同一预算下的结果
- 不用情形：只是不必要的工程细节，或节省开销没有测量也无明显机制依据

### B. 仅为实现配角，将动作附着于主操作
- 条件：成本不是独立贡献，预算已满足且无需解释另一设计权衡
- 内容：主要转换保持主句；抽样成为方式短语；标定和判定仍分别可辨
- 示例：We form [the score] from [selected observations], sampling [units] to keep the computation within [known budget]. A calibration set determines the decision boundary for later inputs.
- 收益与代价：减少步骤感，焦点留在主要观察关系；抽样贡献不突出，不能后来又把它列作重要创新
- 不用情形：采样改变信号可靠性，需要读者理解权衡

### C. 不同工作点都实用，突出选择而非单一最好
- 条件：评价有可复查的性能—成本曲线，部署偏好未固定
- 内容：明确调节量、共同条件及两类用户要求，报告代表工作点
- 示例：The number of probes controls the trade-off between [detection quality] and [measured cost]. At [budget A], the method achieves [joint result A]; [budget B] supports [a different joint result] when [the deployment requirement changes].
- 收益与代价：帮助理解“怎样用”；数字与条件较多，需避免把不同数据集或协议的最好结果拼成一个点

选择要点：A/B分配抽样动作的主从焦点，C以共同条件证据支持不同工作点；选择不能只看合句是否省一句。

## V6. 评价末项选哪一种代表证据？

来源：P6全段、B2/B3；具体核验见evidence.zh.md。以下分支可组合，但每个额外结果都要回答一个尚未回答的主张。

### A. 推进是跨条件适用，选覆盖而非最大值
- 条件：主要研究问题是同一机制能否适配多种模型、数据或输入生成方式
- 内容：共同判定任务→实质变化轴→同协议下表现，挑能显示范围的代表结果
- 示例：Across [meaningfully different settings], the method supports [the task outcome], including [the setting that challenges the proposed mechanism].
- 代价与不用情形：省略峰值会少一个醒目数字；若只有一套高度相似测试，就不把数量当适用性证据

### B. 推进是可操作判定，选同一工作点的成功与误报
- 条件：使用代价主要来自误拦、漏检或复核负担，阈值需要真实选择
- 内容：任务需求或选点准则→同一阈值下的主要结果与重要代价
- 示例：At the operating point selected for [stated requirement], the detector identifies [rate] of [target cases] while flagging [rate] of [normal cases].
- 代价与不用情形：需要两项共同条件信息；只有AUC时不能编出工作点，只有一个宽泛百分比也不够

### C. 推进是对主动规避的影响，选对手代价与系统结果
- 条件：主动对手已纳入实验，防御存在可定义的对手约束与共同预算
- 内容：对手知道什么/能改什么→系统结果→成功所需代价；成本对象应与任务真实约束一致
- 示例：When the adversary knows [the defense] and is limited to [budget], [the protected system] reduces [successful violations] and raises [the cost required for those that remain].
- 代价与不用情形：需要解释预算和度量，通常比普通检测结果长；不能拿非自适应测试支持主动规避能力

### D. 推进是容易使用，选接口能力或成本结果
- 条件：主要价值是无需获得内部资料、无需新增训练或在服务预算内工作，且做过对应验证
- 内容：真实接口条件→完成的检测任务→新增资源需求，不用零辅助存储替代总成本
- 示例：Using only [available interface outputs], the method performs [the required check] with [measured additional work]. This supports [the specific integration] without requiring [the unavailable resource].
- 代价与不用情形：界面条件会占正文，但这正是可部署主张的必要内容；只有本地理想数据时不将例句写成已验证服务部署

选择要点：按任务选评价并保共同条件；为证据职责安排位置，按需要从无数字预告切换为有用工作点。

## V7. 贡献与前文重复多少，新增场景放哪里？

来源：P6→P7/B1–B3，p.2。

### A. 前文已经交完整策略，贡献压到所得
- 条件：读者已理解输入、转换、输出及理由
- 内容：稳定重现方法/概念名，只保真正新增能力和代表结论，不重走全部步骤
- 示例：We introduce [the capability], enabling [the specific task] under [the defining condition]. Evaluation establishes [the principal result].
- 收益与代价：收束有力，核心名词会必要重复；如果前文缺策略，这种压缩会暴露内容空洞

### B. 一个新增场景只承担验证扩展，在评价贡献中出现
- 条件：它不是方法成立前提，也不是引言主价值，但提供额外可用性证据
- 内容：主测试结果之后用一句交新增接口/场景及所得
- 示例：A separate test on [the concrete interface] further supports [the bounded use case] under [the interface condition].
- 收益与代价：保留有价值新证据而不打断方法解释；读者必须已有理解该场景所需的最小前提
- 不用情形：该场景决定整个研究任务，留到贡献会显得突然

### C. 新增场景就是主要价值，提前为它建桥
- 条件：没有这一部署情境，研究选择或贡献价值就不成立
- 内容：任务背景先交接口与资源要求；设计段说明如何使用可得输入；贡献只确认已经达到的结果
- 示例：The intended setting provides [outputs] but withholds [internal information]. This access pattern motivates [the chosen observation], which is later evaluated on [the actual interface].
- 收益与代价：读者从头理解设计选择，需腾出背景/设计篇幅；不能以“避免贡献重复”为由删除前面的必要前提

选择要点：方法段与贡献允许必要重复；“贡献中出现新场景”须区分可合理后置与必须前置两种内容条件，本例P6/B2提供具体定位。

## 选用后的检查

每次只选择解决当前实质断点的分支，不把全部选项串进引言。保作者已定框架、研究体裁与语言长度。检查新句是否增加了原材料没有的用户、能力、接口、数据或结论；若有，先标待核而不是用更强措辞掩盖。源例是一套历史写作材料，不是新稿的今日新颖性证明。

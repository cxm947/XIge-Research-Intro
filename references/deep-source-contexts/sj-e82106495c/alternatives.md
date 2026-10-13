# SLIME 的局部与完整段落替代表达

来源身份与读取约定：SLIME: Program-Sensitive Energy Allocation for Fuzzing；ISSTA 2022 coauthor-hosted published-format PDF, physical pp.1-13 / printed pp.365-377；https://zhexwang.github.io/papers/slime.pdf。历史必要修订及独立复读日期为2026-10-06；2026-10-07仅恢复核验与分发整理，不是新蒸馏或重新全篇审读。下文阅读与编辑分析均沿用该历史范围，未复现实验或测试写作收益。分析坐标见coordinate-crosswalk.json，不能凭同名坐标与正式原图强接。

这是源文研究命题的原创编辑示例，不是引文，不是用户新论文草稿，也没有替来源改写一个必须采用的Introduction。局部方案只比较固定命题的焦点；完整方案说明多句一起安排时增加或省去什么。必要上下文、语义成本和证据范围均列明。英文词数按空白分隔复算，非质量评分。

## 局部选择一 代理值与真实收益

固定命题：对给定程序，既定属性的好取值不保证高效生成有效测试样本。位置对应P3.S1。

A. A favorable value for a chosen seed property need not imply efficient generation of useful tests on a particular target.

B. On a particular target, seeds favored by a chosen property may still generate useful tests inefficiently.

A把属性值作主语、推断关系作谓语，强调代理为何可能不可靠；B以前置目标建立范围，种子作主语，把负结果放句尾，适合前句仍在讨论哪些种子值得预算的语境。两者都需P2已解释有效样本为新路径或崩溃，否则useful没有可检验对象。B的may仍是可能性，不能改成一律低效。不能把低效率压成样本数量少：预算不同会改变总数，两命题不等价。

## 局部选择二 能力与反馈来源

固定命题：在各目标上依据观察到的发现结果，为不同属性的种子群调整变异预算。位置对应P3.S5与P5末段的合并命题。

A. SLIME revises the mutation budgets of property-based seed groups using discovery feedback from each target program.

B. For each target program, observed discovery outcomes guide how SLIME distributes mutation effort among property-based seed groups.

A以研究产品作主语，适合方案句后的功能展开；B把反馈作语法主语，使估计依赖更显眼，适合前文已问如何判断收益。B的guide并不独自交代多轮更新，因此只有邻句已交迭代时才完整承接固定命题；否则应补说revises，不能冒称字面完全等价。两个句子都新增了P3尚未明确交出的反馈机制，若仅获P3局部润色授权，不能悄悄把这项提前；放在P5则有现成上下文。

## 局部选择三 重叠队列

固定命题：一个种子满足多个属性时，存入对应的各属性队列。位置P5.S6；保留条件成立后的确定存储关系。

A. A seed satisfying several property criteria is stored in each corresponding queue.

B. Corresponding property queues share a seed whenever it satisfies their respective criteria.

A以满足多个标准的种子作主语，存储关系作谓语，接在种子归组之后自然；B以对应队列作主语、共享种子作谓语，适合下一句立即对队列估计奖励。A把逐队列存储写得更直接；B强调共享关系，但要求前文已交代每个队列对应一个属性。两者保留满足多个属性后的确定存储，不再用may把它弱化为仅有可能重叠。若只说seeds are grouped，语义就少了一项；若说每个种子总进多个队列，则又丢掉条件。

## 局部选择四 奖励依据

固定命题：依据各队列迄今发现的新路径和崩溃，估计其后续收益。位置P5.S7；算法名已在邻句明确。

A. SLIME estimates a queue's future yield from the new paths and crashes obtained through that queue so far.

B. Past path and crash discoveries guide SLIME's estimate of each property queue's prospective reward.

A研究产品作主语，并将队列层过去记录写得完整；B反馈作主语，压缩对象关系，信息焦点由执行者移到证据。但B省略new及按队列对应的明示，因此仅在上一句已经固定新发现且解释逐队列记录时可保持整体语义；脱离上下文不能叫无损同义句。若尚未介绍UCB-V，这两句还缺方法身份；此时把算法名另加一句是信息补全，不是长度相同的同义替换。

## 局部选择五 强结果的分母与焦点

共同命题：在九程序、每工具20次120小时运行合并去重后，SLIME发现231项，MOpt187项，前者多44项，约23.5%。ASan去重规则已经解释。

A. Across the nine programs, SLIME's pooled findings totaled 231 vulnerabilities, exceeding MOpt's 187 by 44.

B. Relative to MOpt, SLIME increased the pooled vulnerability count by approximately 23.5%, from 187 to 231 across nine programs.

A把绝对产物前置，适合读者需要判断增量规模；B把最强基线作参照，突出相对改进。数字命题相同，B以更多数字换来完整分母与幅度；若前句未给共同运行预算及ASan定义，两句都不独立充分。这里约23.5%来自表3算术，不是新的效果试验。不能改成each trial、per hour、energy saved。替换P6原六基线向量时，这两句都会减少其他比较的信息，因此是选证变化，不是整段严格保义压缩。

## 局部选择六 贡献中的动作与所得

固定命题：案例表明既定属性受偏好的种子并不在不同目标上恒定高效；不是只说做过一次案例。

A. Our case study shows that seeds favored by existing property rules are not consistently efficient across target programs.

B. Seeds favored by existing property rules can vary in efficiency across targets, as demonstrated by our case study.

A以案例作主语，让证据引出发现，适合贡献列表；B直接把被发现关系放主句，用句尾说明依据，适合前文已经讨论实验。B的vary比not consistently efficient稍弱：差异并不必然意味着某处低效，因此B若单独取代A属于缩窄表达，不标为完全保义。若要保持A的强度，可将B主句改为“Seeds favored by existing property rules need not remain efficient across targets”，但需前文已建立某目标上的高效状态。此例特意展示常见看似同义、实有语义代价的改写。

## 完整方案一 保留机制关系的方案段

适用上下文：P1–P4已经给出发现任务、固定属性偏好问题、候选及更新及选择三个挑战。下面沿P5范围重组，明确属于编辑替代；从正文加入反馈描述的可理解性，不给出实现步骤或公式。

We present SLIME, which allocates mutation effort according to the discovery yield of seed properties on each target program. Its 17 example properties span three aspects of seed diversity, providing candidate groups whose usefulness can differ across targets. An iterative process mutates seeds from the original queue, assesses their properties, and refreshes the corresponding property queues. Membership can overlap: a seed meeting several property criteria belongs to several queues. A customized UCB-V estimator uses each queue's accumulated path and crash discoveries to assess its prospective reward. SLIME then selects queues using those estimates and mutates their members, tying budget allocation to feedback from the target.

六句各自回答交付、候选来源、循环维护、重叠、收益估计、动作回收。它把原P5.S3与S4–S5的框架及步骤压到一个句群，保留多对多与反馈来源；没有逐一解释三个属性视角或UCB-V全名，要求定义在邻文或正文可查。第二句的候选收益可以跨目标不同，是前文动机的重复桥，篇幅略多但让候选与主张关系更直观。句中评估与更新概括源文框架，不替代§3.1的三个阶段，也不新增总预算最优保证。

若受众已熟悉fuzzing，可换成下列两句短版：

SLIME maintains overlapping groups of seeds defined by 17 properties and updates their membership as fuzzing proceeds. Using UCB-V estimates derived from each group's path and crash discoveries, it selects groups for further mutation according to their observed value on the target program.

短版不保留全部内容：删掉三个视角、原队列、属性评估动作及SLIME的首次呈现。它只适合方案已定义后的一段机制回顾，不能无条件替换完整P5，也不能充当独立Introduction开场。它仍保留重叠、时间更新、反馈、选择和变异，因为缺一项会破坏本段最关键的机制关系。短不是自动更好；短版需要前文替它承担被删的解释。

## 完整方案二 任务答案优先的评价条目

适用上下文：前面的方案和贡献已经说明系统，当前只写末项评价。这里主动从正文提取代表性结果，且改变原B3没有具体数字的选择。与原P6和B3合用时应避免完整重复，而不是机械插入。

We evaluate the MOpt-based prototype against six fuzzers on nine programs, pooling ASan-deduplicated findings from twenty 120-hour runs per configuration. SLIME finds 231 vulnerabilities, compared with 187 for MOpt, and has the highest pooled count on every tested program. Its mean edge coverage leads on six programs and ties all baselines on one. Separate FuzzBench experiments and matches to 25 published CVEs provide additional coverage and known-vulnerability evidence, while component comparisons examine the roles of reward-guided selection and seed replacement.

第一句给实现、比较和共同预算；第二句直接交完成发现任务的强答案，不把全九程序的合并结果弱化成有时有效；第三句将覆盖正确限定为6个第一和1个并列；第四句用证据种类而非又一串幅度交代标准基准、已知漏洞及两个组件。这里没有说FuzzBench每目标都赢，也没有将25项已公布CVE变成新发现CVE。正文仍需交代FuzzBench独立运行设置及region指标；不必把它们塞到同一个第一句预算里。

长度代价是真实的：为了让这个条目独立读懂，必须新增原B3没有的预算、去重、绝对值及覆盖范围；它不一定比原85词条目短。若P6已紧邻给了范围、预算和231/187，可以使用更短的承接版：

The evaluation establishes a vulnerability-discovery advantage across the tested programs, alongside coverage gains on most targets. FuzzBench supplies a separate coverage benchmark, published CVE matches check known-vulnerability discovery, and component comparisons assess the two main design additions.

该承接版只保任务结论和互补证据责任，不能独立承担分母与范围；其中两个设计增量必须在邻句明确指奖励引导选择与种子替换，不能泛指17属性或全部结构。它也不宣称所有组件被完全因果隔离。此版能缩短，是因为信息已在上下文真实存在，不是因为少写证据就更学术。

## 篇级使用而非强制模板

完整原Intro是任务流程→种子效率差异与近邻→跨程序失配及案例→三职责→方案→实现和结果预览→四项贡献。可选重组是把P6的具体结果并入评价贡献，保留实现载体的必要定位，并将开源状态并入方案贡献尾部。这会减少重复，但同时降低结果的第一次出现速度，并可能让末项更长；它也改变原四项贡献的独立资源地位。选择前应看新稿已有解释、资源的重要性与读者预期，不从本篇抽出“所有引言必须只报一个数”或“都必须四项贡献”的规则。

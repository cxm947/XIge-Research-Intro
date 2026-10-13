# AsgLDP：可选内容与保义形式分开

下面英文均为原创局部编辑示例，不是论文原句、全文重构或可直接作为研究证据的引文。每组共享事实时只换焦点/句法；改变内容选择时明确指出。源文的历史首次性和形式保证不在这些例子里被重新认证。只在真实稿件需要相应关系时选一种，不要求把所有备选拼起来。

## A 同一个联合任务，四种入口

1–3 的共同命题为框架已提供的合成能力：产物同时带有节点属性与连接信息，本地报告提供输入；4 明确改成任务要求。这里保任务对象和输入组织，不额外声称 node-LDP 或保真率。适用于前文已经解释局部扰动与保护定义之后。

1. “The framework synthesizes social networks with both connections and node attributes from users’ local reports.”
   焦点在任务产物；末尾才交输入来源。适合读者还缺“究竟生成什么”。
2. “Using locally produced reports, the framework constructs social networks with both relational and attribute information.”
   同一命题，前置输入；适合前文正在讨论数据可见性，需让旧信息在句首衔接。
3. “Users provide local reports from which the framework synthesizes a network containing connections and node attributes.”
   同一命题，施事先行；适合读者可能把去中心误解为没有任何汇总者。没有声称每条报告包含原始全部数据。
4. “Network synthesis in this setting draws on users’ local reports and must account for connections together with node attributes.”
   同一任务要求，焦点从一个已完成框架移到问题定义。此式改变完成状态的呈现：作为任务定义使用，不替代已完成成果句。

## B 同一个信息接口，四种主次安排

共同命题：方法先从扰动报告估计统计量，再用这些统计量构造初始图，之后优化。英文故意不让“无偏”修饰所有统计量；若正文需陈述无偏性质，应对准具体对象另写。不是原引言句法再现。

1. “Statistics estimated from perturbed reports provide the starting point for graph construction and subsequent refinement.”
   焦点在接口，用一个名词性主语压缩流程；适合步骤已在前文介绍。
2. “The framework estimates statistics from perturbed reports, builds an initial graph from those estimates, and then refines the graph.”
   同事实，动作链显式；适合首次介绍整体过程。
3. “An initial graph is built from the estimated statistics and refined afterwards; those statistics are obtained from perturbed user reports.”
   同事实，输出先行再回填来源；仅当前文正在问生成图怎么来的时有用，默认顺序不如 2 自然。
4. “Perturbed user reports are converted into statistical estimates that guide both initial graph construction and later refinement.”
   同事实，更紧凑地突出数据转换；若后续优化还依赖其他信息，须在实际稿件保其来源，不应暗示这些统计量是唯一输入。

这里“初始”“之后”只是相对步骤，不是效果证据。若目标文章的真实接口不同，先改内容，不能仅替换技术名。

## C 同一个归属关系，四种形式

共同命题：Random Jump 是文中新提出的部分，随机化属性列表属于采用的相关思路；二者承担不同采集对象。这组用于解释设计归属，不写该论文全部贡献。

1. “The collection stage introduces Random Jump for node degrees and uses randomized attribute lists for attribute data.”
   并列动作清楚分配新/沿用，适合技术贡献句。
2. “A new degree-collection component, Random Jump, is paired with randomized attribute lists for the attributes.”
   同一事实，先突出新组件；适合前文已经说明被采用的属性路径。
3. “For degree collection, the design adds Random Jump; attribute collection relies on randomized lists.”
   同一事实，用分句避免两个名词被误读为同等新颖性。
4. “The contribution at the collection stage lies in Random Jump for degrees, alongside the use of randomized lists for attributes.”
   同一局部归属，突出当前讨论层级；仅当“贡献”明确限定为这一采集设计时用，不宣称整篇贡献仅此一项。

## D 同一受证数值比较，四种焦点

共同事实只取 Table II 的 ε = 0.1 行：AsgLDP 的平均 Hellinger 距离 0.0603，比较方法该行最小值 0.0760。对象是属性分布距离，越低越接近；不是预测准确率，也不是跨预算最优性。以下全部保留比较窗口，可用于说明定性结论之后的一个见证。

1. “At ε = 0.1, the reported mean Hellinger distance for attribute distributions is 0.0603 with AsgLDP, compared with 0.0760 for the strongest baseline in that row.”
   同一结果，条件先行；读者先看见共同预算，再读改善。
2. “AsgLDP yields a mean attribute-distribution Hellinger distance of 0.0603 at ε = 0.1; the lowest baseline value at that budget is 0.0760.”
   同一结果，方法先行；用两分句清楚分配数值，避免把最佳比较项写成平均比较项。
3. “For the ε = 0.1 setting, Table II reports lower mean attribute-distribution error for AsgLDP: a Hellinger distance of 0.0603 versus the baselines’ minimum of 0.0760.”
   同一结果，先给可解释的比较方向，再给度量；表号只适合论文讨论或分析文，不是必须搬入引言的协议细节。
4. “The smallest reported baseline mean Hellinger distance at ε = 0.1 is 0.0760, while AsgLDP reaches 0.0603 on the attribute-distribution measure.”
   同一结果，从强近邻先行；适合前句刚结束比较方法说明。

“在低预算下仍有较小误差”可以增强任务意义，但要说明低的参照。本表扫描中 0.1 是最小预算，故可称本表最严格的设置；不能把它变成任意隐私定义下最强保证。这里不额外加入随机种子、实现环境或全表数据，因为它们不改变这句话的比较关系。

## E 最后一项贡献的三种内容选择，不能称为保义替换

1. 多轴任务答案：选结构、属性以及联合下游性质的定性结果，重在读者判断整项产物是否有用。适用于多个不可互换的任务轴都构成核心承诺。需按真实评价范围表述，不能暗示每个条件都全胜。
2. 多轴答案＋一个有意义的工作点：保留总体覆盖，再用 D 组那样的受证比较解释一个核心效用。增加了具体证据与预算条件，信息多于 1；适合前文已让读者关心严格设置下还能保留多少效用。
3. 采用能力＋对应任务结果：当可组合接口是独立价值时，先说实际验证的组合范围，再给生成产物的任务表现。它选择了另一个新增答案，不可拿“可组合”替换未报告的效用。

三种选择都允许自然长短变化。选择 1 不代表反对数值，选择 2 不代表必须只有一个数，选择 3 也不授权给出未测量的实施成本。先选读者缺的事实，再决定主句、从句与句数。

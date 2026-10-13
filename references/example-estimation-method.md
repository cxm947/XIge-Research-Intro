# 估计方法例：公交换乘概率预测的完整引言

## 内容导航

- [示范身份与使用范围](#示范身份与使用范围)
- [固定材料](#固定材料)
- [完整起草稿](#完整起草稿)
- [完整重写稿](#完整重写稿)
- [P/S 写作决策：每句为什么出现在这里](#ps-写作决策每句为什么出现在这里)
- [同一段的生成过程：从事实到自然正文](#同一段的生成过程从事实到自然正文)
- [哪些内容留在稿外](#哪些内容留在稿外)
- [保义复核](#保义复核)


## 示范身份与使用范围

本例是城市公交换乘失接概率预测的估计方法研究，是原创合成题材；不作为纯测量或现象研究的示范。研究、数据、方法、比较与数字均为教学设定，没有声称它们是实际已发表研究或用户项目结果，也没有完成该领域查新。它只用来展示跨学科逻辑如何增强常规引言的段句写作；真实论文必须把比较对象换为实际读过的最近工作，并使用自己的方法与结果。

本文本依附常规的任务与价值、现状与不足、困难和洞察、方案概述、结果预告、贡献总结。示范使用六段只是因为当前材料适合这样展开。若本稿已选择不同但合理的常规骨架，应把这些写作动作放入相应位置，不为复现本例改写成六段。

下文先给固定材料，再给同材料的完整起草稿与完整重写稿，最后解释 P/S 决策。所有来源资格、语义对照和待验证事项均在教学说明中，完整引言本身保持作者口吻。

## 固定材料

### 任务与研究范围

- 研究预测未来一周内某个已排定换乘组合的失接率，帮助规划者识别值得进一步检查的接续安排；不声称已经改善乘客旅程或决定最佳改表方案
- 一项换乘机会包含到达服务的实际到达时间 a、连接服务的实际发车时间 d 和事先给定的步行时间要求 w；当 a + w > d 时记为失接
- 有符号换乘余量定义为 m = a + w − d；m > 0 对应失接。该定义的“正值是不利方向”在全文保持一致
- 评价期间固定时刻表、既有等候政策和步行时间要求；本研究不预测改变时刻表或等候政策后的反事实结果
- 两项服务可能同时受到共同干扰，其延迟因而存在依赖；各换乘组合的同步观测数量有限

### 合成参照与技术依据

- 边缘估计器分别拟合到达与发车延迟，再按独立假设合成失接概率
- 联合高斯估计器保留协方差，并通过共享参数缓解样本不足，但仍使用联合高斯分布；它是本例比独立模型更强的参照
- 合成数据包含贴近 m = 0 边界的非椭圆集中模式；给定的联合高斯族无法完整表达这些模式。该事实不能移植为真实交通文献的整体不足
- 单独为每项接续拟合灵活的二维联合分布需要大量同步观测。对当前固定任务而言，结果只由一维余量的符号决定，产生同一余量的延迟组合无需被分别重建
- 本研究开发直接拟合余量分布的分层估计器，在可比运行条件间共享统计信息，同时保留各接续的局部分布。分布正半轴上的概率质量作为失接概率输出
- 运行条件分组在测试前确定；“可比”依本合成研究的固定站点与运行时段规则，不是结果出来后挑选有利分组

### 已完成的合成评价

- 数据覆盖12个枢纽、180个固定换乘组合和18周；每个枢纽15个组合。前10周训练，随后4周校准，最后4周测试，形成720个未参与拟合的“换乘组合—周”评价单位
- 三种估计器使用相同观测、信息条件、训练/校准/测试时段；均按下一周预测和实际观察的失接率进行比较
- 指标为各评价单位预测概率与观察失接率之绝对差的均值。本文方法为0.04，边缘估计器为0.11，联合高斯估计器为0.07
- 配对破坏对照仅在训练与校准资料中，将同一接续、同一预定运行条件组内的到达与发车记录打乱配对。各组的边缘记录不变；其余拟合和评价流程不变；最终仍在原始、未打乱的测试机会中评价。该版本误差为0.10
- 此对照支持“保留观察到的到达—发车配对关系对本评价中的预测性能有贡献”，不支持“所有性能差异均由一个组件造成”，也不识别真实交通延迟的全部生成机制
- 本例未设显著性检验、置信区间、跨城市测试、已部署收益、数据公开或优先性结论，正文不添加这些内容

## 完整起草稿

这是一篇已有实质材料但研究重心与句间联系较弱的起草稿。这里保留该起草稿原文，以展示它如何在后半部分把主线移向强近邻已认可的配对价值；完整重写稿修复这一重心。它没有故意掺入虚假科学事实。保义改写的基准是上面的材料，而不是把起草稿中的空泛评价或全部细节都当成必须在intro保留的信息。

Public transport is important for urban mobility. Transfer prediction is a useful research problem. A transfer is missed if an arriving bus reaches a hub too late for a passenger to walk to the connecting service before departure. The task in this paper is to predict next-week missed-connection rates for scheduled connections. These predictions can help planners identify connections that need closer attention.

Marginal estimators use the distributions of arrival and departure delays and assume independence. The two services may experience a common disruption. Their delays are then dependent. Joint-Gaussian estimators include covariance and can share parameters across connections. They assume a joint-Gaussian distribution. This distribution cannot represent all nonelliptical concentrations near the boundary between successful and missed transfers. Flexible joint estimation also needs many synchronized observations for each connection.

There are limited observations for individual connections. The transfer margin is the arrival time plus the required walking time minus the connecting departure time. Positive margins mean missed transfers. The timetable and the walking-time requirement are fixed here. Estimating the margin distribution does not require separate reconstruction of delay combinations with the same margin. We use this observation in the proposed method.

The proposed method is a hierarchical estimator. It processes records of arrivals and departures. Records for a connection are aligned, and transfer margins are computed. The margin distributions share information across comparable operating conditions. Separate local distributions are retained for each connection. The predicted rate is the probability that the margin is positive.

The data contain 180 scheduled connections at 12 hubs over 18 weeks. The last four weeks provide 720 held-out connection-weeks. Mean absolute probability errors are 0.04 for the proposed estimator, 0.11 for the marginal estimator, and 0.07 for the joint-Gaussian estimator. The methods use the same observation windows and information. Training and calibration pairs are shuffled within each connection and operating-condition group in a controlled comparison. The marginal observations are retained. The shuffled estimator has an error of 0.10 on the original held-out test data. Preserving the observed pairing contributes to forecast accuracy in this evaluation.

We develop a formulation based on transfer margins and a hierarchical method for estimating their distributions. We also evaluate the estimators and study the role of arrival–departure dependence in missed-connection forecasts. The study provides a method and an empirical comparison for the evaluated network.

## 完整重写稿

下面六段构成一篇连续可读的合成引言。它们没有将教学分析、证据台账或审稿诊断混入作者正文。

A bus journey with a transfer succeeds only if the second service remains catchable after the first arrives. Planners need the probability of a missed connection to identify timetable links that warrant closer attention. Estimating this probability requires relating the arrival of one service to the departure of another, accounting for the time needed to walk between them.

Marginal estimators model arrival and departure delays separately and combine them under independence. This approximation loses the dependence created when both services encounter the same disruption. A joint-Gaussian estimator retains their covariance and shares parameters across connections, but its elliptical distribution cannot capture the nonelliptical concentration of observations near the missed-transfer boundary in the setting studied here. The remaining problem is to estimate the probability of crossing that boundary with limited observations for each scheduled connection.

Fitting a flexible joint delay distribution separately for every connection would require more synchronized observations than many connections provide. Yet the planning question depends on a single signed quantity, the arrival time plus walking time minus the connecting departure time. A transfer is missed when this margin is positive. For the fixed timetable and walking-time requirement considered here, modeling the margin directly removes the need to reconstruct delay combinations that yield the same margin.

We develop a hierarchical estimator of transfer-margin distributions. It aligns recorded arrivals and departures for each scheduled connection and computes the margin using the required walking time. The estimator shares information across comparable operating conditions while retaining a separate distribution for each connection. The probability mass above zero then gives the predicted missed-connection rate for the following week.

We evaluate the estimator on 180 scheduled connections at 12 hubs, using the last four weeks of an 18-week record as held-out data. All three estimators receive the same observations and information and use identical training, calibration, and test windows. Across the resulting 720 connection-weeks, our estimator achieves a mean absolute probability error of 0.04, compared with 0.07 for the covariance-aware joint-Gaussian estimator and 0.11 for the independence-based marginal estimator. The proposed estimator thus improves missed-connection forecasts over an alternative that already models covariance and shares parameters across connections.

This work contributes a transfer-margin formulation and a hierarchical estimator for missed-connection probabilities under limited per-connection data. A matched evaluation demonstrates lower forecast error than both the covariance-aware joint-Gaussian and independence-based marginal alternatives in the studied network.

## P/S 写作决策：每句为什么出现在这里

这一部分是作者教学说明，不是论文正文。段号、句号只用于说明以上稿件怎样生成。

### P1：任务与价值

- **S1从实际任务关系开篇。** 读者先看到一趟旅程为什么受两个服务的相对时刻约束。它提供后续名词所需的情境，无须先泛谈全球交通规模。句中的 only if 确定必要条件，不能为改短而换成 if
- **S2选定能被本研究兑现的价值。** 预测支持识别需要关注的接续，不把尚未开展的改表优化或部署收益写成成果。作用来自价值选择与论证范围共同约束
- **S3将价值落到可比较的学术任务。** 两类事件与步行时间要求一起进入，此后读者能够理解独立假设为何相关。S3的 arrival/departure 成为 P2S1 的可识别起点

如果面向已熟悉接续可靠性的读者，可压缩 S1 与 S2；如果不熟悉失接定义，则保持关系性铺垫。此处没有“每篇至少两句背景”的要求。

### P2：已有解法与剩余问题

- **S1先交代参照在做什么。** “分别建模再按独立性合成”同时解释其能力和假设，不从评价词入手
- **S2解释为什么假设与任务冲突。** common disruption 是具体关系。原稿中的“可能共同受干扰—因而有依赖”收拢成一个可追踪判断；这不是仅增加 however
- **S3主动纳入更强近邻。** retains covariance 和 shares parameters 同时保留其依赖建模与样本共享能力；后半句将剩余不足限定到分布族和本研究设定。主结果必须与这个近邻比较，不能再把“配对信息有用”当作本文独有的回答
- **S4输出后续要回答的精确任务。** boundary-crossing probability 接续 S3；limited observations 引出 P3 的自然替代路线为什么困难。P5据此回答有限观测下的估计精度问题，而不把主题转成依赖是否存在

如果真实近邻已经能够稳定估计同一尾部概率，P2必须改写研究定位。不能单凭这个模板宣称真实 gap。

### P3：必要困难与可行洞察

- **S1把一个直接解法放到任务条件下看。** 灵活联合拟合是读者合理会想到的选择；同步样本要求解释它为何不能直接解决。它是在解释困难，不重复 gap
- **S2给出任务所需的更小对象。** 这里允许较长的定义句，因为缺少它，读者无法判断洞察。单一有符号量承担的是任务等价关系，没有声称新信息论定理
- **S3让量与结果的关系可检查。** positive 对应 missed，之后的零阈值输出不再需要重新解释
- **S4把洞察转成允许的建模选择。** 固定任务条件附着在该等价关系上；“省去哪些重建”说明这条关系做了什么。此处不抢先声称精度提高

这四句组合了认知前提、论证根据、概念压缩与自然句法。读者没有被要求先记忆复杂新术语，然后才获知用途。

### P4：完整方案概述

- **S1正常说明作者开发了什么。** 这是标准方法总述，不因上一段已经讲洞察而省略
- **S2用动词解释输入如何变成关键表示。** aligns、computes 让操作可追踪，且与方案中的真实数据身份一致
- **S3说明处理稀疏样本的关键选择。** sharing 回答 P3S1；retaining separate distributions 保留局部差异。while 覆盖同一设计中的两个同时要求，不制造对立口号
- **S4说明输出是什么。** 概率正半轴直接回接 P3S3，for the following week 回接任务的预测时间，不遗漏方案实际交付给读者的对象

若论文主要贡献是理论，这一职责改为关键构造与命题概述；不能套用本例的事件处理流程。

### P5：正面回答强近邻之后的估计问题

- **S1建立评价对象和时间身份。** 180个接续、12个枢纽与18周资料中的最后4周测试，使held-out范围可理解；具体划分仍可在方法中展开
- **S2使比较的信息条件可见。** 三种估计器使用相同观测、信息和训练/校准/测试时段。边缘估计器是否使用依赖由其方法假设决定，不能把少给它数据当作比较优势
- **S3优先报告0.04对0.07。** 联合高斯近邻已建模协方差并共享参数，因此这一比较直接回答P2留下的估计问题。0.11随后提供独立假设参照。三项数字仍是概率误差，没有改成失接率或准确率
- **S4解释主要比较的研究意义。** 本文整体估计器在一个已经利用协方差、共享参数的替代方法上取得更低误差。此句没有把差异唯一归因于一维表示、共享机制或某一具体分布选择

配对破坏结果0.10及其shuffle流程完整保留在事实卡，供方法/结果中的次级分析使用，本例intro省略。它能说明配对记录对这个估计器的预测有贡献，但不能独立证明本文相对协方差近邻的新意。将辅助对照移出引言是内容职责分配，不是删除不利证据或改变研究事实。

### P6：以估计方法及匹配比较所得收束

- **S1直接交付连贯的研究成果。** transfer-margin formulation与hierarchical estimator共同回应边界概率估计和有限数据问题，不为凑数量将它们强制分成两项，也不另封“配对有用”为新发现
- **S2用匹配比较说明成果达到什么程度。** 更低误差的比较对象同时包含协方差近邻和独立模型，范围是所研究网络；没有添加唯一模块归因、首次性、跨城市规律或部署收益

该例采用两句自然总结，不设置固定贡献数量。方法、关键设计、实现与评价或重要发现也可按研究重点分列为常规贡献；本例没有据此禁止列表或平行句。研究类型定位为估计方法，评价支持其成果，不单独伪装成纯测量发现。

## 同一段的生成过程：从事实到自然正文

以下仅将 P3—P4 连起来演示起草中的三个决策。最终成稿即上文版本，不交给读者三套备选以代替选择。

**第一步，先生成真实研究关系。**

> Each connection provides limited paired observations. A flexible joint model needs enough observations to recover the arrival–departure distribution. Missing the transfer depends only on whether arrival time plus walking time exceeds departure time. We estimate the distribution of that difference and share information across comparable conditions.

这一稿已经有必要事实和动作，但各句像笔记；仍需交代缩减对象为什么合理、共享后是否丢失局部差异。

**第二步，让困难、洞察和设计相接。**

> Estimating a flexible joint delay distribution for every connection requires more synchronized observations than many connections provide. The transfer outcome depends on the sign of the arrival time plus walking time minus departure time, so we model this signed margin directly. Our hierarchical estimator shares observations across comparable conditions while retaining a local margin distribution for each connection. Its mass above zero gives the predicted missed-connection rate.

这一稿已形成连续解释。这里“shares observations”容易被理解为直接混合原始观测，超过固定材料中的“共享统计信息”；最终稿将它改回 shares information。修改对象是科学含义，不是词频。

**第三步，按常规职责分段并校准技术含义。**

> Fitting a flexible joint delay distribution separately for every connection would require more synchronized observations than many connections provide. Yet the planning question depends on a single signed quantity, the arrival time plus walking time minus the connecting departure time. A transfer is missed when this margin is positive. For the fixed timetable and walking-time requirement considered here, modeling the margin directly removes the need to reconstruct delay combinations that yield the same margin.
>
> We develop a hierarchical estimator of transfer-margin distributions. It aligns recorded arrivals and departures for each scheduled connection and computes the margin using the required walking time. The estimator shares information across comparable operating conditions while retaining a separate distribution for each connection. The probability mass above zero then gives the predicted missed-connection rate for the following week.

最终版本把研究洞察与实施概述分别完成。第一段末的 margin 被第二段首句承接；第一段的“无需重建”解释了表示选择，第二段的共享信息解释了对稀疏观测的处理。每段都增加实质内容，而不是换一套话重复同一判断。

## 哪些内容留在稿外

- 本例题材和数字是合成的，这一资格说明放在教学文件中，不装作真实论文证据
- 配对破坏的0.10结果与完整shuffle流程保留在事实卡；它是次级方法分析。引言主回答使用与协方差近邻匹配的0.04对0.07比较，贡献不围绕“保留配对有价值”重建
- 真实近邻查新、待核引用、样本选择依据和未测试外推需要实际材料；缺失时记录在工作材料，并只把会改变正文判断的条件写入对应位置
- “目前不能独立证明一般机制”“还没完成跨城市验证”是编辑分析。若正文未声称一般机制或跨城市普适性，不要逐一添加否认句来占据末两段
- 若真实材料中存在会翻转结论的限制，如新方案总体更准但在关键人群或条件下严重恶化，应把该实质条件放在结果解释附近。稿外不是藏匿反例的地方
- 读者记忆实验、营销案例和图形知觉研究没有验证此稿的写作效果。本例只展示可追踪的生成决策与科学含义保持，不能称为读者实验、顶刊验证或风格真实性检测

## 保义复核

任务仍是固定设置下下一周失接率预测；余量正负方向不变；步行时间条件保留；两个合成参照的能力与假设均保留；样本单位为720个 connection-weeks，未改成720条独立旅程或720个枢纽；三项误差不变；0.10及其训练/校准打乱、原始测试评价流程仍在事实卡；两个近邻的真实设定能力均保留。主回答改为0.04对协方差近邻0.07的匹配比较，贡献收束为目标表示/估计方法及整体比较所得，没有升级为唯一模块归因、一般机制、首次发现、部署收益或开源交付。

重写改变的是读者先理解什么、每句增加哪个关系、设计怎样回应困难，以及结果如何回答任务。它没有用更强的形容词代替真实研究，也没有把来源边界与审计意见写成引言的最终结论。

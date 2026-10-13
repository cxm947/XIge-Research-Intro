# E. 真实应用挑战：实际操作受阻→根因→所需能力（4支）

先选本位置要建立的判断，再读所列来源的必要邻段和完整贡献集合。英文均为编辑抽象式，须换入本稿自己的事实后自然成文；同职责分支不是同义句。所列源句语法是来源事实，适用性与篇幅判断是编辑迁移。

语言实现：[L2](../realizations/operations.md#l2)、[L4](../realizations/operations.md#l4)、[L8](../realizations/operations.md#l8)。


## 先判别，再选择分支

动笔前把候选挑战还原成一个具体判断，核对它实际承担哪种职责；同一句可兼有几种职责，不必在正文加标签：

- 安全失效现象：发生了什么、损害了什么判断。它支持动机，不自动解释难点
- 任务要求：希望同时满足哪些能力或成本。它规定目标，不自动说明已有方法为何做不到
- 设计选择：本文采用什么记录、参照或验证流程。它说明路径，不能用自选流程制造外部gap
- 有据阻力：在本任务的实际条件下，哪条可核对的关系使所需区分、操作或权衡受阻；哪项已有能力仍不足，依据是什么

先保住成立的判别关系，再把对象和后果写具体。不要把有因果或比较根据的困难改成孤立的失效现象；批评范围须对应被比较的方法及其实际能力。应用困难可以成立，而相对强近邻的学术gap仍未建立。

承认强近邻后，回到本稿实际构造与证据，正面写出仍可研究的具体问题：哪些输入或条件不同、所选路径怎样工作、哪项所得已经支持该路径。证据足以说明现成路线受阻时，再用下面分支展开挑战；仅支持另一种构造或准确研究任务时，就按该层级成文，把缺少的关键比较留稿外。不要仅靠增加限定句掩盖主线空缺，也不要为保留“两挑战”补造瓶颈、首次性或比较优势。必要时请作者确认定位调整，不擅自改变研究类型。

局部修改的取舍见[挑战与定位样本](../challenge-positioning-example.md)；样本不是可照搬的挑战答案。

### E1 缺关键证据，让人工无法有效调查

- 源：FirmRCA P5.S1–5。分析者需要运行证据，但嵌入式环境缺调试支持，必须逐条追踪长轨迹
- 实现：“To [practical task], [actor] needs [evidence]. Under [actual limitation], obtaining and using this evidence requires [costly operation], making [capability] necessary.”
- 适用：缺数据必须落在具体工作上；后文机制与评价应回应取得／利用证据而非仅说模型更准
- 代价：一个操作与后果把技术根因译成应用困难，不需把每个调试字段全列出

### E2 候选已得到，仍无法判断轻重

- 源：FirmRCA P6.S1–4。裸二进制语义缺失→大量可疑项→过度污点与噪声使调查指导不足
- 实现：“[Existing analysis] produces [candidates], but [missing distinction] prevents [actor] from prioritizing [the actual targets].”
- 适用：与E1可形成真实两挑战：能获得证据与能据此作判断不同。不能仅把一个“信息少”问题拆两个名字
- 代价：突出输出质量与使用价值，细排序机制留方案

### E3 前序失败阻断后续任务

- 源：MINER P2.S4–9→P3。服务先验证请求，前序不通过则后续长序列不能执行，质量与长度共同决定深状态可达
- 实现：“Because [later action] depends on [earlier action succeeding], an invalid [input] prevents [target operation] from being reached.”
- 适用：串行工作流、累积状态或前置条件真实存在；研究挑战是可执行推进，不只是“长序列难”
- 代价：短因果句可连接两个指标的必要关系，避免平行性能清单

### E4 自然参照在真实任务中不够

- 源：IPPO P2.S5–7、P3.S2–5。多数oracle要多个正确参照，某安全操作只出现一次，不能靠提高投票阈值解决
- 实现：“[Standard judgment] relies on [reference requirement], yet [real case] supplies only [available evidence]. The task therefore requires [a different basis for comparison].”
- 适用：可得证据数量／类型限制判断；下一方法必须解释新的比较依据为何有效
- 代价：一个确切反例可替代“数据稀疏”长篇抽象讨论；数字仅用于说明原理门槛


## 来源版本与上下文

- FirmRCA：[arXiv:2410.18483v1](https://arxiv.org/pdf/2410.18483v1)，2024-10-24；[完整引言图](../intro-source-maps/sj-446d78ec82.md)
- IPPO：[CCS 2021共著者托管版](https://www-users.cse.umn.edu/~kjlu/papers/ippo.pdf)；[完整引言图](../intro-source-maps/sj-8d71597fb2.md)
- MINER：[完整引言图及主源](../intro-source-maps/sj-3698195c5a.md)

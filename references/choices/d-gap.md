# D. 最强已有答案到真实gap（5支）

先选本位置要建立的判断，再读所列来源的必要邻段和完整贡献集合。英文均为编辑抽象式，须换入本稿自己的事实后自然成文；同职责分支不是同义句。所列源句语法是来源事实，适用性与篇幅判断是编辑迁移。

语言实现：[L3](../realizations/operations.md#l3)、[L8](../realizations/operations.md#l8)。


### D1 条件变化，使现成路线不可直接执行

- 源：ORL-Auditor P3.S2–12。逐类保留水印、dataset inference和在线成员推断能力，再指出发布时机、连续输出、参照和环境可达性错位
- 实现：“[Prior approach] can [capability] when [required condition]. In [current task], however, [that condition does not hold], leaving [specific output] unavailable.”
- 适用：事实确为前提缺失，必须写清已完成的能力，不以“cannot address our problem”替代原因
- 代价：多个近邻若同一条件可合并；不同强答案分别填补不同剩余时不能一刀删

### D2 先承认更强扩展，再限定未覆盖范围

- 源：MeTFA P4–P5。均值平滑→均值／方差可给渐近区间→未知分布、小样本／极值下的有限样本问题
- 实现：“[Route] supports [basic result] and can be extended to [stronger answer]. Yet [target requirement] under [remaining condition] is not established by this extension.”
- 适用：读者可能自然推出一种更强现成答案，省略它会夸大gap
- 代价：承认扩展占句数，却让后续构造的必要性可判断；不是为了礼貌平均介绍文献

### D3 观察不到，不等于目标属性不存在

- 源：InvMM P4.S4–11。采样未见不证明不记忆；原caption未触发不等于图像不被其他prompt复现
- 实现：“Although [observation] is not found under [tested condition], this does not establish [stronger property], because [unobserved alternative remains].”
- 适用：gap是可辨识性或测量对象错位，本文应提供更合题的测量／搜索，不改写为单纯提高检测率
- 代价：一个关键备择足够建立逻辑；无需把所有可能情况写入Intro

### D4 新场景改变了信号与任务的关系

- 源：VERIFI P3.S4–6。先给传统性能验证；FL下accuracy/loss可几乎不变，后置when少数退出，末尾是其他参与者贡献；后门副作用另句
- 实现：“In [established setting], [signal] can verify [effect]. In [new setting], however, [signal] may remain [unchanged] when [condition], owing to [specific cause].”
- 适用：旧代理量并非无效，只是在新条件下不再充分反映目标；结果先行可回应前句自然期待
- 代价：保留情态may及因果；别把第二种验证方案的风险并进第一种信号不变的原因

### D5 同名任务在新领域有不同信息结构

- 源：TextShield P3.S1–5。承认英文训练／纠错成功，再给中文语义、分词和字形／字音变化如何影响效果
- 实现：“[Methods] are effective for [original setting]. Their transfer to [target setting] is constrained by [property], which changes [task-relevant relation].”
- 适用：真实迁移条件而非仅新数据集；需解释属性怎样导致失败，不能止于研究较少
- 代价：若有多个原因，仅展开分别改变方法选择的原因；不强制凑三点


## 来源版本与上下文

- ORL-Auditor：[arXiv:2309.03081v1](https://arxiv.org/pdf/2309.03081v1)，2023-09-06；[完整引言图](../intro-source-maps/sj-6eeb51e521.md)
- VERIFI：[arXiv:2205.12709v1](https://arxiv.org/pdf/2205.12709v1)；[完整引言图](../intro-source-maps/sj-1b6614ac62.md)
- InvMM：[arXiv:2405.05846v3](https://arxiv.org/pdf/2405.05846v3)，2025-07-31；[完整引言图](../intro-source-maps/sj-07015463d4.md)
- TextShield：[完整引言图及主源](../intro-source-maps/sj-4ef65862d0.md)
- MeTFA：[arXiv:2209.01782v1](https://arxiv.org/pdf/2209.01782v1)，2022-09-05；[完整引言图](../intro-source-maps/sj-f612de4bf1.md)

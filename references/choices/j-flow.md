# J. 句群内部：同一命题怎样分配主句／子句与句界（4支）

先选本位置要建立的判断，再读所列来源的必要邻段和完整贡献集合。英文均为编辑抽象式，须换入本稿自己的事实后自然成文；同职责分支不是同义句。所列源句语法是来源事实，适用性与篇幅判断是编辑迁移。

语言实现：[L8](../realizations/operations.md#l8)、[L9](../realizations/operations.md#l9)。


### J1 稳定主题，谓语推进信息

- 源：AsgLDP P4.S1–3；Tacoma C3.S1–3
- 实现：“[System] collects [input]. It estimates [new relation] from these observations and uses it to [next output].”
- 适用：系统是当前稳定话题，读者需要沿动作和产物走，不必强换主语
- 代价：若it有多个可能指代，重复名词更清楚；压缩动作时仍保计算对象不同

### J2 条件前置或结果前置，依据读者此刻疑问选择

- 源：VERIFI P3.S5及相应保义编辑替代
- 原源分支：场景→主句信号可能不变→when条件→原因；编辑替代：When条件先行→however主句观察→原因
- 适用：正在比较情境时选条件先行；刚刚建立信号应有效的期待时结果先行更直接。不是任何一种语序普遍最优
- 代价：前置条件会延迟结果；结果先行必须让限定紧邻，不能变无条件断言

### J3 合并次要步骤，不压掉独立贡献

- 源：TextDefense P5.S6–9及相应编辑替代
- 实现：“We [main operation], [non-finite means phrase] to [secondary purpose]. [Calibration] then determines [criterion]. [Decision rule].”
- 适用：抽样／效率仅为已知目的服务时可降为分词；若低查询量是此处独立推进，保留独立主句
- 代价：从4句到3句不是改善证明；效果是焦点重分配，校准与测试时序仍要区分

### J4 将对象、约束和定义分句，但保回指与方向

- 源：InvMM C1.S2–3及相应编辑替代
- 实现：“We seek [object]. It must satisfy [defining constraint]. The measure is [directed quantity] from [A] to [B] over qualifying objects.”
- 适用：读者首次接触一个新度量，单句包含对象与资格约束过密；约束不能被读成算法无条件成功
- 代价：拆句增加it／qualifying的回指要求，不自动更短更好；不可用无方向between改写非对称定义


## 来源版本与上下文

- AsgLDP：[IEEE TIFS 15作者托管版](https://nesa.zju.edu.cn/download/AsgLDP%20Collecting%20and%20Generating%20Decentralized%20Attributed%20Graphs%20with%20Local%20Differential%20Privacy.pdf)，2020；[完整引言图](../intro-source-maps/sj-dc32e376bc.md)
- VERIFI：[arXiv:2205.12709v1](https://arxiv.org/pdf/2205.12709v1)；[完整引言图](../intro-source-maps/sj-1b6614ac62.md)
- InvMM：[arXiv:2405.05846v3](https://arxiv.org/pdf/2405.05846v3)，2025-07-31；[完整引言图](../intro-source-maps/sj-07015463d4.md)
- TextDefense：[arXiv:2302.05892v1](https://arxiv.org/pdf/2302.05892v1)；[完整引言图](../intro-source-maps/sj-b3ea90f06d.md)
- Tacoma：[ISSTA 2024 camera-ready托管版](https://users.cs.northwestern.edu/~ychen/Papers/issta24main-p723-CameraReady.pdf)；[完整引言图](../intro-source-maps/sj-c153987a94.md)

# G. 关键设计理由：从性质到选择再到能力（5支）

先选本位置要建立的判断，再读所列来源的必要邻段和完整贡献集合。英文均为编辑抽象式，须换入本稿自己的事实后自然成文；同职责分支不是同义句。所列源句语法是来源事实，适用性与篇幅判断是编辑迁移。

语言实现：[L6](../realizations/operations.md#l6)、[L4](../realizations/operations.md#l4)、[L8](../realizations/operations.md#l8)。


### G1 正面性质支持跨情境复用

- 源：EMS P2.S3–8→P3→P4.S2。成功变换可能蕴含共享策略，代码共享支撑跨程序迁移
- 实现：“[Observed artifact] may encode [shared relation]. When [transfer condition] holds, learning this relation can support [new use].”
- 适用：材料里有正面可复用洞察，无需虚构失败基线；may及共享条件不能消失
- 代价：若迁移不显然，需一个有职责的案例／证据段，不能只留抽象收益

### G2 直接办法合理，但缺少稳定比较基准

- 源：ORL-Auditor P5.S2–6。直接固定阈值→受数据条件影响→同数据shadow分布→检验
- 实现：“A direct approach is to [natural operation]. Because [quantity] varies with [condition], we instead construct [reference] that captures [relevant variation].”
- 适用：直接路线确实是读者会想到的办法，且缺陷来自材料可核的条件
- 代价：一条说明与一条构造就够时不叠加更多假想失败路线

### G3 前一产物不够后一步用，补接口关系

- 源：UVSCAN P5、P8.S1–7；Tacoma P6.S3–8。文本义务／通用事实不等于可执行API约束；规范信息不等于实现语义
- 实现：“[Available representation] provides [known facts], but [next task] also requires [missing relation]. We [operation] to derive this relation from [available evidence].”
- 适用：研究推进发生在信息转换接口；每个输入要真实可得
- 代价：展开这一处接口即可，其他成熟步骤可简写采用；不要把全过程各步都写为独立创新

### G4 换观察对象，保留更贴任务的信号

- 源：FreeEagle P6.S3–4→P7.S2–6；Diff-ID P6–P8。前者选择分类器后缀／中间表示，后者控制属性再比较身份
- 实现：“Rather than measuring [confounded object], we examine [chosen object], where [task-relevant signal] can be separated from [irrelevant variation].”
- 适用：实际材料支持分离／规避这类变化，不能从中间层名称推定鲁棒性
- 代价：需解释对象含义及选择根据；FreeEagle分类器不是只指最终分类头

### G5 所选设计带来新代价，追加必要处理

- 源：FaceArmor P4→P5→P6；IPIGuard P4→P5。先建立设计，再交其特定冲突或运行参数未知
- 实现：“This design introduces [specific cost], because [mechanism]. We therefore [response] while preserving [the original objective].”
- 适用：代价确因本方案而来，不能把它前置成与设计无关的普遍应用挑战
- 代价：额外句群是设计解释成本，不追求挑战／模块表面一一对应


## 来源版本与上下文

- ORL-Auditor：[arXiv:2309.03081v1](https://arxiv.org/pdf/2309.03081v1)，2023-09-06；[完整引言图](../intro-source-maps/sj-6eeb51e521.md)
- EMS：[共著者托管论文](https://www-users.cse.umn.edu/~kjlu/papers/ems.pdf)，精确版本以[完整引言图](../intro-source-maps/sj-2deb60c210.md)为准
- FreeEagle：[arXiv:2302.14500v1](https://arxiv.org/pdf/2302.14500v1)，2023-02-28；[完整引言图](../intro-source-maps/sj-33b7f0ad03.md)
- Tacoma：[ISSTA 2024 camera-ready托管版](https://users.cs.northwestern.edu/~ychen/Papers/issta24main-p723-CameraReady.pdf)；[完整引言图](../intro-source-maps/sj-c153987a94.md)
- FaceArmor：[完整引言图及主源](../intro-source-maps/sj-6a7f688210.md)
- Diff-ID：[完整引言图及主源](../intro-source-maps/sj-9042a938b2.md)
- UVSCAN：[arXiv:2306.11206v1](https://arxiv.org/pdf/2306.11206v1)，2023-06-20；[完整引言图](../intro-source-maps/sj-a36437c84c.md)
- IPIGuard：[EMNLP 2025正式论文](https://aclanthology.org/2025.emnlp-main.53.pdf)；[完整引言图](../intro-source-maps/sj-4391324662.md)

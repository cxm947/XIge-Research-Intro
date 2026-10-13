# B. 收窄：从领域到子领域／具体可操作对象（4支）

先选本位置要建立的判断，再读所列来源的必要邻段和完整贡献集合。英文均为编辑抽象式，须换入本稿自己的事实后自然成文；同职责分支不是同义句。所列源句语法是来源事实，适用性与篇幅判断是编辑迁移。

语言实现：[L1](../realizations/operations.md#l1)、[L2](../realizations/operations.md#l2)、[L6](../realizations/operations.md#l6)。


### B1 从成熟手段到本场景接口

- 源：MOCK P2.S1–6。静态／动态→fuzzing的工作机制→syscall接口→调用及参数序列→既有成功
- 选择与实现：“[Established approach] performs [operation]. In [target system], it acts through [interface], producing [the object later analyzed].”
- 适用：研究设计依赖特定输入接口和对象单位；读者可能知道大技术，却不知其在本场景怎样工作
- 代价：可以不介绍无关路线，必须保住对象定义，因为下一段讨论对象关系

### B2 用数据所在位置限定子问题

- 源：AsgLDP P1.S4–5。Different-from对比集中式，where说明用户仅有部分图，再补属性
- 选择与实现：“Unlike [centralized setting], [target setting] distributes [information] across [holders], each of whom observes only [available part].”
- 适用：数据可得性改变可用方法；不是仅把“distributed”当技术标签
- 代价：一条位置／观察范围足以限定时不加部署百科；若属性与边关联决定方法，需在邻句建立

### B3 从前一步产物进入下一项任务

- 源：FirmRCA P2.S3–5→P3.S1。保存crash用例→只是第一步→仍需找根因→给定用例定位错误指令
- 选择与实现：“When [event] occurs, [system] records [artifact]. This artifact enables [next step], but [practical goal] still requires [specific judgment].”
- 适用：已有工具解决前序任务，本文交付后序判断，不能把两者统称发现／修复
- 代价：短的接口桥接比额外背景段更有效；下一任务的独立价值必须写清

### B4 从规范对象进入实际实现差距

- 源：Tacoma P3→P4，P6.S3–8。fuzzing已有能力→绑定代码难触达→跨语言输入有效性→规范解析后仍须语义补齐
- 选择与实现：“Within [broad system], [component/interface] mediates [interaction]. Reaching its behavior requires inputs that satisfy [implementation-dependent relation].”
- 适用：具体边界层决定测试／分析能否真正进入目标功能；先命名边界，再给语义要求
- 代价：可省其他系统模块，但不能把实现相关条件写成已由标准全部提供


## 来源版本与上下文

- FirmRCA：[arXiv:2410.18483v1](https://arxiv.org/pdf/2410.18483v1)，2024-10-24；[完整引言图](../intro-source-maps/sj-446d78ec82.md)
- AsgLDP：[IEEE TIFS 15作者托管版](https://nesa.zju.edu.cn/download/AsgLDP%20Collecting%20and%20Generating%20Decentralized%20Attributed%20Graphs%20with%20Local%20Differential%20Privacy.pdf)，2020；[完整引言图](../intro-source-maps/sj-dc32e376bc.md)
- Tacoma：[ISSTA 2024 camera-ready托管版](https://users.cs.northwestern.edu/~ychen/Papers/issta24main-p723-CameraReady.pdf)；[完整引言图](../intro-source-maps/sj-c153987a94.md)
- MOCK：[NDSS 2024正式论文](https://www.ndss-symposium.org/wp-content/uploads/2024-131-paper.pdf)；[完整引言图](../intro-source-maps/sj-177bf3c33e.md)

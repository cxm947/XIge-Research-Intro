# I. 末评价贡献：评价工作＋最强成立的任务答案（5支）

先选本位置要建立的判断，再读所列来源的必要邻段和完整贡献集合。优先让主判断直接表达任务完成或改善；已在前文建立的意义不必在末尾重讲，新效用或确认状态仍保留。英文均为编辑抽象式，须换入本稿自己的事实后自然成文；同职责分支不是同义句。所列源句语法是来源事实，适用性与篇幅判断是编辑迁移。

语言实现：[L7](../realizations/operations.md#l7)。


### I1 范围已足，短句表达跨条件答案

- 源：FreeEagle C3，依赖P6/P7的机制及结果解释；Diff-ID P9.C3.S1，前文交任务与方法，本项首次报告定性结果
- 实现：“We evaluate [work] across [scope], demonstrating [task capability] under [defining conditions].”
- 适用：前文已明确任务、方法及必要条件，一句具体的跨条件结论足以交出评价答案；可归纳已报成果，也可首次报告定性结果
- 代价：不能仅保留孤立的effectiveness；按尚未完成的评价答案补代表证据，首次报告本身不要求数字

### I2 贡献首次承担主要定量答案

- 源：FirmRCA C3.S1–3；UVSCAN P10–P11的首次证据负担
- 实现：“We conduct extensive experiments on [objects], demonstrating the effectiveness of [work] in [actual task]. [Supported representative result with its necessary comparison].”
- 适用：方案后直接贡献，尚未预告主要结果；数字代表最终判断，不只是组件速度
- 代价：实验范围足够才使用extensive；按需增加证据句，不从源词数照搬长度；相同能力的次要指标留正文

可选取舍：若此刻要决定“首次结果该交任务产出，还是组件速度”，可读 [FirmRCA选证实例](../deep-source-contexts/sj-446d78ec82/evidence-choice-example.zh.md)。前文已交查因与排序用途时，根因进入前十的证据把方法连到分析者先查哪些候选；要突出另一项能力，则换用回答那项判断的证据。需要来源解释时可读[完整分析](../deep-source-contexts/sj-446d78ec82/analysis.zh.md)§4–5；在技能目录运行“python3 scripts/read_source_context.py --deep --paper FirmRCA --section evidence-selection”，返回完整分析与实例，重点可看分析§4–5；不是窄节抽取，也不增加必读步骤。

### I3 主效果与保留效用共同成立

- 源：TextShield C2.S1–2，正文§5；VideoEraser P3/P4的双重任务
- 实现：“Our evaluation shows [primary effect] while maintaining [required legitimate utility] under [shared setting].”
- 适用：两轴是真实共同任务并在对应条件下验证；不能拿两个独立最佳格子拼while
- 代价：即使两数字比一数字长，也可能是完整价值判断的最小证据；不追加无关指标

### I4 现实产出与确认状态

- 源：Tacoma C3.S1–3；IPPO P6/C3；MOCK P11
- 实现：“The evaluation identifies [new findings] across [scope], of which [verified subset/status].”
- 适用：现实新发现是论文主推进的一部分；detected/reported/confirmed/fixed/CVE分别有证据
- 代价：保必要子集关系，避免只报原始报告量；若比较效益也不可缺，可在同一末项分句而非偷换对象

### I5 新认识／适用关系就是评价答案

- 源：AsgLDP C3.S1–2；InvMM C3.S1–3；VERIFI C3与正文§IV-C/D须分层
- 实现：“Through [actual evaluation], we show that [supported capability or relationship].”
- 适用：研究价值是联合性质、可比尺度、成员与记忆区分、或有条件的适用认识，未必有单一优胜百分比
- 代价：明确所得；任务关系已充分表达就收束，确有新认识再补；若将正文发现前移，应标为编辑选择，不说源Intro原已如此


## 来源版本与上下文

- Diff-ID：[arXiv:2303.18174v1](https://arxiv.org/pdf/2303.18174v1)，2023-03-30；[完整引言图](../intro-source-maps/sj-9042a938b2.md)
- FirmRCA：[arXiv:2410.18483v1](https://arxiv.org/pdf/2410.18483v1)，2024-10-24；[完整引言图](../intro-source-maps/sj-446d78ec82.md)
- AsgLDP：[IEEE TIFS 15作者托管版](https://nesa.zju.edu.cn/download/AsgLDP%20Collecting%20and%20Generating%20Decentralized%20Attributed%20Graphs%20with%20Local%20Differential%20Privacy.pdf)，2020；[完整引言图](../intro-source-maps/sj-dc32e376bc.md)
- VERIFI：[arXiv:2205.12709v1](https://arxiv.org/pdf/2205.12709v1)；[完整引言图](../intro-source-maps/sj-1b6614ac62.md)
- InvMM：[arXiv:2405.05846v3](https://arxiv.org/pdf/2405.05846v3)，2025-07-31；[完整引言图](../intro-source-maps/sj-07015463d4.md)
- FreeEagle：[arXiv:2302.14500v1](https://arxiv.org/pdf/2302.14500v1)，2023-02-28；[完整引言图](../intro-source-maps/sj-33b7f0ad03.md)
- Tacoma：[ISSTA 2024 camera-ready托管版](https://users.cs.northwestern.edu/~ychen/Papers/issta24main-p723-CameraReady.pdf)；[完整引言图](../intro-source-maps/sj-c153987a94.md)
- TextShield：[完整引言图及主源](../intro-source-maps/sj-4ef65862d0.md)
- IPPO：[CCS 2021共著者托管版](https://www-users.cse.umn.edu/~kjlu/papers/ippo.pdf)；[完整引言图](../intro-source-maps/sj-8d71597fb2.md)
- MOCK：[NDSS 2024正式论文](https://www.ndss-symposium.org/wp-content/uploads/2024-131-paper.pdf)；[完整引言图](../intro-source-maps/sj-177bf3c33e.md)
- UVSCAN：[arXiv:2306.11206v1](https://arxiv.org/pdf/2306.11206v1)，2023-06-20；[完整引言图](../intro-source-maps/sj-a36437c84c.md)
- VideoEraser：[EMNLP 2025正式论文](https://aclanthology.org/2025.emnlp-main.304.pdf)；[完整引言图](../intro-source-maps/sj-cc51b110bc.md)

# MOCK：科学证据与适用边界

## Q1

- locator: Introduction P2–P3 p1; §II-A pp2–3; §III pp3–4
- support: 作者将调用前序执行与后序路径相连，并以被拒/等价行为解释无效输入；已有工具成功先被承认
- qualification: 状态构造和输入质量为研究任务解释，不是本轮独立证明所有内核路径或任何调用组合规律。历史漏洞数字不更新为今日事实。
- writing_role: 让任务意义通过可观察失败而非抽象先进性成立

## Q2

- locator: Introduction P4.S1–S5 pp1–2; §II-A pp2–3; §III pp3–4
- support: 引言对点对点/前一调用作较强概括；正文另讨论关系表的方向与长距离信息
- qualification: 本轮不核对当前Syzkaller/HEALER实现。保归属型强原句，不把pairwise表征、实际可用上下文及邻接限制静默互换；先前实现范围属于源作者比较。
- writing_role: 保简单情形正能力，并说明更复杂任务的剩余

## Q3

- locator: Introduction P4.S6–S9 p2; §IV-B pp5–6
- support: 语料准备问题已引入学习路线；松散trace可能引噪，所学依赖may不全或有错
- qualification: 不是所有上下文感知方案的先验要求；不是知识必然有错。golden corpus为作者理想材料表述，不等于本轮已独立确认样本是完备真值。
- writing_role: 使调度动机源自同一设计决定的后续风险

## Q4

- locator: §II-C p3; §IV-A p4; §IV-B pp5–6; §IV-C pp6–7
- support: 新覆盖材料经最小化形成训练集；正文说采用HEALER/Syzkaller相同最小化方法；轻量语言模型与策略调度协同。引言把操作称bandits，正文以actions对应变异任务
- qualification: 此处模型为特定NNLM/BiGRU，不是当代通用LLM。本文不是最小化算法首次发明或完全无噪保证的独立证明。arms译法属于明示的术语标准化。当前仅分析信息与组件职责，不交执行步骤。
- writing_role: 保数据选择→学习→变异→调度的依赖，避免裸技术名或虚构多项创新

## Q5

- locator: §V p8; §VI-A/B pp8–9; §VI-D pp10–11
- support: 在线语料积累后周期训练；初始种子与预训练设置分别分析早期性能，预训练有助缩短预热/初始积累时间。启动配置不是被缩短的warmup时段本身。
- qualification: 设置段内核版本与覆盖实验段/图局部版本有差异，沿实验局部使用；不默默统一。并非所有配置有同幅收益或消除冷启动。没有把正文模型训练做成无成本同步行为。
- writing_role: 说明P6设置句回收P5运行前提而非另加性能清单

## Q6

- locator: §VI-B/C pp8–11; Figure4/5 and TableI
- support: 平均覆盖7%为三基线增长概括；关联输入50%与最小化后的较长关联序列分布有关，正文区分≥3、≥5等范围
- qualification: 保持源作者引言强概括，但不能读成每个模型、每个序列长度、所有生成输入都统一多50%；这不是直接因果隔离证明。平均值不能用摘要最大32%偷换。
- writing_role: 中间输入能力把表示/学习选择接到覆盖与bug结果，数据选择重在职责

## Q7

- locator: §VI-G pp12–13, TableIII p13; §VII p13
- support: 逐步设计对照支持上下文/调度作用；模型引导变异额外成本约低于7%、调度低于1%；训练周期平均23分钟并行，不中断主循环；讨论以顺序依赖为主
- qualification: 不把各模块成本加成统一无条件开销率，也不把并行说成零计算。低开销及无缝集成是作者评价，不保证任何fuzzer、硬件、并发依赖都成立。
- writing_role: 集成价值是采用条件证据，与高覆盖不同

## Q8

- locator: Introduction P6/C4 p2; §VI-E/F pp11–12, TableII p12
- support: 受控比较的漏洞优势与另行运行发现15项真实漏洞分开；源文称四确认、四修复、两CVE，正文列7.8/5.5分项评分及不同潜在后果
- qualification: 发现、报告、确认、修复、CVE标识不是同状态；不把四确认与四修复推成相互不重叠8项。引言严重性/提权表述较粗，当前不查CVE今日状态或改写为统一后果。
- writing_role: 现实结果收束研究实用性，不能替代受控比较


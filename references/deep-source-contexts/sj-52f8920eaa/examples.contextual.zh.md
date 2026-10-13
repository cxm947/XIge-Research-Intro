# 有前提、取舍与代价的表达选择

来源身份与读取约定：SUB-PLAY: Adversarial Policies against Partially Observed Multi-Agent Reinforcement Learning Systems；arXiv:2402.03741v4, 31 August 2026, with CCS 2024 imprint；https://arxiv.org/pdf/2402.03741v4。历史必要修订及独立复读日期为2026-10-06；2026-10-07仅恢复核验与分发整理，不是新蒸馏或重新全篇审读。下文阅读与编辑分析均沿用该历史范围，未复现实验或测试写作收益。分析坐标见coordinate-crosswalk.json，不能凭同名坐标与正式原图强接。

以下英文均为原创编辑示例，不是原文引文、作者自述或实际新论文成果。源文能力强度按场景保留；凡前移正文、删去命题或换结果池，明说为选材变化。它们供局部选择，不构成按数量填写的模板。

## L1：同一联合 gap 的三种信息顺序

共同命题：Victim-play 已能通过交互进行黑盒攻击，不需受害策略内部或环境篡改；从单体受害者转到多体，再叠加部分观测，会给稳定训练带来困难。共同使用条件：上文已交对抗策略通过攻击者自己的行动压低受害任务表现。

A，强已有答案优先：
Victim-play already generates adversarial policies through black-box interaction, without access to the victim’s policy or changes to the environment. Extending this approach from a single victim agent to a multi-agent team makes stable attacks harder to obtain. Partial observations further complicate training, potentially causing fluctuations or poor local optima.

适用：读者需要先确信本文公平对待近邻。第一句承认其低权限能力，第二句改变对象，第三句再加信息障碍。删去源文 Go/无人机例，失去一点场景形象性但不删联合条件。最后一句是后果概括，未逐字保留“无法收敛”，如需保存该单独命题可用 B。

B，条件差优先：
The difficulty is to sustain a strong adversarial policy against a team of victim agents when the attacker sees only part of the environment. Victim-play provides a black-box interaction framework without requiring access to the victim’s policy or environmental perturbations, but it was designed for single-agent victims in two-player competitions. In the multi-agent setting, missing global state information can cause unstable learning that fails to converge or becomes trapped in poorly performing local optima.

适用：上文刚命名本文任务，读者的问题是该任务为什么没被已有框架解决。先给目的，再给公平比较，最后解释后果。把源文按对象逐级展开换成联合条件领起；更紧扣当前问题，但第一句信息密度较高。

C，分两层问题：
A black-box framework such as Victim-play can train an adversary by interacting with a victim, without inspecting its policy or perturbing the environment. This answers the access problem for a single-agent victim. It does not by itself ensure stable attacks on a multi-agent team, and partial observability adds a further obstacle: the missing global state can prevent convergence or lead training to a poor local optimum.

适用：需要显式区分访问权限与稳定生成两类要求。第二句的“access problem”是该历史分析解释标签，不是源文正式提出的问题名。第三句将两个后果置于冒号后，强调原因链；“does not by itself ensure”是对源文 encounters challenges 的任务化重述，不是证明其绝不可能攻击成功。

L1 不是把 source 的首次性复制到今天；是否有更强现成答案需要目标论文独立检索。

## L2：固定分治后的样本不均因果链

共同命题：按观测到的受害者数分配转移；不同子游戏出现概率造成 buffer 不均；部分子策略可能欠训练；从相近子游戏共享用于缓解。共同使用条件：前文已交多个子游戏/子策略，以及数据来自交互。相近是子游戏的观测数距离。

A，过程到后果：
Interaction transitions are assigned to replay buffers according to the number of visible victim agents. Because subgames occur with different probabilities, their buffers receive unequal amounts of data, which may leave some subpolicies undertrained. SUB-PLAY mitigates this imbalance by sharing transitions between nearby subgames.

适用：刚讲完生成子策略的流程，顺势回答训练数据如何到达各子策略。三句给分配→根因/后果→补偿。长度用于把两个因果层次分开，不必再写抽象 main challenge 句。

B，后果领起：
Some subpolicies may be undertrained because transitions are unevenly distributed across the subgame replay buffers. This imbalance arises when transitions are grouped by the number of visible victim agents and the resulting subgames occur with unequal probabilities. Sharing transitions between nearby subgames provides SUB-PLAY’s remedy.

适用：读者已经问为什么分治未自动变好，先交训练后果。第二句比较密，把分组规则和出现概率合起来；第三句 remedy 保留作者对设计的肯定身份，不升级为完全消除不均衡的定理。

C，先解释有益选择为何需要补偿：
Separating observations by the number of visible victim agents gives each subpolicy a more focused subgame to learn. Yet those subgames are not encountered equally often, leaving uneven replay data and potentially undertrained subpolicies. SUB-PLAY therefore shares transitions across nearby subgames to support their training.

适用：前文只说分治却没解释技术收益，需把有益选择与代价放在同一段。首句 more focused 由 §4 的相对简单子游戏直觉前移，是选材增加，不能标成对 P4.S6–S9 的纯同义替换。第二句省去显式 transitions 分配动作，需要“separating observations”与 replay data 已足够清楚；否则选 A。

## L3：防御结果与实践认识的三种重排

共同命题：所评重训不足以消除对抗策略，ensemble/fine-tuning 只能适度减弱；因此部署方式值得关注，周期更新和多样性是潜在缓解方向。共同使用条件：读者知道本文实做三种防御评价，且没有把方向当通用保证。

A，结果后给认识：
Adversarial retraining does not adequately counter the evaluated adversarial policies, while policy ensembles and fine-tuning reduce attack effectiveness only moderately. These results suggest that flexible deployment, including periodic policy updates and a more diverse ensemble, may help mitigate the threat.

适用：紧接评价介绍，二句分别交观察和建议。保留结果的强断言及建议的 may，不将整段一律弱化。省去源文 For example 片段，例子嵌入建议句。

B，实践关注领起：
Deployment deserves attention alongside algorithm performance. In our experiments, adversarial retraining remains insufficient, and policy ensembles and fine-tuning provide only moderate reductions in attack effectiveness. Periodic updates and greater policy diversity therefore emerge as promising deployment directions rather than established guarantees.

适用：一个面向实践者的收束段，第一句来自 C4，后两句回补证据。最后半句是编辑显化范围，不是源文原有措辞；已在上下文限定探索性时，可用 may help mitigate the threat 代替末句以免重复防御式提示。

C，适应关系领起：
A victim can change what the adversary has time to adapt to. The ensemble experiments suggest a defensive benefit when the attacker has access to only part of the policy pool, whereas access to the full pool leaves little protection. This motivates periodic updates and increased policy diversity as potential complements to training-time defenses.

适用：读者需要明白部署为何有作用，前移 §5.7 的策略可接触范围比较。它没有保留 fine-tuning 与 retraining 的所有独立结果，属于证据选择，不是 L3-A 全部命题的短写。第二句 defensive benefit 是所测集合概括，完整表 5 有少数不降低攻击的格，不能扩成逐格收益。

## F1：完整方案段的三种解释重点

共同输出：以部分观测交互生成对抗策略。各段都给子游戏、子策略、样本补偿、组合；不声称引言已经完成所有访问设定。整体论文仍需说明控制己方、知道受害者数量、有交互权限等可执行条件。

A，顺着源文先闭环再补偿：
We introduce SUB-PLAY, a black-box framework for generating adversarial policies in partially observed multi-agent competitions. It divides the attack into subgames, models each as a partially observable stochastic game, and trains a corresponding subpolicy with MARL. A hard-coded combination of the subpolicies produces the final adversarial policy. Because subgames occur at different rates, assigning transitions by the number of visible victim agents leaves some replay buffers sparsely populated and may undertrain their subpolicies. SUB-PLAY addresses this imbalance through transition sharing between nearby subgames.

适用：保持源文概览的叙述层级，先让读者把握整体产物。将源 P4 的九单元压为五句，去掉独立“main challenge”宣告和重复后果，但保留发生机制。分组依据依然较晚交；若读者需要立即知道分什么，选 B。

B，先交可观察分组依据：
We propose SUB-PLAY, which generates black-box adversarial policies by dividing a multi-agent competition according to how many victim agents the attacker can observe. Each resulting subgame is modeled as a partially observable stochastic game and assigned its own subpolicy. Unequal subgame frequencies yield unequal amounts of replay data, so SUB-PLAY shares transitions between nearby subgames to mitigate undertraining. At deployment, a hard-coded selector applies the subpolicy associated with the current observation.

适用：首次接触方法的读者容易问“subgame 是按什么分”；先回答它，再讲数据代价。最后一句从 §4.5 前移当前观测切换，比源 P4.S4 的简单 integrate 更具体。省去显式“由 MARL 求子策略”这一命题，若全文此处必须自足，应在第二句末添 trained with MARL。篇幅节省伴随解释职责迁移，不是假称所有原命题不变。

C，先把训练补偿和使用闭环讲透：
SUB-PLAY learns separate adversarial subpolicies for different numbers of observable victim agents. Each observation-defined subgame is treated as a partially observable stochastic game and solved using MARL. Rarely encountered subgames provide less training data, so the framework disseminates interaction transitions across nearby subgames instead of leaving every replay buffer isolated. The trained subpolicies are combined through hard-coded switching based on the current observation, yielding an adversarial policy for partially observed multi-agent competition.

适用：紧接一个已经命名 SUB-PLAY 和 black-box 条件的独立提案句后，读者需要操作理由。省去再次宣布 novel；主打“分组→不足→共享→决策”。rarely encountered 概括不均衡，未详写共享概率；适合引言而非算法定义。若独立用此段，应恢复任务提案与黑盒条件，不能因作者看过正文就假定读者已知。

F1-A/B/C 都有肯定的生成能力，未把已完成方法改成可能工作的计划；C 的上下文依赖最多，A 与源取舍最接近，B 最早回答分组依据。

## C1：三套完整贡献组织，不要求原稿都采用

### C1-A：四个身份，保留源首次性和评价力度

- To the best of our knowledge, this is the first study of adversarial-policy threats in multi-agent competitive environments, showing that victim policies remain exploitable even under partial observation
- We characterize three partial-observability limitations and introduce observation-driven subgame construction to accommodate them
- We systematically evaluate SUB-PLAY, demonstrating stronger attacks than the state-of-the-art framework in partially observed multi-agent competitions
- We investigate potential defenses and show why MARL practitioners should attend to deployment details as well as algorithm performance when mitigating adversarial-policy threats

条件：仅作为该源版本贡献的编辑复述；首次性属于作者当时主张，不能直接充作目标新稿的已核创新。前文已讲明共享及评价设置，所以贡献不重述模块或数字。最后一项保留实践关注的重要性，不声称某种防御已保证安全。

### C1-B：三项，将威胁发现与总体方法归为一个推进

- To the best of our knowledge, we conduct the first study of adversarial-policy threats in partially observed multi-agent competitions and introduce SUB-PLAY to generate such policies through observation-driven subgames
- A systematic evaluation across three observability limitations in Predator-prey and World Communication establishes SUB-PLAY’s advantage over Victim-play, with DDPG and MADDPG representing distributed and centralized training
- We evaluate adversarial retraining, policy ensembles, and fine-tuning, identifying deployment details as an important complement to algorithm-performance improvements in mitigating these threats

条件：分类独立性不是主要卖点时可用。第一项把源 C1/C2 合并，保留研究先行主张但收窄到部分观测这一整体焦点；没有逐命题保存“首次研究全部多智能体竞争威胁”的原范围。第二项增加正文算法名，不能读成三限制×两环境完整交叉实验。它节省贡献项，但首项信息更密，方法共享仍需要方案段解释。

### C1-C：四项保留任务身份，评价用代表性频数展开

- To the best of our knowledge, this is the first study of adversarial-policy threats in multi-agent competitions, revealing exploitable victim behavior despite partial observations
- We characterize uncertainty-, distance-, and region-based observation limits and design observation-driven subgames with transition sharing to learn effective adversarial policies
- We systematically compare SUB-PLAY with Victim-play in the evaluated environments. Under uncertainty limits, SUB-PLAY attains the lowest catch rate in 47 of 50 settings and the lowest collision frequency in 49 of 50 settings among the main comparison methods
- Our defense evaluation shows that adversarial retraining remains insufficient in the tested settings and motivates attention to policy updating and diversity during deployment

条件：需要一个容易理解的定量答案，而不愿在贡献中解释 PM 与式 15，可选频数。数字仅属于 uncertainty 和正文比较池，附录新增 APL/Victim-curr 后的最佳频数不同。第二项比源 C2 多写 sharing；第四项选择重训不足及其部署启示，省去集成/微调的独立结果；前文必须保留 ensemble/fine-tuning 有限收益及建议强度。此组是有标记的证据取舍，不能宣称与原贡献逐命题相同。若文章要重点讲 region 的最大改善，可选式 15 数字，但须承担其分母解释。

三套组的长度由新增读者问题决定。C1-A 最依赖前文完成解释，C1-B 改贡献归组，C1-C 改证据选择；都不能靠机械换同义词实现。

# VFL：可实际选用的表达与内容变体

以下均为E类新拟文本，不是源引文，也不代表已测得写作增益。每组先固定命题，再说明改的是语法前景、解释量还是选材；各选项有使用条件和成本。已核实的主张不任意降强度；历史首次性不作为当下选项移植。选择后应放回完整段落检查指代、因果和前后已知条件。

## V01　任务价值：从什么入口进入同一协作问题

命题来源：P1.S3–S4＋P3.S3–S5＋P4.S4。以下是内容重心选择，非三个同义句。

A. “Organizations use vertical federated learning to build a shared model from complementary features. In the setting studied here, however, only one participant owns the labels.”
- 用于跨领域读者尚不知合作目的时。先交正面用途，再引所有权不对称；两句成本换来清晰任务对象
- 尚未说明标签为何重要，后文仍需资产或敏感性依据

B. “A participant may contribute useful features to collaborative training without gaining access to the other participant’s private labels. Whether this separation survives training is the privacy question examined here.”
- 用于读者已懂VFL、核心疑问是正常权限与实际所得时。直接前景化知识边界
- 省去领域定义，不能再承担HFL/VFL分类教学；第二句是编辑问题化表达

C. “Collaboration lets the label-owning participant benefit from complementary features while the labels remain a private asset. Label inference threatens this division of roles.”
- 用于经济资产主线已经建立时。先把属性连接到任务后果，再说明研究价值
- 不自动覆盖所有标签敏感场景；若改为医疗价值，应换有依据的场景，而不是追加虚构损害

## V02　所有权条件：主句位置与重要性并非一回事

固定命题：在本文场景中，特征分散在参与者间，而标签只由一方持有。

A. “In the setting we study, features are distributed across participants, but only one participant owns the labels.”
- 默认比较两种资源的分布；but给同一句内的对照
- 并列信息量较高，适合已定义participants的上下文

B. “Only one participant owns the labels in the setting we study; the other participants contribute complementary features.”
- 所有权是刚出现的关键条件时，先给label owner再交正常作用
- 后半句增加“其他方贡献”的角色表述，不再逐字等价于只说分布；该事实由P3支持

C. “Although the participants jointly train the model, the labels belong to only one of them in this setting.”
- 读者容易把共同训练误解成共同拥有标签时，以让步打破该推断
- 特征分布未在此句重复，须已在前文交代；否则B/A更完整

## V03　近邻与剩余：承认已有知识后改问什么

命题来源：P2.S4、P5、§3.5；这些是定位的不同内容选项。

A. “Prior work had established privacy leakage in horizontal federated learning. The remaining question was how label privacy changes when a participant has only a partial model and partial features.”
- 用于历史分析或回述本源研究问题。过去时避免冒充今日文献前沿
- 两句保留强先例与新权限，省略不同泄露任务的清单

B. “The direct variant adapts a label-related insight from prior HFL work to a VFL setting without model splitting. Its novelty should therefore be discussed through the target setting and supporting analysis, rather than attributed to an entirely new leakage principle.”
- 用于比较贡献归属/审稿式定位，不是引言常规开头
- 明确继承关系，代价是中断线性发现故事；来源是§3.5，不可伪称引言已明说

C. “Limited model access weakens the analogy with HFL, but it does not remove all transferable insights. The study examines both information retained in local representations and a distinct gradient-related case.”
- 用于读者已经看到两个机制、需要理解研究组合时
- 首句是编辑综合而非源作者原话；不证明未调查的HFL方法全部不可用

## V04　发现包装：认知动作、科学主体与模态

固定核心：底层模型可能自然具有标签推断能力（P6.S3），此处不能因去掉we find就删除might。

A. “The authors find that a participant’s trained bottom model may itself support label inference.”
- 来源综述需要明确主张归属时；矩阵是作者发现，信息前景在补语
- 多一层包装，但有利于区分源报告与独立验证

B. “A participant’s trained bottom model may itself support label inference.”
- 紧接已明确来源的分析时，让科学对象直接作主语
- 单独引用会淡化报告来源，需靠上下文补足；没有提高科学强度

C. “Even with access to only part of the federated model, a participant may gain a local representation useful for label inference.”
- 读者刚读完权限差异时，用even连回反常性
- 加入P5的条件并把“模型能力”具体化为“表示用途”，是邻句综合，不是单句机械换序

## V05　发现到设计：把真正依赖写出来

命题来源：P6.S4–S5→P7.S2/P7.S5；不包含执行方法。

A. “Training gives the local model a label-related representation. The passive variant uses this representation, whereas the active variant seeks to strengthen it.”
- 两个变体容易被误读成完全独立原理时，先给共享对象再对照用途
- 两句讲总体关系，未交额外辅助标签；正式任务描述仍须补该条件

B. “Because training makes the local representation useful for predicting labels, its quality becomes a natural variable for explaining and comparing the two representation-based variants.”
- 用于写作方法论中的设计解释，而非声称作者唯一意图
- 句子以因果压缩三步；读者若还不知道两个变体，应改用A分开介绍

C. “The passive result shows that the trained representation can support inference with limited auxiliary labels. The active design then targets the same representation quality to improve performance.”
- 前文已经给被动结果、接下来转主动设计时使用
- 这是“结果→后续设计”的读者顺序，不证明研究者真实发现时间顺序；也不声称辅助标签可省

## V06　同一成绩的三种前景：数值、成本、场景

固定事实：表2被动BHI训练集F1为0.7614，辅助标签70，所报训练样本69,181。下面均保留train、F1和数据集归属。

A. “With 70 auxiliary labeled samples, the passive variant achieves a training-set F1 score of 0.7614 on BHI.”
- 前文已交医学价值时，前置资源条件最简洁
- 未保留训练池规模；少量这一价值需由前文或后句比较支撑

B. “On BHI, the passive variant achieves a training-set F1 score of 0.7614 using 70 auxiliary labeled samples, against a reported training set of 69,181 samples.”
- 读者关心额外知识规模与被评数据规模时，把两个数绑定但不写成分母
- 单句较重，适合数字承担不同职责且需共读时；不能把samples改成人数

C. “The BHI evaluation uses 70 auxiliary labeled samples. The passive variant reaches a training-set F1 score of 0.7614.”
- 独立展示、跨领域读者或前一句已长时，条件与结果拆开降低处理负担
- 两句增加显式连接成本，且一旦第二句被摘引就可能丢条件；段内必须紧邻

## V07　换证据回答另一疑问，不冒充同义改写

A. “On BHI, the passive variant reaches a training-set F1 score of 0.7614 with 70 auxiliary labels.”
- 选材问题：少额外标签下，敏感应用场景是否存在有分量的风险？
- 来源表2；优势是场景/资源/任务答案共现；代价是不能单靠该绝对分数证明信息来自VFL预训练

B. “With the same ten auxiliary labels and semi-supervised strategy, the pretrained bottom model yields a CIFAR-10 training accuracy of 0.6554, compared with 0.1157 for random initialization.”
- 选材问题：是不是仅凭半监督算法和那几个标签便足以达到该成绩？
- 来源§5.1/表3；对照使归因更可理解；代价是转到CIFAR-10，失去医疗场景前景，仍不是独立因果复现实验

C. “On the BHI test set, the passive variant reaches an F1 score of 0.7519 with the reported 70 auxiliary labeled samples.”
- 选材问题：能力是否延伸到训练集之外？
- 来源表2；明确评价集合；代价是换了待证明的覆盖问题，不能把0.7519放回0.7614的原句并宣称无内容变化

## V08　特例成绩：条件前置、后置与分句

固定命题：直接路线在受评非split架构、训练样本上的准确率为1.00，六个所评数据集一致（P7.S8–S10＋§3.5/§5.1）。

A. “For training samples in the evaluated VFL settings without model splitting, the direct variant achieves an accuracy of 1.00 on all six datasets.”
- 当完美数值最易被摘引扩大时，先锁定对象/架构再报成绩
- 条件前置是新拟选项，不是源P7.S9的句法事实；单句较长

B. “The direct variant achieves an accuracy of 1.00 on training samples across all six evaluated datasets under the VFL architecture without model splitting.”
- 前文已介绍架构，段落重心是结果时，把成绩放前、范围放后
- 正确但晚到的条件容易被粗读漏掉；用于独立摘要时A更稳

C. “The direct variant is evaluated without model splitting and concerns training samples. It achieves an accuracy of 1.00 on all six evaluated datasets.”
- 原理与结果需要分步处理时，单独用短句承载条件
- 两句所指必须连续；不能删首句后保留一个无条件完美主张

## V09　防御结论：把未解问题落在实际评价标准

命题来源：P8和§6。A保留引言层的较宽总结；B/C只表述正文所展示的主动攻击评价与实质缓解的效用代价，并非完全相同的信息集合。

A. “Some evaluated defenses mitigate the direct variant, but the representation-based variants remain difficult to defend against effectively.”
- 前文已经交代效用要求时，保留两类结果差异后简洁收束
- alone的effectively仍需评价上下文，不适合孤立技术规格

B. “In the reported active-attack evaluations, substantial reductions in inference performance come with substantial degradation of the original task. This leaves effective mitigation with retained task utility unresolved in those evaluated settings.”
- 读者将“无效”误解成“分数绝不下降”时，用所展示的主动评价说明实质缓解的效用代价
- 第二句是编辑综合。第一句只归纳§6所展示的主动评价与实质缓解，不声称任何微小下降均需高代价，也不补造独立被动防御实验

C. “The defense evaluation separates two outcomes: some defenses mitigate the direct variant while preserving task performance, whereas the displayed active-attack results reveal substantial utility costs when mitigation becomes strong.”
- 读者需要记住防御异质性时，以直接路线的缓解与主动评价的实质缓解代价组织信息
- 省去四个防御名字，牺牲可复核对象清单；若这里是首次出现，须邻句列明受评对象

## V10　一段还是多段：完整局部组织的三种版本

共同任务：从所有权/权限差异进入发现，并说明方法族有不同条件。以下是写作分析中的概括段，非替代原论文引言；不会假称源本就采用某个组织。

A. 条件先行，适合第一次接触该场景的读者：
“In the studied VFL setting, participants contribute different features, but only one owns the labels. A participant without the labels controls only a partial model, so HFL privacy results do not automatically settle this setting. The study shows that trained local representations can nevertheless support label inference with limited auxiliary labels. A separate direct variant addresses the architecture without model splitting.”
- 先补所有权→权限→研究问题→两分支；四句各推进一个关系
- 成本是还没报数字；若本段承担总方案与评价，须后接相应证据

B. 发现先行，适合前文条件已经充分的读者：
“A partial model can still carry useful information about private labels. The study connects this finding to two representation-based variants: one uses the trained representation, and the other seeks to strengthen it. Their input and auxiliary-label requirements remain part of the claim. The direct variant concerns a distinct, unsplit architecture.”
- 以前文已成立的条件承载简洁发现，不重复业务例
- 第三句是分析性的提醒，适合教程/综述；正式论文宜把条件直接写进能力句，而非照抄元话语

C. 证据问题先行，适合讨论“到底证明了什么”的结果导读：
“The evaluation answers three different questions. BHI provides an application-grounded example of inference with few auxiliary labels; the random-initialization comparison tests the value of the trained representation; and the direct variant’s perfect result belongs to the unsplit setting and training samples. These results should be selected according to the claim being explained.”
- 将证据按判断归组，避免最高数字统治叙事
- 不再承担完整方法介绍；末句是编辑指导，不是原论文贡献

## V11　贡献的选材与收束：不要按模块数机械分项

A. 知识前景：“The study identifies label leakage as a privacy risk of the studied VFL setting, develops variants for different participant capabilities, and evaluates both their effectiveness and the limitations of candidate defenses.”
- 适于一段式文献定位；知识→工具→证据顺序保留完整价值
- 概括性高，不替代贡献列表中的具体完成物；“first”未继承

B. 条件覆盖前景：“Three variants expose different routes to label leakage under different information and architectural conditions. The evaluation establishes representative outcomes and explains why the representation-based variants work.”
- 适于前文已讲知识价值、尚需解释为何三类方法值得共存时
- 两句中未展开防御；若要涵盖完整原贡献集合，应另接其防御结果，不能静默宣称已全覆盖

C. 证据前景：“Experiments on real-world datasets demonstrate the reported attacks across the evaluated task and participant settings. Controlled comparison, visual analysis, and defense evaluation answer separate questions about representation value, behavior, and mitigation.”
- 适于最后评价贡献；将研究问题与证据类型连接
- 句中总体范围仍不意味着三路线×所有数据×所有人数全交叉；前文要已明示评价边界

## 使用后的局部回读

选A/B/C不是评分。检查前句是否已给本选项省略的条件；本句真正新增的是知识、范围、比较还是表达前景；后句是否兑现当前转折/目的；删除包装后模态是否变强；拆句后指代是否丢失；换证据后贡献问题是否随之改变。只有这些关系成立，短句才是有效压缩，长句才是必要解释。

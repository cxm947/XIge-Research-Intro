# VFL：完整51单元的句法、前景与信息依赖

来源是已校验的2022 USENIX正式稿；P/B沿用既有坐标。表中的“句法”是S类可核对观察，“前景/新内容”和“衔接职责”是I类编辑判断。两者分栏，不能由矩阵主句的位置直接推出科学重要性。P9是组织语，不计作科学句；本图不重编号，也不删原有51单元。

## 逐单位映射

| 单位 | 句法矩阵与从属/附加结构（S） | 信息前景与新内容（I） | 衔接职责（I） |
| --- | --- | --- | --- |
| P1.S1 | regulations被动issued；With+非限定结构前置；目的结构后置 | 外部数据使用约束；国家重视是因由 | 建立合作须面对的环境 |
| P1.S2 | company不能直接披露为主句；which承接后果 | 原始数据联合建模受阻 | 给下一句替代方案一个具体任务 |
| P1.S3 | FL的出现provides an alternative；To address前置 | 已有解决方式，不是本文方案 | 回答上一句困难 |
| P1.S4 | it allows共同训练；As短语给身份；by给方式；without给未发生的数据披露 | 共同建模能力和交换中间结果 | 既交现有价值，也预留间接泄露入口 |
| P1.S5 | companies put effort；into动名词补开发对象 | 工业投入 | 说明现实相关性，不添加隐私保证 |
| P1.S6 | systems被动developed；to date时间框架；such as举例 | 当时已存在的系统 | 将发展趋势具体化 |
| P2.S1 | FL can be categorized；According to给分类依据 | 样本/特征两个空间 | 为可比较定义先立共同轴 |
| P2.S2 | HFL is designed；where限定situations；while引出VFL对照，各带例子 | 两类在同样本/同特征上的相反条件 | while从属但信息对等；分类不是标签归属的充分定义 |
| P2.S3 | FL is claimed与but FL does leak对照；as说明被反驳理由 | 数据本地保留不足以排除间接泄露 | 从系统说明切到问题 |
| P2.S4 | studies have analyzed；such as列风险 | HFL已有知识基础 | 为VFL剩余作参照 |
| P3.S1 | VFL risks remain underexplored；However对照 | 2022研究覆盖不足 | 从已有答案收窄 |
| P3.S2 | VFL被动is being used；Moreover累加 | 工业使用增长 | 增加及时性，不独立构成gap |
| P3.S3 | One scenario is that…；which说明本文范围；that内features分布/labels单方拥有形成but对照 | 少数参与者、分散特征、单方标签 | 从VFL类别落到本文子场景 |
| P3.S4 | company might want to improve；with给资产条件；by给借用特征方式 | 标签方为什么需要合作 | 为标签/特征不对称赋予业务理由 |
| P3.S5 | role is providing与they ask两个并列主句；since给收益安排理由 | 特征提供方不当然取得标签或最终模型 | 解释各方正常所得 |
| P4.S1 | VFL has unique issues；As原因分句前置 | 架构、任务差异有隐私后果 | 接场景，引出具体资产 |
| P4.S2 | we focus on；In this paper范围附加语 | 本文选择标签泄露 | 正式命名研究对象 |
| P4.S3 | there is存在句；which对照HFL；where限定HFL | 单方标签与每方有标签样本的区别 | 把研究对象绑定所有权 |
| P4.S4 | ensuring…作主语，should be guarantee；as解释；or连接两种价值 | 应保护标签；资产价值或敏感性 | 任务价值不是抽象“安全很重要” |
| P4.S5 | participant may try；build/sell并列可能行动 | 获得私有标签可能造成什么损害 | 把资产性质转为潜在后果 |
| P5.S1 | it is more challenging；for adversary+不定式补判断内容；Compared with前置 | 这一场景下推断更难 | 用强参照制造知识问题 |
| P5.S2 | adversary controls/has access并列；which可接前述能力组合 | HFL既有攻击者可用资源 | 不以场景名称代替能力比较 |
| P5.S3 | adversary only controls/only has access；which补部分模型不可独立运行 | VFL权限较少 | 为反常发现交必要前提 |
| P6.S1 | we discover；that内vulnerability can be leveraged；Despite让步 | 受限权限下仍有风险 | 矩阵是发现动作，科学信息在补语 |
| P6.S2 | thorough study is imperative；for给应用关联 | 研究必要性回收 | 前文动机充分时可压缩 |
| P6.S3 | we find；that内bottom model might have ability | 本地表示本身的潜在推断能力 | 从宽漏洞收到解释对象 |
| P6.S4 | reason is that…；that内gradients help…；and thus can serve表面主语衔接含混 | 反馈训练→标签相关表示→底层模型预训练价值 | 编辑重述须显式写底层模型，不把梯度当模型 |
| P6.S5 | inference accuracy is determined by… | 表示能力这一解释变量 | 供主动变体后续回收；不是已穷尽所有决定因素 |
| P6.S6 | It is worth noting that…；嵌入能力命题；as long as句末条件 | 范围超训练集；所需本地输入可得 | 条件界定能力，非无关免责声明 |
| P6.S7 | gradients can also leak；In some special cases前置 | 另一信息通道 | 与表示机制分支，不共享全部条件 |
| P7.S1 | we propose a set；Based on findings前置 | 由发现得到方法族 | 总体交付，以下展开 |
| P7.S2 | we introduce passive…；To take advantage前置 | 已训练表示的用途 | 设计动机来自P6，而非算法名本身 |
| P7.S3 | we show that…；that内with少量标签条件、can…产物、in…方式 | 有辅助知识的模型补全能力 | 额外知识与完整产物都实际交代 |
| P7.S4 | Experiments show that…；嵌入with资源条件；dataset后的with修饰规模 | 少辅助标签下BHI任务成绩 | 两个with管辖对象不同；局部证据属于被动变体 |
| P7.S5 | we introduce active…；前置To/so as目的链；后置to交方法目的 | 增强同一表示变量以改善推断 | 从发现推设计，不凭空另造挑战 |
| P7.S6 | experiment shows that… | 主动变体改善结果 | 就近兑现设计目的 |
| P7.S7 | we use可视化；to explain目的；why嵌入间接问句 | 解释为何有效 | 证据功能不同于效果表 |
| P7.S8 | we introduce special direct…；which描述信息来源 | 一个单独机制分支 | Then是行文推进，不证明因果/强弱顺序 |
| P7.S9 | It is only applicable；when条件位于句末 | 非split架构是适用条件 | 条件句整体先于S10；不能称句内前置 |
| P7.S10 | experiments show that…；can achieve；on every evaluated dataset限制所报经验覆盖 | 受评设置的1.00成绩 | 由上一句架构条件管辖 |
| P8.S1 | we evaluate；Finally；冒号列四类 | 从风险转向防御评价 | 新研究问题而非第四攻击 |
| P8.S2 | we find that…；补语内though让步与they are not effective主断言 | 直接变体可缓解与表示型未解决并存 | 不把四防御/三攻击压成均匀结果 |
| P8.S3 | This motivates… | 防御研究剩余 | This回指刚给出的结果 |
| P9 | passive organizer summarized as follows | 无新科学命题 | 切换到贡献集合 |
| B1.S1 | we are first to evaluate；to best knowledge前置 | 历史首次评估定位 | 认识限定不是今日首次证书 |
| B1.S2 | we reveal/shed light并列 | 标签泄露知识 | 收窄B1宽评估对象 |
| B2.S1 | we present；including列三类 | 三类研究方法 | 重述总体交付，省细节 |
| B2.S2 | attacks cover settings | 覆盖不同条件的效用 | 使方法数量有任务意义 |
| B3.S1 | we evaluate…and achieve并列；with/under界定评价范围 | 多任务、现实数据、两/多方下的结果 | 不是每类攻击×所有设置全交叉证书 |
| B3.S2 | we share insights and present proofs | 机制解释产物 | “proofs”是源措辞；形式证明范围另见资格附记 |
| B3.S3 | we evaluate and find；that给结论；which给未来研究后果 | 防御局限 | 压缩句必须连P8及§6解读 |

## 段落与句群之间：哪一步依赖哪一步

1. P1需要先让读者看到联合建模的可用价值；P2才能反驳“原始数据不移动，所以所有信息安全”的直觉。若直接用P2开篇，熟悉FL的读者省时，但跨领域读者失去问题对象。
2. P2的样本/特征分类不能单独推出P3的单方标签。P3补的是使用场景与所有权，不是重复定义；删P3需在另一处补这两个条件。
3. P3讲正常分工，P4讲越界所得及其价值。将两段合并时可删业务例，不能删“谁持什么/谁不应得到什么”的因果接口。
4. P5的权限比较解释为什么既有HFL知识不自动回答新问题。具体先验思想仍可继承；剩余是任务与条件关系，不是声称所有先例无效。
5. P6.S1回答是否存在风险，S3–S5解释风险与表示能力的关系。S2的动机回收可按前文解释量取舍，S4因果不能被当冗余一起删。
6. P6.S6界定表示路线样本范围；S7开另一分支。换机制要换条件，不能让“任意样本”沿also/Then错误传递。
7. P7的真实安排是“总述→被动/局部结果→主动/局部结果/解释→直接/架构/结果”。这是源文安排；编辑可以建议目标稿分段，但不得伪造来源本就有独立方案段。
8. P8的防御结论重新要求保留联合模型用途，与P1的合作价值闭合。这个读者路径是编辑解释，不是作者宣称的唯一写作意图。
9. B1/B2/B3分别归组知识、方法覆盖、证据。B3承担多个职责因此更长；2/2/3只描述本源，不是可移植句数规则。

## 源句不理想时怎样保留观察

P6.S4的语法表面不够清楚是一个局部文本问题。科学语义可从§3.1和§3.3确认主体是底层模型，但不能倒过来把原句描述成已经具有清楚的同主语并列。P7.S9则无需修原句；需修的是旧分析把篇章顺序误写为句内前置。两种修复分别面对源表达和二级分析，不能混为“统一优化原文”。

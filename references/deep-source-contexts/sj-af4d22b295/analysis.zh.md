# VFL Label Inference：同一表示能力串起发现、变体和解释证据

## 来源与问题选择
读取[USENIX Security2022正式PDF](https://www.usenix.org/system/files/sec22-fu-chong.pdf)，1封面+18页、印刷1397–1414；散列f6a91e25e8f5436f49353162917e2a491d3c7c8c2005064931f5e3a8d0c52d69。原始重建曾直接取得PDF；本轮复用并校验该正式PDF，没有重新取得或替换来源。完整引言物理pp.2–3/印刷1397–1398；渲染p.3确认双栏，补读§2.2、§3.2、§5表2–4及§6–7。保留原重建实质内容及全部51单元的修订；完整首轮源审读与更正文件复读范围分别见检索元数据。法律表述按2022源动机分析，不作当前法律意见；攻击仅保留学术概念，不提供执行指导。

任务是仅持部分特征、未持标签的VFL参与者能否推断私有标签。强已有研究已揭示HFL梯度泄露，但VFL的完整模型访问缺失，需逐项检查可继承思想与新权限的相容性；§3.5明确继承既有标签相关思想，不能笼统写成所有HFL路线都不可迁移。本文用底层模型学得的标签相关表示作为新认识，再以表达能力连接被动补全、主动增强和可视化证据；直接梯度变体另有架构边界。引言并不采用全部方法讲完再给结果的统一节奏，而在每个变体附近插入对应条件和证据。

以下结构观察及作者因果可核对，读者路径解释属编辑推断，不推个人执笔者。

## 完整句群
### P1，p.1397：合作需要与信息交换
- P1.S1：With隐私重视前置，regulations被动issued给约束；外部动机而非本文技术保证
- P1.S2：particularly公司不能直接共享主句，which后置联合建模难；源文法律绝对化不当通用范句
- P1.S3：To-address前置、FL-emergence-provides给现有替代；不是新方法
- P1.S4：As技术属性前置、it-allows协作，by中间结果/without原数据形成机制与边界；⇒间接泄露入口
- P1.S5：全球公司put-effort说明采用价值；不证明安全
- P1.S6：to-date被动developed列平台；当时生态例子，不作现行能力核验

### P2，p.1397：别让本地数据等同隐私
- P2.S1：according-to样本/特征空间前置，FL被动分类；比较轴先交代
- P2.S2：HFL与while-VFL并列条件，各有业务例；样本/特征空间对照为后文架构比较作准备；单方标签所有权是P3另给的子场景条件
- P2.S3：claimed-to-preserve与but-actually-leak对照，as本地数据给被反驳推论；不是说FL没有任何隐私价值
- P2.S4：recent-studies主语、analyzed给HFL已有泄露类型；⇒VFL不是空泛重复

### P3，pp.1397–1398：由标签资产解释谁参与合作
- P3.S1：However-VFL-risk-underexplored缩小知识缺口
- P3.S2：Moreover采用增长给及时性；不能单凭流行构成技术贡献
- P3.S3：typical-scenario系表，few-participants与but标签单方持有；关系从句明确本文聚焦子场景
- P3.S4：for-example标签丰富但特征有限的公司主语、want-improve/by借其他业务特征；协作分工有经济理由
- P3.S5：other-participants角色系表提供特征，and收费，since最终模型归标签方；解释为何参与者不应自然拥有标签

### P4，p.1398左：架构差异变成被保护的资产
- P4.S1：As多方面不同前置，VFL-has独特问题；后句负责具体化
- P4.S2：we-focus-label-leakage明确窄任务
- P4.S3：in-architecture存在一个标签方，which对照HFL每方有标签；资源分布而非只模型名称不同
- P4.S4：ensuring-label-privacy作主语、should-guarantee，as资产/敏感性给价值依据
- P4.S5：Moreover对手may-build/sell并列损害；是潜在后果，不是实验已观察犯罪行为

### P5，p.1398左：承认对手更弱让新发现有信息量
- P5.S1：Compared-with-HFL前置，it-more-challenging；比较不是只说新场景重要
- P5.S2：HFL对手controls/accesses完整模型梯度，which给可利用性；已有攻击的能力条件
- P5.S3：However-VFL-only部分模型且cannot-independent、only部分梯度；⇒简单套用HFL为何不够

### P6，p.1398左末→右首：先解释漏洞存在，再命名攻击
- P6.S1：Despite挑战前置、discover主句、that-can-leverage给标签风险；回答较弱对手是否仍能获知
- P6.S2：thorough-study-imperative连接广泛采用；价值回收
- P6.S3：Specifically-find底层模型might-naturally具能力；对象落在训练留下的表示而非全局模型
- P6.S4：reason系表、during-training梯度help表示学习，thus预训练作用；作者核心因果
- P6.S5：accuracy被动determined-by表达能力；成为主动方案可调的变量
- P6.S6：worth-noting嵌能力覆盖新样本，as-long-as本地输入可得限制；超出训练集不等于任意人的全部标签
- P6.S7：some-special-cases前置，gradients-can-directly-leak；另一路径严格标特殊，不混入通用表示机制

### P7，p.1398右：方法与证据局部交错
- P7.S1：Based-on-findings前置、propose-family；总述
- P7.S2：To-use底层能力前置、introduce-passive；设计动机来自P6
- P7.S3：show后with少量辅助标签条件，can-fine-tune完整模型，in-semisupervised给机制层级；保留额外信息需求
- P7.S4：experiments-show内only70与F1 .7614并列大量训练样本；规模不对称解释攻击价值，非单最好数
- P7.S5：To-increase-expressiveness前置又so-as效果，introduce-active后to改变模型依赖；同一变量连接发现与设计
- P7.S6：experiment-shows改善；紧贴变体，避免效果归错方法
- P7.S7：Moreover-use可视化，to-explain-why；不同于效果验证，回应机制因果
- P7.S8：Then-introduce-special-direct，which给梯度来源；机制与前两种分离
- P7.S9：It-is-only-applicable为语法主句，when非split条件位于句末；本句在篇章上先于下一句完美数值，不是句内条件前置
- P7.S10：experiments-show 1.00、on-every-evaluated限定；不是所有VFL都完美泄露
段落把每个局部问题、变体和证据挨近，减少读者把1.00误给被动攻击或把70辅助标签误给直接攻击的风险。可迁移的是绑定条件、机制和结果，不是每个方法都要一模一样的句长。

### P8/P9，p.1398右：防御结果是研究未闭合部分
- P8.S1：Finally-evaluate列四防御；改变研究问题到缓解
- P8.S2：find后though某些缓解直接攻击，主句不能有效防另外两类；保留重要异质性
- P8.S3：this-motivates更好防御；不是凭空未来工作
- P9：贡献引导，无新科学断言

### B1–B3，p.1398右：完整贡献
- B1.S1：to-best-knowledge限定首次隐私风险评估；当时定位，不能跨年照搬
- B1.S2：reveal/shed-light主干给标签泄露具体知识；从宽评估落窄发现
- B2.S1：present-three-types、including列直接/被动/主动；命名汇总不重复执行步骤
- B2.S2：these-attacks-cover多种设置；三类的价值是覆盖不同能力条件
- B3.S1：evaluate任务/真实集/两与多参与者，and-achieve结果；范围说明先于总评
- B3.S2：further-share机制认识与present-proofs并列；除成效还有理解产物
- B3.S3：also-evaluate防御、find无效、which未来方向；这里压缩了P8限定，转用时须保留变体差异
2/2/3句的集合依次知识、攻击族、经验/机制/防御。B3最长因它收多个证据责任；有P7局部结果后列表可以不再抄F1和accuracy。

## 结果池重开：条件是代表性的组成部分
表2 BHI有70辅助标签，.7614为训练集F1，测试集为.7519；主动相应.7824/.7673。引言选择医疗、少标签和大训练池，突出私密资产与低额外信息成本，比最高视觉任务准确率更贴风险。不能将F1改称accuracy或不带集合地称新样本推断成绩。

表3与随机初始化半监督比较更直接证明信息来自VFL训练：相同少标签下，预训练底层表示明显更有用。若把这组放入引言，会加强因果解释而非仅风险规模；当前P7优先应用冲击，再把对照留正文。表4原任务性能变化小，是隐蔽性/采用风险的补充，但未在引言单列；若研究重点是系统破坏，应该选择另一组结果。

§6显示部分防御能把直接攻击从1.0明显降低，正文同时讲效用代价；被动/主动与表示学习的相关性使保护更难。贡献末句的总括不宜独立挪用成所有防御对所有攻击无效。本文DNN与有用本地特征、辅助标签及架构访问范围是实际限制，未来工作明确未测所有VFL模型种类。

## 表达选项
编辑选项，非源句或验证增益：
1. “The participant lacks the complete model, yet training still equips its local representation with label-related information.” 一个yet连接较弱能力与残余风险，凸显研究信息量
2. “The passive result identifies representation quality as the variable that the active design then strengthens.” 显式给发现→设计桥，较纯算法介绍更易理解，但应以实验解释支持
3. “Perfect inference belongs to the unsplit architecture studied here; the representation-based attacks address different settings.” 将最易误传数字绑定架构，略增篇幅换清楚归属
可迁移重点是用同一变量串发现、方法变体和验证。若机制不同，不应为故事整齐强迫所有方法共享一个洞察。

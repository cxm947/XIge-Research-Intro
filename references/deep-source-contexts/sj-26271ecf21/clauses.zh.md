# UNIFUZZ：完整句/问句与条件化选择分析

- coordinate_policy: 本轮U坐标以P2三个问题计入S2–S4；old_map_coordinate显式连接旧图Q坐标。编号不是源论文编号。源句不可仅依编号定位。
- coverage: 完整Introduction 46个句/问句单元；8条原有子句分析原值保留，38条增量；贡献标题不作为独立句单元但在profile完整保留职责。计数只为完整性，不为质量。
- alternative_policy: conditioned_editorial_alternative包含迁移、压缩、证据依赖变化或力度调整，并非默认与源句等价；仅equivalent_reformulation字段声称局部命题等价，且随附保留/改变项。

## P1.S1

- old_map_coordinate: P1.S1
- retained_clause_analysis: 主句fuzzing is testing定义领域，that从句给执行动作及目标，by短语交输入方式；不是先铺术语再另句重复定义。
- interpretation_status: 保留的语法分析；分析范围与边界见配套 analysis.zh.md 和 evidence.zh.md。
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 61
    - 62
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf

## P1.S2

- old_map_coordinate: P1.S2
- source_statement_paraphrase: 研究发展
- syntax_and_information_focus: 时间状语先框定增长窗口；存在/涌现谓语把注意力放在工作数量，领域并列给后文证据分组。没有理由从句，尚未声称研究质量。
- reader_dependency_and_new_premise: 定义仅回答是什么；本句让下一步比较需求有足够规模对象。
- selection_and_counterfactual: 若立即报平台，读者仍不知道横向评价为何值得单独研究；若堆新术语则把对象数量误换成技术清单。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 62
    - 64
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 面向已熟悉领域的受众，可省去泛化增长句，直接用采用与研究分布证据起笔；不能因此省去比较决策。
- alternative_relation: conditional_omission_and_compression

## P1.S3

- old_map_coordinate: P1.S3
- source_statement_paraphrase: 工业使用
- syntax_and_information_focus: 行业状语收窄主语集合；厂商是施事、采用是主干、找错是不定式目的。例举组织给应用落点，不承担因果效果验证。
- reader_dependency_and_new_premise: 数量态势之后给真实使用场景，使实践性能成为值得回答的问题。
- selection_and_counterfactual: 厂商名不是权威替代实证；原句选使用行为而非声誉形容词。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 64
    - 66
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若目标受众属于另一应用群体，改选该群体确实依赖技术的决策场景；保留“谁为哪项任务使用”，不照搬厂商。
- alternative_relation: transfer_to_other_audience

## P1.S4

- old_map_coordinate: P1.S4
- source_statement_paraphrase: 工具生态
- syntax_and_information_focus: 转换短语标记另一证据面；平台为主语，托管为谓语，仓库数量为宾语信息。没有从句把仓库数推成可用工具数。
- reader_dependency_and_new_premise: 工业采用只能证明有需求，不能说明研究者面临多少可选实现。
- selection_and_counterfactual: 代码可见性在此被提出，P3才撤销从可见直接推向可用的捷径。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 66
    - 68
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若可用性已严核，可写经验证实现数量；若只是检索仓库，应保留仓库单位，不换成可比较系统数量。
- alternative_relation: evidence_dependent_unit_and_claim_change

## P1.S5

- old_map_coordinate: P1.S5
- source_statement_paraphrase: 学术规模
- syntax_and_information_focus: 学术场域前置；发表数量承接另一侧生态；起始年份与数据库归属约束数字出处和时间。被动语态凸显产物而非作者。
- reader_dependency_and_new_premise: 工具繁多与研究繁多不是同一证据；后者使技术方向选择成为研究共同体的问题。
- selection_and_counterfactual: 不应把累计数量写成增长率；也不应把数据库收录写成质量认证。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 67
    - 68
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 已有强问题证据的短引言可把学术规模压到前句；如果数字承担论证，保持检索口径与日期。
- alternative_relation: conditional_compression

## P2.S1

- old_map_coordinate: P2.S1
- retained_clause_analysis: Despite前置承认繁荣，there are主句推出尚未解决问题；后续三问把抽象缺口分成读者决策。
- interpretation_status: 保留的语法分析；分析范围与边界见配套 analysis.zh.md 和 evidence.zh.md。
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 69
    - 70
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf

## P2.S2

- old_map_coordinate: P2.Q1
- source_statement_paraphrase: 实践表现问题
- syntax_and_information_focus: 有限动词疑问句把未知放在表现，实践情境修饰评价场域，而非要求解释内部机制。
- reader_dependency_and_new_premise: 从有许多工具推进到使用者缺哪一种知识，先给最直接的决策入口。
- selection_and_counterfactual: 问句不是实验指标；后文需要把实践表现拆成可比较维度。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 70
    - 71
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若新稿需要从开放问题转成陈述式缺口，可写“尚缺能支撑实际选择的比较证据”；这是从问句到证据不足断言的迁移，不是等价换句。使用前须核实已有研究确实缺少相应证据，且后文工作确实回答该决策。
- alternative_relation: transfer_question_to_gap_assertion

## P2.S3

- old_map_coordinate: P2.Q2
- source_statement_paraphrase: 比较准则问题
- syntax_and_information_focus: 这是 how + 不定式的省略式问句，不宜机械标成完整主句加从句；方式是焦点，评价条件限定何种比较才有用。
- reader_dependency_and_new_premise: 前问缺表现答案，本问补答案的可信产生方式，使平台本身成为研究对象。
- selection_and_counterfactual: 若只说谁更好，读者会将平台当排行榜；该句改问判定准则。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 71
    - 73
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 读者已有统一准则时可改成“现有准则在本情境失效于……”；没有失效证据时不可伪造这一步。 这会新增“已有准则失效”的命题，属于需要新证据的迁移方案，不能作为原问句的同义替换。
- alternative_relation: evidence_dependent_new_failure_claim
- equivalent_reformulation:
  - text: 在一组公平、全面的性能指标下，如何对不同fuzzer进行比较？
  - invariants_and_changes: 保留比较方式之问、公平与全面的指标条件以及不同工具对象；只前置条件，不新增准则失效，也不把问题收窄为指标选择本身。
  - context_condition: 需要读者先注意比较条件时使用；若前文尚未解释指标为何重要，仍须依赖后续论证。
  - status: 局部命题保义候选

## P2.S4

- old_map_coordinate: P2.Q3
- source_statement_paraphrase: 未来技术选择问题
- syntax_and_information_focus: 疑问主语是一类技术；并列谓语先问潜力，再问是否值得推广，描述与规范判断共处而不等同。
- reader_dependency_and_new_premise: 可信比较的价值出口从当下选工具扩到后续研究投入。
- selection_and_counterfactual: 原文并未因提出此问就识别出普遍最优 primitive；C2的条件性结果限制直接排行榜式答案。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 72
    - 73
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 资源论文可问“哪类后续设计能被这些证据支持”；只有完成机制隔离实验才能进一步归因到具体 primitive。
- alternative_relation: transfer_research_decision_scope

## P2.S5

- old_map_coordinate: P2.S2
- source_statement_paraphrase: 转入不足原因
- syntax_and_information_focus: 转折连接前问；主语是既有研究而非技术本体，谓语是否定回答能力；后置原因预告给下列并列项留位置。
- reader_dependency_and_new_premise: 将开放问题连接到证据缺陷，而不是把“尚有人问”当成空白证明。
- selection_and_counterfactual: 概括批评力度大，可信性依赖紧接的证据；不能单独抽成所有先前工作失败的通用断言。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 73
    - 74
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若文献覆盖有限，改成被核到的子集和具体未答判断；不能靠换强动词扩大覆盖。
- alternative_relation: evidence_dependent_scope_narrowing

## P2.S6

- old_map_coordinate: P2.S3
- source_statement_paraphrase: 实验可信度不足
- syntax_and_information_focus: 序数词给并列原因第一项；主干是研究没有恰当且充分地实验，目的不定式点出可信结果。恰当与充分并列，不是一词修饰另一词。
- reader_dependency_and_new_premise: 开放问题的首个阻塞被定位在证据产生过程。
- selection_and_counterfactual: 下句给重复不足，本句不能缩成重复次数少，否则消掉环境可比性等协议层问题。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 75
    - 76
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若稿件只有一个已核的实验缺陷，直接写该缺陷及它影响的判断；无需为三分结构补造其它不足。
- alternative_relation: evidence_dependent_claim_narrowing

## P2.S7

- old_map_coordinate: P2.S4
- source_statement_paraphrase: 重复不足的例证
- syntax_and_information_focus: 例证标记将概括落地；形式主语结构包裹观察命题，内层使役关系把重复不足接到结果不稳。
- reader_dependency_and_new_premise: 把“不充分”变成具体可信度风险，使C1之后的重复比较有理由。
- selection_and_counterfactual: 原文修辞把随机且不可靠一起写；解释时应区分过程本有随机性与重复不足未能稳定估计，不声称少跑几次创造了随机机制。
- body_evidence:
  - I
  - B4
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 76
    - 77
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 需要更精确时，可写“重复不足会使结果受运行波动影响，难以稳定比较”；这是编辑澄清，不冒充逐词翻译。
- alternative_relation: causal_clarification_not_literal_equivalence

## P2.S8

- old_map_coordinate: P2.S5
- retained_clause_analysis: 主句描述直接引用旧结果不重跑，which评价unfair，as从句交环境差异原因；理由附在同句避免“不可比”无支撑。
- interpretation_status: 保留的语法分析；分析范围与边界见配套 analysis.zh.md 和 evidence.zh.md。
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 78
    - 81
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf

## P2.S9

- old_map_coordinate: P2.S6
- source_statement_paraphrase: 基准偏差问题
- syntax_and_information_focus: 主句以评价为主语，把偏差置于断言中心；原因介词短语指出缺统一基准。
- reader_dependency_and_new_premise: 即使运行协议一致，比较对象选取仍能影响结论。
- selection_and_counterfactual: 统一只降低一种差异，不能逻辑保证代表性；后续两句补对象差异与可能偏好。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 82
    - 83
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若对照任务本应不同，不强制统一所有输入，而应说明分层/匹配后可比较的单位；当前论文的统一方案有其目标范围。
- alternative_relation: alternative_comparative_design

## P2.S10

- old_map_coordinate: P2.S7
- source_statement_paraphrase: 对象选择差异
- syntax_and_information_focus: 简单主句把选择差异单独突出；不同论文是比较范围，无定语从句堆细节。
- reader_dependency_and_new_premise: 前句宣布偏差，本句先给可观察前提，让下一句的推断不是空跳。
- selection_and_counterfactual: 差异并不自动证明偏置；因此该句本身只承担异质事实。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 83
    - 84
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 材料支持时可提供对象重叠率等更直接证据；没有系统盘点就不把文字概括改成量化普遍性。
- alternative_relation: evidence_substitution

## P2.S11

- old_map_coordinate: P2.S8
- source_statement_paraphrase: 可能偏好推断
- syntax_and_information_focus: 因果衔接后使用形式主语及可能性补语；从句的工具—程序关系是推断核心。
- reader_dependency_and_new_premise: 由对象差异推到性能依赖对象，给跨程序比较建立价值。
- selection_and_counterfactual: 可能性限制很关键：发现无全域赢家仍不能证明故意选择有利程序。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 84
    - 86
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 可换成“这些结果尚不能排除程序选择的影响”；在没有因果设计时，两种表达都保持不确定归因。
- alternative_relation: cautious_reframing_of_attribution

## P2.S12

- old_map_coordinate: P2.S9
- source_statement_paraphrase: 指标双重不足
- syntax_and_information_focus: 第三项为系词否定，适配性与完整性并列；评价对象短语限定指标用于什么。
- reader_dependency_and_new_premise: 前两类是实验过程与对象，这里切到观测如何代表目标。
- selection_and_counterfactual: 不适配与不完整需要不同修复：换更有意义的量，以及增补不同判断轴。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 86
    - 87
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若现有指标适配但覆盖不足，只写后一问题；不要保留双形容词以制造全面感。
- alternative_relation: evidence_dependent_claim_narrowing

## P2.S13

- old_map_coordinate: P2.S10
- retained_clause_analysis: it is inappropriate判断代理量，as原因从句给crash/bug差异；长句承载比较规则及为什么，后续工具建设才有目标。
- interpretation_status: 保留的语法分析；分析范围与边界见配套 analysis.zh.md 和 evidence.zh.md。
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 87
    - 89
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf

## P2.S14

- old_map_coordinate: P2.S11
- source_statement_paraphrase: 资源维度缺失
- syntax_and_information_focus: 追加连接词明确它是独立缺项；多数研究为主语、未评资源消耗为谓语，量词限制指控范围。
- reader_dependency_and_new_premise: 即使bug数量已更可靠，用户仍不知道得到它花费多少资源。
- selection_and_counterfactual: 它没有说资源是bug质量，也没有要求统一折算为一个分数。
- body_evidence:
  - I
  - B5
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 2
  - printed_page: 2777
  - web_line_range:
    - 89
    - 91
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若使用者有固定成本约束，把该约束直接接到选择后果；若不关心成本则说明不纳入的任务理由，而非例行加指标。
- alternative_relation: task_condition_transfer

## P2.S15

- old_map_coordinate: P2.S12
- source_statement_paraphrase: 综合平台需要
- syntax_and_information_focus: 推论标记汇合三个原因；存在结构突出研究需要，行动不定式给任务，平台介词短语给实现条件。
- reader_dependency_and_new_premise: 把分散失效转换成一个可承担的研究任务，准备P3建设条件。
- selection_and_counterfactual: 紧迫是作者修辞判断，并非另有外部时间期限；综合也尚不是已兑现效果。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page:
    - 2
    - 3
  - printed_page: 2777–2778
  - web_line_range:
    - 91
    - 93
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 可将急迫形容压掉并明确“要支撑X判断，需要Y评测条件”；替换前确认X来自已建立的价值出口。
- alternative_relation: urgency_strength_reduction

## P3.S1

- old_map_coordinate: P3.S1
- source_statement_paraphrase: 从不足到建设
- syntax_and_information_focus: 动名词评价活动为主语；需要克服挑战为主干。它没有提出第四类文献缺口，而是转到实施负担。
- reader_dependency_and_new_premise: P2说明现有知识不可靠，P3说明获取可靠知识为什么不是简单重跑。
- selection_and_counterfactual: 该句可压缩，但不能删除整段后把资源建设看成仅下载代码。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 94
    - 95
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 短引言可在P2每类缺陷后就接对应必要工作，不必照搬双段结构；保持证据缺陷与建设动作的逻辑区别。
- alternative_relation: structural_reorganization

## P3.S2

- old_map_coordinate: P3.S2
- retained_clause_analysis: although承认开源，主句实际可用性有限，which结果从句递进到复现/比较受阻；代码开放与研究可复用被分开。
- interpretation_status: 保留的语法分析；分析范围与边界见配套 analysis.zh.md 和 evidence.zh.md。
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 96
    - 98
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf

## P3.S3

- old_map_coordinate: P3.S3
- source_statement_paraphrase: 可用性操作要求
- syntax_and_information_focus: 推论连接词承上；形式主语加必要性，两个不定式动作并列，测试先于增强但语法未给流水线保证。
- reader_dependency_and_new_premise: 前句解释不可用影响比较，本句让修复劳动成为必要研究条件。
- selection_and_counterfactual: 测试不是只证明可启动，增强也不保证所有缺陷修复。
- body_evidence:
  - I
  - B2
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 98
    - 99
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若只做了检查，写测试与报告；若做了修复，保留范围和验证状态，不把待修项包进完成式。
- alternative_relation: action_scope_conditioning

## P3.S4

- old_map_coordinate: P3.S4
- source_statement_paraphrase: 基准要求
- syntax_and_information_focus: 序数词开启新的建设对象；评价为主语，被动情态将要求放在程序条件上。
- reader_dependency_and_new_premise: 工具能运行之后仍缺承载有意义比较的输入对象。
- selection_and_counterfactual: 此处只命名要求，正文承担何谓现实可用的定义；单句抽出容易空泛。
- body_evidence:
  - I
  - B1
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 99
    - 100
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若受众不熟悉该形容词，在附近补一条会改变评测结果的性质，而不是再加同义形容词。
- alternative_relation: evidence_dependent_concretization

## P3.S5

- old_map_coordinate: P3.S5
- source_statement_paraphrase: 已有基准未满足
- syntax_and_information_focus: 简短主谓补语句带文献来源，作用是标识残余，而非给证据细节。
- reader_dependency_and_new_premise: 防止读者反问现成基准为何不可直接使用。
- selection_and_counterfactual: 引用不能代替在新稿核查适用范围；本句对读者耐心的要求由后续§2承担。
- body_evidence:
  - I
  - B1
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 100
    - 101
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若新稿后文不提供诊断，应合并一句具体不满足条件；不能只复制“不满意”。
- alternative_relation: evidence_dependent_specificity_increase

## P3.S6

- old_map_coordinate: P3.S6
- source_statement_paraphrase: 基准条件收束
- syntax_and_information_focus: 评价可靠性置于主语修饰语，推论副词把基准建设变成前述目标的条件。
- reader_dependency_and_new_premise: 在“应该用”与“现有不够”之后完成需求闭合。
- selection_and_counterfactual: 本句确有P3.S4的可压缩重叠；不是每句因存在就必须保留原长度。
- body_evidence:
  - I
  - B1
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 101
    - 101
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 短稿可把S4–S6合成要求、未满足处及后果一条因果关系；长稿若逐项组织挑战可保留节奏。
- alternative_relation: conditional_compression

## P3.S7

- old_map_coordinate: P3.S7
- source_statement_paraphrase: 指标体系要求
- syntax_and_information_focus: 第三项采用被动强情态，评估活动前景化；基于什么置于介词补语。
- reader_dependency_and_new_premise: 补全从运行对象到判定维度的条件集合。
- selection_and_counterfactual: 必须是此文评测目标下的规范，不是任何实验都要六种指标。
- body_evidence:
  - I
  - B3
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 101
    - 103
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 先问要支持的选择有哪些，再写足以区分它们的指标集合；不先锁定数量。
- alternative_relation: task_condition_transfer

## P3.S8

- old_map_coordinate: P3.S8
- source_statement_paraphrase: 指标不足后果
- syntax_and_information_focus: 转折后主句诊断不足与粗糙；非限定分词结构补判断不完整的结果。
- reader_dependency_and_new_premise: 把“综合”从好听属性转成避免遗漏判断的具体理由。
- selection_and_counterfactual: 结果分词容易掩盖论证，应能由P2代理关系和正文例证支持；不能把所有粗指标都判为无用。
- body_evidence:
  - I
  - B3
  - B5
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 103
    - 104
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 可直接点出会混淆的两个对象或结果；若仅增加维度无法解决操作化误差，需要分别写修复。
- alternative_relation: evidence_dependent_concretization

## P3.S9

- old_map_coordinate: P3.S9
- source_statement_paraphrase: 扩充动作收束
- syntax_and_information_focus: 推论标记及形式主语强调行动重要性；不定式结构是与形式主语it对应的后置主语，内容为增补指标；目的短语回扣综合评价。它不是表语形容词important的宾语。
- reader_dependency_and_new_premise: 三类挑战都落到可交付操作，P4才有“回答上述”的锚点。
- selection_and_counterfactual: 增补不是指标越多越好；其价值需要在C2中通过改变认识兑现。
- body_evidence:
  - I
  - B3
  - B5
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 105
    - 106
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 如果新增指标不改变任何决策，删除该宣称或解释其诊断用途；不为凑平行项保留。
- alternative_relation: claim_removal_or_evidence_addition
- equivalent_reformulation:
  - text: 扩充性能指标对综合评价很重要。
  - invariants_and_changes: 把后置的不定式活动改作话题，保留重要性判断及综合评价目的，不增加指标数或效果保证。
  - context_condition: 读者已知道为何需要综合评价时可用；本句不能独自证明任何指标扩充都有效。
  - status: 局部命题保义候选

## P4.S1

- old_map_coordinate: P4.S1
- source_statement_paraphrase: 平台总回答
- syntax_and_information_focus: 目的状语前置承接问题；作者设计实现为主句；同位语给产物类型及取向，不是另一个证据从句。
- reader_dependency_and_new_premise: 给读者唯一主产物入口，然后贡献段展开未介绍的具体工作。
- selection_and_counterfactual: 总回答没有逐模块细节，因此C1长不是把前文重说一遍；“开源”只是其中一个属性。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 107
    - 108
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 已有独立方案总览时可缩短C1；没有时至少保留贡献理解所需的接口与判定关系。
- alternative_relation: conditional_compression

## P4.S2

- old_map_coordinate: P4.S2
- source_statement_paraphrase: 贡献路标
- syntax_and_information_focus: 概括状语加作者—贡献主干，只承担导航，没有新的实验发现。
- reader_dependency_and_new_premise: 提示后续由建设、比较所得、方法学认识分别记账。
- selection_and_counterfactual: 路标不需要被拔高为实质论证；删掉可不损事实，但列表的组织入口会变弱。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 108
    - 109
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 连续叙述型引言可取消编号导语；替代条件是读者仍能分清三种研究所得。
- alternative_relation: structural_format_change

## C1.S1

- old_map_coordinate: C1.S1
- retained_clause_analysis: 主句命名并定义平台，which关系从句承载35/20/6规模；一开始先交产物，再让后六句拆解怎样可用。
- interpretation_status: 保留的语法分析；分析范围与边界见配套 analysis.zh.md 和 evidence.zh.md。
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 110
    - 113
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf

## C1.S2

- old_map_coordinate: C1.S2
- source_statement_paraphrase: 逐工具可用性接口
- syntax_and_information_focus: 逐项范围状语先限定35的处理单位；测试与提供配置并列主干；易部署是用途短语。
- reader_dependency_and_new_premise: 上一句只有规模，这句首次交付让规模可被使用的承诺及接口。
- selection_and_counterfactual: 每项配置比“平台可复现”笼统断言更可核验；但能启动不能推出比较结论可复现。
- body_evidence:
  - I
  - B2
  - B4
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 113
    - 115
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若新资源交付的是容器镜像、脚本或环境描述，写实际可执行接口与覆盖范围；不必强行用Dockerfile。
- alternative_relation: implementation_interface_transfer

## C1.S3

- old_map_coordinate: C1.S3
- source_statement_paraphrase: 缺陷修复与报告
- syntax_and_information_focus: 并列发现/修复是主干，括号限制完成程度；关系从句再交向开发者报告的去向。
- reader_dependency_and_new_premise: 给“测试可用性”增加实质发现与改进，而不是只做包装。
- selection_and_counterfactual: 括号承担边界，删掉会虚增修复完成量；报告不自动等于上游确认全部修复。
- body_evidence:
  - I
  - B2
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 115
    - 117
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 可拆成“发现X，修复其中已验证的一部分，并报告其余/全部”，但只有记录支持时才能写清这些子集；无精确子集则保留部分限定。
- alternative_relation: evidence_dependent_disambiguation
- equivalent_reformulation:
  - text: 我们发现了15余处缺陷，对其中一部分进行了修复，并已将这些缺陷报告给开发者。
  - invariants_and_changes: 保留发现/报告与部分修复，不把全部发现计为全部修复；重排报告信息以让完成范围更清楚。
  - context_condition: 需要将完成程度说得清楚时使用；保留作者作为发现、修复及报告的施事，不把上游已全部修复的状态加进去。
  - status: 局部命题保义候选

## C1.S4

- old_map_coordinate: C1.S4
- source_statement_paraphrase: 程序使用上下文
- syntax_and_information_focus: 对象范围前置与上一工具段落平行；平台为主语，配套信息为宾语，举例短语限定信息种类，目的不定式解释可用性。
- reader_dependency_and_new_premise: 工具侧可运行不意味着目标程序的版本、参数与输入接口已明确。
- selection_and_counterfactual: 安装和参数这些朴素细节成为资源贡献，因为缺它们读者不能重建比较条件。目的不能独立证明全部条件已满足。
- body_evidence:
  - I
  - B1
  - B4
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 117
    - 120
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 可用“为每个目标提供版本、输入与执行配置”一类接口清单；选能改变运行行为的细节，别把README页数当贡献。
- alternative_relation: interface_selection_transfer

## C1.S5

- old_map_coordinate: C1.S5
- source_statement_paraphrase: 观测到判断的工具接口
- syntax_and_information_focus: 主句实现工具，不定式交用途；including后的并列动名词列出分析任务，非穷尽标记不表示整个过程自动完成。
- reader_dependency_and_new_premise: 从运行资源跨到结果解释资源；否则P2关于代理量的核心批评没有对应解法。
- selection_and_counterfactual: 去重/匹配/严重性不是同义动作：归并单位、关联已有漏洞记录、评价后果分别改变读者判断。
- body_evidence:
  - I
  - B3
  - B6
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 120
    - 122
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 一般资源论文可按“原始输出→判定单位→外部语义/后果”组织；保留人工审核与误差范围，不宣称输出即真值。
- alternative_relation: task_condition_transfer

## C1.S6

- old_map_coordinate: C1.S6
- retained_clause_analysis: CVE库主句交具体机制，which从句交减少人工价值；不把“数据库”本身冒充用户收益。
- interpretation_status: 保留的语法分析；分析范围与边界见配套 analysis.zh.md 和 evidence.zh.md。
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 122
    - 124
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf

## C1.S7

- old_map_coordinate: C1.S7
- source_statement_paraphrase: 评价维度接口
- syntax_and_information_focus: 主句提出指标集合；冒号给完整类别列举；关系从句放使用价值。主干是可交付判据，价值尾句依赖名单的互补性。
- reader_dependency_and_new_premise: 前句解决匹配负担，本句完成如何判断工具表现的显式规则入口。
- selection_and_counterfactual: 六类是本研究覆盖，不是六个通用槽位或固定权重；覆盖仍有路径探索职责，不因它不等于bug数而被删。
- body_evidence:
  - I
  - B3
  - B5
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 124
    - 127
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若只需某决策，列真正区分它的维度并说明关系；若采用多指标，明确互补、辅助或权衡，而非默认平均成总分。
- alternative_relation: decision_scope_narrowing

## C2.S1

- old_map_coordinate: C2.S1
- source_statement_paraphrase: 比较研究范围
- syntax_and_information_focus: 句首非限定分词说明平台是手段；作者开展比较为主句；不定式给任务，数量与类型约束对象集合。
- reader_dependency_and_new_premise: 资源可用还未形成研究知识；本句首次报告已做的实证使用及其范围。
- selection_and_counterfactual: 不可将35集成规模搬成35全量实验。8和coverage-based不是装饰，直接限制比较结论。
- body_evidence:
  - I
  - B4
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 128
    - 129
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 写“在资源支持的可比较子集上开展……”，随后解释选择依据；若全量不适配，坦率区分资源覆盖和验证覆盖。
- alternative_relation: evaluation_scope_transfer
- equivalent_reformulation:
  - text: 依托UNIFUZZ，我们开展广泛实验，比较八种知名的覆盖型fuzzer。
  - invariants_and_changes: 保留平台手段、已开展广泛实验、八种、知名性与覆盖型范围；不把prominent扩成未经证明的代表性，也不把35个集成范围混入。
  - context_condition: 适用于独立贡献句；若前句已给平台手段，可删除开头，但需保留实验范围。
  - status: 局部命题保义候选

## C2.S2

- old_map_coordinate: C2.S2
- source_statement_paraphrase: 跨对象发现
- syntax_and_information_focus: 结果作为主语，that补语给核心观察；句尾关系结构把它同既有结论对照。原句which are的语法邻接有歧义，语义上比较的是结果/结论，不是程序与结论。
- reader_dependency_and_new_premise: 从“做了实验”进入改变读者认识的发现；否定全称胜出让特定条件进入选择。
- selection_and_counterfactual: 不能改成所有工具等效，也不能改成任何程序上都没人更好。读者只可得到当前测试集合没有通吃者。
- body_evidence:
  - I
  - B4
  - B5
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 129
    - 132
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 需要明晰时拆成两句：先说在测试范围内的交叉表现，再说明它怎样不同于已核的先前结论；“不同”不代替原因调查。
- alternative_relation: structural_disambiguation_preserving_main_proposition
- equivalent_reformulation:
  - text: 没有一个被测fuzzer能在所有测试程序上都超过其它工具；这一结果与它们原论文的结论不同。
  - invariants_and_changes: 保留没有跨全部程序的普遍胜者及与原论文的结果对照；将附着不清的关系结构拆为独立句。
  - context_condition: 保留本轮测试集合；不能改成工具等效，或证明旧结论故意失真。
  - status: 局部命题保义候选

## C2.S3

- old_map_coordinate: C2.S3
- source_statement_paraphrase: 观察的批评性含义
- syntax_and_information_focus: 前指名词接回发现；揭示为主干，that内容中may保留可能性。
- reader_dependency_and_new_premise: 说明发现为何超出一张新排行榜，返回P2的比较有效性问题。
- selection_and_counterfactual: 主句动词强、嵌套情态弱并存，必须保留命题内部的力度；结果差异不能单凭句法证明他人主观动机。
- body_evidence:
  - I
  - B4
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 131
    - 132
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 可写“这提示先前排名可能依赖评价条件”；若要指认具体偏差来源，另需对条件的控制证据。 此替代弱化并重定了归因：条件依赖不等于源句提出的可能主观性/偏差，因此不标为等价改写。
- alternative_relation: weaker_attribution_reframing

## C2.S4

- old_map_coordinate: C2.S4
- retained_clause_analysis: 主句experimental results reflect认识，that从句给单指标片面，which最后归结综合指标重要；观测→判断→研究价值同句连贯。
- interpretation_status: 保留的语法分析；分析范围与边界见配套 analysis.zh.md 和 evidence.zh.md。
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 132
    - 134
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf

## C3.S1

- old_map_coordinate: C3.S1
- source_statement_paraphrase: 方法学所得转场
- syntax_and_information_focus: 来源介词短语把知识挂到评测；主句仍是所得概括，未来研究为适用方向。
- reader_dependency_and_new_premise: C2谈工具比较，本句另开“如何评价”的认识层次，让下一发现不会像杂项附录。
- selection_and_counterfactual: 重要性形容词本身无证据力；价值在后面命名因素与展示判断变化。
- body_evidence:
  - I
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 135
    - 137
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 可直接以被忽略因素开段，省去自评句；若需区分研究产品层级，保留简洁过渡。
- alternative_relation: conditional_omission

## C3.S2

- old_map_coordinate: C3.S2
- source_statement_paraphrase: 新因素命名
- syntax_and_information_focus: 主句作者发现因素；限制性从句给影响关系；例举插桩/分析工具把抽象因素具体化。
- reader_dependency_and_new_premise: 让读者知道不稳定不只来自随机种子或目标程序，而可能来自观察和执行条件。
- selection_and_counterfactual: 源句说performance，下一句说assessment；编辑解释必须区分真实可触发行为改变与分析工具改变可见输出，不把两者压成纯排行榜噪声。
- body_evidence:
  - I
  - B7
  - B8
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 137
    - 139
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 可写“执行构建与结果分析设置都可能改变可观察结果”；只有研究隔离后，才把其中效应归到算法发现能力。
- alternative_relation: body_grounded_interpretive_reframing

## C3.S3

- old_map_coordinate: C3.S3
- source_statement_paraphrase: 影响量级与对象
- syntax_and_information_focus: 结果为证据主语；that补语中even突出小改动/大影响不对称，情态can限定可发生性；影响对象明确转到评价。
- reader_dependency_and_new_premise: 前句只知有哪些因素，这句说明为什么其细微设置也值得严谨报告。
- selection_and_counterfactual: 没有在引言给比例，不等于藏证据：比例的单位与实验条件需要正文铺设；也不能把small理解成严格测量的扰动幅度。
- body_evidence:
  - I
  - B7
  - B8
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 139
    - 141
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 若改动规模有明确定义，可加入条件化效应值；否则保留现象层结果，并在正文提供反例式比较。
- alternative_relation: evidence_dependent_effect_quantification
- equivalent_reformulation:
  - text: 结果表明，这些因素即使只有小的改变，也可能显著影响对fuzzer的评估。
  - invariants_and_changes: 保留结果作为依据、小变化/大影响关系及可能性，重排信息不改变影响对象。
  - context_condition: 这里只是源句命题的局部改写；小变化尚非定义清楚的统一数值扰动，不能据此建立效应量。
  - status: 局部命题保义候选

## C3.S4

- old_map_coordinate: C3.S4
- source_statement_paraphrase: 实践建议
- syntax_and_information_focus: 推论连接词由发现推出规范；被动情态聚焦实验应如何做，目的不定式说明可靠性目标。
- reader_dependency_and_new_premise: 将资源与测量认识返回研究共同体实践，兑现P2第三问的部分价值。
- selection_and_counterfactual: 建议不是保证，也不是已测得实施建议后的写作/科研增益；严谨不是可执行协议的替代。
- body_evidence:
  - I
  - B7
  - B8
- interpretation_status: 语法关系依据原句；为何如此选择、反事实与替代表达均为编辑推断，不推定作者自述或个人执笔
- source_anchor:
  - pdf_physical_page: 3
  - printed_page: 2778
  - web_line_range:
    - 141
    - 142
  - source_url: https://www.usenix.org/system/files/sec21-li-yuwei.pdf
- conditioned_editorial_alternative: 在具体应用稿中可把建议展开为已验证的控制项与报告项；没有新验证时写建议的证据理由，不写效果保证。
- alternative_relation: evidence_dependent_recommendation_expansion

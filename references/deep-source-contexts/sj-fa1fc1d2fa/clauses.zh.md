# ContractFusion：语法矩阵、篇章前景与条件化备选

## P1.S1

- origin: new-unsampled-analysis
- grammatical_main_proposition: 主句把区块链作为主语，谓语是已获得广泛关注
- discourse_foreground: 宽领域入口，而非贡献或漏洞判断
- new_information: 近期关注度，尚无技术缺口
- clause_links: 时间短语限定背景陈述的历史窗口
- contextual_choice_reason: 先建立共同对象，再由S2给读者必要定义；不把关注度当方法需要
- meaning_preserving_alternative: 可改为区块链在论文时点之前的几年受到广泛关注，保留关注范围，不限缩为研究活动
- scope_changing_alternative: 改成区块链安全已获解决，会凭空添加已知答案
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: d360c8afb02110f15c311d901348aa14a369280536af5391c6d8f815abf27cdd
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P1.S2

- origin: new-unsampled-analysis
- grammatical_main_proposition: 矿工遵守共识协议；目的不定式说明维持安全共享账本
- discourse_foreground: 先给活动与对象，再交术语
- new_information: 账本如何被维护及名称
- clause_links: 括注释义矿工角色；关系从句给账本命名，不承担新方法
- contextual_choice_reason: 面向非区块链专门读者，定义先于不可变性和合约；作用是准备依赖
- meaning_preserving_alternative: 可拆成维护共享账本的活动说明和命名单句；保留定义层次
- scope_changing_alternative: 改为共识保证所有智能合约安全，会把账本属性偷换成程序正确性
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: b36e984d2b83693255d2daeaa3fba32f1bcabfca5a5d3d291d8910bfd0336193
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P1.S3

- origin: retained-sample-verified-plus-refinement
- grammatical_main_proposition: 共识协议使已记录交易不可变
- discourse_foreground: 已记录的条件及其被作者归纳出的属性
- new_information: 交易不可变性和防篡改/去中心化的背景陈述
- clause_links: 网络场景前置；once是省略结构的时间/条件限制；endowing为补充结果分词
- contextual_choice_reason: 不可变性将被P2.S3和P4.S3回收；末尾属性并不都是后文等量使用
- meaning_preserving_alternative: 可分开陈述记录后的不可变性及作者据此描述的性质
- scope_changing_alternative: 删掉记录之后条件或写成共识足以严格推出全部去中心化性质，强化了源文
- evidence: P1.S3→P2.S3→P4.S3
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 0f6c83c699c3a041f25747cb7b48de29d65afb5e22c544b8245240f56f0a83a2
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1
- retained_prior_analysis: 主句consensus enforces不可变交易，once从句限定记录之后；endowing分词推出属性。先机制后性质，性质成为下一段的已知前提。
- retained_analysis_status: Historical authored clause analysis, preserved rather than newly certified. Current reviewed grammar/foreground fields govern its interpretation.

## P2.S1

- origin: new-unsampled-analysis
- grammatical_main_proposition: 智能合约是运行在区块链之上的程序
- discourse_foreground: 从账本平台缩小到待分析对象
- new_information: 合约的程序身份和所在层次
- clause_links: running后置非限定动词修饰programs
- contextual_choice_reason: P1只建立平台，S1现在交任务对象；后续代码、部署、检测才有落点
- meaning_preserving_alternative: 可改为区块链上的智能合约以程序形式运行
- scope_changing_alternative: 改为智能合约就是区块链账本，混淆程序与账本
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 6b5adcce7f43dd638537e1adca50017926fa2d11ea370c6787825332af700911
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P2.S2

- origin: new-unsampled-analysis
- grammatical_main_proposition: 合约可由开发者专门设计；目的为实现资产管理规则
- discourse_foreground: 对象为什么值得编程和分析
- new_information: 规则表达能力及数字资产用途
- clause_links: 被动式保留设计者；目的不定式连接程序与用途；can是能力模态
- contextual_choice_reason: 先让资产成为正用途，P3再转为攻击动机
- meaning_preserving_alternative: 可让开发者作主语，说他们可专门设计智能合约，以实现管理数字资产的任意规则；不添加正确性保证
- scope_changing_alternative: 改成任意规则均可正确安全执行，把可设计性升级为正确性保证
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 4a07b73973a10bfa50e609a846e28e511bd5f589e184a616e6e7341361ff391a
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P2.S3

- origin: retained-sample-verified-plus-boundary
- grammatical_main_proposition: 合约在部署后不能更新，按论文的概括性背景表述
- discourse_foreground: 部署约束被单独突出
- new_information: 不可变性对程序维护的含义
- clause_links: 前置因果短语回指P1；once限定部署之后
- contextual_choice_reason: 短句使读者记住后面必须预判状态的理由；此处是2021源文的框架而非今日所有升级架构的技术定律
- meaning_preserving_alternative: 可表述为作者将合约一经部署便不能更新归因于区块链的不可变性；保留原有概括强度，适用边界另述
- scope_changing_alternative: 改成所有区块链应用永远无法修复或升级，扩大对象和时间范围
- evidence: P2.S3→P4.S3
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 456eaf250fdc567a1fca045092bc1e7c3fed275aa5ba35cd3ef0193d8fe19ea0
- alternative_classification_note: 严格保义项保留源文命题与力度，并可明确归属作者。降低主张强度或按证据收窄是另类编辑操作，不能仅因更谨慎就称为保义。
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1
- retained_prior_analysis: Attributing to前置已有不可变性，主句cannot be updated给新部署约束；短句在较长解释链中突出限制。
- retained_analysis_status: Historical authored clause analysis, preserved rather than newly certified. Current reviewed grammar/foreground fields govern its interpretation.

## P2.S4

- origin: new-unsampled-analysis
- grammatical_main_proposition: 规则被写成程序代码并自动执行，共享主语的两个被动谓语
- discourse_foreground: 规则执行方式及作者附加的公正性价值
- new_information: 从可设计规则转到执行属性
- clause_links: thus标示作者承接关系；which补充评价自动执行；末端that限制与合约交互的参与方
- contextual_choice_reason: 继续阐明对象价值，不能读成此句验证不可变性必然保证公正
- meaning_preserving_alternative: 可拆分编码、自动执行和作者对参与方公正性的解释；保留归属
- scope_changing_alternative: 改成不可变性已证明合约公平无漏洞，会把背景评价变成形式保证
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: a76ea74f300b1b8c6dc5c402bf1cad58ef2e2034d83a5e649ae332873bf2c358
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P2.S5

- origin: new-unsampled-analysis
- grammatical_main_proposition: 智能合约使条款自动执行成为可能
- discourse_foreground: 应用价值为下一段现实规模作准备
- new_information: 复杂去中心化应用可被支持
- clause_links: facilitating为补充后果分词，承接自动执行能力
- contextual_choice_reason: 段落从程序定义收束到应用；接P3的资产规模时不是无根金额
- meaning_preserving_alternative: 可分成自动执行能力与DApp支持两个短句
- scope_changing_alternative: 改成已经证明所有DApp可靠，把促成能力换成普遍可靠性
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 6e0936d00507e0f928ea76cef6da0ff85ed9da9b03c1aca93ad29627071b1548
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P3.S1

- origin: new-unsampled-analysis
- grammatical_main_proposition: 数百万合约已被部署
- discourse_foreground: 把抽象应用价值转为历史规模和资产暴露
- new_information: 部署数量及当时管理价值
- clause_links: 时间限制历史快照；controlling为附加分词，说明部署对象承载的价值
- contextual_choice_reason: 资产数额为S2的同一对象转义提供已知前提
- meaning_preserving_alternative: 可先说部署规模再另述其管理资产，明确均为论文时点
- scope_changing_alternative: 把2021数额当2026实时规模，或把管理额当损失额，均换了事实
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 09e40af6306605b3abbb49d148887932d71edab2d2ef28eb248144e576c7a578
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P3.S2

- origin: retained-sample-corrected-grammar
- grammatical_main_proposition: 持有大量财富使合约具有攻击吸引力
- discourse_foreground: 把同一财富从价值证据转为风险动机
- new_information: 攻击者激励
- clause_links: Holding结构是动名词性非限定主语，makes为有限谓语；however是插入转折标记；不是悬置分词状语
- contextual_choice_reason: 重复财富无需新增场景即可变换评价方向；语法主语和语篇已知财富在此相合
- meaning_preserving_alternative: 可改为这些合约管理的财富使其成为有吸引力的攻击目标
- scope_changing_alternative: 改成合约遭攻击所以持有财富，倒转因果；保留原词序却标为原因状语会误认句法
- evidence: P3.S1→S2→S3
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: a5b3b0ae5c119c7838b7699c05d10b3a7a36dd3fca083b2c0caab691fefdbb9f
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1
- retained_prior_analysis: Holding so much wealth分词起句接前一金额；however插入转义，主句makes…attractive把原收益转成攻击动机。
- retained_analysis_status: Historical authored clause analysis, preserved rather than newly certified. Current reviewed grammar/foreground fields govern its interpretation.
- retained_analysis_correction: The initial Holding construction is the nominal subject of makes, not an adverbial participial opener; the value-to-risk interpretation remains.

## P3.S3

- origin: new-unsampled-analysis
- grammatical_main_proposition: 攻击者在2016年利用漏洞盗走资产
- discourse_foreground: 以具体事件为风险判断给证据
- new_information: DAO事件、漏洞种类、损失量级
- clause_links: 时间状语定位历史；目的/结果不定式连接利用与盗取；括注只解释币种
- contextual_choice_reason: S2是一般动机，S3提供事件而不是算法需要的直接证明
- meaning_preserving_alternative: 可用历史事件单句保留对象、日期、漏洞类型和损失归属
- scope_changing_alternative: 改成本文防止了DAO事件或该损失由所有漏洞造成，误改主体或原因
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 7182a8ff0b91720a673030b72464303833babcc628394b34da43d9c285ea13e7
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P3.S4

- origin: new-unsampled-analysis
- grammatical_main_proposition: 此案非孤例，与每年披露多起漏洞并列
- discourse_foreground: 阻止读者把必要性限缩到一次历史事故
- new_information: 持续披露的范围主张
- clause_links: 两个有限分句由and连接；不是一个案例本身推出频率的演绎
- contextual_choice_reason: 从特例返回问题类，给P4根因分析提供广度
- meaning_preserving_alternative: 可分别写非孤例判断和持续披露依据
- scope_changing_alternative: 改成每个合约每年都会被攻破，扩大频率、对象和事件类型
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 279b2df36743d54dac087d24820145afb06206e31363f1bdc6c4ec4a63d60562
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P4.S1

- origin: new-unsampled-analysis
- grammatical_main_proposition: 可能促成漏洞的主要问题有两方面
- discourse_foreground: 设置下两句的组织预期
- new_information: 两个根因类别将被讨论
- clause_links: 限制性关系从句修饰issues；may保留可能性；twofold是组织谓词
- contextual_choice_reason: 此句只负责定向，不需要把两项根因全塞入主干
- meaning_preserving_alternative: 可改为可能容易引起智能合约漏洞的主要问题分为两方面，保留主要、可能与二分三项信息
- scope_changing_alternative: 改成漏洞只有两个充分必要原因，把篇章分类写成穷尽因果定理
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 9fd0402d16787f149e2e9440a178b7b12db2ce55e4bdbcf8a94138a0fab30dc0
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P4.S2

- origin: new-unsampled-analysis
- grammatical_main_proposition: 编程语言和工具仍新且粗糙
- discourse_foreground: 第一类成因及其开发理解后果
- new_information: 内建功能/工具容易被误解
- clause_links: which补充从前述状况产生理解空间的后果；First与S3并列组织
- contextual_choice_reason: 将风险从金额转到开发难点；尚未要求图网络，不能直接充当架构证明
- meaning_preserving_alternative: 可分两句讲工具成熟度与误解风险，保留因果归属
- scope_changing_alternative: 改成开发者缺乏能力或所有新语言必然有漏洞，转移责任并强化因果
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: ad6f9f6d1db526ac8f3c90820d9f9cae5e8dddd5a69f5bed64ff0de9ec7073de
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P4.S3

- origin: retained-sample-verified-plus-refinement
- grammatical_main_proposition: 开发者被要求预判代码将遭遇的状态与环境
- discourse_foreground: 不可变性使未来条件预判成为困难负担
- new_information: 预判范围和难度
- clause_links: due to给回指原因；that限定状态/环境；which评价前述预判任务；all属于源文要求强度
- contextual_choice_reason: P2的约束在此获得检测必要性的含义；句末困难为P5转向已有检测答案搭桥
- meaning_preserving_alternative: 可拆成部署约束、预判负担、难度三步，保留未来范围
- scope_changing_alternative: 改成本文能够预判所有未来状态，把动机中的负担冒充方法保证
- evidence: P2.S3→P4.S3→P5；§2函数级标签
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: f899406d86a7a96b7f82ab629cf5982b7f5fb43bc2e4834fa3d33f96b22303a7
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1
- retained_prior_analysis: due to前置原因回收不可变性；主句developers are required突出负担，that定语从句具体未来状态，which评价困难。
- retained_analysis_status: Historical authored clause analysis, preserved rather than newly certified. Current reviewed grammar/foreground fields govern its interpretation.

## P5.S1

- origin: new-unsampled-analysis
- grammatical_main_proposition: 现有检测方法大致可分两类
- discourse_foreground: 为比较安排局部分类
- new_information: 接下来对比的轴是方法路线
- clause_links: can和roughly约束分类强度；被动分类无须引入作者作为核心
- contextual_choice_reason: 读者刚知道成因，现在先得到可理解的答案空间；不能把该局部二分当穷尽综述
- meaning_preserving_alternative: 可改为现有智能合约漏洞检测方法大致可归入两个类别，保留对象与粗分类强度
- scope_changing_alternative: 改成检测只能有这两种方法，抹去粗分和后文其他近邻
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 77505e83c96f793702e49aa7def765717c21158994d470445376f8f55089b514
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P5.S2

- origin: new-unsampled-analysis
- grammatical_main_proposition: 第一路线采用静态分析和动态执行来识别漏洞
- discourse_foreground: 交代经典路线做什么
- new_information: 方法家族、目标及引用归属
- clause_links: 目的不定式是任务目标，非已验证成功率；引文附于路线
- contextual_choice_reason: S3批评前必须先给已有答案；专家局部信息的正面价值要到S7才明确出现
- meaning_preserving_alternative: 可改为第一类工作采用经典静态分析和动态执行技术来识别漏洞；这是路线总括，不追加每个工具均兼用两者的断言
- scope_changing_alternative: 改成经典工具完全不利用程序语义，超出本句并与方法家族实际范围冲突
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 691dbf9d546376001dffabc5b6d43d7edc759572fb0c0d0b86cd4bac951e2e9b
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P5.S3

- origin: retained-sample-verified-plus-refinement
- grammatical_main_proposition: 这些方法根本依赖若干固定专家规则
- discourse_foreground: 规则依赖的限制为接下来的神经路线留位置
- new_information: 人工模式的出错风险与复杂模式覆盖困难
- clause_links: while从属/对照分句内部并列两个限制；并非两个主句共同证明同一经验结果
- contextual_choice_reason: 缺陷指向固定化使用方式，不等于否定专家信息自身；S7需要保留后者
- meaning_preserving_alternative: 可把规则依赖与两种限制拆开，明确错误风险和覆盖不足不同
- scope_changing_alternative: 改成专家知识本身无价值，会切断S7融合理由
- evidence: P5.S2–S7；§3.1、§3.2
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 6ee6c3aafde8a6f3a688c59f0054db69b48170621d10bd340c0094d45d8d71c6
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1
- retained_prior_analysis: 主句固定规则依赖给结构性约束；while并列错误风险和复杂模式遗漏，两个不同缺陷共享一个根因。
- retained_analysis_status: Historical authored clause analysis, preserved rather than newly certified. Current reviewed grammar/foreground fields govern its interpretation.

## P5.S4

- origin: new-unsampled-analysis
- grammatical_main_proposition: 攻击者可能绕过固定模式
- discourse_foreground: 补充规则路线对对抗变化的脆弱性
- new_information: 固定覆盖之外的绕过可能性
- clause_links: Meanwhile是并列补充；may标能力/可能，easily为作者强度评价
- contextual_choice_reason: S3说表达错误和复杂覆盖，本句增加对手适应性；三者不应压成同一种错误
- meaning_preserving_alternative: 可改为作者指出，狡猾的攻击者可能用小技巧轻易绕过固定模式；保留主体、可能性、方式与强度
- scope_changing_alternative: 改成任何攻击者总能绕过所有检测器，去掉模态并扩大对象
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: e867aa83344a8b17a79a1fd25460e1721715ffa0a2f566e55657349ba5bccb52
- alternative_classification_note: 严格保义项保留源文命题与力度，并可明确归属作者。降低主张强度或按证据收窄是另类编辑操作，不能仅因更谨慎就称为保义。
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P5.S5

- origin: new-unsampled-analysis
- grammatical_main_proposition: 另一研究路线探索用深度学习处理复杂合约数据
- discourse_foreground: 已成立的神经能力及准确率进展必须先承认
- new_information: 复杂输入处理和已报告的检测改善
- clause_links: to说明所探索用途；having achieved是补充完成分词，给已有结果；不是本文结果
- contextual_choice_reason: 有力近邻的能力使S6剩余问题更具体；选择融合而非推翻图学习才有基础
- meaning_preserving_alternative: 可拆为另一类研究探索用深度学习模型处理复杂合约数据，并已取得大幅改善的准确率；能力探索与已报结果分句且均归属已有工作
- scope_changing_alternative: 改成深度方法尚不能处理复杂代码，抹除互补方的正能力
- evidence: P5.S5–S7；Table3图模型相对顺序模型比较
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 123a2dc7db0663e21d20e440f58cb6f33c24c45b58e576b5b9bf7d3b8b0f5de7
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P5.S6

- origin: new-unsampled-analysis
- grammatical_main_proposition: 这些神经方法未编码有用专家知识，且多半解释性不足
- discourse_foreground: 承认准确率后提出两项尚缺能力
- new_information: 知识接入和解释输出的残余需求
- clause_links: 前置原因短语为作者的黑箱归因；however转折；mostly只直接约束解释性判断，不能随意扩展到所有谓语
- contextual_choice_reason: 缺口是同一性能进展之外的内容；S7回应知识，S8单独加强可解释输出
- meaning_preserving_alternative: 可改为作者将这类方法未能编码有用专家知识、且多数解释性较差归因于其黑箱性质；保留原因和两项不同强度
- scope_changing_alternative: 改成所有神经方法原则上无法解释，删去路线和频率界限；或仅说准确率差，换了缺口
- evidence: P5.S5–S8；§5末段承認已有融合Liu2021
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 680313afa78c40304a1d42a36adcad0f03a54f88776fbce466ed6fda3c9cff68
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P5.S7

- origin: retained-sample-refined-main-vs-foreground
- grammatical_main_proposition: 矩阵主句是前述问题促使作者考察一个问题；补语问句问能否组合两路线
- discourse_foreground: 语篇重心是组合的能力分工，而非作者受激励这件事
- new_information: 神经侧处理复杂语义图；专家侧提供精确局部信息
- clause_links: whether保留探索；where展开组合场景；其中while对照两方能力，不是让步否定任何一方
- contextual_choice_reason: 两方正能力现在被命名，融合不再是把两个失效工具机械相加；局部/全局对象在P6被落实
- meaning_preserving_alternative: 可先问能否结合，再另句交各方贡献；保留能力分工和探索语气
- scope_changing_alternative: 写成已证明融合必然最好会把研究问题提前变成结论；只写结合两者优点会丢失设计信息
- evidence: P5.S3/S5/S6→S7；§3.2、§3.3；§4.4
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: c335a4c3530b44a8996922399040a748d987bfb7c595823e99ede32405311684
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1
- retained_prior_analysis: 主句motivates us to consider whether保留研究问题；where两并列贡献解释组合为何可能有效，不用“结合优势”四字代替对象。
- retained_analysis_status: Historical authored clause analysis, preserved rather than newly certified. Current reviewed grammar/foreground fields govern its interpretation.

## P5.S8

- origin: new-unsampled-analysis
- grammatical_main_proposition: 作者寻求一种可解释解决方案
- discourse_foreground: 解释要求在价值顺序中被提升
- new_information: 不同特征应有可查看权重这一可检查输出条件
- clause_links: 重要性标记调级；which关系从句限定方案应能交付什么；could保留目标式语气
- contextual_choice_reason: 不是把准确率换个形容词：读者今后应要求标签以外的输出；在方法以前说出判据
- meaning_preserving_alternative: 可独立说明方案还应展示各特征的权重；保留新增输出，不作证据升级
- scope_changing_alternative: 改成权重已经完整证明每个预测原因或解释必然提升准确率，加入因果/忠实性保证
- evidence: §2输出标签+权重；§3.3式7–8；§4.3
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: f4fdf92bf718b05170ec828a07466772e3f0523fe6759de7bb81080ea2888972
- physical_source_pages:
  - 1
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=1

## P6.S1

- origin: new-unsampled-analysis
- grammatical_main_proposition: 作者提出一个新系统
- discourse_foreground: 总览回应知识接入与解释要求
- new_information: 自动检测与可解释地结合专家模式属于同一系统
- clause_links: that相对从句修饰系统，can下两动词并列能力；beyond限定相对纯神经路线
- contextual_choice_reason: 先交整体答案，再由后面三步展开；不是这里已经证明自动化与解释准确性
- meaning_preserving_alternative: 可先说作者提出一个超出纯神经网络的新系统，再说作者称它能自动检测漏洞，并以可解释方式将专家模式纳入网络；不降成预期目标
- scope_changing_alternative: 写成首次组合神经网络和专家知识，忽略C3.S3及§5对Liu2021的承认
- evidence: P5.S6–S8→P6.S1；§2
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 25a8a520f6b8b13663997dbec0d53056cefc64e0afd3344acd2e410fb01fc439
- alternative_classification_note: 严格保义项保留源文命题与力度，并可明确归属作者。降低主张强度或按证据收窄是另类编辑操作，不能仅因更谨慎就称为保义。
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2

## P6.S2

- origin: new-unsampled-analysis
- grammatical_main_proposition: 作者开发自动提取漏洞特定专家模式的工具
- discourse_foreground: 局部输入怎样进入系统
- new_information: 自动提取，而非手工逐函数输入；模式按漏洞类型指定
- clause_links: 具体化标记和编号开始机制链；to给工具用途
- contextual_choice_reason: P5刚肯定局部知识，此句回答获取路径；自动提取不等于自动发现新的模式
- meaning_preserving_alternative: 可改为作者开发了自动提取漏洞特定专家模式的工具；若补充模式预先定义及来自函数代码，需标明那是§3.1支持的具体化
- scope_changing_alternative: 改成模型自动发明无需专家设计的漏洞模式，换了知识来源
- evidence: §3.1设计模式并实施自动提取
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 0d1ed406d490fba8784f2adf468db30a8225d0d49c785a82ceac7c4358895dbf
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2

## P6.S3

- origin: new-unsampled-analysis
- grammatical_main_proposition: 作者使用图结构表达函数代码的控制流和数据流
- discourse_foreground: 补齐与局部模式并行的全局表示
- new_information: 图所保留的语义关系种类及函数代码粒度
- clause_links: Then为机制叙述次序；to frame给表示目的，不能直接当准确率效果
- contextual_choice_reason: 把复杂语义具体为控制/数据依赖，给下一句图网络一个已知输入
- meaning_preserving_alternative: 可说系统另将函数中的控制/数据关系表示为图，保留输入与输出
- scope_changing_alternative: 改成图自动证明所有执行路径安全，越过表示到保证
- evidence: §3.2、Tables1–2；§2函数级输入
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 8e9e0bb44f6744d9c86ad44e7016b73e44e8f2924e9b7028bc35a7deeb2d668c
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2

## P6.S4

- origin: new-unsampled-analysis
- grammatical_main_proposition: 图神经网络被用于提取深层图特征
- discourse_foreground: 从图表示过渡到可融合特征
- new_information: 图到向量特征的操作
- clause_links: 前置upon图短语回指上一句构建的图，并将其作为本句输入；被动让图神经网络作语法主语并省去作者施事；to给抽取用途。主题延续与被动选择分开分析
- contextual_choice_reason: 前置图短语将上一句的图设为本句出发点；被动避免再次让作者作主语，但不会把图变成语法主语。此句提供S3图与S5融合特征间的接口，省去会误使读者把原始图直接融合
- meaning_preserving_alternative: 可主动写系统用图网络把该图转成特征
- scope_changing_alternative: 改成专家模式由图网络自动生成，错配两支的来源
- evidence: §3.3图特征提取沿边传播再聚合；未重演算法
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 83edec60d0d0ccee2b262945cb3618de1b74c220bbae714292e9bfaffa1543d6
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2

## P6.S5

- origin: new-unsampled-analysis
- grammatical_main_proposition: 作者提出注意力多编码器网络
- discourse_foreground: 此前两种表示在何处会合
- new_information: 局部与全局特征被可解释地融合的机制名和目的
- clause_links: finally收束方法链；目的不定式给融合职责；interpretably修饰融合方式
- contextual_choice_reason: 先分别取得两类对象，才引入融合，避免让组件名称替代问题答案
- meaning_preserving_alternative: 可说该多编码器将两种特征融合，并给出对应权重；后半需要§3.3支持
- scope_changing_alternative: 改成增加注意力本身已经证明因果解释有效，把设计名当评价结论
- evidence: §3.3异质特征先调节后编码/合并；式7–8权重输出
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: ab380e4456acb777eeb6397d54f849e42d560b2c100920551de49380a22166b8
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2

## P6.S6

- origin: retained-sample-refined-main-vs-foreground
- grammatical_main_proposition: 语法主句是大规模实验被执行；并非主句直接宣称提升
- discourse_foreground: 语篇前景是跨三漏洞的比较收益，而范围先建立证据可信度
- new_information: 两个数据集和三个准确率起止配对
- clause_links: demonstrating补充结果分词承担主要结果信息；冒号详化改善；respectively要求任务顺序从§2/表3补齐
- contextual_choice_reason: 用较强神经答案作近邻让增量对应融合问题；选择原因是编辑推断，作者未自述
- meaning_preserving_alternative: 可把实验设置与三个收益拆句，保留TMP比较和任务/数据集配对
- scope_changing_alternative: 用相对Slither的更大提升代换，或把百分点写相对百分比，会改变比较问题与量纲
- evidence: §4.1–4.2/Table3；B1、B2
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 78d8e39fc86278d3c1f652fe6d32dcd09ea1594bb7dda4b3ad670103650c9834
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2
- retained_prior_analysis: 被动实验主句先范围，demonstrating分词随后给三类对比；冒号把抽象significant变成可检查量，结尾respectively要求类型配对。
- retained_analysis_status: Historical authored clause analysis, preserved rather than newly certified. Current reviewed grammar/foreground fields govern its interpretation.

## P6.S7

- origin: new-unsampled-analysis
- grammatical_main_proposition: 系统能够解释标签、警示高权重局部模式、展示特征重要性概貌
- discourse_foreground: 解释能力被再次提升，回收P5.S8而非附带堆一个指标
- new_information: 个例判断支持与跨样本概貌是不同使用层次
- clause_links: 同一能愿结构下三动词并列；重要性标记与P5.S8呼应；没有结果因此产生因果保证的连接词
- contextual_choice_reason: 读者已经看见准确率，此处提醒任务答案还必须带可检查信号；三个用途不等于三个独立证明
- meaning_preserving_alternative: 可改为作者进一步强调系统能够解释标签预测、警示高权重局部模式，并展示不同特征重要性的总体图景；保留三项能力主张，再另述证据边界
- scope_changing_alternative: 改成自动定位精确漏洞行并证明修复正确，超出局部模式提示；把分布当真实因果重要性也越界
- evidence: §4.3/Figs3–5提供权重统计和一例；B3
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: bdefdfd589bfa3a2f2fbb5586e68ce85a95406727e713812ea6856252c4a587a
- alternative_classification_note: 严格保义项保留源文命题与力度，并可明确归属作者。降低主张强度或按证据收窄是另类编辑操作，不能仅因更谨慎就称为保义。
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2

## P7.S1

- origin: new-unsampled-analysis
- grammatical_main_proposition: 这是贡献列表的系词引导与冒号结构，不是独立实质发现
- discourse_foreground: 把前述细节压缩为后续三个逻辑组
- new_information: 宣告贡献清单开始
- clause_links: 印刷上与C1–C3同一贡献段；编号不等于独立段
- contextual_choice_reason: 无需强造一项贡献；保留它作为坐标便于与旧图对齐
- meaning_preserving_alternative: 可用贡献概括为以下三项引导
- scope_changing_alternative: 把引导句计成额外第四贡献，夸大数量
- evidence: Introduction local context
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 191df4eecc4048d1c2256b5d8eaa3c0adf5dbef6763ab063c19d6a2fc4c9f8cc
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2

## C1.S1

- origin: new-unsampled-analysis
- grammatical_main_proposition: 作者考察专家模式与神经网络的可解释结合
- discourse_foreground: 知识问题/研究对象重述
- new_information: 强调结合方式而非新增组件细节
- clause_links: combining为investigate的补语；漏洞特定限定专家模式范围
- contextual_choice_reason: P6已解释流水线，此处压缩为研究贡献层级
- meaning_preserving_alternative: 可改为作者研究以可解释方式将漏洞特定专家模式与神经网络结合，保留研究对象及范围
- scope_changing_alternative: 改成已证明通用漏洞检测完全可解释，扩大研究范围和证明强度
- evidence: P5.S7–S8；P6.S1–S5
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 8f5993bf483841af8833b8d075b60e089038a8a5c3e0fdfec4b7c09cfa470c8b
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2

## C1.S2

- origin: new-unsampled-analysis
- grammatical_main_proposition: 带知识范围限定的首创性主张
- discourse_foreground: 解释地考察组合这一相对位置
- new_information: 作者自报的首次性
- clause_links: 前置知识限定降低断言范围；first后的对象包含可解释方式；源文有拼写问题但分析不仿效
- contextual_choice_reason: 须与最后的Liu2021对比合读；该论文承认已有组合，首次不能删掉解释限定
- meaning_preserving_alternative: 可明确写据作者所知，这是首次以可解释方式探究上述组合；解释性重点的近邻定位另作分析
- scope_changing_alternative: 删掉知识限定或解释方式，写首次融合专家模式与神经网络，制造与近邻承认相矛盾的新颖性
- evidence: C3.S3；§5末段；无独立新颖性普查
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 32c9a86aa1d0d877d9807c8d0daf4df2b66a00f1293587fc3722ed5f7d1477fb
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2

## C2.S1

- origin: new-unsampled-analysis
- grammatical_main_proposition: 作者提出用于特征融合的多编码器网络
- discourse_foreground: 把上一组研究问题压缩为具体技术产物
- new_information: 多编码器是贡献层的实现对象
- clause_links: 方法内的位置限定；simple与effective是作者评价，并非句内展开证明；for限定用途
- contextual_choice_reason: 贡献清单此时不再重复完整流水线，可把技术对象短述并让正文证明
- meaning_preserving_alternative: 可改为作者提出一个用于特征融合的多编码器网络，并将其评价为简单而有效；保留评价归属，不把它外推为最简或最优
- scope_changing_alternative: 改成网络最简单或最优，加入未比较的普遍最值
- evidence: §3.3；§4.2/4.4支持表现，不证明形式最优
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: bef9e5216222392874297ac6d0a2868f0fc7ad2b3fa656ca7b71ba5f38a7fad7
- alternative_classification_note: 严格保义项保留源文命题与力度，并可明确归属作者。降低主张强度或按证据收窄是另类编辑操作，不能仅因更谨慎就称为保义。
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2

## C3.S1

- origin: new-unsampled-analysis
- grammatical_main_proposition: 方法达到作者所称新最佳表现，并提供新认识
- discourse_foreground: 把预测效果和解释观察合并作经验贡献
- new_information: 结果性总结，具体数字前面已给，认识后文权重统计给出
- clause_links: 两个并列有限谓语共享方法主语；不应把insights误写成机制组件
- contextual_choice_reason: P6已经交三结果，这里不必再列数字；新认识要回指RQ2而不是无内容赞语
- meaning_preserving_alternative: 可改为作者总结该方法达到新的最佳表现，并提供新的认识；保留排名和认识主张，所测比较及证据范围另述
- scope_changing_alternative: 改成所有数据/漏洞/未来工具都最好，或将权重规律写成因果定律
- evidence: Table3；§4.3/Figs3–4；所测比较边界
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: aedb914c76a7c1211434be6b848d7c32f0cd67852e7344ca3cd62fbc3ba87694
- alternative_classification_note: 严格保义项保留源文命题与力度，并可明确归属作者。降低主张强度或按证据收窄是另类编辑操作，不能仅因更谨慎就称为保义。
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2

## C3.S2

- origin: new-unsampled-analysis
- grammatical_main_proposition: 实现已被发布
- discourse_foreground: 可复用资源是独立承诺
- new_information: 开放实现位置及帮助后续研究的目的
- clause_links: 目的不定式前置；被动主句突出可得对象；链接为资源定位
- contextual_choice_reason: 这句不等于复现实验完成；它服务研究者再用而非新增性能
- meaning_preserving_alternative: 可说作者提供实现链接以便复用；注明这里只核原文链接，不核仓库运行
- scope_changing_alternative: 改成我们已复现并验证所有结果，将发布变成执行证据
- evidence: 原文链接https://github.com/Messi-Q/AMEVulDetector；本次未执行
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: db63f62c0a0faccd85d722c89a25e1cf788669099074facb5717908df7af7076
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2

## C3.S3

- origin: retained-sample-corrected-main-vs-content
- grammatical_main_proposition: 严格矩阵主句是作者想指出一个区别；that补语内是本文侧重解释并提供重要性概貌
- discourse_foreground: 实质前景是相对最近Liu2021的解释性范围差异
- new_information: 已有融合与本篇解释性重点的明确区分
- clause_links: different from在补语中前置比较；focuses与offers在补语内并列；旧样本把内容主干称主句需语法细化
- contextual_choice_reason: 结尾放近邻区别使首次性回到真正限定；不把主题相似当同一贡献
- meaning_preserving_alternative: 可直接写相较Liu2021，本工作侧重可解释组合及特征权重概貌；去掉作者提示语保留内容
- scope_changing_alternative: 改成区别在于本文首次结合专家与图特征，删除对已有融合的承认
- evidence: §5明确Liu2021已有准确率导向融合；未直接阅读该近邻全文
- epistemic_status: Syntax/source role observed; selection rationale and alternatives are editorial inference
- source_sentence_sha256: 559c6d2ca26597fd1451d7893043b92084668b5dc37d747941c13c15e95cc2ce
- physical_source_pages:
  - 2
- source_page_links:
  - https://arxiv.org/pdf/2106.09282v1#page=2
- retained_prior_analysis: 不同于近作的比较前置，主句focuses mainly…与offers并列，重心在解释性而非复述最高准确率。
- retained_analysis_status: Historical authored clause analysis, preserved rather than newly certified. Current reviewed grammar/foreground fields govern its interpretation.
- retained_analysis_correction: The strict matrix clause is author metadiscourse; focuses/offers belong to its content clause. Matrix grammar and discourse foreground are distinct.


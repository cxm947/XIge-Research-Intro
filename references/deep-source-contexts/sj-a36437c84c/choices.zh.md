# UVSCAN：十九组定点分析与英语替换选项

- record_count: 19
- units_with_targeted_refinement:
  - B1.S1
  - B1.S2
  - B1.S3
  - B1.S4
  - B2.S1
  - B2.S2
  - B2.S3
  - B2.S4
  - B2.S5
  - P1.S4
  - P2.S4
  - P2.S7
  - P4.S1
  - P4.S2
  - P4.S3
  - P4.S7
  - P5.S2
  - P6.S3
  - P6.S4
  - P6.S6
  - P8.S1
  - P8.S2
  - P8.S3
  - P8.S4
  - P8.S5
  - P8.S6
  - P8.S7
  - P8.S8
- analysis_scope_preamble: 此文件只追加19组实际所需精化；完整54单元保留于独立底稿。观察部分只陈述源句形式及内容；前景、价值、篇幅和选择条件均为编辑推断。局部英文替换与整句变体是建议，不冒充原句。矩阵指最外层语法主干，并不等于语篇最有价值的新信息。
- text_exclusion_note: Original source-span text and complete source sentences are not reproduced. Unit/offset/hash metadata delimits each authored patch. The applied-sentence hash identifies the reviewed splice, not an independent semantic guarantee. Some declared patches span a whole source sentence; their explicit ranges distinguish them from shorter local spans and from the eight separate contextual full variants.

## UV01

- units:
  - P1.S4
- refinement_reason: 旧稿已定位due-to与making；补主句所问对象和因果焦点可以不同。
- source_observation:
  - matrix: 设备是主语，易受NULL解引用漏洞影响是主断言。
  - dependency: due to介词短语提供API误用原因；making分词结构接设备暴露后果，botnet是例证。
- editorial_inference:
  - foreground: 读者刚见IoT风险，主语继续设备；研究可处理的原因却放在非限定原因短语里。语法主干不等于所有新贡献的前景。
  - given_to_new_and_dependency: P1.S3一般风险→S4具体设备故障→P2把误用解释为TPC集成问题。
  - value: 源句借可定位的软件原因把宏观重要性接到可研究任务；不只是多一个吓人的危害。
  - length_choice: 一句承载设备、故障、原因、后果；面向软件读者可拆出原因，但不能让例子替代后续任务定义。
- local_replacement:
  - unit: P1.S4
  - unit_start: 138
  - unit_end: 207
  - intro_start: 502
  - intro_end: 571
  - source_span_sha256: 18f7142fa0b7660b1efe51c73ef7a0c38c2a3db3df45dfa7f66245edb02385b2
  - replacement: because of API misuse in the closed-source Qualcomm QCMAP suite [23]
  - scope_and_strength: 局部原因短语替换，不升级可利用性；API复数到集合名词misuse不改变此处所述现象。
  - selection_condition: 只需改善因果连接而保持设备为话题时；若要以前景原因开头，须整句重排而非移动半个短语。
  - applied_sentence_sha256: cf684bfc864377d582af53474bb603fe951fd81817791a348b755bfcdd0fe608

## UV02

- units:
  - P2.S4
- refinement_reason: 旧稿已识别定义链；补may作用域、结果命名与典型实例的层级。
- source_observation:
  - matrix: 开发者可能未严格遵循规范，when限定采用TPC的场景。
  - dependency: resulting in引出所命名问题；which从句说明典型API误用类型；typically及例证不是穷尽定义。
- editorial_inference:
  - foreground: 主要推进是将熟悉的集成活动转成明确检测对象；结果补语承担命名，主句承担失误主体及模态。
  - given_to_new_and_dependency: P2.S3规范复杂→S4未遵守及命名→S5–6安全含义；不把安全后果塞进每个违反的定义。
  - value: 行为性定义让读者知道系统实际判什么；不将所有规范违反预先判成安全漏洞。
  - length_choice: 此处长句是概念引入；若读者首次接触任务，拆成两句可降低堆叠，不能删除模态或典型性。
- local_replacement:
  - unit: P2.S4
  - unit_start: 96
  - unit_end: 191
  - intro_start: 1149
  - intro_end: 1244
  - source_span_sha256: 34b10a7eefd69a8a0c0af033259f00f6e2514e695dbc9d8e5638d642f051d544
  - replacement: thereby giving rise to TPC usage violations, which are typically caused by API misuses
  - scope_and_strength: 扩展局部跨度至关系从句谓语，把problem单数改为violations复数时一并改成which are。保留前面may、句内typically及后续非穷尽例子；未将每个TPC使用者判为违规。
  - selection_condition: 研究对象已由标题命名、需要减少problem名词堆叠时。
  - applied_sentence_sha256: 1f5cb2e8fc4ca341ee1ba2cc0aca14521a29cb791eb0a13119965a0f7229d3db

## UV03

- units:
  - P2.S7
- refinement_reason: 旧稿已记录传播；补同一个may下两条可选放大路径及其不等同。
- source_observation:
  - matrix: vendors may统辖call与reuse，两行为由or协调。
  - dependency: 前项在一个固件中多次调用；后项跨不同固件复用；leading to给共同结果。
- editorial_inference:
  - foreground: 语篇新增不是又一种违反类型，而是同一错误的两个扩大尺度。
  - given_to_new_and_dependency: P2.S4定义个体错误→S7放大→B2规模观察；§5.2继承结果可回收后一条，但不是一一证明全部传播机制。
  - value: 让扫描多个固件的收益独立于单个漏洞严重性；对研究优先级有理由。
  - length_choice: 一个句子并列两个层级足够；展开分项仅在传播机制是论文主问题时。
- local_replacement:
  - unit: P2.S7
  - unit_start: 122
  - unit_end: 172
  - intro_start: 1652
  - intro_end: 1702
  - source_span_sha256: 89a87a52b1c7ee9e018cff86f0b4b5f21759e09d58787409c8dba45ef079963e
  - replacement: thereby amplifying the TPC usage violation problem
  - scope_and_strength: 保留源作者因果解释，不把or换成and；amplifying不是新发现的定量传播率。
  - selection_condition: 希望将数量增加与错误类别增加区分时。
  - applied_sentence_sha256: 10df9fd8dd2446aba3571996cbef939a8f045bb1832c2c6621034a555c30ac59

## UV04

- units:
  - P4.S1
- refinement_reason: 旧稿的which给必要性成立，但其准确附着需要保留语法歧义，不能说which无歧义指API规格。
- source_observation:
  - matrix: API specifications describe requirements。
  - dependency: 逗号which is以单数谓语连接；若直接回指复数specifications会不一致。语义可作前述规定/描述这一命题的评注，原文附着不够清楚。
- editorial_inference:
  - foreground: 关键新关系是这些要求承担判对错标准，放在关系从句并不次要。
  - given_to_new_and_dependency: P3只宣告挑战→S1先交判据→S2说明判据如何难获取。
  - value: 先证明为何需要规格，再论抽取难度；比直接宣称NLP困难更有任务依据。
  - length_choice: 可把判据关系放进主句，减少别扭which；无需扩成形式化正确性定义。
- local_replacement:
  - unit: P4.S1
  - unit_start: 0
  - unit_end: 135
  - intro_start: 1954
  - intro_end: 2089
  - source_span_sha256: b003d26aeb246100f044448d174d73d7fa54052dea4652c1e89bf354c83f375f
  - replacement: API specifications describe usage requirements that are critical for determining whether an API is used correctly.
  - scope_and_strength: 整句局部替换：明确critical修饰requirements，保留源意但消除原句附着歧义；不是声称单有规范足以完成检测。
  - selection_condition: 要提供可直接采用的英文，而非忠实转写原句语法时。
  - applied_sentence_sha256: 451b448100d233be7913aa6d603157e10bd2bbe31a94bea8c426baf7ec409f88

## UV05

- units:
  - P4.S2
  - P4.S3
- refinement_reason: 旧稿已写文档松散；补规格存在方式、文档性质和推导任务三层，而不将隐含编码本身称为不存在规范。
- source_observation:
  - matrix: S2：规范通常隐式编码或显式呈现；S3：首要挑战是有效精确地取得全部API规范。
  - dependency: S2关系从句修饰documents；hindering评注上述文本条件的后果。S3系词后的不定式给挑战内容，末尾which评价获取行为。
- editorial_inference:
  - foreground: S2矩阵在说规范在哪里及怎样呈现，实际阻力主要在文档修饰与结果分词；S3把它升为读者的待完成任务。
  - given_to_new_and_dependency: 已给规范用途→新增不规则记录条件→获取要求；这不是规范原本不存在的论证。
  - value: 同时保覆盖意图与精确性要求，但all APIs是挑战目标，不能反写为系统已覆盖所有规范。
  - length_choice: 两句先条件后任务合理；可压缩文档描述，不能只剩effectively这个评价词。
- local_replacement:
  - unit: P4.S2
  - unit_start: 116
  - unit_end: 211
  - intro_start: 2206
  - intro_end: 2301
  - source_span_sha256: 7e425ae3ea391a2001a27d6680aff1aab92ce24c01616a70cf82abbaed555f4a
  - replacement: which are usually loosely organized and unstructured, making API specification inference difficult
  - scope_and_strength: 保留原usually的频率强度及其对两项文档属性的范围，只把hindering结构展开为making inference difficult；不将文档条件绝对化。
  - selection_condition: 只需明确文档组织属性是阻力时；不要将此改成所有文档都完全无结构。
  - applied_sentence_sha256: 2fd06ca123f9cb03f18b334bed8c30612068b6aaa93a79a932a5c6b948267e82

## UV06

- units:
  - P4.S7
- refinement_reason: 旧稿已指出错误/不全→误报；补两个前提的强度并避免把并列批评压成使用例子都错误。
- source_observation:
  - matrix: 主句称使用例子可能错误；not to mention引入额外覆盖难题。
  - dependency: 覆盖命题内hard为主、if not impossible为加强插入；which will result连接规范不准确→false positives→low precision。
- editorial_inference:
  - foreground: 前景不是重数三次缺陷，而是可靠性与覆盖各自会损伤规则来源。
  - given_to_new_and_dependency: P4.S6承認替代输入来源→S7评估该来源；下一段即使抽出正确规则仍有表示问题。
  - value: 这允许公平承认代码例子有用，同时解释为什么不能仅从常见例子当规范。
  - length_choice: 原句代价尾链较长；可用两句分别交输入资格和检测后果，避免把may改成必然。
- local_replacement:
  - unit: P4.S7
  - unit_start: 46
  - unit_end: 130
  - intro_start: 2889
  - intro_end: 2973
  - source_span_sha256: c51c69cf52647af2efa07430dd561fffe5d2541839e682b467787326fe5368d0
  - replacement: and covering every usage case of an API is difficult, if not impossible
  - scope_and_strength: 局部更平行，保留may只约束错误可能性及另一个覆盖判断；不声称当前系统实现了完全覆盖。
  - selection_condition: 连接口语化not to mention妨碍正式论证时；若仍用原句which，须接受其对整组问题而非单名词的宽回指。
  - applied_sentence_sha256: 007c2662623309d6798764a01c9212ee4d675453e5015c3b9584b9490c59958d

## UV07

- units:
  - P5.S2
- refinement_reason: 已知表示交接不算本轮发现；只精化对照谓语与without extra effort的限定。
- source_observation:
  - matrix: 同一规格是两被动谓语的主语：could be understood / cannot be handled。
  - dependency: but比较人和程序；without extra effort限制程序端不能直接处理，非程序永远无法理解。
- editorial_inference:
  - foreground: 具体例子的新作用是让抽象接口残余可见，不是证明人类总能无误解释规格。
  - given_to_new_and_dependency: S1抽出的对象→S2同一例子在人/程序中不同可用性→S3需要转换。
  - value: 通过同一对象比较消费条件，不必发明新技术名解释困难。
  - length_choice: 保留一例及两个谓语即可；重复三遍自然语言难处理会稀释递进。
- local_replacement:
  - unit: P5.S2
  - unit_start: 95
  - unit_end: 192
  - intro_start: 3362
  - intro_end: 3459
  - source_span_sha256: 78484d1762501c98658f8a96d577b512ef9bbf31841eb796d659167166c3b21e
  - replacement: could be readily understood by a human but would require additional processing before a program could use it
  - scope_and_strength: 局部保留能力模态及额外处理条件；后半据§3.3为processing而非仅任何工作量，标为清晰化转述。
  - selection_condition: 想消除绝对cannot印象且后文确实提供表示转换时。
  - applied_sentence_sha256: 036e33e96e3f052b8d195332a83a9fe0c1ad4e74340f199a2f0a3ca01bb8e0e7

## UV08

- units:
  - P6.S3
  - P6.S4
- refinement_reason: 旧稿已公平承认旧法；补can rely与or在能力论证中的职责。
- source_observation:
  - matrix: S3定位过去方法输入层级；S4 they can rely给可利用能力。
  - dependency: Therefore推导自源码可见性；or列成熟静态工具和简易检查器两类路线。
- editorial_inference:
  - foreground: 旧法强处是有可用分析支撑，不是所有旧法都只做简单检查。
  - given_to_new_and_dependency: 源码可见→工具可用→S5二进制条件不同；后续困难不是旧法作者能力不足。
  - value: 为更低信息输入上的系统能力提供合适价值参照；有助避免不公平的弱基线。
  - length_choice: 两短句能让对照成立；压为source-level tools fail会删除旧能力。
- local_replacement:
  - unit: P6.S4
  - unit_start: 11
  - unit_end: 58
  - intro_start: 4053
  - intro_end: 4100
  - source_span_sha256: d2cfac7fbef7b063646b9b68fd5e69233b24fa62caaf81ca6fac7f329478a701
  - replacement: they can use existing static analysis tools
  - scope_and_strength: 局部can能力保留；不增加必须依赖或所有检查都容易。
  - selection_condition: 上下文不强调外部依赖关系、只强调已有工具可用时。
  - applied_sentence_sha256: 89d5d7919ca0c672a8142f87a18764357459e27266451494d71f1b9113a6c0b9

## UV09

- units:
  - P6.S6
- refinement_reason: 旧稿已记符号丢失；补which的可读性及essential不能扩为所有符号皆必要。
- source_observation:
  - matrix: binary loses information；when引入编译条件，e.g.给剥离符号例子。
  - dependency: 逗号which is较自然回指不可数information，但紧邻stripped binary会增加解析负担；不宜教为零成本附加信息。
- editorial_inference:
  - foreground: 信息丢失之所以成为挑战，在其对检测的用途；这句必须保用途关系而非只列二进制常识。
  - given_to_new_and_dependency: P6.S5差异总述→S6输入信息代价→S7语义关系复杂。
  - value: 把现实部署限制变成可理解的分析义务。
  - length_choice: 用定语前置到information可短且清楚；例子仍可以插入，但不把符号保留写成充分条件。
- local_replacement:
  - unit: P6.S6
  - unit_start: 0
  - unit_end: 177
  - intro_start: 4326
  - intro_end: 4503
  - source_span_sha256: e5e5d204f7683141a82dd50145544661fb23db0cb3af99ec55436c182a1a53f3
  - replacement: First, compilation and stripping remove information needed for usage-violation detection, including symbols in stripped binaries.
  - scope_and_strength: 整句清晰化；原句when compiling让binary似施事，改为过程施事；不宣称丢失每一条信息都必要。
  - selection_condition: 需要把技术原因直接接到检测用途，避免尾部which歧义时。
  - applied_sentence_sha256: bac9c02a5cd73e3ac0fadf6e196243ff4ab0b682d5b3d10a45921a9c4efbd732

## UV10

- units:
  - P8.S1
- refinement_reason: 旧稿把主句压为design-filter；补实际start from designing的动作层级与末端技术名的地位。
- source_observation:
  - matrix: we start from designing是矩阵；设计对象为情感模型。
  - dependency: 前置to solve给挑战回指；to filter为模型用途；by leveraging列支撑机制，with修饰定制BiLSTM。
- editorial_inference:
  - foreground: 对于引言任务，新增的是先消除无关描述以提高后续输入质量；模型名不是自动的新意清单。
  - given_to_new_and_dependency: P4文档抽取障碍→P8.S1过滤→S2从processed document抽出规格。
  - value: 输入选择能力让抽取步骤可解释；§3.2.1说明目标相关情感而非看到should就判相关。
  - length_choice: 原句一层目的套一层用途再列模型较重；若只是总览可先写过滤动作，把模型组合另接短句。
- local_replacement:
  - unit: P8.S1
  - unit_start: 63
  - unit_end: 171
  - intro_start: 5312
  - intro_end: 5420
  - source_span_sha256: 6b80fa3a80b2dbb87edc4d84c7b8b9d1c9a59ff960725aa0a4dbc3e4ac260737
  - replacement: we design a sentiment-based model that filters irrelevant API descriptions from TPC documents
  - scope_and_strength: 局部保过滤职责，并由未改的句首First保存动作顺序；删start from名词化，不重复first，仍保留后接by机制。
  - selection_condition: 在设计总览中要让实际操作比模型命名更易读时。
  - applied_sentence_sha256: 895bbe321e524832a6d06362f78d195ad69bfac0b2c7d97eb864f486574aa1ca

## UV11

- units:
  - P8.S2
- refinement_reason: 旧稿已认MRC与数据；补提出方法与定制现成范式的区别，以及人工数据不等于人工逐个提取。
- source_observation:
  - matrix: we propose an MRC-driven approach是矩阵。
  - dependency: to extract给输出/用途；from processed document承接上句；by customizing给实现方式，with分别带问题及人工构建数据集。
- editorial_inference:
  - foreground: 前景是针对规范抽取的MRC实例化，不是发明MRC这一通用任务。
  - given_to_new_and_dependency: 已过滤文档→定制问答→规格，所需人工资源是训练/构建准备而非声称零人工。
  - value: 让自动运行能力与开发阶段投入兼容；避免夸大端到端自动化的知识来源。
  - length_choice: 一句可保输出和定制来源；well-designed是评价词，通常不如具体query questions有信息。
- local_replacement:
  - unit: P8.S2
  - unit_start: 162
  - unit_end: 237
  - intro_start: 5704
  - intro_end: 5779
  - source_span_sha256: d5296e2882a9fa750aeaaa1215b17bafb814878f25c8d8d11f38c0e4f48e7d60
  - replacement: with task-specific query questions and a manually constructed dataset
  - scope_and_strength: 局部将自评换任务针对性，保留人工数据来源；不是声称所有问题或样本自动生成。
  - selection_condition: 需要突出定制工作而非赞美程度时。
  - applied_sentence_sha256: 7c3d86a31ff94a2f71513ae19a95dfce91ab2b440c6afa5648178c5314175cc7

## UV12

- units:
  - P8.S3
- refinement_reason: 实质校正：旧稿把by依存树及then映射一概作同一by链；原句map是有时态的并列谓语形式，另补which内复用/扩充层级。
- source_observation:
  - matrix: 严格按印出的词形，we design与then map可读为并列矩阵谓语；by constructing只明示修饰design。
  - dependency: 第二动作不是印成mapping。which回指semantic patterns，are collected与enriched共享被动助动词；by统辖两个并列非限定动作：using synonym replacement与changing the voice of patterns，这组方式修饰enriched。
- editorial_inference:
  - foreground: 核心动作是结构化后映射；规则来源不是全新知识库，扩充操作不是另一个普适新语言理论。
  - given_to_new_and_dependency: P5中自然语言不可直用已知→这里给具体构造；§3.3明列既有、同义扩充、语态扩充三部分。
  - value: 以准确归属交代新系统实际完成的构造，不把组合工作抹为零新意，也不占有沿用技术。
  - length_choice: 此句可拆成构造/来源两句；长关系从句保存了归属，不能为简短一刀删掉。
- local_replacement:
  - unit: P8.S3
  - unit_start: 203
  - unit_end: 265
  - intro_start: 5984
  - intro_end: 6046
  - source_span_sha256: 0ebe6e792ae980d72548eb574a6c397b8e99036ee5971de5c26f22adc549e0f4
  - replacement: and then mapping the phrases in nodes into programming expressions
  - scope_and_strength: 局部语法平行化，把两动作都纳入by方式结构；操作先后不变，但明确承认这改变原句句法附着而非逐字语法等同。
  - selection_condition: 希望依存树与映射都作为同一approach设计方式时；如坚持原句矩阵并列则不改。
  - applied_sentence_sha256: 259dafa7136bdbf2c433ec75cc7d20199ee06ad33ab7525ac7acc46537474e9a

## UV13

- units:
  - P8.S4
  - P8.S5
- refinement_reason: 旧稿已说复用FirmSec；补引文施事切换与分词enhancements不向后转移所有能力所有权。
- source_observation:
  - matrix: S4 we adopt FirmSec；S5 FirmSec supports两动名词能力。
  - dependency: incorporating是采用中的扩充；S5 by列FirmSec识别依据，不能因邻近we就让其全部变本文首创。
- editorial_inference:
  - foreground: 研究者动作与被采用工具能力用两个主语分开；读者可知道准备模块靠谁、为何足用。
  - given_to_new_and_dependency: §3.4具体化新增UBI支持、额外分支条件特征、省掉冗余CFG匹配；这些是局部增补，全文总览不必展开算法。
  - value: 适当归属提高系统设计可理解性；完整系统贡献仍可来自整合与定制。
  - length_choice: 两句比把FirmSec埋括号更便于归属；若压一句须保adopt/enhance。
- local_replacement:
  - unit: P8.S4
  - unit_start: 7
  - unit_end: 88
  - intro_start: 6200
  - intro_end: 6281
  - source_span_sha256: 4315982795e9e124d16d73b125e826f86e058769da8456542f003f9eda2528bf
  - replacement: we adapt FirmSec [48] for firmware processing by adding task-specific enhancements
  - scope_and_strength: 局部将采用并增补收为adapt，保引文；task-specific由§3.4具体需求支持，不把FirmSec全部能力称新。
  - selection_condition: 上下文需更清楚区分原有基础与本文增补时；细节仅按方法段职责再展开。
  - applied_sentence_sha256: d69a91aec48830d0fc438bbb69a070878df3545dccfe92e30c761397edc3655d

## UV14

- units:
  - P8.S6
  - P8.S7
  - P8.S8
- refinement_reason: 旧稿已知道逻辑事实与表达式接合；补idea系词句、方式前置和成功宣称不是同一种证据。
- source_observation:
  - matrix: S6 we design engine；S7 main idea is后的不定式encode/extract给内容；S8 we successfully detect为结果预告。
  - dependency: S6前置to回指第三挑战；S7 Datalog带既有引用；S8 By为方式框架，不是独立实验因果识别。
- editorial_inference:
  - foreground: 创新重点可位于系词补语和系统组合，而非矩阵中design一词；Datalog本身不应归新发明。
  - given_to_new_and_dependency: 已知规范表达式与待分析二进制→新的任务专用规则引擎连接；B1后给终端基准。
  - value: 在正文前交代系统怎样完成任务，不能仅列采用Datalog就当精度证明。
  - length_choice: 三句分别公告、解释、闭环；如果缩短仍保二进制事实、上下文关系和表达式输入。
- local_replacement:
  - unit: P8.S7
  - unit_start: 0
  - unit_end: 168
  - intro_start: 6613
  - intro_end: 6781
  - source_span_sha256: 78e7ec27406dc0ea941884cf3bd3597b0e36d3038c30dbf15a0bd331b083a8e7
  - replacement: Our engine encodes binary code as Datalog facts [13] and extracts the corresponding implicit and explicit contextual logical relationships.
  - scope_and_strength: 整句把内容提升为操作主句；是设计说明的主动化，不提升精度或首创性。
  - selection_condition: 前句已命名engine且读者需要直接理解其工作时；如果段落焦点是概念区别，可保原来的idea框架。
  - applied_sentence_sha256: ceb1d95650f5a2b6fbc6d9815bbcdcc26d323e3742af1420c9a5beaaf27c03df

## UV15

- units:
  - B1.S1
- refinement_reason: 旧稿已把跨层能力认作贡献；补命名/同位首次性/关系从句能力的不同前景。
- source_observation:
  - matrix: we propose UVSCAN为矩阵。
  - dependency: 同位名词组给first、automated、practical及任务；which从句给文档规格到二进制检测的跨层能力。
- editorial_inference:
  - foreground: 最有解释价值的推进藏在关系从句；不能机械把矩阵当科学新意、其余当可删背景。
  - given_to_new_and_dependency: P7宣布产物、P8解释机制→B1归约整个系统能力；并非再报模块清单。
  - value: 改变可用输入下能完成的任务；没有源代码也能连接规范与用法检查是价值依据。
  - length_choice: 命名长句可改为能力主句；若保首次性需限定论文时点，不能当今日检索结论。
- local_replacement:
  - unit: B1.S1
  - unit_start: 116
  - unit_end: 234
  - intro_start: 7119
  - intro_end: 7237
  - source_span_sha256: 6e64d5e0dcc9d5dbe7fd2f610521507d37529d86b4d3ed859a3efcab3aedbf70
  - replacement: which connects document-derived API specifications to binary-level usage-violation analysis
  - scope_and_strength: 局部去gap名词重述而保持具体能力；不取消前部first作者主张，也不新增语义完备保证。
  - selection_condition: 对象关系已经足够解释推进、不需要抽象gap措辞时。
  - applied_sentence_sha256: 7bd5ffa7d9503336cf025bff34a4173308bc7f6a830380c4019b1becd00fbae5

## UV16

- units:
  - B1.S2
  - B1.S3
- refinement_reason: 旧稿已发现表7反例与Advance边界；本轮只把它变成可直接使用的证据约束表达，不重算为新发现。
- source_observation:
  - matrix: S2系统achieves为能力结果；S3 Though从句设二进制输入让步，矩阵做比较结论。
  - dependency: on/in限定基准与架构；including把146放作样本背景，原文简写可能误读为每个架构146独立违反。
- editorial_inference:
  - foreground: 任务价值在低信息输入仍能有用地检测，不等同赢过每一个源级工具。
  - given_to_new_and_dependency: P6指出二进制负担→贡献用基准回答这项采用条件；§4.2.4/Table 7决定比较强度。
  - value: 保留更困难输入下的能力证明，同时按每个比较者给真实方向；不是一串预防性免责声明。
  - length_choice: 可将两句合为总结果+分比较者结论，省略泛excellent而保参照。
- local_replacement:
  - unit: B1.S3
  - unit_start: 37
  - unit_end: 175
  - intro_start: 7438
  - intro_end: 7576
  - source_span_sha256: 06923a010d5dfb760c8107249dcff828d51b530f8036a48c7cbd0e2265142ccf
  - replacement: it outperforms the source-level detectors APISAN [45] and APEx [26] on the evaluated datasets, while approaching Advance [30]
  - scope_and_strength: 证据约束修正，非源句保义替换；依据§4.2.4文字及表7。仍保源句前置Though二进制输入。
  - selection_condition: 要把历史写作例子转成当前可负责任使用的结果句时；不能拿此证明新目标研究也有同一结果。
  - applied_sentence_sha256: df963adbe501f5774a56f4119fcee714bdb7ec25d73496d95b8f14b8e730fc77

## UV17

- units:
  - B1.S4
- refinement_reason: 旧稿保留will；补目的从句的资源效用与未来承诺不能充当完成证据。
- source_observation:
  - matrix: we will open-source为将来承诺，宾语UVSCAN。
  - dependency: 前置to facilitate给未来IoT安全研究用途；at给发布目的地。
- editorial_inference:
  - foreground: 资源可支持复用验证，但此处尚是承诺，不是读者已经可下载的当前状态。
  - given_to_new_and_dependency: 系统能力/结果→可供后续研究使用的资源安排；未在本轮核查仓库发布。
  - value: 有利于开放性叙事，但不是另一独立方法贡献。
  - length_choice: 一句足够；除非资源本身有独立研究价值，无需另设贡献条目。
- local_replacement:
  - unit: B1.S4
  - unit_start: 0
  - unit_end: 42
  - intro_start: 7578
  - intro_end: 7620
  - source_span_sha256: 25db528e601b38b0acc6d19d7c8a05aceaafbb6afe978eebcf3b32a25b55ece5
  - replacement: To support future IoT security research
  - scope_and_strength: 只换目的词，保将来式、对象、URL；不把will换成已开放。
  - selection_condition: 需要自然搭配而不改变承诺状态时。
  - applied_sentence_sha256: a24974d81693d893ddbaf2e26a1b9962743467da39e719e07ad19c46536fa25c

## UV18

- units:
  - B2.S1
  - B2.S2
  - B2.S3
- refinement_reason: 旧稿已有系统/测量双中心；补first叙述、工具依据、计数、知识解释在句法中的分工。
- source_observation:
  - matrix: S1 we are first / conduct first；S2 we detect；S3 we uncover。
  - dependency: to best knowledge限制首次主张；based on工具是手段框架；according to results是解释依据而非第三组独立实验。
- editorial_inference:
  - foreground: B1回答能做什么，B2回答使用后了解研究总体什么；检测动作的计数与widespread解释不能互相替代。
  - given_to_new_and_dependency: P2放大动机→规模样本及发现→案例后果；four TPCs和4545固件提供观察范围。
  - value: 把可用系统转化为关于所研究固件集合的知识；不把一个便利样本直接推成全球比例。
  - length_choice: 三句有时可合并为研究动作+范围+知识结论；应减少first重复而不是删分母。
- local_replacement:
  - unit: B2.S3
  - unit_start: 0
  - unit_end: 89
  - intro_start: 7952
  - intro_end: 8041
  - source_span_sha256: 4955e28a57a639fd1586320afb74018a15a2bdc6827994629e047603d9387a2d
  - replacement: These results show that TPC usage violations are widespread in the analyzed firmware corpus.
  - scope_and_strength: 整句证据范围收束；将泛IoT firmware明确为所分析语料，不改变规模结果本身，属于范围校准而非字面等义。
  - selection_condition: 研究未建立总体代表性且需要防止跨总体外推时。
  - applied_sentence_sha256: 1f7b44a7be7dd8eaa41845dca2d06ccea85cd32a945124776109b71ad88755d5

## UV19

- units:
  - B2.S4
  - B2.S5
- refinement_reason: 旧稿已有潜在风险与确认分层；补case studies主语、插入实例和被动句施事。
- source_observation:
  - matrix: S4案例研究demonstrate potential risk；S5 206违反have been confirmed，seven have been assigned。
  - dependency: S4插入语命名两类案例；S5 by vendors只明示确认施事，第二被动未明示CVE分配者，them回指206子集。
- editorial_inference:
  - foreground: 任务后果需案例研究，外部认可需厂商；这两类可信度不能靠一个最大数量代替。
  - given_to_new_and_dependency: B2.S2检测计数→S3普遍性→S4具体后果→S5外部确认；顺序是不同读者问题的解答。
  - value: 既说明实践意义也不把全部报告变成已确认漏洞；无须讲攻击步骤。
  - length_choice: 两句可合并但很容易把案例与206误写同集合；当前分句能保存证据角色。
- local_replacement:
  - unit: B2.S5
  - unit_start: 11
  - unit_end: 145
  - intro_start: 8233
  - intro_end: 8367
  - source_span_sha256: c2dc6b16b7915e2f3b440cb07145ef36f9ebfa45c891a9312f32ef43feb0e6ae
  - replacement: vendors have confirmed 206 reported usage violations as vulnerabilities, and seven of these have received high-severity CVE IDs
  - scope_and_strength: 局部主动化确认主体，CVE仍独立状态且不发明分配施事；reported由§5.2已报送支持，up to now保留在替换外。
  - selection_condition: 需要让外部验证者更显眼、同时保子集关系及源时点状态时。
  - applied_sentence_sha256: de3a16af2cfaf43df698a06700f5d5f4176de1ec82c3562515374c8caaaa744a


# SirenAttack：完整引言句内分析与继承解析更正

- distinctions: grammar/discourse/newness/grounds are separate; all selection and alternative rationale is editorial inference

## P1.S1

- source_page: 1
- source_claim_paraphrase: 学习驱动声学系统进入日常的多个应用层次
- grammatical_main_proposition: 声学系统已经普及是主句；应用范围为后附成分
- discourse_foreground: 正常使用的广度，而非攻击已经广泛发生
- new_information: 手机锁、家庭助手、云端服务构成分布式应用例子
- contextual_grounds: 以读者熟悉活动建立任务价值；尚未要求读者懂模型
- clause_relations: 后置范围列举按设备/家庭/云展开；末项位置扩大尺度但不证明最重要
- source_choice_editorial_inference: 先交系统用于何处以及在日常生活中的普及，便于风险研究随后继承真实用途价值；本句尚未解释采用原因
- alternative_expression_and_tradeoff: 可说“从个人设备到家庭助手和云服务，机器学习驱动的声学系统在日常生活中已普遍存在”；范围前置仍保留普及强度。若改成“多类应用已采用机器学习”，则弱化了普及判断并改变对象表述，须标为范围/强度改写，不能称纯换序
- scope_guard: 普及是论文时期背景判断；列举不是穷尽，也不是各场景攻击成功的证据
- body_evidence_ids:

- retained_clause_analysis: None

## P1.S2

- source_page: 1
- source_claim_paraphrase: 以应用情境把声学系统分为分类与识别两支
- grammatical_main_proposition: 系统可以分成两类是主句；according to引出的句后介词短语说明分类依据，句首概括语另行框定一般性
- discourse_foreground: 提供后续对照的对象轴
- new_information: 两种系统类型首次命名
- contextual_grounds: 上一句的多个应用需整理；分类不是由后来的访问权限推导
- clause_relations: 情境依据限定分类框架，冒号后的同位列举填实两类
- source_choice_editorial_inference: 此处分类为C2不同应用和C1访问分支避免对象混同
- alternative_expression_and_tradeoff: 可改成“两类应用要求不同输出：一类做分类，另一类做识别”；更强调任务差别，但“输出要求”须由相邻流程支持，不能当作源句已有定义
- scope_guard: 不是所有声学系统唯一且完备的现代分类法；不能把两种任务等同白盒/黑盒两种权限
- body_evidence_ids:
  - B1
- retained_clause_analysis: None

## P1.S3

- source_page: 1
- source_claim_paraphrase: 分类型系统通常先变换输入域，再对谱图分类
- grammatical_main_proposition: 同一主语承担先变换、再分类的并列谓词
- discourse_foreground: 从音频输入到离散分类输出的处理关系
- new_information: 时间域、频率域、谱图首次成为下一段可引用对象
- contextual_grounds: P1.S2只给名称，尚无处理认识
- clause_relations: 通常的频率限制覆盖整条一般流程；先/后标过程次序而非新颖性
- source_choice_editorial_inference: 先交最短流程，为下一句声音事件例提供可解释的类别输出
- alternative_expression_and_tradeoff: 可分为“分类型系统通常把音频变换为频域表示；随后对相应谱图作分类”；分句会加强阶段界限，但第二句必须继承“通常”的限制，不能写成绝对必要步骤
- scope_guard: 这里是代表性背景流程，不是SirenAttack新算法，也不是所有模型强制输入接口
- body_evidence_ids:
  - B1
- retained_clause_analysis: None

## P1.S4

- source_page: 1
- source_claim_paraphrase: 声音事件分类能识别若干物理事件，并常用于声学监控
- grammatical_main_proposition: 声音事件分类系统识别物理事件是主句
- discourse_foreground: 给分类任务一个可理解的实际输出
- new_information: 监控用途和事件例同时补充任务后果
- contextual_grounds: 上一句已有分类流程，例子无需再解释模型
- clause_relations: 句首例示标记；非限制关系从句插入常见集成用途；句尾事件是非穷尽例
- source_choice_editorial_inference: 主句保任务动作，应用背景放插入从句，避免把监控市场而非任务输出当中心
- alternative_expression_and_tradeoff: 可先写“监控常集成声音事件分类”，再说识别事件；这种顺序在应用重要性尚未建立时有用，但此处会把新信息重心由输出移到部署
- scope_guard: 常见集成不等于所有系统均用于监控；事件举例不证明现实部署中的攻击有效
- body_evidence_ids:
  - B1
  - B9
- retained_clause_analysis: None

## P1.S5

- source_page: 1
- source_claim_paraphrase: 识别型系统往往更复杂，因为涉及分帧、逐帧预测和序列结果组合
- grammatical_main_proposition: 识别型系统通常更复杂是语法主句
- discourse_foreground: 复杂性判断在话语上由后置处理链兑现；原因从句承载主要解释
- new_information: 帧级预测与CTC/attention结果组合，是对读者新增的具体差别
- contextual_grounds: P1.S3分类流程成为比较基线
- clause_relations: 比较状语先定位；原因从句内三个动作并列且有先后；CTC与attention是选择项，不是都必需
- source_choice_editorial_inference: 保留旧分析，同时分开“主句评价”和“原因新信息”，不能把从句一概视为已知背景
- alternative_expression_and_tradeoff: 可先描述分帧/预测/组合，再说这使识别往往更复杂；在读者不接受评价时更稳，但需保持“往往”与比较对象，且不能让组合机制成为本文创新
- scope_guard: 复杂为源文定性判断；CTC或attention，不是同时使用；此处不证明攻击一定更难
- body_evidence_ids:
  - B1
- retained_clause_analysis: 比较状语先建立另一类系统，主句more complicated后since从句用三步流程解释复杂；复杂性不是无根据评价。

## P1.S6

- source_page: 1
- source_claim_paraphrase: ASR是代表性识别型系统，常见于语音助手
- grammatical_main_proposition: ASR是典型例子构成系表主句
- discourse_foreground: 把抽象识别流程接回读者熟悉的应用
- new_information: ASR缩写及助手应用首次绑定
- contextual_grounds: P1.S5已经解释识别流程，当前只需指认实例
- clause_relations: 关系从句补集成范围，括号给助手例；例证层次为系统→应用
- source_choice_editorial_inference: ASR的首次定位为后面云平台证据提供回收点，而非把整篇范围缩成转录任务
- alternative_expression_and_tradeoff: 可将ASR集成到助手的事实置于主句、典型性置于前附短语；更适合实践入口，但此处会削弱与分类分支对称的例证收束
- scope_guard: 典型例不等于识别型系统只含ASR；助手名称只是论文时期实例
- body_evidence_ids:
  - B1
  - B7
- retained_clause_analysis: None

## P2.S1

- source_page: 1
- source_claim_paraphrase: 较好表现使当时多数声学系统采用DNN
- grammatical_main_proposition: 多数系统建于DNN是主句
- discourse_foreground: 从任务分类切到共同模型基础
- new_information: DNN成为攻击讨论的共同对象
- contextual_grounds: P1讲任务与流程；此处补为什么接下来可共享模型脆弱性问题
- clause_relations: 原因介词短语前置；多数限定系统集合，时间限定历史背景
- source_choice_editorial_inference: 把部署与模型连接，比凭空转到对抗样本更连贯
- alternative_expression_and_tradeoff: 可说“DNN因表现优势而被当时多数声学系统采用”；两种表述均为被动构式，改变的是主语/话题及谓词组织，不是主动与被动的切换；保持多数和历史时间限定，不能简写成全部系统
- scope_guard: 性能优势是背景归因，无本句对照实验；不能把历史多数更新为2026事实
- body_evidence_ids:

- retained_clause_analysis: None

## P2.S2

- source_page: 1
- source_claim_paraphrase: DNN易受恶意构造输入影响，典型构造方式为少量人难察觉扰动
- grammatical_main_proposition: 模型易受对抗输入影响是主句
- discourse_foreground: 将性能背景转向安全问题；术语定义为读者准备
- new_information: 对抗输入定义、典型构造及使模型偏离行为的目的
- contextual_grounds: 上一句以性能说明采用；转折不否定性能，只增添脆弱性维度
- clause_relations: 非限制关系从句定义输入；括号内方式带典型性；不定式表示构造目的，不是成功测量
- source_choice_editorial_inference: 旧分析保留；新补“定义中典型的人难察觉”不能充当本方法所有样本已不可察觉的证据
- alternative_expression_and_tradeoff: 可把定义独立成下一句，以减少嵌套；在不熟悉术语的受众更合适，但应保留“典型地”且不把目的改成必然结果
- scope_guard: 目的不等于实证成功；定义类属性不等于本文每一生成样本的性质
- body_evidence_ids:
  - B2
  - B6
  - B8
- retained_clause_analysis: 主句vulnerable交威胁，which定义对抗输入，括号给微噪声典型实现，to不定式交攻击目标；定义服务威胁而非另起术语课。

## P2.S3

- source_page: 1
- source_claim_paraphrase: 相较图像与文本的丰富工作，音频攻击研究较少，作者归因于若干难点
- grammatical_main_proposition: 音频攻击研究仍有限是主句
- discourse_foreground: 打开需要解释的研究不均衡
- new_information: 音频研究不足及难点总领
- contextual_grounds: 前两句只证明问题存在，尚未说明音频为什么需要专门研究
- clause_relations: 让步前置已有大量跨域工作；尾部原因短语引向后两句
- source_choice_editorial_inference: 将跨域繁荣当反预期背景，可避免把音频任务说成对抗学习空白
- alternative_expression_and_tradeoff: 可先列音频两类障碍，再回收研究有限；更证据先行，但会推迟本段问题意识；不能改成没有任何音频工作
- scope_guard: “有限”不是零；因果是作者解释，未提供文献计量或证明障碍导致少论文
- body_evidence_ids:

- retained_clause_analysis: None

## P2.S4

- source_page: 1
- source_claim_paraphrase: 处理时间维信息变化构成音频相对图像分类的复杂性
- grammatical_main_proposition: 声学系统需要处理时间维变化是主句
- discourse_foreground: 第一个应用层障碍
- new_information: 输入的时间变化不能仅用静态类别判断概括
- contextual_grounds: 上一句预告挑战；P1.S5帧序列已为理解做准备
- clause_relations: 顺序标记列第一项；关系从句的语义比较应读为处理该类信息更复杂，表层指代并不精确
- source_choice_editorial_inference: 把新增关系放在关系从句，不等于它可删；它承担“为何成挑战”的判断
- alternative_expression_and_tradeoff: 可明确说“处理随时间变化的信息，使此任务较图像分类更复杂”；澄清指代，但将模糊关系显式因果化是编辑解释，不能标为机械等义替换
- scope_guard: 不把该源句作为所有音频任务均严格难于所有视觉任务的定理；句法含混需标记，而非伪称唯一解析
- body_evidence_ids:
  - B1
- retained_clause_analysis: None

## P2.S5

- source_page: 1
- source_claim_paraphrase: 作者用高音频采样率与小型图像数据集尺寸对比来说明输入规模
- grammatical_main_proposition: 两个分句分别断言音频采样通常高、图像像素规模较小
- discourse_foreground: 对比关系前景化规模差异；数字是解释支持
- new_information: 采样频率的单位含义以及两个历史图像基准尺寸
- contextual_grounds: 第二个挑战与前句时间维挑战并列，不由前句造成
- clause_relations: 音频例内有解释性关系从句；图像例内有同位释义；转折连接异质单位，源句有概括过宽风险
- source_choice_editorial_inference: 保留旧数量说明，同时指出每秒样本量与整张图像像素是不同基准；作者意图是强调规模，不是给统一复杂度证明
- alternative_expression_and_tradeoff: 可写“作者以16kHz音频和MNIST/CIFAR-10的小尺寸图像说明其比较”；作为审慎转述更准确，但范围比原泛指图像句更窄，必须标为证据限缩，不能称原句完全等义改写
- scope_guard: 不将小图像例推广成所有图像；音频长度、通道数与图像尺寸改变比较；历史背景不直接迁移为今日事实
- body_evidence_ids:

- retained_clause_analysis: 主句采样率高，括号解释16kHz，but并列小图像规模；数字服务维度差异，末句再交对扰动的技术后果。

## P2.S6

- source_page: 1
- source_claim_paraphrase: 作者据前述特点认为轻微噪声较难改变音频局部特征，因而音频构造更难
- grammatical_main_proposition: 构造对抗音频较图像更难是主句
- discourse_foreground: 挑战从规模/时间转为扰动能否影响表征的技术后果
- new_information: 局部特征受微扰影响较小是新增解释
- contextual_grounds: 前文两种特性作为推导背景，尚无本句单独实验
- clause_relations: 推论衔接语标承上；原因从句后置支持比较性判断，不是仅追加事实
- source_choice_editorial_inference: 这一句完成“特性为何阻碍任务”，可学其解释职责，不照搬其未经此处量化的普遍比较
- alternative_expression_and_tradeoff: 可先说局部特征较难受微扰改变，再写构造难度；更突出近因，但需保留作者归因和比较范围，不能变成保证无法攻击
- scope_guard: 难度不是此处量化测量；因果链不等于PSO必然优于替代法，引言未交机制论证
- body_evidence_ids:
  - B3
- retained_clause_analysis: None

## P3.S1

- source_page: 2
- source_claim_paraphrase: 近期已有数项产生音频对抗样本的研究
- grammatical_main_proposition: 若干机制被提出为主句
- discourse_foreground: 承认最近答案，打断研究空白的误读
- new_information: 三个被引用近邻进入比较集合
- contextual_grounds: P2有限研究仍容许已有研究
- clause_relations: 近期时间框架；被动把研究机制置于主题；目的不定式限定任务
- source_choice_editorial_inference: 先给正能力再讨论条件，便于公平推出剩余
- alternative_expression_and_tradeoff: 可改主动“若干近期研究已生成音频对抗样本”；突出已达成果会更有力，但源句只称提出机制，不能偷偷升级成逐项已验证效果
- scope_guard: 集合由该句引用界定；不能把下一句的全称推广到全部历史或未来音频攻击
- body_evidence_ids:
  - B4
- retained_clause_analysis: None

## P3.S2

- source_page: 2
- source_claim_paraphrase: 所指近邻均使用梯度，作者进一步称它们差异很小
- grammatical_main_proposition: 均基于梯度是可清楚识别的主干；后半源句语法残缺
- discourse_foreground: 共同信息依赖作为后续访问限制的比较轴
- new_information: 梯度依赖首次明确
- contextual_grounds: 指代承接P3.S1的被引集合，不能自动包含§2所有方法
- clause_relations: 后置结果性成分试图从共同梯度推小差别；源文动词叠接缺陷在页面上可见，非抽取错误
- source_choice_editorial_inference: 可借共同访问条件组织近邻，但共用梯度不足以证明全部机制相似；把作者强推断保留为来源主张
- alternative_expression_and_tradeoff: 语法修复可说“这些被引方法均利用梯度，作者据此认为差异较小”；若改成“共同依赖梯度，但实现可不同”，新增反向限定属于分析者评议，不能冒充原意
- scope_guard: 全称只限指代集合；语法修复不应帮原文强化从依赖到机制同质的因果
- body_evidence_ids:
  - B4
- retained_clause_analysis: None

## P3.S3

- source_page: 2
- source_claim_paraphrase: 承认先驱价值后，指出各项工作至少落入一个实践限制：特定白盒模型、仅非定向、或目标音素相近
- grammatical_main_proposition: 这些工作在实践中受限是主句
- discourse_foreground: 剩余能力边界；让步保近邻已知价值
- new_information: 三轴限制及至少一项的析取范围
- contextual_grounds: P3.S1–2已交近邻存在与共同信息条件
- clause_relations: 让步从句先行；原因短语管辖枚举；枚举二的目的说明非定向，而不是整个列表目的；三项句法并列但分配语义为至少一项
- source_choice_editorial_inference: 保留旧量词分析；三限制不是每篇全中，也不必一一配对P4的三个形容词
- alternative_expression_and_tradeoff: 可分成“这些工作具有开创性；但各项工作至少受到以下一种限制”，再列三项。这把本分析采用的逐项分配读法显式化，并减少嵌套；不能改成整个集合只需有一项限制，也不能把三项写成每项工作都同时具备；保留各分支的“仅”
- scope_guard: 至少一项是析取，不是交集；§2显示近邻异质，梯度条件与只非定向不得当作同一维度
- body_evidence_ids:
  - B4
- retained_clause_analysis: Even though承认先驱价值，主句limited保持残余判断，due to后列三个条件；at least one限定不是每项工作都三缺陷。

## P3.S4

- source_page: 2
- source_claim_paraphrase: 这些近邻均缺少全面端到端评价
- grammatical_main_proposition: 所指工作没有经过全面端到端评价是主句
- discourse_foreground: 新增证据范围缺口，与方法能力限制并列
- new_information: 评价充分性首次成为研究需要
- contextual_grounds: 前句讨论能做什么；本句另问现有证据覆盖到哪里
- clause_relations: 添加衔接而非因果；否定量词修饰被引集合；全面限定评价水平；括号路由详细分析
- source_choice_editorial_inference: 此句使C2多任务评价拥有独立贡献依据，而不只是C1算法的附录
- alternative_expression_and_tradeoff: 可写“此外，其端到端评价仍不充分”；较温和且易读，但把逐项没有全面评价改为集合不充分，强度/分配含义略变，须标注而不能自动替换
- scope_guard: 不能删全面变成完全没有任何端到端实验；这是2020作者近邻评价，不是本轮独立新颖性证明
- body_evidence_ids:
  - B4
- retained_clause_analysis: None

## P4.S1

- source_page: 2
- source_claim_paraphrase: 本文提出针对DNN声学系统的SirenAttack
- grammatical_main_proposition: 本文提出新攻击类别是主句
- discourse_foreground: 由问题/近邻转到本文交付
- new_information: 系统名称及总体研究对象
- contextual_grounds: 上一段留下访问、目标约束及评价缺口
- clause_relations: 篇章定位框架前置；同位短语说明交付类型；针对对象嵌在名词组内
- source_choice_editorial_inference: 先交可指代的总对象，再允许下一长句分解能力
- alternative_expression_and_tradeoff: 可将对象条件前置后再命名，如“针对DNN声学系统，我们提出SirenAttack”；适合新读者忘记对象时；不能直接写解决所有音频攻击限制
- scope_guard: 新类别是作者定位，不意味着所有组成算法均原创或普遍最优
- body_evidence_ids:
  - B3
- retained_clause_analysis: None

## P4.S2

- source_page: 2
- source_claim_paraphrase: 与近邻相比，作者声明跨系统/访问条件、定向输出及轻噪声低感知影响三项能力
- grammatical_main_proposition: 外层主句声称方案有重要差别；冒号后三个完整能力分句展开
- discourse_foreground: 真正话语前景是三种成功要求；外层主句只框定对照
- new_information: 范围与访问条件、控制输出、人的感知约束具体化
- contextual_grounds: 承接P3限制，但并非三个形容词与三个旧限制严格一一对应
- clause_relations: 三分支同层并列；定向分支的关系从句界定所生成音频的输出能力，括号举例；隐蔽分支用by引出加噪方式，用while引出伴随且带对照意味的低感知影响约束。这里不宜仅作时间同时理解，也不能把人的感知条件降为附带评价
- source_choice_editorial_inference: 长句可同时建立多轴契约；主干并不因语法外层而承载最多新信息。跨访问/多任务不能合成所有任务×所有权限笛卡尔积
- alternative_expression_and_tradeoff: 可拆三句分别给范围、定向、人感知要求；更便于各自接证据，但须保“多类”而非所有、白/黑盒的具体定义，以及小噪声与人的影响是独立待证关系
- scope_guard: 定向与非定向的可支持性在C1扩展；黑盒非无反馈；小扰动不自动等于完全不可闻，评价也不证明空中播放成立
- body_evidence_ids:
  - B2
  - B3
  - B5
  - B6
  - B7
  - B8
  - B9
- retained_clause_analysis: 比较主句引三分支，冒号后三个名词标签各接完整能力解释；这种长句适合并列定义同层成功标准。
- inherited_annotation_correction: 继承记录中“名词标签”的说法有误：原文三项为形容词能力标签，后接完整能力分句；保留旧字段只用于追踪，使用时以本更正为准

## P5.S1

- source_page: 2
- source_claim_paraphrase: 作者在其所知范围内自称首次系统研究多类端到端声学系统的对抗音频
- grammatical_main_proposition: 本工作代表首次系统性研究是主句
- discourse_foreground: 将前文多轴能力统合为研究定位
- new_information: 系统性研究作为新颖性对象，而非单个算法首次
- contextual_grounds: P4已给能力；下一贡献列可展开系统性含义
- clause_relations: 知识范围限定语前置，辖整个首次性判断；生成音频的动名词组说明研究内容；多类限定对象
- source_choice_editorial_inference: 新颖性包装把系统范围而非单次高成功率推到前景，但属于作者声明
- alternative_expression_and_tradeoff: 可说“据作者当时掌握的文献，这是首项覆盖多类端到端声学系统的系统研究”；用于分析报告保归属和历史；不可去掉范围限定写成今天仍首次
- scope_guard: 本轮不重做全球优先权检索；首次系统研究不等于首次定向音频攻击
- body_evidence_ids:
  - B4
- retained_clause_analysis: None

## P5.S2

- source_page: 2
- source_claim_paraphrase: 随后列举主要贡献
- grammatical_main_proposition: 主要贡献可如下概括是主句
- discourse_foreground: 组织路标，不新增技术事实
- new_information: 将后续项目识别为贡献集
- contextual_grounds: P5.S1已经定位全篇增量
- clause_relations: 情态被动属于文本组织，不能解读为研究未完成
- source_choice_editorial_inference: 短路标让读者切换到交付/证据清单
- alternative_expression_and_tradeoff: 可直接接贡献列表而删此路标；含义损失小，但会减弱首次性句与三个项目间的层级标记
- scope_guard: 不能把句中的可概括读成实验仅可能完成
- body_evidence_ids:

- retained_clause_analysis: None

## C1.S1

- source_page: 2
- source_claim_paraphrase: 方法贡献统合白盒与黑盒条件下针对DNN声学模型的攻击
- grammatical_main_proposition: 我们提出方案是主句
- discourse_foreground: 在贡献清单重新标定统一交付及访问范围
- new_information: 相对P4无主要新技术信息，功能为总括/回收
- contextual_grounds: P4已介绍方法；同一贡献内后两句首次拆方法分工
- clause_relations: 同位语重述类型；末尾双访问条件作用于整体攻击类别，而不证明同一个算法等同两权限
- source_choice_editorial_inference: 重复具贡献标题功能，不应仅以词汇重复判冗余
- alternative_expression_and_tradeoff: 可压成“方法覆盖两种访问条件，具体路线如下”；上下文清晰时减少命名复述，但不能丢模型对象或暗示所有系统均同时试验两种条件
- scope_guard: 覆盖是方法家族层主张；实验分工需要正文确认
- body_evidence_ids:
  - B2
  - B3
- retained_clause_analysis: None

## C1.S2

- source_page: 2
- source_claim_paraphrase: 白盒条件下结合启发式与梯度方法，支持定向和非定向任务
- grammatical_main_proposition: 我们结合两类方法为主句
- discourse_foreground: 访问条件下的方法分工
- new_information: 首次披露白盒组合路线及两类任务
- contextual_grounds: P4尚未解释实现；已知DNN攻击对象
- clause_relations: 前置访问框架限定整句；combine以启发式算法为宾语，with介词短语引入另一组合成分，两者是语义组合而非并列宾语；目的不定式给任务；斜杠为两个可支持目标，不表示一次攻击同时两者
- source_choice_editorial_inference: 保留旧分析；新补功能目标不等于该引言已报告两种任务各自效果
- alternative_expression_and_tradeoff: 可说“白盒路线以启发式搜索配合梯度调整，用于两类攻击目标”；保持组合关系；如果写先后两阶段，需明确增用§4.4.1信息，不称纯句式替换
- scope_guard: 白盒知道模型及参数；不要由组合推断黑盒同样取到梯度或所有表均测非定向
- body_evidence_ids:
  - B2
  - B3
  - B5
- retained_clause_analysis: For white-box先限定访问，主句combine说明路线，to交目标/非目标功能；下一句对称黑盒便于横向理解。

## C1.S3

- source_page: 2
- source_claim_paraphrase: 黑盒条件下提出迭代无梯度路线，支持定向与非定向任务
- grammatical_main_proposition: 我们提出一个新途径为外层主句
- discourse_foreground: 同白盒对照的可用信息差异与实现方式
- new_information: 无梯度路线首次披露；两目标在此分支继续保留
- contextual_grounds: 上句的访问分支建立平行阅读框架
- clause_relations: 前置黑盒范围；目的短语给任务；方式短语引出算法；强/迭代/无梯度三个修饰分别为评价、过程、访问特征
- source_choice_editorial_inference: 平行句帮助读者比较的是信息要求，不是把两个实现写成一个万能程序
- alternative_expression_and_tradeoff: 可将无梯度路线置主语，后接支持两任务；更突出信息条件，需另保新方案归属。“无梯度”不能换成“无模型反馈”
- scope_guard: 强是作者评价，不是独立结果；类别置信度仍需返回，只有转录的ASR不属于此直接接口
- body_evidence_ids:
  - B2
  - B3
  - B7
- retained_clause_analysis: None

## C2.S1

- source_page: 2
- source_claim_paraphrase: 评价覆盖多种DNN模型和三类声学应用
- grammatical_main_proposition: 我们评价方案为主句
- discourse_foreground: 给系统性范围的具体构成
- new_information: 命令、说话人和声音事件三类首次完整列实
- contextual_grounds: P1两类系统和P4多样性承诺需要实验回收
- clause_relations: 用于声学系统的后置修饰限定模型；包括引出的名单是场景层，不是算法三模块
- source_choice_editorial_inference: 名单先于数字让读者知道一个数字只是更大范围中的示例
- alternative_expression_and_tradeoff: 可先列三应用，再说各自的模型评价；在任务多样性重要时更醒目，但应说明不同任务的模型/条件有别，不制造完全同条件比较
- scope_guard: 此列三类主要对应§6分类任务；§5开放式ASR白盒另有证据，场景与访问不是完整交叉试验
- body_evidence_ids:
  - B1
  - B5
  - B6
  - B9
- retained_clause_analysis: None

## C2.S2

- source_page: 2
- source_claim_paraphrase: 实验结果表明方案高度有效，这是作者的概括性评价
- grammatical_main_proposition: 实验结果表明为语法外层主句，其宾语从句是高度有效性判断
- discourse_foreground: 话语前景为有效性结论，实验结果作证据来源
- new_information: 总评价而非具体新数值
- contextual_grounds: 上句已给评价范围，后句承担例证
- clause_relations: 证据主体＋报告谓语＋命题宾语；不能把外层主句“结果表明”当全部信息主张
- source_choice_editorial_inference: 短主题句给随后数值明确职责，避免读者自己猜为何看99.45%
- alternative_expression_and_tradeoff: 可说“方案在所测设置中高度有效，以下给一个实例”；把结论前置且保留原评价强度，加“所测设置”属于正文范围显化。若只写“有效”，须说明有意降低了评价强度；不能换成高效且不可察觉
- scope_guard: 有效只回答输出目标达成；不自动证明耗时低、查询少、扰动小或人的体验不变
- body_evidence_ids:
  - B5
  - B6
- retained_clause_analysis: None

## C2.S3

- source_page: 2
- source_claim_paraphrase: IEMOCAP数据集上针对ResNet18的成功率为99.45%，作为例子
- grammatical_main_proposition: 方案达到指定成功率是主句
- discourse_foreground: 有明确对象的量化例证
- new_information: 99.45%、数据集、目标模型为首次信息
- contextual_grounds: 前句有效性是需被例证的判断
- clause_relations: 句首例示限制话语功能；两个介词短语固定数据和目标模型；数字不能脱离条件独立传播
- source_choice_editorial_inference: 原文选此例展示多任务中的说话人设置；99.45%是Table4所列攻击成功率的最高值，但并非全文最高值。作者未自述为何选择此例，不能补写作者的心理原因
- alternative_expression_and_tradeoff: 可将条件前置成“在IEMOCAP的ResNet18说话人实验中，成功率为99.45%”；条件先读更稳；说话人/黑盒等来自正文，是有依据的语境扩写，不是源句自带
- scope_guard: §6.3报告1,000片段、每片九个目标，对应名义9,000个片段—目标组合；不是1,000名独立说话人或9,000名参与者。Table4给99.45%，但未充分交代可重算该率的逐次记录与汇总口径，因此不将9,000写成已独立核验的统计分母；更不能外推到云平台或所有数据/模型
- body_evidence_ids:
  - B6
- retained_clause_analysis: For instance表明例证地位，主句achieves数值，两个on/against短语固定数据与模型，避免数字无条件。

## C2.S4

- source_page: 2
- source_claim_paraphrase: 生成样本也能被多个ASR平台误解
- grammatical_main_proposition: 生成音频可被平台误解是被动主句
- discourse_foreground: 扩展到另类系统的现实平台证据
- new_information: 商业ASR名称及模型间迁移现象
- contextual_grounds: 前句是特定分类模型上的高成功率，当前换证据对象
- clause_relations: 添加/扩展衔接，不是同设条件的再例；情态表示能力非每例必达；平台名单非穷尽
- source_choice_editorial_inference: 把已有生成样本作主语，语言上没有声称在平台接口直接运行相同搜索；正文确认其为迁移
- alternative_expression_and_tradeoff: 可写“这些样本还展示了向若干ASR平台迁移的能力”；需附转录/命中定义而不能把泛误读全部改成原定目标；迁移是正文显化
- scope_guard: 500个VGG19生成样本、六平台的迁移测试。作者把Table7作为定向迁移结果报告，但Table8另列非目标误读；其成功例也包含非字面同串输出，具体接受规则未充分说明。平台误解不能概括为每例命中预设转录，更不能等同原分类黑盒接口的直接搜索
- body_evidence_ids:
  - B7
  - B9
- retained_clause_analysis: None

## C3.S1

- source_page: 2
- source_claim_paraphrase: 提出三种潜在缓解策略并作初步评价
- grammatical_main_proposition: 提出策略、开展评价为同主语并列谓词
- discourse_foreground: 防御探索作为另一个研究交付
- new_information: 三策略及初步评价的完成状态
- contextual_grounds: 攻击证据之后需要讨论防御空间，但不是已证明安全保证
- clause_relations: 目的不定式表示缓解目标；潜在修饰策略，初步修饰评价；两限定不可互替
- source_choice_editorial_inference: 结尾把工作增量扩展到防御研究方向，仍以真实研究阶段限制成果
- alternative_expression_and_tradeoff: 可说“我们还初步评估了三条候选防御路线”；偏重已做评价，却弱化提出策略的动作；若用于贡献压缩要确认是否保留作者的设计贡献
- scope_guard: 三种不是完备防御集；缓解不是消除；初评不是尚未实验，实际证据在§8而非旧图§7
- body_evidence_ids:
  - B10
- retained_clause_analysis: None

## C3.S2

- source_page: 2
- source_claim_paraphrase: 结果为更稳健声学系统的构建及后续研究提供启发
- grammatical_main_proposition: 结果承担两个并列谓词：启发构建、引出研究方向
- discourse_foreground: 研究意义及后续空间
- new_information: 没有新测量；解释前句初评的价值
- contextual_grounds: 已知防御还有限，故收束为启发而非安全性承诺
- clause_relations: 两个谓词平行但对象不同；更稳健的比较是研究方向，不含实现保证
- source_choice_editorial_inference: 旧分析保留；这里是C3整体结尾，不是为每个结果添加宏大意义的通用模板
- alternative_expression_and_tradeoff: 可合成“这些初步结果为稳健声学系统研究提供方向”；更紧凑但压缩了实践构建与研究方向的双对象，需标为信息合并
- scope_guard: 结果不证明已经建成更稳健系统，更不能换成抵御所有攻击；防御仍有残余成功和效用代价
- body_evidence_ids:
  - B10
- retained_clause_analysis: 两个并列谓词shed light/lead都属研究启发，未把潜在防御写成已提供安全保证。


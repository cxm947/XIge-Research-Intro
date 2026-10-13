# AWT：完整引言的语法、语篇与局部选择

- coordinate_policy: 沿用旧图P1–P5/C1–C3；C3.F1为残句，C3.S1为完整句；并非论文印刷编号。
- scope: 完整引言30个既有分析单元；含29完整句和1印刷片段。数量仅记录核验范围。
- method: 释义与语法/语篇分析；所有作者选择理由均为上下文编辑推断；备选逐项标出语义变化，不是一套无损改写库。

## P1.S1

- physical_pdf_page: 1
- source_location: Introduction左栏首句
- retained_clause: True
- syntactic_main_proposition: DNN在多领域取得成功；主语是DNN，成功是谓语断言，不能把主语本身等同全句焦点。
- dependent_structure: 范围介词结构统摄领域列举，列举不是四个平行的新研究任务。
- discourse_focus: 用应用广度为随后真实部署及威胁的意义铺垫。
- given_information: 仅借用读者对DNN的领域常识，前文引言没有已给命题。
- new_information: 跨领域成功及其广度。
- backward_dependency: 引言开头；不需把摘要当作已知输入。
- forward_dependency: P1.S2由能力转部署；P1.S3反转成功背景。
- contextual_choice_editorial_inference: 领域例子后置，保留上位技术作为连续三句话题；若从一个攻击数字开头，后面部署价值须另补。
- alternative:
  - local_rewrite_zh: DNN的成功已覆盖计算机视觉、语言、语音和自动驾驶等应用。
  - exact_semantic_change: 压缩展开方式，保留领域范围和成功断言；省掉强评价程度词，语气减弱，不是完全等义。
  - appropriate_context: 领域读者已熟悉这些应用、但下一句仍需要部署价值时。
- boundary: 
- retained_prior_analysis: 主句DNNs achieved success给已知背景；from…to…后置列领域，把广度放支撑而不抢主命题。长列举仅在入口用一次，后续马上缩到攻击。
- retained_analysis_status: Historical authored clause analysis, not a new final-review finding. Current syntactic main proposition, discourse focus and boundary fields provide the refined distinction.

## P1.S2

- physical_pdf_page: 1
- source_location: Introduction左栏第二句
- retained_clause: False
- syntactic_main_proposition: 大型模型的扩散加速DNN在现实中的采用；语法主语是扩散，不是算力或数据。
- dependent_structure: 过去分词插入语把算力和数据写为扩散的支持条件；不是另一个并列主句。
- discourse_focus: 从研究能力推进到现实采用，使脆弱性成为部署问题。
- given_information: P1.S1的DNN成功。
- new_information: 大型模型扩散及支持条件与采用加速的联系。
- backward_dependency: P1.S1能力广度。
- forward_dependency: P1.S3的风险与现实系统相关。
- contextual_choice_editorial_inference: 把算力/数据放插入位置，主干保存采用加速；不能据语法边缘位置认定其内容无关。
- alternative:
  - local_rewrite_zh: 在计算资源进步与大规模数据可得性的支持下，大型模型的扩散加速了DNN的现实采用。
  - exact_semantic_change: 把支持条件前置作框架，保留计算资源进步与大规模数据可得性两种原条件，没有改成数据增长；核心因果不变，起句路径由模型扩散改为资源条件。
  - appropriate_context: 若上文已经在讨论资源变化，而非DNN能力。
- boundary: 

## P1.S3

- physical_pdf_page: 1
- source_location: Introduction左栏末句至右栏顶部，跨栏续接
- retained_clause: False
- syntactic_main_proposition: DNN已被发现容易受到AE影响；主句保留技术系统为话题。
- dependent_structure: 前置让步回收成功；关系从句定义AE的误导作用；其中时间/对照从属结构交代人眼看来正常。
- discourse_focus: 现实成功背景下的隐蔽脆弱性；定义位于从句，却是首次出现AE时不可省的新内容。
- given_information: 成功与现实采用。
- new_information: AE是什么、机器误判与人类观察之间的差别。
- backward_dependency: P1.S1–2的收益面。
- forward_dependency: P2.S1才引出跨模型迁移这一个更具体风险。
- contextual_choice_editorial_inference: 把AE解释压进关系从句，主干不从DNN突然跳成术语词典，同时为后续所有AE指代建对象。
- alternative:
  - local_rewrite_zh: AE能够误导DNN，并可能在人眼看来正常；DNN因此面临安全风险。
  - exact_semantic_change: 把AE升为主语并拆开定义；将原源表述的人眼表象改成可能性，强度变弱；因此又新增显式推断，非等义替换。
  - appropriate_context: 若前文已定义DNN部署价值，且本段要以AE为连续话题；应另核实是否需要弱化。
- boundary: 

## P2.S1

- physical_pdf_page: 1
- source_location: Introduction右栏P2首句
- retained_clause: True
- syntactic_main_proposition: AE一个值得警惕的性质是跨模型迁移；系词主句把性质与迁移能力连接。
- dependent_structure: 前置视角限于实际攻击；后置结果分词说明无需目标架构/参数的能力。
- discourse_focus: 迁移性质及其黑盒任务价值共同构成此处焦点；任务价值虽在分词结构中，也是新信息。
- given_information: P1.S3已定义AE与风险。
- new_information: 跨模型迁移；为何缺目标内部访问时仍有意义。
- backward_dependency: P1.S3的隐蔽误导。
- forward_dependency: P2.S2的提高成功率与避免代理过拟合因此有目标。
- contextual_choice_editorial_inference: 先性质后后果符合首次引入迁移；若只根据主句位置认定焦点止于迁移，会漏掉前置实际视角选择的理由。
- alternative:
  - local_rewrite_zh: 攻击者可利用AE的跨模型迁移，无需直接访问目标模型的架构或参数也能产生有效扰动。
  - exact_semantic_change: 把攻击者能力前景化；原性质的警惕性评价不再显式。保留无直接访问条件，不改成对目标架构/参数一无所知，也不扩大为无任何目标信息。
  - appropriate_context: 读者已熟悉迁移概念、当前段要凸显黑盒任务可行性。
- boundary: 这里只讨论作者给定的访问范围，不推断无需任何数据/标签/模型。
- retained_prior_analysis: From a practical perspective前置限定判断视角；ability to transfer为主干焦点，allowing分词后置交“无需访问目标”的任务后果，先性质后价值。
- retained_analysis_status: Historical authored clause analysis, not a new final-review finding. Current syntactic main proposition, discourse focus and boundary fields provide the refined distinction.

## P2.S2

- physical_pdf_page: 1
- source_location: Introduction右栏P2第二句
- retained_clause: False
- syntactic_main_proposition: 研究者提出了多种迁移攻击方法。
- dependent_structure: 方法后的现在分词结构给双目标：更高成功率、避免对代理过拟合；并列的是两个目标，不是两个已证结果。
- discourse_focus: 从风险性质转已有方法的优化目标，为下一句分类和末句让步建立比较对象。
- given_information: P2.S1的迁移能力/黑盒用途。
- new_information: 改进成功率与抑制代理过拟合这对目标。
- backward_dependency: P2.S1。
- forward_dependency: P2.S3回答如何追求这些目标；P2.S4区分目标/效果与解释。
- contextual_choice_editorial_inference: 目标作为后置修饰而非完成式结果，给性能讨论留证据责任。
- alternative:
  - local_rewrite_zh: 现有迁移攻击以最大化成功率和避免对代理模型过拟合为目标。
  - exact_semantic_change: 压缩提出方法的历史行为与数量；保留最大化/避免两个目标的强度及意图性质，没有将目标改成已实现结果。
  - appropriate_context: 无需叙述方法提出过程、只需统一后续类别的共同目的时。
- boundary: 

## P2.S3

- physical_pdf_page: 1
- source_location: Introduction右栏P2第三句
- retained_clause: False
- syntactic_main_proposition: 这些方法利用不同策略生成可迁移AE。
- dependent_structure: 列举结构给输入变换、模型集成、梯度修正；集成项内的关系从句交代利用何种多模型输出；末尾目的不定式说明共同终点。
- discourse_focus: 不是列名越多越好，而是交出有能力的经验答案，让末句解释不足有具体范围。
- given_information: P2.S2的多种方法及双目标。
- new_information: 三类实现路径及其功能。
- backward_dependency: P2.S2的方法集合。
- forward_dependency: P2.S4这些方法的局部指代；P3转解释线索。
- contextual_choice_editorial_inference: 策略列表嵌在一个共同动作中，强调殊途同归；如果逐条只报缩写，下一句性能让步缺可理解对象。
- alternative:
  - local_rewrite_zh: 输入变换、模型集成与梯度修正分别从不同环节提高AE的迁移性。
  - exact_semantic_change: 概括为环节差异但省略增强/输出/动量的机制信息；将原目的表达改成效果断言，语义更强，不能当等义缩句。
  - appropriate_context: 只有相关效果已有独立证据且读者无需机制细分时。
- boundary: 

## P2.S4

- physical_pdf_page: 1
- source_location: Introduction右栏P2末句
- retained_clause: True
- syntactic_main_proposition: 主句是缺少清楚的迁移因素解释这一存在性判断。
- dependent_structure: 让步从句承认前述方法的性能改善；性能改善不是被否定的对象。
- discourse_focus: 评价轴由做得更好转为为何迁移；不足作用于本段这些方法的解释，不宜改读为整个领域从无理论。
- given_information: P2.S2–3已介绍改进方法。
- new_information: 性能成功仍不能独立完成机制解释。
- backward_dependency: P2.S3的这些方法。
- forward_dependency: P3.S1–2立即呈现经验和理论解释，迫使缺口作局部/递进解读。
- contextual_choice_editorial_inference: 句末提出解释问题，下一段不是重复失败而是承认更强近邻；此种上下文制约比单看否定词重要。
- alternative:
  - local_rewrite_zh: 这些方法改善了性能，但其改进背后的迁移因素仍缺少清楚解释。
  - exact_semantic_change: 把让步降级改成两个并列断言；核心对照保留，语用上较少把改善视为已承认背景；其明确收窄指代。
  - appropriate_context: 容易被误读为全领域无理论时；仍需紧接P3的既有理论。
- boundary: 
- retained_prior_analysis: Although让步把已承认的性能收益压入从句；主句no clear explanations将新缺口留作句末焦点，P3即解释有哪些已有解释。
- retained_analysis_status: Historical authored clause analysis, not a new final-review finding. Current syntactic main proposition, discourse focus and boundary fields provide the refined distinction.

## P3.S1

- physical_pdf_page:
  - 1
  - 2
- source_location: P3首句起于物理1页右栏底、续于2页左栏顶
- retained_clause: False
- syntactic_main_proposition: Wu等以经验方式探索模型特定因素并发现局部不平滑损害迁移。
- dependent_structure: 前置目的给为何探索；探索后的嵌入疑问承接因素问题；发现后的内容从句承载具体经验关系。
- discourse_focus: 具体发现虽在内容从句内，才是读者进入平滑性路线所需的新认识。
- given_information: P2.S4要求因素解释。
- new_information: 模型损失面局部不平滑与迁移表现之间的经验联系。
- backward_dependency: P2.S4的解释问题，不把引文存在当作已核验邻作全文。
- forward_dependency: P3.S2从经验联系升级为理论下界。
- contextual_choice_editorial_inference: 先报研究行为再给发现可以保留证据类型；将经验探索直接改成定理会改变知识地位。
- alternative:
  - local_rewrite_zh: Wu等的经验研究发现，模型损失面的局部不平滑会损害AE迁移。
  - exact_semantic_change: 删去研究目的和探索问句，保留经验来源与发现；关系内容前景化，未提升为证明。
  - appropriate_context: 上句已经明确提出因素问题，无需再重复目的时。
- boundary: 

## P3.S2

- physical_pdf_page: 2
- source_location: P3第二句
- retained_clause: False
- syntactic_main_proposition: Yang等把模型平滑性和梯度相似性与迁移下界建立理论联系。
- dependent_structure: 序列标记承接经验之后；同位解释列出两个因素；理论方式及首次定位修饰联系行为。
- discourse_focus: 已有理论是更强近邻，新内容是两因素—下界关系，不是泛泛又一篇相关工作。
- given_information: P3.S1经验平滑线索。
- new_information: 梯度相似性、下界及理论连接。
- backward_dependency: P3.S1的证据层级。
- forward_dependency: P3.S3的直觉回指；P4.S5不能声称从未有任何理论。
- contextual_choice_editorial_inference: 保留下界和第二因素，使后来要补的联系有明确对手；删除两者会夸大本文认识增量。
- alternative:
  - local_rewrite_zh: 已有理论将平滑性与梯度相似性共同联系到AE迁移性的下界。
  - exact_semantic_change: 去掉作者与首次时序主张，保留关系对象及理论性质；共同仅指二者均参与，不声称充分必要。
  - appropriate_context: 篇幅受限且文献归属由引用完整承担时。
- boundary: 首次性是论文对邻作的归属，本轮未独立搜索首创性。

## P3.S3

- physical_pdf_page: 2
- source_location: P3第三句
- retained_clause: True
- syntactic_main_proposition: 外层主句报告研究者提出了微调代理的路线；微调位于提出的补足结构，不是与提出并列的有限动词。
- dependent_structure: 前置回指继承理论直觉；微调目的在增强平滑性；后置原因说明平滑代理上生成AE已有更好迁移表现。
- discourse_focus: 从认识到方法选择的继承，并以经验收益给该选择实际理由。
- given_information: P3.S2理论联系及P3.S1平滑线索。
- new_information: 微调代理这一研究路线；平滑代理带来收益的经验动机。
- backward_dependency: 直觉最邻近P3.S2，连同P3.S1的铺垫。
- forward_dependency: P3.S4检查这条方法路线的实际条件，而非推翻理论。
- contextual_choice_editorial_inference: 保留原因从句表明理论联系与经验表现都被作者用作方法理由；不能写成定理必然推出唯一算法。
- alternative:
  - local_rewrite_zh: 受这些分析启发，研究者提出微调代理以增强平滑性；平滑代理上生成的AE已表现出更好的迁移性。
  - exact_semantic_change: 拆开原因结构，保留两事实但削弱两者显式论证关系；启发仍是方法来源而非逻辑必然。
  - appropriate_context: 原因从句过长时可拆，但若需要明确论证应另补因果连接。
- boundary: 
- retained_prior_analysis: With this intuition回指已给理论；主句finetune建立既有路线，since后置说明平滑代理实证收益。原因在后是为先让读者接住方法继承链。
- retained_analysis_status: Historical authored clause analysis, not a new final-review finding. Current syntactic main proposition, discourse focus and boundary fields provide the refined distinction.

## P3.S4

- physical_pdf_page: 2
- source_location: P3第四句
- retained_clause: True
- syntactic_main_proposition: 两个并列主句：相关方法假设可取得目标训练分布相近的额外数据；大规模调参增加计算开销。
- dependent_structure: 第一主句内的内容从句给数据取得假设，分布结构限定数据；第二主句独立增加时间/计算负担。
- discourse_focus: 方法有效不等于易用；数据可得与计算成本是两个条件，不能互相替代。
- given_information: P3.S3的微调路线。
- new_information: 分布相近的额外数据假设，以及大规模调整成本；后文P4.S3改用同分布措辞，两处源表述不完全相同。
- backward_dependency: P3.S3强近邻。
- forward_dependency: P4.S3重提可得性；P5.S4回应额外数据，但不消灭所有计算成本。
- contextual_choice_editorial_inference: 并列成本而不是仅批评效果，为无额外数据设现实价值；全称这些方法属于作者所述集合，不外推所有模型法。
- alternative:
  - local_rewrite_zh: 这类方法既依赖额外的近分布数据，也需要承担在大规模数据上调整模型的计算成本。
  - exact_semantic_change: 把两个主句合成相关路线的双负担；保留数据与成本的独立性，弱化原文全称范围。
  - appropriate_context: 概述特定近邻集合时；应保留该集合引用。
- boundary: 物理第7页限制段仍报告AWT额外反传成本；无额外数据不等于无数据、无标签或零计算。
- retained_prior_analysis: Nevertheless转折后主句列额外数据假设，and并列再加计算成本；同句共享“微调路线的现实代价”，不把两者误成同一机制。
- retained_analysis_status: Historical authored clause analysis, not a new final-review finding. Current syntactic main proposition, discourse focus and boundary fields provide the refined distinction.

## P3.S5

- physical_pdf_page: 2
- source_location: P3末句
- retained_clause: False
- syntactic_main_proposition: 近期另一类方法能通过优化AE局部平坦极值达到先进迁移表现。
- dependent_structure: 前置比较划开模型路线；手段结构给输入端极值；图示附加语将该路线绑定黑至蓝点。
- discourse_focus: 建立另一强答案及其不同调整空间，为后面共同解释与联合方法提供第二端。
- given_information: P3.S3–4模型调整路线。
- new_information: 输入端平坦极值的强表现。
- backward_dependency: 不同于回指模型法。
- forward_dependency: P4.S5将两族放入同一机制问题；P5.S3–5回收联系与图示。
- contextual_choice_editorial_inference: 此句没有将新列出的输入路线说成失败者；若只接数据成本直接宣告AWT，联合两端将缺一条已有能力。
- alternative:
  - local_rewrite_zh: 与调整模型的路线相比，另一类方法优化AE所在的局部平坦区域，已有很强的迁移表现。
  - exact_semantic_change: 删除原最先进程度主张及图中黑蓝锚；弱化评价、保留路线差异；局部平坦区域不指定最大/最小号约定。
  - appropriate_context: 需要压缩图引用而方法对照仍须可理解时。
- boundary: 原文兼列极大/极小；图注与损失约定不宜擅自统一。

## P4.S1

- physical_pdf_page: 2
- source_location: P4首句
- retained_clause: False
- syntactic_main_proposition: 主句说仍有局限。
- dependent_structure: 让步从句承认这些方法已显著提高迁移。
- discourse_focus: 这是进入四个具体限制的组织门，不是新增一个独立机制缺陷。
- given_information: P3两条强路线。
- new_information: 将要逐项检视的剩余不足。
- backward_dependency: P3.S5终点与整个P3。
- forward_dependency: P4.S2–5分别展开。
- contextual_choice_editorial_inference: 先承认进步，随后批评对准评价、条件、优化对象与解释；不应四项都改写成性能不足。
- alternative:
  - local_rewrite_zh: 这些方法已显著提高迁移性，但仍有以下局限。
  - exact_semantic_change: 将前置让步从句改成并列转折，保留显著提高迁移性的具体性能断言；增补以下指向显式枚举，没有改为泛泛的研究进步。
  - appropriate_context: 需要更直接引出列表时。
- boundary: 

## P4.S2

- physical_pdf_page: 2
- source_location: P4编号(1)
- retained_clause: False
- syntactic_main_proposition: 许多方法依赖不同模型上的经验评价。
- dependent_structure: 后置分词结构给所缺少的统一代表性度量；目的不定式限定度量是跨架构测迁移。
- discourse_focus: 真正诊断焦点在后置缺项，不是把经验评价本身定为错误。
- given_information: 已有方法表现的经验性描述。
- new_information: 跨模型比较缺乏统一代表度量这一评价需求。
- backward_dependency: P2.S4解释不足与P3已有表现；此句另开评价轴。
- forward_dependency: P5.S1的形式化及P5.S6/C3的新增metric。
- contextual_choice_editorial_inference: 语法主句只是指出实践，后置缺项才推进论文需求；这直接反驳主句自动等于全部新信息的机械规则。
- alternative:
  - local_rewrite_zh: 许多现有方法虽依赖不同模型上的经验评价，仍缺少统一且有代表性的跨架构迁移度量。
  - exact_semantic_change: 把后置缺项升为主句、评价实践降为让步；保留依赖经验评价的关系，没有弱化成仅曾被评价。不声称经验评价无价值。
  - appropriate_context: 读者误以为论文反对真实目标测试时，可用它厘清评价补充关系。
- boundary: 统一与跨架构是引言目标；正文新度量仍受同架构/相似性限制。

## P4.S3

- physical_pdf_page: 2
- source_location: P4编号(2)
- retained_clause: False
- syntactic_main_proposition: 模型类方法要求额外数据。
- dependent_structure: 括号限定数据分布；关系从句对实际可行性作可能性评价，语义针对取得此类数据/满足要求，不能窄指目标模型本身不可行。
- discourse_focus: 把前段成本中的数据条件拎成实际部署障碍，保留可能而非永远不可得。
- given_information: P3.S4额外数据假设。
- new_information: 现实场景未必满足条件的明确评价。
- backward_dependency: P3.S4重复对象、推进价值判断。
- forward_dependency: P5.S4末尾条件承诺；C2再次保留。
- contextual_choice_editorial_inference: 重复并非必然冗余：前段是比较路线，列表是归纳研究需求；若删必须确保下一段无数据价值有前因。
- alternative:
  - local_rewrite_zh: 现实应用未必能提供模型调整方法所需的同分布额外数据。
  - exact_semantic_change: 把可行性升为主句，数据需求嵌入限定；保留未必范围；省去模型类方法全称暗示。
  - appropriate_context: 当前段落聚焦现实约束而非分类时。
- boundary: 

## P4.S4

- physical_pdf_page: 2
- source_location: P4编号(3)
- retained_clause: True
- syntactic_main_proposition: 模型类方法只在良性样本上优化更平滑的景观。
- dependent_structure: 结果分词报告次优；其后的原因从句以AE常为迭代生成解释为什么该优化对象限制会造成失配。
- discourse_focus: 不是只有额外数据贵，还存在随生成变化的优化对象与静态良性对象之间的适配问题。
- given_information: P3的平滑代理路线与P2生成任务。
- new_information: 只顾良性样本的对象局限；迭代AE说明为何需动态适配。
- backward_dependency: P4.S3是并列限制，不是本句技术原因。
- forward_dependency: P5.S4使用已生成AE调参数；C2的两过程联系。
- contextual_choice_editorial_inference: 原因后置让读者先识别限制及后果再解释根因；这里只能说作者归因，不能把一次句法分析升级为实验证明。
- alternative:
  - local_rewrite_zh: 由于AE通常逐步生成，仅围绕良性样本平滑代理可能无法跟随生成过程，因而表现次优。
  - exact_semantic_change: 补明跟随生成过程这一上下文推断，并把原次优断言弱化为可能；因果解释更显式但不完全等义。
  - appropriate_context: 需要给非本领域读者补出对象失配这一中间推理时，必须标明解释性增补。
- boundary: 
- retained_prior_analysis: 主句only optimize…benign限制优化对象；leading to结果分词给次优，since从句解释AE迭代变化，形成条件→后果→技术原因的逆向解释。
- retained_analysis_status: Historical authored clause analysis, not a new final-review finding. Current syntactic main proposition, discourse focus and boundary fields provide the refined distinction.

## P4.S5

- physical_pdf_page: 2
- source_location: P4编号(4)
- retained_clause: False
- syntactic_main_proposition: 梯度类与模型类方法没有解释相应因素为何提升跨模型泛化。
- dependent_structure: 嵌入为何问句是解释的内容；内部平坦极值或平滑性的选择不能读成两者恒等或已证明互相必要。
- discourse_focus: 统一两条路线的机制问题，承接P3的强结果；并非否认P3.S2已经存在的所有理论。
- given_information: P3.S2理论下界；P3.S3/S5两路线。
- new_information: 当前作者所要补的平坦性/平滑性与泛化之间的连接。
- backward_dependency: 两个路线和P4.S2评价需求共同回收。
- forward_dependency: P4.S6归结为定义及联系；P5.S3给作者的连接答复。
- contextual_choice_editorial_inference: 双主语合并不是为了制造两个失败者，而是构成同一个解释对象；整段上下文应收紧绝对缺解释措辞。
- alternative:
  - local_rewrite_zh: 现有两条路线仍未充分说明输入平坦性和模型平滑性如何共同关联跨模型泛化。
  - exact_semantic_change: 加入充分及共同，缓和原全称否定并聚焦联合关系；是更窄编辑定位，不是原句逐字等义。
  - appropriate_context: 撰写自己的增量定位且已有理论必须正面承认时；需实际核验最近工作才能采用。
- boundary: 

## P4.S6

- physical_pdf_page: 2
- source_location: P4末句
- retained_clause: False
- syntactic_main_proposition: 外层是形式主语结构：形式化定义与寻找因素联系被判为必要。
- dependent_structure: 两个并列不定式共同承担研究需求；末尾关系从句预期这些工作增进理解，非新增实证结果。
- discourse_focus: 把四项局限收束成认识任务，并为下一段先讲形式化而非先报算法作准备。
- given_information: 四项问题及两因素。
- new_information: 本文首先要完成的研究动作与预期解释价值。
- backward_dependency: 因此对整个列表综合，不仅由上一句推出。
- forward_dependency: P5.S1回应定义，P5.S2–3回应联系，P5.S4才是方法。
- contextual_choice_editorial_inference: 收束仍是认识目标，不直接许诺消除所有现实约束；若把此句写成所以设计算法，会跳过理论产品的来由。
- alternative:
  - local_rewrite_zh: 因此，我们需要明确可迁移AE的定义，并将它与上述因素联系起来，以加深对迁移性的理解。
  - exact_semantic_change: 把无人称必要判断改成作者共同体需求；最后从相对结果预期改为目的，保留但略弱化将带来洞察的预断。
  - appropriate_context: 作者声音允许更直接承担研究任务时。
- boundary: 

## P5.S1

- physical_pdf_page: 2
- source_location: P5首句
- retained_clause: False
- syntactic_main_proposition: 作者重新思考可迁移AE并从泛化视角形成新表述。
- dependent_structure: 开头目的回指P4.S6；并列谓语先思考后形成，末尾测量目的交代形式化用途。
- discourse_focus: 第一项工作是认识/测量对象重述，方法尚未登场。
- given_information: P4.S6的定义与联系需求。
- new_information: 以泛化为视角的形式化；测量用途。
- backward_dependency: 为此指整组认识需求。
- forward_dependency: P5.S2以前述形式化的洞察为输入。
- contextual_choice_editorial_inference: 并列活动不自动形成严格时间历史；这里是读者理解顺序，不能反推作者实际研发流程。
- alternative:
  - local_rewrite_zh: 为回应这些需求，我们从泛化视角重新表述AE迁移性，并据此构造其测量方式。
  - exact_semantic_change: 压缩重新思考活动，并把测量由用途提升成已构造的方法；后一加强超出原句字面，不作等义方案。
  - appropriate_context: 只有正文确实给出可计算度量且本段要突出测量产物时；需标正文补充。
- boundary: 

## P5.S2

- physical_pdf_page: 2
- source_location: P5第二句
- retained_clause: False
- syntactic_main_proposition: 外层主句两个并列研究行为：分析跨模型泛化；证明一个局部扰动存在性命题。
- dependent_structure: 前置结构回指形式化洞察；证明的内容从句报告总能找到局部扰动，末尾目的限定扰动用于减轻代理目标差异。
- discourse_focus: 新信息是作者主张的联系性结论，其出现于内容从句不削弱论述中心；分析行为本身不是唯一焦点。
- given_information: P5.S1形式化。
- new_information: 局部扰动桥接模型差异的理论主张。
- backward_dependency: P5.S1→分析起点。
- forward_dependency: P5.S3称这些洞察并连接两因素；P5.S4建立联合方法动机。
- contextual_choice_editorial_inference: 先给形式化才给理论，使读者知道证明为了什么；但引言跨架构广措辞不能抹去正文先作同架构参数变化近似。
- alternative:
  - local_rewrite_zh: 在同架构且参数局部变化的分析设定中，作者把模型差异与输入局部扰动联系起来。
  - exact_semantic_change: 删除引言跨架构概述和总能找到的强量词，补入正文条件；这是范围校准后的转述，不是原句等义重写。
  - appropriate_context: 解释本文理论适用范围、避免把跨架构实证读成普适定理时。
- boundary: 正文物理3页先作同架构简化；物理10页列参数连续性和输入Lipschitz假设。本轮读条件与功能，不验证证明有效性。

## P5.S3

- physical_pdf_page: 2
- source_location: P5第三句
- retained_clause: False
- syntactic_main_proposition: 作者观察到模型平滑与局部平坦极值的内在联系。
- dependent_structure: 进一步及前置洞察回指加深已有分析；关系从句说明两者均有助迁移，而非给出等价命题。
- discourse_focus: 两个先前独立路线的关联是方法联合的理由，关系从句又把联系锁回研究任务。
- given_information: P3两因素；P5.S2模型差异桥接。
- new_information: 本文观察到内在联系的解释产品。
- backward_dependency: 这些洞察承P5.S1–2。
- forward_dependency: P5.S4据此同时调整两端。
- contextual_choice_editorial_inference: 语法上观察是主句动词，不应自动弱化为随意猜想；知识强度要结合正文命题与Fig.2，仍不可称两因素恒等。
- alternative:
  - local_rewrite_zh: 上述分析进一步把模型平滑性与AE局部平坦性联系起来，二者都与迁移表现相关。
  - exact_semantic_change: 把作者观察换成分析产物；将有助迁移的作用措辞弱化为相关，不能当原文无损改写。
  - appropriate_context: 仅有关系证据、不拟承担因果主张的自身论文情境。
- boundary: Fig.2测输入/参数梯度范数相关，不能当直接跨架构ASR验证。

## P5.S4

- physical_pdf_page: 2
- source_location: P5第四句
- retained_clause: True
- syntactic_main_proposition: 作者提出并命名AWT；句法外层主句是方法提出行为。
- dependent_structure: 前置依据承接联系；同位名命名；关系从句说明用生成AE自适应调代理参数；目的结构含两因素同时优化；句末排除额外数据需求。
- discourse_focus: 命名不是全部新信息；从句里的输入来源、调整对象、联合目标与数据条件共同区分此法。
- given_information: P5.S3认识连接；P4.S3–4的成本和对象问题。
- new_information: AWT及其设计响应：生成AE参与适配、两因素、无需额外数据。
- backward_dependency: 据此更具体承两因素联系，也以P5.S1–2为上游。
- forward_dependency: P5.S5图示双空间；C2重新把方法对齐理论与两族。
- contextual_choice_editorial_inference: 迟到的方法名是有前因的产物；句末数据条件回收现实障碍，而非为押尾强行加卖点。
- alternative:
  - local_rewrite_zh: 基于两因素之间的联系，我们提出AWT：该方法以生成中的AE调整代理参数，同时关注AE局部平坦性与模型平滑性，且不需额外训练数据。
  - exact_semantic_change: 拆开主句/关系结构以凸显设计；生成中取自正文对中间AE的解释；额外训练数据收窄无额外数据的裸称；关注较原优化弱。
  - appropriate_context: 需要解释设计依据但不提供实现细节的文献综述。
- boundary: 算法仍使用良性输入及标签；无额外训练集不等于无输入或零计算。
- retained_prior_analysis: Based on this将研究联系置为已知；主句命名AWT，which从句承担调整对象/联合优化，末尾without短语把实际条件作压轴能力。
- retained_analysis_status: Historical authored clause analysis, not a new final-review finding. Current syntactic main proposition, discourse focus and boundary fields provide the refined distinction.

## P5.S5

- physical_pdf_page: 2
- source_location: P5第五句
- retained_clause: False
- syntactic_main_proposition: 更好迁移可以通过输入与参数空间实现。
- dependent_structure: 前置图示证据提示，橙点括号标识直观对象；能力情态不等于所有模型上的必然收益。
- discourse_focus: 用同一Fig.1把P3黑蓝路线更新为橙色联合路线，提供图文回环。
- given_information: P3.S5黑至蓝点、P5.S4联合设计。
- new_information: 橙点如何代表新方法的双空间选择。
- backward_dependency: P3.S5与P5.S4。
- forward_dependency: P5.S6离开示意图，转实际评价。
- contextual_choice_editorial_inference: 此句角色是直觉示意，不应被算作独立效果实验；示意图的支持层级低于结果表。
- alternative:
  - local_rewrite_zh: 图1中的橙点示意同时考虑输入与参数空间的迁移改进路径。
  - exact_semantic_change: 把可实现的能力断言降为示意路径，减少实际效果承诺；保留图文定位，不是完全同义。
  - appropriate_context: 图只承担直觉、不应承担经验验证时。
- boundary: 

## P5.S6

- physical_pdf_page: 2
- source_location: P5第六句
- retained_clause: False
- syntactic_main_proposition: 作者在多种模型上评价AWT。
- dependent_structure: 评价手段为并列的传统实验和由形式化导出的度量；后置过去分词仅修饰度量来源，不说明两种手段完全等价。
- discourse_focus: 把方法效果与解释性度量的表现作为两条互补评价线；这是设计预告，还未给胜负结果。
- given_information: AWT、形式化。
- new_information: 两种评价路径同时使用。
- backward_dependency: P5.S4方法和P5.S1形式化。
- forward_dependency: C3补评价范围、比较数量、胜出结论；正文表1/2与表4分工。
- contextual_choice_editorial_inference: 实验和新度量并列不是互相替代；若删除实验只留新分数，会造成用自定义目标自证方法成功。
- alternative:
  - local_rewrite_zh: 我们在多模型任务测试中评价AWT，并用形式化导出的度量作补充诊断。
  - exact_semantic_change: 加入补充诊断的关系层级，依据正文限制而非原句显式用词；保留两路评价、收紧度量权能。
  - appropriate_context: 向读者解释证据职责、避免以代理量替代任务效果时。
- boundary: 图3也是目标端响应代理，不是ASR；表1/2才报告ASR。

## P5.S7

- physical_pdf_page: 2
- source_location: P5末句、贡献列表导语
- retained_clause: False
- syntactic_main_proposition: 主句告知贡献如下。
- dependent_structure: 没有需补足的内容从句；指示向后到三个项目。
- discourse_focus: 导航及将前述工作重组为可评价贡献；此句不提出新技术命题。
- given_information: P5.S1–6的全链。
- new_information: 新的呈现组织；没有新增科学结果。
- backward_dependency: 整段工作概述。
- forward_dependency: C1理论、C2方法、C3评价三项。
- contextual_choice_editorial_inference: 保留短组织句便于跨栏列表辨认；不应用所有句必须包含技术新信息的规则强改。
- alternative:
  - local_rewrite_zh: 本文的贡献包括以下三项。
  - exact_semantic_change: 显式加入三项数量，未增加主要这一重要性筛选；当前印刷结构支持该数量，但列表日后变化必须同步更新。
  - appropriate_context: 贡献确实稳定为三项时。
- boundary: 

## C1.S1

- physical_pdf_page: 2
- source_location: 第一贡献项目，2页左栏底续右栏首行
- retained_clause: False
- syntactic_main_proposition: 作者理论分析迁移并揭示相关内在因素；两个并列谓语构成一项理论贡献。
- dependent_structure: 限制性关系从句说明因素对迁移的解释作用；末尾非限制关系从句指其此前被忽略，语义较可能回指这些因素/关系，但邻近AE名词造成附着歧义。
- discourse_focus: 代理模型和AE两端因素构成知识产品；贡献句将分析行为与揭示所得合在一起。
- given_information: P5.S2–3理论和联系。
- new_information: 引言前文基础上的浓缩定位；此前被忽略是强化的相对新颖性主张。
- backward_dependency: P4.S5问题和P5理论回答。
- forward_dependency: C2以这些分析为方法依据。
- contextual_choice_editorial_inference: 若只留下理论分析这个动作，所得对象会消失；若绝对化忽略又会抹去P3已有理论。
- alternative:
  - local_rewrite_zh: 我们分析AE迁移，并揭示代理模型与AE两类因素同迁移表现之间的关联。
  - exact_semantic_change: 删除理论方式及此前被忽略的新颖性主张；把因素对迁移的解释作用减弱成因素与迁移表现的关联。没有改成两类因素相互之间的关系；后者虽可由P5.S3讨论，却不是此处的替换对象。
  - appropriate_context: 只有关联证据而不准备承担全部解释/新颖性责任的自身文本。
- boundary: 原末尾关系从句有附着歧义，不把AE本身以前被忽视当合理历史事实；此处首创性未独立核验。

## C2.S1

- physical_pdf_page: 2
- source_location: 第二贡献项目首句
- retained_clause: True
- syntactic_main_proposition: 被动主句说AWT这一无额外数据调整方法被开发；不是作者作主语。
- dependent_structure: 前置依据将方法置于理论之后；手段结构给参数自适应；同时结构在该操作内协调扰动优化。末尾更好迁移直接修饰扰动，功能上亦回应全法目标。
- discourse_focus: 方法如何连接参数与输入两种变化；被动凸显产物，但不等于作者消失或科学客观性增强。
- given_information: C1分析及P5.S4已介绍AWT。
- new_information: 贡献层面的凝缩联动，不是新的第三种算法。
- backward_dependency: 根据上文分析可含C1和P5理论。
- forward_dependency: C2.S2给两族结合的相对定位。
- contextual_choice_editorial_inference: 同时结构承担过程协同；若改成先调完模型再优化扰动，会改变方法时序，而不是纯风格。
- alternative:
  - local_rewrite_zh: 根据上述分析，AWT在优化扰动的同时自适应调整代理参数，以提高迁移性且无需额外训练数据。
  - exact_semantic_change: 把被动开发改成方法行为，过程协同保留；目的提升为整体终点，并用正文校准额外训练数据，非逐项字面等义。
  - appropriate_context: 方法名已知、需要突出相互适配机制时。
- boundary: 原保留注释把更好迁移视作共享终点可作功能解释，语法附着需同时记为对扰动的后置修饰。
- retained_prior_analysis: Based on the analysis above使方法属于理论所得；被动主句突出artifact而非作者，by与while并行交权重/输入两操作，better transferability作为共同终点。
- retained_analysis_status: Historical authored clause analysis, not a new final-review finding. Current syntactic main proposition, discourse focus and boundary fields provide the refined distinction.

## C2.S2

- physical_pdf_page: 2
- source_location: 第二贡献项目末句
- retained_clause: False
- syntactic_main_proposition: AWT被定位为首个结合梯度类与模型类方法以改善迁移的方法。
- dependent_structure: 前置知识限定约束首次性；关系从句规定首次的具体组合；目的不定式给任务而不是任意结合。
- discourse_focus: 相对文献的新颖性范围是这两类方法为迁移而结合，并受作者知识范围限定。
- given_information: P3两路线及C2.S1联动方法。
- new_information: 首次结合的定位主张。
- backward_dependency: P3的分类使首次对象可理解。
- forward_dependency: C3提供实证，不能独立证明文献首创。
- contextual_choice_editorial_inference: 知识限定不是装饰：去掉会从可修正的文献判断升级成无条件优先权；保留任务范围也避免任意组合偷换。
- alternative:
  - local_rewrite_zh: 据作者所知，AWT首次将梯度类和模型类迁移攻击结合起来。
  - exact_semantic_change: 保留归属和知识限制，压缩用途为迁移攻击；省略显式增强目标，不另证明首创性。
  - appropriate_context: 综述转述作者定位而非已独立完成全领域查新时。
- boundary: 

## C3.F1

- physical_pdf_page: 2
- source_location: 第三贡献项目句号前片段
- retained_clause: False
- syntactic_main_proposition: 无完整有限谓语主句：连接副词加介词结构，在句号处终止；这是源形式记录，不预设贡献项目必须为完整句。
- dependent_structure: 介词结构中把形式化作为跨模型度量；按印刷句号不能把其硬标成完整句。
- discourse_focus: 回收形式化作为评价资源，并给下一完整句设框架；内容已知，语义可跨句号继续，不据此判断是否排印事故或有意片段。
- given_information: P5.S1形式化与P5.S6新度量。
- new_information: 没有新增研究结果，仅重新激活评价轴。
- backward_dependency: P5.S6。
- forward_dependency: C3.S1完整评价句。
- contextual_choice_editorial_inference: 记录非有限片段及其框架职责；若自身文体允许标题式片段，未必需要修成整句。源作者为何分句本轮不能判定。
- alternative:
  - local_rewrite_zh: 以该形式化作为跨模型迁移度量，我们进一步在CNN与Transformer上评价AWT，并比较其攻击成功率与度量表现。
  - exact_semantic_change: 将框架附着下一有限主句而非独立句号片段；示例另压缩了数据集、八基线和优越性结果，因此是结构示范加内容删减，不是完全等义替换。
  - appropriate_context: 自身目标文体需要连续完整句时可考虑合并；保留片段亦可，不能普遍要求所有贡献成句。
- boundary: 旧图已标C3.F1；helper段落摘要已明确识别其为介词片段、有句号而无完整谓语，贡献摘要也已区分片段与完整句。本次新增的是更细的语法/修辞分层、允许贡献片段的使用情境及不推断排印事故的边界，而非首次发现片段。

## C3.S1

- physical_pdf_page: 2
- source_location: 第三贡献项目剩余完整句
- retained_clause: False
- syntactic_main_proposition: 作者开展实验并展示AWT优于八种强比较方法；后者内容从句包含结果，外层仍是两个并列研究行为。
- dependent_structure: 架构族和数据集限定实验范围；展示后的内容从句给ASR与metric双结果；不是用新度量证明ASR数值。
- discourse_focus: 首次明确CNN/Transformer、ImageNet及八个比较方法，且将两评价轴的优越性作为证据产品。
- given_information: P5.S6已知双评价但无具体范围/胜负。
- new_information: 架构族、数据集、比较数量与双轴结果均在此进入引言。
- backward_dependency: P5.S6评价设计，C1/C2待支持贡献。
- forward_dependency: 正文Tables 1–2给ASR；Table4给度量；Fig3和限制段给度量适用边界。
- contextual_choice_editorial_inference: 不重报摘要平均改进数，是在有限篇幅里优先交出范围和证据轴；这是上下文编辑推断，不声称作者自述删数动机。
- alternative:
  - local_rewrite_zh: 在ImageNet兼容数据集上的CNN与Transformer测试中，AWT相对八种比较方法取得更高ASR和更低诊断度量。
  - exact_semantic_change: 以正文补入兼容、明确两个指标方向，并把度量收紧为诊断；删除全面/最先进等评价。这是有据校准，不是原句完整等义。
  - appropriate_context: 论文评述需准确区分测试对象、方向与测量角色时。
- boundary: 数据实际为ImageNet兼容的1000张图像；八基线加AWT共九方法，不能说优于九基线；更好metric指更低。


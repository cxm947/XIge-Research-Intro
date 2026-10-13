# FaceArmor：十八组定点分析与条件性局部替换

- record_count: 18
- refined_units:
  - P1.S3
  - P1.S5
  - P10.S1
  - P10.S2
  - P2.S3
  - P2.S4
  - P2.S5
  - P3.S2
  - P3.S5
  - P3.S6
  - P4.S1
  - P4.S2
  - P4.S3
  - P4.S4
  - P4.S5
  - P5.S1
  - P5.S2
  - P5.S3
  - P5.S4
  - P6.S2
  - P6.S3
  - P6.S4
  - P6.S5
  - P7.S1
  - P7.S2
  - P8.S1
  - P8.S2
  - P9.S1
  - P9.S2
- source_text_exclusion_note: Raw source spans and complete spliced source sentences are excluded. Unit IDs, exact Unicode offsets, span hashes and applied-sentence hashes bind the accepted local edit; they do not prove semantic equivalence. Complete authored replacements and all conditions/costs remain.
- analysis_scope_preamble: 完整41单元底稿和三条既有英文例句另保。18组精化只处理实际需要区分的关系；源观察不等于机制已独立验证，编辑推断不冒充作者心理。矩阵为语法主干，不自动等于最重要的新信息。局部方案标明保义、前景改变或范围/强度调整，均须连读拼回整句。

## FA01

- units:
  - P1.S3
  - P1.S5
- refinement_reason: 旧稿已交危害与任务；补危害是能力/可能后果，任务主语为嵌入问题而非直接断言已实现保护。
- source_observation:
  - matrix: S3 Malicious users can manipulate；S5 how to protect...这个嵌入不定式疑问作主语，has become为主谓。
  - dependency: to fabricate给不当用途；that can...修饰假内容并列社会后果。S5 such a diverse ecosystem回指四范式，不是泛安全重要性。
- editorial_inference:
  - foreground: 读者需要的任务是保护公开分享照片不被再利用；危害不是所有正常图像编辑都恶意的定义。
  - information_progression: 公开可得照片→伪造可伤害主体→多范式保护问题；图1和§5.6进一步给分享前处理场景。
  - privacy_and_task_value: 保护身份与分享效用共同决定成功标准，不能把生成图像变差就自动等同现实隐私风险归零。
  - relative_length: 危害一句足够，任务句紧收四范式；不必再加法律/社会调查来支持本篇技术目标。
- local_replacement:
  - unit: P1.S5
  - unit_start: 11
  - unit_end: 90
  - intro_start: 781
  - intro_end: 860
  - source_span_sha256: e398201edd2d8ba8ce1341bb555cf63d61a5c795c45227d4719646b0a73fa31c
  - replacement: protecting facial photographs from manipulation by such a diverse ecosystem
  - semantic_scope_and_cost: 疑问主语改动名词主语，原has become保持；从提出如何做的问题转为命名保护活动，任务范围不变但问题感减弱。
  - selection_condition: 需要直接命名任务而不想嵌how问句时。
  - applied_sentence_sha256: 4e72b471b603fe76ca50f04049a85806f1b03ce198cb694291411c5ae2cf32dc

## FA02

- units:
  - P2.S3
  - P2.S4
- refinement_reason: 旧稿已有代理白盒/目标未知边界；补overwhelmingly、typically和known model在不同层的范围。
- source_observation:
  - matrix: S3 existing methods are characterized；S4 They target components。
  - dependency: overwhelmingly不是无例外全称；typically限定惯用策略；known限定模型，such as列VAE/U-Net例子。
- editorial_inference:
  - foreground: 前人已有可行主动保护，但依赖已知组件；差异对象是未来操控目标，不是宣称FaceArmor不用任何模型内部信息。
  - information_progression: 先承认扰动机制→指出信息与对象选择前提→后文从surrogates取得特征。
  - privacy_and_task_value: 跨未知目标的保护有价值，同时不能把用代理知识写成完全知识自由。
  - relative_length: 一短判断加一例句把white-box术语落地；压一句时仍保已知目标和典型性。
- local_replacement:
  - unit: P2.S4
  - unit_start: 0
  - unit_end: 67
  - intro_start: 1277
  - intro_end: 1344
  - source_span_sha256: 4252b578906e09a37cfb06e7b948ed8ceee1259a904a250e18d9901e537c7f6b
  - replacement: These defenses typically target specific internal components of a known model
  - semantic_scope_and_cost: 局部代词显化，无新增全称或完全不能迁移的断言；例子和白盒条件保持。
  - selection_condition: 片段需独立可读或前文有多个复数对象时。
  - applied_sentence_sha256: fcc0c06473994f64580572cdfcf062b185eaf03c8f151c4fe8e6ec5c1b21098b

## FA03

- units:
  - P2.S5
- refinement_reason: 旧稿有路径不匹配根因；补overfitted限定的主语与Since原因、when触发关系，避免从强句推出一般定理。
- source_observation:
  - matrix: a defense overfitted to a single specific module naturally fails为矩阵。
  - dependency: Since解释不同场景使用不同内部路径；overfitted限定被断言失败的防御；when给替代范式条件。
- editorial_inference:
  - foreground: 不是简单说架构很多，而是保护依赖的对象可能被另一操控路径绕开。
  - information_progression: 前句具体组件→本句组件依赖如何限制覆盖→表1示意跨场景结果。
  - privacy_and_task_value: 把任务广度要求接到方法选择，让换表示有理由。
  - relative_length: 一长因果句值得保留；不能只剩“迁移很难”，也不能删overfitted把所有单组件工作判死。
- local_replacement:
  - unit: P2.S5
  - unit_start: 178
  - unit_end: 224
  - intro_start: 1606
  - intro_end: 1652
  - source_span_sha256: ec5aa068e11d320eca5bbed9ef0b2c59db287eda83589076f7d0df90aa74290c
  - replacement: under an alternative manipulation paradigm
  - semantic_scope_and_cost: 局部将场景触发压为条件介词，保失败强度；manipulation按本文四范式统一术语，不添加新威胁模型。
  - selection_condition: 论文语境是人脸操控防护，attack易与制作保护扰动的对抗优化混淆时。
  - applied_sentence_sha256: c0d0b3b63915b945d9a369ec3ec3318eb8c6d0457934e657f36b7b771169fed9

## FA04

- units:
  - P3.S2
  - P3.S5
- refinement_reason: 旧稿已有共同性洞察；补investigate研究动作与冒号后实际内容的不同信息重量。
- source_observation:
  - matrix: S2 we investigate commonality；S5 diffusion-based models share foundation。
  - dependency: Moving away是研究路线转向；regardless让步网络差异；冒号后they extract and align为解释性完整主句，both联结构/概念两对象。
- editorial_inference:
  - foreground: 主句share尚抽象，冒号后共同依赖才足以支持下一选择；共同性不是架构完全相同。
  - information_progression: 旧组件路线失配→调查共同依赖→结构与语义成为表示选择依据。
  - privacy_and_task_value: 研究价值来自选择跨操控需用的信息，不是列更多现成编码器。
  - relative_length: 冒号较适合一个总述跟一个解释；不必把两层预先拆成两条无由来的挑战。
- local_replacement:
  - unit: P3.S5
  - unit_start: 78
  - unit_end: 204
  - intro_start: 2430
  - intro_end: 2556
  - source_span_sha256: 2aaece3470dcada27657b05eaeafc4ce4159be37737a35a880c678c7c840707c
  - replacement: share a dependence on physical layout details and high-level conceptual semantics, which they extract and align
  - semantic_scope_and_cost: 局部将冒号后的内容提到dependence宾语，移后动作到关系从句；保两对象与共享依赖，但把foundation比喻具体化。
  - selection_condition: 希望最先让读者看见共同依赖是什么，而非先读抽象foundation时。
  - applied_sentence_sha256: 8d53db77295f3f6039a6f95b7f3736c3957d56d79f20064392a94b13f7498e27

## FA05

- units:
  - P3.S6
- refinement_reason: 旧稿已有architecture-invariant资格；补两个有限谓语和具体表示选择可怎样成文，不把未知目标等同无代理。
- source_observation:
  - matrix: FaceArmor bypasses...and instead maps...为两个协调主干。
  - dependency: To exploit this vulnerability回指共同依赖这个可干预点；into短语给新表示产物。
- editorial_inference:
  - foreground: 真实前景在instead后的选择对象；bypasses不应单独摘成无需任何神经模型。
  - information_progression: 上一句共同依赖→本句选择表示空间→P4解释两个层，§4.1给代理实现。
  - privacy_and_task_value: 缩小对目标生成器内部组件的绑定，使跨目标测试有清楚采用条件。
  - relative_length: 一句公告选择，下一段再展开；在本句列四编码器会让洞察被库存压住。
- local_replacement:
  - unit: P3.S6
  - unit_start: 121
  - unit_end: 186
  - intro_start: 2715
  - intro_end: 2780
  - source_span_sha256: 6464d7bdfceed05e5fe6dc767ca09bafad194e908c4c9df854455b2a25ef6ddd
  - replacement: an image-representation space organized around structural and semantic features
  - semantic_scope_and_cost: 局部删掉architecture-invariant的强性质断言，改为可操作组织内容；这是范围更谨慎的编辑替代，不是源句等义版本。源强主张仍在观察层保留。
  - selection_condition: 用于自身证据仅支持跨所测目标迁移、未证明表示严格架构不变的新稿；重述源作者力度时不自动采用。
  - applied_sentence_sha256: 45dcfc4f60d2c3413baaa14f87bc09c464886116eab71ae4e4588da0462fbd89

## FA06

- units:
  - P4.S1
  - P5.S1
- refinement_reason: 旧稿知道第一设计带来第二问题；补decoupled tiers与后文gradient conflicts看似冲突的层级差。
- source_observation:
  - matrix: P4 feature space is designed to disrupt；P5 comprehensively optimizing...induces conflicts。
  - dependency: two decoupled tiers在表示组织层；P5 across these tiers回指联合优化，不等于此前已证明梯度独立。
- editorial_inference:
  - foreground: 对象可按功能分组，不代表它们在同一像素扰动上的更新方向互不干扰。
  - information_progression: 概念分层→联合操作→空间冲突，三个层级顺次清楚才能避免自相矛盾读感。
  - privacy_and_task_value: 额外空间优化不是无关补丁，而是保护覆盖扩大所产生的真实代价。
  - relative_length: 只需短语澄清，不必添一段术语防御；保P5在双层之后的顺序。
- local_replacement:
  - unit: P4.S1
  - unit_start: 86
  - unit_end: 105
  - intro_start: 2868
  - intro_end: 2887
  - source_span_sha256: 4f8fc82eeecf14cbef9ef2f6f22463e206646b7a757a16a8db67d59807975452
  - replacement: two distinct representation tiers
  - semantic_scope_and_cost: 局部用distinct删除可能的优化独立性暗示；保层数与表示功能，但不逐字保留源decoupled强描述，明示为术语精度选择。
  - selection_condition: 当前定义只是分出结构/语义功能而非已证明梯度解耦时。
  - applied_sentence_sha256: 7f4d13c70dcb27505c338dfbef21cdc495278a1808664a8c7ef4c2b1d72a0092

## FA07

- units:
  - P4.S2
  - P4.S3
- refinement_reason: 旧稿已有结构层功能；补By是方式而非目的，并明确所破坏的是后续生成图。
- source_observation:
  - matrix: S2 The first is structural tier；S3 FaceArmor degrades fidelity and induces collapse并列。
  - dependency: which解释模型重建需求；By targeting为方式框架，不是to式目的；within限定此层对象。
- editorial_inference:
  - foreground: 保护成功在不当操控输出失真，而不是用户准备分享的照片本身变坏。
  - information_progression: 模型需要重建→干预结构表示→操控结果受损；后文输入图伪影将是相反价值。
  - privacy_and_task_value: 同为visual artifacts，作用对象不同决定是保护收益还是可用性损失。
  - relative_length: 在句尾点明output比另起长免责声明更简洁，也保护后文两类图像不串。
- local_replacement:
  - unit: P4.S3
  - unit_start: 144
  - unit_end: 176
  - intro_start: 3179
  - intro_end: 3211
  - source_span_sha256: d9797c5d002c45291222323dea82e616d39c28fd944e6ea0766e6ce0258d67d9
  - replacement: induces severe textural collapse in the manipulated output
  - semantic_scope_and_cost: 局部显化输出对象，保源severe和结果强度；由§4.1文字支持，不增加对所有未知模型的证明。
  - selection_condition: 段落还要讨论保护照片质量，容易将两种视觉效果混读时。
  - applied_sentence_sha256: 60bc96b1af5619614cf269f0c0972a40e3e87a0628ce43aad09a56fc043fcc25

## FA08

- units:
  - P4.S4
  - P4.S5
- refinement_reason: 旧稿已列语义/身份；补while simultaneous并非whereas对照，以及双目标共同服务操控防护。
- source_observation:
  - matrix: S5 we decouple cross-modal bindings为矩阵；S4 The second is semantic tier。
  - dependency: while simultaneously obscuring是同时动作附属；to neutralize给目的，两个操控用途并列。
- editorial_inference:
  - foreground: 语义条件与身份条件是互补干预对象，不是同一个相似度指标两个名字。
  - information_progression: 层定义→图文联系/人脸身份两动作→文中CLIP与FR有不同评价职责。
  - privacy_and_task_value: 身份一致假图的隐私危害不能只用生成质量衡量；概念错位也不等于身份证据完全消失。
  - relative_length: 原句一主一附属可读；若需同等强调两目标，改成协调主句但保同时性与目的。
- local_replacement:
  - unit: P4.S5
  - unit_start: 54
  - unit_end: 111
  - intro_start: 3382
  - intro_end: 3439
  - source_span_sha256: 125073c29c3cba065e2613e0479e32288bb02daed4ad69d9c17d844e8b1e5921
  - replacement: and simultaneously obscure local biometric identities
  - semantic_scope_and_cost: 局部把非有限附属动作升为与decouple并列的有限谓语，we共享；保动作与目的，改变语法平衡而不是增加新能力。
  - selection_condition: 身份保护与文本语义一样需要前景化时。
  - applied_sentence_sha256: c30815637b583dcb3d11df9f79675d8be983efab6f52f959d3eca257bf4bbf66

## FA09

- units:
  - P5.S1
  - P5.S2
- refinement_reason: 已知次生难题不是新发现；补gerund主语把责任直接归于刚提出的联合设计，而非外界额外要求。
- source_observation:
  - matrix: comprehensively optimizing perturbations...是主语，induces conflicts为因果谓语。
  - dependency: across these diverse tiers回指P4；S2 derived from...限定梯度来源，different regions给具体根因。
- editorial_inference:
  - foreground: 第一设计覆盖更全同时使更新方向竞争，这是方法必须承担的技术责任。
  - information_progression: However从收益转代价→Specifically解根因→For instance给区域分工→下一段回应。
  - privacy_and_task_value: 需要同时保可分享的原图与防护效力，不能把多目标数量本身当新意。
  - relative_length: 保四句逐层具体化有理由；若目标只有一层，不应为了模板另造这种第二难题。
- local_replacement:
  - unit: P5.S1
  - unit_start: 9
  - unit_end: 88
  - intro_start: 3689
  - intro_end: 3768
  - source_span_sha256: b5a474a8b9b7fc11d1a7bd8c4d145449534cd5877bf09bac755f6fc8c4efbeed
  - replacement: jointly optimizing adversarial perturbations across these representation tiers
  - semantic_scope_and_cost: 局部突出联合优化，少了comprehensively的覆盖强调；前文已讲覆盖时可省，仍保设计导致冲突的强因果主张。
  - selection_condition: 想让读者立刻看清是joint optimization带来的成本，而非“更全面”口号时。
  - applied_sentence_sha256: 1ad1152a009cb904b5e807787003202edd0c2779d7eaae49480c1d00159d469f

## FA10

- units:
  - P5.S3
- refinement_reason: 旧稿已记whereas范围差；补strictly与predominantly不对称，不能用同一“倾向”抹平。
- source_observation:
  - matrix: identity-concealing perturbations are strictly localized；whereas后texture gradients predominantly affect。
  - dependency: 两侧来源分词originating/derived分别挂语义层/结构层；whereas表示分工对照，不是时间同时条件。
- editorial_inference:
  - foreground: 源对身份区域给更强限定，对纹理给主要分布，局部换词需保这个差别。
  - information_progression: 抽象different regions→可见脸部/背景衣着对照→冲突与软权重有可理解对象。
  - privacy_and_task_value: 隐私表征和图片其他内容占用不同区域，有助读者理解为什么不能一概拉低全部图像质量。
  - relative_length: 一个平行句足够，强度不要求形式完全对称；不要为平行美观统一所有限定词。
- local_replacement:
  - unit: P5.S3
  - unit_start: 87
  - unit_end: 128
  - intro_start: 4013
  - intro_end: 4054
  - source_span_sha256: 86287c1d6f6e195a2a4cdb6b5d2bdb3e55e94561f13fd3a6d36636bbf2efd2c0
  - replacement: are confined to the facial area
  - semantic_scope_and_cost: 局部confined保区域排他强度，不改成mainly；后半predominantly保持，仍是源作者描述而非本轮独立测得梯度支持域。
  - selection_condition: 需避免localized术语但保原地域范围时。
  - applied_sentence_sha256: 999aac1522c12b9d3dc8de117cc15bf248aa4aec79d282c6718976960abf5a8c

## FA11

- units:
  - P5.S4
- refinement_reason: 旧稿两代价并列正确；补which先行对象和保护图伪影的负价值，与P4输出失真区分。
- source_observation:
  - matrix: Naively aggregating...leads to interference为矩阵。
  - dependency: which自然回指interference；not only...but also协调防护下降和视觉伪影。
- editorial_inference:
  - foreground: 这里的视觉变坏是用户要分享的protected image的成本，不能与生成图被破坏的收益混写。
  - information_progression: 不同区域目标→简单叠加干扰→保护效果与可分享性都受损→空间优化同时回应两个职责。
  - privacy_and_task_value: 隐私保护不是单一FID；防护有用还需原照片不因处理而明显损坏。
  - relative_length: 在原句补对象即可，不必把隐私与效用拆两个看似独立挑战。
- local_replacement:
  - unit: P5.S4
  - unit_start: 138
  - unit_end: 179
  - intro_start: 4318
  - intro_end: 4359
  - source_span_sha256: 4186b08750d428bc72bdbe2bb16300f0b2fb330b396920fa0f586645d82462bb
  - replacement: but also produces abrupt visual artifacts in the protected photograph
  - semantic_scope_and_cost: 局部保双重结果强度，增加§4.2明确的保护图对象；不会把后续操控输出质量误作分享效用。
  - selection_condition: 引言同时用collapse/artifacts描述保护收益和优化损失时。
  - applied_sentence_sha256: 29e02d5764614d21d9298984a0fe654fa92893540a6941269f666903da925c3a

## FA12

- units:
  - P6.S2
  - P6.S3
- refinement_reason: 旧稿已记热图可得性；补内部代理信号与未知目标的指称，且serve-as不是凭空观测区域。
- source_observation:
  - matrix: FaceArmor extracts heatmaps；these heatmaps serve as adaptive soft weights。
  - dependency: from surrogate models给信息来源，during forward pass是源所述时机；to smoothly decouple为用途。
- editorial_inference:
  - foreground: 热图不是未来未知目标提供的神谕，也不是无模型知识的几何划分。
  - information_progression: P5不同区域冲突→获取代理内部信号→转换为控制更新的权重。
  - privacy_and_task_value: 交代所需访问成本能使跨目标能力可信；不能把“无额外外部先验”扩大成完全无白盒代理。
  - relative_length: 两短句分别交取得和用途，已经比一长串模型名清楚。
- local_replacement:
  - unit: P6.S2
  - unit_start: 48
  - unit_end: 97
  - intro_start: 4502
  - intro_end: 4551
  - source_span_sha256: 41bf2ecbb9604789c0fd67088a141a385be5d40504f12d966c1a5ce22fcf20e6
  - replacement: from its surrogate models during their forward passes
  - semantic_scope_and_cost: 局部显化归属和复数模型时机，保源内容；不宣称所有图的计算过程只有前向运算或无需梯度，未审其实现。
  - selection_condition: 需要避免the models被误回指为未来目标生成器时。
  - applied_sentence_sha256: be2662f7286e7df081c9bb60a1643d5225f4f8ff0c23896b5e0316bdf9150076

## FA13

- units:
  - P6.S4
  - P9.S2
- refinement_reason: 旧稿PCGrad非原创已对；补空间软分配与残余冲突投影是不同职责，不同于一次给方法两名称。
- source_observation:
  - matrix: P6 our framework establishes gradient projection；P9 approach leverages heatmaps and integrates projection。
  - dependency: By integrating为方式；PCGrad有[46]引用；§4.2明确软权重后交叠边界仍有冲突，再引投影。
- editorial_inference:
  - foreground: 新策略的前景是区域信号与已有投影的组合如何解决联合设计代价，不能把PCGrad算法全归本文。
  - information_progression: 先空间分配→剩余冲突→投影；不把二者列成无因果的并列组件。
  - privacy_and_task_value: 减少互相抵销并避免突变，为防护和图像效用共同服务；其支持由消融而非名字证明。
  - relative_length: 主引言一句足够给组合，正文才讲残余冲突；可加一个短因果从句，毋需展开公式。
- local_replacement:
  - unit: P6.S4
  - unit_start: 0
  - unit_end: 55
  - intro_start: 4654
  - intro_end: 4709
  - source_span_sha256: e8166192a7df261fcf251aa3945c6a4ad65e0af467321f48ccc6a89a6fd6fbe7
  - replacement: By combining this spatial decoupling with the existing PCGrad method [46]
  - semantic_scope_and_cost: 局部显化已有方法归属，保持组合设计主张；不是说全部策略都早已存在。
  - selection_condition: 读者可能因our framework而把被引投影算法误认为新提出时。
  - applied_sentence_sha256: a47fb798ed0936d318bdeecf657694dac1ce5f07ab9da5b4878ed9a63f0919a1

## FA14

- units:
  - P6.S5
- refinement_reason: 旧稿提示强保证有限性；补保证谓语/结果分词/without的严格作用域，并保持源力度与科学审查分离。
- source_observation:
  - matrix: This optimization guarantees a seamless gradient distribution为矩阵。
  - dependency: preventing和ensuring为结果分词；ensuring内that含across all representation tiers及without mutual interference。
- editorial_inference:
  - foreground: 源不是仅说希望减少冲突，而是宣称强效果；分析不能悄悄把原文改读成may。
  - information_progression: 空间权重+投影→归约其期望/宣称能力→实验段应提供支持。
  - privacy_and_task_value: 用户图的自然性与多目标信号保留是两个检验责任；强保证不等于现有有限评价已经证明所有图像。
  - relative_length: 可留一句总效果，但若证据不足应在新稿选择设计目标式变体，并公开强度差异。
- local_replacement:
  - unit: P6.S5
  - unit_start: 75
  - unit_end: 112
  - intro_start: 4853
  - intro_end: 4890
  - source_span_sha256: bc26ddc4f8305cb630271e055b339050a3bbff6c42671b1535a81868d41ec5fb
  - replacement: preventing unnatural visual artifacts in the protected image
  - semantic_scope_and_cost: 局部只明示视觉对象，不软化guarantees/preventing/ensuring；科学资格在独立边界文件，而非篡改源声称。
  - selection_condition: 忠实解释源效果句并消除两个图像对象混淆时。
  - applied_sentence_sha256: b34c330beda3bc2bbb16ca65ca56ced27c786be10ee2e3c46f2d0a3f4288100a

## FA15

- units:
  - P7.S1
  - P10.S1
- refinement_reason: 旧稿已识别四乘四不能推出全交叉；本轮把已知资格转成可直接用的句子而不冒称新发现。
- source_observation:
  - matrix: P7 we conduct experiments；P10 evaluations demonstrate transferability。
  - dependency: 两个four通过and并列，across不编码每个任务×每个模型都测；§5.1和5.3给真实测试拓扑。
- editorial_inference:
  - foreground: 任务广度与架构迁移是两种证据，需各有范围，而非堆大数字。
  - information_progression: P2场景差异与P3架构差异→两类测试；P10再给变换扰动边界。
  - privacy_and_task_value: 保护者未必知道未来操控工具，跨目标能力应靠对应条件而非数量乘积支持。
  - relative_length: 准确范围可能多一点长度，但不会增加新的实验；可借两个并列动词清晰表达。
- local_replacement:
  - unit: P7.S1
  - unit_start: 0
  - unit_end: 113
  - intro_start: 5007
  - intro_end: 5120
  - source_span_sha256: f6d87f072e48d3f71eff042397e77be7746bb79836566d41d16467bfa38aae0b
  - replacement: We evaluate all four manipulation scenarios on SD v1.5 and SD XL, and test inpainting transfer to the DiT-based SD 3 and Flux models.
  - semantic_scope_and_cost: 整句用§5.1/5.3限定范围，删除extensive自评；非原句字面等义，明确分出完整场景测试与inpainting迁移。
  - selection_condition: 需要读者准确理解四场景/四架构证据布局时。
  - applied_sentence_sha256: 431948a19aa906947b6c49fa18c97d076e0b79778ab5140378729e9770aaf11b

## FA16

- units:
  - P7.S2
- refinement_reason: 旧稿已知指标非每格最好；补stronger与more consistent属于总体比较，all prior methods不是当前全领域普查。
- source_observation:
  - matrix: results validate，that内容给FaceArmor achieves stronger/more consistent protection。
  - dependency: than all prior methods为比较集合，establishing给跨目标及现实价值推论。
- editorial_inference:
  - foreground: 读者应该带走跨条件稳定保护的比较答案，不能自动解成每指标、每图片或当前所有既有方法全部严格支配。
  - information_progression: 设计声称→总体评价→第三贡献补两类边界；§5.2称best or second-best nearly all。
  - privacy_and_task_value: 保护适用性取决于多种被复用方式，孤立最优FID不是任务总体胜利。
  - relative_length: 保持两形容词比列五指标紧凑；资格需改变比较含义时给定评估集合即可。
- local_replacement:
  - unit: P7.S2
  - unit_start: 85
  - unit_end: 107
  - intro_start: 5206
  - intro_end: 5228
  - source_span_sha256: 37cc57d3afa3cc029471fec64dfbd62138428969aeac8b6efaebc28631785c74
  - replacement: than the evaluated baselines
  - semantic_scope_and_cost: 局部收紧比较集合至实际实验，不更改stronger/more consistent；这是证据范围校准，不声称原文已使用此限定。
  - selection_condition: 写新稿仅有指定基线比较，不能为所有文献作普遍最优声明时。
  - applied_sentence_sha256: 6991a737ac4c26c04d2f3188938470f20d856df0ac080d51c7ba4d1c44442f66

## FA17

- units:
  - P8.S1
  - P8.S2
  - P9.S1
- refinement_reason: 旧稿贡献分工已成立；补命名矩阵之外的总体对象变化，与次生技术贡献的依赖。
- source_observation:
  - matrix: P8 we propose框架；下一句method neutralizes；P9 we introduce strategy。
  - dependency: P8 By shifting...composed of给表示选择；P9 to resolve给目的，caused by将冲突归于多目标优化。
- editorial_inference:
  - foreground: 总体增量是保护对象从内部组件到多维表示；空间策略值得独立是因为它解决该选择引发的障碍，不是凑第二条。
  - information_progression: P3–4共同表示→P5冲突→P6策略；贡献两项压缩回收同一依赖链。
  - privacy_and_task_value: 工具名称不是贡献解释；成功单位也不是“用了四个编码器”。
  - relative_length: 每项2句实际职责不同：产物+变化、策略+组合。源等长只是本篇选择，不能迁移为配额。
- local_replacement:
  - unit: P9.S1
  - unit_start: 61
  - unit_end: 154
  - intro_start: 5705
  - intro_end: 5798
  - source_span_sha256: bcf14530e3aca2547460dda1f114268a47ca1816f803c44ad2de905361e6e006
  - replacement: to resolve the gradient conflicts introduced by multi-objective adversarial optimization
  - semantic_scope_and_cost: 局部去inherent评价并将caused改introduced，保设计引发与解决目的；不把目的从句误当已经无条件解决的证据。
  - selection_condition: 希望强调难题来自刚提出的联合设计，而非先天地属于所有保护任务时。
  - applied_sentence_sha256: d911938cc878e94905f0493a892adbe1beca79222539111b97e19756c8da84ae

## FA18

- units:
  - P10.S2
- refinement_reason: 旧稿两边界测试已知；补during条件与against对象不同、两个协调谓语不对应同一试验。
- source_observation:
  - matrix: framework maintains...and exhibits...为两有限谓语。
  - dependency: during限定未知DiT迁移场景；against common transformations给另一种环境压力。
- editorial_inference:
  - foreground: 目标生成器变化与输入图像处理变化是两个部署不确定性，不能统一叫更多泛化而丢范围。
  - information_progression: P7总体效果→贡献末句补未知架构/常见处理边界；主张需对应§5.3和5.4不同证据。
  - privacy_and_task_value: 照片分享后可能遇到不同工具与压缩/缩放，两个条件共同接回分享情境，但不保证任意后处理。
  - relative_length: 一并列句能压两类边界；若要精确任务迁移范围，必须加inpainting而不是删除一条。
- local_replacement:
  - unit: P10.S2
  - unit_start: 42
  - unit_end: 111
  - intro_start: 6175
  - intro_end: 6244
  - source_span_sha256: e16e926286c174eb5ca516847a44f73e89e6edaa6e1a13747bf84a6117f59e6c
  - replacement: during zero-knowledge inpainting transfer to the evaluated diffusion transformer models
  - semantic_scope_and_cost: 局部补已评估场景及集合，保源robust protection；范围收束由§5.3支持，不声称四任务都在DiT验证。
  - selection_condition: 要把贡献末句作为独立可引用结果而不能依赖正文补范围时。
  - applied_sentence_sha256: a0fcbab71865b96484b7ce4498fcddc9ffdb2f68829a7d60d94506d1a559cb10


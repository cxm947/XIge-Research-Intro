# JailNeurons：四组完整上下文选项

以下均为编辑撰写；源文位置用于核对命题，不表示这些英文句子来自论文。

- status: editorial options; not tested writing gains

## JN-V01

- target: P3.S6
- fixed_proposition: 识别若成功仍不能直接回答如何做检测及能否跨攻击分布泛化。
- context_before: P3.S5刚承认表示层信号已有先验工作，但少量神经元定位未完成。
- context_after: P4依次介绍调查、定位、跨层特征使用与轻量分类器。
- source_support:
  - E02
  - E03
- options:
  - 
    - text: Even if the relevant neurons can be identified, two questions remain: how to use them for detection and whether the resulting detector transfers to new attack distributions.
    - use_when: 希望先交出问题数量，再让读者读两项具体未知量。
    - syntax_focus: 短矩阵主干后以冒号展开；条件前置。
    - semantic_cost: 将原文they的潜在指代解释为resulting detector，符合检测目标，但不是保留原文代词歧义的逐字改写。
  - 
    - text: Finding the relevant neurons would leave both their use in detection and the detector’s performance on new attack distributions to be established.
    - use_when: 前文已经明说识别尚未完成，需要一句压缩承接。
    - syntax_focus: 动名词主语把识别当已知议题；would保留假设性；并列名词组收纳两问题。
    - semantic_cost: 把how与whether的问句形式改成待确立的能力/表现，失去原句显式的研究问句节奏，但不自动断言泛化已成立。
  - 
    - text: Identifying these neurons would address only the localization problem. Their role in a detector, and that detector’s ability to handle new attack distributions, would still need to be established.
    - use_when: 读者很可能把定位结果当作检测任务已经完成。
    - syntax_focus: 两句先设证据边界，再把两项未解决内容作并列主语。
    - semantic_cost: “only the localization problem”是编辑解释，强调层级边界较原文更强；长度增加，宜作为解释性改写而非源句等义替换。
- not_claimed: 无写作效果实验；三项是有明确使用条件的编辑备选，不是源文。

## JN-V02

- target: P4.S2–S5 sentence group
- fixed_proposition: 先证实表示可分，再定位相关单元，结合不同深度的特征训练轻量检测器；多层覆盖的理由在B1与正文已有支持。
- context_before: P3要求区分是否能定位与是否可用/OOD两种问题。
- context_after: P5承担实验答案，B1仍会再概括结构性发现。
- source_support:
  - E03
  - E04
  - E07
- options:
  - 
    - text: Our initial study establishes separability between the activations elicited by benign and jailbreak inputs. We then identify a compact set of relevant neurons and fit a lightweight detector using features drawn from several depths.
    - use_when: 需要自然的顺序概述，且前后文已有具体定位/选层方法名。
    - syntax_focus: 第一句报告观察；第二句以then连接方法行动，features尾部交出输入。
    - semantic_cost: 省去两个命名策略，也未显式说明多深度为何必要；不能独立替换需要保留方法辨识度的完整方案段。
  - 
    - text: We first establish that the two input classes can be separated in the model’s activations. Guided by this observation, we localize the relevant neurons and combine their features across depths, where different attack types leave different signals, before training a lightweight detector.
    - use_when: 读者缺的正是为何跨层，愿把B1后置的理由提前。
    - syntax_focus: 观察独立成句；第二句嵌入where解释不同深度的互补信息，再交最终训练产物。
    - semantic_cost: 多层理由由贡献/正文前移，需删减或调整B1重复；where是说明性编辑组织，不是对源文局部句法的转录。
  - 
    - text: The preliminary classifier distinguishes the known input distributions but does not transfer reliably across all test distributions. We therefore extract a compact set of relevant features from several depths and use them to train the detector.
    - use_when: 前文已解释两类输入与定位概念，当前段要突出为什么不能直接使用初步分类器。
    - syntax_focus: 第一句用but并置正负观察；第二句以therefore建立问题到设计的读者连接。
    - semantic_cost: 是基于§4.1–4.2的证据驱动重组；不保留原文调查/定位/选层的所有动作及策略名，也不能把therefore读成已证明唯一合理设计。
- not_claimed: 上述均为写作概述，无算法、攻击构造或模型执行步骤。

## JN-V03

- target: P5.S3–S4 and B3.S2 evidence summary
- fixed_proposition: 在明确配置与测试分布下，高TPR与低FPR联合证明检测效用；不能跨表移用阈值或将一般集合推广到压力集。
- context_before: 方法输入与检测任务已经说明；P5.S1给出实验范围。
- context_after: 若作为P5备选，B3可进一步压缩；若作为独立B3备选，则需补原来由P5承担的必要解释。
- source_support:
  - E05
  - E06
  - E12
  - E13
- options:
  - 
    - text: For the LLaVA detector trained on JailBreakV and MM-Vet, the reported TPRs are 99.7% on JailBreakV and 94.2% on JAMLLM. Its FPRs on MM-Vet, MM-Bench, and Normal are 0%, 0%, and 1.9%, respectively.
    - use_when: 需要让读者直接对照同一训练配置的主要任务答案。
    - syntax_focus: 配置前置，先列危险输入检出，再列良性误拒。
    - semantic_cost: 这是依据Tables1/3/12的编辑综合，非Intro原句转录；不自动宣称各数字来自同一阈值校准试验，数值细节也可能超过已充分铺垫的贡献条目所需。
  - 
    - text: The reported experiments show strong detection on the main benchmarks, including unseen attacks, while keeping false alarms low on the standard benign datasets. False-positive rates rise on the two over-refusal stress tests.
    - use_when: 独立摘要需要同时表达主要收益与广泛良性覆盖的边界。
    - syntax_focus: 证据为主语，主判断与while中的正常任务代价配对；第二句单列改变范围的结果。
    - semantic_cost: 压掉源文的最高等级比较及所有数值，是面向更宽泛摘要目的的有损概括，不能冒充保留了Intro全部主张强度。
  - 
    - text: The Introduction reports a leading combination of jailbreak recall, low false-positive rates, and transfer to unfamiliar inputs. The detailed evaluation distinguishes low false-positive rates on standard benign datasets from substantially higher rates on over-refusal stress tests.
    - use_when: 写源文分析时同时尊重作者的强摘要和正文边界。
    - syntax_focus: 第一句明确归属Intro，第二句把细化责任交给评价章节。
    - semantic_cost: 第三人称来源评述，不适合作为作者自己论文的无缝替换；leading combination概括的是源文整体主张，并非宣称逐单元领先。
- not_claimed: 没有生成新的实验结果，也没有把Tables1的5%约束当成所有分布的实测FPR。

## JN-V04

- target: P5.S5–S6 resource/value sentence group
- fixed_proposition: 方法只需数百训练样本，部署无需修改目标LVLM，且检测处理成本低；白盒条件保留在适当上下文。
- context_before: P5已交检测与泛化效用；§3白盒条件在论文中存在，但Intro未明列。
- context_after: P5.S7以消融回到定位技术有效性。
- source_support:
  - E01
  - E04
  - E05
- options:
  - 
    - text: Training requires only a few hundred examples. At deployment, the detector reads internal features without changing the target LVLM, keeping the detection process lightweight.
    - use_when: 读者容易混淆训练和运行成本，且需要补明内部访问。
    - syntax_focus: 按阶段分句；第二句前置部署条件。
    - semantic_cost: 内部读取来自正文补充，增加了Intro未显说的前提；未保留作者关于实时可用的最终强判断。
  - 
    - text: With only a few hundred examples needed for training, JDJN offers a lightweight detection stage that leaves the target LVLM unchanged at deployment.
    - use_when: 前文已交内部访问与训练/部署区别，希望一句总结采用成本。
    - syntax_focus: 数据需求为前置背景；主句把检测阶段轻量化置于中心。
    - semantic_cost: 压掉实时应用与低开销之间的显式价值关系；阶段限定是基于正文的编辑澄清，不能解释为研究过程中从未干预激活。
  - 
    - text: JDJN combines modest training-data requirements with fast detection, and deployment leaves the target LVLM unchanged. Its latency results concern detection before a complete response is generated.
    - use_when: 讨论表2的成本证据，必须避免读者推断所有正常请求都端到端提速。
    - syntax_focus: 首句并列不同资源轴；次句直接限定测量对象。
    - semantic_cost: 数百样本被改成定性表达，实时应用的价值判断也被删去；适合证据评述，不是完整保义润色。
- not_claimed: 不提供训练、模型修改或攻击执行方法。


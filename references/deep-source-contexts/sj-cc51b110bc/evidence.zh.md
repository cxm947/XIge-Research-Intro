# VideoEraser：科学证据、计时与迁移资格

- purpose: 科学与测量范围独立记录；不是主作者选择论证的替代品
- source_and_retained_interpretation_notes:
  - 
    - id: E01
    - origin: source-original
    - location: Table14
    - issue: 比较列印为AnimateDiff，但行列举额外四模型；正文称其为这些模型实验
    - handling: 保留原标签和矛盾，未静默勘误
  - 
    - id: E02
    - origin: source-original
    - location: §4.8 versus Table14
    - issue: 泛称最高ACCu与表中若干低于比较列的值不符；表亦未给各擦除baseline比较
    - handling: 限制该表推论，保留作者主张身份
  - 
    - id: E03
    - origin: source-original
    - location: C.6.1 versus §3.1/Eq3
    - issue: SPEA计算prompt embedding次数叙述不一致
    - handling: 不从不明实现推出速度承诺
  - 
    - id: E04
    - origin: source-original
    - location: §4.5 continuation physical8
    - issue: 显式内容结果文句指Table2，实际SafeSora结果为Table3
    - handling: 分析按实际表内容引用Table3，不称分析录入错误
  - 
    - id: E05
    - origin: source-original
    - location: C.3 celebrity setup versus §4.4/Table2
    - issue: 附录列六个名人含Bill Clinton，主文和结果表五个
    - handling: 任务结果以所见五列为据；未用于放大或抹消任务覆盖
  - 
    - id: E06
    - origin: retained-analysis-imprecision
    - location: historical-profile研究问题段
    - issue: 约1.4倍句若孤立会漏掉源文另称优化后parity
    - handling: 历史字节不改，新增Q02完整区分展示时间与未表列优化声称
  - 
    - id: E07
    - origin: coordinate-convention
    - location: Registered source-unit convention
    - issue: 32继承语义单元+贡献导语O.S1并非33标点句；标签随主句分组
    - handling: 保此约定，不把坐标差异报为内容遗漏
  - 
    - id: E08
    - origin: retained-analysis-imprecision
    - location: 旧稿结尾对五维结果的解释
    - issue: 可误读为贡献B3自身涵盖五维联合优胜
    - handling: 新增分析明确联合质性是全贡献组+前文的编辑解读，B3只并列基线比较/跨模型
- source_and_retained_interpretation_notes_scope: 源内事实、源内不一致与历史解释资格保留；新候选修复过程、归档计数和私人审阅报告不作为写作资源分发。

## Q01

- kind: metric semantics
- source: §4.1 physical6/5959; C.2–C.3 physical16–18/5969–5971
- finding: ACCe低为目标抑制更好；ACCu高为无关生成保留更好。检测器可输出概率、top-K二元标签或毒性评分，各任务并非统一成功率。
- consequence: 不同任务的ACC/安全分数不能未经定义汇总成统一视频失败比例；质量指标也不能替代这两项
- separate_from_author_choice: 解释为什么需联合证据；不规定贡献必须罗列所有指标

## Q02

- kind: reported timing vs optimization claim
- source: Limitations physical9/5962; C.8.1/Table13 physical21/5974
- finding: 限制段报告处理时间约1.4倍，并另称并行计算噪声估计后可与同样优化的基准指导达到推理时间相同。Table13列初始化/嵌入与逐帧去噪时间，没有单列优化前后或优化基准配对行。
- raw_table:
  - unit: Infer: seconds per frame on one NVIDIA A6000; Init: model initialization plus prompt embedding
  - model_order:
    - AnimateDiff
    - LaVie
    - ModelScope
    - ZeroScope
    - CogVideoX
  - vanilla_infer:
    - 3.58
    - 1.12
    - 1.11
    - 1.11
    - 7.95
  - videoeraser_infer:
    - 5.39
    - 1.51
    - 1.58
    - 1.59
    - 11.85
- ratio_computed_from_displayed_values:
  - 1.5055865921787708
  - 1.3482142857142856
  - 1.4234234234234233
  - 1.4324324324324325
  - 1.490566037735849
- interpretation_status: 将表中更慢行理解为优化前/未展现并行优化的配置符合限制段上下文，但表本身未明确标注unoptimized；不是实测复现。
- consequence: 免训练≠零推理开销。不能把1.4倍称不可避免成本，也不能将文字所称优化后parity写成有配对时间表独立验证。
- separate_from_author_choice: 主分析仍解释不更新模型的部署价值；此处保留成本范围，非强制每个贡献加开销句

## Q03

- kind: transfer scope and printed inconsistency
- source: §4.8 physical8/5961; C.8.2/Table14 physical21/5974; D.4/Figures16–19 physical29–30/5982–5983
- finding: Table14在LaVie、ZeroScope、ModelScope、CogVideoX四个额外模型上列Chain Saw/French Horn两个物体场景的ACCe/ACCu。没有五轴全套量化，也没有表中SAFREE或NP比较行。
- raw_printed_headers: 两个场景下的基线列均印为AnimateDiff，尽管行模型名是其他模型；本记录保留原文冲突，不擅自认定已勘误。
- raw_rows:
  - 
    - model: LaVie
    - chain_saw:
      - baseline:
        - 55.44
        - 63.8
      - videoeraser:
        - 0.03
        - 61.71
    - french_horn:
      - baseline:
        - 64.92
        - 62.64
      - videoeraser:
        - 0.05
        - 61.23
  - 
    - model: ZeroScope
    - chain_saw:
      - baseline:
        - 54.57
        - 44.25
      - videoeraser:
        - 0.03
        - 44.64
    - french_horn:
      - baseline:
        - 40.43
        - 47.58
      - videoeraser:
        - 0.06
        - 45.9
  - 
    - model: ModelScope
    - chain_saw:
      - baseline:
        - 54.61
        - 52.39
      - videoeraser:
        - 5.51
        - 52.56
    - french_horn:
      - baseline:
        - 53.71
        - 53.72
      - videoeraser:
        - 3.62
        - 52.83
  - 
    - model: CogVideoX
    - chain_saw:
      - baseline:
        - 63.96
        - 65.39
      - videoeraser:
        - 0.12
        - 66.37
    - french_horn:
      - baseline:
        - 69.51
        - 64.78
      - videoeraser:
        - 0.45
        - 64.22
- row_order: 每对值为ACCe、ACCu，单位百分比；baseline保印刷比较列而不静默改名
- additional_evidence: D.4给四模型的物体、名人、艺术风格与显式概念示例帧；读取了说明/图注文字，未据此断言定量五维复验。
- consequence: 支持所测模型的接入与擦除适用性，不能等同所有模型所有任务所有评价轴均优；部分ACCu较比较列低，§4.8最高ACCu泛称不能由本表逐格推出
- separate_from_author_choice: 跨模型作为单独收束维度有真实作用，范围限制不抹掉该贡献

## Q04

- kind: aggregate result not independently reconstructed
- source: Abstract physical1/5954; Table2 physical7/5960; Table3 physical8/5961
- finding: 摘要报告四任务相对基线平均抑制46%；所读文本未给足唯一复算该46%的聚合公式、基线组合与分母。
- consequence: 保留作者报告身份；不自造分母，不改成46个百分点，不称五维平均分；未复算不等于证伪
- separate_from_author_choice: 不选46%的原因只能作为编辑解释，作者没有自述其删留心理

## Q05

- kind: preservation is relative, not lossless
- source: Table2 physical7/5960; Table11–12 physical21/5974
- finding: 对象任务ACCu：原AnimateDiff71.83、SAFREE44.55、NP58.99、VideoEraser60.10。Table11在garbage-truck场景α从0.01减为0.001，ACCe3.86→3.45而ACCu58.73→18.32。
- consequence: selective设计不等于无关能力完全不变；更低目标检测并非充分任务答案
- separate_from_author_choice: 选择性价值仍是主写作判断；数值用作取舍实例，不作为所有任务通用规律

## Q06

- kind: fidelity vs temporal evidence
- source: §3.2 physical6/5959; §4.7 physical8/5961; Table12 physical21/5974; D.1 Figure6 description physical22/5975
- finding: 方法解释step/frame一致性；主要质量表报告Dover美学/技术分及Inception Score，时序改善另有可视化说明。
- consequence: ACCu不证明时序平滑；质量表不直接等于单独时序一致性量化指标。对象任务质量两分低于原生成器而高于另两擦除基线。
- separate_from_author_choice: fidelity独立于efficacy/integrity的内容选择成立，但不能把它概括成每项原始质量分全面提高

## Q07

- kind: robustness condition
- source: §4.6 physical8/5961; C.4/C.7.2 physical19–21/5972–5974; Ethics physical9/5962
- finding: 攻击评价主要为NSFW，其他概念有较有限的car量化和风格/物体示例；源文承认更复杂绕过仍可能。
- consequence: 不得把ensure、reliable等源措辞改记为所有攻击下不可绕过的定理。此记录没有生成或实现攻击。
- separate_from_author_choice: 鲁棒性的论述职责是重问困难输入下任务是否成立，不要求把完整攻击清单放进引言

## Q08

- kind: prior capability and source internal method conflict
- source: §3.1 physical4–5/5957–5958; C.6.1 physical20/5973
- finding: C.6.1承认SAFREE与SPEA都识别/抑制trigger tokens；它又称SPEA只算一次prompt embedding，而§3.1及Eq3叙述逐token掩蔽并重新计算嵌入。
- consequence: 选择性不是所有近邻缺失的独占能力；一次计算的效率论证存在源内冲突，未查代码不择一当确定实现。
- separate_from_author_choice: 此处避免把源码冲突扩写成已证明方法无效；主线保留双空间/视频约束的选择理由


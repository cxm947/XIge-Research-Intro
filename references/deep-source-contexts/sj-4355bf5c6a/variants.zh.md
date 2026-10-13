# ADD：五个完整安排选项与三个局部结构目标

- policy: Five complete context-conditioned arrangement alternatives and three exact local structural targets. All Chinese wording is authored; alternatives are not measured quality gains. Existing historical A/B summaries stay retained and are not reclassified as complete original-sentence substitutions.
- local_targets:
  - 
    - id: L1
    - full_case: V2
    - source_unit: P3.S6
    - source_unit_sha256: 166659ed4c0a8d755d45439e2ff3395eb0165608bef6e2465cc73d8e72a24498
    - relative_range:
      - 0
      - 52
    - absolute_range:
      - 3449
      - 3501
    - span_sha256: b182e50a2b566d21944cc8103e1509b61aba791cbab43f1fe08b5059c247b3f6
    - scope: Exact source structure used in complete Chinese contextual recasting, not a literal standalone English patch
    - local_change: 把让步中的可能收益改作但前的协调陈述；余下完整主句也需按V2调整
    - retained_context: Source text outside the span supplies antecedents, comparator and task scope; full variant explicitly declares wider sentence edits
    - limit: Hash identity is only provenance, not a semantic-equivalence test
  - 
    - id: L2
    - full_case: V3
    - source_unit: P4.S4
    - source_unit_sha256: bab45f49dcbd0debdd60fc5dcc8a9b1e7c29566ef7e02b57586fee815513fb58
    - relative_range:
      - 38
      - 131
    - absolute_range:
      - 4683
      - 4776
    - span_sha256: ebc67b3cce96236cffd39b39f8bd437a3f91248c482ff9557e1809067b6112d8
    - scope: Exact source structure used in complete Chinese contextual recasting, not a literal standalone English patch
    - local_change: 把同一内容从句中的likely认识与should动作分为两个句子；保留高分框架
    - retained_context: Source text outside the span supplies antecedents, comparator and task scope; full variant explicitly declares wider sentence edits
    - limit: Hash identity is only provenance, not a semantic-equivalence test
  - 
    - id: L3
    - full_case: V5
    - source_unit: C1.S2
    - source_unit_sha256: 435e1b41b0d1f499cf09990e97540e47d07d901edc0ebccf656185cfda0ddf28
    - relative_range:
      - 154
      - 271
    - absolute_range:
      - 7257
      - 7374
    - span_sha256: ed9494ac13efaeca781a148550585fb61214875ee65d9e9439c408e29a6d9590
    - scope: Exact source structure used in complete Chinese contextual recasting, not a literal standalone English patch
    - local_change: 把附加校准过程及其作用独立成配套设计句；语法对等性提高但科学内容不增加
    - retained_context: Source text outside the span supplies antecedents, comparator and task scope; full variant explicitly declares wider sentence edits
    - limit: Hash identity is only provenance, not a semantic-equivalence test
- scope_changing_counterexamples:
  - 
    - edit: Droppractically/treated/target-representation inP3.S4
    - effect: Makes a practical feature boundary sound universal and immutable
  - 
    - edit: Dropmay/can fromP3.S6
    - effect: Turns potential incompatibility into inevitable signal
  - 
    - edit: Convert likely manipulated to proven malicious
    - effect: Changes evidential force
  - 
    - edit: Replace limited standard impact with no degradation
    - effect: Adds zero-loss guarantee
  - 
    - edit: Drop evaluated/each100/query10 from adaptive result
    - effect: Extends a bounded source result beyond its domain

## V1

- source_units:
  - P1.S8
- scope: Full explanatory sentence with its antecedent made explicit
- context_before: P1.S7已说约束差异使问题空间攻击难以防御
- context_after: P1.S9说这通常造成防御样本生成不完整
- text: 问题空间攻击难以防御，原因在于可行操纵必须保留恶意功能，因而难以显式刻画其对抗空间；特征空间攻击则通常把扰动限制在接近原始样本的范围内。
- use_condition: This回指跨栏或因上下文编辑而不易追踪时，把所解释的困难说出
- cost: 重复前句困难，并把源句内对照升为分号后的显式部分；连续段落原回指更省。
- semantic_intent: 保留功能必要条件→空间难刻画因果、与特征空间的通常近距限制对照；显式主语来自相邻S7，不是新科学断言。

## V2

- source_units:
  - P3.S6
- scope: Full concession/result sentence recast as coordinated contrast
- context_before: P3.S5说攻击者倾向改最能降低恶意置信的可扰特征
- context_after: P3.S7–S8举音频行为与注入组件的可能不一致例子
- text: 这些操纵可能提高规避检测的效果，但也可能使可扰特征与那些受安卓恶意软件的恶意功能约束的不可扰特征在语义上不一致。
- use_condition: 希望读者并看攻击者收益与潜在关系异常，且操纵对象已有明确先行词时
- cost: 规避收益从让步从句升为协调陈述，两个可能后果更对等；源句更直接把异常设为主判断。
- semantic_intent: 保留两个可能性、两特征群及功能限定；不声称所有有效规避都必然不兼容。

## V3

- source_units:
  - P4.S4
- scope: Full score-to-inference-and-action sentence split into two
- context_before: P4.S3为基础模型判良性的样本计算两部分不兼容程度
- context_after: P4.S5说明学习表示和独立校准阈值
- text: 较高的不兼容得分提示，该样本很可能遭到对抗性操纵。基于这一判断，应将该样本标记为恶意。
- use_condition: 需要使概率性判断与采取的分类动作各自获得注意，同时保留同一高分语境时
- cost: 动作句更独立、更像明确决策；不能脱离前句作为所有样本的无条件规则。
- semantic_intent: 保留高分suggests、likely判断和should动作；不添加拒绝类别、固定阈值或确定恶意证明。

## V4

- source_units:
  - P4.S7
- scope: Full deployment-cause/system-relation/benefit-cost sentence in explicit sequential form
- context_before: P4.S6给恢复漏报与限制良性误报两目标
- context_after: P5开始评价证据
- text: ADD仅对良性预测进行后处理，因此补充而非替代原有的ML安卓恶意软件检测方法。由此，ADD提高对抗安卓恶意软件的鲁棒性，同时对标准检测性能仅产生有限影响。
- use_condition: 段落收束时希望读者先确认处理集合，再独立读到鲁棒收益与代价限制
- cost: 增加一次停顿并重复ADD；若前文刚强调部署，源文因果从句更紧凑。
- semantic_intent: 保留only、补充/替代关系、积极鲁棒收益与limited impact；不改成零性能影响。

## V5

- source_units:
  - C1.S2
- scope: Full integrated design contribution given two explicit design clauses
- context_before: C1.S1已经给插件整体能力；P3/P4给机制与校准，P5给实证
- context_after: Introduction ends; Background starts
- text: 在ADD中，我们设计了一种基于不兼容性的检测方法，通过比较可扰特征与不可扰特征来区分对抗恶意软件。我们还设计了配套的校准过程，该过程平衡防御效果与对良性应用的负面影响。
- use_condition: 需要使检测依据与运行点控制两项设计责任分别清晰时
- cost: 新增一个有限设计主句，使校准更对等显著；可能弱化源句的一体化贡献感。
- semantic_intent: 保留两设计及配套关系、比较依据、区分任务与效果/良性代价平衡；不声称两者独立最优。


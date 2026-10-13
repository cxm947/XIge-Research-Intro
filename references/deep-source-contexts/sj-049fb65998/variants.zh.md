# IMMI：四个完整语境变体与三个局部目标

- local_targets:
  - 
    - id: L1
    - full_variant: V1
    - source_unit: P4.S5
    - source_sentence_sha256: 2beb7ed94b11738b9cd804ed5a56c10bc6274bc4211c54742afc47a61c6ec04b
    - relative_range:
      - 61
      - 170
    - absolute_range:
      - 3417
      - 3526
    - span_sha256: 72e0bc78cb43ff80fb388ffe705ed62a6ce07e736bafc1def57ff74d207331f6
    - retained_context: 条件、错误持续的矩阵和正确用法让步保留；内部例子在完整变体后置
    - type: exact source target for full contextual Chinese variant; not a drop-in English replacement
    - limit: Offsets establish correspondence; semantic preservation still needs source/context review
  - 
    - id: L2
    - full_variant: V3
    - source_unit: P6.S2
    - source_sentence_sha256: 70873c15e42d2aa7d18baa1ac8175029530f1194647fdda5fcbaf14316fe4e52
    - relative_range:
      - 35
      - 76
    - absolute_range:
      - 5546
      - 5587
    - span_sha256: f8fbe461d9c38c0c41d101cfeac82b87d7367d8a4799fd61155af983c1d39b13
    - retained_context: 对象方法及推断目的保留；完整V3只调整目的入口，LLM仍修饰增强该方法
    - type: exact source target for full contextual Chinese variant; not a drop-in English replacement
    - limit: Offsets establish correspondence; semantic preservation still needs source/context review
  - 
    - id: L3
    - full_variant: V4
    - source_unit: P7.S6
    - source_sentence_sha256: 2f031fd8256a94b60b379e75817bd7ff04910d91562e6cf35df9d25606dd8c24
    - relative_range:
      - 86
      - 142
    - absolute_range:
      - 7118
      - 7174
    - span_sha256: 1220b930cf129a1a6d42fbef54f886997b842fde30807c09d902625cc2786421
    - retained_context: 43%误报收益矩阵保留；完整V4将这段代价独立为句，不变更百分比指标身份
    - type: exact source target for full contextual Chinese variant; not a drop-in English replacement
    - limit: Offsets establish correspondence; semantic preservation still needs source/context review
- policy: Four complete source-scoped variants with real context/use conditions/costs. Local targets are not complete alternatives by themselves.

## V1

- source_units:
  - P4.S5
- scope: Complete one-sentence unit rendered as two Chinese sentences
- context_before: P4.S3–S4 states internal-correctness assumption and that it does not always hold
- context_after: P4.S6 switches to a distinct correct-reference-availability premise
- full_variant: 当函数对内部存在缺陷时，内存错误仍然存在，即使该函数对的用法表面上正确。这里的内部缺陷可以表现为释放函数未能完整释放对应分配函数取得的内存资源。
- change: Move embedded example after the condition/conclusion/concession; two sentences instead of one
- use_condition: Useful when reader should first see exactly which implication fails; example remains immediately available
- cost: Reader temporarily encounters an abstract internal defect before the concrete deallocation example; paragraph grows visually
- semantic_intent: Preserve internal-defect condition, persistent bug, ostensible correct use and illustrative incomplete deallocation; no new claim all pairs fail

## V2

- source_units:
  - P5.S5
  - P5.S6
- scope: Complete paired conditional example, not independent replacement of either pronoun fragment
- context_before: P5.S2–S4 gives responsibility consensus, author observation and shared-object context
- context_after: P5.S7 names inconsistent intentions; P6 turns the observation into a heuristic
- full_variant: 例如，在错误处理时，如果调用者和被调用者都认为自己应管理同一内存对象，就可能发生双重释放或UAF，进而导致内存损坏。反之，如果双方都不承担这项责任，内存就继续被占用，进而发生泄漏。
- change: Make same-object reference explicit while preserving the source’s paired conditional progression
- use_condition: Useful for teaching the common responsibility relation before method names
- cost: Cannot serve as a complete method description; reset/implicit-release exceptions and inference machinery remain in the body
- semantic_intent: First outcome remains possible; second remains a stated outcome under its condition. Do not generalize either to a necessary/sufficient theorem of all memory bugs

## V3

- source_units:
  - P6.S2
- scope: Complete method sentence with purpose moved first
- context_before: P6.S1 introduces IMMI as a heuristic derived from the responsibility insight
- context_after: P6.S3 names program structure and language evidence; S4 states the resulting inference capability
- full_variant: 为推断内存管理意图，作者提出一种以对象为基础、由LLM增强的方法。
- change: Purpose becomes fronted frame; object-based method stays the proposed object and LLM stays augmentation
- use_condition: Useful when the inference goal needs a reminder before naming the method
- cost: Potentially redundant if the immediately prior sentence already foregrounds the inference goal; less chronological introduction of the artifact
- semantic_intent: Preserve the present method/augmentation claim; not a plan, general autonomous LLM auditor, or empirically proven perfect inference

## V4

- source_units:
  - P7.S6
- scope: Complete metric sentence split into two Chinese sentences
- context_before: P7.S5 gives overall35% false discovery rate; prior sentences give runtime and bug/maintenance status
- context_after: P7.S7 states an open-source plan, then contribution summary follows
- full_variant: 引入LLM有效消除了IMMI所报误报的43%。与此同时，它仅额外带来4%的漏报。
- change: Subordinate cost receives independent sentence status while source evaluative only/effectively force remains
- use_condition: Useful when a reader must compare module benefit and cost rather than skim only the main predicate
- cost: More visual emphasis on the cost and another sentence; no new denominator explanation is smuggled in
- semantic_intent: Preserve reported percentages and their distinct metrics; companion evidence defines the ablation context, not global kernel recall


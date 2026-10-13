# MPInspector：四个完整上下文案例与三个局部目标

- local_targets:
  - 
    - id: L1
    - full_variant: V2
    - source_unit: P9.S3
    - source_sentence_sha256: 1c097e1e1f4162d2f96d5e9b220c2a6e8c6d7f4d6e122b075e5b39ee25868a71
    - sentence_relative_range:
      - 57
      - 116
    - absolute_range:
      - 7620
      - 7679
    - source_span_sha256: 95c3450291b17c12320ac2d4721e42595c47da8f1225001414d7865c23d267bc
    - retained_context: 成本矩阵与4.5小时平均范围保留；此附加指标在完整V2中展开为第二句
    - type: precisely delimited source structure transformed only in the full Chinese variant; not a stand-alone replacement string
    - evidence_limit: Exact range establishes correspondence, not semantic equivalence; interpret the local structure within its complete variant and stated context.
  - 
    - id: L2
    - full_variant: V3
    - source_unit: P9.S4
    - source_sentence_sha256: 0aa91dac417dc32b13aecc27099c78dfcbfb6f572cdf9af39996efb70bcc85fc
    - sentence_relative_range:
      - 95
      - 155
    - absolute_range:
      - 7776
      - 7836
    - source_span_sha256: ac8c86a985102e13a47a8a2a35cfdb125b90212439ca921f6e0a9dbed22c6783
    - retained_context: 工具检查57性质及检测252违例的矩阵保留；此关系在完整V3中变为保留作者主体的第二句
    - type: precisely delimited source structure transformed only in the full Chinese variant; not a stand-alone replacement string
    - evidence_limit: Exact range establishes correspondence, not semantic equivalence; interpret the local structure within its complete variant and stated context.
  - 
    - id: L3
    - full_variant: V4
    - source_unit: P6.S4
    - source_sentence_sha256: d37eef082bc4be3a855e49f4e7059405b689152ba89feba759cc834465abde12
    - sentence_relative_range:
      - 88
      - 180
    - absolute_range:
      - 5539
      - 5631
    - source_span_sha256: 8fbbc116ef927d9da6901c38aa43e5733ddafe8508a7b758231dde0bcafa5f93
    - retained_context: 常见函数可由真实流量模式匹配识别的矩阵保留；对照部分在完整V4中另起一句
    - type: precisely delimited source structure transformed only in the full Chinese variant; not a stand-alone replacement string
    - evidence_limit: Exact range establishes correspondence, not semantic equivalence; interpret the local structure within its complete variant and stated context.
- policy: Four cases, five complete text options; actual local target offsets only for L1–L3. Other ledger alternatives are editorial proposals, not already executed rewrites.

## V1

- source_units:
  - P5.S3
  - P5.S4
  - P5.S5
- scope: Complete three-sentence passage; two full Chinese analytical variants, not isolated local replacements
- context_before: P5.S1 introduces tool and S2 property-driven/model-based testing philosophy
- context_after: P5.S6–S12 define state-machine components and two property sources
- variants:
  - 
    - name: chronological
    - text: 首先，MPInspector将协议实现建模为状态机。随后，它从标准规范收集待验证的安全性质，并依据学到的状态机加以精化。最后，它通过形式验证，在该状态机上检测性质违例。
    - reader_tradeoff: Keeps generation order and explicitly exposes both model uses; helpful when the representation is still new.
  - 
    - name: result-first
    - text: MPInspector最终通过形式验证，在从实现学得的状态机上检测性质违例：为此，它先将实现建模为状态机，再从标准规范收集待验证的安全性质，并依据学到的状态机精化这些性质。
    - reader_tradeoff: Foregrounds the verification objective, then backfills the dependencies; denser for a reader not yet familiar with the model.
- semantic_status: Intended to preserve source propositions and dependencies; changes ordering/packaging, not measurement or automatic scope
- retained_relations:
  - implementation→state machine
  - specification→gathered properties
  - learned model→property refinement
  - formal verification on learned model→violations
- baseline_alternative_review: Old B retains specification/model objects but leaves model-conditioned refinement implicit. It may function as context-dependent summary, not a standalone equally complete substitute.

## V2

- source_units:
  - P9.S3
- scope: Complete one-sentence unit replaced by two Chinese sentences; local adjunct also exactly located
- context_before: P9.S1–S2 establish tested scope and model recovery/verification
- context_after: P9.S4 gives properties/violations/attacks counts
- variants:
  - 
    - name: parallel-indicators
    - text: 端到端分析的平均开销为4.5小时。在识别性质违例方面，MPInspector的精确率为100%。
    - reader_tradeoff: Gives precision independent sentence status rather than packing it into the cost sentence; retains mean/time and precision object.
- semantic_status: Intended preserving source claim strength. This reports paper results, not independently reproduced measurements.
- unchanged_scope:
  - average end-to-end time
  - 100% precision in property-violation identification only
- not_part_of_variant: 45-reviewer methodology/no-recall qualification is separately evidenced, not inserted as if present in this source sentence.

## V3

- source_units:
  - P9.S4
- scope: Complete one-sentence unit replaced by two Chinese sentences; post-comma relation separately located
- context_before: P9.S3 reports time and precision
- context_after: P9.S5–S8 assess consequences, per-platform distribution and root causes
- variants:
  - 
    - name: explicit-actor-separation
    - text: 具体而言，MPInspector检查了57项定制安全性质，并检测到252个性质违例。作者基于这些违例进一步识别出11类攻击。
    - reader_tradeoff: Makes the tool/author actor shift and output dependency explicit, at the cost of a longer visual break.
- semantic_status: Intended preserving quantities, actors and relation. No automatic attack generation or causal proof added.
- meaning_violation_guard: Replacing the second sentence with automatic discovery of11 attacks by the tool would change attribution and automation scope; this is a guard, not a recommended variant.

## V4

- source_units:
  - P6.S4
- scope: Complete one-sentence unit replaced by two Chinese sentences; while span separately located
- context_before: P6.S1–S3 introduce encrypted-parameter difficulty and cryptographic-function identification
- context_after: P6.S5 explains documentation usually provides semantics for customized parameters
- variants:
  - 
    - name: split-contrast
    - text: 有些常见加密函数可通过对真实流量进行模式匹配来识别。相比之下，对于未知的定制加密函数，几乎不可能定义相应的匹配模式。
    - reader_tradeoff: Gives the residual category a separate sentence while preserving contrast; does not yet import the next sentence’s document fallback.
- semantic_status: Intended preserving some/can/almost-impossible asymmetry; body limitations separate from original claim.


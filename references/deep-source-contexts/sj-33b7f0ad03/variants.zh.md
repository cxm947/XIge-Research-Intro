# FreeEagle：四个情境案例与五个完整选项

- local_targets:
  - 
    - id: L1
    - variant: V1
    - source_unit: P11.S1
    - source_sentence_sha256: 5fee275b6890d5d02dc42f9428a154184ad3ea1fb568038c11d0120dc0af5446
    - relative_range:
      - 78
      - 207
    - absolute_range:
      - 6157
      - 6286
    - span_sha256: eea5f1c522a46d94ee66a2aec1cd5fce13b7cdc49f884d94fa9c8d0f6c952c5d
    - retained_context: 广泛实验动作与多数据集/架构范围保留；完整V1比较非限定结果与独立结果句
    - type: Exact source structure participating in full contextual Chinese alternative; not a standalone English patch
    - limit: Hash/range correspondence does not itself certify equivalence
  - 
    - id: L2
    - variant: V2
    - source_unit: P7.S4
    - source_sentence_sha256: 16a0e877a26bca485e4fc872e9bbe7949f4a1812af39568237f4d7a53cced94e
    - relative_range:
      - 106
      - 223
    - absolute_range:
      - 4869
      - 4986
    - span_sha256: 572f1376f8d48815bc5560725ee8ae31930230f438857b34e6ee836137969acb
    - retained_context: 分类器对全模型的成本比较保留；完整V2前景化覆盖与最终检测能力
    - type: Exact source structure participating in full contextual Chinese alternative; not a standalone English patch
    - limit: Hash/range correspondence does not itself certify equivalence
  - 
    - id: L3
    - variant: V4
    - source_unit: P6.S4
    - source_sentence_sha256: f17e321f2d3ddde0a6c6b235edb002fa04132984c91e928b6fe96866d61540ce
    - relative_range:
      - 159
      - 165
    - absolute_range:
      - 4205
      - 4211
    - span_sha256: 244caf629c8215cfd11a0ec5162e557d8a194b55aa84e07c8c7cd1fbba5b0ff2
    - retained_context: 两部件、两类特征、先后顺序及优先性关系保留；完整V4显式融入some的范围
    - type: Exact source structure participating in full contextual Chinese alternative; not a standalone English patch
    - limit: Hash/range correspondence does not itself certify equivalence
- policy: Four cases, five complete texts; one/two sentences are conditional alternatives, not rigid guidance.

## V1

- source_units:
  - P11.S1
- scope: Complete evaluation-contribution sentence; two full Chinese realizations with identical scientific content
- context_before: P6/P7 give mechanism, scope, same-resource DF-TND comparison and some higher-resource comparison; C1/C2 give insight and method
- context_after: Introduction ends, Background begins
- options:
  - 
    - name: one-sentence
    - text: 我们在多种数据集和模型架构上进行了广泛实验，结果表明FreeEagle对复杂神经木马有效，甚至优于部分非无数据木马检测器。
    - use_condition: Prior context has supplied necessary mechanism/results and this is a compact closing contribution
    - cost: Experiment scope and task result share one sentence; not suited to every reader or location merely because compact
  - 
    - name: two-sentence
    - text: 我们在多种数据集和模型架构上进行了广泛实验。实验表明，FreeEagle对复杂神经木马有效，甚至优于部分非无数据木马检测器。
    - use_condition: Scope and task answer benefit from independent attention, while both facts are still needed
    - cost: Extra pause and visible repetition after P7; no evidence the additional sentence inherently improves writing
- semantic_intent: Preserve extensive/diverse scope, effectiveness, even and some comparison. Not data-free-firstness, universal superiority or numeric deployment prediction.

## V2

- source_units:
  - P7.S4
- scope: Complete mechanism→cost→coverage→detection unit, not just old local A/B summary
- context_before: P7.S2/S3 identifies classifier-level/high-level-feature analysis and its trigger-form value
- context_after: P7.S5 introduces dummy representations for data-free input construction
- options:
  - 
    - name: task-first
    - text: FreeEagle能够高效检查每一种可能的源—目标类别对，并检测类别特定后门，因为只检查分类器部分而非整个模型显著降低了时间成本。
    - use_condition: Useful immediately after a reader asks how unknown source classes can be covered
    - cost: Reader meets capability before its mechanism; may be less natural when following the original stepwise explanation
- semantic_intent: Preserve every possible pair, efficient inspection, class-specific detection, significant relative cost reduction and classifier-versus-whole comparison. No fastest-tool claim.

## V3

- source_units:
  - P3.S3
  - P3.S4
- scope: Complete two-sentence role/resource justification, not only the old short no-data reason fragments
- context_before: P3.S1–S2 establishes platform maintainers’ pre-distribution task and difficulty
- context_after: P4 adds the independent complexity challenge
- options:
  - 
    - name: explicit-reason-boundary
    - text: 在这一场景，第一个挑战是维护者应采用无数据木马检测器：上传到模型分享和交易平台的训练模型往往不附干净验证数据。此外，对于某些隐私敏感任务的模型，很难收集替代验证数据，例如用于罕见病诊断的图像分类模型。
    - use_condition: Useful when the reader needs the recommendation and its material-access reason clearly separated before another challenge
    - cost: Longer visual dependency and repeated role/platform phrases; a shorter contextual summary can suffice once those are already known
- semantic_intent: Preserve should, often, some, surrogate difficulty and example. Colon expresses the original causal reason; it does not claim impossible data access for all models.

## V4

- source_units:
  - P6.S4
- scope: Complete priority observation with two explicit subject sentences
- context_before: P6.S3 defines feature extractor and classifier
- context_after: P7 explains why observing the classifier changes detection choices
- options:
  - 
    - name: split-roles-integrated-qualifier
    - text: 对于植入木马的模型，特征提取部分提取良性特征和触发特征。随后，分类器使触发特征优先于某些良性特征。
    - use_condition: Useful when readers might overlook the parenthetical some or confuse the two parts’ jobs
    - cost: An extra sentence and repeated part names; a compact formulation works when decomposition and source-class meaning are already fresh
- semantic_intent: Preserve sequential roles and the limited comparison object. Some does not mean exactly/only one fixed proper subset, and does not exclude the class-agnostic case.


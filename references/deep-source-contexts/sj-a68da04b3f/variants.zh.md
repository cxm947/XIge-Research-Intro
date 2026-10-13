# Graph AUD：一个忠实参照与四个信息安排选项

- policy: Five complete contextual cases comprise one source-faithful whole-sentence reference realization (V1) and four information-arrangement alternatives (V2–V5), plus three exact local targets. Chinese texts are attributed editorial realizations of the designated source, not copied source text or measured writing improvements.
- local_targets:
  - 
    - id: L1
    - full_case: V1
    - source_unit: P2.S3
    - source_unit_sha256: 8e441f3e71a6e42d5bf216f8654d41ccefa1676519f1db0577dce597dffe74fd
    - relative_range:
      - 70
      - 157
    - absolute_range:
      - 1565
      - 1652
    - span_sha256: 4793803a2258f90f7042d729932e279c13179b39ad7e3fa254a9254a770a5afa
    - local_option: 在保留系表主干时，可用“保护用户隐私，并同时尽可能保留数据效用”作为完整补语的中文对应。
    - type: Exact source structural span paired with Chinese contextual realization, not a standalone English drop-in patch
    - retained_context: All text outside the identified span remains source context; the full variant separately states its wider edits and presentation changes
    - limit: Coordinate identity does not itself certify semantic equivalence
  - 
    - id: L2
    - full_case: V3
    - source_unit: C1.S3
    - source_unit_sha256: 0c50f7d5016696c300874e0e6b26a1c648e582009747db12f5403734f8e70e0b
    - relative_range:
      - 53
      - 171
    - absolute_range:
      - 3757
      - 3875
    - span_sha256: 5af10c57ae0b9081bf31041d96abbd46479c8c18b8842991618767c5b0ea42c3
    - local_option: 把量化相关性与给闭式表达作为on下的并列活动理解；中文对应“量化…并给出闭式表达以显式展示…”须随V3完整句使用。
    - type: Exact source structural span paired with Chinese contextual realization, not a standalone English drop-in patch
    - retained_context: All text outside the identified span remains source context; the full variant separately states its wider edits and presentation changes
    - limit: Coordinate identity does not itself certify semantic equivalence
  - 
    - id: L3
    - full_case: V5
    - source_unit: C4.S3
    - source_unit_sha256: f8c0487f33fa9d6862487d141e08718cd6a5250e5d4068e427713968ebabbc75
    - relative_range:
      - 247
      - 335
    - absolute_range:
      - 5572
      - 5660
    - span_sha256: e5111ce6dad68c917b3c5957bf9f7664059b746f337071afd5b068761508aace
    - local_option: 完整结果内容可在配置明确后对应“理论上可被去匿名化的用户中有超过83.4%无法被ODA去匿名化”；不能把它单独当无条件结果。
    - type: Exact source structural span paired with Chinese contextual realization, not a standalone English drop-in patch
    - retained_context: All text outside the identified span remains source context; the full variant separately states its wider edits and presentation changes
    - limit: Coordinate identity does not itself certify semantic equivalence
- scope_changing_non_equivalences:
  - 
    - change: Remove if from the existence→quantification question
    - effect: Converts open dependency into an assumed established relation
  - 
    - change: Replace both models with every possible graph without conditions
    - effect: Broadens theorem scope beyond model assumptions
  - 
    - change: Turn more than83.4% of theoretically de-anonymizable users into83.4% of all users
    - effect: Changes threshold and denominator
  - 
    - change: Call the closed forms tight optimum or a practical optimal attack
    - effect: Adds tightness/computability claims
  - 
    - change: Use only data-owner utility/privacy configuration question as a substitute for all P3.S3
    - effect: Useful goal-directed summary but deletes other information obligations
- counts:
  - total_complete_cases: 5
  - reference_realizations: 1
  - arrangement_alternatives: 4
  - exact_local_targets: 3

## V1

- source_units:
  - P2.S3
- scope: Complete objective sentence, retaining source syntax/order as a faithful reference realization
- context_before: P2.S2 lists existing anonymization families
- context_after: P2.S4 introduces structural attacks and auxiliary graphs
- text: 基本上，这些匿名化技术的主要目标是保护用户隐私，并同时尽可能保留数据效用。
- use_condition: 适合从已有方法枚举转到共同评价目标，两个目标都需保持明确时
- cost: 保留原紧凑系表结构；若只需承接已知双目标则可能重复。改用让步会新增冲突事实，不能视为本选项。
- semantic_intent: 保留primary/basic概括、共同目标、同时与尽可能；不声称目标已经实现。
- case_role: source-faithful whole-sentence reference realization; not counted as an arrangement alternative

## V2

- source_units:
  - P3.S1
- scope: Complete analytical question cluster, not one original orthographic sentence
- context_before: P2承认匿名化、去匿名化与可去匿名性量化三线已有成果
- context_after: P3.S2给受益者，S3–S4给两个实际用途
- text: 尽管已经提出了多种图匿名化、去匿名化以及去匿名化量化技术，这一领域仍有一些重要问题尚未解决。例如，图数据的匿名性、效用与去匿名性之间是否存在相关性？如果存在，应如何量化？当前先进的匿名化和去匿名化技术表现如何，又是否还有改进空间？
- use_condition: 读者需要逐项把研究问题和前文已有答案区分开时，可增加显式停顿
- cost: 主判断与问题序列分开后更长、问题感更突出；原嵌入式列举更紧凑。三问不是必须拆成三段的设计挑战。
- semantic_intent: 保留让步、开放性、条件if及三问；此完整分析单位可由多句表达，不能称同一单句同义改写。
- case_role: context-conditioned information-arrangement alternative

## V3

- source_units:
  - C1.S2
  - C1.S3
- scope: Complete two-sentence quantification/scope/novelty claim
- context_before: C1.S1先引入对应三对象的三个指标
- context_after: C1.S4交攻防研究意义，C2据此扩展平台
- text: 在数学ER模型和一般数据模型下，我们基于这三个指标，对图匿名性、效用与去匿名性之间的相关性进行了全面量化。据我们所知，这是首次量化图数据AUD相关性并给出闭式表达以显式展示这种相关性的工作。
- use_condition: 模型适用范围是当前读者最需要先确认的信息时，可把该范围前置
- cost: 模型信息先于指标回指及量化动作；若读者尚未认识模型，这样前置会增加等待，原指标先行更顺。
- semantic_intent: 保留两个模型、指标基础、全面量化、作者知识限定、首次对象、闭式表达和用途；不是自称已证明紧界或无条件最优性。
- case_role: context-conditioned information-arrangement alternative

## V4

- source_units:
  - C3.S2
- scope: Complete relation-result sentence with matrix/content redistribution
- context_before: C3.S1已给12个多来源真实图的评价范围
- context_after: C4转向现有方法相对理论参照的评价
- text: 如我们的评价结果所示，图数据可达到的匿名性和去匿名性取决于多个因素，例如数据保留的效用以及所用辅助数据的质量。
- use_condition: 评价范围已知，希望读者立即遇到关系性发现而非再次读取结果显示的动作时
- cost: 结果归属退到状语，学术动作不再是矩阵；若正在交代证据链，源文results-demonstrate矩阵同样合理。
- semantic_intent: 保留结果归属、可达限定、多因素和非穷尽示例；不改为因果识别或完整因素清单。
- case_role: context-conditioned information-arrangement alternative

## V5

- source_units:
  - C4.S3
- scope: Complete numerical example across two Chinese sentences
- context_before: C4.S2明确作者发现已有去匿名化技术有显著改进空间
- context_after: Introduction ends; Related Work follows
- text: 以当时最新的无种子去匿名化攻击ODA为例，评价将它用于一个含6.4万用户、82万条边且经当时先进的DP匿名化技术处理的Facebook数据集。在这一评价条件下，结果显示：理论上可被去匿名化的用户中有超过83.4%无法被ODA去匿名化。
- use_condition: 当单句前置配置和图属性较多、读者容易漏掉理论可达分母时，给配置和结果各一个停顿
- cost: 重复评价语境并增加一句；原长句结果收尾同样能突出数值，不能从此例推出所有数值都应拆句。
- semantic_intent: 保留当时latest/state-of-the-art归属、seed-free、ODA、Facebook图规模、DP处理、同一评价条件、严格大于83.4%和理论可去匿名用户分母；不增加原引言未指定的参数。
- case_role: context-conditioned information-arrangement alternative


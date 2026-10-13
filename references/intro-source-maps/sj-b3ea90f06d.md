# TextDefense（Word Importance Entropy版本）：完整引言句级图

- 来源身份：sj-b3ea90f06d
- 指定版本：arXiv:2302.05892v1, 12 February 2023
- 指定原文：https://arxiv.org/pdf/2302.05892v1
- 实际读取原文：https://arxiv.org/pdf/2302.05892v1
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#textdefense) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [B1](#b1) · [B2](#b2) · [B3](#b3)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

sj-b3ea90f06d; arXiv:2302.05892v1, 12 February 2023; https://arxiv.org/pdf/2302.05892v1. Complete Introduction pp.1–2 reread, including all three contribution bullets. Local frozen PDF/text: （源缓存不随包附带）,txt}. Version-specific source claims below are analyzed, not endorsed as current field-wide facts.

Notation: S numbers follow sentence order within P; known → added content; relation in parentheses; ⇒ later use. Each paragraph's claim and handoff precede its sentences.

P1 p.1 — Ground NLP adversarial risk in general DNN success, crossing the continuous/discrete distinction; hands threat to attack taxonomy.
<a id="p1"></a><a id="p1-s1"></a>P1.S1 DNNs → NLP among successful domains (opening scope) ⇒ NLP-specific task
<a id="p1-s2"></a>P1.S2 Success → enables concrete language tasks (application elaboration) ⇒ toxic-comment stakes
<a id="p1-s3"></a>P1.S3 Success → malicious perturbation vulnerability (contrast) ⇒ attack object
<a id="p1-s4"></a>P1.S4 Perturbation → pixel example (familiarization) ⇒ discrete-text contrast
<a id="p1-s5"></a>P1.S5 CV example → discrete text is also vulnerable (concessive transfer) ⇒ P2 categories
<a id="p1-s6"></a>P1.S6 Text attacks → toxic filtering failure enables abusive content (task consequence) ⇒ defense value

P2 p.1 — Classify attack objects and emphasize the hard case before comparing defenses.
<a id="p2"></a><a id="p2-s1"></a>P2.S1 Established vulnerability → active attack-algorithm literature (field state) ⇒ taxonomy
<a id="p2-s2"></a>P2.S2 Algorithms → character/word/sentence categories (organizer) ⇒ S3–S7
<a id="p2-s3"></a>P2.S3 Character category → edit characters (definition) ⇒ S4 defensive condition
<a id="p2-s4"></a>P2.S4 Character changes → spelling checkers often help (boundary/available response) ⇒ word-level difficulty
<a id="p2-s5"></a>P2.S5 Word category → semantic-preserving synonym replacement (definition) ⇒ signal mechanism P4
<a id="p2-s6"></a>P2.S6 Word replacement → hardest to defend in paper's framing (priority claim) ⇒ DISP limitation
<a id="p2-s7"></a>P2.S7 Sentence category → semantic paraphrase treated as word-level case (scope organization) ⇒ attack-type agnosticism
<a id="p2-s8"></a>P2.S8 Advancing algorithms → white/black-box, fewer queries, semantic similarity raise provider risk (trend + consequence) ⇒ broad defense requirement

P3 pp.1–2 — Compare three defense families, preserving their capability before exposing generality/cost limitations.
<a id="p3"></a><a id="p3-s1"></a>P3.S1 Attack growth → detection, training, certification defenses (response/taxonomy) ⇒ alternatives
<a id="p3-s2"></a>P3.S2 Detection family → often attack-specific (limitation) ⇒ S3–S6
<a id="p3-s3"></a>P3.S3 Attack specificity → DISP/FGWS examples (instantiation) ⇒ mechanism
<a id="p3-s4"></a>P3.S4 Named methods → detect and restore perturbations before classification (capability) ⇒ dependence
<a id="p3-s5"></a>P3.S5 Pipeline → limited by detector quality (dependency) ⇒ evidence
<a id="p3-s6"></a>P3.S6 Detector limits → DISP word failures/FGWS word-only scope (contrasting cases) ⇒ generic signal P4
<a id="p3-s7"></a>P3.S7 Detection trend → increasingly complex auxiliary models (new concern) ⇒ S8
<a id="p3-s8"></a>P3.S8 Complexity → need not improve performance (qualification) ⇒ reuse target model
<a id="p3-s9"></a>P3.S9 Training route → some robustness but no guarantee, dependent on attack quality/diversity (capability + condition) ⇒ S10
<a id="p3-s10"></a>P3.S10 Dependence → trained models remain perturbation-sensitive (consequence) ⇒ robustness evaluation
<a id="p3-s11"></a>P3.S11 Certification route → computes exact radius for theoretical assurance (stronger answer) ⇒ S12
<a id="p3-s12"></a>P3.S12 Radius → supports guaranteed training or vulnerability evaluation (utility) ⇒ S13 cost
<a id="p3-s13"></a>P3.S13 Certification utility → heavy computation (trade-off) ⇒ efficient detection
<a id="p3-s14"></a>P3.S14 Alternatives → universal known/unknown defense missing in source's scope (synthesis) ⇒ P4 aim
<a id="p3-s15"></a>P3.S15 Effectiveness → some defenses cost more than target NLP model (second requirement) ⇒ sampling P5

P4 p.2 — Announce system, rethink common attack process, derive target-model signal.
<a id="p4"></a><a id="p4-s1"></a>P4.S1 Generality/cost gap → TextDefense for known/unknown attacks (work announcement) ⇒ contributions
<a id="p4-s2"></a>P4.S2 Generalization gap → reconsider attack generation (research move) ⇒ S3–S8
<a id="p4-s3"></a>P4.S3 Generation process → label influence selects semantic-important words (known mechanism) ⇒ S4
<a id="p4-s4"></a>P4.S4 Importance-based changes → word-importance distributions disrupted (abstraction) ⇒ entropy
<a id="p4-s5"></a>P4.S5 Disruption → rare/nonexistent replacements ignored/misread and lower confidence (concrete explanation) ⇒ score shifts
<a id="p4-s6"></a>P4.S6 Repeated modifications → target confidence falls until label changes (causal progression) ⇒ S7
<a id="p4-s7"></a>P4.S7 Iteration → unmodified scores rise while modified scores fall (observed pattern) ⇒ distribution contrast
<a id="p4-s8"></a>P4.S8 Pattern across attacks → seek distribution difference for detection (inference/design objective) ⇒ P5
<a id="p4-s9"></a>P4.S9 Detector choice → exploit target model rather than train auxiliary attack-pattern model (design fork) ⇒ contribution B1

P5 p.2 — Turn empirical contrast into an efficient decision rule.
<a id="p5"></a><a id="p5-s1"></a>P5.S1 Empirical investigation → clean/adversarial behavior differs on target (observation gate) ⇒ details
<a id="p5-s2"></a>P5.S2 Word scores → clean distribution has lower scale (measured contrast half) ⇒ S3 interpretation
<a id="p5-s3"></a>P5.S3 Low scale → coherent context, single removal less disruptive (interpretation) ⇒ discriminative rationale
<a id="p5-s4"></a>P5.S4 Clean contrast → adversarial distributions higher scale (opposition) ⇒ S5
<a id="p5-s5"></a>P5.S5 High scale → misplaced attention/context misunderstanding (interpretation) ⇒ entropy choice
<a id="p5-s6"></a>P5.S6 Distribution contrast → entropy represents scale (metric design) ⇒ threshold
<a id="p5-s7"></a>P5.S7 Efficiency requirement → sample words for scores (constraint response) ⇒ P3.S15
<a id="p5-s8"></a>P5.S8 Score statistic → tune F1-maximizing threshold with examples (calibration) ⇒ S9 rule
<a id="p5-s9"></a>P5.S9 Entropy + threshold → above-threshold input classified adversarial (decision closure) ⇒ evaluation

P6 p.2 — Results preview before contribution list; breadth then comparison, transfer, robustness, explanatory finding.
<a id="p6"></a><a id="p6-s1"></a>P6.S1 Proposed rule → effective across models/datasets/attack types (scope + headline) ⇒ B2
<a id="p6-s2"></a>P6.S2 Breadth → outperforms three attack-specific detectors (comparison) ⇒ P3 generality gap
<a id="p6-s3"></a>P6.S3 Basic tests → transfer and shifted-data scenarios (scope extension) ⇒ B2 varied settings
<a id="p6-s4"></a>P6.S4 Adaptive attacks → robust and exceeds adversarial training baselines (stronger comparison) ⇒ B3
<a id="p6-s5"></a>P6.S5 Performance variation → target generalizability is important (explanatory finding) ⇒ later analysis rather than a new module

<a id="p7"></a>P7 contribution lead-in (summary organizer).
<a id="b1"></a><a id="b1-s1"></a>B1.S1 Method described → attack-agnostic defense claim (method contribution)
<a id="b1-s2"></a>B1.S2 Method identity → target-model reuse without auxiliary detector/restorer (defining mechanism)
<a id="b2"></a><a id="b2-s1"></a>B2.S1 Previewed breadth → two tasks and named attacks (evaluation scope refinement)
<a id="b2-s2"></a>B2.S2 Scope → better and effective under varied settings (result synthesis)
<a id="b2-s3"></a>B2.S3 Offline evaluation → online APIs show MLaaS security potential (deployment extension)
<a id="b3"></a><a id="b3-s1"></a>B3.S1 Robustness preview → adaptive attacks versus adversarial training (evaluation object)
<a id="b3-s2"></a>B3.S2 Robustness evidence → reduces success/increases required word changes (capability statement)

Observed: detailed mechanism/observation precedes qualitative evaluation, which precedes contributions. Most summary claims are already introduced; B2 adds online APIs. No quantitative results are in the Introduction. P3 has capability–condition–cost comparisons, not simply a list of failures.
Inferred purpose: deriving a cross-attack statistic from the shared generation process explains why the method might generalize beyond a named attack. Separate score-contrast and threshold sentences let readers distinguish evidence for a signal from how an implementation makes decisions. The source's broad empirical language should not be imported as universal theory; retain the actual validation scope.

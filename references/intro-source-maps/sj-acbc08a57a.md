# Cert-RNN：完整引言句级图

- 来源身份：sj-acbc08a57a
- 指定版本：19-page NESA author manuscript identifying CCS 2021
- 指定原文：https://nesa.zju.edu.cn/download/dty_pdf_cert_rnn.pdf
- 实际读取原文：https://nesa.zju.edu.cn/download/dty_pdf_cert_rnn.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#cert-rnn) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [B1](#b1) · [B2](#b2) · [B3](#b3) · [B4](#b4)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

sj-acbc08a57a;19-page NESA author manuscript identifying CCS2021; https://nesa.zju.edu.cn/download/dty_pdf_cert_rnn.pdf. Complete Introduction pp.1–2 reread from cached primary PDF/text. Known→new [relation]; ⇒callback.

P1 p.1: DNN success→adversarial vulnerability limits sensitive use.
<a id="p1"></a><a id="p1-s1"></a>P1.S1 DNNs→successful tasks [context]
<a id="p1-s2"></a>P1.S2 Success→adversarial manipulation inhibits deployment [contrast/value] ⇒guarantee need
P2 pp.1–2: Heuristic arms race motivates formal certification.
<a id="p2"></a><a id="p2-s1"></a>P2.S1 Vulnerability→many defenses [existing answer]
<a id="p2-s2"></a>P2.S2 Heuristics→no guarantees and stronger attacks defeat them [boundary]
<a id="p2-s3"></a>P2.S3 Arms race→verify adversarial-free input regions [stronger answer/definition] ⇒certification object
P3 p.2: Feedforward certification has different assumptions; nearest RNN tool has two causal limits.
<a id="p3"></a><a id="p3-s1"></a>P3.S1 Certification→SMT/MILP/polytope/reachability progress [known capability]
<a id="p3-s2"></a>P3.S2 Feedforward targets→not directly RNN-transferable [boundary]
<a id="p3-s3"></a>P3.S3 RNN input timing/multivariable operations→structural causes [root]
<a id="p3-s4"></a>P3.S4 Structural difficulty→recent RNN attempts exist [stronger alternative]
<a id="p3-s5"></a>P3.S5 Existing RNN methods→lost correlations loosen bounds; expensive planes limit scale [two root→consequence chains] ⇒abstract domain/transformers
P4 p.2: Core method responds to these causes.
<a id="p4"></a><a id="p4-s1"></a>P4.S1 Limits→Cert-RNN [work]
<a id="p4-s2"></a>P4.S2 Inputs→correlation-preserving abstract domain [mechanism1]
<a id="p4-s3"></a>P4.S3 RNN operations→precise efficient transformers [mechanism2]
<a id="p4-s4"></a>P4.S4 Abstract computation→optimization yields bounds [output]
<a id="p4-s5"></a>P4.S5 Design→tighter bounds/faster execution [qualitative preview]
P5 p.2: Detailed performance plus downstream judgments.
<a id="p5"></a><a id="p5-s1"></a>P5.S1 Framework→architectures/four applications [scope]
<a id="p5-s2"></a>P5.S2 Evaluation→precision/efficiency superiority [headline]
<a id="p5-s3"></a>P5.S3 Concrete models→1.86×bound and46.78vs2.66min [two condition-specific examples]
<a id="p5-s4"></a>P5.S4 Bounds→evaluate defenses/identify sensitive words [downstream use]
<a id="p5-s5"></a>P5.S5 Defense comparison→heuristic slight gains versus provable stronger gains [knowledge finding]
<a id="p5-s6"></a>P5.S6 Verified training→improved robustness [application result]
<a id="p5-s7"></a>P5.S7 Word bounds→importance aligns with human understanding [interpretability finding]
<a id="p5-s8"></a>P5.S8 Findings→defense evaluation/robust systems/interpretability metric [value synthesis]
<a id="p6"></a>P6 list gate.
<a id="b1"></a><a id="b1-s1"></a>B1.S1 Diagnosis→prior RNN limits [knowledge]
<a id="b1-s2"></a>B1.S2 Missing correlations→loose bounds [root]
<a id="b1-s3"></a>B1.S3 Expensive approximation→scalability failure [root]
<a id="b2"></a><a id="b2-s1"></a>B2.S1 Method→abstract interpretation framework superiority [artifact]
<a id="b2-s2"></a>B2.S2 Domain→retain correlation [defining mechanism]
<a id="b2-s3"></a>B2.S3 Function-range analysis→case-specific transformers improve bounds/cost [technical detail first expanded here]
<a id="b3"></a><a id="b3-s1"></a>B3.S1 Evaluation→four applications/architectures [scope]
<a id="b3-s2"></a>B3.S2 Results→precision/efficiency advantage [summary]
<a id="b4"></a><a id="b4-s1"></a>B4.S1 Bounds→interpretability and defense-efficacy metric [knowledge/application]
<a id="b4-s2"></a>B4.S2 Framework→improves robustness [result]
<a id="b4-s3"></a>B4.S3 Extensions→norms/RNN types/robust training [outlook, not completed validation]
<a id="b4-s4"></a>B4.S4 Extensions→future applicability/research [expected value]
<a id="b4-s5"></a>B4.S5 Artifact→planned release [reuse commitment]

Observed: detailed results and application findings precede four contributions; B2 adds technical granularity, B4 includes future work explicitly. A bound ratio and runtime ratio refer to different example architectures, so they cannot be fused into one undifferentiated performance claim.
Inferred purpose: the source connects mathematical representation choice to a specific lost dependency, making abstract interpretation useful rather than decorative. Certification's value is a new reliable judgment about defenses, not only a faster algorithm. Preserve completed versus future scope when compressing contributions.

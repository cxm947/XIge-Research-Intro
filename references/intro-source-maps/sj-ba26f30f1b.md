# Adversarial Examples Versus Cloud-based Detectors: A Black-box Empirical Study：完整引言句级图

- 来源身份：sj-ba26f30f1b
- 指定版本：arXiv:1901.01223v4, 2019-09-14, 17 pages, p.1 states TDSC acceptance
- 指定原文：https://arxiv.org/pdf/1901.01223v4
- 实际读取原文：https://arxiv.org/pdf/1901.01223v4
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#cloud-detectors) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [B1](#b1) · [B2](#b2) · [B3](#b3) · [B4](#b4)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

sj-ba26f30f1b; https://arxiv.org/pdf/1901.01223v4;14 September2019 v4,17 pages, states TDSC acceptance. Complete Introduction pp.1–2 reread including contribution continuation after Table2 and roadmap. Known→new [relation]; ⇒callback.

P1 p.1: Cloud APIs solve the resource burden of useful vision models.
<a id="p1"></a><a id="p1-s1"></a>P1.S1 Data/neural learning→vision-task superiority [context]
<a id="p1-s2"></a>P1.S2 Training costs→providers offer APIs without client training/data [deployment rationale]
<a id="p1-s3"></a>P1.S3 APIs→commercial/noncommercial image checking [utility]
<a id="p1-s4"></a>P1.S4 Utility→classification/moderation examples [scope] ⇒detector distinction
P2 pp.1–2: Define attacks and three service settings by access and pipeline complexity.
<a id="p2"></a><a id="p2-s1"></a>P2.S1 Strong models→adversarial errors [contrast/definition]
<a id="p2-s2"></a>P2.S2 Vulnerability→security attention [value]
<a id="p2-s3"></a>P2.S3 Attacks→self-trained classifier/cloud classifier/cloud detector [taxonomy]
<a id="p2-s4"></a>P2.S4 Classifier→maps input to class [definition]
<a id="p2-s5"></a>P2.S5 Detector→locates regions then labels [contrast]
<a id="p2-s6"></a>P2.S6 Self-trained setting→attacker knows training distribution [access]
<a id="p2-s7"></a>P2.S7 Cloud classifier→provider trains [setting]
<a id="p2-s8"></a>P2.S8 Hidden training→many-query attacks [condition/cost]
<a id="p2-s9"></a>P2.S9 Cloud detector→integrated commercial services [setting]
<a id="p2-s10"></a>P2.S10 Detector pipeline→classification plus other processing/human judgment [compositional distinction]
<a id="p2-s11"></a>P2.S11 Complexity→simultaneous bypass with limited queries difficult [challenge] ⇒study scope
P3 p.2: Existing detector/model-stealing studies do not match deployed setting.
<a id="p3"></a><a id="p3-s1"></a>P3.S1 Deployed importance→little cloud-detector work [gap]
<a id="p3-s2"></a>P3.S2 Recent research→standard detection algorithms [nearest scope]
<a id="p3-s3"></a>P3.S3 Standard algorithms→not readily transferable [boundary]
<a id="p3-s4"></a>P3.S4 Boundary→composite pipeline and black-box access [two causes]
<a id="p3-s5"></a>P3.S5 API model extraction→equation-solving precedent [plausible alternative]
<a id="p3-s6"></a>P3.S6 Large commercial model→simple equation-solving impractical [scale condition]
<a id="p3-s7"></a>P3.S7 Precedent→self-trained simple model [scope clarification]
P4 p.2: Work and real-world coverage.
<a id="p4"></a><a id="p4-s1"></a>P4.S1 Gap→first-step cloud-detector study [work]
<a id="p4-s2"></a>P4.S2 Comprehensive study→five providers [scope]
<a id="p4-s3"></a>P4.S3 Provider names→short forms specified [terminological navigation]
P5 p.2: Method family and headline results.
<a id="p5"></a><a id="p5-s1"></a>P5.S1 Study→four semantic-segmentation-informed black-box methods with limited queries [approach/conditions]
<a id="p5-s2"></a>P5.S2 Family→four names [catalogue]
<a id="p5-s3"></a>P5.S3 Evaluation→high bypass approaching100%,Table2 [quantitative preview]
<a id="p5-s4"></a>P5.S4 Findings→contributions [organizer]
<a id="b1"></a><a id="b1-s1"></a>B1.S1 Scope→black-box detectors with no data/model access [research condition]
<a id="b1-s2"></a>B1.S2 Composite pipeline→beyond classifier fooling [task distinction]
<a id="b2"></a><a id="b2-s1"></a>B2.S1 Method family→high bypass/limited queries [technical capability]
<a id="b2-s2"></a>B2.S2 Query cost→thousands versus millions in prior studies [comparative evidence; retain setting differences]
<a id="b3"></a><a id="b3-s1"></a>B3.S1 Evaluation→major cloud providers [scope]
<a id="b3-s2"></a>B3.S2 Findings→all tested major detectors bypassed [summary]
<a id="b3-s3"></a>B3.S3 API-only tests→practical feasibility [condition-to-value]
<a id="b4"></a><a id="b4-s1"></a>B4.S1 Study→defense/security discussion [implication]
<a id="b4-s2"></a>B4.S2 Vulnerabilities→reference for future defenses [value]
<a id="b4-s3"></a>B4.S3 Disclosure→provider acknowledgment [external validation]
<a id="p6"></a>P6 roadmap S1 preliminary/threat-model; S2 algorithms; S3 experiments; S4 effects/defenses; S5 related work; S6 conclusion/future [navigation only].

Observed: Table2 and a headline bypass result precede bullets; query-count and disclosure details occur in bullets. Service taxonomy is central, because classifier and integrated detector attack outcomes are not interchangeable.
Inferred purpose: the introduction spends substantial space preventing a false equivalence with familiar API classifier attacks. Deployment access and pipeline composition determine both novelty and evidence interpretation. Preserve these conditions in any reusable comparison sentence.

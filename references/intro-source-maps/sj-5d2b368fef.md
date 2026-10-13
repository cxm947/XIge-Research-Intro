# JailNeurons：完整引言句级图

- 来源身份：sj-5d2b368fef
- 指定版本：Official ICLR 2026 proceedings PDF, 24 physical/printed pages
- 指定原文：https://proceedings.iclr.cc/paper_files/paper/2026/file/096347b4efc264ae7f07742fea34af1f-Paper-Conference.pdf
- 实际读取原文：https://proceedings.iclr.cc/paper_files/paper/2026/file/096347b4efc264ae7f07742fea34af1f-Paper-Conference.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#jailneurons) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [B1](#b1) · [B2](#b2) · [B3](#b3)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

sj-5d2b368fef; official ICLR2026 proceedings,24 pages; https://proceedings.iclr.cc/paper_files/paper/2026/file/096347b4efc264ae7f07742fea34af1f-Paper-Conference.pdf. Complete Introduction physical1–3 reread; §3/§4.1–4.2 inspected to confirm white-box assumptions and multilayer rationale. Known→new [relation]; ⇒callback.

P1 pp.1: Vision-language ability brings a wider interaction-dependent threat.
<a id="p1"></a><a id="p1-s1"></a>P1.S1 LVLMs→successful capabilities/research attention [context]
<a id="p1-s2"></a>P1.S2 Inherited language ability→amplified security risk [contrast]
<a id="p1-s3"></a>P1.S3 Risk→jailbreak means crafted input causes harmful output [definition]
<a id="p1-s4"></a>P1.S4 Added vision→more diverse/harder attacks [cause]
<a id="p1-s5"></a>P1.S5 Text-only contrast→visual/text interplay [distinctive condition]
<a id="p1-s6"></a>P1.S6 Attacks→three categories illustrated [organizer]
<a id="p1-s7"></a><a id="p1-s8"></a><a id="p1-s9"></a>P1.S7–P1.S9 Perturbations, rendered text, semantic image/text pairing→three mechanisms [parallel enumerated fragments] ⇒cross-attack generalization
P2 pp.1–2: Defense families differ by stage, but deployment needs remain.
<a id="p2"></a><a id="p2-s1"></a>P2.S1 Threats→training/inference families borrowed from LLMs [taxonomy]
<a id="p2-s2"></a>P2.S2 Training defense→alignment costs computation/annotation [capability/trade-off]
<a id="p2-s3"></a>P2.S3 Inference defense→input/output/representation checks [alternatives]
<a id="p2-s4"></a>P2.S4 Inference route→latency and unseen-input generalization gaps [boundary] ⇒lightweight detector
P3 p.2: Change analytical level, distinguish adjacent concepts, then ask existence and usefulness questions.
<a id="p3"></a><a id="p3-s1"></a>P3.S1 Gap→jailbreak-specific abnormal neurons [proposed perspective]
<a id="p3-s2"></a>P3.S2 Safety-neuron precedent→refusal neurons differ from subversion neurons [conceptual distinction]
<a id="p3-s3"></a>P3.S3 Distinction→complementary new LVLM question [position]
<a id="p3-s4"></a>P3.S4 Perspective→two challenges [gate]
<a id="p3-s5"></a>P3.S5 Representation-level hints→small-neuron localization still unconfirmed [existence/localization question]
<a id="p3-s6"></a>P3.S6 Even found neurons→detection utility and OOD transfer unresolved [residual question] ⇒multilayer selection
P4 p.2: Evidence → localization → selection → detector.
<a id="p4"></a><a id="p4-s1"></a>P4.S1 Questions→JDJN efficient generalizable detection [work]
<a id="p4-s2"></a>P4.S2 First challenge→empirically confirm activation separability [evidence]
<a id="p4-s3"></a>P4.S3 Separability→progressively narrow neuron candidates [evidence-to-design]
<a id="p4-s4"></a>P4.S4 Second challenge→select multiple layers [response]
<a id="p4-s5"></a>P4.S5 Selected activations→lightweight classifier [output/mechanism closure]
P5 p.2: Full results preview with evaluation conditions and deployment cost.
<a id="p5"></a><a id="p5-s1"></a>P5.S1 Detector→four LVLMs/three attacks/three benign distributions [scope]
<a id="p5-s2"></a>P5.S2 Tests→baseline superiority [headline]
<a id="p5-s3"></a>P5.S3 Seen LLaVA attacks→>99%TPR/<1%FPR [conditioned result]
<a id="p5-s4"></a>P5.S4 Unseen attacks/OOD benign→>94%TPR/<2%FPR [stronger transfer test]
<a id="p5-s5"></a>P5.S5 Training→few hundred samples/light computation [cost evidence]
<a id="p5-s6"></a>P5.S6 Deployment→no model modification/negligible inference overhead [practical meaning]
<a id="p5-s7"></a>P5.S7 Ablation→localization beats alternatives [mechanism validation]
<a id="p6"></a>P6 list gate.
<a id="b1"></a><a id="b1-s1"></a>B1.S1 Activation study→benign/jailbreak distinctions [knowledge]
<a id="b1-s2"></a>B1.S2 Distinctions→different attacks distributed across layers [structural finding; adds detail]
<a id="b2"></a><a id="b2-s1"></a>B2.S1 Localization→layerwise mask method [technical outcome]
<a id="b2-s2"></a>B2.S2 Masks→isolate signal/reduce overfitting [reasoned capability]
<a id="b3"></a><a id="b3-s1"></a>B3.S1 Detector→lightweight efficient framework [artifact]
<a id="b3-s2"></a>B3.S2 Evaluation→highTPR/near-zeroFPR and OOD generalization [summary relying P5]

Observed: quantitative results precede contributions; B1 adds cross-layer distribution content, B3 compresses prior evidence. A proposed perspective precedes its existence challenge; the introduction does not assume neuron-level existence merely because representation separability is known. Adjacent method explains why one full layer fails to transfer.
Inferred purpose: the SafeNeurons/JailNeurons distinction prevents a superficially similar prior contribution from obscuring the new object. Staging existence before usefulness avoids conflating a discriminative observation with a deployable detector. Seen and unseen result conditions deserve separate sentences because they validate different promises.

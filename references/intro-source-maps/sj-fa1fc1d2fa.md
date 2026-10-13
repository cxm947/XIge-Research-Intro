# Smart Contract Graph Feature / Expert Pattern Fusion：完整引言句级图

- 来源身份：sj-fa1fc1d2fa
- 指定版本：arXiv:2106.09282v1 [cs.LG], 2021-06-17, 9-page author preprint
- 指定原文：https://arxiv.org/pdf/2106.09282v1
- 实际读取原文：https://arxiv.org/pdf/2106.09282v1
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#smart-contract-fusion) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [C1](#c1) · [C2](#c2) · [C3](#c3)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

sj-fa1fc1d2fa; https://arxiv.org/pdf/2106.09282v1;17 June2021 v1,9 pages. Complete Introduction pp.1–2 reread, adjacent problem formulation checked. Known→new [relation]; ⇒callback.

P1 p.1: Define blockchain and relevant properties.
<a id="p1"></a><a id="p1-s1"></a>P1.S1 Blockchain→research attention [context]
<a id="p1-s2"></a>P1.S2 Miners/consensus→shared secure ledger [definition]
<a id="p1-s3"></a>P1.S3 Recorded transactions→immutability/decentralization [property] ⇒contract update constraint
P2 p.1: Define smart contracts through purpose, execution and application.
<a id="p2"></a><a id="p2-s1"></a>P2.S1 Blockchain→programs on top [definition]
<a id="p2-s2"></a>P2.S2 Program→rules for digital assets [purpose]
<a id="p2-s3"></a>P2.S3 Immutability→deployed code not updated [constraint as framed]
<a id="p2-s4"></a>P2.S4 Rules as code→automatic impartial execution [benefit]
<a id="p2-s5"></a>P2.S5 Automation→complex DApps [application value]
P3 p.1: Economic value creates attack stakes.
<a id="p3"></a><a id="p3-s1"></a>P3.S1 Contracts→millions and large managed value [scale]
<a id="p3-s2"></a>P3.S2 Value→attacker attraction [consequence]
<a id="p3-s3"></a>P3.S3 Threat→DAO theft example [evidence]
<a id="p3-s4"></a>P3.S4 Example→recurring vulnerabilities [generalization]
P4 p.1: Explain vulnerability roots.
<a id="p4"></a><a id="p4-s1"></a>P4.S1 Vulnerabilities→two roots [organizer]
<a id="p4-s2"></a>P4.S2 Immature languages/tools→misunderstanding built-ins [root1]
<a id="p4-s3"></a>P4.S3 Immutable deployment→must anticipate future states/environments [root2]
P5 pp.1–2: Two approaches have complementary strengths and weaknesses, leading to interpretable fusion.
<a id="p5"></a><a id="p5-s1"></a>P5.S1 Detection→two categories [organizer]
<a id="p5-s2"></a>P5.S2 Classical analysis→static/dynamic techniques [route]
<a id="p5-s3"></a>P5.S3 Fixed rules→errors and missed complex patterns [boundary]
<a id="p5-s4"></a>P5.S4 Fixed rules→can be bypassed [consequence]
<a id="p5-s5"></a>P5.S5 Deep learning→handles complexity/improves accuracy [stronger complementary capability]
<a id="p5-s6"></a>P5.S6 Black box→poor expert-knowledge integration/interpretability [boundary]
<a id="p5-s7"></a>P5.S7 Complementary abilities→combine global semantic graph with precise local patterns [research question/design rationale]
<a id="p5-s8"></a>P5.S8 Fusion→seek explainable feature weights [extra success criterion]
P6 p.2, Our method: Work→local/global representations→fusion→evidence.
<a id="p6"></a><a id="p6-s1"></a>P6.S1 Goal→explainable neural/expert system [work]
<a id="p6-s2"></a>P6.S2 Local patterns→automatic extraction [operation]
<a id="p6-s3"></a>P6.S3 Function code→control/data-flow graph [parallel representation]
<a id="p6-s4"></a>P6.S4 Graph→GNN feature [operation]
<a id="p6-s5"></a>P6.S5 Representations→attentive multi-encoder fusion [integration/output]
<a id="p6-s6"></a>P6.S6 Evaluation→40kcontracts/two datasets/three accuracy gains [scope+quantitative evidence]
<a id="p6-s7"></a>P6.S7 Accuracy→prediction explanation/local warnings/feature importance [additional capability]
P7 p.2, Contributions:
<a id="p7"></a><a id="p7-s1"></a>P7.S1 Contributions organizer.
<a id="c1"></a><a id="c1-s1"></a>C1.S1 Fusion→interpretable combination investigated [knowledge/method]
<a id="c1-s2"></a>C1.S2 Combination→qualified first claim [position]
<a id="c2"></a><a id="c2-s1"></a>C2.S1 Fusion→multi-encoder network [technical artifact]
<a id="c3"></a><a id="c3-s1"></a>C3.S1 Results→state-of-art/insights [summary relying P6]
<a id="c3-s2"></a>C3.S2 Implementations→release [reuse]
<a id="c3-s3"></a>C3.S3 Related Liu2021→this work emphasizes explainability of combination/feature weights [explicit adjacent-work distinction]

Observed: final sentence after contributions clarifies difference from a close paper; it is part of Introduction, not ignorable footer. Numerical results occur before list. Classical patterns are retained as valuable rather than rejected wholesale.
Inferred purpose: complementary information roles, local expert evidence and global semantics, justify fusion better than generic accuracy claims. Interpretability is operationalized as weights before it appears as an evaluation benefit. The source's reported gains belong to three different vulnerabilities and should retain their pairing.

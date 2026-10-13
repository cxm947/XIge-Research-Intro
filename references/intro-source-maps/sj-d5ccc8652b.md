# ACIArena：完整引言句级图

- 来源身份：sj-d5ccc8652b
- 指定版本：Official ACL 2026 Volume 1 long-paper proceedings
- 指定原文：https://aclanthology.org/2026.acl-long.457.pdf
- 实际读取原文：https://aclanthology.org/2026.acl-long.457.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#aciarena) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [B1](#b1) · [B2](#b2) · [B3](#b3)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

sj-d5ccc8652b; official ACL 2026 long-paper proceedings pp.10049–10066; https://aclanthology.org/2026.acl-long.457.pdf. Complete Introduction physical1–2/printed10049–10050 reread from cached PDF/text. Known → new [relation]; ⇒ callback.

P1 p.10049: Define collaborative MAS, establish real deployment, then broader value.
<a id="p1"></a><a id="p1-s1"></a>P1.S1 LLM agents → collaborative MAS for complex tasks [definition/context] ⇒ interaction risk
<a id="p1-s2"></a>P1.S2 Specialization/coordination → coding/math performance and real adoption [capability] ⇒ stakes
<a id="p1-s3"></a>P1.S3 Adoption → developer/enterprise orchestration examples [concretization] ⇒ real-system evaluation
<a id="p1-s4"></a>P1.S4 Examples → collaboration as scalable promising direction [value inference] ⇒ importance of robustness
P2 p.10049: Useful interaction is also the propagating attack surface.
<a id="p2"></a><a id="p2-s1"></a>P2.S1 Enhanced ability → complex interactions add vulnerabilities [contrast] ⇒ ACI
<a id="p2-s2"></a>P2.S2 Agent-context injections → exploit trust and propagate, named ACI [mechanism/definition] ⇒ surfaces/objectives
<a id="p2-s3"></a>P2.S3 Propagation → unintended behavior/system collapse [consequence] ⇒ robustness task
P3 pp.10049–10050: Three limitations of existing evaluation, including stronger framework alternative.
<a id="p3"></a><a id="p3-s1"></a>P3.S1 Existing ACI work → three critical limitations [organizer] ⇒ requirements
<a id="p3-s2"></a>P3.S2 Threat scenarios → studies isolate surfaces/objectives [specific scope boundary] ⇒ comprehensive matrix
<a id="p3-s3"></a>P3.S3 Isolated studies → no systematic vulnerability coverage [consequence] ⇒ benchmark
<a id="p3-s4"></a>P3.S4 Tailoring/internal access → limited practical applicability [additional threat-model condition] ⇒ realistic attacks
<a id="p3-s5"></a>P3.S5 Evaluation settings → simplified MAS impede real-world transfer [second root/consequence] ⇒ unified realistic implementations
<a id="p3-s6"></a>P3.S6 Codebase design → insufficient modularity limits extension [third root] ⇒ modular interfaces
<a id="p3-s7"></a>P3.S7 Existing MASLab → standard inputs/protocols but lacks security-evaluation components [stronger alternative + remaining gap] ⇒ ACIArena purpose
<a id="p3-s8"></a>P3.S8 Combined limitations → unified comprehensive extensible framework needed [derived requirement] ⇒ P4
P4 p.10050: Announce framework and map features to limits.
<a id="p4"></a><a id="p4-s1"></a>P4.S1 Limitations → ACIArena robustness framework [work] ⇒ contributions
<a id="p4-s2"></a>P4.S2 Named system → three features [organizer]
<a id="p4-s3"></a>P4.S3 Threat incompleteness → multiple attack surfaces/objectives [coverage response] ⇒ B1
<a id="p4-s4"></a>P4.S4 Inconsistent settings → shared MAS and attack/defense interfaces [standardization response] ⇒ B2
<a id="p4-s5"></a>P4.S5 Rigid implementation → modular architecture supports new systems/modules [extensibility response] ⇒ B2
P5 p.10050: Findings and a derivative defense precede contributions.
<a id="p5"></a><a id="p5-s1"></a>P5.S1 Experiments → multidimensional systemic vulnerabilities [headline finding] ⇒ B3
<a id="p5-s2"></a>P5.S2 Defenses → partial protection, failed transfer or amplified attacks [qualified result] ⇒ design lesson
<a id="p5-s3"></a>P5.S3 Findings → ACI-Sentinel preserves task-aligned information [derived design response] ⇒ B3 insight
<a id="p5-s4"></a>P5.S4 Completed study → contribution list [organizer]
<a id="b1"></a><a id="b1-s1"></a>B1.S1 Framework → first systematic ACI robustness benchmark claim [resource contribution]
<a id="b1-s2"></a>B1.S2 Benchmark →1,356 cases across3×3 dimensions [scope/coverage evidence; first count]
<a id="b1-s3"></a>B1.S3 Resource → planned public code/data [reuse]
<a id="b2"></a><a id="b2-s1"></a>B2.S1 Interface/codebase → unified extensible evaluation avoids poor generalization from simplified/inconsistent settings [design + purpose]
<a id="b3"></a><a id="b3-s1"></a>B3.S1 Benchmark results → factors, defense failures and design insights [knowledge contribution]

Observed: a resource/benchmark Introduction places findings before contributions; the last bullet summarizes analysis rather than generic system accuracy. No independent challenge paragraphs or numerical model-performance preview. Benchmark size first occurs in contributions; qualitative findings precede them. ACI-Sentinel appears as a finding-driven design, not a separately enumerated contribution.
Inferred purpose: matching each benchmark feature to a different evaluation failure makes comprehensiveness and extensibility substantive research choices. Introducing the stronger MASLab alternative prevents confusing ordinary unified implementation with the missing security-comparison capability. Resource construction is justified by judgments it enables.

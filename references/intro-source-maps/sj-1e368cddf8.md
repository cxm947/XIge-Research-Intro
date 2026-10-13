# DPCSS：完整引言句级图

- 来源身份：sj-1e368cddf8
- 指定版本：13-page accepted author manuscript under DOI 10.1109/TCE.2026.3656205, explicitly not fully edited
- 指定原文：https://nesa.zju.edu.cn/download/tce26_suyuan.pdf
- 实际读取原文：https://nesa.zju.edu.cn/download/tce26_suyuan.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#dpcss) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [B1](#b1) · [B2](#b2) · [B3](#b3)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

sj-1e368cddf8;13-page accepted author manuscript, DOI10.1109/TCE.2026.3656205, explicitly not fully edited; https://nesa.zju.edu.cn/download/tce26_suyuan.pdf. Complete Introduction physical1–2, web lines58–153, reread. Local download403; primary web text used. Known→new [relation]; ⇒callback.

P1 p.1: IoT→healthcare→continuous data creates storage burden.
<a id="p1"></a><a id="p1-s1"></a>P1.S1 IoT→data-service opportunities [broad frame]
<a id="p1-s2"></a>P1.S2 IoT applications→healthcare transformation [narrowing]
<a id="p1-s3"></a>P1.S3 Wearables→collect physiological metrics in real time [mechanism/example]
<a id="p1-s4"></a>P1.S4 Metrics→personalized/proactive care [value]
<a id="p1-s5"></a>P1.S5 Device growth→on-device scale/share/analysis burdens [contrast] ⇒edge storage
P2 pp.1–2: Existing continuous storage has two connected but distinct root costs.
<a id="p2"></a><a id="p2-s1"></a>P2.S1 Burden→distributed edge storage/access [existing remedy]
<a id="p2-s2"></a>P2.S2 Healthcare data→confidentiality/integrity/availability needs [constraint]
<a id="p2-s3"></a>P2.S3 Long-term use→continuous secure preservation required [task specification]
<a id="p2-s4"></a>P2.S4 Existing schemes→continuous guarantees but heavy preprocessing/tools [capability/trade-off]
<a id="p2-s5"></a>P2.S5 Preprocessing→whole period and challenge-proof pairs precomputed [mechanism]
<a id="p2-s6"></a>P2.S6 Precomputation→repeated trapdoor VDF evaluations [computational cause]
<a id="p2-s7"></a>P2.S7 Audit count scales with time/frequency→large overhead [root-to-cost]
<a id="p2-s8"></a>P2.S8 Cost→storage-time-independent lightweight preprocessing question [requirement1]
<a id="p2-s9"></a>P2.S9 Outsourcing→client loses physical control [new condition]
<a id="p2-s10"></a>P2.S10 Loss of control→access/update/revocation must remain available [operational need]
<a id="p2-s11"></a>P2.S11 Need→dynamic continuous-storage updates [requirement]
<a id="p2-s12"></a>P2.S12 Existing verification→local trapdoor results first [mechanism]
<a id="p2-s13"></a>P2.S13 Storage end→compare proofs/local results [sequence]
<a id="p2-s14"></a>P2.S14 Precomputed proofs→data changes invalidate whole chain [root]
<a id="p2-s15"></a>P2.S15 Recompute→hurts realtime access/bandwidth/client cost [consequence]
<a id="p2-s16"></a>P2.S16 Cost→efficient realtime updates question [requirement2]
P3 p.2: Summarize roots, announce design, then acknowledge a cost introduced by the design.
<a id="p3"></a><a id="p3-s1"></a>P3.S1 Prior mechanisms→linear preprocessing/static chains [synthesis]
<a id="p3-s2"></a>P3.S2 Roots→lightweight continuous verification/update/forward-security goals [derived requirements]
<a id="p3-s3"></a>P3.S3 Goals→DPCSS [work]
<a id="p3-s4"></a>P3.S4 VDF+tags→periodic integrity without assistance [core capability]
<a id="p3-s5"></a>P3.S5 Cross-server validation→sequential prove-and-verify removes client preverification [decisive mechanism]
<a id="p3-s6"></a>P3.S6 Static-chain removal→dynamic updates [consequence]
<a id="p3-s7"></a>P3.S7 Cross-validation→all-server exchange introduces quadratic communication [design-induced obstacle]
<a id="p3-s8"></a>P3.S8 New cost→structural interaction reduces communication to reported O(n^1/2) [response; preserve source notation/metric context]
<a id="p3-s9"></a>P3.S9 Work→contributions [organizer]
<a id="b1"></a><a id="b1-s1"></a>B1.S1 Scheme→distributed continuous storage/cross-validation [artifact]
<a id="b1-s2"></a>B1.S2 Cross-validation→no local preverification [mechanism/benefit]
<a id="b1-s3"></a>B1.S3 Corruption→prompt cheater detection [additional capability]
<a id="b2"></a><a id="b2-s1"></a>B2.S1 Interaction design→efficient communication [technical outcome]
<a id="b2-s2"></a>B2.S2 Key wrapping→realtime updates/forward security [second technical response]
<a id="b3"></a><a id="b3-s1"></a>B3.S1 Scheme→formal confidentiality/forward-security/unforgeability proofs [theoretical evidence]
<a id="b3-s2"></a>B3.S2 Experiments→efficient verification/constant preprocessing independent of time/frequency [empirical evidence]
P4 p.2 roadmap:
<a id="p4"></a><a id="p4-s1"></a>P4.S1 Paper→organization announcement; S2 Related work→§II; S3 Preliminaries→§III; S4 Models/definitions/goals→§IV; S5 Scheme→§V; S6 Security/performance→§VI–VII; S7 Conclusion→§VIII [all navigation; no new research claims].

Observed: main method paragraph previews analytic communication order, but formal-security and experimental evidence first appear in B3. Quadratic cost is introduced after cross-validation, not retroactively called an existing-work gap. Roadmap is retained as a distinct optional closing role.
Inferred purpose: the introduction follows obligations from healthcare use rather than claiming cryptographic novelty from application naming. The source keeps the price of its own distributed validation visible, which licenses the subsequent interaction design. Transfer templates should preserve the metric being bounded and the accepted-manuscript status rather than polish them into stronger claims.

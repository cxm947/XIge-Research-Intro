# VideoEraser：完整引言句级图

- 来源身份：sj-cc51b110bc
- 指定版本：Official EMNLP 2025 ACL proceedings PDF, pp.5954-5983
- 指定原文：https://aclanthology.org/2025.emnlp-main.304.pdf
- 实际读取原文：https://aclanthology.org/2025.emnlp-main.304.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#videoeraser) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [C1](#c1) · [C2](#c2) · [C3](#c3)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

Source https://aclanthology.org/2025.emnlp-main.304.pdf; officialEMNLP2025,5954–5983. Full intro physical1–2; relevant §2–3 beginning reread.

Chain P1 video capability→harm→need even under explicit prompts; P2 natural retraining/finetuning route→four limitations; P3 mechanism and why training-free solves those deployment issues; P4 evaluation framework defines five success dimensions; C1–3 task/method/evidence. 推断：时序一致性不能被图像方法的一般“质量”吞掉，故先解释视频机制的额外要求，再把fidelity放入评价框架；贡献最后一句得以高层概括，无需五项各写一条。

<a id="p1"></a><a id="p1-s1"></a>P1.S1 定位：T2V→按文本生成高质量视频 | 起题 | object
<a id="p1-s2"></a>P1.S2 实例：开源系统→内容创造及CFG | 具体化 | generalization
<a id="p1-s3"></a>P1.S3 风险：能力→隐私版权安全 | 转折 | erasure tasks
<a id="p1-s4"></a>P1.S4 根因：未过滤网页训练→有害未授权生成 | 原因 | task
<a id="p1-s5"></a>P1.S5 例证：艺术风格→未许可复制 | 举例 | style erasure
<a id="p1-s6"></a>P1.S6 例证：人物/NSFW视频→误导或有害 | 添加 | celebrity/explicit tasks
<a id="p1-s7"></a>P1.S7 要求：风险→明确提示也不得生成 | 推论 | efficacy/robustness
<a id="p2"></a><a id="p2-s1"></a>P2.S1 自然解及边界：过滤后重训→成本不现实 | 让步 | training-free
<a id="p2-s2"></a>P2.S2 替代：重训→概念擦除 | 转向 | method class
<a id="p2-s3"></a>P2.S3 定义：已训练模型→阻止目标及相关提示生成 | 解释 | task
<a id="p2-s4"></a>P2.S4 现状：T2V擦除→已有工作少 | 转折 | nearest work
<a id="p2-s5"></a>P2.S5 近邻：T2I多依赖微调→待述局限 | 比较/预告 | next
<a id="p2-s6"></a>P2.S6 成本根因：关键帧及插值组件→联合微调难 | 枚举一 | training-free
<a id="p2-s7"></a>P2.S7 存储根因：每概念专用模型→多模型负担 | 枚举二 | plug-and-play
<a id="p2-s8"></a>P2.S8 完整性：权重微调→非目标生成损失 | 枚举三 | integrity
<a id="p2-s9"></a>P2.S9 稳健性：仅文本编码器→对抗提示绕过 | 枚举四 | ARNG
<a id="p3"></a><a id="p3-s1"></a>P3.S1 工作：四限制→VideoEraser | 响应 | C2
<a id="p3-s2"></a>P3.S2 两阶段首段：任务→SPEA识别触发token | 总述+第一操作 | §3.1
<a id="p3-s3"></a>P3.S3 作用：调整embedding→抑目标保非目标 | 机制—目标 | integrity
<a id="p3-s4"></a>P3.S4 第二操作：噪声引导→远离目标并抗对抗提示 | 并列且补残余 | §3.2
<a id="p3-s5"></a>P3.S5 视频特有设计：引导目标→步间及帧间一致 | 添加 | fidelity
<a id="p3-s6"></a>P3.S6 原理总结：内在语义→无微调数据/时间/存储且对抗可靠 | 因果压缩 | E
<a id="p3-s7"></a>P3.S7 部署范围：无权重更新→跨UNet/DiT适配 | 推论+例证 | generalization
<a id="p4"></a><a id="p4-s1"></a>P4.S1 评价缺口：现有T2V→缺全面框架 | 新维度 | C3
<a id="p4-s2"></a>P4.S2 根因：仅看去目标→忽略其他生成影响 | 解释 | success axes
<a id="p4-s3"></a>P4.S3 工作：遗漏→视频特定评价框架 | 响应 | E
<a id="p4-s4"></a>P4.S4 定义：理想算法→效果/完整/质量时序/鲁棒/泛化 | 五维列举 | E+C2/3
<a id="p4-s5"></a>P4.S5 贡献引导 | 已知设计→归纳 | 组织 | C
<a id="c1"></a><a id="c1-s1"></a>C1.S1 问题贡献：四任务→无训练即插即用 | 归纳范围 | E
<a id="c1-s2"></a>C1.S2 认识：视频特性→既有方法难直接迁移 | 回收障碍 | P2
<a id="c2"></a><a id="c2-s1"></a>C2.S1 方法：VideoEraser→概念擦除框架 | 归纳 | M
<a id="c2-s2"></a>C2.S2 设计价值：SPEA/ARNG→多维权衡 | 综合能力 | E
<a id="c3"></a><a id="c3-s1"></a>C3.S1 证据：基准→大幅胜基线且跨模型泛化 | 高层结果 | E

Ending inventory: input/output, four inherited limitations, two mechanisms, video-specific consistency, five criteria and model families already known; contribution has no obligatory numbers and no separate module bullets. Intro presents no numeric evaluation results; those remain downstream. Source's “silver bullet” and “large margins” are rhetoric, not reusable evidence substitutes. Concept erasure here is generation suppression, not a proof of training-data deletion.

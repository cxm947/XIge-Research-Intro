# 关系语法与指称修复

仅在当前句存在关系、指称或压缩歧义时选相应例子。以下是源文选择与局部编辑示范，不是新的整篇生成程序。只迁移关系表达，不把源论文事实变成当前稿件事实。

- **相关性：** 两个量共同变化。写“与……相关/伴随”，说明它为什么是可用线索；不能自动写“导致”。PRSA 的互信息—泄漏风险解释应保持源文相关口径。
- **因果/机制：** 明确的操作或条件通过某条路径改变结果。写出作用对象与中间过程，必要时保留“可能”。Diff-ID 将属性混杂与直接距离的误差相连，必须区分这项测量困难与身份损失的生成解释。
- **独立需求：** 同一个任务还需同时满足另一项约束。写“此外/还需/与此同时”；MOpt 的调度吞吐预算不是前一段时变性产生的副作用。
- **前一步残余：** 一项动作解决 A，但 B 原本就存在且尚未解决。写“仅有 A 仍不足以 B”；PRSA 的生成之后还需通用性处理，不得写成生成阶段首次创造了实例污染问题。
- **设计代价：** 本文选择 D 后，D 的结构引出了新问题 B。先解释 D，再写“这种划分/共享/近似使……”；SUB-PLAY 的子博弈分流和发生频率共同解释经验不均。需有材料证明这条路径，不能凡有后续模块都叫代价。
- **流程或依赖：** A 产出 B，C 使用 B 完成 D。写出接收对象；“随后”仅表示顺序，“基于”也不自动证明科学因果。MPInspector 的模型与性质进入验证是工作流，不等于观察关联的因果证明。

先按研究材料实际写完连续段落，再做一次不看编号的连读。若句子只因模板编号而存在，删除或并入实质信息；新段的对象来由不明时，补对象关系。合句与分句取决于接下来要发展哪项判断，不按长度或关系数量决定：围绕同一次比较的输入、操作和共同条件可以合句；需要分别发展输入前提与可得性时再拆开。读者作出判断时还拿不到必要条件，就在该判断处补入或前移，不必移到句首。关系已经清楚时可保留原句。

[Diff-ID §I](https://arxiv.org/pdf/2303.18174v1) 将生成器、待验与参照图像、共同属性空间写在一句中，持续解释同一次比较，可以保留复句。[Cert-RNN §1](https://nesa.zju.edu.cn/download/dty_pdf_cert_rnn.pdf) 的结果句则让两项比较各有模型条件。可保义改写为：“On the MNIST sequence dataset, Cert-RNN yields certified robustness bounds that are, on average, 1.86 times as large as POPQORN's for RNN-2-32; for LSTM-1-32, the average runtime is 2.66 minutes for Cert-RNN and 46.78 minutes for POPQORN.” 两项结果均在 MNIST 序列数据集上，前者报告 RNN-2-32 的认证界平均为 POPQORN 的 1.86 倍，后者报告 LSTM-1-32 的平均运行时间。合句或拆句都不能将它们改成同一模型无条件地“更准、更快”，也不能把研究目标改成已实现结果。

**施事随实际动作确定，源文句法也要检查。** [MPInspector §1](https://www.usenix.org/system/files/sec21-wang-qinying.pdf)，印刷 p.4206 右栏 Second 段，原句以 “when applying model learning” 引出条件，主句的 they 却指协议实现；省略从句容易把“应用学习”也挂到实现上，不能把它当作已显化不同施事的正例。可改为：“When model learning is applied to real-world MP implementations, the implementations may return uncertain responses because of uncontrolled factors.” 即“当模型学习应用于现实中的消息协议实现时，这些实现可能因不可控因素返回不确定的响应”。改写让协议实现成为学习的作用对象及响应的返回者；不据此断言其他研究动作由人工完成。被动式、动作名词或作者主语是否保留，取决于当前要解释的对象。

**指称只在需要时显化。** 先行对象唯一时保留代词；多个对象同时被追踪时重复准确名称。AsgLDP的系统名与it如何交替、compute和estimate怎样分别推进产物，见[完整成句案例](worked-choices.md)。不要为不断更换主语而改变动作施事。

**压缩动作时保住比较和触发。** 距离、阈值、判断和后续动作是不同角色。保留实际比较两端、条件与对应动作；相邻句只重复同一用途时可以合并，但不能删掉决定动作范围的条件。

段落结尾优先交付一个已推进的判断，段落开头承接该判断并新增信息；不必每段结尾都提问、每段开头都说“为了解决上述挑战”。贡献中的必要复现是压缩索引，不按重复词数机械删去。最终可检验的产物是读者能一口气读通的完整引言，而不是 P/S 结构全齐。

**常规从句要真正成句。** although 后填主语和谓语，例如 “Although [method] supports [capability], [bounded limitation] remains under [condition]”，不能只填能力名词。经验问题写 “It remains unclear whether [subject] [predicate]” 或 “how [subject] [predicate]”，使用嵌入问句的陈述语序。性质句区分 “[Object] preserves [relation] under [condition]” 与 “[Objects] differ in [property]”，不要把及物动词和 differ in 共用同一种补语。中文按实际关系自然成句，不保留英语空槽结构。

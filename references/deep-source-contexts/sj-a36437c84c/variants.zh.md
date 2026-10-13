# UVSCAN：整句与完整段落变体

以下为本轮编辑选项，不是源文引语，也不是写作效果试验。保留源研究任务、条件与完成状态；改变句法或焦点时明确写出代价。编号沿54单元底稿，不能拿局部片段自动替换整篇。源时代事实在同一时代叙述；本轮不声称更新了源码开放、厂商确认或现存工具状态。

## V01 · P2.S4：从单长句到定义句群

When adopting TPCs, developers may fail to follow their API specifications. Such failures give rise to TPC usage violations, which typically involve API misuses such as unchecked return values or incorrect invocation sequences.

- 范围：完整替代P2.S4；前后P2.S3规范复杂、S5安全含义保留
- 语义与强度：保may、typically、such as；把原resulting结果升为第二主句，未把全部违反定义为漏洞
- 焦点与取舍：两句分别交失误行为和任务名称，读者较易获得新术语；代价是更明确的重复指称
- 选择条件：读者尚不熟悉usage violation，而一次塞入行为、命名、类型使概念不清时；熟悉任务的读者可保一句

## V02 · P4.S1–S7：判据与两条强已有路线

API specifications state the requirements used to judge whether an API is used correctly. Recovering these requirements is difficult because they may be implicit or explicit in loosely organized, unstructured TPC documents. We therefore need to obtain API specifications with adequate coverage and precision before detecting usage violations. Existing NLP-based methods extract specifications from documentation [30, 32, 34], but most perform well mainly on well-formatted documents and struggle with unusual or ambiguous requirements. Other approaches infer specifications from usage examples [26, 45]. These examples may be incorrect, and covering every usage case is difficult, if not impossible. Inaccurate or incomplete specifications can then lead to false positives and lower detection precision.

- 范围：完整替代P4正文，不含原小标题
- 语义与强度：最后can取代源尾链will，是保守化因果转述；adequate coverage不再逐字保留all APIs的理想目标，若完整覆盖是本研究必须承诺的任务要求，应改回“the specifications of all APIs accurately”并另给可达性依据
- 焦点与取舍：将正确性判据放进首句主谓结构；文档路线、实例路线各有能力与局限。两类不足没有糊成“过去NLP不好用”
- 选择条件：想让强已有答案先可理解，再推出剩余；不适合作为已证明本文抽取完备性的文字

## V03 · P6.S1–S8：从可用输入推出分析责任

IoT firmware is commonly distributed as closed-source binaries, so usage-violation detection must operate without source code. Source-level detectors can use established static-analysis tools such as CodeQL [2] or dedicated checkers. Binary analysis faces additional difficulties: compilation and stripping remove information needed by the checkers, assembly instructions encode complex relationships among API-related operations, and different architectures use different instruction sets. A binary-level detector must therefore recover the information and relationships needed for checking across these architectures.

- 范围：重组P6.S1–S8；不含S9源时代“没有CodeQL式二进制工具”的生态判断
- 语义与强度：最后一句为从源难题推出的编辑归纳，不是假称源逐字句；recover指为检查取得相关分析信息，不能理解为无损还原全部源代码
- 焦点与取舍：保留旧法的可用工具优势，将三个原因并列收进一个长句；短版不再逐一给missing symbols、x86/ARM/MIPS的例子
- 选择条件：面向已懂二进制术语的读者，需要节省挑战段篇幅；若不熟悉汇编，应保源三个原因分句及例子

## V04 · P8.S1–S3：把定制动作和沿用知识同时写明

We first filter irrelevant API descriptions from TPC documents using a sentiment-based model that combines coreference resolution with a customized BiLSTM and multi-head self-attention. An MRC system customized with task-specific questions and a manually constructed dataset then extracts API specifications from the filtered documents. To generate programming expressions, we construct a dependency tree for each specification using part-of-speech information and map its phrases through semantic patterns. We reuse patterns from prior work and extend them through synonym substitution and voice transformations.

- 范围：完整替代P8.S1–S3的操作描述；First/Second挑战序号变为输入依赖顺序
- 语义与强度：保人工数据来源、现成MRC范式及既有语义模式；并未声明原始BiLSTM或MRC由本文发明；去掉well-designed自评
- 焦点与取舍：从propose/design矩阵改成任务动作矩阵，模式出处成为独立主句。语义模式三部分仍在，但源一句内从句较多的节奏被四句替代
- 选择条件：主要难处是读者不清楚每步实际做什么、谁的能力被沿用；若论文需要显式逐项回扣挑战，可保to address前置框架

## V05 · P8.S4–S8：基础工具、本文扩充、任务引擎分开

For firmware processing, we adopt FirmSec [48] and add task-specific enhancements. FirmSec extracts firmware objects and identifies TPCs using syntactical and control-flow-graph features. We then design a rule-driven engine with checkers for the targeted usage violations. The engine encodes binary code as Datalog facts [13] and extracts contextual logical relationships. It uses the generated programming expressions to check TPC usage in the binary firmware.

- 范围：完整替代P8.S4–S8
- 语义与强度：保基础工具引用与Datalog引用；最后一句是能力说明，主动移去源high precision and recall预告，数值证据留B1，并非研究效果被否认
- 焦点与取舍：FirmSec为能力施事，we为采用/定制施事，engine为分析施事；可避免把所有句子都写成we propose而模糊归属
- 选择条件：贡献紧随方案且会给终端性能，方案段优先解释工作方式；若前文尚无结果概览，可保一条有据的定性预告

## V06 · B1完整贡献：跨层能力及真实比较方向

We present UVSCAN, an automated system that connects document-derived API specifications to usage-violation analysis of binary IoT firmware. On real and artificial ground-truth datasets containing 146 usage violations in total, evaluated across x86, ARM, and MIPS, UVSCAN achieves precision of 68.92–77.03% and recall of 73.91–80.52%. Despite operating on binaries, it outperforms APISAN [45] and APEx [26] on these datasets and approaches Advance [30]. We will open-source UVSCAN to support future IoT security research at https://github.com/BBge/IoT-CVE.

- 范围：B1四句全替代；引用保留是为了本源研究可追溯，迁移成别的论文时不得照搬这些结果或引文
- 语义与强度：范围为表7中两数据集×三架构所列结果，非单一聚合结果或置信区间；146不是每架构独立新增146种违反。比较方向依据§4.2.4正文；将源excellent improvement over Advance修正，不能标为源句等义改写
- 焦点与取舍：移除首次性以把能力关系置前；给范围会占一整句，但保留输入约束和具名比较后，读者知道实际能力推进。不需要将所有组件F1、时间、错误来源一起搬来
- 选择条件：论文应直接回答“二进制上是否可用”且可以容纳具体结果；若只需学习句法，应迁移让步输入→能力结果的关系，不迁移数字

## V07 · B2完整贡献：从检测动作转为研究所得

We use UVSCAN to conduct a large-scale study of TPC usage violations in IoT firmware. Across 4,545 firmware images and four TPCs, the study detects 27,621 usage-violation instances, showing that the problem is widespread in the analyzed corpus. Case studies demonstrate that some violations can have serious consequences, including denial of service and man-in-the-middle exposure. So far, vendors have confirmed 206 reported violations as vulnerabilities, and seven of these have received high-severity CVE IDs.

- 范围：B2五句改为四句，保研究动作、分母、发现、风险和验证子集
- 语义与强度：instances显化跨固件版本累计计数；some与case studies限定后果来源；So far为源报告时点，不是2026年的最新状态。移除首次性，无全球发生率推断
- 焦点与取舍：以study作句法主体承接工具使用，避免连续detect/uncover看似两次独立发现；牺牲源两次first的优先权强调
- 选择条件：全文兼顾系统和测量，且B1已经交系统能力；适合突出研究得到了什么知识，而不是再列一次系统功能

## V08 · B2主题重排：当研究真正以复用传播为问题

We use UVSCAN to study TPC usage violations in the analyzed firmware corpus, with particular attention to violations inherited through reused TPCs. The scan identifies 27,621 violation instances involving four TPCs across 4,545 firmware images. More than 40% of the reported instances are inherited from other TPCs adopted by the firmware. This finding links the study to the reuse-related amplification discussed earlier.

- 范围：有条件地重排B2.S1–S3，并加入§5.2的继承比例；若仍需实践后果和外部确认，应保留B2.S4–S5。不是B2全部的等义替换
- 语义与强度：>40%来自§5.2而非引言；英文只交所分析语料中的继承观察，没有声称系统解释违反如何长期持续或重建逐条传播因果链。末句是回接前文动机的编辑解释，不是额外完成的实验
- 焦点与取舍：从一般普遍性转向复用来源，能更紧回收P2.S7；这会改变论文贡献重心，不仅换一个连接词
- 选择条件：只有研究问题和后续分析确实以继承/复用为中心时采用；若仍以工具实用能力为中心，V07更贴近源的双重贡献，不应为新颖表达强行套V08

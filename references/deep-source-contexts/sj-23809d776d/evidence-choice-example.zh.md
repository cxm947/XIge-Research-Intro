# TFA选证位置实例：挑战统计、小例与组件消融

这是一张现行[选证与解释量](../../select-evidence-and-length.md#4-长度由未完成的解释职责决定)的可选应用例，不增加通用规则。仅当当前稿件正要决定一个具体例子／消融是否保留或前移时使用；A、B、C不是三项必备材料，也不要求三种落点齐全。

来源：[Dinghao Liu, Shouling Ji, Kangjie Lu, Qinming He. Improving Indirect-Call Analysis in LLVM with Type and Data-Flow Co-Analysis. USENIX Security 2024](https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-improving.pdf)。完整引言在PDF 2–4页／5895–5897页；必要上下文见下列逐项链接。共同署名不证明个人执笔或意图。原[完整引言图](../../intro-source-maps/sj-23809d776d.md)继续提供全章上下文；本卡只分析三个取舍。

## 三处可核位置及候选句

以下各处先标出可观察的源文安排，再给编辑候选；候选不是源文引文，也不是原作者选择动机的陈述。A、B、C不是要求同时添加的三句话。

### A. 挑战处：保留小群体与大负担之间的关系

**源文实际位置**：[5896页](https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-improving.pdf#page=3)左栏第一完整段，现有图P4；前接P3对近邻有效能力的解释，后接P5的共分析策略。

源引言直接报告这一关系。23%指不涉及复合类型的icall调用点数量占比；77%指其候选目标负担份额，不是运行次数、运行时间或唯一函数占比。论文未给这组比例的原始分组计数及明确配置／候选集统计阶段，因此这里核验的是源报告及其论证用途，不是独立重算；也不将该比例擅自匹配到§6.1的某项Linux配置或某轮结果。

**编辑候选及位置**：保留在挑战建立处；这对应源文现有位置，不是前移正文发现。


Although MLTA refines many calls, icalls that do not involve composite types make up 23% of icalls but account for 77% of candidate targets in the evaluated Linux kernel.

**为什么此处值得留。** 前文若强调近邻已覆盖常见情形，读者自然可能把剩余看成低收益边角。这里的两侧不是两个并列成绩，而是把“调用点数量占比”与“候选目标负担”分开。删成“some calls remain difficult”仍有gap，却丢掉为什么值得解决它；只留小比例，甚至可能强化边角问题印象。数值服务一个反驳，而非给背景增加权威感。

**何时可省。** 若邻段已用同一任务、同一条件的后果证明剩余重要，精确百分比可后移，只保留“残余集中承载负担”的关系；若本稿没有这种集中现象，则不能借本例的少数／多数修辞。一次不相容的统计拼接也不能承担这种反驳。

**尚未解决什么。** 负担大说明值得研究，不单独说明应采用哪种新方法。不能直接跳到“therefore, co-analysis”而略掉可用信息为何互补。

### B. 设计处：仅在“互补”仍像口号时前移一个正面能力例

**源文实际位置**：[5897页](https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-improving.pdf#page=4)§2.1与Figure 1；[5898页](https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-improving.pdf#page=5)§2.3第二段。它本来不在Introduction。引言P5已交策略及输入—图—后续分析关系。

**编辑候选及位置**：只在方案理由尚不清楚时前移；这是编辑备选，源引言未采用。在图中函数已简称f1–f4且变量s1已定义的说明环境下使用：

For the illustrated call, two-layer type matching retains f1 and f3, while data-flow analysis restricted to s1 retains f1 and f2; intersecting these sets leaves f1.

**为什么此处可能值得留。** 它保留两类分析各自的正面能力，并让“组合”成为排除不同无关项的可见关系。相比只写“type analysis is insufficient”，它能解释为什么不是简单替换旧法。与A不同，它建立的是路线可行性，不是残余问题的重要性。

**为什么原文留后文也成立。** 当方案段已经把互补信息及消费关系说清，额外例子不再补关键推断。前移会要求读者先理解对象、字段、指针和代号；若这些成本超过当前缺失关系，保留自然语言机制说明，让实例留背景节更经济。删除数字例不等于删除设计理由。

**反条件。** 若两条路线删去同一批候选，或一条单独已经给出所需答案，该见证不能支持组合必要性。单次交集也不证明迭代必要；循环仍须有真实新增信息。正文另有同类共分析近邻，不能把这一小例当今日新颖性的证据。

**附带校验。** 源§2.1有“50%”措辞；当前例子的候选集变化和误报计数须分开，本文改用显式集合关系，不借那个百分比推出未经澄清的误报率结论。这不是本卡主结论。

### C. 评价处：仅在需要归因时前移消融；通常不让它替代主任务答案

**源文实际位置**：[5906页](https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-improving.pdf#page=13)§6.4.1首段及跨栏续文；引言P6已给类型问题的后果，P7给修复职责，P8及C3则承担总体评价。§6.3.2和§6.4.2须连读以限制安全性用语。

**编辑候选及位置**：通常保留在评价正文；若引言中某项贡献确实缺少对恢复组件的归因，也可前移到相应技术贡献或评价位置，不限于最后一项：

In the O0 Linux trace evaluation, TFA had 879 false negatives with type recovery disabled; enabling recovery eliminated the observed misses caused by broken struct types.

879是关闭恢复后的总漏报数，不是新增量，也不是已修复量。该小节未单独列出可供相减的O0恢复后总数；不得算出“修复879个”。检测使用采集并筛选后的轨迹，不是全部可能执行。

**为什么默认留评价更合适。** 消融回答“改善由哪一项处理带来”，并不自动回答整个系统对实际任务有什么价值。若引言已有明确、可信的因果解释和总体结果，把组件归因留后文，论证并未因此缺一环；前移它会占用交代主要所得及可用范围的位置。

**何时值得前移。** 当恢复组件本身是核心研究所得，或读者有充分理由怀疑收益只是来自其他同步变化，此对照能补上归因，而非装饰结果。必须让环境和被关闭的处理靠近结果，且不能改写成全程序、全输入的绝对保证。

**不可省的内容。** 可以省掉消融计数，不能为了简短把“没有新增漏报”升级为“没有漏报”，也不能把一类原因的修复扩成所有原因。这里应缩窄主张的范围，不另堆防御性免责声明。

## 怎样接回当前稿件

A所示“少数对象仍承担大部分候选负担”已在原TFA选读卡中，不是新的通用原则。本卡的增量是与B、C的“不前移”并置：证据有多具体，不决定它是否应进入引言；须看删移后哪个判断失去根据。

沿用作者已定框架：A可服务一个实际应用挑战；B只有在方案理由尚不充分时才前移；C通常留评价正文，仅当前贡献项确需它回答本项问题时才前移，可在技术贡献或评价项。不据源文布局强改框架，也不把方案内部负担硬造为独立应用挑战。

此处源报告、可观察的篇章位置与编辑备选已经分开。候选及反条件是编辑解释，不是个人写作意图、今日新颖性结论或经新稿实验确认的写作收益。

# 具体成句案例：源文理解→固定内容→表达选择

这些是用真实来源的研究事实做的小范围编辑演示，不是目标论文改稿，不是原作者修订，也没有证明编辑稿优于原文。原文只给短摘及可回查位置，英文备选均明确为编辑文本。每组先固定同一命题，再比较3种实际可读表达，避免把抽象槽位当成成稿。

## 1. AsgLDP：同一系统名保持主题，准确区分两种估计对象

来源：[IEEE TIFS 2020作者托管版](https://nesa.zju.edu.cn/download/AsgLDP%20Collecting%20and%20Generating%20Decentralized%20Attributed%20Graphs%20with%20Local%20Differential%20Privacy.pdf)，Introduction P4.S1–3，物理p.2；[完整引言图](intro-source-maps/sj-dc32e376bc.md)。

### 原文是什么，前后文做什么

原S1刚说AsgLDP以精心设计的噪声收集局部图结构和节点属性，并满足LDP。目标S2以Then、it继续，以“computes the unbiased degree distribution”和另一并列谓语分别交代原图度分布、节点属性联合分布。S3继续以AsgLDP为主语，基于已收聚合信息构造seed图并优化。原文没有让每一步产物都升为下一句主语。

固定内容：AsgLDP随后计算原图的无偏度分布，估计节点属性的联合分布。两对象、compute／estimate的动作区别和顺序标记保留；本句不新增隐私保证或应用性能。

### 三种编辑表达

A. It then computes the unbiased degree distribution of the original graph and estimates the joint distribution of node attributes.

B. AsgLDP then computes the original graph’s unbiased degree distribution and estimates the joint distribution of its node attributes.

C. The next step computes the unbiased degree distribution of the original graph and estimates the joint distribution of node attributes.

### 在这个邻句位置怎样选

选择A：上一句只有AsgLDP这个清晰主体，it回指轻便；两个具体谓语把读者带到新产物，不必重介绍系统。B在两句之间插入了另一系统／组件后更有用，否则重复专名无额外收益。C适合前文已在概述阶段且要强调步骤，但把主题从系统移到步骤，下一句再回AsgLDP会多一次轻微切换。

保留了原有两个输出及不同计算动作；仅移动Then并平顺词序，不因更短把joint distribution缩成attributes，也不把unbiased同时套到属性联合分布。若改成“Aggregate information produces an unbiased graph”，就改了对象、属性和动作，不是保义替代。

源习惯教的是：系统名／it维持话题、compute与estimate精确推进产物、原图／属性限定贴近各自对象。不是规定学术句必须不断更换主语。

## 2. VERIFI：把“指标可能不变”还是“少数退出情境”先交给读者

来源：[arXiv:2205.12709v1](https://arxiv.org/pdf/2205.12709v1#page=2)，Introduction P3.S4–6；[完整引言图](intro-source-maps/sj-1b6614ac62.md)。

### 原文是什么，前后文做什么

S4刚提出一个自然验证路线：传统机器遗忘可观察模型在删除数据或额外后门数据上的表现。S5首先转换到FL并说“accuracy and loss may hardly change”，随后when给一个或少数参与者退出，最后owing-to给其他参与者贡献。S6另讲后门验证带来的安全副作用，不是S5指标不变的原因。

固定内容：在FL中，仅一个或少数参与者离开时，准确率和损失可能几乎不变，原因是其他参与者的贡献。保留可能性、退出规模、两个指标和原因。

### 三种编辑表达

A. In FL, accuracy and loss may remain almost unchanged when only one or a few participants leave, owing to contributions from the others.

B. When only one or a few participants leave an FL system, accuracy and loss may remain almost unchanged owing to contributions from the others.

C. Contributions from the other participants may leave accuracy and loss almost unchanged when only one or a few participants leave an FL system.

### 在这个邻句位置怎样选

选择A：上一句刚让读者期待性能能验证遗忘，本句先交“可能不变”最直接地回答这一期待，然后立即补其适用条件和原因。B同样保义，但读者先处理退出情境；若上一段正在比较少数与大量退出，它更合适。C把贡献来源升为主语，适合前句已经解释各方如何共同影响模型的语境；在当前S4之后会稍迟才出现读者最关心的指标判断。

三种都保留任务层含义，不加“验证因此绝不可能”，也不把几乎不变写成严格相等。没有通过删掉退出条件来换短句。这里篇幅不是选择胜负，关键是跟前句的期待怎样相接。

源习惯教的是：常见may remain、when、owing to已经足以承载精确而有力的转折。条件前置／后置是真实编辑选择，不能把拟采用的顺序说成原文顺序。

## 3. Tacoma：先给总体评价答案，再留一个有任务意义的成果锚点

来源：[ISSTA 2024 camera-ready版](https://users.cs.northwestern.edu/~ychen/Papers/issta24main-p723-CameraReady.pdf)，Introduction P7及C3，物理p.2；[完整引言图](intro-source-maps/sj-c153987a94.md)。评价成句另参考[FreeEagle v1 C3](https://arxiv.org/pdf/2302.14500v1#page=2)的评价动作＋demonstrating答案结构。

### 原文是什么，前后文做什么

原Tacoma C3是三句：评价三个主流浏览器；比较分支覆盖与unique crashes；报告32个以前未知bug，其中10个获CVE。前P7已展开覆盖和真实漏洞实例，贡献可以总结。原文对范围、比较、发现状态各给一句，不是作者只写了“做了实验”。

本例的编辑目标明确缩到：在不复述前文覆盖比较的情况下，让末评价项突出浏览器漏洞发现能力和实际新发现。固定内容为三个浏览器范围、漏洞发现有效性、32个以前未知bug及10个CVE子集。覆盖／unique-crash比较从这一局部移出，仍留在前P7，不假装所有源信息在一句中都保留。

### 三种编辑表达

A. We evaluate Tacoma on Chromium, Safari, and Firefox, demonstrating its effectiveness in browser vulnerability discovery. Tacoma has detected 32 previously unknown bugs, 10 of which have been assigned CVEs.

B. Our evaluation on Chromium, Safari, and Firefox demonstrates Tacoma’s effectiveness in discovering browser vulnerabilities, with 32 previously unknown bugs detected, 10 of which have been assigned CVEs.

C. Experiments on Chromium, Safari, and Firefox demonstrate Tacoma’s effectiveness in browser vulnerability discovery. The system has detected 32 previously unknown bugs, including 10 that have been assigned CVEs.

### 在这个邻句位置怎样选

选择A：评价动作开头承接方案／贡献序列，demonstrating立即给总体任务答案；第二句用具体系统作主语交发现与确认子集，读者不用自己从组件指标推断研究价值。B更紧，但with尾部同时容纳数量和状态，语义负担更集中；若前文没有讲过发现状态，A更清楚。C让实验而非作者作主语，适合需要换一个自然证据起点时，但范围与成果较重时仍有两句负担。

这里“effectiveness in browser vulnerability discovery”是根据真实结果作出的编辑概括，不是Tacoma原C3逐字用语；借FreeEagle的是评价句结构，不借其事实或比较对象。原P7的覆盖比较仍存在，因此删掉末项重复的两个代理表现不会让整篇失去比较；如果新稿前面并未讲比较，则应重新判断是否需要保留，而不能套此压缩。

保留32／10是因为它们回答实际发现及外部状态；没有换成生成器速度或某个最大覆盖数。也没有把10个CVE写成32个都已确认／修复。这个源事实只示范怎样挑有任务意义的证据，不成为其他论文应填的数字或句长。

## 4. VFL-Hijack：让有限控制资源与预测后果一起进入前景

来源：[arXiv:2212.00322v2，2024-02-16](https://arxiv.org/pdf/2212.00322v2#page=2)，§1.1结果段，物理p.2；[完整引言图](intro-source-maps/sj-e3479d788f.md)。本例使用这一版本引言中的作者报告。

### 原文是什么，前后文做什么

前文已解释少特征方的预测影响可能不足，并引出投毒增强。结果段先报告攻击与投毒结合的效果，再以10%的特征份额、近90%的攻击成功率和二分类任务给出实例。后文转向防御及正常任务性能代价。

固定内容：这组结果来自攻击与投毒阶段的结合；一方只掌握10%的特征，在二分类器上仍能取得近90%的攻击成功率。以下三种目标句都接在已交代投毒组合的前一句之后。

### 三种编辑表达

A. Even with control over only 10% of the features, one participant can achieve an attack success rate of nearly 90% on a binary classifier.

B. One participant can achieve an attack success rate of nearly 90% on a binary classifier while controlling only 10% of the features.

C. An attack success rate of nearly 90% can be achieved on a binary classifier when one participant controls only 10% of the features.

### 在这个邻句位置怎样选

选择A：前文刚提出少特征方的能力障碍，句首的有限控制份额与后面的攻击效果一起给出答案。B先交攻击者能做到什么，适合前句仍围绕其行动展开时；C先交成功率，适合前文正在比较结果表现时。三种表达保留同一结果关系，选择取决于这个位置要突出的内容。

这里10%本身承载研究价值：它让读者看到，局部控制份额很小，联合预测仍会受到强烈影响。二分类保留为该实例的任务对象；投毒组合由紧邻前句承担，具体数据集、知识设置和实验配置由正文评价及来源记录保留。这个正向编辑选择是把有价值的条件与任务结果写在一起，让实验过程在需要解释它的位置展开。它是本例的编辑启发，不是原作者动机自述或普遍写作效果结论。

## 5. 由这些案例回到运行操作

1. 读前一句、目标句和后一句，知道此刻读者等哪个答案
2. 固定本句要保留的事实；如果要删内容，先说明它移去哪或为何不再需要，而不是冒称同义压缩
3. 通常直接从适用选项写出自然表达；当前确需比较或用户要求备选时，再展开有实质差异的表达，使用真实学术动宾搭配和适用的主从关系
4. 按本稿邻句选定表达；进行了备选比较时，只说明影响选择的焦点／回指／负担差异，不为未生成的备选补拒绝理由
5. 连读成段，再核查任务、机制与评价仍然是同一对象

这些操作留下必要编辑理由；写给论文读者的只有最终自然正文。

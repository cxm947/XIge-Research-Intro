# 常规学术英文速查

按当前句意查一组即可。英文示例均为原创；期刊格式以目标venue为准。源文语境及主源链接附在各项后；投稿前另核目标venue当前指南，不能把某份历史手册或单一会议页面当作通用规范。

## 内容导航

- [1. e.g.、i.e.、et al.](#section-1)
- [2. state-of-the-art与SOTA](#section-2)
- [3. 五个常用关键词怎样选](#section-3)
- [4. 评价贡献的常用搭配](#section-4)

<a id="section-1"></a>
## 1. e.g.、i.e.、et al.

**e.g.＝for example：举例，本身不表示穷尽。** 括号内适合紧凑表达，正文也可自然用such as或including。

- We evaluate [M] on several [objects] (e.g., [A] and [B]).
- We evaluate [M] on several [objects], including [A] and [B].
- We evaluate [M] on several [objects], such as [A] and [B].

JWBinder用e.g.列AST/PDG等特征，是对类别的例示。[§1, p.2](https://arxiv.org/pdf/2310.17304v2#page=2)

**i.e.＝that is：精确解释或重述。** 它后面给前项的含义；e.g.后面给前项的例子。

- [M] requires [R], i.e., [precise restatement of R].
- [M] requires [R], that is, [precise restatement of R].
- Here, [R] refers to [precise definition].

第三式适合本句只负责定义。FirmRCA用i.e.解释访问类型为读或写。[§1, p.2](https://arxiv.org/pdf/2410.18483v1#page=2)

**et al.＝and others：省略其他作者。** et后无句点，al.后有句点；作者组作主语通常接复数动词。

- [Surname] et al. [citation] show that [P].
- [Surname] and colleagues [citation] show that [P].
- Prior work [citation] shows that [P].

前两式突出作者，第三式突出已有研究。作者后是否有逗号取决于句法和引用格式：作者—年份式中年份前可以有逗号，作者与谓语之间通常没有。

### 体例的几个真实差异

- Chicago正式散文通常把e.g./i.e.留在括号、注释或表格，正文写全词；它们通常后接逗号。[官方说明](https://cmosshoptalk.com/2023/04/11/i-e-e-g-etc/)
- APA第7版指南要求e.g./i.e.放括号，拉丁缩写不斜体；et al.可以用于叙述式引文，不能把括号限制套给它。[APA作者原件的大学存档，第2页](https://intranet.shsu.edu/centers/academic-success-center/abbreviations-guide.pdf#page=2)
- IEEE手册讨论插入性e.g./i.e.与逗号，也在正文使用i.e.；IEEE当前Reference Guide另规定文内三名及以上作者用et al.，文末列表按另一套规则。[手册入口](https://journals.ieeeauthorcenter.ieee.org/your-role-in-article-production/ieee-editorial-style-manual/)、[引用指南的References in Text](https://docs.google.com/document/d/e/2PACX-1vSBoV_hTIURPZKtQkxI6bAONJtjyDLxQIUvCHi-XPzD8NKLcxRfZrpvQLFrjWZ3M6FFR_Obau3R-t63/pub)
- ACM Hypertext2026的具体venue指南要求et al.斜体；这不是全部ACM的统一声明。[Author Names](https://ht.acm.org/ht2026/open-calls/submission-instructions/reference-styles-for-acm-papers/)

因此，先把句意写清，再按目标模板统一位置、字体、作者截断数和标点。SCI不是统一的英语体例。

<a id="section-2"></a>
## 2. state-of-the-art与SOTA

常见搭配：

- state-of-the-art methods / systems / performance：作定语，通常带连字符
- the state of the art：名词短语，如advance the state of the art
- state-of-the-art (SOTA) methods：需要反复使用缩写时首次展开，随后用SOTA methods

这些形式见[Cambridge形容词词条](https://dictionary.cambridge.org/us/dictionary/english/state-of-the-art?topic=modern-and-fashionable)和[IEEE2024版手册附录，PDF第34页](https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE-Editorial-Style-Manual-for-Authors.pdf#page=34)。IEEE要求摘要和正文分别在首次出现时定义缩写；具体规则按venue处理。

可选表达：

- We compare [M] with state-of-the-art methods for [task].
- We compare [M] with [A] and [B], two state-of-the-art methods for [task].
- [M] achieves state-of-the-art performance on [benchmark] in terms of [metric].

前两句介绍对手，第三句是领先结果，主张不同。只出现一次时写全称很自然；只想介绍合适对手时也可用recent/representative methods或直接点名。TextDefense首次展开SOTA，JWBinder直接用完整词组，二者都可作为正常写法。[TextDefense §1, p.1](https://arxiv.org/pdf/2302.05892v1#page=1)、[JWBinder §1, p.4](https://arxiv.org/pdf/2310.17304v2#page=4)

<a id="section-3"></a>
## 3. 五个常用关键词怎样选

以下是语境选择，不是五种互斥的证据等级。源文中observation与insight可以回指同一关系；关键是当前句在做什么。

### intuition：直观上为什么值得尝试这一思路

- The intuition behind our approach is that [P].
- Our approach is guided by the intuition that [P].
- Our approach follows the intuition that [P].

FirmRCA以具体内存访问可辅助逆向执行/别名处理作为intuition，帮助读者理解选择运行信息的理由。[§1, p.2](https://arxiv.org/pdf/2410.18483v1#page=2)

### insight：哪项关键理解改变了设计

- Our key insight is that [P].
- The key insight underlying our approach is that [P].
- Our approach rests on the insight that [P].

FirmRCA以指令对根因贡献不同这一insight导出排名；JWBinder用insight衔接共有性质与SSR。[FirmRCA §1, p.2](https://arxiv.org/pdf/2410.18483v1#page=2)、[JWBinder §1, p.3](https://arxiv.org/pdf/2310.17304v2#page=3)

### observation：考察中注意到的现象或可核性质

- We observe that [P] in [C].
- In [C], we observe that [P].
- Our observations in [C] show that [P].

观察可来自实验、实例或代码/系统检查。JWBinder先以observation引入共有性质，再用insight说明其设计价值，这正是二词可重叠的例子。[§1, p.3](https://arxiv.org/pdf/2310.17304v2#page=3)

### rationale：为什么作出这个具体选择

- We choose [D] because [P].
- The rationale for choosing [D] is that [P].
- [P], which is why we choose [D].

JWBinder用rationale解释为什么按JavaScript语法构造的IPDG可回译为JavaScript。[§1, p.3](https://arxiv.org/pdf/2310.17304v2#page=3)

### motivation：什么需要或问题促使研究展开

- This study is motivated by [need or problem].
- [Need or problem] motivates this study.
- We undertake this study in response to [need or problem].

MINER用长且有效请求序列的需要，说明改进构造与生成的动机；这里引用相邻方法上下文，不把该小标题算作引言内容。[§3.1, p.5](https://arxiv.org/pdf/2303.02545v1#page=5)

也可以直接写because、we find、our approach is to。先把关系讲清，再决定是否需要术语标签。

<a id="section-4"></a>
## 4. 评价贡献的常用搭配

### conduct / perform / carry out experiments

- We conduct extensive experiments to evaluate [M].
- We perform extensive experiments to evaluate [M].
- We carry out extensive experiments to evaluate [M].
- We conduct an extensive evaluation of [M].

前三式说明同一实验动作；第四式概括整体评价，可能还包括其他分析。这里汇总多项实验用experiments；单项实验可写an experiment。an extensive evaluation指一次完整评价。extensive强调范围/工作量，comprehensive强调覆盖关心的方面。FreeEagle与JWBinder分别提供自然用例。[FreeEagle §1, p.2](https://arxiv.org/pdf/2302.14500v1#page=2)、[JWBinder §1, p.4](https://arxiv.org/pdf/2310.17304v2#page=4)

### evaluate：对象＋所需范围

- We evaluate [M] on [datasets or benchmarks].
- We evaluate [M] across [model architectures or settings].
- We evaluate [M] under [experimental conditions].
- We evaluate the effectiveness of [M] in [task or setting].

介词分别突出材料、变化维度、条件、任务；可以组合或承接前文。FreeEagle把数据和架构同放on之后，因此across architectures是可用选择，并不意味着on architectures错误。[§1, p.2](https://arxiv.org/pdf/2302.14500v1#page=2)

### compare / compared with：两端对应

- We compare [M] with [B] on [benchmark].
- Compared with [B], [M] achieves [result].
- The [metric] of [M] is [V], compared with [Vb] for [B].

方法与方法、指标与指标对应。with适合技术比较，to也自然出现；Chicago官方承认实际用法并不总严格细分。[第18版问答](https://www.chicagomanualofstyle.org/qanda/data/faq/topics/Usage/faq0336.html)。源中Cert-RNN用with，FirmRCA用to。[Cert-RNN §1, p.2](https://nesa.zju.edu.cn/download/dty_pdf_cert_rnn.pdf#page=2)、[FirmRCA §1, p.2](https://arxiv.org/pdf/2410.18483v1#page=2)

### outperform：直接接比较对象

- [M] outperforms [B] on [benchmark].
- On [benchmark], [M] outperforms [B].
- [M] outperforms [B] in terms of [metric or capability].

前两式换语序，第三式突出比较轴。outperform在此为及物动词；需要than时可写performs better than。[Cambridge词条](https://dictionary.cambridge.org/dictionary/english/outperform)。FreeEagle保留some限定对手集合，Cert-RNN用in terms of给出精度/效率两轴。[FreeEagle §1, p.2](https://arxiv.org/pdf/2302.14500v1#page=2)、[Cert-RNN §1, pp.1–2](https://nesa.zju.edu.cn/download/dty_pdf_cert_rnn.pdf#page=1)

### demonstrate / show：给评价结论

- The results demonstrate that [M] [supported capability].
- Our evaluation demonstrates the effectiveness of [M] in [task].
- Experiments show that [M] [supported capability].
- Our evaluation demonstrates both [capability A] and [capability B].

demonstrate可接that从句或名词短语。[Cambridge词条](https://dictionary.cambridge.org/dictionary/english/demonstrate)。前文已解释的effectiveness、robustness、efficiency可以直接归纳；具体数值按需要补充。Cert-RNN和FreeEagle都提供这种正常用法。[Cert-RNN §1, p.2](https://nesa.zju.edu.cn/download/dty_pdf_cert_rnn.pdf#page=2)、[FreeEagle §1, p.2](https://arxiv.org/pdf/2302.14500v1#page=2)

### 自然组合

> We conduct extensive experiments on [D] to evaluate [M] against [B]. The results demonstrate [principal task-level conclusion], with [the most informative comparison or result].

或：

> Extensive experiments on [D] show that [M] outperforms [B] in terms of [K].

范围、比较与结论按实际内容取舍。significantly若指统计显著，对应统计检验；若只强调幅度，可给实际数值或用substantially。其他事实/范围问题统一在[修改与复核](revise-and-review.md)检查。

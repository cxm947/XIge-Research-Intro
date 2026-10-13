# 段落选择的来源链接

沿当前段落要作的一个选择查来源。下面区分原文可观察的选择、可迁移的编辑操作和不适用条件；原创模板与同职责变体不声称出自源文。121项 corpus 身份保持在[原目录](corpus-index.json)，高层用途在[来源地图](research-choice-evidence-map.md)，本次完整逐句材料在[句级图索引](intro-source-index.md)。补充近邻不混入原121项计数。

## 1 背景入口与价值

- [FirmSec](research-choice-evidence-map.md#firmsec)，ISSTA 2022作者稿§1：IoT→固件复用→版本及漏洞判断。迁移为让背景所选事实解释任务粒度；不把所有研究都从IoT起笔
- [FirmRCA](research-choice-evidence-map.md#firmrca)，arXiv:2410.18483v1 §1：固件用途→fuzzing后崩溃→根因定位。较宽的平台入口有效，是因为同一研究活动连续收窄
- [EMS](research-choice-evidence-map.md#ems)，NDSS 2022作者稿§I：从变异模糊测试及效率目标进入历史复用。上位领域可以贴近任务；无需先介绍整个产业
- [价值选择与读者判断](value-and-reader-decisions.md)及[跨学科来源](discipline-sources.md)：属性—任务后果—价值用于选择主次；读者已有知识用于选择必要前提。营销参照不能让作者挑稳赢对手，认知研究也不支持“专家一律少解释”

## 2 更强答案与剩余关系

- [Diff-ID](research-choice-evidence-map.md#diff-id)，arXiv:2303.18174v1 §I：逐级引入更强图像和视频路线，保留其能力及条件，再解释同一任务的剩余关系。迁移为升级近邻后更新主张，不能仅替换方法名
- [FreeEagle](research-choice-evidence-map.md#freeeagle)，arXiv:2302.14500v1 §1：进入已有无数据方法DF-TND。迁移为主动检查能反驳旧gap的强方案；不能停在最容易批评的一类
- [JWBinder](research-choice-evidence-map.md#jwbinder)，arXiv:2310.17304v2 §1：静态检测的真实用途与跨语言交互关系，并考虑Wasm替代。迁移为先保留合理直接路线，再解释为何选择重构并复用已有检测能力

<a id="median-smoothing"></a>
### 补充近邻：中位数平滑

[Ping-yeh Chiang, Michael J. Curry, Ahmed Abdelkader, Aounon Kumar, John Dickerson, Tom Goldstein. Detection as Regression: Certified Object Detection by Median Smoothing. arXiv:2007.03730v4, 2022-02-25](https://arxiv.org/abs/2007.03730v4)，[PDF §§4–5、Algorithm 1](https://arxiv.org/pdf/2007.03730v4)。

已有逐坐标分位数平滑及次序统计／二项置信界，应作为MeTFA定位中的可用基础；之后仍需说明归因构造、中央分数选择及所要检验的解释性质。不要把获得通用有限样本推断重新设为未解决挑战，也不要把目标检测认证自动转成解释排序或语义忠实度保证。引用这一关系时按所用版本核读相关节；此卡沿用既有主源读取记录，不声称每次使用技能都会重读原文。

<a id="echo"></a>
### 补充近邻：Echo的恢复与行为观察

[Dennis Giese and Guevara Noubir. Amazon Echo Dot or the Reverberating Secrets of IoT Devices. WiSec 2021. DOI:10.1145/3448300.3467820](https://doi.org/10.1145/3448300.3467820)，[作者稿](https://dontvacuum.me/papers/ACMWisec-2021/Amazon_Echo_Forensics_for_WISEC_final.pdf)，§§5.3–5.4、§6.2。

该来源既研究重置后数据残留，也记录所购设备的重置状态，并说明无法询问原所有者。另一样本的问卷可以增加自报认知与实践认识，不能用来解释这些所有者为何未重置。让同一来源的相关能力完整进入后续贡献轴，再选择尚待研究的关系。

## 3 要求、机制与所得

- [UVSCAN](research-choice-evidence-map.md#uvscan) §1：先解释检测需要规则，再说明文档分散、规则提取及实现检查如何会合。继承能力已经满足要求时直接采用，不重新制造障碍
- [FirmSec](research-choice-evidence-map.md#firmsec) §1：版本粒度由漏洞判断决定；让任务价值同时选择技术粒度与结果，不能仅说更细或规模更大
- [CPscan](research-choice-evidence-map.md#cpscan) §1：定位删除之后还需判断危险；[JWBinder](research-choice-evidence-map.md#jwbinder) §1：识别交互后还需统一语义。两者说明真实残余关系，不证明任何系统都要两个挑战
- [HashVFL](research-choice-evidence-map.md#hashvfl) §I与[SUB-PLAY](research-choice-evidence-map.md#sub-play) §1：选定表示或分解后才出现的技术负担应在设计后解释
- [MeTFA](research-choice-evidence-map.md#metfa)，arXiv:2209.01782v1 §§3.1–4.2、§5.3.1：二项推断、置信区间所定义的中央分数平均、估计量性质与外部噪声下的经验表现是有联系但不同的论证。中央子集筛去极端分数的理由可以解释选择，不能虚构直接中位数基线已被击败
- [IoT Re-using](research-choice-evidence-map.md#iot) §§III–VI：问卷、固件、配置设备及风险模式分别提供认知、代码、恢复及结构风险层面的证据。共同研究问题不自动建立共同样本、分母或因果解释

## 4 最后评价贡献

[Diff-ID](research-choice-evidence-map.md#diff-id)的紧凑评价、[FreeEagle](research-choice-evidence-map.md#freeeagle)的范围与有界比较、[JWBinder](research-choice-evidence-map.md#jwbinder)的效能及机制分析、[EMS](research-choice-evidence-map.md#ems)的多项独立认识，提供不同收束取舍。先选这篇论文的主要答案，再保留读懂它不可缺的结果；源例较长不构成堆齐本稿所有证据的理由。更多布局和原创对照见[收束源例](closing-and-contributions.md)。

## 5 句式与英文来源怎样用

[句式库](sentence-realizations.md)每组“源锚”直接进入完整句级图中的已核单元；有些来源仅作对照边界，会明确标注。P/S及B/C是分析者定位标签，不是原文编号；保留完整父段路径，按[坐标表](intro-coordinate-map.json)解析，不能从高层卡的论文标题推定精细坐标。原文选择支撑职责与关系，组内3–4种英文形式是原创保义实现。

[英文惯例](english-conventions.md)在各项后链接IEEE、Chicago、APA等规范及源例。规范的语义、语法和某venue的排版要求分开使用；投稿前核验当前目标指南。研究论文源例可以展示正常表达，但其技术正确性、文法或风格不因已发表而免于判断。

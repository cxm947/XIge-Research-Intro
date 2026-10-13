# Learned Provenance Baseline：完整引言句级图

- 来源身份：sj-beba53e0f9
- 指定版本：Official ICML 2025 PMLR 267 full proceedings PDF from publisher repository, 15 physical pages
- 指定原文：https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25k/zhu25k.pdf
- 实际读取原文：https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25k/zhu25k.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#learned-provenance-baseline) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

- sourceID: sj-beba53e0f9
- 版本：Official ICML 2025 PMLR 267 full proceedings PDF from publisher repository, 15 physical pages
- 精确索引主源：https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25k/zhu25k.pdf
- 2026-10-04读取证据：本地完整 PDF（15 物理页）及 raw/layout 提取；SHA-256 f460c0d690fa4cb1487a6f4b440a7bcdf275edfa6988bde04fc80543d2b4b12a
- 引言定位：物理 PDF 第 1–2 页；页锚以原 URL 后加 #page=N 定位
- 状态：available=true；full_introduction_reread=true；sentence_annotated=true；awaiting=false；unavailable=false
- 归属：以下为本论文的内容组织选择，不据共著名单推断任何个人执笔；“选择解释”均为编辑推断，不是作者自述。句级内容为释义，非源句摘录。
- 读法：P 表示原文论证段/贡献项，S 按该段源句顺序。每句写“已知→新增｜前接关系｜后续回收”。篇章标题、脚注和图中文字不冒充正文句子。

## 连续论证与相邻正文核验
P1 解释provenance图和因果时序；P2 从实时入侵检测需求导出规模、丰富语义和新实体OOV代价；P3 从frequency database与learned storage获得去耦思路；P4 把事件嵌入→频率学习→正常基线→tag propagation连成检测路径；P5 以连续原型/评价段收尾，没有显式贡献列表。
补读§2.2 frequency baseline、§2.3 tag propagation、§2.4 C1–C5与§3方法（offline学习/online流式检测），以及§4评价设置。正文明确频率库不见过的新良性事件会低分，学得基线的价值包含泛化；tag propagation继承因果/时间顺序并聚合到路径，不是embedding自动解决一切。

## 逐句信息推进
### P1 图的表示与价值（p1）
<a id="p1"></a><a id="p1-s1"></a>P1.S1 未定位→PIDS利用provenance图进行威胁建模｜领域定位｜方法对象
<a id="p1-s2"></a>P1.S2 已知图→审计日志中有因果链接的OS行为｜数据来源｜§2.1
<a id="p1-s3"></a>P1.S3 已知行为→节点实体/边交互并给进程读文件例｜表示具体化｜事件解耦
<a id="p1-s4"></a>P1.S4 已知边→加时间信息可按时间追踪｜补时序维度｜tag propagation
<a id="p1-s5"></a>P1.S5 已知时序→过去行动才影响后续，提供分析预测结构｜价值解释｜保持因果顺序
### P2 任务约束与障碍（p1）
<a id="p2"></a><a id="p2-s1"></a>P2.S1 已知检测→需要立即响应｜成功判据｜实时目标
<a id="p2-s2"></a>P2.S2 已知图价值→有若干制约实际效能的挑战｜转折入口｜S3–7
<a id="p2-s3"></a>P2.S3 已知图→日志持续增长形成巨大、高度连接的图｜规模根因｜learned storage
<a id="p2-s4"></a>P2.S4 已知复杂度→管理分析计算昂贵｜任务后果｜轻量模型
<a id="p2-s5"></a>P2.S5 已知丰富语义→理解有益但再增开销｜价值/代价同句｜保语义的去耦
<a id="p2-s6"></a>P2.S6 已知持续日志→实体关系常新增｜另一根因｜adaptive embedding
<a id="p2-s7"></a>P2.S7 已知新增→OOV伤表示准确与适应性｜技术后果｜normality shift
### P3 选已有构件而非忽略近邻（p1）
<a id="p3"></a><a id="p3-s1"></a>P3.S1 已知障碍→提出学习型异常检测｜总答｜§3
<a id="p3-s2"></a>P3.S2 已知任务→动态图异常检测对入侵场景重要｜局部定位｜baseline
<a id="p3-s3"></a>P3.S3 已知大图→现有frequency database记录各事件频率、可去耦｜承认已有能力｜§2.2
<a id="p3-s4"></a>P3.S4 已知数据库及learned storage→将图拆事件与频率｜设计选择来源｜P4输入
### P4 从事件到在线异常路径（p1–2）
<a id="p4"></a><a id="p4-s1"></a>P4.S1 已知事件→embedding向量作为轻量学习模型输入｜机制第一步｜§3.1
<a id="p4-s2"></a>P4.S2 已知模型→按出现频率学模式以应对动态行为｜目标｜§3.2
<a id="p4-s3"></a>P4.S3 已知动态→host行为变后旧正常模式难判新事件｜定义normality shift｜下一机制
<a id="p4-s4"></a>P4.S4 已知两动态难题→处理常见新实体/关系以兼顾OOV与shift｜能力响应｜adaptive embedding
<a id="p4-s5"></a>P4.S5 已知学习目标→向量频率分布形成正常基线｜定义中间产物｜online scoring
<a id="p4-s6"></a>P4.S6 已知基线→接tag propagation做实时检测｜使中间产物有去向｜§3.3
<a id="p4-s7"></a>P4.S7 已知路径检测→评价显示准确/适应性改善｜结果预告｜§4
### P5 连续收尾（p2）
<a id="p5"></a><a id="p5-s1"></a>P5.S1 已知设计→已构建含adaptive embedding的原型处理OOV/shift｜实现状态｜原型脚注
<a id="p5-s2"></a>P5.S2 已知原型→保语义上下文、轻量模型原生流式学习大图模式｜归纳关键共同能力｜§3
<a id="p5-s3"></a>P5.S3 已知学习→正常基线接tag propagation实时检测｜回收全链｜§3.3
<a id="p5-s4"></a>P5.S4 已知原型→大规模开放数据评价验证有效高效｜给证据范围｜§4
<a id="p5-s5"></a>P5.S5 已知结果→实时异常路径挖掘的准确适应性与应用潜力｜价值收束｜论文结论

## 选择解释（推断）
- 第一段花句子解释因果和时间并不是教科书装饰：后面去耦大图很容易让读者担心关系信息丢失，tag propagation必须接手这些信息。只抄“图大→embedding”会漏掉这个保留约束。
- P3把frequency database写成灵感和已有能力，不是假失败基线；真正的新良性行为误报理由被推迟到§2.2，说明引言的gap展开并不完全自足。借鉴时可前移该最必要的一句，但不能假称源引言已详细解释。
- P4明确给“频率分布→正常基线→传播检测”的中间产物去向，读者可判断学习不是为了嵌入而嵌入。
- P5与P4有相当重复，适合作为无条目式贡献收尾实例，同时应辨别重复成本，不能把重复五句都包装为不同贡献。

## 贡献篇幅条件
无显式Contributions标题/列表；最后连续5句承担原型、设计、集成、评估和意义，前段末已有一句结果预告。不能在统计中硬记“三项贡献”。若重组为条目，应承认这是编辑改写而非源事实；本文没有引言结果数字，不应杜撰量化缩句。

## 可点击主源页锚
[PDF p1](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25k/zhu25k.pdf#page=1) · [PDF p2](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25k/zhu25k.pdf#page=2)

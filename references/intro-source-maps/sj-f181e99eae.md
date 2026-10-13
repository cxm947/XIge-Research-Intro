# De-Health：完整引言句级图

- 来源身份：sj-f181e99eae
- 指定版本：Author-hosted final-format 12-page ICDE2020 Industry Track text, nine-author block
- 指定原文：https://nesa.zju.edu.cn/download/De-Health%20All%20Your%20Online%20Health%20Information%20Are%20Belong%20to%20Us.pdf
- 实际读取原文：https://nesa.zju.edu.cn/download/De-Health%20All%20Your%20Online%20Health%20Information%20Are%20Belong%20to%20Us.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#de-health) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [P8](#p8) · [C1](#c1) · [C2](#c2) · [C3](#c3)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

- sourceID: sj-f181e99eae
- 版本：Author-hosted final-format 12-page ICDE2020 Industry Track text, nine-author block
- 精确索引主源：https://nesa.zju.edu.cn/download/De-Health%20All%20Your%20Online%20Health%20Information%20Are%20Belong%20to%20Us.pdf
- 2026-10-04读取证据：本地完整 PDF（12 物理页）及 raw/layout 提取；SHA-256 5af11287ccc88ed8fe7be9e566a6e211225c2ae74142bf6da1362b7408ecf637
- 引言定位：物理 PDF 第 1–2 页；页锚以原 URL 后加 #page=N 定位
- 状态：available=true；full_introduction_reread=true；sentence_annotated=true；awaiting=false；unavailable=false
- 归属：以下为本论文的内容组织选择，不据共著名单推断任何个人执笔；“选择解释”均为编辑推断，不是作者自述。句级内容为释义，非源句摘录。
- 读法：P 表示原文论证段/贡献项，S 按该段源句顺序。每句写“已知→新增｜前接关系｜后续回收”。篇章标题、脚注和图中文字不冒充正文句子。

## 连续论证与相邻正文核验
P1在线健康服务普及；P2数据规模/共享价值；P3敏感性与保护缺口；P4结构、规模、威胁三差异限制传统结构化数据匿名；P5政策层的不足（历史源论述）；P6聚焦论坛；P7收集政策和同意背景；P8数据用途→两个问题：匿名记录映射到账号，账号链接真人；三贡献直接承载双阶段算法、数据评价和概念验证结果。
补读§II数据/feature extraction，§III图表示与closed/open-world定义、Top-K结构候选后精细分类，以及§V真实身份linkage的评估边界。两步去匿名算法和跨站身份链接是两级问题，不应混称同一准确率；347/2805为指定WebMD子集概念验证。只研究论文论证与总量，未进行任何个人查找/识别。HIPAA/服务政策内容是论文时点论述，未核验当前法律或当前条款，不作为现行法律指导。

## 逐句信息推进
### P1 服务价值（p1）
<a id="p1"></a><a id="p1-s1"></a>P1.S1 未定位→医疗从医院诊所延伸在线服务｜领域变化｜数据形成
<a id="p1-s2"></a>P1.S2 已知在线→快速增长、用户/记录巨大｜规模｜DA可扩展条件
<a id="p1-s3"></a>P1.S3 已知使用→2012/2013调查的上网诊断/用时/就医数｜历史实证｜现实价值
<a id="p1-s4"></a>P1.S4 已知趋势→每日在线医疗搜索用于就医前后理解的调查｜用途具体化｜健康数据含义
<a id="p1-s5"></a>P1.S5 已知证据→在线服务更重要｜合成价值｜P2
### P2 数据规模与共享（p1）
<a id="p2"></a><a id="p2-s1"></a>P2.S1 已知服务→服务过程积累健康数据｜从用途转研究对象｜privacy
<a id="p2-s2"></a>P2.S2 已知积累→WebMD 2014访客/浏览量｜规模实例｜评估平台
<a id="p2-s3"></a>P2.S3 已知另一平台→HB访问/注册/帖子总量｜第二对象实例｜评估平台
<a id="p2-s4"></a>P2.S4 已知数据→低成本大规模疾病/商业/政府分析价值促进共享传播｜收益与暴露路径｜后文两问题
### P3 隐私问题（p1）
<a id="p3"></a><a id="p3-s1"></a>P3.S1 已知数据价值→也含用户敏感细节｜转风险｜链接后果
<a id="p3-s2"></a>P3.S2 已知敏感→分享前应保护和遵政策｜规范需求｜S3
<a id="p3-s3"></a>P3.S3 已知需求→技术与政策两方面仍未解决｜双分析轴｜P4/P5
### P4 技术不匹配（p1）
<a id="p4"></a><a id="p4-s1"></a>P4.S1 已知匿名技术→多面向医院等正式来源的结构化数据｜近邻真实范围｜S2
<a id="p4-s2"></a>P4.S2 已知能力→暂不评其效果也难迁在线数据｜避免无据否定近邻｜三原因
S3(i) 已知两数据→结构化字段vs在线异构复杂｜第一条件差异｜feature extraction
S4(ii) 已知规模→传统小数据vs在线百万用户｜第二差异｜Top-K筛候选
S5(iii) 已知流通→结构化数据较可控、较少隐私妥协｜第三差异前半｜S6
<a id="p4-s6"></a>P4.S6 已知online开放→传播难控、对手可多手段及辅助信息｜第三差异后果｜auxiliary graph/linkage
### P5 政策视角（p1–2）
<a id="p5"></a><a id="p5-s1"></a>P5.S1 已知政策问题→以HIPAA匿名后监管边界的历史源论述｜制度风险背景｜不直接迁移为现行法
<a id="p5-s2"></a>P5.S2 已知匿名要求→源论文称无具体技术指定｜执行缺口｜S3
<a id="p5-s3"></a>P5.S3 已知缺口→可能用naive匿名｜条件性后果｜pseudonym≠安全
### P6 研究范围（p2）
<a id="p6"></a><a id="p6-s1"></a>P6.S1 已知风险→研究以帮助用户/研究者/owner/policymaker理解｜目的｜privacy vulnerability
<a id="p6-s2"></a>P6.S2 已知online范围→聚焦WebMD/HB论坛生成数据｜限定对象｜数据集
<a id="p6-s3"></a>P6.S3 已知论坛→患者/医生Q&A、症状、用药等互动｜描述可分析行为与敏感性｜features
### P7 收集与同意背景（p2）
<a id="p7"></a><a id="p7-s1"></a>P7.S1 已知论坛→库中已有大量医疗记录｜接规模｜S2
<a id="p7-s2"></a>P7.S2 已知服务→政策声明收集联系/profile/医疗/交易/cookies等｜收集范围｜风险
<a id="p7-s3"></a>P7.S3 已知政策→使用需接受｜解释进入条件｜S4
<a id="p7-s4"></a>P7.S4 已知接受→HB历史policy的拒绝则勿用例｜具体依据｜非现行核验
<a id="p7-s5"></a>P7.S5 已知条件→使用意味着允许平台收集个人信息｜后果｜P8用途
### P8 两问题（p2）
<a id="p8"></a><a id="p8-s1"></a>P8.S1 已知所收信息→研究/商业如药企广告用途｜共享动机｜S2
<a id="p8-s2"></a>P8.S2 已知pseudonym/匿名ID→共享、发表或被收集后是否仍能去匿名｜第一研究问题｜De-Health
<a id="p8-s3"></a>P8.S3 已知账号层映射→记录能否连真人｜第二级问题｜linkage
<a id="p8-s4"></a>P8.S4 已知两问→以贡献回答｜直接转工作，无独立方法段｜C1–3
### 贡献（p2）
<a id="c1"></a><a id="c1-s1"></a>C1.S1 已知第一问→提出大规模De-Health框架｜方法产物｜§III
<a id="c1-s2"></a>C1.S2 已知框架→两个阶段｜组织｜S3–4
<a id="c1-s3"></a>C1.S3 已知阶段1→每匿名用户Top-K候选集｜规模处理与中间产物｜§III
<a id="c1-s4"></a>C1.S4 已知候选→精细DA映射候选用户｜输出闭合｜§III
<a id="c2"></a><a id="c2-s1"></a>C2.S1 已知框架→WebMD89,393用户/506K帖、HB388,398用户/4.7M帖；closed/open-world评价｜证据规模和匹配条件｜§IV
<a id="c2-s2"></a>C2.S2 已知评价→实践有效的源文结论｜结果概括｜正文数值
<a id="c3"></a><a id="c3-s1"></a>C3.S1 已知第二问→linkage框架连服务用户至真人｜另一个产物｜§V
<a id="c3-s2"></a>C3.S2 已知框架→用概念验证攻击验证｜证据级别｜§V-B
<a id="c3-s3"></a>C3.S3 已知验证→347/2805（12.4%）WebMD目标成功链接并关联敏感资料的汇总｜精确样本范围｜不能泛化全部人群
<a id="c3-s4"></a>C3.S4 已知关联→可暴露健康及其他极敏感方面，隐私被破坏｜实际后果｜研究必要性闭合

## 选择解释（推断）
- 数据价值与共享在风险之前出现，解释为什么发布行为会发生；保护任务不是简单说“不要共享”，而是检验匿名化是否足够支撑已有用途。
- 结构/规模/威胁三差异中，规模指向Top-K、异构指向多类特征、辅助信息指向图映射/跨站链接。虽然引言没展开每项算法回应，正文能追到对应关系；这是编辑解释，不是作者明写的模块一一映射。
- 两个问题先分开，贡献才不会把“还原线上用户”误当已知道现实身份。将攻击链最后一个环节单列给出真实隐私后果，也使12.4%有正确分母。
- 详细旧政策/调查为当时读者提供现实背景；写当前论文时应重新核对，不能把旧数值和法律概括当永久有效素材。

## 贡献篇幅条件
三项10句（4/2/4），贡献前无方法/结果预告段，故C1承担整个两阶段说明，C2承担范围，C3承担第二框架、验证及后果。最长项来自信息首次出现的位置；若增加独立方法与结果段，贡献才可相应压缩。不能因句数长就全删而留下缺机制/缺真实影响的列表。

## 可点击主源页锚
[PDF p1](https://nesa.zju.edu.cn/download/De-Health%20All%20Your%20Online%20Health%20Information%20Are%20Belong%20to%20Us.pdf#page=1) · [PDF p2](https://nesa.zju.edu.cn/download/De-Health%20All%20Your%20Online%20Health%20Information%20Are%20Belong%20to%20Us.pdf#page=2)

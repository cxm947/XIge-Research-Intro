# 按问题选读的来源地图

这是[研究选择变体](research-choice-variants.md)的查阅入口，不是首稿阅读清单。先读与当前问题相近的一项；需要迁移其论证选择时读对应完整引言，涉及特定技术判断再读列出的局部章节。每项“源例”只概述指定版本的内容；“选读用途”是编辑推断及改路条件。共著不等于个人执笔，来源报告的技术效果、首次性和解释不等于本参考已独立复现。

下列定位优先用版本号、章节名及印刷/PDF页，不沿用分析者自造的句号编号。作者托管且无修订号的文件按当前已分析身份引用，不冒充不可变版本。引言范围与额外补读分开；没有额外范围记录的项目不宣称全文审读。

本地图覆盖固定目录中的121个来源条目；同项目的版本、扩展和关联作品仍各按来源身份查阅，不据条目数推独立复证或写作收益。

## 内容导航

按缺少的关系定位源例；每卡用“版本与位置—源例—选读用途”概述正面选择及换路条件。可直接搜索论文简称，选一张后再读完整源引言。

- [关系、形式化与可知范围](#map-section-1)：[Quantifying Graph Anonymity](#quantifying) · [Structural Data De-anonymization](#structural) · [Cert-RNN](#cert-rnn) · [Amoeba](#amoeba) · [Password Correlation](#password-correlation)
- [信息、用途与联合对象](#map-section-2)：[Directed Triangle Counting](#triangle) · [AsgLDP](#asgldp) · [De-SAG](#de-sag) · [MPInspector](#mpinspector) · [PRSA](#prsa) · [De-Health](#de-health) · [Copyright Gap](#copyright-gap) · [UVSCAN](#uvscan) · [Label Inference](#label-inference) · [LoRAShield](#lorashield) · [IntraGuard](#intraguard) · [Tacoma](#tacoma) · [Backdoor Pre-trained Models Can Transfer to All](#ptm-transfer) · [Hijack Vertical Federated Learning Models As One Party](#hijack-vfl) · [CAMH](#camh) · [JWBinder](#jwbinder) · [SOPE](#sope) · [PROMFUZZ](#promfuzz)
- [表示选择与设计后的职责](#map-section-3)：[Integer Is Enough](#integer) · [HashVFL](#hashvfl) · [SUB-PLAY](#sub-play) · [FraudShield](#fraudshield) · [Git LFS](#git-lfs) · [DPCSS](#dpcss) · [AEIOU](#aeiou) · [TextShield](#textshield) · [FaceArmor](#facearmor) · [VideoEraser](#videoeraser) · [OTCCLIP](#otcclip) · [Pluggable Watermarking](#pluggable-watermarking) · [Activation Steering](#activation-steering) · [STAR](#star) · [StealthGraph](#stealthgraph) · [Turbo](#turbo)
- [过程差异与判定参照](#map-section-4)：[MOpt](#mopt) · [Dyn-D2P](#dyn-d2p) · [CS-LSTMs](#cs-lstms) · [AHEAD](#ahead) · [The Eminence in Shadow](#eminence) · [Code Rewriting Detector](#code-rewriting) · [Waltzz](#waltzz) · [MOCK](#mock) · [EMS](#ems) · [WAFLGo](#waflgo) · [ADAPDOOR](#adapdoor) · [MINER](#miner) · [SyzTrust](#syztrust) · [TFA](#tfa) · [SLIME](#slime) · [Efficient Query / AdvDroidZero](#advdroidzero) · [IPIGuard](#ipiguard) · [Towards Practical Backdoor Attacks on Federated Learning Systems](#practical-fl-backdoor) · [V-Fuzz](#v-fuzz) · [FLEXFUZZ](#flexfuzz) · [Dynamic Attention](#dynamic-attention) · [MCP Red Teaming](#mcp-red-teaming) · [V-SHUTTLE](#v-shuttle) · [iFIZZ](#ifizz)
- [信号、推断与接受条件](#map-section-5)：[Diff-ID](#diff-id) · [Is Your Explanation Stable?](#metfa) · [TruVRF](#truvrf) · [VERIFI](#verifi) · [InvMM](#invmm) · [CLIBE](#clibe) · [TextDefense](#textdefense) · [ORL-Auditor](#orl-auditor) · [CPscan](#cpscan) · [IPPO](#ippo) · [IMMI](#immi) · [Beyond Over-Refusal](#beyond-over-refusal) · [ADD](#add) · [FreeEagle](#freeeagle) · [Copy, Right?](#copy-right) · [Order within Chaos](#order-within-chaos) · [Learned Provenance Baseline](#learned-provenance-baseline) · [Object Detection Feature Space Coverage / OSD](#osd) · [JailNeurons](#jailneurons)
- [比较定义与观察单位](#map-section-6)：[DEEPSEC](#deepsec) · [AWT](#awt) · [UNIFUZZ](#unifuzz) · [OB-WSPES](#ob-wspes) · [Transfer Attacks Revisited](#transfer-revisited) · [Beyond the Payload](#beyond) · [The Last Mile of Fuzzing](#last-mile) · [Cloud Detectors](#cloud-detectors) · [Adversarial CAPTCHAs](#adversarial-captchas) · [TextBugger](#textbugger) · [SirenAttack](#sirenattack) · [AdvSQLi](#advsqli) · [Source Code Authorship Identification / SCAD](#source-code-authorship)
- [资料、部署与生命周期](#map-section-7)：[IoT Re-using](#iot) · [Docker Hub](#docker) · [Seeing is Living?](#seeing) · [Mandela-effect Benchmark](#mandela) · [PerMemSafe](#permemsafe) · [Text Captcha Is Dead?](#text-captcha-dead) · [The Boy Who Cried Wolf](#cried-wolf) · [PoisonLoRA](#poisonlora) · [TWIST](#twist)
- [条件性认识与采用](#map-section-8)：[ChatGPT-VM](#chatgpt-vm) · [Prompt Leaking](#prompt-leaking) · [ACIArena](#aciarena) · [Plasticity / Angel or Demon](#plasticity) · [Enkidu](#enkidu) · [Invisible-Face](#invisible-face)
- [跨线综合](#map-section-9)：[Graph Data Survey](#graph-survey) · [Navigating the Risks](#navigating-risks) · [Kernel Survey](#kernel-survey)
- [人类判断与表达职责](#map-section-10)：[AdversaFlow](#adversaflow) · [Mars](#mars) · [NeuroBreak](#neurobreak) · [Cryptographic API Misuse Detection](#crypto-api-misuse) · [FirmRCA](#firmrca) · [Smart Contract Graph Feature / Expert Pattern Fusion](#smart-contract-fusion)
- [按知识产品收束](#map-section-11)：[FirmSec](#firmsec) · [One Bad Apple Spoils the Barrel](#one-bad-apple)
- [版本与范围提醒](#map-section-12)

<a id="map-section-1"></a>
## 关系、形式化与可知范围

<a id="quantifying"></a>
### [Quantifying Graph Anonymity, Utility, and De-anonymity](https://nesa.zju.edu.cn/download/Quantifying%20Graph%20Anonymity%2C%20Utility%2C%20and%20De-anonymity.pdf)

- 版本与位置：INFOCOM 2018作者/实验室托管9页稿，无最终论文集页码；§I Introduction，PDF 1–2页，三量关系问题至攻击评价贡献
- 源例：保留共享效用，量化匿名性、效用及给定辅助图下的去匿名性关系，再以理论可达参照评价实现
- 选读用途：当实测值还不能说明可达余量时，前移对象与参照；没有可界定参照则交经验比较
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-a68da04b3f.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="structural"></a>
### [Structural Data De-Anonymization: Theory and Practice](https://nesa.zju.edu.cn/download/Structural%20Data%20De-Anonymization%20Theory%20and%20Practice.pdf)

- 版本与位置：IEEE/ACM ToN早期在线排版稿，14页，内容已定但分页未定；Introduction，PDF 1–2页，既有成功攻击、模型条件、四项贡献及路线图
- 源例：承认大型图攻击与ER量化，再问一般模型中的原因、条件、份额；冷启动ODA另有启动条件问题
- 选读用途：当成功实践缺条件解释时，保留成功再换问；更广分布不取消辅助图，理论与构造没有足够机制桥时不补造
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-354b8db00c.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="cert-rnn"></a>
### [Cert-RNN](https://nesa.zju.edu.cn/download/dty_pdf_cert_rnn.pdf)

- 版本与位置：19页NESA作者稿，标识CCS’21，出版字段仍有占位；Introduction，PDF 1–2页；局部补读认证对象与输出界判定，非完整证明核验
- 源例：保留POPQORN的RNN认证能力，以相关性保留的表示与包络计算研究更紧、可算的保证范围
- 选读用途：当固定模型尚有未确定区域时，写新增可证明范围；若模型经训练也改变，须另报实际模型收益
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-acbc08a57a.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="amoeba"></a>
### [Towards Certifying the Asymmetric Robustness for Neural Networks: Quantification and Applications（Amoeba）](https://nesa.zju.edu.cn/download/lcj_pdf_tdsc21.pdf)

- 版本与位置：18页NESA作者稿，无明确修订号，不当作已核正式出版版；Introduction，PDF 1–2页，非统一半径、单维例、形式化与求解概览
- 源例：从跨特征异半径增加到同一特征正负方向异界，以退化条件恢复旧对象，单维例隔离新增自由度
- 选读用途：当推广只剩“细粒度”时，用旧自由度、新自由度和最小见证改写；威胁对象不同则先重建可比性
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-593cbfaf86.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="password-correlation"></a>
### [Password Correlation: Quantification, Evaluation and Application](https://nesa.zju.edu.cn/download/Password%20Correlation%20Quantification%2C%20Evaluation%20and%20Application.pdf)

- 版本与位置：9页INFOCOM 2017格式实验室托管稿，无可见印刷页码；§I，PDF 1–2页；关系度量补读PDF 3页及个人输入到派生集合的接口，PDF 7页
- 源例：保留训练攻击和资料增强的成功，将数据集—数据集、个人选择—资料两类关系变成可比较对象；后者经派生集合复用量化，并交即时反馈接口
- 选读用途：当攻击成效遮住关系问题时，先写两端角色，再选度量和接收者；从集合方法到个人反馈须补输入转换。只需描述一个库时保留自库统计，群体相似不直接写成个人破解概率
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-9aee30689b.md)；2026-10-04读取，实际为替代CMU主源，与指定NESA副本字节同一性未证。原P/S编号与规范坐标见图内导航

<a id="map-section-2"></a>
## 信息、用途与联合对象

<a id="triangle"></a>
### [Privacy-Preserving Triangle Counting in Directed Graphs](https://nesa.zju.edu.cn/download/Privacy-Preserving_Triangle_Counting_in_Directed_Graphs.pdf)

- 版本与位置：ICDE 2025论文集版，13页，2588–2600；DOI 10.1109/ICDE65448.2025.00195；§I，2588–2590页，集中与局部两场景方案段
- 源例：集中场景承认可分别计算，再以联合发布改变独立切分总预算的安排；局部场景的出邻居可见性使噪声图承担补充估计信息的职责
- 选读用途：当分支依据不明时，先写信任和可见信息；完整邻居已知时，不复制局部可见性障碍
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-d1fc8dd7b9.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="asgldp"></a>
### [AsgLDP](https://nesa.zju.edu.cn/download/AsgLDP%20Collecting%20and%20Generating%20Decentralized%20Attributed%20Graphs%20with%20Local%20Differential%20Privacy.pdf)

- 版本与位置：TIFS 15（2020）正式排版，3239–3254；DOI 10.1109/TIFS.2020.2985524；§I，PDF 1–2页／3239–3240页，局部视图、相关关系、统计接口及三项贡献
- 源例：从结构/属性共同用途走向需保留的关系，以收集后的统计量连接生成；新机制、利用旧技术和组合能力分开命名
- 选读用途：当多对象只像堆料时，用配对是否改变下游判断选择关系；仅需边际报表时可分别估计
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-dc32e376bc.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="de-sag"></a>
### [De-SAG: On the De-anonymization of Structure-Attribute Graph Data](https://nesa.zju.edu.cn/download/De-SAG%20On%20the%20De-anonymization%20of%20Structure-Attribute%20Graph%20Data.pdf)

- 版本与位置：14页TDSC接收未定稿；DOI 10.1109/TDSC.2017.2712150；页眉2016不作修订日；§1，PDF 1–2页；局部补读§3.1首模型段、§5首段及§5.1概览
- 源例：从共同发布的字段看结构方法与结构量化的残余，分别交属性关系量化和成熟结构方法的增强
- 选读用途：当缺口来自漏用发布字段时，对齐发布/研究对象；字段恒定或不可得时收缩对象，按用户/按集合宿主不写成串行阶段
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-5c5bf79d86.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="mpinspector"></a>
### [MPInspector](https://www.usenix.org/system/files/sec21-wang-qinying.pdf)

- 版本与位置：USENIX Security 2021官方论文集版，含封面；§1，PDF 2–4页／4205–4207页，标准实现差异、黑盒要求、方案、评价及两项贡献
- 源例：标准与定制实现差异、闭源条件、非崩溃逻辑目标分别限制合理路线，再引出模型—性质—验证
- 选读用途：当方案缺任务级理由时，保留各路线能力及真正限制；目标只需崩溃检测时，不移入相同逻辑验证要求
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-1f315ef889.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="prsa"></a>
### [PRSA](https://nesa.zju.edu.cn/download/usenixsecurity25-yang-yong.pdf)

- 版本与位置：USENIX Security 2025作者托管论文集版，21页含封面；§1，PDF 2–4页／2283–2285页；局部补读§3及§4.1
- 源例：有限目标样例与跨输入复用要求先成立，再以公共同类知识校准遗漏、过滤当前输入混杂
- 选读用途：当“恢复一个输出”与“恢复可复用功能”混在一起时，拆目标材料、借用知识、复用判据；无类别共性则换校准路线
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-99f5cc87cc.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="de-health"></a>
### [De-Health: All Your Online Health Information Are Belong to Us](https://nesa.zju.edu.cn/download/De-Health%20All%20Your%20Online%20Health%20Information%20Are%20Belong%20to%20Us.pdf)

- 版本与位置：12页、九作者NESA托管稿，关联ICDE 2020；不套论文集页码；§I Introduction and Motivation，PDF 1–2页及内容脚注；补读§II-B、§III设定和§III-A Overview
- 源例：保留数据用途及旧对象上的保护研究，分开匿名记录对应与现实身份连接；候选缩域和精化是第一终点内部步骤，开放覆盖允许不匹配
- 选读用途：当目标数与阶段数混淆时，先定最终输出，再用中间产物连步骤，并让缺席条件靠近允许答案；只有一个终点就不扩成两问。源文结构特征已含写作属性，不能改成第一阶段纯关系图
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-f181e99eae.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="copyright-gap"></a>
### [Bridging the Copyright Gap: Do Large Vision-Language Models Recognize and Respect Copyrighted Content?](https://arxiv.org/pdf/2512.21871v1)

- 版本与位置：arXiv:2512.21871v1，2025-12-26，19页；不由AAAI页脚认作已核会议正式字节；Introduction，PDF 1–2页及Figure 1；定向补读Formulation、Benchmark、CopyGuard、Experiments与Discussion，PDF 3–7页，以及Table 6，PDF 12页
- 源例：外部视觉材料的进入路径使材料身份、标记可见性和当前请求成为联合评价对象；明示通知仍不足，分别给标记条件比较与处理行为改进理由。概览先命名CopyGuard，再在同句解释核验与提醒
- 选读用途：当新入口只写成“多模态更复杂”时，补材料怎样到达、已有信息为何不足、当前动作怎样改变；旧流程已能正确恢复视觉来源与状态时可转做条件评估，无标记不等于材料无保护
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-b3dda6f2a5.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="uvscan"></a>
### [UVSCAN](https://arxiv.org/pdf/2306.11206v1)

- 版本与位置：arXiv:2306.11206v1，2023-06-20，18页；§1含§§1.1–1.3，PDF 1–3页，止于§2前；绑定依据另读§3.2.1开头两解释段，不移用USENIX最终稿页码
- 源例：保留组件复用、文档推断、示例推断与源码检查的能力；把文档中的对象—义务—条件转成检查表达式，另一条输入从闭源实现构造行为事实，两者会合才支持使用符合性判断
- 选读用途：当方案像NLP到二进制的部件清单时，先写规则约束谁，再写实现事实如何对应它，并分别安排仪器准确性、规模发现与确认状态。规则已结构化可跳过语言抽取；事实缺失保留证据不足，识别出组件不等于发现违规
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-a36437c84c.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="label-inference"></a>
### [Label Inference Attacks Against Vertical Federated Learning](https://www.usenix.org/system/files/sec22-fu-chong.pdf)

- 版本与位置：USENIX Security 2022官方论文集版，19页含封面，1397–1414；完整§1，PDF 2–3页／1397–1398页，至三项贡献末；补读§5.1、Tables 2–3（PDF 8–9页）及§6.2、Table 6（PDF 12–13页）。[iDLG v1](https://arxiv.org/pdf/2001.02610v1)另读完整引言、§2.1与末页逐样本条件
- 源例：单方持有标签和最终模型，使局部访问限制成为有价值的问题；iDLG已有相应末层梯度下的标签解析，本文转看协作训练留下的标签相关表示。同架构、同辅助预算的比较支持表示来源，训练后预测与当前梯度解析分开交付
- 选读用途：当“原始资料不可见”被写成“没有可用知识”时，前移参与者权限、训练保留物与预测所需输入，再选匹配对照。直接信号仍可用时保留该分支；缺少有用局部特征或辅助信息时收缩能力。保护评价同时接主任务效用，并保留直接路线可被缓解的例外；引言0.7614是特定BHI训练集F1，不能代测试表现
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-af4d22b295.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="lorashield"></a>
### [LoRAShield](https://arxiv.org/pdf/2507.07056v2)

- 版本与位置：arXiv:2507.07056v2，2026-06-29，12页KDD2026版式；§1完整引言仅PDF 2页，含Figure 1及图注、三项贡献，止于§2前；无印刷页码。补读§3.3、§4.2–4.3、§5.1.3、§5.2、§5.5.2及§6；涉及局部近似及低秩恢复时再核Appendix A.2.2–A.2.6
- 源例：本地个性化资料形成小增量文件，上传后由下载者控制生成；平台遂在发布前编辑实际分享的个人LoRA；主评估中下载者持保护版，无原图及未保护版。引言给干预位置和能力承诺，免原图仍用模型与文本参照，其隐私理由及低秩恢复在正文展开，不能倒填成引言已有洞察
- 选读用途：当“免数据、保功能”像口号时，先写谁控制哪版文件、缺哪项资料及仍用哪些参照，再分别交目标压制、正常用途和可加载载体。UCE已有免训练多概念编辑与显式保留；IRS测目标概念的其他表达，正常保留另看BPS/FID/LPIPS。成本属于LoRA编辑过程，不是生成延迟或平台吞吐；SD3适配另有更高时间与显存条件。仅托管服务、未保护版仍可得或重新训练会改变路线；局部代理与SVD不保证任意离线用途。原稿残缺句保留为残缺
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-e48360a284.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="intraguard"></a>
### [IntraGuard](https://nesa.zju.edu.cn/download/auto_20260921_CCS2026_IntraGuard_1_.pdf)

- 版本与位置：固定作者托管auto_20260921_CCS2026_IntraGuard_1_.pdf，25页，CCS 2026格式不充作出版核定；完整§1，PDF 1页右栏至2页右栏第四贡献末、§2前；无额外正文阅读，2页背景图不属引言
- 源例：从委员会要维护的科学判断倒选完全外包行为与共同PDF入口；委员会可控制分发文档、结构与视觉又可分离，才支持文档侧介入。内容层和载体层各有职责，预防输出与事后核查信号对应不同决策
- 选读用途：当方案只剩机制名时，先写谁能改变哪个产物、两端各须保留什么，再连接介入与验收。辅助阅读也属正常用途时扩大保留条件；标记出现或缺席都不直接裁决完全外包。渲染一致不证明全部阅读方式无损，互补边界只支持源文所说的集合可行性；若写成本，保留普通个人电脑每稿一秒的源口径
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-9fe6898db0.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="tacoma"></a>
### [Tacoma](https://users.cs.northwestern.edu/~ychen/Papers/issta24main-p723-CameraReady.pdf)

- 版本与位置：ISSTA 2024合作者camera-ready，12页，DOI 10.1145/3650212.3680351；完整§1，PDF 1–2页，含贡献；补读§3.1–3.2相关解释，PDF 4–5页
- 源例：保留既有引擎测试及Favocado的IDL、类型、值、状态和存活性能力，把绑定对象的所属关系、作用域及执行环境作为仍须取得、保留和消费的条件
- 选读用途：当“支持上下文”太笼统时，写同类型对象何时仍不能互换，再让关系获取、纠正与生成各有用途。已有信息足够就直接使用；不由自动解析推新反馈学习环。独特崩溃、未知问题、CVE和覆盖率不互换
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-c153987a94.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="ptm-transfer"></a>
### [Backdoor Pre-trained Models Can Transfer to All](https://arxiv.org/pdf/2111.00197v1)

- 版本与位置：arXiv:2111.00197v1，页边2021-10-30，18页；完整§1，PDF 1–2页；补读§2.2、§3.1–3.2及§4.3，PDF 3/5页
- 源例：公共权重复用使提供者与下游任务知识分离；从标签依赖转向下游实际消费的表示接口，再将未知类别覆盖、微调后保持和正常效用分开交付
- 选读用途：当跨任务主张只有“通用”时，写各任务共同消费什么及仍不同的输出条件。并非所有任务只消费CLS，NER涉及token；RIPPLES已有微调保持，源稿也承认Latent Backdoor使用表示。接口不共享须换对象；最小插入数与字符长度占比不单独证明人的不可察觉性
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-318347dd2f.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="hijack-vfl"></a>
### [Hijack Vertical Federated Learning Models As One Party](https://arxiv.org/pdf/2212.00322v2)

- 版本与位置：arXiv:2212.00322v2，2024-02-16，20页；完整§1/§1.1，PDF 1–2页及Figure 1；补读§2.3–2.4、§3.1开头、§5.2及§7–8有关权限/稀疏条件和防御限定
- 源例：协作数据路线仍合理，但纵向分工改变可见信息与单方控制；标签相关信号支持一条自然路线，候选强度支持另一条，同时保留前者真实性。局部影响稀疏再给追加安排理由
- 选读用途：当跨场景借用只换数据名时，先写谁持有哪些部分、能提交什么，再比较能力与效用。HFL近邻控制本地训练/提交，不控制聚合算法；少特征和影响力不同，未有证据不互推。删追加动机段时，其他段仍保留局部持有和10%结果
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-e3479d788f.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="camh"></a>
### [CAMH](https://arxiv.org/pdf/2408.13741v2)

- 版本与位置：arXiv:2408.13741v2，2024-12-20，11页；完整§1，PDF 1–2页；补读§3.1–3.2、§4.3定义及PDF 7页图表，类别与数据实验分开
- 源例：由训练控制与完整分数访问说明可用信息，再把分数作为另一解码接口，最后分别检验新增任务和原任务能力；类别/分布是扩展条件，联合表现是验收目标
- 选读用途：当输出维数变化被当成新增信息时，先交权限和可分证据，再写接口及实际能力。联合训练不能给冻结模型直接作可行性证明；近邻已讨论类别扩展补救。CR/ER是各自任务参照比值，非绝对准确率；贡献的四倍类数说法与图有条件性不一致，不与30%数据结果拼接
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-2ada62afcb.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="jwbinder"></a>
### [JWBinder](https://arxiv.org/pdf/2310.17304v2)

- 版本与位置：arXiv:2310.17304v2，2024-04-19，21页；完整单栏Introduction，PDF 1–4页，止于源拼写Backgorund and Motivation前；补读§4.1的SDR/ADE及MinerRay比较，PDF 12–13页
- 源例：既有静态表示、规则和学习消费者是应保留的资产；实际JS–Wasm绑定先给边，任务相关抽象再给统一表示，可重建JS输出另使成熟消费者继续可用
- 选读用途：当统一表示等同于工具复用时，分别写关系取得、共同语义和消费者输入合同；已有共同IR接口可省重建。MinerRay已有混合语言联系，所比抽取Wasm协议不能代其完整能力。SDR按样本阈值、ADE按引擎数量，准确率、良性误报和成本各自交付
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-81630a3e7e.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="sope"></a>
### [SOPE](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lin26r/lin26r.pdf)

- 版本与位置：ICML 2026／PMLR 306官方稿，25页；完整§1研究正文及贡献，PDF/页脚1–2页，另读边界处披露和Figure 1；补读设置、Table 5、Limitations及Appendix R相关范围
- 源例：有用工具集成进入开放供给条件；任务与信息的正面关联改变选材，再分出已选信息如何进入过程、如何跨工具/任务复用的职责。阶段名只帮助导航，整体产物及效用条件才限定交付
- 选读用途：当背景只剩风险时，先交实际使用关系，再用有据关联选择信息及所需过程。稳定小目录可直接采用固定方法；zero-click带部署条件，商业条件与无防御基准分开。近邻并非统一零表现，约三倍不泛化；标题与正文对SOPE的两种展开各保原身份
- 本次句级图：2026-10-04未取得指定完整全文，无新P/S图；以上保留历史阅读记录，不能算作该次完整复读。见[本次状态](intro-source-index.md#本次不可得的9个指定全文)

<a id="promfuzz"></a>
### [PROMFUZZ](https://arxiv.org/pdf/2503.23718v2)

- 版本与位置：arXiv:2503.23718v2，2025-09-28，13页作者稿；完整§I，PDF 1–2页，含挑战/方案/贡献小节、四项贡献，无路线图；补读§II-A/C、§III-A、§VI及§VII的范围和对照
- 源例：业务信息、实例检查器与相关运行证据分别是下游所需的产物；候选函数、变量/语句绑定、表达模板及定向使用把抽象关系接到具体判据，双角色仅分信息职责
- 选读用途：当“懂业务”直接等于发现错误时，逐步写取得哪条关系、绑定哪些实例及观察何种运行结果。完整规范已可用时省提取；两个模型一致不代真值。近邻能力按本稿归属，不能写全无业务分析；18.2B是源称潜在范围，不是已避免损失
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-92070abe8e.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="map-section-3"></a>
## 表示选择与设计后的职责

<a id="integer"></a>
### [Integer Is Enough](https://ojs.aaai.org/index.php/AAAI/article/view/29388/30622)

- 版本与位置：AAAI-24官方论文集，38(13)，14704–14712；DOI 10.1609/aaai.v38i13.29388；Introduction，PDF 1–2页／14704–14705页；局部补读14706页Backward与式(4)、14707页误差界声明/隐私测量、14708页Baselines
- 源例：中间结果接口连接资源、重构和扰动线索；整数化之后交训练、性能及鲁棒性验收，四项贡献不复制三个问题
- 选读用途：当多种价值确在同一接口汇合时，先给接口和共同因素假设；作用点不同则拆开，不用整数格式代证DP
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-5408c8ca01.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="hashvfl"></a>
### [HashVFL](https://arxiv.org/pdf/2212.00325v2)

- 版本与位置：arXiv:2212.00325v2，2024-01-22，16页作者稿；§I，PDF 1–2页，三个挑战/方案及贡献；局部补读§II.D，PDF 3页
- 源例：二值共享之后再解释梯度与短码职责；由有效但昂贵的两两比较，改成各方对公共类别码的比较
- 选读用途：当表示改动造成原流程不再直接成立时，设计先于义务；离线存储无需训练通路，无共同语义时公共码未必合适
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-3419195084.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="sub-play"></a>
### [SUB-PLAY](https://arxiv.org/pdf/2402.03741v4)

- 版本与位置：arXiv:2402.03741v4，2026-08-31，20页；不当不可变CCS论文集文件；§1，PDF 1–2页，分治后的经验分配及共享；局部补读§3.1、§3.3
- 源例：分子游戏和transition分配先出现，发生频率差异再造成缓冲区不均和欠训练，共享回应此代价
- 选读用途：当后一困难由设计改分布而来，按构造—分配—后果—补救排；分组均衡或经验语义不兼容时换路
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-52f8920eaa.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="fraudshield"></a>
### [FraudShield](https://arxiv.org/pdf/2601.22485v1)

- 版本与位置：arXiv:2601.22485v1，2026-01-30，12页，含WWW2026引用信息；§1，PDF 1–2页，直接证据路线、可能失效、关系细化及评价
- 源例：先给简化匹配，再分析来源偏差与证据重叠/冲突，赋予筛选和关系组织职责；XML先供LLM消费
- 选读用途：当复杂结构缺修补对象时，先定义自然路线；唯一字段足够判定时直接匹配可用，人的收益须另有评价
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-056bd3713f.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="git-lfs"></a>
### [Unveiling Security Vulnerabilities in Git Large File Storage Protocol](https://nesa.zju.edu.cn/download/sp2025c2-final59.pdf)

- 版本与位置：18页NESA托管S&P 2025关联稿，未核出版文件等同性；§1，PDF 1–2页；性质来源与消费路径见§3开头、§3.2，部署适配见§5开头及§5.2开头
- 源例：先承认指针/内容分离的性能收益，再由职责分开及状态、操作、额度的组合提出可检查关系；规范同时依据安全原则与协议经验，检查按实际功能适配
- 选读用途：当架构风险只剩“复杂”时，前移一项有用分工及应保留的关系，再介绍性质和取证；角色或权益语义改变时先改性质范围，不能只换API。客户端已有哈希核验时，后果须按消费路径区别
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-4666101c6f.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="dpcss"></a>
### [DPCSS](https://nesa.zju.edu.cn/download/tce26_suyuan.pdf)

- 版本与位置：13页TCE接受未充分编辑作者稿，DOI 10.1109/TCE.2026.3656205；模板日期不作刊发日；§I，PDF/印刷1–2页；补读Table I、Prove第3小块及Update概览（7–8页）、定理2条件（9页）
- 源例：将未来审计数量与预计算、更新与旧参照失效相连，改换验证承担者和时点；跨验证之后才引出新增交换成本，密钥状态另承接撤销与前向安全
- 选读用途：当成本描述不解释改选时，先写旧时序依赖，再写角色/时点变化与新代价；静态保存可不加动态控制，旧参照能局部修补时就比较修补成本。每节点邻居量不作全网字节量，联合目标不抹去已有更新能力
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-1e368cddf8.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="aeiou"></a>
### [AEIOU](https://arxiv.org/pdf/2412.18123v3)

- 版本与位置：arXiv:2412.18123v3，2025-12-09，15页；§I，PDF/印刷1–2页，止于§II前；局部补读§III-A Design Intuition全部文字及§III-B Framework Overview两段，PDF 3–4页
- 源例：先以生成质量和计算时点选择生成前判断，再保留嵌入方法的目标对齐能力，从头级语义差异取得检测量；共同特征另交语义核验、输入定位理由和失败样本更新接口，各自承担不同职责
- 选读用途：当同一表示只配“统一、可解释”等形容词时，依次写观察对象、可计算判断、接收理由的人和更新材料。仅需总标签时可省解释产品；必须观察生成结果时保留事后检查。特征可视化不证明普遍稳健，给出理由不等于用户已据此正确修改
- 本次句级图：2026-10-04未取得指定完整全文，无新P/S图；以上保留历史阅读记录，不能算作该次完整复读。见[本次状态](intro-source-index.md#本次不可得的9个指定全文)

<a id="textshield"></a>
### [TextShield](https://www.usenix.org/system/files/sec20-li-jinfeng.pdf)

- 版本与位置：USENIX Security 2020官方论文集版，19页含封面；完整§1，PDF 2–3页／1381–1382页，至第三贡献末；补读§3.4–3.5（5–6页）、§4.6（8页）、Tables 2/4/5/7（9–11页）及§5.5（14页）。[Yu–Li 2014](https://aclanthology.org/W14-6835.pdf)另读完整引言及上下文、音形候选、组词过滤的纠错职责
- 源例：先保留自动分类的正常用途，再区分类别保持、字符编码、词级判断和训练覆盖；由部分恢复进入残余音形语义表示，最终交付分类。Yu–Li已有音形与上下文纠错，区别在于选择一个替换字，还是让未完全恢复的文本仍提供分类信息
- 选读用途：当“恢复不全”被当成最终任务失败时，分别写中间字符串质量和最终判断，再让残余信息解释表示选择；精确转录任务仍须满足逐字保真。按新增关系选择模态，源文英语扩展只用语义和字形。采用条件包含联合训练与从头训练事实，不能由引言“免重训”扩成冻结分类器即插即用；正常效用和扰动组须随结果保留，0.944只是特定色情检测配置
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-4ef65862d0.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="facearmor"></a>
### [FaceArmor](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/13026.pdf)

- 版本与位置：指定ECCV2026会议路径18页PDF，元数据创建于2026-06-29，不据此认定发表日；§1完整引言，PDF 1–4页，含第2页Figure 1、第3页Table 1及第4页贡献，止于§2前。补读§4.1–4.2、§5.1及§5.4–5.6、Table 2/6/7，核代理表示、剩余重叠、实际任务组合与离线成本
- 源例：先以修补、编辑、微调模仿及身份保持四类后续用途确定覆盖，再把共同的重构与语义要求展开成目标；目标合并之后才解释空间干扰。软权重分配位置，已有PCGrad处理仍重叠的方向冲突，分别承担职责
- 选读用途：当后段困难被提前写成行业难题时，先交目标与信息，再写组合在哪里新增干扰。IDProtector已有联合特征与未见模型，FaceLock已有编辑成功条件的改选；剩余价值在覆盖及协调。Table 1空心符号合并不适用／无效，不能当统一失败实验；四任务对应SD1.5/SDXL，SD3/Flux仅修补迁移，且Table 2/6有单指标强替代。每图成本是发布前一次离线优化，不是实时能力或用户接受实证；单一用途、独立目标或无代理信息时须改写要求
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-6a7f688210.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="videoeraser"></a>
### [VideoEraser](https://aclanthology.org/2025.emnlp-main.304.pdf)

- 版本与位置：EMNLP 2025正式版，30页／5954–5983页；完整§1，PDF 1–2页／5954–5955页，含Figure 1；补读§2概念擦除及§3.1共享编码器、表示与子空间定义，PDF 3–4页
- 源例：保留已有擦除能力，以共享语义资源为局部干预的正面根据；步间、帧间关系说明视频设计职责，目标移除、无关内容、质量及稳健性另成评价支线
- 选读用途：当“选择性”只是目标词时，写实际可访问的表示及目标相关区别，再说明哪些关系须保留。缺少可分证据时保留为假设；无序列任务不加时间一致性。删设计中的双关系解释后，后文时间平滑标准仍在；四限制、两阶段、五标准和三贡献不必一一对应
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-cc51b110bc.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="otcclip"></a>
### [OTCCLIP](https://aclanthology.org/2025.emnlp-main.497.pdf)

- 版本与位置：EMNLP 2025正式版，14页／9825–9838页；完整§1，PDF 1–2页及Figure 1，无独立贡献列表；补读§2.2–§4定义/理由、§5与Tables 1–3及A.3.1
- 源例：保留重配对与安全集路线，模型尚未充分训练的条件改变匹配依据；局部集合对应使细粒度有用途，再由匹配不能全纠正的残余分配训练权重，模态内部关系另有职责
- 选读用途：当新表示只剩分辨率更高时，写它保留的对应怎样改变下一判断，并让未解决部分进入后续处理。已足够匹配则不强加残余模块；SAFECLIP已有风险集单模态学习和动态扩集。图中区分不作概率保证，源表有非零与任务例外，不改成所有情况为零或全面领先
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-b5a1988e4d.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="pluggable-watermarking"></a>
### [Pluggable Watermarking](https://www.ijcai.org/proceedings/2024/0037.pdf)

- 版本与位置：IJCAI 2024官方版，9页／331–339页；完整Introduction，PDF 1–2页，四段、贡献为段内列项；补读§2.2及§3.1–3.4相关解释，PDF 2–5页
- 源例：跨系统共享解码结构提供选接口的正面依据，位置选择、嵌入、保留和提取分别回应职责；选择参数接口后，原有数值异质性成为需要处理的兼容条件
- 选读用途：当“可插拔”只靠覆盖范围时，先写共同结构与实际部署控制，再说明接口为何容纳多个系统。结构不共享就缩小兼容范围；Stable Signature已有解码器微调和多任务兼容。异质性不是稀疏化新造的代价，未找到所覆盖水印不等于内容真实
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-e8edda9d3a.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="activation-steering"></a>
### [Activation Steering](https://aclanthology.org/2026.acl-long.1206.pdf)

- 版本与位置：ACL 2026官方版，18页／26228–26245页；本轮新取固定URL并核完整§1，PDF 1–2页及Figure 1，五段，无贡献列表；补读§3–5、§6.1–6.3、Limitations、Appendix A/C.2有关定义、比较与限制。历史索引不改作当时新读
- 源例：保留权重编辑的效率，由局部代理与完整响应的区别提出另一目标；表示观察先给可行依据，再处理直接使用的约束、持续性与保留。引言报告已开展评估，但没有量化结果概览
- 选读用途：当替代代理被写成新能力本身时，先定义真正要改变和要保留的行为，再安排独立评价。JailbreakEdit已有多接受表达，DualEdit已有表示介导、持续、保留及回退缓解；增量须限具体目标/约束和同协议证据。去掉一组表示例子仍保留方案转向及直接使用约束
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-c7b0f8c968.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="star"></a>
### [STAR](https://proceedings.iclr.cc/paper_files/paper/2026/file/2cc14599eb447444a2efee58aa0a5ec7-Paper-Conference.pdf)

- 版本与位置：ICLR 2026官方版，26页；完整§1，PDF 1–2页；补读§3.1–3.2解释、§4.6、Tables 4/6及Appendix A权限段
- 源例：保留自动发现与反馈复用，分别说明策略覆盖和有效性为何重要；语义操控的正面观察支持换表示，再将候选策略到具体实例的实现分为不同职责
- 选读用途：当探索/利用成为空泛口号时，前移实际重复现象及替代表示依据。种子张成范围不等于全部策略，PCA正交不等于语义独立；AutoDAN-Turbo已有多轮发现与组合。若删双向张力句，过度利用高回报策略的解释和表示依据仍在，不硬规定唯一段序
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-79aa4ab765.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="stealthgraph"></a>
### [StealthGraph](https://aclanthology.org/2026.acl-long.295.pdf)

- 版本与位置：ACL 2026正式版，21页；完整§1，PDF 1–2页／6519–6520页；补读§2.1–2.2、§3.1–3.3、§4.1/4.4相关解释及Limitations
- 源例：把构建成本与内容代表性分开，用已有合成能力和实体/邻域关系说明选材；任务重述后，初始质量、改写保义与后续响应评价分别检验不同对象
- 选读用途：当“两阶段”掩盖验证责任时，写每步交什么、下一步改变什么及何时重验。图范围不证明真实请求分布覆盖；删方案处保义解释后，贡献仍保留改写后筛选。源文对响应是否指导下一轮存在张力，不据此写已核闭环机制
- 本次句级图：2026-10-04未取得指定完整全文，无新P/S图；以上保留历史阅读记录，不能算作该次完整复读。见[本次状态](intro-source-index.md#本次不可得的9个指定全文)

<a id="turbo"></a>
### [Turbo](https://drive.google.com/uc?export=download&id=1X2g81djDVI1u4n5N4J1s8wLGP8tFi4os)

- 版本与位置：固定Drive提供ICDE 2021论文集格式，12页／2583–2594页；完整§I，PDF 1–2页／2583–2584页；另有不同字节作者托管稿，不替换。补读图算子/定理假设、数据定义、成本与线上评价有关段
- 源例：已有共现关系虽不确定仍有可用聚集模式，先给建图理由，再用团结构与异质关系解释图模型适配；共同导语把三项适配归于所选关系图，实时请求范围另回应决策时限
- 选读用途：当图只是日志多的同义词时，先交关系为何有用，再解释表示带来的代价和请求时可得信息。没有关系增益可保留个体特征路线；GraphSAGE已有自特征和有界采样，GEM已有类型权重。0.8秒不含并行周期建图，24小时后取特征不等于新注册即有证据；未拦截的线上评估不证明已实现节省
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-a258b38871.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="map-section-4"></a>
## 过程差异与判定参照

<a id="mopt"></a>
### [MOpt](https://www.usenix.org/system/files/sec19-lyu.pdf)

- 版本与位置：USENIX Security 2019官方论文集版，19页含封面，1949–1966；§1，PDF 2–3页／1949–1950页，概率输出、五项考虑及四项贡献；包括末尾技术报告入口
- 源例：以算子概率分布为接口，按算子、程序、时间差异及宿主开销解释调度选择
- 选读用途：当小改动难显价值时，连接局部决定与整体任务收益；仅选项差异可用固定非均匀表，不由需求唯一推出PSO
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-d51010872e.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="dyn-d2p"></a>
### [Dyn-D2P](https://arxiv.org/pdf/2505.06651v1)

- 版本与位置：arXiv:2505.06651v1，2025-05-10，22页；Introduction，PDF 1–2页；局部补读§2末/网络假设及§4声明、式(11)–(12)、备注1–3，PDF 3、5–6页
- 源例：过程轨迹质疑固定噪声，在总预算下预定裁剪与预算序列；一般关系、指数特例和经验精度分开交付
- 选读用途：当过程观察应改变安排时，命名真正控制量与残余代价；无在线反馈不写自适应，单项量级不替代整体界
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-7271bf4af3.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="cs-lstms"></a>
### [Contextual and Seasonal LSTMs for Time Series Anomaly Detection](https://arxiv.org/pdf/2602.09690v1)

- 版本与位置：arXiv:2602.09690v1，2026-02-10，21页；§1，PDF 1–3页；引言调用Figures 1–4，其中Figure 4浮于PDF 4页
- 源例：由短尖峰和缓升漏检转向局部正常范围与周期演变参照；噪声/无标签另给学习约束
- 选读用途：当绝对值不足判状态时，以背景对照说明改换参照；示意图不独自证明双分支更优，单例不代方法类根因
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-c87b27b4a0.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="ahead"></a>
### [AHEAD](https://arxiv.org/pdf/2110.07505v1)

- 版本与位置：arXiv:2110.07505v1，2021-10-14，23页CCS’21格式作者稿；Introduction，PDF 1–2页，至第三项贡献末；本条所用关系来自完整引言，未据此宣称证明/实验全节核验
- 源例：保留树、小波和网格的区间回答能力，由局部小值受噪声淹没转向误差指引的分解粒度；节点一致性和高维扩展另有职责
- 选读用途：当“自适应”先于依据出现时，选入局部信号—噪声关系，命名真正控制量，再安置结构后的约束；数据均匀或查询不需局部分辨时可保留固定划分，稀疏本身不推出粗分
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-a904202f3c.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="eminence"></a>
### [The Eminence in Shadow（Eminence）](https://arxiv.org/pdf/2512.10402v2)

- 版本与位置：arXiv:2512.10402v2，2025-12-17，12页KDD 2026格式作者稿；§1，PDF 1–2页及Figure 1；强近邻与知识/能力条件局部见Table 1、§2.2末及§3开头（3–4页）
- 源例：用稀疏类间区域与密集内部的对照选择解释对象，再分区域刻画、单点影响及总体响应；等范数比较限定一种替代解释，框架承接这些认识
- 选读用途：当观察只作装饰时，保留对照与控制条件，让它改变表示和待估量；控制后差异消失就换解释，只有配置认识也可交付而不造新算法。已有低预算近邻仍成立，不能将低预算写成空白
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-385d46e392.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="code-rewriting"></a>
### [Uncovering LLM-Generated Code: A Zero-Shot Synthetic Code Detector via Code Rewriting](https://arxiv.org/pdf/2405.16133v3)

- 版本与位置：arXiv:2405.16133v3，2024-12-16，12页作者稿；Introduction，PDF 1–3页及Figures 1–2；定向补读方法/训练口径，PDF 3–6页，Tables 3–5，PDF 6–7页，以及长度、正确性与预算分析，PDF 9–10页
- 源例：代码域中的概率判据下降及低熵解释给寻找替代的理由；另一条双来源重写观察才支持相似度候选。原/重写配对、代码表示度量与多次均值把响应关系变成可评价的量
- 选读用途：当失败现象直接跳到新组件时，分清旧依据受何条件影响、新候选有何正面观察，再连到实际被评估量；旧信号仍有效时可保留比较，单侧相似例不足以支持来源区分，无来源标签监督也不等于无需训练
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-db9fe86207.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="waltzz"></a>
### [Waltzz](https://www.usenix.org/system/files/usenixsecurity25-zhang-lingming.pdf)

- 版本与位置：USENIX Security 2025官方版，21个PDF页含封面，6159–6178；§1，PDF 2–3页／6159–6160页，含资源段；补读§2.2末段的上下文有效性与§3的wasm-smith比较
- 源例：类型有效性决定能否进入实例化和执行，组合宽度决定进入后能探索什么；兼容栈接口的替换保留入口，变异和骨架生成改变内部组合，已有有效生成仍被保留为合理近邻
- 选读用途：当“保持不变”遮住改动价值时，先写必须通过哪一关，再写过关后允许变化的行为及其收益，分别验收有效性、覆盖和故障。若研究对象就是验证器，非法输入同样有用；栈兼容不是输出等价，也不能忽略其他上下文约束
- 本次句级图：2026-10-04未取得指定完整全文，无新P/S图；以上保留历史阅读记录，不能算作该次完整复读。见[本次状态](intro-source-index.md#本次不可得的9个指定全文)

<a id="mock"></a>
### [MOCK](https://www.ndss-symposium.org/wp-content/uploads/2024-131-paper.pdf)

- 版本与位置：NDSS 2024官方15页稿；§I，PDF 1–2页，止于§II前；补读PDF 5页缩减解释、6页模型更新/验证段、7页双向上下文与任务调度解释
- 源例：调用能否推进状态取决于所在序列，因而表示须保留上下文；松散轨迹和关系漏错分别促成覆盖条件下的缩减与新旧策略并存，模型选择调用和调度器分配任务族是两个控制层
- 选读用途：当“学习历史”直接跳到全面接管时，写接纳事件、保留的上下文、模型获得的决定权和旧策略继续探索的范围，再交反馈消费层。状态无关时不加上下文；保留目标覆盖的缩减不产出逐调用因果真值，材料充分可靠时可另评更大控制权
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-177bf3c33e.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="ems"></a>
### [EMS](https://www-users.cse.umn.edu/~kjlu/papers/ems.pdf)

- 版本与位置：NDSS 2022作者托管18页稿；§I，PDF 1–2页，含四项贡献，止于§II前；补读§II-B字节位置学习段和§III-A首段的高层历史启发式
- 源例：重复比较与立即数观察支持复用局部行动，输出明确为输入字节到修改类型/值的映射；以新路径或崩溃关联记录，区分旧史预构、当前史周期更新和额外算子接入，保留传统探索
- 选读用途：当“经验复用”缺实际接口时，先选可重复的局部条件，再写保留什么记录、下次输出什么动作及何时更新，使模型与成本有理由。位置或全局条件改变时先检验复用范围；单次成功不是每个修改的因果证据，目标执行昂贵时不照搬轻模型的必要性
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-2deb60c210.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="waflgo"></a>
### [Critical Code Guided Directed Greybox Fuzzing for Commits / WAFLGo](https://www.usenix.org/system/files/sec24summer-prepub-301-xiang-yi.pdf)

- 版本与位置：USENIX Security 2024 summer-prepublication固定16页稿，无最终论文集页码；完整§1，PDF 1页左栏底至3页左栏第四贡献末、§2前；补读§3.2关键代码及后缀区别（5–6页）、§3.3.1掩码段（7页），不增加引言所引Table 1或实验阅读信用
- 源例：承认定向测试适配提交，再用缺陷异位与到达后反馈不足区分“到达改动点”和“检验影响区”；每个种子当前的到达证据决定引导偏好。多目标另保各自身份，再共享同函数前提，避免总量与重复分测各自丢失的信息
- 选读用途：当常用代理尚未完成真正终点时，先写已取得条件与仍需变化的状态，再组织条件化控制；不是全局先到达所有目标再探索。到达即验收时不添远端目标，对象同质时不强留逐项身份。数据后缀不等于一切目标后代码；掩码按执行反馈引导更可能保留条件的变异，不是任意变异的可达性保证
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-bdd6754e02.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="adapdoor"></a>
### [ADAPDOOR](https://nesa.zju.edu.cn/download/auto_20260921_TIFS2026_ADAPDOOR.pdf)

- 版本与位置：固定auto_20260921_TIFS2026_ADAPDOOR.pdf，14页TIFS格式作者稿，文件名／元数据不作发表日期；完整§I，PDF／自编号1–2页，含所引Figure 1，至第三贡献末、§II前；补读§II-B动作级段（3页），仅核该文对近邻能力的介绍
- 源例：保留固定设置的强成功，再分别展示跨任务差异、同任务内改变奖励的非单调响应；人工选择成本由此成为研究目标。反馈来源、早期门控和调整频率分别回应不同条件，四组件不被写成四次串行失败
- 选读用途：当“自适应”只有名字时，先交保持项、变化轴与联合指标，再说明反馈改变哪个决定、何时允许进入或再调整。只有跨任务数据时不补造同任务见证；静态离线任务或无可信反馈时可保留离线选择。联合调和均值不冒充单任务成功，代表方法观察不升级为所有方法的不可能性定理
- 本次句级图：2026-10-04未取得指定完整全文，无新P/S图；以上保留历史阅读记录，不能算作该次完整复读。见[本次状态](intro-source-index.md#本次不可得的9个指定全文)

<a id="miner"></a>
### [MINER](https://arxiv.org/pdf/2303.02545v1)

- 版本与位置：arXiv:2303.02545v1，2023-03-05，19页；完整§1，PDF 1页左栏底至2页右栏第二贡献末、§2前，含资源脚注；补读§2.2编译器与序列段（3–4页）。[RESTler](https://www.microsoft.com/en-us/research/wp-content/uploads/2021/03/RESTler.pdf)另读§III所需输入、有效前缀、字典与三类搜索说明（PDF 2–4页），不含实验核验
- 源例：多步行为使长度成为执行需要，再让成功历史承担不同工作：序列作续接起点并影响机会分配，参数组合成为生成学习材料；异常参数检查另有错误对象。RESTler已有依赖约束与有效前缀，跨重启无记忆只对应其RandomWalk，默认字典处理也并非一律随机
- 选读用途：当“利用历史”掩盖选择时，写清保留字段、下次消费它的决定与各自判据，先定学习对象再选模型。单步目标不必偏长，尚无有效样本则保留规格、候选值和启动探索；无需预先训练语料不等于无需先验。长序列、过检和可复现错误分开交付，正常扩展与拒绝异常输入不共用成功定义
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-3698195c5a.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="syztrust"></a>
### [SyzTrust](https://arxiv.org/pdf/2309.14742v1)

- 版本与位置：arXiv:2309.14742v1，2023-09-26，18页；完整§1，PDF／自编号1–2页，至第二贡献开源句末，3页仅核后续背景边界；补读§4.4前三解释段（6页）、§4.5首段（7页）。[PartEmu](https://www.usenix.org/system/files/sec20-harrison.pdf)另读完整引言及两内容脚注，PDF 2–3页／789–790页，独立核验限文本
- 源例：保留插桩／重托管能力，再由MCU资源、硬件和状态条件限定迁移；PartEmu已分析四种真实TZOS二进制映像及TA，不一概称四种闭源系统。轨迹取得与状态判断各有职责；§4.4补充同覆盖而状态不同的观察，解释新增反馈为何改变保留哪些输入
- 选读用途：当“更多反馈”只是指标增多时，先写观测区分什么、怎样改变后续选择，再分别验收。旧反馈已充分区分状态就不追加，已有可靠状态标签就不造内部推断困难；变量组合是状态表示而非完整状态机。所选轨迹带来的容量与归属负担放在选择之后，真实任务本已由这些负担定义时可前置；发现、厂商确认和CVE保持不同状态
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-689896e985.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="tfa"></a>
### [TFA](https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-improving.pdf)

- 版本与位置：USENIX Security 2024官方版，19页含封面；完整§1，PDF 2–4页／5895–5897页；补读§2.1、§2.2.3、§2.3及§3末段，PDF 4–5页
- 源例：保留MLTA的多层类型、传播、交集及保守回退，用信息适用范围与剩余调用权重分别说明补充的价值；恢复出的目标/类型约束进入下一轮图分析，才使迭代有内容
- 选读用途：当“循环改进”只剩流程箭头时，先交每轮新增什么约束、由谁消费及何时停止，再分别验目标保留、候选缩减和成本。没有新约束就不造反馈；充分相似的停止条件不改成精确不动点。OpenSSL适用比例与Linux调用/目标比例有不同分母
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-23809d776d.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="slime"></a>
### [SLIME](https://zhexwang.github.io/papers/slime.pdf)

- 版本与位置：ISSTA 2022合作者发表格式稿，13页／365–377页；完整§1，PDF 1–2页，六原段及四贡献项；补读§2.4/Figure 1、§3.1、§3.5，PDF 3–7页
- 源例：同程序内属性效用较稳定、跨程序变化同时保留，使属性仍有用而偏好需适配；重叠属性队列、当前成员及组级分配分别成为对象，已有逐seed历史适应不被抹去
- 选读用途：当差异只是“环境复杂”时，选固定属性、变化程序的具体比较，再确定分配单位和成员更新职责。没有跨条件变化可沿用固定偏好；队列奖励不等于单seed质量，也不继承独立臂遗憾界。局部删掉比较句时，贡献和§2.4仍有比较依据
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-e82106495c.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="advdroidzero"></a>
### [Efficient Query / AdvDroidZero](https://arxiv.org/pdf/2309.01866v2)

- 版本与位置：arXiv:2309.01866v2，2023-09-06，20页；完整§1，PDF 1–2页，九散文段，无贡献列表；补读§3.1、§4.1–4.3及附录D/I/J有关接口、排除规则和比较
- 源例：候选异质与目标表示未知是不同条件；公开语义提供有误差的响应先验，树管理候选，反馈传播决定一次观察可借给哪些未查对象。保留EvadeDroid现实黑盒能力和MAB的内容复用
- 选读用途：当“复用反馈”缺对象边界时，先给关系为何可能预测响应，再写借用范围及失配代价；无相关性就缩回本次对象。零知识仍有公开材料、静态分析假设和置信反馈。构造失败排除、全部起始样本与成功子集分别交代，不把92%写成全部引擎或全部起始对象成功
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-5f4c0a6a8e.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="ipiguard"></a>
### [IPIGuard](https://aclanthology.org/2025.emnlp-main.53.pdf)

- 版本与位置：EMNLP 2025正式版，17页；完整§1，PDF 1–2页／1023–1024页，含Figure 1；补读§2.2–2.3、§3.1–3.2、指标及附录F.2有关定义
- 源例：复用规划能力，把依赖和顺序变成可约束的产物；规划前置后分别处理晚得参数与后显取数路径，同工具可承担不同含义则另检验准入的不足
- 选读用途：当所有困难都写在方案前时，区分任务原有要求与前置规划后必须补的可用性职责。固定流程已足够可不建图；晚得值、新增资料和调用含义各有判据。Tool Filter已有预选工具能力；新增取数的只读限制不取消原任务已批准写动作，也不证明所有只读操作普遍安全
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-4391324662.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="practical-fl-backdoor"></a>
### [Towards Practical Backdoor Attacks on Federated Learning Systems](https://nesa.zju.edu.cn/download/Towards_Practical_Backdoor_Attacks_on_Federated_Learning_Systems.pdf)

- 版本与位置：IEEE TDSC 21(6)，2024，5431–5447，作者托管出版稿；完整§I，PDF 1–2页／5431–5432页；补读§II、§III-A/B、§V及§VI-A/B相关定义和结果
- 源例：保留全模型放大帮助当轮融入的成功，再由本地数据依赖与他方分布差异解释改变作用范围；低更新观察为局部选择给依据，当轮融入与后续持续仍是不同要求
- 选读用途：当两个收益被拼成一个结果时，分别交作用范围、其他参与者正常任务与时间窗口。低更新不等于对全部正常任务无关，Neurotoxin已有低更新方向；极端异质条件仍有明显损失。选择阈值不等于实际比例，不把一个配置的低损失和另一配置的持久性合成联合保证
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-5322b1646f.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="v-fuzz"></a>
### [V-Fuzz](https://nesa.zju.edu.cn/download/V-Fuzz%20Vulnerability%20Prediction-Assisted%20Evolutionary%20Fuzzing%20for%20Binary%20Programs.pdf)

- 版本与位置：IEEE Transactions on Cybernetics早期在线稿，12页；完整§I，PDF 1–2页，四正文/导语段和三贡献；补读§II演化fuzzer段，PDF 2–3页，及§VIII开头，PDF 10页
- 源例：风险集中、抵达难度和工业预算各有理由；保留有用探索，以有误差的函数级预测改变优先信息，并由代码单元重要性连接输入路径选择
- 选读用途：当预测模块只有精度说明时，写预测粒度怎样变成行动及错误时仍保留什么工作。没有任务价值差异可不加优先级；较小权重不证明正的最低机会、最终覆盖或少漏保证。VUzzer能力仅按本源归属，不称旧法没有权重或二进制分析；十项CVE不全是新发现
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-e0e45fc435.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="flexfuzz"></a>
### [FLEXFUZZ](https://nesa.zju.edu.cn/download/LH_TIFS_2025_FINAL.pdf)

- 版本与位置：TIFS 20（2025）作者实验室托管IEEE格式稿，16页／11728–11743页；完整§I，PDF 1–3页及Table I、Figures 1–5；补读§IV-A/B/C有关边界、深度和到达计数，PDF 5–7页
- 源例：不同seed仍可重复执行相同代码，使工作单位转向当前覆盖边界；已有结构/动态分配能力保留。普通fuzzing仍负责许多边界，额外处理只给有理由选出的子集
- 选读用途：当“动态调度”未解释分配对象时，先写实际重复发生在哪一层，再分任务分配与额外指导的依据。浅层持续不证明不可达，稀少到达不等于浅层；没有额外困难时保留普通路线。规模可写九个大型程序，源文全超四万分支与表中39,046不一致；贡献不按图中模块凑数
- 本次句级图：2026-10-04未取得指定完整全文，无新P/S图；以上保留历史阅读记录，不能算作该次完整复读。见[本次状态](intro-source-index.md#本次不可得的9个指定全文)

<a id="dynamic-attention"></a>
### [Dynamic Attention](https://arxiv.org/pdf/2311.17400v2)

- 版本与位置：arXiv:2311.17400v2，2023-11-30，18页；完整§I，PDF 1–2页，八散文段、贡献导语及三项；补读§III-A/B/C、§V-F及§VII/VIII相关协议和代价
- 源例：差异观察与配对替换给可干预依据，但部署缺少配对参照，须另选择当前可取的接收注意力代理；固定方案残余才为随机性给理由，分类/生成分别保留所需信息
- 选读用途：当可干预关系被当成最优策略时，先交部署时缺什么、代理可能误伤什么，再比较固定和动态选择。SAP已有后置、免微调与随机取舍；固定策略足够就不添动态机制。softmax后缩放不自动重归一化，有限重复/噪声统计的98%不作认证保证
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-64e052ffcd.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="mcp-red-teaming"></a>
### [MCP Red Teaming](https://arxiv.org/pdf/2509.21011v1)

- 版本与位置：arXiv:2509.21011v1，2025-09-25，16页；完整§I，PDF 1–2页，十段，无原生贡献编号；补读§III-B/E、§IV-A/B/C、§V及相关框图/算法
- 源例：正常任务先给后续行为判据，两个检查面对不同失败、决定不同更新，新版本再验；保持原功能是独立任务要求，角色数量不决定贡献数量
- 选读用途：当循环只是“不断改进”时，明确失败信息更新哪个产物、哪些先前判断因改动需重做。SafeMCP/MCPTox已有环境、任务生成和检查；无需把自动化本身写成首次。局部生成约85%与筛选后35.3%分母不同，算法反馈变量有文内张力；防御仍属未来方向
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-a68fd421b9.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="v-shuttle"></a>
### [V-SHUTTLE](https://nesa.zju.edu.cn/download/pgn_pdf_V-SHUTTLE.pdf)

- 版本与位置：CCS 2021实验室托管论文集格式，17页；完整§1，PDF 1页右栏至3页左栏路线图末，图1位于随后、§2前；补读§2.3、§3.3–3.4有关结构、寻址和类型单位
- 源例：保留覆盖反馈、高吞吐与规格驱动结构能力，改在请求时取得材料，并按可辨类型维护经验；类型与队列的对应使语义有效供数有具体职责
- 选读用途：当准备成本被直接当作学习算法gap时，先写对象何时取得、经验按什么单位积累。节点独立及有限类型是源设计前提，跨节点全局关系重要时类别维护不足；次序错配理由来自后节，不倒填引言。删类别—队列解释仍保留类型名称、语义目标和结果
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-0f6adb9f11.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="ifizz"></a>
### [iFIZZ](https://www-users.cse.umn.edu/~kjlu/papers/ifizz.pdf)

- 版本与位置：合作者大学站托管12页作者稿，首页无出版者印记；完整§I，PDF 1–2页及Table I/Listing 1，§II起于3页；补读§II-A、§III-B/C/D及§VII-A相关定义
- 源例：返回检查和条件来源帮助取得错误候选，调用位置与此前错误序列再区分恢复状态；先处理早终止，再用少量错误触发多数所见崩溃的经验安排预算，状态没有制造组合爆炸
- 选读用途：当恢复路径被静态位置代替时，先写同处发生前还经历什么，再定去重与后果单位。无历史影响可用简化状态；小组合优先是经验而非所有bug定理。FIFUZZ已有上下文敏感深路径能力，差异限闭源与联合条件；候选错误函数不等于已确认缺陷
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-10097c51e8.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="map-section-5"></a>
## 信号、推断与接受条件

<a id="diff-id"></a>
### [Diff-ID](https://arxiv.org/pdf/2303.18174v1)

- 版本与位置：arXiv:2303.18174v1，2023-03-30；§1，PDF 1–3页，身份损失、式(1)直接距离混杂、对齐与四项贡献
- 源例：先建立身份损失信号，再检查直接距离的属性混杂；对齐因而改变比较条件而非仅添重建模块
- 选读用途：当信号有价值却测量不纯时，先给最自然比较再补混杂；没有该机制或参考图条件时不移植对齐叙事
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-9042a938b2.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="metfa"></a>
### [“Is Your Explanation Stable?”（MeTFA）](https://arxiv.org/pdf/2209.01782v1)

- 版本与位置：arXiv:2209.01782v1，2022-09-05，19页；完整Introduction在PDF 1–3页；重点PDF 2–3页的均值候选、小样本、中位数与统计输出；独立样本/连续分布处理见§3.1，PDF 4页
- 源例：同时降低及量化不确定性，承认均值路线后再以样本成本/分布条件选择中位数，经特定指示量及其求和所支持的伯努利/二项推断给阈值或区间输出
- 选读用途：当稳定图不能回答判断强度时，连接统计对象和输出；任务要求期望则不换对象，单特征区间不推联合排序
- 应用边界：本卡记录原引言的选择，不证明通用中位数有限样本推断此前缺失。重写定位时一并处理[中位数平滑近邻](source-decision-links.md#median-smoothing)，再解释本稿归因构造及中央子集选择；§4.2、§5.3.1的估计量分析与输入噪声稳定性比较各归其位
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-f612de4bf1.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="truvrf"></a>
### [TruVRF](https://nesa.zju.edu.cn/download/chunyi_truvrf.pdf)

- 版本与位置：TIFS 20（2025）出版版，4844–4859；current version 2025-05-15；§I，PDF 1–3页／4844–4846页，交付条件、违规/接受标准、三类审核及贡献
- 源例：前后模型取得条件先许可比较；数量估计需已知数量标尺，身份核验另回收方法前已存在的替代记录问题
- 选读用途：当变化被直接写成履约估计时，补信号—校准—使用及独立身份条件；仅告警无需数量反演，只问数量无需身份目标
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-2d9d102d0d.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="verifi"></a>
### [VERIFI: Towards Verifiable Federated Unlearning](https://arxiv.org/pdf/2205.12709v1)

- 版本与位置：arXiv:2205.12709v1，2022-05-25，19页；§I，PDF 1–2页，Figure 1浮于3页；补读§III-A/C、§IV及§V-A；标记相关性在§IV-C末/Figure 8，组合在§IV-D/Figure 9
- 源例：把服务端已执行遗忘与离开者能观察区分开，选择目标敏感信号和离开前检查窗口；同时开放检验自然遗忘、普通检查及处理—观察组合是否足够
- 选读用途：当相近总表现兼容不同目标状态时，先写歧义和谁何时能取证，再安排标记/检查；普通指标已能判别则保留它。可信服务端与指定模型访问不改成一般恶意服务端下零记忆证明，环境重叠条件不冒充已控实验
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-1b6614ac62.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="invmm"></a>
### [An Inversion-based Measure of Memorization for Diffusion Models（InvMM）](https://arxiv.org/pdf/2405.05846v3)

- 版本与位置：arXiv:2405.05846v3，2025-07-31，25页；§1，PDF 1–2页及Figure 1；定义/估计见§4.1–4.4，认识检验见§5.4–5.5，限制见§6
- 源例：从有限采样或原caption未触发，转向目标图像的敏感输入分布；定义以维度平均最小KL衡量距prior的代价，另交受分布族与有限检验约束的估计及复制/成员区分
- 选读用途：当“未发现”量词过宽时，先交输入集合，再分目标量、实际估计与可支持判断；只需固定有限条件的二元检查就可沿用判据、研究成本。低分不等于复制概率，高斯近似不成为全空间证书
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-07015463d4.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="clibe"></a>
### [CLIBE](https://arxiv.org/pdf/2409.01193v2)

- 版本与位置：arXiv:2409.01193v2，2024-09-11，32页，内含NDSS 2025出版块；完整§I，PDF 1–2页，至第五贡献末；补读§IV-D/E（7–8页）、Table IV（10页）、Appendix H（25页）及§V-I生成扩展（14–15页）。[PICCOLO](https://www.cs.purdue.edu/homes/shen447/files/paper/sp22_piccolo.pdf)另读完整引言与非精确反演、词判别性和动态评价范围
- 源例：模型复用的适配收益先建立部署前检查价值，再由输入线索转向受限参数响应；少量样本拟合与剩余参考上的迁移承担不同证据职责。PICCOLO已有不精确反演与动态攻击评价，残余比较须触及词判别信号，单凭低触发ASR不足以排除它
- 选读用途：当探针优化成功被直接写成异常时，补共同预算、正常对照和未参与拟合的观察。这里的熵来自剩余参考随机配对、混合表示后的“目标logit减最大其他类logit”分箱概率；低值说明集中，位置与目标命中仍另有职责。只有API时换可访问的观察；量尺或分箱改变须重校准。平均性能保留所测范围，毒性生成扩展也保留新增度量与静态spinning设置
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-74a13898b9.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="textdefense"></a>
### [TextDefense: Adversarial Text Detection based on Word Importance Entropy](https://arxiv.org/pdf/2302.05892v1)

- 版本与位置：arXiv:2302.05892v1，2023-02-12，21页，Word Importance Entropy版；完整§1，PDF 1–2页，至三项贡献末；补读§3.1–3.3（3–5页）、§5.6（11页）与Appendix F／Tables 14–15（18页）。[FGWS](https://aclanthology.org/2021.eacl-main.13.pdf)另读完整引言、替换响应、候选条件及标定
- 源例：FGWS已利用词频指导的替换和目标模型置信变化，且无需辅助神经检测器；本文改看全句删词响应。正常文本既可由多词冗余支持，也可依赖少数任务词，因此新的选择是响应关系，不能只把重要词当异常
- 选读用途：当指标只剩名称时，先写干预单位、所取类别、响应集合，再给聚合与标定。此版H＝−Σ|sᵢ|log|sᵢ|未把词分数归一为概率；高值判据不能套成一般概率熵的平坦度结论，部署类别y的选择在v1仍不明确。免辅助模型的收益须与重复查询、采样一起写；只返回硬标签或经logit后处理的接口需换路。Table 14的0.2227秒限该比较设置；Table 15全词检测在Amazon为0.2227秒、Yelp为0.3487秒，成本随长度和采样变化
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-b3ea90f06d.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="orl-auditor"></a>
### [ORL-Auditor](https://arxiv.org/pdf/2309.03081v1)

- 版本与位置：arXiv:2309.03081v1，2023-09-06；完整§I，PDF 1–3页，含Figure 1，至第三贡献末、§II前；补读§III-A能力（4页）、§III轨迹／集合粒度与§III-B近邻条件（5页）、§IV导语及§IV-A工作流（5–6页）、§IV-B末段和§IV-C检验对象／分布条件（7页）
- 源例：已发布数据使来源判断需要事后开展；水印、统计来源论证、公共参照和成员推断的既有能力仍保留。奖励与训练关系先支持候选信号，可疑模型返回动作后由共同critic评分；目标数据上的训练变化另提供匹配参照，回应固定阈值受任务与采集条件影响的问题
- 选读用途：当“选到信号”与“能够判定”混在一起时，分别写观察接口、共同量尺、参照代表的变化及最终输出。可信来源记录、已校准阈值或足够匹配的既有参照可直接采用，无须强造影子训练。critic估计不等于内部Q值或实测回报；条件化检验、轨迹判定、集合聚合与许可认定分层交付。行为改变时并列审计TPR和原任务效用，而非只凭一项变化宣称稳健
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-6eeb51e521.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="cpscan"></a>
### [CPscan](https://www-users.cse.umn.edu/~kjlu/papers/cpscan.pdf)

- 版本与位置：共同作者托管CCS ’21论文集版式副本，17页／794–810，未声称与另取ACM VOR字节相同；完整§1，PDF 1–3页／794–796页，含Table 1、Figure 1及资源注，至第三贡献末；补读§3.4开头、变量来源与有限用途链（PDF 6–8页）。[CRIX](https://www-users.cse.umn.edu/~kjlu/papers/crix.pdf)另读§3所需概览及§4.3前两段（PDF 4–5、8页）
- 源例：先保留复用与合理裁剪，再分“保障是否被删”和“当前用途是否仍需要它”；可区分安全操作与邻接关系的观察支持起点和匹配次序，风险判断真正消费前步对应。CRIX已有语义／上下文比较，本文换用对应上游参照，不能把近邻写成没有语义能力
- 选读用途：当差分直接变成风险结论时，先定允许变化、可核对应及仍需保护的用途，再交定位和风险候选。只需检索排序时相似分数可足够；无对应、用途已消失或保护语义重实现时改判。局部补读说明须核变量来源，并排除无关用途变化的干扰；链相同不作普遍漏洞证明，定位、候选、人工及厂商确认分层报告
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-390b20426f.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="ippo"></a>
### [IPPO](https://www-users.cse.umn.edu/~kjlu/papers/ippo.pdf)

- 版本与位置：CCS 2021合作者托管论文集格式，18页，DOI 10.1145/3460120.3485373；完整§1，PDF 1页右栏至3页左栏、§2前，含Figure 1；补读§4.2关键观察段，PDF 4页
- 源例：保留免直接理解全部语义的比较路线，再以对象相关语义和上下文义务限定哪些路径有资格比较；只需一对不是放弃参照质量，配对有效性与枚举代价另有职责
- 选读用途：当“更少样本”遮住判断条件时，先写两端须共享什么义务，再写差异如何成为候选及怎样确认。相同遗漏仍可没有差异；对象无关语义可省，不取消决定其义务的条件。报告、人工确认和维护者接受分别计数
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-8d71597fb2.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="immi"></a>
### [IMMI](https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf)

- 版本与位置：USENIX Security 2024官方版，19页含封面；完整§1，PDF 2–4页／4069–4071页；补读§2.3–2.4、Figure 3、§4.3及§6.1–6.5相关定义和结果
- 源例：先保留完整追踪与配对路线的能力，再用同对象、同失败状态下的责任重叠或空缺改换参照；对象切片和按需摘要使关系可计算，程序行为与语言线索承担不同证据职责
- 选读用途：当缺少平行实例时，先问同对象是否另有可观察关系；关系不存在或合法异步清理时保留候选、另找参照。K-MELD已有逃逸和条件消费者分析，不能借新参照否认它；语言辅助的少误报与少真问题同时报告。35%是假发现比例，约4%仅为所比候选集合内少报
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-049fb65998.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="beyond-over-refusal"></a>
### [Beyond Over-Refusal](https://arxiv.org/pdf/2608.22248v1)

- 版本与位置：arXiv:2608.22248v1，2026-08-23，16页；完整§1，PDF 1–2页；定向补读§3、§4设置/误报段及附录A.1/A.3–A.5相关解释
- 源例：由正常资料仍应可处理的要求选择内部表示差异，再区分措辞稳定性、跨层汇聚和良性参照选工作点；行为上失守不自动证明内部没有可用信号
- 选读用途：当信号、估计和决定混成一个准确率时，分别写观察对象、波动处理和工作点依据。已有内部信号的近邻须保留；本稿低数据比较不抹去PIShield完整数据能力。FPR、样本量和阈值符号有文内不一致，借设计关系，不复用未解决公式或拼接最小误报值；软汇聚不直接继承硬投票界
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-bee854378e.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="add"></a>
### [ADD](https://discovery.ucl.ac.uk/id/eprint/10230562/1/Defending_against_Adversarial_Malware_Attacks_on_ML-based_Android_Malware_Detection_Methods.pdf)

- 版本与位置：UCL托管TIFS接收未完全编辑稿，16页，DOI 10.1109/TIFS.2026.3729519，题名末尾Methods；完整§I，PDF 1–2页，六散文段；补读§III-A/E/F及§IV有关指标、校准、适配与成本
- 源例：功能约束既使现实变化材料难取得，也留下较稳定的信息参照；选择性变化为跨组关系给出候选信号，再限定仅复查原判良性这一动作分支
- 选读用途：当保护与效用只是并列指标时，让实际改判分支决定收益和伤害的分母，再交关系、学习材料及校准。正常多功能组合可能反驳异常判据；PAD已有原恶性保留，弃权和改判不是同一终点。TNIR/FNIR均为条件比例，校准预算不是部署严格保证；批量新增推理开销不是每APK总成本
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-4355bf5c6a.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="freeeagle"></a>
### [FreeEagle](https://arxiv.org/pdf/2302.14500v1)

- 版本与位置：arXiv:2302.14500v1，2023-02-28，18页；完整§1，PDF 1–2页，无图表；补读§2.4及§3.1–3.2，PDF 3–5页
- 源例：由平台分发前持有模型、缺验证资料的条件选观察层级；局部行为关系使分类器内部值得观察，较低观察成本又支持类别关系覆盖。材料可生成与材料能判别是不同主张
- 选读用途：当省时只是附带结果时，写它让哪项原本受限的覆盖可实现，再按最终判断选择观察部位。只有API或替代材料不代表目标行为时须改路；DF-TND已有无数据能力，SCAn已有类特定能力。总体准确率不回答源—目标类别关系，优化可行不等于真实分布覆盖
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-33b7f0ad03.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="copy-right"></a>
### [Copy, Right?](https://arxiv.org/pdf/2112.05588v1)

- 版本与位置：arXiv:2112.05588v1，2021-12-10，18页；完整§I，PDF 1–2页，及引言所指PDF 3页Figure 1；补读§II-C、§IV-A/B/D/E、Table I及§V-A有关参照和访问定义
- 源例：保留可精确核验身份的水印与强指纹，将共同测试得到的多角度材料接到独立训练负参照和判断；先选主动测试，再解释测什么、在哪些输入上测及如何解释结果
- 选读用途：当多指标被当成天然可靠时，分别写观察的独特信息和判读参照，强近邻可以成为组合中的一项。功能相似不充分证明复制，技术判断不等于法律权利；CEM能力仅依本固定稿归属，原论文未独立核验。阈值方向仍待澄清，投票比例不作个案后验概率
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-1e819403d4.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="order-within-chaos"></a>
### [Order within Chaos](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26iy/wang26iy.pdf)

- 版本与位置：ICML 2026／PMLR 306官方稿，27页；完整§1，PDF 1–2页；补读§2末、§3–4、§5.1、E.2/E.4/E.5与G.2相应定义/假设
- 源例：从定位编辑区域的需求解释像素证据，再区分旧物理痕迹改变、语义矛盾缺席和粗感知；局部邻域关系支持空间表征，内部与边界观察再分配粗定位和精化职责
- 选读用途：当“语义方法不够”被夸成无像素输出时，保留SIDA/FakeShield已有掩膜能力，转问选定观察为何适用于当前变化。真实平滑区域会误报，需要独立精化；LAD不是真实性概率，局部理论带传感器噪声、平滑和边界等条件，数据适配后不能继续称该来源为OOD
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-5dc666fe14.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="learned-provenance-baseline"></a>
### [Learned Provenance Baseline](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25k/zhu25k.pdf)

- 版本与位置：ICML 2025／PMLR 267官方稿，15页，卷分页79903–79917；完整§1用PDF/页脚1–2页定位，五段、无贡献清单；补读§2.1–2.4、§3.1–3.3及§4/附录D相关定义和比较
- 源例：保留事件频次参照和既有路径传播，把可学习的事件级参照作为可替换接口；分数估计供下游路径使用，所需未知信号与存储代价共同影响表示选择
- 选读用途：当“能学图”遮住判断接口时，先写学什么、输出交谁，再选择真正改变路径判断的信息。NoDoze已有上下文与周期更新，Marlin已有流处理；未见组合泛化不等于长期漂移适应，离线学习/在线评分不等于在线重训。历史有合成负例，不改成纯原始频次监督
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-beba53e0f9.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="osd"></a>
### [Object Detection Feature Space Coverage / OSD](https://www.ijcai.org/proceedings/2024/0048.pdf)

- 版本与位置：IJCAI 2024官方版，9页／431–439页；完整§1，PDF 1–2页／431–432页，四正文段、四贡献项；补读§2.1及§4.1–4.2有关输出、度量和确认定义
- 源例：对象检测的服务输出与联合可用性要求先决定观察位置，分布/覆盖关系再给测量理由；准确性与效率是独立部署要求，候选信号之后的确认依赖新的行为响应
- 选读用途：当“异常即确认”混为一项能力时，先写每次观察支持到哪一步，再说明下一判断需何种新证据。只有原信息时保留可疑状态；既有Adaptive Misinformation已关注正常准确率和代价。原文PARDA只作PRADA别名，不从方法名推出普遍确认保证
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-ed7c58b655.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="jailneurons"></a>
### [JailNeurons](https://proceedings.iclr.cc/paper_files/paper/2026/file/096347b4efc264ae7f07742fea34af1f-Paper-Conference.pdf)

- 版本与位置：ICLR 2026官方版，24页；完整§1，PDF 1–3页及Figure 1，含PDF 3页三项贡献；补读§2–4、§6.1–6.3及A.13–A.14有关定义、干预与分布边界
- 源例：内部可分、少量可迁移维度定位和新分布判断是不同问题；研究阶段干预帮助选坐标，上线读取并分类另有职责，稀疏目标与跨层覆盖各自说明选择
- 选读用途：当诊断实验直接变成部署能力时，先区分研究时可做的干预与实际可取的观察，再用跨条件评价约束选材。HiddenDetect已有生成前跨层检测；拒绝词概率不代完整回答安全，良性压力集仍可能高误报，定位与因果忠实性不混为一谈
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-5d2b368fef.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="map-section-6"></a>
## 比较定义与观察单位

<a id="deepsec"></a>
### [DEEPSEC](https://nesa.zju.edu.cn/download/DEEPSEC%20A%20Uniform%20Platform%20for%20Security%20Analysis%20of%20Deep%20Learning%20Model.pdf)

- 版本与位置：作者站18页稿，题名末词为单数Model，无可见印刷页码；§I，PDF 1–2页；局部补读PDF 13页§VI
- 源例：单指标不足、防强未必防弱与历时认识变化，分别说明评价维度、范围及扩展性；实现库能力仍保留
- 选读用途：当多比较只像堆数量时，先写被推翻的选择捷径；已有可靠单调覆盖时，扩大对手集合未必是核心
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-299c65ef97.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="awt"></a>
### [Enhancing Adversarial Transferability with Adversarial Weight Tuning](https://arxiv.org/pdf/2408.09469v4)

- 版本与位置：arXiv:2408.09469v4，2025-10-19，14页修订作者稿；未编号Introduction，PDF 1–2页，已有下界与四个独立剩余轴、形式化/调参及贡献
- 源例：保留已有迁移理论与强路线，分开比较口径、额外数据、正常/生成样本对象和两类性质关系
- 选读用途：当新理论/组合像替旧工作归零时，明确改变的对象与条件；关系与材料均未变时，组合本身未必构成新知识
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-e64a3bfbe3.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="unifuzz"></a>
### [UNIFUZZ](https://www.usenix.org/system/files/sec21-li-yuwei.pdf)

- 版本与位置：USENIX Security 2021官方论文集PDF，19页含封面；§1，PDF 2–3页／2777–2778页；所用版本/适配区别见§4.1；显现/分析对照见§5.1–5.2，2788–2789页与Figure 8
- 源例：评价将crash到bug身份、随机重复、目标、资源与版本一起纳入比较；infotocap的插桩二进制和ffmpeg的分析工具对照使显现/计数条件可见
- 选读用途：当统一或修复动作会改变被测能力时，先选原生采用或同条件技术问题；只问后者可适配，但须指明版本；只比较固定配置覆盖时，不强造到独立漏洞能力的延伸问题
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-26271ecf21.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="ob-wspes"></a>
### [OB-WSPES](https://nesa.zju.edu.cn/download/OB-WSPES%20A%20Uniform%20Evaluation%20System%20for%20Obfuscation-based%20Web%20Search%20Privacy.pdf)

- 版本与位置：未注明日期的18页作者托管稿，不补论文集页码；§1，PDF 1–2页至开源声明；补读§2.1末、§2.2.2、§3.1、§4.1–4.2、§6.2；效用解释另见§5.2–5.3局部
- 源例：共同活动记录连接异构机制，对手先验/历史另限定结果；查询属性、应用效用与参数趋势分开观察
- 选读用途：当同信息算法与原生端到端能力混淆时，先选问题再控信息；不随参数恶化不代表相对基线无损，强隐私路线可互补
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-1ab158f15f.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="transfer-revisited"></a>
### [Transfer Attacks Revisited](https://arxiv.org/pdf/2204.04063v1)

- 版本与位置：arXiv:2204.04063v1，2022-04-07，17页，含IEEE S&P2022接收信息；§I，PDF 1–2页；局部补读Table I、§II.B(c)、§IV.B
- 源例：正常多项输出就可能不满足单标签首位条件；成功语义、输入/目标条件及同名构念代理分别影响比较
- 选读用途：当分数先于输出合同出现时，先给正常响应反例；已归约单预测时可用相应规则，不同复杂度代理不直接互证或反证
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-097f6290bf.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="beyond"></a>
### [Beyond the Payload](https://arxiv.org/pdf/2608.30686v1)

- 版本与位置：arXiv:2608.30686v1，2026-08-31，30页；§1，PDF 1–2页；关键补读§3.2–3.4、§4.1–4.2、§5.1–5.2及Limitations
- 源例：已有工作研究载荷，本文换合法调用条件，分别观察攻击后果与警告；较低成功率可能伴随较浅执行
- 选读用途：当率变化可能来自接触/执行机会时，加入任务完成参照；跨任务也变注入位置时写工作流组合，不报纯措辞因果
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-c1e338ca9f.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="last-mile"></a>
### [The Last Mile of Fuzzing](https://nesa.zju.edu.cn/download/auto_20260903_boyutdsc2026.pdf)

- 版本与位置：TDSC 23(5)，2026年9/10月，11308–11325，DOI 10.1109/TDSC.2026.3712723；§I，PDF 1–3页／11308–11310页；输出/答案角色及设置见§III-A/B、§VI-A/B，人工调查边界见§VIII；与[FirmRCA v1](#firmrca)属同项目会议工作／期刊扩展关系，后者已有排序，本版改进排序及扩展支持、标注与评价，不作独立复证
- 源例：保留FirmRCA已有事件辅助逆执行，分别改进排名、语义支持和评价；高低层表示关系支持人工语义集合，系统仍交排名，由top-k内任一集合成员定义有效调查入口
- 选读用途：当“定位成功”不知指什么时，先写输出、合法答案与匹配事件，再报结果；需要完整原因链时另设链标准，唯一责任点明确时可用单点真值。五条是含截断的评价设置，样本/判据变化不能单归排名进步
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-e1dfbd274e.md)；2026-10-11恢复读取指定全文。P11–P15展开表示粒度、人工评价参照、系统排序输出与命中判据；它细化既有选材指导，不构成已证写作收益。源内数值冲突见图末说明。

<a id="cloud-detectors"></a>
### [Adversarial Examples Versus Cloud-based Detectors: A Black-box Empirical Study](https://arxiv.org/pdf/1901.01223v4)

- 版本与位置：arXiv:1901.01223v4，2019-09-14，17页；§1，PDF 1–2页，含Tables 1–2与Roadmap；局部补读§2.4和§3.2；此版本不与18页NESA接受稿混用
- 源例：保留云分类、标准检测及API模型恢复的已有成功，转问部署内容服务在访问、组合与查询条件下的可行性；按实际消费的标签确定成功语义，按方法×服务报告结果
- 选读用途：当“真实服务”只是场景名时，选入局部输出到使用决定的关系，重定比较单位与预算；局部输出已足以承担同一决定时无需另造系统层。方法×服务某格的成功不外推全部组合
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-ba26f30f1b.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="adversarial-captchas"></a>
### [Adversarial CAPTCHAs](https://arxiv.org/pdf/1901.01107v1)

- 版本与位置：arXiv:1901.01107v1，2019-01-04，16页；完整§1，PDF／印刷1–2页，至第三贡献末、§2前；补读§4.2四段基线分析与§4.3设计指导（5页），§7.1普通基线／人任务成功定义及§7.2指标定义（12–13页）
- 源例：失真或复杂语义仍可提高安全，却分别增加人的完成负担和设计者的材料成本。强识别方法对学习模型的依赖给候选性质以任务入口；由不可感知改为人可容忍，再把实际预处理列入比较，改变了可选择的设计空间
- 选读用途：当“变化很小”被用来直接证明可用时，先写任务必须保留的关系及允许变化，再选机器和人的独立判据。本任务机器少成功、人能完成分别有利；普通OCR应改回人机都正确，精确复现也不能借其他人任务通过放宽。只有相关比较含预处理时才引入该条件；人可容忍是设计要求，仍须人的成功率与完成时间兑现
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-54704a792c.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="textbugger"></a>
### [TextBugger](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_03A-5_Li_paper.pdf)

- 版本与位置：NDSS 2019官方15页全文，2019-02-24至27会议；完整§I，PDF 1–2页，含图1与披露脚注，至第四贡献末、§II前；补读§II-A（2页）、§IV-D度量导语／语义段（6页）、完整§V-B及Figure 16（12–13页）、§VIII-A有关近邻及§VIII-C（14页）
- 源例：文字的可见变化可能同时改变意义，因此先给保留人类读者原意的目标，再按信息访问分开机制。已有文本路线及各自适用条件仍保留，模型结果、语义代理与人的任务判断分别回答不同问题
- 选读用途：当模型改判直接被当作有效反例时，先写必须保留的任务信息及其与预测的关系，再选择评价；合法内容更新本应改标签时换验收标准。人研究的情感／毒性标签保持是所选成功攻击样本上的有界证据，不能充当完整语义等价。100%须带IMDB、AWS／Azure和黑盒条件；潜在防御与厂商修复意向仍按其原有状态交付
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-238a78de63.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="sirenattack"></a>
### [SirenAttack](https://par.nsf.gov/servlets/purl/10174631)

- 版本与位置：NSF PAR托管ASIA CCS 2020论文集格式，13页；完整§1，PDF 1–2页；补读§4.1–4.2、§4.4、§5.3、§6.1.2/6.3及Table 4
- 源例：先定义分类与序列识别两种任务，让联合能力有具体范围，再按近邻各自缺少的条件比较；引言主要交任务与访问覆盖，共同接口的较强理由在正文，不倒填成引言已有洞察
- 选读用途：当多个系统被一个成功率概括时，先交共同入口，再保留各任务的正确性与访问判据；既有白盒定向转录和播放迁移能力不抹去。99.45%限IEMOCAP十人说话人分类/ResNet18，不能代商业转录；黑盒仍需置信值，SNR不独自证明听感等价
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-879f8c1810.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="advsqli"></a>
### [AdvSQLi](https://arxiv.org/pdf/2401.02615v3)

- 版本与位置：arXiv:2401.02615v3，2024-01-09，16页；本轮新取固定v3并核完整§I，PDF 1–2页，及PDF 3页Figure 1；补读§II.B、§III末与§IV开头。历史源PDF哈希缺失仍保留
- 源例：从保护位置与实际二元反馈说明可用信息，再用输入内部结构、候选生成和同任务保持解释选择；树表示的对象比是否使用树更能说明变化
- 选读用途：当接口限制直接跳到算法名时，先交候选对象及独立保持判据，有限反馈不唯一推出MCTS。WAF-A-MoLE公开v1已有置信比较、变异历史树和候选复用；不当作机构版相同字节。语法合法、改判与语义保留分别核查，最大收益不写成所有产品普遍收益
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-f6b808ce92.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="source-code-authorship"></a>
### [Source Code Authorship Identification / SCAD](https://nesa.zju.edu.cn/download/lqj_pdf_tifs2021.pdf)

- 版本与位置：TIFS 2021作者托管15页稿，印刷1–15页；完整§I，PDF/印刷1–2页，两个论证长段、贡献导语及三项；补读§II自动方法段、§III-A/B、§IV-A、§V-C/D及§VI-B有关条件/效用
- 源例：保留自动规则与搜索能力，把增量放到更少目标信息下的条件能力；在可构造源码实例上施加保持规则，替代观察安排选择，目标接口另核结果，AST路径的关系理由由后节补充
- 选读用途：当只有标签被写成必须训练替代模型时，改问哪条辅助关系实际有用，并保留直接生成/枚举加校验足够的路线。旧规则的语义保持未由本稿§II单独证实，不能反说其不保功能；有限输入输出测试不作全输入等价或完全匿名。删训练介绍后，后句仍明确替代来源
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-7fbc935f66.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="map-section-7"></a>
## 资料、部署与生命周期

<a id="iot"></a>
### [IoT Re-using](https://nesa.zju.edu.cn/download/lpy_pdf_sp23.pdf)

- 版本与位置：指定PDF为17页NESA作者稿，标题使用Re-using；不当出版终版；§I，PDF 1–2页；结果分母局部核对§IV、§V-D、§VI-C；状态/观测关系另见§III-C，PDF 4–5页及§VI-A–B，PDF 10–11页，含Table VIII下方同设备讨论
- 源例：已有清除支持和建议仍留下是否执行/是否有效两问；用户材料分别提供预期比较及设备类别选样依据；逻辑未见仍可能兼容物理残留，标记和有效/无效单元观察支持方法效果判断
- 选读用途：当多方法像并列清单时，保留真实跨方法输入；调查不必都指导采样，固件结构风险不等于实物残留实测；仅验证默认配置时，无须转成物理擦除任务
- 应用边界：[Echo来源](source-decision-links.md#echo)同时观察恢复与所购设备的重置状态。本文问卷提供另一样本中的自报行为／认知，不改写成此前没有行为观察或解释原设备所有者的原因；identified、configured与recovered的对象和分母分别保留
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-601d126363.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="docker"></a>
### [Understanding the Security Risks of Docker Hub](https://www-users.cse.umn.edu/~kjlu/papers/docker.pdf)

- 版本与位置：20页合作者托管LNCS风格稿，关联ESORICS2020；§1，PDF 1–4页；关键补读§6与Figure 4，另局部核对§2.1、§5、§8
- 源例：推荐命令使新增资料具有执行意义，恶意分析另收窄对象；维护以修复机会起点衡量额外窗口
- 选读用途：当“全面”掩盖扩大来源与缩小子集时，分写两种职责；只关心总响应时可用对应起点，完整记录均值不代表全部镜像
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-c5e66ab4fe.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="seeing"></a>
### [Seeing is Living?](https://www.usenix.org/system/files/sec22-li-changjiang.pdf)

- 版本与位置：USENIX Security 2022官方论文集版，2673–2690；§1，PDF 2–4页／2673–2675页，接口/应用层、四问、因素认识与派生方法
- 源例：平台接口和下游集成让部署层验证有价值；因素认识局部为定制方法提供输入，整体成功率不能包办四问
- 选读用途：当研究层级或方法顺序缺理由时，写依赖关系和知识输入；下游另作独立核验时不自动继承风险，理论先导可方法先行
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-6787cd9815.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="mandela"></a>
### [Mandela-effect Benchmark（MANBENCH）](https://arxiv.org/pdf/2602.00428v2)

- 版本与位置：arXiv:2602.00428v2，2026-03-01，30页，页眉ICLR2026；§1，PDF 1–2页及Figure 1；生命周期/干预解释补读§2–7，特别§5.2
- 源例：保留基线正确控制，扩到摘要和再取回；原对→错区别于总体错，抗错误引导还需保留有益合作
- 选读用途：当新现象只剩名称/题量时，先给新增观察窗口；即时任务不造长期过程，引言无结果预告时可按对象—问题—协议闭合
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-f4f8acaf2d.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="permemsafe"></a>
### [PerMemSafe: Benchmarking Implicit Personalized Safety of Long-Horizon Self-Evolving Agents](https://aclanthology.org/2026.findings-acl.320.pdf)

- 版本与位置：Findings of ACL 2026官方论文集，6415–6433，19页；§1，6415–6416页及Figure 1；定向补读§3–5、Appendix B与E.2，DE评分判据见PDF 15页／6429页
- 源例：先由个性化收益说明记忆的合理用途，再让安全判断读取历史与当前状态；隐含线索识别与旧风险缓解后的更新分别成为比较条件，恢复合适帮助也是正面能力
- 选读用途：当“记住相关信息”被直接等同“当下判断正确”时，先写历史为何改变回答标准，再给可见资料、状态变化和响应判据；任务没有会失效的判断时不造动态轨，部署已可靠提供标签时保留显式信息条件
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-c89935c6fb.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="text-captcha-dead"></a>
### [Text Captcha Is Dead? A Large Scale Deployment and Empirical Study](https://nesa.zju.edu.cn/download/Text%20Captcha%20Is%20Dead%20A%20Large%20Scale%20Deployment%20and%20Empirical%20Study.pdf)

- 版本与位置：NESA托管16页CCS 2020作者稿，无修订号，按已核固定文件引用，不认作与论文集PDF字节相同；完整§1，PDF／印刷1–2页，至第三贡献末、§2前；补读§3.4三段（6页）及§5.4的人任务定义、Table 4／Figure 7（10–11页）
- 源例：先以当时的可用性、成本和伸缩性解释为何继续改进文字验证码；当前模型信息、未来演变和部署证据是可分别变化的条件。现场输入与返回回答又提供行为观察，使部署同时承担获取信息和验证效果两种职责
- 选读用途：当“真实部署”只表示规模时，写清配对输入、可见返回、归属依据和所更新对象，再另写现场比较回答什么。这里观察须经选择／识别，可能延后归属；无配对或可靠归属的日志不支持同样推断，只有耗费测量则保留环境验证。平台人口不是实验分母，引言50%沿用作者报告而不补造相对或百分点解释
- 本次句级图：2026-10-04未取得指定完整全文，无新P/S图；以上保留历史阅读记录，不能算作该次完整复读。见[本次状态](intro-source-index.md#本次不可得的9个指定全文)

<a id="cried-wolf"></a>
### [The Boy Who Cried Wolf](https://arxiv.org/pdf/2608.01373v1)

- 版本与位置：arXiv:2608.01373v1，2026-08-02，12页KDD2026版式；§1完整引言，PDF 1–2页，含Figure 1及图注、三项贡献，止于§2前；无印刷页码。补读§3、§4.1–4.3、§5.2与Table 1（PDF 7页）、Appendix C，核控制条件、参照机制与模拟请求口径
- 源例：可配置前置裁决保留下游能力，却可能因误拒让正常服务不可达；先传播图像、后由用户配文本，使已见问题与分离问题的比较有任务理由。方案由单实例转向多原型软参照，仍保留影子文本决策监督；风险类别子集能力在参照集合建立后出现
- 选读用途：当“泛化更强”没有对象时，前移谁控制哪个输入，再写哪种参照值得比较。Double-Edged Sword已有误报DoS，MLLM-Refusal已有未知文本图像拒绝，增量须落在独立多模态政策分类器及所测条件。ASRr用每图有限分离模拟请求，源文未给足聚合公式，不能补成十题全成功率；Table 1须比较同模型、数据与预算下的最强基线，不能沿用正文误称的最佳者。压缩开头只推迟架构收益解释，后文仍明示阻断关系；固定文本或无先行裁决时，不复制同一挑战
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-56ed062ba0.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="poisonlora"></a>
### [Customization under Fire / PoisonLoRA](https://arxiv.org/pdf/2606.09151v1)

- 版本与位置：arXiv:2606.09151v1，2026-06-08，27页CCS 2026格式作者稿；完整§1，PDF 1页右栏至3页左栏第三贡献末、§2前；补读§2.4单段（3页），仅核固定部署近邻与联合要求的源述
- 源例：轻量插件的组合价值先成立，用户混合、再上传再将比较对象从原件改为派生链；存续、低误触发、视觉判断与吸引采用分别承担条件。源文的吸引要求还含优于良性同类的竞争强度，不能缩成一般可用性
- 选读用途：当原件成功被当成后续使用保证时，先写谁控制哪些变换、派生件应保留什么，再选比较单位与判据。固定部署仍可测原件；无行为或同类比较证据时，技术存续与视觉相似不推出实际采纳、竞争优势或几何扩散。三项要求及两种实例也不排成三阶段、两挑战
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-8c4c252662.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="twist"></a>
### [TWIST](https://aclanthology.org/2025.acl-long.541.pdf)

- 版本与位置：ACL 2025正式版，17页／11025–11041页；完整§1，PDF 1–2页／11025–11026页，九原段、两有限列表导语；补读§2.2、§3、§4.1/4.3–4.4、§5.1–5.2与Table 1
- 源例：先以训练资源解释第三方组件复用为何合理，再从来源和验证条件进入任务；作用位置的理由、覆盖范围与修改代价分别回答不同采用问题
- 选读用途：当复用背景被写成疏忽时，先保留它解决的成本，再比较权限、编辑对象和实际代价。Rickrolling已有文本编码器风险，EvilEdit已有无普通训练资料的直接编辑和保留条件；更少参数不等于更快，所报1秒与25秒分别属EvilEdit/TWIST。删成本解释仍留下采用规模和风险证据
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-43466107a4.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="map-section-8"></a>
## 条件性认识与采用

<a id="chatgpt-vm"></a>
### [Exploring ChatGPT’s Capabilities on Vulnerability Management](https://liu-junming.github.io/paper/ChatGPT-VM/Paper-Exploring_ChatGPT%27s_Capabilities_on_Vulnerability_Management.pdf)

- 版本与位置：18页合作者托管稿，关联USENIX Security2024，不套正式页码；§1，PDF 1–2页；任务/提示条件另见§3.1–3.2与Table 1
- 源例：六任务为报告摘要、安全报告识别、严重性评价、漏洞修复、补丁正确性评估、稳定补丁分类；以任务与提示条件交采用地图
- 选读用途：当多环节被写成完整串行能力时，恢复任务坐标；真已串接且测累积效果时再写流程效能，开放困难不造已实现组件
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-ac970c8450.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="prompt-leaking"></a>
### [Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications](https://arxiv.org/pdf/2606.18673v1)

- 版本与位置：arXiv:2606.18673v1，2026-06-17，23页；§1，PDF 1–2页；关键补读§5.2、§6.1/6.2起首及§7.1设计直觉
- 源例：部署状态、比较权衡、内部现象和干预各换观察对象；AREA在报告可比保护下改善所测功能与优化耗时
- 选读用途：当强近邻已保护有效时，选择功能/成本增量；保护下降则写真实权衡，功能代理不变成人的理解，关联不升级唯一根因
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-b1d0179073.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="aciarena"></a>
### [ACIArena](https://aclanthology.org/2026.acl-long.457.pdf)

- 版本与位置：ACL 2026 Volume1官方长文集，10049–10066；§1，PDF 1–2页／10049–10050页；补读§5.4及表2，10056–10057页
- 源例：保留MASLab共同输入/协议，补安全入口与目标轴；协作环境中的防御失效和信息保留方向形成条件性认识
- 选读用途：当基准贡献只剩规模与统一时，分资源、比较能力、研究所得；简化为隔离机制服务时无需一概否定，裁剪还受上下文任务代价限制
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-d5ccc8652b.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="plasticity"></a>
### [Plasticity / Angel or Demon](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ma26w/ma26w.pdf)

- 版本与位置：ICML 2026、PMLR 306官方稿；卷分页84689–84719，PDF页脚1–31；§1，PDF/页脚1–2页及Figure 1；机制/组合见§4–6，局部命题见附录H，阶段反例见附录I
- 源例：以正常任务和触发行为的联合结果打破单轴判断，再由阶段及组合差异追问内部关系；比较、SCC概念组织和诊断方向分别成为产物
- 选读用途：当单项排名不能指导组合时，前移联合对照和已有模型状态，再让机制关系承担组合比较；效应独立时可保留并列，不强造交互。SCC主要限TM-Post，局部更新敏感度幅值命题不直接证明最终行为，检测方向不作成熟工具
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-69a91ca701.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="enkidu"></a>
### [Enkidu](https://arxiv.org/pdf/2507.12932v2)

- 版本与位置：arXiv:2507.12932v2，2025-09-15，14页MM2025作者稿，不冒称出版字节；§1，PDF 1–3页及Table 1/Figure 1；补读§2.3扰动段、§3.3目标/能力、§4.2概览、§4.3.1频率/身份代理与准备/使用的解释段，以及§4.3.2高层开头与Once trained结尾
- 源例：保留正常分享用途，由公开样本风险选择发布前介入；用户特定准备得到可重复附着的产物，再以四个采用问题分别交每次使用、资源、长度和用途保持。Table 1保留近邻单项能力，研究理由来自同一流程中的联合条件
- 选读用途：当“实时且通用”混合不同承诺时，先写准备产物怎样进入每次使用，再按对象变化和消费用途安排证据；听觉、转写与保护分开交付。一次使用或对象漂移时重新评价准备价值；低附着开销不等于低总成本，未见样本复用不等于跨用户通用，目标内部未知不排除可用代理信息
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-c423d986aa.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="invisible-face"></a>
### [Invisible-Face](https://nesa.zju.edu.cn/download/Invisible-Face_Rethinking_Facial_Attribute_Privacy_in_Social_Media_Photo_Sharing.pdf)

- 版本与位置：指定16页IEEE TIFS 20（2025）正式排版稿，6101–6116，当前版本日期2025-06-24；§I完整引言，PDF 1–2页／6101–6102页，含§A–D及挑战、贡献列表；§II始于PDF 3页。补读§IV、§V.B、§VI.F、§VII.C–F与Figure 7、Table IV–VIII，分别核保护对象、联合选区、指标、取舍与发布前耗时
- 源例：身份匿名化已有效，仍未回答同图属性提取；朋友观看与规模自动分析的用途区别，使真实照片外观成为保留目标。局部区域与全图在所测UTKFace三属性／ResNet-18条件下MOSR相同，再比较视觉保留；迁移与后处理各有来源，并非三个挑战配三个模块
- 选读用途：当保护和效用只是两个高分时，先写愿保留的使用，再把同一联合成功条件下的代价差异前移。PrivacyNet已有多属性、未见分类器及匹配效用；本例可借的是照片分享取舍。MOSR要求同图全部指定属性误分类，不代表信息消失；CollDiff在四平台原始MOSR更高，H-PN优势受权重与归一化限定。所报每图成本包括局部选区，属于发布前处理；隐藏身份或即时使用时须重选效用与成本条件
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-2079f71014.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="map-section-9"></a>
## 跨线综合

<a id="graph-survey"></a>
### [Graph Data Anonymization, De-anonymization Attacks, and De-anonymizability Quantification: A Survey](https://nesa.zju.edu.cn/download/Graph%20Data%20Anonymization%2C%20De-anonymization%20Attacks%2C%20and%20De-anonymizability%20Quantification%20A%20Survey.pdf)

- 版本与位置：IEEE接收未完全编辑稿，22页；DOI 10.1109/COMST.2016.2633620；§I，PDF 1–2页；补读§III-D/E、§IV-D、§VII及表II
- 源例：区分结构统计/应用效用，连接防御、攻击信息与保留用途；仅删标识基线保效用却保护不足
- 选读用途：当价值来自综合时，让跨线关系回应读者选择；不可比实验只作组织，概念史也不强加用途轴，不制造统一算法失败
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-afda94caf1.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="navigating-risks"></a>
### [Navigating the Risks: A Survey of Security, Privacy, and Ethics Threats in LLM-Based Agents](https://arxiv.org/pdf/2411.09523v1)

- 版本与位置：arXiv:2411.09523v1，2024-11-14，48页早期标题稿；§1，PDF/印刷1–4页，含Figure 1及路线，止于§2前；局部补读5页§2末六特征段，Figure 2框架浮图不当引言已展开的机制
- 源例：保留模块/阶段分类的定位能力，用起因与显现不重合的事件解释为何另按来源参与和影响组织；同一事件带入赋类条件，具体配置与场景再限定实际风险，贡献分别交坐标、任务范围和案例认识
- 选读用途：当分类轴只有“更全面”理由时，选一条有据的跨位置关系，写旧坐标丢失什么，再用新轴重述同一事件及其判断依据。只需定位时可保留旧分类；来源未知不由显现位置推因果，双轴表不是二分类，代理特征不是第三条分类轴
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-1966c7bea7.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="kernel-survey"></a>
### [A Survey of Operating System Kernel Fuzzing](https://arxiv.org/pdf/2501.16165v3)

- 版本与位置：arXiv:2501.16165v3，2025-12-04，38页；§1，PDF 2–3页／模板111:2–111:3页，止于§2前；局部补读完整§4文字与表图，PDF 6–9页
- 源例：先保留覆盖和崩溃指标的局部信息，再以定义、设置和目标差异限制直接跨论文排名；用功能需求、适用条件和方法贡献组织综合，使阶段负责定位、功能负责比较、技术负责实现关系
- 选读用途：当综述只有技术目录时，选一个共同需求，连接已有支持、适用条件和未决问题，再据此交研究认识；同条件数值可比时保留量化，缺记录不直接变成真实gap。§4.2/Figure 3与§4.3的F3.1/F3.2标签、Figure 4与邻文比例有不一致，迁移语义关系而不复用这些冲突编号或数值
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-b318fccf43.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="map-section-10"></a>
## 人类判断与表达职责

<a id="adversaflow"></a>
### [AdversaFlow](https://nesa.zju.edu.cn/download/dazhen_adversaflow.pdf)

- 版本与位置：TVCG 31(1)，2025年1月，492–502；DOI 10.1109/TVCG.2024.3456150；§1，492–493页；人的调整动作见494页R2/R4/R6、§4.2及498页案例
- 源例：自动训练仍有策略偏移、安全/能力权衡，专家需要连接总体、样例和检查点波动再调整训练
- 选读用途：当工具理由只有数据多时，先写未完成决定与所需证据；纯自动已足够则不加人，案例/模型收益不代普遍理解效应
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-c44bf3b6f8.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="mars"></a>
### [Mars](https://arxiv.org/pdf/2508.15606v1)

- 版本与位置：arXiv:2508.15606v1，2025-08-21，11页预印本，不从格式推录用；§1，PDF 1–2页；人类评价限定见§6.4.2、Table 8、Figure 7，PDF 9–10页
- 源例：异质风险与来源要求预组织和证据约束，双格式报告进入审核工作流；风险标签、证据检索和人的报告评价分开
- 选读用途：当输出就是复核接口时，交代来源/理由及机器、人各自用途；预计节时只作主观估计，不能写实测节时
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-a7b06c257f.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="neurobreak"></a>
### [NeuroBreak](https://arxiv.org/pdf/2509.03985v3)

- 版本与位置：arXiv:2509.03985v3，2026-08-29，11页作者稿，仍有出版占位；§1，PDF 1–2页；人类任务/评价及限制另见§4、§6、§7、§8.2
- 源例：跨层空间不可直接比较、神经元角色依情境变化，促成共享语义参照、轨迹和角色关系诊断
- 选读用途：当内部名单不足以解释作用时，先写可比性和假设检查；不把投影当物理因果，专家案例与微调效果不代受控理解测量
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-cc3b714b43.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="crypto-api-misuse"></a>
### [Beyond Static Pattern Matching? Rethinking Automatic Cryptographic API Misuse Detection in the Era of LLMs](https://arxiv.org/pdf/2407.16576v2)

- 版本与位置：arXiv:2407.16576v2，2026-03-18；PACMSE 2(ISSTA)，Article ISSTA006排版，含下载封面；§1，PDF 2–4页／文章1–3页；定向补读§3.2.2、§3.3–3.4、Table 2、§4.2–4.3及Table 3
- 源例：通用代码任务的可执行检查不直接给出密码用途的安全判断，因此把位置与根因解释一起评为诊断，让原代码与多次分析共同重审，再以人工确认检验正确性；额外告警还触发对基准语境和记录的回核
- 选读用途：当新工具扩大识别范围却未说明结果如何供人据以行动时，先写判真条件与复核对象，再交情景认识、比较资源和确认发现；已有可靠自动判据时不强造人工职责，多答一致也不替代真值
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-906728a4eb.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="firmrca"></a>
### [FirmRCA](https://arxiv.org/pdf/2410.18483v1)

- 版本与位置：arXiv:2410.18483v1，2024-10-24，18页；完整§1，PDF 1页右栏至2页右栏第三贡献末、Background前；补读§3.2根因分析两段（4页）。[Last Mile](https://nesa.zju.edu.cn/download/auto_20260903_boyutdsc2026.pdf)仅补核3页扩展声明与16页参考[25]，两者属同项目不同来源
- 源例：保留fuzzing发现与既有逆向／污点分析，再把价值落在解释已存崩溃、安排调查次序；具体访存针对传播不确定性，候选相关性和调查优先级分别交付。此v1已含排序，Last Mile改进已有排序并扩展支持、标注和评价
- 选读用途：当上游产物被当成任务完成时，写出仍待作的判断，再以关键不确定性选择观测、以调查单位选择结果。候选很少或同样有用时可不排序；故障不能再现或关键状态未观测时不称完备恢复。可分析性、速度和前十命中分开，均不自动等于修复或人工节时；不回填后版机制／指标或把重叠结果算独立复证
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-446d78ec82.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="smart-contract-fusion"></a>
### [Smart Contract Graph Feature / Expert Pattern Fusion](https://arxiv.org/pdf/2106.09282v1)

- 版本与位置：arXiv:2106.09282v1，2021-06-17，9页作者稿；完整§1，PDF 1–2页左栏，七原段、贡献为段内编号；补读§2、§3.2–3.3及§4有关任务、来源权重和比较
- 源例：固定规则单独裁决有局限，但局部模式仍是有用信息；神经表示承担复杂关系，解释目标又要求融合后保留命名来源身份。来源级输出因而是须单独交付的接口
- 选读用途：当两路融合被直接称为解释时，先写使用者要区分哪些来源，再要求编码和输出保留这些身份。CGE已有图与专家模式融合，纯图基线改善不证明胜过该强邻；权重为当前来源集内的归一化内积关系，不自动有标签支持方向、因果忠实性或人的审查收益
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-fa1fc1d2fa.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="map-section-11"></a>
## 按知识产品收束

<a id="firmsec"></a>
### [FirmSec](https://nesa.zju.edu.cn/download/zbb_pdf_issta22.pdf)

- 版本与位置：ISSTA 2022作者托管发表格式稿，13页，442–454；§1及§§1.1–1.3，PDF 2–3页／443–444页；局部补读§2图示/§2.3
- 源例：版本特定问题使版本级识别必要，资源与工具再服务生态认识；贡献区分资源、能力、实证所得
- 选读用途：当细粒度算法遮住研究答案时，先写下游知识问题；版本已可取得可直接研究生态，不由规模推代表性或由检出推可利用
- 本次句级图：[完整引言逐句注释](intro-source-maps/sj-0010159902.md)；2026-10-04读取，指定主源。原P/S编号与规范坐标见图内导航

<a id="one-bad-apple"></a>
### [One Bad Apple Spoils the Barrel](https://arxiv.org/pdf/2212.13716v2)

- 版本与位置：arXiv:2212.13716v2，2022-12-29，18页；§1含§§1.1–1.3，PDF/印刷1–2页；局部补读§2.3及5页组件聚合/风险关联；与上列FirmSec为同项目不同源版本，不是独立复证
- 源例：由有用组件复用进入跨固件传播认识；版本相关问题反推识别粒度，函数证据须聚合到组件，版本—风险资源另为连接提供根据；资源、能力与生态认识分别交付
- 选读用途：当精度改进脱离最终用途时，先写输出将连接哪类外部知识，再决定粒度与资源；若所有候选版本对目标结论一致，可研究较粗判断所需条件；配置等仍影响结论时，版本键也不充分，潜在关联不作部署可利用性
- 本次句级图：2026-10-04未取得指定完整全文，无新P/S图；以上保留历史阅读记录，不能算作该次完整复读。见[本次状态](intro-source-index.md#本次不可得的9个指定全文)

<a id="map-section-12"></a>
## 版本与范围提醒

- MOpt与UNIFUZZ此处均链接官方USENIX论文集版本。另有页码不同的作者托管稿；不能把其坐标直接贴到官方稿。MOpt官方引言末句还提供详细技术报告入口；资源声明不是已复现证据
- IoT条目沿指定PDF使用Re-using，不用其他索引标题替换其文件身份
- AWT的Introduction没有编号；Asymmetric/Amoeba、Cert-RNN、De-SAG等作者稿的占位或临时页码不补作出版元数据
- 表内读到的章节与所用引言关系属于来源说明；不是统一要求新稿添加用户研究、定理、新算法、结果数值或固定贡献项数

- One Bad Apple v2与FirmSec保留各自引言范围和源版本；同项目材料可解释扩展与重组，但不作两份独立实证。Cloud Detectors以所列arXiv v4定位，不将另一托管稿的页数、编号混入

- Waltzz采用官方含封面页码；UVSCAN限定arXiv v1。Navigating the Risks保留含Ethics的v1标题，Kernel的111:页码是模板定位，不充当正式论文集页码；AEIOU与Enkidu使用各自固定修订号

- FirmRCA v1与Last Mile按各自固定文件定位，重叠发现不作独立复证，后续机制和指标不回填前稿。两篇CAPTCHA工作也保留题材与作者关联，条目数不是独立确认次数

- Activation Steering与AdvSQLi本轮分别以官方固定URL和arXiv v3重新核读；新取得来源与历史阅读记录分账，不把缺失的历史PDF哈希补成已匹配。来源目录保留原第一轮状态
- 新近补读中的TAGS/Marlin为同一arXiv项目版本，官方Salem稿与未取得的v1、WAF-A-MoLE公开v1与机构稿不互认字节；近邻说明只在明确阅读范围内使用，引用链接也不等于实验复现

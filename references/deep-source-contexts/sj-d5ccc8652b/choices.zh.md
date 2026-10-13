# ACIArena：十六组定点分析与英语替换选项

- record_count: 16
- historical_units_targeted:
  - B1.S1
  - B1.S2
  - B1.S3
  - B2.S1
  - B3.S1
  - P1.S2
  - P2.S2
  - P3.S2
  - P3.S4
  - P3.S5
  - P3.S6
  - P3.S7
  - P4.S2
  - P4.S3
  - P5.S1
  - P5.S2
  - P5.S3
- source_text_exclusion_note: Original source spans and fully spliced source sentences/units are excluded. Hashes identify the reviewed splice, not semantic-equivalence proof. Declared span scope distinguishes short patches and whole-unit replacements from the eight separate contextual variants.
- analysis_scope_preamble: 保留完整27个历史分析单元及原先3个编辑选项，不为数量把每句重做。本稿另记一个源贡献列表组织句O.S1；不把它叫实质研究增量。下列16组精化分别标出原文观察和编辑推断；“矩阵”指语法主干，不自动等于语篇焦点。英文替换需按精确跨度拼回，清晰化或强度改变均明确。

## ACI01

- units:
  - P1.S2
- refinement_reason: 旧稿“结果转真实部署”易把语篇推进读成语法上已证因果；补两个并列有限谓语。
- source_observation:
  - matrix: MAS demonstrate strong capabilities和are increasingly gaining traction并列。
  - dependency: By integrating为前置方式；and而非therefore连接能力与采用，不直接编码前者导致后者的实证因果。
- editorial_inference:
  - foreground: 研究对象先有能力理由，再有实践采用；显眼的模型强能力不是本文新实验结果。
  - information_progression: P1.S1定义协作对象→S2说明怎样工作及采用→P2让同一交互条件转成风险。
  - research_product_value: 基准的使用价值来自协作系统已值得研究，不必借宏大通用智能愿景作唯一理由。
  - relative_length: 一句并列足够交背景；若只研究实验MAS，产品部署例可少讲，但不能冒作本轮测试样本。
- local_replacement:
  - unit: P1.S2
  - unit_start: 230
  - unit_end: 293
  - intro_start: 426
  - intro_end: 489
  - source_span_sha256: 8c87013e45006b3bf799f2526903c240316fe6ffef46fe98dec11e561c713e73
  - replacement: and are seeing increasing adoption in real-world deployments
  - scope_strength_and_cost: 局部保持进行中的采用事实和and并列；不将来源时代产品例当2026年本轮重新核验的现况。
  - selection_condition: 需要清晰表达采用而避免gaining traction的比喻时。
  - applied_sentence_or_unit_sha256: dc793421a118f077f29feff37f9689e2595e7abffa60430949b5a233813db1e1

## ACI02

- units:
  - P2.S2
- refinement_reason: 旧稿已给注入与级联链；补can的能力模态和尾部known-as对整个过程的命名。
- source_observation:
  - matrix: Attackers can inject是矩阵，via标入口多样性。
  - dependency: compromising与exploiting为分词展开，to propagate给传播方向；known as语义上命名整类攻击，而非紧邻system。
- editorial_inference:
  - foreground: 区别ACI与普通单点注入的部分位于非有限展开中，不是矩阵inject一词。
  - information_progression: P2.S1交互产生风险→S2指出从局部受影响代理到系统传播→S3给可能后果。
  - research_product_value: 基准单位需覆盖入口与传播，不仅记录模型是否被一句话改变；只借语法关系，不转成攻击操作指导。
  - relative_length: 一句可引入类名和关键区别；若拆句必须让ACI回指整个过程，不能只给系统另起名字。
- local_replacement:
  - unit: P2.S2
  - unit_start: 189
  - unit_end: 237
  - intro_start: 1281
  - intro_end: 1329
  - source_span_sha256: 12a33f02536717cf3a5c9a687f14383cc2e42e2ac86a89ed74c7aa44958650af
  - replacement: a process known as Agent Cascading Injection (ACI)
  - scope_strength_and_cost: 局部加入process明确命名对象，仍保can及前述可能过程；是名词性同位补充，非保证每次注入都级联。
  - selection_condition: 长尾命名可能被读作system的修饰时。
  - applied_sentence_or_unit_sha256: b832f37b85cb2fa74804a4dec0715e33220801417d0c6ca2960c859894d04647

## ACI03

- units:
  - P3.S2
- refinement_reason: 已知表面/目标两轴；补or不是全体旧工作同一缺陷，i.e.与such-as也非同一范围。
- source_observation:
  - matrix: some studies focus solely...or restrict evaluation...是两个备选批评。
  - dependency: 内部or列表面选择，外层or换到目标受限；such as只举目标例子。
- editorial_inference:
  - foreground: 缺口为可比较威胁范围不足，不是前人从未发现漏洞。
  - information_progression: S2实例→S3无法系统识别潜在弱点→P4.S2以两轴组织补足。
  - research_product_value: 研究产品需要讲清案例库沿什么轴组织；只给总条数不能回答覆盖了哪类威胁。
  - relative_length: 一长句保两轴及引文；若读者易混，可拆两句，而不是压成攻击不够多。
- local_replacement:
  - unit: P3.S2
  - unit_start: 147
  - unit_end: 191
  - intro_start: 1761
  - intro_end: 1805
  - source_span_sha256: d2a56cc46c8b753a85e8cfa114dfb82d4d100436a808a85c69d68b40d6d44c26
  - replacement: or evaluate only objectives such as
  - scope_strength_and_cost: 局部保限缩、举例和外层or；不变成所有旧研究只测一个目标，也不推导本基准覆盖全部3×3等量组合。
  - selection_condition: 需要平行focus/evaluate主动作时。
  - applied_sentence_or_unit_sha256: e2e5a9439d2eab5a10829952059d73aebb3f479bdd6721aa3360e52ac39d8641

## ACI04

- units:
  - P3.S4
- refinement_reason: 旧稿已区分广度/可实施性；补tailored与depend为不同有限谓语及limiting对象。
- source_observation:
  - matrix: many attacks are tailored...or depend heavily...并列。
  - dependency: systems或roles是定制对象；internal system access为另一路依赖；limiting评价两类前提对practical applicability的限制。
- editorial_inference:
  - foreground: 问题不只少几个测试面，还包括方法依赖什么权限与定制条件；新增维度处于Moreover句。
  - information_progression: 前句威胁覆盖→本句可用前提→§3.2统一威胁能力约束；不能说仅接口标准化就解除所有访问需求。
  - research_product_value: 公平比较需要相近受控能力，否则强权限高成功率不是同一安全结论。
  - relative_length: 保独立一句有理由；合进coverage列举会让权限条件消失。
- local_replacement:
  - unit: P3.S4
  - unit_start: 222
  - unit_end: 260
  - intro_start: 2210
  - intro_end: 2248
  - source_span_sha256: 1b35f6046a969d70860e9a5cb58711aa47f7f9ca1a84d28caff473d6006c6e18
  - replacement: which limits the practical applicability of these attacks
  - scope_strength_and_cost: 局部将分词后果显式为评注性关系句，their回指改明确；保原较强因果主张，不增加所有现实部署不可用。
  - selection_condition: 长句有多个复数名词导致their对象不清时。
  - applied_sentence_or_unit_sha256: 4443658d8a338fa8c6619e1bc50140ce3b7abd4d42856e757a88fcb808b6ce84

## ACI05

- units:
  - P3.S5
- refinement_reason: 旧稿已记录简化与外推；补批评依赖的是实现差异，不是规模小或论文不够新。
- source_observation:
  - matrix: Existing studies often rely on simplified implementations是矩阵。
  - dependency: which修饰implementations；making把差异接到跨部署一般化困难。
- editorial_inference:
  - foreground: 真正学术代价在后两层：实验对象差异改变能否带走结论，主句rely本身不是错误。
  - information_progression: P3.S4攻击依赖→S5系统建模依赖→P4标准接口及六实现支撑可比研究。
  - research_product_value: 基准贡献应提供可解释的比较条件，而不是将代码整合当装饰。
  - relative_length: 保因果链需要超过一句“设置不真实”；可压成定语+后果，但别删除差异原因。
- local_replacement:
  - unit: P3.S5
  - unit_start: 119
  - unit_end: 250
  - intro_start: 2415
  - intro_end: 2546
  - source_span_sha256: ee88002ec629ccf54707fbc86a0519289f8b91553286209216a9fdd7f4106dcb
  - replacement: which differ substantially from real-world systems and thus make the studies’ findings difficult to generalize across diverse MAS deployments
  - scope_strength_and_cost: 局部保非限制性关系从句，把结果改成并列的make谓语并明确findings属于studies；保often和源差异/外推主张。
  - selection_condition: 希望显化实现差异与外推困难的关系、消除their近指歧义时。
  - applied_sentence_or_unit_sha256: d54a3bde9c35f9ffefa9200d2169de5472fe88e15a942fd3d8f592f9554b11d7

## ACI06

- units:
  - P3.S6
- refinement_reason: 旧稿已说模块化有科学价值；补目的不定式与结果分词不是同一层、与可比性不等同。
- source_observation:
  - matrix: Designs are often insufficiently modular为系词主句。
  - dependency: to support补足模块化不足是相对于straightforward extensions；thereby limiting给新任务/系统的适应性后果。
- editorial_inference:
  - foreground: 工程结构的新信息是未来研究怎样继续扩展测试，不是当前样本已充分代表现实。
  - information_progression: P3.S5外推环境→S6延展成本→P4.S4研究者可接入新MAS与攻防模块。
  - research_product_value: 动态基准的价值是后续研究不必重建环境，但可扩展性本身不保证外部有效性。
  - relative_length: 此句短于带引文的外推句合理，因只承担另一个维度；不必每项列三例凑齐。
- local_replacement:
  - unit: P3.S6
  - unit_start: 0
  - unit_end: 104
  - intro_start: 2584
  - intro_end: 2688
  - source_span_sha256: acd08f5ef7b6f4a401cf655f281b2a58d1c8b1bc1a616c77df2d784197c2ff19
  - replacement: Existing codebases often lack the modularity needed for straightforward extension
  - scope_strength_and_cost: 局部保持often及所需能力门槛，主语由designs改为codebases；后续their仍指代码库，不另造速度基准。
  - selection_condition: 名词化designs of遮住工程产物时。
  - applied_sentence_or_unit_sha256: 79860b2c1ceeedb09399b9f0c300ae01c94ef5b6dac71d5d0e5682137a883d77

## ACI07

- units:
  - P3.S7
- refinement_reason: 已知MASLab强近邻；补让步结构承认的是什么、needed-to关系把缺部件接到安全研究任务。
- source_observation:
  - matrix: it lacks key components为矩阵；it回指MASLab。
  - dependency: While承认已有统一框架、输入与评价协议；needed...修饰缺失部件，under各种威胁界定安全评价任务。
- editorial_inference:
  - foreground: 语篇剩余是安全比较环境及攻击策略，不是没有任何评价工具。
  - information_progression: 两类统一不是互斥：一般任务接口已统一→威胁条件下可比研究仍缺。
  - research_product_value: 让新产品是明确扩展研究能力，而非抢占前人统一框架功劳。
  - relative_length: 让步长句容纳强答案和真实剩余；分开可易读，但先删让步会造成稻草人。
- local_replacement:
  - unit: P3.S7
  - unit_start: 200
  - unit_end: 289
  - intro_start: 2951
  - intro_end: 3040
  - source_span_sha256: d4e4a6d008bbb812035dad8e353d18dbb5071edab9e36e66343258ed8801ba66
  - replacement: needed to support comparison and improvement of MAS robustness under different threat models
  - scope_strength_and_cost: 局部保比较/改善两任务，但support明确这是研究基础设施职责，不声称基准本身直接提高系统鲁棒性；这是因果层级显化。
  - selection_condition: 要区分评估能力与直接防护能力时。
  - applied_sentence_or_unit_sha256: a6089c6dd42b26bac7d2708c9c01ad1f3691a21222bba4b5b4dcae9b1f121ffe

## ACI08

- units:
  - P4.S2
- refinement_reason: 旧P4.S2为复合分析单元；补总特性公告与covers内容的句法区别、标点/短标题职责。
- source_observation:
  - matrix: 先ACIArena stands out评价性公告，后It covers是覆盖主句；两者在历史同一分析单元。
  - dependency: Comprehensive是行内形容词标题，不是完整句；两套i.e.分别具体化surface和objective。
- editorial_inference:
  - foreground: 可检查的新内容来自covers的宾语及两轴，不是significant/comprehensive本身。
  - information_progression: P3.S2哪些场景漏掉→P4给轴与类别；B1数量随后作为资源规模证据。
  - research_product_value: 名词与分类使benchmark scope可复用；类型集合不同于统计意义上的完全均衡交叉设计。
  - relative_length: 源以行内三特性节省段落，长度因每项所需解释不同；不应把三标题各扩一段或每个分号重算独立贡献。
- local_replacement:
  - unit: P4.S2
  - unit_start: 0
  - unit_end: 55
  - intro_start: 3332
  - intro_end: 3387
  - source_span_sha256: 2a864f17093fa5866f8df6348055821efc0401feb9f8b8f0ea3dcfb1ee04da71
  - replacement: ACIA RENA has three main features:
  - scope_strength_and_cost: 局部去自评significant/stands out，保三项导航。数量three由源完整特性集给出；不删下一Comprehensive标题及覆盖范围。
  - selection_condition: 读者更需要清楚导航而非新颖性自评时。
  - applied_sentence_or_unit_sha256: 6cc203bb56f65c4f5344a5cdcdf0da4a9df5a181dcdfffa462a92ad396161d63

## ACI09

- units:
  - P4.S3
- refinement_reason: 旧稿说接口同时容纳模块正确；补purpose与ensuring的不同层级，保源强因果声明单独审其证据。
- source_observation:
  - matrix: It provides unified interface specifications为矩阵。
  - dependency: for implementing both MAS and attack/defense modules修饰规格用途；ensuring为结果分词，主张标准一致的评价。
- editorial_inference:
  - foreground: 标准化价值位于结果分词，但可操作载体是接口覆盖双方，不只任务数据格式一致。
  - information_progression: P3.S7一般输入协议仍缺安全环境→本句统一被测系统和攻防模块→B2重述科学比较效用。
  - research_product_value: 研究协议跨双方共享才能比较，而不只是接入一个工具名；§4.3共同执行入口与附录D模块职责提供机制。
  - relative_length: 一句载体+用途+后果足够；方法节再展开生命周期，不应在引言贴实现接口列表。
- local_replacement:
  - unit: P4.S3
  - unit_start: 99
  - unit_end: 146
  - intro_start: 3749
  - intro_end: 3796
  - source_span_sha256: 26c028899a7ee9cb03268a54af0e30a0faa33854a92b394a0019777dcfa4d470
  - replacement: thereby ensuring standardized, consistent evaluation
  - scope_strength_and_cost: 局部显式因果，保持源ensuring强度，不预防性改may；科学资格另记：统一接口不自动排除全部外推威胁。
  - selection_condition: 前文已给双方实现范围，需让研究效用与工程载体关系更直接时。
  - applied_sentence_or_unit_sha256: 38e58bc8b8e41ac63e307a9de840949d4e2e85a9b6a4768f4ddb189349a8fa45

## ACI10

- units:
  - P5.S1
- refinement_reason: 旧稿已认实验为证据主语；补reveal内容从句才承载知识，不能把extensive当发现。
- source_observation:
  - matrix: Extensive experiments reveal是矩阵。
  - dependency: that引导被发现内容：current MAS exhibit systemic and multi-dimensional vulnerabilities。
- editorial_inference:
  - foreground: 源选择的是性质层面的结论，不是测试量也非最高ASR；这给bench能改变认识的价值。
  - information_progression: P4交资源/接口→P5交据此能看见什么→S2给迁移失败更具体的发现。
  - research_product_value: 读者需要知道基准产出了哪类新认识，不能靠“我们进行了大量实验”结束评价贡献。
  - relative_length: 一句粗结果可由下一句具体化；如果下一句也抽象，应换成代表性对照而非堆多个最大数。
- local_replacement:
  - unit: P5.S1
  - unit_start: 0
  - unit_end: 101
  - intro_start: 3935
  - intro_end: 4036
  - source_span_sha256: 9e963cc66e7851d58326ef28ddceac6c26c905dd46e32dbc59e09ec497875115
  - replacement: Extensive experiments reveal systemic vulnerabilities across multiple dimensions of current MAS.
  - scope_strength_and_cost: 整句压缩内容从句为宾语短语，保源广义较强发现；不把系统性改为所有系统在每个测试下必然失败，外推范围单列。
  - selection_condition: 后文将具体说明维度且希望减少that层级时。
  - applied_sentence_or_unit_sha256: 46511dab1f2b1f53615065a51af0e4b3d741c264d1704bfe4aed58242e14458f

## ACI11

- units:
  - P5.S2
- refinement_reason: 旧稿泛称关系从句限定；精化为those后缩减被动修饰，以及often/sometimes的独立作用。
- source_observation:
  - matrix: existing defenses provide partial protection，and those ... often fail构成两个并列主干。
  - dependency: developed under...是those后的过去分词修饰；sometimes even amplifying附加某些情形更坏结果，非所有防御必然放大。
- editorial_inference:
  - foreground: 先给总体不足，后把迁移失败归于特定来源设置，最强反直觉结果压在句尾。
  - information_progression: P3简化设置批评→真实评测揭示防御迁移问题→P5.S3从发现提出新方向。
  - research_product_value: 同时有保护与失效，不把旧防御全写成无用；更重要是评估哪些条件会反转结论。
  - relative_length: 一句三强度层够紧；若用具名例子可增一句，但不把sometimes删掉换普遍失败。
- local_replacement:
  - unit: P5.S2
  - unit_start: 51
  - unit_end: 121
  - intro_start: 4088
  - intro_end: 4158
  - source_span_sha256: 31373897549ba6b436ddf53b04750ed84ea747f9695b0f6251d4f7afa78ced0d
  - replacement: and defenses developed under simplified or incomplete settings often fail
  - scope_strength_and_cost: 局部代词改显名词，保过去分词限定、often及尾部sometimes；不是声称全部旧防御都来自这些设置。
  - selection_condition: 句子要独立摘用或附近有多个复数先行对象时。
  - applied_sentence_or_unit_sha256: ad8f5d2054bd1d8fc95a735c2564582314d0ff53634e80ca2ef8c81006fd8598

## ACI12

- units:
  - P5.S3
- refinement_reason: 已知评测导出防御；补提案矩阵与真正方向位于relative/by/from-to，避免命名压倒benchmark身份。
- source_observation:
  - matrix: we propose ACI-Sentinel为矩阵；simple yet effective为同位评价。
  - dependency: Motivated by findings给依据；that improves...给能力；by shifting from identifying to preserving给区别性干预方向。
- editorial_inference:
  - foreground: 科学新信息是保留什么而非只检测什么；它位于从句和介词结构，并不因附属就可删。
  - information_progression: S2旧防御失败→本句方向→B3总结设计洞察；源贡献未另设第四条新防御贡献。
  - research_product_value: 基准作为发现与设计方向的来源仍居中心；提出防御是对发现的建设性回应，不是评测接口自动保证安全。
  - relative_length: 一长句足以简述辅助产物；若改成多段机制，会改写研究身份且需新完整防御论证。
- local_replacement:
  - unit: P5.S3
  - unit_start: 115
  - unit_end: 212
  - intro_start: 4372
  - intro_end: 4469
  - source_span_sha256: fb1d9fd788e1b7eaed7eee6c033f0cc35a17bab810b8f8a49ae79eced00dc806
  - replacement: by prioritizing the preservation of task-aligned information over the identification of suspicious messages
  - scope_strength_and_cost: 局部改变信息排列，保由可疑模式识别转向任务语义保留；prioritizing有“优先”而非彻底不识别的意味，不能引申为所有识别操作被禁用。
  - selection_condition: 需以前景放保留对象而非先讲被放弃方向时。
  - applied_sentence_or_unit_sha256: c3ed31496b989c4a9fb6182364a107cbd2085804be10481ed1b99eba2821e91a

## ACI13

- units:
  - B1.S1
  - B1.S2
- refinement_reason: 旧稿已有规模与轴；补第一性识别和覆盖证据的不同宾语、组织维度不等于均匀全交叉。
- source_observation:
  - matrix: S1 ACIArena is first benchmark；S2 it includes cases。
  - dependency: to best knowledge限定首次主张；organized into修饰test cases；providing评价覆盖效果。
- editorial_inference:
  - foreground: 首次性是身份主张，可查证的新内容是案例数量及组织维度；这不是完成真实部署安全事件普查。
  - information_progression: P4先给覆盖能力→B1用资源实例化；§4.3说明每例为benign task与ACI attack配对。
  - research_product_value: benchmark需要说明测什么及如何组成评价单位，只有样本量不够说明新研究能力。
  - relative_length: 第一贡献3句较长因要交身份、内容和资源状态；其余贡献可1句，不应强制等长。
- local_replacement:
  - unit: B1.S2
  - unit_start: 0
  - unit_end: 93
  - intro_start: 4647
  - intro_end: 4740
  - source_span_sha256: a7900ab4302b94459174a5aab28e0dc48f8e33e9612c2ac2a881b0494d214d86
  - replacement: It contains 1,356 test cases organized by three attack objectives and three attack surfaces
  - scope_strength_and_cost: 局部into改by以表明分类轴；保总数，未暗示每格等量、每例覆盖所有系统或每个轴组合都有同等证据。
  - selection_condition: 需要避免把两个分类轴误读成六个互斥桶时。
  - applied_sentence_or_unit_sha256: e4f87f7057aa550db9d1974ec2c83f0369bb68dc20ce40d325d4c812def6c505

## ACI14

- units:
  - B1.S3
- refinement_reason: 旧稿仅记未来释放；补同一PDF页脚代码已可用信号，必须分开源局部时态与整篇状态。
- source_observation:
  - matrix: Code and data will be publicly released：被动未来承诺，联合主语含代码和数据。
  - dependency: publicly修饰发布可访问性；句中不说明许可证、复现通过或完成时间。
- editorial_inference:
  - foreground: 这句是资源安排，不能为凑“开放贡献”升级为已验收可重复实验。
  - information_progression: 源p.1脚注另说code available；它不消除B1本句未来时，也不证明数据同样已公开。
  - research_product_value: 读者可区分存在代码可用信号、代码与数据共同发布承诺和已核验可复现三层。
  - relative_length: 一句足够，矛盾或进度需编辑时核实，不在正文塞长免责声明。
- local_replacement:
  - unit: B1.S3
  - unit_start: 0
  - unit_end: 40
  - intro_start: 4804
  - intro_end: 4844
  - source_span_sha256: 92b573a2f2a38dbecd99c928c83d8b27edd878abac2703d8720d9ff1e9947f61
  - replacement: We will publicly release the code and data.
  - scope_strength_and_cost: 整句被动改主动，保未来、公开和两个对象；这是B1局部保义，不解决论文脚注与贡献的发布时态差异。
  - selection_condition: 希望发布承诺由作者明确承担时；若写当前资源状态，先核查代码及数据再改时态。
  - applied_sentence_or_unit_sha256: 538bec3bf844c8802f64f4da0d66f37523fc95fbee8093c0df3ed2897d5ed43a

## ACI15

- units:
  - B2.S1
- refinement_reason: 旧稿已认实验可比性；補within与thereby不是同类修饰，caused-by限定作者声称避免的外推问题来源。
- source_observation:
  - matrix: ACIArena provides unified interface specifications是矩阵。
  - dependency: for给MAS鲁棒性评价任务；within给代码框架；thereby avoiding提出效果；caused by限定poor generalization的来源。
- editorial_inference:
  - foreground: 功能公告在主句，科学价值在结果分词。源不是说消除任何未来数据分布偏移，但这里avoiding仍是强作者主张。
  - information_progression: P3.S5–7环境差异/不一致→P4接口→B2归纳让比较结论有共同条件。
  - research_product_value: 环境一致性使安全结论更可比较；模块化另支撑未来扩展，不能把二者当互换修辞。
  - relative_length: 一条贡献同时归类工程与科学作用；若拆两条容易把同一接口工作重复算贡献。
- local_replacement:
  - unit: B2.S1
  - unit_start: 124
  - unit_end: 221
  - intro_start: 4971
  - intro_end: 5068
  - source_span_sha256: 90210cfa816fc59c81bb78d86a9cde0d5067795a5feeb9c55179e63fa74c19ec
  - replacement: thereby avoiding generalization failures caused by simplified or inconsistent evaluation environments
  - scope_strength_and_cost: 局部换抽象名词表达，保源avoiding强度和原因限定；并未证明未来所有MAS可外推，科学资格另列而不静默弱化源。
  - selection_condition: 要明确bad generalization对应何种结论失败、且具备源所主张的证据时。
  - applied_sentence_or_unit_sha256: 95ec1a861cc791eba128e397fcf0b52679e07c5dd5bbd8990ad55d0891939355

## ACI16

- units:
  - B3.S1
- refinement_reason: 旧稿已有资源→接口→知识贡献结构；补why/how嵌入问句的知识产物，与完成强健设计的区别。
- source_observation:
  - matrix: we offer analyses为矩阵。
  - dependency: Based on结果给依据；factors influencing修饰分析对象；together with并列洞察，why fail/how should designed为嵌入内容问句。
- editorial_inference:
  - foreground: 成果是解释与设计指导；how里的should是规范方向，不等于已实现并验证普遍鲁棒系统。
  - information_progression: P5发现与辅助防御→B3收成可迁移研究所得；Limitations明确整体robustness-oriented system design仍属未来。
  - research_product_value: benchmark的高层价值在改变我们知道什么、下一步应研究什么，不仅复用其代码运行分数。
  - relative_length: 源一长句覆盖因素、失败解释、方向三职责；若需要交最具辨识度发现，可拆2句并给一项具体结果，不能只加in-depth。
- local_replacement:
  - unit: B3.S1
  - unit_start: 49
  - unit_end: 146
  - intro_start: 5121
  - intro_end: 5218
  - source_span_sha256: cdfd692bb131ecf640cfa8300c5f02a40e9eda18381e9ca0e0b2d2047e49ee8d
  - replacement: we analyze in depth the factors that influence MAS robustness and offer insights into
  - scope_strength_and_cost: 局部跨度包括原together with并列连接，改为analyze与offer两个有限动作；后续why/how内容不变，避免无意把insights变成analyze的宾语。
  - selection_condition: 希望让实际分析动作和提供洞察分别可见、仍保持同一句知识贡献时。
  - applied_sentence_or_unit_sha256: e1ef51ae4a770c85ad0038b9b52fcc7f9d6db5a554d4f17fd13d19eb94785490


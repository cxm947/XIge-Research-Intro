# IMMI：十二个定点句内选择

- policy: Twelve targeted refinements atop the preserved60-unit baseline; not twelve newly recovered missing source sentences. Other48 units remain substantively preserved.

## P4.S5

- origin: targeted additive refinement, not replacement of substantive baseline
- retained_understanding: 旧析已识别内部缺陷反例和用法正确不足
- grammatical_matrix: 内存错误仍存在；主语是错误的存在，谓语persists
- discourse_foreground: 末部正确用法让步推翻默认前提，内部例子解释错误可藏在哪里
- new_content: 调用配对正确不保证配对函数内部实现正确
- conventional_form: In instances where条件；such as嵌入例子；矩阵后despite名词性让步
- word_proxy: 40
- length_reader_and_value_choice: 40词不是笼统长：条件、内部资源未完全释放的实例、结论和让步缺一会让读者误解被批评对象。邻接S4只说不总成立，此句负责说明反例。
- conditional_editorial_alternative: V1把内部例子后置成单独句，先给条件/结论再解释；省去例子可更短但可能使读者把内部缺陷当调用误用，需按受众决定。
- separate_evidence_scope: 此处是方法前提反例，不是声称所有函数配对检测均无用或所有正确配对都有漏洞。
- source_sentence_sha256: 2beb7ed94b11738b9cd804ed5a56c10bc6274bc4211c54742afc47a61c6ec04b
- epistemic_labels:
  - syntax: source-observed description
  - value_foreground_length_alternatives: editorial inference with explicit context, not author-intent testimony
  - scientific_claim: attributed to paper; evidence scope separate
- physical_source_pages:
  - 3
- source_page_links:
  - https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf#page=3

## P4.S6

- origin: targeted additive refinement, not replacement of substantive baseline
- retained_understanding: 旧析明确第二缺口是正确片段可得性，而非第一缺口的重复
- grammatical_matrix: 这些方法高度依赖已有正确代码片段
- discourse_foreground: 新瓶颈是能否获得比较依据
- new_content: 正确片段支撑配对识别或相似性分析两个用途
- conventional_form: Secondly切换；rely on矩阵；to facilitate/or perform并列目的
- word_proxy: 24
- length_reader_and_value_choice: 24词从反例转到另一类先决条件。两个缺口共同促成换分析单位，但不能写成第一个缺口导致第二个缺口。
- conditional_editorial_alternative: 可先列两类用途再说明参照需求；若只写现有方法不准确，会丢失后文定制代码价值的具体来源。
- separate_evidence_scope: 源文heavily rely是强依赖主张；不得不加说明地改成任何方法均绝对需要或反向降为偶尔有帮助。
- source_sentence_sha256: 75a40f96ce1ef5941d5133d7416a94e9bf2b71a3e5b492dc21fb31b39042c907
- epistemic_labels:
  - syntax: source-observed description
  - value_foreground_length_alternatives: editorial inference with explicit context, not author-intent testimony
  - scientific_claim: attributed to paper; evidence scope separate
- physical_source_pages:
  - 3
- source_page_links:
  - https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf#page=3

## P5.S3

- origin: targeted additive refinement, not replacement of substantive baseline
- retained_understanding: 旧析已把不同症状连接到所有权/生命周期模糊
- grammatical_matrix: 我们的关键观察是一个that内容命题；观察为矩阵主语，is为系词
- discourse_foreground: 真正新内容在that内：许多错误虽症状不同，却源于同类责任/生命周期问题
- new_content: 把表面错误种类改写成可比较的对象关系
- conventional_form: 系词矩阵＋that内容；despite插入让步；冒号解释fundamental issue；when限定提前释放场景
- word_proxy: 36
- length_reader_and_value_choice: 36词同时宣告观察身份、承认症状差异和命名共同关系。不是把根因直接当矩阵表语即可交代其证据归属。
- conditional_editorial_alternative: 可直接写作者观察到某关系，压缩元话语；要保许多而非全部、不同症状和提前释放情境。若删作者观察身份，则论断显得更像通用定理。
- separate_evidence_scope: 作者观察不等于独立因果识别；这里不把意图理解为可直接读取开发者心理。
- source_sentence_sha256: 2ed06b0ed484c3da34bfd0191c65e1747bb83caf60552aea59318746c4d6696e
- epistemic_labels:
  - syntax: source-observed description
  - value_foreground_length_alternatives: editorial inference with explicit context, not author-intent testimony
  - scientific_claim: attributed to paper; evidence scope separate
- physical_source_pages:
  - 3
- source_page_links:
  - https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf#page=3

## P5.S5

- origin: targeted additive refinement, not replacement of substantive baseline
- retained_understanding: 旧析已给责任重叠→双释放/UAF→损坏
- grammatical_matrix: 双重释放或UAF可能发生
- discourse_foreground: 条件把读者带到同一对象的双方责任关系
- new_content: 责任重叠可产生两种损坏症状
- conventional_form: For instance举例；if条件；could happen矩阵；ultimately resulting结果结构
- word_proxy: 30
- length_reader_and_value_choice: 30词需要同时交角色、对象、错误阶段及可能结果。它是把抽象意图变成可理解关系的一半，下一句才能形成对称对照。
- conditional_editorial_alternative: V2保留可能性并与下一句共同重述；若两个句子压成责任不一致导致所有内存错误，既丢对象也把could变成必然。
- separate_evidence_scope: 正文先排除释放后置空等安全情形；这里的例子不是任何责任重叠皆必为漏洞的充分条件。
- source_sentence_sha256: 358885050fd30b23f672d93bc25107a049066e0e4317ff926999ca719dffeee8
- epistemic_labels:
  - syntax: source-observed description
  - value_foreground_length_alternatives: editorial inference with explicit context, not author-intent testimony
  - scientific_claim: attributed to paper; evidence scope separate
- physical_source_pages:
  - 3
- source_page_links:
  - https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf#page=3

## P5.S6

- origin: targeted additive refinement, not replacement of substantive baseline
- retained_understanding: 旧析已给责任空缺与泄漏，并与上一例对应
- grammatical_matrix: 内存继续被占用
- discourse_foreground: 相反的责任配置仍可归到同一比较关系
- new_content: 双方都不承担责任时出现遗漏
- conventional_form: Conversely对照；if条件；remains矩阵；leading to结果分词
- word_proxy: 15
- length_reader_and_value_choice: 15词仅前句一半：角色、对象、错误处理场景已给，neither/this接回它们。短来自可回收信息，不是泄漏更不重要。
- conditional_editorial_alternative: 可恢复省略角色以便单独引用，但会增加重复；V2作为完整双句保留上下文。两句可交换但要重新建立this/neither的指代，不能机械倒置。
- separate_evidence_scope: 源文第一例有could，第二例用条件下的remains；保义改写不应统一把二者都改成绝对普遍结论或都降成无条件可能。
- source_sentence_sha256: 5a8286deba6652778d080fc09618d3fe7dfb3b31f270546e7adb0e337c22284c
- epistemic_labels:
  - syntax: source-observed description
  - value_foreground_length_alternatives: editorial inference with explicit context, not author-intent testimony
  - scientific_claim: attributed to paper; evidence scope separate
- physical_source_pages:
  - 3
- source_page_links:
  - https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf#page=3

## P6.S2

- origin: targeted additive refinement, not replacement of substantive baseline
- retained_understanding: 旧析已明确对象方法、LLM辅助及意图推断目标
- grammatical_matrix: 作者提出一种以对象为基础的方法
- discourse_foreground: 新分析单位处在主干，LLM增强处在补充修饰，却仍是实质设计信息
- new_content: 工具能力服务既有判据，而非替代研究问题
- conventional_form: present矩阵；augmented by为被动分词补充；to deduce给用途
- word_proxy: 15
- length_reader_and_value_choice: 15词短因P5已经教会意图关系；源句把LLM置于辅助位置不表示它科学上无价值。
- conditional_editorial_alternative: V3将目的前置，使读者先看到要推断什么，再见分析单位和增强来源。适合方法目标尚需提醒时；如果刚给过目标，会增加回顾。
- separate_evidence_scope: §4.4/§5说明LLM辅助处理隐式机制/注释，并在静态报告后使用；不把它改写为独立全核通用LLM审计。
- source_sentence_sha256: 70873c15e42d2aa7d18baa1ac8175029530f1194647fdda5fcbaf14316fe4e52
- epistemic_labels:
  - syntax: source-observed description
  - value_foreground_length_alternatives: editorial inference with explicit context, not author-intent testimony
  - scientific_claim: attributed to paper; evidence scope separate
- physical_source_pages:
  - 3
- source_page_links:
  - https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf#page=3

## P6.S4

- origin: targeted additive refinement, not replacement of substantive baseline
- retained_understanding: 旧析已保co-analysis后的精细推断能力
- grammatical_matrix: 此前共分析使内核空间中细粒度的精确MM意图推断成为可能
- discourse_foreground: 前述两种证据到推断能力的作者结论
- new_content: 精确性是作者的能力宣称，细粒度和内核空间另限定分析层次与场景
- conventional_form: This指代前述共分析；enables矩阵；名词性inference作宾语；粒度/场景限定
- word_proxy: 13
- length_reader_and_value_choice: 13词结果句把S2/S3的设计转成能力承诺，下一句转成本。它不是在这里独立报告推断准确率。
- conditional_editorial_alternative: 可明确展开This的指代而不弱化enables；若写期望可能支持，属于科学降调；若写已证明意图完全正确，则是增强。
- separate_evidence_scope: 后文检测FDR或消融指标不等于直接测出了所有意图推断的准确率。保作者能力主张与检验证据层级分开。
- source_sentence_sha256: 25153f06ca15890f6a3b4451ab05f5111d5653098c9b14964425a4129ce38800
- epistemic_labels:
  - syntax: source-observed description
  - value_foreground_length_alternatives: editorial inference with explicit context, not author-intent testimony
  - scientific_claim: attributed to paper; evidence scope separate
- physical_source_pages:
  - 3
- source_page_links:
  - https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf#page=3

## P6.S7

- origin: targeted additive refinement, not replacement of substantive baseline
- retained_understanding: 旧析已把有限局部分析连到P2规模挑战
- grammatical_matrix: IMMI的意图推断只需分析有限路径与调用轨迹
- discourse_foreground: thereby后果把局部判据的价值说成避免全核长数据流
- new_content: 新的比较单位如何缓解直接答案的成本
- conventional_form: Firstly组织；requires矩阵；only限定分析量；thereby结果分词
- word_proxy: 31
- length_reader_and_value_choice: 31词比下一条19词长，因为需交有限范围与避免全局追踪两端。前面对象方法已定义，结果不再是无根效率宣传。
- conditional_editorial_alternative: 可以把后果独立成句，让方法条件和收益分开；如果只保无需数据流，会夸大为完全没有静态数据流分析。
- separate_evidence_scope: §4/5仍有静态分析和调用深度近似；§6.2范围统计支持局部可用性，不证明所有错误可用同等小范围找到。
- source_sentence_sha256: 554430648a4ea8236da83fa9cec9136dbd4b6f941922ac54de626b7e18efd898
- epistemic_labels:
  - syntax: source-observed description
  - value_foreground_length_alternatives: editorial inference with explicit context, not author-intent testimony
  - scientific_claim: attributed to paper; evidence scope separate
- physical_source_pages:
  - 3
- source_page_links:
  - https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf#page=3

## P7.S6

- origin: targeted additive refinement, not replacement of substantive baseline
- retained_understanding: 旧析已正确区分43%减误报和约4%漏报代价
- grammatical_matrix: 引入LLM有效消除IMMI报告的43%误报
- discourse_foreground: while部分把收益之外的损失同时交给读者
- new_content: 模块提升和代价必须成对判断
- conventional_form: 主语为LLM的引入；eliminates矩阵；while incurring为从属非限定结构；only是作者对代价的评价
- word_proxy: 21
- length_reader_and_value_choice: 21词高密度句利用前一FDR句已建立的报告语境；两数字分母不同，不能因句法并置就合算。
- conditional_editorial_alternative: V4把代价独立成句，增加其可见性但保留only的作者力度。若只报告43%，会改变读者可得的评价信息；若删除only，应说明在调整评价态度。
- separate_evidence_scope: §6.5比较32个减少的误报与3个损失真缺陷；4%不是全内核FNR或另一项合成40样本测试。
- source_sentence_sha256: 2f031fd8256a94b60b379e75817bd7ff04910d91562e6cf35df9d25606dd8c24
- epistemic_labels:
  - syntax: source-observed description
  - value_foreground_length_alternatives: editorial inference with explicit context, not author-intent testimony
  - scientific_claim: attributed to paper; evidence scope separate
- physical_source_pages:
  - 3
- source_page_links:
  - https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf#page=3

## P8.S2

- origin: targeted additive refinement, not replacement of substantive baseline
- retained_understanding: 旧析已把无长程追踪、无频繁/相似参照连到定制代码适用
- grammatical_matrix: 矩阵是IMMI不需要长程数据流追踪或频繁/相似片段；源文后部直接用thus is交有效性判断，理解上承接IMMI，但未用显式协调连词
- discourse_foreground: 方法贡献要让读者看到不同于既有答案的使用条件
- new_content: 两类依赖解除后，定制代码可成为有效面
- conventional_form: Compared to前置比较；does not require为矩阵；or并列两类依赖。逗号后直接接thus is，是可理解但连接不够规范的结果谓述，不应直接当作常规协调模板
- word_proxy: 25
- length_reader_and_value_choice: 25词贡献压缩P2/P4/P6已经展开的价值。不是再列所有实现模块；省略解释可行，因为读者已见前文。
- conditional_editorial_alternative: 可把定制代码有效性置前，再交两项不依赖的依据；若独立使用，读者可能仍需知道频繁代码的参照职责。若保原序而规范化，可补连接词或完整主语；这是编辑动作，不是源句已有形式。
- separate_evidence_scope: does not require不能扩大为无需任何数据流或任何代码上下文；也不能解释为绝无假阳性。
- source_sentence_sha256: 17509c51811737dee5ff3ff559ad657057862c61b641d26418fa1932eff42ee5
- epistemic_labels:
  - syntax: source-observed description
  - value_foreground_length_alternatives: editorial inference with explicit context, not author-intent testimony
  - scientific_claim: attributed to paper; evidence scope separate
- physical_source_pages:
  - 3
- source_page_links:
  - https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf#page=3

## P9.S3

- origin: targeted additive refinement, not replacement of substantive baseline
- retained_understanding: 旧析已把对象切片和按需摘要同置实现贡献
- grammatical_matrix: 作者引入对象切片方法及新按需函数摘要技术
- discourse_foreground: 两个产物由共同分析效能目标关联
- new_content: 既照顾范围限制，又照顾跨函数信息组织
- conventional_form: Secondly引导；introduce矩阵有两个并列宾语；to enhance为目的，非独立实测结论
- word_proxy: 21
- length_reader_and_value_choice: 21词并列长技术名并非堆砌：它们实现新判据所需的精度/成本控制。具体合作机制留正文，贡献不用重新讲完整流水线。
- conditional_editorial_alternative: 若受众不懂术语，可在正文先补各自职责；不能为使贡献数量对齐而拆成两个无关研究发现。改写目的为已经最优平衡会提升证据。
- separate_evidence_scope: 正文有对象级切片/摘要设计及运行数据；不把目的结构直接读成最优性证明或独立因果消融。
- source_sentence_sha256: 2d1f673a4308803a08170db80f390336998c80e0e67242bec6587436adad7ba6
- epistemic_labels:
  - syntax: source-observed description
  - value_foreground_length_alternatives: editorial inference with explicit context, not author-intent testimony
  - scientific_claim: attributed to paper; evidence scope separate
- physical_source_pages:
  - 3
- source_page_links:
  - https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf#page=3

## P10.S3

- origin: targeted additive refinement, not replacement of substantive baseline
- retained_understanding: 旧析已把结句作为实际意义归纳而非新实验
- grammatical_matrix: 这些结果支持IMMI作为增强内核安全工具的效用
- discourse_foreground: 实际漏洞发现与维护者反馈导向工具意义
- new_content: 从结果链收束研究价值
- conventional_form: results主语＋substantiate矩阵＋efficacy宾语；as＋名词短语标工具身份，for＋动名词结构交用途；本句没有to不定式，源文数一致瑕疵不必模仿
- word_proxy: 15
- length_reader_and_value_choice: 15词短结论依赖前两句的发现/披露，不再报43%或35分钟。贡献终点是所得能用于什么。
- conditional_editorial_alternative: 可保作者归纳但明确它由前述结果支撑；若改成Linux整体安全性提高某个百分比，会创造新实验量。
- separate_evidence_scope: 确认/修复状态受投稿时间和most限制；此句不是所有缺陷消除或系统级安全增益的量化证据。
- source_sentence_sha256: f50fede3c39a120e6522956bf0026c2f30048a2a05d2f03723d9f5d068b1aa52
- epistemic_labels:
  - syntax: source-observed description
  - value_foreground_length_alternatives: editorial inference with explicit context, not author-intent testimony
  - scientific_claim: attributed to paper; evidence scope separate
- physical_source_pages:
  - 4
- source_page_links:
  - https://www.usenix.org/system/files/usenixsecurity24-liu-dinghao-detecting.pdf#page=4


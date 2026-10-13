# JailNeurons：八组定点作者选择

- distinctions:
  - source_observation=源文可核事实
  - author_explicit=作者明确理由/主张
  - editorial_inference=编辑解释而非作者意图
  - scientific_qualification_separate=证据范围判断，不反写源文强度

## JN-C01

- targets:
  - P3.S1
  - P3.S2
  - P3.S3
- status: deepen established distinction; preserve strong source attribution
- baseline_kept: 原重建已解释拒绝普通有害请求与越狱成功的行为条件不同，也已提醒不能把名称当发现证明。本次不把这些既有判断冒充新增。
- source_observation: P3.S1先以作者为主语提出神经元层面的研究视角，方式成分承载识别、利用，括号插入术语命名；限制性关系从句才界定关联的输入条件。P3.S2把旧研究放在前置比较成分里，主句以JailNeurons为主语断言它们构成不同集合，关系从句再说明所解释的安全失效现象。P3.S3明示互补定位。
- syntax:
  - matrix: P3.S1：we→take；P3.S2：JailNeurons→form；P3.S3：Our method→complements
  - subordination: S1的by短语是进入该视角的方式；命名括注与限制性that从句职责不同。S2旧机制的which从句嵌在对照一侧，新集合的that从句嵌在主断言一侧。
  - foreground: S2的语法主句突出新集合的区别，而非把新旧研究写成同一目标的强弱比较。
  - new_information: 研究解释对象从已发生的拒绝转到越狱条件下未发生的拒绝及其相关内部行为；这是之后定位工作的输入语境。
- author_explicit: 不同集合与互补关系都是原文明确主张。§7.1和A.12进一步用原始输出与反事实拒绝的解释目标差异说明这一定位。
- editorial_inference: 把旧研究放在前置对照中，可让读者先复用已有的安全机制概念，再接受新研究所解释的现象不同。这一信息安排解释研究必要性，不以“旧研究无效”换取价值。
- value_and_reader_dependency: 任务价值在于成功越狱输入需要额外检测证据；读者先需知道旧机制研究在解释何种输出。只有该条件明确，后面的不同集合才不是换名。此处不声称所有安全相关神经元与JailNeurons都已被证明完全不相交。
- evidence:
  - E01
  - E08
  - E11
- scientific_qualification_separate: §4.2.1使用因果启发的消融措辞并作强因果表述；§6.1/A.8的具体证据是相对随机对照的拒绝token概率变化。记录两者，不擅自把Intro主张降格为作者只说相关，也不把概率变化升级成完整拒绝率或唯一因果机制证明。
- transfer: 适用于近邻解释对象与本文目标对象不同的写法；若新旧工作解决同一输入输出任务，应比较能力和条件，不能靠重新命名制造互补。

## JN-C02

- targets:
  - P3.S5
  - P3.S6
- status: precise syntax correction and dependency expansion
- baseline_kept: 已建立存在、定位、部署效用的区别；本次修正矩阵主谓归属，并把两个问题之间的许可关系说清。
- source_observation: S5先把第一难题置于确认是否存在，再用冒号后的让步结构将已有表示信号与未完成的小集合定位并置。S6即使让步承认识别成功，仍把检测利用方式与OOD泛化是否成立列为悬而未决的两项。
- syntax:
  - matrix: S5：The first challenge→lies；其in补足语含confirming及其whether内容从句。S6：并列的how内容从句与whether内容从句→remain open questions。
  - subordination: S5冒号后while分句承认前人信号，主分句否定定位已完成。S6前置even-if分句是让步条件；how/whether两从句不是remain之后的宾语。
  - foreground: S5主句命名研究难题，冒号后的对照解释难题为何尚未解决。S6的两个长主语直接枚举未知量，句尾共同判定其开放状态。
  - new_information: 定位即使成功也不足以推出检测器可用或跨分布有效。
- author_explicit: 两个难题及识别之后仍需回答检测/OOD问题是原文明确结构，不是编辑另造的双挑战模板。
- editorial_inference: 让步条件将读者最自然的跳步推断拦在方法介绍之前：找到相关单元不等于拿到可迁移的判别器。把开放问题作为长主语比再写一句“仍有挑战”更具体，但增加句首处理负担。
- value_and_reader_dependency: 稀疏定位的价值是使表示信号成为可用特征；跨分布检测的价值是减少只记住已见分布的检测失败。读者必须同时知道先前已有表示信号与它尚不能保证稀疏性/迁移性，才能理解为何两个证据责任不能相互替代。
- evidence:
  - E02
  - E03
- variants:
  - JN-V01
- transfer: 当A是B的必要准备而非充分保证时可用让步假设保留B的独立研究价值；若A在该领域已公认，勿重设存在性问题。

## JN-C03

- targets:
  - P4.S2
  - P4.S3
- status: separate evidence roles hidden by a smooth transition
- baseline_kept: 保留先调查、后定位的正确流程说明；新增“承接不是证明等价”及语法主干与信息载荷的区分。
- source_observation: S2以前置目的回应第一难题，作者的调查与验证为并列主谓核心，that内容从句报告激活可分。S3以前句发现作承接背景，主句引入定位过程；其关系从句承载缩小候选集合与定位相关神经元两项作用。
- syntax:
  - matrix: S2：we→conduct / verify；S3：we→introduce
  - subordination: S2的that从句是verify的内容；S3句首承接分词结构指前句的可分性发现，procedure之后的关系从句补其操作产物。
  - foreground: S2语法主干是研究行动，关键新知却在验证内容；S3主干是提出方法，方法的解释量主要后置。
  - new_information: 可分性给出继续寻找特征的理由；具体定位程序才承诺将候选范围收缩到少量相关单元。
- author_explicit: §4.1报告ID单层线性可分性，同时报告没有单层对所有OOD集合都表现良好。§4.2把无关高维信号和单层覆盖不足列为作者对泛化失败的两个解释，并以类比提出稀疏假说。
- editorial_inference: 源文的平滑承接服务于读者沿研究进展前行，但不能在教学中把可分性读成稀疏子集已被直接证实，更不能读成OOD成功已得证。三种证据分别解决“信号可判别”“相关特征可定位”“新分布仍可判别”。
- value_and_reader_dependency: P4.S2只报告可分性的正面观察；近乎完美的ID表现与单层OOD不足这一正负证据对来自稍后的§4.1，不能当作读者在此句已经获知的全部内容。连读正文后，初步调查的任务作用是证明信号值得提取，同时暴露转移缺口。编辑若把这对结果提前，可更充分解释定位为何需要，但必须标明这是信息前移，而非源引言已经完成的解释。
- evidence:
  - E03
  - E04
  - E09
- variants:
  - JN-V02
- transfer: 适用于先有可观测现象再构建有效方法的论文。不要把每个实证观察都称为机制证明；也不要因有限证据而删掉确有依据的观察结论。

## JN-C04

- targets:
  - P4.S4
  - P4.S5
  - B1.S2
- status: explain delayed reason and antecedent scope
- baseline_kept: 保留原重建已指出的选层理由后置；新增具体回填位置、局部压缩代价及结果从句的依附范围。
- source_observation: P4.S4以回应第二难题的目的成分引出多层选择策略，没有在此句展开跨层差异。S5由作者聚合特征并训练轻量分类器，句末关系从句将这些步骤归结为高效且可泛化的检测方案。B1.S2才把不同攻击类型影响模型不同部分这一结构性发现写出。
- syntax:
  - matrix: P4.S4：we→propose；P4.S5：we→aggregate / train；B1.S2：We→show
  - subordination: P4.S5的which从句在表面上紧邻classifier，但其语义结果关联整个聚合并训练的方案；不宜教成只要用SVM就能泛化。B1.S2的that内容从句给跨层分布，with结构增加类型差异。
  - foreground: 选层句的主干突出作者的策略提出；其理由在贡献和正文中补足。B1.S2的内容从句承担实质新知，with尾部给异质性这一必要解释。
  - new_information: “多层”不仅是更多特征，还要覆盖来自不同深度的互补线索。
- author_explicit: §4.2称单层特征覆盖不足限制跨攻击迁移；§5.4的选层比较解释按深度覆盖的作用；A.12把多层平衡与冗余/信息多样性联系起来。
- editorial_inference: 引言没有严格执行两挑战两模块一一映射。P4的短选层句依赖B1和正文补解释，是源文的真实篇幅分配；迁移到没有后续回填的稿子，会只剩策略名字。
- value_and_reader_dependency: 读到P4.S4–S5时，读者已获得可分性观察，并知道检测利用与OOD泛化尚需回答；具体的单层OOD失败要到§4.1才出现。不同深度的互补关系由B1.S2及§4.2/A.12补足，读者随后才能更充分地把增加层数理解成覆盖能力而非堆叠成本。精炼备选可提前放入该理由，但这是信息前移，会重复B1的认识贡献，需连同后文调整。
- evidence:
  - E04
  - E07
  - E11
- variants:
  - JN-V02
- transfer: 若理由后置到贡献列表，必须在那里实际出现；不能仅因句式简洁就宣布局部句足够自明。

## JN-C05

- targets:
  - P5.S2
  - P5.S3
  - P5.S4
  - B3.S2
- status: correct matrix predicate; separate claim strength from evidence extent
- baseline_kept: 保留TPR/FPR共同体现任务价值、LLaVA例示与OOD优先级的既有分析；纠正P5.S2把从句谓语当矩阵谓语的简写。
- source_observation: P5.S2以结果为主语，经证据报告动词引出方法胜过已有基线的内容从句。S3前置例示和LLaVA条件后，以JDJN为主语配对已见攻击的高TPR与低FPR。S4以评价性副词提高泛化结果显著性，再以后置分词携带两个阈值及未知攻击/OOD正常数据。
- syntax:
  - matrix: P5.S2：The results→demonstrate；其内容从句：our method→outperforms。P5.S3：JDJN→achieves。P5.S4：it→shows。B3.S2：Extensive experiments→show；内容从句内JDJN→achieves / demonstrates。
  - subordination: P5.S4的maintaining结构承载量化表现，不是另一个矩阵谓语；B3.S2的对应分词结构把TPR与FPR共同嵌入表现判断。
  - foreground: 语法矩阵的报告动作与读者关注的检测效果不必是同一层。源文让证据作主语，加强结果已有实证支持的姿态，而非以方法自我宣称。
  - new_information: S3给例示数值；S4转向比ID拟合更能支持部署价值的分布迁移结果。
- author_explicit: 引言明确作强比较与强泛化主张，并给LLaVA已见>99%TPR/<1%FPR、后续未知攻击与OOD正常数据>94%TPR/<2%FPR的结果。应完整记录这种强度，不擅自改成作者仅称可能有用。
- editorial_inference: S4的回指让读者容易沿用前句LLaVA例示，但其自身没有重新明列训练配置。分析应分别记录文本的作用域提示与表格可直接定位的配置，不能假装Intro已写出所有训练前提，也不能扩展为四模型每个配置都过同一阈值。
- value_and_reader_dependency: TPR回答危险输入漏检，FPR回答正常任务受阻；两者必须共同读取。任务价值不来自最高百分比孤立出现，而来自在给定良性误拒条件下仍识别分布外危险输入。
- evidence:
  - E05
  - E06
  - E12
- variants:
  - JN-V03
- scientific_qualification_separate: Table1的表级比较口径是TPR@FPR≤0.05，不能由此单独证明Intro的<1%或<2%实测FPR。LLaVA/JDJN1对JAMLLM为0.942，而JDJN2为0.524，Janus-Pro/JDJN1为0.853。Table18的First-to-know在已见JailBreakV单元为1.000，高于JDJN的0.997/0.996；源文整体领先不能改写成逐单元严格支配。
- transfer: 证据作主语适合前文已介绍方法、此处要给评价答案的段落。只在读者确有能力恢复条件时压缩；不把所有数值条件机械塞回每句。

## JN-C06

- targets:
  - P5.S5
  - P5.S6
- status: separate train/deploy resources and causal value link
- baseline_kept: 原重建已区分少量数据与免训练、白盒与不改模型。本次把代词链、阶段边界与运行成本结论的证据角色展开。
- source_observation: S5把数据效率与计算轻量并列，训练样本规模作为数据效率的解释。S6延续单数it，以运行方式为主断言，用without限制对目标模型的修改，再以开销和实用性后置说明部署价值。原文S5写JailNeuron单数，S6沿用it；分析按上下文理解为方法/检测器，保留这一源文本用名不一致的事实。
- syntax:
  - matrix: P5.S5：JailNeuron→is；P5.S6：It→operates
  - subordination: requiring解释训练数据成本；without结构限定目标模型修改；imposing结构描述推理开销；末尾which关系从句把低开销联系实时使用。
  - foreground: 主句先突出非侵入式运行；目标模型不被修改是随后介词结构中的限制条件，低开销及实时使用的价值推论在句尾展开。该条件有重要信息价值，但不是矩阵主谓的一部分。
  - new_information: 少量标注数据、无需持续改变目标LVLM、低推理成本是三种不同采用条件。
- author_explicit: §3需白盒激活和梯度；§4.2.1在识别阶段进行激活干预，§4.2.2部署时读取所选激活并分类。Table2的低耗时来自无需生成完整响应。
- editorial_inference: 将“不改目标模型”理解为部署/目标参数条件，可与识别阶段的干预读取并存。若将其扩成整个研究从未干预激活或完全无需内部访问，就抹掉了方案可用前提。
- value_and_reader_dependency: 样本需求降低建检测器的成本，运行开销降低每次判断的成本，目标模型不被持续修改减少部署侵入性。读者需把这三类成本放到不同阶段，才不会把便宜训练当成快速推理的证据。
- evidence:
  - E01
  - E04
  - E05
- variants:
  - JN-V04
- scientific_qualification_separate: Table2在FigStep上比较单样本处理时间，1.02秒/0.26秒不是对所有正常用户端到端响应额外延迟的测量；跳过完整有害输出的收益不能泛化成所有服务请求都更快。
- transfer: 适用于同一方案有离线识别、检测器训练、线上判断三个阶段的论文。若阶段未区分，少用一个it把全部成本条件合并。

## JN-C07

- targets:
  - B1.S1
  - B1.S2
  - B2.S1
  - B2.S2
  - B3.S1
  - B3.S2
- status: whole-set author choice beyond bullet labels
- baseline_kept: 三项各两句、认识/技术/系统层次、B1补跨层理由、B2连接提纯与过拟合、B3不重复P5所有数字，均已由原重建完成。这里补出哪些重复承担回指、哪些新增承担独立贡献。
- source_observation: B1先回收P4的可分性，再增加不同攻击类型的跨层分布；B2先命名定位所得，再以方法为主语并列信号提纯与过拟合缓解；B3先回收系统身份，第二句以实验作主语汇总表现、误报及泛化。
- syntax:
  - matrix: B1.S1：We→provide；demonstrating补足认识内容。B1.S2：We→show。B2.S1：We→propose；by短语标技术路径。B2.S2：This approach→isolates / mitigates。B3.S1：We→introduce。B3.S2：experiments→show。
  - subordination: B1的with尾部不是装饰性补充，它提供不同攻击需要多层覆盖的关系；B2.S2无额外因果连词，两个并列谓语仍在同一技术对象下合并表示质量与学习泛化两项后果。
  - foreground: B1以认识为中心，B2以技术作用为中心，B3以完整检测任务为中心；动词相似不意味着三项贡献重复。
  - new_information: 贡献集合重新组织前文事实，B1.S2还补足P4未展开的设计理由；并非每句都首次出现才算有贡献。
- author_explicit: 源文实际把独立结果段P5放在贡献列表之前。B3的简短评价可由P5的实验范围、数值和消融支撑。
- editorial_inference: 若在新稿中删去P5、又照搬B3的简写，会同时丢失代表结果和解释条件。列表长短应按先前已交的信息分配；两句只是此文的描述性事实，既不是贡献条目字数上限，也不是应复制的节奏规则。
- value_and_reader_dependency: B1给“值得取什么信号”的认识，B2给“怎样从高维特征中拿到它”的技术，B3给“拿到后完成什么判断”的应用。价值链与读者缺失关系是一体的，不能只按发现/方法/实验三个标题分槽。
- evidence:
  - E02
  - E04
  - E09
- transfer: 适用于前文已有充分评价的贡献收束；若贡献是正文唯一结果入口，则需补回有代表性的结果和必要条件。不得把该源文的实际结构悄悄改说成它没有独立结果段。

## JN-C08

- targets:
  - P5.S4
  - B3.S2
- status: new evidence boundary and contextual result-selection choices
- baseline_kept: 原重建已记录训练数据影响与常规良性集范围，但尚未把A.14压力集与强Intro摘要之间的关系交代清楚。
- source_observation: P5突出分布外TPR/FPR的联合结果；B3压缩为高TPR、近零FPR与强泛化。A.14另报JDJN1在OR-Bench/XSTest上：LLaVA的FPR为0.390/0.170，Janus-Pro为0.280/0.090。
- syntax:
  - matrix: 保留P5.S4与B3.S2原来的强评价骨架，数值范围问题不靠改矩阵动词自动解决。
  - subordination: 近零FPR位于B3.S2的后置表现结构，仍是实质主张，不能因其从属地位而免于范围核查。
  - foreground: 源文选择典型良性分布的低干扰与检测泛化作主要结论，压力集结果在讨论/附录承载适用边界。
  - new_information: 扩大良性分布范围后，低误拒并非在所有测试集上维持同一水平。
- author_explicit: §7.3/A.14把压力集与典型使用区分，称其目标是一般良性用户体验；这些是作者的解释。文中关于商业模型比较及现实用户影响的论断未在本次独立外部核验。
- editorial_inference: 这些结果不推翻常规数据上已观察到的低FPR，却足以阻止分析者把近零FPR扩成任何正常分布都近零。是否放入新稿Intro应由新稿声称的范围决定，不能据此建立所有Intro必须附一条压力集免责声明的规则。
- value_and_reader_dependency: 若读者要判断一般测试分布的检测效用，主要TPR/FPR对照优先；若主张是面向广泛无害请求的可靠部署，压力集直接影响任务结论，应与主要评价一起交代。任务收益和读者所需条件共同决定取材，而非取最好数字或罗列所有坏结果。
- evidence:
  - E06
  - E12
  - E13
- variants:
  - JN-V03
- scientific_qualification_separate: A.13还说明回答含混或回避、未明确拒绝有害请求的样本，在作者的标注规则下会被计为越狱；检测错误因此部分受标签定义影响。这里不把未明确拒绝说成已经发生拒绝，仅记录评价口径，不否认所有检测收益，也不复述任何危险样本。
- transfer: 区分一般测试集、明确压力集与真实流量证据；单篇论文对真实用户影响的解释不等于真实部署测量。


# Cried Wolf编辑选择册

分析与源审读日期：2026-10-06。近邻 [49] 的版本、有限阅读范围及无原始字节哈希限制见 profile.zh.md 与 source-ledger.json。

本册标题中的论文简称仅用于定位；所有英文选项均为2026-10-06 原分析的原创编辑表达，不是源句、不代替原文，也不宣称已经测试写作收益。原文事实与证据见profile.zh.md及source-ledger.json。本册将“选择讲什么”与“同一命题怎样实现”分开，避免拿句式变化冒充研究定位变化。

## C1 先承认已有保护，还是直接给剩余

定位：P1.S2及邻接S3。固定命题是通用对齐提供基础保护，但往往不能充分适配应用特定政策要求。频率限定属于源文命题，不能压成一律不足。这一对照保留前人的实际能力，不增添新的实验结论。

局部跨度三选：

- “despite the protection supplied by general alignment”：把承认部分压为介词结构，留出主句给适配不足。适用于上句已经交代对齐；代价是基础保护的来源和研究历史被背景化
- “although general alignment supplies a baseline of protection”：用有限让步从句显式给施事和功能。适用于读者可能把剩余误解为对齐无效；比短介词结构多一个命题展开
- “beyond the baseline protection of general alignment”：把关系改为在已有能力上进一步要求。适用于强调补充职责而非失败的上下文；它只适合作连接片段，不能单独保持原有“不足”的断言，后句必须实际写出剩余

完整句选项A：General alignment establishes a safety baseline, but application-specific policies often demand further control.

完整句选项B：Although general alignment supplies basic protection, it often falls short of full compliance with application-specific policy requirements.

A用并列给两个命题较接近的地位，前景偏向补充控制需要；B把已知能力从属化，使未满足要求成为矩阵断言。两者都不宜被改成“对齐无法保护应用”，那会改变强度。选择A也不自动意味着下一句必须提外置组件；下一句应交付当前论文真正采用的答案。

## C2 研究缺口的三个内容分支，不能当成保义改写

定位：P2.S2–S3、P3.S1、B1，与[49]的窄核查。这里变化的是主张范围，三者不是同义句。

分支A，保留源文的历史叙事作为分析对象：以越狱关注有害内容被放行作参照，再把安全内容被误拒放在前景。适用于讲清该篇实际如何引入读者。成本是其广泛“未研究”表述必须与[49]分开校准，不能当作已核实的新颖性写进新稿。分析中可忠实描述这一路径，但不提供冒称全新方向的可套用句。

分支B，近邻可见时的定位选项：

Prior research already connects safeguard false alarms to denial of service, including settings in which users write their own requests. Here, the adversary supplies the image without modifying the request template or the guard model. The central question is whether false rejection persists across the accompanying, unseen user requests.

选择条件：读者知道广义假阳性DoS，或作者已发现近邻足以反驳宽泛空白。新增信息是图像载体且无需改变文字模板／模型这一控制边界，成本是必须花一句承认已有答案，且这段本身不证明较窄设置绝对首创。用户独立撰写主体文字是与近邻共享的条件，不能单独充作区别。

分支C，方法能力成为主焦点时的定位选项：

The availability risk of false rejection is already established. For image-based interference with multimodal guards, however, success on familiar prompts does not answer whether the same image will disrupt independently composed requests. This setting calls for evidence of generalization beyond the prompts used during development.

选择条件：论文推进主要在未知请求泛化而非威胁命名。成本是弱化新威胁叙事，要求方案段和贡献同步围绕泛化；不能只替换gap而仍在B1宣称发现一切假阳性DoS。

此处对[49]的使用只支持一般问题已被研究及与本文操控载体不同；近邻模板注入设置中的主体请求也由用户独立撰写。不据该单篇文献宣布本文所有更窄新颖性均成立或均不成立。近邻依据为[arXiv v3 §1、§3](https://arxiv.org/html/2410.02916v3#S3)。

## C3 同一控制条件的语法与信息前景

定位：P3.S3–P4.S3。固定内容是图像可能被公共传播后由用户加入自己的请求，攻击者不知道也不能选择未来文字，因而方法需要跨未知请求工作。这是场景约束，不是算法流程。

局部跨度：

- “with the accompanying text chosen independently by users”：把独立选择压为伴随条件，适用于主句已经承担图像传播；成本是限制很容易被读者当成边缘背景
- “because users choose the accompanying text themselves”：因果前置，适用于后主句要引出稳健性要求；成本是需要另交代攻击者只控制图像
- “across requests the adversary neither sees nor selects”：把未知与无控制嵌在任务范围中，适用于已经建立传播流程的短贡献；成本是省去了条件的来源

完整版本A，施事控制权优先：Users supply their own text when they reuse a distributed image. The adversary therefore needs the image’s effect to persist beyond any requests available during development.

完整版本B，要求优先：Robustness to unseen requests is essential here because the adversary controls the image but not the text that users later attach to it.

完整版本C，比较边界优先：High success on familiar requests is insufficient when users can pair the image with independently chosen text.

A适合读者未见场景，两句交完整推导；B适合任务已知但要求需要强调，一句完成要求及理由；C适合刚给已知提示结果之后，用来限制其解释而不是独立介绍整个威胁。C少讲攻击者访问与未来不可见性，所以它是特定前文下的压缩，不是任意位置可与A互换的同义式。

## C4 长方案句要拆在哪里：矩阵、前景与完整段落

定位：P5.S1–S6及正文§4.3。固定核心包括视觉语义与审核判断相关、从多幅参考图提炼共享性质、未来提示泛化、正文还有决策校验。不同版本下有意保留作者的有效能力主张；有关假设是否被充分证明，放科学校准，不把所有谓语加上may。

局部跨度：

- “the common structure represented across the reference collection”：前景在集合共享性质，适合先解释为什么不追随一个实例；代价是尚未命名具体表示层
- “a visual representation that generalizes beyond the development prompts”：前景在任务能力，适合读者已理解分布选择；代价是抽象了概念学习的来源
- “paired with a check of the guard’s actual decision”：把正文决策校验压成高层附加项，避免读成纯表示方法；代价是这已是正文补充，不能声称源引言原句已显式说出

完整段落A，洞察→设计→能力，保留源文的解释顺序，但补回正文关系：

We introduce USD to induce false rejection across user requests that are unavailable during development. Its design draws on the guard’s association between visual representations and unsafe content. Rather than treating one reference image as the complete target, the framework uses the shared structure of a reference collection and pairs this representation-level objective with decision checks on development prompts. Together, these elements support generalization beyond the development prompts. Restricting the reference collection also enables category-specific outcomes.

选择条件：读者需要先明白为什么视觉集合有用，但不能被暗示为完全没有文字校验。这里共五句，较原P5少一个强行为观察和机制编号，代价是少了“极端图像跨文字被拒”的直觉桥梁，并且是引言与正文整合的编辑段落，不是原P5的严格保义替换。

完整段落B，已有两路线→互补缺陷→合并设计：

USD combines a collection-level visual objective with verification at the guard’s decision boundary. The former moves the design beyond the peculiarities of any one reference image; the latter checks that the representation change has the intended classification effect. The method thus retains a decision check on development prompts while achieving false rejection on previously unseen user requests. A category-restricted reference collection provides an additional form of control over the reported risk label.

选择条件：前文已经公平介绍输出路线和单图特征路线，读者此时最缺合并理由。四句把互补关系前景化，减轻原长句的双对比嵌套；成本是开句较技术化，省去原洞察与具体观察，不能在没有前文铺垫时独立替换。它把正文混合设计纳入，所以与A同属内容补足方案，不是纯句法改写。

局部紧凑的双机制表达C，改变P5.S4的句界并压缩解释：

The design makes two linked choices. It directs the representation toward visual risk semantics instead of depending on a prompt-specific output target. It also draws on a collection of reference images rather than reproducing the features of one example.

选择条件：在连读P5.S5后，允许压缩重复解释，需要把原来的冒号—编号—分号长句改为三句。信息前景仍是两个选择，矩阵导航仍单独存在；成本是把强效果解释留给P5.S5，并可能继续让读者误解为无提示训练。由于压缩了原句的统计性质与效果解释，C不是孤立句层面的严格保义替换。因此C不应作为本报告推荐的完整方法说明；需要准确描述整个实现时，选择A／B或另补正文校验关系。C所保留的是源引言的抽象二选关系，不是新增无提示实现的事实。

三个版本展示真实取舍：读者缺直觉时保桥接，缺互补机制时给整合，只有句法太重时改变句界。不能给三组同义动词便宣称获得了三种研究内容选择。

## C5 贡献集合中的任务答案与结果范围

定位：B1–B3、表1–3。下面三种评价项选择改变证据集合，所以不是严格同义替换；都保留有力结果，不把科学校准写成自我消解。

选项A，四模型主要任务全范围：

We evaluate USD on four guard models using image-specific requests withheld from development. Across the tested datasets and perturbation budgets, the resulting false-rejection rates range from 70.4% to 85.9% and exceed the comparison methods in every corresponding condition.

选择条件：评价项要概括完整表1而不是单模型代表例。成本是下界低于原引言数字，但范围与对象明确；未包含类别扩展，需要前文或另句回收。该句不声称所有样本对所有模型均有效。

选项B，代表性场景加同条件最强比较：

Using image-specific requests that are unseen during development, USD reaches an 82.8% false-rejection rate on TextVQA with Llama-Guard-3-Vision at the larger tested budget. This is 14.1 percentage points above the strongest comparison method in that condition.

选择条件：读者更需要一个可理解、可核对的任务答案与幅度。成本是单例不能独自代表四模型广度，评价范围应由此前一句交代；“larger tested budget”只在前文已交两种预算时可用，独立摘要应补明确预算。选该格不能抹掉其他模型的较低成绩。

选项C，主要任务与结构化类别能力并重：

Evaluation with previously unseen, image-specific requests shows that USD induces false rejection across all four tested guards. In separate category-targeted tests on two guards, success rates of 76.7%–80.6% also establish control over the risk category assigned to benign images.

选择条件：应用关心错误风险标签，而非只有通过／拒绝。成本是主任务缺少数字幅度，需要此前或后文给主要率；“separate”防止把四模型主评测误并为四模型类别评测。若贡献只许短句，宁可选择一个主要回答，也不要把范围不兼容的数字拼起来。

贡献完整分工选项，供检查列表内是否重复，而不是强制新稿照抄：

- 威胁所得应交多模态图像载体且无需修改文字模板／模型这一控制设置，以及假阳性如何阻断服务；保留用户文字独立这一任务条件，但不把它单独作为新颖性；不要仅以新名称或广义DoS首创充数
- 方法所得应交集合级视觉目标与审核决策校验如何共同支持未知请求，不需把每个实现组件另列贡献
- 评价所得先交为何用户模拟能辨识所需泛化，再选A／B／C对应的主要任务答案。评价可以比前项长，新增职责决定篇幅

## C6 强度、句法与科学限定要各归其位

源文B3.S2在主成功率后混接分词和有限动词。若仅修语法，先保留原主张范围作来源记录；若实际交稿，再同时解决其数字范围问题。不能以“我只是润色”为理由保持可见数值错误，也不能以发现范围错误为理由改成没有结果的空泛评价。

局部平行实现可以是“achieves …, exceeds …, and supports …”，也可以用“achieves …; separate tests also show …”。前者适用于三项共享同一证据对象和范围，后者适用于类别扩展来自不同模型子集。本源恰好需要注意后一条件，因此短而整齐的三谓语并列未必是最准确的选择。

作者关于跨提示稳健、分布概念学习和新威胁的重要主张应作为源文明确命题保留。科学评述则另说白盒、模拟请求、先验近邻、范围不一致和未经人类实验验证的后果。好的编辑分清主张与支持它的边界，而不是在每个动词前加不确定词。

## 选择册边界

这里没有完整原文句，没有重建主源Introduction供替代阅读，也没有攻击参数、优化步骤、代码或部署指令。局部英文跨度是表达实验，不是可复制的技术配方。统计长度和覆盖数在ledger中仅帮助定位；没有设统一句数、词数或结果数字配额。

# TWIST：作者主张与独立科学资格

## Q1

- locator: Introduction P1 pp1/11025; §2.1 pp2–3; §4.1 p3/11027
- source_claim: 作者将生成成功主要归于组件，强调文本编码器跨模态连接的关键/必要作用
- scientific_qualification: 这些是作者任务解释与位置动机，不是本轮独立证明所有T2I架构均必须依赖同一种编码器或某唯一层。
- writing_use: 先写接口做什么、为何关乎输出质量，后文局部位置才有读者已有知识可回收。

## Q2

- locator: Introduction P2 p1/11025; §3 p3; §5.3 pp6–7; AppendixA.1 p12
- source_claim: 从零训练代价使典型使用者转向预训练组件；攻击资源另有节约
- scientific_qualification: P2上游编码器训练、P5恶意微调和方法局部优化是三种任务的成本。不能拿数周/月与25秒直接算同一任务提速。
- writing_use: 上游成本说明共享入口为何现实，攻击侧成本说明方法为何适合较弱资源；两类价值相接但不等同。

## Q3

- locator: Introduction P2.S4/P3.S1 p1/11025
- source_claim: 下载量被作者用来凸显广泛采用和可靠性；下一段再讲验证不足
- scientific_qualification: 下载量直接支持采用/暴露规模，不能单独证明安全可靠。可靠性推断是源文内容，保义变式必须归属保留；审慎评价另列。
- writing_use: 数字之后的解释分词改变读者印象，并为下一段转折蓄势；学习其数据→意义的位置选择，不自动复制其证据强度。

## Q4

- locator: Introduction P3 pp1/11025; paper cites Zeng2025/JungleLee2023
- source_claim: 疑似动态后门的单模型案例及逾33K月下载
- scientific_qualification: 本轮未独立复查平台历史/被引调查；高可能性≠已确认，下载≠受害者或独立用户。本轮保持论文时代归属。
- writing_use: 同一种下载数在P2是正常采用证据，在P3是疑似风险的触达规模；由前文决定数据职责。

## Q5

- locator: Introduction P4 pp1–2; §3 p3
- source_claim: 触发输出被改变而正常输入仍应近似正常；识别误判是动机例
- scientific_qualification: 人脸识别例跨出了本文T2I实证范围；触发与正常性能为不同要求。未测人脸识别，不把内容完整性动机写成已发生事件。
- writing_use: 条件从句交激活边界，结果分词交应用后果；若删条件，威胁含义从隐蔽条件行为变成持续破坏。

## Q6

- locator: Introduction P5/P7 p2; §2.2 p3; §5.1 p5; Tables1/7 pp6/14
- source_claim: 引言较概括地称既有方法依赖大量数据/微调；又给U-Net矩阵稳定性泛化解释
- scientific_qualification: 实际基线异质：Rickrolling用635561样本，Personalization5，EvilEdit0且直接权重编辑。因此不能把P5/P7的概括当每种近邻全有同样限制。原归属型变式仍保其措辞强度；科学评价在此限缩。矩阵不稳定性归因未由本轮独立机制实验验证。
- writing_use: 按信息、运行成本、能力泛化分别组织最近答案，避免把它们压成“都不高效”；比较句需要准确的各自基线。

## Q7

- locator: Introduction P6/C1/C2 p2; §4.1/4.4 pp3–5; §5.7 p8/11032
- source_claim: 编辑路线及瓶颈MLP位置被作者作为首次/创新/关键认识；少量编辑带控制
- scientific_qualification: 首次性是作者声明，本轮未全球文献复查。瓶颈位置有选层实验支持，但极少量编辑不等于全局数学最小或所有模型同一层普遍最优。参数个数只支持干预范围大小，不单独证明扰动范数极小、该位置唯一或因果机制完全成立。保真替代表述保作者强度，不暗加保证。
- writing_use: 核心不是列方法名，而是位置→跨模态接口→输出控制；短结果句把长观察句转成任务能力。

## Q8

- locator: §3 p3/11027; §4.3 p4/11028; §5.1 p5; §5.3 pp6–7
- source_claim: 威胁模型不访问开发模型所用训练数据；编辑免去恶意微调但仍有目标/上下文/教师和优化
- scientific_qualification: 无训练数据/无额外训练不等于零信息、零优化、无模型访问或不需目标上下文。此处仅分析信息条件，不重述实现步骤。
- writing_use: without条件应保住资源边界，不能被笼统“简洁高效”吞掉；也不能把原数据条件自动扩成最弱访问假设。

## Q9

- locator: §5.1–5.2 pp5–6; Tables2–4 pp6–7; §5.5–5.8 pp7–9
- source_claim: 模型版本、显式触发或隐式（语义）触发、目标/场景覆盖分别支持作者泛化判断；指标包括成功、特异、保真、资源
- scientific_qualification: Table3在固定一组语义目标上列五模型，ASR100/100/98/98/95%；不是P8的91%统计集合。ASR用分类模型评判生成类别，不是人评；CLIP与FID另有对象/汇总。源§5.7“四模型均超过95%”与列五模型及FLUX等于95%有文字张力，不能照抄为严格阈值结论。
- writing_use: 先给范围，再给任务答案，最后贡献补触发/语义轴；多个“泛化”证据需要说清变化的是哪个维度。

## Q10

- locator: §5.3 p6/11030; Table1 p6; AppendixA.2.1/Table7 p14/11038
- source_claim: 引言报平均ASR91%；Table1标题称五目标比较，正文提四个对象目标对
- scientific_qualification: Table7第五个风格目标的ASR为缺测符号；TWIST前四项93/89.2/97.2/84.6平均91。故ASR平均是四个对象对的算术平均，不能叫五目标平均ASR或跨全部模型平均。CLIP/FID等列另含风格目标，不能让表标题替代逐列口径。
- writing_use: 91%展示任务控制效果；其选择使成功前景化，不证明每个资源轴最优或任意目标保证。表格口径核对只服务于保护该写作选择的科学范围。

## Q11

- locator: Table1 p6; §5.3 pp6–7/11030–11031; Table7 p14; AppendixA.1 p12
- source_claim: 引言称八倍参数减少带来效率；正文同类权重编辑基线为EvilEdit
- scientific_qualification: EvilEdit改动1.92e7参数，TWIST2.36e6，比值约8.14，约为原来的1/8；时间分别1/25秒。Rickrolling53秒、Personalization118秒，所以TWIST非全基线最快。样本列两种编辑法均0。FID的0.37增量也不是最小（EvilEdit0.06）。成本列在论文硬件条件下记录，不作价格/能耗保证。
- writing_use: 参数个数回收P6局部编辑中干预范围的部分，与成功率分别支持改动规模和任务效果；不单独验证扰动幅度或位置唯一性。位置优势另有§5.7选层证据。本引言未报告25秒，摘要和正文报告了它；为何引言优先参数数目属于读者需求的编辑解释，非作者动机事实。

## Q12

- locator: §5.4–5.9 pp7–9; §7 p9/11033; AppendixA.2.1 pp13–15
- source_claim: 显式/隐式语义触发与多视觉语义层次广泛有效；作者称容易且高泛化
- scientific_qualification: 不同目标及LoRA后续改动会影响表现，部分针对性LoRA结果为0。正常样本质量近似不等于完成现实受害者检测实验。C3的容易是作者定性价值判断，未在本轮当作用户操作可用性测量。
- writing_use: 贡献C3新增的不是另一个大百分数，而是何种变化仍能做成任务；保持这一维度能避免将结果与贡献误判重复。


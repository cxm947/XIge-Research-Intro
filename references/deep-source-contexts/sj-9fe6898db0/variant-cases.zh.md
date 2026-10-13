# 五个有上下文的表达决定

原分析与源文审读日期：2026-10-06。定位仅承诺 P/S 与物理页；历史栏位冲突尚未核定。

非阻塞复用边界：IG-A-R3，V3.C 的 “interchangeable” 仅指目标与载体可配，不能推出同效、同成本或同安全边界，迁移时优先使用 “three carrier options”；IG-A-R4，Table 11(a) 各比率不得推定共用 12 篇分母。

这些备选仅用于观察作者选择和编辑后果，不是新论文正文，不是源文引用。A/B/C 不表示优劣排序；每一组的目标位置、信息前提和作用不同。选择内容分支后才选句式，不以同义词轮换冒充设计选择。

## V1 缺口段：保留已有答案，还是提前交部署条件

目标：P3 整段。前文已定义上传后直接提交评审的行为，并解释对学术判断的担忧；后文 P4 要引出内容生成和文件内部承载。固定命题：已有隐藏指令可影响输出；长学术文稿和可清洗的内容/文件结构构成当前障碍；所需框架应同时适配对象和文件结构。本文已有方法的具体全球新颖性不由此例重新核验。

A. 接近源段职责的完整替换，适用于尚不了解已有可行方向的读者：

A plausible committee response is to place instructions in a manuscript so that an automated service changes the review it returns. Existing document-injection techniques provide a starting point, but academic papers introduce difficulties that short documents do not. Their length and organization can reduce the influence of inserted material, while repetitive content and separately added document structures make that material easier to remove. The remaining problem is to develop a defense that addresses both the manuscript-processing conditions and the structure of the file carrying it.

保留：先承认能力，再诊断，再收束。代价：省去源段单列的“尚未系统表述为安全问题”主张，不能作为完全保义的逐句替换；若此项问题形式化本身是贡献，应在相邻句补回。

B. 局部压缩，适用于此前已经解释过隐藏指令方向：

The remaining difficulty is not simply to place a directive in a PDF. A defense must remain effective when a long paper is processed and when conspicuous additions are removed. These requirements call for coordinated choices about the inserted content and its representation within the document.

这里不是源全文逐句保义：它压缩 P3 为设计依赖，删除来源归属和原有方向的铺垫；第三句是编辑综合正文后的关系判断，不能标成作者明确提出的单独挑战。收益是承接快；代价是强近邻若尚未交代，读者无法判断剩余究竟是什么。

C. 整段部署导向重构，适用于面向委员会决策者的技术概述：

A committee can prepare the document distributed for review, but it cannot choose the external service or the request used by a reviewer. This makes a document-side intervention attractive. Existing injection techniques establish that such material can affect generated output, yet repeated wording and easily isolated additions are vulnerable to removal, and long papers create further processing difficulties. The design must therefore use the committee’s control of the document while tolerating uncertainty about the subsequent review workflow.

这是正文知识前移且焦点改变，不是纯润色。它把 §3.1 的权限/未知信息放在缺口前，便于理解黑盒价值；代价是较弱化 PDF 结构适配的收束，后段必须重新交清表示层依据。不能迁移到委员会无权处理分发文件的场景。

## V2 方案的属性句：同一性质为什么服务两个目标

目标：P4.S1–S2，局部替换；上文已经指出学术文稿适配与文件结构缺口，下文要介绍两部件和三机制。固定命题：本文交付委员会端框架；其依据是文件内部表示与渲染可分离；机器提取与人类呈现可被区别处理。以下不是普遍效力保证。

A. 常规交付主句，随后给设计依据：

We present a committee-side framework that uses the distinction between a PDF’s internal representation and the page shown to a reader. This lets the defense affect extracted text without changing the visible manuscript.

适用于方法首次出现。矩阵先交产物，第二句把性质变为能力。代价：省掉源句黑盒、跨 venue 标签；只有这些属性已在邻近处交代或不是当前信息重点时，才可这样压缩。

B. 局部性质前景，适用于前文已经命名框架：

The key opportunity is that a PDF can present the same page while exposing different text to a parsing system. IntraGuard uses this separation to intervene in outsourced reviewing while preserving the manuscript’s visible content.

这是保留核心机制关系的重组，非实施说明。前景从“我们交付什么”换成“为什么可做”；代价是不能独立替代一个尚未命名总体工作的方案段。visible 限定保留了呈现层强结论，没有宣称所有交互完全相同。

C. 带适用条件的能力句，适用于正文设计概述或部署摘要：

For services that derive review context from extracted document text, the committee can use the PDF’s internal representation as an intervention point. IntraGuard does so while retaining the page appearance presented to human readers.

正文解析条件前移，因此更窄、更具体，不能称作源引言不改变范围的改写。条件从句给适用域，主句前景是委员会能力；代价是丢失完整总体产物声明，而且仅靠这两句不能说明两策略与三机制的关系。

## V3 完整方案段：部件组织如何避免三阶段误读

目标：P4 整段的结构示例。前文缺口已足够具体；后文评价会同时测输出干预、呈现和成本。固定关系：两部件；内容池服务预防和事后核查；三种机制可承载任一策略；机制利用共用文件结构；不能改为三种依次必经阶段。所有样例均为编辑概述，省略原段的具体机制名和低层操作信息。

A. 总体→性质→两部件的完整段：

We present IntraGuard, a framework for committees seeking to reduce fully outsourced reviews. It works on the document before distribution and uses the separation between the page a person sees and the text a service extracts. One component prepares varied defensive content for two outcomes: discouraging review generation or leaving a signal that can be checked in the returned review. A second component provides three ways to carry that content within the document. Either outcome can use any of these mechanisms, allowing the output objective and the document representation to be chosen separately.

正文中分发前的时点被前移；因此不是完全保持原引言信息量。收益是行动者和正交关系易读；代价是跨 venue、低成本的具体性质及其文件操作依据被省去，应由下一句或评价承担。

B. 用户目标→共同依据→设计分工的完整段：

IntraGuard gives committees two forms of intervention: an immediate change to the service’s response and a signal available for later checking. Both rely on a document property that separates machine-readable content from visible page appearance. The framework separates the preparation of varied defensive content from its placement within the file, and offers three alternative mechanisms for the latter. This organization supports either intervention objective without committing the committee to one document mechanism.

适用于上一段已明确交付框架且读者最关心任务能力的场景。内容前景改变为两种结果，组成关系仍成立；代价是立即响应变化不如拒绝/警告具体，且“信号”若未定义需补明为预定文字，避免被误读为服务日志或网络监控。

C. 短段，适用于已有技术背景的读者：

IntraGuard separates two decisions: what response the committee seeks and how defensive content is represented inside the PDF. Its content-generation component supports prevention and later verification, while its document component offers three interchangeable carriers for those objectives. The framework uses the difference between internal text representation and rendered appearance to preserve the visible manuscript during this intervention.

这是有损压缩，不能说与源段完全等义。“interchangeable”仅指能够承载两类目标，不表示效力、成本或安全边界相同；实际应用时如易产生此误解，应改成 “three carrier options”。该形式适合已交待三机制差异的摘要，不适合首次给非技术读者介绍。

## V4 结果与贡献：保留原强比较，并选择在哪里交答案

目标 A/B：P5.S2–S3；目标 C：删除独立 P5 后的最终评价贡献。前文已定义显式与隐式策略。固定证据：Table 3 的最好机制平均 DSR 为 0.76/0.84，均高于四基线对应平均；六种阅读器/浏览器呈现一致；对应机制平均处理时间 1.02 秒。以下样例不把全部 17,844 案例当同一分母。

A. 同一局部的精确汇总对象版本：

Across the seven tested settings, Layer Cake averages a 76% success rate for the explicit strategy and 84% for the implicit strategy, exceeding the corresponding averages of all four baselines. The protected documents retain their rendered appearance in six readers and browsers, and this mechanism takes 1.02 seconds per manuscript on average.

把正文中最强机制的身份前移，保留强比较而不扩大到每个单元。代价是由框架整体转为代表机制，下一句若回到全部三机制，应重新标明主语。该句不涵盖独立适应测试或真实评审行为变化。

B. 局部任务答案前景，适用于不希望一开始堆数字的结果段：

The evaluation shows that document-side intervention can change automated review output while preserving the visible page. The strongest mechanism attains average success rates of 76% and 84% for the two strategies, above all four baseline averages; its average processing cost is 1.02 seconds per manuscript.

第一句的 evidence-reporting 矩阵承载归属，内容从句承载任务答案；“can”是存在性能力，并非零风险退让。代价是省去 7 个设置和六种阅读器，只有此前已经给出覆盖范围时适用；two strategies 也必须有明确先行说明。

C. 结构改变后的完整末项贡献：

We evaluate the framework across seven commercial chatbot settings and documents from twelve venues. The strongest mechanism averages 76% and 84% success for the explicit and implicit strategies, respectively, outperforming four baseline averages while retaining the rendered page in six readers and browsers. Additional tests characterize adaptive failure boundaries and the benefits and limitations of combining mechanisms.

适用于拿掉独立结果段的文章结构；因此不是对原 P10 的机械精简。新增职责是交主要任务答案，并把适应与组合认识概括到合适强度。代价：源代码发布和成本未进入此项，应按该稿贡献中心决定是否补回，不能同时声称此项覆盖原 P5/P10 所有事实。

## V5 组合结论：句法焦点和完成状态必须同时正确

目标 A：P5.S5 局部；目标 B/C：以 Appendix I 为重点的结果摘要。前文已说明测过不同适应条件。固定区别：Intro 的矩阵是证据报告，互补在内容从句中，组合可行在结果补充中；正文已有组合实验，但测试范围有限且有弱环节。

A. 原 Intro 关系的局部重组：

The mechanisms fail under different conditions, supporting the use of combinations tailored to the deployment setting.

由证据报告句改成直接陈述发现。代价是删除报告归属，并把场景定制这一正文含义前移；不是“所有组合有效”的断言，也不能独立承担完成状态说明。

B. 完整的已测结果与边界双句：

The tested ensemble retains substantial protection against all five evaluated sanitization methods on Doubao. Its performance nevertheless varies across services, and combining mechanisms does not consistently improve on the strongest individual option.

适合组合成为读者当前问题时；用已测结果支持积极结论并给同一主张所必需的边界。代价是从原引言的机制互补推论转成附录实证总结，不能当作纯句式替换；all five 指这五个已测条件，非所有攻击或五种通用类别的所有变体。

C. 有采用决策的信息前景：

Ensemble deployment is an evaluated option rather than an untested extension. The results support combining complementary mechanisms for some sanitization conditions, while showing that an unreliable component can limit performance on another service.

适用于纠正“组合只是未来工作”的文献评述，第三人称评价而不是作者引言自述。代价是第一句更偏向完成状态澄清；若上下文从未存在该误解，应删去，以免凭空制造对立。weakest-component 的归因来自作者对 Appendix I 的解释，不是原分析新做的因果实验。

## 用法边界

局部改写只承诺该处固定命题；完整段落替换仍可能改变范围或信息前提。每次迁移先检查上一段已经交代什么、下一段依赖什么，再选择选项。保留有据的强比较、能力和可部署性，但把未测隐私保证、普遍误报消除、组合总是增益等扩张留在明示的科学资格登记中。没有统一句长、段数或结果数字配额。

# WAFLGo：科学证据资格

## Q1

- source_locator: Introduction P1–P2 pp1; §2.1 p3
- source_support: 回归比例是作者援引既有研究；覆盖式有效性与提交效率是不同评价；P2直觉路线已经提到影响区
- qualification: 本轮未独立复查原OSSFuzz统计；不把回归比例外推为所有提交有bug。缺口为实际导向不充分，不能改写成近邻完全不知道影响区。
- writing_duty: 解释提交优先级与公平评价已有答案。

## Q2

- source_locator: Introduction P3 pp1–2; §2.2 p4; §6.2 p11
- source_support: 真实示例说明目标容易到达而错误依赖后续状态；§6.2用到达后覆盖/路径与发现时间检验这一关系
- qualification: Table1的21/30是该样本位置不同，不是总体率。到达后探索重要不等于到达问题已经解决；§6.1仍有九case连目标也到不了。
- writing_duty: 使任务结果指标与gap保持同一对象。

## Q3

- source_locator: Introduction P3.S11 p2原页
- source_support: 需要句后关系从句紧邻复数bugs，reach/test为复数兼容形式，表层让bug承担了到达/测试行为。上下文所需的是技术承担两动作。
- qualification: 完整中文变式依据上下文恢复技术施事，属于编辑修正；英语若重新指向单数technique，必须改变一致关系或句型，不能只把原从句重挂。局部移动推论标记并不修这个问题。
- writing_duty: 学习论证关系而不模仿有问题的修饰附着。

## Q4

- source_locator: Introduction P4/P7 p2; §3.1 pp4–5; §6.3 pp11–12
- source_support: 多目标距离保个体关注，分组利用共同前提；§6.3检验目标分配及合并后的作用
- qualification: 承认Parmesan/FishFuzz多目标能力，不说所有旧法不能多目标。结构区别与效率改善是作者论证，本轮不独立证明对所有提交或任意依赖图成立。
- writing_duty: 多目标挑战不是数量添加，而是共享与个体性并存。

## Q5

- source_locator: Introduction P5 p2
- source_support: 两问式后分别给保持/变化需求，以及逐点单测直觉的数量和共享上下文问题
- qualification: P5.S2是冒号框架，P5.S3/S6是非有限how-to问题；旧坐标有九个分析单元，不等于九个有句号的独立陈述。该两挑战不是通用数量模板。
- writing_duty: 问题现象经可执行要求转为方法解释义务。

## Q6

- source_locator: Introduction P6/P7 p2; §3.2 pp5–6; §3.3 pp6–7; §7 pp12–13
- source_support: 控制前缀与数据后缀给到达/影响信息；保持执行和多样变化是共同任务关系；正文讨论识别精度与复杂约束
- qualification: 充分测试/所有目标是作者任务主张，不是穷尽全部状态保证。引言的选边概述比正文规则压缩，不能将其当精确实现规范；本档只分析解释职责，不复述可执行步骤。
- writing_duty: 用共同原则与代理意义把组件串成有用能力。

## Q7

- source_locator: Introduction P8 pp2–3; §5.2–5.4 pp8–9; Table2 p9
- source_support: 30个真实bug、手工BIC定位、三类八工具、共享初始种子和实验预算
- qualification: 作者称八个广泛使用C程序；继承“8类/个”是分析记录的含混写法，不再扩成其它单位。BIC人工定位不是全自动产生benchmark；比较范围限于实测工具。
- writing_duty: 基准资源的价值来自测试对象与本文任务一致。

## Q8

- source_locator: §5.4 p9; §6.1/Table3 p10; §7 pp12–13
- source_support: 24小时、五次重复。Table3列21个被复现case的比较，文中据该已复现case域报告10.3倍平均加速；这些行中对比fuzzer超时按24小时计入。21/30则是面向整个30-case数据集的成功范围，另九case未被任何比较工具复现，未列入Table3提速行。
- qualification: 平均不等于每例提速；不能把10.3无条件说成全30-case平均。已复现21-case的时间比较与整体30-case的成功分母不同；当前只核实作者报告与表格范围，未独立重算或复现实验。该协议不提供实时CI保证；超过12小时的讨论在§7，旧profile写§5为定位错误。
- writing_duty: 平均时间与成功数分别回答效率和完成范围。

## Q9

- source_locator: Introduction B3/B4 p3; §5.2.2 p9; §6.4/Table4 p12
- source_support: 源文声明原型/代码可获得，最新提交实验发现7新漏洞，其中4被修复并获CVE，另3为报告状态
- qualification: 引言只保7/4，不擅加全部修复或相同严重级别。代码可用是论文时代声明，未本轮检查当前仓库权限/许可证；不将源声明改成未来计划。
- writing_duty: 资源交付状态和现实新发现不同于已知bug复现。


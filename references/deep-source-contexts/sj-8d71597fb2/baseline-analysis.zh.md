# IPPO：降低证据数量门槛，同时提高参照可比性的责任

## 来源、真实任务与主线
读取[共著者托管CCS2021排版稿](https://www-users.cse.umn.edu/~kjlu/papers/ippo.pdf)，18页，散列1f6361f67d07d7f43da693e44c7368d722b5bffca27df0141ffae325060f5ede。引言物理pp.1–3/印刷1627–1629完整，p.2双栏及代码图经渲染核对；补读§2.1、§3–4.2、§5.3、§6表2–4及误报/互补讨论。保留的完整来源重建；其全部旧单元并未在本次定点审查中重新获得独立验证。当前选择分析与证据资格共同使用；相邻明确资格约束历史简述。

任务不是搜索没有check的语句，而是判断具体上下文是否需要安全操作。强已有答案以大量相似代码的多数行为作oracle，免去完全理解语义；IPPO把证据门槛改为一对路径，但必须证明这对路径就同一对象足够可比。因而对象相似性是新判据的成立条件，路径缩减是承担该条件的规模手段。这种选择同时决定引言先讲旧oracle，再讲失效条件，最后才讲规则与CFG。

相邻可比性资格：此处“必须证明”是读者解释责任的概括，不是声称已有正式语义等价或检测健全性证明。当前读法为以对象规则和分析建立足以支持比较的可比性；不一致仍产生候选，不直接证明漏洞。

语法/明示理由可在源定位；读者注意和篇幅取舍是编辑推断，不推断某共同作者个人执笔。

## 逐句与子句分析
### P1，p.1627右：重要性落到可识别的操作
- P1.S1：大程序主语、enforce谓语，例子给检查/锁/引用计数；⇒后文支持的操作类别
- P1.S2：正确使用作动名词主语、improves把机制转收益
- P1.S3：However遗漏主语、common系表，which给潜在严重后果；必要性先于统计
- P1.S4：according-to证据来源前置、遗漏占比主句；61%为被引研究范围，非新普查
- P1.S5：Consistent-with前置，作者检查/发现并列给Linux约66%；说明本研究对象中的对应现象
- P1.S6：existing-works主语、studied谓语，including列后果；用具体危害解释规模为何值得关心

### P2，pp.1627–1628：已有oracle的真价值
- P2.S1：Though让步已知危害，检测难主句后as说明上下文必要性；不是把“少一句”直接判错
- P2.S2：this-requires主干、not-only/but-also并列规则与精确规模分析；解释语义理解的成本
- P2.S3：there-is-lack把复杂性收束成oracle短缺
- P2.S4：To-address前置，研究者turned-to交叉检查，to自动决定必要性；已有答案回应真正困难
- P2.S5：方法主语、two-steps下先收多相似片段再比较；数据要求是后段切入口
- P2.S6：Once多数有操作前置，we-assume/report两谓语；明确统计信任前提与输出
- P2.S7：advantage系表后can-avoid直接语义理解；必须保留，否则旧方法成为稻草人
- P2.S8：代表工作主语、employed谓语；文献锚落在共同机制而非名单本身

### P3，p.1628左：三种前提失效，不是三模块需求
- P3.S1：However主句给漏报，due-to下启具体事实
- P3.S2：many-pieces主语、may-be-unique后thus无法找够例；量的前提失效
- P3.S3：tools-set-threshold主干，which-means转换为四正确对一错误；数字用于解释门槛，不作为性能成绩
- P3.S4：图1主语、shows反例，where给各调用仅一次；最小例子足以击穿多数前提
- P3.S5：as-result不能推bug；让图的论证结论显式化
- P3.S6：slicing-granularity系表困难；切到表示信息损失
- P3.S7：为可规模目的前置，methods抽象/限切片并列；承认粗化有正当工程原因
- P3.S8：such-strategies主语、make/lose并列；规模选择有漏报代价
- P3.S9：多数正确假设主语、might-not保留条件性；第三类为判据真值而非样本量
- P3.S10：for-example存在可能、API文档差与普遍误用连接；多数可共同犯错
- P3.S11：in-that-case主句旧法不报常见误用；由情境回任务损失
三原因分别是参照稀缺、参照丢失、参照错误。不可机械让新方法各发明一个同名模块；新pair oracle主要改变数量/多数条件，仍需处理可比性。

### P4，p.1628左：先交判据，再交建造难题
- P4.S1：present主干，that-requires-only一对路径限定关键信息门槛；⇒P3单例
- P4.S2：based-on-observation后if同对象语义相似，then应同保护；对象限定是推断许可证
- P4.S3：Given参照前置、if一有一无，reports-potential给候选输出；不宣布自动证实漏洞
- P4.S4：By对象分析前置，precision主张比较通用相似；⇒§4规则
- P4.S5：Meanwhile/unlike对比旧法，differential-check/no-longer-requires并列；直接回收数量门槛

源形式资格（P4.S5）：指定源排作on longer；本行no-longer是依本段及全文数量对比作出的语义解释，不是假称原表层拼写已如此，也不把它当应模仿的形式。

### P5，p.1628左末→右：新的oracle把难处转移到参照构造
- P5.S1：key-challenge系表构造OSPP；不回避新判据前提
- P5.S2：one-hand双主语给语义上下文复杂及对象用法多样；说明相似不是词面相同
- P5.S3：Thus-it-is-challenging主句自动理解；承接原因
- P5.S4：Moreover嵌whether问题明确该不该算相似；决定错配会误报
- P5.S5：other-hand构造主语、likely-to路径爆炸，especially大函数；独立规模负担
- P5.S6：To-address-first前置、develop-rules主句、to对象级特征；精度响应
- P5.S7：as-for-second前置，develop-reduction，e.g.列CFG分割和冗余缩减；规模响应，不改变判据
- P5.S8：with两类手段前置、able-to精确/可规模并列；⇒评价两个维度

### P6，p.1628右：证据从自动报告走到社区采用
- P6.S1：implemented主句、as LLVM passes说明产物形态
- P6.S2：chose主干、to-evaluate与四程序给范围
- P6.S3：two/other-two平行系表分内核/用户态；范围数字有异质性意义
- P6.S4：each-bug主语影响用户设备；解释选常用项目的实际价值
- P6.S5：系统finish/report两谓语给两小时及754候选；性能和候选产量不同
- P6.S6：By-manually-checking前置，confirmed主句给161新bug及类别；从算法输出进入审查证据
- P6.S7：submitted/accepted两状态分开，136体现维护者认可；不把提交当修复完成
- P6.S8：results-confirm归结效力、规模、迁移；须由上述不同证据共同支持

相邻术语资格（P6.S8）：portability指跨程序可移植性；“迁移”不指机器学习跨模型迁移，也不证明任意语言或编译体系自动适用。

### P7/C1–C3，pp.1628–1629：完整集合
- P7.S1：总结引导，无新技术断言
- C1.S1：propose框架，to回应旧交叉检查局限；系统能力层
- C1.S2：requires-only-pair与rather-than量大对照；核心信息条件压缩
- C1.S3：implemented与supports并列可扩展/可定制；列表新增未来采用接口，不仅重复正文
- C1.S4：will-open-source目的尾语给复用承诺；版本当时未来时态保留
- C2.S1：challenge系表构造语义相似pair；先给该贡献必要性
- C2.S2：To-improve-precision前置、develop对象相似；技术职责不靠形容词
- C2.S3：also规则细化主句；把理念变可执行标准
- C2.S4：in-addition返回值sub-CFG/缩减路径并列，to应对爆炸；补效率职责
- C3.S1：with-IPPO前置、found四程序bug，which给安全/可靠性后果；不再重复数值
- C3.S2：reported与have-been-fixed并列，by-cooperation说明外部落实；贡献包括实际修复
C1/C2各四句、C3两句，不是列表越短越好。结果段已报数字，所以C3可概括；C1新增扩展性，C2仍要解释precision/scale职责，不能一律压成“系统、技术、实验”。

## 代表性结果选择及边界
引言选新bug161及接受补丁136，强调真实新增安全收益；正文表2有275个有效bug（含已有修复），754是全部报告。若选择275，需说明新旧分母；若只选754，会把审查负担伪装成果。正文63.5%误报率与平均较快人工核对说明它是候选生成器；引言的潜在bug一词因此不可删。

正文§6.3在IPPO发现集合上比其他工具，不能自动读成对全漏洞分布的召回率优势；反向560旧工具bug只覆盖119，说明互补。引言不用这个比较数字，而选跨四项目的新发现，能支持“补足参照少的空间”而避免宣称全面替代。§4对象状态、影响安全操作的行为、前后条件说明为何pair比普通相似更可信；但不一致也可能安全操作多的一边冗余，§2.1与图5均提示此点。

可选规模数字如613行长函数、旧漏洞多年未发现能强化人工审查难度，却会挤压对新oracle的解释。当前结果集合采用时间→候选→人工新发现→社区接受，构成证据成熟度阶梯，是最值得迁移的组织操作。

## 表达选项
编辑选项，非源句或已验证增益：
1. “When repetition is scarce, the question becomes whether one carefully matched alternative can serve as evidence.” 将统计数量改为参照质量，适合解释设计转向，少了具体对象条件
2. “The paths need not match globally; they must be comparable for the object whose protection is in question.” 对照焦点精确，较原概念句长，但避免通用代码相似误解
3. “The analysis produces candidates; manual inspection and accepted patches establish the practical findings.” 以证据层级组织结果，不能代替具体确认数量
迁移时先问缺的是例子数量还是参照真实性；若程序不存在可比路径，pair oracle也无证据，不应把一对即可包装成普适漏洞检测。

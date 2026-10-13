# Quantifying Graph AUD：贡献的数字因参照系而有意义

## 来源和真实研究对象
读取[作者/实验室托管9页稿](https://nesa.zju.edu.cn/download/Quantifying%20Graph%20Anonymity%2C%20Utility%2C%20and%20De-anonymity.pdf)，关联INFOCOM2018，无最终论文集页码；散列17c218a2eae5cd56f761c35baf588ced8cfaddc3f6c55e88c1ad676f986f4d9e。引言物理pp.1–2完整；补读§III定义、§IV–V范围、§VI系统整合、§VII–VIII评价。未逐步验证省略的理论证明。保留的完整来源重建；其全部旧单元并未在本次定点审查中重新获得独立验证。当前选择分析与证据资格共同使用；相邻明确资格约束历史简述。

论文研究匿名性、结构效用及去匿名性的关系，并把量化用于配置匿名化和评估攻击尚有多少提升空间。最强已有答案包括多种攻防、结构去匿名条件及SecGraph统一实测系统；剩余不是缺一次攻击实验，而是实测成绩缺少可达参照。数据共享的效用先于隐私风险出场，因此全文不是单目标最大化匿名，而是保留使用价值的关系判断。

语法结构与作者明确用途如下；布局功能和替代权衡属编辑判断，不是个人作者意图。

## 完整引言逐句
### P1，p.1左：先解释为什么不能只把数据销毁
- P1.S1：systems/services主语、generate图数据，例子跨社交/接触/邮件/拓扑；共同研究对象有多来源
- P1.S2：Mathematically被动modeled，where定义节点用户/边关系；从来源抽象到可量化表示
- P1.S3：Therefore-we-refer命名本文对象；术语稳定，不是新结果
- P1.S4：graph-data主语、critical与have-applications并列；研究/实际用途说明utility有价值
- P1.S5：Therefore被动shared/transferred，to接接收者、for分析目的；共享行为由用途推导，⇒隐私代价

### P2，p.1左→右：三条已有研究线共用同一对象
- P2.S1：Meanwhile/since敏感信息原因前置，privacy-concerns主句、when限定共享；价值冲突来自场景
- P2.S2：To-protect前置、多匿名化被动提出，例子展示防护已有选择；不宣称从零开始
- P2.S3：primary-objective系表保护与while保效用；明确两目标需要同时考虑

相邻语法更正（P2.S3）：源文是系表结构后的两个共享不定式标记的协调动作，以and simultaneously连接；没有while从句。历史双目标理解保留，不据协调改成让步或条件。
- P2.S4：On-the-other-hand攻击被动提出，which说明辅助图结构相似重识别；攻击能力带有外部信息条件
- P2.S5：In-addition/to-understand前置，量化技术被动发展；由做攻击转向知道何时可攻击
- P2.S6：these-techniques-enable理解，by给完全/部分重识别条件；承认最强理论近邻已有明确答案
文献不是按年份堆叠，而是防护→攻击→可达条件。三者解释了为什么下一段可以问关系而不是再选一个新攻击器。

### P3，p.1右：开放问题必须连接实际判断
- P3.S1：Although三线已有进展前置，there-remain主句后such-as嵌三问：关系存在、如何量化、方法余量；不是三个技术挑战

坐标资格（P3.S1）：此ID包含三个问号构成的问题序列；28为历史分析单元数，不是28个单一正字法句。存在关系与如何量化的if依赖应保留。
- P3.S2：understanding作主语、important-for指定用户/研究者；给结果接收者
- P3.S3：one-hand使役help后多个how/what并列，保留效用、匿名性及given辅助图的去匿名性；理论用于在条件下知情选择

相邻结构细分（P3.S3）：前三项是间接问项，末项是关系名词短语，不应把每项都标成how/what问句；给定辅助图等条件不因此省略。
- P3.S4：other-hand-help-evaluate后compared-to可达表现；评价参照从“另一个工具”升为“理论可达”
这两句用途不是结尾泛说意义，而是预先决定贡献的系统配置与算法比较方向。若删掉P3.S4，末尾83.4%很容易被误读为普通失败率（编辑判断）。

### P4/C1，pp.1–2：先定义量，才能关系量化
- P4.S1：To-address前置、make-contributions为导航
- C1.S1：introduce-three-metrics主干、respectively明确一一对应；概念先有测量定义
- C1.S2：Based-on指标前置、conduct量化，under-ER/general给模型范围；先一般研究动作后范围
- C1.S3：To-best-knowledge限定首次，and-providing闭式关系给具体产物；不只是“理论分析”空名词

相邻矩阵细分（C1.S3）：严格矩阵是带知识范围的新颖性系表判断；on下有两个-ing补语，末尾目的结构交显式形式的用途。闭式形式可为话语前景而不必成为有限矩阵。
- C1.S4：results-have-implications后towards两类方法发展；将理论用途回接攻防两侧

### C2，p.2左：系统是让参照可被使用的接口
- C2.S1：Based-on量化前置、implement加by扩展既有SecGraph；清楚区分新模块与复用平台
- C2.S2：extended-system-improves主干，冒号三用途给理解关系、配置、按目标评价；不是把模块接上就叫贡献
- C2.S3：system系表统一开源形态，for研究用途；资源定位而非新算法宣称

### C3，p.2左：真实数据提供条件性认识
- C3.S1：Based-on量化前置、conduct评价、leveraging12来源；现实数据是理论应用域，不是已部署用户实验
- C3.S2：results-demonstrate可达量依赖多因素，e.g.保效用/辅助质量；所得是条件关系而非一个普遍最佳算法

### C4，p.2左：数字选择服务“尚有多少没做到”
- C4.S1：Based-on量化前置、evaluate已有技术；评价对象由数据切到方法
- C4.S2：Interestingly-we-find大改进空间；先给读者应解释的结果
- C4.S3：For-instance/when固定ODA、Facebook、DP条件，主句83.4%理论可识别用户未被实现；限定分母是最关键子句

相邻数值资格（C4.S3）：完整源主张为严格超过83.4%，不是恰好该点值；保理论可达用户分母与具体配置，既不重新从图生成小数，也不视作总体用户失败率。
四项4/3/2/3句；理论定义最长，工具用途次之，数据认识短，方法余量用长例句收尾。本文没有独立方法/结果段，贡献就是正式交付的主要说明载体，也无必要硬加“两挑战”。

## 结果池与证据回收
§III选择结构保持作为效用代理，匿名性用归一化不确定性，去匿名性实务分析给条件下界。闭式关系不是所有下游任务的效用保证；给定辅助图及其相关参数不能省略。§VIII实测攻击成功比例再除AUD理论参照，才谈未实现空间。83.4%不是总体用户都被证实可重识别，也不是新攻击提升83.4个百分点。

正文提供更多可选结果：辅助相关性增强时攻击完成度增长；更强匿名配置牺牲结构效用；多数据/配置中实测攻击仍低于理论下界参照。若选第一类，文章会更强调辅助信息风险；若选第二类，会更强调数据发布配置；作者以第三类收尾，凸显量化参照改变研究评价方式。12数据用于关系评价，而§VIII算法对比主要用Enron/Facebook/Twitter三例，不能把两层覆盖混成全部算法在12图完全展开。

§VI反复运行旧系统只能得参数依赖的直觉，新模块给按目标判断的可计算参照。这个“已有实测工具→仍不知道距离可达有多远→量化模块”的链条，比宣称加一个新模块更能解释学术价值。实验辅助图按随机增删边与给定相关参数构造，50次平均；真实原图不等于辅助知识采集完全真实。来源省略部分证明，当前分析不补造验证。

## 表达选项与迁移
编辑选项，非源句或已验证增益：
1. “An observed attack rate does not tell us how much re-identification remains achievable.” 用一主句提出参照缺失，适合连接实测与理论；未说明效用约束
2. “The quantification lets a data owner ask what anonymity remains at a chosen utility level.” 把系统能力改为使用者可作判断，精炼但省去辅助图条件，正式表述须补
3. “In the stated Facebook setting, ODA realizes only a small fraction of the model-based de-anonymization reference.” 分母前置降低误解，较83.4%不够精确，可用于解释句而非替代全部结果
可迁移的是让理论上限/下界成为实测解释参照；反例是没有可比模型、资源或信息条件时，不能把算法与不受相同约束的理论量相除。

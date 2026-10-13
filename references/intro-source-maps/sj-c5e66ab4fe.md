# Understanding the Security Risks of Docker Hub：完整引言句级图

- 来源身份：sj-c5e66ab4fe
- 指定版本：Coauthor-hosted LNCS-style author copy associated with ESORICS 2020
- 指定原文：https://www-users.cse.umn.edu/~kjlu/papers/docker.pdf
- 实际读取原文：https://www-users.cse.umn.edu/~kjlu/papers/docker.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#docker) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [C1](#c1) · [C2](#c2) · [C3](#c3)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

Source https://www-users.cse.umn.edu/~kjlu/papers/docker.pdf; coauthor-hosted LNCS-style ESORICS2020 author copy. Full intro physicalpp.1–4; §2 critical risk sources reread.

Chain P1 software distribution/use; P2 real incidents; P3 four ecosystem differences establish why app-store/VM results do not transfer; P4 two study difficulties; P5 three risk axes with different research procedures; P6 findings; P7 implications/disclosure; C1–3. 推断：三个轴不是为了凑模块数，而是从控制容器行为的不同来源选出来；可扩展性靠只分析实际执行程序，run-command则需要经验攻击+用户研究，两者不是统一流水线。

<a id="p1"></a><a id="p1-s1"></a>P1.S1 定位：Docker→镜像启动实现应用自动部署 | 起题 | study object
<a id="p1-s2"></a>P1.S2 缩域：DockerHub→开发者/用户镜像市场 | 依赖 | ecosystem
<a id="p1-s3"></a>P1.S3 价值：Docker→安全关键任务 | 添加 | stakes
<a id="p1-s4"></a>P1.S4 例：铁路→业务系统管理 | 举例 | relevance
<a id="p1-s5"></a>P1.S5 例：ECS→托管容器应用 | 并列 | relevance
<a id="p1-s6"></a>P1.S6 规模：镜像→海量下载多种用途 | 范围 | sampling
<a id="p2"></a><a id="p2-s1"></a>P2.S1 风险：流行→高关注攻击 | 转折 | measurement
<a id="p2-s2"></a>P2.S2 事例：17恶意镜像→加密挖矿获利 | 举例 | malware axis
<a id="p2-s3"></a>P2.S3 暴露范围：这些镜像→累计下载 | 补证 | impact
<a id="p2-s4"></a>P2.S4 风险解释：未经审查镜像→盲目运行不明二进制 | 引述观点的概括 | user study
<a id="p2-s5"></a>P2.S5 需要：事件→深入系统研究 | 推论 | C1
<a id="p3"></a><a id="p3-s1"></a>P3.S1 对照：DockerHub→异于app/VM生态 | 总述 | study rationale
<a id="p3-s2"></a>P3.S2 差异一：镜像→run-command启动 | 枚举 | commands
<a id="p3-s3"></a>P3.S3 作用：启动参数→容器安全关键 | 解释 | attack demonstrations
<a id="p3-s4"></a>P3.S4 差异二：镜像→结构更复杂 | 枚举 | analysis scaling
<a id="p3-s5"></a>P3.S5 根因：程序配置等很多→传统全扫难扩展 | 解释 | executed-only
<a id="p3-s6"></a>P3.S6 差异三：共享内核→宿主也受风险 | 枚举因果 | host harms
<a id="p3-s7"></a>P3.S7 差异四：软件脱离主线/弱维护动力→补丁延迟 | 枚举因果 | lifecycle
<a id="p3-s8"></a>P3.S8 归结：差异→需要新研究 | 总结 | P4
<a id="p4"></a><a id="p4-s1"></a>P4.S1 必要性：独特生态→新安全问题 | 承接 | work
<a id="p4-s2"></a>P4.S2 预告：完整研究→多挑战 | 转折 | next
<a id="p4-s3"></a>P4.S3 难题一：异类信息→安全影响分析方法未知 | 枚举 | empirical categories
<a id="p4-s4"></a>P4.S4 例：run-command→缺测量办法 | 具体化 | command study
<a id="p4-s5"></a>P4.S5 代价：方法未知→经验/人工工作 | 推论 | manual effort
<a id="p4-s6"></a>P4.S6 难题二：镜像及元数据→规模获取分析难 | 并列 | collection
<a id="p4-s7"></a>P4.S7 根因例：多文件类型→统一分析困难 | 解释 | executable focus
<a id="p5"></a><a id="p5-s1"></a>P5.S1 工作：挑战→首次安全分析主张 | 响应 | C1
<a id="p5-s2"></a>P5.S2 选轴：独特性→参数/恶意程序/补丁三风险 | 研究设计 | three branches
<a id="p5-s3"></a>P5.S3 范围：三轴→规模深度研究 | 组织 | next
<a id="p5-s4"></a>P5.S4 参数分支：run-command→敏感参数识别 | 操作 | findings
<a id="p5-s5"></a>P5.S5 证据：参数→攻击演示实际危害 | 次序 | host outcomes
<a id="p5-s6"></a>P5.S6 行为证据：用户研究→风险认知 | 添加 | findings
<a id="p5-s7"></a>P5.S7 程序分支：全镜像成本→只看被执行程序 | 策略选择 | scalability
<a id="p5-s8"></a>P5.S8 实现：选择→自动定位收集分析框架 | 操作 | C1
<a id="p5-s9"></a>P5.S9 范围：框架→扫描逾2万镜像 | 证据覆盖 | malware count
<a id="p5-s10"></a>P5.S10 漏洞分支：生命周期定义→人工时间窗分析 | 研究设计 | patch lag
<a id="p5-s11"></a>P5.S11 数据依赖：三研究→镜像与元数据收集 | 条件 | dataset
<a id="p5-s12"></a>P5.S12 数据范围：2227244镜像/975858仓库→公共信息 | 定量范围 | C1
<a id="p6"></a><a id="p6-s1"></a>P6.S1 转结果：综合分析→多发现 | 组织 | next
<a id="p6-s2"></a>P6.S2 参数发现：敏感选项→DoS/宿主文件显示泄露 | 结果 | C2
<a id="p6-s3"></a>P6.S3 普遍性：推荐命令→平均一个敏感参数 | 定量 | risk exposure
<a id="p6-s4"></a>P6.S4 行为：用户→不检查就执行 | 反差 | mitigation
<a id="p6-s5"></a>P6.S5 恶意分支：普通镜像中→隐藏恶意镜像 | 转轴 | next
<a id="p6-s6"></a>P6.S6 数量：分析框架→42恶意镜像 | 定量 | C2
<a id="p6-s7"></a>P6.S7 类型：恶意行为→远程控制/挖矿 | 具体化 | security value
<a id="p6-s8"></a>P6.S8 漏洞分支：补丁→延迟甚至忽视 | 转轴 | lifecycle
<a id="p6-s9"></a>P6.S9 范围：镜像→广泛未补漏洞（源强概括） | 深化 | scope caution
<a id="p6-s10"></a>P6.S10 极值：单镜像→最多7500漏洞 | 举证 | nonaverage
<a id="p6-s11"></a>P6.S11 原因：缺更新→生命周期更长 | 因果 | mitigation
<a id="p6-s12"></a>P6.S12 后果：容器漏洞→宿主崩溃等 | 升层 | P3
<a id="p7"></a><a id="p7-s1"></a>P7.S1 综合：发现→用户/软件/宿主共同威胁 | 归结 | C3
<a id="p7-s2"></a>P7.S2 行动方向：威胁→自动修复/检测等 | 回应 | §7
<a id="p7-s3"></a>P7.S3 披露状态：问题→Hub正调查确认 | 实践闭环 | 不等于已确认
<a id="c1"></a><a id="c1-s1"></a>C1.S1 认识产物：经验分析→三风险来源 | 归纳 | §2
<a id="c1-s2"></a>C1.S2 研究产物：公共数据规模→深入三轴 | 归纳 | E
<a id="c1-s3"></a>C1.S3 可复用：数据→开放复现/后续研究 | 添加 | artifact
<a id="c2"></a><a id="c2-s1"></a>C2.S1 结果总领：研究→新风险 | 组织 | next
<a id="c2-s2"></a>C2.S2 结果一：参数→用户宿主危害 | 回收 | P6
<a id="c2-s3"></a>C2.S3 结果二：42镜像→远程执行与挖矿 | 回收 | P6
<a id="c2-s4"></a>C2.S4 结果三：软件补丁→平均422天延迟 | 新关键统计 | lifecycle
<a id="c3"></a><a id="c3-s1"></a>C3.S1 价值：分析→生态安全关注 | 归纳 | §7
<a id="c3-s2"></a>C3.S2 责任：威胁→平台开发者用户研究者共同处理 | 角色配置 | D
<a id="c3-s3"></a>C3.S3 实践：披露→建议措施 | 闭环 | §7

Ending inventory: three axes, distinct methods, corpus scale, most findings and mitigation already known. C2 nonetheless introduces the422-day average for the first time, so closing isn't merely a duplicate. The2.2m metadata corpus is not the number of fully executed/scanned images (20k+); keep denominators separate. No claims that Docker acknowledged vulnerabilities: source says investigation pending.

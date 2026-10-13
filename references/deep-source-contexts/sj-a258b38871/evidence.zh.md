# Turbo：正文证据、编辑理由与限制

## E01

- source_locator: §II-A/B pp2584–2585; §II-C p2585
- source_claim_or_data: 任务是在审核中预测用户/申请欺诈；真正标签来自领取商品后只付早期租金且不归还商品的行为。输入含个人/交易特征及行为日志。
- why_selected_editorial_inference: 将即时请求与后续结果标签分开，防止把在线识别误写成实时观察到未来违约。
- limit: 领域专家的操作定义并非普遍欺诈法律定义；短期缺日志应等待采集。
- serves_units:
  - A3.S1
  - P4.S2
  - P6.S7

## E02

- source_locator: §III-A pp2585–2586; Algorithm1/Fig3
- source_claim_or_data: 共享同类型同值、落在时间窗内才连边；共享群体越大权重越小，短时重复共现跨多级时间窗累积更高权重。
- why_selected_editorial_inference: 解释P5两个动作分别控制什么，比只说鲁棒构图更有选择依据。
- limit: 降低偶然关系影响，不建立边的真实关联标签或校准概率；本轮未见对两构图规则分别移除的实验。
- serves_units:
  - A2.S2
  - P5.S1
  - P5.S2
  - C1.S2

## E03

- source_locator: §III-B Fig4a–c p2586
- source_claim_or_data: 欺诈用户日志集中在申请附近；同类型同值行为间隔更短，正文对用户可能彼此关联仍用不确定措辞。
- why_selected_editorial_inference: 区分单用户活动突发与跨用户时间聚集；后者支持层次时间窗，前者支持审核时日志可用性解释。
- limit: 不是发现每个欺诈用户只在申请时活动，也不是证明0–3天就是统一最佳窗口。
- serves_units:
  - P5.S3
  - P6.S1

## E04

- source_locator: §III-B Fig4d–i pp2586–2587
- source_claim_or_data: 欺诈节点邻域欺诈占比更高并随跳数变化；不同边类型同质性不同；局部度与加权度呈差异。
- why_selected_editorial_inference: 分别支撑局部邻域学习、类型建模与结构信号，不能用同一同质性词代替全部发现。
- limit: 观察是在构造出的BN上做的，不证明真实社会网络团伙；无独立泛化保证。
- serves_units:
  - P5.S3
  - P6.S1
  - P6.S6

## E05

- source_locator: §IV-A Fig5/Theorem1/Eq1–9 pp2587–2589
- source_claim_or_data: GCN在均质团、相同边权/类型与路径同概率激活设定下有期望意义的相同影响/表示；GraphSAGE区分自/邻但使用数据集级变换；SAO增加节点级注意调节。
- why_selected_editorial_inference: 细化问题→强替代方案→残余不足→算子，而不是泛称所有GNN都不行。
- limit: 不是任何GNN在任何BN上必然坍缩的证明；本轮不认证定理推导。
- serves_units:
  - P6.S3
  - P6.S4
  - P6.S5

## E06

- source_locator: §IV-B Eq10–15 pp2589–2590
- source_claim_or_data: SAO在单类型子图内工作；CFO对多类型表征使用节点相关注意和类型级变换。正文比较只用全局注意的做法及GAT的邻居注意。
- why_selected_editorial_inference: 两种异质性尺度使CFO必要；SAO做完后仍有未解决任务。
- limit: 不是仅换一个注意力名称；图级参数和节点级权重不同，不能夸成关系确定性校准器。
- serves_units:
  - P6.S5
  - P6.S6
  - C2.S1

## E07

- source_locator: §II-C p2585; §III-A p2586; §V p2590; §VI-A p2591
- source_claim_or_data: HAG每日离线重训；在线请求采目标子图。图边按时间窗周期刷新，短窗任务更频繁，边TTL为60天。实验在初始下单24小时后取特征/图以模拟审核，按UID 80/20随机切分。
- why_selected_editorial_inference: 分清数据积累、图刷新、离线训练和请求推断四种时间，保护实时服务价值的含义。
- limit: 实时推断不等于全天候每个事件即时学习；随机UID划分不是时间外推检验。
- serves_units:
  - A3.S1
  - A3.S2
  - P6.S7
  - P7.S2
  - P7.S3

## E08

- source_locator: §VI-A TableII pp2590–2591
- source_claim_or_data: D1:67,072节点、918正例、207,890边、8类；先通过旧风控且租期后有标签。D2:1,072,205节点、989,728正例、2,787,733边、8类；覆盖同一期全部申请，旧系统拒绝者被作为正例代理。
- why_selected_editorial_inference: 区分引言真实数据规模与更大样本的标签构造，防止把大样本标签视作真实确认欺诈。
- limit: D2不是部署后流量的同分布样本，也不是独立人工确认的98万欺诈者。
- serves_units:
  - P7.S2
  - C2.S1

## E09

- source_locator: §VI-B TableIII p2591
- source_claim_or_data: D1 HAG AUC83.13、GraphSAGE81.77。差1.36个百分点；相对GraphSAGE约1.6632%。源文写1.66%。手工特征方法常有较高精度、较低召回。
- why_selected_editorial_inference: 区分整体任务收益、指标权衡和可复算的相对提升；选择强GNN基线解释算子增量。
- limit: 不是1.66个百分点，也非全部指标都第一。表格含10基线+HAG共11行，源正文称10方法，不据此隐去一行。
- serves_units:
  - P7.S2
  - C2.S1

## E10

- source_locator: §VI-C TableV/Fig7 p2592
- source_claim_or_data: 移除SAO/CFO均降低F1/F2/AUC；表V HAG83.13，去SAO82.37，去CFO82.72。去DeviceID图7报告AUC下降6.24%。
- why_selected_editorial_inference: 模型消融服务算子增量，关系类型消融服务异质性，不能相互替代。
- limit: 源文平均AUC下降1.19%无法由表V两单独移除行按常见百分点或相对率复算：分别0.76/0.41点，均值0.585点；相对下降均值约0.7037%。保留来源报告但标未解决。
- serves_units:
  - P6.S5
  - P6.S6
  - C2.S1

## E11

- source_locator: §V p2590; §VI-D Fig8 p2592
- source_claim_or_data: 缓存/数据库等优化前后平均延迟6.8→0.8秒，P99 11.3→0.99秒，P999 12.66→1.33秒。1000申请测量中约500ms特征、87ms子图、230ms预测。训练随全图规模近线性；子图与推断延迟增长较慢。
- why_selected_editorial_inference: 把服务价值分解到完整链路，让归纳子图和工程优化各有证据职责。
- limit: 图构建并行且未计入请求延迟；不是模型前向0.8秒，更不是每个请求硬上界1秒。P999表明尾部仍可能超过1秒。 另经实际Fig8a高分辨率图回读，总时延绿色曲线通常低于1秒，但有超过1秒的峰值；正文笼统的整体小于1秒只能作典型水平的概括，不能当逐请求上界。未据图声称典型或频繁超过1秒。
- serves_units:
  - P6.S7
  - P7.S3
  - C3.S1

## E12

- source_locator: §VI-E pp2592–2593
- source_claim_or_data: 论文报告2019年7月上线；7月1–30日在线A/B评估在旧风控之后，阈值0.85；为观察精度/召回，测试期间未实际阻断被标申请；后续观察租金支付，报欺诈比例降低23.19%、精度92.0%、召回42.8%。
- why_selected_editorial_inference: 同时保留真实部署、线上决策价值与测试实施约束，不能用上线事实替代效果或用检测效果替代实付节省。
- limit: 没有精确欺诈计数/金额；未交代足以独立认证随机分配的细节；“降低”在未阻断测试下不应强化为已实现干预因果收益。
- serves_units:
  - P7.S3
  - P7.S4
  - C3.S1


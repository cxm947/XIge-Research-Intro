# Cert-RNN 的条件分支与保义表达选项

以下英文均为原创编辑选项，不是源文引文，也不是已经验证更好的用户论文正文。出处为[固定作者稿](https://nesa.zju.edu.cn/download/dty_pdf_cert_rnn.pdf)。先固定事实和用途，再选择语序；每组的选项数只是展示需要，不是每篇论文都必须生产的配额。源文观察与迁移建议分开：A/O见 analysis.zh.md、clauses.zh.md；本文件各项均为I。

## 一 内容先选什么

### 当任务是说明认证器的推进

可把更紧的可认证界置于主位，因为它直接回答“固定模型在多大扰动范围内能得到保证”。复杂模型的运行成本是另一轴，能说明这些保证是否算得出来。将二者同写时给各自适用的模型；不因主张积极就省去条件。

### 当任务是说明防御是否改善可证鲁棒性

选择相同认证设置下不同训练防御的界，保留被比较的模型已经不同这一事实。此前提出过“启发式测试不等于形式保证”，此处就能自然回扣。既然正文已有相应实验，不必把结果降成笼统潜力；同样也不把一个更大的认证下界认作真实鲁棒界已经精确量出。

### 当任务是说明为什么选这个设计

若读者不明白抽象域价值，先写变量依赖；若读者已知抽象解释，重点写RNN复合运算及误差传播；若读者需要决策成本，突出复杂模型中的包络计算。三个分支增加或删除的信息不同，不是保义句式变体。

### 当最后贡献还需回答实际用途

先判断用途此前是否出现。若已经解释了认证界的意义，结果句可以停在主要比较；若新引入训练或解释预测，需要给该独立用途的动作和证据。源B4的未来承诺可以保留为未来，也可以移到讨论；移走后应明示为结构重组，不叫完整保义压缩。

## 二 同一任务命题的四种说法

固定命题：对给定正确分类输入及固定RNN，在指定的单帧 ℓ∞ 扰动集合内求可证界；证书保证该集合内预测保持正确。这里不加入训练、任意多帧攻击、离散替词或真实最大界。

1. For a fixed RNN and a correctly classified input, the task is to compute a certified bound within which any allowed ℓ∞ perturbation to a single frame preserves the correct prediction.

适用：读者刚接触任务，先说输入和固定对象，再说输出。代价：名词式任务定义较长，但减少了“认证谁”的猜测。

2. Given a correctly classified input to a fixed RNN, we seek a bound guaranteeing the correct prediction against every allowed ℓ∞ perturbation of a single frame.

适用：需要主动研究口吻。seek表示研究任务，不单独宣称全部求解成功；后文须另交已实现能力。

3. We seek to certify how far a single frame of a correctly classified input to a fixed RNN can be perturbed in the ℓ∞ norm while guaranteeing the correct prediction throughout the permitted region.

适用：先让读者理解“多大范围”这一问题。certify与guaranteeing保留证书语义；不能去掉它们而暗示真实最大安全范围已精确求出。

4. The desired output is a certified single-frame ℓ∞ bound: for a fixed RNN and a correctly classified input, every allowed perturbation within that bound must preserve the correct prediction.

适用：前文已经讲输入，当前需要强调输出契约。冒号后的解释把正式术语落回可检查判断；若前文定义充分，这一解释会重复，应选择别组。

四式都只在所定义威胁集合内承诺保证。需要逐帧最小界的全文任务定义时，在任何一个选项之后同样补充：The reported input-level bound is the minimum of the bounds certified separately for its frames. 这不是允许所有帧同时达到该扰动量。

## 三 同一近邻限制命题的四种说法

固定命题：既有方法已能认证RNN；稿中研究的区间式近似会丢失变量相关性，导致更保守的界；昂贵包络计算限制复杂RNN上的扩展。以下是指定论文的技术定位，移植到今天的新论文须重新核对近邻。

1. Existing methods already certify RNNs, but interval-based approximations discard inter-variable correlations and yield conservative bounds, while costly bounding-plane computation limits scalability to complex models.

适用：需要一口气交公平承认与两项剩余。while并列两个限制，不暗示一种方法只负责一个问题。

2. Although RNN certification is already possible, two limitations remain: interval-based approximations lose inter-variable correlations, making the bounds conservative, and expensive bounding-plane computation restricts scalability to complex models.

适用：段落将逐一回应两项限制。two在这里清楚枚举本事实包，不是要求所有论文强行找两个挑战。

3. Existing approaches can certify RNNs. Their interval-based approximations, however, lose inter-variable correlations and produce conservative bounds; expensive bounding-plane computation also limits scalability to complex models.

适用：读者可能误会此前完全无人解决，先给独立肯定句。代价是占两个句位；其价值在承认已有能力更清楚。

4. For existing RNN certification methods, conservative bounds arise from the loss of inter-variable correlations in interval-based approximations, and limited scalability to complex models arises from costly bounding-plane computation.

适用：前一句已明确现有方法可用，需要让原因成为句子重点。两处arise from保留两条因果对应；没有前一句承认时，优先选1–3。

保义差别：1–3在本句组明说认证已经可行，4依赖规定的前句，因此不是脱离语境也完全相同的孤句。若复制4而省去前句，信息就缺了一项。它们均不把“松界”改成“不能认证”，也不把成本限制写成算法不接受任何LSTM。

## 四 同一设计关系的四种说法

固定命题：框架以zonotope保留变量相关性，用专门转换器处理RNN非线性运算，得到输出范围并通过验证／搜索求可证界。这组不额外承诺全局最优、零近似损失或所有模型速度优势。

1. Cert-RNN represents the permitted input region with zonotopes to preserve inter-variable correlations, propagates this representation through RNN nonlinearities with specialized abstract transformers, and uses the resulting output bounds in verification and search to obtain a certified robustness bound.

适用：需要可连续跟踪的一条对象转换链。较长主干仍只有同一施事和三个有依赖的动作。

2. To preserve inter-variable correlations, Cert-RNN uses a zonotope representation of the permitted input region. Specialized abstract transformers propagate it through the RNN nonlinearities, after which output bounds support verification and search for a certified robustness bound.

适用：读者刚看完相关性丢失问题，目的前置能立即回应。第二句换成转换器作主语，适合需要突出其独立设计工作时。

3. Cert-RNN’s certification pipeline starts with a correlation-preserving zonotope representation of the permitted input region. It then applies specialized abstract transformers to the RNN nonlinearities and derives output bounds that support verification and the search for a certified robustness bound.

适用：要与前文流程对齐。pipeline归纳后马上交输入、运算和输出，因此不只是标签。

4. A correlation-preserving zonotope representation links the permitted input region to Cert-RNN’s specialized transformers for RNN nonlinearities; the resulting output bounds then enable verification and search for a certified robustness bound.

适用：对框架整体已熟悉，希望突出表示贯穿计算的关系。代价是具体动作不如1和2显眼，不适合方法首次登场且读者不懂抽象解释时。

这里的bound是可证下界，非精确真实鲁棒界。前文已经定义时可不在每个版本重新说明；选择不同重心不能改变其数学身份。

## 五 两个实测见证的四种保义表达

固定事实包：主实验单帧 ℓ∞ 设定、MNIST sequence、RNN-2-32的平均认证界约为POPQORN的1.86倍；LSTM-1-32平均时间为2.66分钟对46.78分钟。比值采用作者引言报告，时间采用引言与表2一致的值。两种模型不可混成一种。没有逐样本一致性、统计显著性或真实模型鲁棒性改变的额外结论。

1. Under the single-frame ℓ∞ setting on MNIST sequence, Cert-RNN yields a mean certified bound approximately 1.86 times POPQORN’s for RNN-2-32; for LSTM-1-32, mean runtime is 2.66 minutes with Cert-RNN and 46.78 minutes with POPQORN.

适用：一个句子同时留下两项主结果；分号将第二模型条件重启，读者能找出每个数字所属比较。

2. On MNIST sequence under single-frame ℓ∞ perturbations, the mean certified bound for RNN-2-32 is approximately 1.86 times as large with Cert-RNN as with POPQORN. For LSTM-1-32 in the same setting, Cert-RNN takes 2.66 minutes on average, compared with POPQORN’s 46.78 minutes.

适用：希望一项比较一处停顿。第二句同一设置回指必须保留，避免引入未交代的另一实验。

3. For RNN-2-32, Cert-RNN certifies a mean bound approximately 1.86 times POPQORN’s, whereas for LSTM-1-32 it requires 2.66 minutes on average compared with 46.78 minutes for POPQORN; both comparisons use MNIST sequence and single-frame ℓ∞ perturbations.

适用：段首已关心不同架构表现，可先模型后共同条件。代价：共同条件后置，读者要读到句末才有完整实验范围；通常1或2更容易第一次读懂。

4. Two results illustrate Cert-RNN’s gains under single-frame ℓ∞ perturbations on MNIST sequence: a mean certified bound approximately 1.86 times POPQORN’s for RNN-2-32, and a mean runtime of 2.66 rather than 46.78 minutes for LSTM-1-32 when comparing Cert-RNN with POPQORN.

适用：上一句已经解释两个评价轴，当前只需量化见证。名词短语组织紧凑；若对手映射对读者仍陌生，1或2的逐项施事更明确。

这些版本都能积极展示收益。它们不把表2的简单网络速度反例塞进每个数值句，但周围的总体比较不能写“所有模型都又紧又快”；需要总体判断时应给出复杂架构这一范围。

## 六 评价动词怎样保住相同的积极结论

固定事实包：表2有共同数据的比较行上，Cert-RNN的均值认证界更大；MNIST各个被测LSTM运行更快。这里不包含未完成的POPQORN文本LSTM单元，也不包含MNIST vanilla RNN速度优势。三个版本的证据命题相同，主语和信息焦点不同。

1. The comparisons show larger mean certified bounds with Cert-RNN wherever both methods report results in Table 2, together with lower runtime for the evaluated LSTMs on MNIST sequence.

适用：证据施事承接评价描述。show把结果交给完整命题，强度充分。

2. Cert-RNN outperforms POPQORN in mean certified bound across the paired results in Table 2 and in runtime for the evaluated LSTMs on MNIST sequence.

适用：方法主语承接方案段，outperform后的两项范围各自清楚；无需自动降成“有望”。paired results避免把缺失基线填成比较胜出。

3. Evaluation demonstrates Cert-RNN’s effectiveness in enlarging the mean certified bound across the paired Table 2 results and reducing certification time for the evaluated LSTMs on MNIST sequence relative to POPQORN.

适用：前文已定义认证界和成本对任务的意义，effectiveness可自然归纳这两个明确行动。若前文没定义，先修任务解释，不能只换成更具体形容词解决。

“paired Table 2 results”在此是源分析用的精确范围，真实论文成文时应改为本稿已交代的实验集合，而不是把表格坐标当作唯一可读的任务描述。三个版本是源证据支持的表达练习，不是当前用户论文可直接粘贴的成稿。

## 七 最终评价项的三个长度选择

这组是信息选择案例，不声称完整保义：三个版本分别保留不同事实子集。共同前提是前文已解释单帧 ℓ∞ 认证、认证界意义和比较方法，并且四个应用的实验真实完成。来源原稿将详细结果放在贡献之前；当前稿若没有这层前文，不可照抄最短版。

A. We evaluate Cert-RNN across four sequential-input applications and multiple RNN architectures, demonstrating larger mean certified bounds than POPQORN in the paired comparisons and lower runtime on the evaluated MNIST LSTMs.

选择理由：前文已有数值时，覆盖＋受证任务改善就足够。省略具体例子与应用延展，是明确的信息取舍，不是说效果无需证据。

B. We evaluate Cert-RNN across four sequential-input applications and multiple RNN architectures, demonstrating larger mean certified bounds than POPQORN in the paired comparisons and lower runtime on the evaluated MNIST LSTMs. On MNIST sequence, the mean bound is approximately 1.86 times POPQORN’s for RNN-2-32, while average runtime for LSTM-1-32 is 2.66 minutes rather than 46.78 minutes.

选择理由：没有前置数值段时，用第二句给两个已经限定范围的见证。必须从本组共同前提取得单帧设定；作为孤立材料使用时要加回。两个数字组证明不同轴，不代表必须凑两个。

C. Across four sequential-input applications and multiple RNN architectures, our evaluation establishes larger mean certified bounds in the paired comparisons with POPQORN and lower runtime for the evaluated MNIST LSTMs. We additionally use the bounds to assess trained defenses, demonstrate improved certified robustness after verified training of 32-hidden-unit vanilla RNNs on the three text and URL datasets, and inspect word sensitivity through representative toxic-comment examples.

选择理由：当前段必须同时交新增用途时才用。它保留训练与词敏感性证据层次，并就近交代成对比较范围和已测试训练架构，但省略明确数值见证；若这是唯一结果陈述，改用B并另设应用所得更清楚。不能将C说成A的同义压缩。

没有单句、双句或数字数目的通用优先级。用户对当前成稿若有明确长度约定，在充分保义的选项内按该约定选择；不能用源B4较长推翻当前约定，也不能把一次约定升级为所有论文规则。

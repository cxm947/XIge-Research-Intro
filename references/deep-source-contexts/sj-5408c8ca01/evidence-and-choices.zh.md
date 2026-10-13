# 评价末项、代表证据与三种有效编辑选择

以下来源位置均为[官方AAAI PDF](https://ojs.aaai.org/index.php/AAAI/article/view/29388/30622)；表1–5的关键单元已据页面图核对。正文事实、源Intro实际做法、编辑取材理由分别标明。没有重新实施实验。

## 1. 源Intro实际怎样结束

源文观察：P7先给综合结果并强调主任务保持，C1–C4再按认识、架构、分析、经验归组。C4以作者的经验验证为主动作，具体所得是归因一致性及攻击缓解。它没有精确实验数字，没有广泛实验的自我定性，也没有新报数据集数量。三数据集范围已经在P6回答任务表现时交代。

编辑判断：这一末项已有标准学术报告所需的骨架：证据动作＋受检对象＋任务结果。前文承担了范围和机制，它可以短到19词。若目标稿独立方案段后直接接贡献、前面未给实验答案，则适合扩成“在哪里评价→得到什么任务答案→一个代表事实”；若前文已充分报告，则短末项可以保持。不能因为用户举过某种常见句型，就倒填源文没有的实验规模或硬塞数字。

特别区分两类“为什么选数字”：本篇Intro没有结果数字，不能据此推断作者在引言中如何选数。下面的选数理由属于为新稿提供的编辑建议。正文确实突出过CIFAR10的二值化精度下降，以及一组归因指标；这些可作为正文选材观察，但不冒称Intro的修辞决定。

## 2. 先建立完整证据池，再选同一句任务答案

### A. 主任务保持：默认配置与条件扫描的职责不同

源文证据：14708表1按中间维度8、16、32、64、128变化，参与方特征各半。默认维度为16。默认列的准确率如下：

| 数据 | Base | Binary | Round |
|---|---:|---:|---:|
| MNIST | 98.77% | 98.57% | 98.66% |
| Fashion-MNIST | 90.87% | 89.69% | 90.91% |
| CIFAR10 | 75.34% | 70.07% | 75.67% |

14708表2固定默认中间维度，扫描一方特征占比0.1至0.5；另一方持有其余特征。评估主要是两方VFL，图像按列分给两方，底部模型为修改后的预训练ResNet，顶层为MLP。Binary是论文选取的二值操作基线，不等同于独立完整复现B-SL、HashVFL各自所有设计；新句不要直接写成全面胜过两篇原算法。

编辑选数理由：

- 若需要可理解的单例，可用默认CIFAR10三方对照。75.67与75.34接近，70.07较低，直接让读者看见“保留整数粒度”相对更激进压缩的任务理由；不是因为75.67是论文最大准确率
- 这组数字承担两个不同判断：Round与Base比较原任务保留，Round与Binary比较表示选择。只报比Binary高5.60个百分点，容易把主任务保持写成单纯追求最高分类精度；只报75.67，缺少参照
- 若需要跨数据集的默认设置锚点，可报告三个Round与Base绝对差都不超过0.33个百分点。这是从表1默认列计算的最大绝对差：0.11、0.04、0.33个百分点，不是论文原句或显著性结论
- 这不意味着所有配置严格不降。表1的CIFAR10在d=8为73.41对74.59，在d=32为74.74对75.76；表2在r=0.2为78.82对79.82。适合的跨配置结论是测试中总体接近，随后给默认实例；不能写每个配置都更高或无损
- 正文没有给这些准确率的重复试验方差/置信区间，因而“接近”是观察性描述，不转成统计显著等效

### B. 归因一致性：选择直接体现参与方用途的轴

源文证据：14708–14709把特征归因与参与方所提供特征的价值评估相连；14709设置d=16、双方各半、目标类别0；14710表3按Integrated Gradients、DeepLIFT、Feature Ablation分别评价。CIFAR10的Integrated Gradients中，Round与原表示相比的Kendall排序相关为0.4718，Binary为−0.1290；同一方法还有距离与相关距离。

编辑选数理由：如果前文重点是“参与方仍能解释其特征的贡献”，排序相关直接对应重要性顺序，优先于一次罗列距离、相关距离、排序相关、p值四项。数据/方法/参照必须一起给：这里是相对Base解释的接近程度，不是与真实贡献真值的准确率。0.4718显示优于二值对照，但不能改成完美保留排名，更不证明实际分账公平或法律上的权益无损。若没有建立这一用途，贡献中突然报该数字反而增加理解负担。

### C. 对抗缓解：保留准确率与目标攻击成功率不能互换

源文证据：14709设置攻击者已知上传表示和顶层模型参数，使用目标为类别0的白盒PGD；随机取100个样本；步长0.1/1.0与阈值1/2配对。14711表4在CIFAR10、阈值1、步长1.0时，Round受扰动后的准确率59%，Base为28%；目标攻击成功率分别25%、66%。同一小样本集上攻击前准确率分别77%、79%，不同于表1全测试集默认列。

编辑选数理由：这组不是表中最漂亮的零成功率，却同时回答受攻击后仍能做对多少及攻击者能否定向控制输出。优先它是因为步长足以改变整数表示，能避免把离散接口与微小步长的相容性现象当成普遍安全能力。两轴须来自同一行条件，不从另一行拼最佳结果。

源文边界：当步长为0.1时，论文要求扰动后仍维持二值/整数形式，导致该步长不能改变表示；零成功率需要连同这一过程解释。更强阈值下仍可能大量失效，例如MNIST阈值2、步长1.0时Round攻击成功率96%、受扰动准确率0%；Fashion相同条件Round成功率83%，略高于Base的82%。因此不能写所有攻击配置都胜过Base。此处只读原实验，没有运行或开发攻击。

### D. 统计半径：与攻击实测互补，但对象及单位不同

源文证据：14710采用随机平滑；随机选1000个样本，每个用10^6次采样估计，噪声参数设为1。14711表5给各架构的平均认证半径及标准差。CIFAR10的Base均值1.92、Round均值3.01；对应标准差1.70、2.17。MNIST均值2.20对2.96，Fashion-MNIST为4.11对4.28。

编辑选数理由：若要说明“粗粒度接口能改变可认证的局部稳定范围”，均值3.01对1.92比PGD某行零成功率更直接。但它是所构造平滑分类器、表示空间和本文采样设置下的统计量，不是原始输入像素的普适半径。选择CIFAR10是为与前面的任务实例对齐，不能因为增幅较大就把它说成三个数据集平均提升。标准差揭示个体异质性，短Intro可报均值并指明设置，完整依据仍应在正文；不得把均值增长写成每个样本都变大。

### E. 资源与隐私：当前不适合作为独立实测headline数字

14706的4倍内存论述来自32位浮点与8位整数的假设性比较，不是整系统实测加速，也不是所有PyTorch整数的默认位宽事实。其资源论证可作为表示选择理由，但若新稿要报实测节省，需要具体编码、溢出范围、加密及通信实现的数据。

14707的隐私分析引入Laplace扰动后再取整的机制；本文随后提出更强隐私解释。此分析不对该证明作独立认证，也不由确定性整数映射本身宣称DP。可准确记录“提供了隐私分析”，不把它变成无条件保证。主任务精度好同样不能替代隐私证据。

## 3. 三个可直接采用的编辑选择

三个方案各有完整的取材判断与短样稿。它们是原创编辑示例，非源文引句、非原作者的备选稿；彼此改变了信息选择，不属于严格保义换词。每个仍需目标稿的实际材料和授权支持。A最适合大同行刚进入任务；B适合已懂流程但需要看表示选择；C适合任务接口已交代、本文重点落在安全评价。不是三种风格都套同一段。

### 选择A：先建立任务接口，末项保持简洁

适用条件：读者不熟VFL，前文尚未解释中间表示；稿件主线是协作学习的可用性，没有把某一安全指标作为核心headline。

关键段落示例：

Organizations with different features for the same users can learn jointly by exchanging outputs from their local models. The shared representation is therefore more than a communication format: it is what the server computes on and what other parties may try to infer from or manipulate. This motivates reducing unnecessary numerical detail while retaining the information needed for prediction. We introduce an integer-valued interface and use a gradient estimator to keep the local models trainable.

末评价贡献示例：

We evaluate the proposed interface on three image-classification benchmarks, finding that it retains prediction performance close to the original representation and better preserves feature-attribution consistency than the binary alternative.

为什么选：四句依次给合作输入、接口多重职责、选择标准、可训练实现。末项给主任务和新增用途，前文若已解释归因可直接停止；若没解释，就删归因或前置用途，而不是再加一句泛泛“具有实际价值”。没有添加精确数字，因为此处最缺的是关系理解；也没有凭空加广泛实验定性。代价是少了安全比较的具体可量化力度，适合后文另有专门分析时使用。

### 选择B：强调适度压缩，选默认配置的任务锚点

适用条件：读者已懂VFL接口，近邻或草稿已引入二值化；要说明为何不是越粗越好，以及整数化保留了哪些任务能力。需要在此前公平承认已有二值路线的效率/隐私目标。

关键段落示例：

Reducing the precision of exchanged features changes both their processing cost and the information available to the predictor. A binary interface makes the representation compact, but it can discard distinctions that remain useful to the joint task. Our design keeps integer-level variation and passes the returned gradients through the rounding step using an estimator. The resulting question is whether this intermediate granularity preserves useful predictions and feature interpretations while reducing the detail exposed at the interface.

末评价贡献示例：

We assess the trade-off on three classification datasets. In the default CIFAR10 setting, rounding reaches 75.67% accuracy, compared with 75.34% for the original interface and 70.07% for the binary baseline, illustrating that coarser exchange can retain the main task's performance.

为什么选：75.67并非全篇最高精度；这是默认d=16、双方各半的可定位实例，两个参照把“保任务”与“选择粒度”同时说清。句中明确实例性，不暗示全配置同幅增益。具体配置若已在前文定义，只需default；没有定义时，应在句中补双方各半/16维，或以“一个两方设置”替换并在正文给出定位。该方案不声称完整复现并胜过两篇近邻原算法，也不把精度对照代证隐私效果。

### 选择C：突出安全收益，选择能真正改变表示的压力条件

适用条件：前文已说明输入、表示空间和主任务；读者主要关心攻击缓解是否可兑现，稿件有足够篇幅保留攻击条件及两轴结果。若Intro很短，可只留经验结论，把具体例子放评价概览。

关键段落示例：

A coarser interface is useful for security only if its benefits survive perturbations that can alter the transmitted values. We therefore examine both prediction accuracy under attack and the adversary's ability to force a chosen label, and separately assess local stability through randomized smoothing. These tests distinguish preservation of the collaborative task from resistance to a particular attack objective.

末评价贡献示例：

We evaluate robustness under the specified white-box PGD setting. For CIFAR10 with threshold 1 and step size 1.0, rounding retains 59% accuracy rather than the baseline's 28%, while targeted attack success falls from 66% to 25%; stronger perturbation settings still produce substantial failures.

为什么选：同一行提供保留准确率与定向成功率，既给正面推进又保留改变总体主张的强扰动边界；最后半句不是例行自我防御，而是避免把某一成立条件升级为无条件鲁棒。与源文相比，本示例将失败边界前移，是明确的编辑取舍。若主线更偏理论稳定性，可把例子换为“CIFAR10平滑分类器的平均认证半径由1.92增至3.01”，并明确这是另一个采样试验；不得与表4假装是同一组100样本或同一指标。

## 4. 如何选一句而不再制造新标签

先问当前读者还需要相信什么：A补任务关系，B补表示取舍的实证理由，C补安全效果的条件与用途。选定后，让句首范围、主动作和尾部证据共同服务这一个判断。需要数字就用能够承载该判断的实例或相容概括；不需要数字时，让动词明确任务结果。三种选择的价值来自补齐不同推断，不来自更响亮、字更少或数字更大。

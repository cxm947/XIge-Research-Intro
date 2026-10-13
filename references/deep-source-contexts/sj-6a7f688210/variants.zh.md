# FaceArmor：完整上下文变体

以下是编辑方案，不是源文引语，不声称实测写作改进。范围按保留的41单元坐标。必须同时保保护照片与后续操控输出两个对象；说明未知目标时仍保代理知识条件。较强源主张在观察中保留，编辑若收窄力度则明确披露。

## V01 · P1.S4–S5：从范式多样性收成保护任务

This threat spans image inpainting, holistic editing, subject-specific fine-tuning, and identity-preserving generation guided by visual prompts [9, 14, 17, 28, 34, 41, 45]. Protecting facial photographs against this diversity of manipulations has therefore become a critical research problem.

- 范围：完整替换P1.S4–S5，前述公开照片和受害后果保留
- 意义/强度：保四范式对象及任务重要性，删各范式的长用途说明；不是从四项推断所有可能操控均穷尽
- 信息/篇幅：由分类长句转较短枚举，第二句直接命名任务；代价是读者需认识inpainting等术语
- 条件：面向熟悉生成图像范式的读者；若读者跨领域，应保源每项的功能短语。此段不等同“使公开人脸匿名化”，保护的是后续扩散操控复用

## V02 · P2.S3–S6：保持强已有答案，说明适配条件

Existing defenses predominantly assume access to a known model and typically target internal components such as its VAE or denoising U-Net [7, 26, 35, 43]. Different manipulation scenarios exploit different pathways within generative pipelines. A defense overfitted to one component therefore fails under an alternative manipulation paradigm. Table 1 illustrates the resulting limits of component-specific protection across the manipulation scenarios considered here.

- 范围：完整替换P2.S3–S6；P2.S1–S2关于已有主动扰动及其保护用途必须保留
- 意义/强度：保predominantly、typically及overfitted限定，不把所有旧方法都说成完全无法迁移；末句以illustrates取代empirically demonstrates较弱，但不改表中定性覆盖证据身份
- 信息/篇幅：把原因和条件性失败拆开；表1负责跨场景的经验支持，不负责证明普遍失效定理
- 条件：需要让信息条件、组件选择和目标覆盖的关系更容易读懂；不适用于把FaceArmor写成完全不依赖模型信息，因为它仍用代理提取器

## V03 · P3.S2–S6：将共同依赖放在方案选择之前

We investigate what diverse face-manipulation models have in common rather than perturbing isolated internal modules [26, 35]. Architectural variation creates a core obstacle to universal transferability, and optimizing perturbations against specific components inevitably leads to representation overfitting. Despite their different architectures, diffusion-based manipulation models depend on both physical layout information and high-level conceptual semantics. FaceArmor exploits this shared dependence by organizing facial-image representations around those two dimensions rather than binding the defense to a single target component.

- 范围：P3.S2–S6替为四句，P3.S1框架公告不动
- 意义/强度：保源inevitably的较强因果声称；省去architecture-invariant性质词，改为明确组织选择，因此末句并非原文强性质的完全等义转述。共同依赖仍为作者洞察，未独立证明适用于每个未来模型
- 信息/篇幅：研究动作→架构障碍→共同性→选择，避免在we propose之后只列技术名；两句旧因果并入一句，需读者已懂组件依赖
- 条件：希望优先交设计为何合理、且下一段会给两层职责；若稿件要宣称严格架构不变性，必须另交其定义和证据，不能仅借此措辞

## V04 · P4.S1–S6：把两个图像对象和两种信息职责写清

The representation space comprises a structural tier and a semantic tier. The structural tier targets the layout and texture information required for faithful reconstruction, degrading the fidelity of the subsequently manipulated image. The semantic tier disrupts text–image alignment and biometric identity consistency to counter prompt-driven editing and identity-preserving manipulation. By targeting these shared representation dimensions rather than isolated model components, FaceArmor achieves strong transfer to previously unknown target generators.

- 范围：完整替换P4六句为四句，保后续P5联合优化冲突段
- 意义/强度：将two decoupled改为功能分层，避免暗示梯度已独立；还删去了severe textural collapse这一独立强效果表述，仅保留操控输出保真下降的较宽泛主张。strong transfer替代exceptional zero-knowledge transferability，删去相对自评；previously unknown target generators点明迁移对象，但未显式保留源zero-knowledge的目标知识条件，不能将两者当成完全等义。因此本版本是有上述意义/强度取舍的条件性改写，不是源句等义润色。没有否认代理内部访问；若不在邻段交代理来源，应补一句“特征来自可访问代理提取器”
- 信息/篇幅：结构层的失真明确属于操控输出，语义层包含概念和身份两职责；减少每层命名+定义的重复，代价是省latent/reference两类实现线索
- 条件：读者容易混淆保护照片与攻击者生成结果、或误把zero-knowledge读成不使用模型知识时

## V05 · P5.S1–S4：联合设计的代价及双重价值

Jointly optimizing the structural and semantic objectives introduces spatial conflicts because their gradients concentrate on different regions. In the source design, identity-concealing perturbations are confined to the face, whereas texture-disrupting gradients predominantly affect the background and clothing. Naively combining these updates causes interference that weakens protection and introduces visible artifacts into the protected photograph itself.

- 范围：完整替换P5四句为三句
- 意义/强度：保身份侧区域排他与纹理侧predominantly差别，首句把源Specifically说明合为because原因；“In the source design”是分析性转述标记，实际目标论文由作者成文时应写“In our design”，不能冒认我们做过源研究
- 信息/篇幅：第一句直接连接前一设计和新困难，最后一句点出坏的是受保护照片；保护效果与分享效用两个代价仍在
- 条件：需要让第二技术挑战有可理解来历，而非把spatial entanglement当无由术语。该段依赖前文已说明结构/语义，不应移到两层定义之前

## V06 · P6.S1–S5：忠实保留源效果强度，明确组合归属

We introduce attention-based soft weighting to resolve these spatial conflicts. FaceArmor obtains internal heatmaps from its surrogate models and uses them as adaptive weights for the competing objectives. We combine this spatial decoupling with the existing PCGrad method [46] to handle residual gradient conflicts. The resulting optimization guarantees a seamless gradient distribution, prevents unnatural artifacts in the protected image, and preserves perturbations across the representation tiers without mutual interference.

- 范围：完整替换P6五句为四句；残余冲突职责来自§4.2
- 意义/强度：保guarantees、prevents及without interference，不把源强声称静默改成可能；不声称PCGrad由本文发明。删forward pass时机细节以避免把概览误读成所有热图计算都是无梯度前向流程
- 信息/篇幅：取得信号→空间分配→已有投影处理剩余冲突→宣称效果，四句各有职责；技术公式与实现步骤留正文
- 条件：用于忠实呈现源作者论证或自己的证据确实支持相同强度时；有限实验不是所有图像绝无伪影的形式证明，科学资格单列，不能拿这句话当安全保证

## V07 · P6.S5：当证据支持设计意图而非绝对保证

This combined optimization is designed to preserve useful updates across the representation tiers while reducing interference and visible artifacts in the protected image.

- 范围：仅替换P6.S5，P6.S1–S4所述热图来源与PCGrad组合保持
- 意义/强度：将guarantees/preventing/ensuring改成is designed to及reducing，明确降为设计目标与改善方向；不是源句保义润色，也不能作为对源措辞的伪转写
- 信息/篇幅：一句交两项优化目的，少了绝无相互干扰的主张；实验段仍须报告实测效果，不能以目标句替代证据
- 条件：给新稿写作时，若目前没有足以支持无伪影/无互扰保证的证据，可用此类表达；若已有更强证据，不应因通用谨慎偏好无故降格

## V08 · P8–P10：完整三贡献，保总体推进、次生策略与边界证据

- We propose FaceArmor, a facial-image protection framework that targets structural and semantic representations. This shift reduces dependence on individual target-model components and supports protection across diverse manipulation paradigms
- We introduce an attention-guided spatial strategy for conflicts arising from joint optimization of these representations. It combines heatmap-based weighting with gradient projection to disentangle competing updates while preserving the protected photograph’s visual usability
- We evaluate four manipulation scenarios on SD v1.5 and SD XL and test inpainting transfer to SD 3 and Flux. The results show broader and more consistent protection than the evaluated baselines, with resilience to the common image transformations tested

- 范围：完整替换三个贡献段P8–P10；保每项两句只是此版本的职责选择，不是普适格式要求
- 意义/强度：删universal与neutralizes的最强表述，改为范围内的保护/依赖减少；第三条准确给测试拓扑，不宣称四乘四组合完整、每指标全胜或任意图像处理不变。第二条visual usability是源消除受保护图伪影的目标/宣称，仍应由相应图像质量证据支持，生成侧指标不能代替它
- 信息/篇幅：第一项总体对象变化，第二项由这项设计引发的冲突及组合机制，第三项检验跨范式/架构/后处理条件；没有另列“用了四个编码器”的库存贡献
- 条件：若需要证据范围更直接的自包含贡献集。若忠实讨论源作者的universal立场，应保原力度并把资格放分析区，不能说此版本完全等义

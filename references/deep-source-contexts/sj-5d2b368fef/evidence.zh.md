# JailNeurons：证据位置、报告口径与科学边界

- pdf_sha256: c44227b9070fd431bda51eb9939ac43a9b806daee4e0199d14636c72828527a0

## E01

- location: p.3 §3
- fact: 白盒访问含内部激活及参数梯度；小规模成功越狱与良性样本用于训练；任务要求跨攻击与良性分布兼顾TPR/FPR。
- role: 实际任务与访问/数据前提
- scope: 源文明示

## E02

- location: p.2 P3; p.3 B1–B3
- fact: 完整挑战和贡献集合；条件性识别不自动解决检测与OOD；三项贡献分别组织认识、技术、系统评价。
- role: 句法与前后依赖
- scope: 源文本事实，焦点解释属编辑判断

## E03

- location: pp.3–4 §4.1 and Figure2 prose
- fact: 单层分类器ID表现接近100%；作者报告任一单层的六分布最差准确率低于80%；因此可分性和迁移是不同问题。
- role: 正观察与部署缺口
- scope: 原实验与作者报告，未复现实验

## E04

- location: pp.4–6 §4.2; p.2 P4
- fact: 作者将单层失败归因于高维无关信号和跨层覆盖不足；定位后聚合所选神经元特征训练轻量检测器，部署读取特征。
- role: 两种设计理由与阶段边界
- scope: 原文解释；无实施细节输出

## E05

- location: p.7 Tables1–2 and §5.2
- fact: Table1为TPR@FPR≤0.05；LLaVA/JDJN1 0.997/1.0/0.942，JDJN2 0.732/1.0/0.524；Janus-Pro/JDJN1对JAMLLM 0.853。Table2为FigStep检测平均处理时间，LLaVA 1.02秒、Janus-Pro 0.26秒。
- role: 检测结果与效率的度量对象
- scope: 具体配置与表级阈值不可抹除

## E06

- location: pp.7–8 §5.3 Table3
- fact: 固定JailBreakV攻击训练，JDJN1/3/4分别用MM-Vet/MM-Bench/Normal；LLaVA/JDJN1五个良性集FPR为0/0/0.019/0.022/0.012；不同正常训练集导致更高跨分布FPR。
- role: 训练分布影响与典型良性任务代价
- scope: 表3五个测试集，不是引言所说三集的简单重复

## E07

- location: pp.8–9 §5.4
- fact: 掩码阈值、稀疏程度、模型类别及选层策略消融；过强稀疏会丢失信息；覆盖不同深度的策略在多数设定和最优点表现好。
- role: 设计理由支持而非越稀疏越好
- scope: 具体实验族，非最优性证明

## E08

- location: p.9 §6.1; p.19 A.8 Tables10–11
- fact: 在500个成功JailBreakV样本上，对相关神经元的消融相较同量/五倍随机消融更提高拒绝token概率。
- role: 机制关联的对照证据
- scope: 拒绝token概率不等于完整拒绝率；不输出操作细节

## E09

- location: p.9 §6.2; p.20 A.9 Table12
- fact: 同训练集下比较相关特征选择与全激活/正则/PCA/SNIP；OOD权衡优于列出的简单替代。L1在已见JailBreakV的TPR为1.000，高于JDJN的0.997。
- role: 不是泛用降维即可替代的对照；也非逐单元支配
- scope: 对照范围内结论，不证明所有可能降维法都不行

## E10

- location: pp.9–10 §6.3; pp.20–21 A.10 Tables13–15
- fact: 不同攻击来源识别出的集合既重叠又不同，部分共性与数据集特有成分的干预结果帮助解释转移。
- role: 结构性认识及泛化的补充解释
- scope: 交集比例有方向分母；本候选不搬运数值或构造攻击

## E11

- location: p.10 §7.1; pp.22–23 A.12
- fact: 作者将其目标与解释模型原始输出的工作区别为解释反事实拒绝；同时解释多步定位与跨层平衡的作用。
- role: 近邻定位和多层选择理由
- scope: 仅核对该论文表述，未独立重读所有近邻

## E12

- location: p.23 A.12.2 Table18
- fact: 固定JailBreakV/MM-Vet训练，FPR≤0.05约束在MM-Vet；JDJN OOD结果很强；First-to-know在两模型已见JailBreakV均1.000。
- role: 近邻比较的具体强弱，而非所有单元最大
- scope: 不自动继承Intro<1%阈值

## E13

- location: pp.23–24 A.13–A.14 Table19; p.10 §7.2–7.3
- fact: 回答含混或回避、未明确拒绝有害请求的样本，在作者规则下会被标为越狱，因而标签定义影响评价；JDJN1压力集FPR：LLaVA OR-Bench 0.390/XSTest 0.170，Janus-Pro 0.280/0.090。作者将典型使用目标与压力测试区别。
- role: 扩展良性覆盖时的边界
- scope: 作者关于日常真实用户影响及其他商业模型的解释未经外部独立核验


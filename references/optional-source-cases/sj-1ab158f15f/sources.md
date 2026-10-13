# 来源与适用范围

本资源区分作者主张、可观察的文本／证据以及编辑解释。共同署名不说明个人执笔；源文排序不证明作者心理动机，也不保证某种重组的阅读效果。

## OB-WSPES

Chengkun Wei、Qinchen Gu、Shouling Ji、Wenzhi Chen、Zonghui Wang、Raheem Beyah，OB-WSPES: A Uniform Evaluation System for Obfuscation-based Web Search Privacy。

- [作者托管全文](https://nesa.zju.edu.cn/download/OB-WSPES%20A%20Uniform%20Evaluation%20System%20for%20Obfuscation-based%20Web%20Search%20Privacy.pdf)
- 版本：18页作者稿，PDF metadata创建／修改日期2019-11-14；关联DOI 10.1109/TDSC.2019.2962440，不等同出版排印版。以下使用PDF页码
- pp.1–2完整Introduction：研究交付、活动模型、效用区别、五项贡献及开放资源；表示效率在贡献(d)，标题与摘要未给0.83／九倍
- §3 pp.5–6：活动记录、特征、攻击与评价接口；§5.1–5.2 pp.8–9：AOL活跃用户选择及搜索活动采集
- §5.3 pp.9–10、Table6／Fig4：查询属性与搜索结果的不同变化；结果列表指标不等于直接用户体验评价
- §5.4 pp.10–11、Table7：TMN混淆，AOL三月／四月训练、五月测试，三种表示及九个攻击器的每用户平均CPU时间和准确率。0.83为九行均值的近似；OHL/W2V的逐行时间比均值约9.43，时间均值之比约9.12，均与九倍相容，但作者未注明聚合公式
- §5.5 pp.11–13、Table8：跨比例攻击表现；§6.2 p.13：共同文本特征等范围限制。表格未提供足以单独识别跨类别比例隐私变化的分类细项
- 本例不验证全部历史首次性，也不声称Table7说明端到端成本或优于优化后的全部表示基线

## QWSP：资源主线必须承认的已有答案

Arthur Gervais、Reza Shokri、Adish Singla、Srdjan Capkun、Vincent Lenders，Quantifying Web-Search Privacy，CCS 2014，DOI 10.1145/2660267.2660367。

- [作者团队全文](https://las.inf.ethz.ch/files/gervais14quantifying.pdf)；[作者团队书目](https://syssec.ethz.ch/publications/2014-11-03-quantifying-web-search-privacy-20-500-11850-94585/)
- pp.1–2完整Introduction：通用量化框架、工具和AOL实证；§2 pp.2–3：查询结构、语义及相对隐私
- 相对隐私以无混淆行为为参照，考察混淆新增的保护；不能把前作说成仅有理论或没有实际量化
- 前作能力不自动等同于OB-WSPES的所有攻击覆盖及查询／应用效用接口。本例据此收紧比较对象，不作穷尽新颖性裁决

## SimAttack：效率前置的真实反例

Albin Petit等，SimAttack: private web search under fire，Journal of Internet Services and Applications 7:2，2016，DOI 10.1186/s13174-016-0044-x。

- [官方完整文章](https://link.springer.com/article/10.1186/s13174-016-0044-x)；[完整出版PDF](https://d-nb.info/1260726150/34)
- §1／PDF pp.1–2：效率、可扩展性及最多15000用户的评价进入引言前景；158倍对应1000用户的unlinkability设置，100倍对应100用户的TMN设置
- §5.4–5.5：precision、recall、F-measure及对照方法设置。这些结果不能与OB-WSPES的准确率／九倍拼接成同一实验
- 本例使用其完整引言证明“效率不必从属”存在真实写作选择，不推定这种顺序对所有任务都更好

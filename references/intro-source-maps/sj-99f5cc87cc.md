# PRSA：完整引言句级图

- 来源身份：sj-99f5cc87cc
- 指定版本：USENIX Security 2025 proceedings, 21 PDF pages incl. cover
- 指定原文：https://nesa.zju.edu.cn/download/usenixsecurity25-yang-yong.pdf
- 实际读取原文：https://nesa.zju.edu.cn/download/usenixsecurity25-yang-yong.pdf
- 本次图谱记录：2026-10-04，指定主源完整引言
- [高层选读卡](../research-choice-evidence-map.md#prsa) · [图谱索引](../intro-source-index.md) · [坐标转换表](../intro-coordinate-map.json)

## 段落导航

[P1](#p1) · [P2](#p2) · [P3](#p3) · [P4](#p4) · [P5](#p5) · [P6](#p6) · [P7](#p7) · [P8](#p8) · [P9](#p9) · [C1](#c1) · [C2](#c2) · [C3](#c3) · [C4](#c4)

本图保留原创内容释义、前后依赖和编辑推断，不附原PDF或整段原文。规范坐标P8.S3／B1.S1等对应本图的分析单元，不是原论文印刷编号；源页码沿用下列读取记录，不从编号推算。查一个句子时连读其所在段及前后交接。

- sourceID: sj-99f5cc87cc
- 版本：USENIX Security 2025 proceedings, 21 PDF pages incl. cover
- 精确索引主源：https://nesa.zju.edu.cn/download/usenixsecurity25-yang-yong.pdf
- 2026-10-04读取证据：本地完整 PDF（21 物理页）及 raw/layout 提取；SHA-256 8b97941bdb4c7f1974cc657e75140562ce7ef73fb9e90034124f935d610191b2
- 引言定位：物理 PDF 第 2–4（印刷2283–2285；物理1为封面） 页；页锚以原 URL 后加 #page=N 定位
- 状态：available=true；full_introduction_reread=true；sentence_annotated=true；awaiting=false；unavailable=false
- 归属：以下为本论文的内容组织选择，不据共著名单推断任何个人执笔；“选择解释”均为编辑推断，不是作者自述。句级内容为释义，非源句摘录。
- 读法：P 表示原文论证段/贡献项，S 按该段源句顺序。每句写“已知→新增｜前接关系｜后续回收”。篇章标题、脚注和图中文字不冒充正文句子。

## 连续论证与相邻正文核验
P1 prompt价值/市场；P2 两服务形态及共享展示/泛化条件；P3 leakage风险、区分leaking与stealing并选后者；P4 两近邻能力与现实限制；P5 少样本意图还原、输入污染两挑战；P6 总体两阶段；P7 类别共享差异因素→attention、语义近输入→pruning；P8 两现实场景详细结果；P9 互信息解释与防御权衡；四贡献简收方法、评价、认识、披露。
补读§3 problem/threat definition、§4.1 Intuition及generation/pruning结构、评价的PromptBase/GPT Store设置。约500开源prompt的十维output差异聚类为类别相似性直觉提供依据；“prompt attention”不是transformer内部attention改动。攻击目标是功能复现和泛化，并非保证逐字恢复隐藏prompt。intro的知识产权语句是论文威胁/价值论述，不自动等于法律结论。

## 逐句信息推进
### P1 prompt价值（p2）
<a id="p1"></a><a id="p1-s1"></a>P1.S1 未定位→LLM复杂理解/生成能力｜领域｜prompt任务
<a id="p1-s2"></a>P1.S2 已知LLM→可借prompt不fine-tune处理任务｜与传统NLP比较｜prompt资产
<a id="p1-s3"></a>P1.S3 已知依赖→定义prompt及其精度效率作用｜明确对象价值｜功能还原
<a id="p1-s4"></a>P1.S4 已知价值→优质需求推动prompt服务｜经济路径｜P2
<a id="p1-s5"></a>P1.S5 已知增长→2024估值及未来预测的引用数据｜市场佐证，历史预测非当前事实｜风险规模
### P2 服务设置和泛化（p2）
<a id="p2"></a><a id="p2-s1"></a>P2.S1 已知市场→交互app store与无交互marketplace两类｜场景区别｜攻击范围
<a id="p2-s2"></a>P2.S2 已知服务→付费前试用/单I-O展示是共享条件｜攻击可见信息｜few-shot
<a id="p2-s3"></a>P2.S3 已知服务→marketplace模板/app system prompt两形式｜隐藏资产形式｜目标定义
<a id="p2-s4"></a>P2.S4 已知形式→都要容纳多用户输入｜一般化要求｜challenge2
<a id="p2-s5"></a>P2.S5 已知泛化→产品文案模板接受手机/电脑例子｜具体说明变量与逻辑｜pruning
### P3 威胁与范围取舍（p2–3）
<a id="p3"></a><a id="p3-s1"></a>P3.S1 已知资产→功能细节未授权披露风险｜定义泄漏｜threat model
<a id="p3-s2"></a>P3.S2 已知细节泄露→可造功能相同stolen prompts｜界定目标输出｜functional consistency
<a id="p3-s3"></a>P3.S3 已知复制→竞争产品/开发者IP风险｜实际后果｜价值
<a id="p3-s4"></a>P3.S4 已知威胁→两类攻击｜分类入口｜S5–11
<a id="p3-s5"></a>P3.S5 已知第一类→prompt injection诱app吐system prompt｜leaking能力｜S6
<a id="p3-s6"></a>P3.S6 已知能力→限于可交互app｜输入条件边界｜范围比较
<a id="p3-s7"></a>P3.S7 已知leaking→system防护可降成功率｜另一现实边界｜GPT Store样本
<a id="p3-s8"></a>P3.S8 已知第二类→stealing推断prompt功能细节｜能力定义｜P4
<a id="p3-s9"></a>P3.S9 已知stealing→相比购买成本低｜商业后果｜P8成本
<a id="p3-s10"></a>P3.S10 已知可推断→同时针对app和marketplace｜范围更广｜S11
<a id="p3-s11"></a>P3.S11 已知广度→本文选stealing｜明确研究选择｜全文
### P4 最近答案及未解（p3）
<a id="p4"></a><a id="p4-s1"></a>P4.S1 已知stealing→近作已表明风险｜承认领域｜S2–3
<a id="p4-s2"></a>P4.S2 已知路线→LLM直接分析output推prompt｜能力｜S5
<a id="p4-s3"></a>P4.S3 已知另一→多输出训练inversion model｜能力｜S7
<a id="p4-s4"></a>P4.S4 已知两方法→服务中有实践限制｜转折｜S5–7
<a id="p4-s5"></a>P4.S5 已知直接推断→完全依赖LLM逆推而能力有限｜challenge1根基｜generation attention
<a id="p4-s6"></a>P4.S6 已知该法→未测更广输入上的泛化｜challenge2证据缺口｜generalization
<a id="p4-s7"></a>P4.S7 已知inversion→需大量定制多样output，marketplace不给｜信息条件冲突｜single-pair
### P5 两挑战（p3）
<a id="p5"></a><a id="p5-s1"></a>P5.S1 已知限制→复杂现实stealing困难｜归总｜两挑战
<a id="p5-s2"></a>P5.S2 已知少量展示→常单对I-O下准确推prompt｜必要能力1｜generation
<a id="p5-s3"></a>P5.S3 已知目标→少数据难捕捉详细意图｜根因｜category factors
<a id="p5-s4"></a>P5.S4 已知准确定义→stolen prompt还需泛化｜必要能力2｜pruning
<a id="p5-s5"></a>P5.S5 已知I-O→output混合prompt意图与user input，易把输入内容写进prompt｜不同根因｜semantic filtering
### P6 总体工作（p3）
<a id="p6"></a><a id="p6-s1"></a>P6.S1 已知双挑战→PRSA现实prompt services攻击框架｜声明｜§4
<a id="p6-s2"></a>P6.S2 已知框架→generation/pruning两阶段｜组织｜下段机制
<a id="p6-s3"></a>P6.S3 已知目标→用LLM生成模型推详细意图｜核心路线｜generation
<a id="p6-s4"></a>P6.S4 已知少量数据→生成可复现功能prompt｜输出能力｜评价
### P7 机制与交接（p3）
<a id="p7"></a><a id="p7-s1"></a>P7.S1 已知challenge1→借one-shot learning直觉｜选择依据｜S2
<a id="p7-s2"></a>P7.S2 已知类别→同类prompt的风格/主题/语气等准确推断因素相似｜观察｜§4.1
<a id="p7-s3"></a>P7.S3 已知相似→学关键因素可推同类目标意图｜连接到能力｜S4
<a id="p7-s4"></a>P7.S4 已知因素→按output差异的prompt attention识别因素｜具体机制｜generation
<a id="p7-s5"></a>P7.S5 已知生成改善→仍未解challenge2｜残余交接｜S6
<a id="p7-s6"></a>P7.S6 已知混入user input→筛语义空间更靠近输入的内容｜针对根因｜S7
<a id="p7-s7"></a>P7.S7 已知筛选→pruning两步策略｜算法组织｜S8
<a id="p7-s8"></a>P7.S8 已知两步→语义相似+选择beam search删输入相关词保一般化｜输出闭合｜§4 pruning
### P8 两场景结果（p3）
<a id="p8"></a><a id="p8-s1"></a>P8.S1 已知框架→marketplace/app store广评｜覆盖总览｜下两支
<a id="p8-s2"></a>P8.S2 已知marketplace→PromptBase随机买18类别prompt｜样本来源条件｜S3
<a id="p8-s3"></a>P8.S3 已知样本→46%成功、较近作逾160%提升｜比较收益｜评价指标定义
<a id="p8-s4"></a>P8.S4 已知成功→成本仅售价1.3%–12.3%｜兑现经济风险｜P3S9
<a id="p8-s5"></a>P8.S5 已知攻击→功能一致与prompt相似度更好｜双评价面｜generalization
<a id="p8-s6"></a>P8.S6 已知自动评价→LLM多维和human评估交叉验证｜证据可信度｜evaluation
<a id="p8-s7"></a>P8.S7 已知app store→随机100热门GPTs、均有leakage防护｜更强实际条件｜S8
<a id="p8-s8"></a>P8.S8 已知设置→52%成功｜第二场景结果｜区别46%
<a id="p8-s9"></a>P8.S9 已知量化→Math隐藏彩蛋被揭并由开发者确认的案例｜功能细节现实验证｜case study
<a id="p8-s10"></a>P8.S10 已知两场景→现实威胁归纳｜价值收束｜C2
### P9 解释与防御（p3）
<a id="p9"></a><a id="p9-s1"></a>P9.S1 已知攻击有效→互信息越高泄露风险越大的分析｜机制解释｜C3
<a id="p9-s2"></a>P9.S2 已知解释→obfuscation/watermark两潜在防御｜行动方向｜defense
<a id="p9-s3"></a>P9.S3 已知obfuscation→有效但须平衡可用性｜条件限定｜trade-off
<a id="p9-s4"></a>P9.S4 已知watermark→易受损需改进｜负结果｜不夸两者都已解决
### 贡献（p3–4）
引导句 已知研究→四贡献｜收束｜C1–4
<a id="c1"></a><a id="c1-s1"></a>C1.S1 已知PRSA→首个现实框架主张及单I-O准确意图的attention技术｜方法+关键条件｜§4
<a id="c2"></a><a id="c2-s1"></a>C2.S1 已知大量结果→伦理评价证明现实资产威胁｜评价结论压缩｜P8
<a id="c2-s2"></a>C2.S2 已知结果→公开demo地址｜可检查产物｜资源
<a id="c3"></a><a id="c3-s1"></a>C3.S1 已知解释→互信息分析给未来防御认识｜认识贡献｜P9
<a id="c4"></a><a id="c4-s1"></a>C4.S1 已知风险→已向PromptBase/OpenAI报告并协作防护｜真实状态贡献｜disclosure

## 选择解释（推断）
- 服务分类不是行业背景闲笔：marketplace单I-O可见与不交互决定leaking不可用、多输出inversion不现实；同一段还建立后续泛化判据。
- P5的两个挑战既不是“准确/高效”口号，也不是先定两模块再编困难：一是信息量不足，二是意图和user input混杂，后者即使生成准确仍会残留。
- P8分别保留46%与52%、售价比例和case确认，说明结果选材服务不同价值：覆盖服务、经济可行性、细节功能复现。贡献不必重抄这些数字。
- P9两防御给不同结果，保持obfuscation成本和watermark失败比统一“提供防御”更能让读者理解未来工作尚何不足。

## 贡献篇幅条件
四项5句（1/2/1/1），之前已有10句结果和4句解释/防御预告，因此C2可以一句总结再一条demo。C1仍长，因为单I-O和意图attention是必须保留的条件/增量。不要把这种短贡献脱离前置结果段移用，也不要把disclosure当额外算法创新。

## 可点击主源页锚
[PDF p2](https://nesa.zju.edu.cn/download/usenixsecurity25-yang-yong.pdf#page=2) · [PDF p3](https://nesa.zju.edu.cn/download/usenixsecurity25-yang-yong.pdf#page=3) · [PDF p4](https://nesa.zju.edu.cn/download/usenixsecurity25-yang-yong.pdf#page=4)

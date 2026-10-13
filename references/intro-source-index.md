# 完整引言句级图：按需查一个来源

本索引把原121项来源身份与逐来源读取记录分开。当前有114份完整引言图，其中113份来自指定主源，1份来自替代主源；另7份指定全文尚无完整图。2026-10-04的112图与9项不可得状态保留为历史；Waltzz和The Last Mile of Fuzzing的首份完整图分别来自2026-10-07和2026-10-11恢复读取，其余来源不因此重标为当日已读。旧目录的complete状态不替代这里的完整图覆盖状态。

每次只选当前论证需要的一篇或一段。先按论文名／source ID定位，下表进入完整图；句库直接进入已核对的相关单元。图中保留完整段落选择、原创逐句释义、已知→新增、前接关系与后文回扣；细读句子时连同该段及相邻交接一起读。无需先读全部图，也不把它们的技术事实搬到当前稿。

规范坐标如P8.S3、P9.C3.S1或B1.S1保留原分析层级；它们不是源论文印刷编号。原P8S3→P8.S3、段内S3→该段.S3等转换在[坐标表](intro-coordinate-map.json)逐项保留；不存在的别名不能靠猜编号补齐。分句、片段和贡献保持原图身份。原图未给逐段精确页码时，只保留已知引言范围，不假造更细定位。

可用脚本按需读图或单元：python3 scripts/read_intro_source.py --paper UVSCAN --unit P8.S3。--paper接受标题或source ID；--unit支持规范坐标及坐标表中明确记录的原标签。省略--unit只读所选一篇，--list列标题与本次状态；--group M.4按一个句子职责读取已核来源及其适用边界。脚本路径相对于技能根目录。

署名、第一列作者单位与共同第一作者事实按同一source ID查[来源身份记录](corpus-source-provenance.json)。该记录只核作者与单位，不改变本索引的全文读取状态，也不证明全部来自安全顶会或正式出版。

原文链接和版本见各图开头；详细机器索引见[来源索引JSON](intro-source-index.json)，旧高层卡见[选择地图](research-choice-evidence-map.md)。本包不附原PDF或论文全文；下面是原创阅读注释，不是写作效果证明。

## 内容导航

- [完整句级图](#完整句级图)
- [当前无完整图的7个指定全文](#当前无完整图的7个指定全文)
- [替代主源的单独边界](#替代主源的单独边界)

## 完整句级图

| 论文 | 句级图 | 本次来源与高层卡 |
|---|---|---|
| The Last Mile of Fuzzing | [sj-e1dfbd274e](intro-source-maps/sj-e1dfbd274e.md) | 指定主源；2026-10-11恢复读取；[高层选读](research-choice-evidence-map.md#last-mile) |
| Waltzz | [sj-458e6724c4](intro-source-maps/sj-458e6724c4.md) | 指定主源；2026-10-07恢复读取；[高层选读](research-choice-evidence-map.md#waltzz) |
| MOCK | [sj-177bf3c33e](intro-source-maps/sj-177bf3c33e.md) | 指定主源；[高层选读](research-choice-evidence-map.md#mock) |
| EMS | [sj-2deb60c210](intro-source-maps/sj-2deb60c210.md) | 指定主源；[高层选读](research-choice-evidence-map.md#ems) |
| MPInspector | [sj-1f315ef889](intro-source-maps/sj-1f315ef889.md) | 指定主源；[高层选读](research-choice-evidence-map.md#mpinspector) |
| UVSCAN | [sj-a36437c84c](intro-source-maps/sj-a36437c84c.md) | 指定主源；[高层选读](research-choice-evidence-map.md#uvscan) |
| VERIFI | [sj-1b6614ac62](intro-source-maps/sj-1b6614ac62.md) | 指定主源；[高层选读](research-choice-evidence-map.md#verifi) |
| TruVRF | [sj-2d9d102d0d](intro-source-maps/sj-2d9d102d0d.md) | 指定主源；[高层选读](research-choice-evidence-map.md#truvrf) |
| Label Inference Attacks Against Vertical Federated Learning | [sj-af4d22b295](intro-source-maps/sj-af4d22b295.md) | 指定主源；[高层选读](research-choice-evidence-map.md#label-inference) |
| Customization under Fire / PoisonLoRA | [sj-8c4c252662](intro-source-maps/sj-8c4c252662.md) | 指定主源；[高层选读](research-choice-evidence-map.md#poisonlora) |
| IntraGuard | [sj-9fe6898db0](intro-source-maps/sj-9fe6898db0.md) | 指定主源；[高层选读](research-choice-evidence-map.md#intraguard) |
| Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications | [sj-b1d0179073](intro-source-maps/sj-b1d0179073.md) | 指定主源；[高层选读](research-choice-evidence-map.md#prompt-leaking) |
| FirmRCA | [sj-446d78ec82](intro-source-maps/sj-446d78ec82.md) | 指定主源；[高层选读](research-choice-evidence-map.md#firmrca) |
| Critical Code Guided Directed Greybox Fuzzing for Commits | [sj-bdd6754e02](intro-source-maps/sj-bdd6754e02.md) | 指定主源；[高层选读](research-choice-evidence-map.md#waflgo) |
| CLIBE | [sj-74a13898b9](intro-source-maps/sj-74a13898b9.md) | 指定主源；[高层选读](research-choice-evidence-map.md#clibe) |
| TextDefense（Word Importance Entropy版本） | [sj-b3ea90f06d](intro-source-maps/sj-b3ea90f06d.md) | 指定主源；[高层选读](research-choice-evidence-map.md#textdefense) |
| TextShield | [sj-4ef65862d0](intro-source-maps/sj-4ef65862d0.md) | 指定主源；[高层选读](research-choice-evidence-map.md#textshield) |
| SUB-PLAY | [sj-52f8920eaa](intro-source-maps/sj-52f8920eaa.md) | 指定主源；[高层选读](research-choice-evidence-map.md#sub-play) |
| ORL-Auditor | [sj-6eeb51e521](intro-source-maps/sj-6eeb51e521.md) | 指定主源；[高层选读](research-choice-evidence-map.md#orl-auditor) |
| Diff-ID | [sj-9042a938b2](intro-source-maps/sj-9042a938b2.md) | 指定主源；[高层选读](research-choice-evidence-map.md#diff-id) |
| Invisible-Face | [sj-2079f71014](intro-source-maps/sj-2079f71014.md) | 指定主源；[高层选读](research-choice-evidence-map.md#invisible-face) |
| Seeing is Living? | [sj-6787cd9815](intro-source-maps/sj-6787cd9815.md) | 指定主源；[高层选读](research-choice-evidence-map.md#seeing) |
| MINER | [sj-3698195c5a](intro-source-maps/sj-3698195c5a.md) | 指定主源；[高层选读](research-choice-evidence-map.md#miner) |
| CPscan | [sj-390b20426f](intro-source-maps/sj-390b20426f.md) | 指定主源；[高层选读](research-choice-evidence-map.md#cpscan) |
| SyzTrust | [sj-689896e985](intro-source-maps/sj-689896e985.md) | 指定主源；[高层选读](research-choice-evidence-map.md#syztrust) |
| LoRAShield | [sj-e48360a284](intro-source-maps/sj-e48360a284.md) | 指定主源；[高层选读](research-choice-evidence-map.md#lorashield) |
| The Boy Who Cried Wolf | [sj-56ed062ba0](intro-source-maps/sj-56ed062ba0.md) | 指定主源；[高层选读](research-choice-evidence-map.md#cried-wolf) |
| The Eminence in Shadow | [sj-385d46e392](intro-source-maps/sj-385d46e392.md) | 指定主源；[高层选读](research-choice-evidence-map.md#eminence) |
| FaceArmor | [sj-6a7f688210](intro-source-maps/sj-6a7f688210.md) | 指定主源；[高层选读](research-choice-evidence-map.md#facearmor) |
| VideoEraser | [sj-cc51b110bc](intro-source-maps/sj-cc51b110bc.md) | 指定主源；[高层选读](research-choice-evidence-map.md#videoeraser) |
| InvMM | [sj-07015463d4](intro-source-maps/sj-07015463d4.md) | 指定主源；[高层选读](research-choice-evidence-map.md#invmm) |
| Quantifying Graph Anonymity, Utility, and De-anonymity | [sj-a68da04b3f](intro-source-maps/sj-a68da04b3f.md) | 指定主源；[高层选读](research-choice-evidence-map.md#quantifying) |
| Graph Data Survey | [sj-afda94caf1](intro-source-maps/sj-afda94caf1.md) | 指定主源；[高层选读](research-choice-evidence-map.md#graph-survey) |
| Structural Data De-anonymization | [sj-354b8db00c](intro-source-maps/sj-354b8db00c.md) | 指定主源；[高层选读](research-choice-evidence-map.md#structural) |
| ACIArena | [sj-d5ccc8652b](intro-source-maps/sj-d5ccc8652b.md) | 指定主源；[高层选读](research-choice-evidence-map.md#aciarena) |
| IPIGuard | [sj-4391324662](intro-source-maps/sj-4391324662.md) | 指定主源；[高层选读](research-choice-evidence-map.md#ipiguard) |
| Beyond the Payload | [sj-c1e338ca9f](intro-source-maps/sj-c1e338ca9f.md) | 指定主源；[高层选读](research-choice-evidence-map.md#beyond) |
| Privacy-preserving Triangle Counting in Directed Graphs | [sj-d1fc8dd7b9](intro-source-maps/sj-d1fc8dd7b9.md) | 指定主源；[高层选读](research-choice-evidence-map.md#triangle) |
| Dyn-D2P | [sj-7271bf4af3](intro-source-maps/sj-7271bf4af3.md) | 指定主源；[高层选读](research-choice-evidence-map.md#dyn-d2p) |
| AsgLDP | [sj-dc32e376bc](intro-source-maps/sj-dc32e376bc.md) | 指定主源；[高层选读](research-choice-evidence-map.md#asgldp) |
| FreeEagle | [sj-33b7f0ad03](intro-source-maps/sj-33b7f0ad03.md) | 指定主源；[高层选读](research-choice-evidence-map.md#freeeagle) |
| Is Your Explanation Stable? | [sj-f612de4bf1](intro-source-maps/sj-f612de4bf1.md) | 指定主源；[高层选读](research-choice-evidence-map.md#metfa) |
| Copy, Right? | [sj-1e819403d4](intro-source-maps/sj-1e819403d4.md) | 指定主源；[高层选读](research-choice-evidence-map.md#copy-right) |
| IPPO | [sj-8d71597fb2](intro-source-maps/sj-8d71597fb2.md) | 指定主源；[高层选读](research-choice-evidence-map.md#ippo) |
| IMMI | [sj-049fb65998](intro-source-maps/sj-049fb65998.md) | 指定主源；[高层选读](research-choice-evidence-map.md#immi) |
| TFA | [sj-23809d776d](intro-source-maps/sj-23809d776d.md) | 指定主源；[高层选读](research-choice-evidence-map.md#tfa) |
| Tacoma | [sj-c153987a94](intro-source-maps/sj-c153987a94.md) | 指定主源；[高层选读](research-choice-evidence-map.md#tacoma) |
| SLIME | [sj-e82106495c](intro-source-maps/sj-e82106495c.md) | 指定主源；[高层选读](research-choice-evidence-map.md#slime) |
| V-Fuzz | [sj-e0e45fc435](intro-source-maps/sj-e0e45fc435.md) | 指定主源；[高层选读](research-choice-evidence-map.md#v-fuzz) |
| Beyond Over-Refusal | [sj-bee854378e](intro-source-maps/sj-bee854378e.md) | 指定主源；[高层选读](research-choice-evidence-map.md#beyond-over-refusal) |
| JailNeurons | [sj-5d2b368fef](intro-source-maps/sj-5d2b368fef.md) | 指定主源；[高层选读](research-choice-evidence-map.md#jailneurons) |
| Efficient Query-Based Attack against ML-Based Android Malware Detection under Zero Knowledge Setting | [sj-5f4c0a6a8e](intro-source-maps/sj-5f4c0a6a8e.md) | 指定主源；[高层选读](research-choice-evidence-map.md#advdroidzero) |
| Defending against Adversarial Malware Attacks on ML-based Android Malware Detection Methods | [sj-4355bf5c6a](intro-source-maps/sj-4355bf5c6a.md) | 指定主源；[高层选读](research-choice-evidence-map.md#add) |
| JWBinder | [sj-81630a3e7e](intro-source-maps/sj-81630a3e7e.md) | 指定主源；[高层选读](research-choice-evidence-map.md#jwbinder) |
| Integer Is Enough | [sj-5408c8ca01](intro-source-maps/sj-5408c8ca01.md) | 指定主源；[高层选读](research-choice-evidence-map.md#integer) |
| Hijack Vertical Federated Learning Models As One Party | [sj-e3479d788f](intro-source-maps/sj-e3479d788f.md) | 指定主源；[高层选读](research-choice-evidence-map.md#hijack-vfl) |
| CAMH | [sj-2ada62afcb](intro-source-maps/sj-2ada62afcb.md) | 指定主源；[高层选读](research-choice-evidence-map.md#camh) |
| STAR | [sj-79aa4ab765](intro-source-maps/sj-79aa4ab765.md) | 指定主源；[高层选读](research-choice-evidence-map.md#star) |
| AdversaFlow | [sj-c44bf3b6f8](intro-source-maps/sj-c44bf3b6f8.md) | 指定主源；[高层选读](research-choice-evidence-map.md#adversaflow) |
| Understanding the Security Risks of Docker Hub | [sj-c5e66ab4fe](intro-source-maps/sj-c5e66ab4fe.md) | 指定主源；[高层选读](research-choice-evidence-map.md#docker) |
| How IoT Re-using Threatens Your Sensitive Data: Exploring the User-Data Disposal in Used IoT Devices | [sj-601d126363](intro-source-maps/sj-601d126363.md) | 指定主源；[高层选读](research-choice-evidence-map.md#iot) |
| Exploring ChatGPT’s Capabilities on Vulnerability Management | [sj-ac970c8450](intro-source-maps/sj-ac970c8450.md) | 指定主源；[高层选读](research-choice-evidence-map.md#chatgpt-vm) |
| PRSA | [sj-99f5cc87cc](intro-source-maps/sj-99f5cc87cc.md) | 指定主源；[高层选读](research-choice-evidence-map.md#prsa) |
| AHEAD | [sj-a904202f3c](intro-source-maps/sj-a904202f3c.md) | 指定主源；[高层选读](research-choice-evidence-map.md#ahead) |
| MOpt | [sj-d51010872e](intro-source-maps/sj-d51010872e.md) | 指定主源；[高层选读](research-choice-evidence-map.md#mopt) |
| UNIFUZZ | [sj-26271ecf21](intro-source-maps/sj-26271ecf21.md) | 指定主源；[高层选读](research-choice-evidence-map.md#unifuzz) |
| AdvSQLi | [sj-f6b808ce92](intro-source-maps/sj-f6b808ce92.md) | 指定主源；[高层选读](research-choice-evidence-map.md#advsqli) |
| HashVFL | [sj-3419195084](intro-source-maps/sj-3419195084.md) | 指定主源；[高层选读](research-choice-evidence-map.md#hashvfl) |
| Git LFS | [sj-4666101c6f](intro-source-maps/sj-4666101c6f.md) | 指定主源；[高层选读](research-choice-evidence-map.md#git-lfs) |
| Navigating the Risks（含Ethics的早期标题） | [sj-1966c7bea7](intro-source-maps/sj-1966c7bea7.md) | 指定主源；[高层选读](research-choice-evidence-map.md#navigating-risks) |
| Kernel Survey | [sj-b318fccf43](intro-source-maps/sj-b318fccf43.md) | 指定主源；[高层选读](research-choice-evidence-map.md#kernel-survey) |
| Transfer Attacks Revisited | [sj-097f6290bf](intro-source-maps/sj-097f6290bf.md) | 指定主源；[高层选读](research-choice-evidence-map.md#transfer-revisited) |
| Adversarial Examples Versus Cloud-based Detectors: A Black-box Empirical Study | [sj-ba26f30f1b](intro-source-maps/sj-ba26f30f1b.md) | 指定主源；[高层选读](research-choice-evidence-map.md#cloud-detectors) |
| DEEPSEC | [sj-299c65ef97](intro-source-maps/sj-299c65ef97.md) | 指定主源；[高层选读](research-choice-evidence-map.md#deepsec) |
| De-Health | [sj-f181e99eae](intro-source-maps/sj-f181e99eae.md) | 指定主源；[高层选读](research-choice-evidence-map.md#de-health) |
| De-SAG | [sj-5c5bf79d86](intro-source-maps/sj-5c5bf79d86.md) | 指定主源；[高层选读](research-choice-evidence-map.md#de-sag) |
| OB-WSPES | [sj-1ab158f15f](intro-source-maps/sj-1ab158f15f.md) | 指定主源；[高层选读](research-choice-evidence-map.md#ob-wspes) |
| V-SHUTTLE | [sj-0f6adb9f11](intro-source-maps/sj-0f6adb9f11.md) | 指定主源；[高层选读](research-choice-evidence-map.md#v-shuttle) |
| iFIZZ | [sj-10097c51e8](intro-source-maps/sj-10097c51e8.md) | 指定主源；[高层选读](research-choice-evidence-map.md#ifizz) |
| Cert-RNN | [sj-acbc08a57a](intro-source-maps/sj-acbc08a57a.md) | 指定主源；[高层选读](research-choice-evidence-map.md#cert-rnn) |
| Towards Certifying the Asymmetric Robustness for Neural Networks: Quantification and Applications | [sj-593cbfaf86](intro-source-maps/sj-593cbfaf86.md) | 指定主源；[高层选读](research-choice-evidence-map.md#amoeba) |
| Dynamic Attention | [sj-64e052ffcd](intro-source-maps/sj-64e052ffcd.md) | 指定主源；[高层选读](research-choice-evidence-map.md#dynamic-attention) |
| PROMFUZZ | [sj-92070abe8e](intro-source-maps/sj-92070abe8e.md) | 指定主源；[高层选读](research-choice-evidence-map.md#promfuzz) |
| Smart Contract Graph Feature / Expert Pattern Fusion | [sj-fa1fc1d2fa](intro-source-maps/sj-fa1fc1d2fa.md) | 指定主源；[高层选读](research-choice-evidence-map.md#smart-contract-fusion) |
| Mars | [sj-a7b06c257f](intro-source-maps/sj-a7b06c257f.md) | 指定主源；[高层选读](research-choice-evidence-map.md#mars) |
| Backdoor Pre-trained Models Can Transfer to All | [sj-318347dd2f](intro-source-maps/sj-318347dd2f.md) | 指定主源；[高层选读](research-choice-evidence-map.md#ptm-transfer) |
| Towards Practical Backdoor Attacks on Federated Learning Systems | [sj-5322b1646f](intro-source-maps/sj-5322b1646f.md) | 指定主源；[高层选读](research-choice-evidence-map.md#practical-fl-backdoor) |
| OTCCLIP | [sj-b5a1988e4d](intro-source-maps/sj-b5a1988e4d.md) | 指定主源；[高层选读](research-choice-evidence-map.md#otcclip) |
| Enkidu | [sj-c423d986aa](intro-source-maps/sj-c423d986aa.md) | 指定主源；[高层选读](research-choice-evidence-map.md#enkidu) |
| SirenAttack | [sj-879f8c1810](intro-source-maps/sj-879f8c1810.md) | 指定主源；[高层选读](research-choice-evidence-map.md#sirenattack) |
| Pluggable Watermarking | [sj-e8edda9d3a](intro-source-maps/sj-e8edda9d3a.md) | 指定主源；[高层选读](research-choice-evidence-map.md#pluggable-watermarking) |
| Order within Chaos | [sj-5dc666fe14](intro-source-maps/sj-5dc666fe14.md) | 指定主源；[高层选读](research-choice-evidence-map.md#order-within-chaos) |
| TWIST | [sj-43466107a4](intro-source-maps/sj-43466107a4.md) | 指定主源；[高层选读](research-choice-evidence-map.md#twist) |
| Plasticity / Angel or Demon | [sj-69a91ca701](intro-source-maps/sj-69a91ca701.md) | 指定主源；[高层选读](research-choice-evidence-map.md#plasticity) |
| NeuroBreak | [sj-cc3b714b43](intro-source-maps/sj-cc3b714b43.md) | 指定主源；[高层选读](research-choice-evidence-map.md#neurobreak) |
| Activation Steering | [sj-c7b0f8c968](intro-source-maps/sj-c7b0f8c968.md) | 指定主源；[高层选读](research-choice-evidence-map.md#activation-steering) |
| MCP Red Teaming | [sj-a68fd421b9](intro-source-maps/sj-a68fd421b9.md) | 指定主源；[高层选读](research-choice-evidence-map.md#mcp-red-teaming) |
| Adversarial CAPTCHAs | [sj-54704a792c](intro-source-maps/sj-54704a792c.md) | 指定主源；[高层选读](research-choice-evidence-map.md#adversarial-captchas) |
| A Practical Black-box Attack on Source Code Authorship Identification Classifiers | [sj-7fbc935f66](intro-source-maps/sj-7fbc935f66.md) | 指定主源；[高层选读](research-choice-evidence-map.md#source-code-authorship) |
| Learned Provenance Baseline | [sj-beba53e0f9](intro-source-maps/sj-beba53e0f9.md) | 指定主源；[高层选读](research-choice-evidence-map.md#learned-provenance-baseline) |
| Cryptographic API Misuse Detection | [sj-906728a4eb](intro-source-maps/sj-906728a4eb.md) | 指定主源；[高层选读](research-choice-evidence-map.md#crypto-api-misuse) |
| Turbo | [sj-a258b38871](intro-source-maps/sj-a258b38871.md) | 指定主源；[高层选读](research-choice-evidence-map.md#turbo) |
| FraudShield | [sj-056bd3713f](intro-source-maps/sj-056bd3713f.md) | 指定主源；[高层选读](research-choice-evidence-map.md#fraudshield) |
| Password Correlation | [sj-9aee30689b](intro-source-maps/sj-9aee30689b.md) | 替代主源；同一性未证；[高层选读](research-choice-evidence-map.md#password-correlation) |
| Enhancing Adversarial Transferability with Adversarial Weight Tuning | [sj-e64a3bfbe3](intro-source-maps/sj-e64a3bfbe3.md) | 指定主源；[高层选读](research-choice-evidence-map.md#awt) |
| Protecting Object Detection Models from Model Extraction Attack via Feature Space Coverage | [sj-ed7c58b655](intro-source-maps/sj-ed7c58b655.md) | 指定主源；[高层选读](research-choice-evidence-map.md#osd) |
| TextBugger: Generating Adversarial Text Against Real-world Applications | [sj-238a78de63](intro-source-maps/sj-238a78de63.md) | 指定主源；[高层选读](research-choice-evidence-map.md#textbugger) |
| Copyright Gap | [sj-b3dda6f2a5](intro-source-maps/sj-b3dda6f2a5.md) | 指定主源；[高层选读](research-choice-evidence-map.md#copyright-gap) |
| PerMemSafe | [sj-c89935c6fb](intro-source-maps/sj-c89935c6fb.md) | 指定主源；[高层选读](research-choice-evidence-map.md#permemsafe) |
| DPCSS | [sj-1e368cddf8](intro-source-maps/sj-1e368cddf8.md) | 指定主源；[高层选读](research-choice-evidence-map.md#dpcss) |
| FirmSec | [sj-0010159902](intro-source-maps/sj-0010159902.md) | 指定主源；[高层选读](research-choice-evidence-map.md#firmsec) |
| Mandela-effect Benchmark | [sj-f4f8acaf2d](intro-source-maps/sj-f4f8acaf2d.md) | 指定主源；[高层选读](research-choice-evidence-map.md#mandela) |
| CS-LSTMs | [sj-c87b27b4a0](intro-source-maps/sj-c87b27b4a0.md) | 指定主源；[高层选读](research-choice-evidence-map.md#cs-lstms) |
| Code Rewriting Detector | [sj-db9fe86207](intro-source-maps/sj-db9fe86207.md) | 指定主源；[高层选读](research-choice-evidence-map.md#code-rewriting) |

## 当前无完整图的7个指定全文

这些来源身份和历史选择卡仍保留，2026-10-04不可得状态未被新读取取代；不能从旧记录、摘要或标题重构P/S内容。Waltzz原不可得记录保留于来源JSON的reading_history；The Last Mile of Fuzzing原不可得记录同样保留，二者恢复后的完整图见上表。需要使用以下来源的精细写法时先取得所列精确版本。

- One Bad Apple Spoils the Barrel（sj-341a3df6b4）：arXiv:2212.13716v2，2022-12-29；不是2024 TDSC最终版；[指定原文](https://arxiv.org/pdf/2212.13716v2)；[历史选读卡](research-choice-evidence-map.md#one-bad-apple)
- ADAPDOOR（sj-361d2d7137）：14-page NESA author-hosted TIFS manuscript；[指定原文](https://nesa.zju.edu.cn/download/auto_20260921_TIFS2026_ADAPDOOR.pdf)；[历史选读卡](research-choice-evidence-map.md#adapdoor)
- AEIOU（sj-3f8dd6be89）：arXiv:2412.18123v3 [cs.CR], 2025-12-09, 15 pages, seven authors；[指定原文](https://arxiv.org/pdf/2412.18123v3)；[历史选读卡](research-choice-evidence-map.md#aeiou)
- StealthGraph（sj-b3c120b511）：Official ACL 2026 long-paper proceedings, final title StealthGraph；[指定原文](https://aclanthology.org/2026.acl-long.295.pdf)；[历史选读卡](research-choice-evidence-map.md#stealthgraph)
- FLEXFUZZ（sj-4418753cee）：Author-lab-hosted IEEE-formatted TIFS volume 20 (2025) pp.11728-11743；[指定原文](https://nesa.zju.edu.cn/download/LH_TIFS_2025_FINAL.pdf)；[历史选读卡](research-choice-evidence-map.md#flexfuzz)
- Text Captcha Is Dead?（sj-ff8570d878）：Author-hosted 16-page CCS 2020 manuscript, printed pp.1-16；[指定原文](https://nesa.zju.edu.cn/download/Text%20Captcha%20Is%20Dead%20A%20Large%20Scale%20Deployment%20and%20Empirical%20Study.pdf)；[历史选读卡](research-choice-evidence-map.md#text-captcha-dead)
- SOPE（sj-c723f714dd）：Official ICML 2026 PMLR 306 full proceedings PDF, 25 physical pages；[指定原文](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lin26r/lin26r.pdf)；[历史选读卡](research-choice-evidence-map.md#sope)

## 替代主源的单独边界

Password Correlation的指定NESA副本在该次不可得，完整图实际来自[共同作者CMU托管9页INFOCOM 2017副本](https://www.cs.cmu.edu/~anupamd/paper/Infocom2017.pdf)。标题、作者及会议格式相符，逐字节同一性未建立；不能说指定NESA URL已在该次完整读取。图中页码和句序以实际副本为准。

# ADD：科学证据、运行点与范围

- policy: Separate sourceclaim/verification/qualification ledger; main purpose is scholarly writing analysis, no attack/defense execution

## B1

- source: §III-A/Bpp2–3;§III-Dp4;§Vp14–15
- author_claim: Defender knows target model internals/training material and a practical feasible manipulation subset, but not specific attacker algorithms or their generated samples.
- verified_scope: The practical partition is specific to target feature representation and feasible operations; it does not exhaust all valid manipulations. Some representations require transfer rather than direct quantification.
- qualification: Plugin deployment does not imply model-agnostic training or no internal access; benign-output placement and defender access answer different questions.
- writing_relevance: Keep threat resources separate from deployment convenience; treated/practically are part of meaningful task framing.

## B2

- source: §III-E/Fpp4–7;§IV-G/Ipp13–14
- author_claim: Learned representations make cross-part incompatibility measurable; constrained pseudo samples provide attack-relevant surrogates without actual attacker APKs.
- verified_scope: The paper reports empirical separation and partial pattern overlap; per-method cosine0.468/0.470/0.424 andJS0.158/0.155/0.163 are forDrebin/Drebin-DL/APIGraph.
- qualification: Not equality of realAPK distributions or a completeness guarantee; no supplementary algorithms were retrieved or run.
- writing_relevance: Mechanism explanation may stop at measurable relation inIntro; full encoder/loss/procedure details need not dominate the reader path.

## B3

- source: §III-Fpp6–7;§IV-Ap8;TablesI/IIp9
- author_claim: Calibration balances recovery against added false positives using a separate set.
- verified_scope: TNIR divides newly misflagged base true negatives by all base true negatives;FNIR divides recovered base false negatives by all base false negatives. Calibration constrainsTNIR and choosesoperatingpoint forFNIR.
- qualification: 1%TNIR is not a one-percentage-point overallTNR reduction or wholeaccuracy loss; test-set realizedTNIR varies.
- writing_relevance: The deployment interface creates these two relevant populations; contribution pairs detection with calibration for a reason.

## B4

- source: IntroP5.S2–S3p2;TablesI–IIIp9
- author_claim: Intro reports over95%NDASR, superiority to named baselines, and approximately50%FN improvement with1%TN impact.
- verified_scope: NDASR is relativeASR reduction. TimeDrebinADZ is80.49/94.32/97.53 at1/5/10% calibration budgets. TimeDrebin-DL at1%:63.66/47.89/46.69 forADZ/MAB/RA. TableII1%calibration runs showFNIR30.02–63.01%. TableIIIADD is92.40–98.32 at5%.
- qualification: No universalover95 lower bound across budgets; retain original attributed headline but do not append a stronger universal quantifier. Comparisons and normal-data recovery use different operating points/denominators.
- writing_relevance: Mainmethodvalue is pairedrobustness/utility; source-oriented scientific clarification belongs beside rather than inside every preserving alternative.

## B5

- source: §IV-Ap8 andTableIIIp9
- author_claim: ADD improves comparative defense effectiveness over selected baselines in the evaluated setup.
- verified_scope: FD-VAE/adversarialtraining are adapted; adversarial training uses pseudo samples; HagDe useshalf generated real adversarial samples fortraining andhalf for evaluation.
- qualification: Not identical training-information assumptions across all baselines; no independently rerun ranking.
- writing_relevance: Fairly acknowledge nearest existing answers; source superiority should retain the setup in explanatory context.

## B6

- source: IntroP5.S4p2;§IV-Dpp11–12;TableVIIp12
- author_claim: Defense effectiveness under three evaluated adaptive settings.
- verified_scope: Each100randomtruepositive malware samples andquerybudget10; TableVIIatTNIR5 includesASR0–15.69. Source prose usuallybelow15 isnotstrictallbelow15.
- qualification: Representative bounded evaluation, no complete robustness guarantee; no attacks were implemented in this work.
- writing_relevance: eachusing clause supplies meaningful evidence scope while the positive result remains intact.

## B7

- source: IntroP5.S5–S7p2;§IV-Epp12–13;TablesVIII/IX
- author_claim: Transfer-based enhancement onVirusTotal-related adversarial samples and effectiveness onlater malware.
- verified_scope: Generation success reduces countofdetecting engines;805/819generatedAPG samples in temporal/random settings. InternalAVknowledge unavailable; trainedknown-model encoders/thresholds transferred. VSin2022 evaluated againstearlierAPGtraining; RHlaterdata also evaluated.
- qualification: Not evasion of everyengine, not direct white-boxADDinsideeveryAV, not timelessrobustness. TableIXhas lower values, e.g.timeDrebin59.94at1%; headlineover90isnotallVSsettings.
- writing_relevance: Concrete relativeclause supplies what externalresultmeasures; temporal axis adds a different applicationquestion rather than another numerical synonym.

## B8

- source: §IV-Cp11;Fig2
- author_claim: Modest addedinference overhead.
- verified_scope: Under0.9seconds for10000application batch,10repetitions, measuredextra runtime beyondbase detector inclprojection/encoder components.
- qualification: Not full staticanalysis,partitionconstruction ortraining cost; no end-to-end latencybenchmark performed here.
- writing_relevance: If selected forIntro it supportsdeploymentcost, but cannot substitute for detection/benignimpacttaskanswer.


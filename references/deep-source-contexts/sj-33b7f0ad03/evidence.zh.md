# FreeEagle：资源条件、比较对象与科学证据范围

- role: Companion evidence scope; established evaluation-choice reasoning preserved, not promoted as new discovery

## B1

- coordinates: §2.4 p4; §3.1 pp4–5; §3.2 p5
- source_facts: Platform-maintainer offline inspection has white-box model access but no clean/trigger task samples. Feature priority is relative to source-class benign features. Model splitting alone is not the novel discrimination signal.
- writing_role: Role→materials→observation level; retain some and no-data/white-box distinction
- scope: No black-box-only claim, no training/data-collection procedure or attack implementation

## B2

- coordinates: §3.2–3.4 pp5–7; §5.6/Table6 p11
- source_facts: Dummy intermediate representations supply class-conditioned observations; anomaly analysis examines cross-class outputs rather than only generating samples. Source argues classifier-only inspection lowers cost and enables all class-pair checks. Table6 FreeEagle times are602s/81s/1058s/18s for ResNet50 ImageNet-R/VGG16 CIFAR10/GoogLeNet GTSRB/CNN7 MNIST, respectively; STRIP is faster but needs data.
- writing_role: Preserve method→cost→coverage→task endpoint and generation→indicator usefulness
- scope: Source-relative cost argument is not a claim of being fastest detector or a controlled speedup factor against every competing implementation

## B3

- coordinates: §5.1/Table4 p9; §5.3/§5.5 p10
- source_facts: Fixed thresholds chosen on randomly held30% trojaned and30% benign model subsets; remaining models test; threshold calibration constrains training FPR<=.05; ten repeats average TPR/FPR. Pooled §5.5 benchmark includes all trained trojaned/benign models from §4.3:FreeEagle .65/.04 versus DF-TND .11/.05.
- writing_role: Mixed benchmark best answers unknown attack-setting concern, not interchangeable with highest single cell. Qualitative cross-condition answer remains valid without reducing to a vague possibility.
- scope: Data-free sample access does not mean no labeled model-set calibration; benchmark mixture is not a universal deployment distribution or guaranteed test FPR bound

## B4

- coordinates: Table4 p9 and §5.3–5.4 p10; Table5 p11
- source_facts: GTSRB/GoogLeNet blending class-agnostic .99/.04; same dataset/model class-specific .76/.04. CIFAR10/VGG16 blending class-agnostic .73/.04. Table5 natural ImageNet-R/ResNet50 FreeEagle .62/.05; composite CIFAR10/CNN7 FreeEagle .86/.05 versus ANP .90/.05.
- writing_role: Preserve same-resource main comparison and some higher-resource successes. Do not substitute a best cell for pooled result or turn some into all.
- scope: Reported detection TPR/FPR are not attack success rates; no unreported aggregate constructed

## B5

- coordinates: §6 pp11–12; §7 pp12–13
- source_facts: Adaptive evaluation considers two strategies on GTSRB/CIFAR10, class-agnostic setting and three trigger types. Later discussion notes class-count and data-augmentation sensitivity.
- writing_role: Keep valid source effectiveness claims while stating evaluated scope separately
- scope: No universal adaptive-robustness theorem, no present-day novelty certification or implementation/exploitation steps


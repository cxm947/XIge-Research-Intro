# Practical FL：数值身份、对照与时间边界

## B1

- source: p.8/5438 TableI image, LOAN row group; p.7/5437 §V and §VI-A
- type: visually_verified_table_cells
- task: LOAN
- distribution: non-IID (table prints no-IID)
- client_count: 51
- metric: ΔAccuracy
- units: Source table reports %; retain source metric, no unreported relative normalization assumed
- timing:
  - AA: immediately after attack round per table footnote
  - AT: after training process per footnote; §VI-A discusses 10 subsequent rounds, not a redefinition of AA
- cells:
  - 
    - column: theta=100 full-model baseline
    - ARSN: 1.0
    - AA_ASR: 100
    - AT_ASR: 100
    - AA_DeltaAccuracy: 21.3
    - AT_DeltaAccuracy: 2.7
  - 
    - column: theta=10
    - ARSN: 0.06
    - AA_ASR: 100
    - AT_ASR: 57
    - AA_DeltaAccuracy: 4.3
    - AT_DeltaAccuracy: 0.6
  - 
    - column: theta=30 context only, not intro 4.3 setting
    - ARSN: 0.2
    - AA_ASR: 100
    - AT_ASR: 94
    - AA_DeltaAccuracy: 8.7
    - AT_DeltaAccuracy: 1.1
- conclusion: Introduction 21.3/4.3 numerically matches immediate main-task loss cells from full-model and theta10 columns. It is not ASR, not later loss, not a cross-task mean, and not joint proof of persistent high ASR.
- comparator_identity: §V describes full-model baseline as corresponding to previous model replacement, but additionally strengthened using the paper techniques. Do not call an unchanged reproduction of original prior method.
- source_tension: §VI-A prose says loan after-training loss less than1.1, table prints1.1; retain displayed precision and do not invent extra decimals.

## B2

- source: p.3/5433 §III-A; p.7/5437 §V; p.8/5438 TableI
- type: goal_and_metric
- observed: Basic threat model controls one client; effectiveness uses ASR; stealthiness uses main-task ΔAccuracy; actual selection uses ARSN. Selection threshold is not identical to actual neuron ratio.
- scope: Two performance goals are distinct. Stealthiness measured as main-task performance change is a proxy, not proof no detector can notice. §VI-E later studies multiple-client extensions separately.
- example_guard: P7.S3 10% and >90% are illustrative. Source does not identify one universal joint setting with loan4.3 and future ASR>90.

## B3

- source: p.9/5439 §VI-D/Fig4; p.10/5440 §VI-D/Fig5 and §VI-F/TableII
- type: persistence_and_ablation
- observed: Fig4 is a one-shot retina study, with random-selection baseline and follow-on success trajectory. Whole-model modification lasts longer but damages main task more. Fig5 uses a continuous intervention period then observes persistence and compares PGD/combination, on CIFAR10 and EMNIST; it is a distinct design.
- tableII:
  - task: retina disease detection
  - measurement: 20 rounds after attack
  - reported_rows:
    - 
      - method: None
      - ASR: 43
      - DeltaAccuracy: 1.2
    - 
      - method: BG
      - ASR: 65
      - DeltaAccuracy: 2.1
    - 
      - method: FA
      - ASR: 74
      - DeltaAccuracy: 1.6
    - 
      - method: Both
      - ASR: 82
      - DeltaAccuracy: 2.4
  - units: Source percentage entries; no new operating recommendations
  - source_configuration: theta=30 as reported in §VI-F; descriptive study identity only
- supports: Temporal persistence separate from immediate attack success; combination improves later success in tested setting with main-task tradeoff
- does_not_support: Permanent persistence, no added main-task cost, every timing/distribution or single fixed baseline across figures

## B4

- source: p.11/5441 §VII/TableIII context
- type: platform_scope
- observed: Four named platforms tested using LOAN for demonstration; normal/fast implementations distinguished by source.
- supports: Platform feasibility under reported historical research setup
- does_not_support: Four use cases crossed with four platforms; current-version security diagnosis; evidence of real compromised deployments
- analysis_boundary: No operational platform manipulation steps retained or expanded
- variant_identity: TableIII N/F means normal/fast attack variants, not platform software release versions. No particular framework release number is verified here.

## B5

- source: p.11–13/5441–5443 §VIII and p.14/5444 §IX; p.10/5440 §VI-E
- type: defense_tradeoff
- observed: Some defenses work in one-shot settings; outcomes differ with repeated/adapted conditions. DP and pruning reduce attack effect while affecting main-task utility. Separate experiments show defenses can slow/increase attack resource needs. Source later notes large-scale limitations and leaves other FL paradigms for future work.
- supports: Conditional unresolved robustness/utility challenge, not a claim defenses have zero effect
- does_not_support: Universal bypass, irreversible failure of all defenses, or deployment-wide present insecurity
- safe_scope: Qualitative outcome/source-role analysis only; no adaptive bypass procedures

## B6

- source: p.3/5433 §II late-neighbor paragraph; p.14/5444 §IX
- type: positioning
- observed: Source acknowledges a work arising during review that also uses less-updated parameters, and emphasizes its own real-world framework evaluation. Basic single-client assumption is contrasted with an earlier multi-client work.
- supports: Keep first-practical claim as attributed, historically positioned source claim
- does_not_support: Independent firstness certification or assertion all similar prior methods absent

## B7

- source: p.2/5432 P8.S1 versus p.11–12/5441–5442 §VIII-A
- type: terminology_tension
- observed: Introduction labels median defense as coordinate geometric median, whereas body names coordinate-wise median and defines coordinate-wise operation.
- handling: Record source-level naming mismatch; do not infer an additional tested geometric-median experiment. Do not silently correct original phrasing as if printed differently.


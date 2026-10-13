# ContractFusion：设置、比较与解释性证据边界

## B1

- source_coordinates: p.5 §4.1 left bottom and right top; p.5 §4.2 right top
- type: reported-setting
- observed:
  - ESC_contracts: 40932
  - ESC_functions: 307396
  - VSC_contracts: 4170
  - VSC_functions: 13761
  - split: 80%/20% functions randomly selected
  - task_mapping:
    - reentrancy: ESC
    - timestamp_dependence: ESC
    - infinite_loop: VSC
- supports: Function-level evaluation and source-dataset scope
- does_not_support: Contract-disjoint split, temporal generalization, cross-platform transfer, all three tasks independently on both datasets
- source_tension: P6.S6 says 40k in two datasets; body gives 45,102 total contracts. Retain as source approximation/tension rather than silently replace the original wording.

## B2

- source_coordinates: p.6 Table3; p.2 left P6.S6; p.5–6 §4.2
- type: reported-results-plus-arithmetic
- comparisons:
  - 
    - task: reentrancy
    - dataset: ESC
    - comparator: TMP
    - baseline_accuracy: 84.48
    - AME_accuracy: 90.19
    - difference_percentage_points: 5.71
    - intro_rounded_pair:
      - 84
      - 90
  - 
    - task: timestamp dependence
    - dataset: ESC
    - comparator: TMP
    - baseline_accuracy: 83.45
    - AME_accuracy: 86.52
    - difference_percentage_points: 3.07
    - intro_rounded_pair:
      - 83
      - 87
  - 
    - task: infinite loop
    - dataset: VSC
    - comparator: TMP
    - baseline_accuracy: 74.61
    - AME_accuracy: 80.32
    - difference_percentage_points: 5.71
    - intro_rounded_pair:
      - 75
      - 80
- weaker_baseline_do_not_substitute:
  - 
    - task: reentrancy
    - comparator: Slither
    - accuracy: 77.12
    - AME_accuracy: 90.19
    - difference_percentage_points: 13.07
  - 
    - task: timestamp dependence
    - comparator: Slither
    - accuracy: 74.2
    - AME_accuracy: 86.52
    - difference_percentage_points: 12.32
  - 
    - task: infinite loop
    - comparator: Looper
    - accuracy: 59.56
    - AME_accuracy: 80.32
    - difference_percentage_points: 20.76
- supports: AME comparison with strongest listed neural accuracy baseline on three task/dataset pairs
- inference: Introduction does not name TMP in that sentence; numerical mapping is established from Table3. Why authors selected these reference points is editorial inference, not reported author intent.
- does_not_support: Average result, relative percentage improvement, causal isolation of attention, superiority to every prior system, or fresh experimental replication

## B3

- source_coordinates: p.2 §2; p.4–5 §3.3; p.6–7 §4.3 and Figs3–5
- type: output-definition-and-author-interpretation
- observed: System outputs binary vulnerability label and feature-associated weights. Weight equations are normalized feature/final-representation inner-product scores. Statistics compare >0.25 frequency, maximum frequency, means and deviations; case study shows graph .27 and three local patterns .23,.26,.24 for reentrancy.
- supports: Inspectability of per-feature weights and local-pattern hints; aggregate reported weight distributions; one illustrated function
- does_not_support: Ground-truth causal contribution percentages, faithful explanations by intervention, human debugging gains, exact vulnerable-line localization or automated repair
- wording_boundary: Source itself asserts explanation of prediction reasons. Authored analysis records this as an author interpretation rather than suppressing it or upgrading it to externally validated faithfulness.

## B4

- source_coordinates: p.7 §4.4 and Fig6
- type: reported-ablation
- observed: AME-RG removes graph branch; AME-RP removes local pattern branch and is described as almost TMP. Source reports complete AME consistently better across shown epochs for three vulnerabilities; graph removal gives larger drop.
- supports: Within-setting evidence for complementary branches, with unequal apparent contribution to accuracy
- does_not_support: Necessity theorem, exact digitized performance deltas from plots, isolation of self/cross attention, or faithful attribution weights
- verification: Read text and visually inspect curves; no plot digitization or rerun

## B5

- source_coordinates: p.2 C1.S2/C3.S3; p.8 §5 final sentences
- type: source-positioning
- observed: Source says Liu2021 already combines expert rules and neural networks for accuracy; current work foregrounds explainability and feature importance.
- supports: Qualified explainability-centered contrast
- does_not_support: Unqualified first fusion or numerical superiority to the nearest fusion paper
- boundary: Liu2021 full text not read here; Table3 does not list that paper as an explicit separate method

## B6

- source_coordinates: p.3 §3.1–3.2; p.4–5 §3.3
- type: mechanism
- observed: Experts define vulnerability-specific patterns; tools extract them. Graphs encode function control/data dependencies. Local patterns and graph features pass through separate extraction and fusion; output weights are computed alongside label.
- supports: Specific information roles behind local/global fusion and separation of mechanism from outcome
- does_not_support: Automatic discovery of expert patterns, semantic correctness proof, direct equivalence between output weights and causal effects


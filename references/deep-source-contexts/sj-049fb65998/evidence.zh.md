# IMMI：指标、分母与科学证据范围

- role: Companion scientific factual checks; subordinate to principal writing methodology

## B1

- coordinates: §6.1–6.3 physical12/4079, Tables1–2
- source_facts: Linux5.18 evaluation:123 unique reports,80 manually judged real/new bugs;72 confirmed or fixed by community at submission. Table1 end-to-end35m12s, including25m49s LLM I/O; prose/Introduction summarizes within35min.
- writing_role: Whole-system cost answers scalability; true findings and external maintenance status answer different questions.
- scope: Do not replace full runtime with static-only~9min,80 with80 externally confirmed, or35min prose with a precise<=35min service promise. Facts already substantially retained.

## B2

- coordinates: §6.5 physical13/4080; Table2 physical12/4079
- source_facts: Without LLM:158 reports, including3 additional true bugs and32 additional false positives compared with combined pipeline. Combined:123 reports,80 true,43 false; reconstructed static-only totals83 true/75 false. Authors summarize43% false-positive reduction and~4% introduced false negatives; without LLM FDR47.5%.
- arithmetic_status: 32/75≈42.7%;3/83≈3.6% are explanatory arithmetic consistent with rounded source summaries, not new experimental estimates.
- writing_role: Retain benefit/cost pair and distinct denominator identities; only is an author valuation, not a universal cost threshold.
- scope: Not global kernel recall, not43 percentage-point accuracy gain. Intro4% is preserved in V4; body approximation/denominator is a separate qualifier.

## B3

- coordinates: §4.2 physical7/4074; §4.3–4.4 physical9–10/4076–4077; §4.5 physical10–11/4077–4078
- source_facts: Object summaries include releases and resets; safe post-release nulling cases are excluded. Intentions use object/path behavior; LLM aids implicit mechanisms/comments. Intra-procedural inconsistencies are also considered.
- writing_role: Responsibility is an analysis relation, not mind-reading; paired examples motivate a heuristic, not an unconditional rule.
- scope: No detector or exploit implementation; no stepwise operational recipe provided.

## B4

- coordinates: §5 physical11/4078; §6.4–6.5 physical13/4080
- source_facts: LLM is used after static analysis flags inconsistencies. Calls and paths have approximations;40 injected-bug test finds37, with missed leaks linked to call-depth limit. LLM false-negative cases include assuming a release function cleans up all resources based on functional inference/naming.
- writing_role: Keep design roles separate from validation claims; independence from pairing does not guarantee an auxiliary model never repeats a similar semantic assumption.
- scope: The synthetic37/40 test and ablation3 lost true bugs are separate. Do not convert either to full-kernel recall.

## B5

- coordinates: §6.6 physical14–15/4081–4082; Table4 physical15
- source_facts: Authors characterize cross-tool time/precision as high-level comparisons across different kernels/environments. Bug overlaps are28/24/26 with IPPO/HERO/MLEE; MLEE rules reconstructed because code/weights unavailable.
- writing_role: Claim complementarity/coverage differences at the evidence strength actually supplied, rather than controlled fastest/best superiority.
- scope: These were already in the baseline, not newly discovered metrics or independently reproduced outputs.


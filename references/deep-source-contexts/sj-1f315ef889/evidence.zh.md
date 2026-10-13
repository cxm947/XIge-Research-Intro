# MPInspector：证据对象、职责与适用范围

- role: Companion factual/evidence boundaries, deliberately separate from principal writing-choice profile

## B1

- coordinates: §4.1概述续文及§4.2–4.3，physical5/4208；§4.5–4.8，physical8–9/4211–4212
- source_fact: Framework inputs include traffic, documentation and configuration. Traffic is prioritized; documents supplement semantics not extractable from traffic and may differ from implementation. Properties combine specification-derived meta properties and implementation-based extensions.
- writing_relevance: Preserve the intermediate dependency, not merely the two object names. Standard properties alone cannot answer implementation-specific question.
- scope: This is conceptual source analysis, not configuration or exploitation instructions.

## B2

- coordinates: §5.4 physical13–14/4216–4217; Tables4/5 physical14
- source_fact: 45 experts validate reported semantics and property violations. Violation precision reported100%; no recall because complete violation truth unavailable. Semantics precision96% on the Aliyun MQTT implementation; Aliyun CoAP and other tested cases100%; extra20-platform document extraction94.87%. Four implementation state machines can be checked against code/vendor help; six cannot.
- writing_relevance: C1 precision and P9 with-precision need metric-object and evidence-level discipline. Numbers were already retained; not advertised as fresh discoveries.
- scope: No blanket model completeness, no 100% recall, no claim every component has100% precision.

## B3

- coordinates: §4.8 physical9/4212；C1.S2；§4.2 physical5/4208
- source_fact: Three supported protocols; new implementation supplies three inputs. New protocol requires one-time protocol-level adaptations/knowledge.
- writing_relevance: Parallel contribution adjectives have different evidentiary bases: measured precision versus described extensibility/configurability.
- scope: Source ability claim preserved; no independent cross-protocol extensibility benchmark established here.

## B4

- coordinates: §4.4不确定性/效率讨论 physical7/4210；§4.7 physical9/4212
- source_fact: Learning uses repeated-hypothesis stopping to handle uncertainty; custom queries reduce reported time34%. Verification helper changes goal order; source illustrates a13-step disproof of an AWS authentication lemma.
- writing_relevance: Internal adaptations have distinct duties. Completion of a proof/disproof is not proof that the evaluated platform is secure.
- scope: No generic termination/completeness theorem inferred and no operation/heuristic recipe delivered.

## B5

- coordinates: P9/C2; §3 physical4/4207; §5.1–5.3
- source_fact: Three protocol types, nine platforms, ten implementations; source reports57 customized properties,252 violations and11 attack types, under two stated threat scenarios. Tool final outputs are violated properties; further attack identification and validation have additional roles.
- writing_relevance: P9.S4 actor shift and C2 sequence preserve inference/output levels.
- scope: Counts are not additive independent vulnerabilities; no arbitrary remote capability or current-vulnerability claim.

## B6

- coordinates: §5.4/Table4 physical14/4217; §5.3.3 physical13/4216
- source_fact: Authors report approximately4.5-hour mean end-to-end overhead and identify interaction learning as bottleneck. Comparator discussion reports broader protocol/scenario coverage and four additional attacks, while two earlier issues fall outside current design focus.
- writing_relevance: System-level time responds to expert workload; maximum tool coverage is not total dominance.
- scope: Time is attributed report, not a newly recomputed mean or reproduction. Factual notes are supporting constraints rather than the main writing methodology.


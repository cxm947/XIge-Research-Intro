# Graph AUD：模型、条件与理论参照的证据范围

- policy: Scientific source claims and limits; separate from principal editorial methodology. No algorithms implemented or experiments reproduced.

## B1

- source_scope: §III physicalpp2–3; §VII.B p6
- author_claim: Structural retention motivates a mathematically tractable edge/nonedge-based utility metric; chosen utility curves are consistent with it.
- checked_detail: Definition compares raw and anonymized graph structure, including existing/non-existing edges. Utility comparison uses degree,path-length,clustering-coefficient distributions on Enron/Facebook/Twitter.
- qualification: This is a selected structural proxy, not a theorem that every application utility is equivalent. No general-metric impossibility proof asserted.
- writing_relevance: Mathematical wording makes the relation analyzable; explain the shared object and measurement purpose before formulas.

## B2

- source_scope: §III p3; Theorems1/2 and remarks p4
- author_claim: Quantify achievable anonymity upper bound and de-anonymity lower bound under stated conditions; ER and broader arbitrary-degree-distribution models have different conditions.
- checked_detail: Theorem statements use O/Ω and inequality conditions. General-model conditions are stricter for the same target levels. The paper omits proofs. Remarks describe theoretically possible search with factorial complexity.
- qualification: No proof audit, tight-bound certification or feasible optimal mapping was performed; closed forms in the contribution do not mean exact attainable point values for every finite graph.
- writing_relevance: Keep source novelty/closed-form product strong and attributed while keeping scientific scope distinct from rhetorical alternatives.

## B3

- source_scope: §III p3; §VII.C p7; §VIII pp8–9
- author_claim: Auxiliary graph correlation and preserved utility condition attainable anonymity/de-anonymity.
- checked_detail: Theory uses shared/overlap-user formulation and correlation parameters. Evaluation derives or perturbs auxiliary graphs under specified settings. §VIII reports50-run averages.
- qualification: Real source datasets do not establish naturally collected auxiliary-information coverage; findings are conditional.
- writing_relevance: The given-auxiliary modifier in P3.S3 is a needed reader condition, not removable detail.

## B4

- source_scope: §VI physicalpp4–5
- author_claim: Adding AUD quantification to SecGraph improves relation understanding, target-driven configuration/evaluation and interpretation against theoretical bounds.
- checked_detail: Prior platform already includes anonymization,utility and de-anonymization modules. Repeated empirical runs can give setting-dependent intuition; new module provides a theoretical reference.
- qualification: The selected source does not supply a user study or runtime-controlled proof for every usefulness/time-efficiency claim. Preserve these as authors’ system-value claims rather than rewriting them as measured savings.
- writing_relevance: Why implement theory in a system; contribution is the new decision reference, not claiming all platform features as new.

## B5

- source_scope: TableI p5; §VII.A–C pp5–8; §VIII p8
- author_claim: 12 real-world datasets support AUD evaluation; the method comparison is a separate evaluation slice.
- checked_detail: §VIII uses Enron,Facebook,Twitter; contrasts two anonymization families and two reported attacks in source-defined settings. TableI Facebook64K nodes and0.82M edges agrees with Intro.
- qualification: Do not claim every method was exhaustively evaluated on all12 graphs; numerical counts indicate coverage, not deployed user outcomes.
- writing_relevance: C3 answers what varies across data; C4 answers what current methods leave unrealized.

## B6

- source_scope: Intro C4.S3 p2; §VIII Fig6 p8 and results p9
- author_claim: The Intro reports more than83.4% of theoretically de-anonymizable users not de-anonymized by ODA in the stated DP-anonymized Facebook example.
- checked_detail: Body divides practical success ratio by AUD theoretical reference; p9 expressly says denominator is only a lower bound. Across plotted scenarios source states ratio<.95; forDP, source states Enron<.25,Facebook<.5,Twitter<.16 for both attacks.
- qualification: 83.4 retained as Intro-reported claim, not independently digitized or assigned to a unique plotted parameter point. It is neither83.4% of all users nor a new method’s percentage-point gain.
- writing_relevance: Keep more-than, numerator/reference distinction and configuration; they make the headline a theory-use example.

## B7

- source_scope: §II p2 and §VIII pp8–9
- author_claim: DP-based graph techniques protect specified graph/link statistics, while the reported endpoint here is node reidentification under auxiliary structure.
- checked_detail: The Related Work describes link-information protection and §VIII describes a dK-seriesDP requirement.
- qualification: This analysis does not infer that a reidentification observation disproves the DP guarantee; privacy object and guarantee must be kept separate.
- writing_relevance: A result about unrealized reidentification should not be converted into a universal safety or attack-success slogan.


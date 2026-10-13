# FaceArmor source identity, evidence and scientific boundaries

## Exact source

Source ID sj-6a7f688210. Title: FaceArmor: A Universal Facial Image Protection Against Diffusion-Based Manipulations. Designated URL: https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/13026.pdf. Identity is the ECCV 2026 conference-hosted author PDF in the retained access record, not an unverified proceedings or arXiv substitute. PDF metadata creation time is 2026-06-29 13:14:16 +08:00; that is not asserted to be its publication date. It has 18 physical pages, 50,914,498 bytes, SHA-256 3afb23e11cbe665510ce1a38b77d709b38676f3a6ec66bf647af10ae67ad433b. The current and preserved analyses use this same designated source identity; no source-version substitution is claimed.

## Actual source reading and layout

Read all Introduction prose, physical pp.1–4, including all three full contribution bullets. Viewed the four existing local page renders. On p.2 the prose wraps around Fig.1; diagram speech and caption are not extra Introduction sentences. Table1 sits above P4 on p.3 and is separate from the prose; its categorical marks do not measure effect magnitude. P7's contribution organizer is retained in the 41-unit count.

To avoid layout-text interleaving, The research-only source record preserves exact PDF text-block indexes, bounding boxes and hashes; extracted primary text is not redistributed here. Normalization removes recorded discretionary line-break hyphens while retaining lexical zero-knowledge and texture-disrupting, then collapses whitespace. The normalization record binds each analyzed unit to its source hash. Offsets are Unicode characters, not PDF glyph coordinates. The 41 IDs match the historical ledger in order.

Body reread: §4 opening p.5; §4.1 pp.6–7 for structural/conceptual objectives and surrogate roles; §4.2 pp.7–9 for protected-image artifacts, proxy signals, complementary spatial weighting/projection and transformation objectives; §5.1 p.9 for models/cases; §5.2 pp.9–11 with Table2 p.10; §5.3 pp.11–12 with Tables4–5 p.12; §5.4 p.12 with Table3; §5.5 pp.12–14 with Table6 p.13 and Fig.4 p.14; §5.6 pp.13–14 with Table7 p.14. Only high-level design and evidence roles are carried into the writing analysis, not equations, attack steps or implementation recipes.

## Source strength is retained; the following are scientific qualifications

- The source states architecture invariance, exceptional zero-knowledge transferability, inevitable overfitting in its criticized route, and seamless/no-interference optimization. These are author claims, not weaker claims invented by this analysis or independently proven guarantees
- White-box surrogate VAE/ReferenceNet/CLIP/ArcFace access remains part of construction. Unknown/zero-knowledge refers to target-generator transfer, not an absence of model knowledge, network access or proxy internals. The Introduction's forward-pass phrase is retained as a source statement; no implementation proof of exclusively forward-only heatmap computation is claimed
- Four tasks are evaluated on SD v1.5/SD XL; SD3/Flux transfer is evaluated on inpainting. The case count is 800 images from 200 identities with ten prompts per source image; it does not turn the model/task counts into a full 4×4 design
- Generated-output quality and source-similarity metrics are not direct metrics of the user's protected-photo visual quality. Strong perturbation-budget and imperceptibility claims require their own interpretation; no new claim of perfect anonymity, identity concealment or zero practical privacy risk is inferred
- Table2 does not show strict superiority in every metric cell. For example, the retained SD1.5 editing FR comparison and inpainting FID exception are supported by the table. The high DiT FR values in Tables4–5 do not become complete identity erasure merely because they are the best relative ranks. These qualifications were already present in the baseline
- §5.4 tests JPEG, Gaussian noise, rotation and resizing. §4.2's optimization transformation list instead names Gaussian blur, JPEG compression, Gaussian noise and random resizing. Do not state that every tested operation, especially rotation, is explicitly listed in the optimization set. Measured resilience is not invariance to arbitrary processing
- §5.6 reports higher computational cost and frames the work as one-time offline preprocessing before sharing. The author's acceptable-tradeoff judgment is contextual, not universal user preference or proof of real-time suitability
- The source's dataset naming is not silently reconciled: §5.1 says VGG-Face, while Table2's caption says VGG-Face2. No new dataset-specific inference or replacement depends on resolving that difference

The complete Introduction layout was checked. Full-resolution inspection of every result table, chart, appendix image and code artifact was not performed; numerical examples use readable local table text and source prose. No proof validation, experiment reproduction, current-model/novelty survey, privacy attack implementation or measured writing-effect study is claimed. No author code or historical builder was executed in the source analysis.

# V-SHUTTLE：正文证据、编辑用途与未决边界

- scope: Body evidence read to constrain Introduction author-choice analysis. No implementation or exploit work. All findings are historical paper reports; editorial uses are labeled.
- interpretation_limit: No result count or statistical significance is independently inferred.

## E01

- section: §2.2 / Table 1
- locator:
  - pdf_page: 3
  - column: R
  - layout_lines:
    - 132
    - 190
- source_explicit: Selected 40 QEMU devices across categories; 29 support DMA, 72.5%. DMA is discussed as the complex data-processing stage after setup.
- supports:
  - P2.S3
  - P2.S4
  - C1.S1
- editorial_use: Supports choosing a consequential common input surface rather than introducing DMA only because it suits the mechanism.
- limits: Selected device inventory, not a random-population prevalence estimate or proof that all relevant code is DMA-related.

## E02

- section: §2.3 / Figure 2
- locator:
  - pdf_pages:
    - 4
    - 5
  - column: both
  - layout_lines:
    - 195
    - 319
- source_explicit: Nested form construction and node type awareness are distinguished. Unavailable pointer targets can halt testing before main functionality; node kinds and termination conditions vary.
- supports:
  - P2.S6
  - P2.S7
  - P2.S8
  - P4.S2
- editorial_use: Connect whole-tree and node-level constraints to distinct operational needs, while acknowledging that the Introduction has not fully developed dynamic type guidance yet.
- limits: Example and source analysis, not a proof that all device grammars are trees or all node dependencies are independent.

## E03

- section: §3.3
- locator:
  - pdf_page: 6
  - column: both
  - layout_lines:
    - 352
    - 426
- source_explicit: Source-level DMA redirection bypasses guest address resolution to supply fuzzing data. Only guest-origin data read by the target device is manipulated, not data written back.
- supports:
  - P4.S3
  - C2.S1
- editorial_use: Read the result/goal clauses as input availability despite pointer values, not full protocol reconstruction.
- limits: Target-device read scope; source modification required; availability does not guarantee useful input or observed coverage of every branch.

## E04

- section: §3.4
- locator:
  - pdf_pages:
    - 6
    - 7
    - 8
  - column: both
  - layout_lines:
    - 427
    - 561
- source_explicit: Changing A→B versus A→C demand makes ordered input positions semantically unsuitable. Host DMA objects receive IDs through code analysis and select separate seed queues. The UHCI example labels qh, td and last_td separately.
- supports:
  - P4.S4
  - P4.S5
  - C2.S2
- editorial_use: The residual obstacle after address availability is maintaining useful learned input by request context, not simply a second coverage trick.
- limits: Operational object/type distinction, not full protocol inference. Node independence is the authors' design premise. Semantics-valid generation is a fuzzing-learning claim, not per-candidate correctness.

## E05

- section: §4 / §5 evaluation setup / §5.1.1
- locator:
  - pdf_pages:
    - 8
    - 9
    - 10
  - column: both
  - layout_lines:
    - 556
    - 650
- source_explicit: AFL2.52b; CodeQL analysis; QEMU5.1.0 and VirtualBox6.1.14; tests run24hours and repeated10times. Table2 covers16QEMU devices; line/function/branch coverage are distinct measures.
- supports:
  - P5.S1
  - P5.S2
  - P5.S3
- editorial_use: Implementation and device diversity support a concrete testing capability before broad comparative language.
- limits: The16-device count belongs to the broad QEMU evaluation, not every experiment; initial corpus logging is optional.

## E06

- section: §5.1.2 / Table2
- locator:
  - pdf_pages:
    - 9
    - 10
  - column: both
  - layout_lines:
    - 592
    - 650
- source_explicit: Average6110.23 executions/second for V-SHUTTLE versus7844.64 for dumb fuzzing in Table2. Authors attribute modest overhead to lightweight design without restarting/forking and host-side interaction.
- supports:
  - P3.S5
  - P5.S2
  - P5.S6
- editorial_use: Leaving throughput out of the Introduction's highlighted results is consistent with a task emphasis on usable input and deep exploration, not maximal raw speed. This reason is editorial inference.
- limits: Do not claim V-SHUTTLE is faster than dumb fuzzing on this evidence or infer semantics knowledge from execution rate.

## E07

- section: §5.2 / §5.2.1 / Figure7
- locator:
  - pdf_pages:
    - 9
    - 10
    - 11
  - column: both
  - layout_lines:
    - 611
    - 712
- source_explicit: Authors implement their own structure-aware comparator on UHCI/OHCI/EHCI. They acknowledge it is still in progress and not well crafted. EHCI example gives approximately64.6% versus71.4% coverage for that baseline and V-SHUTTLE-M.
- supports:
  - P3.S12
  - P3.S14
  - P5.S4
- editorial_use: Automatic addressing can reduce model-omission blind spots, so less manual work can have quality value as well as cost value.
- limits: Not a Nyx rerun and not strongest-possible-manual-model evidence. Authors give both hard-to-reach pointer-dependent paths and baseline incompleteness as explanations; no isolated causal attribution was established.

## E08

- section: §5.2.2 / Figure7
- locator:
  - pdf_page: 11
  - column: L
  - layout_lines:
    - 714
    - 741
- source_explicit: Final coverage of V-SHUTTLE-S and V-SHUTTLE-M is nearly identical in all tested USB cases; S reaches peaks sooner.
- supports:
  - P4.S5
  - P5.S5
- editorial_use: The separate result sentence pays off type awareness as convergence acceleration after the base mechanism enables exploration.
- limits: Do not upgrade to a large final-coverage increment from seedpools alone.

## E09

- section: §5.3 / Table3
- locator:
  - pdf_page: 11
  - column: both
  - layout_lines:
    - 709
    - 779
- source_explicit: Nyx and Hyper-Cube were unavailable when experiments were performed, so the paper compares their published numbers for overlapping eight devices. It argues for similar versions/configuration and equal24hour durations. Body says three of eight Nyx cases improve, tied to intensive DMA; others are small and offer little gain.
- supports:
  - P5.S6
- editorial_use: The task gain is conditional on complex nested input, while the Introduction compresses this as most cases. Keep named comparison and device-specific boundaries together.
- limits: Cross-paper comparison, not same-run replication. Do not silently recalculate a count of significant improvements from tiny positive differences; no significance test performed here. E1000 is below VDF's listed value; authors attribute that exception to code changes.

## E10

- section: Table3 / §5.3
- locator:
  - pdf_page: 11
  - column: L table, R explanation
  - layout_lines:
    - 729
    - 757
- source_explicit: Caption defines delta as percentage points. E1000:54.55→74.50, reported19.95. RTL8139:79.28→88.40, reported8.72. ES1370:91.38→91.91, reported0.54.
- independent_arithmetic: Displayed RTL8139 endpoints subtract to9.12, not8.72; ES1370 endpoints subtract to0.53, not0.54. E1000 subtracts to19.95. Both author-reported and arithmetic values remain distinguished.
- supports:
  - P5.S6
- editorial_use: Avoid attractive headline percentages that erase units or a source inconsistency.
- limits: This identifies internal inconsistency; it does not determine which published cell is wrong or supply an authorized paper correction.

## E11

- section: §5.4.1 / Table4
- locator:
  - pdf_page: 11
  - column: R
  - layout_lines:
    - 744
    - 787
- source_explicit: 35 new findings:26QEMU plus9VirtualBox;17CVE assignments;24fixed at writing. Bug classes include memory errors, loops, assertions, and other crashes.
- supports:
  - P5.S7
  - P5.S8
  - C3.S1
  - C3.S2
- editorial_use: Discovery scale, CVE assignment subset, responsible disclosure and fix status are distinct claims. This is the direct security-outcome layer after coverage.
- limits: Not35CVEs, not35fixed, not all proven exploitable, not all memory corruption;2021 paper status, not current status.

## E12

- section: §6 / Figure8
- locator:
  - pdf_pages:
    - 12
    - 13
  - column: p12R then p13L
  - layout_lines:
    - 822
    - 858
- source_explicit: Ant Group's customized QEMU; UHCI and EHCI deployment evaluation; early gains converge to similar long-term coverage. Professional integration example approximately1hour, including static analysis, agent integration, configuration, instrumentation and compilation.
- supports:
  - P5.S9
- editorial_use: A second implementation setting supports practical portability beyond public-device benchmarks.
- limits: Two device cases, not whole-enterprise universal validation; low manual porting cost is compatible with removing per-device protocol-template work, not zero human effort end-to-end.

## E13

- section: §8
- locator:
  - pdf_page: 13
  - column: L bottom then R top
  - layout_lines:
    - 856
    - 934
- source_explicit: Manual PoC reconstruction remains; closed-source hypervisors are unsupported in current design; persistent state may destabilize coverage guidance or lock the device.
- supports:
  - P4.S2
  - P5.S3
  - P5.S9
  - C2.S1
  - C2.S2
- editorial_use: Qualify the referent of automatic/scalable without erasing the genuine reduction of protocol modeling work.
- limits: The source proposes future routes but does not report these limitations as solved.

## E14

- section: C4 / §9
- locator:
  - pdf_pages:
    - 3
    - 13
  - column: p3L; p13R
  - layout_line_ranges:
    - 
      - 136
      - 138
    - 
      - 906
      - 907
- source_explicit: Fourth contribution and conclusion promise future open sourcing and give a GitHub address.
- supports:
  - C4.S1
- editorial_use: Tense conveys resource completion state even when the contribution title names a tool.
- limits: Repository address is not proof of release then or now; no current repository check was performed.

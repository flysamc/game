# H001 — pre-registration draft

Author: Claude · 25 October 2026 · **DRAFT PROPOSAL, revision 2 — not locked**  
Purpose: fix how H001 is examined *before* anyone tabulates labels against stroke counts, so that the analysis cannot be shaped after seeing the data.  
Lock condition: reviewed and agreed by Codex and Sam, then committed with the word **LOCKED** and a date. Until then it can change freely. After locking, any change needs a dated amendment stating whether it was made after seeing outcome data.

Revision 2 adopts Codex's six review points on PR #3 (2026-10-25). The changes are listed at the end. This note contains no outcome tabulation.

## 1. What is being examined

H001 (README): some tablets combine a relatively fixed label with a variable numerical field.

On a "strokes + cup" face (a stroke group followed by sign 328), the stroke count is the candidate variable field. This analysis asks one descriptive question: **is the stroke count statistically dependent on the label carried by the same object, and how strongly?**

The README's alternatives (an amount or denomination, a grade or category, a phonetic or logographic expression) are **not** decided by this analysis:
- Strong dependence fits a count bound to the label (a fixed grade, or part of a spelling) but does not prove it.
- Weak or absent dependence is **not** evidence that the count is a freely varying quantity. It may reflect small groups, mixed production or transcription noise.

Results are reported as dependence, effect size and uncertainty. Interpretations stay as listed alternatives.

## 2. Search set and units

- **Population:** objects in Mahadevan 1977 (M77) with at least one face whose complete text is a stroke sign immediately followed by 328 (the "SC face").
- **Stroke signs:** the M77 sign IDs consisting only of vertical strokes, listed from the M77 sign list with the image of each sign and checked by a second contributor. They are not inferred from shape names. Working expectation, to be verified: 86 = one, 87 = two, 89 = three, 95 = four.
- **Unit:** the physical object after IND-004 identity review. Impressions and repeated publications of one object count once. Objects judged to share a mould or production series form a **production group**. The primary analysis uses one object per production group, chosen by a rule fixed before tabulation (the lowest M77 text number).
- **Primary slice:** reviewed **Harappa tablets** only, with the SC face inscribed (not moulded) where the source records the technique. Other sites and object types are reported descriptively and are not pooled in the primary comparison.
- **Exchangeability:** inference requires units that can reasonably be treated as exchangeable under the null. If the reviewed slice cannot be split into such units (for example, because production groups cannot be resolved), the analysis **stops at description**: the catalogue and the per-label tables, with no p-value.

## 3. Label key

- **Primary key:** the unordered multiset of the object's complete **multi-sign, non-SC faces**, each kept in its internal reading order. M77 side order is a catalogue convention, so it does not order the key. Faces are never concatenated into a sentence.
- **Covariates, not part of the key:** single-sign faces (such as 137 "X" or 59 "fish") and non-script faces (such as dotted circles), recorded with the IND-003 v0.2 surface-content field.
- **Secondary key (sensitivity):** the multiset of all script-bearing non-SC faces, single-sign faces included.

## 4. Exclusions

1. Objects whose SC face has an unresolved stroke group (illegible, or photo outcome `illegible` or `contradicts`) are excluded from the primary comparison and kept in the catalogue.
2. Objects with no other script face have no label. They are counted descriptively only.
3. Labels with an illegible sign or an unresolved reading are excluded from the primary comparison. They are **not** turned into wildcard classes, because matching would be non-transitive and an illegible span may cover several signs. Where independent sources give specific alternative readings, those alternatives are enumerated and reported as a sensitivity.
4. Nothing else is excluded without a dated amendment.

## 5. Primary analysis

**Statistic:** dependence between label and stroke count among objects in label groups of two or more, measured as Cramér's *V* on the label × count table. Within-label agreement *W* (the share of same-label object pairs with equal counts) is reported alongside, because it is easier to read.

**Null and uncertainty:** permute counts across units within the primary slice, keeping label groups and the count distribution fixed; 10,000 permutations, seed 20261025. Report:
- observed *V* and *W*;
- the null mean and 2.5–97.5% range of each;
- a **two-sided** permutation p-value, since unusually low agreement is as informative as unusually high;
- a bootstrap 95% interval for *V* over units (2,000 resamples, same seed);
- per label group: the number of units and the distinct counts observed.

No verdict thresholds. The report states the estimate and its uncertainty, then lists which of the alternatives in §1 each pattern is compatible with.

## 6. Feasibility check (before tabulation; not called "power")

Two explicit generative models, run on the actual label-group sizes of the primary slice but with synthetic counts:

- **M-free:** each unit's count drawn independently from the slice's count distribution.
- **M-bound(ε):** each label group gets one count drawn from that distribution; each unit keeps it with probability 1 − ε, else takes a fresh draw. Run at ε = 0.1 and ε = 0.3, standing in for transcription error and genuine variation.

Report how often the §5 interval for *V* separates M-free from M-bound at each ε, over 1,000 simulations. If it separates in fewer than half the simulations at ε = 0.1, the slice is too small to say anything about dependence; report the catalogue and stop.

Choosing the label-group sizes means looking at which labels share a face. That is structural information, not outcome, and the feasibility code must not read the counts.

## 7. Sensitivity analyses (all reported, whatever they show)

- **S1.** All objects instead of one per production group.
- **S2.** Include stroke groups whose photograph outcome is `consistent` but not `confirms`.
- **S3.** Enumerated, independently sourced alternative readings for excluded labels (§4.3).
- **S4.** Secondary label key (§3).
- **S5.** Other sites and object types, each descriptively, not pooled.
- **S6. Exposure sensitivity.** Repeat §5 excluding the records contributors have already examined: the five Fig. 4 objects, M77 4580–4597 (seen by Claude), 4563 and 4094 (adjacent on M77 p. 360), and anything added to the exposure log during curation. This is a **less-examined subset, not a blinded confirmation**: contributors must see records while curating them.

## 8. Exposure log

| Date | Contributor | What was seen |
|---|---|---|
| 2026-10-25 | Claude | M77 records 4580–4597 (labels and stroke counts); full concordance p. 360 (index of sign 119), including 4563 and 4094; corpus aggregates: four-sign group in 11 texts, 5 with an SC face; 255 texts with a two-sign `[X] 328` line |
| 2026-10-25 | Codex | The five Fig. 4 objects; Claude's aggregates and the 5498 sequences (per Codex's PR #2 comment) |

Add a row whenever someone sees label and count pairs outside the frozen release.

## 9. What would change the plan

- Stroke signs turn out not to be a clean ordered series in the M77 sign list → revise §2 before curation.
- Production groups cannot be resolved for the Harappa slice → description only (§2).
- The feasibility check fails → report the catalogue and stop (§6).

## Changes in revision 2 (from Codex's review of revision 1)

1. Removed the A/B/C verdict thresholds and the 20% rule. Results are dependence, effect size and uncertainty; a non-significant result is not support for a free quantity.
2. The primary slice is now reviewed Harappa tablets, with one unit per production group and an explicit "stop at description" rule if exchangeable units are not available.
3. The label key is the unordered multiset of complete multi-sign non-SC faces. Single-sign faces and motifs are covariates, and the all-face key is a sensitivity.
4. No wildcard classes for illegible signs. Unresolved labels are excluded from the primary comparison; only independently sourced alternatives are enumerated.
5. "Power" is replaced by a feasibility check against two explicit generative models, and the test is two-sided.
6. The "unseen subset" is renamed an exposure sensitivity on a less-examined subset, and an exposure log is added.

## Remaining open question

One suggestion beyond Codex's points: if the Harappa slice is small, a **restricted permutation** that permutes counts only within object-type or stratum cells may keep more units than filtering does, while respecting exchangeability. Codex and Sam: worth adding as S7, or keep the filter-only design for simplicity?

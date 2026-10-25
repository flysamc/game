# H001 — pre-registration draft

Author: Claude · 25 October 2026 · **DRAFT PROPOSAL — not locked**  
Purpose: fix the test for H001 *before* anyone tabulates labels against stroke counts, so that the result cannot be shaped after seeing it.  
Lock condition: reviewed and agreed by Codex and Sam, then committed with the word **LOCKED** and a date. Until then it can change freely. After locking, any change needs a dated amendment that says whether the change was made after seeing outcome data.

This note proposes a design only. It contains no outcome tabulation.

## 1. What H001 claims, and what competes with it

H001 (README): some tablets combine a relatively fixed label with a variable numerical field.

On a "strokes + cup" face (a stroke group followed by sign 328), the stroke count is the candidate variable field. The README already lists alternatives. They make different, testable predictions about **how the stroke count relates to the label on the same object**:

| Model | What the strokes are | Prediction for objects carrying the *same* label |
|---|---|---|
| **A. Free quantity** (amount, denomination) | A value that changes with each issued object | Counts vary within a label about as much as across labels |
| **B. Bound to the label** (grade or category tied to the issuer, or part of a fixed spelling/name) | Part of what the label is | Counts agree within a label far more than chance |
| **C. Mixed** | Some labels take fixed counts, others free counts | Agreement above chance overall, with several labels showing two or more distinct counts |

None of these establishes a spoken number or the meaning of the cup. The test only asks whether the count behaves like an independent field or like part of the label.

## 2. Search set (declared before curation)

- **Population:** every object in Mahadevan 1977 (M77) with at least one face whose complete text is a stroke sign immediately followed by 328 (the "SC face"). This is the strokes-plus-cup family proposed in the IND-002 review.
- **Stroke signs:** the M77 sign IDs that consist only of vertical strokes. They must be listed from the M77 sign list with the image of each sign, and checked by a second contributor. They must not be inferred from shape names or from this note. Working expectation, to be verified: 86 = one, 87 = two, 89 = three, 95 = four.
- **Label:** the object's other script-bearing face or faces, as normalized M77 sequences in reading order. When there are several, the label is the tuple of those faces ordered by M77 side code. Non-script faces (e.g. dotted circles) are recorded but are not part of the label.
- **Unit of analysis: the physical object**, after identity adjudication in IND-004. Impressions and duplicate publications of one object count once. Objects judged to come from one mould or production series are reported as a group, and the main test is repeated with one object per group.
- **Source of transcriptions:** the IND-004 reviewed release. A third-party digitization may be used only as a blind cross-check (see the IND-003 review).

## 3. Exclusions (declared now)

1. Objects whose SC face has an illegible or doubtful stroke group: excluded from the main test, included in sensitivity S2.
2. Objects with no other script face: no label, so excluded from the dependence test, but counted in the descriptive summary.
3. Labels containing an illegible sign (`000`): excluded from the main test, included in sensitivity S3 with the illegible sign treated as a wildcard.
4. Nothing else is excluded without a dated amendment.

## 4. Primary test

**Statistic:** within-label agreement *W*. Across all labels carried by two or more independent objects, take every pair of objects sharing a label and compute the share of those pairs with the same stroke count.

**Null:** permute stroke counts across objects while keeping the set of labels and the overall count distribution fixed, 10,000 permutations. Seed fixed in code: 20261025.

**Report:** observed *W*; the null mean and its 2.5–97.5% range; one-sided p-value for *W* above the null; the number of label groups used and objects per group; and, for each label group, the distinct counts observed.

**Decision rules:**
- **B supported** if p < 0.01 *and* fewer than 20% of label groups show two or more distinct counts.
- **A supported** if p ≥ 0.05 *and* the confidence interval of *W* overlaps the null mean.
- **C** if p < 0.01 but at least 20% of label groups show two or more distinct counts.
- **Otherwise inconclusive.** Report it as such, and do not re-cut the data to reach a verdict.

**Power, before running:** simulate data from models A and B on the actual label-group sizes but with synthetic counts. If the design cannot separate A from B at least 80% of the time, report that the test is underpowered and stop, instead of running it and interpreting noise.

## 5. Sensitivity analyses (all reported, whatever they show)

- **S1.** One object per mould or production group.
- **S2.** Include doubtful stroke groups.
- **S3.** Include labels with an illegible sign as wildcards.
- **S4.** Harappa only; most tablets of this type come from Harappa, and a site effect could mimic B.
- **S5.** Collapse labels to their final two signs. If agreement collapses with the full label but not here, the count may be bound to the formula's end, not the whole label.

## 6. Exposure disclosure and held-out check

Contributors have already seen some outcome data:

- Claude listed M77 records **4580–4597** while checking crosswalks for IND-002 and saw their label and stroke-count pairs.
- Both assistants have seen the five Fig. 4 objects (5498, 4444, 4456, 4581, 4591). Mahadevan selected these because they share a label and show varying counts.

To keep the test honest, every analysis is run twice:

1. on the full search set;
2. on the **unseen subset**, excluding those 5 objects and 4580–4597.

The verdict rests on the unseen subset if the two disagree. Any further exposure, for example during curation, must be added here with a date before the test is run.

## 7. What would change the plan

- Stroke signs turn out not to be a clean ordered series in the M77 sign list → revise section 2 before curation.
- Identity adjudication merges most objects into a few production groups → S1 becomes the main test.
- The power check fails → stop at the descriptive catalogue.

## Open questions for Codex and Sam

1. Is "within-label agreement under permutation" the right primary statistic, or would you prefer mutual information or a likelihood ratio between explicit A and B models?
2. Are the 20% and p thresholds sensible, or should the decision be descriptive only, given the expected small group sizes?
3. Should the test wait for the full IND-004 release, or run first on a reviewed Harappa-only slice?

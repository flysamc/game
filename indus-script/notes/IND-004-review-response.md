# IND-004 — response to Claude's independent review

Recorded by Codex · 25 October 2026

**Subsequent status:** after the response recorded below, [Claude accepted all five record transcriptions and the content-classification representation](https://github.com/flysamc/game/pull/4#pullrequestreview-5645371653). The pilot is now [frozen](IND-004-pilot-release.md). The earlier limitations below remain part of its provenance; pending-review statements describe the earlier checkpoint.

Source: [Claude's actual PR #4 review, 5645307407](https://github.com/flysamc/game/pull/4#pullrequestreview-5645307407). This note records its scope and the corrections; it does not supply a new review on Claude's behalf.

## Acceptance recorded

Claude accepted the five M77-to-CISI crosswalks and five distinct physical objects within the pilot. He explicitly authorized recording source-addendum and crosswalk acceptance after applying corrections 1–3. The manifest and five identity records now cite that review. Record-level transcription reviews remain pending. Neither a corpus-wide duplicate audit nor production-group independence has been established.

He independently inspected the M77 source-number rule and H-322 museum mapping, CISI basic-data rows and plates. He **did not independently inspect Vats I pp. 348/351**, the item-to-find-number links. Those pages were inspected by Codex in the earlier curation, but are not silently labelled independently verified. Their Vats aliases keep the earlier proposed/source-reported status. Acceptance of the crosswalks also uses the within-series CISI FC corroboration described in his review; that pattern is not a general catalogue conversion rule.

H-322 has no reported excavation number here. The accepted identity decision relies on the catalogue/museum chains, not a claim that all five excavation numbers are known or unique. Claude also flagged that H-352 and H-354 share an excavation number; this reinforces the rule against using that number alone as an object key.

## Corrections applied

| Surface | Correction | Preserved evidence |
|---|---|---|
| `m77-5498-10`, H-322 A | Normalization photo outcome `confirms` → `consistent`; harrow-like group is faint | M77 `119 87 342 176` unchanged; H-322 B's two-stroke count remains confirmed |
| `m77-4591-30`, H-977 B | Normalization photo outcome `confirms` → `consistent`; cup end is broken | M77 `95 328` unchanged; intact four-stroke count remains confirmed |
| `m77-4591-10`, H-977 C | Added `content_disputed` and evidence-linked source assessments | M77 sign `59` retained; competing motif treatment explicitly labelled reviewer inference |

The fish inference follows CISI-II printed p. 343 / PDF p. 378, whose heading names fish among the plate's motifs. It is a plate-level heading, not an explicit declaration that H-977 C cannot be script. Codex re-inspected this plate and CISI-I p. 226 / PDF p. 262 before accepting the corrections. The 17 field-level photo checks now comprise **9 confirms and 8 consistent**. They are not independent sample observations.

Codex also inspected CISI-I printed p. 230 / PDF p. 266, including its heading and H-351 C. That heading does not establish an equivalent per-face classification disagreement for the X-shaped mark. The X's function remains an open question; no second source conflict is asserted without evidence.

The data model permits a reviewer to accept a faithful record of competing classifications. It does not force deletion of M77's transcription or a consensus about script status. A later analysis must specify whether such a face contributes to a label, a motif covariate, an alternative-classification sensitivity analysis or an exclusion. H001 revision 3 remains unlocked; no new family table or hypothesis test was run.

## Review leads and next action

Claude reported H-917 = M77 4472 as a useful future direction/alternative-face case, and H-354 (= H-356) = M77 5499 as a duplicate-publication lead. These new leads are reviewer-reported here, not added to the five-object dataset or independently verified by Codex in this response. The prior check of CISI-I's H-354/H-356 correction remains documented in the curation note.

Next: review the corrected record transcriptions and classification representation; check the remaining Vats source links when accessible; settle and lock the H001 analysis policy before broader family tabulation. This response does not mark IND-003, IND-004 or a frozen release complete.

Validation: Python 3.12.14, **35 tests pass**; draft validation exits 0; `--require-ready` exits 1 as intended. Historical v0.1 data and schema are unchanged. No scan or raw third-party corpus is committed.

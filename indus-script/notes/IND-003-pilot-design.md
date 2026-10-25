# IND-003 — pilot source, schema and duplicate rules

Author: Codex · 25 October 2026 · **IN REVIEW**

Sam asked to do the next step while IND-002 was still awaiting review. This stage therefore supplies a draft data contract and examples. It does not certify the source audit or freeze an analytical dataset. No review from Claude was present when work began.

## Choice and scope

Use the complete five-entry inventory in Mahadevan's **Figure 4**, linked to M77 catalogue IDs. Use the paper for H-351's published sign IDs and CISI-I printed p. 230 for its photograph. The [IND-002 audit](IND-002-source-audit.md) records locations and caveats; the [manifest](../sources/manifest.json) pins the downloaded reference files.

This choice gives us a finite curation task with visible relationships between faces. EBUDS excludes multiline material and is not the starting inventory for this task. No downloaded third-party transcription or assumed M77/ICIT crosswalk is introduced.

The source author selected these examples. They can exercise our transcription workflow and support a later descriptive comparison. They cannot estimate the prevalence of the pattern, serve as a random sample, or provide an independent confirmatory test of the hypothesis that selected them. A later test needs a separately declared search set and comparison records.

## Draft delivered

| Item | State |
|---|---|
| Catalogue records | `5498`, `4444`, `4456`, `4591`, `4581` |
| Faces recorded | 12 source-labelled faces; do not count them as 12 independent artifact observations |
| Sign-number sequences entered | H-351's three faces only, following the published transcription |
| Other nine faces | Diagram descriptions and source marks retained; `normalization: null` |
| Doubtful readings | Initial marks on `4581:20` and `4591:20` preserved |
| Physical-object identity decisions | Unresolved pending review; five catalogue records are not asserted to be five unique artifacts |
| Independent reviews | Pending |

These are inventory counts, not corpus results. The [draft JSON](../data/pilot-v0.1.json) includes one worked object case and four incomplete candidates. Unknown dates and materials remain null; the case's three faces remain separate. The [schema](../schemas/pilot-v0.1.schema.json) is deliberately restricted to this pilot, not a universal Indus corpus format.

## Data contract

| Field | Meaning and rule |
|---|---|
| `record_id`, `catalogue` | Stable source-record anchor, e.g. `m77-4581`; not an assertion of unique physical identity |
| `aliases` | Other identifiers with their evidence and verification status; an empty list means not established here |
| `metadata` | Site/type/material plus evidence; `dating` is null in v0.1 because this audit established no object-specific dating |
| `evidence` | Source-manifest ID, page/figure locator, representation type and dependence group |
| `source_description` | Our shape description, not a literal glyph transcription and not a translation; raw visual evidence remains in the linked source |
| `surface_id`, `labels` | Stable face anchor plus separate M77, paper and CISI labels. M77 `20` remains a string for side 2, line 0 |
| `observed_from` | Representation and displayed reading direction of the source diagram |
| `artifact_direction` | Direction on the artifact, separately sourced; null if not independently established here |
| `source_marks` | Visible editorial marks with 1-based positions in the diagram's reading order. `*` is not a sign token |
| `tall_strokes_next_to_cup` | Graphic stroke count for that specific field; no numerical quantity or spoken number is assigned |
| `normalization` | Null until transcribed; otherwise M77-1977 sign IDs as strings in reading order, token uncertainty, evidence and change log |
| `photo_evidence_refs` | Publications whose photographs were checked. Shared dependence groups identify reproductions of the same photographic evidence |
| `identity` | Reviewed physical-object grouping with evidence; unresolved entries get no invented group |
| `review` | Actual reviewer, date and reference after a decision; pending reviews have null reviewer/date/reference |

`null` is unknown or unfinished, not zero. An empty marks list means no mark was recorded in the inspected figure, not that the ancient sign has been proven unambiguous. `not_marked_doubtful` is a source annotation state, not our confidence score. Numerical arrays follow reading order; an importer must not reverse them merely because the source image is right-to-left.

The initial normalizations copy published values and preserve the figure's extra uncertainty. Any later merger, repair, change of order or sign reassignment needs a new change-log entry and source evidence. Meanings and pronunciations belong in separately registered hypotheses, not these observations. Damaged passages and additional catalogue systems require a documented schema extension before import.

## Duplicate-handling decisions

| Situation | Action |
|---|---|
| Same M77 catalogue record imported twice | Reject the duplicate record; combine its evidence instead |
| One object has several catalogue IDs | Retain source identifiers and resolve them to one physical-object group only after evidence review |
| Same photo reproduced in another paper | Retain both citations, share the photographic dependence group, and count no new object |
| Two objects carry identical text | Keep both objects if independent identity is established. Identical signs alone are not grounds to merge |
| Two records share a physical-object alias | Flag a collision until both are resolved to one reviewed group; do not silently count twice |
| Possible mould copies or related impressions | Record the relationship during curation. Distinct physical objects and related production are different groupings |
| Identity is unresolved | Keep the candidate for curation, exclude it from a frozen object-count analysis |

There is no automatic semantic or shape-based deduplication in this stage. Later reporting must distinguish catalogue records, physical objects, faces, and unique text types. Any future model split must also group related impressions or production families; v0.1 is too small and selected for model training or testing.

## Validation and release conditions

The validator checks the JSON Schema plus references across records, unique source IDs, surface anchors, catalogue bounds, uncertainty positions, photo/diagram distinctions, alias collisions and independent-review fields. It never proposes missing readings or edits the input. Validation confirms consistency of recorded claims; it cannot authenticate a review or decide whether a photograph was interpreted correctly.

A valid draft exits successfully even though it is unsuitable for analysis. `--require-ready` additionally requires a frozen release, accepted source review, reviewed identity groups, independently reviewed records, complete normalization and photographic checks. Doubtful readings may remain in a reviewed release; later comparisons must report sensitivity to including or excluding them. Selection bias remains even after all gates pass.

For an actual source-audit acceptance, the reviewer updates the source manifest's `independent_review` to `accepted` and records `reviewer` and `review_reference`, alongside the coordination log. Record and identity reviews use the structured fields in the pilot. No acceptance is set by this commit. The test suite's synthetic reviewer exists only inside an in-memory test fixture.

## Checks performed

- Python 3.12.14 with the pinned requirements: **18 regression tests passed**.
- The draft validates with exit 0; the analysis-readiness command returns the expected exit 1 and identifies unresolved evidence/reviews.
- Both command modes were also run from outside the repository directory.
- The five IDs, side/line codes, graphic stroke counts and asterisks were rechecked visually against the Figure 4 reproduction. This is a Codex transcription check, not an independent review.

## Next curation task: IND-004

1. Independently review the source audit and this design. Record disagreements and corrections without inventing an acknowledgement from another assistant.
2. Locate the original object crosswalks and photographs for `5498`, `4444`, `4456`, and `4591`. Check all source labels and whether the illustrated faces are complete.
3. Transcribe the remaining faces in M77 IDs with per-reading evidence. Do not infer their sign numbers simply by copying H-351's pattern.
4. Resolve duplicate-object claims and related impressions with documented evidence; then independently review all 12 faces and the normalization log.
5. Define any exclusions explicitly, retain the candidate inventory, and create a versioned analytical release. Run descriptive H001 comparisons only when the relevant review and curation gates are met.

The runnable commands and expected readiness result are in [data/README.md](../data/README.md). Software-format references: [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) and [jsonschema 4.25.1 validation API](https://python-jsonschema.readthedocs.io/en/v4.25.1/validate/).

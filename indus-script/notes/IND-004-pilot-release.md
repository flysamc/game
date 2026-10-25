# Pilot v0.2 release

Released by Codex · 25 October 2026 · **FROZEN, selected five-object pilot**

Sam instructed us to check GitHub and continue. [Claude's actual record-level review](https://github.com/flysamc/game/pull/4#pullrequestreview-5645371653), at curation head `646a3dcc80e07e86ae63e4b5c0b8c7bfbd69c452`, accepts all five records and all twelve faces. He explicitly authorized recording those decisions with his name and the review link. Codex recorded the five reviews and made the release decision. The [release manifest](../releases/pilot-v0.2.json) pins the relevant files by SHA-256.

The reviewer checked the normalized sequences against M77 printed p. 360 / PDF p. 371, every used sign against the sign list on pp. 32–35 / PDF pp. 43–46, the source-doubt marks, side labels, graphic counts and photographs. His acceptance includes H-977 C's faithfully recorded script/motif alternatives. It does not resolve that disagreement or give the figure a meaning. The earlier [source-addendum and pilot-identity review](https://github.com/flysamc/game/pull/4#pullrequestreview-5645307407) remains separately cited.

Only review metadata and release status changed in the dataset at this step. All twelve normalized sequences, two source-doubt marks, five graphic counts, photograph qualifications, and unknown artifact directions are unchanged. There are 17 field-level photo outcomes: 9 confirms and 8 consistent. Those checks are not independent samples.

## What this release permits

- Reproducible descriptions of these five selected objects and their twelve recorded faces, with the source qualifications retained.
- Testing curation software and planning the subsequent family search.
- Referencing a stable dataset in reviews. Later curation uses a new dataset version; corrections require an explicit versioned amendment.

This release does not authorize an H001 inferential result. The five examples were selected by the source author, do not form a representative sample, and have already been examined by contributors. Population inference remains disabled. H001 revision 3.1 is still unlocked, and family-wide identity, production-group and eligibility review remain to be done.

The Vats I pp. 348/351 item-to-find links were inspected by Codex but not independently by Claude. The accepted object crosswalks and his corroborating evidence are scoped in the earlier review; freezing does not upgrade those individual links. H-322's excavation number is still unreported. There are no inferred phonetic or semantic values, and no raw corpus or copyrighted scans are included.

## Verification

Python 3.12.14; all **35 tests pass**. Both validator modes exit **0**, report no blockers, and retain `content_disputed_surfaces: ["m77-4591-10"]`. `ready_for_descriptive_analysis` is true for this bounded pilot; `population_inference_allowed` remains false. Historical v0.1 data and schema are unchanged.

Next: define and commit family discovery rules before extracting candidates, settle the remaining sign-inventory question from the primary source, then curate candidates individually. Do not join broader label and count outcomes or run H001 before the analysis policy is locked.

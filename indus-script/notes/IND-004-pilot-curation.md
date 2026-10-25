# IND-004 — five-record photographic curation

Author: Codex · 25 October 2026 · **IN REVIEW**

The nine missing face sequences are now transcribed, giving **12 normalized faces across five catalogue records**. [Claude's review](https://github.com/flysamc/game/pull/4#pullrequestreview-5645307407) accepts the source addendum, crosswalks and five distinct physical objects within this pilot. Its three requested corrections are applied; record-level transcription review remains pending. This is not a decipherment or a frozen analytical corpus. [Pilot v0.2](../data/pilot-v0.2.json) preserves v0.1 as history. See the [review response](IND-004-review-response.md) for the precise acceptance scope and unverified Vats links.

## Object crosswalks

The chain uses published object identifiers, then compares photographs with the normalized diagram. Equal inscriptions alone do not establish identity. PDF page numbers below are 1-based and specific to the files hashed in the [manifest](../sources/manifest.json).

| M77 record | Accepted CISI match | Identifier chain | Photograph |
|---|---|---|---|
| 5498 | **CISI-I H-322** | M77 p. 824 → ASI **49.255.200** → CISI-I p. 372, H-322 row (also ASI 63.11.192; FC 4177; excavation number unreported) | CISI-I p. 226, PDF 262, A/B |
| 4444 | **CISI-I H-303** | M77 p. 821 → Vats item **444** → Vats I p. 348, find **11291** → CISI-I p. 371 (FC 3444; ASI 63.11.102) | CISI-I p. 225, PDF 261, A/B |
| 4456 | **CISI-II H-916** | M77 p. 821 → Vats item **456** → Vats I p. 348, find **12516** → CISI-II p. 444 (FC 3456; HM 320) | CISI-II p. 339, PDF 374, A/A bis/B |
| 4591 | **CISI-II H-977** | M77 p. 821 → Vats item **591** → Vats I p. 351, find **8480** → CISI-II p. 444 (FC 3591; HM 421) | CISI-II p. 343, PDF 378, A/B/B bis/C/C bis |
| 4581 | **CISI-I H-351**, prior author-reported match | Paper §3; corroborated through Vats item **581**, find **2429**, CISI-I p. 372 (FC 3581; ASI 63.11.75) | CISI-I p. 230, PDF 266, A/B/C |

Two catalogue traps were checked directly in the page images:

- CISI's second basic-data column is **FC (Finnish Concordance)**, not M77. The key on CISI-I pp. 365–366 explicitly says concordance numbers can differ. Do not apply a blanket ±1000 conversion.
- On CISI-I p. 372, **ASI 49.255.200 is the continuation of H-322's row**, above H-323. A web-extracted table attached it to H-323 incorrectly. H-322's photographs match the pilot; H-323's do not. The image, not OCR row alignment, controls this crosswalk.

Claude accepted these as five distinct physical objects using the registered catalogue and museum identifiers. The data now contain five pilot-scoped physical-object groups. This is not a corpus-wide duplicate or production-family audit. H-322's excavation number is unreported; do not claim five distinct excavation numbers or use excavation number alone as an object key. Claude did not independently inspect Vats I pp. 348/351: those item-to-find links remain Codex-checked only. Vats aliases retain their earlier source-reported/proposed status; the accepted CISI crosswalks are recorded separately.

## Face mappings and readings

Tokens are **M77 sign identifiers in the source's reading order**. `*119` preserves the printed doubtful-reading mark. Shape names are labels, not translations. The original M77 p. 360 (PDF 371) agrees with the paper's reproduced Figure 4; these are dependent presentations of the same normalization.

| M77 | Main face | Strokes-plus-cup face | Additional face |
|---|---|---|---|
| 5498 / H-322 | `10` = A: `119 87 342 176` | `20` = B: `87 328` (2 strokes) | None reported in this pilot |
| 4444 / H-303 | `10` = A: `119 87 342 176` | `20` = B: `89 328` (3 strokes) | None reported in this pilot |
| 4456 / H-916 | `10` = A: `119 87 342 176` | `20` = B: `89 328` (3 strokes) | None reported in this pilot |
| 4591 / H-977 | `20` = A: `*119 87 342 176` | `30` = B: `95 328` (4 strokes) | `10` = C: `59`, fish-shaped |
| 4581 / H-351 | `20` = A: `*119 87 342 176` | `30` = B: `95 328` (4 strokes) | `10` = C: `137`, X-shaped |

The sign list was checked in M77 printed pp. 32–35 / PDF pp. 43–46. A stroke **group** such as `95` is one sign identifier; its four visible strokes are a separate graphic count. No value, quantity, word or sound is assigned to it. Artifact writing direction remains unadjudicated; the normalized display's direction is recorded separately.

## What the photographs support

The data store **17 field-specific checks on 12 faces**, performed by Codex and revised following Claude's review: 9 `confirms`, 8 `consistent`. These counts are a curation inventory, not independent observations or a statistical test. A check's scope is its named field, not the entire object identification or the mark's linguistic function.

| Object | Main normalization | Cup/count | Additional face |
|---|---|---|---|
| H-322 | Consistent; harrow-like final group is faint | Confirms cup and two tall strokes | — |
| H-303 | Confirms four-group reading | Confirms cup and three tall strokes | — |
| H-916 | Consistent; first group's oblique form differs from standardized glyph | Confirms cup and three tall strokes | — |
| H-977 | Consistent; worn first group remains doubtful | Normalization consistent: cup end broken; four-stroke count confirmed | Figure consistent with M77 59; script/motif classification disputed |
| H-351 | Consistent; first group remains doubtful | Consistent with four; edge/slant limits unqualified confirmation | X-shaped sign confirmed |

H-351's qualification incorporates the earlier [Claude source review](IND-002-review-claude.md). The later PR #4 review accepts the crosswalks and agrees with the other 14 photographic outcomes, while leaving record-level transcription sign-off for a subsequent review. “Consistent” must not be silently changed to “confirmed.” Repeated photographs (`bis`) and reproduced plates do not create new physical objects.

For **H-977 C**, M77 encodes the figure as sign 59, while CISI-II p. 343's plate-level heading mentions fish iconography. The latter is evidence for a competing motif assessment, inferred by the reviewers; it is not an explicit per-face editorial ruling. `content_disputed: true` and two evidence-linked `content_assessments` preserve that difference. The M77 token is unchanged. Codex also inspected CISI-I p. 230: its heading does not establish an equivalent classification disagreement for H-351 C's X. That remains an open question, not a second asserted source conflict.

## Changes requested by Claude's pilot review

- **Photo outcomes:** each check names its field, outcome (`confirms`, `consistent`, `illegible`, `contradicts`), checker, date, evidence and explanation. A list of consulted images alone cannot pass the v0.2 readiness gate. Illegible/contradictory checks block freezing until adjudicated. Qualified consistency can support a reviewed release; it remains visibly qualified.
- **Surface content:** `script`, `non_script_motif`, `blank`, `not_reported`. Here `script` means classified as an inscription in the working source, not proof that the system encodes a particular language. A photographed motif can have a CISI anchor without an invented M77 code or sign sequence. Unreported content is not blankness. The 12 working classifications retain the M77 encodings; H-977 C also carries the competing motif assessment. A false dispute flag means no recorded conflict, not proven linguistic status. Review can accept a faithful record of ambiguity without erasing it; any later analysis must declare how alternative classifications affect eligibility or label construction.
- **Unknown spans:** M77 p. 31 says its illegibility marker can cover one or more signs. The third-party `000` convention therefore cannot automatically become a one-sign wildcard, a real sign, or zero strokes. v0.2 deliberately rejects sign zero. A later importer must preserve an explicit illegible-span event with unknown length before expanding the family; do not silently drop or guess it.
- **Third-party evidence:** the schema can label digitizations separately. They cannot be sole normalization evidence. The source addendum now records Claude's separate acceptance and its scope; it does not inherit or expand IND-002's acceptance.
- **Family scope:** the five examples remain a workflow pilot. The broader strokes-plus-cup family is accepted as a subsequent search target; [H001 proposal #3](https://github.com/flysamc/game/pull/3) is at revision 3 and remains unlocked. No family-wide label/count table or hypothesis test was run.

The new content handling is motivated by actual nearby material: CISI-I H-352–354 have dotted-circle faces. They are not added to this five-record pilot. CISI-I p. 375 also corrects H-356 A/B/C to **H-354 A/B/C bis**: a concrete duplicate-publication trap for later curation, not a sixth pilot object.

## Public digitization cross-check

Pinned [joyboseroy/indus_decipher](https://github.com/joyboseroy/indus_decipher/tree/cd600349f6d3193a241c3eb87ff80a2a65377efc) at `cd600349f6d3193a241c3eb87ff80a2a65377efc`. After writing the primary-source transcription checkpoint, compared only the 12 pilot rows in `data/m77_indusscript_real_corpus.csv`: all base-sign sequences agree. The two starred main faces each have `mean_uncertainty=25.0`; exact doubtful positions still come from the primary diagram.

The converter **claims** an IndusScript.in export through a logged-in browser. We did not audit that extraction or obtain its raw input. Its CSV drops exact star positions, defaults direction to `R-L` meaning as-stored, and sets `damaged=False` by default. None of those defaults is independent archaeological evidence. The repository has an MIT software license; underlying portal-data reuse rights remain unestablished. No raw corpus, code from that project or reference scans are committed here. Full-corpus counts in Claude's earlier note remain reviewer-reported and were not replicated in this pass.

## Validation and handoff

Run commands in [data/README.md](../data/README.md). Python 3.12.14: **35 tests pass** (18 legacy contract tests and 17 v0.2 cases); draft validation exits 0; `--require-ready` exits 1. The latter is expected: independent record-level transcription review, review of the newly encoded classification alternatives, and a frozen release are still absent. Source-addendum and pilot identity acceptance are now recorded with the actual review link.

For the next reviewer:

1. If checking the remaining source-link gap, inspect Vats I pp. 348/351 (PDF pp. 372/375). The accepted crosswalks and pilot identity decisions need not be repeated without new evidence.
2. Review all 12 normalized sequences, both asterisks, the sign variants, corrected photographic outcomes and the fish's explicitly qualified content assessments. Record each actual transcription decision; current record reviews remain pending.
3. Run the validator/tests and scrutinize motif/unknown-span handling. Record actual acceptance or corrections; do not accept an analytical release just because structural validation passes. A future family audit still needs duplicate-publication and production-group decisions beyond these five objects.
4. Resolve the H001 design comments before further family tabulation. The exposed five are not a blind test set. Contributors have also seen adjacent plates, the M77 p. 360 context, Claude's aggregate report and the 12-row cross-check; record that exposure in any subsequent evaluation plan.

This curation supports a bounded observation: the published selected examples combine the same normalized main group with two, three or four tall strokes beside a cup-like sign. Whether this reflects quantities, categories, titles, workshops or another function remains unresolved. These selected examples cannot establish a corpus frequency, causal relation or word meaning.

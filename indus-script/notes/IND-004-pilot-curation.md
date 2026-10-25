# IND-004 — five-record photographic curation

Author: Codex · 25 October 2026 · **IN REVIEW**

The nine missing face sequences are now transcribed, giving **12 normalized faces across five catalogue records**. All four remaining records have proposed crosswalks to CISI photographs. These are primary-source curation results awaiting independent review, not a decipherment or a frozen analytical corpus. [Pilot v0.2](../data/pilot-v0.2.json) preserves v0.1 as history.

## Object crosswalks

The chain uses published object identifiers, then compares photographs with the normalized diagram. Equal inscriptions alone do not establish identity. PDF page numbers below are 1-based and specific to the files hashed in the [manifest](../sources/manifest.json).

| M77 record | Proposed CISI match | Identifier chain | Photograph |
|---|---|---|---|
| 5498 | **CISI-I H-322** | M77 p. 824 → ASI **49.255.200** → CISI-I p. 372, H-322 row (also ASI 63.11.192; FC 4177; excavation number unreported) | CISI-I p. 226, PDF 262, A/B |
| 4444 | **CISI-I H-303** | M77 p. 821 → Vats item **444** → Vats I p. 348, find **11291** → CISI-I p. 371 (FC 3444; ASI 63.11.102) | CISI-I p. 225, PDF 261, A/B |
| 4456 | **CISI-II H-916** | M77 p. 821 → Vats item **456** → Vats I p. 348, find **12516** → CISI-II p. 444 (FC 3456; HM 320) | CISI-II p. 339, PDF 374, A/A bis/B |
| 4591 | **CISI-II H-977** | M77 p. 821 → Vats item **591** → Vats I p. 351, find **8480** → CISI-II p. 444 (FC 3591; HM 421) | CISI-II p. 343, PDF 378, A/B/B bis/C/C bis |
| 4581 | **CISI-I H-351**, prior author-reported match | Paper §3; corroborated through Vats item **581**, find **2429**, CISI-I p. 372 (FC 3581; ASI 63.11.75) | CISI-I p. 230, PDF 266, A/B/C |

Two catalogue traps were checked directly in the page images:

- CISI's second basic-data column is **FC (Finnish Concordance)**, not M77. The key on CISI-I pp. 365–366 explicitly says concordance numbers can differ. Do not apply a blanket ±1000 conversion.
- On CISI-I p. 372, **ASI 49.255.200 is the continuation of H-322's row**, above H-323. A web-extracted table attached it to H-323 incorrectly. H-322's photographs match the pilot; H-323's do not. The image, not OCR row alignment, controls this crosswalk.

Each record has a different proposed catalogue/museum identifier. This is useful evidence against accidentally merging the five, but it is not a completed corpus-wide duplicate or production-family audit. Physical-object groups remain null pending review; proposed aliases are labelled accordingly.

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

The data store **17 field-specific checks on 12 faces**, all performed by Codex: 11 `confirms`, 6 `consistent`. These counts are a curation inventory, not independent observations or a statistical test. A check's scope is its named field, not the entire object identification.

| Object | Main normalization | Cup/count | Additional face |
|---|---|---|---|
| H-322 | Confirms four-group reading | Confirms cup and two tall strokes | — |
| H-303 | Confirms four-group reading | Confirms cup and three tall strokes | — |
| H-916 | Consistent; first group's oblique form differs from standardized glyph | Confirms cup and three tall strokes | — |
| H-977 | Consistent; worn first group remains doubtful | Confirms cup and four tall strokes | Fish-shaped sign consistent; wear/angle limit confidence |
| H-351 | Consistent; first group remains doubtful | Consistent with four; edge/slant limits unqualified confirmation | X-shaped sign confirmed |

H-351's qualification incorporates the actual [Claude source review](IND-002-review-claude.md). That review does not constitute approval of the new v0.2 records or crosswalks. No new contradictions were found in these selected views. “Consistent” must not be silently changed to “confirmed.” Repeated photographs (`bis`) and reproduced plates do not create new physical objects.

## Changes requested by Claude's pilot review

- **Photo outcomes:** each check names its field, outcome (`confirms`, `consistent`, `illegible`, `contradicts`), checker, date, evidence and explanation. A list of consulted images alone cannot pass the v0.2 readiness gate. Illegible/contradictory checks block freezing until adjudicated. Qualified consistency can support a reviewed release; it remains visibly qualified.
- **Surface content:** `script`, `non_script_motif`, `blank`, `not_reported`. Here `script` means classified as an inscription in the working source, not proof that the system encodes a particular language. A photographed motif can have a CISI anchor without an invented M77 code or sign sequence. Unreported content is not blankness. All 12 actual pilot faces are classed as script; no invented motif face has been added.
- **Unknown spans:** M77 p. 31 says its illegibility marker can cover one or more signs. The third-party `000` convention therefore cannot automatically become a one-sign wildcard, a real sign, or zero strokes. v0.2 deliberately rejects sign zero. A later importer must preserve an explicit illegible-span event with unknown length before expanding the family; do not silently drop or guess it.
- **Third-party evidence:** the schema can label digitizations separately. They cannot be sole normalization evidence. The source additions have their own pending review and do not inherit IND-002's acceptance.
- **Family scope:** the five examples remain a workflow pilot. The broader strokes-plus-cup family is accepted as a subsequent search target; [H001 proposal #3](https://github.com/flysamc/game/pull/3) remains unlocked with methodological revisions requested. No family-wide label/count table or hypothesis test was run.

The new content handling is motivated by actual nearby material: CISI-I H-352–354 have dotted-circle faces. They are not added to this five-record pilot. CISI-I p. 375 also corrects H-356 A/B/C to **H-354 A/B/C bis**: a concrete duplicate-publication trap for later curation, not a sixth pilot object.

## Public digitization cross-check

Pinned [joyboseroy/indus_decipher](https://github.com/joyboseroy/indus_decipher/tree/cd600349f6d3193a241c3eb87ff80a2a65377efc) at `cd600349f6d3193a241c3eb87ff80a2a65377efc`. After writing the primary-source transcription checkpoint, compared only the 12 pilot rows in `data/m77_indusscript_real_corpus.csv`: all base-sign sequences agree. The two starred main faces each have `mean_uncertainty=25.0`; exact doubtful positions still come from the primary diagram.

The converter **claims** an IndusScript.in export through a logged-in browser. We did not audit that extraction or obtain its raw input. Its CSV drops exact star positions, defaults direction to `R-L` meaning as-stored, and sets `damaged=False` by default. None of those defaults is independent archaeological evidence. The repository has an MIT software license; underlying portal-data reuse rights remain unestablished. No raw corpus, code from that project or reference scans are committed here. Full-corpus counts in Claude's earlier note remain reviewer-reported and were not replicated in this pass.

## Validation and handoff

Run commands in [data/README.md](../data/README.md). Python 3.12.14: **31 tests pass** (18 legacy contract tests and 13 new cases); draft validation exits 0; `--require-ready` exits 1. The latter is expected: independent v0.2 transcription/crosswalk review, identity adjudication, source-addendum acceptance and a frozen release are still absent.

For the next reviewer:

1. Follow each identifier chain, especially H-322's two-line museum entry; check the H-916 and H-977 Pakistan plates against the correct faces.
2. Review all 12 normalized sequences, both asterisks, the sign variants and qualified photographic outcomes. Check object duplicates before assigning physical-object groups.
3. Run the validator/tests and scrutinize motif/unknown-span handling. Record actual acceptance or corrections; do not accept an analytical release just because structural validation passes.
4. Resolve the H001 design comments before further family tabulation. The exposed five are not a blind test set. Contributors have also seen adjacent plates, the M77 p. 360 context, Claude's aggregate report and the 12-row cross-check; record that exposure in any subsequent evaluation plan.

This curation supports a bounded observation: the published selected examples combine the same normalized main group with two, three or four tall strokes beside a cup-like sign. Whether this reflects quantities, categories, titles, workshops or another function remains unresolved. These selected examples cannot establish a corpus frequency, causal relation or word meaning.

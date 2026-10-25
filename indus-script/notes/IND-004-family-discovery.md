# IND-004 — first family discovery queue

Author: Codex · 25 October 2026 · **IN REVIEW; candidates are not curated objects**

The pinned export yields **241 candidate M77 catalogue anchors**, comprising the five frozen pilot entries and **236 additional entries**. They come from 242 matching source rows: one catalogue anchor has more than one matching row. These are discovery references, not 241 verified physical objects, not 241 independent observations, and not a representative analytical dataset. No other-face label/count table or H001 test was made.

The [protocol](IND-004-family-discovery-protocol.md) was committed at [`b0d5e27`](https://github.com/flysamc/game/commit/b0d5e27bbb92a52e13f145a6e4ee263b2a0a454d) **before extraction**. It uses the unchanged tall-stroke inventory 86/87/89/95/96 followed by 328. [Primary inspection](H001-stroke-inventory-check.md) shows 108 and 110 are short forms with six and seven strokes respectively; their exclusion and that correction await independent review.

## Source and accounting

Input: the registered public CSV at `joyboseroy/indus_decipher`, commit `cd600349f6d3193a241c3eb87ff80a2a65377efc`. Git blob `c61d3777ad19807efd7835da6296fa6d10833845` was verified before parsing. SHA-256: `c87b82a6d0ce2d02e70c96711f4ae6fd2a01f8b0dbb9795e564e17b12e2ce1d3`; 266,368 bytes. The [separate source/query manifest](../sources/family-discovery-v0.1.json) leaves the frozen pilot manifest unchanged.

| Export/discovery unit | Count | Meaning |
|---|---:|---|
| Exported nonempty source rows | 3,573 | Catalogue text number plus side/line pair |
| Distinct catalogue anchors in export | 2,906 | Not deduplicated archaeological objects |
| Rows containing 328 | 313 | All accounted for below |
| Matching candidate rows | 242 | Exact tall-stroke/cup row, line code 0, no other exported row on that side |
| Manual-review rows | 11 | Contain zero/unknown-span tokens; no wildcard interpretation |
| Other excluded cup rows | 60 | 52 not exact two-token matches; 8 with undeclared prefixes |
| Candidate catalogue anchors | 241 | All remain discovery candidates in this output |
| Already in the frozen pilot | 5 | Existing independent review remains in the pilot dataset |
| Additional candidate anchors | 236 | Require primary-source curation and independent review |

The accounting is exact: 242 + 11 + 60 = 313. No duplicate normalized row IDs, malformed source rows or sign codes outside the pilot's M77 inventory were encountered. There are **15 candidate rows with nonzero source uncertainty**; they stay flagged, and exact doubtful positions must come from primary sources. No reversed or multiline exact matches arose in this export run; the implementation still tests those failure cases with synthetic fixtures.

These are inventory checks on this particular digitization. Matching published corpus totals would not establish the correctness, completeness or reuse rights of the underlying portal export. The source converter omits empty records and supplies unknown/default site, type, motif, direction and damage values. Missing non-script faces and metadata still require primary inspection.

## Files and reproduction

- [Candidate queue and all-cup-row audit](../data/family-candidates-v0.1.json): identifiers, uncertainty flags, reasons, input hashes and extractor hash. It contains no raw sign sequences, candidate stroke counts or other-face labels.
- [Extractor](../scripts/discover_family.py): standard-library Python; rejects an input other than the pinned blob. It does not run external repository code.
- [Synthetic checks](../tests/test_discover_family.py): line versus face, same-side conflicts, uncertainty, unknown spans, excluded variants, reversed pairs, duplicate IDs, source pinning and output limits.

From the repository root, with a separately obtained local copy of the pinned source file:

```sh
python3 indus-script/scripts/discover_family.py \
  --input /path/to/m77_indusscript_real_corpus.csv \
  --output /tmp/family-candidates-v0.1.json \
  --protocol-commit b0d5e27bbb92a52e13f145a6e4ee263b2a0a454d
python3 -m unittest discover -s indus-script/tests -p 'test_discover_family.py' -v
```

Use the pilot's documented dependencies for the full test suite. **44 tests pass**: 35 existing pilot checks and 9 discovery checks. Every SHA-256 in the frozen pilot release manifest still matches. The primary images and raw CSV remain outside the repository.

## Next curation and review

Follow the committed ascending-ID rule. The first ten additional catalogue anchors are **4314, 4324, 4342, 4345, 4346, 4348, 4350, 4352, 4353, 4354**. Their identifiers are leads only. Do not infer their site or tablet status merely from a number pattern; confirm metadata and every face from the primary catalogues.

Manual unknown-span row references: `1165.0`, `2188.0`, `4347.20`, `4494.20`, `4546.20`, `4639.20`, `5281.20`, `5428.20`, `5456.20`, `7238.0`, `7280.0`. These are separate from accepted exact matches; an unknown span can represent one or more signs. Any restoration must be sourced and versioned.

Reviewer checklist:

1. Check the input identity and the source row/face distinction against M77 p. 31 and the pinned converter description.
2. Confirm the tall/short inventory decision, especially 108 and 110, from M77 p. 32.
3. Re-run the extractor and compare the output; inspect the complete cup-row audit and synthetic failure tests.
4. Accept or correct the discovery method explicitly. Do not treat method acceptance as transcription review of 236 new objects.

After this method review, curate the first new entry, M77 4314, with primary identity, complete face coverage, photographs and uncertainties. H001 revision 3.1 remains unlocked; analytic eligibility, physical duplicates, production groups, site/type filters and the eventual analysis policy remain separate decisions.

Exposure update: the extraction program read all exported token rows for matching and integrity checks. Codex inspected the resulting identifiers, audit reasons, uncertainty flags and file-accounting totals, not a joined table of candidate counts and other-face labels. This is disclosed filtering, not blind confirmation.

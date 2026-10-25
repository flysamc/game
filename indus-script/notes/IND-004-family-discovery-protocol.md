# IND-004 — family discovery protocol v0.1

Author: Codex · 25 October 2026 · **DISCOVERY RULES; H001 NOT LOCKED**

This protocol is committed before running a broader candidate extraction. It defines an auditable discovery queue, not a reviewed corpus, a label/count table or a statistical test. The five-object pilot is already frozen. Prior exposure includes that pilot, adjacent primary-source plates, M77 p. 360, the earlier reported aggregates, and the third-party converter's published claims. This is not blind discovery or preregistration of the H001 analysis.

## Fixed source and query

Use only the registered third-party file at `joyboseroy/indus_decipher`, commit `cd600349f6d3193a241c3eb87ff80a2a65377efc`, path `data/m77_indusscript_real_corpus.csv`, Git blob `c61d3777ad19807efd7835da6296fa6d10833845`. Verify its blob identity and record its SHA-256 before parsing. The source author claims a portal export; neither its extraction nor corpus completeness is established here. The raw CSV remains outside the repository.

The inspected converter defines each row as a **catalogue text number plus side/line code**, not a complete physical object or necessarily a complete face. `site`, `object_type`, `motif`, direction and damage defaults cannot supply archaeological evidence. Its uncertainty percentage loses the positions of asterisks. The CSV header and converter were read before this protocol; no new candidate list was extracted before committing it.

1. Match the complete as-stored row to exactly two tokens: one of **86, 87, 89, 95, 96**, then **328**. These represent the tall single-row series in M77 p. 32. Their visible stroke counts are 1–5; this does not assign numerical or linguistic meanings. Do not reverse a sequence or merge signs.
2. M77 p. 31 defines final line-code digit **0** as the only text line on that side. Promote an exact row match to a **discovery candidate** only if its line-code digit is 0 and no other exported row belongs to that same catalogue number/side. Other line codes or conflicting side rows enter the manual-review queue. An exported two-sign line must not silently become a complete two-sign face.
3. A doubtful exact match remains a discovery candidate, flagged for primary uncertainty checking. No analytical inclusion follows from discovery. A zero/unknown-span token is never a wildcard or a stroke count; rows containing 328 and such a token enter manual review.
4. Maintain an audit of **every other exported row containing 328**. Exact reversed pairs, multiline/ambiguous faces and unknown spans enter manual review. Other rows receive an explicit exclusion reason: undeclared stroke variant, non-stroke prefix, or not an exact two-token face candidate. This is discovery exclusion only; later evidence can justify a versioned query amendment.
5. The short, stacked and combined signs **88, 90–94, 97–110** are outside the tall-series query. The [primary-source inventory check](H001-stroke-inventory-check.md) resolves 108 as six short strokes and 110 as seven short strokes. No inventory extension is made.

## Output contract

Output catalogue anchors and source side/line identifiers, uncertainty flags, decision reasons and provenance. Group candidate rows by M77 catalogue number for the review queue; **do not call that grouping physical-object deduplication**. Keep one candidate per catalogue anchor with all qualifying row references. Flag the five existing pilot anchors separately.

Do not emit raw sign sequences, the observed stroke count per candidate, other-face labels, site/type guesses, semantic readings or direction claims. Do not join candidate stroke counts to label faces, rank cases by label/count outcomes, calculate an H001 statistic or run feasibility simulations at this step. Integrity counts describe the export and discovery process, not the archaeological population.

The implementation must reject a different input blob, malformed row IDs/tokens, duplicate normalized row IDs, or invalid uncertainty values rather than silently losing rows. Unexpected source sign codes are logged for primary inspection; they are not treated as valid M77 tokens by assumption. Synthetic fixtures must exercise line-versus-face distinctions, uncertainty and unknown spans, reversed pairs, excluded variants and duplicate IDs.

## Subsequent curation and review

Process new catalogue anchors in ascending M77 number; do not select objects because their label/count relationship looks interesting. Site and object type must come from primary source metadata. All candidates remain unreviewed until their full object, face coverage, identifiers, photographs and uncertainty are checked. A later Harappa-tablet analysis filter is distinct from discovery across the export.

The reviewed pilot remains unchanged. New objects require a separate dataset/version and independent review. Missing non-script faces and rows omitted by the converter remain possible; the queue is not a complete inventory of archaeological objects or marks. Physical duplicates, production groups, inscription technique, dating and analytic eligibility remain unresolved.

Claude should review the source-unit parsing, inventory decision and queue audit before candidate curation is treated as complete. H001 revision 3.1 is still unlocked. The analysis plan must be agreed before expanded label/count tabulation; discovery does not lock it or substitute for that agreement.

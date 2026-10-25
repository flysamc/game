# Indus script research

Started: 25 October 2026  
Status: IND-002 reviewed and merged; IND-004 five-record curation and v0.2 review corrections prepared. Independent v0.2 review remains pending. No decipherment or corpus statistics yet.

This folder is the shared research workspace for Sam, Codex, Claude, and other contributors. The goal is to investigate how much structure, function, meaning, and eventually pronunciation can be recovered from Indus inscriptions through reproducible tests.

Start here, then read [COORDINATION.md](COORDINATION.md) for the current task and handoff. Work through the stages in order. Keep this research within `indus-script/`; the repository also contains unrelated game and visual projects.

## What has actually been done

- An initial literature scan covered comparative/rebus readings, statistical models, cryptanalysis, sign variants, archaeological interpretations, and recent neural approaches.
- Mahadevan's published normalized transcription of Harappa tablet **H-351** was read and selected as a first case.
- A provisional hypothesis and an ordered research plan were defined.
- [IND-002 source audit](notes/IND-002-source-audit.md): checked H-351 against the CISI photograph and separate illustration supplement; identified five candidate catalogue entries, source-specific surface labels, and two doubtful sign readings. [Claude accepted the source audit with additions](notes/IND-002-review-claude.md); PR #1 is merged.
- Added a [source manifest](sources/manifest.json) with retrieval details and hashes for downloaded reference PDFs.
- [IND-003 pilot design](notes/IND-003-pilot-design.md) defines source selection, per-face records and duplicate-handling rules. [IND-004 curation](notes/IND-004-pilot-curation.md) completes all twelve normalized faces and proposes photographic crosswalks to H-322, H-303, H-916, H-977 and H-351. The [v0.2 inventory](data/README.md) retains qualified readings and both doubtful signs.
- Updated the schema and validator for field-specific photo outcomes and non-script faces. Thirty-one tests pass; the draft intentionally fails the analysis-readiness gate pending independent review and identity adjudication. The broader [H001 proposal](https://github.com/flysamc/game/pull/3) remains unlocked.

This was an initial literature review, not an exhaustive systematic review. **Published photographs for all five pilot records have now been compared with their source normalizations. A small machine-readable draft inventory exists, but no independently validated analytical corpus is available; no corpus statistics, sign pronunciation or translation have been established.** Numbers and results below belong to the cited studies unless explicitly marked as our own future results.

## Starting position

The literature reviewed through 25 October 2026 still treats the Indus script as undeciphered. There is no generally accepted dictionary or full decipherment. Short inscriptions, uncertainty about the underlying language(s), and the absence of an accepted bilingual inscription limit what can be inferred. Recent computational work continues to investigate structure rather than established meanings. [Yadav et al. 2010][yadav]; [Tiwari 2026][tiwari].

We will keep three levels separate:

| Level | Example | Meaning of the claim |
|---|---|---|
| Shape description | “Fish,” “cup,” “jar,” or “harrow” | A convenient visual label, not a translation |
| Structural observation | A sign tends to end a text | A distributional role, not a known word or grammatical suffix |
| Semantic or phonetic hypothesis | Fish-shaped sign represents a word pronounced *mīn*, meaning “star” | A proposal requiring evidence beyond resemblance or a plausible reading |

Do not assume in advance that the inscriptions are Tamil, Sanskrit, another particular language, or a simple substitution cipher. Consider phonetic, logographic, mixed, and nonlinguistic administrative interpretations. These are competing models, not equally established conclusions.

## What earlier researchers have tried

| Approach | Primary starting reference | What it contributes; limit |
|---|---|---|
| Sign catalogues, frequencies, positions, recurring groups | Mahadevan 1977, as used by [Yadav et al. 2010][yadav] | Establishes distributions and candidate units; catalogue IDs are not readings |
| Rebus and comparative linguistics | [Parpola 2009][parpola] | Develops Proto-Dravidian proposals using homophony and context; readings remain hypotheses |
| Entropy and information theory | [Rao et al. 2009, Science][entropy]; [Sproat 2014][sproat] | Measures sequence constraints; structured nonlinguistic systems complicate claims of linguisticity |
| Markov models and n-grams | [Rao et al. 2009, PNAS][markov]; [Yadav et al. 2010][yadav] | Predicts sign sequences and suggests restorations; prediction is not translation |
| Network analysis | [Sinha et al. 2011][network] | Finds organizational patterns and candidate segmentation; does not establish meanings |
| Allograph identification | [Daggumati & Revesz 2021][allographs] | Proposes grouping variants of the same sign; merging decisions need independent checks |
| Archaeology and administrative semantics | [Mukhopadhyay 2019][muk2019]; [2023][muk2023] | Proposes logographic/semasiographic and trade-related functions; those functions remain interpretations |
| Dictionary matching and cryptanalysis | [Yajnadevam 2024 manuscript][crypto] | Claims Sanskrit readings using regular expressions, set intersections, and Shannon-based arguments; record as a claim, not an accepted solution |
| Neural and visual models | [Tiwari 2026, NLP4DH proceedings][tiwari] | Combines visual clustering, entropy, HMMs, and BiLSTM sequence modeling; reports structure, not a decipherment |

Publication status matters: a manuscript claim, a conference paper, and an established corpus are different kinds of evidence. Peer review alone also does not validate a decipherment.

The fish-to-star proposal is a useful example of the reasoning to scrutinize. Parpola connects fish-shaped signs with reconstructed Dravidian homophones for “fish” and “star,” and interprets some numerical-plus-fish sequences astronomically. We may test this proposal later; we will not build it into the transcription or use it as a confirmed training label.

Our methodological assessment: matching an assumed language is insufficient if sign mergers, reading direction, segmentation, phonetic rules, and dictionary choices can change to accommodate each inscription. A Shannon-based uniqueness argument is conditional on the encoding and language model; it does not independently establish those assumptions.

## First case: Harappa tablet H-351

Source: Iravatham Mahadevan, [*A Megalithic Pottery Inscription and a Harappa Tablet: A Case of Extraordinary Resemblance*][tablet], section 3, PDF pp. 2–3; parallels discussed in section 5, PDF pp. 3–4.

The source identifies the object as **Vats 581 = IM 77:4581 = CISI-I:H-351**, a three-sided miniature steatite tablet. These are identifiers for the object/text, not separate independent observations.

| Surface | Published sign sequence, in the author's reading order | Conventional shape labels |
|---|---|---|
| Side 1 | `119 – 87 – 342 – 176` (first sign marked doubtful in reproduced M77 figure) | “Raindrops”; two tall strokes; “jar”; “harrow” |
| Side 2 | `95 – 328` | Four tall strokes; “cup” |
| Side 3 | `137` | X-shaped sign |

The [source audit](notes/IND-002-source-audit.md) maps these labels to CISI A/B/C and M77 side/line codes: paper Side 1 = CISI A = M77 `20`; Side 2 = B = `30`; Side 3 = C = `10`. Keep these labels separate and retain the doubtful-reading annotation on `119`.

The sign numbers use **Mahadevan's scheme**. A number such as 95 is a sign identifier, not a decoded quantity. Store the source's order explicitly; do not reverse it merely because the original script is usually described as right-to-left. Seal faces and impressions also require different orientation handling.

Mahadevan describes related Harappa tablets with the same four-sign group on one side and a cup preceded by two, three, or four tall strokes on another. This gives us a tractable comparison. The present project uses his Harappa transcription; it has not evaluated or adopted his separate argument about continuity with much later Sulur marks.

### Hypothesis H001 — fixed label with variable numerical field

**Status: proposed; five illustrated candidates identified in IND-002, with independent transcription review and hypothesis testing still pending.**

Some tablets may combine a relatively fixed label with a variable numerical field.

Alternatives include an amount or denomination, a numbered category or grade, or a phonetic/logographic expression whose variation is not simply quantitative. A single tablet cannot distinguish these.

The first test is to locate the actual parallel objects, verify each side and sign against its source, and catalogue what changes while the other field remains fixed. Avoid counting duplicate photographs, impressions, or publications as new objects. Supporting a numerical-field interpretation would still not reveal the spoken number words or the meaning of “cup.”

## Corpus choices

- **Mahadevan 1977 (M77):** foundational corpus and sign numbering. Yadav et al. report 2,906 texts in 3,573 lines and a 417-sign inventory.
- **EBUDS:** the published filtered benchmark derived from M77, containing 1,548 distinct, unambiguous single-line texts. It is a useful replication target, but this project has not obtained or verified the underlying sequence file.
- **CISI:** *Corpus of Indus Seals and Inscriptions*, the photographic reference for checking individual objects and transcriptions.
- **ICIT:** Wells and Fuls's [Interactive Corpus of Indus Text][icit], with search, positional analysis, and archaeological metadata. Its official page describes access by contacting the administrator; no access request has been sent by this project.

Do not merge sign IDs across catalogues without an explicit crosswalk. Object counts, text counts, line counts, duplicate counts, and distinct-sign counts are different quantities. Two digitizations of the same artifacts are not independent archaeological validation datasets.

As literature benchmarks, Yadav et al. identify signs 267, 391, and 293 as common beginners, and 342, 176, and 211 as common endings. These are results to reproduce, not results generated here.

## Ordered approach and completion criteria

1. **Verify sources and the starting case.** Establish usable corpus access, provenance, licensing, ID conventions, and the evidence for H-351. Record missing materials rather than guessing.
2. **Curate a small pilot.** Collect sourced H-351 parallels and stroke-plus-cup records, with individual sides kept distinct. Independently review transcriptions before freezing a pilot version.
3. **Run descriptive analysis.** Count signs, positions, repeated groups, and substitutions. Check whether apparent patterns survive object-level deduplication and alternative plausible readings.
4. **Replicate and challenge structural models.** Compare unigram and bigram baselines; use shuffled and structured administrative controls. Evaluate on genuinely withheld records and, where feasible, sites.
5. **Test semantic and phonetic proposals.** Specify mappings and rules before evaluation. Record failures and alternatives. Seek independent archaeological or linguistic anchors.

A proposed analysis table should retain: corpus/version; object ID; side/line ID; site; object type; dating information with uncertainty; source/page/image reference; source sign scheme; raw transcription; proposed normalized transcription; orientation and its evidence; damaged/uncertain signs; duplicate group; transcriber; reviewer; and review status. Proposed meanings belong in separate hypothesis fields.

For model tests, group duplicate and related records before splitting, fit transformations only on training data, tune on validation data, and retain a final test set. Report sample sizes and sensitivity to allograph choices. A favourable entropy, perplexity, or prediction score is evidence about structure, not proof of language identity.

## What would count as progress

Near-term progress means a verified dataset, replicated structural findings, and clearly testable functional hypotheses. Stronger progress would be a fixed interpretation that predicts independent inscriptions and fits external evidence with few exceptions. Model agreement or two assistants agreeing does not replace independent evidence.

The immediate handoff is **review of the [IND-002 source audit](notes/IND-002-source-audit.md) and [IND-003 pilot design](notes/IND-003-pilot-design.md)**, followed by completing the object crosswalks and transcriptions in IND-004. See [COORDINATION.md](COORDINATION.md) for status. Do not start translation generation or large models before the source and transcription checks.

[yadav]: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0009506
[parpola]: https://tuhat.helsinki.fi/ws/portalfiles/portal/127256488/Parpola_A_2009._Hind_leg_fish_in_the_Indus_script._Scripta1_37_76.pdf
[entropy]: https://pubmed.ncbi.nlm.nih.gov/19389998/
[sproat]: https://doi.org/10.1353/lan.2014.0031
[markov]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2721819/
[network]: https://arxiv.org/abs/1005.4997
[allographs]: https://www.nature.com/articles/s41599-021-00713-0
[muk2019]: https://www.nature.com/articles/s41599-019-0274-1
[muk2023]: https://www.nature.com/articles/s41599-023-02320-7
[crypto]: https://rarebooksocietyofindia.org/book_archive/A_cryptanalytic_decipherment_of_the_Indu.pdf
[tiwari]: https://aclanthology.org/2026.nlp4dh-1.28/
[tablet]: https://www.harappa.com/sites/default/files/pdf/sulur-megalithic.pdf
[icit]: https://www.epigraphica.de/indus/menueindus.htm

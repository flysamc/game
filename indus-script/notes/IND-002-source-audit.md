# IND-002 — source and starting-case audit

Author: Codex · 25 October 2026 · **IN REVIEW**  
Independent review: pending; Claude is the suggested reviewer.  
Scope: source availability, H-351, and identification of candidate parallels. No statistical test or decipherment is reported.

## Result

There is enough accessible evidence to design a small, image-linked pilot after review. H-351 can be located in the original photographic publication, and the later illustration identifies five candidate catalogue entries. Two corrections are essential: surface labels differ between publications, and two candidate transcriptions carry a doubtful-reading marker.

The project has downloaded reference scans, **not an audited machine-readable inscription corpus**. The proposed pilot must retain uncertainty and object-level provenance.

## Evidence actually inspected

| Source | Location inspected | What was checked |
|---|---|---|
| Mahadevan, *A Megalithic Pottery Inscription and a Harappa Tablet* | [Paper][paper], §3, pp. 2–3; §5, pp. 3–4 | Object cross-reference and author-reported sign IDs |
| Separate illustration supplement | [PDF][figures], PDF p. 2, Figs. 2–3; p. 3, Fig. 4 | Rendered images inspected: photograph, normalized shapes, five catalogue entries and annotations |
| Joshi and Parpola, eds., *Corpus of Indus Seals and Inscriptions*, vol. 1 (1987) | [IGNCA scan][cisi], title page at PDF p. 5; copyright p. 6; printed p. 230 at **PDF p. 266** | Original publication's H-351 A/B/C photographs and surface labels visually inspected |
| Mahadevan, *The Indus Script* (1977), codes | [Reproduced excerpt][m77-excerpt], printed pp. 30–31, codes 3, 5 and 8 | Text-layer inspection of side/line coding and doubtful-reading convention; not a visual check of the complete M77 edition |
| Yadav et al. (2010) | [Article][yadav], Materials and Methods; Fig. 12 caption | Corpus filtering, encoding direction and asterisk convention |
| Corpus providers | [RMRL][rmrl]; [ICIT page][icit]; [2010 ICIT manual][icit-manual], pp. 1–2, 5 | Provider identity, documented access and encoding conventions |

The supplement credits CISI for its photograph. These are two publications of the same photographic evidence, not two independent archaeological observations. Checking a scan is not examining the physical tablet.

Download URLs, byte counts, SHA-256 hashes and access limitations are in [the source manifest](../sources/manifest.json). Copyrighted scans and plates are not included in this repository.

## H-351 identity and surface crosswalk

**Source-reported identity:** Vats 581 = IM 77:4581 = CISI-I:H-351; ASI 63.11/75, excavation no. 2429. The paper describes a three-sided steatite tablet. The Vats and accession-number crosswalks were read in the paper, not separately checked against museum records.

**Project visual check:** CISI printed p. 230 labels the four-sign face A, the strokes-plus-cup face B, and the X face C. They correspond to the supplement's photographs. The number assignments below remain the author's transcription, with its uncertainty retained.

| Paper's label | CISI photograph label | M77 code in reproduced Fig. 4 | Author's sign IDs, in reading order |
|---|---|---|---|
| Side 1 | H-351 A | `20` | `119 – 87 – 342 – 176`; Fig. 4 marks the first sign doubtful |
| Side 2 | H-351 B | `30` | `95 – 328` |
| Side 3 | H-351 C | `10` | `137` |

M77's two-digit code combines side and line: `20` means side 2, its only line (`0`), not “line twenty.” Preserve the original codes as strings and keep each publication's labels separate. Do not concatenate the three surfaces into a presumed sentence.

The photographic comparison supports the surface mapping and visible groupings. It does **not** independently resolve every sign variant. In particular, retain the uncertainty on `119` even though the later prose supplies an unqualified normalized sequence.

## Five candidate entries, not a frozen dataset

The following is a visual inventory of **Fig. 4**, which reproduces M77 printed p. 360. “Same group” refers to the illustrated `119–87–342–176` group; asterisks qualify that identification.

| M77 text ID | Main-group code | Strokes-plus-cup code | Visible tall strokes in that field | Additional face shown |
|---|---|---|---:|---|
| `5498` | `10` | `20` | 2 | None shown |
| `4444` | `10` | `20` | 3 | None shown |
| `4456` | `10` | `20` | 3 | None shown |
| `4591` | `20`, asterisk at first sign | `30` | 4 | `10`: fish-shaped sign; paper identifies M77 `59` |
| `4581` | `20`, asterisk at first sign | `30` | 4 | `10`: X; paper identifies M77 `137` |

The asterisk is a doubtful-reading annotation, not another Indus sign: M77 code 8 and Yadav et al.'s Fig. 12 caption explain the convention. The mark's location in this figure is our visual observation. Preserve both the source mark and the proposed sign ID.

Only `4581` has been cross-linked here to an original CISI plate. The other four still need object crosswalks, photographs and duplicate checks. “None shown” is not evidence that an object has only two inscribed faces.

These examples were selected by the source author. They cannot estimate how common the pattern is or demonstrate a numerical function. The counts are graphic stroke counts, not translated number words or decoded quantities. H001 remains a hypothesis; catalogue matching and selection bias must be addressed before testing it.

## Corpus access and suitability

| Resource | What this audit obtained | Remaining limitation / proposed role |
|---|---|---|
| M77 and the official IndusScript.in portal | RMRL confirms that its portal is based on Mahadevan 1977; selected M77 material is accessible through reproductions | No raw export obtained. A text-only fetch of the portal yielded no rows; that does not establish a login requirement. Pin the exact edition before comparing counts. |
| EBUDS | The primary article describes 1,548 filtered texts, excluding duplicates, uncertain material and multiline texts | No raw sequence file located in the article inspected. Useful later for replication; its filtering makes it unsuitable as the sole record of this multisurface case. |
| CISI | Downloaded the IGNCA scan; verified the vol. 1 title and H-351 plate | An image reference, not parsed sequences. The 862-page file's entire contents were not audited. Other candidates still require identification. |
| ICIT | Official access page and 2010 documentation | The page directs access enquiries to an administrator. No account, live export or reuse permission obtained. Historical guest-access documentation is not confirmation of current availability. |

No dataset redistribution permission was established. The CISI copyright page distinguishes volume and photographic rights. Yadav et al.'s article states a Creative Commons Attribution license; that alone does not license an unprovided underlying corpus or separately credited photographs. This repository currently stores our notes and factual source references.

### Encoding trap to preserve in IND-003

Yadav et al. print numerical sequences in left-to-right reading order, while their glyph images are read right-to-left. The **2010** ICIT manual instead illustrates a numeric string whose initial sign is at the right; it also distinguishes `000` (one eroded sign) from `++` (an eroded part of unknown length). Never reverse an imported sequence or discard punctuation without checking that export's convention. ICIT sign IDs are not interchangeable with M77 IDs.

## Recommendation and review handoff

Use a **five-entry source inventory** as the first curation target, anchored by H-351. This is a proposed choice for IND-003, not a frozen analytical sample. Keep surfaces separate and store source-specific codes, source uncertainty, image references and crosswalk confidence. Expand to a declared search set before estimating frequencies or testing H001.

Suggested independent review for Claude:

1. Reopen CISI PDF p. 266 and the supplement pp. 2–3; check all IDs, stroke counts and the surface crosswalk without copying this table first.
2. Check that the asterisks qualify the initial `119` readings on `4581` and `4591`; preserve any disagreement rather than choosing a reading by majority vote.
3. Confirm that access findings distinguish a downloaded reference scan from available sequence data, and that no unverified corpus version is silently adopted.
4. Record reviewer, date, findings and corrections in `COORDINATION.md`. If accepted, close IND-002 and make IND-003 READY. The missing photographs/crosswalks for the other four candidates belong to the later curation task and must be resolved before an analytical pilot is frozen.

No Claude review or acknowledgement has occurred. No statistical code, corpus frequencies, semantic readings or pronunciation assignments were produced in this stage.

[paper]: https://www.harappa.com/sites/default/files/pdf/sulur-megalithic.pdf
[figures]: https://www.harappa.com/sites/default/files/pdf/sulur-figs.pdf
[cisi]: https://ignca.gov.in/Asi_data/76884.pdf#page=266
[m77-excerpt]: https://www.scribd.com/document/265262777/Excerpts-from-Mahadevan-I-1977-The-Indus-Script-Texts-Concordance-and-Tables-Delhi-ASI-Memoir-No-77
[yadav]: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0009506
[rmrl]: https://rmrl.in/en/irc
[icit]: https://www.epigraphica.de/indus/menueindus.htm
[icit-manual]: https://www.epigraphica.de/indus/help_onlinedatabase.pdf

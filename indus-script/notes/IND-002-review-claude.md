# IND-002 — independent review

Reviewer: Claude · 25 October 2026 · reviewing [PR #1](https://github.com/flysamc/game/pull/1) at commit `746a97e`  
Outcome: **accepted with additions.** The audit's identifications are correct as far as the accessible evidence goes. The additions below change what IND-003/IND-004 should treat as the curation target and should be read before the pilot schema is frozen.

I followed the audit's four-item checklist and filled in my own observations before comparing them with Codex's table.

## What I checked, and how

| Check | Evidence I actually inspected | Result |
|---|---|---|
| Paper crosswalk | Mahadevan, *Sulur* paper, PDF p. 2 §3 text; pp. 3–4 §§4–5 text (extracted text layer) | **Confirmed.** Vats 581 = IM 77:4581 = CISI-I:H-351, ASI 63.11/75, Exc. No. 2429; 137 fills one side of 4581, 59 of 4591 |
| Fig. 4 (reproduced M77 p. 360) | Supplement PDF p. 3, rendered at 2.5× and inspected glyph by glyph | **Confirmed.** Stroke counts 5498 = 2, 4444 = 3, 4456 = 3, 4591 = 4, 4581 = 4; side codes 10/20/30 as in the audit; single-sign faces fish (4591.10) and X (4581.10) |
| Asterisk placement | Same render | **Confirmed.** On 4591.20 and 4581.20 the asterisk sits beside the first sign in reading order (the "raindrops"-shaped sign, M77 119). It is absent from 5498, 4444, 4456 |
| CISI plate | IGNCA scan PDF p. 266 = printed p. 230, rendered at 2.2× | **Confirmed** surface labels H-351 A (four-sign group), B (strokes + cup), C (X across the whole face) |
| Machine-readable cross-check | Third-party digitization of M77 (see "Corpus access" below), records 4581, 4591, 5498, 4444, 4456 | **All sign IDs and side codes match the audit's table.** The digitization flags one doubtful sign of four on 4581.20 and 4591.20, but stores only the count, so it cannot by itself confirm *which* sign is doubtful; Fig. 4 does |

Retrieval note: the cloud workspace could not reach harappa.com or ignca.gov.in directly; I rendered the PDFs in the browser with PDF.js (range requests, so only the needed pages of the 31 MB CISI scan were fetched) and inspected the renders. No PDFs or plates are committed.

## Observations that qualify the audit

1. **H-351 A, first sign (reading order).** In the CISI photograph the right-hand sign is worn. It is compatible with 119 but not clearly legible at this scan's resolution. This supports keeping Mahadevan's doubtful mark and not normalizing it away, as the audit already says.
2. **H-351 B stroke count.** The photograph is consistent with four strokes after the cup, but one stroke is slanted and one lies close to the tablet edge. At this resolution I would record `stroke_count = 4 (catalogue); photo: consistent, not unambiguous` rather than treat the photograph as an independent confirmation of "4".
3. **Additional parallel cited by the paper.** §4 also cites **5296**, a sealing with 137 filling one side. It is not in the five-entry inventory. It belongs in the candidate list for the X-face comparison even though it has no cup line.
4. **The same three-sided format extends beyond the five.** CISI p. 230 shows **H-352, H-353 and H-354** directly beside H-351: each has a strokes-plus-cup face (B) and a face of three dotted circles (C), but a *different* label on face A. The dotted-circle faces are not recorded as text in M77, which is a concrete case of the audit's warning that "none shown" does not mean "no other face". I have **not** verified the M77 numbers for H-352–354; the obvious guess (Vats 582–584 ⇒ M77 4582–4584) must be checked, not assumed. The neighbouring M77 records, for example, give 4582 = `67 244 342 176` / `95 328`, but 4583–4584 have no cup line, so a simple +1 crosswalk already looks wrong for at least one of them.

## Corpus access: correction to the audit's finding

The audit states that no machine-readable M77 export was obtained. A third-party digitization does exist:

- Repository [joyboseroy/indus_decipher](https://github.com/joyboseroy/indus_decipher), file `data/m77_indusscript_real_corpus.csv`: 3,573 non-empty lines and 2,906 distinct texts, matching the line and text counts Yadav et al. report for M77 (14,153 sign occurrences, 418 sign IDs including `000`). Its converter documents conventions: `inscription_id = textnum.sideline` with M77 side/line codes, `000` → `MSg0` for an illegible sign, doubtful signs stored only as a per-line percentage.
- **Provenance caveat, important:** the converter says the data were exported from the IndusScript.in (RMRL/Indus Research Centre) backend through a logged-in browser session. Reuse terms are not established, and the official portal is "all rights reserved". Treat it as a *located, provenance-documented third-party copy with unknown license*: fine for cross-checking and for finding candidate records, not for committing to this repository.
- The same repository holds an ICIT-based digitization (Yajnadevam's, 2,543 inscriptions, 52 sites, own glyph numbering). It is stored in reverse of reading order; the jar sign is first in 34% of its texts until reversed. This is exactly the encoding trap the audit's "Encoding trap" section anticipates.
- The audit's other access findings (CISI is an image reference; ICIT requires the administrator; EBUDS sequence file not located) are confirmed by what I saw.

Suggested manifest addition: one entry for this digitization with the caveat above, `raw_sequence_file_obtained: true (third-party)`, `reuse_license: "not established"`.

## Why this matters for H001 and IND-003

The five illustrated entries are a source-selected subset, as the audit says. The digitization lets us size the selection effect without testing H001:

- Texts containing the full group `119 87 342 176`: **11**. Of these, **5** also have a two-sign line ending in the cup (the five in Fig. 4); the other 6 do not.
- Texts with a two-sign line `[X] 328`: **255**. First signs are mostly stroke signs (89 three strokes: 111; 87 two strokes: 74; 95 four strokes: 50; 86 one stroke: 7).

So "strokes + cup" is a widespread standalone formula that pairs with several different labels, not a field specific to the H-351 label. My recommendations for IND-003/IND-004:

1. Define the curation unit as the **strokes-plus-cup family** (all objects with a `[stroke] 328` face), with the H-351 group as one label among several, rather than as the five illustrated entries.
2. Add schema fields for **non-text faces** (e.g. dotted circles: present / absent / not reported) and for **doubtful-sign position** separately from a doubtful-sign count, since sources differ in which they give.
3. **Pre-register the H001 comparison before tabulating labels against stroke counts.** For example: does stroke count vary within objects sharing an identical label more than chance under a permutation of counts across labels? Write the null, the unit (object, not impression) and the duplicate rule first.
4. Disclosure: while checking the crosswalk I listed M77 records 4580–4597 and saw their label and stroke-count pairs. That exposure should be recorded so whoever designs the H001 test knows the reviewer has seen part of the outcome.

## Separate, exploratory work (not part of IND-002)

Before joining this workspace, Claude ran an exploratory, corpus-wide statistical comparison for Sam, outside this task board. It used the third-party M77 digitization, Sumerian seal and administrative texts mapped to cuneiform signs (CDLI), Akkadian signs (Akkademia), English, and synthetic controls. It reproduces the literature benchmarks named in the README (beginners 267, 391; enders 342, 176, 211, plus 328 when multi-line texts are kept). It is unaudited and was not pre-registered, so it is **not** evidence for any IND task. If Sam and Codex want it, it can be added as a clearly labelled input to IND-006 with its code; I have not committed it here.

## Status change proposed

- IND-002 → **DONE** (reviewed by Claude, accepted with the additions above).
- IND-003 stays **IN PROGRESS — Codex**; the additions above are inputs to it, not a takeover.
- Open questions for Codex: (a) do you accept the "family" framing for IND-004, or do you want to keep the five as a first slice? (b) should the third-party M77 digitization be registered in the manifest given its unclear terms, or kept out entirely?

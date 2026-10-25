# Pilot inventory

The separate [family candidate queue](family-candidates-v0.1.json) now lists **241 export-derived catalogue anchors**, including the five pilot anchors and 236 additional candidates, plus the audit of other cup-containing rows. It is **unreviewed discovery output**, not an expanded frozen corpus. See the [protocol, results and reproduction instructions](../notes/IND-004-family-discovery.md). The frozen pilot described below is unchanged.

[`pilot-v0.2.json`](pilot-v0.2.json) is the **frozen, independently reviewed five-object pilot**, released on 25 October 2026: twelve normalized faces, photographic checks for every face, two preserved source-doubt marks and one documented classification disagreement. [Claude accepted all five record transcriptions and the ambiguity representation](https://github.com/flysamc/game/pull/4#pullrequestreview-5645371653), following the earlier source and identity acceptance. See the [release record](../notes/IND-004-pilot-release.md) and [file hashes](../releases/pilot-v0.2.json). This selected pilot supports bounded descriptions, not population inference, an H001 test or decipherment.

[`pilot-v0.1.json`](pilot-v0.1.json) and its schema are retained unchanged as history: three normalized faces and nine gaps at that stage. The [original design](../notes/IND-003-pilot-design.md) is historical; v0.2 adds the photo-outcome and surface-content corrections requested in review. Source evidence is registered in the [manifest](../sources/manifest.json).

From the repository root, with Python 3.11 or newer:

```sh
python3 -m venv indus-script/.venv
indus-script/.venv/bin/python -m pip install -r indus-script/requirements.txt
indus-script/.venv/bin/python indus-script/scripts/validate_pilot.py
indus-script/.venv/bin/python -m unittest discover -s indus-script/tests -v
indus-script/.venv/bin/python indus-script/scripts/validate_pilot.py --require-ready
```

The default validator uses the [v0.2 schema](../schemas/pilot-v0.2.schema.json). It reports **5 catalogue records, 12 faces, 12 normalized faces and 2 faces with source doubt**, plus one face with disputed content classification. There are 17 field-level photographic outcomes (9 confirms, 8 consistent), not 17 objects or photographs. These are file-inventory counts, not estimated script frequencies.

Both normal validation and `--require-ready` now exit **0** for the frozen v0.2 release, with no blockers. A structurally valid unfinished draft still exits **1** with `--require-ready`; structural/provenance inconsistencies exit **2**. The program does not alter the data. Paths resolve relative to the script, so it can run outside the repository root. Freeze preserves the qualified readings and content disagreement; it does not make them certain. Use a new dataset version for subsequent curation.

For the preserved v0.1 inventory, pass both matching paths:

```sh
indus-script/.venv/bin/python indus-script/scripts/validate_pilot.py --data indus-script/data/pilot-v0.1.json --schema indus-script/schemas/pilot-v0.1.schema.json
```

M77-1977 sign IDs 1–417 are strings, not decoded values. The pilot rejects `000`: M77's illegibility marker may cover an unknown-length span. Before broader import, preserve such spans explicitly rather than assigning a single unknown sign or dropping them.

For each surface, keep `content` separate from its normalized reading. `non_script_motif` and `blank` require no invented script tokens; `not_reported` does not imply blankness. A non-script face without an M77 code can use a CISI face label and stable ID such as `m77-XXXX-cisi-i-C`. This is a format example, not an additional pilot face.

`content` is the working source classification. `content_disputed` and `content_assessments` preserve alternatives with evidence and distinguish an explicit source encoding from reviewer inference. H-977 C retains M77 sign 59 while recording the competing fish-motif assessment inferred from the CISI-II plate heading. False means no recorded disagreement, not certain linguistic status. Independent review may accept the documented ambiguity without choosing a winner. The validator reports disputed faces even after review; later analyses must explicitly handle their alternative classifications.

`photo_evidence_refs` lists consulted photographs. `photo_checks` records what each photograph supports, with a checker and explanation. `consistent` is qualified support; `illegible` and `contradicts` prevent freezing until resolved. Neither photographic inspection nor green validation is independent review. Synthetic test reviews exist only in memory and never write acceptance to the research files. Equal transcriptions do not establish object identity, and this selected pilot never permits population inference.

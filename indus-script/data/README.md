# Pilot inventory

[`pilot-v0.2.json`](pilot-v0.2.json) is the current **draft curation inventory**: five source-selected catalogue records, twelve normalized faces, photographic checks for every face, and two preserved source-doubt marks. Read the [curation note](../notes/IND-004-pilot-curation.md) for the object crosswalks and qualifications. Independent v0.2 transcription, identity and source-addendum reviews remain pending. No analytical release or decipherment is claimed.

[`pilot-v0.1.json`](pilot-v0.1.json) and its schema are retained unchanged as history: three normalized faces and nine gaps at that stage. The [original design](../notes/IND-003-pilot-design.md) is historical; v0.2 adds the photo-outcome and surface-content corrections requested in review. Source evidence is registered in the [manifest](../sources/manifest.json).

From the repository root, with Python 3.11 or newer:

```sh
python3 -m venv indus-script/.venv
indus-script/.venv/bin/python -m pip install -r indus-script/requirements.txt
indus-script/.venv/bin/python indus-script/scripts/validate_pilot.py
indus-script/.venv/bin/python -m unittest discover -s indus-script/tests -v
indus-script/.venv/bin/python indus-script/scripts/validate_pilot.py --require-ready
```

The default validator uses the [v0.2 schema](../schemas/pilot-v0.2.schema.json). It reports **5 catalogue records, 12 faces, 12 normalized faces and 2 faces with source doubt**. There are 17 field-level photographic outcomes (11 confirms, 6 consistent), not 17 objects or photographs. These are file-inventory counts, not estimated script frequencies.

Normal validation exits **0** for a valid draft. For the current draft, `--require-ready` intentionally exits **1** and lists the outstanding reviews and identity decisions. Structural/provenance inconsistencies exit **2**. The program does not alter the data. Paths resolve relative to the script, so it can run outside the repository root.

For the preserved v0.1 inventory, pass both matching paths:

```sh
indus-script/.venv/bin/python indus-script/scripts/validate_pilot.py --data indus-script/data/pilot-v0.1.json --schema indus-script/schemas/pilot-v0.1.schema.json
```

M77-1977 sign IDs 1–417 are strings, not decoded values. The pilot rejects `000`: M77's illegibility marker may cover an unknown-length span. Before broader import, preserve such spans explicitly rather than assigning a single unknown sign or dropping them.

For each surface, keep `content` separate from its normalized reading. `non_script_motif` and `blank` require no invented script tokens; `not_reported` does not imply blankness. A non-script face without an M77 code can use a CISI face label and stable ID such as `m77-XXXX-cisi-i-C`. This is a format example, not an additional pilot face.

`photo_evidence_refs` lists consulted photographs. `photo_checks` records what each photograph supports, with a checker and explanation. `consistent` is qualified support; `illegible` and `contradicts` prevent freezing until resolved. Neither photographic inspection nor green validation is independent review. Synthetic test reviews exist only in memory and never write acceptance to the research files. Equal transcriptions do not establish object identity, and this selected pilot never permits population inference.

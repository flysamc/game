# Pilot inventory

`pilot-v0.1.json` is a **draft curation inventory**, not a decoded text corpus. It holds five source-selected catalogue records and twelve faces. Only H-351's three faces have provisional sign-number sequences. Nine faces remain untranscribed, and independent reviews and physical-object duplicate decisions remain pending.

Read the [pilot design](../notes/IND-003-pilot-design.md) before editing. The [JSON Schema](../schemas/pilot-v0.1.schema.json) defines allowed fields; the validator also checks cross-record provenance and review conditions. Source evidence is registered in the [manifest](../sources/manifest.json).

From the repository root, with Python 3.11 or newer:

```sh
python3 -m venv indus-script/.venv
indus-script/.venv/bin/python -m pip install -r indus-script/requirements.txt
indus-script/.venv/bin/python indus-script/scripts/validate_pilot.py
indus-script/.venv/bin/python -m unittest discover -s indus-script/tests -v
```

The validator reports a valid draft, **5 catalogue records, 12 faces, 3 normalized faces and 2 faces with source doubt**. It also reports that analysis is not ready. These are file-inventory counts, not estimated script frequencies or independent artifact counts.

To enforce the analysis gate:

```sh
indus-script/.venv/bin/python indus-script/scripts/validate_pilot.py --require-ready
```

For this draft, the command intentionally exits **1** and lists the missing evidence/reviews. Structural or provenance inconsistencies exit **2**; a valid draft without `--require-ready` exits **0**. The program does not alter the data. All paths are resolved relative to the script by default, so it can also run outside the repository root.

The schema's fixed M77-1977 inventory uses sign IDs 1–417 as strings. It does not accept ICIT IDs or infer unknown IDs from shape names. The source marks and source-specific side labels must survive every edit. Equal transcriptions do not establish equal object identity.

Do not interpret a green validation result as independent epigraphic review. The test suite covers failure cases and a clearly labelled synthetic readiness case; it does not write a reviewer or approval into the research files.

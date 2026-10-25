#!/usr/bin/env python3
"""Validate the pilot's structure and provenance links; do not infer readings."""

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

ROOT = Path(__file__).resolve().parents[1]


def _reference_uses(value, path=""):
    if isinstance(value, dict):
        for key, child in value.items():
            location = f"{path}/{key}"
            if key.endswith("_refs"):
                for reference in child:
                    yield location, reference
            else:
                yield from _reference_uses(child, location)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _reference_uses(child, f"{path}/{index}")


def _review_errors(review, author, label):
    errors = []
    if review["status"] == "pending":
        if any(review[k] is not None for k in ("reviewer", "reviewed_on", "reference")):
            errors.append(f"{label}: pending review must not imply a completed reviewer/date/reference")
    else:
        if any(not review[k] or not review[k].strip() for k in ("reviewer", "reviewed_on", "reference")):
            errors.append(f"{label}: a review decision needs reviewer, date and reference")
        if review["reviewer"] and review["reviewer"].strip().casefold() == author.strip().casefold():
            errors.append(f"{label}: the transcriber cannot supply the independent review")
    return errors


def validate(data, schema, manifest):
    """Return errors plus a readiness report. A valid draft need not be ready."""
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [f"/{'/'.join(map(str, e.absolute_path))}: {e.message}" for e in validator.iter_errors(data)]
    if errors:
        return errors, {"valid": False, "ready_for_descriptive_analysis": False}

    if not isinstance(manifest, dict) or not isinstance(manifest.get("sources"), list) or any(
        not isinstance(s, dict) or not isinstance(s.get("id"), str) or not s["id"].strip()
        for s in manifest.get("sources", [])
    ):
        return ["source manifest must contain source objects with nonempty string IDs"], {"valid": False, "ready_for_descriptive_analysis": False}
    sources = {s["id"] for s in manifest["sources"]}
    evidence = {e["id"]: e for e in data["evidence"]}
    for label, values in (
        ("manifest source ID", [s["id"] for s in manifest["sources"]]),
        ("evidence ID", [e["id"] for e in data["evidence"]]),
        ("record ID", [r["record_id"] for r in data["records"]]),
        ("catalogue ID", [r["catalogue"]["text_id"] for r in data["records"]]),
        ("surface ID", [s["surface_id"] for r in data["records"] for s in r["surfaces"]]),
    ):
        for value, count in Counter(values).items():
            if count > 1:
                errors.append(f"duplicate {label}: {value}")
    selected = set(data["selection"]["catalogue_ids"])
    recorded = {r["catalogue"]["text_id"] for r in data["records"]}
    if selected != recorded:
        errors.append("selection catalogue_ids must match the recorded catalogue IDs")
    for item in data["evidence"]:
        if item["source_id"] not in sources:
            errors.append(f"{item['id']}: unknown manifest source {item['source_id']}")
    for path, reference in _reference_uses(data):
        if reference not in evidence:
            errors.append(f"{path}: unknown evidence reference {reference}")

    blockers = []
    if data["release_status"] != "frozen":
        blockers.append("Dataset is a draft, not a frozen release.")
    source_reviewed = (
        manifest.get("independent_review") == "accepted"
        and isinstance(manifest.get("reviewer"), str)
        and bool(manifest["reviewer"].strip())
        and manifest["reviewer"].strip().casefold() != manifest.get("author", "").strip().casefold()
        and isinstance(manifest.get("review_reference"), str)
        and bool(manifest["review_reference"].strip())
    )
    if not source_reviewed:
        blockers.append("IND-002 source audit has no recorded independent acceptance.")

    aliases = defaultdict(list)
    surfaces = []
    for record in data["records"]:
        rid = record["record_id"]
        if rid != f"m77-{record['catalogue']['text_id']}":
            errors.append(f"{rid}: record ID must retain its M77 catalogue anchor")
        errors.extend(_review_errors(record["review"], record["recorded_by"], rid))
        errors.extend(_review_errors(record["identity"]["review"], record["recorded_by"], f"{rid} identity"))
        identity = record["identity"]
        if identity["status"] == "resolved":
            if not identity["physical_object_group"] or not identity["evidence_refs"] or identity["review"]["status"] != "accepted":
                errors.append(f"{rid}: resolved identity needs a group, evidence and independent review")
        elif identity["physical_object_group"] is not None:
            errors.append(f"{rid}: unresolved identity must not assert a physical-object group")
        record_aliases = [(a["scheme"], a["value"]) for a in record["aliases"]]
        if len(set(record_aliases)) != len(record_aliases):
            errors.append(f"{rid}: duplicate alias within record")
        for alias in record_aliases:
            aliases[alias].append(record)

        missing = []
        if record["review"]["status"] != "accepted":
            missing.append("independent transcription review")
        if identity["status"] != "resolved":
            missing.append("object identity/duplicate adjudication")
        unnormalized = sum(s["normalization"] is None for s in record["surfaces"])
        unphotographed = sum(not s["photo_evidence_refs"] for s in record["surfaces"])
        if unnormalized:
            missing.append(f"normalization on {unnormalized} face(s)")
        if unphotographed:
            missing.append(f"photographic checks on {unphotographed} face(s)")
        if missing:
            blockers.append(f"{rid}: missing " + "; ".join(missing))

        for surface in record["surfaces"]:
            surfaces.append(surface)
            sid = surface["surface_id"]
            labels = surface["labels"]
            namespaces = [x["namespace"] for x in labels]
            if len(set(namespaces)) != len(namespaces):
                errors.append(f"{sid}: duplicate label namespace")
            m77 = [x["value"] for x in labels if x["namespace"] == "M77-side-line"]
            if len(m77) != 1 or not re.fullmatch(r"[0-6][0-39]", m77[0]) or sid != f"{rid}-{m77[0]}":
                errors.append(f"{sid}: invalid M77 side/line label or surface anchor")
            for reference in surface["photo_evidence_refs"]:
                if reference in evidence and evidence[reference]["kind"] != "photograph":
                    errors.append(f"{sid}: photograph check points to non-photograph {reference}")
            for reference in surface["observed_from"]["evidence_refs"]:
                if reference in evidence and evidence[reference]["kind"] != "normalized_diagram":
                    errors.append(f"{sid}: diagram observation points to a different representation {reference}")
            if surface["artifact_direction"] is not None and not surface["artifact_direction_evidence_refs"]:
                errors.append(f"{sid}: artifact direction requires evidence")
            if surface["artifact_direction"] is None and surface["artifact_direction_evidence_refs"]:
                errors.append(f"{sid}: direction evidence supplied without a direction decision")
            marks = surface["source_marks"]
            positions = [m["position_1based"] for m in marks]
            if len(set(positions)) != len(positions):
                errors.append(f"{sid}: repeated doubtful-reading mark at one position")
            normalization = surface["normalization"]
            if normalization is None:
                continue
            tokens = normalization["tokens"]
            if any(p > len(tokens) for p in positions):
                errors.append(f"{sid}: mark position exceeds normalized sequence length")
            for position, token in enumerate(tokens, 1):
                if not 1 <= int(token["sign_id"]) <= 417:
                    errors.append(f"{sid}: sign ID outside this M77-1977 inventory")
                if (token["certainty"] == "source_doubtful") != (position in positions):
                    errors.append(f"{sid}: doubtful-reading marker and token certainty disagree at position {position}")

    for alias, owners in aliases.items():
        if len(owners) > 1:
            groups = {r["identity"]["physical_object_group"] for r in owners}
            if None in groups or len(groups) != 1 or any(r["identity"]["status"] != "resolved" for r in owners):
                errors.append(f"shared alias {alias}: resolve all records to one reviewed physical-object group")

    if data["release_status"] == "frozen" and blockers:
        errors.append("frozen release has unresolved evidence or review blockers")
    report = {
        "valid": not errors,
        "dataset_id": data["dataset_id"],
        "release_status": data["release_status"],
        "catalogue_records": len(data["records"]),
        "surfaces": len(surfaces),
        "normalized_surfaces": sum(s["normalization"] is not None for s in surfaces),
        "surfaces_with_source_doubt": sum(bool(s["source_marks"]) for s in surfaces),
        "ready_for_descriptive_analysis": not errors and not blockers,
        "population_inference_allowed": False,
        "blockers": blockers,
    }
    return errors, report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=ROOT / "data/pilot-v0.1.json")
    parser.add_argument("--schema", type=Path, default=ROOT / "schemas/pilot-v0.1.schema.json")
    parser.add_argument("--manifest", type=Path, default=ROOT / "sources/manifest.json")
    parser.add_argument("--require-ready", action="store_true")
    args = parser.parse_args()
    try:
        data, schema, manifest = [json.loads(path.read_text(encoding="utf-8")) for path in (args.data, args.schema, args.manifest)]
        errors, report = validate(data, schema, manifest)
    except (OSError, ValueError, SchemaError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}, indent=2))
        return 2
    report["errors"] = errors
    print(json.dumps(report, indent=2))
    if errors:
        return 2
    if args.require_ready and not report["ready_for_descriptive_analysis"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

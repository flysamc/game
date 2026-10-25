"""Data-contract regressions; synthetic review fixtures are not research reviews."""

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_pilot import validate


class PilotContractTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "data/pilot-v0.1.json").read_text())
        self.schema = json.loads((ROOT / "schemas/pilot-v0.1.schema.json").read_text())
        self.manifest = json.loads((ROOT / "sources/manifest.json").read_text())

    def check(self):
        return validate(self.data, self.schema, self.manifest)

    def h351(self):
        return next(r for r in self.data["records"] if r["record_id"] == "m77-4581")

    def main_face(self):
        return next(s for s in self.h351()["surfaces"] if s["surface_id"] == "m77-4581-20")

    def test_draft_is_structurally_valid_but_not_ready(self):
        errors, report = self.check()
        self.assertEqual(errors, [])
        self.assertFalse(report["ready_for_descriptive_analysis"])
        self.assertEqual(report["normalized_surfaces"], 3)

    def test_h351_surface_mapping_and_uncertainty_survive_serialization(self):
        expected = {"20": ("Side 1", "A"), "30": ("Side 2", "B"), "10": ("Side 3", "C")}
        for face in self.h351()["surfaces"]:
            labels = {x["namespace"]: x["value"] for x in face["labels"]}
            self.assertEqual((labels["Mahadevan-paper-side"], labels["CISI-I-face"]), expected[labels["M77-side-line"]])
        token = self.main_face()["normalization"]["tokens"][0]
        self.assertEqual(token, {"sign_id": "119", "certainty": "source_doubtful"})

    def test_unknown_evidence_is_rejected(self):
        self.main_face()["normalization"]["evidence_refs"] = ["invented-source"]
        self.assertTrue(any("unknown evidence" in e for e in self.check()[0]))

    def test_unregistered_publication_is_rejected(self):
        self.data["evidence"][0]["source_id"] = "invented-publication"
        self.assertTrue(any("unknown manifest source" in e for e in self.check()[0]))

    def test_malformed_manifest_returns_a_validation_error(self):
        self.manifest = {"sources": [None]}
        self.assertTrue(any("source manifest" in e for e in self.check()[0]))

    def test_ambiguous_manifest_source_id_is_rejected(self):
        self.manifest["sources"].append(copy.deepcopy(self.manifest["sources"][0]))
        self.assertTrue(any("duplicate manifest source ID" in e for e in self.check()[0]))

    def test_out_of_inventory_sign_is_rejected(self):
        self.main_face()["normalization"]["tokens"][1]["sign_id"] = "520"
        self.assertTrue(any("outside this M77-1977 inventory" in e for e in self.check()[0]))

    def test_doubtful_sign_cannot_be_silently_made_certain(self):
        self.main_face()["normalization"]["tokens"][0]["certainty"] = "not_marked_doubtful"
        self.assertTrue(any("certainty disagree" in e for e in self.check()[0]))

    def test_marker_position_must_fit_the_sequence(self):
        self.main_face()["source_marks"][0]["position_1based"] = 5
        self.assertTrue(any("exceeds normalized sequence" in e for e in self.check()[0]))

    def test_source_ids_are_strings_and_cannot_become_quantities(self):
        self.main_face()["normalization"]["tokens"][0]["sign_id"] = 119
        self.assertTrue(self.check()[0])

    def test_boolean_is_not_a_stroke_count(self):
        face = next(s for s in self.h351()["surfaces"] if s["tall_strokes_next_to_cup"])
        face["tall_strokes_next_to_cup"]["count"] = True
        self.assertTrue(self.check()[0])

    def test_duplicate_catalogue_record_is_rejected(self):
        self.data["records"].append(copy.deepcopy(self.h351()))
        self.assertTrue(any("duplicate catalogue ID" in e for e in self.check()[0]))

    def test_shared_object_alias_requires_identity_adjudication(self):
        self.data["records"][0]["aliases"].append(copy.deepcopy(self.h351()["aliases"][0]))
        self.assertTrue(any("shared alias" in e for e in self.check()[0]))

    def test_diagram_does_not_count_as_photographic_check(self):
        self.main_face()["photo_evidence_refs"] = ["fig4"]
        self.assertTrue(any("non-photograph" in e for e in self.check()[0]))

    def test_freeze_cannot_hide_unfinished_curation(self):
        self.data["release_status"] = "frozen"
        self.assertTrue(any("frozen release" in e for e in self.check()[0]))

    def test_self_review_does_not_supply_independent_acceptance(self):
        self.h351()["review"] = {"status": "accepted", "reviewer": "Codex", "reviewed_on": "2026-10-25", "reference": "synthetic-test"}
        self.assertTrue(any("cannot supply the independent review" in e for e in self.check()[0]))

    def test_unrecorded_artifact_direction_is_rejected(self):
        self.main_face()["artifact_direction"] = "right_to_left"
        self.assertTrue(any("direction requires evidence" in e for e in self.check()[0]))

    def test_ready_path_with_explicitly_synthetic_reviews(self):
        # This fixture exercises the gate only; it never writes acceptance to disk.
        record = self.h351()
        self.data["records"] = [record]
        self.data["selection"]["catalogue_ids"] = ["4581"]
        self.data["selection"]["scope"] = "Synthetic test fixture; not a research sample."
        self.data["release_status"] = "frozen"
        review = {"status": "accepted", "reviewer": "Synthetic reviewer", "reviewed_on": "2026-10-25", "reference": "synthetic-test-only"}
        record["review"] = copy.deepcopy(review)
        record["identity"] = {"status": "resolved", "physical_object_group": "synthetic-H351", "evidence_refs": ["paper-case", "cisi230"], "review": copy.deepcopy(review)}
        self.manifest.update(independent_review="accepted", reviewer="Synthetic reviewer", review_reference="synthetic-test-only")
        errors, report = self.check()
        self.assertEqual(errors, [])
        self.assertTrue(report["ready_for_descriptive_analysis"])
        self.assertFalse(report["population_inference_allowed"])


if __name__ == "__main__":
    unittest.main()

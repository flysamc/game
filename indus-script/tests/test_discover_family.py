"""Synthetic source fixtures; no unreviewed archaeological readings are invented."""
import copy
import csv
import io
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from discover_family import FIELDS, blob_sha, discover


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((ROOT / 'sources/family-discovery-v0.1.json').read_text())

    def run_fixture(self, rows):
        out = io.StringIO(newline='')
        writer = csv.DictWriter(out, fieldnames=FIELDS)
        writer.writeheader()
        for rid, sequence, uncertainty in rows:
            writer.writerow(dict(inscription_id=rid, sign_sequence=sequence,
                                 site='unknown', object_type='unknown', line_count=1,
                                 damaged=False, reading_direction='R-L', motif='unknown',
                                 mean_uncertainty=uncertainty))
        raw = out.getvalue().encode()
        manifest = copy.deepcopy(self.manifest)
        manifest['source']['git_blob_sha'] = blob_sha(raw)
        return discover(raw, manifest, '0' * 40)

    def test_complete_faces_group_by_catalogue_without_merging_objects(self):
        result = self.run_fixture([('1002.10', 'MSg86 MSg328', 0),
                                   ('1001.10', 'MSg95 MSg328', 0),
                                   ('1001.20', 'MSg87 MSg328', 0)])
        self.assertEqual([r['catalogue_id'] for r in result['candidates']], ['1001', '1002'])
        self.assertEqual([len(r['matching_rows']) for r in result['candidates']], [2, 1])
        self.assertTrue(all(r['identity_status'] == 'not_adjudicated_by_discovery' for r in result['candidates']))

    def test_matching_line_is_not_promoted_to_complete_face(self):
        result = self.run_fixture([('1001.11', 'MSg86 MSg328', 0),
                                   ('1001.12', 'MSg59', 0),
                                   ('1002.10', 'MSg87 MSg328', 0),
                                   ('1002.11', 'MSg59', 0)])
        self.assertEqual(result['candidates'], [])
        self.assertEqual({r['reason'] for r in result['manual_review_rows']},
                         {'matching_line_not_complete_face', 'conflicting_rows_on_same_side'})

    def test_doubt_is_retained_and_unknown_span_cannot_fill_a_count(self):
        result = self.run_fixture([('1001.0', 'MSg86 MSg328', 50),
                                   ('1002.0', 'MSg0 MSg328', 0)])
        self.assertTrue(result['candidates'][0]['matching_rows'][0]['source_uncertainty_present'])
        self.assertEqual(result['manual_review_rows'][0]['reason'], 'unknown_span_not_a_wildcard')

    def test_reverse_pairs_and_short_variants_are_audited_without_normalization(self):
        result = self.run_fixture([('1001.0', 'MSg328 MSg86', 0),
                                   ('1002.0', 'MSg108 MSg328', 0),
                                   ('1003.0', 'MSg110 MSg328', 0),
                                   ('1004.0', 'MSg119 MSg328', 0),
                                   ('1005.0', 'MSg119 MSg87 MSg328', 0)])
        self.assertEqual(result['candidates'], [])
        self.assertEqual(result['integrity']['rows_containing_cup'], 5)
        self.assertEqual(result['integrity']['manual_review_rows'], 1)
        self.assertEqual(result['audit_reason_counts']['excluded_stroke_variant'], 2)
        self.assertTrue(result['integrity']['all_cup_rows_accounted_for'])

    def test_output_never_contains_sequences_or_count_label_fields(self):
        result = self.run_fixture([('1001.0', 'MSg95 MSg328', 0), ('1001.10', 'MSg119 MSg87', 0)])
        payload = json.dumps(result)
        for forbidden in ['MSg95', 'MSg119', 'sign_sequence', 'label_key', 'stroke_count', 'reading_direction']:
            # The protocol's boolean prohibition has "stroke_counts" in its key;
            # check the candidate records themselves for field-name leakage.
            target = json.dumps(result['candidates']) if forbidden == 'stroke_count' else payload
            self.assertNotIn(forbidden, target)

    def test_duplicate_canonical_ids_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate normalized'):
            self.run_fixture([('1001.0', 'MSg86 MSg328', 0), ('1001.00', 'MSg87 MSg328', 0)])

    def test_wrong_input_blob_cannot_be_used(self):
        with self.assertRaisesRegex(ValueError, 'pinned Git blob'):
            discover(b'not the corpus', self.manifest, '0' * 40)

    def test_malformed_ids_tokens_and_uncertainty_fail(self):
        for row in [('unknown.0', 'MSg86 MSg328', 0), ('1001.0', '*MSg86 MSg328', 0),
                    ('1001.0', 'MSg86 MSg328', 'NaN'), ('1001.0', 'MSg86 MSg328', 101)]:
            with self.subTest(row=row), self.assertRaises(ValueError):
                self.run_fixture([row])

    def test_unexpected_codes_and_field_symbols_need_manual_review(self):
        result = self.run_fixture([('1001.0', 'MSg418 MSg328', 0), ('1002.9', 'MSg86 MSg328', 0)])
        self.assertEqual(result['candidates'], [])
        self.assertEqual(result['integrity']['unexpected_sign_code_rows'], 1)
        self.assertEqual({r['reason'] for r in result['manual_review_rows']}, {'unexpected_sign_code', 'field_symbol_line_code'})


if __name__ == '__main__':
    unittest.main()

"""Failure cases for photographic claims and non-script faces; no real reviews."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_pilot import validate


class PhotoAndContentTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'data/pilot-v0.2.json').read_text())
        self.schema = json.loads((ROOT / 'schemas/pilot-v0.2.schema.json').read_text())
        self.manifest = json.loads((ROOT / 'sources/manifest.json').read_text())

    def check(self):
        return validate(self.data, self.schema, self.manifest)

    def face(self):
        return self.data['records'][0]['surfaces'][0]

    def make_synthetic_ready(self):
        # Never written to research data. Exercises gates, not their truth.
        self.data['records'] = [self.data['records'][0]]
        self.data['selection']['catalogue_ids'] = ['5498']
        self.data['selection']['scope'] = 'Synthetic gate fixture, not a research release.'
        self.data['release_status'] = 'frozen'
        review = dict(status='accepted', reviewer='Synthetic reviewer', reviewed_on='2026-10-25', reference='synthetic-only')
        r = self.data['records'][0]
        r['review'] = copy.deepcopy(review)
        r['identity'].update(status='resolved', physical_object_group='synthetic-5498', review=copy.deepcopy(review))
        self.manifest['curation_addendum'].update(independent_review='accepted', reviewer='Synthetic reviewer', reviewed_on='2026-10-25', review_reference='synthetic-only')

    def test_all_twelve_readings_are_valid_draft_with_qualified_photo_checks(self):
        errors, report = self.check()
        self.assertEqual(errors, [])
        self.assertEqual(report['normalized_surfaces'], 12)
        self.assertEqual(report['photo_check_outcomes'], {'confirms': 11, 'consistent': 6})
        self.assertFalse(report['ready_for_descriptive_analysis'])

    def test_consulted_photo_is_not_a_completed_check(self):
        self.face()['photo_checks'] = []
        errors, report = self.check()
        self.assertEqual(errors, [])
        self.assertTrue(any('missing explicit photographic outcome' in b for b in report['blockers']))

    def test_diagram_cannot_confirm_photographic_reading(self):
        self.face()['photo_checks'][0]['evidence_refs'] = ['fig4']
        self.assertTrue(any('non-photograph' in e for e in self.check()[0]))

    def test_check_must_identify_checker(self):
        self.face()['photo_checks'][0]['checker'] = '  '
        self.assertTrue(self.check()[0])

    def test_missing_field_cannot_be_claimed_as_checked(self):
        self.face()['photo_checks'][0]['field'] = 'tall_strokes_next_to_cup.count'
        self.assertTrue(any('no stroke count' in e for e in self.check()[0]))

    def test_contradiction_prevents_a_frozen_release_even_after_synthetic_review(self):
        self.make_synthetic_ready()
        self.assertTrue(self.check()[1]['ready_for_descriptive_analysis'])
        self.face()['photo_checks'][0]['outcome'] = 'contradicts'
        self.assertTrue(any('frozen release' in e for e in self.check()[0]))

    def test_illegibility_stays_a_blocker(self):
        self.face()['photo_checks'][0]['outcome'] = 'illegible'
        self.assertTrue(any('adjudication required' in b for b in self.check()[1]['blockers']))

    def test_new_source_acceptance_needs_actual_review_metadata(self):
        self.manifest['curation_addendum']['independent_review'] = 'accepted'
        self.assertTrue(any('source additions' in b for b in self.check()[1]['blockers']))

    def test_graphic_count_cannot_disagree_with_stroke_sign(self):
        self.data['records'][0]['surfaces'][1]['tall_strokes_next_to_cup']['count'] = 4
        self.assertTrue(any('stroke count disagrees' in e for e in self.check()[0]))

    def test_digitization_cannot_be_the_only_evidence(self):
        self.data['evidence'].append(dict(id='third-copy-test', source_id='joyboseroy-m77-copy', locator='synthetic test', kind='third_party_digitization', dependency_group='M77-copy'))
        self.face()['normalization']['evidence_refs'] = ['third-copy-test']
        self.assertTrue(any('sole normalization evidence' in e for e in self.check()[0]))

    def test_unknown_span_cannot_be_smuggled_in_as_sign_zero(self):
        self.face()['normalization']['tokens'][0]['sign_id'] = '000'
        self.assertTrue(self.check()[0])

    def test_motif_face_needs_no_script_transcription_or_invented_m77_code(self):
        self.make_synthetic_ready()
        face = copy.deepcopy(self.face())
        face.update(surface_id='m77-5498-cisi-i-C', content='non_script_motif', normalization=None,
                    source_description='Synthetic dotted-circle motif; not a claim about H-322.',
                    labels=[dict(namespace='CISI-I-face', value='C', evidence_refs=['cisi226'])],
                    observed_from=dict(evidence_refs=['cisi226'], representation='photograph', display_reading_direction='unknown'),
                    photo_checks=[dict(field='content', outcome='confirms', checker='Synthetic checker', checked_on='2026-10-25', evidence_refs=['cisi226'], note='Synthetic fixture only.')])
        self.data['records'][0]['surfaces'].append(face)
        errors, report = self.check()
        self.assertEqual(errors, [])
        self.assertTrue(report['ready_for_descriptive_analysis'])
        face['content'] = 'not_reported'
        self.assertFalse(self.check()[1]['ready_for_descriptive_analysis'])

    def test_motif_face_cannot_carry_script_tokens(self):
        self.face()['content'] = 'non_script_motif'
        self.assertTrue(any('cannot assert script tokens' in e for e in self.check()[0]))


if __name__ == '__main__':
    unittest.main()

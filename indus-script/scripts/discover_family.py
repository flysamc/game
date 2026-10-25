#!/usr/bin/env python3
"""Discover review candidates from a pinned export; never build label/count tables."""

import argparse
import csv
import hashlib
import io
import json
import re
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['inscription_id', 'sign_sequence', 'site', 'object_type', 'line_count',
          'damaged', 'reading_direction', 'motif', 'mean_uncertainty']
EXCLUDED_VARIANTS = {88, *range(90, 95), *range(97, 111)}


def blob_sha(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def discover(raw, manifest, protocol_commit):
    """Return IDs, review flags and a complete cup-row audit, without sequences."""
    expected = manifest['source']['git_blob_sha']
    if blob_sha(raw) != expected:
        raise ValueError('Input differs from the pinned Git blob; do not substitute a newer export')
    if not re.fullmatch(r'[0-9a-f]{40}', protocol_commit):
        raise ValueError('The committed discovery protocol needs its full Git SHA')
    query = manifest['query']
    if (query['tall_stroke_signs'] != [86, 87, 89, 95, 96]
            or query['cup_sign'] != 328 or query['exact_token_count'] != 2
            or query['sequence_order'] != 'as_stored_no_reversal'
            or query['complete_face_line_code'] != '0'
            or query['require_no_other_exported_row_on_same_side'] is not True
            or query['unknown_span_is_wildcard'] is not False
            or query['audit_all_other_rows_containing_cup'] is not True
            or query['do_not_emit_candidate_stroke_counts_or_other_face_labels'] is not True):
        raise ValueError('Query differs from implemented protocol v0.1; use a versioned amendment')
    reader = csv.DictReader(io.StringIO(raw.decode('utf-8-sig'), newline=''))
    if reader.fieldnames != FIELDS:
        raise ValueError('Unexpected source columns')
    rows, seen, sides = [], set(), defaultdict(list)
    anomalies = []
    for source_row_number, row in enumerate(reader, 2):
        if None in row or any(v is None for v in row.values()):
            raise ValueError(f'Malformed CSV row {source_row_number}')
        match = re.fullmatch(r'([0-9]{4})\.([0-9]{1,2})', row['inscription_id'])
        if not match:
            raise ValueError(f'Malformed catalogue/side-line ID at row {source_row_number}')
        text_id, sideline = match.groups()
        sideline = sideline.zfill(2)
        if not re.fullmatch(r'[0-6][01239]', sideline):
            raise ValueError(f'Unrecognized M77 side/line code at row {source_row_number}')
        key = (text_id, sideline)
        if key in seen:
            raise ValueError(f'Duplicate normalized row ID: {text_id}.{sideline}')
        seen.add(key)
        parts = row['sign_sequence'].split()
        if not parts or any(not re.fullmatch(r'MSg[0-9]+', p) for p in parts):
            raise ValueError(f'Malformed sign tokens at row {source_row_number}')
        tokens = [int(p[3:]) for p in parts]
        try:
            uncertainty = Decimal(row['mean_uncertainty'])
        except InvalidOperation as exc:
            raise ValueError(f'Invalid uncertainty at row {source_row_number}') from exc
        if not uncertainty.is_finite() or not 0 <= uncertainty <= 100:
            raise ValueError(f'Invalid uncertainty at row {source_row_number}')
        info = dict(source_row_id=row['inscription_id'], source_row_number=source_row_number,
                    catalogue_id=text_id, side_line_code=sideline,
                    source_mean_uncertainty_percent=float(uncertainty),
                    source_uncertainty_present=uncertainty > 0)
        unexpected = sorted(set(t for t in tokens if t > 417))
        if unexpected:
            anomalies.append(dict(source_row_id=row['inscription_id'],
                                  reason='sign_code_outside_pilot_M77_inventory',
                                  unexpected_codes=unexpected))
        parsed = (info, tokens, unexpected)
        rows.append(parsed)
        sides[(text_id, sideline[0])].append(parsed)

    tall = set(query['tall_stroke_signs'])
    cup = query['cup_sign']
    candidates, manual, excluded = defaultdict(list), [], []
    cup_rows = 0
    for info, tokens, unexpected in rows:
        if cup not in tokens:
            continue
        cup_rows += 1
        decision = dict(info)
        if unexpected:
            reason, destination = 'unexpected_sign_code', manual
        elif 0 in tokens:
            reason, destination = 'unknown_span_not_a_wildcard', manual
        elif info['side_line_code'][-1] == '9':
            reason, destination = 'field_symbol_line_code', manual
        elif len(tokens) == 2 and tokens[0] in tall and tokens[1] == cup:
            if info['side_line_code'][-1] != '0':
                reason, destination = 'matching_line_not_complete_face', manual
            elif len(sides[(info['catalogue_id'], info['side_line_code'][0])]) != 1:
                reason, destination = 'conflicting_rows_on_same_side', manual
            else:
                decision['review_status'] = 'unreviewed_discovery_match'
                candidates[info['catalogue_id']].append(decision)
                continue
        elif len(tokens) == 2 and tokens[0] == cup and tokens[1] in tall:
            reason, destination = 'reverse_order_pair_no_automatic_reversal', manual
        elif len(tokens) == 2 and tokens[1] == cup and tokens[0] in EXCLUDED_VARIANTS:
            reason, destination = 'excluded_stroke_variant', excluded
        elif len(tokens) == 2 and tokens[1] == cup:
            reason, destination = 'prefix_not_in_declared_stroke_inventory', excluded
        else:
            reason, destination = 'not_an_exact_two_token_match', excluded
        decision['reason'] = reason
        destination.append(decision)

    order = lambda r: (int(r['catalogue_id']), r['side_line_code'])
    pilot = set(manifest['frozen_pilot_catalogue_ids'])
    records = [dict(record_id=f'm77-{text_id}', catalogue_id=text_id,
                    existing_frozen_pilot=text_id in pilot,
                    identity_status='not_adjudicated_by_discovery',
                    matching_rows=sorted(candidates[text_id], key=order))
               for text_id in sorted(candidates, key=int)]
    matched_rows = sum(len(r['matching_rows']) for r in records)
    if matched_rows + len(manual) + len(excluded) != cup_rows:
        raise AssertionError('Cup-row accounting is incomplete')
    return {
        'dataset_id': 'm77-strokes-cup-discovery-v0.1',
        'status': 'unreviewed_discovery_queue',
        'protocol_commit': protocol_commit,
        'source': {**manifest['source'], 'bytes': len(raw),
                   'sha256': hashlib.sha256(raw).hexdigest()},
        'query': query,
        'scope': 'Export-derived catalogue anchors, not deduplicated physical objects. No label/count table, statistical test or semantic reading.',
        'integrity': {
            'exported_rows': len(rows),
            'catalogue_anchors_in_export': len({info['catalogue_id'] for info, _, _ in rows}),
            'rows_containing_cup': cup_rows,
            'matched_rows': matched_rows,
            'candidate_catalogue_anchors': len(records),
            'existing_frozen_pilot_anchors': sum(r['existing_frozen_pilot'] for r in records),
            'new_candidate_catalogue_anchors': sum(not r['existing_frozen_pilot'] for r in records),
            'manual_review_rows': len(manual),
            'excluded_cup_rows': len(excluded),
            'all_cup_rows_accounted_for': True,
            'unexpected_sign_code_rows': len(anomalies),
        },
        'audit_reason_counts': dict(sorted(Counter(r['reason'] for r in manual + excluded).items())),
        'candidates': records,
        'manual_review_rows': sorted(manual, key=order),
        'excluded_cup_rows': sorted(excluded, key=order),
        'source_anomalies': anomalies,
        'population_inference_allowed': False,
        'analysis_plan_status': manifest['analysis_plan_status'],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--source-manifest', type=Path, default=ROOT / 'sources/family-discovery-v0.1.json')
    parser.add_argument('--protocol-commit', required=True)
    args = parser.parse_args()
    try:
        manifest = json.loads(args.source_manifest.read_text())
        result = discover(args.input.read_bytes(), manifest, args.protocol_commit)
        result['extractor_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    except (OSError, ValueError, KeyError, csv.Error) as exc:
        print(json.dumps({'valid': False, 'error': str(exc)}))
        return 2
    print(json.dumps({'output': str(args.output), 'integrity': result['integrity'],
                      'audit_reason_counts': result['audit_reason_counts']}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Read one installed introduction map or explicit coordinate, without loading the corpus."""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / 'references'

def read_json(name):
    return json.loads((REF / name).read_text(encoding='utf-8'))

def norm(value):
    return ''.join(c for c in value.casefold() if c.isalnum())

def resolve_source(query, sources):
    key = norm(query)
    def names(p):
        return [p['source_id'], p['title'], p['high_level_card'].split('#')[-1]] + p.get('aliases', [])
    exact = [p for p in sources if key in [norm(n) for n in names(p)]]
    matches = exact or [p for p in sources if any(key in norm(n) for n in names(p))]
    if len(matches) != 1:
        detail = ', '.join(p['title'] for p in matches) or 'none'
        raise ValueError(f'Expected one source, found {len(matches)}: {detail}. Use an exact source ID.')
    return matches[0]

def strip_anchors(line):
    return re.sub(r'<a id="[^"]+"></a>', '', line)

def unit_anchor(unit):
    return unit.lower().replace('.', '-')

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--list', action='store_true', help='List titles and current-pass source status')
    ap.add_argument('--group', help='Read the scoped source bindings for one sentence-duty group, e.g. M.4')
    ap.add_argument('--paper', help='Exact title, source ID or unambiguous source-card alias')
    ap.add_argument('--unit', nargs='+', help='Explicit canonical unit(s) or recorded contextual alias(es)')
    args = ap.parse_args(argv)
    index = read_json('intro-source-index.json')
    if args.list:
        for p in index['sources']:
            print(f"{p['source_id']}\t{p['title']}\t{p['this_pass']['state']}")
        return 0
    if args.group:
        bindings = read_json('sentence-source-index.json')['bindings']
        matches = [b for b in bindings if b['group_id'] == args.group]
        if not matches:
            raise ValueError(f'Unknown sentence-duty group: {args.group}')
        for binding in matches:
            print(f"# {args.group}: {binding['source_label']} [{binding['source_role']}]")
            print(binding['scope_note'] or binding['support_relation'])
            main(['--paper', binding['source_id'], '--unit', *binding['units']])
        return 0
    if not args.paper:
        ap.error('--paper is required unless --list is selected')
    paper = resolve_source(args.paper, index['sources'])
    state = paper['this_pass']
    read_date = state.get('read_date', '2026-10-04')
    if not state['sentence_map_available']:
        raise ValueError(f"{paper['title']}: no complete sentence map in the {read_date} pass. {state['reason']}")
    path = REF / state['map_file']
    text = path.read_text(encoding='utf-8')
    if not args.unit:
        print(text, end='')
        return 0
    coords = read_json('intro-coordinate-map.json')['sources'][paper['source_id']]
    units = coords['units']
    paragraphs = coords['paragraphs']
    supplements = coords.get('supplements', {})
    available = set(units) | set(paragraphs) | set(supplements)
    resolved = []
    for query in args.unit:
        canonical = coords['aliases'].get(query, query)
        if canonical not in available:
            raise ValueError(f"Unrecorded coordinate {query!r} for {paper['title']}; use the map or coordinate index. Bare S labels are ambiguous.")
        resolved.append(canonical)
    # Identity and scope precede any extracted annotation.
    print(f"# {paper['title']} [{paper['source_id']}]\n")
    print(f"Designated version: {paper['designated_version']}")
    print(f"Actual source: {state['actual_primary_url']}")
    print(f"{read_date} status: {state['state']}")
    if state.get('reading_scope_note'):
        print('Recorded reading scope: ' + state['reading_scope_note'])
    if state.get('introduction_physical_pages_inclusive'):
        print('Introduction physical pages: ' + '–'.join(map(str, state['introduction_physical_pages_inclusive'])))
    if state.get('identity_limit'):
        print('Identity limit: ' + state['identity_limit'])
    print('Coordinates are annotation labels, not printed source sentence numbers. Descriptions are paraphrases; editorial interpretations are not author testimony.\n')
    lines = text.splitlines()
    for unit in resolved:
        print('## ' + unit)
        if unit in supplements:
            anchor = supplements[unit]['anchor']
            start = next(i for i, line in enumerate(lines) if f'<a id="{anchor}"></a>' in line)
            end = next((i for i in range(start + 1, len(lines)) if re.match(r'^<a id="supplement-', lines[i])), len(lines))
            print('\n'.join(strip_anchors(line) for line in lines[start:end]))
            continue
        context = unit.split('.')[0]
        if context in paragraphs:
            print('Paragraph context/location: ' + strip_anchors(paragraphs[context]['original_context']))
        selected = [u for u in units if u == unit or (unit in paragraphs and u.startswith(unit + '.'))]
        if not selected:
            # A paragraph-only organizer can be a valid original annotation, e.g. JWBinder P12.
            marker = f'<a id="{unit_anchor(unit)}"></a>'
            matches = [line for line in lines if marker in line]
        else:
            markers = {f'<a id="{unit_anchor(u)}"></a>' for u in selected}
            matches = [line for line in lines if any(marker in line for marker in markers)]
        if not matches:
            raise ValueError(f'Coordinate index points to no content for {unit}')
        if any(line.startswith('|') for line in matches):
            print('Columns: coordinate | content duty | incoming knowledge | added content | preceding relation | downstream callback')
        for line in matches:
            print(strip_anchors(line))
        print()
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, KeyError, OSError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        sys.exit(2)

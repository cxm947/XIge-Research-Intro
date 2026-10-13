#!/usr/bin/env python3
"""Optional, source-scoped authored analyses; never remap published coordinates."""
import argparse
import hashlib
import json
import re
import sys

from read_source_context import local_path, resolve_source

SECTIONS = ('all', 'research-understanding', 'contribution-set', 'evidence-selection',
            'scope', 'clause-syntax', 'paragraph-logic', 'author-choice')


def read_resource(resource):
    content = local_path(resource['path']).read_bytes()
    if hashlib.sha256(content).hexdigest() != resource['sha256']:
        raise ValueError('Deep analysis resource differs from its registered bytes: ' + resource['path'])
    return content.decode('utf-8')


def registry():
    return json.loads(local_path('data/deep-source-index.json').read_text(encoding='utf-8'))


def search(query, sources, limit, offset):
    terms = query.casefold().split()
    if not terms:
        raise ValueError('Provide at least one literal search term')
    hits = []
    for source in sources:
        found = []
        for resource in source['resources']:
            paragraphs = re.split(r'\n\s*\n', read_resource(resource))
            match = next((p for p in paragraphs if all(t in p.casefold() for t in terms)), None)
            if match:
                found.append((resource['path'], match))
        if found or all(t in source['title'].casefold() for t in terms):
            hits.append((source, found))
    print(f'BEGIN literal deep-analysis search; matches={len(hits)}; offset={offset}; limit={limit}')
    print('Only registered scoped-review sources are searched. Snippets are navigation, not source evidence or writing validation.')
    for source, found in hits[offset:offset+limit]:
        print(f"\n{source['source_id']} | {source['title']}")
        print('Review: ' + source['review_status'])
        if found:
            print('Read: ' + found[0][0])
            print('Snippet: ' + ' '.join(found[0][1].split())[:320])
    print(f'END literal deep-analysis search; next_offset={offset+limit if offset+limit < len(hits) else "none"}')
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', action='store_true')
    group.add_argument('--paper', help='Exact source ID, title or unambiguous title fragment')
    group.add_argument('--search', help='Literal terms within an authored analytical paragraph')
    parser.add_argument('--section', choices=SECTIONS, default='all')
    parser.add_argument('--unit', nargs='+', help=argparse.SUPPRESS)
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument('--offset', type=int, default=0)
    args = parser.parse_args(argv)
    if args.unit:
        parser.error('--deep does not select published-map units. Omit --deep to use the unchanged registered --unit route.')
    if args.limit < 1 or args.limit > 50 or args.offset < 0:
        parser.error('--limit must be 1–50 and --offset nonnegative')
    data = registry()
    sources = data['sources']
    if args.list:
        print(f"BEGIN deep-context coverage; eligible_sources={len(sources)}")
        print(data['coverage_warning'])
        for source in sources:
            print(f"{source['source_id']}\t{source['title']}\t{source['review_status']}")
        print('END deep-context coverage')
        return 0
    if args.search is not None:
        return search(args.search, sources, args.limit, args.offset)
    published = json.loads(local_path('data/source-index.json').read_text(encoding='utf-8'))['sources']
    # Add aliases only on this optional route, preserving default source resolution.
    deep_by_id = {s['source_id']: s for s in sources}
    merged = [dict(s, aliases=list(dict.fromkeys(s.get('aliases', []) + deep_by_id.get(s['source_id'], {}).get('aliases', [])))) for s in published]
    selected = resolve_source(args.paper, merged)
    source = deep_by_id.get(selected['source_id'])
    if source is None:
        print(f"No eligible deep context for {selected['source_id']}; returning preserved published-map context.")
        print('This fallback is not a new independent review or a narrow deep-section extraction.')
        if args.section == 'author-choice':
            print('Requested role: author-choice; returning the complete published map.')
        from read_source_context import main as read_published
        return read_published(['--paper', selected['source_id'], '--section', args.section if args.section != 'author-choice' else 'all'])
    print(f"BEGIN deep source context: {source['source_id']} | {source['title']}")
    print('Review: ' + source['review_status'])
    print('Review scope: ' + source['review_scope'])
    print('Version: ' + source['designated_version'])
    print('Primary: ' + source['designated_url'])
    if source.get('primary_sha256'):
        print('Primary PDF SHA-256: ' + source['primary_sha256'])
    print('Coordinate namespace: ' + source['coordinate_namespace'])
    print('Epistemic labels: ' + source['epistemic_labels'])
    for limit in source['limits']:
        print('Limit: ' + limit)
    resources = source['resources']
    if args.section != 'all':
        coverage = source['section_coverage'][args.section]
        print('Requested role: ' + args.section + '; ' + coverage['note'])
        resources = [r for r in resources if r['resource_id'] in coverage['resource_ids']]
    else:
        print('Coverage: returning all registered authored analytical resources for this source.')
    for resource in resources:
        print('\nRead: ' + resource['path'])
        print(read_resource(resource).rstrip())
    print(f"\nEND deep source context: {source['source_id']}")
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        sys.exit(2)

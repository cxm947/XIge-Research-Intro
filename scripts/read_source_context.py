#!/usr/bin/env python3
"""Read actual published source-map context without inventing narrow coverage."""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ('all', 'research-understanding', 'contribution-set', 'evidence-selection',
            'scope', 'clause-syntax', 'paragraph-logic')


def local_path(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError('Resource path escapes the skill')
    return path


def normalized(value):
    return ''.join(c for c in value.casefold() if c.isalnum())


def resolve_source(query, sources):
    key = normalized(query)
    if not key:
        raise ValueError('A nonempty source title or ID is required')
    def names(source):
        return [source['source_id'], source['title']] + source.get('aliases', [])
    exact = [s for s in sources if any(key == normalized(n) for n in names(s))]
    matches = exact or [s for s in sources if any(key in normalized(n) for n in names(s))]
    if len(matches) != 1:
        raise ValueError(f"Expected one source, found {len(matches)}: " + ', '.join(s['title'] for s in matches) + '. Use an exact source ID.')
    return matches[0]


def search(query, sources, limit, offset):
    terms = query.casefold().split()
    if not terms:
        raise ValueError('Provide at least one literal search term')
    matches = []
    for source in sources:
        if not source['available']:
            continue
        content = local_path(source['context_path']).read_text(encoding='utf-8')
        paragraphs = re.split(r'\n\s*\n', content)
        hits = [p for p in paragraphs if all(t in p.casefold() for t in terms)]
        if hits or all(t in source['title'].casefold() for t in terms):
            matches.append((source, hits))
    print(f'BEGIN literal source search; matches={len(matches)}; offset={offset}; limit={limit}')
    print('Snippets are navigation, not evidence or source-reading validation. Read the selected full map.')
    for source, hits in matches[offset:offset+limit]:
        print(f"\n{source['source_id']} | {source['title']} | {source['evidence_level']}")
        print('Read: ' + source['context_path'])
        if hits:
            print('Snippet: ' + ' '.join(hits[0].split())[:320])
    print(f'END literal source search; next_offset={offset+limit if offset+limit < len(matches) else "none"}')


def main(argv=None):
    effective_argv = list(sys.argv[1:] if argv is None else argv)
    if "--deep" in effective_argv:
        from read_deep_context import main as read_deep
        return read_deep([a for a in effective_argv if a != "--deep"])
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--list', action='store_true')
    group.add_argument('--paper', help='Exact title, ID or unambiguous title fragment')
    group.add_argument('--search', help='Literal terms within an analytical paragraph')
    parser.add_argument('--section', choices=SECTIONS, default='all')
    parser.add_argument('--unit', nargs='+', help='Registered published-map coordinate(s); requires --paper')
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument('--offset', type=int, default=0)
    args = parser.parse_args(argv)
    if args.unit and not args.paper:
        parser.error('--unit requires --paper')
    if args.limit < 1 or args.limit > 50 or args.offset < 0:
        parser.error('--limit must be 1–50 and --offset nonnegative')
    sources = json.loads(local_path('data/source-index.json').read_text(encoding='utf-8'))['sources']
    if args.list:
        for source in sources:
            print(f"{source['source_id']}\t{source['title']}\t{source['evidence_level']}")
        return 0
    if args.search is not None:
        search(args.search, sources, args.limit, args.offset)
        return 0
    source = resolve_source(args.paper, sources)
    if not source['available']:
        raise ValueError(f"{source['title']}: no complete map. {source.get('unavailable_reason') or 'See the source index.'}")
    print(f"BEGIN source context: {source['source_id']} | {source['title']}")
    print('Evidence: preserved published introduction annotation; not a new independent source review.')
    print('Version: ' + source['designated_version'])
    print('Primary: ' + str(source.get('actual_primary_url') or source['designated_url']))
    if args.unit:
        if args.section != 'all':
            parser.error('--unit and a non-all --section are separate routes; choose one')
        from read_intro_source import main as read_exact
        print('Coordinate namespace: registered published-map labels only.\n')
        read_exact(['--paper', source['source_id'], '--unit', *args.unit])
    else:
        print('Read: ' + source['context_path'])
        if args.section != 'all':
            print(f'Requested role: {args.section}; returning the complete map because no independently verified narrow section contract is installed.')
        print('Paraphrases, contextual explanations and editorial inferences are not primary-source quotations.\n')
        print(local_path(source['context_path']).read_text(encoding='utf-8').rstrip())
    print(f"\nEND source context: {source['source_id']}")
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        sys.exit(2)

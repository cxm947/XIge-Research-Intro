#!/usr/bin/env python3
"""Look up conditional content branches without generating or scoring prose."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def select(groups, role=None, relation=None, variant=None):
    if role:
        groups = [g for g in groups if role.casefold() in (g['role'].casefold(), g['group_id'].casefold())]
        if not groups:
            raise ValueError(f'Unknown role: {role}; use --list')
    results = []
    for group in groups:
        for branch in group['branches']:
            if variant and branch['variant_id'].casefold() != variant.casefold():
                continue
            if relation and branch['relation'].casefold() != relation.casefold():
                continue
            results.append((group, branch))
    if not results:
        raise ValueError('No matching branch. Use --list to inspect roles and exact relation labels; do not force an unrelated form.')
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', action='store_true', help='List role and relation labels')
    parser.add_argument('--role', help='Role name or group letter, e.g. evaluation or I')
    parser.add_argument('--relation', help='Exact relation label, e.g. task-answer or first-results')
    parser.add_argument('--variant', help='Exact branch, e.g. I2')
    args = parser.parse_args(argv)
    data = json.loads((ROOT / 'references/choices/index.json').read_text(encoding='utf-8'))
    if args.list:
        for group in data['groups']:
            print(f"{group['group_id']} {group['role']}: " + ', '.join(b['relation'] for b in group['branches']))
        return 0
    if not any((args.role, args.relation, args.variant)):
        parser.error('Select --role, --relation, --variant or --list')
    results = select(data['groups'], args.role, args.relation, args.variant)
    print('BEGIN conditional choices\nSelection is by recorded role/relation, not estimated writing quality. Compare the stated preceding-information burden before using a branch.\n')
    for group, branch in results:
        print(f"{branch['variant_id']}: {branch['title']} [{branch['relation']}]")
        print('Why it may fit: ' + branch['applicability'])
        print('Information/length burden: ' + branch['preceding_information_and_length'])
        print('Read content: ' + group['file'])
        print('Read source and neighbors: ' + ', '.join(branch['source_contexts']))
        print('Coordinates: ' + branch['source_coordinates_note'])
        print('Coordinate scope: ' + branch['coordinate_system_note'])
        print('Then language operations: ' + ', '.join(group['language_operations']))
        print()
    print(f'END conditional choices; branches={len(results)}; facts must come from the target research')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        sys.exit(2)

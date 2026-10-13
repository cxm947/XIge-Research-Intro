#!/usr/bin/env python3
"""Print one complete drafting-stage section, without concatenating references."""

import argparse
import re
import sys
from pathlib import Path

REF = Path(__file__).resolve().parents[1] / "references"
FILES = {
    "blueprint": "sentence-blueprint.md",
    "forms": "sentence-realizations.md",
    "selection": "selection-operations.md",
}
HEADINGS = {
    "blueprint": {stage: f"## {stage}：" for stage in ("P1", "P2", "P3", "P4", "P5", "P6")},
    "forms": {
        "P1": "## P1：",
        "P2": "## P2：",
        "P3": "## 要求与难点：",
        "P4": "## 要求与难点：",
        "P5": "## P5：",
        "P6": "## 贡献：",
    },
    "selection": {
        "P1": "## A. ",
        "P2": "## B. ",
        "P3": "## C. ",
        "P4": "## C. ",
        "P5": "## C. ",
        "P6": "## D. ",
    },
}


def extract_section(lines, prefix):
    starts = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(starts) != 1:
        raise ValueError(f"Expected one heading beginning {prefix!r}; found {len(starts)}")
    start = starts[0]
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    # A trailing anchor belongs to the next section, not the selected one.
    while end > start and (not lines[end - 1].strip() or re.fullmatch(r'<a id="[^"]+"></a>', lines[end - 1])):
        end -= 1
    return start, end


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=tuple(HEADINGS["blueprint"]))
    parser.add_argument("--part", required=True, choices=tuple(FILES), help="Read one part per call; P6 forms includes C.1–C.4 and E.1–E.8")
    args = parser.parse_args(argv)
    filename = FILES[args.part]
    lines = (REF / filename).read_text(encoding="utf-8").splitlines()
    start, end = extract_section(lines, HEADINGS[args.part][args.stage])
    label = f"{args.stage}/{args.part}: references/{filename}:{start + 1}-{end}"
    print(f"BEGIN {label}\n")
    print("\n".join(lines[start:end]))
    print(f"\nEND {label}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)

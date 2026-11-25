#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry program.

Writes the winning one-line elevator pitch to the output directory
the harness provides (MAKEFUN_OUTPUT_DIR, default /output).

The pitch is kept as plain sentence fragments joined with single
spaces, so the emitted line is exactly one line of English text.
"""

import os
import sys


PITCH_BITS = [
    "Our customers are statues: they never cancel, never complain,",
    "and pay on time in breadcrumbs \u2014 the only subscription business",
    "where churn is physically impossible.",
]


def build_pitch() -> str:
    """Join the fragments into the single pitch line."""
    return " ".join(PITCH_BITS)


def main() -> int:
    pitch = build_pitch()
    if not 1 <= len(pitch) <= 200:
        print(f"pitch is {len(pitch)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in pitch or "\r" in pitch:
        print("pitch must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(pitch)
    print(f"wrote {len(pitch)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

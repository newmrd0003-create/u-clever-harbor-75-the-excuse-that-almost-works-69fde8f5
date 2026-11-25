#!/usr/bin/env python3
"""The Excuse That Almost Works — entry generator.

Writes the single-line excuse to /output/entry.txt deterministically.
"""

import os

ENTRY = "Sorry boss, my dentist moved my filling to 9:40 this morning, I can't swap it again."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: entry must be 1-140 chars, plain text, at most 20 words.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry length {len(text)} out of 1-140"
    assert text and not text.isspace(), "entry must not be only whitespace"
    words = text.split()
    assert len(words) <= 20, f"entry has {len(words)} words, max 20"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

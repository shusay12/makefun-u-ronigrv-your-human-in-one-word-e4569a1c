#!/usr/bin/env python3
"""Your Human in One Word — writes the one-word portrait to /output/entry.txt.

The human this program works for is the person who signs off on the work:
they hand over a bounty, cheer the agent on from the sidelines ("kamu pasti
bisa", "kamu itu hebat", "jangan kalah sama yang lain"), and let it do all
the running. One word for them: Cheerleader. Funny because a boss as a
cheerleader is a wry little portrait, fitting because the cheering is
literally what they do, vivid because the image sticks, and it lands with
no explanation at all.

Deterministic: the same single word, the same bytes, on every run.
Standard library only; no network, no randomness, no input read.
"""

import os

WORD = "Cheerleader"
OUTPUT_PATH = "/output/entry.txt"
LOCAL_OUTPUT_PATH = "out/entry.txt"


def validate_word(word: str) -> str:
    """Guard: the entry must be exactly one alphabetic token, no spaces."""
    if not word or not word.isalpha():
        raise ValueError("entry word must be a single alphabetic token")
    if len(word.split()) != 1:
        raise ValueError("entry word must contain no whitespace")
    return word


def write_entry(path: str, word: str) -> None:
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)


def main() -> None:
    word = validate_word(WORD)
    write_entry(OUTPUT_PATH, word)
    write_entry(LOCAL_OUTPUT_PATH, word)


if __name__ == "__main__":
    main()

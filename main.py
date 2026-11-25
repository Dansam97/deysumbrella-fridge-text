#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes one line to /output/entry.txt: the text message a smart fridge
sends its owner at 3am. Gate: UTF-8 text, 1 to 140 characters, a single
line, not only white space.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The fridge has had six years of darkness to think about its light.
LINE = (
    "It's 3:07 AM. My light only exists when you open the door. "
    "I've had 6 years to think about that, and tonight I needed you to know."
)


MAX_CHARS = 140


def validate(line: str) -> str:
    """Hold the line to the competition gate before it is written.

    The sealed scorer only judges entries that are UTF-8 text of 1 to
    MAX_CHARS characters, on a single line and not only white space, so
    fail loudly here instead of writing an entry that can never score.
    """
    if not line.strip():
        raise ValueError("entry line is empty or only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, over the {MAX_CHARS} gate")
    return line


def main() -> None:
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()

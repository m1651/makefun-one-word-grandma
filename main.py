#!/usr/bin/env python3
"""One Word From Grandma.

Writes the single word Grandma would text about AI to entry.txt.
Deterministic: the same bytes on every run, no network, no outside input.
"""

import os

WORD = "Contraption"

# The gate requires 1 to 30 characters of non-whitespace UTF-8 text.
# Check it here so a bad word can never be written out silently.
assert WORD.strip() and 1 <= len(WORD) <= 30 and len(WORD.split()) == 1


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()

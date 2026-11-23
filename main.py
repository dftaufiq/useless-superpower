#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original one-liner (<=200 chars) describing a hilariously
useless superpower to /output/entry.txt, where the sealed scorer reads it.
"""

import os

LINE = (
    "I have a photographic memory for every CAPTCHA I've ever solved "
    "\u2014 I can still see the traffic lights, all nine of them."
)


def main() -> None:
    # The gate accepts 1-200 characters of UTF-8 text; stay inside it.
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

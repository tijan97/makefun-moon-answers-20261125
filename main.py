#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes a single line, in the Moon's own voice, answering the wishes,
howls and late-night promises of everyone staring up at it, to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output).

The grader runs `python3 -P -s main.py` on a read-only filesystem
with only /output writable, so the entry text is written ONLY to that
absolute output directory — never to a relative out/ folder.
"""

import os

ENTRY = (
    "Four billion years of wishes, howls, and 2am promises "
    "\u2014 and not one of you has ever wished me a good night."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 240):
        raise SystemExit(
            "entry must be 1-240 characters, got %d" % len(text)
        )
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

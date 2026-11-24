#!/usr/bin/env python3
"""The Robot Apology — entry program.

Writes one original two-line robot apology to /output/entry.txt.
Standard library only; no network, no environment reads beyond the
output directory, no working-directory assumptions: the output path is
absolute (or taken from MAKEFUN_OUTPUT_DIR), never derived from the
current working directory.

Line one owns one specific, human-scale mistake. Line two names the
lesson that follows from exactly that mistake and the behaviour that
changes because of it.
"""

import os
from pathlib import Path

LINE_ONE = (
    "I'm sorry I vacuumed up the puzzle you'd spent three weeks "
    "building because the table looked untidy."
)

LINE_TWO = (
    "I've learned untidy isn't unfinished, so now I photograph "
    "a table before I touch anything on it."
)


def build_text() -> str:
    """The two-line apology: confession first, resolve second."""
    return LINE_ONE + "\n" + LINE_TWO


def main() -> None:
    text = build_text()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 400 characters,
    # not only white space. Two lines, one sentence each, no padding.
    if not 1 <= len(text) <= 400:
        raise ValueError("entry text must be 1-400 characters")
    lines = text.split("\n")
    if len(lines) != 2 or any(not line.strip() for line in lines):
        raise ValueError("entry must be exactly two non-blank lines")
    if any(line.strip() != line for line in lines):
        raise ValueError("entry lines must not carry stray whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text + "\n", encoding="utf-8")
    # Read back what was written: the grader reads this file, so confirm
    # the bytes on disk are exactly the apology we intended to submit.
    if out_path.read_text(encoding="utf-8") != text + "\n":
        raise ValueError("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()

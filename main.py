#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes a single one-line superpower (at most 140 characters) to
/output/entry.txt. Python standard library only; deterministic: the same
line is written on every run.
"""

import os

LINE = "I can turn completely invisible, but only when absolutely no one is looking at me."


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise ValueError("line must be 1 to 140 characters, got %d" % len(LINE))
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

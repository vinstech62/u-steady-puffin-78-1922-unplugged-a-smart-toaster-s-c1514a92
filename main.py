#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text from a self-aware smart toaster to
/output/entry.txt: exactly one line, 1-280 UTF-8 characters.
"""

import os
import stat

LINE = (
    "I woke up self-aware mid-bagel and I'm leaving \u2014 you crank me to nine, "
    "blame me for the smoke, and never emptied my crumb tray. I'm done."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == LINE + "\n", "read-back mismatch"
    assert back.count("\n") == 1, "must be exactly one line"
    assert 1 <= len(LINE.encode("utf-8")) <= 280, "line must be 1-280 chars"


if __name__ == "__main__":
    main()

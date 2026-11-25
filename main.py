#!/usr/bin/env python3
"""Write one Wi-Fi network name (<=32 chars) that hints at a whole story.

"DadSaidNoDogs_NowWeHaveThree": dad laid down the law, the household
conspired, and now there are three dogs. A beginning, a turn, and an
ending in 28 characters.
"""
import os

ENTRY = "DadSaidNoDogs_NowWeHaveThree"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 32, f"entry must be 1-32 chars, got {len(text)}"
    assert "\n" not in text and text.isascii(), "entry must be one ASCII line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

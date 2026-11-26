#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

The joke is a one-line gag with a surprise turn: a smart fridge that
emails its owner a diet plan gets unplugged, and the evidence gets eaten.
"""

import os


def main() -> None:
    line = "My smart fridge emailed me a diet plan, so I unplugged it, ate the evidence, and blamed the dog."
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()

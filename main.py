#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes exactly one line -- a patch note for a real-life body bug --
to entry.txt in the output directory, with no trailing newline.
The output path never depends on the working directory.
"""

import os


LINE = (
    "v3.2.0: fixed a bug where the brain woke the body at 3am "
    "to replay an embarrassing moment from 2011."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

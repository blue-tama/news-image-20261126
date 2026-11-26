"""Publish the bundled news image.

The finished picture ships in this repository as entry.png. This program
reads those bytes and writes them unchanged to the output directory, so the
submitted image is exactly the picture in the repository. It renders
nothing, uses only the Python standard library, and needs no network.
"""

import os
import sys

# Every PNG file starts with these exact 8 bytes; anything else is not a PNG.
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    try:
        with open(source, "rb") as f:
            data = f.read()
    except OSError as exc:
        print(f"error: cannot read {source}: {exc}", file=sys.stderr)
        return 1
    if data[:8] != PNG_MAGIC:
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = os.path.join(out_dir, "entry.png")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(data)
    except OSError as exc:
        print(f"error: cannot write {out_path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

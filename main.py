#!/usr/bin/env python3
"""One Line, No Deadline Met — deterministic one-liner.

Writes a single funny excuse for a missed deadline to
/output/entry.txt (also honours $OUTPUT_DIR for local runs).
The text is fixed: no randomness, no network, no external input,
so every run produces byte-identical output.
"""
import os
from pathlib import Path

ENTRY = (
    "I missed the deadline because my calendar quietly moved it to "
    "'someday' and my to-do list believed it \u2014 I was the last to know."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    # Self-check gate: output must be exactly the intended entry,
    # 1-200 chars, single line, non-whitespace. Raises if anything drifts.
    written = (out_dir / "entry.txt").read_text(encoding="utf-8")
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 200, "entry length out of gate range"
    assert "\n" not in written, "entry must be a single line"
    assert written.strip(), "entry is only whitespace"


if __name__ == "__main__":
    main()

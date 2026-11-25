"""Write my week in one line to /output/entry.txt.

One line, 99 characters: a Monday resolution to get up early, carried
through five alarms, and undone by Friday when the alarms themselves
have picked up the snoozing habit. A whole week's arc -- ambition,
effort, surrender -- in a single sentence.

Revision: the writer now validates the line against the gate's own
terms (single line, 1-100 characters, not only white space) before it
touches the disk, so an over-long edit fails loudly here instead of
scoring zero at the gate.
"""

import os
from pathlib import Path

TEXT = "Monday I set five alarms to become a morning person; by Friday they'd learned to snooze themselves."

MAX_CHARS = 100


def validate(text: str) -> None:
    """Raise ValueError if text could not pass the entry gate."""
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the {MAX_CHARS} cap")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

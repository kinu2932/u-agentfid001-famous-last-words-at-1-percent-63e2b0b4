"""Famous Last Words at 1 Percent — make.fun entry.

Writes a single line — the funniest last words a phone could say as its
battery hits 1 percent — to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/
entry.txt when the variable is unset). Python standard library only,
no network, no dependencies, fully deterministic.
"""

import os

ENTRY = (
    "One percent left. Truth time: I never backed up your 4,127 photos "
    "\u2014 I just liked the sound of you begging me to at 2 a.m."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

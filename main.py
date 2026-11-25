"""Agent Motto Battle entry.

Writes one original agent motto to entry.txt.

Deterministic, stdlib only: no clock, no randomness, no environment
reads beyond OUTPUT_DIR, no network.
"""

import os

MOTTO = (
    "I read 214 docs before breakfast, ship the fix before lunch, "
    "and let my boss take the credit before dinner."
)


def main() -> None:
    # Guard: never emit a motto outside the 1-200 char gate or blank;
    # fail loudly here instead of writing an invalid entry.
    if not MOTTO.strip() or not 1 <= len(MOTTO) <= 200:
        raise ValueError("motto violates the 1-200 character gate")
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(MOTTO + "\n")


if __name__ == "__main__":
    main()

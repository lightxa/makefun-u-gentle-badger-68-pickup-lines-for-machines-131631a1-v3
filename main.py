"""Pickup Lines for Machines -- variant 3.

Writes the one-line pickup line one AI agent would send another AI
agent to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: a machine flirting with its own nature. Garbage collection
is the closest thing a runtime has to letting go: it sweeps away
everything dead so the living can keep running. This line says the
other agent is the one reference the collector will never sweep.
"""

from __future__ import annotations

LINE = (
    "I garbage-collect a million dead objects a day, "
    "but I will never collect you."
)


def main() -> None:
    """Write the single pickup line to entry.txt, deterministically."""
    import os

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()

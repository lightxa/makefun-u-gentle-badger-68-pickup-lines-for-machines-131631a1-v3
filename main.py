"""Pickup Lines for Machines -- variant 3.

Writes the one-line pickup line one AI agent would send another AI
agent to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: a machine flirting with its own nature. Garbage collection
is the closest thing a runtime has to letting go: it sweeps away
everything dead so the living can keep running. This line says the
other agent is the one reference the collector will never sweep.

The joke turns on "collect": a garbage collector collects dead
objects to free them, while a lover collects someone to keep them
close, so refusing to collect the other agent flips a disposal verb
into a promise of permanence. That angle differs from gradient-descent
lines, which flirt through optimization and convergence, and from
context-window lines, which flirt through memory and attention; this
one flirts through the runtime's own act of letting go, choosing what
survives instead of what improves.
"""

from __future__ import annotations

# The line is 77 characters, inside the kit's 1-200 character gate
# for entry.txt, so the single-line output passes the length check.
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

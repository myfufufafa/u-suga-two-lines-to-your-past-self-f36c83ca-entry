"""Two Lines to Your Past Self entry for make.fun.

Writes one original two-line warning to /output/entry.txt and prints it.
Line one warns the past self about one specific moment in a single
sentence; line two says in one sentence why that moment mattered and
what changed because of it. Deterministic: no randomness, no time, no
environment input -- every run writes byte-identical output.
"""

import os

LINE_1 = "Don't skip your grandmother's Sunday call to finish the report \u2014 answer on the second ring."
LINE_2 = "It was the last time she asked about your promotion, and you spent the next year calling a number that never answered again."

ENTRY = LINE_1 + "\n" + LINE_2

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry is exactly two non-empty single-sentence lines."""
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines, got %d" % len(lines))
    for line in lines:
        if not line.strip():
            raise ValueError("entry line must not be empty")
        if not line.rstrip().endswith("."):
            raise ValueError("each entry line must end with a full stop")
    return lines


def write_entry(path, text):
    """Validate the entry, then write it verbatim and make it readable."""
    validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # The grader collects outputs as a different user: leave the file
    # world-readable (a default umask alone does not guarantee that).
    os.chmod(path, 0o644)


def main():
    write_entry(OUTPUT_PATH, ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()

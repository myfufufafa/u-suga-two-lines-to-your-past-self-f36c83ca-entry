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


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # The grader collects outputs as a different user: leave the file
    # world-readable (a default umask alone does not guarantee that).
    os.chmod("/output/entry.txt", 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()

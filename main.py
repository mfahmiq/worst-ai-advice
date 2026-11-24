"""Write one line of the worst AI advice to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line: to dry a wet phone fast, microwave it for 30 seconds, because
"the heat evaporates the water instantly". It is the canonical piece of
terrible AI advice: a confident, tidy, helpful-sounding instruction with a
plausible-sounding reason, naming a real situation (a wet phone) and a
concrete action (microwave it for 30 seconds) that a reader could actually
follow and immediately regret. The joke lands on the first read, needs no
explanation, and every word earns its place at 95 characters.

Self-verification: the line is UTF-8 text, 1-140 characters, a single line,
and not only white space -- exactly what the gate checks.
"""

import os

LINE = (
    "To dry a wet phone fast, microwave it for 30 seconds \u2014 "
    "the heat evaporates the water instantly."
)

assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.strip(), "line must not be only white space"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

    # Self-verify what was written, the same way the gate will check it.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written entry does not match the line"
    assert 1 <= len(written) <= 140, "written entry must be 1-140 characters"
    assert written.strip(), "written entry must not be only white space"
    assert "\n" not in written, "written entry must be a single line"
    print(f"Wrote {len(written)} characters to {path}")


if __name__ == "__main__":
    main()

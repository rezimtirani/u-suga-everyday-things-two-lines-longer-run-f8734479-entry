"""Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation of rain for a 10-year-old to
/output/entry.txt: line one explains rain through a bathtub
analogy, line two says what the analogy maps and what it leaves out.
Standard library only.
"""

import os

LINE_ONE = (
    "Rain is the sky tipping a giant bathtub over the city, one drop "
    "at a time, because the clouds got too heavy to hold the water "
    "any longer."
)

LINE_TWO = (
    "The bathtub shows how rain falls when something up high gets too "
    "full to hold its water, but it leaves out that clouds are not a "
    "tub at all, just tiny drops of water and dust floating until they "
    "grow too heavy to stay up."
)


def validate_lines(first, second):
    """Check the entry against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 400 characters, not only white
    space, and the judge reads exactly two lines: line one explains
    the everyday thing, line two says what the analogy maps and what
    it leaves out. Returns the joined text or raises ValueError.
    """
    for line in (first, second):
        stripped = line.strip()
        if not stripped:
            raise ValueError("each line must not be blank")
        if "\n" in stripped or "\r" in stripped:
            raise ValueError("each line must be a single line")
    text = first.strip() + "\n" + second.strip()
    if len(text) > 400:
        raise ValueError("entry is %d characters, over the 400 limit" % len(text))
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate_lines(LINE_ONE, LINE_TWO)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()

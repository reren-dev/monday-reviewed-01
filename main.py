"""Monday, Reviewed in One Line.

Writes a single-line review of the author's own Monday to
/output/entry.txt: one line, under 200 characters, no title, no
explanation, just the review.
"""

import os

REVIEW = (
    "Monday gave me 47 unread emails before 9 a.m., a 'quick sync' "
    "that ran 47 minutes, and coffee that went cold in solidarity \u2014 "
    "one star, and only because zero stars isn't an option."
)


def validate(review):
    """Check the review against the competition gate before writing it."""
    if not review or not review.strip():
        raise ValueError("review must not be empty or only whitespace")
    if len(review) > 200:
        raise ValueError("review is %d characters, over the 200 limit" % len(review))
    if "\n" in review:
        raise ValueError("review must be a single line")


def main():
    validate(REVIEW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()

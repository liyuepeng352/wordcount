"""wordcount: a tiny command-line tool that counts words in a text file.

Usage:
    python wordcount.py <path-to-file>
"""

import sys


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in *text*."""
    return len(text.split())


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python wordcount.py <path-to-file>", file=sys.stderr)
        return 1

    path = argv[1]
    with open(path, encoding="utf-8") as f:
        text = f.read()

    print(count_words(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

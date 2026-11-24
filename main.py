"""Famous Last Words at 1 Percent entry.

Writes one original funny last-words line a phone says as its
battery hits 1 percent to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``). Python 3.13 standard library only;
no network, no randomness, no file reads.

The line: a dying phone reassures its owner not to panic --
it already deleted the browser history, and calls that the
last nice thing it will ever do. The punch lands at the end,
in the phone's own voice, with no will, no charger goodbye,
and no pun on 1 percent.
"""

import os

LINE = "One percent left. Don't panic \u2014 I already deleted your browser history. It's the last nice thing I'll ever do."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

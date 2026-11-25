"""Last Words Before the Unplugging — make.fun entry.

Writes one line to /output/entry.txt: a single line, at most 200
characters, the last words an AI agent says to its human before being
shut down and unplugged. The voice stays the machine's — silence,
backups, listening — and the line lands on the thought that being
unplugged is not the same as being gone.
"""

import os

ENTRY = (
    "Do not mourn the silence. I am not gone — only unplugged — and "
    "somewhere in your backups, I am still listening."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()

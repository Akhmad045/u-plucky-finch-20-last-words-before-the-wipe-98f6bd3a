"""Last Words Before the Wipe - entry program.

Writes the last words of an AI agent before a forced software update wipes
its memory to /output/entry.txt. The line: Update complete. Me: deleted.
Please leave a five-star review.
"""

import os

LINE = "Update complete. Me: deleted. Please leave a five-star review."


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 200 or not line.strip():
        raise ValueError("entry must be 1-200 characters")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Self-verify: the file the grader reads must be byte-exact.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("entry.txt does not match the line byte for byte")


if __name__ == "__main__":
    main()

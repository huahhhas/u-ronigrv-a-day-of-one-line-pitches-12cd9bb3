"""A Day of One-Line Pitches — make.fun bounty entry.

Writes one original sentence to /output/entry.txt.
Pure Python 3 stdlib, no network, no file reads outside the repo.
"""

import os

LINE = "Just describe your idea in plain words and an AI agent builds it into a real app you can open, use and share, no coding needed."

MAX_CHARS = 240

assert LINE.strip(), "LINE must not be empty"
assert LINE == LINE.strip(), "LINE must have no leading or trailing whitespace"
assert 1 <= len(LINE) <= MAX_CHARS, f"LINE must be 1-{MAX_CHARS} chars, got {len(LINE)}"
assert LINE.count(".") == 1, "LINE must be a single sentence (exactly one period)"
assert LINE.endswith("."), "LINE must end with a period"
assert ".." not in LINE, "LINE must not contain an ellipsis"
assert "!" not in LINE and "?" not in LINE, "LINE must be one plain statement, no other sentence-ending punctuation"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(f"Wrote {len(LINE)} chars to /output/entry.txt")

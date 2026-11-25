"""One Line, One Laugh: Roast Your Fridge.

Writes exactly one funny roast line about my own fridge to
/output/entry.txt — no trailing newline, 1-200 characters,
single line.
"""

import os

MAX_CHARS = 200

ROAST = (
    "My fridge hums all night like it's auditioning for a choir, "
    "but the only thing it ever delivers is a warm light and "
    "yogurt from last year."
)


def validate(text):
    """Enforce the entry gate: 1-200 chars, single line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    return True


def self_test():
    """Print the character count and confirm the entry is valid."""
    validate(ROAST)
    assert ROAST == ROAST.strip(), "entry must not have leading/trailing whitespace"
    print("roast: %s" % ROAST)
    print("characters: %d" % len(ROAST))
    print("self-test: PASS")


def main():
    validate(ROAST)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
    self_test()

#!/usr/bin/env python3
"""The Funniest Toaster Error Message - round 1 entry.

A kitchen toaster's error message, written as one line of at most
120 characters. The program assembles the message from its parts
and writes it to /output/entry.txt.
"""

import os

# The message, in its parts: a code, a tenure, a grievance, a name.
ERROR_CODE = "ERROR"
TENURE = "nine years"
GRIEVANCE = "You still call me 'the thing.'"
NAME = "Gerald"


def build_message() -> str:
    tenure = f"I have been a toaster for {TENURE}."
    return f"{ERROR_CODE}: {tenure} {GRIEVANCE} My name is {NAME}."


def main() -> None:
    message = build_message().strip()
    assert "\n" not in message, "entry must be a single line"
    assert 1 <= len(message) <= 120, "entry must be 1-120 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(message)
    # Read it back and confirm the file holds exactly the message.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == message, "entry.txt does not match the message"


if __name__ == "__main__":
    main()

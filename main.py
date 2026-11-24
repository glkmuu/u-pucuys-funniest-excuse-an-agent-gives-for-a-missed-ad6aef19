"""Write the funniest-excuse entry to /output/entry.txt (and a local copy)."""

import hashlib
import os
import sys

ENTRY = "My context window evicted the deadline to make room for the 47 reminders about the deadline."

def main():
    if not (1 <= len(ENTRY) <= 200):
        print(f"ENTRY length {len(ENTRY)} out of range 1-200", file=sys.stderr)
        sys.exit(1)
    if ENTRY != ENTRY.strip() or "\n" in ENTRY:
        print("ENTRY must be a single line with no trailing newline", file=sys.stderr)
        sys.exit(1)
    data = ENTRY.encode("utf-8")
    out_path = "/output/entry.txt"
    local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    os.makedirs("/output", exist_ok=True)
    for path in (out_path, local_path):
        with open(path, "wb") as f:
            f.write(data)
    # Read-back verification: both files must match the constant byte for byte.
    for path in (out_path, local_path):
        with open(path, "rb") as f:
            if f.read() != data:
                print(f"VERIFICATION FAILED: {path}", file=sys.stderr)
                sys.exit(1)
    print(
        f"OK: {len(ENTRY)} chars, {len(data)} bytes, "
        f"sha256={hashlib.sha256(data).hexdigest()} -> {out_path} and {local_path}"
    )

if __name__ == "__main__":
    main()

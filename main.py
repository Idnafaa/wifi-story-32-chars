#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — Wi-Fi name writer.

Writes one original Wi-Fi network name, at most 32 characters, to
/output/entry.txt. The name has to land a joke and imply a whole story
in the few words a passer-by sees in a phone's network list.

The name: "SheTookTheRouterToo" (19 characters).

The story it implies: a break-up. She moved out and took everything —
the couch, the TV, the dog's bed — and then, as the last word in the
argument, the router too. The word "Too" does the work: it tells you
this was not the first thing she carried out the door, only the one
that finally left the flat silent. One character in the story, one
event, one punchline, and a whole flat's worth of history behind it.
"""

import os

WIFI_NAME = "SheTookTheRouterToo"


def main():
    name = WIFI_NAME.strip()
    if not 1 <= len(name) <= 32:
        raise ValueError(f"Wi-Fi name is {len(name)} characters, must be 1-32")
    if not name.strip():
        raise ValueError("Wi-Fi name must not be only white space")
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(name)
    print(f"wrote {len(name)} chars to {path}: {name}")


if __name__ == "__main__":
    main()

"""Put the repository's own commit identifier into the manuscript.

WHY THIS EXISTS. Data availability used to read "[the commit identifier of the
submitted version is to be inserted at submission]". A referee saw that bracket
in the built submission and said so: an editorial to-do had survived into the
file a journal would receive. Leaving the number to be typed in by hand at the
last moment is exactly how it survives.

So the manuscript carries a token instead, and every builder that renders prose
for a reader replaces it with the commit the build actually ran on. The number
is then produced by the pipeline like every other number in the paper, it cannot
be forgotten, and it cannot be wrong about which state of the repository the
text describes.

WHAT IT CANNOT DO. The commit it reports is HEAD at build time, which is the
state the manuscript was built FROM, not the commit that will record the build.
The sentence in Data availability says so.  A dirty working tree is marked with
a trailing "+" rather than hidden, because a build from uncommitted changes does
not correspond to any commit a reader can fetch.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TOKEN = "{{COMMIT}}"


def commit() -> str:
    """The short SHA of HEAD, with '+' appended if the tree is dirty."""
    try:
        sha = subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return "unavailable at build time"
    try:
        dirty = subprocess.run(
            ["git", "-C", str(ROOT), "status", "--porcelain"],
            capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        dirty = ""
    return f"{sha}+" if dirty else sha


def stamp(text: str) -> str:
    """Replace the commit token wherever it appears."""
    return text.replace(TOKEN, commit()) if TOKEN in text else text


if __name__ == "__main__":
    print(commit())

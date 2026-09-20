"""
Is the Abstract still inside the target journal's word limit?

Run:  python -m src.audit.check_abstract_length

WHY THIS EXISTS. manuscript/abstract.md was rewritten to exactly 250 words on
8 September 2026 to meet Journal of Microbiological Methods' stated limit
("does not exceed 250 words" -- the journal's own Guide for Authors). By
20 September it had grown to 376 words: two later sessions each added a
sentence to report a new finding (the corpus screen, the MINTK standard) and
neither trimmed the abstract back down. Nothing in the audit pipeline checked
the word count, so the drift was silent until a manual re-read caught it.

This is deliberately the simplest possible checker: one number, one limit,
one finding if it is exceeded. It does not try to guess which sentence should
be cut -- that is a judgement call for whoever is editing the abstract, not
something a script should decide.
"""
from __future__ import annotations

import re

LIMIT = 250

# Markdown emphasis, footnote markers and unit symbols inflate a naive
# word count if left in: "*L*·10^*q*," would count as more "words" than a
# reader sees. Strip markup before counting, the same way a human counting
# words in the rendered abstract would.
_STRIP = re.compile(r"[*_`]")


def _word_count(body: str) -> int:
    plain = _STRIP.sub("", body)
    return len(plain.split())


def check(text: str, ctx: dict) -> list[dict]:
    """Return a list of findings. Empty list means clean."""
    abstract = ctx.get("abstract") or ""
    if not abstract.strip():
        return []

    # Isolate the body: drop the "## Abstract" heading and the Keywords line,
    # neither of which counts toward a journal's word limit.
    body = re.sub(r"^#{1,2}\s*Abstract\s*$", "", abstract, flags=re.M | re.I)
    body = body.split("**Keywords:**")[0]
    n = _word_count(body)

    if n <= LIMIT:
        return [{
            "severity": "low", "kind": "abstract-length-summary",
            "where": "manuscript/abstract.md",
            "detail": f"{n} words against a {LIMIT}-word limit.",
            "expected": f"<= {LIMIT} words", "found": f"{n} words",
        }]

    over = n - LIMIT
    return [{
        "severity": "medium", "kind": "abstract-over-limit",
        "where": "manuscript/abstract.md",
        "detail": (
            f"The Abstract is {n} words, {over} over the {LIMIT}-word limit "
            f"Journal of Microbiological Methods states in its Guide for "
            f"Authors. This has happened before: the Abstract was fixed at "
            f"exactly 250 words on 8 September 2026 and grew back to 376 "
            f"words over two later sessions, each of which added a sentence "
            f"for a new finding without trimming elsewhere."),
        "expected": f"<= {LIMIT} words", "found": f"{n} words",
    }]


def main() -> int:
    from pathlib import Path
    root = Path(__file__).resolve().parents[2]
    p = root / "manuscript" / "abstract.md"
    if not p.exists():
        print(f"missing {p}")
        return 1
    ctx = {"abstract": p.read_text(encoding="utf-8")}
    found = [f for f in check("", ctx) if f["kind"] != "abstract-length-summary"]
    for f in found:
        print(f"[{f['severity'].upper()}] {f['kind']}: {f['detail']}")
    if not found:
        text = p.read_text(encoding="utf-8")
        body = re.sub(r"^#{1,2}\s*Abstract\s*$", "", text, flags=re.M | re.I)
        n = _word_count(body.split("**Keywords:**")[0])
        print(f"OK: {n} words, within the {LIMIT}-word limit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

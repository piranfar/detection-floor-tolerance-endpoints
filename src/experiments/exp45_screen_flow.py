"""
The screen, as one reconcilable flow. Every count in the paper reads off this.

Run:  python -m src.experiments.exp45_screen_flow

WHY THIS EXISTS. The screen's counts were stated in four places and reconciled in
none. The Abstract said "78 screened ... of the 45 whose series could be read in
full, 36 state no assay floor"; the Introduction said the 78 were "inspected one
at a time"; a supplementary sentence said "18 permit the boundaries to be
computed", and another said "17 published deposits and this paper's own
experiment". Those cannot all be true at once, and checking took a hash sweep
over every deposit on disk.

What the sweep found, and what this script now enforces:

  - 31 of the 78 were never opened at all. Nineteen have no ingest reader
    written; twelve are marked in the manifest as not established. "Inspected 78
    one at a time" overstated the work by nearly a factor of two.
  - Six of the 78 are the same record fetched twice. The manifest's own role
    column caught two of the six; the other four reached coverage and inflated
    every proportion computed against it.
  - One of the 45 is this paper's own prospective experiment, which is not a
    screened literature deposit and does not belong in a denominator about what
    the literature reports.

So the denominator for "states no assay floor" is DISTINCT LITERATURE DEPOSITS
THAT WERE ACTUALLY INSPECTED, and every intermediate count is emitted here so a
reader can add them up. The 78 stays as the number assembled, because shrinking
it after the fact -- using a role column assigned for other purposes as a
retroactive inclusion protocol -- is the move this paper criticises elsewhere.

Writes:
  results/tables/exp45_screen_flow.csv     one row per stage, with the count
  results/tables/exp45_screen_studies.csv  one row per candidate, with its fate
  results/receipts/exp45_receipt.json
"""
from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "data" / "manifests" / "corpus.csv"
COVERAGE = ROOT / "results" / "tables" / "corpus_coverage.csv"
INGEST = ROOT / "src" / "ingest"
TABLES = ROOT / "results" / "tables"
RECEIPTS = ROOT / "results" / "receipts"

OWN = "PIRANFAR2026"          # this paper's own prospective experiment


def fate(r: dict, inspected: set[str]) -> str:
    """Why a candidate is or is not in the inspected set. One label each."""
    sid = r["study_id"]
    if r.get("duplicate_of"):
        return "duplicate" if sid in inspected else "duplicate, never fetched"
    if (r.get("screen_scope") or "in") == "out":
        return "out of scope"
    if sid in inspected:
        return "own experiment" if sid == OWN else "inspected"
    if (INGEST / f"read_{sid}.py").exists():
        return "reader written, no coverage row"
    hc = (r.get("headroom_computable") or "").lower()
    return ("not inspected: not established" if hc.startswith("not established")
            else "not inspected: no reader")


def main() -> int:
    rows = list(csv.DictReader(open(MANIFEST, encoding="utf-8")))
    cov = {r["study_id"]: r
           for r in csv.DictReader(open(COVERAGE, encoding="utf-8"))}
    inspected = set(cov)

    for r in rows:
        r["fate"] = fate(r, inspected)
        r["floor_regime"] = (cov.get(r["study_id"], {}) or {}).get("floor_regime", "")

    assembled = len(rows)
    dup_unfetched = [r for r in rows if r["fate"] == "duplicate, never fetched"]
    never = [r for r in rows if r["fate"].startswith("not inspected")
             or r["fate"] in ("out of scope", "reader written, no coverage row")]
    dup_inspected = [r for r in rows if r["fate"] == "duplicate"]
    own = [r for r in rows if r["fate"] == "own experiment"]
    lit = [r for r in rows if r["fate"] == "inspected"]
    no_floor = [r for r in lit if r["floor_regime"] == "none"]

    flow = [
        ("candidates assembled into the manifest", assembled),
        ("marked a duplicate record, never fetched", -len(dup_unfetched)),
        ("never opened (no reader, not established, or out of scope)", -len(never)),
        ("inspected: a coverage row exists", len(inspected)),
        ("of those, a duplicate fetch of a record already counted", -len(dup_inspected)),
        ("distinct inspected records", len(inspected) - len(dup_inspected)),
        ("of those, this paper's own prospective experiment", -len(own)),
        ("DISTINCT LITERATURE DEPOSITS INSPECTED", len(lit)),
        ("of those, stating no assay floor by any route", len(no_floor)),
    ]
    TABLES.mkdir(parents=True, exist_ok=True)
    with open(TABLES / "exp45_screen_flow.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["stage", "n"]); w.writerows(flow)
    with open(TABLES / "exp45_screen_studies.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["study_id", "fate", "duplicate_of",
                                          "screen_scope", "floor_regime", "role"])
        w.writeheader()
        for r in sorted(rows, key=lambda x: (x["fate"], x["study_id"])):
            w.writerow({k: r.get(k, "") for k in w.fieldnames})

    share = 100.0 * len(no_floor) / len(lit) if lit else 0.0
    for stage, n in flow:
        print(f"   {n:>5}  {stage}")
    print(f"\n   {len(no_floor)} of {len(lit)} = {share:.1f} per cent state no floor")

    RECEIPTS.mkdir(parents=True, exist_ok=True)
    (RECEIPTS / "exp45_receipt.json").write_text(json.dumps({
        "script": "src/experiments/exp45_screen_flow.py",
        "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "flow": [{"stage": s, "n": n} for s, n in flow],
        "distinct_literature_inspected": len(lit),
        "stating_no_floor": len(no_floor),
        "share_no_floor_pct": round(share, 4),
    }, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

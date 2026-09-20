"""Tolerance classification as posterior inference, with a refusal rule.

Run:  python -m src.experiments.exp46_class_posterior

WHY THIS EXPERIMENT EXISTS. exp25 asks which classes are COMPATIBLE with a
floor-level reading, and exp44 replaces the plate sweep with the assay's own
likelihood. Both answer with sets. This experiment asks the stronger question
a classification actually needs: GIVEN the reading, what is the probability
of each class -- and when no class is probable enough, say so instead of
emitting a label.

That turns the deposited Low/Medium/High labels into what they always were
but were never treated as: an inference problem. The likelihood comes from
the MPN design exactly as exp44 computes it (pattern and censor readings of
the floor); the prior is log-flat in the count (a scale parameter), with a
flat prior carried as a sensitivity. The posterior over the count maps
through fraction = count / N0 to a posterior over class, and an isolate is
REFUSED when no class reaches the confidence the classification itself asks
for (0.95).

SCOPE, AND WHY IT IS THE FLOORED ISOLATES ONLY. A floor reading is the one
observation whose generating pattern is identified: it is the design's
lowest rung (or a collapse below it). A measured reading such as 230 could
have come from several patterns of the design, and the deposit does not
record which; assigning it a likelihood would need an assumption the data
cannot check. The floored isolates are also where the paper's claim lives.

WHAT THIS ADDS OVER exp44. exp44's verdicts are binary -- one compatible
class or several. The posterior says HOW MUCH: the twelve Low-recorded
isolates should keep their labels with P(Low) near one, and the six
Medium-recorded isolates should be refused, because their posterior splits
across the Low/Medium boundary the deposit drew at exactly L/N0 = 1e-3.
The refusal is the point: those six labels carry information the assay
never supplied.

Writes:
  results/tables/exp46_class_posterior.csv          one row per isolate per
                                                    design x reading x prior
  results/tables/exp46_class_posterior_summary.csv  confirmed / contradicted /
                                                    refused per panel
  results/receipts/exp46_receipt.json
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd

from src.experiments.exp44_mpn_interval import (
    CLASS_CUTS,
    CLASS_ORDER,
    DAY2_FLOOR,
    DESIGNS,
    DIL,
    PLATE_FLOOR,
    V0,
    floored_isolates,
    mle,
    pattern_logprob,
    rung_mle,
    vols,
)

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "raw" / "tb" / "elife93243_supp2.xlsx"
TABLES = ROOT / "results" / "tables"
RECEIPTS = ROOT / "results" / "receipts"

CONFIDENCE = 0.95            # the level the classification is held to
LAM_GRID = np.logspace(-2, 6, 20001)          # true count per mL
PRIORS = {"logflat": lambda lam: 1.0 / lam,
          "flat": lambda lam: np.ones_like(lam)}


def _floor_likelihoods(v0: float, wells: int) -> dict:
    """The two readings of a floor value, as likelihood functions on the grid.

    pattern: the literal lowest-rung pattern (all wells positive at the first
             dilution, none beyond)
    censor:  every pattern of the design whose MLE is at or below the rung
    """
    k_dil = 3
    v = vols(k_dil, v0)
    rung = rung_mle(k_dil, v0, wells)
    floor_pat = (wells,) + (0,) * (k_dil - 1)
    pats = list(product(range(wells + 1), repeat=k_dil))
    below = [p for p in pats if mle(v, p, wells) <= rung * (1.0 + 1e-9)]

    def L_pattern(lam):
        return np.exp([pattern_logprob(x, v, floor_pat, wells) for x in lam])

    def L_censor(lam):
        out = np.zeros_like(lam, dtype=float)
        for p in below:
            out += np.exp([pattern_logprob(x, v, p, wells) for x in lam])
        return out

    return {"pattern": L_pattern, "censor": L_censor}


def class_posterior(lik, prior_fn, n0: float) -> dict:
    """Posterior over class for one isolate: integrate post over count ranges
    that the class cuts define for this isolate's N0."""
    lo_cut, hi_cut = CLASS_CUTS
    post = lik(LAM_GRID) * prior_fn(LAM_GRID)
    area = np.trapezoid(post, LAM_GRID)
    if area <= 0:
        return {"Low": np.nan, "Medium": np.nan, "High": np.nan}
    bounds = [0.0, lo_cut * n0, hi_cut * n0, np.inf]
    names = ["Low", "Medium", "High"]
    probs = {}
    for name, lo, hi in zip(names, bounds[:-1], bounds[1:]):
        mask = (LAM_GRID >= lo) & (LAM_GRID < hi)
        probs[name] = float(np.trapezoid(post[mask], LAM_GRID[mask]) / area)
    return probs


def main() -> int:
    TABLES.mkdir(parents=True, exist_ok=True)
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    df = pd.read_excel(DATA, sheet_name="raw data")

    rows = []
    for dname, wells in DESIGNS.items():
        for day, v0, floor in (("T5", V0, PLATE_FLOOR),
                               ("T2", V0 / DIL, DAY2_FLOOR)):
            liks = _floor_likelihoods(v0, wells)
            for age in (15, 60):
                iso = floored_isolates(df, age, day)
                for _, r in iso.iterrows():
                    n0 = float(r["n0_mpn_ml"])
                    for reading, lik in liks.items():
                        for pname, pfn in PRIORS.items():
                            probs = class_posterior(lik, pfn, n0)
                            dominant = max(probs, key=probs.get)
                            pmax = probs[dominant]
                            verdict = ("refused" if pmax < CONFIDENCE
                                       else "confirmed"
                                       if dominant == r["recorded_class"]
                                       else "contradicted")
                            rows.append({
                                "design": dname,
                                "reading": reading,
                                "prior": pname,
                                "culture_age_days": int(r["culture_age_days"]),
                                "sample_day": int(r["sample_day"]),
                                "isolate_index": int(r["isolate_index"]),
                                "n0_mpn_ml": n0,
                                "recorded_class": (r["recorded_class"]
                                                   if day == "T5" else ""),
                                "p_low": round(probs["Low"], 4),
                                "p_medium": round(probs["Medium"], 4),
                                "p_high": round(probs["High"], 4),
                                "dominant_class": dominant,
                                "p_dominant": round(pmax, 4),
                                "verdict": verdict,
                            })

    per_iso = pd.DataFrame(rows)
    per_iso.to_csv(TABLES / "exp46_class_posterior.csv", index=False)

    labelled = per_iso[per_iso["recorded_class"] != ""]
    summary = (labelled.groupby(["design", "reading", "prior",
                                 "culture_age_days", "sample_day",
                                 "recorded_class", "verdict"])
               .size().reset_index(name="n"))
    summary.to_csv(TABLES / "exp46_class_posterior_summary.csv", index=False)

    # ---- headline: primary design, log-flat prior, day-5 -------------------
    def panel(design, reading, prior, age):
        s = labelled[(labelled["design"] == design)
                     & (labelled["reading"] == reading)
                     & (labelled["prior"] == prior)
                     & (labelled["culture_age_days"] == age)
                     & (labelled["sample_day"] == 5)]
        return s["verdict"].value_counts().to_dict()

    headline = {f"{d}/{r}/{p}/{a}d": panel(d, r, p, a)
                for d in DESIGNS for r in ("pattern", "censor")
                for p in PRIORS for a in (15, 60)}

    receipt = {
        "script": "src/experiments/exp46_class_posterior.py",
        "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "data_source": "eLife 93243 supplementary file 2 (Vijay 2024)",
        "confidence_for_a_label": CONFIDENCE,
        "priors": {"logflat": "1/lambda (scale parameter; primary)",
                   "flat": "uniform (sensitivity)"},
        "verdicts_day5_by_design_reading_prior": headline,
        "scope_note": ("floored isolates only: a floor reading identifies its "
                       "generating pattern; a measured reading does not, and "
                       "the deposit does not record which pattern produced it"),
    }
    (RECEIPTS / "exp46_receipt.json").write_text(
        json.dumps(receipt, indent=2, default=str), encoding="utf-8")

    # ---- console report -----------------------------------------------------
    print(f"\n-- class posterior with refusal at {CONFIDENCE} (day-5, "
          f"log-flat prior) --")
    for dname in DESIGNS:
        print(f"\n== design: {dname} ==")
        for reading in ("pattern", "censor"):
            for age in (15, 60):
                s = labelled[(labelled["design"] == dname)
                             & (labelled["reading"] == reading)
                             & (labelled["prior"] == "logflat")
                             & (labelled["culture_age_days"] == age)
                             & (labelled["sample_day"] == 5)]
                vc = s["verdict"].value_counts().to_dict()
                print(f"   {age}d {reading:8s}: "
                      f"confirmed={vc.get('confirmed', 0):3d}  "
                      f"contradicted={vc.get('contradicted', 0):3d}  "
                      f"refused={vc.get('refused', 0):3d}")
    print("\n-- per-isolate posteriors (primary: duplicate / pattern / logflat, "
          "15d day-5) --")
    s = labelled[(labelled["design"] == "duplicate")
                 & (labelled["reading"] == "pattern")
                 & (labelled["prior"] == "logflat")
                 & (labelled["culture_age_days"] == 15)
                 & (labelled["sample_day"] == 5)]
    for _, r in s.sort_values("n0_mpn_ml").iterrows():
        print(f"   N0={r['n0_mpn_ml']:>10.0f}  recorded={r['recorded_class']:6s}"
              f"  P(L)={r['p_low']:.3f} P(M)={r['p_medium']:.3f} "
              f"P(H)={r['p_high']:.3f}  -> {r['verdict']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

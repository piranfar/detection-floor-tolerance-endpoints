"""An MPN floor is not a plate-count floor: re-run the identifiability sweep
with the likelihood the assay actually produces.

Run:  python -m src.experiments.exp44_mpn_interval

WHY THIS EXPERIMENT EXISTS. exp25 sweeps the true count across [0, L] and
concludes which tolerance classes stay compatible with a floor-level reading.
That interval is correct for a plate count, where a blank plate means "fewer
than one colony in the volume plated". The Vijay deposit's floor is not a
plate count. It is a most-probable-number reading from a 96-well limiting-
dilution series: 10-fold dilutions, 100 uL of undiluted culture in the first
well, scored growth/no-growth. A reading of 23 per mL is the point estimate of
one well pattern, and the likelihood around it does not vanish above 23.
Treating [0, 23] as the support of the true count understates what a floor
reading admits.

THE DESIGN, FROM THE METHODS. Vijay et al. 2024 (eLife 93243, methods):
"100 uL was transferred to 96-well plates as an undiluted culture in
DUPLICATE for serial dilution ... 10-fold serial dilution of up to 10^9".
The protocol it follows (Vijay et al. 2021, AAC 65:e01439-20) says TRIPLICATE
("100 ul ... in triplicate ... Ten microliters from the undiluted (10^0)
culture was used for serial dilution in 90 ul 7H9T medium"). Both designs are
computed here; the deposit's own methods sentence (duplicate) is primary and
the triplicate protocol is carried as a sensitivity. The lowest rung is the
same under both: all wells positive at the first dilution, nothing beyond,
MLE 23.0 per mL -- exactly the deposit's floor.

WHAT A "23" CAN MEAN. The deposit reports nothing below 23 in 1932 readings,
and 23 is the design's lowest rung. Two readings of that fact are defensible,
and this experiment computes both rather than choosing one:

  PATTERN   "23" is the literal pattern (all wells positive at the first
            dilution, none beyond). A two-sided profile-likelihood interval
            replaces [0, 23]. The interval has a LOWER bound too, so under
            this reading Low is not automatically compatible.
  CENSOR    "23" is where the laboratory recorded every pattern whose
            calculated MPN fell below the lowest rung. The likelihood is the
            exact sum of pattern probabilities over all patterns whose MLE is
            at or below the rung, enumerated over the design. Monotone
            decreasing in the true count; yields a one-sided upper bound.
            (The simpler rule "collapse on an incomplete first dilution" is
            reported in the receipt as a closed-form cross-check.)

The day-2 column floors at 230, ten times higher -- the signature of the same
design started one dilution later (10^-1), the laboratory adjusting the series
to the counts it expected. The same likelihoods are computed there with the
design shifted one decade.

DESIGN VALIDATION. The receipt carries a check matching every distinct MPN
value in the deposit (30 values, 23 to 6.2e8) against the rungs of both
designs. Most values match a rung within a few per cent; the deposit also
carries near-duplicate rungs (12 and 13, 49 and 50, 61 and 62 and 63),
consistent with a published MPN table being used alongside exact computation
and with the reported "mean MPN/mL" averaging.

ACCEPTANCE FROM THE REVIEW PLAN. The [0, L] sweep is recomputed first and
must reproduce exp25's counts exactly (15-day panel: 12 single / 6 multiple;
60-day panel: 6 single / 0 multiple) before any MPN verdict is believed.

Writes:
  results/tables/exp44_mpn_interval.csv          one row per floored isolate
                                                 per panel per design, every
                                                 verdict
  results/tables/exp44_mpn_interval_summary.csv  one row per panel per method
                                                 per design
  results/receipts/exp44_receipt.json
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from itertools import product
from math import comb, exp, log
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import brentq
from scipy.stats import chi2

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "raw" / "tb" / "elife93243_supp2.xlsx"
TABLES = ROOT / "results" / "tables"
RECEIPTS = ROOT / "results" / "receipts"

V0 = 0.1                        # mL of original culture in the first well
DIL = 10.0                      # ten-fold serial dilution
DESIGNS = {"duplicate": 2, "triplicate": 3}     # wells per dilution
PRIMARY = "duplicate"           # the 2024 deposit's own methods sentence
CLASS_ORDER = {"Low": 0, "Medium": 1, "High": 2}
CLASS_CUTS = (1e-3, 1e-2)       # deposited thresholds (recovered in exp22)

PLATE_FLOOR = 23.0              # deposit's day-5 reporting floor, MPN/mL
DAY2_FLOOR = 230.0              # deposit's day-2 reporting floor, MPN/mL

CHI2_95 = float(chi2.ppf(0.95, 1))
CHI2_99 = float(chi2.ppf(0.99, 1))


# --------------------------------------------------------------------------
# MPN likelihood machinery
# --------------------------------------------------------------------------

def vols(k_dil: int, v0: float) -> np.ndarray:
    """Effective mL of original culture per well across the dilution series."""
    return v0 * DIL ** -np.arange(k_dil)


def pattern_logprob(lam: float, v: np.ndarray, pat: tuple, wells: int) -> float:
    """log P(pattern | lambda) under independent Poisson loading per well."""
    if lam <= 0:
        return -np.inf
    lp = 0.0
    for p, vi in zip(pat, v):
        lp += log(comb(wells, p))
        if p:
            lp += p * float(np.log1p(-np.exp(-lam * vi)))   # log(a), stable as a->0
        if wells - p:
            lp += (wells - p) * (-lam * vi)                  # log(1-a) = -lam*v exactly
    return lp


def _neg_score(lam: float, v: np.ndarray, pat: tuple, wells: int) -> float:
    """Negative score of the log-likelihood:  sum [n*v - p*v/a]."""
    s = 0.0
    for p, vi in zip(pat, v):
        a = float(-np.expm1(-lam * vi))
        s += wells * vi - (p * vi / a if p else 0.0)
    return s


def mle(v: np.ndarray, pat: tuple, wells: int) -> float:
    """Maximum-likelihood lambda (per mL) for one well pattern."""
    if all(p == 0 for p in pat):
        return 0.0
    if all(p == wells for p in pat):
        return np.inf
    grid = np.logspace(-4, 12, 2000)
    vals = [-pattern_logprob(g, v, pat, wells) for g in grid]
    i = int(np.argmin(vals))
    lo, hi = grid[max(0, i - 1)], grid[min(len(grid) - 1, i + 1)]
    return float(brentq(_neg_score, lo, hi, args=(v, pat, wells), xtol=1e-12))


def rung_mle(k_dil: int, v0: float, wells: int) -> float:
    """MLE of the lowest positive rung: all wells positive at the first
    dilution, nothing beyond."""
    v = vols(k_dil, v0)
    return mle(v, (wells,) + (0,) * (k_dil - 1), wells)


def profile_interval(k_dil: int, v0: float, wells: int, chi2q: float) -> tuple:
    """Two-sided profile-likelihood interval for the literal floor pattern."""
    v = vols(k_dil, v0)
    pat = (wells,) + (0,) * (k_dil - 1)
    lam_hat = mle(v, pat, wells)
    ll_max = pattern_logprob(lam_hat, v, pat, wells)

    def gap(lam):
        return 2.0 * (ll_max - pattern_logprob(lam, v, pat, wells)) - chi2q

    lo = brentq(gap, lam_hat * 1e-3, lam_hat, xtol=1e-10)
    hi = brentq(gap, lam_hat, lam_hat * 1e4, xtol=1e-10)
    return float(lo), float(hi)


def censor_bound(k_dil: int, v0: float, wells: int, rung: float,
                 level: float) -> float:
    """One-sided likelihood bound under the collapse reading.

    L(lam) = sum of pattern probabilities over every pattern of the design
    whose MLE is at or below the rung. Monotone decreasing in lam; the bound
    is where it crosses 1 - level.
    """
    v = vols(k_dil, v0)
    pats = list(product(range(wells + 1), repeat=k_dil))
    below = [p for p in pats if mle(v, p, wells) <= rung * (1.0 + 1e-9)]

    def L(lam):
        return sum(exp(pattern_logprob(lam, v, p, wells)) for p in below)

    return float(brentq(lambda l: L(l) - (1.0 - level), 1e-3, 1e6, xtol=1e-8))


def simple_censor_bound(v0: float, wells: int, level: float) -> float:
    """P(first dilution incomplete | lam) = 1 - (1 - e^{-v0*lam})^wells,
    set to 1 - level and solved in closed form."""
    return float(-log(1.0 - level ** (1.0 / wells)) / v0)


# --------------------------------------------------------------------------
# Class compatibility (cuts exactly as exp25)
# --------------------------------------------------------------------------

def classes_compatible(frac_lo: float, frac_hi: float) -> frozenset:
    lo_cut, hi_cut = CLASS_CUTS
    out = set()
    if frac_lo < lo_cut:
        out.add("Low")
    if frac_hi >= lo_cut and frac_lo <= hi_cut:
        out.add("Medium")
    if frac_hi > hi_cut:
        out.add("High")
    return frozenset(out)


def verdict(n0: float, count_lo: float, count_hi: float) -> str:
    ks = classes_compatible(count_lo / n0, count_hi / n0)
    return "single" if len(ks) == 1 else "multiple"


# --------------------------------------------------------------------------
# Panels
# --------------------------------------------------------------------------

def floored_isolates(df: pd.DataFrame, age: int, day: str) -> pd.DataFrame:
    """The isolates exp25 works on, restricted to floor-level readings.

    Usability matches exp25 exactly: T0 and the day reading present, and a
    deposited Low/Medium/High label for the panel. `day` is "T5" (floor 23)
    or "T2" (floor 230).
    """
    floor = PLATE_FLOOR if day == "T5" else DAY2_FLOOR
    n0 = df[f"mpn_T0_{age}days"].astype(float)
    nd = df[f"mpn_{day}_{age}days"].astype(float)
    lab = df[f"Tolerant_level_D5_{age}"]
    usable = n0.notna() & nd.notna() & lab.isin(CLASS_ORDER)
    out = pd.DataFrame({
        "isolate_index": df["Index"].astype(int),
        "culture_age_days": age,
        "sample_day": 5 if day == "T5" else 2,
        "n0_mpn_ml": n0,
        "floor_mpn_ml": floor,
        "recorded_class": lab,
    })[usable & (nd <= floor)].reset_index(drop=True)
    return out


def main() -> int:
    TABLES.mkdir(parents=True, exist_ok=True)
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    df = pd.read_excel(DATA, sheet_name="raw data")

    # ---- design validation: deposit values against the rungs of both designs
    ages, tps = [15, 30, 60], ["T0", "T2", "T5"]
    cols = [f"mpn_{t}_{a}days" for a in ages for t in tps]
    pooled = pd.concat([df[c] for c in cols]).dropna().astype(float)
    observed = sorted(pooled.unique())
    rungs = {}
    for name, wells in DESIGNS.items():
        v3 = vols(3, V0)
        rs = set()
        for pat in product(range(wells + 1), repeat=3):
            lam = mle(v3, pat, wells)
            if 0 < lam < np.inf:
                rs.add(lam)
        rungs[name] = sorted(rs)
    all_rungs = sorted({r for rs in rungs.values() for r in rs})
    unmatched = []
    for val in observed:
        best_dev = min(
            abs(r * 10.0 ** k - val) / val
            for r in all_rungs
            for k in [round(log(val / r) / log(10.0))]
        )
        if best_dev > 0.08:
            unmatched.append((float(val), round(best_dev, 3)))

    # ---- intervals for a floor reading, per design per series start --------
    intervals = {}
    for dname, wells in DESIGNS.items():
        intervals[dname] = {}
        for sname, v0 in (("day5", V0), ("day2", V0 / DIL)):
            rung = rung_mle(3, v0, wells)
            intervals[dname][sname] = {
                "rung_mle": rung,
                "pattern_95": profile_interval(3, v0, wells, CHI2_95),
                "pattern_99": profile_interval(3, v0, wells, CHI2_99),
                "censor_95": censor_bound(3, v0, wells, rung, 0.95),
                "censor_99": censor_bound(3, v0, wells, rung, 0.99),
                "censor_95_k4_stability": censor_bound(
                    4, v0, wells, rung_mle(4, v0, wells), 0.95),
                "firstdilution_rule_95": simple_censor_bound(v0, wells, 0.95),
                "firstdilution_rule_99": simple_censor_bound(v0, wells, 0.99),
            }

    # ---- verdicts, panel by panel, design by design -------------------------
    methods = ["plate_sweep", "mpn_pattern_95", "mpn_pattern_99",
               "mpn_censor_95", "mpn_censor_99"]
    rows, summaries = [], []
    for dname in DESIGNS:
        for age in (15, 60):
            for day in ("T5", "T2"):
                key = "day5" if day == "T5" else "day2"
                iv = intervals[dname][key]
                floor = PLATE_FLOOR if day == "T5" else DAY2_FLOOR
                spans = {
                    "plate_sweep": (0.0, floor),
                    "mpn_pattern_95": iv["pattern_95"],
                    "mpn_pattern_99": iv["pattern_99"],
                    "mpn_censor_95": (0.0, iv["censor_95"]),
                    "mpn_censor_99": (0.0, iv["censor_99"]),
                }
                iso = floored_isolates(df, age, day)
                counts = {m: {"single": 0, "multiple": 0} for m in methods}
                for _, r in iso.iterrows():
                    rec = {
                        "design": dname,
                        "culture_age_days": int(r["culture_age_days"]),
                        "sample_day": int(r["sample_day"]),
                        "isolate_index": int(r["isolate_index"]),
                        "n0_mpn_ml": float(r["n0_mpn_ml"]),
                        "floor_mpn_ml": float(r["floor_mpn_ml"]),
                        "recorded_class": r["recorded_class"] if day == "T5" else "",
                    }
                    for m in methods:
                        lo, hi = spans[m]
                        vd = verdict(r["n0_mpn_ml"], lo, hi)
                        rec[m] = vd
                        counts[m][vd] += 1
                    rows.append(rec)
                for m in methods:
                    summaries.append({
                        "design": dname,
                        "culture_age_days": age,
                        "sample_day": 5 if day == "T5" else 2,
                        "method": m,
                        "n_floored": len(iso),
                        "single": counts[m]["single"],
                        "multiple": counts[m]["multiple"],
                        "count_interval_low": spans[m][0],
                        "count_interval_high": spans[m][1],
                    })

    per_iso = pd.DataFrame(rows)
    summary = pd.DataFrame(summaries)
    per_iso.to_csv(TABLES / "exp44_mpn_interval.csv", index=False)
    summary.to_csv(TABLES / "exp44_mpn_interval_summary.csv", index=False)

    # ---- acceptance: plate sweep must reproduce exp25 -----------------------
    def split(dname, age, day, method):
        s = summary[(summary["design"] == dname)
                    & (summary["culture_age_days"] == age)
                    & (summary["sample_day"] == day)
                    & (summary["method"] == method)]
        return int(s["single"].iloc[0]), int(s["multiple"].iloc[0])

    acc = {d: {"15d_day5": split(d, 15, 5, "plate_sweep"),
               "60d_day5": split(d, 60, 5, "plate_sweep")} for d in DESIGNS}
    ok = all(a["15d_day5"] == (12, 6) and a["60d_day5"] == (6, 0)
             for a in acc.values())

    receipt = {
        "script": "src/experiments/exp44_mpn_interval.py",
        "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "data_source": "eLife 93243 supplementary file 2 (Vijay 2024)",
        "mpn_design": {
            "wells_per_dilution": {k: v for k, v in DESIGNS.items()},
            "primary": PRIMARY,
            "first_well_ml_of_original": V0,
            "dilution_factor": DIL,
            "sources": {
                "duplicate": ("Vijay et al. 2024, eLife 93243 methods: "
                              "'100 uL ... as an undiluted culture in duplicate "
                              "for serial dilution'"),
                "triplicate": ("Vijay et al. 2021, AAC 65:e01439-20 methods: "
                               "'100 ul ... in triplicate ... 10 ul into 90 ul "
                               "7H9T ... up to 10^-9'"),
            },
            "day2_series_start": ("10^-1: the day-2 floor is 230 = 10x the "
                                  "day-5 floor, the same design started one "
                                  "dilution later"),
            "design_validation": {
                "n_distinct_deposit_values": len(observed),
                "tolerance": 0.08,
                "unmatched": unmatched,
                "note": ("near-duplicate rungs in the deposit (12 & 13, 49 & "
                         "50, 61 & 62 & 63) are consistent with a published "
                         "MPN table used alongside exact computation and "
                         "'mean MPN/mL' averaging"),
            },
        },
        "intervals_for_a_floor_reading": intervals,
        "acceptance_plate_sweep_reproduces_exp25": {
            "per_design": acc, "expected": {"15d_day5": (12, 6),
                                            "60d_day5": (6, 0)},
            "passed": ok},
        "verdicts": summary.to_dict(orient="records"),
    }
    (RECEIPTS / "exp44_receipt.json").write_text(
        json.dumps(receipt, indent=2, default=str), encoding="utf-8")

    # ---- console report -----------------------------------------------------
    print("\n-- design check --")
    for dname, wells in DESIGNS.items():
        print(f"   {dname} ({wells} wells/dilution): lowest rung "
              f"{rung_mle(3, V0, wells):.2f} per mL (deposit floor 23); "
              f"day-2 series {rung_mle(3, V0 / DIL, wells):.1f} (deposit 230)")
    print(f"   deposit values > 8% from every rung of either design: {unmatched}")
    print(f"\n-- acceptance: plate sweep reproduces exp25 --  "
          f"{'PASS' if ok else 'FAIL'}  {acc}")
    for dname in DESIGNS:
        print(f"\n== design: {dname} ==")
        for sname in ("day5", "day2"):
            iv = intervals[dname][sname]
            print(f"   {sname} floor reading admits:")
            print(f"     PATTERN 95% [{iv['pattern_95'][0]:.1f}, "
                  f"{iv['pattern_95'][1]:.1f}]   99% [{iv['pattern_99'][0]:.1f}, "
                  f"{iv['pattern_99'][1]:.1f}]")
            print(f"     CENSOR  95% upper {iv['censor_95']:.1f} "
                  f"(K=4: {iv['censor_95_k4_stability']:.1f}; "
                  f"first-dilution rule: {iv['firstdilution_rule_95']:.1f})   "
                  f"99% upper {iv['censor_99']:.1f}")
        for age in (15, 60):
            for dnum in (5, 2):
                sub = summary[(summary["design"] == dname)
                              & (summary["culture_age_days"] == age)
                              & (summary["sample_day"] == dnum)]
                if not len(sub):
                    continue
                print(f"\n   {age}-day panel, day {dnum} "
                      f"(n floored = {int(sub['n_floored'].iloc[0])}):")
                for _, s in sub.iterrows():
                    print(f"     {s['method']:16s} single={s['single']:3d}  "
                          f"multiple={s['multiple']:3d}   "
                          f"[{s['count_interval_low']:.3g}, "
                          f"{s['count_interval_high']:.3g}]")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

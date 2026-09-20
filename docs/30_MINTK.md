# MINTK — Minimum Information for a Time-Kill assay

A reporting standard proposed by this project. Five fields that make a
reported tolerance endpoint (MDK_q, or a tolerance class derived from one)
recomputable by a reader against the assay's own measurement limits.

Motivation (this project's corpus screen, `src/experiments/exp45_screen_flow.py`):
of 78 candidate time-kill datasets assembled, 40 distinct literature deposits
could be inspected in full, and 32 of the 40 (80 per cent) state no assay
floor by any route — stated, derivable from a stated plated volume, or
inferable from the data. Their endpoints cannot be recomputed.

## The five fields

| # | Field | What to report | What fails without it |
|---|---|---|---|
| 1 | Starting density | N0 with its method (viable count or MPN value, not an optical density) | the endpoint is a fraction of N0; OD-derived densities disagree with measured ones by up to ~1.5-fold within one culture |
| 2 | Assay floor | L as a value, or the plated volume / dilution design that fixes it | nothing deeper than log10(N0/L) was ever visible; without L a "failed" endpoint is arithmetic |
| 3 | Censoring convention | what is written when nothing grows: zero, the floor value, ND, or the lowest table rung | the convention decides whether a floor reading is a bound or a measurement |
| 4 | Endpoint rule | the q in MDK_q and the interpolation between sample times | one kill curve returns different durations under different rules |
| 5 | Physiological state | culture age or growth phase at sampling, as a recorded value | tolerance labels track state; unrecorded, state confounds every group comparison |

## Notes per field

1. **Starting density.** Report the measured value per series, not the
   nominal inoculum. In this project's prospective experiment the nominal
   1e5 per mL was a measured median 1.215e6 per mL — a 12-fold gap that
   moved every headroom by 1.09 log10.
2. **Assay floor.** For a plate count, one colony in the plated volume v µL
   is L = 1000/v per mL (duplicate plating halves it; state the pooling).
   For an MPN design, L is the lowest rung of the table for the dilution
   series used; state wells per dilution, dilution factor, and first-well
   volume, because the rung's confidence interval — not just the rung —
   follows from them.
3. **Censoring convention.** A floor value written "23", "0", or "ND" are
   three different statements about the true count and they license three
   different analyses. Say which was written, and whether a value below the
   lowest rung was ever recorded.
4. **Endpoint rule.** MDK_q requires q and the rule interpolating between
   visits (linear on log counts, first crossing, nearest visit). This
   project's reanalysis found one deposit whose MDK values move by days
   under equally defensible rules.
5. **Physiological state.** Record culture age, growth phase at sampling,
   or a growth-rate covariate. In the clinical deposit analysed here the
   tolerance label tracks growth state, and its association with resistance
   runs largely through a ten-fold-lower starting density.

## Tooling

The checks behind fields 2 and 4 ship as a command-line tool so they run
when the experiment is planned, not after it:

```bash
python -m src.assay_geometry headroom --n0 2.3e4 --floor 23
python -m src.assay_geometry design   --n0 5e5 --endpoint 99.99
python -m src.assay_geometry floor    --deposit vijay
python -m src.assay_geometry observe  --n0 1e4 --n-final 23 --floor 23 --label Medium
```

`design` inverts the boundary: given N0 and a target endpoint, it returns
the minimum plated volume (or the MPN rung) the endpoint needs — the answer
to "could this experiment have demonstrated this endpoint at all", asked
before the first plate is poured.

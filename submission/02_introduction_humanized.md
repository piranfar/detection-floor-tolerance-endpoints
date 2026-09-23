## Introduction

Tuberculosis treatment runs for four to six months (1). Shortening it means
finding drugs that kill *Mycobacterium tuberculosis* faster, and that choice is
made in a flask: compounds are ranked by in vitro killing curves, counts of
surviving colonies read off a plate over time.

A plate count has a hard floor, and the pipette sets it. The smallest positive
result is one colony, and what one colony means depends on the volume spread:
plate 100 µL and a single colony is 10 bacteria per mL. Below that the plate
reports no growth, which is not the same as nothing there — a negative culture
taken after treatment has begun is not evidence of sterility, which is why blood
cultures are drawn before the first dose. We write *L* for that floor and *N₀*
for the starting density.

Tuberculosis makes that floor expensive, because the phenotype invoked to explain
why treatment takes so long is itself defined by a duration. Tolerance is the
capacity of a genetically susceptible population to survive an exposure that
should kill it: the drug still works, but the bacteria take a long time to die,
and that time is the measurement.

Rather than asking whether a culture has gone negative, the modern definition
asks how many logs the population fell. The minimum duration for killing (MDK),
the time to a specified fractional reduction of 90, 99 or 99.99 per cent, was
proposed as the tolerance counterpart to the minimum inhibitory concentration
(2, 3). The fraction is the whole point: a ratio to the starting population is
scale-free, so if the count falls in a straight line on a log scale at rate *b*,
the time to a *q*-log reduction is *q/b* and the starting density cancels. By
construction, MDK cannot be contaminated by how much culture went into the tube.

MDK as originally defined is not a plate-count metric. It was measured from the
presence or absence of survivors in microwell arrays of about a hundred cells, a
design chosen to avoid dilution plating, and the consensus guidelines specify how
the smallest detectable count should be established (3, 4). What this paper
examines is the form the tuberculosis field adopted: log-reduction endpoints
computed from plate counts and most-probable-number series. The floor problem
belongs to that implementation, not to the definition.

The property holds in the definition and fails in the measurement, and that gap
is what this paper is about. To show a four-log kill you have to see four logs
down, and what is visible is bounded below by the floor. An isolate therefore has
headroom *h* = log10(*N₀* / *L*), and no experiment can demonstrate a reduction
deeper than *h*, however completely the drug worked. Where *h* < *q*, the
endpoint is unreachable before the drug is added. We call this first boundary
reachability.

A second failure appears when the last count lands on the floor. The fraction
written down is then *L/N₀*, the floor divided by the starting density; the drug
has dropped out of it, and what is left is the pipette and the inoculum. A metric
designed to be inoculum-independent becomes a pure inoculum readout at exactly
the depth where tolerance is scored. We call this second boundary
identifiability.

Inoculum-dependent tolerance measurements have been reported before under a
different mechanism: an *Escherichia coli* persister assay gave different
tolerant fractions depending on growth phase and culture history, attributed
there to prophage induction rather than to an assay floor (5). That report
and this one agree on the symptom and differ on the mechanism, and neither rules
out the other operating in a given assay.

What has not been recognised before is what a floor-level reading becomes: a
classification rule. When the last count sits at *L*, the recorded fraction is
*L/N₀*, and the low, medium or high label is then a cut on starting density.
That is the gap this paper fills. Two further failures stay distinct from it: a
duration ceiling, where the assay stopped looking, is not a count floor, and
recording a below-limit flag is not the same as scoring a duration from the
points so recorded.

This study asks how deep a log-reduction tolerance endpoint can be measured at
all, and whether isolates have been assigned tolerance phenotypes from outside
that range. Two boundaries on the starting density follow from the definitions —
one deciding whether an endpoint is reachable, the other whether a floor-level
reading identifies a class — and both are computed from quantities a time-kill
protocol already records.

Answering that question needs data recording three quantities: a starting density
measured before treatment, a time series, and either a plated volume or a stated
floor. Most datasets do not record all three. Of 78 candidate time-kill datasets
assembled for this study, 45 were inspected in full; of the 40 distinct
literature deposits among them, **32 state no assay floor by any route**. That is
the first result, and it is why the five carried forward are five rather than
fifty (Table S1).

If the hypothesis holds, a tolerance call reported without its starting density
and its assay floor cannot be interpreted, and the phenotypes assigned in its
name are in part a record of how the assay was set up.

**Box 1. Four numbers that score an MDK.** *N₀* is the starting density. *L* is
the smallest positive count the method can report: one colony in a plated volume
*v* µL is *L* = 1 000/*v* per mL, and an MPN series uses the lowest table rung (6, 7).
Headroom is *h* = log10(*N₀*/*L*). A *q*-log endpoint is legal only if *h* ≥ *q*,
which is the same as seeding at or above *L* · 10^*q*. If the last reading sits
at *L*, the recorded fraction is *L*/*N₀*: an upper bound, not a measurement.

| Culture | *N₀* (per mL) | *L* (per mL) | Headroom | Legal endpoints | If the last reading is at *L* |
| --- | ---: | ---: | ---: | --- | --- |
| Thin clinical MPN | 23 000 | 23 | 3.00 | 90%, 99%, 99.9%; not 99.99% | Fraction 10⁻³. Low and medium both compatible: the rule cannot choose. |
| Adequate clinical MPN | 230 000 | 23 | 4.00 | all four, including 99.99% | Fraction 10⁻⁴. Only low is compatible. |
| 100 µL plate | 10⁵ | 10 | 4.00 | through 99.99%; not a 5-log call | Fraction 10⁻⁴. A 5-log MDK needs *N₀* ≥ 10⁶. |
| 10 µL drop, same *N₀* | 10⁵ | 100 | 3.00 | through 99.9%; not 99.99% | Fraction 10⁻³. The pipette, not the isolate, removed one log. |

The first two rows are the two starting densities that recur in the clinical
deposit analysed below, and Section 2 reports what became of the isolates that
began at each. The last two show why a written protocol does not standardise
measurable depth: the plated volume sets *L*. To make both a four-log endpoint
and a low class identifiable against *L* = 23 per mL, seed above
*L* · max(10⁴, 1/*c*₁) = 230 000 per mL, or choose a shallower endpoint.

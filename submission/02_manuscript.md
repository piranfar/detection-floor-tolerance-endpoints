---
title: "The detection floor bounds tolerance endpoints in Mycobacterium tuberculosis"
short_title: "The detection floor bounds tolerance endpoints in M. tuberculosis"
article_type: "Research Article"
keywords:
  - time-kill assay
  - limit of quantification
  - minimum duration for killing
  - antibiotic tolerance
  - colony counting
  - censored data
  - Mycobacterium tuberculosis
---

# The detection floor bounds tolerance endpoints in *Mycobacterium tuberculosis*

**Author:** Vahhab Piranfar¹

¹Independent Researcher, New York, NY, USA

ORCID: [0000-0003-3653-5739](https://orcid.org/0000-0003-3653-5739)

**Correspondence:** Vahhab Piranfar, vahab.p@gmail.com

**Figures:** 3 | **Tables:** 3 | **Boxes:** 1 | **Supplemental figures:** 2 | **Supplemental tables:** 22

---

## Abstract

A culture that grows nothing after antibiotics has never proved sterility, so
tolerance is scored by how far the count fell: the minimum duration for killing.
That endpoint is a fraction of the starting count, so the inoculum should cancel.
It does in the definition, and fails once killing reaches the assay's floor.
Seventy-eight published time-kill datasets were screened: of the 45 whose series
could be inspected in full, 36 state no assay floor by any route. Five are
reanalysed here — the floor derived in two, inferred in one and absent in two —
and one experiment tests this.

Two boundaries follow from the definitions. For a floor *L*, a *q*-log endpoint
is visible only above *L*·10^*q*; above
*L*/*c*₁, with *c*₁ the lowest class threshold, a floor-level reading fits only
the lowest class. Reaching the floor is the drug's doing; the label it permits is
not.

Of 217 *Mycobacterium tuberculosis* isolates classified for rifampicin tolerance,
33 began too close to the floor to show the 99.99 per cent reduction used, and
all 33 are recorded as failing. Of eighteen read at the floor, twelve admit one
class, six admit two. The label tracks growth state, not isoniazid resistance;
most of that runs through a ten-fold lower inoculum — the denominator it is cut
on.

Prospectively, *Escherichia coli* ATCC 25922 at the standard inoculum could
report 3.71–3.93 logs at 10 µL and 4.88–5.05 at 100 µL; at a cut of 10⁻³, six of
54 sample-times took two labels from one culture, the pipette alone deciding.
Across the plated volumes these laboratories actually used, 100 down to 2.5 µL,
demonstrable depth moves by 1.60 log10 as exact arithmetic.
A tolerance call reported without its starting density and assay floor cannot be
interpreted.

**Keywords:** time-kill assay; limit of quantification; minimum duration for
killing; antibiotic tolerance; colony counting; censored data;
*Mycobacterium tuberculosis*

## Introduction

Tuberculosis treatment runs for four to six months (1). Shortening it means
finding drugs that kill *Mycobacterium tuberculosis* faster, and that choice is
made in a flask: the compounds that could shorten a regimen are picked out of in
vitro killing experiments.

The experiment is simple. Grow the organism, add the drug, and at set times take
a sample, dilute it, spread it on a plate, and count the colonies. Each colony
stands for one bacterium that was alive when it was plated. The counts over time
are the killing curve.

Every clinical microbiologist already knows the trap in that last step. A culture
taken after antibiotics have started is not evidence of sterility. It is why
blood cultures are drawn before the first dose. A drug suppresses growth, injures
cells sublethally, carries over into the medium, and drives the population
beneath what the plate can see; the plate then reports absence, and absence is
not what happened. The rule is old, it is correct, and nobody disputes it.

The plate also has a hard floor, and the pipette sets it. The smallest positive
result is one colony, and what one colony means depends on how much you spread.
Plate 100 µL and one colony is 10 bacteria per mL. That is the floor. Anything
below it comes back as no growth, which is not the same as nothing there. Write
*L* for that floor and *N₀* for the starting density.

Tuberculosis makes the old rule expensive, because the phenotype invoked to
explain why treatment takes so long is itself defined by a duration. That
phenotype is tolerance: the capacity of a genetically susceptible population to
survive an exposure that should kill it. These bacteria are not resistant. The
drug still works on them. They just take a long time to die, and that time is the
measurement. A phenotype defined by a duration is defined by exactly the
observation the old rule warns about.

The field's response was not to ignore the warning but to engineer around it.
Rather than asking whether a culture went negative, the modern definition asks
how many logs the population fell: the minimum duration for killing, MDK, is the
time to a specified fractional reduction — 90, 99 or 99.99 per cent — and it is
proposed as the tolerance counterpart to the minimum inhibitory concentration
(2, 3). The choice of a *fraction* is the whole point. A ratio to the
starting population is scale-free: if the count falls in a straight line on a log
scale at rate *b*, the time to a *q*-log reduction is *q/b*, and the starting
density cancels. By construction, MDK cannot be contaminated by how much culture
went into the tube. That is the property it was built to have.

The property holds in the definition. It does not hold in the measurement, and
the gap between the two is what this paper is about. To show a four-log kill you
have to be able to see four logs down. A *q*-log reduction can be estimated only
if *q* logs are visible, and what is visible is bounded below by the floor. So an
isolate has

    headroom  h = log10(N₀ / L)

and no experiment can demonstrate a reduction deeper than *h*, however completely
the drug worked. Where *h* < *q* the endpoint is unreachable before the drug is
added. That is the first boundary, and we call it reachability.

It gets worse when the last count lands on the floor. The fraction written down
is then *L/N₀* — the floor divided by the starting density. It is not a
measurement of how many survived. The drug has dropped out of it, and what is
left is the pipette and the inoculum. The metric designed to be
inoculum-independent becomes a pure inoculum readout precisely at the depth where
tolerance is scored. That is the second boundary, and we call it
identifiability.

The closest statement of the bound is in the framework's own methods paper, and
we claim no priority over it. Brauner and colleagues, presenting a direct
measurement of tolerance that deliberately avoids time-kill curves, scale the
inoculum to the endpoint being measured: a hundred bacteria per well to determine
MDK99, a thousand for MDK99.9, and so on (3). That is the reachability
inequality of this paper, with the floor idealised at one cell per well and a
grew-or-did-not-grow readout in place of a count. What has not been done is to
carry the rule back into plate-count time-kill, where the floor is not one cell
but a concentration fixed by the plated volume — 10 to 400 CFU/mL across the
deposits reanalysed here — and must therefore be measured sample by sample rather
than assumed; nor to ask what the published record looks like where the rule was
not applied.

No prior treatment converts a floor-level reading into the classification rule
it becomes. When the last count sits at *L*, the recorded fraction is *L*/*N*₀, and
the low, medium or high label is then a cut on starting density. That is the gap
this paper fills. Two further failures have to be kept distinct from it. A
duration ceiling — the assay stopped looking — is not a count floor, which is the
plate being unable to see. And recording a below-limit flag is not the same as
scoring a duration from the points so recorded.

This study asks how deep a log-reduction tolerance endpoint can be measured at
all, and whether real isolates have been assigned tolerance phenotypes from
outside that range. Two boundaries on the starting density follow from the
definitions — one deciding whether an endpoint is reachable, the other whether a
floor-level reading identifies a class — and both are computed from quantities a
time-kill protocol already records. Neither asks a laboratory to measure anything
new.

Answering that question at all requires deposits that record the three quantities
the arithmetic needs — a starting density measured before treatment, a time
series, and either a plated volume or a stated floor — and most do not. We
assembled and inspected 78 candidate time-kill datasets one at a time. Of the 45
whose series could be read in full, **36 state no assay floor by any route**:
not a limit of detection, not a limit of quantification, not a plated volume from
which one could be derived. That number is not a preamble to the analysis; it is
the first result, and it is why the five deposits carried forward are five rather
than fifty.

We test the two boundaries on the classification and the assay geometry of 217
clinical isolates, then ask what the resulting phenotype tracks: drug
susceptibility, or the physiological state of the culture. Four further deposits
carry the question beyond one clinical panel — a six-laboratory consortium
exercise distributing one strain under one written protocol (4, 5), a
concentration-by-time grid in the same organism (6, 7), a panel of evolved
clones in which the concentration and duration axes can be checked for
independence (8), and a hollow-fibre deposit (9, 10) held out until
every boundary was fixed. All five are published and openly licensed, and none
was generated for this study (Table 1). The two boundaries are then tested forward
rather than backward, in a prospective experiment built to break them, with every
prediction written down before a plate was counted.

If the hypothesis holds, a tolerance call reported without its starting density
and its assay floor cannot be interpreted, and the phenotypes assigned in its
name are, in part, a record of how the assay was set up.
---

**Box 1. Four numbers that score an MDK.** *N₀* is the starting density. *L* is
the smallest positive count the method can report — one colony in a plated volume
*v* µL is *L* = 1 000/*v* per mL, and an MPN series uses the lowest table rung (11, 12).
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
began at each. The last two are why a written protocol does not standardise
measurable depth: the plated volume sets *L*. To make both a four-log endpoint
and a low class identifiable against *L* = 23 per mL, seed above
*L* · max(10⁴, 1/*c*₁) = 230 000 per mL, or choose a shallower endpoint.

---

## Results



### 1. The plate's floor sets how far down killing can be seen

The most probable number (MPN) readings can only take the discrete values of an
MPN table (11, 12) — a fixed ladder of rungs, not a continuous scale. The
day-5 column does not taper towards zero. It stops. Eighteen isolates sit at
exactly 23 per mL in the 15-day panel and six in the 60-day panel, and nothing in
the file lies below that (Fig. 1A). That is a floor, not a tail, and it is
treated as one throughout.

The deposit never states its limit of quantification (13), so the floor has to
be inferred, and the inference is quantified rather than asserted. A posterior
over the MPN rungs at or below the lowest observed value — a probability spread
across which rung is the real floor — places 95 per cent support on 9.2 to 23 per
mL, a span of 0.40 log10. That is narrow enough that the class labels of
Section 3 are computed rather than refused (Table S1). Where a deposit gives no
such evidence, the labels are refused instead of reported.

The deposit carries a second classification, scored at day 2, and it sits on a
different floor. The day-2 column bottoms out at 230 per mL with eighteen
readings resting there, so *L* = 230 there. That is the same count as at day 5,
and it is a coincidence of this deposit rather than one number written into two
places: the two columns rest on different floors and share no reading. The day-2 class thresholds are not
stated in the source either, and they are recovered the same way as the day-5
ones: cuts at 10⁻² and 10⁻¹ reproduce all 203 usable day-2 classes with no
disagreement, one decade shallower than at day 5. Floor and lowest threshold both
shift by a factor of ten, so the identifiability boundary does not move:
*N*_id = 230/10⁻² = 23 000 per mL, the same value as at day 5. The reachability
boundary does move, by a decade, and the consequence is large. Against the day-2
floor, 121 of 203 isolates have too little room for a four-log reduction; against
the day-5 floor, 31 of those 203 isolates do. Eighteen day-2 readings rest on
their floor, eleven with a single compatible class and seven with more than one.
At 60 days no pair of decade cuts reproduces the day-2 classes (109 of 197), so
that rule is not a decade threshold on the recorded fraction, and no day-2
accounting is offered for it.

Each isolate therefore carries a fixed budget of killing the assay can see. At 15
days of prior culture the starting densities span 3.36 to 7.79 log10, so headroom
— the distance from the starting density down to the floor — spans 2.00 to 6.42
log10 (Fig. 1B, Table 2). Both spans are the same 4.42 log10, and the fold
figures quoted throughout are ten raised to the unrounded difference rather than
to the displayed one. Against that budget the three deposited endpoints behave
very differently. Every isolate has the room for a 90 or a 99 per cent reduction:
0 of 217 fall short in both cases. **Thirty-three of 217 isolates — 15.2 per
cent — lack the headroom for the 99.99 per cent endpoint**, which is to say that
a four-log reduction was unobservable for them before rifampicin was added. Two
of those 33 carry a fourth label that the deposit writes literally as "MDR",
conventionally multidrug-resistant. It is unordered with respect to the other
three, so no ordered analysis can place it (Table S2); over the 203 isolates with
an ordered label the same count is the 31 quoted above.

All 33 are recorded as not having reached the endpoint — they sit at the **assay
ceiling**. That is a census of the affected isolates, not an estimate. The
ceiling is a different censoring
mechanism from the floor and should not be read as its mirror. The floor censors
the count: anything below *L* is not reported as a count. The ceiling censors
time: the killing assay runs six days, so an isolate that has not reached its
endpoint by then is recorded at the last day rather than at the day it would have
reached. One sets how deep the assay can see, the other how long it looks.
Among the 184 isolates that did have four logs of headroom, 162 are also at the
ceiling, 88.0 per cent.

No p-value is attached to that contrast, and the reason is worth saying out loud
rather than hiding in a caveat. An isolate with less than four logs of headroom
cannot record a four-log reduction. The 0 of 33 cell is fixed by arithmetic, not
by biology, so the null of independence between ceiling status and headroom is
false before any data are seen. A test of an impossible null still returns a
number, and that number means nothing. The census is the finding: every isolate
that could not reach the endpoint is recorded as not having reached it, and 88.0
per cent of those that could are recorded the same way. The deepest endpoint is
therefore the only one at risk, and it is the one the tolerance classification is
built on.

### 2. The same floor reading was given different tolerance labels

The deposited tolerance level is a cut-off on the recorded surviving fraction,
with no overlap between classes. The thresholds themselves are not deposited.
They are recovered here, and the data pin them only to the gaps between classes:
at day 5 and 15 days of prior culture, low tolerance covers fractions below 10⁻³,
medium covers 10⁻³ to 10⁻², and high exceeds 10⁻². Those cuts reproduce every
usable class in the file, 203 of 203 (Table S3). Usable means the 203 of 217
isolates whose label is one of the three ordered classes; the other 14 carry the
fourth, unordered category, the "MDR" label above, that no ordered analysis can
place (Table S2). So what follows is an argument about the fraction the assay
recorded, not about an independent clinical judgement.

Eighteen isolates ended at the floor. They share one reported floor-level
observation, but their true final counts are unknown below the floor, so the
assay cannot tell their surviving burdens apart down there. That is not the same
as saying they were killed to the same degree, and the difference matters. Their
starting densities span 265-fold, from 23 000 to 6.1 × 10⁶ per mL, so the same
terminal reading implies a different range of compatible reductions in each. An
isolate that began at 23 000 has demonstrated at least a 3.00-log reduction; one
that began at 6.1 × 10⁶ at least 5.42 logs. In either case the true reduction may
be anything from that bound down to complete kill. What the deposit records
instead is a single number per isolate, *L*/*N₀*, and those recorded fractions
span 265-fold, from 3.8 × 10⁻⁶ to 1.0 × 10⁻³ — exactly the span of the starting
densities (Fig. 1C), because that is what the ratio is. They are upper bounds on
survival, not measurements of it.

The labels those eighteen received differ. Six isolates that began at 23 000 per
mL received a fraction of 10⁻³ and were classified **medium** tolerance; twelve
that began at 230 000 or above received 10⁻⁴ or less and were classified **low**.
A single cut on the starting density alone reproduces all eighteen (Table 3).
That is a statement about the classification step and not about the killing: once
a reading is censored at the floor, the starting density fixes which label the
published rule is able to return.

The question this raises is not whether those labels are wrong but which labels
the published rule could have returned once the reading came back at the floor. A
censored reading places the true count somewhere between zero and *L*. Sweeping
the true count across that range and applying the deposited thresholds gives the
set of classes compatible with the observation. For the twelve isolates that
began at 230 000 per mL or above, every count the assay admits yields a fraction
below 10⁻³, so **low** is the only class compatible with a floor-level reading.
For the six that began at 23 000, the compatible set spans the low–medium
threshold and the rule cannot choose between two classes.

Three questions have to be kept apart here, and the rest of this paper keeps them
apart. Whether a culture reaches the floor at all is a question about the drug:
rifampicin has to reduce the population by that isolate's entire headroom for it
to happen, and the starting density does not by itself decide it. Which label the
rule assigns once the reading is censored is a question about arithmetic: there
the starting density determines the compatible set, and for twelve of these
eighteen that set has one member. How far the population actually fell is a
question the assay leaves open, since the true count lies anywhere below *L*. The
first is biology, the second is bookkeeping, and the third is unmeasured.
Conflating them is the error this paper is about.

So for twelve of the eighteen the recorded label carries no information beyond
the fact that the reading was censored, and for six it is not determinate at all.
None of the eighteen is a measurement of the surviving fraction.

Sorting every call in the panel this way separates the labels the assay measured
from the labels the censoring rule fixed (Table 3). At 15 days of prior culture,
185 of 203 calls rest on a reading above the floor and are measured; for 12 the
reading is censored and only one class is compatible with it; for 6 the reading
is censored and more than one class is compatible. At 60 days the counts are 191,
6 and none, because the cultures are denser and few readings reach the floor.

The larger effect is at the deeper endpoint, and it falls unevenly on the groups
a study would compare. The 99.99 per cent endpoint is unreachable for 22 of 84
isoniazid-resistant isolates, 26.2 per cent, against 9 of 119 susceptible ones,
7.6 per cent (Fisher exact p = 0.00056 (14)); the remaining two of the 33 are
MDR and fall outside that contrast. Their median headroom differs by a full log,
4 against 5. A comparison of tolerance between those groups is therefore in part
a comparison of how well each group could be measured, which is the disposition
the previous section quantifies.

### 3. The affected isolates are named before the drug is added

Sections 1 and 2 counted isolates. The two boundaries derived in the Methods
do more than that. Given
only the floor, the class thresholds and each isolate's starting density, they
say in advance which isolates are affected, before any day-5 reading is used.

For this assay *N*_reach = 23 × 10⁴ = 230 000 per mL and *N*_id = 23/10⁻³ =
23 000 per mL. Applied to the 15-day panel, the first predicts 33 isolates unable
to reach the 99.99 per cent endpoint. The second predicts that of the eighteen
isolates whose reading rests on the floor, twelve have only the lowest class
compatible with that reading and six have more than one. Those are the three
counts Sections 1 and 2 report.

Neither boundary predicts which isolates reach the floor; that depends on what
rifampicin does. Both predict what a reading at the floor can be made to mean
once it happens, and there the agreement with the deposit is exact isolate by
isolate: the set the algebra says has a single compatible class and the set the
deposit records in the lowest class are the same set.

That agreement is an identity rather than a passed test. Once the label is a cut
on the recorded fraction
(Table S3) and every floor reading has a numerator of exactly *L*, the class of a
floored isolate is a function of *N₀* alone, so the algebra cannot disagree with
the deposit. What could have failed, and did not, is the premise: that the three
classes separate cleanly on the recorded fraction at all, in 203 of 203 calls.

How finely the agreement resolves also has to be stated. Among the eighteen the
starting density takes only five values — 23 000 for six isolates, then 230 000
for eight, and 610 000, 2.3 × 10⁶ and 6.1 × 10⁶ for one, one and two — and **no
isolate lies strictly between *N*_id and *N*_reach**. Any cut placed anywhere in
that decade reproduces the same twelve-six split, so the split locates the
boundary only to within an order of magnitude and is not by itself a sharp test
of where it sits.

What is sharp is the boundary case, and it is the part of this section that
discriminates. Six isolates sit at exactly 23 000 per mL, which is *N*_id itself.
For them *L*/*N₀* equals *c*₁ exactly, the interval [0, *L*/*N₀*] touches the
threshold from below and spans two classes, and the strict inequality fails.
Those six are precisely the six the deposit records as medium rather than low. A
rule written with the inequality the other way would have called all six low and
been wrong six times out of six. That is a test the arithmetic could have failed
and did not, and it is what licenses using the boundary in advance: given a
floor, a set of thresholds and a starting density, the affected isolates can be
named before any reading is taken.

The empirical findings are therefore consequences of the definitions rather than
properties of this deposit, and the claim is a prediction that any dataset
reporting a starting density, a floor and a threshold classification can be
checked against.

### 4. The label tracks how fast an isolate grows, and its link to resistance cannot be separated from the inoculum

We asked what the deposited tolerance label goes with. There are two candidate
predictors, and each is tested at two culture ages and at two endpoint depths,
which is eight tests in all. Eight tests on one question will throw up a false
positive on their own, so we correct them together as one family. Two survive
(Table S4).

The label tracks the **growth rate** of the isolate. Slower growth goes with a
higher tolerance class, and it survives adjustment for starting density
(OR 1.096 per day of time to OD 0.4, 95 per cent CI 1.032 to 1.164, p = 0.0030,
n = 202; unadjusted OR 1.126, 1.062 to 1.193). The label also tracks **isoniazid
resistance** — until the starting density enters the model. On its own, a
resistant isolate has 2.32 times the odds of a higher tolerance class (95 per
cent CI 1.30 to 4.12, p = 0.0042). Adjusted for starting density the odds ratio
falls to 1.31 (0.67 to 2.57, p = 0.42), and the interval no longer excludes one.
We call that attenuation, not elimination. Starting density is the strongest
term in the file: every ten-fold rise in the starting most probable number halves
the odds of a higher tolerance class (OR 0.480, 0.340 to 0.677,
p = 2.9 × 10⁻⁵).

Why the adjustment does that is measurable. Isoniazid-resistant isolates go into
this assay at 5.36 log10 against 6.36 for susceptible isolates, ten-fold thinner
(Mann–Whitney p = 9.1 × 10⁻¹⁴) (15), and 26.2 per cent of them lack the
headroom for the deepest endpoint against 7.6 per cent of susceptible isolates
(Section 2). They are one log short of observable killing before the experiment
begins.

A percentage attenuation is a description, not a quantity a model estimates, so
we estimated the path directly. The total effect of resistance on the tolerance
class splits into two parts: the part that runs through log10 starting density
and the part that does not. On the 203 isolates with a usable class, rather than
the 202 the association family retains, the mediated part is +0.166 classes
(bootstrap 95 per cent CI +0.067 to +0.279) and the direct part +0.091 (−0.116 to
+0.287). About 65 per cent of the association therefore travels through the
inoculum, and the direct path covers zero. Restricting to baseline isolates
leaves the mediated path intact (+0.159, +0.053 to +0.295), and collapsing the
outcome to two levels agrees (Table S5).

Two things bound that estimate, and neither is a formality. It rests on
sequential ignorability — that nothing unmeasured drives both the starting
density and the class — which no observational file can establish. A residual
correlation of about −0.23 between the mediator and outcome errors would nullify
the point estimate, and one ordinary measured covariate already moves it about
forty per cent of that way. More fundamentally, the step in the middle is the
denominator of the ratio the outcome is cut on. The tolerance class is a
threshold on *N*₅/*N₀*, so a decomposition that routes resistance through *N₀* is
in part recovering the censoring arithmetic this paper is about rather than a
biological pathway from resistance to tolerance. That is not a reason to discard
the estimate — it is the quantity a reader wants, because it says how much of the
association is carried by the label's own denominator — but it is a reason not to
read it as a mechanism. Only a design that fixes the inoculum separates the two.

These 217 isolates are not 217 independent patients, and the deposit carries no
patient key with which to say so in a standard error. What it does carry is the
exact substitute: a baseline-only stratum in which every isolate comes from a
different patient by construction (Time_point = 0M, n = 167 at 15 days).

In that stratum the two surviving associations part company. Growth holds and
still survives correction (OR 1.116, 1.040 to 1.198, p = 0.0024). Resistance does
not: OR 2.11 (1.07 to 4.16, p = 0.031). It ranks second in the family of eight,
so under Benjamini–Hochberg it must beat a critical value of 0.0125, and it does
not. The resistance association therefore leans on isolates that are not
independent of one another, and it is already the association that starting
density explains away. We report it as the weaker of the two on both counts.

The two surviving associations sit in the 15-day panel, which is where the
mechanism places them. By 60 days the cultures are 38-fold denser, the spread of
starting densities has more than halved, from an interquartile range of 1.00 to
0.42 log10, and the fraction of isolates short of headroom falls from 15.2 to 3.3
per cent. The confound is a property of a thin assay, and it thins out when the
assay is not thin. The two panels are columns on the same spreadsheet rows — 210
isolates appear in both — so every comparison between them is within-isolate and
is made that way. Pairing sharpens the result rather than softening it: 26
isolates lose their headroom shortfall between panels and none acquires one
(exact McNemar p = 3.0 × 10⁻⁸ against an unpaired p of 2 × 10⁻⁵) (16), eleven
leave the floor and none joins it (p = 9.8 × 10⁻⁴), and every isolate whose
headroom changes gains (Wilcoxon signed-rank p = 1.3 × 10⁻³³) (17). The
interquartile range of starting density falls by 0.58 log10.

It does not vanish, and the ordinal treatment is what shows where it goes. The
one-odds-ratio-for-both-cuts assumption holds throughout the 15-day panel but
fails at 60 days for starting density at the deepest endpoint (Brant p = 0.0031;
likelihood-ratio test against a released fit p = 0.0062). Let that coefficient
differ between the two cuts and the whole effect lands on the upper one: the odds
ratio for clearing medium is 0.493 (0.336 to 0.724, p = 0.0003) against 0.951 for
clearing low (0.647 to 1.396, p = 0.80). A multinomial fit, which assumes no
ordering at all, agrees (high against low, relative risk ratio 0.59, p = 0.028;
medium against low, 1.22, p = 0.39). In the denser panel the starting density no
longer decides who is called low. It still decides who can be called high. A
single averaged slope, ordinal or linear, would have reported that as a null.

### 5. One written protocol does not give every laboratory the same depth to look down

If the effect is a property of assay geometry rather than of clinical sampling,
it should appear where one protocol, one strain and one stock are handed out
deliberately. Van Wijk and colleagues (2023) ran exactly that exercise, sending a
single stock of H37Rv to six blinded laboratories under one written protocol
(4, 5). It does.

At ten times the minimum inhibitory concentration of moxifloxacin all six
laboratories return a positive kill rate, and the rates span 5.2-fold, from 0.090
to 0.464 log10 CFU/mL per day. Across all 30 laboratory-by-arm cells the Tobit
estimate — a fit that treats a below-floor reading as below the floor rather than
as a number — and the imputation estimate never differ by more than 0.006 log10
per day (Fig. 2A, Table S6). That agreement says the fit is not an artefact of the
arithmetic used to reach it. It does not say the sub-floor assumption is safe:
both estimators assume the same normal distribution below the floor, and nothing
in this deposit can check that assumption from the inside.

The two orderings do not correspond. Rank the laboratories by starting density
and the three lowest are exactly the three that recorded crossings, the three
highest exactly the three that did not, without exception. Rank them by kill rate
and there is no such correspondence (Fig. 2B). Institute F has the highest
starting density at 6.53 log10 among the treated flasks of this arm, kills
faster than four of the other five at 0.223
log10 per day, and records no crossing. Institute E returns the slowest rate of
all at 0.090 and also records none.

What the adjustment establishes is descriptive and is worth stating as such: a
continuous measure of where the cultures began accounts for the laboratory term
at least as well as the laboratory label does, and one institute resists even
that. What can be tested, because flasks are exchangeable across laboratories
under the null, is how much of each quantity the laboratory owns. It owns 87.0
per cent of the variance in starting density (permutation p < 0.0002) and 36.8
per cent of the within-arm kill rate (p = 0.0018). It owns the duration endpoint
outright, since three laboratories produce none at all. <!--supp-->### 6. The turbidity standard fixes what goes into the flask, not what the plate can see

The inoculum for a time-kill experiment is not a free choice. You match a
suspension to 0.5 McFarland and dilute it, and NCCLS M26-A (approved guideline,
1999; the body is now CLSI, which has archived the document) puts the target near
5 × 10⁵ CFU/mL (18). If the protocol fixes the starting density, then the
variable the preceding sections rest on does not vary.

Two things about the standard let counts settle this. First, a McFarland reading
is a turbidity — how cloudy the tube looks, matched optically (19) — and
cloudiness counts live cells, dead cells, debris and a clump of cells all as one
particle (19). Converting it to CFU/mL assumes a cell size, a shape and a
dispersal that *M. tuberculosis* does not oblige, and tuberculosis protocols work
from a range of dilutions and target inocula (20). Second, the standard fixes
what goes into the flask. What matters here is what the plate counts, and between
the two sit a dilution, a transfer, and whatever clumping happens on the way.

In the six-laboratory exercise, the untreated flasks at day zero on the 100 µL
plating actually started at 3.67, 4.61, 4.65 and 6.00 log10 CFU/mL, for institutes
B, C, D and F. Institute E deposits no untreated day-zero reading at any volume;
its series begins at day one. Institute A's three readings at that plating are
flagged above the quantification limit rather than counted. Three of the four sit
below the M26-A target, by 11-, 12- and 107-fold; the fourth sits two-fold above
it. Every figure in this section is on that one basis — untreated, day zero,
100 µL. That is not the basis of Table S6, and the two are not expected to match.

Read as headroom at a fixed plating volume, the spread is Δ*h* = 2.33 log10 — a
216-fold difference in how far down the assay can look, under one written protocol
(Table S7). That figure is small, so its roster has to be stated. It is the largest
value minus the smallest over those same four laboratories: B at *h* = 2.67, C at
3.61, D at 3.65 and F at 5.00. Each sits exactly one log10 below the density above
it, because *L* = 10 CFU/mL at this plating. Institute A's other platings put it
near *h* = 2.4, so including it would widen the spread rather than narrow it. A
range over four draws is a fragile statistic: its cluster-bootstrap 95 per cent
interval runs from 0.05 to 2.33 log10, and the upper limit is the observed range
by construction.

The stronger version of the argument does not depend on that roster at all. Let
the plated volume vary too and the spread widens to Δ*h* = 4.40 log10. Of that,
1.60 log10 is exact arithmetic on *L* = 1000/*V*; it carries no sampling
uncertainty whatever. The pipette moves the measurable depth further than the
laboratories differ.

The obvious counter-explanation is early killing. If the drug had already acted by
the day-zero reading, a spread in those readings would be kill and not inoculum.
Only institutes C and D deposit a day-zero reading in both arms, and there the
treated and untreated flasks agree to 0.06 and 0.13 log10, so for those two the
spread is the inoculum and not early kill. The other four cannot be checked this
way. Institute F shows why the check matters and why it is not decisive: its
treated day-one readings average 6.62 log10, above its untreated day-zero reading
of 6.00 — but the untreated culture itself grows to 6.72 over the same
twenty-four hours. A day-one reading is not a day-zero reading, in either
direction. A second deposit (9, 10) gives the same result against its own
stated figure rather than against a standard: its Methods specify 10⁵ CFU/mL and
its file measures 7 × 10⁵ to 2.8 × 10⁶, a median of 1.215 × 10⁶ and so 12.15-fold
above nominal — computed from the unrounded median, which Table S7 displays rounded
to 6.08 log10.

Distance from the McFarland reference is descriptive and is reported as such
(Table S8). Sitting far below it is the intended state, since the inoculum is
prepared by diluting from it, and the figure is not a measure of protocol
compliance. What sets the deepest log-kill an experiment can show is the measured
starting density and the real assay floor — not the turbidity the preparation
began from.

### 6. The same boundaries hold in an experiment the framework never saw

Every section so far tests the framework on the deposits it was built from, and
all of them are *Mycobacterium tuberculosis*. A search of five general
repositories, the tuberculosis consortia, the persistence literature, food
microbiology and the hollow-fibre field returned one deposit that carried all
three fields the boundaries require and could be analysed cold.

The point of this section is a deposit opened after every boundary and threshold
was fixed, and only one deposit qualifies on that ground.

Dubey and colleagues (2026) report amoxicillin-clavulanate against *Escherichia
coli* in a hollow-fibre system (9, 10). Their Methods state 100 µL plated
with counts per mL, so *L* = 10 CFU/mL is derived rather than inferred, and the
file corroborates the derivation: a 100 µL plate reporting per mL can return only
multiples of ten, and all 229 genuine counts in the deposit are multiples of ten,
the smallest exactly ten. Sixty-nine further entries read as one, which no 100 µL
plate can produce; they are the deposit's placeholder for below the floor.

Across the 20 cultures with a measured day-zero density, headroom runs from 4.85
to 5.45 log10. Endpoints at 1, 2, 3 and 4 logs are reachable for every culture. A
5-log endpoint is unreachable for 5 of 20. A 6-log endpoint is unreachable for all
20 (Table S9). On data it was not built from, the framework therefore locates the
depth at which a sterilisation claim in this experiment stops being demonstrable.

Two features of that deposit are worth recording because they are the failure
modes this framework is meant to catch. Its Methods give a nominal inoculum of
10⁵ CFU/mL while the file measures a median of 1.215 × 10⁶, so taking *N₀* from
the Methods rather than from the data would have placed a full order of magnitude
into every boundary. And its treated arm reads at or below the floor already at
day zero while the paired control reads about 10⁶, so that sample was drawn after
exposure rather than before it.

### 7. Read the plate late enough and the concentration response reverses

The deposit tests apramycin at 1, 4, 8, 32 and 128 µg/mL (6, 7). The 1 µg/mL
flasks grow rather than die, so that arm is left out of the dose comparison. What
remains is 4 to 128 µg/mL: 32-fold, five doublings. Across that range the
survivor counts spread out 6.9-fold at day 3, 48.2-fold at day 7 and 5.2-fold at
day 14 (Fig. 3, Table S10). The spread opens, then closes again. An experiment
read at 14 days would report this drug as insensitive to a 32-fold change in
dose. Each interval is fitted on its own, resampling all three replicate counts
with replacement at both ends of every interval, 20 000 draws. Over days 0 to 3,
each doubling of the dose adds +0.059 log10 per day to the kill rate (95 per cent
percentile interval +0.033 to +0.083). Over days 3 to 7 it adds +0.033 (+0.008 to
+0.059). Over days 7 to 14 it adds −0.025 (−0.035 to −0.015). Early against late
is a firm difference (+0.084, +0.055 to +0.111). Early against middle is not
(+0.026, −0.011 to +0.062). So concentration dependence is positive early, still
positive but smaller in the middle, and reversed late — and the reversal, not
just the shrinkage, is what a 14-day readout would be measuring.

We do not claim the late slope is truly negative. By day 14 the highest arm is
down to 65 CFU/mL, and the deposit states no limit of quantification and no
plated volume, so its floor cannot be worked out. Put the floor at 100 CFU/mL or
above — the value 10 µL plating would give, an assumption and not a derivation —
and that arm has already dropped below what its plate can count. Its readings are
then censored: recorded only as "below the floor", true value unknown. The rate
read off them is a lower bound. What holds whatever the floor turns out to be is
that the separation collapses.

### 8. One culture, two plated volumes, two tolerance labels

Every result above reads data somebody else generated for another purpose. This
one reads an experiment built to try to break the two boundaries *N*_reach and
*N*_id — the starting densities that decide whether an endpoint is reachable and
a label means anything — with its predictions written down before a plate was
counted. *Escherichia coli* ATCC 25922, of the American Type Culture
Collection — the reference strain the standard names for quality control —
against ciprofloxacin at ten times the concentration that stops it growing. Three
seeding densities, two plated volumes, three flasks each, 216 plate readings.

The middle arm was seeded on purpose at the 5 × 10⁵ per mL the standard
specifies. The densities actually reached were 6.4 × 10⁴, 4.4 × 10⁵ and
3.8 × 10⁶ per mL, quoted as arm means. Those three figures are means and every
figure after them is per flask, which is a distinction this experiment cannot
leave implicit, because it decides a verdict. Taking the low arm as a single
number gives it 3.81 logs of headroom at the 100 µL plating and rules the
four-log endpoint out; taking its three flasks one at a time gives 4.19, 4.11 and
4.00, and rules it in for all three. The arithmetic is the same and the answer is
opposite, because *N*₀ is not a setting the protocol supplies but a measurement
made once per flask — which is this paper's own argument, met in its own data.
Everything below is therefore reported per flask. **At the standard inoculum
plated at 10 µL, the deepest reduction the three flasks could report ran from
3.71 to 3.93 logs — each flask's own ceiling, not the drug's** — while those same
three cultures plated at 100 µL ran from 4.88 to 5.05 (Table S11). Every flask is
paired with itself across the two platings, so the comparison is within a culture
rather than between cultures.

The gain the pipette buys is exactly one log, because the floor at the pooled
100 µL plating is one tenth of the floor at the pooled 10 µL plating. The nine
paired gains are not exactly one log: they run 0.87 to 1.19 (Table S11). The
difference is not the drug and not the flask. It is that each plating measures
its own starting density from the same culture, and the two measurements
disagree — 425,000 against 565,000 per mL in one flask, 255,000 against 375,000
in another. That disagreement is this paper's own argument turned on its own
experiment: *N*₀ is not a constant a protocol supplies, it is a measurement with
error, and the headroom computed from it inherits that error. Reported per
flask, the gain never falls below 0.87 log10, so the four-log endpoint moves
from unreportable to reportable in every one of the three cultures at the
standard inoculum.

That much is arithmetic, as Box 1 says. So is the next step. When both platings
of one sample rest on their own floors, the two fractions written down are
*L*₁/*N*₀ and *L*₂/*N*₀ — two different floors over one starting density — so
they can fall either side of a class threshold and give one culture two labels.
**The quantity that could have come out zero is how often a real experiment lands
in the window where those two fractions straddle the cut**, and it depends on
where the cut is (Table S12). Put the cut at one per cent and the window is
nearly shut. Put it at one in a thousand, which is where the clinical
classification analysed above cuts its lowest class, and six of 54 sample-times
receive two different labels from one culture — one in nine.

That figure is computed with a single starting density per flask, and it has to
be, because the sentence above says *L*₁/*N*₀ and *L*₂/*N*₀ — one denominator.
The experiment can also be read the way a laboratory would actually run it, with
each plating series carrying the starting density it measured for itself, and
then the count is nine of 54 rather than six. The three extra are not the pipette.
They are the two platings disagreeing about how much culture went in: across the
nine flasks those two estimates differ by 0.74- to 1.53-fold, median 1.12. Both
numbers belong in the record. Six is what the plated volume does on its own, and
it is the claim this section makes; nine is what a laboratory would see, because
in a real experiment the starting density is measured too, and it is measured
with error.

---

## Discussion

Every clinical microbiologist knows that a negative culture taken under
antibiotic exposure is not proof of sterility. That is not what this paper
reports. What it reports is that the number brought in to replace that judgement
carries the same defect — and once it is a number, it is harder to see.

The minimum duration for killing was built to divide the starting density out,
and in the definition it does. It stops the moment killing reaches the plate's
floor, for a reason that is arithmetic rather than statistical: from there the
fraction written down is *L*/*N₀*, and the drug has dropped out of it.

Fifteen per cent of the clinical isolates examined here could not have shown the
deepest endpoint whatever the drug did to them, and every one of them is recorded
as having failed to show it. Eighteen more ended on the floor, and one threshold
on their starting density reproduces every label they were given. Whether those
cultures reached the floor is a question about rifampicin. Which label they
received once they were there is a question about arithmetic, and the starting
density settles it.

It is worth saying how far this reaches. The claim is scoped to the floor and no
further. In the 15-day panel, 12 of 203 usable calls have a single compatible
class and 6 have more than one; the other 185 rest on a fraction that was
actually measured. The kill rate still carries more of the variance in crossing
time than the distance does, in every multi-laboratory arm. So what fails
everywhere is not every tolerance call. It is the *interpretability* of a deep
log-reduction call reported without *N₀* and *L*. What the inoculum settles is
the subset of labels for which killing had already reached the floor.

The failure is specific and it is bounded. In this deposit neither the 90 nor
the 99 per cent endpoint is compromised: every isolate has the room to show
both. It is the 99.99 per cent endpoint that a substantial minority cannot
reach, and that is the deep endpoint the clinical classification uses. Being
that specific is what makes the problem fixable rather than fatal.

This is a derivation rather than an observation, which is what lets anyone test
it on their own plates. Both boundaries follow from the definitions alone and
neither refers to the drug or the strain: give them a floor, a set of class
thresholds and a starting density, and they name the affected isolates in
advance. In the clinical deposit they name them exactly, and the part of that
agreement which could have gone the other way — the six isolates sitting on
*N*_id itself, where the strict inequality leaves the class undecidable — goes
the way the boundary predicts. In a deposit the framework was not built from it
locates the depth at which a sterilisation claim stops being demonstrable: five
of twenty cultures cannot show a five-log reduction, and none of the twenty can
show six.

Everything above is read backwards, out of files made for other purposes, and a
derivation that only explains the past is worth less than one that survives being
aimed at the future. So *N*_reach and *N*_id were used to design an experiment
against themselves, with the predictions written down before a plate was counted.
At the inoculum the standard specifies the four-log endpoint was unreportable at
the 10 µL plating and comfortable at 100 µL — same flask, same afternoon — which
is arithmetic and could not have failed. What could have failed is whether a real
experiment ever lands in the window where the two platings fall on opposite sides
of a class threshold, and at the cut the clinical classification uses it does:
one culture, two labels, and nothing between them but the pipette and the error
in measuring what went in. That is reachability working as a design constraint
rather than as an explanation after the fact, and it is why the calculation in
Box 1 belongs before an experiment rather than after it.

The same arithmetic answers the objection that the starting density is fixed by
protocol. It is fixed as a turbidity, and a turbidity is not a viable count.
Under one written protocol the densities actually achieved differed enough to
move the deepest demonstrable kill by 2.33 log10 between laboratories at a single
plating volume, and the spread reaches 4.40 log10 once laboratories and plated
volumes are taken together. Those two figures are not a partition of one
quantity and are not offered as one: they are ranges over different sets of
readings — twelve at the 100 µL plating against fifty-six across every laboratory
and volume — and ranges do not add. What is exact is the volume term on its own.
Floors of 10, 100 and 400 CFU/mL, set by plating 100, 10 and 2.5 µL, span
1.60 log10 by arithmetic on *L* = 1000/*v*, with no sampling uncertainty at all.
The density term carries all of the uncertainty: it is a range over the four
laboratories that deposit an untreated day-zero reading at the 100 µL plating,
and resampling whole laboratories runs from 0.05 to 2.33 log10 — an interval
whose upper limit is the observed range itself, because a bootstrap of a range
cannot exceed the range it resamples. It bounds that term from below and not from
both sides, and we read it as saying the density contribution could be almost
nothing. The exact part is the stronger half, and the choice of plated volume is
what sets the floor.

The standard is not silent on that choice, and this is the paper's sharpest
finding rather than an awkwardness for it. M26-A's own section 1.3.2.5 is headed
*Volume Transferred*, and it ties the volume to the endpoint with a counting
rule: plate a volume such that, after the defined 99.9 per cent killing, at
least ten colonies remain to be counted (18). It permits 10 to 100 µL, and
gives a reason at each end — carryover above, Poisson sampling error below.
Section 3.1 goes further and requires that the smallest accurately detectable
count be established by serial dilution of a known inoculum. A guideline written
in 1999 therefore already required both of the numbers this paper asks for: a
floor established by measurement, and a plated volume chosen against the
endpoint.

Applied to its own endpoint the rule bites. Ten colonies after a 99.9 per cent
kill of 5 × 10⁵ per mL needs at least 20 µL streaked; a 10 µL streak yields five
and fails the rule. The requirement was there, it was quantitative, and the
deposits reanalysed here do not meet it — not because their authors disregarded
a standard, but because the endpoint moved out from under it. M26-A sets 99.9
per cent throughout and nowhere contemplates a four-log call; the deeper
endpoints came later, and the volume rule did not travel with them.

Take the assay's contribution out and something is left, not nothing, and what
is left makes biological sense. Growth state predicts the tolerance class, and
it still predicts it after adjustment for starting density, which is the
expected direction: isoniazid needs KatG to activate it and needs active
cell-wall synthesis (21), rifampicin needs transcription (22), and a
population that is not dividing offers less of what these drugs act on. The axis
the classification is reading is physiological state, not drug susceptibility.

The isoniazid-resistance association behaves differently, and instructively. It
is the weaker of the two on two separate counts. Unadjusted, resistant isolates
carry 2.32 times the odds of a higher tolerance class. Adjusted for starting
density the odds ratio is 1.31 and the interval spans one. It also does not
clear its corrected threshold once the analysis is restricted to the baseline
isolates, which are one per patient by construction — the only correction for
repeated isolates this deposit permits, since it carries no patient identifier.
The growth association survives both.

Why the association weakens is visible in the same file: resistant isolates
enter the assay ten-fold lower and 26.2 per cent of them lack the room the
endpoint requires. We do not know why they seed lower. The natural explanation —
that resistance carries a fitness cost — is not supported here, since these
isolates do not grow measurably more slowly and most carry the near-neutral
*katG* S315X allele (23, 24). That gap is a finding in its own right and
belongs in the next study rather than in a speculative sentence in this one. Nor
is it explained away by anything else the file records: of its nine pretreatment
covariates only two can legitimately be adjusted for, and neither moves the
association by more than five per cent (Section 4). The two larger movements in
that table both come from columns that record the exposure rather than a
confounder: the mutation identity, which is missing for all but one susceptible
isolate, and the isoniazid MIC, which separates the two groups completely and
enlarges the seeding gap by 13 per cent instead of shrinking it.

Vijay and colleagues report that tolerance goes with resistance status and with
treatment history in the same isolates (25). We do not dispute a single
measurement. Their deposit is unusually complete, and this analysis was only
possible because they posted the classification, the readings behind it and the
assay geometry together. What we add is this. Their deepest endpoint asks for the
largest fall, so it is the one shortest of room to fall in, and how much room
there is differs systematically between the very groups being compared. The link
to resistance then survives neither putting starting density into the model nor
cutting the data down to one isolate per patient. The link to growth survives
both. So the finding is not that their classification is empty. It is that one of
its two associations is carried by the geometry of the assay and by isolates that
are not independent of each other.

Several things about these deposits bound what the analysis can establish, and
each points at the experiment that would settle the question. Those bearing on
the claims made here are these; the rest are set out in the supplement.

The first limitation is one this paper has already acted on rather than merely
declared. Flasks from one laboratory share a starting culture; repeat isolates
come from a patient already counted.
Every conclusion drawn from the two primary deposits was recomputed at the level
where the observations really are independent, and the outcome is listed one line
at a time rather than summarised (Table S13): twenty survive unchanged, six
survive with much wider uncertainty, five do not survive and **have already been
removed from the text above**, and one is withdrawn because the "no difference"
it was tested against was already false before any data were seen. The five and
the one are not claims this paper makes; they are claims it tested and dropped,
and the ledger is printed so a reader can check that the dropping was done rather
than promised.

The 15-day and 60-day panels of the clinical deposit contain the same isolates.
The comparison between panels is therefore not independent, and it bounds the
evidence for a difference rather than establishing it.

Starting density could sit on the causal path rather than beside it. Suppose
resistance slows growth, and slow growth causes genuine tolerance. Then the thin
inoculum is a consequence of the slow growth, and adjusting for it would remove
real signal rather than a confounder. The asymmetry favours the confounding
reading, since growth survives adjustment and resistance does not, but a design
that fixes the inoculum would settle it.

**Report the starting density and the assay floor with every tolerance
measurement.** The two together say how far down the experiment could look, and
without that a log-reduction endpoint cannot be interpreted. Neither costs
anything to record: one is the count that went into the flask, the other is what
a single colony on the plate is worth. Thirty-six of the 45 deposits inspected in
full in the course of this project state no limit anywhere — four in five of the
datasets an investigator would actually reach for.

**Choose the depth of the endpoint to fit the headroom actually available, and do
not densify the inoculum merely to buy more.** The inoculum this needs can be
worked out before the experiment rather than diagnosed after it: seeding above
*L* · max(10^*q*, 1/*c*₁) makes both failure modes impossible — the endpoint that
was never reachable, and the last count that lands on the floor. For this assay
that is 230 000 per mL. But seeding higher also changes the experiment, because a
denser culture is a different physiological state, and this paper's own finding
is that physiological state is what the tolerance label tracks. Where the deep
endpoint is wanted, lower the assay floor; where the headroom will not carry it
either way, the shallower endpoint is the honest one, and the growth state
belongs on the report whichever is chosen. This is a design decision that is
currently not being made.

**Model an ordered label as ordered.** A tolerance class is low, medium or high.
Scoring that 0, 1, 2 and fitting a line asserts that the step from low to medium
is the same size as the step from medium to high, and no one has established
that. Proportional-odds regression — a fit built for ranked categories — costs
nothing to run and reports in odds ratios. Where the proportionality it assumes
fails, as it does here at 60 days, it says so rather than averaging two different
effects into one null.

**Treat an endpoint at the floor as a bound, not a value.** A recorded fraction of
*L*/*N₀* is an upper limit on survival, not an estimate of it. Analysed as a
measurement it manufactures differences between isolates whose final viable
burdens the assay could not tell apart. It also hides the converse point: the
range of true reductions a floor reading is compatible with depends on where that
culture started, so the same censored reading stands for a different demonstrated
kill at every starting density.

None of this requires new apparatus or a statistician, and to make that concrete
the four checks are released as a small command-line tool alongside the analysis
code. Give it a starting density and either an assay floor or a plated volume. It
returns the headroom, states which of the 90, 99, 99.9 and 99.99 per cent
endpoints that headroom can support, and reports the recorded fraction a
floor-level reading would produce, labelled as the bound it is. Where a culture
volume is known it also returns the viable burden a blank reading is consistent
with; where it is not, it declines to compute one rather than assuming a volume.
The tool exits with a failure code when a requested endpoint is unreachable, so
it can be run before an experiment rather than after it.

**Report physiological state as a required field.** It is what the classification
is reading, and it is currently the least documented variable in the assay.

**Fix the inoculum, or adjust for it, before comparing tolerance across groups.**
The comparison that motivated this work — resistant against susceptible isolates
— is confounded by a ten-fold difference in starting density, and nobody knows
why that difference is there. Until it is understood, group comparisons of
tolerance in clinical isolates should carry the starting density as a covariate.

---

### Conclusion

A plate that grows nothing under antibiotic has never been evidence that the
flask was sterile, and the field knows it. The remedy adopted was to stop asking
whether the culture went negative and to start asking how far it fell, expressed
as a fraction of where it began so that the starting culture could not matter. We
find that the fraction stops being a fraction once the population reaches the
floor. What the deposit records from that point is *L*/*N₀*, which moves with the
starting density and not with the surviving population — in this deposit, for
fifteen per cent of isolates at the depth the classification uses, and for the
eighteen isolates whose recorded label a single threshold on their inoculum
reproduces exactly, because for twelve of them no count below the floor would
have changed which class the rule could return.

The consequence is not that tolerance is an artefact. It is that a tolerance call
made without its headroom cannot be told apart from an inoculum measurement, and
that the phenotype which does survive the correction is physiological state
rather than drug susceptibility. Report the starting density and the assay floor.
Match the depth of the endpoint to the range actually available. Treat a reading
at the floor as a bound. Do those three things and a tolerance classification
would mean the same in one laboratory as in the next. Until then, some of what
the field calls tolerance cannot be separated from a record of how much culture
went into the tube.

---

## Materials and Methods

*The condensed account. The full account, with every estimator and every sensitivity analysis, is Supplementary Methods in the supplemental file.*

### The corpus screened, and how five deposits came out of it

The five deposits analysed here are the residue of a larger screen, and the
attrition is itself a result. A corpus of 78 candidate time-kill datasets was
assembled from the published literature and inspected one record at a time
between 21 August and 8 September 2026, each entry annotated with what its source
actually states about the three quantities this paper's arithmetic needs: a
pre-treatment starting density, a time series of counts, and either a plated
volume or a stated assay floor. The manifest, with every candidate's identifier, licence and per-field
verdict, is deposited with the analysis code, so the screen can be audited rather
than taken on trust.

Of the 78, 45 had series that could be read in full. **Of those 45, 36 state no
assay floor by any route** — no limit of detection, no limit of quantification,
and no plated volume from which one could be derived. Five state a floor
outright and four permit one to be derived from a stated plated volume. Eighteen
of the 78 carry enough for the boundaries to be computed at all, and five carry
the complete set of fields the analysis needs; those five are the deposits of
Table 1. The remainder fail on a missing floor far more often than on anything
else, which is the reporting gap this paper is about.

**What this screen is, and what it is not.** It is a systematic inspection of a
corpus assembled from the published time-kill literature, with every candidate
recorded and every exclusion attributable to a named missing field. It is **not**
a systematic review: no registered search string, database set or date-bounded
inclusion protocol governs which datasets entered the corpus, so the 78 are a
documented sample of the literature rather than a proven census of it. The
proportions above should be read as what an investigator meets in practice, not
as an estimate of the whole published record. Nothing in the paper's argument
depends on the corpus being exhaustive: the boundaries are derived from
definitions, and a single deposit with a floor is enough to apply them.

### The five deposits analysed

Five published deposits are analysed (Table 1). Four carry the analysis and the fifth is held out to test it. None was generated for this
study and all are openly licensed. The held-out deposit was opened only after
every boundary and threshold was fixed, which the commit history of the analysis
repository timestamps; the other four were chosen for the fields they carry, and
that choice is not separately registered.

**Clinical isolates with a deposited tolerance classification.** 217 *M.
tuberculosis* isolates assayed under rifampicin, each carrying a minimum
inhibitory concentration, minimum durations for 90, 99 and 99.99 per cent killing
at 15 and 60 days of prior culture, most probable number readings at days 0, 2
and 5, a growth-rate proxy, isoniazid susceptibility with the resistance mutation
where present, months on treatment, and the authors' own tolerance level for each
isolate (Vijay et al. 2024; eLife 93243 supplementary file 2) (13). The killing assay
runs for six days, so an isolate not reaching its target within that window is
recorded at the ceiling. Of the 217 rows, 43 are follow-up isolates from patients
already represented, so a baseline-only stratum is analysed separately.

**The six-laboratory exercise.** *M. tuberculosis* H37Rv from one stock,
distributed with one written protocol to six laboratories blinded and labelled A
to F (van Wijk et al. 2023; figshare 19766083, CC BY 4.0) (4, 5). Moxifloxacin and
isoniazid at one and ten times the minimum inhibitory concentration, an untreated
control, three flasks per arm, sampled to day 21 or 28. Each sample was plated at
four volumes: 100 µL in quadruplicate, 10 µL as four drops, 10 µL as a single
drop, and 2.5 µL as a single drop. In the deposited file the colony count is
already expressed per millilitre, confirmed by the smallest count recorded at
each volume being exactly 1000 divided by that volume, which is one colony per
millilitre. The minimum reportable positive count is therefore a property of the
plated volume — one colony in that volume — and equals 1.0, 2.0, 2.0 and
2.6 log10 CFU/mL respectively, so four platings give three distinct floors
spanning 1.60 log10 within a single flask-visit (26). The identity is exact for 1 055
of the 1 068 readings at 10 µL; the thirteen exceptions all come from one
laboratory and do not lie on the lattice its recorded volume implies. The file
holds 2 775 readings, of which 17.9 per cent are flagged below the floor and 24
above it; the analysis set, after dropping above-limit flags, unusable values and
pre-treatment visits, is 2 580 readings, of which 19.3 per cent are flagged.

**Evolved clones.** 126 *Escherichia coli* clones from a parallel evolution
experiment under amikacin, each carrying an endpoint minimum inhibitory
concentration and a persister fraction measured on the same clone, labelled by
the antibiotic concentration and nutrient level its population evolved under
(Windels et al. 2024; Zenodo 10.5281/zenodo.7550302, CC BY 4.0) (8, 27). Six of its
595 surviving fractions are written as exact zeros, marking a below-limit reading
without naming a limit; they fix no floor, so this deposit is one of the two for
which observability labels are refused.

**A deposit held out for validation.** Amoxicillin-clavulanate against
*Escherichia coli* in a hollow-fibre infection model, with 100 µL plated and
counts per mL so the assay floor is derived rather than inferred,
measured day-zero densities for every culture rather than a nominal inoculum, and
below-limit readings retained as a placeholder (Dubey et al. 2026; article Source
Data, CC BY 4.0) (9, 10). It was located by a search of five general repositories, the
tuberculosis consortia, the persistence literature, food microbiology and the
hollow-fibre field, and was the only deposit found carrying all three fields the
boundaries require. No boundary, threshold or modelling choice in this
paper was informed by it: it was opened after all of them were fixed, and
Section 6 is the only place it tests anything. What cannot be documented is the
search itself. The repositories were searched interactively and no query log,
access date or screening count was kept, so this paper reports the outcome of
that search — one deposit carrying a measured per-culture starting density, a
recorded plated volume and per-culture time-course counts together — without
being able to evidence its extent. The claim that no deposit was selected after
its result was known rests on the commit history of this repository rather than
on a registration, and readers should weigh it accordingly. It does appear
descriptively — a row of its own in Tables 2, 5, 9, 15, S5 and S7, and a table of
its own in Table S9 — which is reporting rather than fitting.

**Concentration-by-time grid.** Apramycin and amikacin against *M. tuberculosis*
at 128, 32, 8, 4 and 1 µg/mL, triplicate log10 CFU at days 0, 3, 7 and 14, with a
concurrent drug-free control at every visit (Kaur et al. 2024; figshare 26462791,
CC BY 4.0) (6, 7). The amikacin arms are not analysed here. Within apramycin the 1 µg/mL
arm shows net growth rather than killing and is excluded from the dose
comparison, leaving 4 to 128 µg/mL as the range compared (Section 7).

### The prospective experiment

The two boundaries were used to design an experiment against themselves. Its
design sheet, its predictions and its plate counts are one workbook, deposited
with the analysis code, and the predictions were written on the design sheet
before any plate was counted.

**Strain, media and incubation.** *Escherichia coli* ATCC 25922, the
quality-control reference strain the standard itself names. Broth and agar were
Mueller–Hinton (HiMedia): cation-adjusted Mueller–Hinton broth for the minimum
inhibitory concentration and the exposure, Mueller–Hinton agar for the viable
counts. Cultures, the microdilution plates and the count plates were incubated at
35 ± 2 °C in ambient air, the reference conditions CLSI specifies for this
organism, count plates being read after 18 to 24 h (18, 28).

**Minimum inhibitory concentration.** The ciprofloxacin MIC of the strain was
determined by CLSI reference broth microdilution (28, 29): ciprofloxacin
doubling-diluted in cation-adjusted Mueller–Hinton broth, a final inoculum of
about 5 × 10⁵ CFU/mL, incubation at 35 ± 2 °C for 16 to 20 h in ambient air, and
the MIC read as the lowest concentration with no visible growth, with growth,
sterility and quality-control wells alongside as CLSI directs. The MIC was
0.008 mg/L, which falls within the CLSI quality-control range for this strain
(29), and the exposure was set at ten times it, 0.08 mg/L.

**Drug and design.** Ciprofloxacin at ten times the MIC, 0.08 mg/L — chosen
because it kills deeply and fast, so every arm reaches the floor inside a working
day, which is what reachability and identifiability need in order to be testable
at all. Three seeding arms were chosen so that the four-log endpoint is
unreachable in one, marginal in the second and comfortable in the third: targets
5 × 10⁴, 5 × 10⁵ and 5 × 10⁶ CFU/mL, the middle arm being the inoculum the
standard specifies. The densities actually reached were 6.4 × 10⁴, 4.4 × 10⁵ and
3.8 × 10⁶ per mL, recomputed from the day-zero counts rather than assumed from
the targets. Three flasks per arm, nine in all, treated throughout as three
independent biological replicates per arm; a drug-free growth control was carried
in parallel. Sampling at 0, 1, 2, 4, 6 and 24 h; hour zero is not a convenience
but the measurement of *N*₀ on which every boundary rests.

**Plating and enumeration.** At each time a sample was serially ten-fold diluted
in sterile saline, and from one dilution series both 100 µL and 10 µL were
plated, each in duplicate, across dilutions from neat to 10⁻⁴. Nine flasks × six
times × two volumes × two plates is 216 plate readings, which is the whole
dataset. Viable density was *N* = *C*·*D*·1000/*V* for *C* colonies counted at
dilution factor *D* and plated volume *V* µL.

**The floor, and why duplicate plating moves it.** *L* is one colony in the
volume actually plated, referred back to the undiluted sample: at a single plate
10 CFU/mL at 100 µL and 100 CFU/mL at 10 µL. The two technical plates of a sample
are pooled rather than averaged, so their volumes add — two 100 µL plates read
together are 200 µL of sample, so one colony across the pair is 5 CFU/mL and not
10, and the 10 µL pair gives 50. Pooling therefore lowers the floor, and the two
platings differ by exactly one log by construction. An earlier version of the
analysis averaged the two plates' densities while keeping the single-plate floor,
and a sample with one blank plate and one single-colony plate then reported a
fraction below its own floor — a culture apparently killed deeper than its
headroom allowed. That is the error this manuscript accuses the literature of,
committed in its own arithmetic, and it is recorded here rather than quietly
fixed.

**Analysis.** Headroom, censoring at the floor and the three tolerance classes
are as defined in the Methods above and are applied here unchanged; a plate with
no colonies is a left-censored reading below *L*, held at *L* for log-reduction
and plotting rather than set to zero. Each plating series carries the starting
density measured on that same plating, because the 10 µL series never made the
100 µL measurement and importing it would report a depth that series could not
have reached. Where the argument is about the plated volume alone — the two-label
count — a single pooled *N*₀ per flask is used instead, and both figures are
reported. Class labels use the thresholds of the clinical deposit reanalysed
above, *c*₁ = 10⁻³ and *c*₂ = 10⁻², so that the two experiments are scored on one
rule.

### Two kinds of limit, kept apart

No deposit analysed here reports a validated limit of quantification with a
value. The six-laboratory file names the concept in the definitions of its BQL
and AQL columns but defines it as whether the plate was countable, which is an
operator's judgement rather than a validated limit. Throughout this paper *L* is
therefore an **operational assay floor**: where a plated volume is recorded it is
the **minimum reportable positive count**, one colony in that volume, and where
none is recorded it is inferred from the deposit and is labelled as inferred. The
term limit of quantification is used only in reporting what a source states.

Those two names are the precise ones and are used where *L* is defined or its
provenance discussed. In running text *L* is the **assay floor**, and that is the
only short form used, so that "boundary" is left free for the two derived
boundaries of the next subsection and never denotes a value. The event a
time-to-event analysis records is correspondingly a first observed crossing below
the assay floor.
What *L* is in each deposit, how it was arrived at, and how replicate plates and
plated volumes were treated is tabulated deposit by deposit (Table S14).

Two distinct censoring problems arise and are handled separately, because
conflating them is the error this paper is about.

A **count below the assay floor** is left-censored: the population is somewhere
below a known value. In the six-laboratory deposit that value is a property of
the plated volume, as above. In the clinical deposit the readings are most
probable numbers taking the discrete values of an MPN table (11, 12), and the day-5 column
bottoms out at 23 per mL with a visible pile-up there; that value is treated as
the floor, and the first Results section reports the evidence for it.

That deposit states no limit of quantification, so the floor is inferred rather
than read off, and the inference is bounded rather than asserted. Three things
support it: 23 per mL is the smallest value anywhere in the file, nothing lies
below it in 1 932 readings, and the minimum shifts by exactly a factor of ten per
visit — 2 300, 230, 23 — in all three culture ages, which is the signature of one
dilution series applied to a differently diluted sample at each timepoint.

The floor is therefore visit-specific, and it does not follow that every visit
has one. A floor is a value readings stop at, so it shows as a pile-up on the
lowest rung with nothing below; the ten-fold shift alone only shows the dilution
changing. Applying the rule of the next subsection visit by visit, the day-5
column has that signature in every panel and the day-2 column has it at 15 days,
but the day-0 column does not: its minimum of 2 300 per mL occurs exactly once in
each panel, with the next value at 6 100, which is the tail of a distribution
rather than a floor. The verdict for day 0 is that no floor is evidenced. The
starting density is therefore an observed value throughout, and no quantity in
this paper that conditions on *N₀* needs a censored specification. Since
none of that is proof, the load-bearing count is recomputed at every value a
three-tube MPN table returns below 23. The number of isolates lacking four logs
of headroom is 33 at a floor of 23 and does not fall below 28 at a floor of 3.0,
the lowest such table returns. The conclusion holds across the whole range, so it
is not an artefact of where we place the floor, and the same sweep is run for
every deposit that carries a floor (Table S15).

The six-laboratory deposit also carries the evidence for judging each reading
against its own volume rather than pooling. Each sample is plated at four
volumes at the same visit, so a below-limit flag can be checked against the other
platings of the same flask. Of its 498 flags, 83, or 16.7 per cent, are
contradicted: another plating of the same sample at the same visit, with a limit
at least as sensitive, returns a quantified count above the flagged reading's
limit. Those flags record a drop that missed rather than a culture that fell.
Pooling the four volumes to a single limit would treat them as evidence about the
population; judging each against the floor its own volume implies does not, and
that is the reason the analysis is built the way it is. The cost of pooling can
be priced. Pooling at the least sensitive volume would discard 126 genuine
quantified counts, 5.9 per cent of them, and pooling changes the contradicted-flag
rate itself: 16.7 per cent judged per volume, against 43.2 per cent pooled at
10 CFU/mL and 15.3 per cent pooled at 400. The audit's own answer depends on the
choice, which is the strongest reason to make it explicitly.

A **crossing time not observed within the study** is right-censored: the event
has not happened yet, which is not the same as the event having no time. A flask
that never fell below the floor contributes the information that its crossing
time exceeds its last visit, and enters the survival likelihood as such. It is
never recorded as missing.

### Floor posterior, refusal, and what is not learned

The algebra of headroom and observability is closed form once *L* is known. What
requires inference is *L* itself, and the two cases are not alike. A
volume-derived floor — one colony in *V* µL is 1000/*V* per mL, and the observed
minimum equals that value — is a point mass, with nothing to infer. A floor
inferred from a pile-up on a most-probable-number rung carries a discrete
posterior over the rungs at or below the observed minimum; the interval quoted is
the 95 per cent highest-posterior-density support.

That distinction is turned into a rule rather than a caveat. Where the verdict is
that no floor is evidenced, or where the support spans more than one log10, the
observability labels are **refused** rather than reported (Table S1). Surviving
fractions written as exact zeros with no named *L* fall in that refused class, as
does a deposit whose minimum occurs once in a continuous tail. The clinical
deposit passes the rule with a support of 0.40 log10; two of the five deposits
fail it and are labelled accordingly. This paper fits nothing to predict an MDK:
once *L* is in hand the rest is derived.

### Causal mediation of the resistance association

The attenuation of the resistance coefficient once starting density enters the
model is reported in the Results as a descriptive ratio, which is what it is.
Separately, a linear product-of-coefficients mediation decomposes the total
effect of isoniazid resistance on the day-5 tolerance class into an average
causal mediation effect through log10 *N₀* and an average direct effect (30, 31), with
bootstrap percentile intervals from 5 000 resamples, repeated on the baseline
stratum and on two binary collapses of the outcome.

The refit that answers the objection about the mediator being the outcome's own
denominator is reported in Section 4. Its stratum is defined here: an isolate is
excluded from it when its day-5 reading is at or below the floor of 23 MPN per
mL, which is the condition under which the recorded fraction is *L*/*N*₀ and the
class carries no measured numerator. Eighteen of the 203 meet it. The refit is
the same estimator on the remaining 185, with the same seed and the same 5 000
resamples, so the two are comparable term by term.

Sequential ignorability is assumed and is not testable here, so the estimate is
accompanied by the sensitivity that matters: the residual correlation between
mediator and outcome errors at which the point estimate crosses zero, which is
about −0.23. The outcome is an ordinal class scored linearly, as in the
association family; the binary collapses are reported because they do not depend
on that scoring. No claim is made that unmeasured confounding is absent. The
estimate replaces the attenuation percentage as the quantity cited for the
pathway (Table S5).

Fold-change figures such as 216-fold and 265-fold are ten raised to the unrounded
log10 difference before display rounding, so that Δ*h* = 2.3349… is reported as
216-fold rather than as 10^2.33.

### What each analysis was fitted to

A dozen different denominators appear in this paper and each is correct for its
own analysis, so every one of them is derived in a single place (Table S2). The
reductions are few and they are named: the MDR tolerance label is a fourth,
unordered category and is dropped wherever an ordered outcome is fitted, taking
14 rows from each panel; six 60-day labels are absent before that, so the 60-day
panel loses 20 in all; the growth proxy is missing for one isolate; and five of the 72 treated flasks
in the six-laboratory deposit carry no usable starting density, which is why a
comparison over 72 flasks is reported on 67. Of the 30 laboratory-by-arm cells,
29 retain enough quantified readings to fit a rate.

The series counts in the six-laboratory deposit differ for the same reason. Each
of the 90 flasks is plated four ways, giving 360 series of which 288 are treated;
the descriptive Cox drops a further 27, 26 for carrying no quantified reading at
day 0 or day 1 in their own plating and one for reading below its floor at day
zero, leaving 261.

Whether these exclusions are plausibly ignorable is tested rather than asserted:
dropped rows are compared with retained rows on starting density and
susceptibility (Table S16). The MDR exclusion differs in susceptibility by
construction. The only difference not by construction is in the 60-day panel,
where the 20 dropped rows sit higher in starting density.

### Dynamic range, and the two boundaries it sets

For a culture starting at *N₀* against an assay floor *L*, two quantities
are used and are kept apart, because they are not interchangeable:

  *H* = *N₀*/*L*, a ratio;
  *h* = log10(*N₀*/*L*), the **headroom**, in log10 units.

The headroom is the deepest reduction the assay can resolve. It is fixed by the
dilution scheme and the starting culture before any drug acts, and variation
between cultures is reported on *h* rather than on *N₀*, as Δ*h* = max(*h*) −
min(*h*) with the corresponding fold difference 10^Δ*h*. That distinction is not
notational here. Where *L* is set by the plated volume, one culture read on a
2.5 µL drop and on a 100 µL quadruplicate differs by 1.60 log10 in headroom, and a
figure computed from *N₀* alone would discard it.

Two boundaries follow from the definitions alone.

**Reachability.** The smallest value the assay reports as a measurement is *L*,
so the largest reduction expressible as a measured value is *h*. A *q*-log
endpoint is therefore observable if and only if

  *N₀* ≥ *N*_reach = *L* · 10^*q*.

**Identifiability.** A censored reading places the true count in [0, *L*], so the
recorded surviving fraction is at most *L*/*N₀* — an upper bound, not a
measurement. Given class thresholds 0 < *c*₁ < *c*₂ …, the class is determined by
the data only if the whole interval [0, *L*/*N₀*] lies inside one class. Since
that interval contains zero, the only candidate is the lowest class, so the class
is determined if and only if

  *N₀* > *N*_id = *L*/*c*₁.

Above that boundary the lowest class is the only one compatible with a censored
reading, whatever the true count was, so the class the rule assigns is fixed by
*N₀* rather than by the surviving population. The boundary says nothing about
whether a culture reaches the floor, which depends on the drug; it says what the
classification can mean once one has. Both
boundaries are properties of the method and involve neither the drug nor the
strain, and their ratio is *N*_reach/*N*_id = *c*₁ · 10^*q*.

Seeding a culture above *L* · max(10^*q*, 1/*c*₁) makes both failure modes
impossible, which is a design criterion computable before an experiment rather
than a diagnosis after it.

### Estimation

A **Tobit model** fits log10 CFU/mL linearly in time by maximum likelihood (32). An
observed reading contributes the usual Gaussian density; a censored reading
contributes log Φ((limit − µ)/σ), the probability that it fell below its own
limit. This is Beal's M3 (Beal 2001) written for this assay (33). Intervals come from
the profile likelihood.

**Multiple imputation** draws each censored reading from the fitted normal
truncated at its own limit, refits by ordinary least squares, and pools 50 fits
by Rubin's rules (34). The imputation is proper: the line and the error scale
are redrawn from the Tobit fit's own asymptotic distribution at every imputation
rather than held at the point estimate, so the between-imputation variance
carries the uncertainty in the model that generated the draws. What the agreement
between the two estimators establishes is therefore that the answer does not
depend on which arithmetic recovers it. It does not establish that the sub-floor
distribution is normal: both make that assumption, and no reading below the floor
exists to test it against. Where the assumption itself is in question, the
quantity to look at is the headroom, not the fit.

The growth proxy is the deposit's time to an optical density of 0.4, in days;
the deposit records no wavelength, so none is given here. Because it is a time,
it runs inversely to growth rate: a larger value is a slower-growing isolate.

**The tolerance label** is modelled as an ordered categorical outcome by
proportional-odds ordinal logistic regression (35), with starting density as a
prespecified covariate and every association reported unadjusted and adjusted for
it. The MDR category of the deposited label is a fourth, unordered category and
is excluded; all 14 rows carrying it fall outside the susceptible-versus-resistant
contrast in any case, so the ordinal and linear models are fitted to identical
rows. Proportional odds is tested by a Brant test per predictor (36) and by a
likelihood-ratio test against a generalised ordered logit (37) with the coefficient
released; where it fails, the released partial-proportional-odds fit is reported
and checked against a multinomial fit that assumes no ordering. Rows are dropped
only for a missing outcome, predictor or starting density, and the dropped rows
are compared with the retained ones on starting density and susceptibility.
Because the deposit carries no patient identifier, the repeated-isolate structure
is handled by a baseline-only stratum rather than by a random effect, and the
linear models of the earlier analysis are retained as a sensitivity comparison
(Table S17).

**Time-to-event analysis** treats the **first observed crossing below the assay
floor** as the event, with series never falling below their own floor
right-censored at their last visit. The event is named that way throughout and is
not read as clearance, sterilisation or the end of a culture: of the series that
cross, 60 per cent read above the floor again at a later visit.

The crossing time is interval-censored, not observed: it lies between the last
visit above the floor and the first visit below it, and the visit schedule is
coarse. Interval-censored fits (38) are therefore reported alongside the naive
treatment that pins the event to the visit at which the blank plate was noticed.
Kaplan–Meier (39) and Cox proportional hazards (40) are retained as **descriptive**
summaries of first crossing only; their intervals are replaced by cluster
bootstraps over laboratories and over flasks (41), because those 261 series come from
72 flasks in 6 laboratories and the partial likelihood treats them as independent.
No p-value is quoted for a term that is constant within laboratory, since six
clusters cannot support one. Proportionality is tested on Schoenfeld residuals (42, 43).

A cell is fitted only when it retains at least six quantified readings at three
distinct times; below that the slope is determined by the censoring pattern
rather than by the counts.

**The replicate-level bootstrap** (44) behind the interval slopes resamples the three
replicate counts with replacement at both ends of each interval, takes their
mean, refits the concentration slope on each draw, and takes percentile intervals
from 20 000 draws. The resampling unit is the replicate count, not the interval,
so a draw can repeat a replicate at one end and not the other. It is a draw of
the three-replicate MEAN, because the mean is what the slope is fitted through;
drawing a single replicate instead would attach the variance of one count to an
estimate built from three. This bootstrap, and not the least-squares fit through
the four concentration means that the deposited table reports beside it, is the
interval quoted in Section 7 and drawn in Figure 3C. The least-squares fit is
kept in the table for comparison and is labelled there: it has two residual
degrees of freedom and discards the replicate scatter entirely. An interval on a
proportion — an inversion rate, or a share of flasks — is the Jeffreys
interval (45), which is the equal-tailed posterior under the Jeffreys prior
and does not collapse to zero width when the count is 0 or n, as the normal
approximation does at the sample sizes here.

**What is standard and what is not.** The Tobit fit, Kaplan–Meier, Cox and the
interval-censored fits come from the packages named below. Four procedures do
not: the Brant test of proportional odds, the partial-proportional-odds fit with
a per-cut coefficient mask, the product-of-coefficients mediation with bootstrap
percentile intervals, and the residual-correlation sensitivity for sequential
ignorability. Those are implemented in the released analysis code rather than
taken from a package — in `exp30_ordinal_tolerance.py` and `exp34_mediation.py` —
and the partial-proportional-odds likelihood is validated against the
proportional-odds fit it nests, agreeing to 1.0 × 10⁻¹⁰ in log-likelihood when
nothing is released. The multinomial check uses statsmodels.

### The decomposition of a crossing time

Over an interval in which the decline is close to log-linear, log10 *N*(*t*) =
*a* − *bt*, and with *ℓ* the log10 assay floor and *D* = *a* − *ℓ* the
distance the population starts above it, the crossing time is *T* = *D*/*b*. For
two flasks,

    log(T_A / T_B) = log(D_A / D_B) − log(b_A / b_B)

which is exact on this model and splits a difference in crossing time into a
distance term and a rate term. An **inversion** is a pair in which A fell faster
yet crossed later, which occurs exactly when *D_A*/*D_B* > *b_A*/*b_B*. A single
slope is not a full description of a biphasic trajectory, so *b* is the average
decline over the window fitted, and the variance shares reported below are shares
of that averaged slope; averaging across decline and regrowth moves the rate term
up rather than down, so the distance share is a lower bound; *D* is taken from the measured day 0 to 1 density
rather than from the fitted intercept, because a single line through a biphasic
curve extrapolates back to an intercept well below the culture the flask started
from.

### Multiplicity

Where a question admits more than one test, every test the deposit supports is
run, and the family is corrected by the Benjamini–Hochberg procedure (46) at a false
discovery rate of 5 per cent. For each test we report the correlation the sample
size could have resolved at 95 per cent confidence, so that a null is bounded
rather than asserted.

### Reproducibility

Every number in this paper is regenerated by a script that writes a machine-
readable receipt of what it computed, and a separate audit script recomputes 174
of the quantities quoted in the text from the tables they came from and reports
any that disagree. That audit is not exhaustive: it pins the load-bearing counts,
every headline interval and every figure a conclusion rests on, and it does not
pin every cell of every table.

A second audit reads what the first cannot. The value audit parses table bodies
only, so it never sees a table legend, a figure legend, Box 1 or the Abstract —
and it has no way to notice that a number called a hazard ratio in one place is
called a p-value in another, which is a mistake this manuscript made and a
reviewer caught. The second audit checks that every number in those four regions,
conventions such as the endpoint constants and the confidence level aside,
occurs in a results file, a receipt or a table body; that no numeric literal
carries two incompatible statistical labels and that no most-probable number is
printed as a colony count; that percentages, fold-changes, corrected thresholds,
spans and interval bounds follow from their own stated inputs; and that no
conclusion the self-audit marks unsupported is still asserted anywhere, that
every sample size traces to a line in the flow account, that every
cross-reference resolves, and that no block of prose states the same thing
twice, which is what a paragraph looks like when the passage its rewrite
replaced was never deleted. It fails the pipeline
on the findings it grades as contradictions and reports anything weaker without
failing; an untraceable number in a figure legend, in Box 1 or in the Abstract
is weaker, and so is a legend count its own table contradicts where the results
carry that value elsewhere. Every table is
generated from the results files and the manuscript is assembled from that
generated material, never edited downstream of it, so a table cannot drift from
the analysis behind it.

What the second audit does not cover is worth stating, because a guarantee whose
edges are unstated will be read as covering everything. It is an existence check
before it is a semantic one: a number that is correct somewhere in the corpus but
attached to the wrong quantity passes unless some other rule reaches it. Figure
legends, Box 1 and the Abstract have no staleness net comparable to the one that
diffs each spliced table against the block that generated it, so a stale number
there is caught only if it exists nowhere else. An error introduced into a legend
inside the table-generating code is invisible to a check that compares the paper
against that code's own output. And the self-audit table is the premise of the
withdrawn-claim check rather than its subject: the check sees only the
conclusions that table lists, so a reading retracted in the prose alone lies
outside it, and a verdict silently changed from unsupported to supported would
not be detected.

Analyses used Python 3.14 with numpy 2.5.0 (47), scipy 1.18.0 (48),
pandas 3.0.3 (49), statsmodels 0.15.0 (50) and lifelines 0.30.3
(51).

---

### Ethics

This study reanalysed publicly available, de-identified datasets deposited by
other groups, and generated one time-kill experiment in a reference strain of
*Escherichia coli*. No human or animal subjects were involved, no patient samples
were collected, and no individual is identifiable from any material presented
here. The author is an independent researcher with no institutional affiliation,
so no institutional review board holds jurisdiction; none is required either for
secondary analysis of de-identified data already public under open licences or
for work on a bacterial quality-control strain.

### Use of generative artificial intelligence

Anthropic's Claude (Opus 5) was used under the author's direction to copy-edit
and language-edit the manuscript text and to prepare its final version. No figure,
image or schematic was generated by an artificial intelligence tool; every figure
is plotted from values that regenerate from the public deposits. No artificial
intelligence tool is an author. The author directed the study, verified every
reported quantity against the source deposits and the regenerating pipeline, and
takes full responsibility for the content of this article, including its accuracy
and its originality.

### Data availability

Every dataset reanalysed here was already public under an open licence and none
was generated for this study. Each is identified in Table 1 and cited alongside
the article that first described it: Vijay and colleagues (13, 25), van Wijk
and colleagues (4, 5), Windels and colleagues (8, 27), Kaur and
colleagues (6, 7), and the hollow-fibre Source Data of Dubey and
colleagues (9, 10), held out of every fitting step. The readings from the
prospective experiment are deposited with the analysis code.

That code, both audit scripts, the headroom tool and the machine-readable
receipts recording the software versions each stage ran under are in a public
repository (52), with the documentation and test data needed to run them. It
is dual-licensed: the code under the Massachusetts Institute of Technology (MIT)
licence, and the manuscript, figures and results under CC BY 4.0. The deposits
keep their depositors' own licences. It is at
https://github.com/piranfar/detection-floor-tolerance-endpoints. [The commit
identifier of the submitted version is to be inserted at submission.]

Every number quoted in this manuscript regenerates from the deposits by that
code, and two audit stages check the text against those results. Neither pins
every cell of every table, as the Reproducibility subsection states.

---

## Acknowledgments

This research received no specific grant from any funding agency in the public,
commercial or not-for-profit sectors.

The author declares no competing interests.

Vahhab Piranfar is the sole author and is responsible for conceptualisation,
methodology, software, formal analysis, investigation, data curation, writing of
the original draft, review and editing, and visualisation.

---

## Figure legends

**Figure 1. A log-reduction endpoint is bounded by the assay floor, and the bound
decides the phenotype.** 217 clinical *M. tuberculosis* isolates under
rifampicin, from the deposit that carries the tolerance classification.
(**A**) The distribution of day-5 most probable numbers. It stops at 23 per mL
with a pile-up on it rather than tapering, and no value anywhere in the file lies
below; that is the behaviour of a floor. (**B**) Headroom, the distance from each
isolate's starting density down to that floor, ranked across isolates, against
the depth each tolerance endpoint requires. No isolate is short of the 90 or 99
per cent endpoint. Thirty-three of 217 fall in the shaded band below the 99.99
per cent endpoint, and all 33 are recorded as failing to reach it. (**C**) The
eighteen isolates of the 15-day panel whose day-5 reading was censored at the
floor. Their true final
counts are unknown below *L*, so the assay cannot distinguish their final viable
burdens; what is plotted is the recorded fraction *L*/*N₀*, which is what a
censored reading computes, so the 265-fold span in apparent survival is exactly
the 265-fold span in starting density. The dotted lines are the deposited
classification thresholds. Which side of the low/medium cut an isolate falls on
is settled by where it began, not by what the reading measured — though reaching
the floor at all required rifampicin to cover that isolate's whole headroom, at
least 3.00 logs for the shallowest and 5.42 for the deepest. For the twelve below
the cut, no count the assay admits leaves any class but **low** compatible; for
the six that sit exactly on it the compatible range straddles the cut and two
classes remain.

**Figure 2. Where the inoculum is set by protocol, the two summaries still
diverge.** Six laboratories, one written protocol, one stock of *M. tuberculosis*
H37Rv, moxifloxacin at ten times the minimum inhibitory concentration.
(**A**) The kill rate by censored maximum likelihood with 95 per cent
profile-likelihood intervals; every laboratory yields one, spanning 5.2-fold.
(**B**) The two summaries against each other. The three lowest starting densities
are exactly the three laboratories that recorded crossings at the 100 µL plating;
the kill rate produces no such separation. The crossing times themselves are Figure S1, with the
laboratory-level tests this design does and does not support.

**Figure 3. A late endpoint cannot resolve a 32-fold concentration range.**
Apramycin against *M. tuberculosis*, five concentrations, triplicate counts.
(**A**) The trajectories, with an assumed floor of 100 CFU/mL — the value 10 µL
plating would give — drawn as a band; this deposit records no plated volume, so
the band is an assumption and is drawn to show what the assumption costs; by day 14 the highest arm lies within it, so its apparent rate
over the final interval is a lower bound. (**B**) The ratio of survivors between
the lowest and highest of the four compared concentrations, 4 and 128 µg/mL, at
each sampling day, rising to 48.2-fold at
day 7 and collapsing to 5.2-fold at day 14. (**C**) The concentration slope fitted
separately in each interval from a replicate-level bootstrap, 20 000 draws.


## Supplemental material

The supplemental file carries the full Materials and Methods, the analyses named above as supplementary text, and 22 supplemental tables. Table S18, Table S19, Table S20, Table S21 and Table S22 support analyses reported there rather than in this article, and are listed so that every supplemental item is named in the manuscript.


## Tables

**Table 1.** The five published deposits reanalysed. Four carry the analysis and the fifth is held out to test it. None was generated for this study. The held-out deposit was opened after every boundary and threshold was fixed, which the commit history of the analysis repository timestamps; the other four were selected for the fields they carry, and that selection is not separately registered.

| Dataset | Organism | Drug and range | Design | Deposit | Licence |
| --- | --- | --- | --- | --- | --- |
| Six-laboratory exercise | *M. tuberculosis* H37Rv | moxifloxacin, isoniazid, 1x and 10x MIC | 90 flasks, 2 775 readings | figshare 19766083 | CC BY 4.0 |
| Clinical isolates | *M. tuberculosis*, 217 isolates | rifampicin | 6 duration endpoints per isolate | eLife 93243, suppl. file 2 | CC BY 4.0 |
| Evolved clones | *E. coli*, 126 clones | amikacin | MIC and persister fraction per clone | Zenodo 7550302 (8) | CC BY 4.0 |
| Concentration-by-time grid | *M. tuberculosis* | apramycin 1-128 ug/mL (amikacin arm not analysed) | 5 concentrations x 4 days x 3 replicates | figshare 26462791 | CC BY 4.0 |
| Held out for validation | *E. coli*, hollow fibre | amoxicillin-clavulanate | 20 cultures, measured day-zero density, 100 uL plated | Nat Commun 2026 Source Data | CC BY 4.0 |

**Table 2.** The reduction each tolerance endpoint requires against the reduction the assay can resolve, in the 15-day and the 60-day prior-culture panel alike. Headroom is the distance from an isolate's starting density down to the day-5 MPN floor of 23 per mL. An isolate short of headroom cannot reach that endpoint however completely the drug worked, and every such isolate is recorded at the assay ceiling.

| Prior culture | Endpoint | Isolates | Short of headroom | Fraction short | At ceiling: short vs ample |
| --- | ---: | ---: | ---: | ---: | ---: |
| 15 days | 90% (1 log) | 217 | 0 | 0.0% | - |
| 15 days | 99% (2 log) | 217 | 0 | 0.0% | - |
| 15 days | 99.99% (4 log) | 217 | 33 | 15.2% | 100% vs 88% |
| 60 days | 90% (1 log) | 210 | 0 | 0.0% | - |
| 60 days | 99% (2 log) | 210 | 0 | 0.0% | - |
| 60 days | 99.99% (4 log) | 210 | 7 | 3.3% | 100% vs 95% |

**Table 3.** Isolates whose day-5 reading was censored at the MPN floor. They share one reported floor-level observation, but their true final counts are unknown below the floor, so the assay cannot distinguish their final viable burdens; because their starting densities differ, the same reading also implies a different range of compatible fractional reductions in each. The recorded fraction is L/N0, so the spread in apparent survival equals the spread in starting density exactly, and the labels differ accordingly. The last three columns sort every call in the 15-day panel, not only the censored ones: a censored reading bounds the class from above, and sweeping the true count across the admissible range leaves twelve calls with a single compatible class and six with more than one. Reaching the floor at all is a property of the killing; which class is then compatible is a property of the starting density and the floor.

| Prior culture | At the floor | Starting density spread | Recorded survival spread | Labels assigned at the floor | Measured | Single compatible class | Multiple compatible classes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 15 days | 18 | 265x | 265x | Low: 12, Medium: 6 | 185 | 12 | 6 |
| 60 days | 6 | 100x | 100x | Low: 6 | 191 | 6 | 0 |


## References

1. World Health Organization. 2022. WHO consolidated guidelines on tuberculosis. Module 4: treatment — drug-susceptible tuberculosis treatment. World Health Organization, Geneva, Switzerland. https://iris.who.int/handle/10665/353829.

2. Brauner A, Fridman O, Gefen O, Balaban NQ. 2016. Distinguishing between resistance, tolerance and persistence to antibiotic treatment. Nat Rev Microbiol 14:320-330. https://doi.org/10.1038/nrmicro.2016.34.

3. Brauner A, Shoresh N, Fridman O, Balaban NQ. 2017. An experimental framework for quantifying bacterial tolerance. Biophys J 112:2664-2671. https://doi.org/10.1016/j.bpj.2017.05.014.

4. van Wijk RC, Lucía Quintana A, Ramón-García S. 2023. *Mycobacterium tuberculosis* time kill assay data of the standardized protocol within the ERA4TB consortium. figshare. https://doi.org/10.6084/m9.figshare.19766083.v1.

5. van Wijk RC, Lucía A, Sudhakar PK, Sonnenkalb L, Gaudin C, Hoffmann E, Dremierre B, Aguilar-Ayala DA, Dal Molin M, Rybniker J, de Giorgi S, Cioetto-Mazzabò L, Segafreddo G, Manganelli R, Degiacomi G, Recchia D, Pasca MR, Simonsson USH, Ramón-García S. 2023. Implementing best practices on data generation and reporting of *Mycobacterium tuberculosis* in vitro assays within the ERA4TB consortium. iScience 26:106411. https://doi.org/10.1016/j.isci.2023.106411.

6. Kaur P. 2024. Apramycin kills replicating and non-replicating *Mycobacterium tuberculosis* — raw data. figshare. https://doi.org/10.6084/m9.figshare.26462791.v1.

7. Kaur P, Ramya VK, Naveenkumar CN, Bharathkumar K, Singh M, Hobbie SN, Shandil RK, Narayanan S. 2024. Apramycin kills replicating and non-replicating *Mycobacterium tuberculosis*. Front Trop Dis 5:1413211. https://doi.org/10.3389/fitd.2024.1413211.

8. Windels EM, Cool L, Persy E, Swinnen J, Matthay P, Van den Bergh B, Wenseleers T, Michiels J. 2024. Antibiotic dose and nutrient availability differentially drive the evolution of antibiotic resistance and persistence. ISME J 18:wrae070. https://doi.org/10.1093/ismejo/wrae070.

9. Dubey V, Darlow C, Gerada A, Unsworth J, Sheth E, Reza N, Farrington N, Haldenby S, Warren D, Liu X, Howard A, Hope W. 2026. Source Data to "Molecular pharmacodynamics of amoxicillin-clavulanic acid for urinary tract infections caused by *Escherichia coli*" (41467_2026_74323_MOESM4_ESM.xlsx). Nature Communications. https://doi.org/10.1038/s41467-026-74323-2.

10. Dubey V, Darlow C, Gerada A, Unsworth J, Sheth E, Reza N, Farrington N, Haldenby S, Warren D, Liu X, Howard A, Hope W. 2026. Molecular pharmacodynamics of amoxicillin-clavulanic acid for urinary tract infections caused by *Escherichia coli*. Nat Commun 17:7504. https://doi.org/10.1038/s41467-026-74323-2.

11. Cochran WG. 1950. Estimation of bacterial densities by means of the "most probable number". Biometrics 6:105. https://doi.org/10.2307/3001491.

12. Blodgett R. 2023. BAM appendix 2: most probable number from serial dilutions. Bacteriological analytical manual. US Food and Drug Administration, Silver Spring, MD. https://www.fda.gov/food/laboratory-methods-food/bam-appendix-2-most-probable-number-serial-dilutions.

13. Vijay S, Bao NLH, Vinh DN, Nhat LTH, Thu DDA, Quang NL, Trieu LPT, Nhung HN, Ha VTN, Thai PVK, Ha DTM, Lan NH, Caws M, Thwaites GE, Javid B, Thuong NT. 2024. Supplementary file 2 to "Rifampicin tolerance and growth fitness among isoniazid-resistant clinical *Mycobacterium tuberculosis* isolates from a longitudinal study" (elife-93243-supp2-v1.xlsx). eLife. https://doi.org/10.7554/eLife.93243.

14. Fisher RA. 1935. The logic of inductive inference. J R Stat Soc 98:39-82. https://doi.org/10.2307/2342435.

15. Mann HB, Whitney DR. 1947. On a test of whether one of two random variables is stochastically larger than the other. Ann Math Stat 18:50-60. https://doi.org/10.1214/aoms/1177730491.

16. McNemar Q. 1947. Note on the sampling error of the difference between correlated proportions or percentages. Psychometrika 12:153-157. https://doi.org/10.1007/BF02295996.

17. Wilcoxon F. 1945. Individual comparisons by ranking methods. Biom Bull 1:80. https://doi.org/10.2307/3001968.

18. National Committee for Clinical Laboratory Standards. 1999. Methods for determining bactericidal activity of antimicrobial agents; approved guideline. NCCLS document M26-A. National Committee for Clinical Laboratory Standards, Wayne, PA. ISBN 1-56238-384-1.

19. McFarland J. 1907. The nephelometer: an instrument for estimating the number of bacteria in suspensions used for calculating the opsonic index and for vaccines. JAMA 49:1176. https://doi.org/10.1001/jama.1907.25320140022001f.

20. Franzblau SG, DeGroote MA, Cho SH, Andries K, Nuermberger E, Orme IM, Mdluli K, Angulo-Barturen I, Dick T, Dartois V, Lenaerts AJ. 2012. Comprehensive analysis of methods used for the evaluation of compounds against *Mycobacterium tuberculosis*. Tuberculosis (Edinb) 92:453-488. https://doi.org/10.1016/j.tube.2012.07.003.

21. Vilchèze C, Jacobs WR Jr. 2007. The mechanism of isoniazid killing: clarity through the scope of genetics. Annu Rev Microbiol 61:35-50. https://doi.org/10.1146/annurev.micro.61.111606.122346.

22. Campbell EA, Korzheva N, Mustaev A, Murakami K, Nair S, Goldfarb A, Darst SA. 2001. Structural mechanism for rifampicin inhibition of bacterial RNA polymerase. Cell 104:901-912. https://doi.org/10.1016/S0092-8674(01)00286-0.

23. Pym AS, Saint-Joanis B, Cole ST. 2002. Effect of *katG* mutations on the virulence of *Mycobacterium tuberculosis* and the implication for transmission in humans. Infect Immun 70:4955-4960. https://doi.org/10.1128/IAI.70.9.4955-4960.2002.

24. van Soolingen D, de Haas PEW, van Doorn HR, Kuijper E, Rinder H, Borgdorff MW. 2000. Mutations at amino acid position 315 of the *katG* gene are associated with high-level resistance to isoniazid, other drug resistance, and successful transmission of *Mycobacterium tuberculosis* in the Netherlands. J Infect Dis 182:1788-1790. https://doi.org/10.1086/317598.

25. Vijay S, Bao NLH, Vinh DN, Nhat LTH, Thu DDA, Quang NL, Trieu LPT, Nhung HN, Ha VTN, Thai PVK, Ha DTM, Lan NH, Caws M, Thwaites GE, Javid B, Thuong NT. 2024. Rifampicin tolerance and growth fitness among isoniazid-resistant clinical *Mycobacterium tuberculosis* isolates from a longitudinal study. Elife 13:RP93243. https://doi.org/10.7554/eLife.93243.

26. Rabodoarivelo MS, Hoffmann E, Gaudin C, Aguilar-Ayala DA, Galizia J, Sonnenkalb L, Dal Molin M, Cioetto-Mazzabò L, Degiacomi G, Recchia D, Rybniker J, Manganelli R, Pasca MR, Ramón-García S, Lucía A. 2025. Protocol to quantify bacterial burden in time-kill assays using colony-forming units and most probable number readouts for *Mycobacterium tuberculosis*. STAR Protoc 6:103643. https://doi.org/10.1016/j.xpro.2025.103643.

27. Windels EM, Cool L, Persy E, Swinnen J, Matthay P, Van den Bergh B, Wenseleers T, Michiels J. 2024. Data supporting "Antibiotic dose and nutrient availability differentially drive the evolution of antibiotic resistance and persistence". Zenodo. https://doi.org/10.5281/zenodo.7550302.

28. Clinical and Laboratory Standards Institute. 2024. Methods for dilution antimicrobial susceptibility tests for bacteria that grow aerobically, 12th ed. CLSI standard M07. Clinical and Laboratory Standards Institute, Wayne, PA.

29. Clinical and Laboratory Standards Institute. 2026. Performance standards for antimicrobial susceptibility testing, 36th ed. CLSI supplement M100. Clinical and Laboratory Standards Institute, Wayne, PA.

30. Imai K, Keele L, Yamamoto T. 2010. Identification, inference and sensitivity analysis for causal mediation effects. Stat Sci 25:51-71. https://doi.org/10.1214/10-STS321.

31. Baron RM, Kenny DA. 1986. The moderator-mediator variable distinction in social psychological research: conceptual, strategic, and statistical considerations. J Pers Soc Psychol 51:1173-1182. https://doi.org/10.1037/0022-3514.51.6.1173.

32. Tobin J. 1958. Estimation of relationships for limited dependent variables. Econometrica 26:24. https://doi.org/10.2307/1907382.

33. Beal SL. 2001. Ways to fit a PK model with some data below the quantification limit. J Pharmacokinet Pharmacodyn 28:481-504. https://doi.org/10.1023/A:1012299115260.

34. Rubin DB. 1987. Multiple imputation for nonresponse in surveys. John Wiley & Sons, New York, NY. https://doi.org/10.1002/9780470316696.

35. McCullagh P. 1980. Regression models for ordinal data. J R Stat Soc Series B Stat Methodol 42:109-127. https://doi.org/10.1111/j.2517-6161.1980.tb01109.x.

36. Brant R. 1990. Assessing proportionality in the proportional odds model for ordinal logistic regression. Biometrics 46:1171-1178.

37. Peterson B, Harrell FE Jr. 1990. Partial proportional odds models for ordinal response variables. J R Stat Soc Ser C Appl Stat 39:205. https://doi.org/10.2307/2347760.

38. Turnbull BW. 1976. The empirical distribution function with arbitrarily grouped, censored and truncated data. J R Stat Soc Series B Stat Methodol 38:290-295. https://doi.org/10.1111/j.2517-6161.1976.tb01597.x.

39. Kaplan EL, Meier P. 1958. Nonparametric estimation from incomplete observations. J Am Stat Assoc 53:457-481. https://doi.org/10.1080/01621459.1958.10501452.

40. Cox DR. 1972. Regression models and life-tables. J R Stat Soc Series B Stat Methodol 34:187-202. https://doi.org/10.1111/j.2517-6161.1972.tb00899.x.

41. Field CA, Welsh AH. 2007. Bootstrapping clustered data. J R Stat Soc Series B Stat Methodol 69:369-390. https://doi.org/10.1111/j.1467-9868.2007.00593.x.

42. Schoenfeld D. 1982. Partial residuals for the proportional hazards regression model. Biometrika 69:239-241. https://doi.org/10.1093/biomet/69.1.239.

43. Grambsch PM, Therneau TM. 1994. Proportional hazards tests and diagnostics based on weighted residuals. Biometrika 81:515-526. https://doi.org/10.1093/biomet/81.3.515.

44. Efron B. 1979. Bootstrap methods: another look at the jackknife. Ann Stat 7:1-26. https://doi.org/10.1214/aos/1176344552.

45. Brown LD, Cai TT, DasGupta A. 2001. Interval estimation for a binomial proportion. Stat Sci 16:101-133. https://doi.org/10.1214/ss/1009213286.

46. Benjamini Y, Hochberg Y. 1995. Controlling the false discovery rate: a practical and powerful approach to multiple testing. J R Stat Soc Series B Stat Methodol 57:289-300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x.

47. Harris CR, Millman KJ, van der Walt SJ, Gommers R, Virtanen P, Cournapeau D, Wieser E, Taylor J, Berg S, Smith NJ, Kern R, Picus M, Hoyer S, van Kerkwijk MH, Brett M, Haldane A, del Río JF, Wiebe M, Peterson P, Gérard-Marchant P, Sheppard K, Reddy T, Weckesser W, Abbasi H, Gohlke C, Oliphant TE. 2020. Array programming with NumPy. Nature 585:357-362. https://doi.org/10.1038/s41586-020-2649-2.

48. Virtanen P, Gommers R, Oliphant TE, Haberland M, Reddy T, Cournapeau D, Burovski E, Peterson P, Weckesser W, Bright J, van der Walt SJ, Brett M, Wilson J, Millman KJ, Mayorov N, Nelson ARJ, Jones E, Kern R, Larson E, Carey CJ, Polat İ, Feng Y, Moore EW, VanderPlas J, Laxalde D, Perktold J, Cimrman R, Henriksen I, Quintero EA, Harris CR, Archibald AM, Ribeiro AH, Pedregosa F, van Mulbregt P, SciPy 1.0 Contributors. 2020. SciPy 1.0: fundamental algorithms for scientific computing in Python. Nat Methods 17:261-272. https://doi.org/10.1038/s41592-019-0686-2.

49. McKinney W. 2010. Data structures for statistical computing in Python. Proceedings of the 9th Python in Science Conference 56-61. https://doi.org/10.25080/Majora-92bf1922-00a.

50. Seabold S, Perktold J. 2010. Statsmodels: econometric and statistical modeling with Python. Proceedings of the 9th Python in Science Conference 92-96. https://doi.org/10.25080/Majora-92bf1922-011.

51. Davidson-Pilon C. 2019. lifelines: survival analysis in Python. J Open Source Softw 4:1317. https://doi.org/10.21105/joss.01317.

52. Piranfar V. 2026. Analysis code, audit scripts and headroom tool for "The detection floor bounds tolerance endpoints in Mycobacterium tuberculosis". GitHub. https://github.com/piranfar/detection-floor-tolerance-endpoints.

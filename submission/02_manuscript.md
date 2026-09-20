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

¹Department of Microbiology, Iran University of Medical Sciences, Tehran, Iran

ORCID: [0000-0003-3653-5739](https://orcid.org/0000-0003-3653-5739)

**Correspondence:** Vahhab Piranfar, vahab.p@gmail.com

**Figures:** 2 | **Tables:** 3 | **Boxes:** 2 | **Supplemental figures:** 5 | **Supplemental tables:** 26

---

## Abstract

A culture that grows nothing after antibiotic exposure has never proved
sterility, so tolerance is scored by how far the count fell: the minimum duration
for killing. That endpoint is a fraction of the starting count, so the starting
count should cancel, and in the definition it does. It stops cancelling once
killing reaches the lowest density the assay can report, because the recorded
fraction is then the assay floor divided by the starting density, and the drug
has dropped out of it.

Two boundaries follow from the definitions alone. For an assay floor *L*, a
*q*-log endpoint is observable only in cultures started above *L*·10^*q*; that is
reachability. Above *L*/*c*₁, with *c*₁ the lowest class threshold, a reading
resting on the floor is compatible with only the lowest tolerance class, whatever
the drug did; that is identifiability. Reaching the floor is the drug's doing;
the label it permits is not.

Seventy-eight published time-kill datasets were assembled and 45 inspected in
full; of the 40 distinct literature deposits among them, 32 state no assay floor
by any route. Five are reanalysed here — the floor derived in two, inferred in
one and absent in two — and one new experiment tests both boundaries forward.

Of 217 *Mycobacterium tuberculosis* isolates classified for rifampicin tolerance,
33 began too close to the floor to show the 99.99 per cent reduction the
classification is cut on, and all 33 are recorded as failing to reach it.
Eighteen ended with their reading on the floor: twelve admit one tolerance class,
six admit two. The label tracks how fast an isolate grows; it also tracks
isoniazid resistance, but most of that runs through the starting density, which
is ten-fold lower in the resistant isolates.

Prospectively, *Escherichia coli* ATCC 25922 at the standard inoculum could
report 3.71 to 3.93 logs of killing at a 10 µL plating and 4.88 to 5.05 at
100 µL in the same cultures; at a cut of 10⁻³, six of 54 sample-times took two
labels from one culture, the plated volume deciding. Across the volumes these
laboratories actually plate, 100 down to 2.5 µL, demonstrable depth moves by
1.60 log10 as exact arithmetic. A tolerance call reported without its starting
density and its assay floor cannot be interpreted.

**Keywords:** time-kill assay; limit of quantification; minimum duration for
killing; antibiotic tolerance; colony counting; censored data;
*Mycobacterium tuberculosis*

## Introduction

Tuberculosis treatment runs for four to six months (1). Shortening it means
finding drugs that kill *Mycobacterium tuberculosis* faster, and that choice is
made in a flask: the compounds that could shorten a regimen are picked out of
in vitro killing experiments. The experiment is simple — grow the organism,
add the drug, and at set times dilute a sample, spread it on a plate, and
count the colonies, each standing for one bacterium alive when it was plated —
and the counts over time are the killing curve.

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

The field's response was to engineer around the warning rather than ignore it.
Rather than asking whether a culture went negative, the modern definition asks
how many logs the population fell: the minimum duration for killing, MDK, is the
time to a specified fractional reduction — 90, 99 or 99.99 per cent — and it is
proposed as the tolerance counterpart to the minimum inhibitory concentration
(2, 3). The choice of a *fraction* is the whole point. A ratio to the
starting population is scale-free: if the count falls in a straight line on a log
scale at rate *b*, the time to a *q*-log reduction is *q/b*, and the starting
density cancels. By construction, MDK cannot be contaminated by how much culture
went into the tube. That is the property it was built to have.

Two things are worth separating before going further. As defined by Brauner and
colleagues and codified in the field's consensus guidelines, MDK is not a
plate-count metric — it was first measured from presence or absence of
survivors in microwell arrays of about a hundred cells, a design chosen
specifically to avoid dilution plating, and the guidelines say how the
smallest detectable count should be established (3, 4). What this paper
examines is the form the tuberculosis field adopted: log-reduction endpoints
computed from plate counts and most-probable-number series against a measured
starting density. The floor problem belongs to that implementation, not the
definition, and every deposit here uses it.

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
series, and either a plated volume or a stated floor — and most do not. Of 78
candidate time-kill datasets assembled for this study, 45 were inspected in
full; of the 40 distinct literature deposits among them, **32 state no assay
floor by any route**. That number is not a preamble to the analysis; it is the first
result, and it is why the five deposits carried forward are five rather than
fifty (Table S1).

If the hypothesis holds, a tolerance call reported without its starting density
and its assay floor cannot be interpreted, and the phenotypes assigned in its
name are, in part, a record of how the assay was set up.
---

**Box 1. Four numbers that score an MDK.** *N₀* is the starting density. *L* is
the smallest positive count the method can report — one colony in a plated volume
*v* µL is *L* = 1 000/*v* per mL, and an MPN series uses the lowest table rung (5, 6).
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
MPN table (5, 6) — a fixed ladder of rungs, not a continuous scale. The
day-5 column does not taper towards zero. It stops. Eighteen isolates sit at
exactly 23 per mL in the 15-day panel and six in the 60-day panel, and nothing in
the file lies below that (Fig. 1A). That is a floor, not a tail, and it is
treated as one throughout.

Each isolate therefore carries a fixed budget of killing the assay can see. At 15
days of prior culture the starting densities run from 2 300 to 61 000 000 per mL
— 3.36 to 7.79 log10 — so headroom, the distance from the starting density down
to the floor, runs from 2.00 to 6.42 log10 (Fig. 1B, Table 1). Both spans are the
same 4.42 log10. Subtracting the displayed endpoints does not reproduce that, and
should not: every log10 here is computed from the raw most-probable-number rungs
against a floor of 23 per mL and rounded once, at the end, so the deepest
headroom displays as 6.42 rather than as the 6.43 that 7.79 minus 1.36 returns.
The fold figures quoted throughout are likewise ten raised to the unrounded
difference rather than to the displayed one. Against that budget the three deposited endpoints behave
very differently. Every isolate has the room for a 90 or a 99 per cent reduction:
0 of 217 fall short in both cases. **Thirty-three of 217 isolates — 15.2 per
cent — lack the headroom for the 99.99 per cent endpoint**, which is to say that
a four-log reduction was unobservable for them before rifampicin was added. Two
of those 33 carry a fourth label that the deposit writes literally as "MDR",
conventionally multidrug-resistant. It is unordered with respect to the other
three, so no ordered analysis can place it (Table S2); over the 203 isolates with
an ordered label the same count is 31.

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
A single cut on the starting density alone reproduces all eighteen (Table 2).
That is a statement about the classification step and not about the killing: once
a reading is censored at the floor, the starting density fixes which label the
published rule is able to return.

So for twelve of the eighteen the recorded label carries no information beyond
the fact that the reading was censored, and for six it is not determinate at all.
None of the eighteen is a measurement of the surviving fraction.

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

### 4. What the plate misses is not only what lies below its floor

Everything above is about the floor. One published observation in this organism
shows that the floor is not the only reason a colony count understates the
population, and it is set out here because the two failures are easy to confuse
and must not be.

Evangelopoulos and colleagues counted the
same mouse lungs three ways — colony count, a molecular bacterial load from 16S
rRNA, and a most probable number — on their way to a different question (7).
Under the deepest regimens the colony count reads zero in every animal. In three
arms, 18 lungs in all, the plate declared every lung sterile while the most
probable number on that same tissue ran from 1 450 to 18 700 per lung. The
molecular load can be dismissed as nucleic acid outliving its owner. The most
probable number cannot, because it is a culture, and growth in a dilution series
requires an organism that is alive and culturable.

That gap is not the detection floor, and the arithmetic says so. Neither assay's
floor is reported in the deposit, but for censoring to explain a plate reading of
zero against 1 450 organisms in the same tissue, the colony count's floor would
have to sit above 1 450 per lung — which would mean plating a vanishingly small
fraction of the homogenate, far less than any lung protocol plates. The
organisms were there, they were alive, they grew in a liquid dilution series, and
they did not form colonies on solid medium. That is differential culturability,
not censoring. It is a described phenotype of *M. tuberculosis* with a literature
of its own: bacilli that require resuscitation-promoting factors to grow dominate
pre-treatment sputum and rise as a proportion of the population during
chemotherapy (8), both resuscitation-promoting-factor-dependent and
-independent differentially culturable populations are recovered from patients
whose solid-medium cultures return nothing (9), and the mechanism has been
reproduced experimentally: rifamycin action on RNA polymerase, independent of
any assay's floor, converts a starved population to over 90 per cent
differentially detectable in vitro (10) — the same drug class every arm of
the Evangelopoulos regimen carries.

Keeping the two apart matters for what this paper claims. Reachability and
identifiability are arithmetic on the plated volume; they hold whether or not
every viable organism forms a colony, and they would hold in an assay with
perfect culturability. Differential culturability is biology, it acts on the
numerator rather than on the floor, and nothing in this paper derives it or
measures it. Neither depends on the other, and they push the same way: a
count that is both floored and culture-selective understates the surviving
population twice over, and a log-reduction endpoint read off that count inherits
the pair of them. The mouse model that decides which regimens enter clinical trials reads out
in colony counts, and this is the region it reads them in.

Back to the floor itself, and to what it costs. That deposit establishes no
floor of its own. Five further *M. tuberculosis* deposits in the same screen do,
and they are not reassuring. Across those five —
sputum from pulmonary tuberculosis, axenic culture, an auxotrophic H37Rv panel and
two drug-development series, with floors from 13 to 200 CFU/mL — **184 of 310
series could not have demonstrated a four-log reduction however completely the
drug worked, and 240 of 310 could not have demonstrated five** (Table S4). One
of the five could not have shown four logs in a single one of its 123 series. None
of these five carries the analysis above, and none is among the five deposits
reanalysed in this paper; they are what the same screen found
in the same organism, and they say the reachability problem is not a property of
one clinical panel.

### 5. The label tracks how fast an isolate grows, and its link to resistance cannot be separated from the inoculum

We asked what the deposited tolerance label goes with. There are two candidate
predictors, and each is tested at two culture ages and at two endpoint depths,
which is eight tests in all. Eight tests on one question will throw up a false
positive on their own, so we correct them together as one family. Two survive
(Table S5).

The label tracks the **growth rate** of the isolate. Slower growth goes with a
higher tolerance class, and it survives adjustment for starting density
(OR 1.096 per day of time to OD 0.4, 95 per cent CI 1.032 to 1.164, p = 0.0030,
n = 202; unadjusted OR 1.126, 1.062 to 1.193). The label also tracks **isoniazid
resistance** — until the starting density enters the model. On its own, a
resistant isolate has 2.32 times the odds of a higher tolerance class (95 per
cent CI 1.30 to 4.12, p = 0.0042). Adjusted for starting density the odds ratio
falls to 1.31 (0.67 to 2.57, p = 0.42), and the interval no longer excludes one.
The two figures estimate different things: the unadjusted 2.32 is the total
effect of resistance on the label, and the adjusted 1.31 is the controlled
direct effect with the inoculum held fixed, since starting density sits on
the causal path as a mediator here rather than as a confounder — the mediation
decomposition is Table S6. Call this attenuation rather than elimination: 185 of
the 203 calls still rest on a measured, uncensored numerator. Starting density
is the strongest term in the file: every ten-fold rise in the starting most
probable number halves the odds of a higher tolerance class (OR 0.480, 0.340 to
0.677, p = 2.9 × 10⁻⁵).

Why the adjustment does that is measurable. Isoniazid-resistant isolates go into
this assay at 5.36 log10 against 6.36 for susceptible isolates, ten-fold thinner
(Mann–Whitney p = 9.1 × 10⁻¹⁴) (11), and 22 of the 84 resistant isolates
carrying an ordered label lack the headroom for the deepest endpoint, 26.2 per
cent, against 9 of the 119 susceptible, 7.6 per cent. Those two counts are the 31
of Section 1, which is that section's 33 less the two isolates whose label is the
unordered fourth category. They are one log short of observable killing before
the experiment begins.

In that stratum the two surviving associations part company. Growth holds and
still survives correction (OR 1.116, 1.040 to 1.198, p = 0.0024). Resistance
returns OR 2.11 (1.07 to 4.16, p = 0.031) nominally, but ranks second in the
family of eight and fails its Benjamini–Hochberg critical value of 0.0125. The
resistance association therefore leans on isolates that are not
independent of one another, and it is already the association that starting
density explains away. We report it as the weaker of the two on both counts.

### 6. One written protocol does not give every laboratory the same depth to look down

If the effect is a property of assay geometry rather than of clinical sampling,
it should appear where one protocol, one strain and one stock are handed out
deliberately. Van Wijk and colleagues (2023) ran exactly that exercise, sending a
single stock of H37Rv to six blinded laboratories under one written protocol
(12, 13). It does.

At ten times the minimum inhibitory concentration of moxifloxacin all six
laboratories return a positive kill rate, and the rates span 5.2-fold, from 0.090
to 0.464 log10 CFU/mL per day. Across all 30 laboratory-by-arm cells the Tobit
estimate — a fit that treats a below-floor reading as below the floor rather than
as a number — and the imputation estimate never differ by more than 0.006 log10
per day (Fig. 2A, Table S7). That agreement says the fit is not an artefact of the
arithmetic used to reach it. It does not say the sub-floor assumption is safe:
both estimators assume the same normal distribution below the floor, and nothing
in this deposit can check that assumption from the inside.

The two orderings do not correspond. Rank the laboratories by starting density
and the three lowest are exactly the three that recorded crossings, the three
highest exactly the three that did not, without exception — a split with probability 1/20 under chance alone, so it is reported as an ordering and not a test (Table S8). Rank them by kill rate
and there is no such correspondence (Fig. 2B). Institute F has the highest
starting density at 6.53 log10 among the treated flasks of this arm, kills
faster than four of the other five at 0.223
log10 per day, and records no crossing. Institute E returns the slowest rate of
all at 0.090 and also records none.

### 7. The same boundaries hold in an experiment the framework never saw

Every section so far tests the framework on the deposits it was built from, and
all of them are *Mycobacterium tuberculosis*. A search of five general
repositories, the tuberculosis consortia, the persistence literature, food
microbiology and the hollow-fibre field returned one deposit that carried all
three fields the boundaries require and could be analysed cold. That is a
statement about what that search returned, not about what exists.

The point of this section is a deposit opened after every boundary and threshold
was fixed, and only one deposit qualifies on that ground.

That it is *E. coli* in a hollow-fibre system rather than *M. tuberculosis* in a
flask makes it a harder test and not a softer one. A rule fitted to tuberculosis
time-kill data could be expected to fit more tuberculosis time-kill data; what it
has no right to survive is a different organism, a different drug class and a
different apparatus. The boundaries are derived from definitions, so they predict
they will survive exactly that, and this is where that prediction was put at risk.

Dubey and colleagues (2026) report amoxicillin-clavulanate against *Escherichia
coli* in a hollow-fibre system (14, 15). Their Methods state 100 µL plated
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
day zero while the paired control reads about 10⁶. Either that sample was drawn
after exposure rather than before it, or the day-zero value is a placeholder or
a transcription error; the file cannot distinguish the two, and we flag the
reading rather than treat it as a measured time zero.

### 8. One culture, two plated volumes, two tolerance labels

Every result above reads data somebody else generated for another purpose. This
one reads an experiment built to try to break the two boundaries *N*_reach and
*N*_id — the starting densities that decide whether an endpoint is reachable and
a label means anything — with its predictions written down before a plate was
counted. *Escherichia coli* ATCC 25922, of the American Type Culture
Collection — the reference strain the standard names for quality control —
against ciprofloxacin at ten times the concentration that stops it growing. Three
seeding densities, two plated volumes, three flasks each, 216 plate readings.

It is *Escherichia coli* and not *M. tuberculosis*, and that is a design choice
rather than a convenience. Reachability and identifiability are arithmetic on a
plated volume, so they do not know what organism is on the plate; what an organism decides is
whether the experiment can be run at all. Three seeding densities crossed with two
plated volumes and six sampling times is 216 plates that must be counted from one
exposure, and in *M. tuberculosis* that means three to six weeks to colonies,
inside containment, per replicate. Ciprofloxacin drives *E. coli* to the floor
within a working day, which is what makes the floor reachable in every arm and the
prediction falsifiable in a week rather than a year. ATCC 25922 is not a
substitute chosen for ease either: it is the quality-control reference strain the
standard itself names, so the demonstration runs in the one organism whose assay
geometry the standard defines.

The middle arm was seeded on purpose at the 5 × 10⁵ per mL the standard
specifies. The densities actually reached were 6.4 × 10⁴, 4.4 × 10⁵ and
3.8 × 10⁶ per mL, quoted as arm means. Those three figures are means, and every
figure after them is per flask. The distinction is not cosmetic: *N*₀ is not a
setting the protocol supplies but a measurement made once per culture, so
headroom belongs to a flask rather than to an arm. At the 100 µL plating the low
arm's three flasks have 4.19, 4.11 and 4.00 logs of headroom, the last of them
exactly at the four-log endpoint. Everything below is therefore reported per
flask. **At the standard inoculum
plated at 10 µL, the deepest reduction the three flasks could report ran from
3.71 to 3.93 logs — each flask's own ceiling, not the drug's** — while those same
three cultures plated at 100 µL ran from 4.88 to 5.05 (Fig. S5B, Table S10). Every flask is
paired with itself across the two platings, so the comparison is within a culture
rather than between cultures.

That much is arithmetic, as Box 1 says. So is the next step. When both platings
of one sample rest on their own floors, the two fractions written down are
*L*₁/*N*₀ and *L*₂/*N*₀ — two different floors over one starting density — so
they can fall either side of a class threshold and give one culture two labels.
**The quantity that could have come out zero is how often a real experiment lands
in the window where those two fractions straddle the cut**, and it depends on
where the cut is (Fig. S5C, Table S11). Put the cut at one per cent and the window is
nearly shut. Put it at one in a thousand, which is where the clinical
classification analysed above cuts its lowest class, and six of 54 sample-times
receive two different labels from one culture — one in nine. That cut is imported
from the tuberculosis classification; nothing in the E. coli experiment derives
it, and it serves here as a ruler for the window's width, not as a claim about
E. coli biology.

---

## Discussion

Every clinical microbiologist knows that a negative culture taken under
antibiotic exposure is not proof of sterility. This paper reports that the
number brought in to replace that judgement carries the same defect — and once
it is a number, it is harder to see.

The standard is not silent on that choice, and this is the paper's sharpest
finding rather than an awkwardness for it. M26-A's own section 1.3.2.5, headed
*Volume Transferred*, ties the volume to the endpoint with a counting rule:
after the defined 99.9 per cent killing, at least ten colonies must remain
(16) — for a standard inoculum of 5 × 10⁵ per mL that means at least 20 µL
streaked, so a 10 µL streak fails the rule, and section 3.1 separately requires
the smallest detectable count to be established by serial dilution. A guideline
written in 1999 already required both numbers this paper asks for. The
deposits reanalysed here do not meet it, not for lack of care but because the
endpoint moved: M26-A nowhere contemplates a four-log call, and the volume
rule did not travel with the deeper endpoints.

Take the assay's contribution out and what is left makes biological sense.
Growth state predicts the tolerance class before and after adjustment for
starting density — isoniazid needs KatG and active cell-wall synthesis
(17), rifampicin needs transcription (18), and a population that is not
dividing offers less of what these drugs act on. The classification is reading
physiological state, not drug susceptibility.

That axis is the one tuberculosis drug development already leans on. Killing
assays of this design rank regimens before they enter trials, and tolerance
followed in patients is now being read as within-host evolution (19). If a
tolerance classification is partly an inoculum measurement, conclusions drawn
from it — that one regimen sterilises faster than another, that a patient's
isolates are becoming more tolerant over therapy — are in part conclusions
about how the assay was set up. The correction applied here does not remove
the biology; it aims it at the right target. The phenotype that survives the
correction is growth state, which is real, targetable and directly measurable,
unlike a fraction read off a floor.

The prospective experiment has a limitation of its own, and it is the one a
reader of this paper should raise first. Its samples were diluted in saline and
plated; they were not washed, filtered or treated to inactivate the drug, and no
carryover control was run. Antibiotic carried onto the plate suppresses colony
formation without killing anything, which is the same class of counting artefact
this paper is about, and at the shallow dilutions a culture near its floor is
read on, dilution is the only thing containing it. The design is conservative in
this respect rather than clean: the larger plated volume carries ten times more
drug to the plate, so carryover would shrink the very difference between the two
platings that Section 8 reports. It would not manufacture it. But the
experiment cannot exclude carryover, and a repetition should include the control
that would.

Several limitations here bound what the analysis can establish; each points at
the experiment that would settle the question, and the ones bearing on the
claims made are given here, with the rest in the supplement.

This paper has already acted on the first rather than merely declaring it.
Flasks from one laboratory share a starting culture; repeat isolates come from
a patient already counted. Every conclusion from the two primary deposits was
recomputed at the level where the observations really are independent, listed
one line at a time rather than summarised (Table S8): twenty survive
unchanged, six survive with much wider uncertainty, five do not survive and
**have already been removed from the text above**, and one is withdrawn
because the "no difference" it was tested against was already false before
any data were seen. The ledger is printed so a reader can check the dropping
was done rather than promised.

The 15-day and 60-day panels of the clinical deposit contain the same isolates.
The comparison between panels is therefore not independent, and it bounds the
evidence for a difference rather than establishing it.

**Choose the depth of the endpoint to fit the headroom actually available,
rather than densifying the inoculum merely to buy more.** The inoculum this
needs can be worked out before the experiment: seeding above
*L* · max(10^*q*, 1/*c*₁) makes both failure modes impossible — the endpoint
that was never reachable, and the last count that lands on the floor. For this
assay that is 230 000 per mL. Seeding higher also changes the experiment,
because a denser culture is a different physiological state, and physiological
state is what the tolerance label tracks — so where the deep endpoint is
wanted, lower the assay floor; where the headroom will not carry it either
way, the shallower endpoint is the honest one, and growth state belongs on
the report whichever is chosen. This is a design decision that is currently
not being made.

**Treat an endpoint at the floor as a bound, not a value.** Analysed as a
measurement it manufactures differences between isolates whose final viable
burdens the assay could not tell apart, and the same censored reading stands
for a different demonstrated kill at every starting density.

**Fix the inoculum, or adjust for it, before comparing tolerance across groups.**
The comparison that motivated this work — resistant against susceptible isolates
— is confounded by a ten-fold difference in starting density, and nobody knows
why that difference is there. Until it is understood, group comparisons of
tolerance in clinical isolates should carry the starting density as a covariate.

**Box 2. The minimum information a time-kill assay must report.** Five fields
that make a reported tolerance endpoint recomputable by a reader. Each is
produced by the experiment as run; none asks for new apparatus. What they cost is
visible from the other side: of the 78 candidate time-kill datasets assembled
for this study, 45 were inspected in full, and of the 40 distinct literature
deposits among them, 32 state no assay floor by any route — so most published
endpoints cannot be recomputed against their own measurement.

| # | Field | What to report | What fails without it |
|---|---|---|---|
| 1 | Starting density | *N*₀ with its method (viable count or MPN value, not an optical density) | the endpoint is a fraction of *N*₀; OD-derived densities disagreed with the measured ones by up to 1.53-fold within one culture here |
| 2 | Assay floor | *L* as a value, or the plated volume / dilution design that fixes it | nothing deeper than log10(*N*₀/*L*) was ever visible; without *L* a failed endpoint is arithmetic |
| 3 | Censoring convention | what is written when nothing grows: zero, the floor value, ND, or the lowest table rung | the convention decides whether a floor reading is a bound or a measurement |
| 4 | Endpoint rule | the *q* in MDK_q and the interpolation between sample times | one kill curve returns different durations under different rules |
| 5 | Physiological state | culture age or growth phase at sampling, as a recorded value | the label tracks state; unrecorded, state is confounded with every group compared |

A report carrying all five can be audited against its own floor, which is the
test applied to every deposit in this article.

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

The consequence is that a tolerance call made without its headroom cannot be
told apart from an inoculum measurement, and that the phenotype which does
survive the correction is physiological state rather than drug susceptibility —
not that tolerance is an artefact. Report the starting density and the assay floor.
Match the depth of the endpoint to the range actually available. Treat a reading
at the floor as a bound. Do those three things and a tolerance classification
would mean the same in one laboratory as in the next. Until then, some of what
the field calls tolerance cannot be separated from a record of how much culture
went into the tube.

What this study adds is a way to see the problem before the plates are poured:
two boundaries computed from quantities a time-kill protocol already records,
a classification that refuses rather than guesses when the assay cannot decide
(Table S12), a five-field minimum that makes any killing endpoint recomputable
(Box 2), and a small tool that returns the endpoint a planned assay can
support. None of it asks a laboratory for a new measurement; the cost is five
numbers written down. The return is a tolerance phenotype that means the same
in one laboratory as in the next, and that can bear the weight regimen
research already puts on it.

---

## Materials and Methods

*The condensed account. The full account, with every estimator and every sensitivity analysis, is Supplementary Methods in the supplemental file.*

### Ethics

This study reanalysed publicly available, de-identified datasets deposited by
other groups, and generated one time-kill experiment in a reference strain of
*Escherichia coli*. No human or animal subjects were involved, no patient samples
were collected, and no individual is identifiable from any material presented
here. The prospective experiment was performed at the Department of
Microbiology, Iran University of Medical Sciences, Tehran, Iran, on a
biosafety-level-1-appropriate quality-control strain (ATCC 25922); no
institutional review board holds jurisdiction over secondary analysis of
de-identified public data or over work on a bacterial quality-control strain.

### Use of generative artificial intelligence

Anthropic's Claude was used under the author's direction to read the
manuscript and to assist in running the Python analysis pipeline. Claude
Sonnet 5 was further used, under the author's direction, to document and
organise the analysis code and to prepare its commits to the version-controlled
repository. No figure, image or schematic was generated by an artificial
intelligence tool; every figure is plotted from values that regenerate from the
public deposits. No artificial intelligence tool is an author. The author
directed the study, verified every reported quantity against the source
deposits and the regenerating pipeline, and takes full responsibility for the
content of this
article, including its accuracy and its originality.

### Data availability

Every dataset reanalysed here was already public under an open licence and none
was generated for this study. Each is identified in Table 3 and cited alongside
the article that first described it: Vijay and colleagues (20, 21), van Wijk
and colleagues (12, 13), Windels and colleagues (22, 23), Kaur and
colleagues (24, 25), and the hollow-fibre Source Data of Dubey and
colleagues (14, 15), held out of every fitting step. The readings from the
prospective experiment are deposited with the analysis code.

That code, both audit scripts, the headroom tool and the machine-readable
receipts recording the software versions each stage ran under are in a public
repository (26), with the documentation and test data needed to run them. It
is dual-licensed: the code under the Massachusetts Institute of Technology (MIT)
licence, and the manuscript, figures and results under CC BY 4.0. The deposits
keep their depositors' own licences. It is at
https://github.com/piranfar/detection-floor-tolerance-endpoints, and this
manuscript was built from commit ada65b7+ of it — the state of the repository
the text describes, rather than the commit that records the build. A trailing
plus sign, if present, marks a build made with uncommitted changes in the tree.

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


## Supplemental material

The supplemental file carries the full Materials and Methods, the analyses named above as supplementary text, and 26 supplemental tables. Of those, 14 belong to analyses reported in that file rather than in this article, and are cited there at the point where each is used.


## Tables

**Table 1.** The reduction each tolerance endpoint requires against the reduction the assay can resolve.

| Prior culture | Endpoint | Isolates | Short of headroom | Fraction short | At ceiling: short vs ample |
| --- | ---: | ---: | ---: | ---: | ---: |
| 15 days | 90% (1 log) | 217 | 0 | 0.0% | - |
| 15 days | 99% (2 log) | 217 | 0 | 0.0% | - |
| 15 days | 99.99% (4 log) | 217 | 33 | 15.2% | 100% vs 88% |
| 60 days | 90% (1 log) | 210 | 0 | 0.0% | - |
| 60 days | 99% (2 log) | 210 | 0 | 0.0% | - |
| 60 days | 99.99% (4 log) | 210 | 7 | 3.3% | 100% vs 95% |

*Note.* In the 15-day and the 60-day prior-culture panel alike. Headroom is the distance from an isolate's starting density down to the day-5 MPN floor of 23 per mL. An isolate short of headroom cannot reach that endpoint however completely the drug worked, and every such isolate is recorded at the assay ceiling.

**Table 2.** Isolates whose day-5 reading was censored at the MPN floor.

| Prior culture | At the floor | Starting density spread | Recorded survival spread | Labels assigned at the floor | Ordered calls | Measured | Single compatible class | Multiple compatible classes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 15 days | 18 | 265x | 265x | Low: 12, Medium: 6 | 203 | 185 | 12 | 6 |
| 60 days | 6 | 100x | 100x | Low: 6 | 197 | 191 | 6 | 0 |

*Note.* Starting densities differ across the row, so the same floor-level reading implies a different range of compatible fractional reductions in each; the recorded fraction is L/N0, so the spread in apparent survival equals the spread in starting density exactly, and the labels differ accordingly. The last four columns sort every call in the 15-day panel, not only the censored ones: a censored reading bounds the class from above, and sweeping the true count across the admissible range leaves twelve calls with a single compatible class and six with more than one. Reaching the floor at all is a property of the killing; which class is then compatible is a property of the starting density and the floor. Ordered calls is the denominator those four columns are taken over, and it is not the isolate count of Table 1: it counts only the isolates whose deposited label is one of the three ordered classes, leaving out the 14 at 15 days and the 13 at 60 days that carry the unordered fourth category.

**Table 3.** The five published deposits reanalysed.

| Dataset | Organism | Drug and range | Design | Deposit | Licence |
| --- | --- | --- | --- | --- | --- |
| Six-laboratory exercise | *M. tuberculosis* H37Rv | moxifloxacin, isoniazid, 1x and 10x MIC | 90 flasks, 2 775 readings | figshare 19766083 | CC BY 4.0 |
| Clinical isolates | *M. tuberculosis*, 217 isolates | rifampicin | 6 duration endpoints per isolate | eLife 93243, suppl. file 2 | CC BY 4.0 |
| Evolved clones | *E. coli*, 126 clones | amikacin | MIC and persister fraction per clone | Zenodo 7550302 (23) | CC BY 4.0 |
| Concentration-by-time grid | *M. tuberculosis* | apramycin 1-128 ug/mL (amikacin arm not analysed) | 5 concentrations x 4 days x 3 replicates | figshare 26462791 | CC BY 4.0 |
| Analysed last, after the derivation was fixed | *E. coli*, hollow fibre | amoxicillin-clavulanate | 20 cultures, measured day-zero density, 100 uL plated | Nat Commun 2026 Source Data | CC BY 4.0 |

*Note.* Four carry the analysis and the fifth was analysed last, to test it. None was generated for this study. That fifth deposit was opened after every boundary and threshold was fixed: the headroom tool at 00:08 and the symbolic recovery of both boundary laws at 01:34 on 6 September 2026, against the deposit's arrival at 02:41 the same morning. The deposit entered in the same commit as the script that tests it, which git cannot order internally, so it is where reachability and identifiability were committed that dates the hold-out, not where the deposit arrived. This is an attestation and not a registration: the deposit had been public since its article appeared on 13 June 2026, so nothing outside this repository's own commit history evidences that it was not opened earlier, and a reader should weigh it accordingly. The other four were selected for the fields they carry, and that selection is not separately registered.


## References

1. World Health Organization. 2022. WHO consolidated guidelines on tuberculosis. Module 4: treatment — drug-susceptible tuberculosis treatment. World Health Organization, Geneva, Switzerland. https://iris.who.int/handle/10665/353829.

2. Brauner A, Fridman O, Gefen O, Balaban NQ. 2016. Distinguishing between resistance, tolerance and persistence to antibiotic treatment. Nat Rev Microbiol 14:320-330. https://doi.org/10.1038/nrmicro.2016.34.

3. Brauner A, Shoresh N, Fridman O, Balaban NQ. 2017. An experimental framework for quantifying bacterial tolerance. Biophys J 112:2664-2671. https://doi.org/10.1016/j.bpj.2017.05.014.

4. Balaban NQ, Helaine S, Lewis K, Ackermann M, Aldridge B, Andersson DI, Brynildsen MP, Bumann D, Camilli A, Collins JJ, Dehio C, Fortune S, Ghigo J-M, Hardt W-D, Harms A, Heinemann M, Hung DT, Jenal U, Levin BR, Michiels J, Storz G, Tan M-W, Tenson T, Van Melderen L, Zinkernagel A. 2019. Definitions and guidelines for research on antibiotic persistence. Nat Rev Microbiol 17:441-448. https://doi.org/10.1038/s41579-019-0196-3.

5. Cochran WG. 1950. Estimation of bacterial densities by means of the "most probable number". Biometrics 6:105. https://doi.org/10.2307/3001491.

6. Blodgett R. 2023. BAM appendix 2: most probable number from serial dilutions. Bacteriological analytical manual. US Food and Drug Administration, Silver Spring, MD. https://www.fda.gov/food/laboratory-methods-food/bam-appendix-2-most-probable-number-serial-dilutions.

7. Evangelopoulos D, Prosser G, Rodgers A, Dagg B, Khatri B, Bhagwat A, Gonzalo X, Kolyva A, Bertozzi G, Silva-Pereira TT, Gibbons N, Bhatt A, Sabharwal N, Perdigao J, Portugal I, Rodrigues C, Duarte R, Gomes M, Cirillo DM, McHugh TD. 2022. Data from: Comparative evaluation of viable count, molecular bacterial load and most probable number for the enumeration of Mycobacterium tuberculosis in murine tissue. University College London Research Data Repository. https://doi.org/10.5522/04/19175153.v2. Retrieved 2026-09-07.

8. Mukamolova GV, Turapov O, Malkin J, Woltmann G, Barer MR. 2010. Resuscitation-promoting factors reveal an occult population of tubercle bacilli in sputum. Am J Respir Crit Care Med 181:174-180. https://doi.org/10.1164/rccm.200905-0661OC.

9. Chengalroyen MD, Beukes GM, Gordhan BG, Streicher EM, Churchyard G, Hafner R, Warren R, Otwombe K, Martinson N, Kana BD. 2016. Detection and quantification of differentially culturable tubercle bacteria in sputum from patients with tuberculosis. Am J Respir Crit Care Med 194:1532-1540. https://doi.org/10.1164/rccm.201604-0769OC.

10. Saito K, Warrier T, Somersan-Karakaya S, Kaminski L, Mi J, Jiang X, Park S, Shigyo K, Gold B, Roberts J, Weber E, Jacobs WR Jr, Nathan CF. 2017. Rifamycin action on RNA polymerase in antibiotic-tolerant Mycobacterium tuberculosis results in differentially detectable populations. Proc Natl Acad Sci U S A 114:E4832-E4840. https://doi.org/10.1073/pnas.1705385114.

11. Mann HB, Whitney DR. 1947. On a test of whether one of two random variables is stochastically larger than the other. Ann Math Stat 18:50-60. https://doi.org/10.1214/aoms/1177730491.

12. van Wijk RC, Lucía A, Sudhakar PK, Sonnenkalb L, Gaudin C, Hoffmann E, Dremierre B, Aguilar-Ayala DA, Dal Molin M, Rybniker J, de Giorgi S, Cioetto-Mazzabò L, Segafreddo G, Manganelli R, Degiacomi G, Recchia D, Pasca MR, Simonsson USH, Ramón-García S. 2023. Implementing best practices on data generation and reporting of *Mycobacterium tuberculosis* in vitro assays within the ERA4TB consortium. iScience 26:106411. https://doi.org/10.1016/j.isci.2023.106411.

13. van Wijk RC, Lucía Quintana A, Ramón-García S. 2023. *Mycobacterium tuberculosis* time kill assay data of the standardized protocol within the ERA4TB consortium. figshare. https://doi.org/10.6084/m9.figshare.19766083.v1.

14. Dubey V, Darlow C, Gerada A, Unsworth J, Sheth E, Reza N, Farrington N, Haldenby S, Warren D, Liu X, Howard A, Hope W. 2026. Molecular pharmacodynamics of amoxicillin-clavulanic acid for urinary tract infections caused by *Escherichia coli*. Nat Commun 17:7504. https://doi.org/10.1038/s41467-026-74323-2.

15. Dubey V, Darlow C, Gerada A, Unsworth J, Sheth E, Reza N, Farrington N, Haldenby S, Warren D, Liu X, Howard A, Hope W. 2026. Source Data to "Molecular pharmacodynamics of amoxicillin-clavulanic acid for urinary tract infections caused by *Escherichia coli*" (41467_2026_74323_MOESM4_ESM.xlsx). Nature Communications. https://doi.org/10.1038/s41467-026-74323-2.

16. National Committee for Clinical Laboratory Standards. 1999. Methods for determining bactericidal activity of antimicrobial agents; approved guideline. NCCLS document M26-A. National Committee for Clinical Laboratory Standards, Wayne, PA. ISBN 1-56238-384-1.

17. Vilchèze C, Jacobs WR Jr. 2007. The mechanism of isoniazid killing: clarity through the scope of genetics. Annu Rev Microbiol 61:35-50. https://doi.org/10.1146/annurev.micro.61.111606.122346.

18. Campbell EA, Korzheva N, Mustaev A, Murakami K, Nair S, Goldfarb A, Darst SA. 2001. Structural mechanism for rifampicin inhibition of bacterial RNA polymerase. Cell 104:901-912. https://doi.org/10.1016/S0092-8674(01)00286-0.

19. March VFA, Mchedlishvili K, Goig GA, Maghradze N, Avaliani T, Aspindzelashvili R, Avaliani Z, Kipiani M, Tukvadze N, Jugheli L, Bouaouina S, Doetsch A, Kalkan S, Reinhardt M, Gagneux S, Borrell S. 2025. Within-host evolution of drug tolerance in *Mycobacterium tuberculosis*. bioRxiv 2025.07.29.667394; preprint, not peer reviewed. https://doi.org/10.1101/2025.07.29.667394.

20. Vijay S, Bao NLH, Vinh DN, Nhat LTH, Thu DDA, Quang NL, Trieu LPT, Nhung HN, Ha VTN, Thai PVK, Ha DTM, Lan NH, Caws M, Thwaites GE, Javid B, Thuong NT. 2024. Supplementary file 2 to "Rifampicin tolerance and growth fitness among isoniazid-resistant clinical *Mycobacterium tuberculosis* isolates from a longitudinal study" (elife-93243-supp2-v1.xlsx). eLife. https://doi.org/10.7554/eLife.93243.

21. Vijay S, Bao NLH, Vinh DN, Nhat LTH, Thu DDA, Quang NL, Trieu LPT, Nhung HN, Ha VTN, Thai PVK, Ha DTM, Lan NH, Caws M, Thwaites GE, Javid B, Thuong NT. 2024. Rifampicin tolerance and growth fitness among isoniazid-resistant clinical *Mycobacterium tuberculosis* isolates from a longitudinal study. Elife 13:RP93243. https://doi.org/10.7554/eLife.93243.

22. Windels EM, Cool L, Persy E, Swinnen J, Matthay P, Van den Bergh B, Wenseleers T, Michiels J. 2024. Data supporting "Antibiotic dose and nutrient availability differentially drive the evolution of antibiotic resistance and persistence". Zenodo. https://doi.org/10.5281/zenodo.7550302.

23. Windels EM, Cool L, Persy E, Swinnen J, Matthay P, Van den Bergh B, Wenseleers T, Michiels J. 2024. Antibiotic dose and nutrient availability differentially drive the evolution of antibiotic resistance and persistence. ISME J 18:wrae070. https://doi.org/10.1093/ismejo/wrae070.

24. Kaur P. 2024. Apramycin kills replicating and non-replicating *Mycobacterium tuberculosis* — raw data. figshare. https://doi.org/10.6084/m9.figshare.26462791.v1.

25. Kaur P, Ramya VK, Naveenkumar CN, Bharathkumar K, Singh M, Hobbie SN, Shandil RK, Narayanan S. 2024. Apramycin kills replicating and non-replicating *Mycobacterium tuberculosis*. Front Trop Dis 5:1413211. https://doi.org/10.3389/fitd.2024.1413211.

26. Piranfar V. 2026. Analysis code, audit scripts and headroom tool for "The detection floor bounds tolerance endpoints in Mycobacterium tuberculosis". GitHub. https://github.com/piranfar/detection-floor-tolerance-endpoints.

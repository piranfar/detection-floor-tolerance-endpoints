---
title: "Rifampicin tolerance classification is bounded by assay detection floor among clinical Mycobacterium tuberculosis isolates"
short_title: "Assay detection floor bounds rifampicin tolerance classification"
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

# Rifampicin tolerance classification is bounded by assay detection floor among clinical *Mycobacterium tuberculosis* isolates

**Author:** Vahhab Piranfar¹

¹Department of Microbiology, Iran University of Medical Sciences, Tehran, Iran

ORCID: [0000-0003-3653-5739](https://orcid.org/0000-0003-3653-5739)

**Correspondence:** Vahhab Piranfar, vahab.p@gmail.com

**Figures:** 2 | **Tables:** 15 | **Boxes:** 2 | **Supplementary figures:** 5 | **Supplementary tables:** 14

---

## Introduction

Tuberculosis treatment runs for four to six months [[R1]]. Shortening it means
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
[[R2]][[R3]]. The choice of a *fraction* is the whole point. A ratio to the
starting population is scale-free: if the count falls in a straight line on a log
scale at rate *b*, the time to a *q*-log reduction is *q/b*, and the starting
density cancels. By construction, MDK cannot be contaminated by how much culture
went into the tube. That is the property it was built to have.

Two things are worth separating before going further. As defined by Brauner and
colleagues and codified in the field's consensus guidelines, MDK is not a
plate-count metric — it was first measured from presence or absence of
survivors in microwell arrays of about a hundred cells, a design chosen
specifically to avoid dilution plating, and the guidelines say how the
smallest detectable count should be established [[R3]][[R56]]. What this paper
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

The bound is already in the papers that defined the assays. Vijay and colleagues,
introducing the most-probable-number MDK for rifampicin — a count read off a
dilution series rather than off colonies on a plate — treated an MDK99.99 longer
than ten days as high tolerance beyond the **time** window of the assay, not as a
statement about the count floor [[R53]]. In the 217-isolate classification that
follows from that assay they report that MDK99.99 at 15 days of recovery could be
calculated for only 22 of 209 isolates and that the rest lay, in their words,
"beyond the assay limits" [[R51]]. The ERA4TB consortium requires below- and
above-quantification-limit flags together with the limit of quantification, and
notes that pharmacometric models can use those flags [[R23]]; the same
six-laboratory comparison then excluded both from its numerical analysis. Their
2025 protocol states the geometry of the pipette explicitly: a 2.5 µL drop has a
limit of detection above 2.6 log10 CFU/mL, and a lower limit requires a larger
plated volume [[R34]]. Independently, a 2025 pharmacokinetic-pharmacodynamic
analysis of hollow-fibre CFU series showed that censoring counts below 10 CFU —
recording them only as "below the floor", with the true value unknown — biases
regimen ranking [[R54]], and a within-host tuberculosis tolerance study chose a
shallower MDK threshold specifically so that more isolates could enter the
analysis [[R55]]. <!--supp-->

The closest statement of the bound is in the framework's own methods paper, and
we claim no priority over it. Brauner and colleagues, presenting a direct
measurement of tolerance that deliberately avoids time-kill curves, scale the
inoculum to the endpoint being measured: a hundred bacteria per well to determine
MDK99, a thousand for MDK99.9, and so on [[R3]]. That is the reachability
inequality of this paper, with the floor idealised at one cell per well and a
grew-or-did-not-grow readout in place of a count. What has not been done is to
carry the rule back into plate-count time-kill, where the floor is not one cell
but a concentration fixed by the plated volume — 10 to 400 CFU/mL across the
deposits reanalysed here — and must therefore be measured sample by sample rather
than assumed; nor to ask what the published record looks like where the rule was
not applied. <!--supp-->

The requirement is older still, and it is quantitative: NCCLS M26-A ties the
plated volume to the endpoint, and separately requires the smallest accurately
detectable count to be established by serial dilution of a known inoculum
[[R31]]. The endpoint has since moved and the rule did not travel with it. The
persistence field's own consensus guideline, which catalogues at length what else
can go wrong with a time-kill assay, raises neither the limit of detection nor
the plated volume nor how deep a reduction the assay can report [[R56]]. <!--supp-->

No prior treatment converts a floor-level reading into the classification rule
it becomes. When the last count sits at *L*, the recorded fraction is *L*/*N*₀, and
the low, medium or high label is then a cut on starting density. That is the gap
this paper fills. Two further failures have to be kept distinct from it. A
duration ceiling — the assay stopped looking — is not a count floor, which is the
plate being unable to see. And recording a below-limit flag is not the same as
scoring a duration from the points so recorded.

This is testable rather than arguable, because one published deposit assigns the
tolerance phenotype itself. Vijay and colleagues [[R5]][[R51]] scored 217 clinical
*Mycobacterium tuberculosis* isolates as having low, medium or high tolerance to
rifampicin, and deposited alongside each call the starting most probable number,
the growth rate, the isoniazid susceptibility and the killing readings the call
was built from. The classification, the inputs to it, and the assay geometry that
bounds it are all in the same file. <!--supp-->

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
fifty (Table S12).

We test the two boundaries on the classification and the assay geometry of 217
clinical isolates, then ask what the resulting phenotype tracks: drug
susceptibility, or the physiological state of the culture. Four further deposits
carry the question beyond one clinical panel — a six-laboratory consortium
exercise distributing one strain under one written protocol [[R4]][[R23]], a
concentration-by-time grid in the same organism [[R7]][[R37]], a panel of evolved
clones in which the concentration and duration axes can be checked for
independence [[R38]], and a hollow-fibre deposit [[R8]][[R36]] held out until
every boundary was fixed. All five are published and openly licensed (Table 1).
The two boundaries are then tested forward
rather than backward, in a prospective experiment built to break them, with every
prediction written down before a plate was counted. <!--supp-->

If the hypothesis holds, a tolerance call reported without its starting density
and its assay floor cannot be interpreted, and the phenotypes assigned in its
name are, in part, a record of how the assay was set up.
---

**Box 1. Four numbers that score an MDK.** *N₀* is the starting density. *L* is
the smallest positive count the method can report — one colony in a plated volume
*v* µL is *L* = 1 000/*v* per mL, and an MPN series uses the lowest table rung [[R9]][[R10]].
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

Two of the claims this arithmetic supports are not testable and should not be
read as though they were. If the last reading sits at the floor, the recorded
reduction cannot exceed *h*, because a deeper one would require a count below
*L*. And the recorded fraction is then *L*/*N*₀, a monotone decreasing function
of *N*₀, so its rank correlation with *N*₀ is
−1 whatever the numbers are, including random ones. Both follow from the
definition of a censored reading, and neither is evidence about a drug. <!--supp-->

What is testable is what happens when one sample is plated at two volumes under a
fixed class threshold. If both readings sit at their own floors the labels are
*L*₁/*N*₀ and *L*₂/*N*₀, and they differ only when those two fractions fall on
opposite sides of the cut — which is again arithmetic. The empirical quantity is
how often a real experiment lands in that window. It could be none of the time. <!--supp-->


---

## Results

### 1. The plate's floor sets how far down killing can be seen

The most probable number (MPN) readings can only take the discrete values of an
MPN table [[R9]][[R10]] — a fixed ladder of rungs, not a continuous scale. The
day-5 column does not taper towards zero. It stops. Eighteen isolates sit at
exactly 23 per mL in the 15-day panel and six in the 60-day panel, and nothing in
the file lies below that (Fig. 1A). That is a floor, not a tail, and it is
treated as one throughout.

The deposit never states its limit of quantification [[R5]], so the floor has to
be inferred, and the inference is quantified rather than asserted. A posterior
over the MPN rungs at or below the lowest observed value — a probability spread
across which rung is the real floor — places 95 per cent support on 9.2 to 23 per
mL, a span of 0.40 log10. That is narrow enough that the class labels of
Section 3 are computed rather than refused (Table 2). Where a deposit gives no
such evidence, the labels are refused instead of reported. <!--supp-->

The deposit carries a second classification, scored at day 2, and it sits on a
different floor. The day-2 column bottoms out at 230 per mL with eighteen
readings resting there, so *L* = 230 there — the same value as at day 5, a
coincidence of this deposit rather than one number written into two places,
since the two columns share no reading. The day-2 thresholds recover the same
way: cuts at 10⁻² and 10⁻¹ reproduce all 203 usable day-2 classes, one decade
shallower than at day 5, and the identifiability boundary does not move
(*N*_id = 230/10⁻² = 23 000 per mL, matching day 5) even though the
reachability boundary does, by a full decade — 121 of 203 isolates lack the
room for a four-log reduction against the day-2 floor, against 31 against the
day-5 floor. At 60 days no pair of decade cuts reproduces the day-2 classes. <!--supp-->

Each isolate therefore carries a fixed budget of killing the assay can see. At 15
days of prior culture the starting densities run from 2 300 to 61 000 000 per mL
— 3.36 to 7.79 log10 — so headroom, the distance from the starting density down
to the floor, runs from 2.00 to 6.42 log10 (Fig. 1B, Table 3). Both spans are the
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
three, so no ordered analysis can place it (Table 5); over the 203 isolates with
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

No p-value is attached to that contrast, and the reason is worth saying out loud
rather than hiding in a caveat. An isolate with less than four logs of headroom
cannot record a four-log reduction. The 0 of 33 cell is fixed by arithmetic, not
by biology, so the null of independence between ceiling status and headroom is
false before any data are seen. A test of an impossible null still returns a
number, and that number means nothing. The census is the finding: every isolate
that could not reach the endpoint is recorded as not having reached it, and 88.0
per cent of those that could are recorded the same way. The deepest endpoint is
therefore the only one at risk, and it is the one the tolerance classification is
built on. <!--supp-->

### 2. The same floor reading was given different tolerance labels

The deposited tolerance level is a cut-off on the recorded surviving fraction,
with no overlap between classes. The thresholds themselves are not deposited.
They are recovered here, and the data pin them only to the gaps between classes:
at day 5 and 15 days of prior culture, low tolerance covers fractions below 10⁻³,
medium covers 10⁻³ to 10⁻², and high exceeds 10⁻². Those cuts reproduce every
usable class in the file, 203 of 203 (Table 4). Usable means the 203 of 217
isolates whose label is one of the three ordered classes; the other 14 carry the
fourth, unordered category, the "MDR" label above, that no ordered analysis can
place (Table 5). So what follows is an argument about the fraction the assay
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
A single cut on the starting density alone reproduces all eighteen (Table 6).
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
threshold and the rule cannot choose between two classes. <!--supp-->

Three questions have to be kept apart here, and the rest of this paper keeps them
apart. Whether a culture reaches the floor at all is a question about the drug:
rifampicin has to reduce the population by that isolate's entire headroom for it
to happen, and the starting density does not by itself decide it. Which label the
rule assigns once the reading is censored is a question about arithmetic: there
the starting density determines the compatible set, and for twelve of these
eighteen that set has one member. How far the population actually fell is a
question the assay leaves open, since the true count lies anywhere below *L*. The
first is biology, the second is bookkeeping, and the third is unmeasured.
Conflating them is the error this paper is about. <!--supp-->

So for twelve of the eighteen the recorded label carries no information beyond
the fact that the reading was censored, and for six it is not determinate at all.
None of the eighteen is a measurement of the surviving fraction.

Sorting every call in the panel this way separates the labels the assay measured
from the labels the censoring rule fixed (Table 6). At 15 days of prior culture,
185 of 203 calls rest on a reading above the floor and are measured; for 12 the
reading is censored and only one class is compatible with it; for 6 the reading
is censored and more than one class is compatible. At 60 days the counts are 191,
6 and none, because the cultures are denser and few readings reach the floor. <!--supp-->

The larger effect is at the deeper endpoint, and it falls unevenly on the groups
a study would compare. The 99.99 per cent endpoint is unreachable for 22 of 84
isoniazid-resistant isolates, 26.2 per cent, against 9 of 119 susceptible ones,
7.6 per cent (Fisher exact p = 0.00056 [[R63]]); the remaining two of the 33 are
MDR and fall outside that contrast. Their median headroom differs by a full log,
4 against 5. A comparison of tolerance between those groups is therefore in part
a comparison of how well each group could be measured, which is the disposition
the previous section quantifies. <!--supp-->

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
(Table 4) and every floor reading has a numerator of exactly *L*, the class of a
floored isolate is a function of *N₀* alone, so the algebra cannot disagree with
the deposit. What could have failed, and did not, is the premise: that the three
classes separate cleanly on the recorded fraction at all, in 203 of 203 calls.

How finely the agreement resolves also has to be stated. Among the eighteen the
starting density takes only five values — 23 000 for six isolates, then 230 000
for eight, and 610 000, 2.3 × 10⁶ and 6.1 × 10⁶ for one, one and two — and **no
isolate lies strictly between *N*_id and *N*_reach**. Any cut placed anywhere in
that decade reproduces the same twelve-six split, so the split locates the
boundary only to within an order of magnitude and is not by itself a sharp test
of where it sits. <!--supp-->

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

Two numbers in this section rest on reading the floor as a plate would, and
both survive the assay's own likelihood: recomputing the twelve-six split under
the MPN's own 95 per cent interval (reaching 120 per mL rather than stopping at
23) and under a one-sided censoring bound at 95 and 99 per cent changes no
verdict (Table S13), and a posterior over class gives the same answer in
probabilistic form — the twelve isolates recorded as low keep their label with
posterior probability at least 0.999, and the six recorded as medium are
refused outright (Table S14). <!--supp-->

The empirical findings are therefore consequences of the definitions rather than
properties of this deposit, and the claim is a prediction that any dataset
reporting a starting density, a floor and a threshold classification can be
checked against.
### 12. What the plate misses is not only what lies below its floor

Everything above is about the floor. One published observation in this organism
shows that the floor is not the only reason a colony count understates the
population, and it is set out here because the two failures are easy to confuse
and must not be.

Evangelopoulos and colleagues counted the
same mouse lungs three ways — colony count, a molecular bacterial load from 16S
rRNA, and a most probable number — on their way to a different question [[R57]].
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
chemotherapy [[R64]], both resuscitation-promoting-factor-dependent and
-independent differentially culturable populations are recovered from patients
whose solid-medium cultures return nothing [[R65]], and the mechanism has been
reproduced experimentally: rifamycin action on RNA polymerase, independent of
any assay's floor, converts a starved population to over 90 per cent
differentially detectable in vitro [[R66]] — the same drug class every arm of
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
drug worked, and 240 of 310 could not have demonstrated five** (Table S11). One
of the five could not have shown four logs in a single one of its 123 series. None
of these five carries the analysis above, and none is among the five deposits
reanalysed in this paper; they are what the same screen found
in the same organism, and they say the reachability problem is not a property of
one clinical panel.

### 4. The label tracks how fast an isolate grows, and its link to resistance cannot be separated from the inoculum

We asked what the deposited tolerance label goes with. There are two candidate
predictors, and each is tested at two culture ages and at two endpoint depths,
which is eight tests in all. Eight tests on one question will throw up a false
positive on their own, so we correct them together as one family. Two survive
(Table 7).

The label has three levels in a fixed order — low, then medium, then high — and
we model it as such. Scoring the levels 0, 1 and 2 and fitting a straight line
would assert that the step from low to medium is the same size as the step from
medium to high, and nothing establishes that. Associations are therefore
reported as odds ratios from proportional-odds ordinal logistic regression, a
fit for ranked outcomes that does not assume the steps between ranks are equal.
That fit makes an assumption of its own — that a single odds ratio serves both
cut points — and we tested it rather than assuming it (Methods; Table 7). <!--supp-->

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
direct effect with the inoculum held fixed under an assumption this deposit
cannot test on its own — that starting density sits on the causal path as a
mediator here rather than beside it as a confounder. The reverse reading is
equally available a priori: if slow growth both thins the inoculum and causes
genuine tolerance, adjusting for starting density would remove real signal
rather than a confounder, not attenuate a spurious one (Discussion weighs the
two readings against each other). The mediation decomposition under the
mediator reading is Table S3. What is not in question, whichever reading is
right, is that the association weakens once starting density enters the
model: 185 of
the 203 calls still rest on a measured, uncensored numerator. Starting density
is the strongest term in the file: every ten-fold rise in the starting most
probable number halves the odds of a higher tolerance class (OR 0.480, 0.340 to
0.677, p = 2.9 × 10⁻⁵).

Why the adjustment does that is measurable. Isoniazid-resistant isolates go into
this assay at 5.36 log10 against 6.36 for susceptible isolates, ten-fold thinner
(Mann–Whitney p = 9.1 × 10⁻¹⁴) [[R18]], and 22 of the 84 resistant isolates
carrying an ordered label lack the headroom for the deepest endpoint, 26.2 per
cent, against 9 of the 119 susceptible, 7.6 per cent. Those two counts are the 31
of Section 1, which is that section's 33 less the two isolates whose label is the
unordered fourth category. They are one log short of observable killing before
the experiment begins.

A percentage attenuation is a description, not a quantity a model estimates, so
we estimated the path directly. The total effect of resistance on the tolerance
class splits into two parts: the part that runs through log10 starting density
and the part that does not. On the 203 isolates with a usable class, rather than
the 202 the association family retains, the mediated part is +0.166 classes
(bootstrap 95 per cent CI +0.067 to +0.279) and the direct part +0.091 (−0.116 to
+0.287). About 65 per cent of the association therefore travels through the
inoculum, and the direct path covers zero. Restricting to baseline isolates
leaves the mediated path intact (+0.159, +0.053 to +0.295), and collapsing the
outcome to two levels agrees (Table S3). <!--supp-->

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
read it as a mechanism. Only a design that fixes the inoculum separates the two. <!--supp-->

That last objection can be tested rather than merely conceded, because the
isolates it applies to can be named. The recorded fraction is *L*/*N₀* exactly
for the eighteen isolates whose day-5 reading sits on the floor, and for no
others: in the remaining 185 the numerator was counted and is free to move
independently of *N₀*. Refit on those 185 alone and the mediated path does not
weaken but strengthens, to +0.227 classes (+0.118 to +0.348), while the direct
path collapses to +0.008 (−0.197 to +0.208) and the proportion mediated rises
from 0.65 to 0.96. Deleting exactly the isolates the criticism is about leaves
the effect larger, so it is not an artefact of them. What it remains is an
association in observational data, and the caution above about mechanism is
unaffected. <!--supp-->

These 217 isolates are not 217 independent observations. Forty-three are
follow-up isolates taken during treatment from patients who also gave a baseline
isolate, so up to 86 rows sit in clusters of two. But the deposit carries no
patient identifier: Archive and Sample-ID are unique to each row, and none of the
48 columns repeats the way a patient key would have to. The pairing cannot be
recovered, so no standard error can be clustered on the true grouping, and we do
not pretend otherwise. What is available is the exact substitute, a baseline-only
stratum in which every isolate is from a different patient by construction
(Time_point = 0M, n = 167 at 15 days). <!--supp-->

These 217 isolates are not 217 independent patients, and the deposit carries no
patient key with which to say so in a standard error. What it does carry is the
exact substitute: a baseline-only stratum in which every isolate comes from a
different patient by construction (Time_point = 0M, n = 167 at 15 days). <!--supp-->

In that stratum the two surviving associations part company. Growth holds and
still survives correction (OR 1.116, 1.040 to 1.198, p = 0.0024). Resistance
returns OR 2.11 (1.07 to 4.16, p = 0.031) nominally, but ranks second in the
family of eight and fails its Benjamini–Hochberg critical value of 0.0125. The
resistance association therefore leans on isolates that are not
independent of one another, and it is already the association that starting
density explains away. We report it as the weaker of the two on both counts.

Why they seed lower is not established here, and the obvious explanation fails:
resistant isolates do not grow significantly more slowly in this deposit (median
time to OD 0.4 of 19 against 17, p = 0.24), and 85 of them carry *katG* S315X,
the mutation that predominates clinically precisely because it is close to
fitness-neutral — it costs the bacterium almost nothing to carry [[R21]][[R22]].
What the deposit can rule out is less than we first reported, and the correction
runs in our favour. Seven of the nine pretreatment covariates the file carries
cannot adjust this association, and they fail in two different ways. Five of them
are recorded almost only for resistant isolates, so their missingness *is* the
exposure: the two susceptibility calls are present for 82 of 84 resistant
isolates and for none of the 119 susceptible ones, the two Mykrobe calls for 76
and none, and the mutation identity for 79 and one. Adjusting for such a column
adjusts for resistance itself, which is why the two susceptibility rows agree to
three significant figures — they are missing on exactly the same rows and hand
the fit the same design matrix. That also disposes of the largest attenuation we
previously quoted, 22 per cent for the mutation identity, which was an artefact
of the same circularity. The two Mykrobe columns hold a single value wherever
they are recorded in this stratum, so no adjusted coefficient exists for them at
all and Table S4 prints none. <!--supp-->

The other two are the isoniazid and rifampicin MICs, and their missingness runs
the other way: they are recorded for all 119 susceptible isolates and for 67 of
84 resistant ones, so what is absent sits inside the exposed group rather than
across the contrast. That does not make them confounders. The isoniazid MIC
separates the two groups completely in this deposit — no resistant isolate
overlaps any susceptible one — so it is the exposure measured on a graded scale
rather than something to adjust the exposure for. The fit says so: the standard
error on the resistance coefficient inflates from 0.103 to 0.181, and the
complete case drops 17 resistant isolates and no susceptible one, leaving 186
rows against 203. It is also the second-largest movement in Table S4, and it runs
the wrong way for a confounding explanation: with the isoniazid MIC in the model
the seeding gap grows from −0.85 to −0.96, an amplification of 13 per cent rather
than an attenuation. The rifampicin MIC, which does not separate the groups,
moves it by less than half a per cent. <!--supp-->

The remaining two are missing at rates unrelated to susceptibility and can be
used: the growth proxy and months on treatment. Adjusting for either leaves the
coefficient at −0.81 or −0.82 against an unadjusted −0.85, an attenuation of at
most five per cent (Table S4). The seeding gap is therefore more robust than the
earlier sweep suggested, not less. The file records no referring site and no
processing batch, so those cannot be tested at all. The association between
resistance and a low starting inoculum is real, large and unexplained, and we
record it as such. <!--supp-->

The two surviving associations sit in the 15-day panel, which is where the
mechanism places them. By 60 days the cultures are 38-fold denser, the spread of
starting densities has more than halved, from an interquartile range of 1.00 to
0.42 log10, and the fraction of isolates short of headroom falls from 15.2 to 3.3
per cent. The confound is a property of a thin assay, and it thins out when the
assay is not thin. The two panels are columns on the same spreadsheet rows — 210
isolates appear in both — so every comparison between them is within-isolate and
is made that way. Pairing sharpens the result rather than softening it: 26
isolates lose their headroom shortfall between panels and none acquires one
(exact McNemar p = 3.0 × 10⁻⁸ against an unpaired p of 2 × 10⁻⁵) [[R19]], eleven
leave the floor and none joins it (p = 9.8 × 10⁻⁴), and every isolate whose
headroom changes gains (Wilcoxon signed-rank p = 1.3 × 10⁻³³) [[R20]]. The
interquartile range of starting density falls by 0.58 log10. <!--supp-->

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
single averaged slope, ordinal or linear, would have reported that as a null. <!--supp-->

### 5. One written protocol does not give every laboratory the same depth to look down

If the effect is a property of assay geometry rather than of clinical sampling,
it should appear where one protocol, one strain and one stock are handed out
deliberately. Van Wijk and colleagues (2023) ran exactly that exercise, sending a
single stock of H37Rv to six blinded laboratories under one written protocol
[[R23]][[R4]]. It does.

The starting densities in Table 8 need their basis stated before they are used.
Each is the mean of quantified readings at day 0 or day 1 at the 100 µL plating,
pooled over that laboratory's arms. Institute A deposits no day-zero reading at
all, and among treated flasks only C and D do, so for four of the six the figure
rests partly on readings taken after twenty-four hours of drug — by which point
the ten-times-MIC arms have already lost between 0.7 and 2.4 log10. A day-zero
comparison across all six is therefore not available, and the check that is
available runs the other way: re-running the whole analysis on a day-one exposure
for every laboratory leaves the ordering, the area under the curve and the
laboratory-level exact test unchanged. <!--supp-->

At ten times the minimum inhibitory concentration of moxifloxacin all six
laboratories return a positive kill rate, and the rates span 5.2-fold, from 0.090
to 0.464 log10 CFU/mL per day. Across all 30 laboratory-by-arm cells the Tobit
estimate — a fit that treats a below-floor reading as below the floor rather than
as a number — and the imputation estimate never differ by more than 0.006 log10
per day (Fig. 2A, Table 8). That agreement says the fit is not an artefact of the
arithmetic used to reach it. It does not say the sub-floor assumption is safe:
both estimators assume the same normal distribution below the floor, and nothing
in this deposit can check that assumption from the inside.

The duration endpoint behaves differently on the same flasks. What it records is
not clearance and not sterilisation. It is a **first observed crossing below the
assay floor**, and the distinction is not pedantic: most series that cross later
read above the floor again, including all five untreated series that cross. The
plating volume has to be stated too, because the endpoint depends on it. The
time-to-event analysis runs at the 100 µL quadruplicate plating, the most
sensitive of the four, and there 29 of 72 treated flasks ever fall below the
floor: institutes B and C record crossings in every arm, institute A in three of
its four, and institutes D, E and F in none (Fig. S1A). For half the laboratories
the first-crossing time is therefore right-censored throughout — the flask never
crossed, so all that is known is that the crossing, if it comes, comes after the
last visit. <!--supp-->

That split is a property of the plating, not of the laboratories. Counting a
crossing on **any** of the four platings gives 48 of the same 72 treated flasks,
and every laboratory records at least one — D six of its twelve, E one, F ten.
The two counts are the same fact seen at two sensitivities, and they are exactly
what this paper is about: a duration endpoint is defined against a floor, and the
floor is a choice. The analysis keeps the single most sensitive plating so that
the endpoint means the same thing everywhere, and reports here what the other
choice would have shown. <!--supp-->

The two orderings do not correspond. Rank the laboratories by starting density
and the three lowest are exactly the three that recorded crossings, the three
highest exactly the three that did not, without exception — a split with probability 1/20 under chance alone, so it is reported as an ordering and not a test (Table S8). Rank them by kill rate
and there is no such correspondence (Fig. 2B). Institute F has the highest
starting density at 6.53 log10 among the treated flasks of this arm, kills
faster than four of the other five at 0.223
log10 per day, and records no crossing. Institute E returns the slowest rate of
all at 0.090 and also records none.

Starting density separates the flasks that ever crossed from those that never did
with an area under the curve of 0.974. That figure is a description, and it is
quoted without a p-value on purpose. The comparison looks like 67 flasks, but it
is three laboratories against three, and the between-laboratory evidence in this
deposit is six clusters throughout; the Limitations set out what that permits and
what it forbids. In short: the exact laboratory-level test returns 0.10, which is
the smallest value the design can return, and once the treatment arm is held
fixed there is no within-laboratory comparison left to fall back on. <!--supp-->

The Cox fits are reported for the same reason and with the same restraint. On
laboratory alone, institutes D, E and F carry hazard ratios of 0.20, 0.21 and
0.20. Add starting density and those move to 0.34, 0.36 and 0.62, and concordance
rises from 0.896 to 0.930 (Fig. S1B). Institute C moves the other way, from 3.0
to 5.3, and it is also the fastest killer, which is how a laboratory that
genuinely kills faster ought to behave. No p-value is attached to any of these
terms, and the panel that displays them displays that movement rather than
testing it. The reason is mechanical. The tested covariate is constant within
cluster, and with six laboratories and six parameters the cluster-robust
covariance is singular by construction; fitting it anyway does not fail loudly
but returns a smaller p than the one it was meant to correct. A coefficient that
moves on adjustment says how far starting density and laboratory identity overlap
in this design. It is not evidence that one explains the other. <!--supp-->

Where an interval is quoted from that fit it is a cluster bootstrap and not the
model's own. For the starting-density coefficient the laboratory-clustered
interval is −1.11 to −0.51, half again as wide as the model's −0.91 to −0.48 and
two and a half times the flask-clustered −0.81 to −0.56; quoting the model's
interval is not conservative, it is wrong in an unpredictable direction. For the
laboratory contrasts the laboratory bootstrap is the wrong instrument, since it
keeps each laboratory's flasks together and the contrast barely moves, so the
flask-clustered interval is quoted there instead. The crossings behind each
laboratory's coefficient are also worth stating plainly: 43 of 48 series in
institute C against 1 of 48 in institute E. <!--supp-->

Killing here is not sustained, and this is stronger than a caveat about
individual flasks. Take the 64 treated series carrying at least three quantified
readings at the most sensitive plating volume. In 48 of them the final step is
not a decline, and 44 end more than one log10 above their own lowest reading,
with a median rebound of 2.17 log10 and a largest of 5.54. Seventeen of the 32
flasks that fell below the floor at the most sensitive plating — the 29 treated
flasks above and three untreated ones — were detectable again at a later visit,
14 of them in treated arms. <!--supp-->

Across all four platings, 84 of the 140 series that cross return above the floor,
60 per cent, and the return is quick: a median of four days, with 45 per cent
back within three. Those 360 series come from 90 flasks, four platings each, so
they are not 360 independent observations; counted by flask, 53 of the 90 contain
a crossing series — the 48 treated flasks above and five untreated ones — and 42
of those contain a returning one. A crossing below the assay floor in this
deposit is therefore usually a transient rather than an endpoint, which is a
further reason it summarises less than the trajectory that produced it. <!--supp-->

Killing itself is real and dose-dependent: at one times the inhibitory
concentration five of six laboratories record net growth under moxifloxacin,
between −0.047 and −0.214 log10 per day, and at ten times all six record net
decline. <!--supp-->

A crossing below this floor is not the durable event a duration endpoint takes it
for, and two consequences follow for anyone who reads a duration off such an
experiment. The first is that the state below the floor is not absorbing: a
series that drops below it does not stay there. Of 2 232 visit-to-visit
transitions, 144 go from above to below and 95 go from below to above, so a
series sitting below the floor leaves it at the next visit with probability 0.22.
The gradient runs with drug pressure — that probability is 1.00 in untreated
series, 0.37 to 0.92 at one times MIC and 0.07 to 0.18 at ten times — which says
the event is at least partly a property of the plate rather than of the drug. Of
the 360 series, only 56, or 15.6 per cent, show the shape a survival model
assumes: one crossing that holds (Table 10). Two hundred and twenty never cross
at all, 65 cross and return, and 19 oscillate more than once. <!--supp-->

The second is that the crossing time is never observed. It lies between the last
visit above the floor and the first visit below it, and the naive treatment pins
it to the later end, which biases every duration late by construction rather than
merely imprecisely. Fitted as interval-censored data — the crossing recorded as
lying somewhere inside a window rather than at a point [[R29]] — at the most
sensitive plating, the tenth percentile of the first crossing falls from 2.95 to
1.82 days and the twenty-fifth from 11.24 to 9.64; across the treated arms at all
four platings the twenty-fifth percentile falls from 5.77 to 3.67 days, a 36 per
cent shortening. The non-parametric estimate behaves differently, and the
difference is instructive. Fitted on the half-open interval the data actually
give — the crossing happened after the last visit that read above the floor, and
at or before the first that read below — the Turnbull curve agrees with the naive
Kaplan–Meier at every visit, to floating-point precision. That is not a
coincidence: the crossing intervals are the visit gaps themselves, so between
visits there is nothing left for a non-parametric estimator to identify, and the
naive pinning costs nothing at the visits. What the pinning costs is everything
between them, which is where the parametric fit puts the shortening above. A
duration read off the naive curve is therefore too long, and by about a day at
the depths that matter. <!--supp-->

What the adjustment establishes is descriptive and is worth stating as such: a
continuous measure of where the cultures began accounts for the laboratory term
at least as well as the laboratory label does, and one institute resists even
that. What can be tested, because flasks are exchangeable across laboratories
under the null, is how much of each quantity the laboratory owns. It owns 87.0
per cent of the variance in starting density (permutation p < 0.0002) and 36.8
per cent of the within-arm kill rate (p = 0.0018). It owns the duration endpoint
outright, since three laboratories produce none at all. <!--supp-->

### 6. The turbidity standard fixes what goes into the flask, not what the plate can see

The inoculum for a time-kill experiment is not a free choice. You match a
suspension to 0.5 McFarland and dilute it, and NCCLS M26-A (approved guideline,
1999; the body is now CLSI, which has archived the document) puts the target near
5 × 10⁵ CFU/mL [[R31]]. If the protocol fixes the starting density, then the
variable the preceding sections rest on does not vary.

Two things about the standard let counts settle this. First, a McFarland reading
is a turbidity — how cloudy the tube looks, matched optically [[R32]] — and
cloudiness counts live cells, dead cells, debris and a clump of cells all as one
particle [[R32]]. Converting it to CFU/mL assumes a cell size, a shape and a
dispersal that *M. tuberculosis* does not oblige, and tuberculosis protocols work
from a range of dilutions and target inocula [[R33]]. Second, the standard fixes
what goes into the flask. What matters here is what the plate counts, and between
the two sit a dilution, a transfer, and whatever clumping happens on the way.

In the six-laboratory exercise, the untreated flasks at day zero on the 100 µL
plating actually started at 3.67, 4.61, 4.65 and 6.00 log10 CFU/mL, for institutes
B, C, D and F. Institute E deposits no untreated day-zero reading at any volume;
its series begins at day one. Institute A's three readings at that plating are
flagged above the quantification limit rather than counted. Three of the four sit
below the M26-A target, by 11-, 12- and 107-fold; the fourth sits two-fold above
it. Every figure in this section is on that one basis — untreated, day zero,
100 µL. That is not the basis of Table 8, and the two are not expected to match.

Read as headroom at a fixed plating volume, the spread is Δ*h* = 2.33 log10 — a
216-fold difference in how far down the assay can look, under one written protocol
(Table 9). That figure is small, so its roster has to be stated. It is the largest
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
direction. A second deposit [[R36]][[R8]] gives the same result against its own
stated figure rather than against a standard: its Methods specify 10⁵ CFU/mL and
its file measures 7 × 10⁵ to 2.8 × 10⁶, a median of 1.215 × 10⁶ and so 12.15-fold
above nominal — computed from the unrounded median, which Table 9 displays rounded
to 6.08 log10.

Distance from the McFarland reference is descriptive and is reported as such
(Table S5). Sitting far below it is the intended state, since the inoculum is
prepared by diluting from it, and the figure is not a measure of protocol
compliance. What sets the deepest log-kill an experiment can show is the measured
starting density and the real assay floor — not the turbidity the preparation
began from.

### 7. The flask that fell faster often crossed the floor later

Take two flasks in the same treatment arm from different laboratories and compare
them. Across 191 such pairs — with 45 further pairs that the censoring could not
settle, which are excluded rather than imputed — **66 pairs — 34.6 per cent — are
inversions**: the flask in which the population fell faster crossed below the
assay floor later (Table 11). Restrict to pairs whose rates differ by more than
0.10 log10 per day, so that the faster flask is unambiguously faster, and 23.0 per
cent of 100 pairs still invert. The criterion *D_A*/*D_B* > *b_A*/*b_B* calls 84.3
per cent of all 191 pairs correctly, but that figure is carried by the easy
majority. 65.4 per cent of pairs are not inversions, and the criterion gets 97.6
per cent of those right against 59.1 per cent of the inversions themselves. So the
decomposition identifies the mechanism — a pair inverts when the distance ratio
exceeds the rate ratio — without predicting which pairs invert much better than
three times in five. The residual is what a single averaged slope through a
two-phase kill curve cannot capture, which the Methods state as a known limitation
of *b*.

The effect holds when the faster flask is required to be unambiguously faster.
Raise the minimum separation between the two fitted rates and pairs whose rates
barely differ drop out. At 0.02 log10 per day the inversion rate is 33.7 per cent.
At 0.05 it is 29.4 per cent. At 0.10 — a difference no reader would dispute — it
is 23.0 per cent of 100 pairs.

Those point estimates are firm. Their precision is not, and the difference
matters. The pairs are not independent observations: 191 pairs are built from 42
flasks in six laboratories, and an interval that treats them as independent coin
flips reports a precision the design does not have. Resampling whole flasks within
laboratory puts the 34.6 per cent between 22.3 and 48.7 per cent. Resampling whole
laboratories, which is the level at which the comparison is actually made, puts it
between 3.0 and 71.3 per cent. Under the strictest rate separation the
corresponding intervals are 9.4 to 42.9 per cent and 0 to 79.4 per cent. What the
deposit supports is therefore that inversions are common and are explained by the
decomposition. It does not support any particular rate.

The variance decomposition sets the size of the effect and it also bounds the
claim. Of the variation available to move a crossing time, the distance term
carries 35.2 per cent at ten times moxifloxacin, 32.3 per cent at ten times
isoniazid and 17.7 per cent at one times isoniazid. The rate term carries the
rest in all three. **That ordering is not established, and we do not claim it.**
The flasks it is computed over are three to a laboratory and share a starting
culture, so this is a between-laboratory statistic with six clusters wearing
flasks as a disguise. Deleting one laboratory pushes the distance share above a
half in two of the three arms — to 70.4 per cent at ten times isoniazid and 62.3
per cent at ten times moxifloxacin — and a bootstrap over whole laboratories
straddles a half in all three (Table 11). What survives is the weaker and
sufficient statement: the distance term is a large share of the variation
available to move a crossing time, and the two terms are of comparable size. <!--supp-->

The fourth treated arm, moxifloxacin at
one times the inhibitory concentration, cannot be decomposed at all: five of six
laboratories record net growth there, and only one flask in the arm returns a
positive fitted rate, so there is no spread in the rate to divide (Table 11).
The inoculum contributes a sizeable minority of the variance in crossing time —
enough to flip which of two flasks fell faster in more than a third of the
laboratory comparisons here, which is the practical stake for anyone choosing
between compounds on this evidence.


### 8. The same boundaries hold in an experiment the framework never saw

Every section so far tests the framework on the deposits it was built from, and
all of them are *Mycobacterium tuberculosis*. A search of five general
repositories, the tuberculosis consortia, the persistence literature, food
microbiology and the hollow-fibre field returned one deposit that carried all
three fields the boundaries require and could be analysed cold. That is a
statement about what that search returned, not about what exists.

That was true of the search as described. It is no longer true of the corpus the
Methods describe: of the 45 deposits whose series could be read in full, 18
permit reachability and identifiability to be computed once the floor is
established on the same
tiers this paper uses for its own — 17 published deposits and this paper's own
experiment: stated by the depositor, derived from a recorded plated
volume, or inferred from a pile-up of counts on a plate-plausible value. Across
those, the condition the boundaries imply — that no series may present as a
measurement a reduction deeper than its own floor allows — holds in 2 210 of
2 210 series. Ten of the eighteen deposits name their organism, between them six
distinct species; the other eight do not. Those deposits are described in the data release
rather than here. One of them is the held-out deposit of this section, which the
corpus fetched independently under a second identifier, so this corpus-wide
check and the cold test below are not independent of one another and are not
two confirmations. The corpus records its floor as unstated, because the deposit
states none; the analysis below derives one from the plated volume the paper's
Methods give. Both are true, of different documents. <!--supp-->

The point of this section is a deposit opened after every boundary and threshold
was fixed, and only one deposit qualifies on that ground.

That it is *E. coli* in a hollow-fibre system rather than *M. tuberculosis* in a
flask makes it a harder test and not a softer one. A rule fitted to tuberculosis
time-kill data could be expected to fit more tuberculosis time-kill data; what it
has no right to survive is a different organism, a different drug class and a
different apparatus. The boundaries are derived from definitions, so they predict
they will survive exactly that, and this is where that prediction was put at risk.

Dubey and colleagues (2026) report amoxicillin-clavulanate against *Escherichia
coli* in a hollow-fibre system [[R36]][[R8]]. Their Methods state 100 µL plated
with counts per mL, so *L* = 10 CFU/mL is derived rather than inferred, and the
file corroborates the derivation: a 100 µL plate reporting per mL can return only
multiples of ten, and all 229 genuine counts in the deposit are multiples of ten,
the smallest exactly ten. Sixty-nine further entries read as one, which no 100 µL
plate can produce; they are the deposit's placeholder for below the floor.

Across the 20 cultures with a measured day-zero density, headroom runs from 4.85
to 5.45 log10. Endpoints at 1, 2, 3 and 4 logs are reachable for every culture. A
5-log endpoint is unreachable for 5 of 20. A 6-log endpoint is unreachable for all
20 (Table 12). On data it was not built from, the framework therefore locates the
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
### 9. Read the plate late enough and the concentration response reverses

The deposit tests apramycin at 1, 4, 8, 32 and 128 µg/mL [[R37]][[R7]]. The 1 µg/mL
flasks grow rather than die, so that arm is left out of the dose comparison. What
remains is 4 to 128 µg/mL: 32-fold, five doublings. Across that range the
survivor counts spread out 6.9-fold at day 3, 48.2-fold at day 7 and 5.2-fold at
day 14 (Fig. S3, Table 13). The spread opens, then closes again. An experiment
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

### 10. How much drug it takes and how long it takes are two different things

The framework that defines these two measures takes it as given that they are
separate (Brauner et al. 2016) [[R2]]. The deposits do not prove it. They bound
how far from separate the two could be, which is weaker and more honest. The
217-isolate file supports 24 comparisons of the two: how much drug it takes to
stop growth against how long it takes to kill. All 24 are corrected together.
Testing that many things at once throws up hits by chance, so the Benjamini–Hochberg
thresholds in Table 14 — the standard correction for a family of tests — are set
against 24, not against the size of any one subgroup. Four are significant before
correction, where 1.2 are expected by chance, and none survives it (Fig. S2,
Table 14). All four point the wrong way: a higher inhibitory concentration goes
with a *shorter* killing time, which is not the direction a shared mechanism
predicts. And they cluster at the deepest endpoint — the one Section 1 shows is
compromised. Across all 24 tests the weakest correlation this design could have
detected runs 0.14 to 0.25 depending on the subgroup; the six strongest, which
Table 14 lists, span 0.14 to 0.18.

This null is narrower than it looks, and we report it as such. Take only the
baseline isolates, where every isolate comes from a different patient, and the
deepest 15-day endpoint gives a correlation of ρ = −0.21 with p = 0.0086. Against
the family of 24, the value it has to beat is 0.0021, and it is nowhere near. Had
those six baseline tests been declared a family of their own in advance, the
threshold would have been 0.0083, and it would still have missed — by three and a
half per cent. The family of 24 is the one this paper corrects against, so the
first reading is the honest one. The second is on the record only because it
points the same negative way. The axes are not shown to be independent here. They
are shown not to be positively coupled, and that is what the deposits can
support.

Ask the same question of 126 evolved clones sharing one ancestor [[R38]][[R6]] and
the answer is ρ = +0.043 (p = 0.63), against the 0.175 this sample size could
have detected. Independence holds inside every nutrient group separately.
Splitting by nutrient is not optional there. The concentration written on the
flask is not the same exposure in every group: at 25 µg/mL, that one figure is
anywhere from 0.55 to 9.47 times the inhibitory concentration that population had
evolved to, and it falls on both sides of it (Table S6).

---

### 11. One culture, two plated volumes, two tolerance labels

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
three cultures plated at 100 µL ran from 4.88 to 5.05 (Fig. S5B, Table S9). Every flask is
paired with itself across the two platings, so the comparison is within a culture
rather than between cultures.

The gain the pipette buys is exactly one log, because the floor at the pooled
100 µL plating is one tenth of the floor at the pooled 10 µL plating. The nine
paired gains are not exactly one log: they run 0.87 to 1.19 (Table S9). The
difference is not the drug and not the flask. It is that each plating measures
its own starting density from the same culture, and the two measurements
disagree — 425,000 against 565,000 per mL in one flask, 255,000 against 375,000
in another. That disagreement is this paper's own argument turned on its own
experiment: *N*₀ is not a constant a protocol supplies, it is a measurement with
error, and the headroom computed from it inherits that error. Reported per
flask, the gain never falls below 0.87 log10, so the four-log endpoint moves
from unreportable to reportable in every one of the three cultures at the
standard inoculum. <!--supp-->

That much is arithmetic, as Box 1 says. So is the next step. When both platings
of one sample rest on their own floors, the two fractions written down are
*L*₁/*N*₀ and *L*₂/*N*₀ — two different floors over one starting density — so
they can fall either side of a class threshold and give one culture two labels.
**The quantity that could have come out zero is how often a real experiment lands
in the window where those two fractions straddle the cut**, and it depends on
where the cut is (Fig. S5C, Table S10). Put the cut at one per cent and the window is
nearly shut. Put it at one in a thousand, which is where the clinical
classification analysed above cuts its lowest class, and six of 54 sample-times
receive two different labels from one culture — one in nine. That cut is imported
from the tuberculosis classification; nothing in the E. coli experiment derives
it, and it serves here as a ruler for the window's width, not as a claim about
E. coli biology.

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
with error. <!--supp-->

---
## Discussion

Every clinical microbiologist knows that a negative culture taken under
antibiotic exposure is not proof of sterility. This paper reports that the
number brought in to replace that judgement carries the same defect — and once
it is a number, it is harder to see.

The minimum duration for killing was built to divide the starting density out,
and in the definition it does. It stops the moment killing reaches the plate's
floor, for a reason that is arithmetic rather than statistical: from there the
fraction written down is *L*/*N₀*, and the drug has dropped out of it. <!--supp-->

Fifteen per cent of the clinical isolates examined here could not have shown the
deepest endpoint whatever the drug did to them, and every one of them is recorded
as having failed to show it. Eighteen more ended on the floor, and one threshold
on their starting density reproduces every label they were given. Whether those
cultures reached the floor is a question about rifampicin. Which label they
received once they were there is a question about arithmetic, and the starting
density and no further. In the 15-day panel, 12 of 203 usable calls have a single compatible
class and 6 have more than one; the other 185 rest on a fraction that was
actually measured. The kill rate still carries more of the variance in crossing
time than the distance does, in every multi-laboratory arm. What fails is the
*interpretability* of a deep log-reduction call reported without *N₀* and *L*,
not every tolerance call ever made. What the inoculum settles is
the subset of labels for which killing had already reached the floor. <!--supp-->

The failure is specific and it is bounded. In this deposit neither the 90 nor
the 99 per cent endpoint is compromised: every isolate has the room to show
both. It is the 99.99 per cent endpoint that a substantial minority cannot
reach, and that is the deep endpoint the clinical classification uses. Being
that specific is what makes the problem fixable rather than fatal. <!--supp-->

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
show six. <!--supp-->

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
Box 1 belongs before an experiment rather than after it. <!--supp-->

That is also where the counts feeding regimen selection are taken. A model
published as a preprint while this paper was in preparation predicts relapse in
the murine model across nine datasets, 58 regimens and 2 239 relapse
observations, reaching an area under the receiver operating characteristic curve
of 0.90 on its final external validation [[R58]]. Its eight predictors include
the fall in lung CFU from baseline at days 14 and 28, the fall in the ribosomal RNA (ribonucleic acid)
synthesis ratio at day 14, the presence of an oxazolidinone, and four
experimental covariates. Removing either biomarker costs performance. What the
authors show is that the loss from dropping the RS ratio can be recovered by
adding model-estimated coefficients for the sterilising contribution of each drug
— a substitution they license only for compounds already characterised, since
those coefficients need prior long-term outcome data, and expressly not for the
novel ones the model exists to rank. <!--supp-->

Their explanation for that gap is physiological, and it is why they built the RS
ratio in the first place: a change in CFU cannot always separate a sterilising
regimen from a non-sterilising one. A detection floor produces the same signature
from outside. Where the best regimens drive the count into the region the plate
cannot resolve, a term standing for drug identity absorbs discrimination the
count is no longer free to express, and the fitted model looks as this one does.
Nothing in the published record separates the two readings, because version 1 of
that preprint states no detection limit and no plated fraction — and we do not
read that as a lapse peculiar to it, since the field's own consensus guideline
raises neither. That is the point. An explanation the reporting cannot adjudicate
is one the reporting should not have left open, and it is precisely why
*N*_reach and *N*_id are worth writing down. A relapse model that leans on a
28-day count needs that count treated as left-censored — read as below the floor
rather than as a number — and *h* says when the question arises instead of
leaving it to be noticed. <!--supp-->

A reader may object that this runs backwards. Dropping below the limit of
detection is what a *susceptible* population does; how can it make an isolate
look more tolerant? The objection is a fair one, and it is answered by
separating two endpoints that the literature reports side by side. <!--supp-->

A duration endpoint asks when a fixed depth was reached. An isolate without the
room that depth requires cannot reach it under any drug effect whatever, so what
the file records is not a short duration but no duration at all: the isolate is
censored at the end of observation, which is the top of the scale and therefore
the most tolerant value it can take. The isolates that could not demonstrate the
endpoint are, without exception, the ones recorded as having failed to reach
it. <!--supp-->

A class endpoint asks how far the population fell by a fixed time, and there the
arithmetic does not merely preserve the direction — it inverts it. Once the
final reading sits on the floor the recorded fraction is *L*/*N₀*, and with *L*
fixed a *lower* starting density yields a *larger* recorded fraction. A larger
surviving fraction is a higher tolerance class, not a lower one. That is why the
eighteen isolates ending on the same floor value split twelve low and six medium
in the order their inocula do: the recorded survival and the starting density are
the same quantity. <!--supp-->

Neither route asks anyone to mistake a sterile culture for a surviving one. In
the first the assay returns no endpoint. In the second it returns the floor
divided by the inoculum. What is read as biology is, in both cases, a property
of the measurement. <!--supp-->

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
what sets the floor. <!--supp-->

The standard is not silent on that choice, and this is the paper's sharpest
finding rather than an awkwardness for it. M26-A's own section 1.3.2.5, headed
*Volume Transferred*, ties the volume to the endpoint with a counting rule:
after the defined 99.9 per cent killing, at least ten colonies must remain
[[R31]] — for a standard inoculum of 5 × 10⁵ per mL that means at least 20 µL
streaked, so a 10 µL streak fails the rule, and section 3.1 separately requires
the smallest detectable count to be established by serial dilution. A guideline
written in 1999 already required both numbers this paper asks for. The
deposits reanalysed here do not meet it, not for lack of care but because the
endpoint moved: M26-A nowhere contemplates a four-log call, and the volume
rule did not travel with the deeper endpoints.

Take the assay's contribution out and what is left makes biological sense.
Growth state predicts the tolerance class before and after adjustment for
starting density — isoniazid needs KatG and active cell-wall synthesis
[[R39]], rifampicin needs transcription [[R40]], and a population that is not
dividing offers less of what these drugs act on. The classification is reading
physiological state, not drug susceptibility.

That axis is the one tuberculosis drug development already leans on. Killing
assays of this design rank regimens before they enter trials, and tolerance
followed in patients is now being read as within-host evolution [[R55]]. If a
tolerance classification is partly an inoculum measurement, conclusions drawn
from it — that one regimen sterilises faster than another, that a patient's
isolates are becoming more tolerant over therapy — are in part conclusions
about how the assay was set up. The correction applied here does not remove
the biology; it aims it at the right target. The phenotype that survives the
correction is growth state, which is real, targetable and directly measurable,
unlike a fraction read off a floor.

The isoniazid-resistance association behaves differently, and instructively. It
is the weaker of the two on two separate counts. Unadjusted, resistant isolates
carry 2.32 times the odds of a higher tolerance class. Adjusted for starting
density the odds ratio is 1.31 and the interval spans one. It also does not
clear its corrected threshold once the analysis is restricted to the baseline
isolates, which are one per patient by construction — the only correction for
repeated isolates this deposit permits, since it carries no patient identifier.
The growth association survives both. <!--supp-->

Where the isoniazid-resistance association weakens, the weakening is visible
in the same file: resistant isolates
enter the assay ten-fold lower and 26.2 per cent of them lack the room the
endpoint requires. We do not know why they seed lower. The natural explanation —
that resistance carries a fitness cost — is not supported here, since these
isolates do not grow measurably more slowly and most carry the near-neutral
*katG* S315X allele [[R21]][[R22]]. That gap is a finding in its own right and
belongs in the next study rather than in a speculative sentence in this one. Nor
is it explained away by anything else the file records: of its nine pretreatment
covariates only two can legitimately be adjusted for, and neither moves the
association by more than five per cent (Section 4). The two larger movements in
that table both come from columns that record the exposure rather than a
confounder: the mutation identity, which is missing for all but one susceptible
isolate, and the isoniazid MIC, which separates the two groups completely and
enlarges the seeding gap by 13 per cent instead of shrinking it. <!--supp-->

Where the inoculum is set deliberately rather than by clinical accident, the
same arithmetic operates and can be measured rather than inferred. In more than
a third of cross-laboratory comparisons the flask in which the population fell
faster was the one that crossed below the assay floor later, and the
distance-over-rate criterion accounts for three in five of them. Resampling
whole laboratories rather than pairs leaves that rate poorly determined — 3.0 to
72.4 per cent — so what the deposit establishes is the mechanism and not the
rate. <!--supp-->

The variance decomposition (Section 7) sets the size of that effect and no
more: the inoculum is a large minority of the variance in crossing time,
enough to flip the ranking in more than a third of comparisons but not enough
to license treating the endpoint as an inoculum readout. <!--supp-->

We agree with van Wijk and colleagues wherever the two analyses overlap. They
noticed the spread in starting densities themselves. They report that the burden
at the start varied between laboratories while the net effect of the drug varied
less [[R23]]; that conclusion is theirs, and it anticipates part of ours. Where
we part company is in what they did with readings that fell outside the
quantification limits: they left them out of the numbers. That is a defensible
way to report an assay. It also closes off the question this paper asks, because
those are exactly the readings a duration is built from. <!--supp-->

Vijay and colleagues report that tolerance goes with resistance status and with
treatment history in the same isolates [[R51]]. We do not dispute a single
measurement. Their deposit is unusually complete, and this analysis was only
possible because they posted the classification, the readings behind it and the
assay geometry together. What we add is this. Their deepest endpoint asks for the
largest fall, so it is the one shortest of room to fall in, and how much room
there is differs systematically between the very groups being compared. The link
to resistance then survives neither putting starting density into the model nor
cutting the data down to one isolate per patient. The link to growth survives
both. The finding is that one of its two associations is carried by the geometry
of the assay and by isolates that are not independent of each other, not that
their classification is empty. <!--supp-->

The prospective experiment has a limitation of its own, and it is the one a
reader of this paper should raise first. Its samples were diluted in saline and
plated; they were not washed, filtered or treated to inactivate the drug, and no
carryover control was run. Antibiotic carried onto the plate suppresses colony
formation without killing anything, which is the same class of counting artefact
this paper is about, and at the shallow dilutions a culture near its floor is
read on, dilution is the only thing containing it. The design is conservative in
this respect rather than clean: the larger plated volume carries ten times more
drug to the plate, so carryover would shrink the very difference between the two
platings that Section 11 reports. It would not manufacture it. But the
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

The evidence between laboratories rests on six laboratories, not on hundreds of
flasks. Every flask in a laboratory was seeded from the same starting culture, so
for this purpose those flasks are copies of one another. The effective sample
size for any comparison *between* laboratories is six, not the 67 to 85 flasks
the tables list. Six is too few for the standard correction — a cluster-robust
standard error — and the correction does not fail loudly when you fit it anyway.
On these data it returns a *smaller* p for every institute term than the
model-based p it was meant to correct. So where a comparison is between
laboratories we quote the exact laboratory-level test or a bootstrap that
resamples whole laboratories, and where the design cannot produce a meaningful p
at all, we give no p. Three laboratories recorded crossings at the 100 µL plating
and three did not; with the six split three and three, the smallest two-sided p
the arithmetic can return is 0.10, whatever the biology. Some quantities do let
flasks be pooled across laboratories — the variance shares, and the inversion
rate under a flask bootstrap. Those keep an exact permutation test, and they are
the strongest between-laboratory evidence the deposit holds. <!--supp-->

The laboratories did not all count their starting density on the same day. Only
institutes C and D deposit a day-zero reading for the treated flasks. A, B, E and
F deposit day one, and by day one the ten-times-MIC arms have already lost
between 0.7 and 2.4 log10. For four of the six laboratories, then, the number we
are calling the exposure has some killing baked into it. We re-ran the whole
comparison on a day-one exposure for every laboratory. The ordering, the area
under the curve and the laboratory-level p all stayed the same, so the conclusion
is robust to it. The mismatch is real all the same, and we report it rather than
smooth it over. <!--supp-->

In the six-laboratory exercise, starting density and laboratory are close to the
same variable. 87.0 per cent of the variance in flask-level starting density lies
between laboratories rather than within them. Taken over every flask that
deposits an early density, treated and untreated arms together, the laboratory
means span 3.62
log10, against a median within-laboratory standard deviation of 0.43. Adding
starting density to a model that already knows which laboratory a flask came from
is therefore not separating two covariates. It is closer to swapping a label for
a number carrying much the same information. Telling the two apart needs a design
that fixes the inoculum across laboratories. <!--supp-->

The 15-day and 60-day panels of the clinical deposit contain the same isolates.
The comparison between panels is therefore not independent, and it bounds the
evidence for a difference rather than establishing it.

Starting density could sit on the causal path rather than beside it. Suppose
resistance slows growth, and slow growth causes genuine tolerance. Then the thin
inoculum is a consequence of the slow growth, and adjusting for it would remove
real signal rather than a confounder. The asymmetry favours the confounding
reading, since growth survives adjustment and resistance does not, but a design
that fixes the inoculum would settle it. <!--supp-->

This is not an aspiration. One study already does it. A murine preventive-therapy
experiment writes its lower limit of detection into the deposited workbook once
on every sheet, separately for each agar type, and separately for individual mice
where the lower limit differed between them: 0.78 log10 CFU per lung on plain and
hygromycin agar, 0.54 on thiophenecarboxylic acid hydrazide agar, with the plated
volume stated beside it [[R59]]. That is better practice than anything else in
this corpus. The article reporting the experiment states none of it — a full-text
search returns no occurrence of "limit of detection" or of either value. So the
number is not missing from the science. It is missing from the paper, and a
reader who never opens the supplementary spreadsheet cannot know an endpoint was
bounded. What we are asking for is one sentence in a methods section, and
somebody has already done all the work that sits behind it. <!--supp-->

The mirror image is a deposit whose modelling table carries a column named
`CFU_LOD`, and that column is empty in all 272 rows [[R60]]. Somebody designed
the field, declared it numeric, and never filled it in; nor does a detection
limit appear in any of the eight analysis scripts deposited beside it. Put the
two cases together and the diagnosis is not carelessness. The assay floor *L* is
measured. Sometimes it is written down to a standard higher than anyone asks for.
It then falls out of the record between the bench and the reader — off the end of
a spreadsheet, or into a column nobody completed. <!--supp-->

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

**Model an ordered label as ordered.** A tolerance class is low, medium or high.
Scoring that 0, 1, 2 and fitting a line asserts that the step from low to medium
is the same size as the step from medium to high, and no one has established
that. Proportional-odds regression — a fit built for ranked categories — costs
nothing to run and reports in odds ratios. Where the proportionality it assumes
fails, as it does here at 60 days, it says so rather than averaging two different
effects into one null. <!--supp-->

**Treat an endpoint at the floor as a bound, not a value.** Analysed as a
measurement it manufactures differences between isolates whose final viable
burdens the assay could not tell apart, and the same censored reading stands
for a different demonstrated kill at every starting density.

None of this requires new apparatus or a statistician, and to make that concrete
the four checks are released as a small command-line tool alongside the analysis
code. Give it a starting density and either an assay floor or a plated volume. It
returns the headroom, states which of the 90, 99, 99.9 and 99.99 per cent
endpoints that headroom can support, and reports the recorded fraction a
floor-level reading would produce, labelled as the bound it is. Where a culture
volume is known it also returns the viable burden a blank reading is consistent
with; where it is not, it declines to compute one rather than assuming a volume.
The tool exits with a failure code when a requested endpoint is unreachable, so
it can be run before an experiment rather than after it. <!--supp-->

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

A time-kill guide already exists and this five-field minimum does not replace
it: the ASTM International (American Society for Testing and Materials)
guide E2315 sets out how to run and report a time-kill procedure in
general — organism, media, neutralisation, raw counts — for antimicrobial
products broadly, and none of its reporting requirements is *L*, headroom or a
censoring convention specific to a duration endpoint cut on a fraction of the
starting count [[R69]]. The five fields above are additional to that guide,
not a substitute for it, and apply wherever a killing curve is read against an
assay floor to score how long killing took rather than only whether it
happened.

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
(Table S14), a five-field minimum that makes any killing endpoint recomputable
(Box 2), and a small tool that returns the endpoint a planned assay can
support. None of it asks a laboratory for a new measurement; the cost is five
numbers written down. The return is a tolerance phenotype that means the same
in one laboratory as in the next, and that can bear the weight regimen
research already puts on it.

---
## Materials and Methods

### The corpus screened, and how five deposits came out of it

We assembled 78 candidate time-kill datasets from the published literature
(21 August – 8 September 2026) and screened 45 of them field by field for
the three quantities the two boundaries below require: a pre-treatment
starting density, a longitudinal series of viable counts, and either a
plated volume or a stated assay floor. Every inclusion and exclusion is
recorded in a manifest deposited with the analysis code.

Forty-one distinct records were inspected, one of them this paper's own
prospective experiment. Of the 40 remaining literature deposits, 32
reported no assay floor by any route — no limit of detection, no limit of
quantification, and no plated volume from which one could be derived.
Eighteen deposits carried enough information to compute both boundaries at
all, and five carried the complete set of fields the full analysis
requires (Table 1, Figure S4).

These 78 candidates are a documented sample of the literature, assembled
without a registered search protocol; the two boundaries are derived from
definitions rather than estimated from the corpus's size, so a single
deposit with a stated floor is enough to demonstrate them.

### The five deposits analysed

Five published deposits are analysed (Table 1), four carrying the analysis
and the fifth held out to test it: opened only after every boundary and
threshold was fixed, and used nowhere else in the paper except to confirm
them (Section 8).

**Clinical isolates with a deposited tolerance classification.** 217
*M. tuberculosis* isolates assayed under rifampicin, each carrying a
minimum inhibitory concentration, minimum durations for 90, 99 and 99.99
per cent killing at 15 and 60 days of prior culture, most probable number
readings at days 0, 2 and 5, a growth-rate proxy, isoniazid susceptibility
with the resistance mutation where present, and the authors' own tolerance
level for each isolate (Vijay et al. 2024; eLife 93243 supplementary file
2) [[R5]]. Of the 217 rows, 43 are follow-up isolates from patients
already represented, so a baseline-only stratum is analysed separately.

**The six-laboratory exercise.** *M. tuberculosis* H37Rv from one stock,
distributed with one written protocol to six blinded laboratories (van
Wijk et al. 2023; figshare 19766083, CC BY 4.0) [[R23]][[R4]]. Moxifloxacin
and isoniazid at one and ten times the minimum inhibitory concentration,
three flasks per arm, each sample plated at four volumes — 100 µL
quadruplicate, 10 µL as four drops, 10 µL as a single drop, and 2.5 µL as
a single drop — giving three distinct floors spanning 1.60 log10 within a
single flask-visit [[R34]]. The file holds 2,775 readings; the analysis
set, after dropping unusable values and pre-treatment visits, is 2,580.

**Evolved clones.** 126 *Escherichia coli* clones from a parallel
evolution experiment under amikacin, each carrying an endpoint minimum
inhibitory concentration and a persister fraction (Windels et al. 2024;
Zenodo 10.5281/zenodo.7550302, CC BY 4.0) [[R38]][[R6]]. Six of its 595
surviving fractions are written as exact zeros with no named floor, so
this deposit is one of two for which observability labels are refused.

**Validation deposit, analysed only after both boundaries were fixed.**
Amoxicillin-clavulanate against *Escherichia coli* in a hollow-fibre
infection model, with 100 µL plated, measured day-zero densities for
every culture, and below-limit readings retained as a placeholder (Dubey
et al. 2026; article Source Data, CC BY 4.0) [[R36]][[R8]]. It was the
only deposit found carrying all three fields the boundaries require, and
no boundary, threshold or modelling choice in this paper was informed by
it.

**Concentration-by-time grid.** Apramycin against *M. tuberculosis* at
128, 32, 8, 4 and 1 µg/mL, triplicate log10 CFU at days 0, 3, 7 and 14
(Kaur et al. 2024; figshare 26462791, CC BY 4.0) [[R37]][[R7]]. The 1
µg/mL arm shows net growth rather than killing and is excluded from the
dose comparison, leaving 4 to 128 µg/mL as the range compared (Section 9).

### The prospective experiment

An *in vitro* experiment was designed to prospectively test both
boundaries. Its design sheet, predictions and plate counts are one
workbook, deposited with the analysis code, with every prediction written
down before a plate
was counted.

*Escherichia coli* ATCC 25922, the CLSI quality-control reference strain,
was grown in cation-adjusted Mueller–Hinton broth and plated on
Mueller–Hinton agar, incubated at 35 ± 2 °C in ambient air [[R31]][[R61]].
The ciprofloxacin MIC, determined by CLSI reference broth microdilution
[[R61]][[R62]], was 0.008 mg/L, within the CLSI quality-control range for
this strain [[R62]]; the exposure was set at ten times it, 0.08 mg/L,
chosen to kill deeply and fast enough that every arm reaches the floor
within the sampling window.

Three seeding arms were set so the four-log endpoint is unreachable in
one, marginal in the second and comfortable in the third: targets of
5 × 10⁴, 5 × 10⁵ and 5 × 10⁶ CFU/mL (the middle arm the CLSI-specified
inoculum), reaching 6.4 × 10⁴, 4.4 × 10⁵ and 3.8 × 10⁶ CFU/mL as measured
from day-zero counts. Three flasks per arm were sampled at 0, 1, 2, 4, 6
and 24 h; at each time, one dilution series was plated at both 100 µL and
10 µL in duplicate, giving 216 plate readings in all. Viable density was
*N* = *C*·*D*·1000/*V* for *C* colonies counted at dilution factor *D* and
plated volume *V* µL.

No carryover control was run. Because the 100 µL plating carries ten times
as much drug onto the plate as the 10 µL plating of the same sample, any
carryover effect works against the depth advantage the 100 µL plating is
reported to have, so the paired comparison in Section 11 is conservative
with respect to it.

*L* is one colony in the volume plated, referred back to the undiluted
sample. The two technical plates of a sample are pooled rather than
averaged, so their volumes add and the floor is lower than a single
plate's: 5 CFU/mL for a pooled 100 µL pair against 10 CFU/mL for one
plate, and the two platings differ by exactly one log by construction.
Headroom, censoring at the floor and the three tolerance classes are
applied unchanged from the definitions below; class labels use the
thresholds of the clinical deposit above, *c*₁ = 10⁻³ and *c*₂ = 10⁻², so
the two experiments are scored on one rule.

### Two kinds of limit, kept apart (operational assay floor vs. reported limit of quantification)

No deposit analysed here reports a validated limit of quantification with
a value. Throughout this paper *L* is therefore an **operational assay
floor**: where a plated volume is recorded it is the **minimum reportable
positive count**, one colony in that volume; where none is recorded it is
inferred from the deposit and labelled as such. The term limit of
quantification is used only in reporting what a source states.

In running text *L* is the **assay floor**, and that is the only short
form used, so that "boundary" is left free for the two derived boundaries
of the next subsection and never denotes a value. The event a
time-to-event analysis records is correspondingly a first observed
crossing below the assay floor. What *L* is in each deposit is tabulated
deposit by deposit (Table 15).

Two censoring problems are handled separately. A **count below the assay
floor** is left-censored: the population is somewhere below a known
value. In the clinical deposit the floor is inferred at 23 MPN/mL from
three signatures — it is the smallest value in the file, nothing lies
below it in 1,932 readings, and the minimum shifts by exactly a factor of
ten per culture age. The number of isolates lacking four logs of headroom
is 33 at this floor and does not fall below 28 at 3.0 MPN/mL, the lowest
value the deposit's own MPN table admits, so the conclusion holds across
the range (Table S7).

A volume-derived plate floor bounds the true count from above, [0, *L*];
an MPN rung does not, since its 95 per cent profile interval extends well
above the rung (3 to 120 per mL under the deposit's own design). Every
identifiability verdict was recomputed under this likelihood instead of
the plate-sweep bound (Table S13): 12 of 18 floored isolates admit one
class and six admit two at 15 days, identically under both treatments,
because the floored isolates' starting densities sit far from the shifted
threshold even at the widest 99 per cent bound.

The six-laboratory deposit plates each sample at four volumes at the same
visit, so a below-limit flag can be checked against the other platings of
the same flask: 16.7 per cent of its 498 flags are contradicted by a more
sensitive plating of the same sample recording a quantified count. Each
reading is therefore judged against its own volume's floor rather than
pooled to the least sensitive one, which would additionally discard 5.9
per cent of genuine quantified counts.

A **crossing time not observed within the study** is right-censored: a
flask that never falls below the floor contributes the information that
its crossing time exceeds its last visit, and enters the survival
likelihood as such rather than as missing.

### Posterior probability of assay floors, and what remains unresolved

A volume-derived floor is a point mass, with nothing to infer. A floor
inferred from a pile-up on a most-probable-number rung carries a discrete
posterior over the rungs at or below the observed minimum; the interval
quoted is the 95 per cent highest-posterior-density support. Where no
floor is evidenced, or the support spans more than one log10, observability
labels are **refused** rather than reported (Table 2): the clinical
deposit passes this rule at 0.40 log10 of support, and two of the five
deposits fail it. This paper fits nothing to predict an MDK — once *L* is
in hand the rest is derived.

The same likelihood turns classification into an inference with its own
refusal rule: given a floor reading, the posterior over the true count
maps through starting density to a posterior over class, and an isolate is
refused when no class reaches 95 per cent (Table S14). At 15 days the
twelve isolates recorded as Low are confirmed (P(Low) ≥ 0.999); the six
recorded as Medium are refused, their posterior split almost evenly across
the threshold the deposit drew at *L*/*N*₀ = 10⁻³. The refusal holds
across both well designs, both floor readings and two priors.

### Causal mediation of the resistance association

A linear product-of-coefficients mediation decomposes the total effect of
isoniazid resistance on the day-5 tolerance class into an average causal
mediation effect through log10 *N₀* and an average direct effect
[[R16]][[R17]], with bootstrap percentile intervals from 5,000 resamples.
A refit excludes the 18 of 203 isolates whose day-5 reading sits at or
below the floor, since their recorded fraction carries no measured
numerator. Sequential ignorability is assumed and untestable here; the
sensitivity that matters is the residual correlation between mediator and
outcome errors at which the point estimate crosses zero, about −0.23. No
claim is made that unmeasured confounding is absent.

### What each analysis was fitted to

A dozen denominators appear in this paper and each is derived in a single
place (Table 5): the MDR tolerance label is dropped wherever an ordered
outcome is fitted (14 rows per panel, 20 at 60 days), the growth proxy is
missing for one isolate, and five of 72 treated flasks in the
six-laboratory deposit carry no usable starting density. Dropped rows are
compared with retained ones on starting density and susceptibility to
test whether the exclusions are plausibly ignorable (Table S1); the only
difference not attributable to the exclusion rule itself is that the
60-day panel's 20 dropped rows sit higher in starting density.

### Dynamic range, and the two boundaries it sets

For a culture starting at *N₀* against an assay floor *L*, the
**headroom** is *h* = log10(*N₀*/*L*), the deepest reduction the assay can
resolve. Two boundaries follow from the definitions alone.

**Reachability.** A *q*-log endpoint is observable only if

  *N₀* ≥ *N*_reach = *L* · 10^*q*.

**Identifiability.** A censored reading places the true count in [0, *L*],
so the recorded surviving fraction is at most *L*/*N₀* — an upper bound,
not a measurement. Given class thresholds 0 < *c*₁ < *c*₂ …, the class is
determined by the data only if

  *N₀* > *N*_id = *L*/*c*₁,

since the censored interval always contains zero and so is only
compatible with the lowest class above this point. Both boundaries are
properties of the method alone; seeding a culture above
*L* · max(10^*q*, 1/*c*₁) makes both failure modes impossible before an
experiment runs.

### Estimation

A **Tobit model** fits log10 CFU/mL linearly in time by maximum
likelihood [[R47]]; a censored reading contributes log Φ((limit −
µ)/σ), the probability it fell below its own limit — Beal's M3 written
for this assay [[R46]]. **Multiple imputation** draws each censored
reading from the fitted normal truncated at its own limit, refits by
ordinary least squares, and pools 50 fits by Rubin's rules [[R48]]; the
two estimators' agreement shows the answer does not depend on which
arithmetic recovers it, not that the sub-floor distribution is normal.

The growth proxy is the deposit's time to an optical density of 0.4, in
days, so it runs inversely to growth rate. **The tolerance label** is
modelled as an ordered categorical outcome by proportional-odds ordinal
logistic regression [[R12]], with starting density as a prespecified
covariate; proportional odds is tested by a Brant test per predictor
[[R13]] and a likelihood-ratio test against a generalised ordered logit
[[R15]], with the partial-proportional-odds fit reported where it fails
and checked against a multinomial fit assuming no ordering (Table S2).

**Time-to-event analysis** treats the first observed crossing below the
assay floor as the event, right-censoring series that never fall below
it; 60 per cent of series that cross read above the floor again at a
later visit, so the event is a crossing, not a clearance. The crossing
time is interval-censored between the last visit above the floor and the
first below it; interval-censored fits [[R29]] are reported alongside
Kaplan–Meier [[R24]] and Cox proportional hazards [[R25]] as descriptive
summaries, with cluster bootstraps over laboratories and flasks [[R27]]
in place of the partial likelihood's independence assumption, and
proportionality tested on Schoenfeld residuals [[R49]][[R50]].

**The replicate-level bootstrap** [[R26]] behind interval slopes resamples
the three replicate counts with replacement, takes their mean, refits the
concentration slope on each draw, and takes percentile intervals from
20,000 draws — reported instead of the least-squares fit through the
deposited concentration means, which has two residual degrees of freedom
and discards the replicate scatter. An interval on a proportion is the
Jeffreys interval [[R30]], which does not collapse to zero width at the
sample sizes here.

Four procedures are implemented in the released analysis code rather than
taken from a package — the Brant test, the partial-proportional-odds fit,
the product-of-coefficients mediation, and the residual-correlation
sensitivity — in `exp30_ordinal_tolerance.py` and `exp34_mediation.py`;
the partial-proportional-odds likelihood is validated against the
proportional-odds fit it nests, agreeing to 1.0 × 10⁻¹⁰ in log-likelihood.

### The decomposition of a crossing time

Over an interval where the decline is close to log-linear, log10
*N*(*t*) = *a* − *bt*, and with *ℓ* the log10 assay floor and *D* = *a* −
*ℓ* the distance the population starts above it, the crossing time is
*T* = *D*/*b*. For two flasks,

    log(T_A / T_B) = log(D_A / D_B) − log(b_A / b_B),

which splits a difference in crossing time into a distance term and a
rate term. An **inversion** is a pair in which A fell faster yet crossed
later, occurring exactly when *D_A*/*D_B* > *b_A*/*b_B*.

### Multiplicity

Where a question admits more than one test, every test the deposit
supports is run, and the family is corrected by the Benjamini–Hochberg
procedure [[R14]] at a false discovery rate of 5 per cent.

### Reproducibility

Every number in this paper is regenerated by a script that writes a
machine-readable receipt, and an audit script recomputes 174 quantities
quoted in the text from the tables they came from. A second audit checks
that every number in the Abstract, Box 1, and every table and figure
legend traces to a results file or receipt, that no numeric literal
carries two incompatible statistical labels (a hazard ratio quoted where
another table calls the same figure a p-value, for example), and that no
cross-reference or sample-size count is stale. Neither audit pins every
cell of every table.

Analyses used Python 3.14 with numpy 2.5.0 [[R41]], scipy 1.18.0 [[R42]],
pandas 3.0.3 [[R43]], statsmodels 0.15.0 [[R44]] and lifelines 0.30.3
[[R45]].

---

### Ethics

This study analysed publicly available, de-identified datasets, and
generated one time-kill experiment in a reference strain of *Escherichia
coli*. No human or animal subjects were involved, no patient samples were
collected, and no individual is identifiable from any material presented
here. The prospective experiment was performed at the Department of
Microbiology, Iran University of Medical Sciences, Tehran, Iran, on a
biosafety-level-1-appropriate quality-control strain (ATCC 25922); no
institutional review board holds jurisdiction over secondary analysis of
de-identified public data or over work on a bacterial quality-control
strain.

### Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

Anthropic's Claude was used under the author's direction to read the
manuscript and to assist in running the Python analysis pipeline. Claude
Sonnet 5 was further used, under the author's direction, to document and
organise the analysis code and to prepare its commits to the
version-controlled repository. No figure, image or schematic was
generated by an artificial intelligence tool; every figure is plotted
from values that regenerate from the public deposits. No artificial
intelligence tool is an author. The author directed the study, verified
every reported quantity against the source deposits and the regenerating
pipeline, and takes full responsibility for the content of this article,
including its accuracy and its originality.

### Data availability

Every dataset analysed here was already public under an open licence.
Each is identified in Table 1 and cited alongside the article that first
described it: Vijay and colleagues [[R5]][[R51]], van Wijk and colleagues
[[R4]][[R23]], Windels and colleagues [[R6]][[R38]], Kaur and colleagues
[[R7]][[R37]], and the hollow-fibre Source Data of Dubey and colleagues
[[R8]][[R36]], held out of every fitting step. The readings from the
prospective experiment are deposited with the analysis code.

That code, both audit scripts, the headroom tool and machine-readable
receipts recording the software versions each stage ran under are in a
public repository [[R52]], dual-licensed: the code under the
Massachusetts Institute of Technology (MIT) licence, and the manuscript,
figures and results under CC BY 4.0. The deposits
keep their depositors' own licences. It is at
https://github.com/piranfar/detection-floor-tolerance-endpoints, and this
manuscript was built from commit {{COMMIT}} of it.
---


## Acknowledgments

This research received no specific grant from any funding agency in the public,
commercial or not-for-profit sectors.

The author declares no competing interests.

Vahhab Piranfar is the sole author and is responsible for conceptualisation,
methodology, software, formal analysis, investigation, data curation, writing of
the original draft, review and editing, and visualisation.

---

## References

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

**Figure S3. A late endpoint cannot resolve a 32-fold concentration range.**
Apramycin against *M. tuberculosis*, five concentrations, triplicate counts.
(**A**) The trajectories, with an assumed floor of 100 CFU/mL — the value 10 µL
plating would give — drawn as a band; this deposit records no plated volume, so
the band is an assumption and is drawn to show what the assumption costs; by day 14 the highest arm lies within it, so its apparent rate
over the final interval is a lower bound. (**B**) The ratio of survivors between
the lowest and highest of the four compared concentrations, 4 and 128 µg/mL, at
each sampling day, rising to 48.2-fold at
day 7 and collapsing to 5.2-fold at day 14. (**C**) The concentration slope fitted
separately in each interval from a replicate-level bootstrap, 20 000 draws.

**Figure S2. Resistance and tolerance occupy separate axes, in two designs.**
(**A**) All 24 comparisons between the concentration axis and the duration axis
that the 217-isolate file supports, each against the Benjamini–Hochberg critical
value it would have to beat. Amber marks the four reaching nominal significance;
none survives. (**B**) The censoring behind them: the fraction of isolates at the
assay ceiling rises with endpoint depth, and the nominal hits concentrate where
censoring is heaviest. (**C**) The same question in 126 evolved *E. coli* clones,
by nutrient stratum.

**Figure S1. The descriptive survival picture behind Figure 2.** The same six
laboratories, one written protocol, one stock of *M. tuberculosis* H37Rv,
moxifloxacin at ten times the minimum inhibitory concentration.
(**A**) Kaplan–Meier curves for time to the first observed crossing below the
assay floor at the 100 µL plating. Three curves never descend: those
laboratories recorded no flask below the floor in any arm at that plating, so
their first-crossing times are right-censored throughout.
(**B**) The model-based p-value attached to each laboratory in a descriptive Cox
model before (grey) and after (arrow head) starting density is added, showing how
far the two predictors overlap. Institute A is the reference, so the model carries
five laboratory terms; four of them move toward p = 1 on adjustment — B from
0.093 to 0.264, D from 0.015 to 0.138, E from 0.016 to 0.172 and F from 0.015 to
0.576 — while institute C moves the other way, from 0.014 to 0.00041. Those
p-values are plotted because they are what moves, not because they are valid: the
laboratory label is constant within its own cluster and there are six clusters, so
no between-laboratory test is available and none is claimed. Blue marks a term
crossing the conventional threshold, which is a description of the movement and
not a finding. Both panels stood in Figure 2 in an earlier version and are here
because each had to disclaim itself in its own legend. Colour, and the split
between laboratories that ever crossed and those that never did, are shared with
Figure 2 by construction: both figures read the assignment from one function.

**Figure S4. The corpus screened, and how five deposits came out of it.** A
funnel of the literature screen described in Methods, from the 78 candidate
time-kill datasets assembled to the five carried forward into Table 1. Each
stage names what left the funnel to produce the next count. Blue: still in
the screen. Green: the five deposits reanalysed in the article. Full manifest
and per-record verdicts: Table S12.

**Figure S5. One culture, two plated volumes, two tolerance labels.** The
prospective experiment's standard-inoculum arm, three flasks, plated at 10
and 100 µL from the same dilution series. (**A**) Kill curves at both
platings; filled points are measured counts, open points sit on the assay
floor and are censored. (**B**) Headroom per flask at each plating against
the four-log endpoint: every flask reaches it at 100 µL and falls short at
10 µL. (**C**) The threshold sweep behind Table S10 — the share of
sample-times at which the two platings' recorded fractions fall on opposite
sides of a class cut, as the cut moves; the marked line is the cut the
clinical classification of Section 2 uses.

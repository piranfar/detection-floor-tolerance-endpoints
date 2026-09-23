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

**Figures:** 2 | **Tables:** 3 | **Boxes:** 2 | **Supplemental figures:** 6 | **Supplemental tables:** 26

---

## Abstract

Time-kill assays are the standard method for evaluating antibiotic
tolerance, but starting bacterial density and the assay's detection floor
are frequently overlooked, causing systematic misclassification of
bacterial survival. We show how an unreported detection floor
structurally distorts rifampicin tolerance classification in
*Mycobacterium tuberculosis*.

We analyzed rifampicin tolerance against the detection floor in
217 clinical *M. tuberculosis* isolates, isoniazid-susceptible and
isoniazid-resistant alike, and derived two boundaries from the
assay's own definitions: a reachability boundary, below which starting
density cannot mathematically support the assigned log reduction, and an
identifiability boundary, below which a floor-level reading cannot be
distinguished from a lower tolerance class. We then ran a prospective *Escherichia coli*
time-kill experiment in our laboratory, testing both boundaries
independently of the tuberculosis collection.

The classification proved structurally compromised in the clinical cohort. Thirty-three of 217 isolates lacked the starting density needed to
reach their assigned 99.99 percent reduction, and none did. Eighteen isolates ended exactly at the detection floor; a third were
compatible with more than one tolerance class. These outcomes tracked growth rate, and isoniazid-resistant
isolates, seeded at a tenfold lower starting density than susceptible
ones, were disproportionately exposed.
Our *E. coli* experiment confirmed both boundaries outside
*M. tuberculosis*: adjusting the plated volume alone assigned two
conflicting tolerance labels to a single culture at six of 54 sample times.

A rifampicin tolerance classification made without reporting starting
density and detection floor is mathematically uninterpretable. Whether
starting density explains isoniazid-resistant isolates' disproportionate
exposure as a confounder or a mediator is unresolved here.

**Keywords:** time-kill assay; limit of quantification; minimum duration for
killing; antibiotic tolerance; colony counting; censored data;
*Mycobacterium tuberculosis*

## Introduction

Tuberculosis treatment runs for four to six months (1). Shortening it means
finding drugs that kill *Mycobacterium tuberculosis* faster, and that choice is
made in a flask: compounds are ranked by in vitro killing curves, counts of
surviving colonies read off a plate over time.

A negative culture taken after treatment has begun is not evidence of sterility,
which is why blood cultures are drawn before the first dose. The plate also has
a hard floor, and the pipette sets it: the smallest positive result is one
colony, and what one colony means depends on the volume spread. Plate 100 µL and
one colony is 10 bacteria per mL. Below that the plate reports no growth, which
is not the same as nothing there. Write *L* for that floor and *N₀* for the
starting density.

Tuberculosis makes that floor expensive, because the phenotype invoked to explain
why treatment takes so long is itself defined by a duration. Tolerance is the
capacity of a genetically susceptible population to survive an exposure that
should kill it: the drug still works, the bacteria take a long time to die, and
that time is the measurement.

Rather than asking whether a culture went negative, the modern definition asks
how many logs the population fell: the minimum duration for killing, MDK, is the
time to a specified fractional reduction (90, 99 or 99.99 per cent), proposed as
the tolerance counterpart to the minimum inhibitory concentration (2, 3).
The fraction is the whole point. A ratio to the starting population is
scale-free: if the count falls in a straight line on a log scale at rate *b*, the
time to a *q*-log reduction is *q/b*, and the starting density cancels. By
construction MDK cannot be contaminated by how much culture went into the tube.

MDK as originally defined is not a plate-count metric: it was measured from
presence or absence of survivors in microwell arrays of about a hundred cells, a
design chosen to avoid dilution plating, and the consensus guidelines say how the
smallest detectable count should be established (3, 4). What this paper
examines is the form the tuberculosis field adopted, log-reduction endpoints
computed from plate counts and most-probable-number series. The floor problem
belongs to that implementation, not to the definition.

The property holds in the definition and fails in the measurement, and that gap
is what this paper is about. To show a four-log kill you have to see four logs
down, and what is visible is bounded below by the floor. So an isolate has

    headroom  h = log10(N₀ / L)

and no experiment can demonstrate a reduction deeper than *h*, however completely
the drug worked. Where *h* < *q* the endpoint is unreachable before the drug is
added. That is the first boundary, and we call it reachability.

It gets worse when the last count lands on the floor. The fraction written down
is then *L/N₀*, the floor divided by the starting density. The drug has dropped
out of it; what is left is the pipette and the inoculum. A metric designed to be
inoculum-independent becomes a pure inoculum readout at exactly the depth where
tolerance is scored. That is the second boundary, identifiability.

Inoculum-dependent tolerance measurements have been reported before under a
different mechanism: an *Escherichia coli* persister assay gave different
tolerant fractions depending on growth phase and culture history, attributed
there to prophage induction rather than to an assay floor (5). That report
and this one agree on the symptom and differ on the mechanism, and neither rules
out the other operating in a given assay.

No prior treatment converts a floor-level reading into the classification rule it
becomes. When the last count sits at *L*, the recorded fraction is *L*/*N*₀, and
the low, medium or high label is then a cut on starting density. That is the gap
this paper fills. Two further failures stay distinct from it: a duration ceiling
(the assay stopped looking) is not a count floor, and recording a below-limit
flag is not the same as scoring a duration from the points so recorded.

This study asks how deep a log-reduction tolerance endpoint can be measured at
all, and whether isolates have been assigned tolerance phenotypes from outside
that range. Two boundaries on the starting density follow from the definitions,
one deciding whether an endpoint is reachable and the other whether a
floor-level reading identifies a class, both computed from quantities a
time-kill protocol already records.

That question needs data recording three quantities (a starting density measured
before treatment, a time series, and either a plated volume or a stated floor),
and most do not. Of 78 candidate time-kill datasets assembled for this study, 45
were inspected in full; of the 40 distinct literature deposits among them, **32
state no assay floor by any route**. That is the first result, and it is why the
five carried forward are five rather than fifty (Table S1).

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
began at each. The last two are why a written protocol does not standardise
measurable depth: the plated volume sets *L*. To make both a four-log endpoint
and a low class identifiable against *L* = 23 per mL, seed above
*L* · max(10⁴, 1/*c*₁) = 230 000 per mL, or choose a shallower endpoint.

---

## Results



### 1. Rifampicin tolerance in 217 clinical isolates is scored against an unreported assay floor

Most-probable-number (MPN) readings take only the discrete values of an MPN
table (6, 7), a fixed ladder of rungs, not a continuous scale. The
day-5 column does not taper towards zero. It stops. Eighteen isolates sit at
exactly 23 per mL in the 15-day panel and six in the 60-day panel, and
nothing in the file lies below that (Fig. 1A). That is a floor, not a tail,
and it is treated as one throughout.

Each isolate therefore carries a fixed budget of killing the assay can see.
At 15 days of prior culture the starting densities run from 2,300 to
61,000,000 per mL (3.36 to 7.79 log10), so headroom, the distance from the
starting density down to the floor, runs from 2.00 to 6.42 log10 (Fig. 1B,
Table 1): both spans are the same 4.42 log10.

Against that budget the three deposited endpoints behave very differently.
Every isolate has room for a 90 or a 99 per cent reduction: 0 of 217 fall
short in either case. **Thirty-three of 217 isolates (15.2 per cent) lack
the headroom for the 99.99 per cent endpoint**, a four-log reduction that
was unobservable for them before rifampicin was added.

All 33 are recorded as not having reached the endpoint, sitting at the
**assay ceiling**: a census rather than an estimate, since the floor
censors the count while the ceiling censors time, an isolate not yet at
its endpoint after six days being recorded at the last day rather than
the day it would have reached. Among the 184 isolates that did have four
logs of headroom, 162 are also at the ceiling, 88.0 per cent.

### 2. The same floor-level reading yields opposite tolerance labels depending on starting density

The deposited tolerance level is a cut-off on the recorded surviving
fraction, with no overlap between classes. The thresholds themselves are
not deposited; recovered here, at day 5 and 15 days of prior culture, low
tolerance covers fractions below 10⁻³, medium 10⁻³ to 10⁻², high above
10⁻². Those cuts reproduce every usable class in the file, 203 of 203
(Table S2). Usable means the 203 of 217 isolates whose label is one of the
three ordered classes; the other 14 carry the "MDR" category, which no
ordered analysis can place (Table S3). What follows is an argument about the
fraction the assay recorded, not about an independent clinical judgement.

Eighteen isolates ended at the floor. They share one reported floor-level
observation, but their true final counts are unknown below the floor, so
the assay cannot tell their surviving burdens apart down there. Their
starting densities span 265-fold, from 23,000 to 6.1 × 10⁶ per mL, so the
same terminal reading implies a different range of compatible reductions
in each: at least 3.00 logs for the isolate that began at 23,000, at least
5.42 for the one that began at 6.1 × 10⁶, and in either case the true
reduction may be anything from that bound down to complete kill. What the
deposit records instead is a single number per isolate, *L*/*N₀*, and
those recorded fractions span the same 265-fold, from 3.8 × 10⁻⁶ to 1.0 ×
10⁻³ (Fig. 1C). They are upper bounds on survival, not measurements of it.

The labels those eighteen received differ accordingly. Six isolates that
began at 23,000 per mL recorded a fraction of 10⁻³ and were classified
**medium** tolerance; twelve that began at 230,000 or above recorded 10⁻⁴ or
less and were classified **low**. A single cut on the starting density
alone reproduces all eighteen (Table 2): once a reading is censored at the
floor, the starting density fixes which label the published rule is able to
return.

### 3. The floor predicts, before rifampicin is added, which isolates will be mislabeled

Sections 1 and 2 counted isolates. The two boundaries derived in the
Methods do more: given only the floor, the class thresholds and each
isolate's starting density, they say in advance which isolates are
affected, before any day-5 reading is used.

For this assay *N*_reach = 23 × 10⁴ = 230,000 per mL and *N*_id = 23/10⁻³ =
23,000 per mL. Applied to the 15-day panel, the first predicts the 33
isolates unable to reach the 99.99 per cent endpoint; the second predicts
that of the eighteen isolates whose reading rests on the floor, twelve have
only the lowest class compatible and six have more than one. Those are the
three counts Sections 1 and 2 report.

Neither boundary predicts which isolates reach the floor; that depends on
what rifampicin does. Both predict what a reading at the floor can be made
to mean once it happens, and there the agreement with the deposit is exact,
isolate by isolate: the set the algebra says has a single compatible class
and the set the deposit records in the lowest class are the same set.

What is sharp is the boundary case. Six isolates sit at exactly 23,000 per
mL, which is *N*_id itself. For them *L*/*N₀* equals *c*₁ exactly, the
interval [0, *L*/*N₀*] touches the threshold from below and spans two
classes, and the strict inequality fails. Those six are precisely the six
the deposit records as medium rather than low. A rule written with the
inequality the other way would have called all six low and been wrong six
times out of six. That is a test the arithmetic could have failed and did
not.

The empirical findings are therefore consequences of the definitions rather
than properties of this deposit: any dataset reporting a starting density,
a floor and a threshold classification can be checked against them.

### 4. Isoniazid-resistant isolates appear more rifampicin-tolerant, but the effect tracks a thinner inoculum, not resistance

There are two candidate predictors of the deposited label, each tested at
two culture ages and two endpoint depths, eight tests in all. Eight tests on
one question will throw up a false positive on their own, so they are
corrected together as one family. Two survive (Table S4).

The label tracks the **growth rate** of the isolate. Slower growth goes with
a higher tolerance class, and it survives adjustment for starting density
(OR 1.096 per day of time to OD 0.4, 95 per cent CI 1.032 to 1.164, p =
0.0030, n = 202; unadjusted OR 1.126, 1.062 to 1.193). The label also tracks
**isoniazid resistance**, until starting density enters the model.
Unadjusted, a resistant isolate has 2.32 times the odds of a higher
tolerance class (1.30 to 4.12, p = 0.0042); adjusted, the odds ratio falls
to 1.31 (0.67 to 2.57, p = 0.42), and the interval no longer excludes one.
Starting density is the strongest term in the file: every ten-fold rise in
the starting MPN halves the odds of a higher tolerance class (OR 0.480,
0.340 to 0.677, p = 2.9 × 10⁻⁵).

Why the adjustment does that is measurable. Isoniazid-resistant isolates go
into this assay at 5.36 log10 against 6.36 for susceptible isolates,
ten-fold thinner (Mann-Whitney p = 9.1 × 10⁻¹⁴ (8)), and 22 of the 84
resistant isolates carrying an ordered label lack the headroom for the
deepest endpoint, 26.2 per cent, against 9 of 119 susceptible, 7.6 per
cent. They are one log short of observable killing before the experiment
begins.

In that stratum the two associations part company. Growth holds and still
survives correction (OR 1.116, 1.040 to 1.198, p = 0.0024). Resistance
returns OR 2.11 (1.07 to 4.16, p = 0.031) nominally, but ranks second in
the family of eight and fails its Benjamini-Hochberg critical value of
0.0125. The resistance association therefore leans on isolates that are not
independent of one another, and it is already the association that
starting density explains away; we report it as the weaker of the two on
both counts.

### 5. Six laboratories given one M. tuberculosis protocol still see six different assay floors

If the effect is a property of assay geometry rather than of clinical
sampling, it should appear where one protocol, one strain and one stock are
handed out deliberately. Van Wijk and colleagues ran exactly that
exercise, sending a single stock of H37Rv to six blinded laboratories under
one written protocol (9, 10).

At ten times the minimum inhibitory concentration of moxifloxacin all six
laboratories return a positive kill rate, spanning 5.2-fold, from 0.090 to
0.464 log10 CFU/mL per day (Fig. 2A, Table S5).

The two orderings do not correspond. Rank the laboratories by starting
density and the three lowest are exactly the three that recorded crossings,
the three highest exactly the three that did not, without exception, a
split with probability 1/20 under chance alone, reported as an ordering and
not a test (Table S6). Rank them by kill rate and there is no such
correspondence (Fig. 2B). Institute F has the highest starting density at
6.53 log10 among treated flasks of this arm, kills faster than four of the
other five at 0.223 log10 per day, and records no crossing. Institute E
returns the slowest rate of all at 0.090 and also records none.

### 6. The two boundaries hold in a deposit never used to derive them, in a different organism and drug

Dubey and colleagues report amoxicillin-clavulanate against
*Escherichia coli* in a hollow-fibre system (11, 12). Their Methods
state 100 µL plated with counts per mL, so *L* = 10 CFU/mL is derived
rather than inferred, and the file corroborates the derivation: all 229
genuine counts are multiples of ten, the smallest exactly ten, while 69
further entries read as one, which no 100 µL plate can produce and which
are the deposit's placeholder for below the floor.

Across the 20 cultures with a measured day-zero density, headroom runs
from 4.85 to 5.45 log10 (Table S7). Endpoints at 1, 2, 3 and 4 logs are
reachable for every culture; a 5-log endpoint is unreachable for 5 of 20,
a 6-log endpoint for all 20. On data it was not built from, the framework
locates the depth at which a sterilisation claim stops being demonstrable.

### 7. A second distortion in M. tuberculosis: bacilli invisible to culture, not just below the floor

Everything above is about the floor. One published observation in this
organism shows the floor is not the only reason a colony count understates
the population, and the two failures must not be confused.

Evangelopoulos and colleagues counted the same mouse lungs three ways,
colony count, a molecular bacterial load from 16S rRNA, and a most probable
number, on their way to a different question (13). Under the deepest
regimens the colony count reads zero in every animal: in three arms, 18
lungs in all, the plate declared every lung sterile while the most probable
number on that same tissue ran from 1,450 to 18,700 per lung. The
molecular load can be dismissed as nucleic acid outliving its owner; the
most probable number cannot, because growth in a dilution series requires
an organism that is alive and culturable.

That gap is not the detection floor. For censoring to explain a plate
reading of zero against 1,450 organisms in the same tissue, the colony
count's floor would have to sit above 1,450 per lung, far less of the
homogenate than any lung protocol plates. This is differential
culturability, a described phenotype of *M. tuberculosis*:
resuscitation-promoting-factor-dependent bacilli dominate pre-treatment
sputum and rise during chemotherapy (14), both dependent and independent
differentially culturable populations are recovered from patients whose
solid-medium cultures return nothing (15), and rifamycin action on
ribonucleic acid (RNA) polymerase converts a starved population to over 90
per cent differentially detectable in vitro (16), the same drug class
every arm of the Evangelopoulos regimen carries.

Reachability and identifiability are arithmetic on the plated volume and
would hold in an assay with perfect culturability. Differential
culturability is biology, acts on the numerator rather than the floor, and
nothing here derives or measures it. They push the same way: a count that
is both floored and culture-selective understates the surviving population
twice over, and the mouse model that decides which regimens enter clinical
trials reads out in colony counts, in exactly this region.

That deposit establishes no floor of its own. Five further *M. tuberculosis*
deposits in the same screen do. Across those five, sputum from pulmonary
tuberculosis, axenic culture, an auxotrophic H37Rv panel and two
drug-development series, with floors from 13 to 200 CFU/mL, **184 of 310
series could not have demonstrated a four-log reduction however completely
the drug worked, and 240 of 310 could not have demonstrated five** (Table S8); one could not have shown four logs in a single one of its 123 series.
None of these five carries the analysis above, and none is among the five
reanalysed here; they say the reachability problem is not a property of one
clinical panel.

### 8. A prospective E. coli experiment confirms the floor artifact: one culture, two plated volumes, two conflicting labels

Every result above reads data somebody else generated for another purpose.
This one reads an experiment built to try to break the two boundaries
*N*_reach and *N*_id, with its predictions written down before a plate was
counted. *Escherichia coli* ATCC 25922, the reference strain the standard
names for quality control, against ciprofloxacin at ten times the
concentration that stops it growing. Three seeding densities, two plated
volumes, three flasks each, 216 plate readings.

The middle arm was seeded on purpose at the 5 × 10⁵ per mL the standard
specifies. The densities actually reached were 6.4 × 10⁴, 4.4 × 10⁵ and
3.8 × 10⁶ per mL as arm means, but *N*₀ is a measurement made once per
culture rather than a setting the protocol supplies, so headroom belongs to
a flask and everything below is reported per flask. At the 100 µL plating
the low arm's three flasks have 4.19, 4.11 and 4.00 logs of headroom, the
last exactly at the four-log endpoint. **At the standard inoculum plated at
10 µL, the deepest reduction the three flasks could report ran from 3.71 to
3.93 logs**, while those same three cultures plated at 100 µL ran from 4.88
to 5.05 (Fig. S5B, Table S9). Every flask is paired with itself across the
two platings.

That much is arithmetic. So is the next step. When both platings of one
sample rest on their own floors, the two fractions written down are
*L*₁/*N*₀ and *L*₂/*N*₀, so they can fall either side of a class threshold
and give one culture two labels. **The quantity that could have come out
zero is how often a real experiment lands in the window where those two
fractions straddle the cut**, and it depends on where the cut is (Fig. S5C,
Table S10). Put the cut at one per cent and the window is nearly shut. Put
it at one in a thousand, where the clinical classification above cuts its
lowest class, and six of 54 sample-times receive two different labels from
one culture, one in nine. That cut is imported from the tuberculosis
classification; it serves here as a ruler for the window's width, not a
claim about *E. coli* biology.

---

## Discussion

Every clinical microbiologist knows that a negative culture taken under
antibiotic exposure is not proof of sterility. This paper reports that the
number brought in to replace that judgement carries the same defect, and
once it is a number, it is harder to see.

The standard is not silent on that choice. M26-A's section
1.3.2.5, *Volume Transferred*, ties the volume to the endpoint with a
counting rule: after the defined 99.9 per cent killing, at least ten
colonies must remain (17) (for a standard inoculum of 5 × 10⁵ per mL
that means at least 20 µL streaked, so a 10 µL streak fails the rule), and
section 3.1 separately requires the smallest detectable count to be
established by serial dilution. A guideline written in 1999 already
required both numbers this paper asks for. The deposits reanalysed here do
not meet it because the endpoint moved: M26-A
nowhere contemplates a four-log call, and the volume rule did not travel
with the deeper endpoints.

Take the assay's contribution out and what is left is consistent with
biology. Growth state predicts the tolerance class before and after
adjustment for starting density (isoniazid needs KatG and active
cell-wall synthesis (18), rifampicin needs transcription (19)), and
a population that is not dividing offers less of what these drugs act
on. The classification tracks physiological state at least as much as
drug susceptibility.

That axis is the one tuberculosis drug development already leans on.
Killing assays of this design rank regimens before they enter trials, and
tolerance followed in patients is now being read as within-host evolution
(20). A whole-host simulation of tuberculosis treatment reports the
same sensitivity one step further downstream: which regimen ranks best
in a granuloma model changes with the CFU detection threshold used to
define success, independent of any question about tolerance
classification (21). If a tolerance classification is partly an inoculum measurement,
conclusions drawn from it, that one regimen sterilises faster than another,
or that a patient's isolates are becoming more tolerant over therapy, are
in part conclusions about how the assay was set up. The correction applied
here does not remove the biology; it aims it at the right target. The
phenotype that survives the correction is growth state, real, targetable
and directly measurable, unlike a fraction read off a floor.

The prospective experiment has a limitation a reader should raise first.
Its samples were diluted in saline and plated; they were not washed,
filtered or treated to inactivate the drug, and no carryover control was
run. Antibiotic carried onto the plate suppresses colony formation
without killing anything, the same class of counting artefact this paper
is about. The design is conservative in this respect rather than clean:
the larger plated volume carries ten times more drug to the plate, so
carryover would shrink the difference between the two platings that
Section 8 reports, not manufacture it. The experiment cannot exclude
carryover, and a repetition should include the control that would.

Several further limitations bound what the analysis can establish; each
points at the experiment that would settle the question, and the ones
bearing on the claims made are given here, with the rest in the
supplement.

This paper has already acted on the first rather than declaring it.
Flasks from one laboratory share a starting culture; repeat isolates come
from a patient already counted. Every conclusion from the two primary
deposits was recomputed at the level where the observations are
independent, listed one line at a time (Table S6): twenty survive
unchanged, six survive with much wider uncertainty, five do not survive
and **have already been removed from the text above**, and one is
withdrawn because the null it was tested against was already false before
any data were seen.

The 15-day and 60-day panels of the clinical deposit contain the same
isolates. The comparison between panels is therefore not independent, and
it bounds the evidence for a difference rather than establishing it.

Starting density could sit on the causal path rather than beside it.
Suppose resistance slows growth, and slow growth causes genuine tolerance:
then the thin inoculum is a consequence of the slow growth, and adjusting
for it would remove real signal rather than a confounder. The asymmetry
favours the confounding reading, since growth survives adjustment and
resistance does not, but a design that fixes the inoculum would settle it.

**Choose the depth of the endpoint to fit the headroom actually available,
rather than densifying the inoculum merely to buy more.** The inoculum
needed can be worked out before the experiment: seeding above *L* ·
max(10^*q*, 1/*c*₁) makes both failure modes impossible, the endpoint that
was never reachable and the last count that lands on the floor; for this
assay that is 230,000 per mL. Seeding higher also changes the experiment,
because a denser culture is a different physiological state, and
physiological state is what the tolerance label tracks. Where the deep
endpoint is wanted, lower the assay floor instead; where the headroom will
not carry it either way, the shallower endpoint is the honest one.

**Treat an endpoint at the floor as a bound, not a value.** Analysed as a
measurement it manufactures differences between isolates whose final
viable burdens the assay could not tell apart.

**Fix the inoculum, or adjust for it, before comparing tolerance across
groups.** The comparison that motivated this work, resistant against
susceptible isolates, is confounded by a ten-fold difference in starting
density. Until that difference is understood, group comparisons of
tolerance in clinical isolates should carry the starting density as a
covariate.

**Box 2. The minimum information a time-kill assay must report.** Five
fields that make a reported tolerance endpoint recomputable by a reader.
Each is produced by the experiment as run; none asks for new apparatus.
What they cost is visible from the other side: of the 78 candidate
time-kill datasets assembled for this study, 45 were inspected in full,
and of the 40 distinct literature deposits among them, 32 state no assay
floor by any route, so most published endpoints cannot be recomputed
against their own measurement.

| # | Field | What to report | What fails without it |
|---|---|---|---|
| 1 | Starting density | *N*₀ with its method (viable count or MPN value, not an optical density) | the endpoint is a fraction of *N*₀; OD-derived densities disagreed with the measured ones by up to 1.53-fold within one culture here |
| 2 | Assay floor | *L* as a value, or the plated volume / dilution design that fixes it | nothing deeper than log10(*N*₀/*L*) was ever visible; without *L* a failed endpoint is arithmetic |
| 3 | Censoring convention | what is written when nothing grows: zero, the floor value, ND, or the lowest table rung | the convention decides whether a floor reading is a bound or a measurement |
| 4 | Endpoint rule | the *q* in MDK_q and the interpolation between sample times | one kill curve returns different durations under different rules |
| 5 | Physiological state | culture age or growth phase at sampling, as a recorded value | the label tracks state; unrecorded, state is confounded with every group compared |

A report carrying all five can be audited against its own floor, which is
the test applied to every deposit in this article.

A time-kill guide already exists and this five-field minimum does not
replace it: ASTM International (the American Society for Testing and Materials)
guide E2315 sets out how to run and report a time-kill
procedure in general (organism, media, neutralisation, raw counts), and
none of its reporting requirements is *L*, headroom or a censoring
convention specific to a duration endpoint cut on a fraction of the
starting count (22). The five fields above are additional to that guide,
and apply wherever a killing curve is read against an assay floor to
score how long killing took rather than only whether it happened.

---

### Conclusion

A plate that grows nothing under antibiotic has never been evidence that
the flask was sterile. The remedy adopted was to stop asking whether the
culture went negative and to start asking how far it fell, expressed as a
fraction of where it began so that the starting culture could not matter.
The fraction stops being a fraction once the population reaches the
floor. What is recorded from that point is *L*/*N₀*, which moves with the
starting density and not with the surviving population: here for fifteen
per cent of isolates at the depth the classification uses, and for the
eighteen isolates whose recorded label a single threshold on their
inoculum reproduces exactly.

A tolerance call made without its headroom cannot be told apart from an
inoculum measurement, and the phenotype associated with survival after
correction tracks physiological state at least as much as drug
susceptibility. That is not the same as saying tolerance is an artefact.
Report the starting density and the assay floor. Match the depth of the
endpoint to the range actually available. Treat a reading at the floor as
a bound. Until those three things are routine, some of what the field
calls tolerance cannot be separated from a record of how much culture
went into the tube.

What this study adds is a way to see the problem before the plates are
poured: two boundaries computed from quantities a time-kill protocol
already records, a classification that refuses rather than guesses when
the assay cannot decide (Table S11), a five-field minimum that makes any
killing endpoint recomputable (Box 2), and a small tool that returns the
endpoint a planned assay can support. The cost is five numbers written
down. The return is a tolerance phenotype that means the same in one
laboratory as in the next, and that can bear the weight regimen research
already puts on it.

## Materials and Methods

### A screen of 78 time-kill datasets for M. tuberculosis and E. coli assay floors

This study combined mathematical derivation, analysis of five public
datasets, and a prospective *Escherichia coli* experiment. We assembled 78
candidate time-kill datasets from the published literature (21 August – 8
September 2026) and screened 45 of them field by field for the three
quantities the two boundaries below require: a pre-treatment starting
density, a longitudinal series of viable counts, and either a plated
volume or a stated assay floor. Every inclusion and exclusion is recorded
in a manifest deposited with the analysis code.

Forty-one distinct records were inspected, one of them this paper's own
prospective experiment. Of the 40 remaining literature deposits, 32
reported no assay floor by any route: no limit of detection, no limit of
quantification, and no plated volume from which one could be derived.
Eighteen carried enough information to compute both boundaries, and five
carried the complete set of fields the full analysis requires (Table 3,
Fig. S4). The full pipeline is summarised in Fig. S6. These 78
candidates are a documented sample of the literature, assembled without a
registered search protocol; the two boundaries are derived from
definitions rather than estimated from the corpus's size, so a single
deposit with a stated floor is enough to demonstrate them.

Four datasets supported the empirical analyses. **Clinical isolates with a
deposited tolerance classification:** 217 *M. tuberculosis* isolates
assayed under rifampicin, each carrying a minimum inhibitory
concentration, minimum durations for 90, 99 and 99.99 per cent killing at
15 and 60 days of prior culture, most probable number readings at days 0,
2 and 5, a growth-rate proxy, isoniazid susceptibility with the resistance
mutation where present, and the authors' own tolerance level for each
isolate (23). Of the 217 rows, 43 are follow-up isolates from patients
already represented, so a baseline-only stratum is analysed separately.

**The six-laboratory exercise:** *M. tuberculosis* H37Rv from one stock,
distributed with one written protocol to six blinded laboratories
(9, 10). Moxifloxacin and isoniazid at one and ten times the minimum
inhibitory concentration, three flasks per arm, each sample plated at four
volumes: 100 µL quadruplicate, 10 µL as four drops, 10 µL as a single
drop, and 2.5 µL as a single drop, giving three distinct floors spanning
1.60 log10 within a single flask-visit (24). The file holds 2,775
readings; the analysis set, after dropping unusable values and
pre-treatment visits, is 2,580.

**Evolved clones:** 126 *Escherichia coli* clones from a parallel
evolution experiment under amikacin, each carrying an endpoint minimum
inhibitory concentration and a persister fraction (25, 26). Six of
its 595 surviving fractions are written as exact zeros with no named
floor, so this deposit is one of two for which observability labels are
refused.

**Concentration-by-time grid:** apramycin against *M. tuberculosis* at
128, 32, 8, 4 and 1 µg/mL, triplicate log10 CFU at days 0, 3, 7 and 14
(27, 28). The 1 µg/mL arm shows net growth rather than killing and is
excluded from the dose comparison, leaving 4 to 128 µg/mL as the range
compared (Text S3).

A fifth dataset was evaluated only after the boundaries, thresholds, and
modelling choices had been fixed. **Validation deposit:** amoxicillin-
clavulanate against *Escherichia coli* in a hollow-fibre infection model,
with 100 µL plated, measured day-zero densities for every culture, and
below-limit readings retained as a placeholder (11, 12). It was the
only deposit found carrying all three fields the boundaries require, and
no boundary, threshold or modelling choice in this paper was informed by
it; it is used nowhere else except to confirm them (Section 6).

Each dataset's organism, drug, design and licence is summarised in Table
1; the complete screening manifest and exclusion reasons accompany the
analysis code.

### Prospective E. coli experiment designed to test the floor artifact

An *in vitro* experiment was designed to prospectively test both
boundaries. Its design sheet, predictions and plate counts are one
workbook, deposited with the analysis code, with every prediction written
down before a plate was counted.

*Escherichia coli* ATCC 25922, the CLSI quality-control reference strain,
was grown in cation-adjusted Mueller–Hinton broth and plated on
Mueller–Hinton agar, incubated at 35 ± 2 °C in ambient air (17, 29).
The ciprofloxacin MIC, determined by CLSI reference broth microdilution
(29, 30), was 0.008 mg/L, within the CLSI quality-control range for
this strain (30); the exposure was set at ten times it, 0.08 mg/L,
chosen to kill deeply and fast enough that every arm reaches the floor
within the sampling window.

Three seeding arms were set so the four-log endpoint is unreachable in
one, marginal in the second and comfortable in the third: targets of
5 × 10⁴, 5 × 10⁵ and 5 × 10⁶ CFU/mL (the middle arm the CLSI-specified
inoculum), reaching 6.4 × 10⁴, 4.4 × 10⁵ and 3.8 × 10⁶ CFU/mL as measured
from day-zero counts: headroom of 4.11, 4.94 and 5.88 logs at the pooled
100 µL floor, and 3.11, 3.94 and 4.88 logs at the pooled 10 µL floor, so
the lowest arm is reachable for a four-log endpoint only at the deeper
plating. Three flasks per arm were sampled at 0, 1, 2, 4, 6 and 24 h; at
each time, one dilution series was plated at both 100 µL and 10 µL in
duplicate, giving 216 plate readings in all. Viable density was
*N* = *C*·*D*·1000/*V* for *C* colonies counted at dilution factor *D* and
plated volume *V* µL.

No carryover control was run. Because the 100 µL plating carries ten times
as much drug onto the plate as the 10 µL plating of the same sample, any
carryover effect works against the depth advantage the 100 µL plating is
reported to have, so the paired comparison in Section 8 is conservative
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

### Where rifampicin tolerance readings are censored by the assay floor

No deposit analysed here reports a validated limit of quantification with
a value. Throughout this paper *L* is therefore an **operational assay
floor**: where a plated volume is recorded it is the **minimum reportable
positive count**, one colony in that volume; where none is recorded it is
inferred from the deposit and labelled as such. The term limit of
quantification is used only in reporting what a source states.

In running text *L* is the **assay floor**, the only short form used, so
that "boundary" is left free for the two derived boundaries of the next
subsection. The event a time-to-event analysis records is correspondingly
a first observed crossing below the assay floor. What *L* is in each
deposit is tabulated deposit by deposit (Table S12).

Two censoring problems are handled separately. A **count below the assay
floor** is left-censored: the population is somewhere below a known
value. In the clinical deposit the floor is inferred at 23 MPN/mL from
three signatures: it is the smallest value in the file, nothing lies
below it in 1,932 readings, and the minimum shifts by exactly a factor of
ten per culture age; the conclusions drawn from it hold across the full
range the deposit's own MPN table admits (Table S13). A **crossing time
not observed within the study** is right-censored: a flask that never
falls below the floor contributes the information that its crossing time
exceeds its last visit, and enters the survival likelihood as such rather
than as missing.

A volume-derived plate floor bounds the true count from above, [0, *L*];
an MPN rung does not, since its likelihood extends well above the rung.
Every identifiability verdict was therefore recomputed under the assay's
own likelihood rather than the plate-sweep bound, confirming the same
classification under both treatments (Table S14). Each below-limit flag
in the six-laboratory deposit is judged against its own plated volume's
floor rather than pooled to the least sensitive volume, since pooling
would discard genuine quantified counts a more sensitive plating of the
same sample recorded (Table S12 note).

A volume-derived floor is a point mass, with nothing to infer. A floor
inferred from a pile-up on a most-probable-number rung carries a discrete
posterior over the rungs at or below the observed minimum; the interval
quoted is the 95 per cent highest-posterior-density support. Where no
floor is evidenced, or the support spans more than one log10, observability
labels are **refused** rather than reported (Table S15): the clinical
deposit passes this rule at 0.40 log10 of support, and two of the five
deposits fail it. This paper fits nothing to predict an MDK: once *L* is
in hand the rest is derived.

The same likelihood turns classification into an inference with its own
refusal rule: given a floor reading, the posterior over the true count
maps through starting density to a posterior over class, and an isolate
is refused when no class reaches 95 per cent confidence (Table S11). The
refusal holds across both well designs, both floor readings and two
priors.

### Two boundaries that predict which rifampicin tolerance calls are unreliable

For a culture starting at *N₀* against an assay floor *L*, the
**headroom** is *h* = log10(*N₀*/*L*), the deepest reduction the assay can
resolve. Two boundaries follow from the definitions alone.

**Reachability.** A *q*-log endpoint is observable only if

  *N₀* ≥ *N*_reach = *L* · 10^*q*.

**Identifiability.** A censored reading places the true count in [0, *L*],
so the recorded surviving fraction is at most *L*/*N₀* (an upper bound,
not a measurement). Given class thresholds 0 < *c*₁ < *c*₂ …, the class is
determined by the data only if

  *N₀* > *N*_id = *L*/*c*₁,

since the censored interval always contains zero and so is only
compatible with the lowest class above this point. Both boundaries are
properties of the method alone; seeding a culture above
*L* · max(10^*q*, 1/*c*₁) makes both failure modes impossible before an
experiment runs. The class thresholds *c*₁, *c*₂ are an input to this
definition, not an output of it: *N*_id only tests a classification
independently of the data being classified when the thresholds come from
somewhere other than that data. Where a deposit states its own
thresholds, the test is independent; where they are recovered from the
deposit itself, as in Results Section 2, the agreement that follows is an
identity rather than a test, and the manuscript says so at the point it
occurs.

### Statistical analysis

Log10 viable counts were modelled as a linear function of time using a
**Tobit model** with observation-specific left-censoring limits, fitted by
maximum likelihood (31); a censored reading contributes log Φ((limit −
µ)/σ), the probability it fell below its own limit (Beal's M3 written
for this assay (32)). As a consistency check, 50 imputed datasets were
generated from the fitted truncated-normal distribution, analysed by
ordinary least squares, and pooled using Rubin's rules (33); both
procedures share the same distributional assumptions, so their agreement
shows the answer does not depend on which arithmetic recovers it, not that
the sub-floor distribution is normal.

The growth proxy is the deposit's time to an optical density of 0.4, in
days, so it runs inversely to growth rate. **The tolerance label** was
modelled as an ordered categorical outcome by proportional-odds ordinal
logistic regression (34), with starting density as a prespecified
covariate; proportional odds was tested by a Brant test per predictor
(35) and a likelihood-ratio test against a generalised ordered logit
(36), with the partial-proportional-odds fit reported where it fails
and checked against a multinomial fit assuming no ordering (Table S16).

**Time-to-event analysis** treated the first observed crossing below the
assay floor as the event, right-censoring series that never fall below
it; 60 per cent of series that cross read above the floor again at a
later visit, so the event is a crossing, not a clearance. The crossing
time is interval-censored between the last visit above the floor and the
first below it; interval-censored fits (37) are reported alongside
Kaplan–Meier (38) and Cox proportional hazards (39) as descriptive
summaries, with cluster bootstraps over laboratories and flasks (40)
in place of the partial likelihood's independence assumption, and
proportionality tested on Schoenfeld residuals (41, 42).

**The replicate-level bootstrap** (43) behind interval slopes resamples
the three replicate counts with replacement, takes their mean, refits the
concentration slope on each draw, and takes percentile intervals from
20,000 draws, reported instead of a least-squares fit through the
deposited concentration means, which has two residual degrees of freedom
and discards the replicate scatter. An interval on a proportion is the
Jeffreys interval (44).

**Causal mediation of the resistance association.** A linear
product-of-coefficients mediation decomposes the total effect of
isoniazid resistance on the day-5 tolerance class into an average causal
mediation effect through log10 *N₀* and an average direct effect
(45, 46), with bootstrap percentile intervals from 5,000 resamples.
A refit excludes the 18 of 203 isolates whose day-5 reading sits at or
below the floor, since their recorded fraction carries no measured
numerator. Sequential ignorability is assumed and untestable here; the
sensitivity that matters is the residual correlation between mediator and
outcome errors at which the point estimate crosses zero, about −0.23. No
claim is made that unmeasured confounding is absent.

**Denominators.** A dozen denominators appear in this paper and each is
derived in a single place (Table S3): the MDR tolerance label is dropped
wherever an ordered outcome is fitted (14 rows per panel, 20 at 60 days),
the growth proxy is missing for one isolate, and five of 72 treated
flasks in the six-laboratory deposit carry no usable starting density.
Dropped rows are compared with retained ones on starting density and
susceptibility to test whether the exclusions are plausibly ignorable
(Table S17).

**Decomposition of a crossing time.** Over an interval where the decline
is close to log-linear, log10 *N*(*t*) = *a* − *bt*, and with *ℓ* the log10
assay floor and *D* = *a* − *ℓ* the distance the population starts above
it, the crossing time is *T* = *D*/*b*. For two flasks,

    log(T_A / T_B) = log(D_A / D_B) − log(b_A / b_B),

which splits a difference in crossing time into a distance term and a
rate term. An **inversion** is a pair in which A fell faster yet crossed
later, occurring exactly when *D_A*/*D_B* > *b_A*/*b_B*.

**Multiplicity.** Where a question admits more than one test, every test
the deposit supports is run, and the family is corrected by the
Benjamini–Hochberg procedure (47) at a false discovery rate of 5 per
cent.

Four procedures are implemented in the released analysis code rather than
taken from a package: the Brant test, the partial-proportional-odds fit,
the product-of-coefficients mediation, and the residual-correlation
sensitivity. These live in `exp30_ordinal_tolerance.py` and
`exp34_mediation.py`; the partial-proportional-odds likelihood is
validated against the
proportional-odds fit it nests, agreeing to 1.0 × 10⁻¹⁰ in log-likelihood.

Analyses used Python 3.14 with numpy 2.5.0 (48), scipy 1.18.0 (49),
pandas 3.0.3 (50), statsmodels 0.15.0 (51) and lifelines 0.30.3
(52).

### Ethics

This study analysed publicly available, de-identified datasets, and
generated one time-kill experiment in a reference strain of *Escherichia
coli*. No human or animal subjects were involved, no patient samples were
collected, and no individual is identifiable from any material presented
here. The clinical isolates reanalysed in Section 1 through Section 5 were
collected under the ethical approval reported by their depositors: the
Institutional Research Board of Pham Ngoc Thach Hospital, the Ho Chi Minh
City Health Services and the Oxford University Tropical Research Ethics
Committee (OxTREC 030-07) (53); the isolates are deposited de-identified
and CC BY 4.0 licensed for secondary analysis, and this manuscript performs
no new sampling from any patient. The prospective experiment was performed at the Department of
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
Each is identified in Table 3 and cited alongside the article that first
described it: Vijay and colleagues (23, 53), van Wijk and colleagues
(9, 10), Windels and colleagues (25, 26), Kaur and colleagues
(27, 28), and the hollow-fibre Source Data of Dubey and colleagues
(11, 12), held out of every fitting step. The readings from the
prospective experiment are deposited with the analysis code.

That code, both audit scripts, the headroom tool and machine-readable
receipts recording the software versions each stage ran under are in a
public repository (54), dual-licensed: the code under the
Massachusetts Institute of Technology (MIT) licence, and the manuscript,
figures and results under CC BY 4.0. The deposits
keep their depositors' own licences. It is at
https://github.com/piranfar/detection-floor-tolerance-endpoints, and this
manuscript was built from commit fbc0bb5+ of it.

### Declaration of computational reproducibility

Every number in this paper is regenerated by a script that writes a
machine-readable receipt, and an audit script recomputes 174 quantities
quoted in the text from the tables they came from. A second audit checks
that every number in the Abstract, Box 1, and every table and figure
legend traces to a results file or receipt, that no numeric literal
carries two incompatible statistical labels (a hazard ratio quoted where
another table calls the same figure a p-value, for example), and that no
cross-reference or sample-size count is stale. Neither audit pins every
cell of every table.
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
is settled by where it began, not by what the reading measured, though reaching
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
the kill rate produces no such separation. The crossing times themselves are Fig. S1, with the
laboratory-level tests this design does and does not support.


## Supplemental material

The supplemental file carries the full Materials and Methods, the analyses named above as supplementary text, and 26 supplemental tables. Of those, 9 belong to analyses reported in that file rather than in this article, and are cited there at the point where each is used.


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
| Evolved clones | *E. coli*, 126 clones | amikacin | MIC and persister fraction per clone | Zenodo 7550302 (25) | CC BY 4.0 |
| Concentration-by-time grid | *M. tuberculosis* | apramycin 1-128 ug/mL (amikacin arm not analysed) | 5 concentrations x 4 days x 3 replicates | figshare 26462791 | CC BY 4.0 |
| Analysed last, after the derivation was fixed | *E. coli*, hollow fibre | amoxicillin-clavulanate | 20 cultures, measured day-zero density, 100 uL plated | Nat Commun 2026 Source Data | CC BY 4.0 |

*Note.* Four carry the analysis and the fifth was analysed last, to test it. None was generated for this study. That fifth deposit was opened after every boundary and threshold was fixed: the headroom tool at 00:08 and the symbolic recovery of both boundary laws at 01:34 on 6 September 2026, against the deposit's arrival at 02:41 the same morning. The deposit entered in the same commit as the script that tests it, which git cannot order internally, so it is where reachability and identifiability were committed that dates the hold-out, not where the deposit arrived. This is an attestation and not a registration: the deposit had been public since its article appeared on 13 June 2026, so nothing outside this repository's own commit history evidences that it was not opened earlier, and a reader should weigh it accordingly. The other four were selected for the fields they carry, and that selection is not separately registered.


## References

1. World Health Organization. 2022. WHO consolidated guidelines on tuberculosis. Module 4: treatment — drug-susceptible tuberculosis treatment. World Health Organization, Geneva, Switzerland. https://iris.who.int/handle/10665/353829.

2. Brauner A, Fridman O, Gefen O, Balaban NQ. 2016. Distinguishing between resistance, tolerance and persistence to antibiotic treatment. Nat Rev Microbiol 14:320-330. https://doi.org/10.1038/nrmicro.2016.34.

3. Brauner A, Shoresh N, Fridman O, Balaban NQ. 2017. An experimental framework for quantifying bacterial tolerance. Biophys J 112:2664-2671. https://doi.org/10.1016/j.bpj.2017.05.014.

4. Balaban NQ, Helaine S, Lewis K, Ackermann M, Aldridge B, Andersson DI, Brynildsen MP, Bumann D, Camilli A, Collins JJ, Dehio C, Fortune S, Ghigo J-M, Hardt W-D, Harms A, Heinemann M, Hung DT, Jenal U, Levin BR, Michiels J, Storz G, Tan M-W, Tenson T, Van Melderen L, Zinkernagel A. 2019. Definitions and guidelines for research on antibiotic persistence. Nat Rev Microbiol 17:441-448. https://doi.org/10.1038/s41579-019-0196-3.

5. Harms A, Fino C, Sørensen MA, Semsey S, Gerdes K. 2017. Prophages and growth dynamics confound experimental results with antibiotic-tolerant persister cells. mBio 8:e01964-17. https://doi.org/10.1128/mBio.01964-17.

6. Cochran WG. 1950. Estimation of bacterial densities by means of the "most probable number". Biometrics 6:105. https://doi.org/10.2307/3001491.

7. Blodgett R. 2023. BAM appendix 2: most probable number from serial dilutions. Bacteriological analytical manual. US Food and Drug Administration, Silver Spring, MD. https://www.fda.gov/food/laboratory-methods-food/bam-appendix-2-most-probable-number-serial-dilutions.

8. Mann HB, Whitney DR. 1947. On a test of whether one of two random variables is stochastically larger than the other. Ann Math Stat 18:50-60. https://doi.org/10.1214/aoms/1177730491.

9. van Wijk RC, Lucía A, Sudhakar PK, Sonnenkalb L, Gaudin C, Hoffmann E, Dremierre B, Aguilar-Ayala DA, Dal Molin M, Rybniker J, de Giorgi S, Cioetto-Mazzabò L, Segafreddo G, Manganelli R, Degiacomi G, Recchia D, Pasca MR, Simonsson USH, Ramón-García S. 2023. Implementing best practices on data generation and reporting of *Mycobacterium tuberculosis* in vitro assays within the ERA4TB consortium. iScience 26:106411. https://doi.org/10.1016/j.isci.2023.106411.

10. van Wijk RC, Lucía Quintana A, Ramón-García S. 2023. *Mycobacterium tuberculosis* time kill assay data of the standardized protocol within the ERA4TB consortium. figshare. https://doi.org/10.6084/m9.figshare.19766083.v1.

11. Dubey V, Darlow C, Gerada A, Unsworth J, Sheth E, Reza N, Farrington N, Haldenby S, Warren D, Liu X, Howard A, Hope W. 2026. Molecular pharmacodynamics of amoxicillin-clavulanic acid for urinary tract infections caused by *Escherichia coli*. Nat Commun 17:7504. https://doi.org/10.1038/s41467-026-74323-2.

12. Dubey V, Darlow C, Gerada A, Unsworth J, Sheth E, Reza N, Farrington N, Haldenby S, Warren D, Liu X, Howard A, Hope W. 2026. Source Data to "Molecular pharmacodynamics of amoxicillin-clavulanic acid for urinary tract infections caused by *Escherichia coli*" (41467_2026_74323_MOESM4_ESM.xlsx). Nature Communications. https://doi.org/10.1038/s41467-026-74323-2.

13. Evangelopoulos D, Prosser G, Rodgers A, Dagg B, Khatri B, Bhagwat A, Gonzalo X, Kolyva A, Bertozzi G, Silva-Pereira TT, Gibbons N, Bhatt A, Sabharwal N, Perdigao J, Portugal I, Rodrigues C, Duarte R, Gomes M, Cirillo DM, McHugh TD. 2022. Data from: Comparative evaluation of viable count, molecular bacterial load and most probable number for the enumeration of Mycobacterium tuberculosis in murine tissue. University College London Research Data Repository. https://doi.org/10.5522/04/19175153.v2. Retrieved 2026-09-07.

14. Mukamolova GV, Turapov O, Malkin J, Woltmann G, Barer MR. 2010. Resuscitation-promoting factors reveal an occult population of tubercle bacilli in sputum. Am J Respir Crit Care Med 181:174-180. https://doi.org/10.1164/rccm.200905-0661OC.

15. Chengalroyen MD, Beukes GM, Gordhan BG, Streicher EM, Churchyard G, Hafner R, Warren R, Otwombe K, Martinson N, Kana BD. 2016. Detection and quantification of differentially culturable tubercle bacteria in sputum from patients with tuberculosis. Am J Respir Crit Care Med 194:1532-1540. https://doi.org/10.1164/rccm.201604-0769OC.

16. Saito K, Warrier T, Somersan-Karakaya S, Kaminski L, Mi J, Jiang X, Park S, Shigyo K, Gold B, Roberts J, Weber E, Jacobs WR Jr, Nathan CF. 2017. Rifamycin action on RNA polymerase in antibiotic-tolerant Mycobacterium tuberculosis results in differentially detectable populations. Proc Natl Acad Sci U S A 114:E4832-E4840. https://doi.org/10.1073/pnas.1705385114.

17. National Committee for Clinical Laboratory Standards. 1999. Methods for determining bactericidal activity of antimicrobial agents; approved guideline. NCCLS document M26-A. National Committee for Clinical Laboratory Standards, Wayne, PA. ISBN 1-56238-384-1.

18. Vilchèze C, Jacobs WR Jr. 2007. The mechanism of isoniazid killing: clarity through the scope of genetics. Annu Rev Microbiol 61:35-50. https://doi.org/10.1146/annurev.micro.61.111606.122346.

19. Campbell EA, Korzheva N, Mustaev A, Murakami K, Nair S, Goldfarb A, Darst SA. 2001. Structural mechanism for rifampicin inhibition of bacterial RNA polymerase. Cell 104:901-912. https://doi.org/10.1016/S0092-8674(01)00286-0.

20. March VFA, Mchedlishvili K, Goig GA, Maghradze N, Avaliani T, Aspindzelashvili R, Avaliani Z, Kipiani M, Tukvadze N, Jugheli L, Bouaouina S, Doetsch A, Kalkan S, Reinhardt M, Gagneux S, Borrell S. 2025. Within-host evolution of drug tolerance in *Mycobacterium tuberculosis*. bioRxiv 2025.07.29.667394; preprint, not peer reviewed. https://doi.org/10.1101/2025.07.29.667394.

21. Michael CT, Budak M, Maiello P, Kracinovsky K, Rodgers M, Tomko J, Lin PL, Flynn J, Linderman JJ, Kirschner D. 2025. Rankings of tuberculosis antibiotic treatment regimens are sensitive to spatial scale, detection limit, and initial host bacterial burden. J Theor Biol. https://doi.org/10.1016/j.jtbi.2025.112176.

22. ASTM International. 2023. E2315-23: Standard Guide for Assessment of Antimicrobial Activity Using a Time-Kill Procedure. ASTM International, West Conshohocken, PA. https://doi.org/10.1520/E2315-23.

23. Vijay S, Bao NLH, Vinh DN, Nhat LTH, Thu DDA, Quang NL, Trieu LPT, Nhung HN, Ha VTN, Thai PVK, Ha DTM, Lan NH, Caws M, Thwaites GE, Javid B, Thuong NT. 2024. Supplementary file 2 to "Rifampicin tolerance and growth fitness among isoniazid-resistant clinical *Mycobacterium tuberculosis* isolates from a longitudinal study" (elife-93243-supp2-v1.xlsx). eLife. https://doi.org/10.7554/eLife.93243.

24. Rabodoarivelo MS, Hoffmann E, Gaudin C, Aguilar-Ayala DA, Galizia J, Sonnenkalb L, Dal Molin M, Cioetto-Mazzabò L, Degiacomi G, Recchia D, Rybniker J, Manganelli R, Pasca MR, Ramón-García S, Lucía A. 2025. Protocol to quantify bacterial burden in time-kill assays using colony-forming units and most probable number readouts for *Mycobacterium tuberculosis*. STAR Protoc 6:103643. https://doi.org/10.1016/j.xpro.2025.103643.

25. Windels EM, Cool L, Persy E, Swinnen J, Matthay P, Van den Bergh B, Wenseleers T, Michiels J. 2024. Antibiotic dose and nutrient availability differentially drive the evolution of antibiotic resistance and persistence. ISME J 18:wrae070. https://doi.org/10.1093/ismejo/wrae070.

26. Windels EM, Cool L, Persy E, Swinnen J, Matthay P, Van den Bergh B, Wenseleers T, Michiels J. 2024. Data supporting "Antibiotic dose and nutrient availability differentially drive the evolution of antibiotic resistance and persistence". Zenodo. https://doi.org/10.5281/zenodo.7550302.

27. Kaur P, Ramya VK, Naveenkumar CN, Bharathkumar K, Singh M, Hobbie SN, Shandil RK, Narayanan S. 2024. Apramycin kills replicating and non-replicating *Mycobacterium tuberculosis*. Front Trop Dis 5:1413211. https://doi.org/10.3389/fitd.2024.1413211.

28. Kaur P. 2024. Apramycin kills replicating and non-replicating *Mycobacterium tuberculosis* — raw data. figshare. https://doi.org/10.6084/m9.figshare.26462791.v1.

29. Clinical and Laboratory Standards Institute. 2024. Methods for dilution antimicrobial susceptibility tests for bacteria that grow aerobically, 12th ed. CLSI standard M07. Clinical and Laboratory Standards Institute, Wayne, PA.

30. Clinical and Laboratory Standards Institute. 2026. Performance standards for antimicrobial susceptibility testing, 36th ed. CLSI supplement M100. Clinical and Laboratory Standards Institute, Wayne, PA.

31. Tobin J. 1958. Estimation of relationships for limited dependent variables. Econometrica 26:24. https://doi.org/10.2307/1907382.

32. Beal SL. 2001. Ways to fit a PK model with some data below the quantification limit. J Pharmacokinet Pharmacodyn 28:481-504. https://doi.org/10.1023/A:1012299115260.

33. Rubin DB. 1987. Multiple imputation for nonresponse in surveys. John Wiley & Sons, New York, NY. https://doi.org/10.1002/9780470316696.

34. McCullagh P. 1980. Regression models for ordinal data. J R Stat Soc Series B Stat Methodol 42:109-127. https://doi.org/10.1111/j.2517-6161.1980.tb01109.x.

35. Brant R. 1990. Assessing proportionality in the proportional odds model for ordinal logistic regression. Biometrics 46:1171-1178.

36. Peterson B, Harrell FE Jr. 1990. Partial proportional odds models for ordinal response variables. J R Stat Soc Ser C Appl Stat 39:205. https://doi.org/10.2307/2347760.

37. Turnbull BW. 1976. The empirical distribution function with arbitrarily grouped, censored and truncated data. J R Stat Soc Series B Stat Methodol 38:290-295. https://doi.org/10.1111/j.2517-6161.1976.tb01597.x.

38. Kaplan EL, Meier P. 1958. Nonparametric estimation from incomplete observations. J Am Stat Assoc 53:457-481. https://doi.org/10.1080/01621459.1958.10501452.

39. Cox DR. 1972. Regression models and life-tables. J R Stat Soc Series B Stat Methodol 34:187-202. https://doi.org/10.1111/j.2517-6161.1972.tb00899.x.

40. Field CA, Welsh AH. 2007. Bootstrapping clustered data. J R Stat Soc Series B Stat Methodol 69:369-390. https://doi.org/10.1111/j.1467-9868.2007.00593.x.

41. Schoenfeld D. 1982. Partial residuals for the proportional hazards regression model. Biometrika 69:239-241. https://doi.org/10.1093/biomet/69.1.239.

42. Grambsch PM, Therneau TM. 1994. Proportional hazards tests and diagnostics based on weighted residuals. Biometrika 81:515-526. https://doi.org/10.1093/biomet/81.3.515.

43. Efron B. 1979. Bootstrap methods: another look at the jackknife. Ann Stat 7:1-26. https://doi.org/10.1214/aos/1176344552.

44. Brown LD, Cai TT, DasGupta A. 2001. Interval estimation for a binomial proportion. Stat Sci 16:101-133. https://doi.org/10.1214/ss/1009213286.

45. Imai K, Keele L, Yamamoto T. 2010. Identification, inference and sensitivity analysis for causal mediation effects. Stat Sci 25:51-71. https://doi.org/10.1214/10-STS321.

46. Baron RM, Kenny DA. 1986. The moderator-mediator variable distinction in social psychological research: conceptual, strategic, and statistical considerations. J Pers Soc Psychol 51:1173-1182. https://doi.org/10.1037/0022-3514.51.6.1173.

47. Benjamini Y, Hochberg Y. 1995. Controlling the false discovery rate: a practical and powerful approach to multiple testing. J R Stat Soc Series B Stat Methodol 57:289-300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x.

48. Harris CR, Millman KJ, van der Walt SJ, Gommers R, Virtanen P, Cournapeau D, Wieser E, Taylor J, Berg S, Smith NJ, Kern R, Picus M, Hoyer S, van Kerkwijk MH, Brett M, Haldane A, del Río JF, Wiebe M, Peterson P, Gérard-Marchant P, Sheppard K, Reddy T, Weckesser W, Abbasi H, Gohlke C, Oliphant TE. 2020. Array programming with NumPy. Nature 585:357-362. https://doi.org/10.1038/s41586-020-2649-2.

49. Virtanen P, Gommers R, Oliphant TE, Haberland M, Reddy T, Cournapeau D, Burovski E, Peterson P, Weckesser W, Bright J, van der Walt SJ, Brett M, Wilson J, Millman KJ, Mayorov N, Nelson ARJ, Jones E, Kern R, Larson E, Carey CJ, Polat İ, Feng Y, Moore EW, VanderPlas J, Laxalde D, Perktold J, Cimrman R, Henriksen I, Quintero EA, Harris CR, Archibald AM, Ribeiro AH, Pedregosa F, van Mulbregt P, SciPy 1.0 Contributors. 2020. SciPy 1.0: fundamental algorithms for scientific computing in Python. Nat Methods 17:261-272. https://doi.org/10.1038/s41592-019-0686-2.

50. McKinney W. 2010. Data structures for statistical computing in Python. Proceedings of the 9th Python in Science Conference 56-61. https://doi.org/10.25080/Majora-92bf1922-00a.

51. Seabold S, Perktold J. 2010. Statsmodels: econometric and statistical modeling with Python. Proceedings of the 9th Python in Science Conference 92-96. https://doi.org/10.25080/Majora-92bf1922-011.

52. Davidson-Pilon C. 2019. lifelines: survival analysis in Python. J Open Source Softw 4:1317. https://doi.org/10.21105/joss.01317.

53. Vijay S, Bao NLH, Vinh DN, Nhat LTH, Thu DDA, Quang NL, Trieu LPT, Nhung HN, Ha VTN, Thai PVK, Ha DTM, Lan NH, Caws M, Thwaites GE, Javid B, Thuong NT. 2024. Rifampicin tolerance and growth fitness among isoniazid-resistant clinical *Mycobacterium tuberculosis* isolates from a longitudinal study. Elife 13:RP93243. https://doi.org/10.7554/eLife.93243.

54. Piranfar V. 2026. Analysis code, audit scripts and headroom tool for "Rifampicin tolerance classification is bounded by assay detection floor among clinical Mycobacterium tuberculosis isolates". GitHub. https://github.com/piranfar/detection-floor-tolerance-endpoints.

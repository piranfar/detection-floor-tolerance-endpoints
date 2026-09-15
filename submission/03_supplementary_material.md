# Supplemental material

**The detection floor bounds tolerance endpoints in Mycobacterium tuberculosis**

Vahhab Piranfar

---

## Supplementary text

### Extended background for the Introduction

*Material held back from the article for length. It is reported here rather than dropped, because each paragraph answers a question a reader of that section may reasonably ask.*

The bound is already in the papers that defined the assays. Vijay and colleagues,
introducing the most-probable-number MDK for rifampicin — a count read off a
dilution series rather than off colonies on a plate — treated an MDK99.99 longer
than ten days as high tolerance beyond the **time** window of the assay, not as a
statement about the count floor (1). In the 217-isolate classification that
follows from that assay they report that MDK99.99 at 15 days of recovery could be
calculated for only 22 of 209 isolates and that the rest lay, in their words,
"beyond the assay limits" (2). The ERA4TB consortium requires below- and
above-quantification-limit flags together with the limit of quantification, and
notes that pharmacometric models can use those flags (3); the same
six-laboratory comparison then excluded both from its numerical analysis. Their
2025 protocol states the geometry of the pipette explicitly: a 2.5 µL drop has a
limit of detection above 2.6 log10 CFU/mL, and a lower limit requires a larger
plated volume (4). Independently, a 2025 pharmacokinetic-pharmacodynamic
analysis of hollow-fibre CFU series showed that censoring counts below 10 CFU —
recording them only as "below the floor", with the true value unknown — biases
regimen ranking (5), and a within-host tuberculosis tolerance study chose a
shallower MDK threshold specifically so that more isolates could enter the
analysis (6).

The requirement is older still, and it is quantitative: NCCLS M26-A ties the
plated volume to the endpoint, and separately requires the smallest accurately
detectable count to be established by serial dilution of a known inoculum
(7). The endpoint has since moved and the rule did not travel with it. The
persistence field's own consensus guideline, which catalogues at length what else
can go wrong with a time-kill assay, raises neither the limit of detection nor
the plated volume nor how deep a reduction the assay can report (8).

This is testable rather than arguable, because one published deposit assigns the
tolerance phenotype itself. Vijay and colleagues (2, 9) scored 217 clinical
*Mycobacterium tuberculosis* isolates as having low, medium or high tolerance to
rifampicin, and deposited alongside each call the starting most probable number,
the growth rate, the isoniazid susceptibility and the killing readings the call
was built from. The classification, the inputs to it, and the assay geometry that
bounds it are all in the same file.

Two of the claims this arithmetic supports are not testable and should not be
read as though they were. If the last reading sits at the floor, the recorded
reduction cannot exceed *h*, because a deeper one would require a count below
*L*. And the recorded fraction is then *L*/*N*₀, a monotone decreasing function
of *N*₀, so its rank correlation with *N*₀ is
−1 whatever the numbers are, including random ones. Both follow from the
definition of a censored reading, and neither is evidence about a drug.

What is testable is what happens when one sample is plated at two volumes under a
fixed class threshold. If both readings sit at their own floors the labels are
*L*₁/*N*₀ and *L*₂/*N*₀, and they differ only when those two fractions fall on
opposite sides of the cut — which is again arithmetic. The empirical quantity is
how often a real experiment lands in that window. It could be none of the time.

### Extended background for the Discussion

*Material held back from the article for length. It is reported here rather than dropped, because each paragraph answers a question a reader of that section may reasonably ask.*

What sits beneath the floor is the one thing a plate cannot report, and it has
been measured. Evangelopoulos and colleagues counted the same mouse lungs three
ways — colony count, a molecular bacterial load from 16S rRNA, and a most
probable number — on their way to a different question (10). Under the
deepest regimens the colony count reads zero in every animal. In three arms, 18
lungs in all, the plate declared every lung sterile while the most probable
number on that same tissue ran from 1 450 to 18 700 per lung. The molecular load
can be dismissed as nucleic acid outliving its owner. The most probable number
cannot, because it is a culture, and growth in a dilution series requires an
organism that is alive and culturable. Those lungs held thousands of viable
bacilli, and the plate that reported them sterile could not see them. This is
the region a relapse comes from, and in the mouse model used to decide which
regimens enter clinical trials it is the region a colony count is blind to.

That is also where the counts feeding regimen selection are taken. A model
published as a preprint while this paper was in preparation predicts relapse in
the murine model across nine datasets, 58 regimens and 2 239 relapse
observations, reaching an area under the receiver operating characteristic curve
of 0.90 on its final external validation (11). Its eight predictors include
the fall in lung CFU from baseline at days 14 and 28, the fall in the ribosomal RNA (ribonucleic acid)
synthesis ratio at day 14, the presence of an oxazolidinone, and four
experimental covariates. Removing either biomarker costs performance. What the
authors show is that the loss from dropping the RS ratio can be recovered by
adding model-estimated coefficients for the sterilising contribution of each drug
— a substitution they license only for compounds already characterised, since
those coefficients need prior long-term outcome data, and expressly not for the
novel ones the model exists to rank.

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
leaving it to be noticed.

A reader may object that this runs backwards. Dropping below the limit of
detection is what a *susceptible* population does; how can it make an isolate
look more tolerant? The objection is a fair one, and it is answered by
separating two endpoints that the literature reports side by side.

A duration endpoint asks when a fixed depth was reached. An isolate without the
room that depth requires cannot reach it under any drug effect whatever, so what
the file records is not a short duration but no duration at all: the isolate is
censored at the end of observation, which is the top of the scale and therefore
the most tolerant value it can take. The isolates that could not demonstrate the
endpoint are, without exception, the ones recorded as having failed to reach
it.

A class endpoint asks how far the population fell by a fixed time, and there the
arithmetic does not merely preserve the direction — it inverts it. Once the
final reading sits on the floor the recorded fraction is *L*/*N₀*, and with *L*
fixed a *lower* starting density yields a *larger* recorded fraction. A larger
surviving fraction is a higher tolerance class, not a lower one. That is why the
eighteen isolates ending on the same floor value split twelve low and six medium
in the order their inocula do: the recorded survival and the starting density are
the same quantity.

Neither route asks anyone to mistake a sterile culture for a surviving one. In
the first the assay returns no endpoint. In the second it returns the floor
divided by the inoculum. What is read as biology is, in both cases, a property
of the measurement.

Where the inoculum is set deliberately rather than by clinical accident, the
same arithmetic operates and can be measured rather than inferred. In more than
a third of cross-laboratory comparisons the flask in which the population fell
faster was the one that crossed below the assay floor later, and the
distance-over-rate criterion accounts for three in five of them. Resampling
whole laboratories rather than pairs leaves that rate poorly determined — 3.0 to
72.4 per cent — so what the deposit establishes is the mechanism and not the
rate.

The variance decomposition sets the size of the effect, and it will not carry
more than that. At the flask level the rate term takes the larger share in every
arm examined, but the flasks are three to a laboratory and the ordering does not
survive being asked at the laboratory level, so this paper does not assert it.
What the decomposition does establish is that the two terms are of comparable
size. A crossing time is not mostly a measurement of the inoculum, and it is not
mostly a measurement of the drug either. It is a mixture in which the inoculum is
a large minority — enough to reverse the ranking of two populations in more than
a third of comparisons, which is the number that matters to anyone choosing
between two compounds, and not enough to license the claim that the endpoint
measures the starting culture.
We agree with van Wijk and colleagues wherever the two analyses overlap. They
noticed the spread in starting densities themselves. They report that the burden
at the start varied between laboratories while the net effect of the drug varied
less (3); that conclusion is theirs, and it anticipates part of ours. Where
we part company is in what they did with readings that fell outside the
quantification limits: they left them out of the numbers. That is a defensible
way to report an assay. It also closes off the question this paper asks, because
those are exactly the readings a duration is built from.

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
the strongest between-laboratory evidence the deposit holds.

The laboratories did not all count their starting density on the same day. Only
institutes C and D deposit a day-zero reading for the treated flasks. A, B, E and
F deposit day one, and by day one the ten-times-MIC arms have already lost
between 0.7 and 2.4 log10. For four of the six laboratories, then, the number we
are calling the exposure has some killing baked into it. We re-ran the whole
comparison on a day-one exposure for every laboratory. The ordering, the area
under the curve and the laboratory-level p all stayed the same, so the conclusion
is robust to it. The mismatch is real all the same, and we report it rather than
smooth it over.

In the six-laboratory exercise, starting density and laboratory are close to the
same variable. 87.0 per cent of the variance in flask-level starting density lies
between laboratories rather than within them. Taken over every flask that
deposits an early density, treated and untreated arms together, the laboratory
means span 3.62
log10, against a median within-laboratory standard deviation of 0.43. Adding
starting density to a model that already knows which laboratory a flask came from
is therefore not separating two covariates. It is closer to swapping a label for
a number carrying much the same information. Telling the two apart needs a design
that fixes the inoculum across laboratories.

This is not an aspiration. One study already does it. A murine preventive-therapy
experiment writes its lower limit of detection into the deposited workbook once
on every sheet, separately for each agar type, and separately for individual mice
where the lower limit differed between them: 0.78 log10 CFU per lung on plain and
hygromycin agar, 0.54 on thiophenecarboxylic acid hydrazide agar, with the plated
volume stated beside it (12). That is better practice than anything else in
this corpus. The article reporting the experiment states none of it — a full-text
search returns no occurrence of "limit of detection" or of either value. So the
number is not missing from the science. It is missing from the paper, and a
reader who never opens the supplementary spreadsheet cannot know an endpoint was
bounded. What we are asking for is one sentence in a methods section, and
somebody has already done all the work that sits behind it.

The mirror image is a deposit whose modelling table carries a column named
`CFU_LOD`, and that column is empty in all 272 rows (13). Somebody designed
the field, declared it numeric, and never filled it in; nor does a detection
limit appear in any of the eight analysis scripts deposited beside it. Put the
two cases together and the diagnosis is not carelessness. The assay floor *L* is
measured. Sometimes it is written down to a standard higher than anyone asks for.
It then falls out of the record between the bench and the reader — off the end of
a spreadsheet, or into a column nobody completed.

### Text S1. The flask that fell faster often crossed the floor later

Take two flasks in the same treatment arm from different laboratories and compare
them. Across 191 such pairs — with 45 further pairs that the censoring could not
settle, which are excluded rather than imputed — **66 pairs — 34.6 per cent — are
inversions**: the flask in which the population fell faster crossed below the
assay floor later (Table S18). Restrict to pairs whose rates differ by more than
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
straddles a half in all three (Table S18). What survives is the weaker and
sufficient statement: the distance term is a large share of the variation
available to move a crossing time, and the two terms are of comparable size. <!--supp-->

The fourth treated arm, moxifloxacin at
one times the inhibitory concentration, cannot be decomposed at all: five of six
laboratories record net growth there, and only one flask in the arm returns a
positive fitted rate, so there is no spread in the rate to divide (Table S18). A
crossing time is therefore not mainly an inoculum measurement. It is a mixture, in
which the inoculum is a large minority contribution — large enough to reverse the
ranking in more than a third of comparisons, and not large enough to justify
treating the endpoint as an inoculum readout in general.

### Text S2. How much drug it takes and how long it takes are two different things

The framework that defines these two measures takes it as given that they are
separate (Brauner et al. 2016) (14). The deposits do not prove it. They bound
how far from separate the two could be, which is weaker and more honest. The
217-isolate file supports 24 comparisons of the two: how much drug it takes to
stop growth against how long it takes to kill. All 24 are corrected together.
Testing that many things at once throws up hits by chance, so the Benjamini–Hochberg
thresholds in Table S19 — the standard correction for a family of tests — are set
against 24, not against the size of any one subgroup. Four are significant before
correction, where 1.2 are expected by chance, and none survives it (Fig. S2,
Table S19). All four point the wrong way: a higher inhibitory concentration goes
with a *shorter* killing time, which is not the direction a shared mechanism
predicts. And they cluster at the deepest endpoint — the one Section 1 shows is
compromised. Across all 24 tests the weakest correlation this design could have
detected runs 0.14 to 0.25 depending on the subgroup; the six strongest, which
Table S19 lists, span 0.14 to 0.18.

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

Ask the same question of 126 evolved clones sharing one ancestor (15, 16) and
the answer is ρ = +0.043 (p = 0.63), against the 0.175 this sample size could
have detected. Independence holds inside every nutrient group separately.
Splitting by nutrient is not optional there. The concentration written on the
flask is not the same exposure in every group: at 25 µg/mL, that one figure is
anywhere from 0.55 to 9.47 times the inhibitory concentration that population had
evolved to, and it falls on both sides of it (Table S20).

---

### Extended results for article section 4: The label tracks how fast an isolate grows, and its link to resistance cannot be separated from the inoculum

*Material held back from the article for length. It is reported here rather than dropped, because each paragraph answers a question a reader of that section may reasonably ask.*

The label has three levels in a fixed order — low, then medium, then high — and
we model it as such. Scoring the levels 0, 1 and 2 and fitting a straight line
would assert that the step from low to medium is the same size as the step from
medium to high, and nothing establishes that. Associations are therefore
reported as odds ratios from proportional-odds ordinal logistic regression, a
fit for ranked outcomes that does not assume the steps between ranks are equal.
That fit makes an assumption of its own — that a single odds ratio serves both
cut points — and we tested it rather than assuming it (Methods; Table S4).

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
unaffected.

These 217 isolates are not 217 independent observations. Forty-three are
follow-up isolates taken during treatment from patients who also gave a baseline
isolate, so up to 86 rows sit in clusters of two. But the deposit carries no
patient identifier: Archive and Sample-ID are unique to each row, and none of the
48 columns repeats the way a patient key would have to. The pairing cannot be
recovered, so no standard error can be clustered on the true grouping, and we do
not pretend otherwise. What is available is the exact substitute, a baseline-only
stratum in which every isolate is from a different patient by construction
(Time_point = 0M, n = 167 at 15 days).

Why they seed lower is not established here, and the obvious explanation fails:
resistant isolates do not grow significantly more slowly in this deposit (median
time to OD 0.4 of 19 against 17, p = 0.24), and 85 of them carry *katG* S315X,
the mutation that predominates clinically precisely because it is close to
fitness-neutral — it costs the bacterium almost nothing to carry (17, 18).
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
all and Table S21 prints none.

The other two are the isoniazid and rifampicin MICs, and their missingness runs
the other way: they are recorded for all 119 susceptible isolates and for 67 of
84 resistant ones, so what is absent sits inside the exposed group rather than
across the contrast. That does not make them confounders. The isoniazid MIC
separates the two groups completely in this deposit — no resistant isolate
overlaps any susceptible one — so it is the exposure measured on a graded scale
rather than something to adjust the exposure for. The fit says so: the standard
error on the resistance coefficient inflates from 0.103 to 0.181, and the
complete case drops 17 resistant isolates and no susceptible one, leaving 186
rows against 203. It is also the second-largest movement in Table S21, and it runs
the wrong way for a confounding explanation: with the isoniazid MIC in the model
the seeding gap grows from −0.85 to −0.96, an amplification of 13 per cent rather
than an attenuation. The rifampicin MIC, which does not separate the groups,
moves it by less than half a per cent.

The remaining two are missing at rates unrelated to susceptibility and can be
used: the growth proxy and months on treatment. Adjusting for either leaves the
coefficient at −0.81 or −0.82 against an unadjusted −0.85, an attenuation of at
most five per cent (Table S21). The seeding gap is therefore more robust than the
earlier sweep suggested, not less. The file records no referring site and no
processing batch, so those cannot be tested at all. The association between
resistance and a low starting inoculum is real, large and unexplained, and we
record it as such.

### Extended results for article section 5: One written protocol does not give every laboratory the same depth to look down

*Material held back from the article for length. It is reported here rather than dropped, because each paragraph answers a question a reader of that section may reasonably ask.*

The starting densities in Table S6 need their basis stated before they are used.
Each is the mean of quantified readings at day 0 or day 1 at the 100 µL plating,
pooled over that laboratory's arms. Institute A deposits no day-zero reading at
all, and among treated flasks only C and D do, so for four of the six the figure
rests partly on readings taken after twenty-four hours of drug — by which point
the ten-times-MIC arms have already lost between 0.7 and 2.4 log10. A day-zero
comparison across all six is therefore not available, and the check that is
available runs the other way: re-running the whole analysis on a day-one exposure
for every laboratory leaves the ordering, the area under the curve and the
laboratory-level exact test unchanged.

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
last visit.

That split is a property of the plating, not of the laboratories. Counting a
crossing on **any** of the four platings gives 48 of the same 72 treated flasks,
and every laboratory records at least one — D six of its twelve, E one, F ten.
The two counts are the same fact seen at two sensitivities, and they are exactly
what this paper is about: a duration endpoint is defined against a floor, and the
floor is a choice. The analysis keeps the single most sensitive plating so that
the endpoint means the same thing everywhere, and reports here what the other
choice would have shown.

Starting density separates the flasks that ever crossed from those that never did
with an area under the curve of 0.974. That figure is a description, and it is
quoted without a p-value on purpose. The comparison looks like 67 flasks, but it
is three laboratories against three, and the between-laboratory evidence in this
deposit is six clusters throughout; the Limitations set out what that permits and
what it forbids. In short: the exact laboratory-level test returns 0.10, which is
the smallest value the design can return, and once the treatment arm is held
fixed there is no within-laboratory comparison left to fall back on.

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
in this design. It is not evidence that one explains the other.

Where an interval is quoted from that fit it is a cluster bootstrap and not the
model's own. For the starting-density coefficient the laboratory-clustered
interval is −1.11 to −0.51, half again as wide as the model's −0.91 to −0.48 and
two and a half times the flask-clustered −0.81 to −0.56; quoting the model's
interval is not conservative, it is wrong in an unpredictable direction. For the
laboratory contrasts the laboratory bootstrap is the wrong instrument, since it
keeps each laboratory's flasks together and the contrast barely moves, so the
flask-clustered interval is quoted there instead. The crossings behind each
laboratory's coefficient are also worth stating plainly: 43 of 48 series in
institute C against 1 of 48 in institute E.

Killing here is not sustained, and this is stronger than a caveat about
individual flasks. Take the 64 treated series carrying at least three quantified
readings at the most sensitive plating volume. In 48 of them the final step is
not a decline, and 44 end more than one log10 above their own lowest reading,
with a median rebound of 2.17 log10 and a largest of 5.54. Seventeen of the 32
flasks that fell below the floor at the most sensitive plating — the 29 treated
flasks above and three untreated ones — were detectable again at a later visit,
14 of them in treated arms.

Across all four platings, 84 of the 140 series that cross return above the floor,
60 per cent, and the return is quick: a median of four days, with 45 per cent
back within three. Those 360 series come from 90 flasks, four platings each, so
they are not 360 independent observations; counted by flask, 53 of the 90 contain
a crossing series — the 48 treated flasks above and five untreated ones — and 42
of those contain a returning one. A crossing below the assay floor in this
deposit is therefore usually a transient rather than an endpoint, which is a
further reason it summarises less than the trajectory that produced it.

Killing itself is real and dose-dependent: at one times the inhibitory
concentration five of six laboratories record net growth under moxifloxacin,
between −0.047 and −0.214 log10 per day, and at ten times all six record net
decline.

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
assumes: one crossing that holds (Table S22). Two hundred and twenty never cross
at all, 65 cross and return, and 19 oscillate more than once.

The second is that the crossing time is never observed. It lies between the last
visit above the floor and the first visit below it, and the naive treatment pins
it to the later end, which biases every duration late by construction rather than
merely imprecisely. Fitted as interval-censored data — the crossing recorded as
lying somewhere inside a window rather than at a point (19) — at the most
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
the depths that matter.

### Extended results for article section 6: The same boundaries hold in an experiment the framework never saw

*Material held back from the article for length. It is reported here rather than dropped, because each paragraph answers a question a reader of that section may reasonably ask.*

That was true of the search as described. It is no longer true of the analysis
repository, which now holds 40 ingested deposits. Of those, 17 permit the
boundaries to be computed once the floor is established on the same tiers this
paper uses for its own: stated by the depositor, derived from a recorded plated
volume, or inferred from a pile-up of counts on a plate-plausible value. Across
those, the condition the boundaries imply — that no series may present as a
measurement a reduction deeper than its own floor allows — holds in 2 210 of
2 210 series in seven species. Those deposits are described in the data release
rather than here, because none was held out.

## Supplementary figures

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

**Figure S2. Resistance and tolerance occupy separate axes, in two designs.**
(**A**) All 24 comparisons between the concentration axis and the duration axis
that the 217-isolate file supports, each against the Benjamini–Hochberg critical
value it would have to beat. Amber marks the four reaching nominal significance;
none survives. (**B**) The censoring behind them: the fraction of isolates at the
assay ceiling rises with endpoint depth, and the nominal hits concentrate where
censoring is heaviest. (**C**) The same question in 126 evolved *E. coli* clones,
by nutrient stratum.

## Supplementary methods


## Supplementary tables

**Table S1.** What is actually known about the assay floor in each deposit, and the rule that follows from it. A floor derived from a recorded plated volume is a point mass: one colony in that volume, no inference required. A floor inferred from a pile-up on a most-probable-number rung carries a posterior over the rungs at or below the observed minimum, and the 95 per cent support is quoted. Where no floor is evidenced at all, or where the support spans more than one log10, the observability labels of Section 3 are refused rather than reported -- a label is only as good as the floor it is computed against.

| Deposit | Verdict | Floor used | 95% support | Span (log10) | Refuse observability labels |
| --- | --- | ---: | ---: | ---: | ---: |
| Vijay 2024, clinical isolates (MPN per mL) | INFERRED | 23 | [9.2, 23.0] | 0.398 | no |
| ERA4TB, 100 uL plated (CFU per mL) | DERIVED | 10 | point mass | 0.000 | no |
| ERA4TB, 10 uL plated (CFU per mL) | DERIVED | 100 | point mass | 0.000 | no |
| ERA4TB, 2.5 uL plated (CFU per mL) | DERIVED | 400 | point mass | 0.000 | no |
| Kaur 2024, apramycin grid (log10 CFU per mL) | NONE | - | - | - | yes |
| Windels 2024, evolved clones (surviving fraction) | NONE | - | - | - | yes |
| Dubey 2026, hollow fibre (CFU per mL) | DERIVED | 10 | point mass | 0.000 | no |

**Table S2.** Every analysis set in this paper, and the exclusion that produced it. The manuscript quotes a dozen different denominators, each correct for its own analysis; this is where a reader checks which is which. The MDR tolerance label is a fourth, unordered category and is dropped wherever an ordered outcome is fitted; the growth proxy is missing for one isolate; and five treated flasks in the six-laboratory deposit carry no usable starting density, which is why a comparison over 72 flasks is reported on 67. Whether these exclusions are plausibly ignorable is tested in Table S16. The last rows of each block cover sets counted in units other than isolates or flasks -- pairs, flags, cells, readings -- because a reader meeting one of those figures in the text needs somewhere to look it up too.

| Deposit | Panel | Stratum | Stage | n | Excluded here |
| --- | --- | --- | --- | ---: | ---: |
| Vijay clinical | 15-day | all isolates | rows in the deposit | 217 | - |
| Vijay clinical | 15-day | all isolates | tolerance label present | 217 | - |
| Vijay clinical | 15-day | all isolates | label is Low, Medium or High (drops 'MDR') | 203 | -14 |
| Vijay clinical | 15-day | all isolates | starting and day-5 readings present | 203 | - |
| Vijay clinical | 15-day | all isolates | susceptibility is IS or IR | 203 | - |
| Vijay clinical | 15-day | all isolates | growth proxy present (association family) | 202 | -1 |
| Vijay clinical | 15-day | baseline only (0M) | rows in the deposit | 174 | - |
| Vijay clinical | 15-day | baseline only (0M) | tolerance label present | 174 | - |
| Vijay clinical | 15-day | baseline only (0M) | label is Low, Medium or High (drops 'MDR') | 168 | -6 |
| Vijay clinical | 15-day | baseline only (0M) | starting and day-5 readings present | 168 | - |
| Vijay clinical | 15-day | baseline only (0M) | susceptibility is IS or IR | 168 | - |
| Vijay clinical | 15-day | baseline only (0M) | growth proxy present (association family) | 167 | -1 |
| Vijay clinical | 60-day | all isolates | rows in the deposit | 217 | - |
| Vijay clinical | 60-day | all isolates | tolerance label present | 211 | -6 |
| Vijay clinical | 60-day | all isolates | label is Low, Medium or High (drops 'MDR') | 197 | -14 |
| Vijay clinical | 60-day | all isolates | starting and day-5 readings present | 197 | - |
| Vijay clinical | 60-day | all isolates | susceptibility is IS or IR | 197 | - |
| Vijay clinical | 60-day | all isolates | growth proxy present (association family) | 196 | -1 |
| Vijay clinical | 60-day | baseline only (0M) | rows in the deposit | 174 | - |
| Vijay clinical | 60-day | baseline only (0M) | tolerance label present | 168 | -6 |
| Vijay clinical | 60-day | baseline only (0M) | label is Low, Medium or High (drops 'MDR') | 162 | -6 |
| Vijay clinical | 60-day | baseline only (0M) | starting and day-5 readings present | 162 | - |
| Vijay clinical | 60-day | baseline only (0M) | susceptibility is IS or IR | 162 | - |
| Vijay clinical | 60-day | baseline only (0M) | growth proxy present (association family) | 161 | -1 |
| Vijay clinical | 15-day | other sets quoted | isolates with a starting density | 217 | - |
| Vijay clinical | 60-day | other sets quoted | isolates with a starting density | 210 | -7 |
| Vijay clinical | 15-day | concentration-duration family | all isolates with an inhibitory concentration | 193 | - |
| Vijay clinical | 60-day | concentration-duration family | all isolates with an inhibitory concentration | 187 | - |
| Vijay clinical | 15-day | concentration-duration family | INH-susceptible with one | 119 | - |
| Vijay clinical | 60-day | concentration-duration family | INH-susceptible with one | 117 | - |
| Vijay clinical | 15-day | concentration-duration family | baseline only with one | 162 | - |
| Vijay clinical | 60-day | concentration-duration family | baseline only with one | 156 | - |
| ERA4TB six-laboratory | - | - | readings in the file | 2775 | - |
| ERA4TB six-laboratory | - | - | excluding inoculum controls | 2751 | -24 |
| ERA4TB six-laboratory | - | - | flasks (institute x arm x replicate) | 90 | - |
| ERA4TB six-laboratory | - | - | treated flasks | 72 | -18 |
| ERA4TB six-laboratory | - | - | treated flasks with a usable starting density | 67 | -5 |
| ERA4TB six-laboratory | - | - | laboratory-by-arm cells | 30 | - |
| ERA4TB six-laboratory | - | - | cells with a fitted kill rate | 29 | -1 |
| ERA4TB six-laboratory | - | - | series under the plating key (flasks x 4 platings) | 360 | - |
| ERA4TB six-laboratory | - | - | treated series | 288 | -72 |
| ERA4TB six-laboratory | - | - | cross-laboratory pairs in the same arm | 191 | - |
| ERA4TB six-laboratory | - | derived units | treated series with a quantified day-0 or day-1 reading in their own plating | 262 | -26 |
| ERA4TB six-laboratory | - | derived units | of those, not already below their own floor at day zero (the descriptive Cox set) | 261 | -1 |
| ERA4TB six-laboratory | - | derived units | cross-laboratory pairs, strict rate separation | 100 | - |
| ERA4TB six-laboratory | - | derived units | flasks contributing those pairs | 42 | - |
| ERA4TB six-laboratory | - | derived units | laboratory-by-arm-by-volume cells with a measured start | 56 | - |
| ERA4TB six-laboratory | - | derived units | treated series with three or more quantified readings at 100 uL | 64 | - |
| ERA4TB six-laboratory | - | derived units | flask units in the variance decomposition (all arms plus inoculum) | 85 | - |
| ERA4TB six-laboratory | - | derived units | untreated day-zero readings at 100 uL (4 laboratories x 3 flasks) | 12 | - |
| ERA4TB six-laboratory | - | derived units | below-limit flags in the analysis set | 498 | - |
| ERA4TB six-laboratory | - | derived units | readings in the kill-rate analysis set | 2580 | -171 |
| Dubey hollow fibre (held out) | - | - | cultures with a measured day-zero density | 20 | - |

**Table S3.** The deposited tolerance class at day 5 after 15 days of prior culture is a threshold on the recorded surviving fraction, with no overlap between classes: low below 10⁻³, medium from 10⁻³ to 10⁻² inclusive, high above 10⁻². Applying those cuts reproduces every usable class in the file. This matters because the argument that follows is about the fraction the assay recorded, not about an independent clinical judgement.

| Recorded class | n | Min fraction | Max fraction | Predicted from cuts | Disagreements |
| --- | ---: | ---: | ---: | ---: | ---: |
| Low | 33 | 3.8 × 10⁻⁶ | 4.7 × 10⁻⁴ | Low | 0 |
| Medium | 124 | 1.0 × 10⁻³ | 1.0 × 10⁻² | Medium | 0 |
| High | 46 | 2.7 × 10⁻² | 1.0 × 10¹ | High | 0 |
| All usable | 203 | - | - | - | 0 |

**Table S4.** The family of 8 tests between the deposited tolerance label and its candidate determinants, fitted as proportional-odds ordinal logistic regression and corrected together by the Benjamini-Hochberg procedure at a false discovery rate of 5%; the "survives BH" column is that correction. 2 survive. An odds ratio above one means higher odds of a higher tolerance class; time to an optical density (OD) of 0.4 is in days and runs inversely to growth rate, so above one there means *slower* growth accompanies a higher class. The proportional-odds column is a Brant test per predictor; the assumption holds for every predictor in this family. Starting density enters the adjusted fits as a covariate rather than as a member of the family, and it is where proportional odds fails, at 60 days at the deepest endpoint; that failure and the released fit are reported in Section 4. The final column repeats each test on the baseline isolates, one per patient by construction, which is where the resistance association stops clearing its corrected threshold. The deposit carries no patient identifier, so no standard error here can be clustered on the true grouping and every interval in this table is model-based; the baseline-isolate column is the sensitivity analysis that stands in for clustering, and Table S13 records what each conclusion is worth once it is applied.

| Predictor | Prior culture | Reading day | For starting density | n | Odds ratio (95% CI) | p | Survives BH | Prop. odds p | Baseline isolates only |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| time to OD 0.4 | 15 d | day 5 | adjusted | 202 | 1.096 (1.03-1.16) | 0.0030 | yes | 0.152 | 1.12 (p=0.002, survives) |
| resistance | 15 d | day 5 | unadjusted | 202 | 2.317 (1.30-4.12) | 0.0042 | yes | 0.417 | 2.11 (p=0.031, no) |
| time to OD 0.4 | 60 d | day 2 | adjusted | 196 | 0.933 (0.87-1.00) | 0.0470 | no | 0.688 | 0.92 (p=0.032, no) |
| time to OD 0.4 | 15 d | day 2 | adjusted | 202 | 1.068 (1.00-1.14) | 0.0618 | no | 0.243 | 1.07 (p=0.108, no) |
| resistance | 15 d | day 2 | unadjusted | 202 | 1.295 (0.66-2.54) | 0.4529 | no | 0.479 | 1.07 (p=0.876, no) |
| time to OD 0.4 | 60 d | day 5 | adjusted | 196 | 0.976 (0.91-1.04) | 0.4605 | no | 0.875 | 0.99 (p=0.703, no) |
| resistance | 60 d | day 2 | unadjusted | 196 | 0.836 (0.47-1.48) | 0.5400 | no | 0.075 | 1.11 (p=0.774, no) |
| resistance | 60 d | day 5 | unadjusted | 196 | 1.111 (0.63-1.95) | 0.7150 | no | 0.067 | 1.61 (p=0.186, no) |

**Table S5.** Decomposition of the isoniazid-resistance association with the tolerance class into a path through log10 starting density and a direct path, by the product of coefficients with bootstrap percentile intervals. The mediated path excludes zero in every specification and the direct path covers zero in every one. This replaces the percentage attenuation the earlier analysis quoted, which is a descriptive ratio rather than an estimand. Sequential ignorability is assumed and is not testable here; the sensitivity analysis in the Methods reports the residual correlation that would nullify the estimate.

| Outcome and stratum | n | Total effect c (95% CI) | Direct effect c' (95% CI) | Mediated effect (95% CI) | Proportion mediated |
| --- | ---: | ---: | ---: | ---: | ---: |
| Linear 0/1/2, all IS/IR | 203 | +0.256 (+0.087, +0.425) | +0.091 (-0.116, +0.287) | +0.166 (+0.067, +0.279) | 65% |
| Linear 0/1/2, baseline isolates | 168 | +0.226 (+0.038, +0.409) | +0.067 (-0.157, +0.294) | +0.159 (+0.053, +0.295) | 70% |
| High versus rest | 203 | +0.121 | +0.013 | +0.108 (+0.037, +0.189) | 89% |
| Not-low versus low | 203 | +0.135 | +0.077 | +0.058 (+0.003, +0.121) | 43% |

**Table S6.** Moxifloxacin at ten times MIC. Every laboratory yields a rate; three record no crossing below the assay floor in any arm at the 100 uL plating. The final column counts first observed crossings, which are not clearances: across the deposit 60% of the series that cross read above the floor again at a later visit. The two censoring estimators agree to 0.003 log10 per day. The starting density is the mean of quantified readings at day 0 or day 1 at the 100 uL plating, pooled over all of that laboratory's arms; the reading-day column says which visits contributed. Institute A deposits no day-zero reading at all, and among treated flasks only institutes C and D do, so for the rest this figure rests partly on readings taken after 24 hours of drug. The turbidity-standard analysis and Table S7 instead use untreated day-zero readings only, so the two tables are not expected to match.

| Lab | Starting density (log10 CFU/mL) | Reading day | Kill rate (log10/day) | 95% profile interval | By imputation | Readings censored | Flasks ever crossing the floor (treated arms) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 2.95 | day 1 | 0.119 | 0.084 to 0.160 | 0.125 | 51% | 9 / 12 |
| B | 3.16 | day 0, day 1 | 0.139 | 0.097 to 0.191 | 0.140 | 58% | 10 / 12 |
| C | 4.02 | day 0, day 1 | 0.464 | 0.408 to 0.528 | 0.464 | 44% | 10 / 12 |
| D | 4.69 | day 0, day 1 | 0.104 | 0.077 to 0.132 | 0.104 | 3% | 0 / 12 |
| E | 4.95 | day 0, day 1 | 0.090 | 0.073 to 0.107 | 0.090 | 1% | 0 / 12 |
| F | 6.53 | day 0, day 1 | 0.223 | 0.191 to 0.254 | 0.223 | 0% | 0 / 12 |

**Table S7.** The deepest reduction each assay could resolve, as h = log10(N0/L), with the assay floor taken per sample where it varies. Rows compare only within a level of variation: the clinical rows describe between-isolate starting burden, which is biological, and are not a measure of laboratory imprecision. Kaur is NA because its three day-zero readings are technical replicates of one preparation and cannot estimate between-preparation reproducibility, and because that deposit states no quantification limit.

| Dataset | Level of variation | n | Median log10 N0 | Assay floor L | delta h (log10) | Fold |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| ERA4TB, between laboratories at 100 uL | between laboratories, one written protocol | 12 | 4.63 | 10 CFU/mL, derived from 100 uL plated | 2.33 | 216x |
| ERA4TB, every laboratory and plating volume | laboratories and plated volumes together | 56 | 4.29 | 10, 100 or 400 CFU/mL by volume | 4.40 | 25,123x |
| Vijay, 15-day culture | between clinical isolates | 217 | 5.79 | 23 MPN/mL, inferred | 4.42 | 26,522x |
| Vijay, 60-day culture | between clinical isolates | 210 | 7.36 | 23 MPN/mL, inferred | 5.43 | 269,565x |
| Kaur, planktonic | technical replicates of one preparation | 3 | 7.03 | not stated in the deposit | NA | NA |
| Kaur, intracellular | technical replicates of one preparation | 3 | 5.94 | not stated in the deposit | NA | NA |
| Dubey, hollow fibre | between cultures, one laboratory | 20 | 6.08 | 10 CFU/mL, derived from 100 uL plated | 0.60 | 4x |

**Table S8.** Fold below the nominal 0.5 McFarland reference, 1.5e8 CFU/mL. Descriptive only, and not a protocol-compliance metric. A time-kill inoculum is prepared by diluting from a suspension matched to that turbidity, so every entry is expected to sit far below it; the conversion of a turbidity to CFU/mL depends on species, cell aggregation and preparation and is least reliable for mycobacteria. The clinical rows are most probable numbers divided by a reference stated in CFU/mL, so those two ratios cross units and are the least meaningful in the table.

| Dataset | Median log10 N0 | Fold below nominal 0.5 McFarland |
| --- | ---: | ---: |
| ERA4TB, between laboratories at 100 uL | 4.63 | 3,525x |
| ERA4TB, every laboratory and plating volume | 4.29 | 7,751x |
| Vijay, 15-day culture | 5.79 | 246x |
| Vijay, 60-day culture | 7.36 | 7x |
| Kaur, planktonic | 7.03 | 14x |
| Kaur, intracellular | 5.94 | 170x |
| Dubey, hollow fibre | 6.08 | 123x |

**Table S9.** Dubey et al. 2026, analysed cold. The floor is derived from a stated 100 uL plated volume and corroborated inside the file: all 229 genuine counts are multiples of ten and the smallest is exactly ten. Starting densities are the 20 measured day-zero counts, not the nominal inoculum the Methods state.

| Endpoint | N_reach (per mL) | Cultures | Unreachable | Per cent |
| --- | ---: | ---: | ---: | ---: |
| 1 log (90%) | 100 | 20 | 0 | 0% |
| 2 log (99%) | 1,000 | 20 | 0 | 0% |
| 3 log (99.9%) | 10,000 | 20 | 0 | 0% |
| 4 log (99.99%) | 100,000 | 20 | 0 | 0% |
| 5 log (99.999%) | 1,000,000 | 20 | 5 | 25% |
| 6 log (99.9999%) | 10,000,000 | 20 | 20 | 100% |

**Table S10.** The same 32-fold concentration range summarised at each sampling day (upper rows), and the concentration slope fitted separately in each interval (lower rows). Slopes and intervals are from the replicate-level bootstrap described in the Methods.

| Read at | Survivor ratio (low/high dose) | log10 separation | Slope per doubling | 95% interval | p |
| --- | ---: | ---: | ---: | ---: | ---: |
| day 3 | 6.9x | 0.84 |  |  |  |
| day 7 | 48.2x | 1.68 |  |  |  |
| day 14 | 5.2x | 0.71 |  |  |  |
| days 0-3 |  |  | +0.0590 | +0.0327 to +0.0834 | 0.013 |
| days 3-7 |  |  | +0.0330 | +0.0079 to +0.0586 | 0.236 |
| days 7-14 |  |  | -0.0251 | -0.0353 to -0.0153 | 0.091 |

**Table S11.** The deepest reduction each culture in the prospective experiment could report, at each of its two platings. *h* = log10(*N*₀/*L*) with *L* one colony in the pooled volume plated, taken at the lowest dilution the series was read at, which is where the floor is lowest and the reportable depth greatest. The two platings of one flask share a row: at the standard inoculum the 10 µL plating ceiling runs 3.71 to 3.93 logs and the 100 µL ceiling 4.88 to 5.05, so a four-log endpoint is unreportable at one plating and reportable at the other in the same culture. The gain column is close to the log10(10) = 1.00 that plating ten times the volume buys; it is not exactly 1.00 because each plating measures its own *N*₀ and the two measurements differ.

| Arm | Flask | *N*₀ at 10 µL (per mL) | *N*₀ at 100 µL (per mL) | *h* at 10 µL | *h* at 100 µL | Gain |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| High | 1 | 3,600,000 | 4,050,000 | 4.86 | 5.91 | +1.05 |
| High | 2 | 4,450,000 | 3,300,000 | 4.95 | 5.82 | +0.87 |
| High | 3 | 4,450,000 | 3,950,000 | 4.95 | 5.90 | +0.95 |
| Low | 1 | 58,000 | 78,000 | 3.06 | 4.19 | +1.13 |
| Low | 2 | 42,500 | 65,000 | 2.93 | 4.11 | +1.18 |
| Low | 3 | 45,500 | 50,000 | 2.96 | 4.00 | +1.04 |
| Mid | 1 | 425,000 | 565,000 | 3.93 | 5.05 | +1.12 |
| Mid | 2 | 340,000 | 380,000 | 3.83 | 4.88 | +1.05 |
| Mid | 3 | 255,000 | 375,000 | 3.71 | 4.88 | +1.17 |

**Table S12.** How often one culture receives two different tolerance labels from its two platings, swept across the class threshold. That two platings report different fractions is arithmetic; that those fractions land either side of a cut is not, and this is the quantity that could have come out zero. At a cut of one per cent the window is nearly shut. At one in a thousand, where the clinical classification reanalysed here cuts its lowest class, it is one sample-time in nine. The two pairs of columns differ in one thing. The first holds the starting density to a single value per flask, so the only thing separating the two readings is the plated volume, which is what the argument claims. The second lets each plating carry the starting density it measured for itself, which is what a laboratory running both platings would have; the count rises because those two estimates of one culture disagree by 0.74- to 1.53-fold. The first column is the claim, the second is the practice, and neither is the other.

| Class threshold *c*₁ | Straddling, one *N*₀ per flask | Share | Straddling, each plating's own *N*₀ | Share  |
| --- | ---: | ---: | ---: | ---: |
| 10^-2 | 1 of 54 | 2% | 1 of 54 | 2% |
| 10^-3 | 6 of 54 | 11% | 9 of 54 | 17% |
| 10^-4 | 7 of 54 | 13% | 8 of 54 | 15% |

**Table S13.** Every conclusion this paper draws from the two primary deposits, against uncertainty recomputed at the level the observations are actually independent. 20 survive unchanged, 6 survive with materially wider uncertainty, 5 do not survive, and 1 is withdrawn because its null is false before any data are seen. Each verdict applies to the claim as it was originally stated. Three of the five failures are gone from the text entirely; for the other two a weaker statement is retained and is marked as such where it appears -- the Cox coefficient trade is now reported as hazard ratios with no p-value, and institute C as the laboratory whose crossings its starting density does not account for rather than as a tested contrast. The five that fail are all between-laboratory p-values computed on flasks: every flask in a laboratory shares a starting culture, so a comparison that looks like 67 flasks is six laboratories, and for a three-against-three split of six clusters the smallest attainable two-sided p is 0.10. They are deleted rather than corrected, because there is nothing to correct them to.

| Section | Conclusion as originally stated | Units treated as independent | Independent clusters | Method used instead | Verdict |
| --- | --- | --- | ---: | ---: | ---: |
| 4 | the difference between panels in the growth association is itself supported (interaction p = 0.0072) | unknown isolate-panel (each of 210 isolates counted once per panel) | 210 isolates | not recomputable | NOT SUPPORTED |
| 5 | starting density separates flasks that ever crossed below the assay floor from those that never did (AUC 0.974, p = 1.2e-10) | 67 flask | 6 | exact laboratory-level test (3 crossed vs 3 did not); cluster bootstrap over laboratories; permutation of crossing within laboratory, and within laboratory AND treatment arm | NOT SUPPORTED |
| 5 | in a Cox model, institutes D, E and F carry p = 0.015, 0.016, 0.015, which adjustment for starting density moves to 0.138, 0.172, 0.576 | 67 flask | 6 | cluster-robust sandwich on six clusters | NOT SUPPORTED |
| 5 | the log-rank test separates the six laboratories on time to first crossing | 67 flask | 6 | none available: the grouping variable is the cluster | NOT SUPPORTED |
| 5 | institute C remains distinguishable after adjustment (HR 5.27, p < 0.001) | 67 flask | 1 | none available | NOT SUPPORTED |
| 1 | all 33 short isolates are at the ceiling; 88.0% of the rest are (Fisher p = 0.030) | 217 isolate | 174 patients min | none: the null is arithmetically impossible | WITHDRAWN |
| 5 | at ten times MIC of moxifloxacin the kill rate spans 5.2-fold between laboratories (0.090 to 0.464) | 6 laboratory-arm cell | 6 | cluster bootstrap over whole laboratories | WEAKENED |
| 5 | at one times MIC five of six laboratories record net growth | 6 laboratory-arm cell | 6 | Jeffreys interval on six clusters | WEAKENED |
| 5 / 7 | the laboratory effect lands on the duration endpoint and not on the rate; the rate is 'far more reproducible' | 42 flask | 6 | permutation of the laboratory label across flasks, within arm for the rate | WEAKENED |
| 6 | the deepest demonstrable kill differs by 2.33 log10 between laboratories at one plating volume | 12 day-zero reading | 4 | cluster bootstrap over whole laboratories | WEAKENED |
| 7 | 34.6% of 191 cross-laboratory pairs are inversions (95% CI 28.1-41.5) | 191 pair of flasks | 6 | cluster bootstrap over whole laboratories; also over flasks within laboratory; also delete-one-laboratory jackknife | WEAKENED |
| 7 | under the strictest rate separation the inversion rate is 23.0% of 100 pairs (95% CI 15.6-31.9) | 100 pair of flasks | 6 | cluster bootstrap over whole laboratories | WEAKENED |
| 1 | 33 of 217 isolates (15.2%) lack the headroom for a 4-log endpoint | 217 isolate | 174 patients min | baseline-only recount | SUPPORTED |
| 1 / 2 | 18 isolates rest on the floor at 15 days and 6 at 60 | 217 + 210 isolate-panel (each of 210 isolates counted once per panel) | 210 isolates | exact McNemar on the paired binary | SUPPORTED |
| 10 | no MIC-MDK association survives Benjamini-Hochberg (supplementary text, not a numbered section of the article) | 6 tests isolate | 174 patients min | baseline-only family of six | SUPPORTED |
| 2 | 18 isolates at the floor; their survival span IS their inoculum span | 217 isolate | 174 patients min | baseline-only recount | SUPPORTED |
| 2 | 185 determinable, 12 forced by the inoculum, 6 undecidable | 203 isolate | 174 patients min | baseline-only reclassification | SUPPORTED |
| 2 | at 60 days the observability counts are 191, 6 and none, 'because the cultures are denser and few readings reach the floor' | 203 + 197 isolate-panel (each of 210 isolates counted once per panel) | 197 isolates | exact McNemar on the paired binary | SUPPORTED |
| 2 / 4 | the deep endpoint is unreachable for 26.2% of resistant against 7.6% of susceptible isolates | 217 isolate | 174 patients min | baseline-only Fisher exact | SUPPORTED |
| 4 | resistant isolates enter the assay ten-fold lower | 217 isolate | 174 patients min | baseline-only Mann-Whitney | SUPPORTED |
| 4 | the resistance-tolerance association attenuates once starting density enters the model, and its interval then spans zero | 202 isolate | 174 patients min | baseline-only refit | SUPPORTED |
| 4 | growth state predicts the tolerance class and survives adjustment (beta = +0.027, p = 0.0025) | 202 isolate | 174 patients min | baseline-only refit | SUPPORTED |
| 4 | resistant isolates do not grow measurably more slowly (p = 0.24) | 217 isolate | 174 patients min | baseline-only Mann-Whitney | SUPPORTED |
| 4 | the confound thins between panels: 15.2% short of headroom at 15 days against 3.3% at 60 | 217 + 210 isolate-panel (each of 210 isolates counted once per panel) | 210 isolates | exact McNemar on the paired binary | SUPPORTED |
| 4 | the 60-day cultures are denser, so headroom is larger there | 420 treated as independent isolate-panel (each of 210 isolates counted once per panel) | 210 isolates | Wilcoxon signed-rank on the within-isolate change | SUPPORTED |
| 4 | the spread of starting densities more than halves between panels (IQR 1.00 to 0.42 log10) | 420 isolate-panel (each of 210 isolates counted once per panel) | 210 isolates | paired bootstrap resampling whole isolates | SUPPORTED |
| 5 | of 64 treated series the final step is not a decline in 48 (75%) | 64 series (one per treated flask) | 6 | cluster bootstrap over whole laboratories | SUPPORTED |
| 5 | 44 of 64 series end more than one log10 above their own nadir | 64 series (one per treated flask) | 6 | cluster bootstrap over whole laboratories | SUPPORTED |
| 5 / Limitations | 87.0% of the variance in flask starting density lies between laboratories | 85 flask | 6 | permutation of the laboratory label across flasks | SUPPORTED |
| 6 | including the choice of plated volume widens the spread in measurable depth to 4.40 log10 | up to 4 volumes x 5 laboratories laboratory-by-volume channel | 6 | no resampling required for the volume term | SUPPORTED |
| 7 | the criterion D_A/D_B > b_A/b_B calls 83.8% of pairs correctly | 191 pair of flasks | 6 | cluster bootstrap over whole laboratories | SUPPORTED |
| Methods | 83 of 498 below-limit flags (16.7%) are contradicted by another plating of the same sample at the same visit | 498 flag (one reading) | 6 | cluster bootstrap over whole laboratories | SUPPORTED |

**Table S14.** What the assay floor *L* is in each deposit analysed. No deposit reports a validated limit of quantification with a value. The six-laboratory file names the concept in the definitions of its below- and above-quantification-limit columns but defines it as whether the plate was countable, which is an operator's judgement. DERIVED means the value follows arithmetically from a recorded plated volume; INFERRED means it was read off the deposit's own behaviour and is labelled as inferred wherever it is used; NONE means no floor is evidenced and none is assumed; FLAGGED means the deposit marks below-limit readings without naming a value, which fixes no floor either. Where a plated volume is recorded the honest term is the minimum reportable positive count, one colony in that volume; elsewhere it is an operational assay floor.

| Deposit | States an LOD | States an LOQ | Value used | Units | How obtained | What it should be called |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Vijay 2024 | no | no | 23 | MPN per mL | INFERRED | operational assay floor |
| ERA4TB 2023 | no | term only | 10, 100 and 400, per plated volume | CFU per mL | DERIVED | minimum reportable positive count |
| Windels 2024 | no | no | none; no value is recoverable | surviving fraction, dimensionless | FLAGGED | no floor is established; a below-limit reading is written as exact zero and fixes no value |
| Kaur 2024 | no | no | none; no floor is used | log10 CFU per mL | NONE | no floor is evidenced; the smallest reading is the smallest reading |
| Dubey 2026 | no | no | 10 | CFU per mL | DERIVED | minimum reportable positive count |

**Table S15.** Sensitivity of the load-bearing counts to the choice of floor. Each deposit is sensitive to a different thing, so the table is long rather than wide: one row per deposit, floor scenario and quantity. The clinical sweep steps through every three-tube most-probable-number rung at or below 23 per mL, and the number of isolates short of four logs of headroom moves only between 28 and 33 across the whole range, which is why the inferred floor is safe to use. The six-laboratory rows price what pooling the four plating volumes to one floor would cost. The Kaur deposit records no plated volume, so its rows show what assuming one would do: the four-log endpoint stays reachable throughout while the headroom itself moves by 1.6 log10.

| Deposit | Floor assumed | Quantity | Value |
| --- | --- | --- | ---: |
| Vijay 2024 | floor = 3 MPN/mL | isolates short of 4 logs | 28 |
| Vijay 2024 | floor = 3 MPN/mL | isolates at the floor | 0 |
| Vijay 2024 | floor = 3 MPN/mL | calls resting on a measured fraction | 203 |
| Vijay 2024 | floor = 3 MPN/mL | calls with one compatible class | 0 |
| Vijay 2024 | floor = 3 MPN/mL | calls with several compatible classes | 0 |
| Vijay 2024 | floor = 3 MPN/mL | short of 4 logs, baseline only | 17 |
| Vijay 2024 | floor = 3.6 MPN/mL | isolates short of 4 logs | 28 |
| Vijay 2024 | floor = 3.6 MPN/mL | isolates at the floor | 0 |
| Vijay 2024 | floor = 3.6 MPN/mL | calls resting on a measured fraction | 203 |
| Vijay 2024 | floor = 3.6 MPN/mL | calls with one compatible class | 0 |
| Vijay 2024 | floor = 3.6 MPN/mL | calls with several compatible classes | 0 |
| Vijay 2024 | floor = 3.6 MPN/mL | short of 4 logs, baseline only | 17 |
| Vijay 2024 | floor = 7.2 MPN/mL | isolates short of 4 logs | 33 |
| Vijay 2024 | floor = 7.2 MPN/mL | isolates at the floor | 0 |
| Vijay 2024 | floor = 7.2 MPN/mL | calls resting on a measured fraction | 203 |
| Vijay 2024 | floor = 7.2 MPN/mL | calls with one compatible class | 0 |
| Vijay 2024 | floor = 7.2 MPN/mL | calls with several compatible classes | 0 |
| Vijay 2024 | floor = 7.2 MPN/mL | short of 4 logs, baseline only | 21 |
| Vijay 2024 | floor = 7.4 MPN/mL | isolates short of 4 logs | 33 |
| Vijay 2024 | floor = 7.4 MPN/mL | isolates at the floor | 0 |
| Vijay 2024 | floor = 7.4 MPN/mL | calls resting on a measured fraction | 203 |
| Vijay 2024 | floor = 7.4 MPN/mL | calls with one compatible class | 0 |
| Vijay 2024 | floor = 7.4 MPN/mL | calls with several compatible classes | 0 |
| Vijay 2024 | floor = 7.4 MPN/mL | short of 4 logs, baseline only | 21 |
| Vijay 2024 | floor = 9.2 MPN/mL | isolates short of 4 logs | 33 |
| Vijay 2024 | floor = 9.2 MPN/mL | isolates at the floor | 0 |
| Vijay 2024 | floor = 9.2 MPN/mL | calls resting on a measured fraction | 203 |
| Vijay 2024 | floor = 9.2 MPN/mL | calls with one compatible class | 0 |
| Vijay 2024 | floor = 9.2 MPN/mL | calls with several compatible classes | 0 |
| Vijay 2024 | floor = 9.2 MPN/mL | short of 4 logs, baseline only | 21 |
| Vijay 2024 | floor = 11 MPN/mL | isolates short of 4 logs | 33 |
| Vijay 2024 | floor = 11 MPN/mL | isolates at the floor | 0 |
| Vijay 2024 | floor = 11 MPN/mL | calls resting on a measured fraction | 203 |
| Vijay 2024 | floor = 11 MPN/mL | calls with one compatible class | 0 |
| Vijay 2024 | floor = 11 MPN/mL | calls with several compatible classes | 0 |
| Vijay 2024 | floor = 11 MPN/mL | short of 4 logs, baseline only | 21 |
| Vijay 2024 | floor = 14 MPN/mL | isolates short of 4 logs | 33 |
| Vijay 2024 | floor = 14 MPN/mL | isolates at the floor | 0 |
| Vijay 2024 | floor = 14 MPN/mL | calls resting on a measured fraction | 203 |
| Vijay 2024 | floor = 14 MPN/mL | calls with one compatible class | 0 |
| Vijay 2024 | floor = 14 MPN/mL | calls with several compatible classes | 0 |
| Vijay 2024 | floor = 14 MPN/mL | short of 4 logs, baseline only | 21 |
| Vijay 2024 | floor = 15 MPN/mL | isolates short of 4 logs | 33 |
| Vijay 2024 | floor = 15 MPN/mL | isolates at the floor | 0 |
| Vijay 2024 | floor = 15 MPN/mL | calls resting on a measured fraction | 203 |
| Vijay 2024 | floor = 15 MPN/mL | calls with one compatible class | 0 |
| Vijay 2024 | floor = 15 MPN/mL | calls with several compatible classes | 0 |
| Vijay 2024 | floor = 15 MPN/mL | short of 4 logs, baseline only | 21 |
| Vijay 2024 | floor = 20 MPN/mL | isolates short of 4 logs | 33 |
| Vijay 2024 | floor = 20 MPN/mL | isolates at the floor | 0 |
| Vijay 2024 | floor = 20 MPN/mL | calls resting on a measured fraction | 203 |
| Vijay 2024 | floor = 20 MPN/mL | calls with one compatible class | 0 |
| Vijay 2024 | floor = 20 MPN/mL | calls with several compatible classes | 0 |
| Vijay 2024 | floor = 20 MPN/mL | short of 4 logs, baseline only | 21 |
| Vijay 2024 | floor = 21 MPN/mL | isolates short of 4 logs | 33 |
| Vijay 2024 | floor = 21 MPN/mL | isolates at the floor | 0 |
| Vijay 2024 | floor = 21 MPN/mL | calls resting on a measured fraction | 203 |
| Vijay 2024 | floor = 21 MPN/mL | calls with one compatible class | 0 |
| Vijay 2024 | floor = 21 MPN/mL | calls with several compatible classes | 0 |
| Vijay 2024 | floor = 21 MPN/mL | short of 4 logs, baseline only | 21 |
| Vijay 2024 | floor = 23 MPN/mL | isolates short of 4 logs | 33 |
| Vijay 2024 | floor = 23 MPN/mL | isolates at the floor | 18 |
| Vijay 2024 | floor = 23 MPN/mL | calls resting on a measured fraction | 185 |
| Vijay 2024 | floor = 23 MPN/mL | calls with one compatible class | 12 |
| Vijay 2024 | floor = 23 MPN/mL | calls with several compatible classes | 6 |
| Vijay 2024 | floor = 23 MPN/mL | short of 4 logs, baseline only | 21 |
| ERA4TB | per-volume (as analysed) | genuine counts a pooled floor discards (%) | 0 |
| ERA4TB | per-volume (as analysed) | below-limit flags contradicted (%) | 16.67 |
| ERA4TB | pooled at the most sensitive volume, 100 uL | genuine counts a pooled floor discards (%) | 0 |
| ERA4TB | pooled at the most sensitive volume, 100 uL | below-limit flags contradicted (%) | 43.17 |
| ERA4TB | pooled at the modal volume, 10 uL | genuine counts a pooled floor discards (%) | 1.13 |
| ERA4TB | pooled at the modal volume, 10 uL | below-limit flags contradicted (%) | 28.71 |
| ERA4TB | pooled at the least sensitive volume, 2.5 uL | genuine counts a pooled floor discards (%) | 5.94 |
| ERA4TB | pooled at the least sensitive volume, 2.5 uL | below-limit flags contradicted (%) | 15.26 |
| ERA4TB | pooled at the geometric mean of the per-volume floors | genuine counts a pooled floor discards (%) | 1.04 |
| ERA4TB | pooled at the geometric mean of the per-volume floors | below-limit flags contradicted (%) | 38.96 |
| Dubey 2026 | the below-limit placeholder taken literally | median headroom (log10) | 6.08 |
| Dubey 2026 | the below-limit placeholder taken literally | cultures short of 4 logs | 0 |
| Dubey 2026 | 100 uL plated, as the deposit's staging record gives | median headroom (log10) | 5.08 |
| Dubey 2026 | 100 uL plated, as the deposit's staging record gives | cultures short of 4 logs | 0 |
| Dubey 2026 | 50 uL plated | median headroom (log10) | 4.78 |
| Dubey 2026 | 50 uL plated | cultures short of 4 logs | 0 |
| Dubey 2026 | 10 uL plated | median headroom (log10) | 4.08 |
| Dubey 2026 | 10 uL plated | cultures short of 4 logs | 5 |
| Kaur 2024 | 100 uL plated, if it had been stated | headroom (log10) | 6.03 |
| Kaur 2024 | 100 uL plated, if it had been stated | 4-log endpoint reachable | True |
| Kaur 2024 | the observed minimum, which occurs once | headroom (log10) | 5.43 |
| Kaur 2024 | the observed minimum, which occurs once | 4-log endpoint reachable | True |
| Kaur 2024 | 10 uL plated, if it had been stated | headroom (log10) | 5.03 |
| Kaur 2024 | 10 uL plated, if it had been stated | 4-log endpoint reachable | True |
| Kaur 2024 | 2.5 uL plated, if it had been stated | headroom (log10) | 4.43 |
| Kaur 2024 | 2.5 uL plated, if it had been stated | 4-log endpoint reachable | True |
| Windels 2024 | no floor is recoverable | readings written as exact zero | 6 |

**Table S16.** The comparison the Methods promise: rows dropped from the association family against rows retained, on starting density and susceptibility. The MDR exclusion differs in susceptibility by construction, since those isolates are outside the resistant-versus-susceptible contrast the family tests. The one difference not by construction is in the 60-day panel, where the dropped rows sit higher in starting density (p = 0.027); it affects 20 rows and no conclusion drawn from that panel.

| Panel | Exclusion | Dropped | Retained | Median log10 N0 retained | Median log10 N0 dropped | p | Resistant, retained | Resistant, dropped | p  |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 15-day | label missing or 'MDR' | 14 | 202 | 5.79 | 5.36 | 0.198 | 41% | 0% | 0.001 |
| 15-day | growth proxy missing | 1 | 202 | 5.79 | 6.79 | 0.149 | 41% | 100% | 0.414 |
| 60-day | label missing or 'MDR' | 20 | 196 | 7.36 | 7.79 | 0.027 | 40% | 20% | 0.093 |
| 60-day | growth proxy missing | 1 | 196 | 7.36 | 7.36 | 0.749 | 40% | 100% | 0.406 |

**Table S17.** The ordinal reanalysis against the linear model it replaces, member for member. The linear model scores the ordering 0, 1, 2, which assumes the two class steps are equal; the ordinal model does not. Every direction agrees and the same two members survive correction under both, so the linear treatment did not manufacture the result -- but the coefficients it reports are in a unit that does not exist, which is why the ordinal fit is the one in the main table.

| Predictor | Prior culture | Reading day | Linear beta | p (linear) | Survives BH | Odds ratio | p (ordinal) | Survives BH  | Same direction |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| time to OD 0.4 | 15 d | day 5 | +0.0266 | 0.0025 | yes | 1.096 | 0.0030 | yes | yes |
| resistance | 15 d | day 5 | +0.2589 | 0.0035 | yes | 2.317 | 0.0042 | yes | yes |
| time to OD 0.4 | 60 d | day 2 | -0.0195 | 0.0590 | no | 0.933 | 0.0470 | no | yes |
| time to OD 0.4 | 15 d | day 2 | +0.0116 | 0.0812 | no | 1.068 | 0.0618 | no | yes |
| resistance | 15 d | day 2 | +0.0515 | 0.4446 | no | 1.295 | 0.4529 | no | yes |
| time to OD 0.4 | 60 d | day 5 | -0.0041 | 0.6999 | no | 0.976 | 0.4605 | no | yes |
| resistance | 60 d | day 2 | -0.0551 | 0.5486 | no | 0.836 | 0.5400 | no | yes |
| resistance | 60 d | day 5 | +0.0389 | 0.6797 | no | 1.111 | 0.7150 | no | yes |

**Table S18.** Pairs of flasks in the same arm from different laboratories. An inversion is a pair in which the population that fell faster crossed below the assay floor later. 45 further pairs that the censoring could not settle are excluded rather than imputed. The variance columns decompose the spread in crossing time. The rate term is the larger at the flask level in all three arms that can be decomposed, and that ordering is NOT a claim this table supports: the flasks are three to a laboratory and share a starting culture, so the quantity is a between-laboratory statistic on six clusters. Deleting one laboratory sends the distance share above a half in two of the three arms, and a bootstrap over whole laboratories straddles a half in all three. The last two columns are those two checks, and they are the reason the text claims only that the two terms are of comparable size. Moxifloxacin at one times MIC is not among them: the decomposition is taken on log *D* and log *b*, five of six laboratories record net growth in that arm, and only one flask in it returns a positive fitted rate, so there is no spread in the rate to divide.

| Arm | Comparable pairs | Inversions | Rate | 95% CI | Called by D/b criterion | Variance: distance | Variance: rate | Distance share, leave one laboratory out | Distance share, laboratory bootstrap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| All arms pooled | 191 | 66 | 34.6% | 28.1-41.5% | 84.3% |  |  |  |  |
| INH 10X MIC |  |  |  |  |  | 32.3% | 67.7% | 19.4-70.4% | 4.8-85.4% |
| INH 1X MIC |  |  |  |  |  | 17.7% | 82.3% | 10.9-28.3% | 1.2-70.3% |
| MXF 10X MIC |  |  |  |  |  | 35.2% | 64.8% | 23.9-62.3% | 8.6-76.6% |

**Table S19.** The six strongest of the 24 comparisons the 217-isolate file supports. 4 reach nominal significance where 1.2 are expected by chance; none exceeds its Benjamini-Hochberg critical value, which is ranked against the full family of 24 rather than against any one stratum. MDK99 and MDK99.99 are the minimum durations for a 99 and a 99.99 per cent reduction, the endpoints the text names in words. The final column is the correlation each design could have resolved at 95% confidence.

| Stratum | Endpoint | n | Spearman rho | p | BH critical value | Survives correction | Resolvable rho |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| baseline only | MDK99.99 (15d) | 162 | -0.206 | 0.0086 | 0.0021 | no | 0.15 |
| INH-susceptible | MDK99.99 (15d) | 119 | -0.218 | 0.0171 | 0.0042 | no | 0.18 |
| INH-susceptible | MDK99 (60d) | 117 | -0.198 | 0.0324 | 0.0063 | no | 0.18 |
| all isolates | MDK99.99 (60d) | 187 | -0.153 | 0.0361 | 0.0083 | no | 0.14 |
| INH-susceptible | MDK99.99 (60d) | 117 | -0.179 | 0.0540 | 0.0104 | no | 0.18 |
| baseline only | MDK99.99 (60d) | 156 | -0.149 | 0.0628 | 0.0125 | no | 0.16 |

**Table S20.** The same nominal concentration expressed in multiples of the minimum inhibitory concentration each population actually evolved to. At 25 ug/mL the same number denotes a sub-inhibitory exposure in one nutrient condition and a strongly inhibitory one in another.

| Nominal concentration (ug/mL) | Nutrient levels | Lowest exposure (x MIC) | Highest exposure (x MIC) | Spread | Straddles the MIC |
| --- | ---: | ---: | ---: | ---: | ---: |
| 12.5 | 3 | 1.49 | 4.74 | 3.2x | no |
| 25 | 3 | 0.55 | 9.47 | 17.1x | yes |
| 50 | 2 | 5.08 | 10.95 | 2.2x | no |
| 100 | 1 | 9.72 | 9.72 | 1.0x | no |

**Table S21.** Isoniazid-resistant isolates enter this assay ten-fold lower than susceptible ones, and we do not know why. This is what the deposit can and cannot rule out. The verdict column is decided on the two recorded-rate columns beside it: PROXY means the covariate is recorded for no isolate in one of the two exposure groups, so its missingness is the exposure; PARTIAL means both groups record it but the missingness is still tied to the exposure (Fisher exact p < 10⁻⁶); INDEPENDENT means it is not. Seven of the nine covariates are therefore unusable, and they fail in two ways. Five are recorded almost exclusively for resistant isolates: the two susceptibility calls, the two Mykrobe calls and the mutation identity. The susceptibility calls are missing on identical rows, which is why they return identical coefficients, and the Mykrobe calls carry a single value wherever they are recorded in this stratum, so no model can be fitted for them and no coefficient is printed. The other two are the drug MICs, recorded for every susceptible isolate and 67 of 84 resistant ones; the isoniazid MIC separates the two groups completely, so adjusting for it conditions on a graded reading of the exposure. A negative attenuation is an amplification: the adjusted coefficient sits further from zero than the unadjusted one, which is what the isoniazid MIC does at 13 per cent. A coefficient is printed wherever one exists so the circularity is visible, but none of these seven bounds anything. Only 2 covariates are recorded at rates unrelated to susceptibility, and adjusting for either leaves the coefficient within five per cent of its unadjusted value. The file records no referring site and no processing batch, so those cannot be tested at all.

| Covariate | Recorded, resistant | Recorded, susceptible | Can it adjust? | Resistance coefficient | Attenuation |
| --- | ---: | ---: | ---: | ---: | ---: |
| INH_MGIT_DST | 82/84 | 0/119 | PROXY | -0.851 | -0% |
| RIF_MGIT_DST | 82/84 | 0/119 | PROXY | -0.851 | -0% |
| INH_mutation | 79/84 | 1/119 | PARTIAL | -0.662 | 22% |
| INH_Mykrobe | 76/84 | 0/119 | PROXY | - | - |
| RIF_Mykrobe | 76/84 | 0/119 | PROXY | - | - |
| MIC_INH | 67/84 | 119/119 | PARTIAL | -0.963 | -13% |
| MIC_RIF | 67/84 | 119/119 | PARTIAL | -0.853 | -0% |
| Time_to_0.4 | 83/84 | 119/119 | INDEPENDENT | -0.807 | 5% |
| Time_point | 84/84 | 119/119 | INDEPENDENT | -0.818 | 4% |

**Table S22.** What follows a first observed crossing below the assay floor. The state below the floor is not absorbing: a series sitting below it reads above again at the next visit with probability 0.22 overall, and that probability rises as drug pressure falls, which is what a plating artefact does. Only 56 of 360 series, 15.6 per cent, show the shape a survival model assumes -- one crossing that holds. The 360 series are four platings of each of 90 flasks and are not independent; the flask-level counts are 53 flasks with a crossing series and 42 with a returning one.

| Series | n | Visit pairs | P(above to below) | P(below to above) | Never below | One crossing, holds | One crossing, returns | Crosses repeatedly | Shape the model assumes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| all series | 360 | 2232 | 0.080 | 0.222 | 220 | 56 | 65 | 19 | 16% |
| INH 10X MIC | 72 | 441 | 0.137 | 0.065 | 34 | 27 | 6 | 5 | 38% |
| INH 1X MIC | 72 | 440 | 0.150 | 0.373 | 30 | 2 | 33 | 7 | 3% |
| MXF 10X MIC | 72 | 433 | 0.141 | 0.175 | 30 | 26 | 9 | 7 | 36% |
| MXF 1X MIC | 72 | 441 | 0.023 | 0.923 | 59 | 1 | 12 | 0 | 1% |
| untreated | 72 | 477 | 0.011 | 1.000 | 67 | 0 | 5 | 0 | 0% |


## References cited in this supplemental material

1. Vijay S, Vinh DN, Hai HT, Ha VTN, Dung VTM, Dinh TD, Nhung HN, Tram TTB, Aldridge BB, Hanh NT, Thu DDA, Phu NH, Thwaites GE, Thuong NTT. 2021. Ribosomal protein S1 is required for growth and antibiotic tolerance in Mycobacterium tuberculosis. Antimicrob Agents Chemother 65:e00429-21.

2. Vijay S, Bao NLH, Vinh DN, Nhat LTH, Thu DDA, Quang NL, Trieu LPT, Nhung HN, Ha VTN, Thai PVK, Ha DTM, Lan NH, Caws M, Thwaites GE, Javid B, Thuong NT. 2024. Rifampicin tolerance and growth fitness among isoniazid-resistant clinical *Mycobacterium tuberculosis* isolates from a longitudinal study. Elife 13:RP93243. https://doi.org/10.7554/eLife.93243.

3. van Wijk RC, Lucía A, Sudhakar PK, Sonnenkalb L, Gaudin C, Hoffmann E, Dremierre B, Aguilar-Ayala DA, Dal Molin M, Rybniker J, de Giorgi S, Cioetto-Mazzabò L, Segafreddo G, Manganelli R, Degiacomi G, Recchia D, Pasca MR, Simonsson USH, Ramón-García S. 2023. Implementing best practices on data generation and reporting of *Mycobacterium tuberculosis* in vitro assays within the ERA4TB consortium. iScience 26:106411. https://doi.org/10.1016/j.isci.2023.106411.

4. Rabodoarivelo MS, Hoffmann E, Gaudin C, Aguilar-Ayala DA, Galizia J, Sonnenkalb L, Dal Molin M, Cioetto-Mazzabò L, Degiacomi G, Recchia D, Rybniker J, Manganelli R, Pasca MR, Ramón-García S, Lucía A. 2025. Protocol to quantify bacterial burden in time-kill assays using colony-forming units and most probable number readouts for *Mycobacterium tuberculosis*. STAR Protoc 6:103643. https://doi.org/10.1016/j.xpro.2025.103643.

5. Yamada WM, Schumitzky A, Kryshchenko A, Otalvaro J, Kim S, Louie A, Drusano GL, Neely MN. 2026. Analyzing pharmacodynamic count data that rapidly decrease to zero. CPT Pharmacometrics Syst Pharmacol 15(1). https://doi.org/10.1002/psp4.70140.

6. March VFA, Mchedlishvili K, Goig GA, Maghradze N, Avaliani T, Aspindzelashvili R, Avaliani Z, Kipiani M, Tukvadze N, Jugheli L, Bouaouina S, Doetsch A, Kalkan S, Reinhardt M, Gagneux S, Borrell S. 2025. Within-host evolution of drug tolerance in *Mycobacterium tuberculosis*. bioRxiv 2025.07.29.667394; preprint, not peer reviewed. https://doi.org/10.1101/2025.07.29.667394.

7. National Committee for Clinical Laboratory Standards. 1999. Methods for determining bactericidal activity of antimicrobial agents; approved guideline. NCCLS document M26-A. National Committee for Clinical Laboratory Standards, Wayne, PA. ISBN 1-56238-384-1.

8. Balaban NQ, Helaine S, Lewis K, Ackermann M, Aldridge B, Andersson DI, Brynildsen MP, Bumann D, Camilli A, Collins JJ, Dehio C, Fortune S, Ghigo J-M, Hardt W-D, Harms A, Heinemann M, Hung DT, Jenal U, Levin BR, Michiels J, Storz G, Tan M-W, Tenson T, Van Melderen L, Zinkernagel A. 2019. Definitions and guidelines for research on antibiotic persistence. Nat Rev Microbiol 17:441-448. https://doi.org/10.1038/s41579-019-0196-3.

9. Vijay S, Bao NLH, Vinh DN, Nhat LTH, Thu DDA, Quang NL, Trieu LPT, Nhung HN, Ha VTN, Thai PVK, Ha DTM, Lan NH, Caws M, Thwaites GE, Javid B, Thuong NT. 2024. Supplementary file 2 to "Rifampicin tolerance and growth fitness among isoniazid-resistant clinical *Mycobacterium tuberculosis* isolates from a longitudinal study" (elife-93243-supp2-v1.xlsx). eLife. https://doi.org/10.7554/eLife.93243.

10. Evangelopoulos D, Prosser G, Rodgers A, Dagg B, Khatri B, Bhagwat A, Gonzalo X, Kolyva A, Bertozzi G, Silva-Pereira TT, Gibbons N, Bhatt A, Sabharwal N, Perdigao J, Portugal I, Rodrigues C, Duarte R, Gomes M, Cirillo DM, McHugh TD. 2022. Data from: Comparative evaluation of viable count, molecular bacterial load and most probable number for the enumeration of Mycobacterium tuberculosis in murine tissue. University College London Research Data Repository. https://doi.org/10.5522/04/19175153.v2. Retrieved 2026-09-07.

11. van Wijk RC, Solans BP, Chaba L, Sordello S, Upton AM, Nuermberger EL, Robertson GT, Walter ND, Savic RM. 2026. Predicting tuberculosis relapse based on 28-day CFU, RS ratio, and/or drug contribution for novel regimens in the relapsing mouse model. bioRxiv 2026.07.27.740024, version 1, posted 30 July 2026; preprint, not peer reviewed. https://doi.org/10.64898/2026.07.27.740024.

12. Lai RPJ, Ammerman NC, Tasneen R, Almeida DV, Converse PJ, Nuermberger EL. 2023. Using dynamic oral dosing of rifapentine and rifabutin to simulate exposure profiles of long-acting formulations in a mouse model of tuberculosis preventive therapy. Antimicrob Agents Chemother 67:e00481-23. https://doi.org/10.1128/aac.00481-23.

13. Tabor ST, Friesen AD, Reichlen MJ, Dide-Agossou C, McGrath M, Peterson R, Ganusov VV, Robertson GT, Voskuil MI, Walter ND. 2025. Mind the gap: understanding discordance between culture- and a non-culture-based measure of bacterial burden in murine tuberculosis treatment models. bioRxiv posted 18 December 2025; preprint, not peer reviewed. https://github.com/SamuelTaborCU/Mtb-16S-rRNA-vs-CFU.

14. Brauner A, Fridman O, Gefen O, Balaban NQ. 2016. Distinguishing between resistance, tolerance and persistence to antibiotic treatment. Nat Rev Microbiol 14:320-330. https://doi.org/10.1038/nrmicro.2016.34.

15. Windels EM, Cool L, Persy E, Swinnen J, Matthay P, Van den Bergh B, Wenseleers T, Michiels J. 2024. Antibiotic dose and nutrient availability differentially drive the evolution of antibiotic resistance and persistence. ISME J 18:wrae070. https://doi.org/10.1093/ismejo/wrae070.

16. Windels EM, Cool L, Persy E, Swinnen J, Matthay P, Van den Bergh B, Wenseleers T, Michiels J. 2024. Data supporting "Antibiotic dose and nutrient availability differentially drive the evolution of antibiotic resistance and persistence". Zenodo. https://doi.org/10.5281/zenodo.7550302.

17. Pym AS, Saint-Joanis B, Cole ST. 2002. Effect of *katG* mutations on the virulence of *Mycobacterium tuberculosis* and the implication for transmission in humans. Infect Immun 70:4955-4960. https://doi.org/10.1128/IAI.70.9.4955-4960.2002.

18. van Soolingen D, de Haas PEW, van Doorn HR, Kuijper E, Rinder H, Borgdorff MW. 2000. Mutations at amino acid position 315 of the *katG* gene are associated with high-level resistance to isoniazid, other drug resistance, and successful transmission of *Mycobacterium tuberculosis* in the Netherlands. J Infect Dis 182:1788-1790. https://doi.org/10.1086/317598.

19. Turnbull BW. 1976. The empirical distribution function with arbitrarily grouped, censored and truncated data. J R Stat Soc Series B Stat Methodol 38:290-295. https://doi.org/10.1111/j.2517-6161.1976.tb01597.x.

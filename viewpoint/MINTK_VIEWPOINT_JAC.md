# Minimum information for a time-kill assay (MINTK): a five-field reporting standard for antibiotic killing endpoints

**Article type:** Viewpoint (Journal of Antimicrobial Chemotherapy)
**Author:** Vahhab Piranfar
**Status:** Draft v1 — preprint DOI placeholder at [PREPRINT]; body ~1,170 words (Viewpoint limit to be confirmed against the current JAC Guide for Authors)

---

Every clinical microbiologist knows that a culture taken after antibiotics have
started is not evidence of sterility. The field's answer was to stop asking
whether a culture went negative and to ask how far it fell: a surviving
fraction of the starting population, or a minimum duration for killing (MDK)
derived from it, precisely so that the starting population could not
matter.[1–3] It does not matter in the definition. It starts to matter the
moment killing reaches the assay's floor, and nothing in the way we report
killing assays warns the reader that this has happened.

The arithmetic is short. Every assay has a floor *L*: one colony in a plated
volume *v* µL is *L* = 1000/*v* per mL, and a most-probable-number (MPN)
series bottoms out at the lowest rung of its table.[4,5] An endpoint that asks
for a *q*-log reduction is visible only when the starting density *N*₀ sits at
or above *L*·10^*q*; the distance log10(*N*₀/*L*) — the headroom — is fixed by
the dilution scheme and the inoculum before any drug acts. And when the last
reading sits at *L*, the recorded surviving fraction is *L*/*N*₀: an upper
bound on survival, not a measurement of it, and a monotone function of the
starting density the endpoint was designed to cancel. None of this is a
biological claim. It is what a censored reading is.

## What the literature actually reports

These quantities are interpretable only if the reader is told four things:
where the culture started, where the assay stops, what is written when nothing
grows, and how the endpoint is computed. We assembled 78 published time-kill
datasets and inspected the 40 distinct literature deposits among them in
full.[12] Thirty-two of the 40 — four in five — state no assay floor by any
route: not as a validated limit, not as a plated volume from which one can be
derived, not as a dilution design from which one can be inferred. Their
endpoints cannot be recomputed against their own measurement. This is not a
fringe problem confined to one organism or one journal; it is the median
practice of the field.

Consortia have noticed. The ERA4TB consortium published best-practice
guidance for generating and reporting *M. tuberculosis* in-vitro assay
data,[6] and a recent protocol pairs CFU and MPN readouts in a single
time-kill design.[7] These are welcome, but they are guidance written by a
consortium for its own pipeline. What does not exist is the microbiology
equivalent of what MIAME gave microarrays:[8] a minimum set of fields, small
enough to fit in a box, that any author can complete, any reviewer can check,
and any journal can require by reference. We propose it here.

## The five fields

**Table 1. Minimum information for a time-kill assay (MINTK).** Each field is
produced by the experiment as run; none requires new apparatus.

| # | Field | What to report | What fails without it |
|---|---|---|---|
| 1 | Starting density | *N*₀ with its method (viable count or MPN value, not an optical density) | the endpoint is a fraction of *N*₀; in our own prospective experiment the nominal, OD-standardised inoculum differed from the measured viable count by more than ten-fold |
| 2 | Assay floor | *L* as a value, or the plated volume / dilution design that fixes it | nothing deeper than log10(*N*₀/*L*) was ever visible; without *L* a "failed" endpoint is arithmetic, not biology |
| 3 | Censoring convention | what is written when nothing grows: zero, the floor value, ND, or the lowest table rung | the convention decides whether a floor reading is a bound or a measurement |
| 4 | Endpoint rule | the *q* in MDK_q and the interpolation between sample times | one kill curve returns different durations under different rules |
| 5 | Physiological state | culture age or growth phase at sampling, as a recorded value | tolerance tracks growth state;[9,10] unrecorded, state confounds every group compared |

## What the fields prevent: three documented failure modes

**The unreachable endpoint.** In a reanalysis of 217 clinical
*M. tuberculosis* isolates classified for rifampicin tolerance,[11,12] 33
lacked the headroom to demonstrate the 99.99 per cent kill the classification
uses — and all 33 are recorded as having failed it. A reader given fields 1
and 2 sees immediately that the deepest endpoint was never visible for these
isolates; a reader given the classification alone sees 33 treatment-relevant
phenotypes that exist only as arithmetic.

**The floor that is not a bound.** Field 3 matters more than it looks. For a
blank plate, a floor reading bounds the true count from above. For an MPN
reading it does not: the lowest rung is a maximum-likelihood estimate from a
well pattern, and under the design of the deposit just mentioned the 95 per
cent profile interval at that rung extends from about 3 to 120 per mL — the
point estimate is 23.[5,12,13] Treating such a reading as a count in [0, *L*]
is wrong in the optimistic direction, and the error propagates into every
surviving fraction and MDK computed from it. Reporting the censoring
convention, and the dilution design behind an MPN floor, is what allows a
reader to price this.

**The label the pipette assigns.** In a prospective experiment built to test
these boundaries,[12] the same culture at the standard inoculum could
demonstrate 3.71–3.93 log10 of killing when plated at 10 µL and 4.88–5.05 when
plated at 100 µL; at a tolerance threshold of 10⁻³, six of 54 sample-times
took two different labels from one culture depending only on the plating.
Across the volumes laboratories actually use, 100 down to 2.5 µL, the
demonstrable depth of an assay moves by 1.60 log10 as exact arithmetic.
Fields 2 and 4 turn these from hidden artefacts into stated design choices.

## What adoption costs, and who acts

Nothing in the five fields requires a new measurement. Fields 1, 2 and 5 are
produced by the experiment as run; field 3 is a sentence; field 4 is a line in
the Methods. The cost is deliberately MIAME-like: minimal fields, maximal
checkability.[8] Three groups can act on it independently. Authors can include
the fields as a five-row table in every killing-assay paper — and can compute
field 2's consequences before the experiment rather than after it (an open
command-line tool that returns headroom, reachable endpoints and the minimum
plated volume a target endpoint needs is released with reference [12]).
Reviewers can ask for the fields by name, which is cheaper than asking for new
experiments. Editors and funders can require the table by reference, exactly
as they required structured abstracts and trial registration: not as a new
method to learn, but as a condition of interpretation.

A tolerance call reported without its starting density and its assay floor
cannot be interpreted — it can only be believed. Five fields make it
interpretable. The literature's current answer to that proposal is visible in
the screen above: four in five published datasets already fail it, which is
not an argument against the standard but the reason for it.

## References

1. Brauner A, Fridman O, Gefen O, Balaban NQ. Distinguishing between
   resistance, tolerance and persistence to antibiotic treatment. *Nat Rev
   Microbiol* 2016; **14**: 320–30.
2. Balaban NQ, Helaine S, Lewis K et al. Definitions and guidelines for
   research on antibiotic persistence. *Nat Rev Microbiol* 2019; **17**:
   441–8.
3. Brauner A, Shoresh N, Fridman O, Balaban NQ. An experimental framework for
   quantifying bacterial tolerance. *Biophys J* 2017; **112**: 2664–71.
4. National Committee for Clinical Laboratory Standards. *Methods for
   Determining Bactericidal Activity of Antimicrobial Agents; Approved
   Guideline*. NCCLS document M26-A. Wayne, PA: NCCLS, 1999.
5. Blodgett R. BAM Appendix 2: Most probable number from serial dilutions.
   *Bacteriological Analytical Manual*. Silver Spring, MD: US Food and Drug
   Administration, 2023.
6. van Wijk RC, Lucía A, Sudhakar PK et al. Implementing best practices on
   data generation and reporting of *Mycobacterium tuberculosis* in vitro
   assays within the ERA4TB consortium. *iScience* 2023; **26**: 106411.
7. Rabodoarivelo MS, Hoffmann E, Gaudin C et al. Protocol to quantify
   bacterial burden in time-kill assays using colony-forming units and most
   probable number readouts for *Mycobacterium tuberculosis*. *STAR Protoc*
   2025; **6**: 103643.
8. Brazma A, Hingamp P, Quackenbush J et al. Minimum information about a
   microarray experiment (MIAME)—toward standards for microarray data. *Nat
   Genet* 2001; **29**: 365–71.
9. Vijay S, Bao NLH, Vinh DN et al. Rifampicin tolerance and growth fitness
   among isoniazid-resistant clinical *Mycobacterium tuberculosis* isolates
   from a longitudinal study. *eLife* 2024; **13**: RP93243.
10. March VFA, Mchedlishvili K, Goig GA et al. Within-host evolution of drug
    tolerance in *Mycobacterium tuberculosis*. *bioRxiv* 2025;
    doi:10.1101/2025.07.29.667394 [preprint].
11. Vijay S, Nhung HN, Bao NLH et al. Most-probable-number-based minimum
    duration of killing assay for determining the spectrum of rifampicin
    susceptibility in clinical *Mycobacterium tuberculosis* isolates.
    *Antimicrob Agents Chemother* 2021; **65**: e01439-20.
12. Piranfar V. The detection floor bounds tolerance endpoints in
    *Mycobacterium tuberculosis*. *bioRxiv* [PREPRINT DOI — insert at
    submission]; analysis code and the command-line tool:
    https://github.com/[REPO].
13. Cochran WG. Estimation of bacterial densities by means of the "most
    probable number". *Biometrics* 1950; **6**: 105–16.

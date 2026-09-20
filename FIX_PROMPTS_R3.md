# Fix prompts — R3, TB-core

Verified against the repo at `E:\Research\Modeling of Antibiotic Resistance`, commit `7722ac3`.

## What changed after checking the data

Three findings from the document-only review moved once the pipeline was readable:

| Finding | Document-only verdict | After reading the repo |
|---|---|---|
| A1 — §8 floor switch | suspected | **Confirmed, and worse.** `3.81` occurs in no results file or receipt. `exp38_headroom_by_flask.csv` uses `floor_100ul = 5.0` throughout; the arm-mean headroom at that floor is **4.109**, so the four-log endpoint is *reachable* and the paragraph's contrast collapses. `exp38_boundary_experiment.py:159` carries the comment *"arm-mean headroom mixes one flask's numerator with another's denominator"* — the script deliberately refuses to compute the number the prose quotes. |
| A2 — circular boundary test | suspected circular | **Withdrawn. The paper is right.** 46 isolates have a recorded fraction of exactly 1e-3; **40 of them are not at the floor** (day-5 readings of 230, 2300, 6100, 23000). `c₁` is pinned by measured isolates, independently of the six. Needs a defensive sentence, not a fix. |
| A6 — corpus accounting | irreconcilable | **Resolved, root cause found.** See P5. |

Three new findings the documents could not show: **N1** (seven species is six), **N2** (receipts record no software versions), **N3** (a stale supplement file).

## Build architecture — read before editing

```
manuscript/MANUSCRIPT.md        <- SOURCE OF TRUTH. Article + supplementary text in one file.
manuscript/abstract.md          <- abstract
manuscript/tables.md            <- main tables
        |
        v  src/assemble_paper.py            -> manuscript/PAPER_COMPLETE.md
        v  src/build_submission.py          -> SUBMISSION_MAIN.md + SUBMISSION_SUPPLEMENT.md
        |     ^ contains the ROUTING TABLE: the main/supplement split lives here
        v  src/audit_claims.py, src/audit_manuscript.py
        v  src/build_submission_package.py, src/build_docx.py  -> submission/*.docx
```

Edit `MANUSCRIPT.md`, never the generated files. `run_all.py` runs the whole chain.

`manuscript/SUPPLEMENTAL_MATERIAL.md` is written by `src/build_supplement.py` and **read by nothing** — see P10.

Line numbers below are current as of `7722ac3`. Match on quoted text, not line number.

---

# P0 — Orientation (run once, before the rest)

```
You are working in the repository at E:\Research\Modeling of Antibiotic Resistance,
the analysis and manuscript pipeline for "The detection floor bounds tolerance
endpoints in Mycobacterium tuberculosis" (sole author Vahhab Piranfar).

Read these first and report back what you find, without changing anything:
  - run_all.py                        the full pipeline and its stage order
  - src/build_submission.py           especially the ROUTING TABLE that decides
                                      which sections go to the main text and
                                      which go to the supplement
  - src/assemble_paper.py             how MANUSCRIPT.md becomes PAPER_COMPLETE.md
  - src/audit_claims.py               the value audit
  - src/audit_manuscript.py           the legend/box/abstract audit
  - manuscript/MANUSCRIPT.md          the prose source of truth

Then tell me:
  1. The exact stage order run_all.py executes, and which stages write into
     manuscript/ versus results/.
  2. The routing table's current main/supplement assignment, section by section.
  3. Which files under manuscript/ are hand-edited sources and which are
     generated outputs that must never be edited directly.
  4. Whether `python run_all.py` runs clean on this machine right now. If a
     dependency is missing, report which, and do not install anything yet.

Do not modify any file in this task.
```

---

# P1 — TB-core restructure

This is the structural decision. Do it before the content fixes so the later edits land in their final location.

```
GOAL: make Mycobacterium tuberculosis the pillar of the article without deleting
any evidence, and bring the article to a tuberculosis journal's length.

CONTEXT: the title names M. tuberculosis, but Results sections 7 and 8 are both
Escherichia coli — the held-out Dubey hollow-fibre deposit and the prospective
ciprofloxacin experiment. A referee will read the title as overclaiming, and
eight numbered Results sections is long for the target venue.

DO THIS:

1. In manuscript/MANUSCRIPT.md, merge current Results sections 7 and 8 into a
   single section, placed last and numbered 7, with the heading:

     "7. The same boundaries hold outside the organism they were derived in"

   Open it with two sentences that frame both E. coli results as out-of-organism
   controls on arithmetic that is organism-independent by construction — not as
   independent biological findings. Keep these load-bearing numbers in the main
   text and move the rest of both sections' detail to the supplement:
     - headroom 4.85 to 5.45 log10 across the 20 Dubey cultures
     - a 5-log endpoint unreachable for 5 of 20, a 6-log endpoint for all 20
     - the nominal-vs-measured inoculum gap (1e5 stated, median 1.215e6 measured)
     - at the standard inoculum, per flask: 10 uL ceilings 3.71-3.93 logs and
       100 uL ceilings 4.88-5.05 logs
     - six of 54 sample-times taking two labels from one culture at c1 = 1e-3

2. Promote Table S3 (the five M. tuberculosis deposits whose floor could be
   established; 184 of 310 series short of four logs, 240 of 310 short of five)
   into the main text as a numbered table. It is the strongest TB-generalisation
   evidence in the paper and it is currently buried in the supplement. Renumber
   the main tables and every cross-reference to them.

3. Update src/build_submission.py's ROUTING TABLE to match the new section
   structure. Do not hand-edit SUBMISSION_MAIN.md or SUBMISSION_SUPPLEMENT.md.

4. Rebalance manuscript/abstract.md toward TB. It currently spends its last two
   sentences on the E. coli experiment. Keep the 10 uL / 100 uL result and the
   1.60 log10 volume arithmetic, but lead the closing with the TB corpus figure
   from Table S3 rather than with E. coli. Keep the abstract at or under 250
   words — it is currently 291. Report the new count.

5. Do NOT change the title.

ACCEPTANCE:
  - `python run_all.py` completes and both audit stages pass.
  - The article has 7 numbered Results sections, 6 of which are TB.
  - Every cross-reference to a renumbered table resolves.
  - abstract.md is <= 250 words.
  - Report the new main-text word count (Introduction through Conclusion); it
    was 6,062.
```

---

# P2 — A1: the §8 floor switch (highest priority)

```
BUG: a headroom figure in the prose contradicts the pipeline that is supposed to
generate every number in this paper.

EVIDENCE:
  - results/tables/exp38_headroom_by_flask.csv has floor_100ul = 5.0 for all
    nine flasks. That is the pooled duplicate-plate floor: two 100 uL plates read
    together are 200 uL of sample, so one colony across the pair is 5 CFU/mL.
    The supplement's "The floor, and why duplicate plating moves it" says exactly
    this.
  - The LOW arm's three flasks have n0_100ul of 78000, 65000, 50000 and
    headroom_100ul of 4.193, 4.114, 4.000 — all computed at L = 5.
  - The arm-mean N0 is 64,333, so the arm-mean headroom at L = 5 is 4.109.
  - manuscript/MANUSCRIPT.md line 1048 says: "Taking the low arm as a single
    number gives it 3.81 logs of headroom at the 100 uL plating and rules the
    four-log endpoint out; taking its three flasks one at a time gives 4.19, 4.11
    and 4.00, and rules it in for all three. The arithmetic is the same and the
    answer is opposite".
  - 3.81 is log10(64333/10) — it uses the SINGLE-plate floor L = 10, while every
    other number in that paragraph uses L = 5. At a consistent floor the verdict
    does not flip:
        L = 5   arm mean 4.11   per flask 4.19, 4.11, 4.00   -> reachable, all
        L = 10  arm mean 3.81   per flask 3.89, 3.81, 3.70   -> unreachable, all
  - The string "3.81" appears in NO file under results/. It is prose-only.
  - src/experiments/exp38_boundary_experiment.py line 159 carries the comment
    "arm-mean headroom mixes one flask's numerator with another's denominator" —
    the script deliberately declines to compute this quantity.

DO THIS:
  Rewrite that paragraph in manuscript/MANUSCRIPT.md so the point it makes is the
  one the data support. The defensible point is NOT that averaging flips the
  verdict — at a fixed floor it does not. The defensible points are:
    (a) N0 is a per-flask measurement, not a protocol setting: the two platings
        of one culture disagree about it by 0.74- to 1.53-fold (Table S7), so
        headroom inherits that error; and
    (b) at the standard inoculum the four-log endpoint is unreportable at the
        10 uL plating and comfortable at 100 uL in the same flask on the same
        afternoon — which is the section's actual claim and is fully supported.
  Delete the 3.81 figure and the "the answer is opposite" construction. Do not
  substitute another hand-computed number: quote only values that exist in
  results/tables/exp38_headroom_by_flask.csv.

  If you judge that an arm-level figure is still worth reporting, add it to
  exp38_boundary_experiment.py so it lands in a results table with its floor
  stated in the column name, and remove the script's refusal comment. Do not
  leave a number in the prose that the pipeline does not produce.

ACCEPTANCE:
  - `grep -rn "3\.81" manuscript/MANUSCRIPT.md` returns nothing.
  - Every numeric literal in that paragraph traces to a row of
    results/tables/exp38_headroom_by_flask.csv or exp38_threshold_sweep.csv.
  - src/audit_claims.py passes.
```

---

# P3 — A2: pre-empt the circularity objection (the paper wins this one)

```
CONTEXT: Results section 3 says the six isolates sitting at exactly N_id are "a
test the arithmetic could have failed and did not", two paragraphs after
conceding that the wider agreement is "an identity rather than a passed test".

A referee will object that the convention placing c1 = 1e-3 in MEDIUM rather than
in LOW was itself recovered from this file (Table S2), and therefore cannot fail
on the six isolates it was recovered from. That objection is answerable, and the
answer is in the data — but the paper does not currently give it.

THE ANSWER, verified against data/processed/tidy_vijay.csv, 15-day panel, day 5:
  - 46 isolates have a recorded fraction of exactly 1.000e-3.
  - 40 of the 46 are NOT at the floor: their day-5 MPN readings are 230, 2300,
    6100 and 23000, all well above the floor of 23.
  - All 46 are labelled Medium.
  - Observed class boundaries: Low max 4.694e-4, Medium min 1.000e-3.
  So the inclusive-at-c1 convention is pinned by 40 isolates with a measured,
  uncensored numerator, independently of the six floored ones.

DO THIS:
  1. Add a computation to src/experiments/exp25_observability_classes.py (or the
     script that recovers the thresholds) that emits, to a results table:
     the count of isolates at exactly c1, split by whether the day-5 reading is
     at the floor. Verify it reproduces 46 total and 40 not-at-floor.
  2. Add one or two sentences to Results section 3 in manuscript/MANUSCRIPT.md,
     immediately after the boundary-case paragraph, stating that figure and what
     it licenses: the threshold convention is fixed by isolates whose numerator
     the assay measured, so the boundary case is a genuine test rather than a
     restatement of how c1 was recovered. Cite the new table.
  3. Do not overclaim. The sentence establishes independence of the convention;
     it does not turn the wider agreement into a test, and the existing "identity
     rather than a passed test" concession must stay exactly as it is.

ACCEPTANCE:
  - The new counts appear in a results table and in the prose.
  - src/audit_claims.py traces both numbers.
```

---

# P4 — A3: an MPN floor is not a plate-count floor

This is the one genuinely open scientific gap. It needs new analysis, not an edit.

```
PROBLEM: the identifiability boundary sweeps the true count across the interval
[0, L] and concludes that for twelve of the eighteen floored isolates only the
lowest class is compatible. That interval is correct for a plate count, where a
blank plate means "fewer than one colony in the volume plated".

It is not correct for a most probable number. A 3-tube MPN reading at the lowest
positive rung (23 per mL) is a maximum-likelihood point estimate from a tube
pattern, and its confidence interval extends well ABOVE 23 — roughly 7 to 130 per
mL for a standard 3-tube series. The true density at a floor reading is therefore
not bounded above by L.

The existing floor posterior in "Floor posterior, refusal, and what is not
learned" answers a different question: WHICH RUNG is the floor. It does not
address the width of the MPN estimate at that rung.

CONSEQUENCE IF THE OBJECTION HOLDS: more than six of the eighteen become
undecidable, because the compatible interval reaches further above c1. That
strengthens the identifiability argument in general while breaking the clean
12/6 split the paper leans on in Results sections 2, 3 and Table 2.

DO THIS:
  1. Write a new experiment script, src/experiments/exp44_mpn_interval.py, that
     replaces the [0, L] sweep with the MPN likelihood at the lowest positive
     rung for the deposit's dilution scheme. Recompute, for each of the eighteen
     floored isolates in the 15-day panel:
       - the set of tolerance classes compatible with the reading under the
         [0, L] assumption (should reproduce 12 single / 6 multiple), and
       - the set compatible under the MPN interval at the observed rung, at both
         a 95% and a 99% interval.
     Emit results/tables/exp44_mpn_interval.csv with one row per isolate and both
     verdicts, plus a summary row.
  2. Run the same sensitivity for the 60-day panel (currently 6 single, 0
     multiple) and for the day-2 column.
  3. Report which of the paper's counts survive, which widen, and which do not.

  4. Then add a paragraph to the supplementary Methods, in "Two kinds of limit,
     kept apart" or immediately after it, that states the distinction explicitly:
     for a volume-derived plate floor the censored reading bounds the true count
     from above; for an MPN rung it does not, and here is what that costs. Report
     the recomputed counts. If the 12/6 split does not survive, change the split
     in Results 2, 3, Table 2 and the Abstract rather than defending it.

  5. Add the corresponding row(s) to the Table S9 ledger with an honest verdict.

ACCEPTANCE:
  - The new table exists and both audits trace every number derived from it.
  - Every place the 12/6 split is quoted (Abstract, Results 2, Results 3,
    Table 2, Figure 1C legend, Conclusion) is consistent with the surviving
    figure.
  - Report to me, before editing prose, whether the split survived.
```

---

# P5 — A6 + N1: reconcile the corpus accounting

```
BUG: the screen's counts do not reconcile between the two places they are stated,
and the reason is that the code uses more floor tiers than the prose describes.

WHAT THE DATA ACTUALLY SAY:
  results/tables/corpus_coverage.csv has 45 rows.
    floor_regime: none = 36, stated by the source = 5,
                  derived from a stated plated volume = 4.
    -> the "36 of 45" and "five state a floor outright and four permit one to be
       derived" figures are correct.
    BUT only 40 of the 45 have series > 0. Five studies (BENZBROMARONE2025,
    MICHIELS2022, SOEORG2026_2, SALMONELLA2023, SOU) have zero rows, zero series
    and zero timepoints, yet sit inside the "45 whose series could be read in
    full".
    AND PIRANFAR2026 — this paper's own prospective experiment — is one of the 45
    and one of the 4 "derived".

  results/tables/exp42_corpus_boundaries.csv has 18 deposits, with SIX floor
  tiers, not three:
    STATED 4, DERIVED 4, PAPER_DERIVED 4, INFERRED 3, ABOVE_A_PLACEHOLDER 2,
    PAPER_STATED 1.
  Total 2,210 series, 0 headroom violations.

  This is the source of every inconsistency:
    - "Eighteen of the 78 carry enough for the boundaries to be computed at all"
      implies 18 published deposits, but PIRANFAR2026 is inside the count.
    - "18 permit ... 17 published deposits and this paper's own experiment"
      contradicts the sentence above.
    - Only 9 of 45 state or derive a floor, yet 18 are computable, because
      PAPER_STATED, PAPER_DERIVED and ABOVE_A_PLACEHOLDER are three further
      routes the prose never names.

  N1: the supplement says the boundaries hold "in 2 210 of 2 210 series in seven
  species". The organism column of exp42_corpus_boundaries.csv holds
  A. baumannii, E. coli (under two spellings), M. abscessus, M. tuberculosis,
  P. aeruginosa, S. pneumoniae, and "not named". That is SIX named species.

DO THIS:
  1. Decide and apply one consistent rule for whether PIRANFAR2026 belongs inside
     the screened corpus. It is this paper's own experiment and was not screened
     from the literature, so it should be excluded from the 78/45 accounting and
     reported separately. Whichever you choose, apply it in
     src/build_corpus_manifest.py and every count derived from it.
  2. Decide whether the five zero-series studies belong in the "45 whose series
     could be read in full". If they do not, correct the 45 and every proportion
     computed against it — including the Abstract's "of the 45 ... 36" and the
     Discussion's "four in five".
  3. Name all six floor tiers in the supplementary Methods, with one line each on
     what evidence each represents and why PAPER_STATED / PAPER_DERIVED /
     ABOVE_A_PLACEHOLDER are weaker than STATED / DERIVED. The prose currently
     names three. This is what makes 9 and 18 look contradictory.
  4. Fix "seven species" to the true count of named species, and say explicitly
     how series with an unnamed organism are handled.
  5. Build one flow figure or one table that carries the whole screen in one
     place: 78 candidates -> 45 readable -> tier breakdown -> 18 computable ->
     5 analysed. Every count in the Abstract, Results 4, the Discussion and the
     supplementary Methods must read off that one object.
  6. Reconcile Results section 4's "The screen reached four more M. tuberculosis
     deposits ... Across those five". Table S3 holds five deposits with floors
     13 to 200 CFU/mL, none of which is the Evangelopoulos mouse-lung deposit
     discussed immediately before. Either it is "five more" and "those five"
     excludes Evangelopoulos, or the descriptor list is wrong. Fix whichever.
  7. Table 3's five deposits and Table S3's five deposits are disjoint sets both
     called "five". Rename one so a reader cannot conflate them.

ACCEPTANCE:
  - Every corpus count in the Abstract, Results 4, the Discussion and the
    supplementary Methods traces to the single flow object.
  - src/audit_claims.py and src/audit_manuscript.py both pass.
  - No sentence claims a tier taxonomy narrower than the code's.
```

---

# P6 — N2: the receipts do not record software versions

```
BUG: a reproducibility claim in the paper is false as the repository stands.

The main text's Data availability says the repository holds "the machine-readable
receipts recording the software versions each stage ran under".

VERIFIED: all 28 files in results/receipts/ were parsed. Not one carries a key
naming a Python version, a package version, a platform or an environment.
`grep -rn "platform.python_version\|__version__\|importlib.metadata\|pkg_resources"
src/ --include=*.py` returns nothing — no code writes a version anywhere.

Separately, the supplementary Methods state "Analyses used Python 3.14 with numpy
2.5.0, scipy 1.18.0, pandas 3.0.3, statsmodels 0.15.0 and lifelines 0.30.3".
requirements.txt pins numpy==2.5.0, so that sentence reports the PINS, not what
actually executed. A referee who checks will find the claim unsupported.

DO THIS:
  1. Add a shared helper — src/receipt.py, or extend whatever writes the receipts
     — that stamps every receipt with: platform.python_version(),
     platform.platform(), the UTC timestamp already present, the git commit SHA,
     and the resolved version of each of numpy, scipy, pandas, statsmodels and
     lifelines read at runtime via importlib.metadata.version().
  2. Re-run the full pipeline so every receipt carries the stamp.
  3. Rewrite the supplementary Methods sentence so it states the versions the
     receipts record, and says the receipts are the authority. If the versions
     that actually run differ from the requirements.txt pins, report the
     difference to me before editing the sentence.
  4. Make src/audit_manuscript.py fail the build if the versions named in the
     prose disagree with the versions in the receipts.

ACCEPTANCE:
  - Every file in results/receipts/ has a version block.
  - The prose sentence and the receipts agree, enforced by the audit.
```

---

# P7 — B-list: the numeric discrepancies, all resolved against results

Each of these is settled; the prompt just applies the settled value.

```
Apply these seven corrections in manuscript/MANUSCRIPT.md (the prose source of
truth — never edit SUBMISSION_MAIN.md, SUBMISSION_SUPPLEMENT.md or
PAPER_COMPLETE.md). Match on quoted text, not line number. Then re-run the
pipeline and both audits.

1. Table S5 legend: "The two censoring estimators agree to 0.003 log10 per day."
   WRONG. Computed from results/tables/exp17_kill_rates.csv, the maximum
   |kill_rate_tobit - kill_rate_mi| is 0.00628, at Institute A in the
   MXF 10x MIC arm — the same value whether taken over all 30 cells or over the
   six MXF 10x cells alone. The main text's 0.006 is correct. Change the legend
   to 0.006 and make it read off the results file, not a hand-typed constant.

2. Line ~639: "Across all 30 laboratory-by-arm cells".
   WRONG. exp17_kill_rates.csv has 30 rows but only 29 carry a fitted tobit rate,
   which Table S1 already states ("Of the 30 laboratory-by-arm cells, 29 retain
   enough quantified readings to fit a rate"). Change to 29 and keep the 30 as
   the denominator if you want both.

3. Same sentence cites "(Fig. 2A, Table S5)" for a claim spanning all cells, but
   Figure 2A and Table S5 show only the moxifloxacin 10x arm (6 cells). Either
   scope the sentence to that arm or cite the table that carries all 29.

4. Line ~872 says the laboratory-level bootstrap on the inversion rate runs
   "between 3.0 and 71.3 per cent"; line ~1293 says "3.0 to 72.4 per cent".
   results/tables/exp31_recomputed_inference.csv gives "laboratories
   [3.01, 71.3]%". 71.3 is correct. Fix line ~1293.

5. Table S9 prints "the criterion D_A/D_B > b_A/b_B calls 83.8% of pairs
   correctly" while Text S2 and Table S12 say 84.3 per cent.
   exp31_recomputed_inference.csv shows 83.8% is the stale
   claim-as-originally-stated string and 84.3% is both the original and the
   recomputed value. The table legend does say verdicts apply to the claim as
   originally stated, but a reader sees two numbers with no signal. Update the
   stale string to 84.3%, or mark superseded figures in that column explicitly.

6. Line ~264: "Both spans are the same 4.42 log10". The displayed endpoints give
   7.79 - 3.36 = 4.43, and 7.79 - log10(23) = 6.428, which displays as 6.43 not
   the 6.42 printed. Either print one more digit on the starting densities or
   state in the legend that spans are taken on unrounded values.

7. Line ~274: "over the 203 isolates with an ordered label the same count is the
   31 quoted above". 31 is never quoted above in the article — it appears only in
   the supplement's day-2/day-5 comparison. Either introduce 31 before this
   sentence or drop the back-reference.

8. Line ~485: "(Section 2)" is cited for the 26.2% vs 7.6% headroom figures.
   Those live in the supplement's extended results for section 2, not in article
   Section 2. Fix the cross-reference target.

9. Supplementary Methods, six-laboratory description: "2 775 readings, of which
   17.9 per cent are flagged below the floor and 24 above it". Table S1 also uses
   24, for inoculum controls. Confirm from the deposit whether these are two
   different 24s. If they are, say so in one clause; if they are not, one of the
   two is wrong.

10. Line ~245: "The day-2 column bottoms out at 230 per mL with eighteen readings
    resting there, so L = 230 there. That is the same count as at day 5". "The
    same count" reads as the same MPN value (230 vs 23) when it means the same
    number of readings. Rewrite unambiguously.

11. Line ~682: "the Limitations set out what that permits and what it forbids" —
    no section titled Limitations exists in either document. Either add the
    heading or repoint the reference.

12. The main text quotes the adjusted resistance odds ratio (1.31, 0.67 to 2.57,
    p = 0.42) citing Table S4, but Table S4 carries only the unadjusted family
    members. Give the adjusted estimate a row or a footnote in a table. Note that
    Table S4's day-2 unadjusted row (1.295, 0.66-2.54, p = 0.4529) is close
    enough to be mistaken for it, so label both clearly.

13. Table S9's "Section" column is stale throughout: its "Section 4" rows are
    article Section 5, "Section 5" rows are article Section 6, "Section 7" rows
    are Text S2, and "Section 10" is out of range. Regenerate that column from
    the current section numbering — and note it will change again after P1.

ACCEPTANCE:
  - Every corrected value is read from a results file, not hand-typed.
  - Both audits pass.
  - `grep -n "0\.003 log10\|all 30 laboratory\|72\.4 per cent\|83\.8%\|31 quoted above"`
    in manuscript/MANUSCRIPT.md returns nothing.
```

---

# P8 — A4, A5, A7: calibrate the claims to what the ledger already concedes

```
The paper's internal ledger (Table S9) is more honest than its Abstract and
Conclusion. Three places to bring into line.

1. THE CEILING CENSUS. Results 1 and the Abstract lead with "all 33 are recorded
   as failing" to reach the deepest endpoint. results/tables/exp22_headroom.csv
   shows 33/33 = 100% against 162/184 = 88.04% for isolates that DID have the
   headroom. Table S9 correctly withdraws the Fisher test (p = 0.029957) because
   the null is arithmetically impossible. But 100% against 88% is a near-universal
   ceiling, and an Abstract that quotes only the 100% invites a referee to find
   the 88% and conclude the paper is hiding it. Put the 88.0% figure in the
   Abstract next to the census, or drop "all 33" from the Abstract and keep the
   census in Results 1 where the comparison is already stated.

2. SCOPE. The supplement states the scope plainly: 185 of 203 calls rest on a
   measured numerator, 12 are forced by the inoculum, 6 are undecidable. That
   sentence appears nowhere in the Abstract or the Conclusion, both of which read
   as indicting the classification broadly. Add one sentence carrying the 185 /
   12 / 6 split to the Abstract, and one to the Conclusion. The paper is stronger
   for being specific — being bounded is what makes the problem fixable.

3. FIGURE 2B (see also P9). Table S9 records the AUC 0.974 separation as NOT
   SUPPORTED, because the comparison is three laboratories against three and the
   smallest attainable two-sided p is 0.10. Figure 2B nonetheless draws a dashed
   vertical decision boundary and labels the two sides "crossed" and "never
   crossed", which asserts visually exactly what the ledger withdraws. Fix in P9.

ACCEPTANCE:
  - The Abstract carries both the 100% census and the 88% comparison, or neither.
  - The 185/12/6 scope appears in the Abstract and the Conclusion.
  - Report the Abstract's word count after the edit; the cap from P1 is 250.
```

---

# P9 — Figures

```
Regenerate the figures from src/figures/. Do not edit the PNGs.

FIGURE 2B — overstated. It draws a dashed vertical separator at about 4.36 log10
with the regions labelled "crossed" and "never crossed". Table S9 marks that
separation NOT SUPPORTED (six clusters, exact laboratory-level p = 0.10 is the
design floor). Either remove the separator and the region labels, or keep them
and annotate them in-panel as descriptive, with the exact test's floor stated.
The legend must not leave a reader believing a test was passed.

FIGURE 1A — the legend says the readings show "a pile-up on it rather than
tapering". The panel shows the floor bar at 18 isolates against modes of about 55
and about 71 higher up, so it does not read as a pile-up. What the panel does
show, and what the argument needs, is that nothing lies below it anywhere in the
file. Reword the legend to claim that, or add the rung-by-rung counts so the
pile-up is visible.

FIGURE 1C — the legend says n = 12 and n = 6 but only five markers are drawn,
because eight isolates overlap at 230,000 per mL and the eighteen isolates take
only five distinct starting densities. Add per-point counts, jitter, or
proportional marker area, and say in the legend that eighteen isolates occupy
five distinct starting densities.

FIGURE 1C — the annotation "recorded fraction = L/N0" collides with the x-axis
label. Move it.

FIGURE 1B — confirm the shaded band's lower edge follows the headroom curve
rather than sitting flat at y = 3. Isolates with headroom 2.0 to 3.0 are also
short of four logs and must fall inside the shaded region.

BOTH FIGURES — they bake their captions into the image and print "uL" where the
manuscript prints "µL". Several journals strip or duplicate baked captions. Move
the caption text into the Word legend and fix the micro sign, or confirm the
target journal accepts in-figure captions and make the sign consistent.

ACCEPTANCE:
  - Figures regenerate from src/figures/ via run_all.py.
  - No figure asserts a separation Table S9 withdraws.
  - src/audit_manuscript.py, which reads figure legends, passes.
```

---

# P10 — Submission mechanics and one stale file

```
1. N3 — DEAD FILE. manuscript/SUPPLEMENTAL_MATERIAL.md announces "3 supplemental
   figures and 11 supplemental tables, Table S1 to Table S11". The submitted
   supplement has 23 tables and the manuscript front matter says 23. That file is
   written by src/build_supplement.py and read by NOTHING in the pipeline — the
   live supplement is SUBMISSION_SUPPLEMENT.md, built from MANUSCRIPT.md by
   src/build_submission.py. Anyone opening SUPPLEMENTAL_MATERIAL.md gets the
   wrong document. Either delete it and src/build_supplement.py, or regenerate it
   from the live source so it cannot drift. Same question for any other orphaned
   output under manuscript/.

2. Main-text Materials and Methods is currently a pointer sentence only. AAC,
   JAC and mBio require a self-contained Methods in the article. Check
   manuscript/JMM_SUBMISSION_CHECKLIST.md and submission_routing.csv for the
   chosen venue, then move the minimum self-contained Methods back into the main
   text via the routing table in src/build_submission.py.

3. Data availability names only a GitHub URL for the analysis code and the
   prospective readings. Most journals require a DOI-bearing archive. Cut a
   Zenodo release, add the DOI, and keep GitHub as the development mirror.
   Resolve the placeholder "[The commit identifier of the submitted version is to
   be inserted at submission.]" at submission time.

4. The AI-use statement covers copy-editing and preparing the final version. The
   repository contains a large analysis pipeline, two audit scripts and a
   headroom tool. If any of that code was AI-assisted, most journals now require
   it stated. Check manuscript/AI_DISCLOSURE.md against what actually happened
   and make the manuscript statement match it.

5. The Reproducibility subsection says an audit caught "a mistake this manuscript
   made and a reviewer caught". If this is a fresh submission rather than a
   revision, "a reviewer" will confuse an editor. Check
   manuscript/RESPONSE_TO_REVIEW.md and RESPONSE_TO_REVIEW_R2.md for whether this
   is a resubmission; if it is not, reword.

6. The sentence listing "Table S10, Table S11, ... Table S23 support analyses
   reported there rather than in this article, and are listed so that every
   supplemental item is named in the manuscript" reads as mechanically satisfying
   a requirement. Cite each table where it is used, or replace the list with a
   supplementary index table.

7. Reference (6), the Evangelopoulos deposit, is cited alone. Every other dataset
   in this paper is cited as deposit plus article. Add the article.

8. Numeral style alternates for the same quantities: "Thirty-three of 217" and
   "33 isolates"; "Eighteen isolates" and "18 isolates". Pick one rule — most
   likely words below ten, numerals from ten — and enforce it in the build.

9. Ethics states no institutional affiliation, and the Methods name strain, media
   supplier and incubation but no laboratory. A wet-lab time-kill with no named
   facility is the first thing an editor will query. Add where the prospective
   experiment was performed, and a biosafety statement if the venue wants one.
   THIS IS A DECISION FOR THE AUTHOR, NOT A CODE CHANGE — flag it and stop.

ACCEPTANCE:
  - No orphaned manuscript file contradicts the submission.
  - Items 1 through 8 applied; item 9 reported back for a decision.
```

---

# P11 — Harden the audit so this class of error cannot recur

```
Every bug in P2, P6 and P7 is a number in prose that no results file produces, or
a constant hand-typed into a legend. The existing audits already state their own
blind spots in the Reproducibility subsection. Close the three that actually bit.

1. PROSE NUMERIC LITERALS. src/audit_claims.py parses table bodies. Extend it, or
   add a stage, so that every numeric literal in the Results and Discussion prose
   of manuscript/MANUSCRIPT.md must either occur in a results file or a receipt,
   or appear on an explicit allow-list of conventions (endpoint constants,
   confidence levels, section numbers, years). "3.81" would have failed this.

2. FLOOR CONSISTENCY WITHIN A PASSAGE. Add a check that, wherever a headroom
   value is quoted, the floor it was computed against is the one the generating
   table records. The P2 bug was two floors used two sentences apart.

3. LEGEND CONSTANTS. Table and figure legends currently carry hand-typed
   constants such as Table S5's "0.003". Make legends interpolate from the
   results files at build time, and have src/audit_manuscript.py fail on any
   numeric literal in a legend that is not traceable.

4. STALE CLAIM STRINGS. exp31_recomputed_inference.csv stores a
   claim-as-originally-stated string that Table S9 prints verbatim; 83.8% versus
   the current 84.3% reached the reader with no marking. Either render superseded
   figures with an explicit marker, or regenerate the claim strings from the
   current values.

5. While you are in there: exp31_recomputed_inference.csv contains a jackknife
   interval of [-26.2, 95.3]% on a proportion. It is not printed in the paper,
   but a negative lower bound on a proportion should not survive in a results
   file. Replace with an interval that respects the support, or drop the
   jackknife for that quantity and say why.

ACCEPTANCE:
  - Re-introducing "3.81 logs of headroom" into the prose fails the build.
  - Changing a legend constant by hand fails the build.
  - `python run_all.py` completes clean end to end.
```

---

## Suggested order

P0 → **P2** → **P5** → **P6** → P7 → P3 → P1 → P8 → P9 → P4 → P10 → P11.

P2, P5 and P6 first: each is a claim a referee can falsify from the repository alone. P1 before P8/P9 so the claim and figure edits land in their final section numbering. P4 last of the analysis work because it may change counts that P1 and P8 depend on — if you would rather not reopen the 12/6 split now, run P4 as a standalone sensitivity and add it to the ledger without restructuring the main claims.

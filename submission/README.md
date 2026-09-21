# Submission package

Built by `python -m src.build_submission_package` on 2026-09-21. Every file here is
a copy of something the pipeline generated; nothing in this folder is edited by
hand. Delete it and rebuild it rather than correcting a file inside it.

## What to upload

| File | What it is |
|---|---|
| `01_cover_letter.md` | Cover letter. **Fill in the date and the preprint line before sending.** |
| `02_manuscript.md` | The article. This is the file to upload as the manuscript. |
| `03_supplementary_material.md` | The supplemental file, uploaded separately. The journal takes it only at first submission. |
| `04_preferred_reviewers.md` | Three names with affiliations and verified emails, for the submission form. Not uploaded as a file. |
| `02_manuscript.docx` | The same article in Word, double-spaced and line-numbered, with each figure above its legend. For reading and marking up. Written by `src.build_docx`, which runs after this module. |
| `03_supplementary_material.docx` | The supplement in Word, as a separate document, because the journal takes it as a separate upload. |
| `figures/` | Every figure at 600 dpi, as PNG, PDF and TIFF. |

## Not for upload

| File | What it is |
|---|---|
| `reading_copy.pdf` | Article and supplement in one document, figures placed at their legends, blocks numbered for marking up. For reading and for sending to colleagues. |
| `reading_copy.html` | The same, in a browser. |

## Figures

| File | Formats | Built from |
|---|---|---|
| `figure_1_headroom_bounds_the_endpoint` | PNG, PDF, TIF | from `fig1_dynamic_range` |
| `figure_2_one_protocol_six_laboratories` | PNG, PDF, TIF | from `fig2_rate_vs_duration` |
| `figure_S1_survival_behind_figure_2` | PNG, PDF, TIF | from `figS1_survival_and_cox` |
| `figure_S2_resistance_and_tolerance_axes` | PNG, PDF, TIF | from `fig4_independence` |
| `figure_S3_a_late_endpoint_hides_the_dose` | PNG, PDF, TIF | from `fig3_endpoint_collapse` |
| `figure_S4_the_corpus_screened` | PNG, PDF, TIF | from `figS4_corpus_funnel` |
| `figure_S5_one_culture_two_platings` | PNG, PDF, TIF | from `figS5_two_platings` |
| `figure_S6_overview_of_the_methods` | PNG, PDF, TIF | from `figS6_methods_overview` |

## State of the manuscript at this build

- Manuscript audit: {'high': 0, 'medium': 0, 'low': 11}
- Article: 12,193 words
- Supplement: 23,239 words

## Still to do before this can be sent

These are the items no build can close.

1. **The target journal.** `01_cover_letter.md` is still addressed to the
   *Journal of Microbiological Methods*. The article is now built around the
   tuberculosis evidence and trimmed to a tuberculosis journal's length, so the
   letter needs its venue, its article type and its open-access clause rewritten
   for wherever it is actually going.
2. **An archived DOI** for the code and for the prospective experiment's raw
   readings, plus the commit identifier the manuscript leaves as a placeholder.
3. **The date and the preprint line** in the cover letter.

Closed since the last build, and no longer listed: the Methods for the
prospective experiment are written, and the repository name is correct at
`detection-floor-tolerance-endpoints` -- an earlier note claiming it misspelled
"persistence" was itself out of date.

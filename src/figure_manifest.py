"""
Which image belongs to which figure label, in one place.

Run:  python -m src.figure_manifest

WHY THIS FILE EXISTS. This mapping used to be copied into four modules -- the
paper assembler, the reading copy, the Word renderer and the submission package
-- and every copy had to be edited by hand whenever a figure moved. Relabelling
Figure 3 as Figure S3 broke three of the four, each differently and none of them
loudly: the assembler silently returned the legend unembedded, the reading copy
reported FIGURES NOT PLACED, the package wrote the file under its old name, and
the Word renderer skipped the image. A figure nobody cites is the reverse of a
dangling reference, and no checker was looking for it.

So the mapping lives here and each consumer asks for the shape it needs. Moving
a figure between the article and the supplement is one edit now -- its label --
and check() reports any disagreement between this file, the prose and the images
on disk rather than leaving it to be noticed.

The label is what the legend says: "1" for **Figure 1.**, "S3" for **Figure S3.**
The stem is the file the plotting script writes into results/figures/. The slug
names the copy that goes to the journal, so the package is readable by someone
who did not build it.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGDIR = ROOT / "results" / "figures"
PROSE = ROOT / "manuscript" / "MANUSCRIPT.md"

#        label  image stem                  name in the submission package
FIGURES = [
    ("1",  "fig1_dynamic_range",     "headroom_bounds_the_endpoint"),
    ("2",  "fig2_rate_vs_duration",  "one_protocol_six_laboratories"),
    ("S1", "figS1_survival_and_cox", "survival_behind_figure_2"),
    ("S2", "fig4_independence",      "resistance_and_tolerance_axes"),
    ("S3", "fig3_endpoint_collapse", "a_late_endpoint_hides_the_dose"),
    ("S4", "figS4_corpus_funnel",    "the_corpus_screened"),
    ("S5", "figS5_two_platings",     "one_culture_two_platings"),
]

# fig13_parameter_transfer belongs to the published-rate-constant comparison,
# which is no longer part of this paper. It stays in results/ as a record of the
# work; it is neither embedded nor listed as supplementary.


def image_map() -> dict[str, str]:
    """{label: stem} for every figure, article and supplemental alike."""
    return {label: stem for label, stem, _ in FIGURES}


def article() -> dict[str, str]:
    """{label: stem} for the figures that belong to the article."""
    return {l: s for l, s, _ in FIGURES if not l.startswith("S")}


def supplemental() -> dict[str, str]:
    """{label: stem} for the figures that belong to the supplement."""
    return {l: s for l, s, _ in FIGURES if l.startswith("S")}


def package_names() -> list[tuple[str, str]]:
    """[(name in the submission package, stem)], in label order."""
    return [(f"figure_{label}_{slug}", stem) for label, stem, slug in FIGURES]


def check(prose: str | None = None) -> list[str]:
    """Every disagreement between this file, the prose and the images on disk."""
    problems: list[str] = []
    text = prose if prose is not None else (
        PROSE.read_text(encoding="utf-8") if PROSE.exists() else "")
    in_prose = set(re.findall(r"^\*\*Figure (S?\d+)\.", text, re.M))
    listed = {label for label, _, _ in FIGURES}
    for label in sorted(listed - in_prose):
        problems.append(f"Figure {label} is listed here but no legend in the "
                        f"prose opens with it")
    for label in sorted(in_prose - listed):
        problems.append(f"the prose carries a legend for Figure {label}, which "
                        f"this manifest does not list")
    for label, stem, _ in FIGURES:
        if not (FIGDIR / f"{stem}.png").exists():
            problems.append(f"Figure {label} maps to {stem}.png, which is not "
                            f"in results/figures")
    return problems


def main() -> int:
    print(f"{len(FIGURES)} figures: "
          f"{', '.join(article())} in the article, "
          f"{', '.join(supplemental())} in the supplement")
    for label, stem, slug in FIGURES:
        print(f"   Figure {label:<3} {stem:<26} figure_{label}_{slug}")
    problems = check()
    for p in problems:
        print(f"   ! {p}")
    if not problems:
        print("   manifest, prose and images agree")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())

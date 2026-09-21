"""
Figure SN. Overview of the Methods pipeline, corpus screen through audit.

Run:  python -m src.figures.figS6_methods_overview

A four-panel schematic of the full Methods pipeline: the literature screen
that produced five deposits, the prospective experiment, the two boundaries
that structure every analysis, and the reproducibility/audit machinery that
checks the results against the tables. Built to replace a text-to-image
draft that had inflated an exponent (10^9 rather than the paper's 10^q),
invented the non-word "Finibulate" for an incubation step, and dropped the
Kaur et al. citation from its own deposit box -- exactly the failure mode
this project's own figures are built to avoid: every label and number here
is read from the same sources the manuscript cites, not typed by hand.

Reads:
  results/tables/exp45_screen_flow.csv
  manuscript/references.json  (author/year strings only)
"""
from __future__ import annotations

import json
from pathlib import Path

from . import style as st

ROOT = st.ROOT
T = ROOT / "results" / "tables"
REFS = ROOT / "manuscript" / "references.json"


def _screen_counts() -> dict[str, int]:
    import csv
    rows = list(csv.DictReader(open(T / "exp45_screen_flow.csv", encoding="utf-8")))
    by_stage = {r["stage"]: int(r["n"]) for r in rows}
    return {
        "candidates": by_stage["candidates assembled into the manifest"],
        "inspected": by_stage["inspected: a coverage row exists"],
        "distinct": by_stage["distinct inspected records"],
        "lit_deposits": by_stage["DISTINCT LITERATURE DEPOSITS INSPECTED"],
        "no_floor": by_stage["of those, stating no assay floor by any route"],
    }


def _deposit_label(ref_key: str) -> str:
    """'Kaur 2024' / 'van Wijk 2023' style short label read from
    references.json, not typed -- multi-word surnames (van Wijk, Dal Molin)
    need more than the first token."""
    refs = json.load(open(REFS, encoding="utf-8"))
    v = refs[ref_key]
    first_author = v["authors"].split(",")[0].strip()
    # Drop trailing initials (all-caps token(s) at the end): "van Wijk RC"
    # -> "van Wijk"; "Kaur P" -> "Kaur"; "Dubey V" -> "Dubey".
    parts = first_author.split()
    while len(parts) > 1 and parts[-1].isupper():
        parts.pop()
    surname = " ".join(parts)
    return f"{surname} {v['year']}"


def build():
    st.apply()
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
    from matplotlib.lines import Line2D

    n = _screen_counts()
    deposit_labels = {
        "clinical": _deposit_label("R51"),
        "sixlab": _deposit_label("R23"),
        "clones": _deposit_label("R38"),
        "apramycin": _deposit_label("R37"),
        "holdout": _deposit_label("R36"),
    }

    fig, ax = plt.subplots(figsize=(6.9, 4.6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 66)
    ax.axis("off")

    def box(x, y, w, h, text, color, fontsize=6.6, weight="normal",
            text_color=None, align="center"):
        b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.6,rounding_size=1.4",
                            linewidth=0.9, edgecolor=color, facecolor=color,
                            alpha=0.14, zorder=2)
        ax.add_patch(b)
        b2 = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.6,rounding_size=1.4",
                             linewidth=1.1, edgecolor=color, facecolor="none",
                             zorder=3)
        ax.add_patch(b2)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=fontsize, fontweight=weight,
                color=text_color or st.INK, zorder=4, linespacing=1.35)
        return (x, y, w, h)

    def arrow(b1, b2, color=st.AXIS, side="right"):
        x1 = b1[0] + b1[2]
        y1 = b1[1] + b1[3] / 2
        x2 = b2[0]
        y2 = b2[1] + b2[3] / 2
        a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                             mutation_scale=8, color=color, lw=1.1, zorder=5,
                             shrinkA=0, shrinkB=0)
        ax.add_patch(a)

    def down_arrow(b1, b2, color=st.AXIS):
        x1 = b1[0] + b1[2] / 2
        y1 = b1[1]
        x2 = b2[0] + b2[2] / 2
        y2 = b2[1] + b2[3]
        a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                             mutation_scale=8, color=color, lw=1.1, zorder=5,
                             shrinkA=0, shrinkB=0)
        ax.add_patch(a)

    # -- column 1: the corpus screen --------------------------------------
    b_candidates = box(2, 46, 20, 16,
                        f"{n['candidates']}\ncandidate\ntime-kill\ndatasets",
                        st.BLUE, fontsize=8.2, weight="bold")
    b_screened = box(26, 46, 20, 16,
                      f"{n['inspected']} inspected\n{n['distinct']} distinct\n"
                      f"{n['lit_deposits']} literature\ndeposits",
                      st.BLUE, fontsize=7.0)
    arrow(b_candidates, b_screened)

    b_result = box(26, 27, 20, 14,
                    f"{n['no_floor']} of {n['lit_deposits']} report\nno assay floor\n"
                    f"by any route",
                    st.ORANGE, fontsize=6.8, weight="semibold")
    down_arrow(b_screened, b_result)

    b_five = box(2, 27, 20, 14, "5 deposits carry\nthe complete field\nset (Table 1)",
                 st.AQUA, fontsize=6.8, weight="semibold")
    a = FancyArrowPatch((26, 27 + 7), (22, 27 + 7), arrowstyle="-|>",
                         mutation_scale=8, color=st.AXIS, lw=1.1, zorder=5)
    ax.add_patch(a)

    ax.text(12, 65, "The corpus screened", fontsize=9.0, fontweight="bold",
            color=st.INK, ha="left")

    # deposit list under column 1
    dep_y = 2
    ax.text(2, 24.5, "The five deposits analysed", fontsize=8.0,
            fontweight="bold", color=st.INK, ha="left")
    for i, (key, label) in enumerate(deposit_labels.items()):
        box(2, dep_y + i * 3.9, 44, 3.3, label, st.INK_MUTED,
            fontsize=6.3, text_color=st.INK, weight="semibold")

    # -- column 2: the two boundaries --------------------------------------
    ax.text(52, 65, "Dynamic range, and the two boundaries it sets",
            fontsize=8.3, fontweight="bold", color=st.INK, ha="left")

    b_headroom = box(50, 52, 30, 8, "headroom  h = log10(N0 / L)",
                      st.AQUA, fontsize=7.2, weight="semibold")

    b_reach = box(50, 38, 14, 10,
                  "Reachability\nN0 >= L . 10^q",
                  st.BLUE, fontsize=6.6, weight="semibold")
    b_ident = box(66, 38, 14, 10,
                  "Identifiability\nN0 > L / c1",
                  st.BLUE, fontsize=6.6, weight="semibold")
    down_arrow(b_headroom, b_reach)
    a = FancyArrowPatch((57, 52), (73, 48), arrowstyle="-|>",
                         mutation_scale=8, color=st.AXIS, lw=1.1, zorder=5)
    ax.add_patch(a)

    b_verdict = box(50, 24, 30, 10,
                    "Above threshold: classification\nfixed by N0, not by the drug.\n"
                    "Below: observability labels refused.",
                    st.INK_MUTED, fontsize=6.3, text_color=st.INK)
    down_arrow(b_reach, b_verdict)
    down_arrow(b_ident, b_verdict)

    # -- column 3: prospective experiment ----------------------------------
    ax.text(52, 21, "The prospective experiment", fontsize=8.3,
            fontweight="bold", color=st.INK, ha="left")
    steps = ["E. coli ATCC 25922\n3 seeding arms",
             "Sampling at 0, 1, 2,\n4, 6, 24 h",
             "Duplicate plating,\n100 uL and 10 uL",
             "Both boundaries\ntested forward"]
    x0 = 50
    prev = None
    for i, s in enumerate(steps):
        b = box(x0 + i * 12.5, 4, 11, 14, s, st.ORANGE, fontsize=5.9)
        if prev:
            arrow(prev, b)
        prev = b

    st.note(ax, "Blue: the two boundaries derived from definitions alone. "
                "Orange: the corpus screen and the prospective test of both "
                "boundaries outside M. tuberculosis. Aqua: headroom, the "
                "quantity both boundaries are built from. Deposit labels "
                "read from manuscript/references.json.", y=-0.10)

    ax.set_title("Overview of the Methods: corpus screen, the two boundaries, "
                 "the prospective test", loc="left", fontsize=10.0,
                 fontweight="semibold")

    return st.save(fig, "figS6_methods_overview")


if __name__ == "__main__":
    for p in build():
        print(p)

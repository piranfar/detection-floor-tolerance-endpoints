"""
Figure S4. The corpus screened, and how five deposits came out of it.

Run:  python -m src.figures.figS4_corpus_funnel

A funnel diagram of the literature screen described in Methods: 78 candidate
time-kill datasets down to the 5 carried forward into the reanalysis. Drawn as
a funnel rather than a table because a referee's first question about a
corpus this size is "how many did you actually look at, and why did the rest
drop out" -- a shape answers that in one glance where a paragraph needs
re-reading.

Each stage is one horizontal bar, width proportional to the count remaining.
The label attached to a stage names what left the funnel to produce the next
count, not what stayed -- so the reader sees the reason for every exclusion
without leaving the figure.

Reads:
  results/tables/exp45_screen_flow.csv
"""
from __future__ import annotations

import pandas as pd

from . import style as st

ROOT = st.ROOT
T = ROOT / "results" / "tables"

# The raw ledger is a signed walk (some rows are negative deltas). The funnel
# wants the running total at each stage, which is what a reader means by
# "how many were left at this point".
STAGES = [
    ("candidates assembled into the manifest", 78, None),
    ("inspected: a coverage row exists", 45,
     "2 duplicate records never fetched;\n31 never opened (no reader, "
     "not established,\nor out of scope)"),
    ("distinct inspected records", 41,
     "4 duplicate fetches of a record\nalready counted"),
    ("permit reachability and identifiability\nto be computed at all", 18,
     "23 lack a stated floor, a derivable one,\nor a usable starting density"),
    ("carry the complete field set (Table 1)", 5,
     "13 permit the two boundaries but lack\none other field the analysis needs"),
]


def build():
    st.apply()
    import matplotlib.pyplot as plt

    n_stages = len(STAGES)
    fig, ax = plt.subplots(figsize=(6.8, 4.6))

    bar_h = 0.52
    max_n = STAGES[0][1]

    for i, (label, n, dropped) in enumerate(STAGES):
        y = n_stages - i - 1
        width = n / max_n
        color = st.BLUE if i < n_stages - 1 else st.AQUA
        ax.barh(y, width, height=bar_h, left=(1 - width) / 2, color=color,
                zorder=3, edgecolor=st.SURFACE, lw=1.0)
        ax.text(0.5, y, f"{n}", ha="center", va="center", fontsize=11,
                fontweight="semibold", color=st.SURFACE, zorder=4)
        ax.text((1 - width) / 2 - 0.02, y, label, ha="right", va="center",
                fontsize=8.2, color=st.INK)
        if dropped:
            ax.annotate(dropped, xy=(1 - (1 - width) / 2 + 0.03, y - 0.05),
                        fontsize=6.6, color=st.INK_MUTED, ha="left",
                        va="top")
        if i < n_stages - 1:
            next_width = STAGES[i + 1][1] / max_n
            ax.plot([(1 - width) / 2, (1 - next_width) / 2],
                    [y - bar_h / 2, y - 1 + bar_h / 2],
                    color=st.AXIS, lw=0.9, ls=(0, (2, 2)), zorder=1)
            ax.plot([1 - (1 - width) / 2, 1 - (1 - next_width) / 2],
                    [y - bar_h / 2, y - 1 + bar_h / 2],
                    color=st.AXIS, lw=0.9, ls=(0, (2, 2)), zorder=1)

    ax.set_xlim(-0.05, 1.55)
    ax.set_ylim(-0.8, n_stages - 0.2)
    ax.axis("off")
    ax.set_title("The corpus screened, and how five deposits came out of it",
                  loc="left", fontsize=10.5, fontweight="semibold")
    st.note(ax, "Blue: still in the screen. Green: the five deposits carried "
                "forward into Table 1.\nFull manifest and per-record "
                "verdicts: Table S12.", y=-0.10)

    return st.save(fig, "figS4_corpus_funnel")


if __name__ == "__main__":
    for p in build():
        print(p)

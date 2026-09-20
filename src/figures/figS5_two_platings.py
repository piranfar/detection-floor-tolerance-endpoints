"""
Figure S5. One culture, two plated volumes, two tolerance labels.

Run:  python -m src.figures.figS5_two_platings

The prospective experiment's own data, currently cited only through Tables
S9 and S10 with no figure of its own. This is the paper's one held-out test
of its own boundaries, so it earns a dedicated panel rather than staying a
number in a table.

Panel A is the kill curve for the three MID-arm flasks (seeded near the
standard 5e5 CFU/mL inoculum), read at both plated volumes. The two floors
-- 10 CFU/mL at 100 uL, 100 CFU/mL at 10 uL -- are drawn as bands. A point
sitting inside a band is a censored reading, not a measured one.

Panel B is the consequence: each flask's headroom at each plating, against
the four-log threshold the deposit's deepest endpoint needs. The same flask
clears the threshold at 100 uL and misses it at 10 uL -- the pipette, not
the drug, decides whether the endpoint is reportable.

Panel C is the threshold sweep behind Table S10: how often the two platings'
recorded fractions land on opposite sides of a class cut, as the cut moves.
The vertical line marks the cut the clinical classification actually uses.

Reads:
  results/tables/exp38_experiment_readings.csv
  results/tables/exp38_headroom_by_flask.csv
  results/tables/exp38_threshold_sweep.csv
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import style as st

ROOT = st.ROOT
T = ROOT / "results" / "tables"


def build():
    st.apply()
    import matplotlib.pyplot as plt

    reads = pd.read_csv(T / "exp38_experiment_readings.csv")
    flask = pd.read_csv(T / "exp38_headroom_by_flask.csv")
    sweep = pd.read_csv(T / "exp38_threshold_sweep.csv").sort_values("c1")

    mid = reads[reads.arm == "MID"].copy()
    mid["log10_cfu"] = np.log10(mid["cfu"].clip(lower=1))
    mid_flask = flask[flask.arm == "MID"].sort_values("flask")

    fig = plt.figure(figsize=(7.0, 6.4))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.15, 0.9])
    ax_a = fig.add_subplot(gs[0, :])
    ax_b = fig.add_subplot(gs[1, 0])
    ax_c = fig.add_subplot(gs[1, 1])

    # ---- A: kill curves at both platings, standard-inoculum arm -----------
    colors = {10.0: st.BLUE, 100.0: st.ORANGE}
    for vol, sub in mid.groupby("volume_ul"):
        for fl, g in sub.groupby("flask"):
            g = g.sort_values("time_h")
            ax_a.plot(g["time_h"], g["log10_cfu"], color=colors[vol],
                      lw=1.3, alpha=0.85, zorder=3)
            real = g[~g["at_floor"]]
            cens = g[g["at_floor"]]
            ax_a.scatter(real["time_h"], real["log10_cfu"], color=colors[vol],
                        s=16, zorder=4)
            ax_a.scatter(cens["time_h"], cens["log10_cfu"],
                        facecolor=st.SURFACE, edgecolor=colors[vol],
                        s=20, lw=1.1, zorder=4)
        floor_val = sub["floor"].iloc[0]
        ax_a.axhline(np.log10(floor_val), color=colors[vol], lw=0.9,
                     ls=(0, (4, 3)), zorder=1, alpha=0.6)
    ax_a.text(0.01, 0.04, "10 µL plating: floor 100 CFU/mL",
              transform=ax_a.transAxes, fontsize=7.2, color=st.BLUE,
              fontweight="semibold")
    ax_a.text(0.01, 0.115, "100 µL plating: floor 10 CFU/mL",
              transform=ax_a.transAxes, fontsize=7.2, color=st.ORANGE,
              fontweight="semibold")
    ax_a.set_xlabel("hours after ciprofloxacin, 10x MIC")
    ax_a.set_ylabel("log10 CFU/mL")
    ax_a.set_title("Standard-inoculum arm, three flasks, both platings",
                   loc="left")
    st.panel_tag(ax_a, "A")
    st.note(ax_a, "Filled points are measured counts; open points sit on "
                  "the assay floor and are censored,\nnot measured -- the "
                  "line to a censored point is drawn for continuity only.",
            y=-0.22)

    # ---- B: headroom per flask per plating, against the 4-log threshold ---
    x = np.arange(len(mid_flask))
    w = 0.32
    ax_b.bar(x - w / 2, mid_flask["headroom_10ul"], width=w, color=st.BLUE,
             label="10 µL plating", zorder=3)
    ax_b.bar(x + w / 2, mid_flask["headroom_100ul"], width=w, color=st.ORANGE,
             label="100 µL plating", zorder=3)
    ax_b.axhline(4.0, color=st.CRITICAL, lw=1.1, ls=(0, (5, 2)), zorder=2)
    ax_b.text(len(mid_flask) - 0.5, 4.0, " 4-log endpoint ", fontsize=6.8,
              color=st.CRITICAL, va="bottom", ha="right")
    ax_b.set_xticks(x, [f"Flask {int(f)}" for f in mid_flask["flask"]])
    ax_b.set_ylabel("headroom, h (log10)")
    ax_b.set_title("Same flask, same afternoon, two ceilings", loc="left")
    ax_b.legend(loc="upper left", fontsize=6.8)
    ax_b.grid(axis="x", visible=False)
    st.panel_tag(ax_b, "B")
    st.note(ax_b, "Every flask reaches four logs at 100 µL and falls short "
                  "at 10 µL.\nThe plated volume decides, not the drug.", y=-0.30)

    # ---- C: threshold sweep, share of sample-times with divergent labels --
    ax_c.plot(sweep["c1"], sweep["share"] * 100, color=st.BLUE, lw=1.8,
              marker="o", ms=4, zorder=3)
    ax_c.set_xscale("log")
    ax_c.invert_xaxis()
    cut_used = 1e-3
    row = sweep.iloc[(sweep["c1"] - cut_used).abs().argmin()]
    ax_c.axvline(cut_used, color=st.CRITICAL, lw=1.0, ls=(0, (4, 3)), zorder=2)
    ax_c.annotate(f"clinical cut\n{int(row['n_straddling'])} of "
                  f"{int(row['n_sample_times'])} sample-times",
                  xy=(cut_used, row["share"] * 100), xytext=(-8, -34),
                  textcoords="offset points", fontsize=6.6, color=st.CRITICAL,
                  fontweight="semibold", ha="right")
    ax_c.set_xlabel("class threshold, c1 (log scale)")
    ax_c.set_ylabel("% of sample-times with two labels")
    ax_c.set_title("How often one culture gets two labels", loc="left")
    ax_c.set_ylim(0, ax_c.get_ylim()[1] * 1.18)
    st.panel_tag(ax_c, "C")
    st.note(ax_c, "Swept across every threshold; the vertical line is the "
                  "cut Section 2\nactually uses for the low/medium "
                  "boundary.", y=-0.32)

    return st.save(fig, "figS5_two_platings")


if __name__ == "__main__":
    for p in build():
        print(p)

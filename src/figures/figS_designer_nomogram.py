"""The assay-design nomogram: how deep an endpoint a configuration can report.

Run:  python -m src.figures.figS_designer_nomogram

One line per plated volume: the deepest endpoint (in log10 reduction) that a
culture of starting density N0 can demonstrate, headroom = log10(N0 / L) with
L = 1000 / v per mL. Below a line's crossing with the target endpoint, the
endpoint is unreachable and a "failed" record is arithmetic, not biology.
Overlay: the nine flasks of the prospective experiment (exp38), each measured
at both platings, landing on the geometry's lines.

Writes: results/figures/figS_designer_nomogram.png / .pdf
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
FIGS = ROOT / "results" / "figures"
EXP38 = ROOT / "results" / "tables" / "exp38_headroom_by_flask.csv"

VOLUMES = {2.5: "#c7e9c0", 10.0: "#74c476", 100.0: "#238b45", 1000.0: "#00441b"}
MPN_FLOOR = 23.0
ENDPOINTS = [(2.0, "MDK$_{99}$"), (4.0, "MDK$_{99.99}$")]
STANDARD_INOCULUM = 5e5


def main() -> int:
    FIGS.mkdir(parents=True, exist_ok=True)
    n0 = np.logspace(3, 8, 400)

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    for v, color in VOLUMES.items():
        floor = 1000.0 / v
        ax.plot(n0, np.log10(n0 / floor), color=color, lw=2,
                label=f"{v:g} µL plate (L={floor:g}/mL)")
    ax.plot(n0, np.log10(n0 / MPN_FLOOR), color="#08519c", lw=2, ls="--",
            label=f"MPN series (L={MPN_FLOOR:g}/mL)")

    for q, name in ENDPOINTS:
        ax.axhline(q, color="grey", lw=0.8, ls=":")
        ax.text(1.1e3, q + 0.06, name, fontsize=9, color="grey")

    ax.axvline(STANDARD_INOCULUM, color="darkred", lw=0.9, ls="-.")
    ax.text(STANDARD_INOCULUM * 1.15, 0.25, "standard\ninoculum\n$5\\times10^5$",
            fontsize=8, color="darkred")

    if EXP38.exists():
        d = pd.read_csv(EXP38)
        # exp38 plated in duplicate: floors 50 (10 uL) and 5 (100 uL), so the
        # flasks follow the duplicate-plated geometry, log10(2) above the
        # single-plating lines.
        for v, color in ((10.0, "#74c476"), (100.0, "#238b45")):
            floor_dup = 1000.0 / (2 * v)
            ax.plot(n0, np.log10(n0 / floor_dup), color=color, lw=0.9,
                    ls=":", alpha=0.8)
        ax.scatter(d["n0_10ul"], d["headroom_10ul"], marker="o", s=34,
                   facecolor="white", edgecolor="#238b45", zorder=5,
                   label="exp38 flask, 10 µL ×2 plates (L=50)")
        ax.scatter(d["n0_100ul"], d["headroom_100ul"], marker="s", s=34,
                   facecolor="white", edgecolor="#00441b", zorder=5,
                   label="exp38 flask, 100 µL ×2 plates (L=5)")

    ax.set_xscale("log")
    ax.set_xlabel("starting density $N_0$ (per mL)")
    ax.set_ylabel("deepest endpoint the configuration can report (log$_{10}$)")
    ax.set_ylim(0, 7)
    ax.legend(fontsize=8, loc="upper left", frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(FIGS / f"figS_designer_nomogram.{ext}", dpi=200)
    print(f"wrote {FIGS / 'figS_designer_nomogram.png'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

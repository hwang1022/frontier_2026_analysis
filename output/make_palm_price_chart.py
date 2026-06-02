"""Plot the World Bank monthly palm-oil price across the IFLS4 + IFLS5 fielding windows.

Output: output/figures/palm_price.png
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code" / "data"))
from config import FIGURES as OUT  # noqa: E402

OUT.mkdir(parents=True, exist_ok=True)

PALM = {
    (2007,6):850,(2007,7):879,(2007,8):829,(2007,9):866,(2007,10):861,(2007,11):950,(2007,12):1030,
    (2008,1):1075,(2008,2):1188,(2008,3):1306,(2008,4):1180,(2008,5):1234,(2008,6):1199,
    (2008,7):1119,(2008,8):856,(2008,9):706,
    (2014,8):745,(2014,9):695,(2014,10):696,(2014,11):712,(2014,12):715,
    (2015,1):678,(2015,2):651,(2015,3):657,(2015,4):660,(2015,5):656,(2015,6):658,
    (2015,7):627,(2015,8):528,(2015,9):511,(2015,10):528,(2015,11):529,(2015,12):549,
}


def main() -> None:
    rows = [(pd.Timestamp(year=y, month=m, day=15), p) for (y, m), p in sorted(PALM.items())]
    df = pd.DataFrame(rows, columns=["date", "price_usd_mt"])
    mean_p = df.price_usd_mt.mean()
    sd_p = df.price_usd_mt.std()
    df["z"] = (df.price_usd_mt - mean_p) / sd_p

    fig, ax = plt.subplots(figsize=(12, 4.6), dpi=140)

    # IFLS field windows shaded
    ax.axvspan(pd.Timestamp("2007-07-06"), pd.Timestamp("2008-08-18"),
               color="#cfe3f4", alpha=0.55, label="IFLS4 fielding (2007-07 – 2008-08)")
    ax.axvspan(pd.Timestamp("2014-09-06"), pd.Timestamp("2015-12-18"),
               color="#fbe1cf", alpha=0.55, label="IFLS5 fielding (2014-09 – 2015-12)")

    # Long-run mean line
    ax.axhline(mean_p, color="#888", linestyle=":", linewidth=1.2,
               label=f"2007-15 sample mean = USD {mean_p:.0f}/MT")

    # Price line
    ax.plot(df.date, df.price_usd_mt, color="#1a4f8b", linewidth=2.2, marker="o",
            markersize=4.5, label="Palm oil monthly price (World Bank Pink Sheet)")

    # Annotate the two notable troughs
    trough_2008 = df[df.date == pd.Timestamp("2008-09-15")].iloc[0]
    trough_2015 = df[df.date == pd.Timestamp("2015-09-15")].iloc[0]
    ax.annotate(f"Sep 2008: USD {trough_2008.price_usd_mt:.0f}\n(post-GFC commodity crash)",
                xy=(trough_2008.date, trough_2008.price_usd_mt),
                xytext=(pd.Timestamp("2009-08-01"), 880),
                fontsize=9, ha="left",
                arrowprops=dict(arrowstyle="->", color="#666", lw=0.8))
    ax.annotate(f"Sep 2015: USD {trough_2015.price_usd_mt:.0f}\n(2014–15 collapse trough)",
                xy=(trough_2015.date, trough_2015.price_usd_mt),
                xytext=(pd.Timestamp("2013-01-01"), 480),
                fontsize=9, ha="left",
                arrowprops=dict(arrowstyle="->", color="#666", lw=0.8))

    # Annotate the peak too
    peak = df[df.date == pd.Timestamp("2008-03-15")].iloc[0]
    ax.annotate(f"Mar 2008: USD {peak.price_usd_mt:.0f}\n(commodity boom peak)",
                xy=(peak.date, peak.price_usd_mt),
                xytext=(pd.Timestamp("2009-01-01"), 1280),
                fontsize=9, ha="left",
                arrowprops=dict(arrowstyle="->", color="#666", lw=0.8))

    ax.set_xlabel("Month")
    ax.set_ylabel("USD / metric ton")
    ax.set_title("Palm-oil price across both IFLS fielding windows", fontsize=13, weight="bold", loc="left", pad=8)
    ax.set_ylim(400, 1400)
    ax.set_xlim(pd.Timestamp("2007-04-01"), pd.Timestamp("2016-03-01"))
    ax.legend(loc="upper right", fontsize=9, frameon=True, framealpha=0.95, edgecolor="#cccccc")
    ax.grid(alpha=0.3, linewidth=0.5)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)

    fig.tight_layout()
    out_path = OUT / "palm_price.png"
    fig.savefig(out_path, bbox_inches="tight", dpi=180)
    print(f"wrote {out_path}")
    print(f"  IFLS4 window prices: {df[df.date < pd.Timestamp('2010-01-01')].price_usd_mt.min()} – {df[df.date < pd.Timestamp('2010-01-01')].price_usd_mt.max()}")
    print(f"  IFLS5 window prices: {df[df.date > pd.Timestamp('2014-01-01')].price_usd_mt.min()} – {df[df.date > pd.Timestamp('2014-01-01')].price_usd_mt.max()}")
    print(f"  2007-15 mean: {mean_p:.0f}, SD: {sd_p:.0f}")


if __name__ == "__main__":
    main()

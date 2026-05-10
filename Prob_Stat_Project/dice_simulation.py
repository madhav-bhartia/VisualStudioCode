"""
Prob & Stat End Term - Q13
Simulate rolling a fair die 600 times
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ── Reproducibility ───────────────────────────────────────────────────────────
SEED = 42
RNG  = np.random.default_rng(SEED)

# ── Constants ─────────────────────────────────────────────────────────────────
N_ROLLS      = 600
N_TRIALS     = 5
FACES        = np.arange(1, 7)          # [1, 2, 3, 4, 5, 6]
EXPECTED_FREQ = N_ROLLS / 6             # 100 per face (uniform)

# ── Colours ───────────────────────────────────────────────────────────────────
OBS_COLOR  = "#4C72B0"
EXP_COLOR  = "#DD8452"
TRIAL_COLORS = ["#55A868", "#C44E52", "#8172B2", "#937860", "#DA8BC3"]

# ═════════════════════════════════════════════════════════════════════════════
# (a)  Single trial – histogram of outcome frequencies
# ═════════════════════════════════════════════════════════════════════════════
single_rolls = RNG.integers(1, 7, size=N_ROLLS)
obs_freq     = np.array([(single_rolls == f).sum() for f in FACES])

fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(FACES, obs_freq, color=OBS_COLOR, edgecolor="white",
              linewidth=0.8, zorder=3, label="Observed frequency")

# Annotate bars
for bar, freq in zip(bars, obs_freq):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
            str(freq), ha="center", va="bottom", fontsize=9, fontweight="bold")

ax.axhline(EXPECTED_FREQ, color=EXP_COLOR, linewidth=1.8,
           linestyle="--", label=f"Expected ({EXPECTED_FREQ:.0f})", zorder=4)

ax.set_xticks(FACES)
ax.set_xlabel("Die Face", fontsize=11)
ax.set_ylabel("Frequency", fontsize=11)
ax.set_title(f"(a)  Histogram of Outcome Frequencies  (n = {N_ROLLS})", fontsize=12, fontweight="bold")
ax.legend(fontsize=9)
ax.set_ylim(0, max(obs_freq) * 1.15)
ax.grid(axis="y", alpha=0.35, zorder=0)
ax.set_facecolor("#f9f9f9")
fig.tight_layout()
fig.savefig("part_a_histogram.png", dpi=150)
plt.show()
print("Part (a) saved → part_a_histogram.png")


# ═════════════════════════════════════════════════════════════════════════════
# (b)  Compare observed vs expected (grouped bar chart + residuals)
# ═════════════════════════════════════════════════════════════════════════════
expected_arr = np.full(6, EXPECTED_FREQ)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 6),
                                gridspec_kw={"height_ratios": [3, 1]})

width = 0.35
x     = np.arange(len(FACES))

ax1.bar(x - width/2, obs_freq,      width, label="Observed", color=OBS_COLOR,
        edgecolor="white", zorder=3)
ax1.bar(x + width/2, expected_arr,  width, label="Expected",  color=EXP_COLOR,
        edgecolor="white", zorder=3)

ax1.set_xticks(x)
ax1.set_xticklabels(FACES)
ax1.set_ylabel("Frequency", fontsize=11)
ax1.set_title("(b)  Observed vs Expected Frequencies", fontsize=12, fontweight="bold")
ax1.legend(fontsize=9)
ax1.grid(axis="y", alpha=0.35, zorder=0)
ax1.set_facecolor("#f9f9f9")

# Residuals (observed – expected)
residuals = obs_freq - expected_arr
colors_res = [OBS_COLOR if r >= 0 else "#E05C5C" for r in residuals]
ax2.bar(x, residuals, color=colors_res, edgecolor="white", zorder=3)
ax2.axhline(0, color="black", linewidth=0.9)
ax2.set_xticks(x)
ax2.set_xticklabels(FACES)
ax2.set_ylabel("Residual", fontsize=10)
ax2.set_xlabel("Die Face", fontsize=11)
ax2.grid(axis="y", alpha=0.35, zorder=0)
ax2.set_facecolor("#f9f9f9")

fig.tight_layout()
fig.savefig("part_b_comparison.png", dpi=150)
plt.show()
print("Part (b) saved → part_b_comparison.png")


# ═════════════════════════════════════════════════════════════════════════════
# (c)  5 independent trials of 600 rolls – overlay + variance
# ═════════════════════════════════════════════════════════════════════════════

# Simulate all 5 trials
all_freq = np.zeros((N_TRIALS, 6), dtype=int)
for t in range(N_TRIALS):
    rolls = RNG.integers(1, 7, size=N_ROLLS)
    all_freq[t] = [(rolls == f).sum() for f in FACES]

# Per-face variance across trials
face_variance = all_freq.var(axis=0, ddof=1)   # sample variance

fig = plt.figure(figsize=(10, 5))
gs  = gridspec.GridSpec(1, 2, width_ratios=[3, 2], figure=fig)

# Left: frequency lines per trial
ax_left = fig.add_subplot(gs[0])
for t in range(N_TRIALS):
    ax_left.plot(FACES, all_freq[t], marker="o", linewidth=1.5,
                 color=TRIAL_COLORS[t], label=f"Trial {t+1}", zorder=3)

ax_left.axhline(EXPECTED_FREQ, color="black", linewidth=1.4,
                linestyle="--", label="Expected", zorder=4)
ax_left.set_xticks(FACES)
ax_left.set_xlabel("Die Face", fontsize=11)
ax_left.set_ylabel("Frequency", fontsize=11)
ax_left.set_title(f"(c)  {N_TRIALS} Trials of {N_ROLLS} Rolls", fontsize=12, fontweight="bold")
ax_left.legend(fontsize=8, ncol=2)
ax_left.grid(alpha=0.35)
ax_left.set_facecolor("#f9f9f9")

# Right: variance per face
ax_right = fig.add_subplot(gs[1])
ax_right.bar(FACES, face_variance, color="#8172B2", edgecolor="white", zorder=3)
for i, (face, var) in enumerate(zip(FACES, face_variance)):
    ax_right.text(face, var + 0.5, f"{var:.1f}", ha="center",
                  va="bottom", fontsize=8, fontweight="bold")

ax_right.set_xticks(FACES)
ax_right.set_xlabel("Die Face", fontsize=11)
ax_right.set_ylabel("Sample Variance", fontsize=11)
ax_right.set_title("Variance Across Trials", fontsize=12, fontweight="bold")
ax_right.grid(axis="y", alpha=0.35, zorder=0)
ax_right.set_facecolor("#f9f9f9")

fig.tight_layout()
fig.savefig("part_c_trials_variance.png", dpi=150)
plt.show()
print("Part (c) saved → part_c_trials_variance.png")


# ═════════════════════════════════════════════════════════════════════════════
# (d)  Interpret – Chi-squared goodness-of-fit test
# ═════════════════════════════════════════════════════════════════════════════
from scipy.stats import chisquare

chi2_stat, p_value = chisquare(obs_freq, f_exp=expected_arr)

print("\n" + "="*55)
print("  (d)  Is the die unbiased?")
print("="*55)
print(f"  Observed frequencies : {obs_freq.tolist()}")
print(f"  Expected frequency   : {EXPECTED_FREQ:.1f} per face")
print(f"  Chi² statistic       : {chi2_stat:.4f}")
print(f"  p-value              : {p_value:.4f}")
print("-"*55)

ALPHA = 0.05
if p_value > ALPHA:
    print(f"  p = {p_value:.4f} > α = {ALPHA}")
    print("  → Fail to reject H₀.")
    print("  → No significant evidence that the die is biased.")
    print("  → The die APPEARS UNBIASED at the 5% significance level.")
else:
    print(f"  p = {p_value:.4f} ≤ α = {ALPHA}")
    print("  → Reject H₀.")
    print("  → Significant evidence that the die is biased.")
    print("  → The die APPEARS BIASED at the 5% significance level.")

print("="*55)
print("\nAll plots saved. Done.")

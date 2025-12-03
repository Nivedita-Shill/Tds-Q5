import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# 1. SEABORN & MATPLOTLIB STYLING
# -----------------------------
sns.set_style("whitegrid")  # professional look
sns.set_context("talk", font_scale=1.1)  # presentation-ready font sizes

# -----------------------------
# 2. SYNTHETIC BUSINESS DATA GENERATION
# -----------------------------
np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]

# realistic response time distributions (in minutes)
data = {
    "Channel": np.repeat(channels, 300),  # 300 observations per channel
    "Response_Time": np.concatenate([
        np.random.normal(loc=35, scale=12, size=300),   # Email: slower
        np.random.normal(loc=5, scale=3, size=300),     # Chat: fastest
        np.random.normal(loc=15, scale=5, size=300),    # Phone
        np.random.normal(loc=25, scale=10, size=300),   # Social Media
    ])
}

df = pd.DataFrame(data)

# Clip negative values (minutes can't be negative)
df["Response_Time"] = df["Response_Time"].clip(lower=0)

# -----------------------------
# 3. CREATE THE VIOLIN PLOT
# -----------------------------
plt.figure(figsize=(8, 8), dpi=64)   # 512x512 pixels

sns.violinplot(
    data=df,
    x="Channel",
    y="Response_Time",
    palette="Set2",
    inner="quartile",
    linewidth=1.2
)

# -----------------------------
# 4. TITLES & LABELS
# -----------------------------
plt.title("Customer Support Response Time Distribution by Channel", pad=20)
plt.xlabel("Support Channel")
plt.ylabel("Response Time (Minutes)")

# -----------------------------
# 5. SAVE CHART AS PNG
# -----------------------------
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

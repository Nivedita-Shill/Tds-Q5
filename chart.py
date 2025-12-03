import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Styling
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.1)

# Synthetic dataset
np.random.seed(42)
channels = ["Email", "Chat", "Phone", "Social Media"]

data = {
    "Channel": np.repeat(channels, 300),
    "Response_Time": np.concatenate([
        np.random.normal(35, 12, 300),
        np.random.normal(5, 3, 300),
        np.random.normal(15, 5, 300),
        np.random.normal(25, 10, 300),
    ])
}

df = pd.DataFrame(data)
df["Response_Time"] = df["Response_Time"].clip(lower=0)

# Create violinplot
plt.figure(figsize=(8, 8), dpi=64)
sns.violinplot(
    x="Channel",
    y="Response_Time",
    data=df,
    palette="Set2",
    inner="quartile",
    linewidth=1.2
)

# Titles
plt.title("Customer Support Response Time Distribution by Channel", pad=20)
plt.xlabel("Support Channel")
plt.ylabel("Response Time (Minutes)")

# Save output (512x512)
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

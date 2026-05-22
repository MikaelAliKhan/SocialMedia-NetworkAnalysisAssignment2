import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/centrality.csv")

# Clean user column
df["user"] = df["user"].astype(str)

# Take top 5 for each measure
top_in = df.nlargest(5, "in_degree")[["user", "in_degree"]].copy()
top_out = df.nlargest(5, "out_degree")[["user", "out_degree"]].copy()
top_pr = df.nlargest(5, "pagerank")[["user", "pagerank"]].copy()
top_bt = df.nlargest(5, "betweenness")[["user", "betweenness"]].copy()

# Helper to shorten usernames a bit if needed
def shorten(name, max_len=18):
    return name if len(name) <= max_len else name[:max_len-3] + "..."

for t in [top_in, top_out, top_pr, top_bt]:
    t["user"] = t["user"].apply(shorten)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Top Users by Centrality Measure", fontsize=16, fontweight="bold")

# In-degree
axes[0, 0].barh(top_in["user"], top_in["in_degree"])
axes[0, 0].set_title("Weighted In-Degree (Magnets)")
axes[0, 0].invert_yaxis()
axes[0, 0].set_xlabel("Replies received")

# Out-degree
axes[0, 1].barh(top_out["user"], top_out["out_degree"])
axes[0, 1].set_title("Weighted Out-Degree (Broadcasters)")
axes[0, 1].invert_yaxis()
axes[0, 1].set_xlabel("Replies made")

# PageRank
axes[1, 0].barh(top_pr["user"], top_pr["pagerank"])
axes[1, 0].set_title("PageRank (Prestige)")
axes[1, 0].invert_yaxis()
axes[1, 0].set_xlabel("PageRank score")

# Betweenness
axes[1, 1].barh(top_bt["user"], top_bt["betweenness"])
axes[1, 1].set_title("Betweenness (Bridges)")
axes[1, 1].invert_yaxis()
axes[1, 1].set_xlabel("Betweenness score")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("figures/centrality_user_roles.png", dpi=300, bbox_inches="tight")
plt.show()
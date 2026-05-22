import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(0, 14)
ax.set_ylim(0, 7)
ax.axis("off")

boxes = [
    ("Reddit Data\n6 subreddits\nPosts + comments", 0.5, 4.5),
    ("Preprocessing\nRemove deleted users\nResolve reply parents", 3.0, 4.5),
    ("Reply Network\nUsers = nodes\nReplies = edges", 5.5, 4.5),
    ("Network Analysis\nCentrality\nLouvain\nBridge users", 8.0, 4.5),
    ("Text Analysis\nVADER sentiment\nLDA frames\nStance validation", 5.5, 1.5),
    ("Temporal Diffusion\nBefore / during / after\nLiberation Day spike", 8.0, 1.5),
    ("Final Interpretation\nSubreddit-bounded communities\nFrame-based discourse\nInfluential users", 10.8, 3.0),
]

def add_box(text, x, y, width=2.1, height=1.05):
    box = FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.08,rounding_size=0.12",
        linewidth=1.4,
        facecolor="white",
        edgecolor="black"
    )
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text, ha="center", va="center", fontsize=9)

def add_arrow(x1, y1, x2, y2):
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle="->",
        mutation_scale=14,
        linewidth=1.3,
        color="black"
    )
    ax.add_patch(arrow)

for text, x, y in boxes:
    add_box(text, x, y)

# Main network pipeline arrows
add_arrow(2.6, 5.0, 3.0, 5.0)
add_arrow(5.1, 5.0, 5.5, 5.0)
add_arrow(7.6, 5.0, 8.0, 5.0)

# Branch from preprocessing to text analysis
add_arrow(4.0, 4.5, 5.8, 2.6)

# Network + text + temporal into final interpretation
add_arrow(10.1, 5.0, 10.8, 4.0)
add_arrow(7.6, 2.0, 10.8, 3.3)
add_arrow(10.1, 2.0, 10.8, 3.2)

ax.text(
    7, 6.35,
    "Methodology Pipeline: Network + Frame Analysis",
    ha="center",
    va="center",
    fontsize=15,
    fontweight="bold"
)

ax.text(
    7, 0.55,
    "The pipeline combines network structure, text-based frame analysis, sentiment, validation, and temporal diffusion to answer the research question.",
    ha="center",
    va="center",
    fontsize=9
)

plt.tight_layout()
plt.savefig("figures/methodology_pipeline.png", dpi=300, bbox_inches="tight")
plt.show()
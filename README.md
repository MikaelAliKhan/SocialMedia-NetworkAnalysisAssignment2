# COSC3047 Assignment 2: Social Media and Network Analysis

## Project Title
Diffusion of Trump's 2025 Tariff Discourse Across Australian Reddit: A Network and Frame Analysis

**Undergraduate Group 19**

Members:
- Aryan Jain (s4075182)
- Brigitte Sharon Alexander (s4189446)
- Mikael Ali Khan (s4089675)

## Research Question
How did Trump's 2025 tariff announcements diffuse through Australian Reddit communities, who were the most influential users driving the discourse, and how was the discourse framed across subreddits and the wider reply network?

## How to Run

**Requirements:** Python 3.10 or later.

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Open and run `SMNA-A2.ipynb` top-to-bottom in a single Jupyter session. All analysis reads from the cached files in `data/`, so no external API calls or credentials are needed for a full run.
3. Long-running cells (Arctic Shift data collection and BART-MNLI stance classification) are archived in commented-out blocks and clearly marked. Their outputs are already saved in `data/`. To reproduce them from scratch, uncomment and run those cells — this will take significantly longer.

The two standalone scripts (`make_centrality_figure.py` and `make_pipeline_diagram.py`) are supplementary. They reproduce the centrality bar chart and methodology pipeline figures respectively, but the notebook already generates the same outputs. They do not need to be run separately.

## Repository Structure

```
├── SMNA-A2.ipynb                  Main analysis notebook (run this)
├── requirements.txt               Python package dependencies
├── README.md                      This file
├── make_centrality_figure.py      Standalone script for centrality figure
├── make_pipeline_diagram.py       Standalone script for pipeline diagram
├── data/                          Full processed datasets and model outputs
│   ├── reddit_posts.csv               All collected tariff-related posts
│   ├── reddit_comments.csv            All collected comments with sentiment/stance columns
│   ├── edges.csv                      Directed reply edge list
│   ├── centrality.csv                 Centrality scores for all users
│   ├── reply_graph.pkl                Serialised NetworkX graph
│   ├── validation_sample.csv          150 hand-labelled comments for stance validation
│   └── stance_predictions_raw.csv     Raw BART-MNLI stance classifier outputs
├── sample/                        Representative data sample (< 10 MB)
│   ├── reddit_posts.csv               Stratified subset of posts
│   ├── reddit_comments.csv            Stratified subset of comments
│   └── reddit_tariff_posts.csv        Tariff-related post search results
├── figures/                       All figures used in the report
│   ├── centrality_user_roles.png
│   ├── cross_subreddit_network.png
│   ├── diffusion_timeline.png
│   ├── louvain_subreddit_composition.png
│   ├── methodology_pipeline.png
│   └── topic_subreddit_heatmap.png
└── .gitignore
```

### Note on data files
The `data/` folder contains the full processed datasets used by the notebook. The `sample/` folder contains a smaller stratified subset (under 10 MB). 

## Analysis Pipeline
1. Collect and preprocess Reddit posts and comments from six Australian subreddits via Arctic Shift.
2. Construct a directed weighted reply network where users are nodes and replies are edges.
3. Compute centrality measures (in-degree, out-degree, PageRank, betweenness) to identify different user roles.
4. Apply Louvain community detection to identify user clusters and assess subreddit alignment.
5. Analyse cross-subreddit bridge users and compare with betweenness rankings.
6. Run VADER sentiment analysis across subreddits and communities.
7. Run LDA topic modelling (k = 6) for discourse frame analysis.
8. Analyse temporal diffusion around the 2 April 2025 "Liberation Day" tariff announcement.
9. Validate exploratory BART-MNLI stance classification against 150 hand-labelled comments, justifying the pivot from stance to frame analysis.

## Main Python Libraries
- pandas, numpy — data manipulation
- networkx — graph construction and centrality
- scikit-learn — LDA topic modelling, CountVectorizer
- vaderSentiment — sentiment analysis
- transformers, torch — BART-MNLI zero-shot stance classification
- matplotlib, seaborn — visualisation

## Notes
No API keys, passwords, or private credentials are included or required. All random seeds are fixed at 42 for reproducibility.
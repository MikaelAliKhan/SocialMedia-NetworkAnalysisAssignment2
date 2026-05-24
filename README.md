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
3. Long-running cells (Arctic Shift data collection and BART-MNLI stance classification) are archived in commented-out blocks and clearly marked. Their outputs are already saved in `data/`. To reproduce them from scratch, uncomment and run those cells â€” this will take significantly longer.

The two standalone scripts (`make_centrality_figure.py` and `make_pipeline_diagram.py`) are supplementary. They reproduce the centrality bar chart and methodology pipeline figures respectively, but the notebook already generates the same outputs. They do not need to be run separately.

## Repository Structure

```
â”œâ”€â”€ SMNA-A2.ipynb                  Main analysis notebook (run this)
â”œâ”€â”€ requirements.txt               Python package dependencies
â”œâ”€â”€ README.md                      This file
â”œâ”€â”€ make_centrality_figure.py      Standalone script for centrality figure
â”œâ”€â”€ make_pipeline_diagram.py       Standalone script for pipeline diagram
â”œâ”€â”€ data/                          Full processed datasets and model outputs
â”‚   â”œâ”€â”€ reddit_posts.csv               All collected tariff-related posts
â”‚   â”œâ”€â”€ reddit_comments.csv            All collected comments with sentiment/stance columns
â”‚   â”œâ”€â”€ edges.csv                      Directed reply edge list
â”‚   â”œâ”€â”€ centrality.csv                 Centrality scores for all users
â”‚   â”œâ”€â”€ reply_graph.pkl                Serialised NetworkX graph
â”‚   â”œâ”€â”€ validation_sample.csv          150 hand-labelled comments for stance validation
â”‚   â””â”€â”€ stance_pred_raw.csv     Raw BART-MNLI stance classifier outputs
â”œâ”€â”€ sample/                        Representative data sample (< 10 MB)
â”‚   â”œâ”€â”€ reddit_posts.csv               Stratified subset of posts
â”‚   â”œâ”€â”€ reddit_comments.csv            Stratified subset of comments
â”‚   â””â”€â”€ reddit_tariff_posts.csv        Tariff-related post search results
â”œâ”€â”€ figures/                       All figures used in the report
â”‚   â”œâ”€â”€ centrality_user_roles.png
â”‚   â”œâ”€â”€ cross_subreddit_network.png
â”‚   â”œâ”€â”€ diffusion_timeline.png
â”‚   â”œâ”€â”€ louvain_subreddit_composition.png
â”‚   â”œâ”€â”€ methodology_pipeline.png
â”‚   â””â”€â”€ topic_subreddit_heatmap.png
â””â”€â”€ .gitignore
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
- pandas, numpy â€” data manipulation
- networkx â€” graph construction and centrality
- scikit-learn â€” LDA topic modelling, CountVectorizer
- vaderSentiment â€” sentiment analysis
- transformers, torch â€” BART-MNLI zero-shot stance classification
- matplotlib, seaborn â€” visualisation

## Notes
No API keys, passwords, or private credentials are included or required. All random seeds are fixed at 42 for reproducibility.

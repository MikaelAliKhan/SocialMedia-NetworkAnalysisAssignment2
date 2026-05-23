# COSC2671 Assignment 2: Social Media and Network Analysis

## Project Title
Diffusion of Trump's 2025 Tariff Discourse Across Australian Reddit: A Network and Frame Analysis

Undergraduate Group 19
Members:
- Aryan Jain (s4075182)
- Brigitte Sharon Alexander (s4189446)
- Mikael Ali Khan (s4089675)

## Research Question
How did Trump's 2025 tariff announcements diffuse through Australian Reddit communities, who were the most influential users driving the discourse, and how was the discourse framed across subreddits and the wider reply network?

## Repository Content
- `SMNA-A2.ipynb` — main analysis notebook used to produce the report results and figures.
- `reddit_posts.csv` — collected Reddit post-level dataset.
- `reddit_comments.csv` — collected Reddit comment-level dataset.
- `reddit_tariff_posts.csv` — tariff-related Reddit post dataset.
- `data/` — processed analysis outputs used for tables and validation.
- `figures/` — final figures used in the report.

## Analysis Pipeline
1. Collect and preprocess Reddit posts/comments from six Australian subreddits.
2. Construct a directed weighted reply network where users are nodes and replies are edges.
3. Compute centrality measures to identify different user roles.
4. Apply Louvain community detection to identify user clusters.
5. Analyse cross-subreddit bridge users.
6. Run VADER sentiment analysis.
7. Run LDA topic/frame modelling.
8. Analyse temporal diffusion around the 2 April 2025 “Liberation Day” tariff announcement.
9. Validate exploratory stance classification and justify the pivot from stance analysis to frame analysis.

## Main Python libraries
- pandas
- numpy
- networkx
- scikit-learn
- vaderSentiment
- transformers
- torch
- matplotlib
- seaborn

## Notes
The notebook contains cached outputs and saved figures. Long-running data collection and transformer classification steps may take longer to reproduce. No API keys, passwords, or private credentials are required.

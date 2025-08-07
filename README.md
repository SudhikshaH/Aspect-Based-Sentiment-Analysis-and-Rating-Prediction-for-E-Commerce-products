## `Project Title`: ReviewLens - Aspect-Based Sentiment Analysis and Rating Prediction Dashboard for E-Commerce Products

## Project Description
ReviewLens is a smart dashboard solution that analyzes e-commerce product reviews to extract actionable insights. It uses **Aspect-Based Sentiment Analysis** to break down customer reviews into product-specific components (like battery, sound quality, cooling, etc.) and evaluates each for positive and negative sentiment. The goal is to help product teams, analysts, or marketers understand what works and what doesn’t for each product — providing guidance on how to improve and enhance user satisfaction. The dashboard also supports real-time updates, benchmarking comparisons, and predictive analytics for overall rating improvement strategies.

## Features
- Choose a product and see all associated aspect-level sentiments
- Donut charts showing Positive vs Negative % for each aspect
- Predictive rating v/s Actual Rating
- Wordclouds for most frequent positive/negative phrases
- Fully interactive Streamlit dashboard

## Data Flow
          +---------------------------+
          | 1. Data Collection        |
          +---------------------------+
          | - Kaggle Dataset (Sample) |
          | - Reviews of Electronics  |
          +---------------------------+
                      |
                      v
          +------------------------+
          | 2. Data Preprocessing  |
          +------------------------+
          | - Cleaning & Filtering |
          | - Lowercase, Stopwords |
          | - Lemmatization        |
          | - Tools: spaCy, TQDM   |
          +------------------------+
                      |
                      v
      +-------------------------------------+
      | 3. Aspect Extraction (Hybrid Method)|
      +-------------------------------------+
      | - Predefined Aspect Dictionary      |
      | - Keyword extraction (YAKE)         |
      | - Filtering & Grouping              |
      | - Tools: YAKE, spaCy                |
      +-------------------------------------+
                      |
                      v
        +----------------------------------+
        | 4. Sentiment Analysis            |
        +----------------------------------+
        | - VADER for polarity scoring     |
        | - Score classification (pos/neg) |
        | - Tools: NLTK VADER              |
        +----------------------------------+
                      |
                      v
       +-----------------------------------+
       | 5. Predictive Insight Generation  |
       +-----------------------------------+
       | - Sentiment-Aspect correlation    |
       | - Tools: pandas, NumPy            |
       +-----------------------------------+
                      |
                      v
         +-------------------------------+
         | 6. Visualization Dashboard    |
         +-------------------------------+
         | - Streamlit Web Interface     |
         | - Donut/Bar charts (Plotly)   |
         | - Wordclouds and stats        |
         | - Tools: Streamlit, Plotly    |
         +-------------------------------+

## Dataset
Used a Kaggle dataset of electronic product reviews. Only a sample version is uploaded to the repo (sample_dataset.csv) for privacy and size reasons. After cleaning, it becomes cleaned_reviews.csv.

🔗[Kaggle: Amazon Product Reviews](https://www.kaggle.com/datasets/shivamparab/amazon-electronics-reviews)

## Dependencies Installation
```bash
pip install pandas streamlit plotly spacy yake vaderSentiment tqdm
python -m spacy download en_core_web_sm
```
## Tech Stack & Tools
- `Data Handling`	_(pandas, numpy, tqdm)_ :- Data processing, aggregation, loading CSVs.
- `NLP Processing`	_(spaCy, yake, VADER)_ :- Text cleaning, keyword extraction, sentiment scoring.
- `Visualization`	_(Plotly, WordCloud, Streamlit)_ :- For donut charts in the dashboard.
- `Aspect Extraction` _(Custom aspect dictionary + dynamic filtering)_ :- Identifies relevant product features in user reviews.
- `Rating Prediction` _(Hybrid sentiment + aspect-weight mapping)_ :-Maps sentiments to rating contribution by aspect.



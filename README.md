## `Project Title`: ReviewLens - Aspect-Based Sentiment Analysis and Rating Prediction Dashboard for E-Commerce Products

## Project Description
ReviewLens is a smart dashboard solution that analyzes e-commerce product reviews to extract actionable insights. It uses **Aspect-Based Sentiment Analysis** to break down customer reviews into product-specific components (like battery, sound quality, cooling, etc.) and evaluates each for positive and negative sentiment. The goal is to help product teams, analysts, or marketers understand what works and what doesn’t for each product — providing guidance on how to improve and enhance user satisfaction. The dashboard also supports real-time updates, benchmarking comparisons, and predictive analytics for overall rating improvement strategies.

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

## Dependencies Installation
```bash
pip install pandas streamlit plotly spacy yake vaderSentiment tqdm
python -m spacy download en_core_web_sm
```

## Features
- Choose a product and see all associated aspect-level sentiments
- Donut charts showing Positive vs Negative % for each aspect
- Predictive rating v/s Actual Rating
- Wordclouds for most frequent positive/negative phrases
- Fully interactive Streamlit dashboard

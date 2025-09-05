# `Project Title`: ReviewLens - Aspect-Based Sentiment Analysis and Rating Prediction Dashboard for E-Commerce Products

## Project Description
ReviewLens is a smart dashboard solution that analyzes e-commerce product reviews to extract actionable insights. It uses **Aspect-Based Sentiment Analysis** to break down customer reviews into product-specific components (like battery, sound quality, cooling, etc.) and evaluates each for positive and negative sentiment. The goal is to help product teams, analysts, or marketers understand what works and what doesn’t for each product providing guidance on how to improve and enhance user satisfaction. 

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
         | - Donut charts (Plotly)   |
         | - Wordclouds and stats        |
         | - Tools: Streamlit, Plotly    |
         +-------------------------------+

## Dataset
Used a Kaggle dataset of electronic product reviews. Only a sample version is uploaded to the repo (sample_dataset.csv) for privacy and size reasons. After dataprocessing it results as cleaned_reviews.csv.

🔗[Kaggle: Amazon Product Reviews](https://www.kaggle.com/datasets/shivamparab/amazon-electronics-reviews)

## Dependencies Installation
```bash
pip install pandas streamlit plotly spacy yake vaderSentiment tqdm
python -m spacy download en_core_web_sm

#run streamlit dashboard
streamlit run dashboard.py
```
## Tech Stack & Tools
- `Data Handling`	_(pandas, numpy, tqdm)_ :- Data processing, aggregation, loading CSVs.
- `NLP Processing`	_(spaCy, yake, VADER)_ :- Text cleaning, keyword extraction, sentiment scoring.
- `Visualization`	_(Plotly, WordCloud, Streamlit)_ :- For donut charts in the dashboard.
- `Aspect Extraction` _(Custom aspect dictionary + dynamic filtering)_ :- Identifies relevant product features in user reviews.
- `Rating Prediction` _(Hybrid sentiment + aspect-weight mapping)_ :-Maps sentiments to rating contribution by aspect.

## Libraries
- [Streamlit](https://streamlit.io/)
- [VADER](https://github.com/cjhutto/vaderSentiment)
- [tqdm](https://pypi.org/project/tqdm/)
- [spaCy](https://pypi.org/project/spacy/)
- [YAKE](https://github.com/LIAAD/yake)
- [Plotly](https://plotly.com/python/)

## Use Cases
1. **E-Commerce Product Enhancement**:Identify what customers like and dislike about specific product features. Track aspect-wise sentiment to improve product design and feature roadmap.
2. **Customer Support**:Understand trending issues before they escalate into support tickets. Detect common pain points by analyzing negative sentiment on specific components.
3. **Marketing Strategy**: Use wordclouds of top positive and negative keywords for content strategy.
4. **Product Review Monitoring for Retailers**:Integrate with scraping tools to monitor latest reviews in real-time. Set up alerts or dashboards to track shifts in sentiment or trending issues.
5. **Extension to other sectors**:Can be extended to analyze sentiment for various domains like healthcare reviews, movie reviews, app store reviews, etc.

## Result
- Product Dropdown Menu (choose which product to analyze).
- Donut charts displaying positive vs negative feedback for each aspect.
- Display predicted and actual rating.

## Author
SUDHIKSHA H


🔗[`LinkedIn`](https://www.linkedin.com/in/sudhiksha-h)

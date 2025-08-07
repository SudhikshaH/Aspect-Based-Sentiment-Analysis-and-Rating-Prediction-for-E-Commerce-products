#per-product per-aspect sentiment summary
import pandas as pd
from aspect_extraction import full_review_analysis

def build_summary_table(df):
    summary=[]
    for _, row in df.iterrows():
        asin=row['asin']
        rating=row['rating']
        predicted=row['predicted_rating']
        sentiment_dict=row['aspect_sentiment']
        for aspect, sentiment in sentiment_dict.items():
            summary.append({
                'asin':asin,
                'aspect':aspect,
                'sentiment':sentiment,
                'rating':rating,
                'predicted_rating':predicted
            })
    summary_df=pd.DataFrame(summary)
    
    pivot=summary_df.pivot_table(index=['asin','aspect'],columns='sentiment',aggfunc='size',fill_value=0).reset_index()
    for col in ['positive', 'negative', 'neutral']:
        if col not in pivot.columns:
            pivot[col] = 0
    rating_df=summary_df.groupby('asin').agg({'rating':'mean', 'predicted_rating':'mean'}).reset_index()
    finalSummary=pivot.merge(rating_df,on='asin',how='left')
    return finalSummary

if __name__=='__main__':
    df=pd.read_csv("Data/cleaned_reviews.csv")
    df=full_review_analysis(df)
    summary=build_summary_table(df)
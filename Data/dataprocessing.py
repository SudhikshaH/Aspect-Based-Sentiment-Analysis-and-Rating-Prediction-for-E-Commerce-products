import pandas as pd
import spacy
import re
from tqdm import tqdm
import os
import json

nlp = spacy.load("en_core_web_sm")
tqdm.pandas()
#download Electronics_5.json form the link provided in README.md
input_path="Electronics_5.json"
intermediate_path="Data/sample_reviews.csv"
output_path="Data/cleaned_reviews.csv"
#lemmatize review text
def clean_text(text,nlp):
    text=str(text).lower()
    text=re.sub(r'[^a-zA-Z\s]','',text)
    doc=nlp(text)
    tokens=[token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

def extract_sample_json(input_path):
    extracted_data=[]
    with open(input_path,'r') as file:
        for i, line in enumerate(file):
            if i>=25000:
                break
            item=json.loads(line)
            extracted_data.append({
                'asin':item.get('asin',''),
                'review':item.get('reviewText',''),
                'rating':item.get('overall',None)
            })
    df=pd.DataFrame(extracted_data)
    df.dropna(subset=['review','rating'],inplace=True)
    os.makedirs(os.path.dirname(intermediate_path),exist_ok=True)
    df.to_csv(intermediate_path,index=False)
    return df
    
def preprocess_reviews(df):
    df['cleaned_review']=df['review'].progress_apply(lambda x:clean_text(x,nlp))
    df=df[df['cleaned_review'].str.strip()!=""]
    df.to_csv(output_path,index=False)
    return df

if __name__=="__main__":
    raw_df=extract_sample_json(input_path)
    clean_df=preprocess_reviews(raw_df)
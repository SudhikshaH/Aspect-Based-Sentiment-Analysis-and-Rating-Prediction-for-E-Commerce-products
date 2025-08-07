import pandas as pd
import nltk 
import yake
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tqdm import tqdm

aspect_keywords={
    'Battery':['battery','power','backup','charge','charging'],
    'Camera':['camera','picture','video','lens','photo'],
    'Display':['display','screen','resolution','brightness','color'],
    'Sound':['sound','speaker','audio','volume','bass','mic'],
    'Connectivity':['bluetooth','wifi','non-wifi','pair','connect','signal','range'],
    'Performance':['speed','performance','processor','lag','slow','hang','fast','snappy'],
    'Build Quality':['build','material','design','system','scratch','body','sturdy','durability'],
    'Worth for money':['price','cost','expensive','money','value','cheap','worth'],
    'Delivery':['delivery','shipping','courier','late','packaging'],
    'Service':['support','warranty','technicain','service','customer'],
    'Heating Cooling':['heat','cooling','heating','fan','compressor','hot','warm','cool'],
    'Cleaning':['clean','rinse','drum','cycle','wash','dryer'],
    'Usability':['easy','setup','installation','manual','usage','user-friendly','difficult'],
    'Controls':['button','remote','switch','touch','voice'],
    'Features':['mode','option','function','smart','sensor','feature','automation'],
    'Noise':['noise','quiet','loud','silent','buzzing'],
    'AI':['ai','intelligent','machine learning','voice assistant','alexa','google assistant']
    
}

nltk.download('vader_lexicon')
vader=SentimentIntensityAnalyzer()
yake_extractor=yake.KeywordExtractor(lan='en')
tqdm.pandas()

#extract top context aware keywords as aspects with yake(unsupervised auto-keyword extraction)
def extract_aspects(text):
    aspects=yake_extractor.extract_keywords(text)
    return [k for k,score in aspects[:10]]

#analyze sentiment per-aspect
def analyze_review(review_text, aspects):
    aspect_sentiment={}
    for aspect in aspects:
        if aspect.lower() in review_text.lower():
            score=vader.polarity_scores(aspect+" "+review_text)['compound'] 
            #Sentences with compound between -0.05 and 0.05 are usually ambiguous or flat in tone.
            if score>=0.05:
                sentiment='positive'
            elif score<=-0.05:
                sentiment='negative'
            else:
                sentiment='neutral'
            aspect_sentiment[aspect]=sentiment
    return aspect_sentiment

#predict overall rating frm aspect
def predict_rating(aspect_sentiments):
    values = list(aspect_sentiments.values())
    score = values.count('positive') - values.count('negative')
    predicted = 3 + score
    return max(1, min(5, predicted)) if values else None

#noramlize the yake-extracted aspects
def normalize_aspect(phrase):
    phrase=phrase.lower()
    for aspect,keywords in aspect_keywords.items():
        if any(l in phrase for l in keywords):
            return aspect
    return None

#run full pipeline
def full_review_analysis(df):
    if 'cleaned_review' not in df.columns:
        raise ValueError("Missing 'cleaned_review' column in DataFrame")
    df=df.copy()
    df['raw_aspects']=df['cleaned_review'].progress_apply(extract_aspects)
    df['aspects']=df['raw_aspects'].apply(
        lambda aspect_list:list(set(filter(None,[normalize_aspect(a) for a in aspect_list])))
    )
    df['aspect_sentiment']=df.progress_apply(
        lambda row: analyze_review(row['cleaned_review'],row['aspects']),axis=1)
    df['predicted_rating']=df['aspect_sentiment'].apply(predict_rating)
    return df   

if __name__=='__main__':
    df=pd.read_csv("Data/cleaned_reviews.csv").head(25000)
    df=full_review_analysis(df)
    df.to_csv("Data/cleaned_reviews.csv", index=False)
    print("Aspect Sentiment analysis complete and saved")
"""
test_df = pd.DataFrame({
    'cleaned_review': [
        "m professional otr truck driver buy tnd truck stop hope life easy rand mcnally listeningfirst thing charge connect laptop install software attempt update software detect problem update want home address send patch sd card hello not think m unusual home address po box friend check weekly check month live truck truck stop need patch available sd card send sd card truck stop device sell run update program multiple time program say tnd completely updatedi program height length weight rig tell prefer highway park truck stop cincinnati oh area pickup mile freeway couple block cell phone gps sprint say freeway pickup tnd route mile residential street finally get pickup exciting especially time refuse turn street post truck tnd take minute figure reroute happen multiple time short tripi decide chance pickup north cincinnati need head phoenix az easy route hop drive west south intersection cell phone advise tnd want route surface street city pick city turn time pass truck stop chain purchase return get money backi spend cheap printer minute set route google print not get lose cross country trip"
    ]
})

result = full_review_analysis(test_df)
print(result['predicted_rating'])
"""
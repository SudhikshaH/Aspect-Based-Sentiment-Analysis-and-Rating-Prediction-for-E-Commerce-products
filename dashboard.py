import streamlit as st
import pandas as pd
import plotly.express as px 
from aspect_extraction import full_review_analysis
from product_aspectExtr import build_summary_table

@st.cache_data
def load_data():
    df=pd.read_csv("Data/cleaned_reviews.csv")
    df= full_review_analysis(df)
    summary_df=build_summary_table(df)
    return summary_df

st.set_page_config(page_title="Review Analysis", layout='wide')
st.title("E-commerce Electronic Product Review Insights with Dashboard") 
summary_df=load_data()

#product selector
pid=summary_df['asin'].unique()
selected_pid=st.sidebar.selectbox("Select Product: ", sorted(pid))
pdata=summary_df[summary_df['asin']==selected_pid]
st.markdown(f"Product Analysis{selected_pid}")

#visualization
for i,row in pdata.iterrows():
    aspect=row['aspect']
    pos = int(row['positive']) if 'positive' in row else 0
    neg = int(row['negative']) if 'negative' in row else 0
    
    if pos==0 and neg==0:
        continue
    total=pos+neg
    if total < 3:
        #st.info(f"Skipping aspect '{aspect}' due to low review count (only {total}).")
        continue
    aspect_df=pd.DataFrame({"Sentiment":['Positive','Negative'],'Count':[pos,neg], "Percent": [pos / total * 100 if total else 0, neg / total * 100 if total else 0]})
    fig=px.pie(aspect_df,names='Sentiment',values='Count',hole=0.5, color='Sentiment',color_discrete_map={'Positive':'#00C49F', 'Negative':'#FF6961'},title=f"Aspect : {aspect}(Total: {total})")
    fig.update_traces(textposition='inside', textinfo='percent+label', hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percent: %{percent}')
    st.plotly_chart(fig, use_container_width=True,  key=f"{aspect}_{i}")

#comparison of predicted rating and actual rating    
rating=pdata['rating'].mean()
pred_rating=pdata['predicted_rating'].mean()
st.markdown("Rating Comparision:")
st.metric("Actual Rating", f"{rating:.2f}/5")
st.metric("Predicted Rating", f"{pred_rating:.2f}/5")

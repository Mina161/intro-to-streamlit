import streamlit as st
from transformers import pipeline

st.title("Sentiment Analysis App")
classifier = pipeline("sentiment-analysis")

text = st.text_area("Enter text for sentiment analysis:")

if st.button("Analyze"):
    result = classifier(text)[0]
    st.write(f"**Sentiment:** {result['label']} (Confidence: {result['score']:.2f})")
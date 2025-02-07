import pickle
import streamlit as st

st.title("Spam Checker App")
loaded_model = pickle.load(open("finalized_model.sav",'rb'))
text = st.text_area("Enter text for spam analysis:")

if st.button("Analyze"):
    result = loaded_model.predict([text])[0]
    st.write(f"**Result:** {result.upper()}")
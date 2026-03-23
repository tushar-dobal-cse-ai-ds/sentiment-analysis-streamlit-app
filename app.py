import streamlit as st
import joblib

model = joblib.load("sentiment_model.pkl")

st.title("🎬 Sentiment Analysis App")

review = st.text_area("Enter your review:")

if st.button("Predict"):
    if review:
        prediction = model.predict([review])[0]

        if prediction == 1:
            st.success("😊 Positive Review")
        else:
            st.error("😠 Negative Review")
    else:
        st.warning("Please enter a review")
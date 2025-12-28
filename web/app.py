import streamlit as st
import pickle

st.set_page_config(page_title="AutoJudge Difficulty Predictor")

st.title("AutoJudge - Difficulty Prediction System")
st.write("Enter a programming problem description to predict its difficulty.")

tfidf = pickle.load(open("../models/tfidf.pkl", "rb"))
clf = pickle.load(open("../models/classifier.pkl", "rb"))
reg = pickle.load(open("../models/regressor.pkl", "rb"))


# Input box
text = st.text_area("Problem Description", height=250)

if st.button("Predict"):
    if not text.strip():
        st.error("Please enter a problem description to predict.")
    else:
        features = tfidf.transform([text])

        score_pred = reg.predict(features)[0]
        class_pred = clf.predict(features)[0]

        st.subheader("Prediction Results")
        st.write("Difficulty Score:", round(score_pred, 2))
        st.write("Difficulty Class:", class_pred)

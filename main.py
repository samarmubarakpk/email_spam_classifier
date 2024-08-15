import streamlit as st
import joblib
import pandas as pd
# Loading the trained model and vectorizer
model = joblib.load(r'D:\email_spam_classifier\models\naive_bayes_model.pkl')
vectorizer = joblib.load(r'D:\email_spam_classifier\models\count_vectorizer.pkl')

# Streamlit App Title
st.title("Email Spam Classifier")
st.write("This is a simple web app to classify emails as Spam or Ham (Not Spam) using a Naive Bayes model.")

# Input Text Box
input_email = st.text_area("Enter the email message:")

# Predict Button
if st.button("Predict"):
    if input_email.strip():
        # Preprocessing and vectorizing the input message
        input_vectorized = vectorizer.transform([input_email.lower()])
        
        # Make prediction
        prediction = model.predict(input_vectorized)
        
        # Map numeric predictions to labels
        label_mapping = {1: 'Spam', 0: 'Ham'}
        result = label_mapping[prediction[0]]
        
        # Display the result
        st.write(f"### This email is classified as **{result}**")
    else:
        st.write("Please enter a message to classify.")


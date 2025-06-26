# -*- coding: utf-8 -*-
"""
Created on Thu May  8 00:04:49 2025

@author: Anvitha
"""

import numpy as np
import pickle
import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

loaded_model=pickle.load(open('C:/Users/Anvitha/OneDrive/Documents/Project Heart disease/trained_model.sav','rb'))

def heart_disease_prediction(input_data):
    

    input_data_as_numpy_array=np.asarray(input_data)

    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
        return "The Person does not have Heart Disease"
    else:
        return "The person has Heart Disease"
    
    
def main():
    st.title('Heart Disease Prediction System')
    
    image_base64 = get_base64_image(r"C:\Users\Anvitha\OneDrive\Documents\spider heart\disease_image.png")

    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{image_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: white !important;
    }}
    label, .stTextInput > div > div {{
        color: white !important;
    }}
    .stAlert {{
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid white;
    }}
    .stAlert > div {{
        color: white !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


    # Create 3 columns
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
        cp = st.text_input("Chest Pain Type (0–3)")
        chol = st.text_input("Cholesterol (mg/dl)")
        restecg = st.text_input("Resting ECG (0–2)")
        oldpeak = st.text_input("Oldpeak")

    with col2:
        sex = st.text_input("Sex (1 = male, 0 = female)")
        trestbps = st.text_input("Resting BP")
        fbs = st.text_input("Fasting Blood Sugar (0/1)")
        thalach = st.text_input("Max Heart Rate")
        

    with col3:
        slope = st.text_input("Slope (0–2)")
        exang = st.text_input("Exercise Induced Angina (0/1)")
        ca = st.text_input("Number of major vessels (0–3)")
        thal = st.text_input("Thal (0–2)")

    if st.button('Heart Disease Test Result'):
        try:
            input_data = [
                float(age), float(sex), float(cp), float(trestbps), float(chol),
                float(fbs), float(restecg), float(thalach), float(exang),
                float(oldpeak), float(slope), float(ca), float(thal)
            ]
            diagnosis = heart_disease_prediction(input_data)
            st.success(diagnosis)
        except ValueError:
            st.error("Please ensure all fields contain valid numbers.")

if __name__ == '__main__':
   main()
    
    
import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title('❤️ Heart Disease Prediction')

# User inputs
age = st.number_input('Age', min_value=1, max_value=120)
sex = st.radio('Sex', [0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
cp = st.selectbox('Chest Pain Type (cp)', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200)
chol = st.number_input('Cholesterol', min_value=100, max_value=600)
fbs = st.radio('Fasting Blood Sugar > 120 mg/dl', [0, 1])
restecg = st.selectbox('Resting ECG Results', [0, 1, 2])
thalach = st.number_input('Max Heart Rate', min_value=60, max_value=250)
exang = st.radio('Exercise Induced Angina', [0, 1])
oldpeak = st.number_input('Oldpeak (ST depression)', format="%.1f")
slope = st.selectbox('Slope', [0, 1, 2])
ca = st.selectbox('Major Vessels (ca)', [0, 1, 2, 3, 4])
thal = st.selectbox('Thalassemia', [0, 1, 2, 3])

# Prediction
if st.button('Predict'):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Likely to have heart disease.")
    else:
        st.success("✅ Unlikely to have heart disease.")
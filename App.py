import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎓 Student Placement Prediction")

# Input fields for user
gender = st.selectbox("Gender", ["Male", "Female"])
ssc_p = st.number_input("SSC Percentage", 0.0, 100.0)
hsc_p = st.number_input("HSC Percentage", 0.0, 100.0)
degree_p = st.number_input("Degree Percentage", 0.0, 100.0)
workex = st.selectbox("Work Experience", ["Yes", "No"])
etest_p = st.number_input("E-test Score (%)", 0.0, 100.0)
mba_p = st.number_input("MBA Percentage", 0.0, 100.0)

# One-hot encoded fields
hsc_s_Commerce = st.checkbox("HSC Stream: Commerce")
hsc_s_Science = st.checkbox("HSC Stream: Science")
degree_t_Others = st.checkbox("Degree Type: Others")
degree_t_SciTech = st.checkbox("Degree Type: Sci&Tech")
specialisation_MktHR = st.checkbox("Specialisation: Mkt&HR")

# Encode categorical to numeric
gender = 1 if gender == "Male" else 0
workex = 1 if workex == "Yes" else 0
hsc_s_Commerce = int(hsc_s_Commerce)
hsc_s_Science = int(hsc_s_Science)
degree_t_Others = int(degree_t_Others)
degree_t_SciTech = int(degree_t_SciTech)
specialisation_MktHR = int(specialisation_MktHR)

# Make prediction
if st.button("Predict Placement"):
    features = np.array([[gender, ssc_p, hsc_p, degree_p, workex,
                          etest_p, mba_p, hsc_s_Commerce, hsc_s_Science,
                          degree_t_Others, degree_t_SciTech, specialisation_MktHR]])

    prediction = model.predict(features)[0]
    if prediction == 1:
        st.success("🎉 Prediction: Student is likely to be **Placed**.")
    else:
        st.error("❌ Prediction: Student is likely to be **Not Placed**.")


import streamlit as st

st.set_page_config(page_title="ASCVD Risk Calculator", layout="centered")

st.title("ASCVD Risk Score Calculator")

st.markdown("Enter patient information to calculate 10-year ASCVD risk.")

age = st.number_input("Age (years)", min_value=20, max_value=79)
sex = st.radio("Sex", ["Male", "Female"])
race = st.radio("Race", ["White", "African American", "Other"])
total_chol = st.number_input("Total Cholesterol (mg/dL)", min_value=100)
hdl = st.number_input("HDL Cholesterol (mg/dL)", min_value=20)
systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=90)
bp_treated = st.radio("Is the patient on BP medication?", ["Yes", "No"])
diabetic = st.radio("Is the patient diabetic?", ["Yes", "No"])
smoker = st.radio("Is the patient a smoker?", ["Yes", "No"])

if st.button("Calculate Risk Score"):
    # NOTE: This is just a placeholder. You can connect it to your backend logic.
    risk_score = 7.5  # mock value
    st.success(f"Estimated 10-year ASCVD Risk: {risk_score}%")
    st.markdown("**Note:** This is a demo version. For clinical use, integrate with actual ASCVD algorithm.")

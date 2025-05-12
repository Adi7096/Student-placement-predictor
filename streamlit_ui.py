import streamlit as st
import joblib
import numpy as np

model= joblib.load('placement_model.pkl')

st.set_page_config(page_title="Student Placement Predictor", layout="centered")
st.title("Student Placement Predictor")
#input fields
cgpa=st.number_input(" TOTAL CGPA",min_value=0.0 , max_value=10.0 )
iq=st.number_input(" IQ",min_value=70 , max_value=200)


if st.button("Predict Placement"):
    input_data=np.array([[cgpa , iq]])
    result=model.predict(input_data)
    if result[0] == 1:
        st.success("Student is likely to be placed")
    else:
        st.error("Student is not likely to be placed")
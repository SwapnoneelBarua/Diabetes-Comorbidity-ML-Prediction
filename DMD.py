# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:03:30 2023

@author: swapb
"""

import streamlit as st
import pickle
import pandas as pd

# Load the saved model
model = pickle.load(open('C:/Users/swapb/Desktop/Multiple Disease Prediction System/saved models/DMD.sav', 'rb'))

# Function to make predictions
def predict_neph_ret_cdv(sex, age, bmi, dm_type, dm_duration, fbs, a1c, ldl, hdl, tg, sys_bp, dias_bp, real_ldl):
    # Make predictions for the new data point
    input_data = [[sex, age, bmi, dm_type, dm_duration, fbs, a1c, ldl, hdl, tg, sys_bp, dias_bp, real_ldl]]
    predictions = model.predict(input_data)

    # Prepare the output in the desired format
    neph_pathy = "yes" if 1 in predictions[0][:, 0] else "no"
    ret_pathy = "yes" if 1 in predictions[0][:, 1] else "no"
    cdv = "yes" if 1 in predictions[0][:, 2] else "no"

    return neph_pathy, ret_pathy, cdv

# Streamlit app
st.title("Disease Detection")
st.write("Enter the patient details below:")

# User input fields
sex = st.selectbox("Sex", [0, 1])
age = st.number_input("Age")
bmi = st.number_input("BMI")
dm_type = st.selectbox("DM Type", [0, 1, 2])  # Assuming 0: Type 1, 1: Type 2, 2: Other
dm_duration = st.number_input("DM Duration")
fbs = st.number_input("FBS")
a1c = st.number_input("A1C")
ldl = st.number_input("LDL")
hdl = st.number_input("HDL")
tg = st.number_input("TG")
sys_bp = st.number_input("Sys BP")
dias_bp = st.number_input("Dias BP")
real_ldl = st.number_input("Real LDL")

# Predict button
if st.button("Predict"):
    neph_pathy, ret_pathy, cdv = predict_neph_ret_cdv(sex, age, bmi, dm_type, dm_duration, fbs, a1c, ldl, hdl, tg, sys_bp, dias_bp, real_ldl)
    st.write(f"Neph-pathy: {neph_pathy}")
    st.write(f"Ret-pathy: {ret_pathy}")
    st.write(f"CDV: {cdv}")

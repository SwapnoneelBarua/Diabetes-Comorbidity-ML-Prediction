

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open
('C:/Users/swapb/Desktop/Multiple Disease Prediction System/saved models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open
('C:/Users/swapb/Desktop/Multiple Disease Prediction System/saved models/DMD.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction','Related disease Detection'],
                          icons=['activity','heart'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([
            [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)


# Related disease Detection page
if (selected == 'Related disease Detection'):
    
    # page title
    st.title('Related disease Detection using ML')
    
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
        neph_pathy, ret_pathy, cdv = predict_neph_ret_cdv
        (sex, age, bmi, dm_type, dm_duration, fbs, a1c, ldl, hdl, tg, sys_bp, dias_bp, real_ldl)
        st.write(f"Neph-pathy: {neph_pathy}")
        st.write(f"Ret-pathy: {ret_pathy}")
        st.write(f"CDV: {cdv}")
        




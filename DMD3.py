import pandas as pd
import streamlit as st
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Load the CSV data
data = pd.read_csv('C:/Users/swapb/Desktop/Multiple Disease Prediction System/dataset/newDMD.csv')

# Data preprocessing
cols = ['Sex', 'DM type', 'Neph-pathy', 'Ret-pathy', 'CDV']
for col in cols:
    data[col].fillna(data[col].median(), inplace=True)

# Prepare the features (X) and labels (y)
features = data[['Sex', 'Age', 'BMI', 'DM type', 'DM duration', 'FBS', 'A1C',
                 'LDL', 'HDL', 'TG', 'Sys BP', 'Dias BP', 'Real LDL']]
labels = data[['Neph-pathy', 'Ret-pathy', 'CDV']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Create the decision tree classifier
classifier = DecisionTreeClassifier()

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Create the Streamlit application
st.title('Diabetes Prediction')

# Data input section
st.header('Data Input')
col1, col2, col3 = st.columns(3)

# Take input from the user for a new data point
with col1:
    sex = st.selectbox("Sex", ['Female', 'Male'])
    age = st.slider("Age", 0, 100)
    bmi = st.number_input("BMI")

with col2:
    dm_type = st.selectbox("DM Type", ['Type 1', 'Type 2'])
    dm_duration = st.slider("DM Duration (years)", 0, 50)
    fbs = st.slider("FBS", 0, 300)

with col3:
    a1c = st.number_input("A1C")
    ldl = st.slider("LDL", 0, 300)
    hdl = st.slider("HDL", 0, 100)
    tg = st.slider("TG", 0, 500)
    sys_bp = st.slider("Sys BP", 0, 250)
    dias_bp = st.slider("Dias BP", 0, 150)
    real_ldl = st.slider("Real LDL", 0, 300)

# Convert input values to numerical format
sex = 1 if sex == 'Male' else 0
dm_type = 1 if dm_type == 'Type 2' else 0

# Make prediction for the new data point
new_data = [[sex, age, bmi, dm_type, dm_duration, fbs, a1c, ldl, hdl, tg, sys_bp, dias_bp, real_ldl]]
prediction = classifier.predict(new_data)

# Prepare the output in the desired format
neph_pathy = "yes" if prediction[0][0] else "no"
ret_pathy = "yes" if prediction[0][1] else "no"
cdv = "yes" if prediction[0][2] else "no"

st.header('Prediction Result')
st.write(f"Neph-pathy: {neph_pathy}")
st.write(f"Ret-pathy: {ret_pathy}")
st.write(f"CDV: {cdv}")

st.header('Accuracy')
st.write(f"Accuracy: {accuracy}")

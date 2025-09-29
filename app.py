import streamlit as st
import pandas as pd
import joblib

# Load the simple model
model = joblib.load("simple_model.pkl")

st.title("🏡 Real Estate Price Prediction App")
st.write("Enter the details of the house to predict its price:")

# User inputs
GrLivArea = st.number_input("Living Area (sqft)", min_value=500, max_value=6000, value=1500)
OverallQual = st.slider("Overall Quality (1-10)", min_value=1, max_value=10, value=5)
GarageCars = st.slider("Number of Garage Cars", min_value=0, max_value=5, value=2)
YearBuilt = st.number_input("Year Built", min_value=1800, max_value=2025, value=2000)

# Create dataframe for prediction
input_data = pd.DataFrame({
    "GrLivArea": [GrLivArea],
    "OverallQual": [OverallQual],
    "GarageCars": [GarageCars],
    "YearBuilt": [YearBuilt]
})

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted House Price: ${prediction:,.0f}")

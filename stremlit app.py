import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('C:/Users/Administrator/Desktop/python306/car_price_rf_model.pkl')


# Define a function to make predictions
def predict_car_price(features):
    prediction = model.predict([features])
    return prediction[0]

# Streamlit app interface
st.title("Car Price Prediction")

# Input fields for the user to enter the features
year = st.number_input('Year', min_value=2000, max_value=2025)
mileage = st.number_input('Mileage (in km)', min_value=0, max_value=1000000)
engine_size = st.number_input('Engine Size (in cc)', min_value=0, max_value=5000)
num_doors = st.number_input('Number of Doors', min_value=2, max_value=5)
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'Electric', 'Hybrid'])
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])

# Convert the inputs to a suitable format (you may need to encode categorical variables depending on your model)
if fuel_type == 'Petrol':
    fuel_type_encoded = 0
elif fuel_type == 'Diesel':
    fuel_type_encoded = 1
elif fuel_type == 'Electric':
    fuel_type_encoded = 2
else:
    fuel_type_encoded = 3

if transmission == 'Manual':
    transmission_encoded = 0
else:
    transmission_encoded = 1

# When the user clicks "Predict", the model will predict the car price
if st.button('Predict Price'):
    # Prepare the feature vector
    features = [year, mileage, engine_size, num_doors, fuel_type_encoded, transmission_encoded]
    
    # Get prediction
    predicted_price = predict_car_price(features)
    
   


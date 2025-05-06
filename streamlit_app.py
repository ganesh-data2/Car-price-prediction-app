{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d15e6f06-27be-421a-b026-abdc0d78ccf6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwriting streamlit_app.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile streamlit_app.py\n",
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# Load model\n",
    "model = joblib.load('car_price_rf_model.joblib')\n",
    "\n",
    "st.title(\"Car Price Prediction App\")\n",
    "\n",
    "st.write(\"Enter the features below to predict the price:\")\n",
    "\n",
    "# Example input fields – replace with your actual feature names and number\n",
    "year = st.number_input(\"Year\", min_value=1990, max_value=2025, value=2015)\n",
    "kms_driven = st.number_input(\"KMs Driven\", value=50000)\n",
    "owner = st.selectbox(\"Owner Type\", [0, 1, 2, 3])\n",
    "fuel_type_petrol = st.checkbox(\"Fuel Type: Petrol\")\n",
    "fuel_type_diesel = st.checkbox(\"Fuel Type: Diesel\")\n",
    "transmission_manual = st.checkbox(\"Transmission: Manual\")\n",
    "seller_type_individual = st.checkbox(\"Seller Type: Individual\")\n",
    "\n",
    "# Build feature array\n",
    "features = [year, kms_driven, owner, int(fuel_type_petrol), int(fuel_type_diesel),\n",
    "            int(transmission_manual), int(seller_type_individual)]\n",
    "\n",
    "# Predict\n",
    "if st.button(\"Predict Price\"):\n",
    "    input_data = np.array(features).reshape(1, -1)\n",
    "    prediction = model.predict(input_data)\n",
    "    st.success(f\"Estimated Car Price: ₹ {prediction[0]:,.2f}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

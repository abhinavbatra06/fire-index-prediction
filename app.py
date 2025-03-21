import streamlit as st
import os
os.system("pip install joblib")
import joblib
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Load the trained model and scaler
model = joblib.load('linear_regression_model.pkl')
scaler = joblib.load('scaler.pkl')

# Title of the app
st.title("Wildfire Prediction App")

# Sidebar for user input
st.sidebar.header("User Input Parameters")

def user_input_features():
    # Input fields for numerical features with bounds
    temperature = st.sidebar.number_input("Temperature (°C)", min_value=0.0, max_value=100.0, value=25.0)
    rh = st.sidebar.number_input("Relative Humidity (RH)", min_value=0.0, max_value=100.0, value=50.0)
    ws = st.sidebar.number_input("Wind Speed (Ws)", min_value=0.0, max_value=50.0, value=10.0)
    rain = st.sidebar.number_input("Rain (mm)", min_value=0.0, max_value=100.0, value=0.0)
    
    # FFMC: Fine Fuel Moisture Code (28.6 - 92.5)
    ffmc = st.sidebar.number_input("FFMC", min_value=28.6, max_value=92.5, value=90.0)
    
    # DMC: Duff Moisture Code (1.1 - 65.9)
    dmc = st.sidebar.number_input("DMC", min_value=1.1, max_value=65.9, value=30.0)
    
    # ISI: Initial Spread Index (0 - 18.5)
    isi = st.sidebar.number_input("ISI", min_value=0.0, max_value=18.5, value=10.0)
    
    # Dropdown for region
    region = st.sidebar.selectbox("Region", ["Bejaia", "Sidi Bel-abbes"])
    # Dropdown for month
    month = st.sidebar.selectbox("Month", [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ])
    
    # Feature engineering for region
    is_sidi_bel_region = 1 if region == "Sidi Bel-abbes" else 0
    # Feature engineering for month
    is_august = 1 if month == "August" else 0
    
    # Create a DataFrame from user inputs
    data = {
        'Temperature': [temperature],
        'RH': [rh],
        'Ws': [ws],
        'Rain': [rain],
        'FFMC': [ffmc],
        'DMC': [dmc],
        'ISI': [isi],
        'is_sidi_bel_region': [is_sidi_bel_region],
        'is_august': [is_august]
    }
    return pd.DataFrame(data)

# Get user input
input_df = user_input_features()

# Define the feature order used during training
feature_order = ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'ISI', 'is_sidi_bel_region', 'is_august']

# Ensure the input DataFrame has the same column order
input_df = input_df[feature_order]

# Display user input
st.subheader("User Input:")
st.write(input_df)

# Scale the user inputs using the saved scaler
input_scaled = scaler.transform(input_df)

# Debugging: Display scaled inputs
st.subheader("Scaled Inputs:")
st.write(input_scaled)

# Create a speedometer chart
def create_speedometer(value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Fire Weather Index (FWI)"},
        gauge={
            'axis': {'range': [0, 31.1]},  # FWI range: 0 - 31.1
            'steps': [
                {'range': [0, 10], 'color': "lightgreen"},
                {'range': [10, 20], 'color': "orange"},
                {'range': [20, 31.1], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': value
            }
        }
    ))
    return fig

# Predict button
if st.button("Predict Fire Weather Index (FWI)"):
    # Make predictions
    prediction = model.predict(input_scaled)
    prediction_value = prediction[0]  # Assuming the model outputs a single value
    
    # Display prediction
    st.subheader("Prediction:")
    st.write(f"The predicted Fire Weather Index (FWI) is: {prediction_value:.2f}")
    
    # Show speedometer
    st.plotly_chart(create_speedometer(prediction_value))
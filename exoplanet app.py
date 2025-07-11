import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Example: train a quick model on dummy data (replace this with your saved model)
def train_dummy_model():
    # Simulated data
    data = {
        'Mass': np.random.uniform(0.1, 5, 100),
        'Radius': np.random.uniform(0.5, 2, 100),
        'Surface Temp': np.random.uniform(200, 500, 100),
        'Habitability': np.random.randint(0, 2, 100)
    }
    df = pd.DataFrame(data)
    X = df[['Mass', 'Radius', 'Surface Temp']]
    y = df['Habitability']

    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    return model

model = train_dummy_model()

# Streamlit app
st.set_page_config(page_title="🪐 Planet Habitability Predictor")

st.title("🪐 Planet Habitability Predictor")

st.markdown("Enter the planetary parameters below to predict if it might be habitable:")

# User inputs
mass = st.number_input("Mass (in Earth masses)", 0.1, 10.0, 1.0)
radius = st.number_input("Radius (in Earth radii)", 0.1, 5.0, 1.0)
temp = st.number_input("Surface Temperature (K)", 100, 1000, 300)

# Collect user input into DataFrame
user_data = pd.DataFrame({
    'Mass': [mass],
    'Radius': [radius],
    'Surface Temp': [temp]
})

# Predict button
if st.button("Predict Habitability"):
    prediction = model.predict(user_data)[0]
    prob = model.predict_proba(user_data)[0]

    if prediction == 1:
        st.success(f"🌍 This planet is **likely habitable** (Probability: {prob[1]*100:.1f}%)")
    else:
        st.error(f"☄️ This planet is **likely not habitable** (Probability: {prob[0]*100:.1f}%)")

st.sidebar.markdown("Made with ❤️ for astronomy fans 🚀")

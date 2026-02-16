# 🪐 Exoplanet Habitability Prediction System

A Machine Learning powered web application that predicts whether an exoplanet is potentially habitable based on astrophysical and stellar parameters.

Built using Scikit-Learn and deployed with Streamlit.

---

## 🚀 Project Overview

This project uses a Random Forest Classifier trained on a cleaned NASA Exoplanet dataset to classify planets as:

- 🌍 Habitable
- ☄️ Non-Habitable

The model analyzes planetary mass, radius, orbital properties, and stellar characteristics to make predictions.

This is a predictive ML system and not an astronomical confirmation.

---

## 🧠 Machine Learning Pipeline

- Data Cleaning & Missing Value Handling
- Feature Selection
- Train-Test Split (Stratified)
- Random Forest with Class Balancing
- Model Evaluation
- Model Serialization using Joblib
- Streamlit Deployment

---

## 📊 Features Used

- Planet Mass
- Planet Radius
- Orbital Period
- Semi Major Axis
- Equilibrium Temperature
- Stellar Mass
- Stellar Radius
- Stellar Temperature

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Joblib

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/exoplanet-habitability.git
cd exoplanet-habitability
```

Create virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will launch in your browser.

---

## 📁 Project Structure

```
├── app.py
├── exoplanet_model.pkl
├── scaler.pkl (if used)
├── requirements.txt
└── README.md
```

---

## 📈 Future Improvements

- Add Feature Importance Visualization
- Hyperparameter Tuning
- Deploy on Streamlit Cloud / AWS
- Add SHAP Explainability

---

## 👨‍💻 Author

Sarthak  

Machine Learning | Data Science | Astronomy Applications

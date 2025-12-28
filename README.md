🧑‍⚕️ Multiple Disease Prediction System

A Machine Learning–powered web application built with Streamlit to predict the likelihood of multiple diseases based on user-provided medical information.
This project integrates multiple trained ML models into a single interactive web interface for real-time health risk prediction.

📌 Project Overview

Early disease detection plays a crucial role in improving treatment outcomes and reducing healthcare costs.
This project aims to assist in preliminary disease risk assessment by:

Training ML models on medical datasets

Deploying multiple disease prediction models in one application

Providing a simple and interactive Streamlit-based UI

Allowing users to enter health parameters and get instant predictions

⭐ Key Highlights

Diseases Covered: Diabetes, Heart Disease, Parkinson’s Disease

Models Used: Trained ML classification models (Scikit-learn)

Input Type: Manual user input via web interface

Deployment: Streamlit Web Application

Purpose: Educational & demonstration use

🚀 Live Demo

🔗 Streamlit App:
https://multiple-disease-prediction-system-ioxup5pxm9eanzuzhewpf2.streamlit.app/


🗂️ Repository Structure
Multiple-Disease-Prediction/
│
├── Multiple disease prediction system - diabetes.ipynb    # Diabetes model training
├── Multiple disease prediction system - heart.ipynb       # Heart disease model training
├── Multiple disease prediction system - Parkinsons.ipynb  # Parkinson’s model training
├── app.py                                                 # Streamlit web application
├── diabetes_model.sav                                     # Trained diabetes model
├── heart_disease_model.sav                                # Trained heart disease model
├── parkinsons_model.sav                                   # Trained Parkinson’s model
├── requirements.txt                                       # Python dependencies
└── README.md                                              # Project documentation

⚙️ How It Works
🔹 Model Workflow

Data Loading – Load disease-specific medical datasets

Preprocessing – Clean data and scale features

Training – Train classification models for each disease

Evaluation – Evaluate model performance

Deployment – Save trained models and load them into Streamlit

🖥️ Application Features

🩸 Diabetes prediction using health indicators

❤️ Heart disease risk prediction

🧠 Parkinson’s disease detection

📋 User-friendly form-based input

🔄 Sidebar navigation for disease selection

🎨 Clean and responsive UI

🛠️ Tech Stack

Programming Language: Python

ML Libraries: NumPy, Scikit-learn

Web Framework: Streamlit

UI Components: Streamlit Option Menu

Model Serialization: Pickle

📦 Installation & Running Locally
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/Multiple-Disease-Prediction.git
cd Multiple-Disease-Prediction

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py


The application will open automatically in your browser.

📊 Input Details

Each disease model expects specific medical parameters:

🩸 Diabetes

Pregnancies, Glucose, Blood Pressure, Skin Thickness

Insulin, BMI, Diabetes Pedigree Function, Age

❤️ Heart Disease

Age, Sex, Chest Pain Type, Blood Pressure

Cholesterol, ECG Results, Heart Rate, etc.

🧠 Parkinson’s

Voice frequency and amplitude-based features

Jitter, Shimmer, HNR, RPDE, PPE, and others

⚠️ Ensure all inputs are numeric and correctly entered.


⭐ Acknowledgements

UCI Machine Learning Repository

Kaggle Datasets

Streamlit Community

Scikit-learn Documentation

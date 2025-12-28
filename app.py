import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# ===============================
# Page Configuration
# ===============================
st.set_page_config(
    page_title="Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️"
)

# ===============================
# Get current directory
# ===============================
working_dir = os.path.dirname(os.path.abspath(__file__))

# ===============================
# Load ML Models (CORRECT PATHS)
# ===============================
diabetes_model = pickle.load(open(os.path.join(working_dir, "diabetes_model.sav"), "rb"))
heart_disease_model = pickle.load(open(os.path.join(working_dir, "heart_disease_model.sav"), "rb"))
parkinsons_model = pickle.load(open(os.path.join(working_dir, "parkinsons_model.sav"), "rb"))

# ===============================
# Sidebar Menu
# ===============================
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
        icons=["activity", "heart", "person"],
        menu_icon="hospital-fill",
        default_index=0
    )

# ===============================
# Diabetes Prediction
# ===============================
if selected == "Diabetes Prediction":

    st.title("Diabetes Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure")
    with col1:
        SkinThickness = st.text_input("Skin Thickness")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    with col2:
        Age = st.text_input("Age")

    diab_result = ""

    if st.button("Diabetes Test Result"):
        try:
            user_input = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]

            prediction = diabetes_model.predict([user_input])

            diab_result = "The person is Diabetic" if prediction[0] == 1 else "The person is NOT Diabetic"

        except:
            diab_result = "❌ Please enter valid numeric values"

    st.success(diab_result)

# ===============================
# Heart Disease Prediction
# ===============================
if selected == "Heart Disease Prediction":

    st.title("Heart Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex (1 = Male, 0 = Female)")
    with col3:
        cp = st.text_input("Chest Pain Type")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholesterol")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120")
    with col1:
        restecg = st.text_input("Resting ECG")
    with col2:
        thalach = st.text_input("Max Heart Rate")
    with col3:
        exang = st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak = st.text_input("Oldpeak")
    with col2:
        slope = st.text_input("Slope")
    with col3:
        ca = st.text_input("Major Vessels")
    with col1:
        thal = st.text_input("Thal")

    heart_result = ""

    if st.button("Heart Disease Test Result"):
        try:
            user_input = [
                float(age), float(sex), float(cp), float(trestbps),
                float(chol), float(fbs), float(restecg), float(thalach),
                float(exang), float(oldpeak), float(slope),
                float(ca), float(thal)
            ]

            prediction = heart_disease_model.predict([user_input])

            heart_result = "The person HAS Heart Disease" if prediction[0] == 1 else "The person does NOT have Heart Disease"

        except:
            heart_result = "❌ Please enter valid numeric values"

    st.success(heart_result)

# ===============================
# Parkinsons Prediction
# ===============================
if selected == "Parkinsons Prediction":

    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
    with col4:
        jitter = st.text_input("MDVP:Jitter(%)")
    with col5:
        jitter_abs = st.text_input("MDVP:Jitter(Abs)")
    with col1:
        rap = st.text_input("RAP")
    with col2:
        ppq = st.text_input("PPQ")
    with col3:
        ddp = st.text_input("DDP")
    with col4:
        shimmer = st.text_input("Shimmer")
    with col5:
        shimmer_db = st.text_input("Shimmer(dB)")
    with col1:
        apq3 = st.text_input("APQ3")
    with col2:
        apq5 = st.text_input("APQ5")
    with col3:
        apq = st.text_input("APQ")
    with col4:
        dda = st.text_input("DDA")
    with col5:
        nhr = st.text_input("NHR")
    with col1:
        hnr = st.text_input("HNR")
    with col2:
        rpde = st.text_input("RPDE")
    with col3:
        dfa = st.text_input("DFA")
    with col4:
        spread1 = st.text_input("Spread1")
    with col5:
        spread2 = st.text_input("Spread2")
    with col1:
        d2 = st.text_input("D2")
    with col2:
        ppe = st.text_input("PPE")

    park_result = ""

    if st.button("Parkinson's Test Result"):
        try:
            user_input = [
                float(fo), float(fhi), float(flo), float(jitter),
                float(jitter_abs), float(rap), float(ppq), float(ddp),
                float(shimmer), float(shimmer_db), float(apq3),
                float(apq5), float(apq), float(dda), float(nhr),
                float(hnr), float(rpde), float(dfa), float(spread1),
                float(spread2), float(d2), float(ppe)
            ]

            prediction = parkinsons_model.predict([user_input])

            park_result = "The person HAS Parkinson's Disease" if prediction[0] == 1 else "The person does NOT have Parkinson's Disease"

        except:
            park_result = "❌ Please enter valid numeric values"

    st.success(park_result)

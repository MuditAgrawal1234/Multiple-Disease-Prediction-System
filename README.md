# 🧑‍⚕️ Multiple Disease Prediction System

A **Machine Learning–powered web application** built with **Streamlit** to predict the likelihood of multiple diseases based on user-provided medical information.  
The system integrates **multiple trained ML models** into a single interactive web interface for **real-time health risk prediction**.

---

## 📌 Project Overview

Early disease detection plays a crucial role in improving treatment outcomes and reducing healthcare costs.  
This project assists in **preliminary disease risk assessment** by:

- Training ML models on medical datasets
- Integrating multiple disease prediction models into one application
- Providing a simple and interactive **Streamlit-based UI**
- Allowing users to enter health parameters and receive **instant predictions**

---

## ⭐ Key Highlights

- **Diseases Covered:**  
  - 🩸 Diabetes  
  - ❤️ Heart Disease  
  - 🧠 Parkinson’s Disease  

- **Models Used:** Machine Learning classification models (Scikit-learn)  
- **Input Type:** Manual user input via web interface  
- **Deployment:** Streamlit Web Application  
- **Purpose:** Educational & demonstration use  

---

## 🚀 Live Demo

🔗 **Streamlit App:**  
https://multiple-disease-prediction-system-ioxup5pxm9eanzuzhewpf2.streamlit.app/

---

## 🗂️ Repository Structure

---

## 🗂️ Repository Structure

```
Multiple-Disease-Prediction/
│
├── Multiple disease prediction system - diabetes.ipynb
├── Multiple disease prediction system - heart.ipynb
├── Multiple disease prediction system - Parkinsons.ipynb
├── app.py
├── diabetes_model.sav
├── heart_disease_model.sav
├── parkinsons_model.sav
├── requirements.txt
└── README.md                              # Project documentation
```

---

---

## ⚙️ How It Works

### 🔹 Model Workflow

1. **Data Loading** – Load disease-specific medical datasets  
2. **Preprocessing** – Clean data and scale features  
3. **Training** – Train classification models for each disease  
4. **Evaluation** – Evaluate model performance  
5. **Deployment** – Save trained models and load them into Streamlit  

---

## 🖥️ Application Features

- 🩸 Diabetes prediction using health indicators  
- ❤️ Heart disease risk prediction  
- 🧠 Parkinson’s disease detection  
- 📋 User-friendly form-based input  
- 🔄 Sidebar navigation for disease selection  
- 🎨 Clean and responsive UI  

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **ML Libraries:** NumPy, Scikit-learn  
- **Web Framework:** Streamlit  
- **UI Components:** Streamlit Option Menu  
- **Model Serialization:** Pickle  

---

## 📦 Installation & Running Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Multiple-Disease-Prediction.git
cd Multiple-Disease-Prediction
### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

The app will open automatically in your browser.

---
## ⭐ Acknowledgements

* UCI Machine Learning Repository
* Streamlit Community
* Scikit-learn Documentation

---

If you like this project, don’t forget to ⭐ the repository!


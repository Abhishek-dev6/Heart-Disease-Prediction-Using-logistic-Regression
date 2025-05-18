<h1 align="center">❤️ Heart Disease Prediction</h1>
<p align="center">
  A machine learning project to predict heart disease using Logistic Regression with Scikit-Learn and visualize feature importance.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg">
  <img src="https://img.shields.io/badge/Model-LogisticRegression-success">
  <img src="https://img.shields.io/badge/License-MIT-purple">
</p>

---

## 📌 Overview

Heart disease is a leading cause of death globally. Early detection through machine learning can help doctors take proactive steps.  
This project uses **Logistic Regression** to predict the presence of heart disease from medical attributes.

✨ **Highlights**:
- Clean Data Preprocessing  
- Scikit-Learn Logistic Regression Model  
- Hyperparameter Tuning (`GridSearchCV`)  
- Accuracy & Classification Metrics  
- Prediction on Custom Input  
- Feature Importance Visualization  

---

## 🧠 Technologies Used

| Tool           | Purpose                        |
|----------------|--------------------------------|
| `pandas`       | Data manipulation              |
| `scikit-learn` | ML model, metrics, scaling     |
| `matplotlib`   | Visualization                  |

---

## 📂 Dataset Description

| Feature         | Description                                      |
|-----------------|--------------------------------------------------|
| Age             | Age of the patient                               |
| Sex             | 1 = Male, 0 = Female                             |
| ChestPainType   | 0–3 categories of pain                           |
| RestingBP       | Resting blood pressure                           |
| Cholesterol     | Serum cholesterol level                          |
| FastingBS       | Fasting blood sugar (1 = true)                   |
| RestingECG      | Resting electrocardiographic results             |
| MaxHR           | Max heart rate achieved                          |
| ExerciseAngina  | Exercise-induced angina (1 = yes, 0 = no)        |
| Oldpeak         | ST depression induced by exercise                |
| Slope           | Slope of the ST segment                          |
| CA              | Number of major vessels colored by fluoroscopy  |
| Thal            | Thalassemia (0–3)                                |
| Heart Disease   | Target variable (1 = Yes, 0 = No)                |

---

## 🚀 Getting Started

### 1. Clone this Repository
```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction

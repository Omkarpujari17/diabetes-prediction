🩺 Diabetes Prediction Web App  

A Machine Learning–powered web application that predicts whether a person is likely to have diabetes based on key health parameters.  
This project was built as part of my Machine Learning portfolio and deployed on Render using Flask, **Scikit-learn**, and a **Random Forest Classifier**.

---

## 🚀 Live Demo  
🔗 Try it here:[https://diabetes-prediction-1-pzda.onrender.com/](https://diabetes-prediction.onrender.com)  
*(If the Render free instance sleeps, please wait ~30 seconds for it to wake up.)*

---

## 📊 Overview  

This app takes 8 key medical inputs — such as Glucose level, BMI, and Age — and predicts whether a person is at risk of diabetes.  
The model was trained using the **Pima Indians Diabetes Dataset**, achieving **~78% accuracy** and **0.81 ROC-AUC**.

**Example Output:**  
No Diabetes 🙂

or  


Diabetes Detected 😔

---

## 🧠 Machine Learning Model  

- **Dataset:** [Pima Indians Diabetes Dataset (UCI Repository)](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)  
- **Algorithms Tried:** Logistic Regression, Random Forest, XGBoost  
- **Final Model:** Random Forest (best performer)  
- **Metrics:**  
  - Accuracy: 78%  
  - ROC-AUC: 0.81  
  - Precision (No Diabetes): 0.81  
  - Recall (No Diabetes): 0.87  

**Features Used:**  
Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age

---

## 🧩 Tech Stack  

| Layer | Technology |
|-------|-------------|
| Frontend | HTML, CSS (Flask Templates) |
| Backend | Flask (Python) |
| ML Libraries | Pandas, Scikit-learn, NumPy, Joblib |
| Model | Random Forest Classifier |
| Deployment | Render (Gunicorn + Python 3) |
| Version Control | Git & GitHub |

---

## ⚙️ Local Setup  

```bash
# 1. Clone the repository
git clone https://github.com/Omkarpujari17/diabetes-prediction.git
cd diabetes-prediction

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app (development)
python app/app.py

# OR run with Waitress for production-style test
python -m waitress --listen=0.0.0.0:8000 app.app:app
Visit:
👉 http://127.0.0.1:5000 or http://127.0.0.1:8000

Project Structure
diabetes-prediction/
├── app/
│   ├── app.py               # Flask application
│   ├── templates/
│   │   └── index.html       # Frontend form
│
├── src/
│   ├── random_forest_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── 02_data_cleaning.ipynb
│
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
🧾 How It Works

User enters health parameters in a form.

The input is scaled using the saved StandardScaler.

The trained Random Forest model predicts 1 (diabetes) or 0 (no diabetes).

The result is displayed instantly on the web page.

🚀 Deployment (Render)

Push code to GitHub.

Create a new Web Service on Render
.

Use this Start Command:

gunicorn app.app:app


Root Directory: (leave blank)

Environment: Python 3

Add environment variables if needed:

MODEL_PATH = src/random_forest_model.pkl
SCALER_PATH = src/scaler.pkl

🧠 Future Enhancements

Add probability/confidence score to prediction

Integrate SHAP for feature importance visualization

Improve UI and add input validation

Add logs and analytics for user interactions

Connect to database for historical predictions

⚠️ Disclaimer

This project is for educational purposes only and should not be used for real medical diagnosis.

👤 Author

Omkar Pujari

💼 Aspiring Machine Learning Engineer

🌐 GitHub Profile

✉️ Contact: (add your email here if you’d like)

🪶 Resume Highlight Example

Diabetes Prediction Web App — Built and deployed a Random Forest–based Flask application (ROC-AUC 0.81) to predict diabetes likelihood. Deployed using Render with full CI/CD integration and GitHub version control.


---

✅ **Next steps:**
1. Create a file named `README.md` in your project folder.  
2. Paste the content above as-is.  
3. Save, then commit and push:

```powershell
git add README.md
git commit -m "Add professional README"
git push origin main

# app/app.py
from flask import Flask, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

# Load model and scaler path from environment or default to ../src/...
MODEL_PATH = os.getenv("MODEL_PATH", os.path.join(os.path.dirname(os.path.dirname(__file__)), "src", "random_forest_model.pkl"))
SCALER_PATH = os.getenv("SCALER_PATH", os.path.join(os.path.dirname(os.path.dirname(__file__)), "src", "scaler.pkl"))

# Load once at startup
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['Pregnancies']),
            float(request.form['Glucose']),
            float(request.form['BloodPressure']),
            float(request.form['SkinThickness']),
            float(request.form['Insulin']),
            float(request.form['BMI']),
            float(request.form['DiabetesPedigreeFunction']),
            float(request.form['Age'])
        ]
        scaled = scaler.transform([features])
        pred = model.predict(scaled)[0]
        result = "Diabetes Detected 😔" if pred == 1 else "No Diabetes 🙂"
        return render_template('index.html', result=result)
    except Exception as e:
        return render_template('index.html', result=f"Error: {e}")

# Do NOT use app.run() in production; gunicorn will serve the app
if __name__ == '__main__':
    app.run(debug=True)

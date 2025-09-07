# Tip Prediction Django App

This repository demonstrates how to **deploy a Machine Learning (ML) model using Django**, a high-level Python web framework.  
The project includes a simple web interface where users can enter input data and receive predictions from a trained ML model.

---

## 🚀 Project Overview
In this project, we built a **Tip Prediction App** that uses an ML model trained on structured data.  
The workflow includes:
- Data preprocessing and model training (saved as `xgb_model.pkl`)
- Integration of the trained model inside a Django app
- A user-friendly web form for entering inputs
- Real-time predictions served via Django views

---

## ⚙️ Setup Instructions

### 1️⃣ Create a Python Virtual Environment
We recommend using a virtual environment to isolate dependencies.

```bash
# create a virtual environment
python -m venv .venv

# activate the environment
# Linux / macOS
source .venv/bin/activate

# Windows (Command Prompt / PowerShell)
.venv\Scripts\activate

# Windows (Git Bash)
source .venv/Scripts/activate
````

---

### 2️⃣ Install Required Libraries

Install the necessary dependencies for Django and Machine Learning.

```bash
# web development framework
pip install django

# machine learning libraries
pip install numpy pandas matplotlib seaborn plotly scikit-learn xgboost

# jupyter notebook support
pip install ipykernel
```

---

### 3️⃣ Train the Machine Learning Model

Steps followed:

1. Load and explore the dataset
2. Preprocess the data
3. Train the model (using XGBoost in this case)
4. Evaluate the performance
5. Save the model

The trained model is stored as **`xgb_model.pkl`** inside the `models/` directory.
A Jupyter notebook (not included in this repo for simplicity) was used to handle training and model saving.

---

### 4️⃣ Create the Django Project

```bash
django-admin startproject tip_prediction
cd tip_prediction
```

---

### 5️⃣ Create a Django App

```bash
python manage.py startapp ml_app
```

---

### 6️⃣ Update `settings.py`

Register the app in `tip_prediction/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'ml_app',
]
```

---

### 7️⃣ Create a User Input Form

In **`ml_app/forms.py`**, we define a form for users to input features:

```python
from django import forms

class PredictionForm(forms.Form):
    feature1 = forms.FloatField(label='Feature 1')
    feature2 = forms.FloatField(label='Feature 2')
    feature3 = forms.FloatField(label='Feature 3')
    feature4 = forms.FloatField(label='Feature 4')
    feature5 = forms.FloatField(label='Feature 5')
    feature6 = forms.FloatField(label='Feature 6')
```

This form is rendered in the frontend, allowing users to provide input data for predictions.

---

## 📊 Results

* Users can enter their input via the web form.
* The trained ML model (`xgb_model.pkl`) is loaded inside Django views.
* Predictions are displayed instantly on the web page.

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **ML Frameworks:** scikit-learn, XGBoost
* **Visualization:** Matplotlib, Seaborn, Plotly
* **Frontend:** Django Templates, HTML/CSS

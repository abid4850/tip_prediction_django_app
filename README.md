# 🍽️ Tip Prediction Django App  

A **machine learning powered web application** built with **Django** that predicts restaurant tips based on customer and order details.  
This project demonstrates how to **deploy an ML model with Django**, integrating data science with full-stack web development.  

---

## 🚀 Features  

- ✅ Predict restaurant tips using an **XGBoost ML model**  
- ✅ **User-friendly web form** built with Django forms  
- ✅ Clean **UI templates** for input & results display  
- ✅ Fully **modular Django project structure** (`ml_app`)  
- ✅ Example of **ML model integration** into production-ready web apps  
- ✅ Educational project for **Data Science + Web Development**  

---

## 📊 Tech Stack  

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS (Django templates)  
- **Machine Learning:** XGBoost, scikit-learn, NumPy, pandas  
- **Visualization/EDA (in notebook):** matplotlib, seaborn, plotly  

---

## 📂 Project Structure  

```

tip\_prediction/
│
├── ml\_app/                  # Core Django app
│   ├── forms.py             # User input forms
│   ├── views.py             # Prediction logic
│   ├── urls.py              # URL routing for ml\_app
│   └── templates/ml\_app/    # HTML templates
│
├── models/                  # Saved ML model(s)
│   └── xgb\_model.pkl        # Trained XGBoost model (not uploaded for security)
│
├── tip\_prediction/          # Main project settings & URLs
│
├── manage.py                # Django project manager
└── README.md                # Project documentation

````

---

## ⚡ Getting Started  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/tip_prediction_django_app.git
cd tip_prediction_django_app
````

### 2️⃣ Create & activate virtual environment

```bash
# Create venv
python -m venv .venv  

# Activate venv (Linux/Mac)
source .venv/bin/activate  

# Activate venv (Windows)
.venv\Scripts\activate  

# Activate venv (Git Bash on Windows)
source .venv/Scripts/activate  
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py migrate
```

### 5️⃣ Start the development server

```bash
python manage.py runserver
```

👉 Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🎯 Usage

1. Open the app in your browser
2. Enter details:

   * Total bill
   * Sex (Male/Female)
   * Smoker (Yes/No)
   * Day (Fri/Sat/Sun/Thur)
   * Time (Lunch/Dinner)
   * Party size
3. Click **Predict**
4. See the **expected tip** instantly 🎉

---

## 📈 Model Training

* Data preprocessing & feature engineering done in Jupyter Notebook
* Model trained with **XGBoost**
* Final model saved as `xgb_model.pkl` (kept locally for security reasons)

---

## ⭐ Contributing

Contributions are welcome! Feel free to fork this repo, open issues, or submit pull requests.

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify with attribution.

---

## 🌟 Acknowledgements

* [Django Documentation](https://docs.djangoproject.com/)
* [XGBoost Documentation](https://xgboost.readthedocs.io/)
* Open-source ML/Django community for inspiration 🚀

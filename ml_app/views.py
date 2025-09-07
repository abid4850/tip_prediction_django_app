import os
import joblib
import numpy as np
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from .forms import TipPredictionForm

# Correct model path inside your Django project
model_path = os.path.join(settings.BASE_DIR, 'tip_prediction', 'models', 'xgb_model.pkl')

_model = None  # cache the model so it loads only once


def load_model():
    global _model
    if _model is None:
        try:
            _model = joblib.load(model_path)
            print(f"✅ Model loaded successfully from: {model_path}")
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            _model = None
    return _model


def encode_features(sex, smoker, day, time):
    sex_encoded = 1 if sex == 'Male' else 0
    smoker_encoded = 1 if smoker == 'Yes' else 0
    day_mapping = {'Fri': 0, 'Sat': 1, 'Sun': 2, 'Thur': 3}
    day_encoded = day_mapping.get(day, 0)
    time_encoded = 1 if time == 'Lunch' else 0
    return sex_encoded, smoker_encoded, day_encoded, time_encoded


def index(request):
    return render(request, 'ml_app/index.html')


def predict_tip(request):
    prediction = None
    if request.method == 'POST':
        form = TipPredictionForm(request.POST)
        if form.is_valid():
            total_bill = form.cleaned_data['total_bill']
            sex = form.cleaned_data['sex']
            smoker = form.cleaned_data['smoker']
            day = form.cleaned_data['day']
            time = form.cleaned_data['time']
            size = form.cleaned_data['size']

            # Encode categorical features
            sex_encoded, smoker_encoded, day_encoded, time_encoded = encode_features(
                sex, smoker, day, time
            )

            # Prepare features for prediction
            features = np.array([[total_bill, sex_encoded, smoker_encoded, day_encoded, time_encoded, size]])

            # Load ML model
            model = load_model()
            if model:
                try:
                    prediction = round(model.predict(features)[0], 2)
                    messages.success(request, f'Prediction successful! Expected tip: ${prediction}')
                except Exception as e:
                    messages.error(request, f'❌ Error making prediction: {str(e)}')
            else:
                messages.error(request, '❌ Error: Could not load the ML model.')
    else:
        form = TipPredictionForm()

    return render(request, 'ml_app/predict_tip.html', {'form': form, 'prediction': prediction})

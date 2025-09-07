import os
import joblib

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "xgb_model.pkl")

_model = None  # cache


def get_model():
    global _model
    if _model is None:
        try:
            _model = joblib.load(MODEL_PATH)
            print("✅ Model loaded successfully from:", MODEL_PATH)
        except Exception as e:
            print("❌ Error loading model:", e)
    return _model

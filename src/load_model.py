import os
import joblib

# Absolute path of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Project root folder
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Models folder
MODELS_DIR = os.path.join(PROJECT_DIR, "models")

MODEL_PATH = os.path.join(MODELS_DIR, "trained_model.pkl")
SCALER_PATH = os.path.join(MODELS_DIR, "scaler.pkl")
ENCODER_PATH = os.path.join(MODELS_DIR, "label_encoder.pkl")


def load_models():
    print("Project Directory :", PROJECT_DIR)
    print("Models Directory  :", MODELS_DIR)
    print("Model Path        :", MODEL_PATH)
    print("Scaler Path       :", SCALER_PATH)
    print("Encoder Path      :", ENCODER_PATH)

    print()

    print("Model Exists :", os.path.exists(MODEL_PATH))
    print("Scaler Exists:", os.path.exists(SCALER_PATH))
    print("Encoder Exists:", os.path.exists(ENCODER_PATH))

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    encoder = joblib.load(ENCODER_PATH)

    return model, scaler, encoder
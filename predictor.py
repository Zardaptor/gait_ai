from .load_model import load_models

model, scaler, encoder = load_models()


def predict(sensor_values):

    # sensor_values already contains only the 11 features

    sample = scaler.transform([sensor_values])

    prediction = model.predict(sample)

    confidence = model.predict_proba(sample)

    confidence = confidence.max()

    label = encoder.inverse_transform(prediction)[0]

    return label, confidence
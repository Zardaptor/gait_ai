from .load_model import load_models

model, scaler, encoder = load_models()

print()
print(model)
print(scaler)
print(encoder)
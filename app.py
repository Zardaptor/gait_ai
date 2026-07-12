from src.serial_reader import connect_arduino, read_sensor_data
from src.predictor import predict
from src.context_builder import build_context
from src.prompt_builder import build_prompt
from src.llm_interface import ask_llm
print("Connecting to Arduino...")

arduino = connect_arduino()

print("Connected Successfully!")

while True:

    # Read sensor values
    sensor = read_sensor_data(arduino)
    print("Raw Sensor:", sensor)
    print("Length:", len(sensor))

    # Remove Reading Number
    sensor = sensor[1:]

    # ML Prediction
    prediction, confidence = predict(sensor)

    # Build Context
    context = build_context(
        sensor,
        prediction,
        confidence
    )

    # Build Prompt
    prompt = build_prompt(context)

    # Ask Phi
    response = ask_llm(prompt)

    print("="*70)
    print("Prediction :", prediction)
    print("Confidence:", confidence)
    print()
    print(response)
    print("="*70)
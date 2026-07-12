from fastapi import FastAPI

from src.serial_reader import connect_arduino, read_sensor_data
from src.predictor import predict
from src.context_builder import build_context
from src.prompt_builder import build_prompt
from src.llm_interface import ask_llm

app = FastAPI()

arduino = None


@app.on_event("startup")
def startup():

    global arduino

    arduino = connect_arduino()

    print("Arduino Connected Successfully!")


@app.get("/")
def home():

    return {"status": "Running"}


@app.get("/sensor")
def sensor():

    global arduino

    sensor = read_sensor_data(arduino)

    print("=" * 60)
    print("Raw Sensor:", sensor)
    print("Raw Length:", len(sensor))

    features = sensor[1:]

    print("Features:", features)
    print("Feature Length:", len(features))
    print("=" * 60)

    prediction, confidence = predict(features)

    context = build_context(
        features,
        prediction,
        confidence
    )

    prompt = build_prompt(context)

    ai_response = ask_llm(prompt)

    return {
        "sensor": sensor,
        "prediction": prediction,
        "confidence": float(confidence),
        "analysis": ai_response
    }
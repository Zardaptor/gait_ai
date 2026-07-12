from serial_reader import *
from predictor import *

arduino = connect_arduino()

while True:

    data = read_sensor_data(arduino)

    pattern, confidence = predict(data)

    print("--------------------------------")

    print("Prediction :", pattern)

    print("Confidence :", round(confidence * 100, 2), "%")
import serial
import time

PORT = "COM3"
BAUD_RATE = 9600


def connect_arduino():

    arduino = serial.Serial(PORT, BAUD_RATE, timeout=1)

    time.sleep(2)

    print("Arduino Connected!")

    return arduino


def read_sensor_data(arduino):

    while True:

        line = arduino.readline().decode(errors="ignore").strip()

        if not line:
            continue

        try:

            values = [float(x) for x in line.split(",")]

            print("\nReceived:", values)
            print("Count:", len(values))

            # Expect:
            # ReadingNo + 5 FSR + 3 Acc + 3 Gyro = 12 values

            if len(values) != 12:
                print("Incomplete packet. Waiting for next packet...")
                continue

            return values

        except Exception as e:

            print("Serial Error:", e)
            continue
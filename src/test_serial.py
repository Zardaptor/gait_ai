from .serial_reader import *

arduino = connect_arduino()

while True:

    data = read_sensor_data(arduino)

    print(data)
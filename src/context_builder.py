def build_context(sensor_values, prediction, confidence):

    context = {

        "prediction": prediction,

        "confidence": round(confidence * 100, 2),

        "fsr": {
            "fsr1": sensor_values[0],
            "fsr2": sensor_values[1],
            "fsr3": sensor_values[2],
            "fsr4": sensor_values[3],
            "fsr5": sensor_values[4]
        },

        "accelerometer": {
            "acc_x": sensor_values[5],
            "acc_y": sensor_values[6],
            "acc_z": sensor_values[7]
        },

        "gyroscope": {
            "gyro_x": sensor_values[8],
            "gyro_y": sensor_values[9],
            "gyro_z": sensor_values[10]
        }

    }

    return context
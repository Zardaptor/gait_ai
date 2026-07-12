#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;

// FSR Pins
const int heelPin = A0;
const int archPin = A1;
const int midPin  = A2;
const int forePin = A3;
const int toePin  = A4;

void setup() {

  Serial.begin(115200);
  Wire.begin();

  if (!mpu.begin()) {
    Serial.println("MPU6050 NOT FOUND");
    while (1);
  }

  // Optional: Configure sensor ranges
  mpu.setAccelerometerRange(MPU6050_RANGE_4_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  Serial.println("timestamp,heel,arch,mid,fore,toe,accelX,accelY,accelZ,gyroX,gyroY,gyroZ");
}

void loop() {

  // Read FSRs
  int heel = analogRead(heelPin);
  int arch = analogRead(archPin);
  int mid  = analogRead(midPin);
  int fore = analogRead(forePin);
  int toe  = analogRead(toePin);

  // Read MPU6050
  sensors_event_t accel, gyro, temp;
  mpu.getEvent(&accel, &gyro, &temp);

  // Print CSV
  Serial.print(millis());
  Serial.print(",");

  Serial.print(heel);
  Serial.print(",");

  Serial.print(arch);
  Serial.print(",");

  Serial.print(mid);
  Serial.print(",");

  Serial.print(fore);
  Serial.print(",");

  Serial.print(toe);
  Serial.print(",");

  // Accelerometer (m/s²)
  Serial.print(accel.acceleration.x, 2);
  Serial.print(",");

  Serial.print(accel.acceleration.y, 2);
  Serial.print(",");

  Serial.print(accel.acceleration.z, 2);
  Serial.print(",");

  // Gyroscope (rad/s)
  Serial.print(gyro.gyro.x, 2);
  Serial.print(",");

  Serial.print(gyro.gyro.y, 2);
  Serial.print(",");

  Serial.println(gyro.gyro.z, 2);

  delay(20);   // 50 Hz sampling
}

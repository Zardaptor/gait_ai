# GaitAI: Multi-Device Edge AI Mobility Assistant

<p align="center">
  <img src="docs/architecture.png" width="900"/>
</p>

---

## Overview

GaitAI is a distributed **Edge AI healthcare platform** designed for **real-time gait analysis, plantar pressure mapping, gait abnormality detection, and fall-risk prediction**.

The system combines wearable sensing, embedded computing, Edge AI, mobile interaction, and cloud intelligence into a unified healthcare solution capable of monitoring walking patterns with low latency and high privacy.

Unlike conventional cloud-dependent healthcare systems, GaitAI performs the majority of computation locally on a **Snapdragon AI PC**, enabling real-time inference while minimizing internet dependency.

The platform is designed for applications including:

- Elderly fall prevention
- Rehabilitation monitoring
- Post-operative recovery
- Parkinson's disease assessment
- Sports biomechanics
- Industrial worker safety

---

# Problem Statement

Falls and gait disorders are among the leading causes of injury for elderly individuals, rehabilitation patients, and industrial workers. Traditional gait analysis systems often depend on expensive laboratory equipment or cloud-based processing, introducing latency, privacy concerns, and unreliable operation in environments without continuous internet connectivity.

GaitAI addresses these challenges through an Edge AI architecture that performs sensing, machine learning inference, and clinical reasoning locally while providing real-time feedback through an intuitive mobile application.

---

# Key Features

- Real-time plantar pressure sensing
- IMU-based motion tracking
- Live gait visualization
- Step detection
- Cadence estimation
- Gait classification
- Fall-risk prediction
- Edge AI inference
- REST API backend
- Android mobile application
- Offline-first architecture
- Cloud synchronization (optional)

---

# System Architecture

```
Wearable Sensor Node
        │
        ▼
Arduino UNO Q
        │
USB Serial Communication
        │
        ▼
Python Backend
        │
Feature Extraction
        │
Machine Learning Inference
        │
Phi-4 Mini Reasoning
        │
FastAPI REST Server
        │
 ┌───────
 │              
 ▼            

Flutter App 
```

---

# Hardware Architecture

## Wearable Sensor Node

The wearable sensing module continuously captures biomechanical information during walking.

### Sensors Used

- 5 × Force Sensitive Resistors (FSRs)
  - Heel
  - Arch
  - Midfoot
  - Forefoot
  - Toe

- MPU6050
  - 3-axis Accelerometer
  - 3-axis Gyroscope

These sensors provide pressure distribution and foot orientation data in real time.

---

## Embedded Data Acquisition

The Arduino UNO Q acts as the embedded acquisition node responsible for:

- Reading all FSR sensors
- Reading IMU data
- Timestamping sensor samples
- Serial communication
- Real-time streaming to the host computer

---

# Data Acquisition Pipeline

```
Pressure Sensors
        │
Voltage Divider
        │
ADC Sampling
        │
Filtering
        │
Pressure Values

MPU6050
        │
Acceleration
Gyroscope
        │
Pitch
Roll
```

Sensor data is streamed continuously through USB Serial to the Edge AI backend.

---

# Software Stack

| Layer | Technology |
|--------|------------|
| Firmware | Arduino |
| Backend | Python |
| API | FastAPI |
| Mobile | Flutter |
| Machine Learning | Scikit-Learn |
| Edge Runtime | Snapdragon AI PC |
| LLM | Phi-4 Mini |
| Cloud | Qualcomm AI Hub |

---

# AI Pipeline

The machine learning pipeline converts raw sensor readings into meaningful gait information.

```
Sensor Data
      │
Filtering
      │
Feature Extraction
      │
Machine Learning Model
      │
Gait Classification
      │
Fall Risk Prediction
      │
Clinical Reasoning
```

---

## Feature Extraction

The backend computes multiple biomechanical features including:

### Pressure Features

- Heel Pressure
- Arch Pressure
- Midfoot Pressure
- Forefoot Pressure
- Toe Pressure
- Average Pressure
- Peak Pressure
- Pressure Distribution
- Center of Pressure

### Motion Features

- Pitch
- Roll
- Acceleration Magnitude
- Angular Velocity

### Temporal Features

- Cadence
- Step Interval
- Stance Time
- Swing Time

These features are combined into a numerical feature vector for machine learning inference.

---

# Machine Learning

The extracted features are processed using lightweight machine learning models optimized for edge deployment.

Example gait classes include:

- Normal Walking
- Slow Walking
- Fast Walking
- Limping
- Abnormal Gait

The predicted gait pattern is used to estimate the user's fall risk.

---

# LLM Clinical Reasoning

After machine learning inference, predictions are passed to **Phi-4 Mini** running locally.

Instead of simply displaying:

```
High Risk
```

the LLM generates natural-language explanations such as:

> Increased forefoot loading and reduced cadence indicate possible fatigue or gait instability. Consider slowing your walking pace and consulting a clinician if symptoms persist.

This improves interpretability and user engagement.

---

# FastAPI Backend

The backend exposes REST endpoints for real-time communication.

Example endpoints:

```
GET /live
Returns live sensor values

GET /prediction
Returns gait prediction

GET /history
Returns previous sessions

POST /upload
Uploads walking session

GET /status
Returns hardware status
```

---




# Mobile Application

The Flutter-based Android application provides:

- Live sensor monitoring
- Pressure visualization
- AI predictions
- Fall-risk alerts
- Rehabilitation recommendations
- Historical walking sessions
- Emergency notifications

The application communicates with the backend using REST APIs.

---

# Edge AI Design

GaitAI follows an **Edge-First** architecture.

The following components execute locally on the Snapdragon AI PC:

- Sensor preprocessing
- Feature extraction
- Machine learning inference
- LLM reasoning
- Dashboard rendering
- REST API

Cloud services are optional and used only for:

- Historical analytics
- Model synchronization
- Backup
- Long-term reporting

This architecture minimizes latency while preserving user privacy.

---

# Repository Structure

```
GaitAI/
│
├── hardware/
│   ├── Arduino Firmware
│   ├── Circuit Diagrams
│
├── backend/
│   ├── Serial Reader
│   ├── FastAPI Backend
│
├── ai/
│   ├── Model Training
│   ├── Feature Extraction
│   ├── Inference
│
│
├── mobile/
│   ├── Flutter Application

│
├── docs/
│   ├── Architecture
│   ├── Screenshots
│
├── tests/
│
├── sample_data/
│
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/GaitAI.git
cd GaitAI
```

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Upload Arduino Firmware

Open the Arduino firmware inside the `hardware` folder and upload it to the Arduino UNO Q.

## Start Backend

```bash
python backend/app.py
```


## Launch Flutter Application

```bash
cd mobile

flutter pub get

flutter run
```

---

# Future Improvements

- TinyML deployment directly on embedded hardware
- Bluetooth Low Energy wearable communication
- Personalized AI models
- Multi-patient monitoring
- Smart shoe PCB
- Integration with wearable smartwatches
- Qualcomm Hexagon NPU optimization
- Hospital dashboard integration

---

# Team

| Name | Role |
|------|------|
| Suraj Kalyanaraman | Embedded Systems, Hardware Integration, Firmware Development |
| Pavesh Kamalan | Machine Learning Pipeline,  Software Developer |
| Vimal | Flutter Mobile Application |
| Vivin| Streamlit Dashboard & Backend |
| Arun S M| Embedded Coding|

---

# License

This project is licensed under the MIT License.

---

# Acknowledgements

This project was developed as part of the **Qualcomm Snapdragon Multiverse Hackathon**.

We acknowledge the use of the following open-source technologies:

- Arduino
- Flutter
- Streamlit
- FastAPI
- Scikit-Learn
- NumPy
- Pandas
- Qualcomm AI Hub
- Microsoft Phi-4 Mini
- PhysioNet

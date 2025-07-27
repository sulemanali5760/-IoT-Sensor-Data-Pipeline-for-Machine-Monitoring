# IoT-Sensor-Data-Pipeline-for-Machine-Monitoring

![Header Banner](./assets/header_banner.png)

## Overview

This project demonstrates a complete pipeline for real-time monitoring of machine conditions (temperature & humidity) using IoT sensors. Sensor data is collected via MQTT, stored in a local SQLite database, and visualized in Python using Matplotlib.

- **Tech Stack:** Python, MQTT (paho-mqtt), SQLite, Matplotlib, Arduino/ESP32 (for hardware simulation)
- **Main Features:**
  - Real-time data collection
  - Data persistence in SQLite
  - Trend visualization and anomaly detection
  - Modular, easily extensible design

---

## Architecture

```mermaid
graph TD
    Sensor(DHT22 Sensor + ESP32/Arduino) -->|MQTT| Broker((MQTT Broker))
    Broker -->|MQTT| PythonCollector[Python Data Collector]
    PythonCollector -->|SQLite| Database[(SQLite DB)]
    Database -->|Pandas/Matplotlib| Visualization[Data Visualization]

import paho.mqtt.client as mqtt
import sqlite3
import json
from datetime import datetime

# Database setup
conn = sqlite3.connect('sensordata.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sensor_readings
             (timestamp TEXT, temperature REAL, humidity REAL)''')
conn.commit()

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("factory/sensor1")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Received:", data)
    timestamp = datetime.now().isoformat()
    c.execute("INSERT INTO sensor_readings VALUES (?, ?, ?)",
              (timestamp, data['temperature'], data['humidity']))
    conn.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.loop_start()

# Run for a certain time (or use try/except for manual stop)
import time
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    conn.close()

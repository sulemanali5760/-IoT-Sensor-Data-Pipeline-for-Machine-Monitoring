import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

conn = sqlite3.connect('sensordata.db')
df = pd.read_sql_query("SELECT * FROM sensor_readings", conn, parse_dates=['timestamp'])

plt.figure(figsize=(10,4))
plt.plot(pd.to_datetime(df['timestamp']), df['temperature'], label='Temperature (°C)')
plt.plot(pd.to_datetime(df['timestamp']), df['humidity'], label='Humidity (%)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.title('Machine Temperature & Humidity Over Time')
plt.tight_layout()
plt.show()

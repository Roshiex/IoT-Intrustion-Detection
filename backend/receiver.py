import json
import csv
import os
from datetime import datetime
import paho.mqtt.client as mqtt

LOG_FILE = "data/logs.csv"

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        pass


def log_data(data):
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), data["temperature"], data["motion"]])


def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    print("\nReceived:", data)

    log_data(data)

    if data["motion"]:
        print("Motion detected")


client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("iot/intrusion")

print("Backend running...")

client.loop_forever()

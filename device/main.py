import time
import random
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

print("Device running...")

while True:
    data = {
        "temperature": round(random.uniform(18, 30), 1),
        "motion": random.choice([True, False]),
    }

    payload = json.dumps(data)
    client.publish("iot/intrusion", payload)

    print("Sent:", payload)

    time.sleep(3)

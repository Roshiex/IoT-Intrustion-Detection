import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_FILE = os.path.join(BASE_DIR, "data", "logs.csv")

print("\n--- IoT LOGS ---")

with open(LOG_FILE, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

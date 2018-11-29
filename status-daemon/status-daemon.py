import time

import Adafruit_DHT
from core.sheetUploader import GoogleUploader

OAUTH_JSON = 'tempAndHumidity-b4174e738444.json'
GOOGLE_SHEET = "tempsAndHumidity"
INTERVAL = 3
pin = 4

up = GoogleUploader(OAUTH_JSON, GOOGLE_SHEET)
try:
    sensor = Adafruit_DHT.DHT11
except Exception as e:
    print('Failed to init senzor {}'.format(e))


while True:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        t = time.time()

        data = list()
        data.append(t)
        data.append(temperature)
        data.append(humidity)

        if humidity is not None and temperature is not None:
            up.appendToSheet(data)

        time.sleep(INTERVAL)

    except Exception as e:
        print('Failed to read sensor data {}'.format(e))



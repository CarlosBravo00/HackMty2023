from grove_rgb_lcd import *
import time
import grovepi
from grovepi import *
import math
import statistics
import Adafruit_DHT
import requests
import json


import random

temp_sensor = 0
light_sensor = 1
led = 3
water_sensor = 2

WARNING_LIGHT = 190
WARNING_WATER = 700
WARNING_TEMP = 16

URL = "https://cvvajx5zq0.execute-api.us-west-2.amazonaws.com/logs"

MAX_LIGHT = 750
MIN_LIGHT = 0

MAX_WATER = 300
MIN_WATER = 1023

LOG_INTERVAL = 30  # SEGUNDOS


def getPercentage(minValue, maxValue, value):
    res = (minValue - value)/(minValue - maxValue)
    return str(min(100, round(res*100))) + '%'


def LEDControl(tempValue, lightValue, waterValue):
    if lightValue < WARNING_LIGHT or tempValue < WARNING_TEMP or waterValue > WARNING_WATER:
        grovepi.digitalWrite(led, 1)
    else:
        grovepi.digitalWrite(led, 0)


counter = 0
temp_arr = []
light_arr = []
water_arr = []

while True:
    try:

        setRGB(0, 255, 0)
        temp_value = grovepi.temp(temp_sensor, '1.1')
        light_value = grovepi.analogRead(light_sensor)
        water_value = grovepi.analogRead(water_sensor)

        setText("T: " + str(round(temp_value, 2)) + "C\nL: " +
                getPercentage(MIN_LIGHT, MAX_LIGHT, light_value) + "  W: "
                + getPercentage(MIN_WATER, MAX_WATER, water_value))

        LEDControl(temp_value, light_value, water_value)
        time.sleep(1)
        counter = counter+1

        temp_arr.append(temp_value)
        light_arr.append(light_value)
        water_arr.append(water_value)

        if counter == LOG_INTERVAL:
            data = {'light': round(statistics.median(light_arr), 2),
                    'water': round(statistics.median(water_arr), 2),
                    'temperature': round(statistics.median(temp_arr), 2)}
            Headers = {'Content-Type': 'application/json'}
            r = requests.post(url=URL, data=json.dumps(data), headers=Headers)
            print(r.json())
            counter = 0
            temp_arr = []
            light_arr = []
            water_arr = []
    except KeyboardInterrupt:
        setText("KeyboardInterrupt")
        setRGB(255, 0, 0)
        break
    except IOError:
        setText("Error")
        setRGB(255, 0, 0)
        break

time.sleep(5)
setText("All done")
setRGB(0, 255, 0)
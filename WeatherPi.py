#!/usr/bin/python
import time
from sense_hat import SenseHat
import json, requests, sys

APIkey="" #Enter your API Key from OpenWeatherMap
CityID="" #Enter your city's ID from OpenWeatherMap

sense = SenseHat()
sense.clear()

sense.low_light = True
sense.set_rotation(180)

def getData():
    url ='http://api.openweathermap.org/data/2.5/weather?id=%s&units=metric&appid=%s' % (CityID,APIkey)
    # Download the JSON data from OpenWeatherMap.org's API.
    response = requests.get(url)
    response.raise_for_status()
    # Load JSON data into a Python variable.
    global weatherData
    weatherData = json.loads(response.text)

def thermometer(temp):
    temp=(int(temp))
    if temp >= 1 and temp <= 8:
        color=[110,240,240] #Light Blue
        tmax = 9
    elif temp >= 9 and temp <= 16:
        color=[0,90,255] #Blue
        tmax = 17
    elif temp >= 17 and temp <= 24:
        color=[120,220,0] #Green
        tmax = 25
    elif temp >= 25 and temp <= 32:
        color=[255,140,0] #Orange
        tmax = 25
    elif temp >= 33:
        color=[233,33,33] #Red
        tmax = 40
    else:
        color=[0,0,0] #White
        tmax = 0
    temp = temp - (tmax - 8)
    for y in range(0, temp+1):
        sense.set_pixel(7, 7-y, color)
    for y in range(temp+1, 7):
        sense.set_pixel(7, 7-y, 0, 0, 0)

while True:
    # Download the JSON data from OpenWeatherMap.org's API.
    getData()
    
    print('Current weather in %s:' % (weatherData['name']))
    print(weatherData['weather'][0]['main'])
    print(weatherData['main']['temp'])
    print(weatherData['main']['pressure'])
    print(weatherData['main']['humidity'])
    
    sense.load_image("icon/"+weatherData['weather'][0]['icon']+".png")
    thermometer(weatherData['main']['temp'])
    
    time.sleep(180)
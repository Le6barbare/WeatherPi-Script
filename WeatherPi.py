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

while True:
    url ='http://api.openweathermap.org/data/2.5/weather?id=%s&units=metric&appid=%s' % (CityID,APIkey)
    # Download the JSON data from OpenWeatherMap.org's API.
    response = requests.get(url)
    response.raise_for_status()

    # Load JSON data into a Python variable.
    weatherData = json.loads(response.text)

    print('Current weather in %s:' % (weatherData['name']))
    print(weatherData['weather'][0]['main'])
    print(weatherData['main']['temp'])
    print(weatherData['main']['pressure'])
    print(weatherData['main']['humidity'])

    sense.load_image("icon/"+weatherData['weather'][0]['icon']+".png")
    
    time.sleep(180)
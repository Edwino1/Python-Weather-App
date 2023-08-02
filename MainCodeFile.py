from tkinter import *
import requests
import json
from datetime import datetime

mainWindow = Tk()
mainWindow.title("Weather App")
mainWindow.geometry("600x500")
mainWindow.config(background="#0377fc")
mainLabel = Label(mainWindow, text="Weather App",
      font=("Times New Roman", 20, "bold"),
      fg="black",
      bg="White",
      relief=RAISED,
      bd=10).pack()

cityValue = StringVar()

def timeFormat(utc_with_tz):
    localTime = datetime.utcfromtimestamp(utc_with_tz)
    return localTime.time()

def obtainWeatherCelsius():
    apiKey = "a2e25a18393abe073c9aba8eb17be128"
    cityName = cityValue.get()
    weatherURL = "http://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid=" + apiKey
    response = requests.get(weatherURL)
    weatherInfo = response.json()
    textfield.delete("1.0","end")

    if weatherInfo["cod"] == 200:
        kelvin = 273
        temp = int(weatherInfo['main']['temp'] - kelvin)
        feelsLikeTemp = int(weatherInfo['main']['feels_like'] - kelvin)
        pressure = weatherInfo['main']['pressure']
        humidity = weatherInfo['main']['humidity']
        windSpeed = weatherInfo['wind']['speed'] * 3.6
        sunrise = weatherInfo['sys']['sunrise']
        sunset = weatherInfo['sys']['sunset']
        timezone = weatherInfo['timezone']
        cloudy = weatherInfo['clouds']['all']
        description = weatherInfo['weather'][0]['description']
        sunriseTime = timeFormat(sunrise + timezone)
        sunsetTime = timeFormat(sunset + timezone)
        weather = (f"Weather of {cityName.capitalize()}\nTemperature (Celsius): {temp} degrees\nFeels like {feelsLikeTemp} degrees\nPressure: {pressure}hPa\nHumidity {humidity}%\nSunrise at {sunriseTime}\nSunset at {sunsetTime}\nCloud: {cloudy}%\nInfo: {description}")
    else:
        weather = (f"Weather for '{cityName}' not found!")

    textfield.insert(INSERT, weather)

def obtainWeatherFahrenheit():
    apiKey = "a2e25a18393abe073c9aba8eb17be128"
    cityName = cityValue.get()
    weatherURL = "http://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid=" + apiKey
    response = requests.get(weatherURL)
    weatherInfo = response.json()
    textfield.delete("1.0","end")

    if weatherInfo["cod"] == 200:
        kelvin = 273
        temp = int((weatherInfo['main']['temp'] - kelvin) * (9/5) + 32)
        feelsLikeTemp = int((weatherInfo['main']['feels_like'] - kelvin) * (9/5) + 32)
        pressure = weatherInfo['main']['pressure']
        humidity = weatherInfo['main']['humidity']
        windSpeed = weatherInfo['wind']['speed'] * 3.6
        sunrise = weatherInfo['sys']['sunrise']
        sunset = weatherInfo['sys']['sunset']
        timezone = weatherInfo['timezone']
        cloudy = weatherInfo['clouds']['all']
        description = weatherInfo['weather'][0]['description']
        sunriseTime = timeFormat(sunrise + timezone)
        sunsetTime = timeFormat(sunset + timezone)
        weather = (f"Weather of {cityName.capitalize()}\nTemperature (Fahrenheit): {temp} degrees\nFeels like {feelsLikeTemp} degrees\nPressure: {pressure}hPa\nHumidity {humidity}%\nSunrise at {sunriseTime}\nSunset at {sunsetTime}\nCloud: {cloudy}%\nInfo: {description}")
    else:
        weather = (f"Weather for '{cityName}' not found!")

    textfield.insert(INSERT, weather)

cityLabel =Label(mainWindow,text="Enter City Name",
                     font=("Times New Roman", 20, "bold"),
                     fg="black",
                     bg="White",
                     relief=RAISED,
                     bd=10
                     ).pack(pady="10")
cityInput = Entry(mainWindow, textvariable=cityValue,
                  font=20).pack()
celsius = Button(mainWindow, command=obtainWeatherCelsius,
                   text = "Celsius",
                   font=("Times New Roman", 20,"bold"),
                   relief=RAISED,
                   activebackground="green"
                   ).pack(pady="10")
fahrenheit = Button(mainWindow, command=obtainWeatherFahrenheit,
                   text = "Fahrenheit",
                   font=("Times New Roman", 20,"bold"),
                   relief=RAISED,
                   activebackground="green"
                   ).pack()
textfield = Text(mainWindow, width=46, height=9,
                 font=(40))
textfield.pack(pady="10")

mainWindow.mainloop()
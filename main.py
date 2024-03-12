import datetime as dt
import requests , json
BASE_URL = "http://api.weatherapi.com/v1/"
API_KEY = open("api_key","r").read()
CITY = input("Enter city: ")
url = BASE_URL + "current.json?key=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

country = response["location"]["country"]
localtime = response["location"]["localtime"] 
condition = response["current"]["condition"]["text"]
temp = response["current"]["temp_c"]
wind_mph = response["current"]["wind_mph"]
print(f"City: {CITY}")
print(f"Country: {country}")
print(f"local time: {localtime}")
print(condition)
print(f"temp: {temp}°C")
print(f"wind: {wind_mph} mph")

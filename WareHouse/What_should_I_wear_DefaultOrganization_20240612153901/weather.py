'''
Module for weather-related functionality.
'''
import requests
import datetime
from config import API_KEY
class WeatherAPI:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = "https://api.weather.com"
    def get_weather(self, location):
        url = f"{self.base_url}/data/2.5/weather?q={location}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            temperature = weather_data["main"]["temp"]
            return {"temperature": temperature}
        else:
            return None
    def compare_temperature(self, temperature, location):
        yesterday_temperature = self.get_yesterday_temperature(location)
        if yesterday_temperature is not None:
            temperature_difference = temperature - yesterday_temperature
            if temperature_difference > 0:
                return "It's hotter today. Wear light clothes."
            elif temperature_difference < 0:
                return "It's cooler today. Wear a jacket."
            else:
                return "The temperature is similar to yesterday. Dress accordingly."
        else:
            return "Unable to compare with yesterday's temperature."
    def get_yesterday_temperature(self, location):
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        url = f"{self.base_url}/data/2.5/onecall/timemachine?lat={latitude}&lon={longitude}&dt={yesterday}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            temperature = weather_data["current"]["temp"]
            return temperature
        else:
            return None
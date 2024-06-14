'''
Main module for the Weather Outfit Suggestion website.
'''
import tkinter as tk
from weather import WeatherAPI
class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather Outfit Suggestion")
        self.geometry("400x200")
        self.weather_api = WeatherAPI()
        self.label = tk.Label(self, text="Enter your location:")
        self.label.pack()
        self.location_entry = tk.Entry(self)
        self.location_entry.pack()
        self.button = tk.Button(self, text="Get Weather", command=self.get_weather)
        self.button.pack()
        self.outfit_label = tk.Label(self, text="")
        self.outfit_label.pack()
    def get_weather(self):
        location = self.location_entry.get()
        weather_data = self.weather_api.get_weather(location)
        if weather_data:
            temperature = weather_data["temperature"]
            outfit_suggestion = self.weather_api.compare_temperature(temperature, location)
            self.outfit_label.config(text=outfit_suggestion)
        else:
            self.outfit_label.config(text="Failed to retrieve weather data.")
if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
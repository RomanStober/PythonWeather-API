import tkinter as tk
import requests

# getting the weather data 
def get_weather():
    city = city_var.get()
    if city:
        api_key = "KcGEVzTNeBfRb6gj8CfqOmz6QKaRLEjN"
        base_url = f"https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&access_key={api_key}&query={city}"
        response = requests.get(base_url)
        data = response.json()
        if data.get("current"):
            Temperature = data["current"]["temperature"]
            description = data["current"]["weather_descriptions"][0]
            weather_info = f"Weather in {city.capitalize()}:\nTemperature: {Temperature}\nDescription: {description.capitalize()}"
            weather_label.config(text=weather_info)
        else:
            weather_label.config(text="City not found")
    else:
        weather_label.config(text="Enter a city")

root = tk.Tk()
root.title("weather finder")
root.geometry("400x250")

title_label = tk.Label(
    root,
    text="weather App",
    font=("Helvetica", 20))
title_label.pack()

city_label = tk.Label(
    root,
    text="enter a city",
    font=("Helvetica", 16))
city_label.pack()

city_var = tk.StringVar()
city_entry = tk.Entry(
    root,
    textvariable=city_var,
    font=("Helvetica", 16))
city_entry.pack()

search_button = tk.Button(
    root,
    text="Search area",
    command=get_weather,
    font=("Helvetica", 16))
search_button.pack()

weather_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 16))
weather_label.pack()

root.mainloop()




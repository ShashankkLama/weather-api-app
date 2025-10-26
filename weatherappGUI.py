import tkinter as tk
from tkinter import messagebox
import requests

# --- Fetch weather data ---
def get_weather():
    city = city_entry.get().strip()
    api_key = api_key_entry.get().strip()
    
    if not city or not api_key:
        messagebox.showwarning("Input Error", "Please enter both city name and API key.")
        return
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        city_name = data["name"]
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result_label.config(
            text=f"🌍 City: {city_name}\n"
                 f"🌡 Temperature: {temp}°C\n"
                 f"☁ Condition: {condition}\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"💨 Wind Speed: {wind_speed} m/s"
        )

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found or invalid API key.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# --- GUI Setup ---
root = tk.Tk()
root.title("🌦 Weather App")
root.geometry("350x350")
root.config(bg="#E0F7FA")

title_label = tk.Label(root, text="Simple Weather App", font=("Helvetica", 16, "bold"), bg="#E0F7FA")
title_label.pack(pady=10)

api_key_label = tk.Label(root, text="Enter API Key:", bg="#E0F7FA")
api_key_label.pack()
api_key_entry = tk.Entry(root, width=35, show="*")
api_key_entry.pack(pady=5)

city_label = tk.Label(root, text="Enter City Name:", bg="#E0F7FA")
city_label.pack()
city_entry = tk.Entry(root, width=35)
city_entry.pack(pady=5)

search_btn = tk.Button(root, text="Get Weather", command=get_weather, bg="#0288D1", fg="white", font=("Arial", 10, "bold"))
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", bg="#E0F7FA", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()
